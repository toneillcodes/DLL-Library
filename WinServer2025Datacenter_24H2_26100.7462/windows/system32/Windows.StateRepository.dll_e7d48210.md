# Binary Specification: Windows.StateRepository.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Windows.StateRepository.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e7d48210a8211809d1662430e1c51a0bf0c2c032b238070c81a012194cb8e123`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `ServiceMain` | `0xA2970` | 620 | UnwindData |  |
| 3 | `StateRepository_DataAccessLayer_DatabaseCache_Add` | `0xC97E0` | 57 | UnwindData |  |
| 4 | `StateRepository_DataAccessLayer_DatabaseCache_Get` | `0xC9820` | 60 | UnwindData |  |
| 5 | `StateRepository_Initialize` | `0xC9870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `StateRepository_Shutdown` | `0xC9880` | 31,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `SvchostPushServiceGlobals` | `0xD1260` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `StateRepository_Service_UpdateStatus` | `0xD13E0` | 24 | UnwindData |  |
