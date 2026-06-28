# Binary Specification: MosStorage.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\MosStorage.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `569e27976307d0ad63777c8685a10e31e4f49256301636d10ec7f788d30dd8ec`
* **Total Exported Functions:** 33

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 33 | `MosStorage_SetServiceCallbacks` | `0x6F10` | 11,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `MosStorageDumpConfiguration` | `0x9BF0` | 384 | UnwindData |  |
| 6 | `MosStorageEnsureIsAppContainerCompliant` | `0x9D80` | 305 | UnwindData |  |
| 7 | `MosStorageEnsureMapDataDirectory` | `0x9EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `MosStorageEnsureMapDataDirectoryAndKeepFileHandle` | `0x9ED0` | 741 | UnwindData |  |
| 9 | `MosStorageEnsureMapDataDirectoryReturnPath` | `0xA1C0` | 274 | UnwindData |  |
| 10 | `MosStorageGetBrowseCacheSizeInMBytes` | `0xA2E0` | 144 | UnwindData |  |
| 11 | `MosStorageGetCurrentLocation` | `0xA380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `MosStorageGetDataDirectory` | `0xA390` | 442 | UnwindData |  |
| 13 | `MosStorageGetDefaultExternalStorage` | `0xA550` | 182 | UnwindData |  |
| 14 | `MosStorageGetLocations` | `0xA610` | 161 | UnwindData |  |
| 15 | `MosStorageGetMapDataMaxBrowseCacheSizeInBytes` | `0xA6C0` | 159 | UnwindData |  |
| 16 | `MosStorageGetMapsRepairAttempts` | `0xA770` | 161 | UnwindData |  |
| 17 | `MosStorageGetMigrationState` | `0xA820` | 77 | UnwindData |  |
| 18 | `MosStorageGetResourceDirectory` | `0xA880` | 185 | UnwindData |  |
| 19 | `MosStorageGetStorageDeviceDataFromDeviceGuid` | `0xA940` | 151 | UnwindData |  |
| 20 | `MosStorageGetStorageSizesInBytes` | `0xA9E0` | 395 | UnwindData |  |
| 21 | `MosStorageGetSystemDataDirectory` | `0xAB80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `MosStorageGetTotalMapDataInBytes` | `0xAB90` | 377 | UnwindData |  |
| 23 | `MosStorageGetWhetherSpaceAvailable` | `0xAD10` | 234 | UnwindData |  |
| 24 | `MosStorageIsStorageStateValid` | `0xAE00` | 99 | UnwindData |  |
| 25 | `MosStorageResetCacheValues` | `0xAE70` | 85 | UnwindData |  |
| 26 | `MosStorageResetPreferredLocationIfDefined` | `0xAF50` | 180 | UnwindData |  |
| 27 | `MosStorageResetPreferredLocationIfNotPresent` | `0xB010` | 318 | UnwindData |  |
| 28 | `MosStorageSetLocation` | `0xB160` | 886 | UnwindData |  |
| 29 | `MosStorageSetMapsRepairAttempts` | `0xB4E0` | 167 | UnwindData |  |
| 30 | `MosStorageSetMigrationState` | `0xB590` | 98 | UnwindData |  |
| 31 | `MosStorageUseDefaultExternalStorage` | `0xB600` | 212 | UnwindData |  |
| 32 | `MosStorageValidateLocation` | `0xB6E0` | 1,588 | UnwindData |  |
| 1 | `MosQueryAnyPackagesFromPath` | `0xEBA0` | 115 | UnwindData |  |
| 2 | `MosQueryCatalogExists` | `0xEC20` | 687 | UnwindData |  |
| 3 | `MosQueryPackages` | `0xEEE0` | 159 | UnwindData |  |
| 4 | `MosQueryPackagesFromPath` | `0xEF90` | 13,020 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
