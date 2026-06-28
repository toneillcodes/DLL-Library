# Binary Specification: eShims.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\eShims.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `98fcc4e4103780dae90e5ee3a47a0c3f9501abd5ffa895a08b5be8707757f563`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `RegisterFlashShimHandler` | `0xA960` | 11,392 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `IEShims_Initialize` | `0xD5E0` | 319 | UnwindData |  |
| 10 | `IEShims_Uninitialize` | `0xD730` | 1,264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `IEShims_CreateFileW` | `0xDC20` | 254 | UnwindData |  |
| 3 | `IEShims_FindClose` | `0xDD30` | 86 | UnwindData |  |
| 4 | `IEShims_FindFirstFileW` | `0xDD90` | 169 | UnwindData |  |
| 5 | `IEShims_GetFileAttributesExW` | `0xDE40` | 330 | UnwindData |  |
| 6 | `IEShims_GetFileAttributesW` | `0xDF90` | 242 | UnwindData |  |
| 11 | `IEShims_WNetGetConnectionW` | `0xE400` | 129 | UnwindData |  |
| 7 | `IEShims_GetFullPathNameW` | `0xF220` | 473 | UnwindData |  |
| 8 | `IEShims_GetLongPathNameW` | `0xF400` | 386 | UnwindData |  |
