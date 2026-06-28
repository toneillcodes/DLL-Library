# Binary Specification: wecsvc.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wecsvc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `471262d2e67fddbef4ef8c17af2acbaff3bbb1767e53d520b6e07b9ddab6ccf9`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `ServiceMain` | `0x2C70` | 422 | UnwindData |  |
| 2 | `SvchostPushServiceGlobals` | `0x2EF0` | 2,400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x3850` | 156,828 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x3850` | 156,828 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
