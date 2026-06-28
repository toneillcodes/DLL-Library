# Binary Specification: MosHostClient.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\MosHostClient.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `813e90d189e64f500618add230c1c6fd5b5798a6db61be9634fa6dc35bc675a6`
* **Total Exported Functions:** 56

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 17 | `MosCacheStateGetSizes` | `0xA540` | 101 | UnwindData |  |
| 18 | `MosCacheStateSetMaxSize` | `0xA5B0` | 79 | UnwindData |  |
| 19 | `MosCacheStateSetSlotSize` | `0xA610` | 100 | UnwindData |  |
| 20 | `MosCacheStateSnapshot` | `0xA680` | 90 | UnwindData |  |
| 21 | `MosCacheStateUnuseSlot` | `0xA6E0` | 97 | UnwindData |  |
| 22 | `MosCacheStateUseSlot` | `0xA750` | 116 | UnwindData |  |
| 23 | `MosDeleteDataAsyncOperation` | `0xA7D0` | 580 | UnwindData |  |
| 24 | `MosGetBrowseCacheSizeInMBytes` | `0xAA20` | 103 | UnwindData |  |
| 25 | `MosGetCopyrightString` | `0xAA90` | 108 | UnwindData |  |
| 26 | `MosGetDataAsync` | `0xAB10` | 386 | UnwindData |  |
| 27 | `MosGetDataAsyncOperation` | `0xACA0` | 596 | UnwindData |  |
| 28 | `MosGetDataDirectory` | `0xAF00` | 118 | UnwindData |  |
| 29 | `MosGetResourceDirectory` | `0xAF80` | 118 | UnwindData |  |
| 30 | `MosHostClose` | `0xB000` | 149 | UnwindData |  |
| 4 | `MapsPackageFree` | `0xB0A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `MapsStorageFree` | `0xB0A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `MosHostFree` | `0xB0A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `OdmlFree` | `0xB0A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `MosHostOpen` | `0xB0C0` | 58 | UnwindData |  |
| 33 | `MosReportCacheMiss` | `0xB100` | 160 | UnwindData |  |
| 34 | `MosRequestResourceLock` | `0xB1B0` | 116 | UnwindData |  |
| 35 | `MosRequestResourceUnlock` | `0xB230` | 87 | UnwindData |  |
| 36 | `OdmlAddMapPackages` | `0xE090` | 88 | UnwindData |  |
| 37 | `OdmlCancelMapDataMigration` | `0xE0F0` | 72 | UnwindData |  |
| 38 | `OdmlCancelMapPackage` | `0xE140` | 79 | UnwindData |  |
| 39 | `OdmlClose` | `0xE1A0` | 127 | UnwindData |  |
| 40 | `OdmlDeleteAllMaps` | `0xE230` | 72 | UnwindData |  |
| 41 | `OdmlFindNearbyPackagesAsync` | `0xE280` | 182 | UnwindData |  |
| 43 | `OdmlGetAutoUpdateEnabled` | `0xE340` | 80 | UnwindData |  |
| 44 | `OdmlGetAvailablePackages` | `0xE3A0` | 93 | UnwindData |  |
| 45 | `OdmlGetCopyrightString` | `0xE410` | 88 | UnwindData |  |
| 46 | `OdmlGetIsStorageStateValid` | `0xE470` | 80 | UnwindData |  |
| 47 | `OdmlGetShouldUseWlanString` | `0xE4D0` | 80 | UnwindData |  |
| 48 | `OdmlGetUpdateOnlyOnWifi` | `0xE530` | 80 | UnwindData |  |
| 49 | `OdmlGetUserPackages` | `0xE590` | 81 | UnwindData |  |
| 50 | `OdmlOpen` | `0xE5F0` | 64 | UnwindData |  |
| 51 | `OdmlRemoveMapPackages` | `0xE640` | 88 | UnwindData |  |
| 52 | `OdmlSetAutoUpdateEnabled` | `0xE6A0` | 79 | UnwindData |  |
| 53 | `OdmlSetUpdateOnlyOnWifi` | `0xE700` | 79 | UnwindData |  |
| 54 | `OdmlStartCheckForUpdates` | `0xE760` | 72 | UnwindData |  |
| 55 | `OdmlStartInstallUpdate` | `0xE7B0` | 72 | UnwindData |  |
| 56 | `OdmlStartMapDataMigration` | `0xE800` | 115 | UnwindData |  |
| 1 | `MapsPackageAddMapPackageAsync` | `0xFD30` | 97 | UnwindData |  |
| 2 | `MapsPackageClose` | `0xFDA0` | 135 | UnwindData |  |
| 3 | `MapsPackageFindNearbyPackagesAsync` | `0xFE30` | 182 | UnwindData |  |
| 5 | `MapsPackageGetPackages` | `0xFEF0` | 93 | UnwindData |  |
| 6 | `MapsPackageOpen` | `0xFF60` | 64 | UnwindData |  |
| 7 | `MapsStorageClose` | `0x10B10` | 127 | UnwindData |  |
| 9 | `MapsStorageGetCurrentLocation` | `0x10BA0` | 89 | UnwindData |  |
| 10 | `MapsStorageGetDataDirectory` | `0x10C00` | 108 | UnwindData |  |
| 11 | `MapsStorageGetLocations` | `0x10C80` | 99 | UnwindData |  |
| 12 | `MapsStorageGetMigrationState` | `0x10CF0` | 89 | UnwindData |  |
| 13 | `MapsStorageOpen` | `0x10D50` | 61 | UnwindData |  |
| 14 | `MapsStorageQueueSwitchToDefaultExternalStorage` | `0x10DA0` | 72 | UnwindData |  |
| 15 | `MapsStorageUseDefaultExternalStorage` | `0x10DF0` | 80 | UnwindData |  |
| 16 | `MapsStorageValidateLocationAsync` | `0x10E50` | 128 | UnwindData |  |
