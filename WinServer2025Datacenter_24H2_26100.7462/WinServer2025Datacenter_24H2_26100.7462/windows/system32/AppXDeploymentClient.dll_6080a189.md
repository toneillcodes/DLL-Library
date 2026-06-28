# Binary Specification: AppXDeploymentClient.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\AppXDeploymentClient.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6080a1893e4953e76699a012185d58aae05ea311ce2aa215b6c01be8fef2d4b8`
* **Total Exported Functions:** 108

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 23 | `RegisterNotification` | `0x46A0` | 28 | UnwindData |  |
| 24 | `UnregisterNotification` | `0x46D0` | 28 | UnwindData |  |
| 39 | `RegisterNotificationForUser` | `0x4BA0` | 180 | UnwindData |  |
| 40 | `UnregisterNotificationForUser` | `0x4F60` | 176 | UnwindData |  |
| 65 | `GetMetadataRootForPackage` | `0xAE10` | 2,655 | UnwindData |  |
| 41 | `GetNotificationPayloadForUser` | `0xE120` | 110 | UnwindData |  |
| 49 | `GetApplicability5` | `0xFDF0` | 676 | UnwindData |  |
| 44 | `EnsurePackageFamilyIsRegisteredBeforeActivation` | `0x14670` | 809 | UnwindData |  |
| 68 | `GetPackageRegistrationStatusForUserAndDefaultAccount` | `0x183F0` | 152 | UnwindData |  |
| 58 | `GetPackageRegistrationStatusForUser` | `0x1A020` | 53 | UnwindData |  |
| 77 | `DllCanUnloadNow` | `0x27690` | 377 | UnwindData |  |
| 106 | `DllGetClassObject` | `0x28050` | 122 | UnwindData |  |
| 105 | `DllGetActivationFactory` | `0x28890` | 1,105 | UnwindData |  |
| 50 | `DeleteApplicabilityInfoArray` | `0x29770` | 144 | UnwindData |  |
| 29 | `AppxValidatePackagesWithOptions` | `0x2B3C0` | 1,117 | UnwindData |  |
| 59 | `IsSharedAppsEnabled` | `0x2C1C0` | 185 | UnwindData |  |
| 67 | `ClientDeleteAllPackagesFromMainPackageArray` | `0x31870` | 283 | UnwindData |  |
| 47 | `CheckComCallerHasCapabilities` | `0x31B60` | 35 | UnwindData |  |
| 26 | `NotifyPackageStatusChanged` | `0x31F60` | 134 | UnwindData |  |
| 66 | `ClientGetAllPackagesToBeInstalledForUser` | `0x32530` | 158 | UnwindData |  |
| 2 | `GetApplicability` | `0x37380` | 120,496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `AppxAddPackageToAllUserStoreForPbr` | `0x54A30` | 116,688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `AppxPackageRepositoryRecoverStagedPackages` | `0x54A30` | 116,688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `AppxPackageRepositoryRecoverUserInstalls` | `0x54A30` | 116,688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `AppxRecoverUserInstallsForUpgrade` | `0x54A30` | 116,688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `FixJunctionsForAppsIfNecessary` | `0x54A30` | 116,688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `GetApplicability2` | `0x54A30` | 116,688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `GetApplicability4` | `0x54A30` | 116,688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | *Ordinal Only* | `0x71200` | 363 | UnwindData |  |
| 95 | `MsixIsPackageFeatureSupported` | `0x79180` | 157 | UnwindData |  |
| 93 | `MsixIsPackageRegisteredOrNewerAvailable` | `0x79230` | 545 | UnwindData |  |
| 102 | `MsixIsPayloadFileStaged` | `0x79460` | 1,043 | UnwindData |  |
| 60 | `AppInstallerUpdateAllTask` | `0x7AF80` | 38 | UnwindData |  |
| 46 | `AppxCleanupOrphanPackages` | `0x7AFB0` | 53 | UnwindData |  |
| 45 | `AppxCleanupSystemAppsMigratedToFOD` | `0x7AFF0` | 1,444 | UnwindData |  |
| 42 | `AppxCleanupWCIReparsePoints` | `0x7B5A0` | 178 | UnwindData |  |
| 3 | `AppxCreateSharedLocalFolder` | `0x7B660` | 71 | UnwindData |  |
| 15 | `AppxCreateSharedLocalFolderForFamilyName` | `0x7B6B0` | 71 | UnwindData |  |
| 7 | `AppxDeletePackageFiles` | `0x7B700` | 149 | UnwindData |  |
| 19 | `AppxDestagePackage` | `0x7B7A0` | 1,149 | UnwindData |  |
| 70 | `AppxDoesSharedLocalFolderExistForFamilyName` | `0x7BC30` | 349 | UnwindData |  |
| 18 | `AppxGetPackageInstalledLocation` | `0x7BDA0` | 701 | UnwindData |  |
| 21 | `AppxGetStagedPackageFullNameFromFamilyName` | `0x7C070` | 1,813 | UnwindData |  |
| 22 | `AppxIsStagedPackageStoreSigned` | `0x7C790` | 312 | UnwindData |  |
| 28 | `AppxPreRegisterAllInboxPackages` | `0x7C8D0` | 201 | UnwindData |  |
| 12 | `AppxPreRegisterPackage` | `0x7C9A0` | 257 | UnwindData |  |
| 11 | `AppxPreStageCleanupRunTask` | `0x7CAB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `AppxRegisterPackage` | `0x7CAC0` | 349 | UnwindData |  |
| 74 | `AppxRemoveAllPackagesForUserSid` | `0x7CC30` | 907 | UnwindData |  |
| 30 | `AppxRemovePackageForAllUsers` | `0x7CFD0` | 431 | UnwindData |  |
| 37 | `AppxRemovePackageForUserSid` | `0x7D190` | 1,883 | UnwindData |  |
| 8 | `AppxRequestRemovePackageForUser` | `0x7D900` | 61 | UnwindData |  |
| 78 | `AppxResetPackage` | `0x7D950` | 496 | UnwindData |  |
| 17 | `AppxStagePackage` | `0x7DB50` | 2,304 | UnwindData |  |
| 85 | `AppxSvcPrepareForSysprepGeneralize` | `0x7E460` | 55 | UnwindData |  |
| 71 | `AppxValidatePackages` | `0x7E4A0` | 20 | UnwindData |  |
| 61 | `CheckAppInstallerUpdateAvailability` | `0x7E4C0` | 111 | UnwindData |  |
| 75 | `CheckForUpdatesAndWaitForInstallerIfNeeded` | `0x7E540` | 346 | UnwindData |  |
| 73 | `CleanupProfileForUser` | `0x7E6A0` | 320 | UnwindData |  |
| 94 | `ClientExistsAnyPackageToBeInstalledForUser` | `0x7E7F0` | 278 | UnwindData |  |
| 38 | `CreateCanonicalPriFile` | `0x7E910` | 159 | UnwindData |  |
| 81 | `DeleteAutoUpdateSettings` | `0x7E9C0` | 76 | UnwindData |  |
| 100 | `ExistPackagesPendingDeferredRemovalForUser` | `0x7EA20` | 147 | UnwindData |  |
| 99 | `FreeApplicationSecret` | `0x7EAC0` | 17 | UnwindData |  |
| 16 | *Ordinal Only* | `0x7EAE0` | 76 | UnwindData |  |
| 34 | `GeneratePreInstalledPriFiles` | `0x7EB40` | 93 | UnwindData |  |
| 96 | `GetApplicationSecret` | `0x7EBB0` | 93 | UnwindData |  |
| 48 | `GetBundleApplicablePackages` | `0x7EC20` | 2,878 | UnwindData |  |
| 25 | `GetNotificationPayload` | `0x7F770` | 53 | UnwindData |  |
| 72 | `HasPackageFamilyBeenRegisteredForUser` | `0x7F7B0` | 581 | UnwindData |  |
| 9 | `IsPackageInstalled` | `0x7FA00` | 128 | UnwindData |  |
| 64 | `IsPackageMetadataUnderSystemMetadata` | `0x7FA90` | 61 | UnwindData |  |
| 84 | `MSIXForceReRegisterPackage` | `0x7FAE0` | 475 | UnwindData |  |
| 107 | `MsixAppxAllUserStoreIsInboxPackage` | `0x7FD60` | 380 | UnwindData |  |
| 108 | `MsixEnsurePackageIsRegistered` | `0x7FEF0` | 212 | UnwindData |  |
| 104 | `MsixGetOutdatedPackagesForUser` | `0x7FFD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `MsixIsPackageRegistrationPending` | `0x7FFE0` | 414 | UnwindData |  |
| 86 | `MsixPackageVolumeIsRepairNeeded` | `0x80190` | 60 | UnwindData |  |
| 87 | `MsixPackageVolumeRepair` | `0x801E0` | 62 | UnwindData |  |
| 103 | `MsixPreRegisterPackagesIfNeeded` | `0x80230` | 640 | UnwindData |  |
| 92 | `MsixPreRegisterUupProducts` | `0x804C0` | 519 | UnwindData |  |
| 91 | `MsixRemovePackageByUriAsync` | `0x806D0` | 289 | UnwindData |  |
| 90 | `MsixRepairPackageAsync` | `0x80800` | 329 | UnwindData |  |
| 89 | `MsixResetPackageAsync` | `0x80950` | 329 | UnwindData |  |
| 82 | `PauseAutoUpdateSettings` | `0x80AA0` | 87 | UnwindData |  |
| 35 | `PopulateProtocolAndFTA` | `0x80B00` | 250 | UnwindData |  |
| 10 | `RDSRecoverRequests` | `0x80C00` | 167 | UnwindData |  |
| 13 | `ReArmAppxPreStageCleanupTask` | `0x80CB0` | 19 | UnwindData |  |
| 101 | `RemoveDeferredPackages` | `0x80CD0` | 285 | UnwindData |  |
| 43 | `RepairPackageFileAcls` | `0x80E00` | 100 | UnwindData |  |
| 31 | `RequestContentGroups` | `0x80E70` | 82 | UnwindData |  |
| 33 | `RequestContentGroupsForFullTrust` | `0x80ED0` | 82 | UnwindData |  |
| 98 | `ResetApplicationSecrets` | `0x80F30` | 51 | UnwindData |  |
| 83 | `ScheduleAppInstallerBackgroundUpdate` | `0x80F70` | 44 | UnwindData |  |
| 97 | `SetApplicationSecret` | `0x80FB0` | 93 | UnwindData |  |
| 53 | `UpdateAgentCancelAllDownloads` | `0x81020` | 51 | UnwindData |  |
| 76 | `UpdateAgentCancelDownload` | `0x81060` | 54 | UnwindData |  |
| 51 | `UpdateAgentCreateDownload` | `0x810A0` | 144 | UnwindData |  |
| 62 | `UpdateAgentFreeDownloadRanges` | `0x81140` | 37 | UnwindData |  |
| 79 | `UpdateAgentGetDownloadPackageReturnValue` | `0x81170` | 105 | UnwindData |  |
| 52 | `UpdateAgentGetDownloadRanges` | `0x811E0` | 71 | UnwindData |  |
| 69 | `UpdateAgentGetDownloadingPackageCount` | `0x81230` | 71 | UnwindData |  |
| 80 | `UpdateAppInstallerSettings` | `0x81280` | 302 | UnwindData |  |
| 55 | `UpdateDataSourceAddRange` | `0x813C0` | 105 | UnwindData |  |
| 57 | `UpdateDataSourceCancelRun` | `0x81430` | 71 | UnwindData |  |
| 54 | `UpdateDataSourceRegister` | `0x81480` | 100 | UnwindData |  |
| 56 | `UpdateDataSourceRun` | `0x814F0` | 71 | UnwindData |  |
| 27 | `VerifyPackage` | `0x81540` | 83 | UnwindData |  |
