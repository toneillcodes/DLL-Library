# DLL-Library

An automated binary analysis and documentation pipeline designed to fingerprint, inspect, and map the exported interfaces of Windows Dynamic Link Libraries (DLLs). By combining low-level PE header analysis with structural filesystem mirroring, this toolset generates comprehensive, version-locked interface specifications of an operating system's user-mode attack surface.

This is highly effective for building system baselines, mapping potential proxying/sideloading targets, profiling binaries for tradecraft (such as identifying code caves or module-stomping targets), and tracking undocumented API changes across different Windows patch levels.

---

## Architecture Overview

The pipeline splits the collection and presentation phases into two decoupled tools to ensure high performance and data portability:

1. **`dll_inventory.py` (The Collector):** A multi-threaded engine that crawls a specified directory, parses structural data directly from PE headers via `pefile`, and outputs a centralized dataset to a CSV file.
* [dll_inventory.py Documentation](docs/dll_inventory.md)
2. **`doc_generator.py` (The Transformer):** A serialization utility that consumes the generated CSV dataset, mirrors the original file system's nested directory architecture, and generates human-readable Markdown documentation complete with cross-referenced indices.
* [doc_generator.py Documentation](docs/doc-generator.md)

---

## 🚀 Usage Guide

### Step 1: Generate the Environment Target Folder
To keep documentation organized across different installations or patch revisions, run the following commands in PowerShell to generate an OS-specific version string and create your destination directory:

```
$OSInfo = Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion"
$Prod = ($OSInfo.ProductName -replace 'Windows ', 'Win' -replace ' ', '')
$Ver = if ($OSInfo.DisplayVersion) { $OSInfo.DisplayVersion } else { "Unknown" }
$Build = $OSInfo.CurrentBuild
$UBR = $OSInfo.UBR
$DirName = "${Prod}_${Ver}_${Build}.${UBR}"
New-Item -Path "C:\dev\dll-library" -Name $DirName -ItemType Directory -Force
```

Example directory generated: `C:\dev\dll-library\Win11Pro_23H2_22631.3737`

### Step 2: Run the Inventory Collector
Execute the concurrent crawler against your target folder (e.g., testing an application directory or full system folder):

```cmd
python dll_inventory.py "C:\Windows\System32" "C:\dev\dll-inventory.csv"
```

## 📂 Output Target Structure

Upon completion, your library output will be structured as follows:

```text
📁 C:\dev\dll-library\Win11Pro_23H2_22631.3737\
│
├── 📄 README.md                 # Master Index Gateway (Lists all tracked directories)
│
└── 📁 Windows\
    └── 📁 System32\
        ├── 📄 README.md         # Local Directory Index (Table of contents for System32)
        ├── 📄 ntdll_a1b2c3d4.md  # Detailed Specification Map (Ordinal, Name, RVA, Size)
        └── 📄 kernel32_e5f6g7h8.md
```