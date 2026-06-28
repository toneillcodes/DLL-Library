# Binary Specification: igc64.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_1973c0a49e1f4f8c\igc64.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2d1bb9af769a753c83c74390b11967515b0460bde44473d5b2f9aed4432e48c1`
* **Total Exported Functions:** 13

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `Create` | `0x73F30` | 42 | UnwindData |  |
| 4 | `Delete` | `0x740C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `Register` | `0x740E0` | 32,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CIFCreateMain` | `0x7BF90` | 54 | UnwindData |  |
| 5 | `JITCompile` | `0x54A3E0` | 121 | UnwindData |  |
| 6 | `JITCompile_v2` | `0x54A460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `freeBlock` | `0x54A480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `getJITVersion` | `0x54A490` | 18,524,208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `OpenCompiler10` | `0x16F4CC0` | 26 | UnwindData |  |
| 8 | `OpenCompiler12` | `0x16F4E30` | 890 | UnwindData |  |
| 1 | `OpenCompiler9` | `0x17C9030` | 452 | UnwindData |  |
| 9 | `OpenOGLCompiler` | `0x17FC870` | 161 | UnwindData |  |
| 10 | `OpenVulkanCompiler` | `0x180C1B0` | 160 | UnwindData |  |
