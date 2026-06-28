# Binary Specification: aeinv.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\aeinv.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c9232615bd0899dcd20b73c6b7a2ecc7b7ad4d77ab33f05c2e194e415b27483e`
* **Total Exported Functions:** 13

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `GetAppInfo2` | `0x7D50` | 3,934 | UnwindData |  |
| 1 | `CreateAppxPackageInventory` | `0x45F70` | 341 | UnwindData |  |
| 2 | `CreateAppxPackageInventoryExtracted` | `0x460D0` | 498 | UnwindData |  |
| 3 | `CreateSoftwareInventory` | `0x46710` | 2,619 | UnwindData |  |
| 5 | `GetAppInfo` | `0x482A0` | 50 | UnwindData |  |
| 6 | `GetAppInventory` | `0x482E0` | 9,980 | UnwindData |  |
| 7 | `GetApplicationKBsTC2` | `0x4AD60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `GetCachedAppInventory` | `0x4AD70` | 1,761 | UnwindData |  |
| 9 | `GetDetailedAppInventory` | `0x4CC40` | 4,206 | UnwindData |  |
| 10 | `GetDetailedAppInventoryFile` | `0x4DCC0` | 1,424 | UnwindData |  |
| 11 | `GetDetailedAppInventoryOrphanFile` | `0x4E260` | 1,547 | UnwindData |  |
| 12 | `UpdateSoftwareInventoryW` | `0x55B60` | 991 | UnwindData |  |
| 13 | `UpdateSoftwareInventoryWTCEx` | `0x55F50` | 361 | UnwindData |  |
