# Binary Specification: Windows.StateRepositoryClient.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Windows.StateRepositoryClient.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `880bc374697ef521fd7ef044f9ab4e8d46c78f30cef6f50ad4f6322829afc175`
* **Total Exported Functions:** 52

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllCanUnloadNow` | `0x8910` | 65 | UnwindData |  |
| 3 | `DllGetActivationFactory` | `0x8960` | 45 | UnwindData |  |
| 4 | `DllGetClassObject` | `0x89A0` | 171 | UnwindData |  |
| 1 | `SRGetExternalLocation` | `0xC360` | 714 | UnwindData |  |
| 5 | `SRAddOrUpdateUupProduct` | `0xCBD0` | 1,404 | UnwindData |  |
| 10 | `SRCacheCheckIntegrity` | `0xD160` | 436 | UnwindData |  |
| 11 | `SRCheckIntegrity` | `0xD320` | 26 | UnwindData |  |
| 12 | `SRCheckIntegrity2` | `0xD340` | 567 | UnwindData |  |
| 14 | `SRDictionaryFree` | `0xD580` | 20 | UnwindData |  |
| 15 | `SRDictionaryToPropertySet` | `0xD5A0` | 54 | UnwindData |  |
| 16 | `SREnsureCacheIsInitialized` | `0xD5E0` | 103 | UnwindData |  |
| 18 | `SRFindPackageFullNamesByUupProductId` | `0xD650` | 929 | UnwindData |  |
| 19 | `SRGetAllPackageFullNamesInUupProducts` | `0xDA00` | 868 | UnwindData |  |
| 20 | `SRGetAllUupProductsForPackageFullName` | `0xDD70` | 895 | UnwindData |  |
| 24 | `SRGetIsEffectiveSupportedUsersMultiple` | `0xE100` | 201 | UnwindData |  |
| 26 | `SRGetPackageOriginForUser` | `0xE1D0` | 629 | UnwindData |  |
| 33 | `SRGetStagedPackageOrigin` | `0xE450` | 385 | UnwindData |  |
| 39 | `SRPropertySetToDictionary` | `0xE5E0` | 313 | UnwindData |  |
| 44 | `SRRepair` | `0xE720` | 537 | UnwindData |  |
| 50 | `SRWorkloads_FindIds` | `0xE940` | 3,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `SRWorkloads_GetWorkload` | `0xE940` | 3,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `SRAddPackageDependency` | `0xF5A0` | 584 | UnwindData |  |
| 13 | `SRDeletePackageDependency` | `0xF7F0` | 236 | UnwindData |  |
| 17 | `SRFindPackageDependency` | `0xF8F0` | 525 | UnwindData |  |
| 23 | `SRGetIdForPackageDependencyContext` | `0xFB10` | 335 | UnwindData |  |
| 25 | `SRGetPackageDependencyInformation` | `0xFC70` | 1,192 | UnwindData |  |
| 30 | `SRGetProcessesUsingPackageDependency` | `0x10120` | 453 | UnwindData |  |
| 31 | `SRGetResolvedPackageFullNameForPackageDependency` | `0x102F0` | 304 | UnwindData |  |
| 32 | `SRGetResolvedPackageFullNameForPackageDependency2` | `0x10430` | 304 | UnwindData |  |
| 35 | `SRPackageDependencyExistsByUserAndPackageFullName` | `0x10570` | 229 | UnwindData |  |
| 40 | `SRRemovePackageDependency` | `0x10660` | 160 | UnwindData |  |
| 45 | `SRTryCreatePackageDependency` | `0x10710` | 120 | UnwindData |  |
| 46 | `SRTryCreatePackageDependency2` | `0x10790` | 408 | UnwindData |  |
| 7 | `SRAppExtensionIterator_Close` | `0x134C0` | 22 | UnwindData |  |
| 8 | `SRAppExtensionIterator_GetNext` | `0x134E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `SRAppExtension_FindByUserAndName` | `0x134F0` | 344 | UnwindData |  |
| 21 | `SRGetEffectivePackageStatusForUserFromToken` | `0x14790` | 196 | UnwindData |  |
| 22 | `SRGetEffectivePackageStatusForUserSid` | `0x14860` | 258 | UnwindData |  |
| 27 | `SRGetPackageStatus` | `0x14970` | 243 | UnwindData |  |
| 28 | `SRGetPackageStatusForUserFromToken` | `0x14A70` | 170 | UnwindData |  |
| 29 | `SRGetPackageStatusForUserSid` | `0x14B20` | 229 | UnwindData |  |
| 34 | `SRImportPackageUserStatus` | `0x14C10` | 454 | UnwindData |  |
| 41 | `SRRemovePackageStatus` | `0x14DE0` | 282 | UnwindData |  |
| 42 | `SRRemovePackageStatusForUserFromToken` | `0x14F00` | 155 | UnwindData |  |
| 43 | `SRRemovePackageStatusForUserSid` | `0x14FB0` | 329 | UnwindData |  |
| 47 | `SRUpdatePackageStatus` | `0x15100` | 282 | UnwindData |  |
| 48 | `SRUpdatePackageStatusForUserFromToken` | `0x15220` | 185 | UnwindData |  |
| 49 | `SRUpdatePackageStatusForUserSid` | `0x152E0` | 342 | UnwindData |  |
| 36 | `SRPkgExtensionIterator_Close` | `0x16870` | 22 | UnwindData |  |
| 37 | `SRPkgExtensionIterator_GetNext` | `0x16890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `SRPkgExtension_FindByUserAndName` | `0x168A0` | 344 | UnwindData |  |
| 52 | `StateRepositoryDoMaintenanceTasks` | `0x17B40` | 330 | UnwindData |  |
