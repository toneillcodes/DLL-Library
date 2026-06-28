# Binary Specification: drvstore.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\drvstore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9984d170f23d774926d6d0c0c2732401cfe694437c45db9f73697b958068a16d`
* **Total Exported Functions:** 62

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 33 | `DriverStoreGetObjectPropertyW` | `0x17CA0` | 2,012 | UnwindData |  |
| 8 | `DriverPackageEnumEventProvidersW` | `0x2AAB0` | 501 | UnwindData |  |
| 11 | `DriverPackageEnumFiltersW` | `0x2ACB0` | 473 | UnwindData |  |
| 7 | `DriverPackageEnumEventAutoLoggersW` | `0x2B400` | 499 | UnwindData |  |
| 14 | `DriverPackageEnumPropertiesW` | `0x2C250` | 494 | UnwindData |  |
| 12 | `DriverPackageEnumInterfacesW` | `0x2C450` | 500 | UnwindData |  |
| 15 | `DriverPackageEnumRegKeysW` | `0x2D030` | 530 | UnwindData |  |
| 10 | `DriverPackageEnumFilesW` | `0x2D620` | 850 | UnwindData |  |
| 16 | `DriverPackageEnumServicesW` | `0x2DA50` | 500 | UnwindData |  |
| 6 | `DriverPackageEnumDriversW` | `0x2DF40` | 885 | UnwindData |  |
| 19 | `DriverPackageGetVersionInfoW` | `0x508A0` | 673 | UnwindData |  |
| 20 | `DriverPackageOpenW` | `0x50F90` | 30 | UnwindData |  |
| 18 | `DriverPackageGetPropertyW` | `0x51460` | 3,826 | UnwindData |  |
| 1 | `DriverPackageClose` | `0x52360` | 71 | UnwindData |  |
| 62 | `pServerImportDriverPackage` | `0x52E10` | 715 | UnwindData |  |
| 30 | `DriverStoreEnumW` | `0x53130` | 364 | UnwindData |  |
| 26 | `DriverStoreEnumDeviceDriversW` | `0x532B0` | 338 | UnwindData |  |
| 31 | `DriverStoreFindW` | `0x53410` | 399 | UnwindData |  |
| 21 | `DriverStoreClose` | `0x535B0` | 286 | UnwindData |  |
| 45 | `DriverStoreOpenW` | `0x53720` | 1,990 | UnwindData |  |
| 52 | `DriverStoreSetObjectPropertyW` | `0x76BE0` | 394 | UnwindData |  |
| 5 | `DriverPackageEnumDevicesW` | `0x7B1E0` | 680 | UnwindData |  |
| 51 | `DriverStoreSetLogContext` | `0x7C190` | 36 | UnwindData |  |
| 28 | `DriverStoreEnumObjectsW` | `0x7C220` | 357 | UnwindData |  |
| 17 | `DriverPackageEnumSoftwareW` | `0x7C4E0` | 489 | UnwindData |  |
| 2 | `DriverPackageEnumClassesW` | `0x7CB40` | 760 | UnwindData |  |
| 61 | `pServerDeleteDriverPackage` | `0x7F550` | 582 | UnwindData |  |
| 22 | `DriverStoreConfigureW` | `0x81AB0` | 10,848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DriverPackageEnumConfigurationsW` | `0x84510` | 455 | UnwindData |  |
| 48 | `DriverStoreReflectW` | `0x846F0` | 200 | UnwindData |  |
| 3 | `DriverPackageEnumComponentsW` | `0x84950` | 489 | UnwindData |  |
| 25 | `DriverStoreDriverPackageResolveCallbackW` | `0x88210` | 1,457 | UnwindData |  |
| 46 | `DriverStorePublishW` | `0x8A080` | 1,930 | UnwindData |  |
| 56 | `DriverStoreUnpublishW` | `0x8A810` | 1,555 | UnwindData |  |
| 13 | `DriverPackageEnumOsVersionsW` | `0x9EE70` | 166 | UnwindData |  |
| 35 | `DriverStoreImportW` | `0x9F7E0` | 1,581 | UnwindData |  |
| 34 | `DriverStoreGetParameter` | `0xAA960` | 1,727 | UnwindData |  |
| 53 | `DriverStoreSetParameter` | `0xAB190` | 737 | UnwindData |  |
| 24 | `DriverStoreDeleteW` | `0xACF70` | 1,064 | UnwindData |  |
| 23 | `DriverStoreCopyW` | `0xAD3A0` | 1,197 | UnwindData |  |
| 27 | `DriverStoreEnumNodesW` | `0xADE80` | 351 | UnwindData |  |
| 36 | `DriverStoreMountNodeW` | `0xADFF0` | 350 | UnwindData |  |
| 50 | `DriverStoreSelectNodeW` | `0xAE160` | 221 | UnwindData |  |
| 55 | `DriverStoreUnmountNodeW` | `0xAE250` | 188 | UnwindData |  |
| 32 | `DriverStoreGetObjectPropertyKeysW` | `0xAE320` | 369 | UnwindData |  |
| 47 | `DriverStoreReflectCriticalW` | `0xB66D0` | 64 | UnwindData |  |
| 57 | `DriverStoreUnreflectCriticalW` | `0xB6720` | 98 | UnwindData |  |
| 58 | `DriverStoreUnreflectW` | `0xB6790` | 200 | UnwindData |  |
| 54 | `DriverStoreUnconfigureW` | `0xB8850` | 10,272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `DriverStoreUpdateDevicesW` | `0xBB070` | 1,383 | UnwindData |  |
| 60 | `DriverStoreVerifyIntegrityW` | `0xBE6B0` | 1,242 | UnwindData |  |
| 37 | `DriverStoreOfflineAddDriverPackageA` | `0xC2CD0` | 710 | UnwindData |  |
| 38 | `DriverStoreOfflineAddDriverPackageW` | `0xC2FA0` | 988 | UnwindData |  |
| 39 | `DriverStoreOfflineDeleteDriverPackageA` | `0xC3390` | 279 | UnwindData |  |
| 40 | `DriverStoreOfflineDeleteDriverPackageW` | `0xC34B0` | 442 | UnwindData |  |
| 41 | `DriverStoreOfflineEnumDriverPackageA` | `0xC3670` | 372 | UnwindData |  |
| 42 | `DriverStoreOfflineEnumDriverPackageW` | `0xC37F0` | 283 | UnwindData |  |
| 43 | `DriverStoreOfflineFindDriverPackageA` | `0xC3920` | 520 | UnwindData |  |
| 44 | `DriverStoreOfflineFindDriverPackageW` | `0xC3B30` | 376 | UnwindData |  |
| 49 | `DriverStoreRunDllW` | `0xC7520` | 375 | UnwindData |  |
| 29 | `DriverStoreEnumRelatedDriversW` | `0xC7F70` | 480 | UnwindData |  |
| 9 | `DriverPackageEnumFileSignatureAttributesW` | `0xE3EC0` | 185 | UnwindData |  |
