# Binary Specification: mpunits.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\mpunits.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a6cbbea85a51c6a2b565538fcfede4536ae6cd3439f34e2f697fed5ce3d4c2fd`
* **Total Exported Functions:** 14

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `MI_Main` | `0x63E0` | 4,112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `_BinaryLogReader_GetNextInstance` | `0x73F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `_BinaryLogReader_ValidateHeader` | `0x7410` | 131,664 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `SyncBmilReader_Create` | `0x27660` | 226 | UnwindData |  |
| 6 | `SyncBmilReader_Delete` | `0x27750` | 99 | UnwindData |  |
| 7 | `SyncBmilReader_ReadInstance` | `0x277C0` | 112 | UnwindData |  |
| 8 | `SyncBmilWriter_Create` | `0x27840` | 204 | UnwindData |  |
| 9 | `SyncBmilWriter_Delete` | `0x27920` | 99 | UnwindData |  |
| 10 | `SyncBmilWriter_WriteInstance` | `0x27990` | 107 | UnwindData |  |
| 2 | `MPUnitsTraps` | `0x49010` | 6,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `NITS_STUB` | `0x4AA60` | 40,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `monitoring_platformFT_V1` | `0x549B8` | 15,784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `monitoring_platform_reactive_extensionsFT_V1` | `0x58760` | 104,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `NITS_PRESENCE_STUB` | `0x72048` | 0 | Indeterminate |  |
