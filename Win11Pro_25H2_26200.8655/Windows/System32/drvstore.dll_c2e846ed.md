# Binary Specification: drvstore.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\drvstore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c2e846ed05e52dc0b61aa42fb9bce254ff40f149e6d5b8f046b3c6707c0028a3`
* **Total Exported Functions:** 62

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 33 | `DriverStoreGetObjectPropertyW` | `0x238B0` | 2,012 | UnwindData |  |
| 8 | `DriverPackageEnumEventProvidersW` | `0x33E50` | 501 | UnwindData |  |
| 11 | `DriverPackageEnumFiltersW` | `0x34050` | 473 | UnwindData |  |
| 7 | `DriverPackageEnumEventAutoLoggersW` | `0x347A0` | 499 | UnwindData |  |
| 14 | `DriverPackageEnumPropertiesW` | `0x355F0` | 494 | UnwindData |  |
| 12 | `DriverPackageEnumInterfacesW` | `0x357F0` | 500 | UnwindData |  |
| 15 | `DriverPackageEnumRegKeysW` | `0x363D0` | 530 | UnwindData |  |
| 10 | `DriverPackageEnumFilesW` | `0x369C0` | 850 | UnwindData |  |
| 16 | `DriverPackageEnumServicesW` | `0x36DF0` | 500 | UnwindData |  |
| 6 | `DriverPackageEnumDriversW` | `0x372E0` | 885 | UnwindData |  |
| 19 | `DriverPackageGetVersionInfoW` | `0x43A90` | 673 | UnwindData |  |
| 20 | `DriverPackageOpenW` | `0x44180` | 30 | UnwindData |  |
| 18 | `DriverPackageGetPropertyW` | `0x44650` | 3,826 | UnwindData |  |
| 1 | `DriverPackageClose` | `0x45550` | 71 | UnwindData |  |
| 62 | `pServerImportDriverPackage` | `0x469F0` | 715 | UnwindData |  |
| 30 | `DriverStoreEnumW` | `0x46D10` | 364 | UnwindData |  |
| 26 | `DriverStoreEnumDeviceDriversW` | `0x46E90` | 338 | UnwindData |  |
| 31 | `DriverStoreFindW` | `0x46FF0` | 399 | UnwindData |  |
| 21 | `DriverStoreClose` | `0x47190` | 286 | UnwindData |  |
| 45 | `DriverStoreOpenW` | `0x47300` | 1,990 | UnwindData |  |
| 52 | `DriverStoreSetObjectPropertyW` | `0x74CD0` | 394 | UnwindData |  |
| 5 | `DriverPackageEnumDevicesW` | `0x79090` | 680 | UnwindData |  |
| 51 | `DriverStoreSetLogContext` | `0x7A600` | 36 | UnwindData |  |
| 28 | `DriverStoreEnumObjectsW` | `0x7A690` | 357 | UnwindData |  |
| 17 | `DriverPackageEnumSoftwareW` | `0x7A950` | 489 | UnwindData |  |
| 2 | `DriverPackageEnumClassesW` | `0x7AFB0` | 760 | UnwindData |  |
| 61 | `pServerDeleteDriverPackage` | `0x7D720` | 582 | UnwindData |  |
| 22 | `DriverStoreConfigureW` | `0x7FD10` | 9,872 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DriverPackageEnumConfigurationsW` | `0x823A0` | 455 | UnwindData |  |
| 48 | `DriverStoreReflectW` | `0x82580` | 200 | UnwindData |  |
| 3 | `DriverPackageEnumComponentsW` | `0x827E0` | 489 | UnwindData |  |
| 25 | `DriverStoreDriverPackageResolveCallbackW` | `0x85BD0` | 1,457 | UnwindData |  |
| 46 | `DriverStorePublishW` | `0x87A40` | 1,930 | UnwindData |  |
| 56 | `DriverStoreUnpublishW` | `0x881D0` | 1,555 | UnwindData |  |
| 13 | `DriverPackageEnumOsVersionsW` | `0x9DD30` | 166 | UnwindData |  |
| 35 | `DriverStoreImportW` | `0x9E6A0` | 1,581 | UnwindData |  |
| 34 | `DriverStoreGetParameter` | `0xA7490` | 1,741 | UnwindData |  |
| 53 | `DriverStoreSetParameter` | `0xA7CD0` | 713 | UnwindData |  |
| 24 | `DriverStoreDeleteW` | `0xA95A0` | 1,064 | UnwindData |  |
| 23 | `DriverStoreCopyW` | `0xA99D0` | 1,197 | UnwindData |  |
| 27 | `DriverStoreEnumNodesW` | `0xAA4B0` | 351 | UnwindData |  |
| 36 | `DriverStoreMountNodeW` | `0xAA620` | 350 | UnwindData |  |
| 50 | `DriverStoreSelectNodeW` | `0xAA790` | 221 | UnwindData |  |
| 55 | `DriverStoreUnmountNodeW` | `0xAA880` | 188 | UnwindData |  |
| 32 | `DriverStoreGetObjectPropertyKeysW` | `0xAA950` | 369 | UnwindData |  |
| 47 | `DriverStoreReflectCriticalW` | `0xB2A40` | 64 | UnwindData |  |
| 57 | `DriverStoreUnreflectCriticalW` | `0xB2A90` | 98 | UnwindData |  |
| 58 | `DriverStoreUnreflectW` | `0xB2B00` | 200 | UnwindData |  |
| 54 | `DriverStoreUnconfigureW` | `0xB48E0` | 16,400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `DriverStoreUpdateDevicesW` | `0xB88F0` | 1,383 | UnwindData |  |
| 60 | `DriverStoreVerifyIntegrityW` | `0xBC320` | 1,242 | UnwindData |  |
| 37 | `DriverStoreOfflineAddDriverPackageA` | `0xC06B0` | 710 | UnwindData |  |
| 38 | `DriverStoreOfflineAddDriverPackageW` | `0xC0980` | 988 | UnwindData |  |
| 39 | `DriverStoreOfflineDeleteDriverPackageA` | `0xC0D70` | 279 | UnwindData |  |
| 40 | `DriverStoreOfflineDeleteDriverPackageW` | `0xC0E90` | 442 | UnwindData |  |
| 41 | `DriverStoreOfflineEnumDriverPackageA` | `0xC1050` | 372 | UnwindData |  |
| 42 | `DriverStoreOfflineEnumDriverPackageW` | `0xC11D0` | 283 | UnwindData |  |
| 43 | `DriverStoreOfflineFindDriverPackageA` | `0xC1300` | 520 | UnwindData |  |
| 44 | `DriverStoreOfflineFindDriverPackageW` | `0xC1510` | 376 | UnwindData |  |
| 49 | `DriverStoreRunDllW` | `0xC4F00` | 375 | UnwindData |  |
| 29 | `DriverStoreEnumRelatedDriversW` | `0xC5950` | 480 | UnwindData |  |
| 9 | `DriverPackageEnumFileSignatureAttributesW` | `0xE1450` | 185 | UnwindData |  |
