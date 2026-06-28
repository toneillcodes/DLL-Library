# Binary Specification: AppxAllUserStore.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\AppxAllUserStore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f2d58abcbffbba61800ab1e696311b335d4c81122c497c33b119777ade792a7a`
* **Total Exported Functions:** 103

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 37 | `GetAllPackagesToBeInstalledForUser` | `0x2660` | 40 | UnwindData |  |
| 36 | `GetAllPackagesToBeInstalledForSetupPhase` | `0x2690` | 36 | UnwindData |  |
| 74 | `MarkStatusOfMainPackageForUser` | `0x3310` | 418 | UnwindData |  |
| 59 | `IsPackageEndOfLife` | `0x3E10` | 157 | UnwindData |  |
| 67 | `IsPackageInUpgradeKey` | `0x5320` | 148 | UnwindData |  |
| 28 | `DidAppSurviveOSUpgradeForUser` | `0x59B0` | 534 | UnwindData |  |
| 60 | `IsPackageFamilyInUninstallBlocklist` | `0xEF40` | 51 | UnwindData |  |
| 22 | `DeleteAllPackagesFromMainPackageArray` | `0x13150` | 274 | UnwindData |  |
| 45 | `GetPackageSetupPhase` | `0x14B40` | 111 | UnwindData |  |
| 44 | `GetPackageOverrideSetupPhase` | `0x14D40` | 346 | UnwindData |  |
| 101 | `UpdatePackageInRegistryStore` | `0x153D0` | 586 | UnwindData |  |
| 23 | `DeleteAllPackagesFromPackageArray` | `0x15EC0` | 163 | UnwindData |  |
| 99 | `TryGetEndOfLifePackageFullName` | `0x15F70` | 61 | UnwindData |  |
| 90 | `RemoveUpgradePackagesFromRegistryStore` | `0x16180` | 277 | UnwindData |  |
| 30 | `FamilyMonikerStringToSid` | `0x162A0` | 223 | UnwindData |  |
| 47 | `GetProvisionedSharedPackageContainersFromRegistryStore` | `0x16680` | 189 | UnwindData |  |
| 55 | `IsInboxPackage` | `0x16750` | 275 | UnwindData |  |
| 57 | `IsNonInboxAllUserPackage` | `0x16870` | 334 | UnwindData |  |
| 58 | `IsNonInboxAllUserPackageSpecificPackage` | `0x169D0` | 334 | UnwindData |  |
| 75 | `MoveEndOfLifePackageToDeletedStoreExternal` | `0x16B30` | 385 | UnwindData |  |
| 89 | `RemoveStatusOfMainPackageForAllUsers` | `0x183A0` | 51 | UnwindData |  |
| 65 | `IsPackageInStagedKey` | `0x18590` | 51 | UnwindData |  |
| 103 | `UpdateUpgradePackageInRegistryStore` | `0x19840` | 258 | UnwindData |  |
| 53 | `IsCleanupTaskComplete` | `0x19970` | 269 | UnwindData |  |
| 40 | `GetAllUpdatedPackages` | `0x1B1D0` | 2,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `GetAllInboxPackages` | `0x1BAA0` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `DeleteUpdatedPackageKey` | `0x1BCA0` | 32,864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `AddDeprovisionedPackageMarking` | `0x23D00` | 582 | UnwindData |  |
| 2 | `AddDeprovisionedSharedPackageContainerMarking` | `0x23F50` | 352 | UnwindData |  |
| 3 | `AddDownlevelInstalledPackageToRegistryStore` | `0x240C0` | 259 | UnwindData |  |
| 4 | `AddEndOfLifePackageMarking` | `0x241D0` | 51 | UnwindData |  |
| 5 | `AddEndOfLifePackageMarkingForAllUsers` | `0x24210` | 51 | UnwindData |  |
| 6 | `AddPackageToPinnedList` | `0x24250` | 272 | UnwindData |  |
| 7 | `AddPackageToPreinstalledAppsVolume` | `0x24370` | 121 | UnwindData |  |
| 8 | `AddPackageToRegistryStore` | `0x243F0` | 201 | UnwindData |  |
| 9 | `AddSharedPackageContainerToRegistryStore` | `0x244C0` | 201 | UnwindData |  |
| 10 | `AddStagedPackageToPreinstalledAppsVolume` | `0x24590` | 189 | UnwindData |  |
| 11 | `AddStagedPackageToRegistryStore` | `0x24660` | 206 | UnwindData |  |
| 12 | `AddUpgradePackageAndStubPreferenceToPreinstalledVolume` | `0x24740` | 271 | UnwindData |  |
| 13 | `AddUpgradePackageToPreinstalledVolume` | `0x24860` | 277 | UnwindData |  |
| 14 | `AddUpgradePackageToRegistryStore` | `0x24980` | 227 | UnwindData |  |
| 15 | `ApplyFrameworkPackageRootFolderACLs` | `0x24A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `ApplyPackageRootFolderACLs` | `0x24A80` | 341 | UnwindData |  |
| 17 | `ApplySharedFileACLs` | `0x24BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `CheckPackagePreinstallPolicy` | `0x24BF0` | 237 | UnwindData |  |
| 19 | `CleanupPreinstalledPackageForRemoval` | `0x24CF0` | 57 | UnwindData |  |
| 20 | `CommitTakeOwnershipSession` | `0x24D30` | 20 | UnwindData |  |
| 21 | `DeleteAllContainersFromContainerArray` | `0x24D50` | 224 | UnwindData |  |
| 24 | `DeletePackageFamiliesArray` | `0x24E40` | 111 | UnwindData |  |
| 25 | `DeletePackageInfo` | `0x24EC0` | 95 | UnwindData |  |
| 27 | `DeleteUserRegistryKeyFromAllUserStore` | `0x24F30` | 173 | UnwindData |  |
| 29 | `DoesPerUserStoreExist` | `0x24FF0` | 190 | UnwindData |  |
| 31 | `FindExistingVersionInRegistryStore` | `0x250C0` | 92 | UnwindData |  |
| 32 | `FindFullNameForFamilyNameInAppxAllUserStore` | `0x25130` | 77 | UnwindData |  |
| 33 | `FixPreInstalledAppxAllUserStoreIntegrity` | `0x25190` | 55 | UnwindData |  |
| 35 | `GetAllNonInboxPackagesFromRegistryStore` | `0x251D0` | 189 | UnwindData |  |
| 38 | `GetAllPinnedPackages` | `0x252A0` | 507 | UnwindData |  |
| 39 | `GetAllStagedPackagesForMainPackageFromRegistryStore` | `0x254B0` | 215 | UnwindData |  |
| 41 | `GetAppxProvisionFactory` | `0x25590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `GetFoldersToKeepForPBR` | `0x255A0` | 197 | UnwindData |  |
| 43 | `GetOptionalPackageInfoForPackage` | `0x25670` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `GetPackagesThatMayNeedPreinstallPackageStatusMarked` | `0x256A0` | 37 | UnwindData |  |
| 48 | `GetRegionExcludedPreinstalledPackages` | `0x256D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `GetStatusOfPackageFamilyForUser` | `0x256E0` | 433 | UnwindData |  |
| 50 | `GetUpgradePackageVolumeKey` | `0x258A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `HasCentennial` | `0x258C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `HasStagedPackages` | `0x258D0` | 506 | UnwindData |  |
| 54 | `IsEnterprisePolicyEnabled` | `0x25AD0` | 60 | UnwindData |  |
| 56 | `IsInboxPackageAndPath` | `0x25B20` | 82 | UnwindData |  |
| 61 | `IsPackageFamilyInUninstallBlocklistByPackageFullName` | `0x25B80` | 128 | UnwindData |  |
| 62 | `IsPackageFamilyOnPreInstalledDeletedKey` | `0x25C10` | 84 | UnwindData |  |
| 63 | `IsPackageInDownlevelInstalledKey` | `0x25C70` | 69 | UnwindData |  |
| 64 | `IsPackageInEndOfLifeKey` | `0x25CC0` | 140 | UnwindData |  |
| 66 | `IsPackageInUpdatedApplicationsKey` | `0x25D60` | 246 | UnwindData |  |
| 68 | `IsPackageInUsersUpgradeKey` | `0x25E60` | 133 | UnwindData |  |
| 69 | `IsPackageNeedingPreregister` | `0x25EF0` | 246 | UnwindData |  |
| 70 | `IsPackageOnPreinstalledVolume` | `0x25FF0` | 279 | UnwindData |  |
| 71 | `IsPackagePinned` | `0x26110` | 246 | UnwindData |  |
| 72 | `IsSystemInAuditBoot` | `0x26210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `MarkPackageAsRequiringAllUserStoreRefresh` | `0x26220` | 72 | UnwindData |  |
| 77 | `PackageIdBasicFromFullName` | `0x262D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `PackageSidToPackageCapabilitySid` | `0x262E0` | 170 | UnwindData |  |
| 79 | `RemoveDeprovisionedPackageMarking` | `0x26390` | 464 | UnwindData |  |
| 80 | `RemoveDeprovisionedSharedPackageContainerMarking` | `0x26570` | 321 | UnwindData |  |
| 81 | `RemoveDownlevelInstalledPackagesFromRegistryStore` | `0x266C0` | 244 | UnwindData |  |
| 82 | `RemoveEndOfLifePackageMarkingForAllUsers` | `0x267C0` | 51 | UnwindData |  |
| 83 | `RemoveInboxInstalledStatusOfPackageForUser` | `0x26800` | 160 | UnwindData |  |
| 84 | `RemovePackageFromPinnedList` | `0x268B0` | 274 | UnwindData |  |
| 85 | `RemovePackageFromRegistryStore` | `0x269D0` | 229 | UnwindData |  |
| 86 | `RemovePackageFromRegistryStoreConfigIfExists` | `0x26AC0` | 339 | UnwindData |  |
| 87 | `RemoveSharedPackageContainerFromRegistryStore` | `0x26C20` | 194 | UnwindData |  |
| 88 | `RemoveStagedPackageFromRegistryStore` | `0x26CF0` | 213 | UnwindData |  |
| 91 | `RestoreDownlevelAllUserStore` | `0x26DD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `RollbackTakeOwnershipSession` | `0x26DF0` | 177 | UnwindData |  |
| 93 | `SetAllUserStorePathForTest` | `0x26EB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `SetPackageOverrideSetupPhase` | `0x26ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `SetPreinstalledRegionPolicyChecked` | `0x26EE0` | 245 | UnwindData |  |
| 96 | `SetTargetOsVersionOnPreinstalledVolume` | `0x26FE0` | 146 | UnwindData |  |
| 97 | `TakeOwnershipOnFolder` | `0x27080` | 310 | UnwindData |  |
| 98 | `TryGetDownlevelInstalledPackageFullName` | `0x271C0` | 61 | UnwindData |  |
| 100 | `UpdateFrameworkPackageInRegistryStore` | `0x27210` | 216 | UnwindData |  |
| 102 | `UpdatePackageSetupPhase` | `0x272F0` | 430 | UnwindData |  |
| 76 | `PackageFamilyNameFromId` | `0x3E840` | 48,348 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
