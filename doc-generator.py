import os
import csv
import sys
from collections import defaultdict
from pathlib import Path

def sanitize_filename(name):
    """Removes or replaces characters that are illegal in file systems."""
    return "".join(c for c in name if c.isalnum() or c in (' ', '_', '-', '.')).rstrip()

def get_relative_mirror_path(absolute_dll_path):
    """
    Converts an absolute file path into a clean relative directory path 
    by removing drive letters or root symbols, preserving the tree structure.
    """
    path_obj = Path(absolute_dll_path)
    parts = path_obj.parent.parts
    
    # Strip Windows drive letter (e.g., 'C:') or Unix root '/' if present
    if path_obj.drive:
        parts = parts[1:]
    elif parts and parts[0] == '/':
        parts = parts[1:]
        
    return Path(*parts)

def generate_markdown_docs(csv_path, output_dir):
    """Reads the inventory CSV and builds a mirrored directory tree of documentation."""
    print(f"[*] Checking CSV path: {csv_path}")
    
    if not os.path.exists(csv_path):
        print(f"[-] Error: Target CSV file '{csv_path}' does not actually exist on disk.")
        return

    print(f"[+] CSV file found. Opening and parsing...")
    
    # Structure: absolute_dll_dir_str -> dll_name -> list of export rows
    tree_registry = defaultdict(lambda: defaultdict(list))
    
    # Parse and group data by directory structure
    with open(csv_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        
        print(f"[*] Detected CSV Headers: {reader.fieldnames}")
        if not reader.fieldnames:
            print("[-] Error: CSV file appears to have no headers or is corrupted.")
            return
            
        row_count = 0
        for row in reader:
            row_count += 1
            try:
                dll_path = Path(row['FilePath'])
                dll_dir = str(dll_path.parent)
                dll_name = dll_path.name
                tree_registry[dll_dir][dll_name].append(row)
            except KeyError as e:
                print(f"[-] Missing expected column in CSV: {e}")
                print("[*] Please verify your CSV has standard 'FilePath', 'SHA256', etc. columns.")
                return

        print(f"[+] Successfully parsed {row_count} total rows from CSV.")

    print(f"[*] Distinct directories identified: {len(tree_registry)}")
    if not tree_registry:
        print("[-] Error: Tree registry is completely empty. No data to process.")
        return

    base_output_path = Path(output_dir)
    base_output_path.mkdir(parents=True, exist_ok=True)
    
    print(f"[*] Generating mirrored documentation structure inside: {output_dir}")
    
    # Track directories that need local READMEs generated
    dir_manifests = defaultdict(list)

    # 1. Generate all individual DLL specification files
    for abs_dir_str, dlls in tree_registry.items():
        # Compute where this fits in our mirrored output folder
        sample_row = next(iter(dlls.values()))[0]
        rel_mirror_dir = get_relative_mirror_path(sample_row['FilePath'])
        target_write_dir = base_output_path / rel_mirror_dir
        target_write_dir.mkdir(parents=True, exist_ok=True)

        for dll_name, exports in dlls.items():
            sample = exports[0]
            sha256 = sample['SHA256']
            arch = sample['Architecture']
            
            doc_filename = f"{sanitize_filename(dll_name)}_{sha256[:8]}.md"
            doc_file_path = target_write_dir / doc_filename
            
            # Log this file to its directory container for the sub-README
            dir_manifests[rel_mirror_dir].append({
                'name': dll_name,
                'arch': arch,
                'sha256': sha256,
                'export_count': len(exports),
                'doc_file': doc_filename
            })

            # Write the DLL specific markdown specification
            with open(doc_file_path, mode="w", encoding="utf-8") as md:
                md.write(f"# Binary Specification: {dll_name}\n\n")
                md.write("## Binary Metadata\n")
                md.write(f"* **Original Path:** `{sample['FilePath']}`\n")
                md.write(f"* **Architecture:** {arch}\n")
                md.write(f"* **SHA256 Fingerprint:** `{sha256}`\n")
                md.write(f"* **Total Exported Functions:** {len(exports)}\n\n")
                
                md.write("## Exported Interface Map\n")
                md.write("| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |\n")
                md.write("| :---: | :--- | :---: | :---: | :---: | :--- |\n")
                
                for exp in exports:
                    name = f"`{exp['ExportName']}`" if exp['ExportName'] else "*Ordinal Only*"
                    rva = f"`{exp['RVA']}`"
                    size = f"{int(exp['FunctionSize']):,}" if exp['FunctionSize'].isdigit() else exp['FunctionSize']
                    
                    notes = ""
                    if exp['SizeCalculationMethod'] == "Forwarded":
                        size = "-"
                        notes = f"Forwarded to: `{exp['ForwardedURL']}`"
                    elif exp['SizeCalculationMethod'] in ("ContiguousDelta", "SectionBoundedDelta"):
                        notes = "*Size estimated via contiguous RVA delta.*"

                    md.write(f"| {exp['Ordinal']} | {name} | {rva} | {size} | {exp['SizeCalculationMethod']} | {notes} |\n")

    # 2. Generate local READMEs for every directory containing binaries
    print(f"[*] Compiling {len(dir_manifests)} subdirectory table-of-contents files...")
    for rel_dir_path, dll_list in dir_manifests.items():
        generate_sub_directory_readme(base_output_path / rel_dir_path, rel_dir_path, dll_list)

    # 3. Generate the top-level Master README index
    print(f"[*] Creating main index entry portal: {base_output_path / 'README.md'}")
    generate_master_root_readme(base_output_path, dir_manifests)
    
    print(f"[+] Documentation tree compilation complete.")

def generate_sub_directory_readme(target_dir_path, relative_path, dll_list):
    """Generates a contextual README table of contents for a single mirrored subdirectory."""
    readme_path = target_dir_path / "README.md"
    dll_list.sort(key=lambda x: x['name'].lower())
    
    # Calculate relative hop back to root index
    depth = len(relative_path.parts)
    back_to_root = "../" * depth if depth > 0 else "./"
    
    with open(readme_path, mode="w", encoding="utf-8") as md:
        md.write(f"# Directory Inventory: `/{relative_path.as_posix()}`\n\n")
        md.write(f"[⬅ Back to Root System Index]({back_to_root}README.md)\n\n")
        md.write("### Binary Inventory Table of Contents\n\n")
        md.write("| Binary Name | Architecture | Exports Count | SHA256 (Short) | Details Link |\n")
        md.write("| :--- | :---: | :---: | :---: | :--- |\n")
        
        for dll in dll_list:
            link = f"[View Specification](./{dll['doc_file']})"
            md.write(f"| **{dll['name']}** | {dll['arch']} | {dll['export_count']} | `{dll['sha256'][:10]}` | {link} |\n")

def generate_master_root_readme(base_output_path, dir_manifests):
    """Generates the main navigation portal at the root directory."""
    readme_path = base_output_path / "README.md"
    sorted_directories = sorted(list(dir_manifests.keys()))
    
    with open(readme_path, mode="w", encoding="utf-8") as md:
        md.write("# System Interface Documentation Directory\n\n")
        md.write("Automated surface map tree organizing exported binary dependencies by file system context.\n\n")
        md.write("## Navigation Tree Structure\n\n")
        md.write("| Monitored Path Structure | Total Target Binaries | Navigation Link |\n")
        md.write("| :--- | :---: | :--- |\n")
        
        for rel_path in sorted_directories:
            dll_count = len(dir_manifests[rel_path])
            posix_str = rel_path.as_posix()
            
            nav_link = f"[Explore Folder](./{posix_str}/README.md)"
            md.write(f"| 📁 `/{posix_str}` | {dll_count} | {nav_link} |\n")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python doc_generator.py <input_csv_path> <output_markdown_directory>")
        sys.exit(1)

    csv_input = sys.argv[1]
    md_output_dir = sys.argv[2]
    
    generate_markdown_docs(csv_input, md_output_dir)