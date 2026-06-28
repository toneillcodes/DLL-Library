# DLL Inventory Collector (`dll_inventory.py`)

A high-throughput, concurrent filesystem crawler designed to extract structural telemetry directly from Portable Executable (PE) headers. 

## Technical Internals & Architecture

### Concurrency Model
The script utilizes Python's `concurrent.futures.ThreadPoolExecutor` to parallelize disk operations and binary parsing. Because checking deep system directories involves heavy I/O operations, dropping into background processing threads allows the script to overlap read times efficiently. It utilizes tight worker routines wrapped around a global thread-safe CSV `Lock` to prevent output contamination.

### Binary Sizing Engines
To calculate an exported function's byte footprint without full debugging symbols, the script applies a tiered resolution strategy:
1. **Unwind Table Lookup (x64):** The script parses the Exception Data Directory (`.pdata`). It extracts the explicit runtime function table (`RUNTIME_FUNCTION` entries), mapping the `BeginAddress` and `EndAddress` virtual markers to pinpoint exact assembly blocks.
2. **Contiguous RVA Delta (x86 / Stripped Fallback):** When unwind data is absent or the binary is compiled for x86 architectures, the script collects all export Relative Virtual Addresses (RVAs), sorts them chronologically, and calculates the memory distance between adjacent entry points.
3. **Section Bounding:** If an export is the final entry in the sorted RVA list, its size is bound against the remaining virtual space available inside its parent `.text` code section.

### Export Type Verification
The parser isolates standard exports from **Forwarded Exports** (where an export points to a string redirecting to another library, like `NTDLL.RtlAllocateHeap`). Forwarders are logged explicitly with their destination string, preventing incorrect size assertions.

## Implementation Prerequisites

```bash
pip install pefile
```

## Argument Specifications
```bash
python dll_inventory.py <target_directory> <output_csv_path>
```
* `target_directory`: The absolute or relative root path to crawl for .dll binaries (e.g., `C:\Windows\System32`).
* `output_csv_path`: The target file location where raw tabular data will be stored (e.g., `C:\dev\inventory.csv`).