# Binary Specification: eShims.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\eShims.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a023aa972a7d60a8463b5c9a60f99f2ccc0efe9504e7f8b33429e59f281c7ee8`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `RegisterFlashShimHandler` | `0xA940` | 11,392 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `IEShims_Initialize` | `0xD5C0` | 319 | UnwindData |  |
| 10 | `IEShims_Uninitialize` | `0xD710` | 1,264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `IEShims_CreateFileW` | `0xDC00` | 254 | UnwindData |  |
| 3 | `IEShims_FindClose` | `0xDD10` | 86 | UnwindData |  |
| 4 | `IEShims_FindFirstFileW` | `0xDD70` | 169 | UnwindData |  |
| 5 | `IEShims_GetFileAttributesExW` | `0xDE20` | 330 | UnwindData |  |
| 6 | `IEShims_GetFileAttributesW` | `0xDF70` | 242 | UnwindData |  |
| 11 | `IEShims_WNetGetConnectionW` | `0xE3E0` | 129 | UnwindData |  |
| 7 | `IEShims_GetFullPathNameW` | `0xF200` | 473 | UnwindData |  |
| 8 | `IEShims_GetLongPathNameW` | `0xF3E0` | 386 | UnwindData |  |
