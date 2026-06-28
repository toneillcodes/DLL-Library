# Binary Specification: MosHostClient.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\MosHostClient.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1f948627ad8d769bc04c379aae780aa6ca35a71c8c799ba35b6797c33564b37c`
* **Total Exported Functions:** 56

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 17 | `MosCacheStateGetSizes` | `0xA530` | 101 | UnwindData |  |
| 18 | `MosCacheStateSetMaxSize` | `0xA5A0` | 79 | UnwindData |  |
| 19 | `MosCacheStateSetSlotSize` | `0xA600` | 100 | UnwindData |  |
| 20 | `MosCacheStateSnapshot` | `0xA670` | 90 | UnwindData |  |
| 21 | `MosCacheStateUnuseSlot` | `0xA6D0` | 97 | UnwindData |  |
| 22 | `MosCacheStateUseSlot` | `0xA740` | 116 | UnwindData |  |
| 23 | `MosDeleteDataAsyncOperation` | `0xA7C0` | 580 | UnwindData |  |
| 24 | `MosGetBrowseCacheSizeInMBytes` | `0xAA10` | 103 | UnwindData |  |
| 25 | `MosGetCopyrightString` | `0xAA80` | 108 | UnwindData |  |
| 26 | `MosGetDataAsync` | `0xAB00` | 386 | UnwindData |  |
| 27 | `MosGetDataAsyncOperation` | `0xAC90` | 596 | UnwindData |  |
| 28 | `MosGetDataDirectory` | `0xAEF0` | 118 | UnwindData |  |
| 29 | `MosGetResourceDirectory` | `0xAF70` | 118 | UnwindData |  |
| 30 | `MosHostClose` | `0xAFF0` | 149 | UnwindData |  |
| 4 | `MapsPackageFree` | `0xB090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `MapsStorageFree` | `0xB090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `MosHostFree` | `0xB090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `OdmlFree` | `0xB090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `MosHostOpen` | `0xB0B0` | 58 | UnwindData |  |
| 33 | `MosReportCacheMiss` | `0xB0F0` | 160 | UnwindData |  |
| 34 | `MosRequestResourceLock` | `0xB1A0` | 116 | UnwindData |  |
| 35 | `MosRequestResourceUnlock` | `0xB220` | 87 | UnwindData |  |
| 36 | `OdmlAddMapPackages` | `0xE080` | 88 | UnwindData |  |
| 37 | `OdmlCancelMapDataMigration` | `0xE0E0` | 72 | UnwindData |  |
| 38 | `OdmlCancelMapPackage` | `0xE130` | 79 | UnwindData |  |
| 39 | `OdmlClose` | `0xE190` | 127 | UnwindData |  |
| 40 | `OdmlDeleteAllMaps` | `0xE220` | 72 | UnwindData |  |
| 41 | `OdmlFindNearbyPackagesAsync` | `0xE270` | 182 | UnwindData |  |
| 43 | `OdmlGetAutoUpdateEnabled` | `0xE330` | 80 | UnwindData |  |
| 44 | `OdmlGetAvailablePackages` | `0xE390` | 93 | UnwindData |  |
| 45 | `OdmlGetCopyrightString` | `0xE400` | 88 | UnwindData |  |
| 46 | `OdmlGetIsStorageStateValid` | `0xE460` | 80 | UnwindData |  |
| 47 | `OdmlGetShouldUseWlanString` | `0xE4C0` | 80 | UnwindData |  |
| 48 | `OdmlGetUpdateOnlyOnWifi` | `0xE520` | 80 | UnwindData |  |
| 49 | `OdmlGetUserPackages` | `0xE580` | 81 | UnwindData |  |
| 50 | `OdmlOpen` | `0xE5E0` | 64 | UnwindData |  |
| 51 | `OdmlRemoveMapPackages` | `0xE630` | 88 | UnwindData |  |
| 52 | `OdmlSetAutoUpdateEnabled` | `0xE690` | 79 | UnwindData |  |
| 53 | `OdmlSetUpdateOnlyOnWifi` | `0xE6F0` | 79 | UnwindData |  |
| 54 | `OdmlStartCheckForUpdates` | `0xE750` | 72 | UnwindData |  |
| 55 | `OdmlStartInstallUpdate` | `0xE7A0` | 72 | UnwindData |  |
| 56 | `OdmlStartMapDataMigration` | `0xE7F0` | 115 | UnwindData |  |
| 1 | `MapsPackageAddMapPackageAsync` | `0xFD20` | 97 | UnwindData |  |
| 2 | `MapsPackageClose` | `0xFD90` | 135 | UnwindData |  |
| 3 | `MapsPackageFindNearbyPackagesAsync` | `0xFE20` | 182 | UnwindData |  |
| 5 | `MapsPackageGetPackages` | `0xFEE0` | 93 | UnwindData |  |
| 6 | `MapsPackageOpen` | `0xFF50` | 64 | UnwindData |  |
| 7 | `MapsStorageClose` | `0x10B00` | 127 | UnwindData |  |
| 9 | `MapsStorageGetCurrentLocation` | `0x10B90` | 89 | UnwindData |  |
| 10 | `MapsStorageGetDataDirectory` | `0x10BF0` | 108 | UnwindData |  |
| 11 | `MapsStorageGetLocations` | `0x10C70` | 99 | UnwindData |  |
| 12 | `MapsStorageGetMigrationState` | `0x10CE0` | 89 | UnwindData |  |
| 13 | `MapsStorageOpen` | `0x10D40` | 61 | UnwindData |  |
| 14 | `MapsStorageQueueSwitchToDefaultExternalStorage` | `0x10D90` | 72 | UnwindData |  |
| 15 | `MapsStorageUseDefaultExternalStorage` | `0x10DE0` | 80 | UnwindData |  |
| 16 | `MapsStorageValidateLocationAsync` | `0x10E40` | 128 | UnwindData |  |
