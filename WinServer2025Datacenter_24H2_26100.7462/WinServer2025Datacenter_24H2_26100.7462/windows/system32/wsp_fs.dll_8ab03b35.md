# Binary Specification: wsp_fs.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wsp_fs.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8ab03b3535313229ef3968d0fd1c74002dffaceb6090862350bb5f3d164f39c8`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 8 | `PreShutdown` | `0x5220` | 25,504 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `SetShutdownCallback` | `0x5220` | 25,504 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `MI_Main` | `0xB5C0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `SmpUnload` | `0xB620` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0xB670` | 47 | UnwindData |  |
| 2 | `DllGetClassObject` | `0xB6B0` | 119 | UnwindData |  |
| 3 | `DllMain` | `0xB730` | 134 | UnwindData |  |
| 4 | `DllRegisterServer` | `0xB7C0` | 72 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0xB810` | 65 | UnwindData |  |
| 6 | `GetProviderClassID` | `0xB9A0` | 651,376 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
