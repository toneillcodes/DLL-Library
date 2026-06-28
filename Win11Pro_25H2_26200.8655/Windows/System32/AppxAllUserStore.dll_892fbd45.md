# Binary Specification: AppxAllUserStore.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\AppxAllUserStore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `892fbd45720939fb716af7de8a75593c16fa1af43f085f26ee89a572a8d26692`
* **Total Exported Functions:** 106

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 60 | `IsPackageEndOfLife` | `0x3460` | 157 | UnwindData |  |
| 68 | `IsPackageInUpgradeKey` | `0x4820` | 148 | UnwindData |  |
| 29 | `DidAppSurviveOSUpgradeForUser` | `0x4E10` | 534 | UnwindData |  |
| 37 | `GetAllPackagesToBeInstalledForSetupPhase` | `0xBBB0` | 36 | UnwindData |  |
| 38 | `GetAllPackagesToBeInstalledForUser` | `0xCA30` | 40 | UnwindData |  |
| 61 | `IsPackageFamilyInUninstallBlocklist` | `0xD4A0` | 51 | UnwindData |  |
| 23 | `DeleteAllPackagesFromMainPackageArray` | `0x112D0` | 274 | UnwindData |  |
| 46 | `GetPackageSetupPhase` | `0x129B0` | 111 | UnwindData |  |
| 45 | `GetPackageOverrideSetupPhase` | `0x12BB0` | 346 | UnwindData |  |
| 24 | `DeleteAllPackagesFromPackageArray` | `0x13A60` | 163 | UnwindData |  |
| 100 | `TryGetEndOfLifePackageFullName` | `0x13B10` | 61 | UnwindData |  |
| 91 | `RemoveUpgradePackagesFromRegistryStore` | `0x13D20` | 277 | UnwindData |  |
| 31 | `FamilyMonikerStringToSid` | `0x13E40` | 223 | UnwindData |  |
| 48 | `GetProvisionedSharedPackageContainersFromRegistryStore` | `0x14700` | 189 | UnwindData |  |
| 56 | `IsInboxPackage` | `0x147D0` | 251 | UnwindData |  |
| 58 | `IsNonInboxAllUserPackage` | `0x148E0` | 313 | UnwindData |  |
| 59 | `IsNonInboxAllUserPackageSpecificPackage` | `0x14A20` | 313 | UnwindData |  |
| 75 | `MarkStatusOfMainPackageForUser` | `0x14B60` | 335 | UnwindData |  |
| 76 | `MoveEndOfLifePackageToDeletedStoreExternal` | `0x14CC0` | 385 | UnwindData |  |
| 103 | `UpdatePackageInRegistryStore` | `0x14E50` | 649 | UnwindData |  |
| 90 | `RemoveStatusOfMainPackageForAllUsers` | `0x16D10` | 51 | UnwindData |  |
| 66 | `IsPackageInStagedKey` | `0x16F00` | 51 | UnwindData |  |
| 106 | `UpdateUpgradePackageInRegistryStore` | `0x181B0` | 258 | UnwindData |  |
| 54 | `IsCleanupTaskComplete` | `0x182E0` | 269 | UnwindData |  |
| 41 | `GetAllUpdatedPackages` | `0x19B40` | 1,760 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `GetAllInboxPackages` | `0x1A220` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `DeleteUpdatedPackageKey` | `0x1A3B0` | 42,688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `AddDeprovisionedPackageMarking` | `0x24A70` | 582 | UnwindData |  |
| 2 | `AddDeprovisionedSharedPackageContainerMarking` | `0x24CC0` | 352 | UnwindData |  |
| 3 | `AddDownlevelInstalledPackageToRegistryStore` | `0x24E30` | 259 | UnwindData |  |
| 4 | `AddEndOfLifePackageMarking` | `0x24F40` | 51 | UnwindData |  |
| 5 | `AddEndOfLifePackageMarkingForAllUsers` | `0x24F80` | 51 | UnwindData |  |
| 6 | `AddPackageToPinnedList` | `0x24FC0` | 272 | UnwindData |  |
| 7 | `AddPackageToPreinstalledAppsVolume` | `0x250E0` | 121 | UnwindData |  |
| 8 | `AddPackageToRegistryStore` | `0x25160` | 263 | UnwindData |  |
| 9 | `AddPackageToRegistryStore2` | `0x25270` | 239 | UnwindData |  |
| 10 | `AddSharedPackageContainerToRegistryStore` | `0x25370` | 201 | UnwindData |  |
| 11 | `AddStagedPackageToPreinstalledAppsVolume` | `0x25440` | 189 | UnwindData |  |
| 12 | `AddStagedPackageToRegistryStore` | `0x25510` | 206 | UnwindData |  |
| 13 | `AddUpgradePackageAndStubPreferenceToPreinstalledVolume` | `0x255F0` | 271 | UnwindData |  |
| 14 | `AddUpgradePackageToPreinstalledVolume` | `0x25710` | 277 | UnwindData |  |
| 15 | `AddUpgradePackageToRegistryStore` | `0x25830` | 227 | UnwindData |  |
| 16 | `ApplyFrameworkPackageRootFolderACLs` | `0x25920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `ApplyPackageRootFolderACLs` | `0x25930` | 341 | UnwindData |  |
| 18 | `ApplySharedFileACLs` | `0x25A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `CheckPackagePreinstallPolicy` | `0x25AA0` | 237 | UnwindData |  |
| 20 | `CleanupPreinstalledPackageForRemoval` | `0x25BA0` | 57 | UnwindData |  |
| 21 | `CommitTakeOwnershipSession` | `0x25BE0` | 20 | UnwindData |  |
| 22 | `DeleteAllContainersFromContainerArray` | `0x25C00` | 224 | UnwindData |  |
| 25 | `DeletePackageFamiliesArray` | `0x25CF0` | 111 | UnwindData |  |
| 26 | `DeletePackageInfo` | `0x25D70` | 95 | UnwindData |  |
| 28 | `DeleteUserRegistryKeyFromAllUserStore` | `0x25DE0` | 173 | UnwindData |  |
| 30 | `DoesPerUserStoreExist` | `0x25EA0` | 190 | UnwindData |  |
| 32 | `FindExistingVersionInRegistryStore` | `0x25F70` | 92 | UnwindData |  |
| 33 | `FindFullNameForFamilyNameInAppxAllUserStore` | `0x25FE0` | 77 | UnwindData |  |
| 34 | `FixPreInstalledAppxAllUserStoreIntegrity` | `0x26040` | 55 | UnwindData |  |
| 36 | `GetAllNonInboxPackagesFromRegistryStore` | `0x26080` | 189 | UnwindData |  |
| 39 | `GetAllPinnedPackages` | `0x26150` | 507 | UnwindData |  |
| 40 | `GetAllStagedPackagesForMainPackageFromRegistryStore` | `0x26360` | 215 | UnwindData |  |
| 42 | `GetAppxProvisionFactory` | `0x26440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `GetFoldersToKeepForPBR` | `0x26450` | 197 | UnwindData |  |
| 44 | `GetOptionalPackageInfoForPackage` | `0x26520` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `GetPackagesThatMayNeedPreinstallPackageStatusMarked` | `0x26550` | 37 | UnwindData |  |
| 49 | `GetRegionExcludedPreinstalledPackages` | `0x26580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `GetStatusOfPackageFamilyForUser` | `0x26590` | 397 | UnwindData |  |
| 51 | `GetUpgradePackageVolumeKey` | `0x26730` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `HasCentennial` | `0x26750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `HasStagedPackages` | `0x26760` | 506 | UnwindData |  |
| 55 | `IsEnterprisePolicyEnabled` | `0x26960` | 60 | UnwindData |  |
| 57 | `IsInboxPackageAndPath` | `0x269B0` | 82 | UnwindData |  |
| 62 | `IsPackageFamilyInUninstallBlocklistByPackageFullName` | `0x26A10` | 128 | UnwindData |  |
| 63 | `IsPackageFamilyOnPreInstalledDeletedKey` | `0x26AA0` | 84 | UnwindData |  |
| 64 | `IsPackageInDownlevelInstalledKey` | `0x26B00` | 69 | UnwindData |  |
| 65 | `IsPackageInEndOfLifeKey` | `0x26B50` | 140 | UnwindData |  |
| 67 | `IsPackageInUpdatedApplicationsKey` | `0x26BF0` | 246 | UnwindData |  |
| 69 | `IsPackageInUsersUpgradeKey` | `0x26CF0` | 133 | UnwindData |  |
| 70 | `IsPackageNeedingPreregister` | `0x26D80` | 246 | UnwindData |  |
| 71 | `IsPackageOnPreinstalledVolume` | `0x26E80` | 255 | UnwindData |  |
| 72 | `IsPackagePinned` | `0x26F90` | 246 | UnwindData |  |
| 73 | `IsSystemInAuditBoot` | `0x27090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `MarkPackageAsRequiringAllUserStoreRefresh` | `0x270A0` | 72 | UnwindData |  |
| 78 | `PackageIdBasicFromFullName` | `0x27150` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `PackageSidToPackageCapabilitySid` | `0x27160` | 170 | UnwindData |  |
| 80 | `RemoveDeprovisionedPackageMarking` | `0x27210` | 464 | UnwindData |  |
| 81 | `RemoveDeprovisionedSharedPackageContainerMarking` | `0x273F0` | 321 | UnwindData |  |
| 82 | `RemoveDownlevelInstalledPackagesFromRegistryStore` | `0x27540` | 244 | UnwindData |  |
| 83 | `RemoveEndOfLifePackageMarkingForAllUsers` | `0x27640` | 51 | UnwindData |  |
| 84 | `RemoveInboxInstalledStatusOfPackageForUser` | `0x27680` | 160 | UnwindData |  |
| 85 | `RemovePackageFromPinnedList` | `0x27730` | 274 | UnwindData |  |
| 86 | `RemovePackageFromRegistryStore` | `0x27850` | 229 | UnwindData |  |
| 87 | `RemovePackageFromRegistryStoreConfigIfExists` | `0x27940` | 339 | UnwindData |  |
| 88 | `RemoveSharedPackageContainerFromRegistryStore` | `0x27AA0` | 194 | UnwindData |  |
| 89 | `RemoveStagedPackageFromRegistryStore` | `0x27B70` | 213 | UnwindData |  |
| 92 | `RestoreDownlevelAllUserStore` | `0x27C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `RollbackTakeOwnershipSession` | `0x27C70` | 177 | UnwindData |  |
| 94 | `SetAllUserStorePathForTest` | `0x27D30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `SetPackageOverrideSetupPhase` | `0x27D50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `SetPreinstalledRegionPolicyChecked` | `0x27D60` | 245 | UnwindData |  |
| 97 | `SetTargetOsVersionOnPreinstalledVolume` | `0x27E60` | 146 | UnwindData |  |
| 98 | `TakeOwnershipOnFolder` | `0x27F00` | 310 | UnwindData |  |
| 99 | `TryGetDownlevelInstalledPackageFullName` | `0x28040` | 61 | UnwindData |  |
| 101 | `TryGetExternalLocationForFullNameInAppxAllUserStore` | `0x28090` | 161 | UnwindData |  |
| 102 | `UpdateFrameworkPackageInRegistryStore` | `0x28140` | 216 | UnwindData |  |
| 104 | `UpdatePackageInRegistryStore2` | `0x28220` | 664 | UnwindData |  |
| 105 | `UpdatePackageSetupPhase` | `0x284C0` | 430 | UnwindData |  |
| 77 | `PackageFamilyNameFromId` | `0x3F790` | 47,692 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
