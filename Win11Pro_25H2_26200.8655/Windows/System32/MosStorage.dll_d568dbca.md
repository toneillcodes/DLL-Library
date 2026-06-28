# Binary Specification: MosStorage.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\MosStorage.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d568dbcadeef201578b45cb42a9672f21e9fb5042b5825004a7bfaceb457bc91`
* **Total Exported Functions:** 33

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 33 | `MosStorage_SetServiceCallbacks` | `0x6F20` | 11,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `MosStorageDumpConfiguration` | `0x9C00` | 384 | UnwindData |  |
| 6 | `MosStorageEnsureIsAppContainerCompliant` | `0x9D90` | 305 | UnwindData |  |
| 7 | `MosStorageEnsureMapDataDirectory` | `0x9ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `MosStorageEnsureMapDataDirectoryAndKeepFileHandle` | `0x9EE0` | 741 | UnwindData |  |
| 9 | `MosStorageEnsureMapDataDirectoryReturnPath` | `0xA1D0` | 274 | UnwindData |  |
| 10 | `MosStorageGetBrowseCacheSizeInMBytes` | `0xA2F0` | 144 | UnwindData |  |
| 11 | `MosStorageGetCurrentLocation` | `0xA390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `MosStorageGetDataDirectory` | `0xA3A0` | 442 | UnwindData |  |
| 13 | `MosStorageGetDefaultExternalStorage` | `0xA560` | 182 | UnwindData |  |
| 14 | `MosStorageGetLocations` | `0xA620` | 161 | UnwindData |  |
| 15 | `MosStorageGetMapDataMaxBrowseCacheSizeInBytes` | `0xA6D0` | 159 | UnwindData |  |
| 16 | `MosStorageGetMapsRepairAttempts` | `0xA780` | 161 | UnwindData |  |
| 17 | `MosStorageGetMigrationState` | `0xA830` | 77 | UnwindData |  |
| 18 | `MosStorageGetResourceDirectory` | `0xA890` | 185 | UnwindData |  |
| 19 | `MosStorageGetStorageDeviceDataFromDeviceGuid` | `0xA950` | 151 | UnwindData |  |
| 20 | `MosStorageGetStorageSizesInBytes` | `0xA9F0` | 395 | UnwindData |  |
| 21 | `MosStorageGetSystemDataDirectory` | `0xAB90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `MosStorageGetTotalMapDataInBytes` | `0xABA0` | 377 | UnwindData |  |
| 23 | `MosStorageGetWhetherSpaceAvailable` | `0xAD20` | 234 | UnwindData |  |
| 24 | `MosStorageIsStorageStateValid` | `0xAE10` | 99 | UnwindData |  |
| 25 | `MosStorageResetCacheValues` | `0xAE80` | 85 | UnwindData |  |
| 26 | `MosStorageResetPreferredLocationIfDefined` | `0xAF60` | 180 | UnwindData |  |
| 27 | `MosStorageResetPreferredLocationIfNotPresent` | `0xB020` | 318 | UnwindData |  |
| 28 | `MosStorageSetLocation` | `0xB170` | 886 | UnwindData |  |
| 29 | `MosStorageSetMapsRepairAttempts` | `0xB4F0` | 167 | UnwindData |  |
| 30 | `MosStorageSetMigrationState` | `0xB5A0` | 98 | UnwindData |  |
| 31 | `MosStorageUseDefaultExternalStorage` | `0xB610` | 212 | UnwindData |  |
| 32 | `MosStorageValidateLocation` | `0xB6F0` | 1,588 | UnwindData |  |
| 1 | `MosQueryAnyPackagesFromPath` | `0xEBB0` | 115 | UnwindData |  |
| 2 | `MosQueryCatalogExists` | `0xEC30` | 687 | UnwindData |  |
| 3 | `MosQueryPackages` | `0xEEF0` | 159 | UnwindData |  |
| 4 | `MosQueryPackagesFromPath` | `0xEFA0` | 13,020 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
