# Binary Specification: igc64.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_188be4c1587f7330\igc64.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1c486f4690119cdf5cfe0600d8520bcc38282416305aecdb237e323276639065`
* **Total Exported Functions:** 13

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `Create` | `0x70BB0` | 42 | UnwindData |  |
| 4 | `Delete` | `0x70D50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `Register` | `0x70D70` | 32,688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CIFCreateMain` | `0x78D20` | 54 | UnwindData |  |
| 5 | `JITCompile` | `0x57E080` | 121 | UnwindData |  |
| 6 | `JITCompile_v2` | `0x57E100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `freeBlock` | `0x57E120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `getJITVersion` | `0x57E130` | 19,724,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `OpenCompiler10` | `0x184D9C0` | 26 | UnwindData |  |
| 8 | `OpenCompiler12` | `0x184DB30` | 991 | UnwindData |  |
| 1 | `OpenCompiler9` | `0x191FFB0` | 464 | UnwindData |  |
| 9 | `OpenOGLCompiler` | `0x1951140` | 161 | UnwindData |  |
| 10 | `OpenVulkanCompiler` | `0x195E3C0` | 160 | UnwindData |  |
