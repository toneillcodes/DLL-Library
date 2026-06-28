# Binary Specification: defragsvc.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\defragsvc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `95632bd780942879aee7a7e84703acb7fd442d33fa38534453242b8a3cc0d306`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x3FEE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x3FF00` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x40110` | 131 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x401A0` | 98 | UnwindData |  |
| 5 | `ServiceMain` | `0x40330` | 135,932 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
