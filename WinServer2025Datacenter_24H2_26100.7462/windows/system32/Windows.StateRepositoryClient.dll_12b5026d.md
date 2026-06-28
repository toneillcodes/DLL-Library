# Binary Specification: Windows.StateRepositoryClient.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Windows.StateRepositoryClient.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `12b5026d009a1e8d5f12dd1de6e8cb6b7579a91f6eb8a33849d1c6e04f1ab7bd`
* **Total Exported Functions:** 52

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllCanUnloadNow` | `0x8990` | 65 | UnwindData |  |
| 3 | `DllGetActivationFactory` | `0x89E0` | 45 | UnwindData |  |
| 4 | `DllGetClassObject` | `0x8A20` | 171 | UnwindData |  |
| 1 | `SRGetExternalLocation` | `0xC2F0` | 714 | UnwindData |  |
| 5 | `SRAddOrUpdateUupProduct` | `0xCAB0` | 1,404 | UnwindData |  |
| 10 | `SRCacheCheckIntegrity` | `0xD040` | 436 | UnwindData |  |
| 11 | `SRCheckIntegrity` | `0xD200` | 26 | UnwindData |  |
| 12 | `SRCheckIntegrity2` | `0xD220` | 567 | UnwindData |  |
| 14 | `SRDictionaryFree` | `0xD460` | 20 | UnwindData |  |
| 15 | `SRDictionaryToPropertySet` | `0xD480` | 54 | UnwindData |  |
| 16 | `SREnsureCacheIsInitialized` | `0xD4C0` | 103 | UnwindData |  |
| 18 | `SRFindPackageFullNamesByUupProductId` | `0xD530` | 929 | UnwindData |  |
| 19 | `SRGetAllPackageFullNamesInUupProducts` | `0xD8E0` | 868 | UnwindData |  |
| 20 | `SRGetAllUupProductsForPackageFullName` | `0xDC50` | 895 | UnwindData |  |
| 24 | `SRGetIsEffectiveSupportedUsersMultiple` | `0xDFE0` | 201 | UnwindData |  |
| 26 | `SRGetPackageOriginForUser` | `0xE0B0` | 629 | UnwindData |  |
| 33 | `SRGetStagedPackageOrigin` | `0xE330` | 385 | UnwindData |  |
| 39 | `SRPropertySetToDictionary` | `0xE4C0` | 313 | UnwindData |  |
| 44 | `SRRepair` | `0xE600` | 537 | UnwindData |  |
| 50 | `SRWorkloads_FindIds` | `0xE820` | 5,744 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `SRWorkloads_GetWorkload` | `0xE820` | 5,744 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `SRAddPackageDependency` | `0xFE90` | 721 | UnwindData |  |
| 13 | `SRDeletePackageDependency` | `0x10170` | 236 | UnwindData |  |
| 17 | `SRFindPackageDependency` | `0x10270` | 525 | UnwindData |  |
| 23 | `SRGetIdForPackageDependencyContext` | `0x10490` | 335 | UnwindData |  |
| 25 | `SRGetPackageDependencyInformation` | `0x105F0` | 1,192 | UnwindData |  |
| 30 | `SRGetProcessesUsingPackageDependency` | `0x10AA0` | 453 | UnwindData |  |
| 31 | `SRGetResolvedPackageFullNameForPackageDependency` | `0x10C70` | 304 | UnwindData |  |
| 32 | `SRGetResolvedPackageFullNameForPackageDependency2` | `0x10DB0` | 304 | UnwindData |  |
| 35 | `SRPackageDependencyExistsByUserAndPackageFullName` | `0x10EF0` | 229 | UnwindData |  |
| 40 | `SRRemovePackageDependency` | `0x10FE0` | 160 | UnwindData |  |
| 45 | `SRTryCreatePackageDependency` | `0x11090` | 120 | UnwindData |  |
| 46 | `SRTryCreatePackageDependency2` | `0x11110` | 408 | UnwindData |  |
| 7 | `SRAppExtensionIterator_Close` | `0x13D80` | 22 | UnwindData |  |
| 8 | `SRAppExtensionIterator_GetNext` | `0x13DA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `SRAppExtension_FindByUserAndName` | `0x13DB0` | 344 | UnwindData |  |
| 21 | `SRGetEffectivePackageStatusForUserFromToken` | `0x15050` | 196 | UnwindData |  |
| 22 | `SRGetEffectivePackageStatusForUserSid` | `0x15120` | 258 | UnwindData |  |
| 27 | `SRGetPackageStatus` | `0x15230` | 243 | UnwindData |  |
| 28 | `SRGetPackageStatusForUserFromToken` | `0x15330` | 170 | UnwindData |  |
| 29 | `SRGetPackageStatusForUserSid` | `0x153E0` | 229 | UnwindData |  |
| 34 | `SRImportPackageUserStatus` | `0x154D0` | 454 | UnwindData |  |
| 41 | `SRRemovePackageStatus` | `0x156A0` | 282 | UnwindData |  |
| 42 | `SRRemovePackageStatusForUserFromToken` | `0x157C0` | 155 | UnwindData |  |
| 43 | `SRRemovePackageStatusForUserSid` | `0x15870` | 329 | UnwindData |  |
| 47 | `SRUpdatePackageStatus` | `0x159C0` | 282 | UnwindData |  |
| 48 | `SRUpdatePackageStatusForUserFromToken` | `0x15AE0` | 185 | UnwindData |  |
| 49 | `SRUpdatePackageStatusForUserSid` | `0x15BA0` | 342 | UnwindData |  |
| 36 | `SRPkgExtensionIterator_Close` | `0x17120` | 22 | UnwindData |  |
| 37 | `SRPkgExtensionIterator_GetNext` | `0x17140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `SRPkgExtension_FindByUserAndName` | `0x17150` | 344 | UnwindData |  |
| 52 | `StateRepositoryDoMaintenanceTasks` | `0x186C0` | 330 | UnwindData |  |
