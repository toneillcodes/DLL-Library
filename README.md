# DLL-Library

An automated binary analysis and documentation pipeline designed to fingerprint, inspect, and map the exported interfaces of Windows Dynamic Link Libraries (DLLs). By combining low-level PE header analysis with structural filesystem mirroring, this toolset generates comprehensive, version-locked interface specifications of an operating system's user-mode attack surface.

This is highly effective for building system baselines, mapping potential proxying/sideloading targets, profiling binaries for tradecraft (such as identifying code caves or module-stomping targets), and tracking undocumented API changes across different Windows patch levels.

---

## Catalog
* [Win11Pro_25H2_26200.8655](Win11Pro_25H2_26200.8655/README.md)

## Architecture Overview

The pipeline splits the collection and presentation phases into two decoupled tools to ensure high performance and data portability:

1. **`dll-inventory.py` (The Collector):** A multi-threaded engine that crawls a specified directory, parses structural data directly from PE headers via `pefile`, and outputs a centralized dataset to a CSV file.
* [dll-inventory.py Documentation](docs/dll-inventory.md)
2. **`doc-generator.py` (The Transformer):** A serialization utility that consumes the generated CSV dataset, mirrors the original file system's nested directory architecture, and generates human-readable Markdown documentation complete with cross-referenced indices.
* [doc-generator.py Documentation](docs/doc-generator.md)

---

## 🚀 Usage Guide

## Prerequisites

This tool requires the `pefile` library to parse Portable Executable headers. You can install it via `pip`:

```bash
pip install pefile
```

### Step 1: Generate the Environment Target Folder
To keep documentation organized across different installations or patch revisions, run the following commands in PowerShell to generate an OS-specific version string and create your destination directory:

```
$OSInfo = Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion"
# Query CIM for the real marketing name (e.g., "Microsoft Windows 11 Pro")
$RealName = (Get-CimInstance Win32_OperatingSystem).Caption
# Clean it up to "Win11Pro"
$Prod = ($RealName -replace 'Microsoft ', '' -replace 'Windows ', 'Win' -replace ' ', '')
$Ver = if ($OSInfo.DisplayVersion) { $OSInfo.DisplayVersion } else { "Unknown" }
$Build = $OSInfo.CurrentBuild
$UBR = $OSInfo.UBR
$DirName = "${Prod}_${Ver}_${Build}.${UBR}"
New-Item -Path "D:\dev\DLL-Library" -Name $DirName -ItemType Directory -Force
```

Example directory generated: `D:\dev\DLL-Library\Win11Pro_25H2_26200.8655`

Example output
```
PS D:\dev\DLL-Library> $OSInfo = Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion"
PS D:\dev\DLL-Library> # Query CIM for the real marketing name (e.g., "Microsoft Windows 11 Pro")
PS D:\dev\DLL-Library> $RealName = (Get-CimInstance Win32_OperatingSystem).Caption
PS D:\dev\DLL-Library> # Clean it up to "Win11Pro"
PS D:\dev\DLL-Library> $Prod = ($RealName -replace 'Microsoft ', '' -replace 'Windows ', 'Win' -replace ' ', '')
PS D:\dev\DLL-Library> $Ver = if ($OSInfo.DisplayVersion) { $OSInfo.DisplayVersion } else { "Unknown" }
PS D:\dev\DLL-Library> $Build = $OSInfo.CurrentBuild
PS D:\dev\DLL-Library> $UBR = $OSInfo.UBR
PS D:\dev\DLL-Library> $DirName = "${Prod}_${Ver}_${Build}.${UBR}"
PS D:\dev\DLL-Library> New-Item -Path "D:\dev\DLL-Library" -Name $DirName -ItemType Directory -Force


    Directory: C:\dev\DLL-Library


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         6/27/2026  10:03 PM                Win11Pro_25H2_26200.8655


PS D:\dev\DLL-Library>
```

### Step 2: Run the Inventory Collector
Execute the concurrent crawler against your target folder (e.g., testing an application directory or full system folder):

```cmd
python dll-inventory.py "C:\Windows\System32" "D:\dev\dll-inventory.csv"
```
Example output
```
PS D:\dev\DLL-Library> python dll-inventory.py "C:\Windows\System32" "D:\dev\dll-inventory.csv"
[*] Initializing scan on target directory: C:\Windows\System32
[*] Results will be saved to: D:\dev\dll-inventory.csv
[*] Scheduled 5671 DLL files for analysis. Processing...
    Progress: 5671/5671 files evaluated.
[+] Inventory process completed successfully.
PS D:\dev\DLL-Library>
```

### Step 3: Compile the Markdown Library
Point the documentation transformer at the collected dataset and output straight into your version-locked target directory:

```cmd
python doc-generator.py "C:\dev\dll-inventory.csv" "D:\dev\DLL-Library\Win11Pro_25H2_26200.8655"
```
Example output
```
PS D:\dev\DLL-Library> python doc-generator.py D:\dev\dll-inventory.csv D:\dev\DLL-Library\Win11Pro_25H2_26200.8655
[*] Checking CSV path: D:\dev\dll-inventory.csv
[+] CSV file found. Opening and parsing...
[*] Detected CSV Headers: ['SHA256', 'FilePath', 'Architecture', 'ExportName', 'Ordinal', 'RVA', 'FunctionSize', 'SizeCalculationMethod', 'ForwardedURL']
[+] Successfully parsed 350660 total rows from CSV.
[*] Distinct directories identified: 226
[*] Generating mirrored documentation structure inside: D:\dev\DLL-Library\Win11Pro_25H2_26200.8655
[*] Compiling 226 subdirectory table-of-contents files...
[*] Creating main index entry portal: D:\dev\DLL-Library\Win11Pro_25H2_26200.8655\README.md
[+] Documentation tree compilation complete.
PS D:\dev\DLL-Library>
```

## 📂 Output Target Structure

Upon completion, your library output will be structured as follows:

```text
📁 C:\dev\DLL-Library\Win11Pro_25H2_26200.8655\
│
├── 📄 README.md                 # Master Index Gateway (Lists all tracked directories)
│
└── 📁 Windows\
    └── 📁 System32\
        ├── 📄 README.md         # Local Directory Index (Table of contents for System32)
        ├── 📄 ntdll_a1b2c3d4.md  # Detailed Specification Map (Ordinal, Name, RVA, Size)
        └── 📄 kernel32_e5f6g7h8.md
```