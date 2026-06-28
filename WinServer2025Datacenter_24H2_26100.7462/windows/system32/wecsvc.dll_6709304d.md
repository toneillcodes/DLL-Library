# Binary Specification: wecsvc.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wecsvc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6709304dbf84c442b47a0657e5c1aeadf7fbef780ff3cc8c0bb65fd3f0b9c511`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `ServiceMain` | `0x2A50` | 422 | UnwindData |  |
| 2 | `SvchostPushServiceGlobals` | `0x2CD0` | 2,400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x3630` | 127,084 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x3630` | 127,084 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
