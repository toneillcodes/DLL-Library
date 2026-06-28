# Binary Specification: Windows.StateRepository.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Windows.StateRepository.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1f8d29d391db8c96a58b4e5cb487649a4f2ccbac23f9e4ecbfb1ac8908ea8d31`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `ServiceMain` | `0xA9340` | 1,032 | UnwindData |  |
| 3 | `StateRepository_DataAccessLayer_DatabaseCache_Add` | `0xC67D0` | 57 | UnwindData |  |
| 4 | `StateRepository_DataAccessLayer_DatabaseCache_Get` | `0xC6810` | 60 | UnwindData |  |
| 5 | `StateRepository_Initialize` | `0xC6860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `StateRepository_Shutdown` | `0xC6870` | 37,664 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `SvchostPushServiceGlobals` | `0xCFB90` | 976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `StateRepository_Service_UpdateStatus` | `0xCFF60` | 35 | UnwindData |  |
