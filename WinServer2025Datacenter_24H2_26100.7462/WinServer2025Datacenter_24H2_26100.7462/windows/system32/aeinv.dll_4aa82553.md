# Binary Specification: aeinv.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\aeinv.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4aa82553122ca9abe22e11518b22dcaead7052d4d1736b8a0480bdb153306439`
* **Total Exported Functions:** 13

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `GetAppInfo2` | `0x12740` | 3,928 | UnwindData |  |
| 1 | `CreateAppxPackageInventory` | `0x49C70` | 341 | UnwindData |  |
| 2 | `CreateAppxPackageInventoryExtracted` | `0x49DD0` | 498 | UnwindData |  |
| 3 | `CreateSoftwareInventory` | `0x4A410` | 2,598 | UnwindData |  |
| 5 | `GetAppInfo` | `0x4BA00` | 50 | UnwindData |  |
| 6 | `GetAppInventory` | `0x4BA40` | 8,562 | UnwindData |  |
| 7 | `GetApplicationKBsTC2` | `0x4E040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `GetCachedAppInventory` | `0x4E050` | 1,750 | UnwindData |  |
| 9 | `GetDetailedAppInventory` | `0x50230` | 4,051 | UnwindData |  |
| 10 | `GetDetailedAppInventoryFile` | `0x51210` | 1,410 | UnwindData |  |
| 11 | `GetDetailedAppInventoryOrphanFile` | `0x517A0` | 1,539 | UnwindData |  |
| 12 | `UpdateSoftwareInventoryW` | `0x58970` | 1,251 | UnwindData |  |
| 13 | `UpdateSoftwareInventoryWTCEx` | `0x58E60` | 361 | UnwindData |  |
