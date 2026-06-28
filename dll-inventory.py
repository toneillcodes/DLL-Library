import os
import csv
import hashlib
import concurrent.futures
import threading
from pathlib import Path
import pefile

# Thread-safe lock for writing to the CSV file
csv_write_lock = threading.Lock()

def calculate_sha256(file_path):
    """Calculates the SHA256 hash of a file efficiently by chunking."""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except (PermissionError, FileNotFoundError):
        return None

def get_unwind_sizes(pe):
    """
    Parses the x64 exception directory (.pdata) to map function RVAs to sizes.
    Returns a dict of {start_rva: size}
    """
    unwind_sizes = {}
    if not hasattr(pe, 'DIRECTORY_ENTRY_EXCEPTION'):
        return unwind_sizes

    for entry in pe.DIRECTORY_ENTRY_EXCEPTION:
        try:
            # RUNTIME_FUNCTION entry attributes
            begin_rva = entry.struct.BeginAddress
            end_rva = entry.struct.EndAddress
            size = end_rva - begin_rva
            unwind_sizes[begin_rva] = size
        except AttributeError:
            continue
    return unwind_sizes

def process_dll(file_path, csv_writer):
    """Parses a single DLL, extracts exports, sizes them, and logs to CSV."""
    try:
        sha256 = calculate_sha256(file_path)
        if not sha256:
            return  # Skip if we couldn't read the file for hashing

        pe = pefile.PE(file_path, fast_load=True)
        pe.parse_data_directories(directories=[
            pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_EXPORT'],
            pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_EXCEPTION']
        ])

        # Determine architecture
        arch = "x64" if pe.FILE_HEADER.Machine == pefile.MACHINE_TYPE['IMAGE_FILE_MACHINE_AMD64'] else "x86"

        if not hasattr(pe, 'DIRECTORY_ENTRY_EXPORT'):
            pe.close()
            return  # No exports to process

        # Parse unwind data maps if available (x64)
        unwind_map = get_unwind_sizes(pe) if arch == "x64" else {}

        # First pass: gather all valid, non-forwarded exports to sort for fallback calculations
        valid_exports = []
        for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
            # If it's a forwarded export, RVA points to a string name in the export section, not code
            is_forwarded = exp.forwarder is not None
            rva = exp.address if not is_forwarded else 0
            
            valid_exports.append({
                'exp_obj': exp,
                'name': exp.name.decode('utf-8', errors='ignore') if exp.name else None,
                'ordinal': exp.ordinal,
                'rva': rva,
                'is_forwarded': is_forwarded,
                'forwarder_str': exp.forwarder.decode('utf-8', errors='ignore') if is_forwarded else None
            })

        # Sort exports by RVA for contiguous calculation fallbacks
        # Forwarded exports end up at the front (RVA 0), we will filter or handle them
        valid_exports.sort(key=lambda x: x['rva'])

        # Get the size of the text section as a boundary fallback for the final export
        text_section_size = 0
        for section in pe.sections:
            if b'.text' in section.Name:
                text_section_size = section.Misc_VirtualSize
                break

        rows_to_write = []

        for idx, exp in enumerate(valid_exports):
            name = exp['name']
            ordinal = exp['ordinal']
            rva = exp['rva']
            
            if exp['is_forwarded']:
                rows_to_write.append([
                    sha256, file_path, arch, name, ordinal, f"0x{rva:X}", 0, "Forwarded", exp['forwarder_str']
                ])
                continue

            # Sizing Strategy Selection
            size = 0
            method = "Unknown"

            # 1. Attempt Unwind Data mapping (.pdata)
            if rva in unwind_map:
                size = unwind_map[rva]
                method = "UnwindData"
            # 2. Fallback to contiguous RVA delta calculations
            else:
                # Find the next export that has a higher RVA
                next_rva = None
                for nxt in valid_exports[idx + 1:]:
                    if nxt['rva'] > rva:
                        next_rva = nxt['rva']
                        break
                
                if next_rva:
                    size = next_rva - rva
                    method = "ContiguousDelta"
                elif text_section_size and rva < text_section_size:
                    # Last export fallback: bound by the estimated remaining space in text section
                    size = text_section_size - rva
                    method = "SectionBoundedDelta"
                else:
                    size = 0
                    method = "Indeterminate"

            rows_to_write.append([
                sha256, file_path, arch, name, ordinal, f"0x{rva:X}", size, method, ""
            ])

        pe.close()

        # Thread-safe write to CSV
        with csv_write_lock:
            for row in rows_to_write:
                csv_writer.writerow(row)

    except pefile.PEFormatError:
        pass  # Gracefully skip if file is corrupted or not an actual PE
    except Exception as e:
        # Catch-all for transient locking issues or specific edge-case I/O errors
        pass

def crawl_and_inventory(target_directory, output_csv_path, max_threads=16):
    """Crawls the target directory and manages the thread pool worker execution."""
    headers = [
        "SHA256", "FilePath", "Architecture", "ExportName", 
        "Ordinal", "RVA", "FunctionSize", "SizeCalculationMethod", "ForwardedURL"
    ]

    print(f"[*] Initializing scan on target directory: {target_directory}")
    print(f"[*] Results will be saved to: {output_csv_path}")

    with open(output_csv_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)

        # Build execution pool
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
            futures = []
            
            # Recurse directory structure safely
            for root, _, files in os.walk(target_directory):
                for file in files:
                    if file.lower().endswith('.dll'):
                        full_path = os.path.join(root, file)
                        futures.append(executor.submit(process_dll, full_path, writer))

            # Monitor progress slightly
            total_files = len(futures)
            print(f"[*] Scheduled {total_files} DLL files for analysis. Processing...")
            
            completed = 0
            for future in concurrent.futures.as_completed(futures):
                completed += 1
                if completed % 100 == 0 or completed == total_files:
                    print(f"    Progress: {completed}/{total_files} files evaluated.", end="\r")
                    
    print("\n[+] Inventory process completed successfully.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python dll_inventory.py <target_directory> <output_csv_path>")
        sys.exit(1)

    target_dir = sys.argv[1]
    output_csv = sys.argv[2]
    
    crawl_and_inventory(target_dir, output_csv)