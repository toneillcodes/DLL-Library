# Binary Specification: AppXDeploymentClient.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\AppXDeploymentClient.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ad5fd54d6a5642ec0aced5698b986375c3f6b25f423064899fcd63c60a144073`
* **Total Exported Functions:** 109

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 65 | `GetMetadataRootForPackage` | `0x85F0` | 2,671 | UnwindData |  |
| 41 | `GetNotificationPayloadForUser` | `0xB990` | 110 | UnwindData |  |
| 49 | `GetApplicability5` | `0xD660` | 676 | UnwindData |  |
| 23 | `RegisterNotification` | `0x131C0` | 28 | UnwindData |  |
| 24 | `UnregisterNotification` | `0x131F0` | 28 | UnwindData |  |
| 39 | `RegisterNotificationForUser` | `0x136C0` | 180 | UnwindData |  |
| 40 | `UnregisterNotificationForUser` | `0x13A80` | 176 | UnwindData |  |
| 58 | `GetPackageRegistrationStatusForUser` | `0x169D0` | 53 | UnwindData |  |
| 68 | `GetPackageRegistrationStatusForUserAndDefaultAccount` | `0x17BC0` | 113 | UnwindData |  |
| 44 | `EnsurePackageFamilyIsRegisteredBeforeActivation` | `0x1B8B0` | 809 | UnwindData |  |
| 77 | `DllCanUnloadNow` | `0x25CF0` | 377 | UnwindData |  |
| 107 | `DllGetClassObject` | `0x26800` | 122 | UnwindData |  |
| 50 | `DeleteApplicabilityInfoArray` | `0x27A90` | 144 | UnwindData |  |
| 29 | `AppxValidatePackagesWithOptions` | `0x29700` | 1,117 | UnwindData |  |
| 59 | `IsSharedAppsEnabled` | `0x2A470` | 185 | UnwindData |  |
| 67 | `ClientDeleteAllPackagesFromMainPackageArray` | `0x2FC70` | 283 | UnwindData |  |
| 47 | `CheckComCallerHasCapabilities` | `0x2FFB0` | 35 | UnwindData |  |
| 26 | `NotifyPackageStatusChanged` | `0x30340` | 134 | UnwindData |  |
| 66 | `ClientGetAllPackagesToBeInstalledForUser` | `0x30710` | 207 | UnwindData |  |
| 106 | `DllGetActivationFactory` | `0x321B0` | 392 | UnwindData |  |
| 2 | `GetApplicability` | `0x364A0` | 118,896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `AppxAddPackageToAllUserStoreForPbr` | `0x53510` | 119,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `AppxPackageRepositoryRecoverStagedPackages` | `0x53510` | 119,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `AppxPackageRepositoryRecoverUserInstalls` | `0x53510` | 119,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `AppxRecoverUserInstallsForUpgrade` | `0x53510` | 119,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `FixJunctionsForAppsIfNecessary` | `0x53510` | 119,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `GetApplicability2` | `0x53510` | 119,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `GetApplicability4` | `0x53510` | 119,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | *Ordinal Only* | `0x70900` | 363 | UnwindData |  |
| 95 | `MsixIsPackageFeatureSupported` | `0x78DC0` | 157 | UnwindData |  |
| 93 | `MsixIsPackageRegisteredOrNewerAvailable` | `0x78E70` | 545 | UnwindData |  |
| 102 | `MsixIsPayloadFileStaged` | `0x790A0` | 1,043 | UnwindData |  |
| 60 | `AppInstallerUpdateAllTask` | `0x7ADF0` | 38 | UnwindData |  |
| 46 | `AppxCleanupOrphanPackages` | `0x7AE20` | 53 | UnwindData |  |
| 45 | `AppxCleanupSystemAppsMigratedToFOD` | `0x7AE60` | 1,444 | UnwindData |  |
| 42 | `AppxCleanupWCIReparsePoints` | `0x7B410` | 178 | UnwindData |  |
| 3 | `AppxCreateSharedLocalFolder` | `0x7B4D0` | 71 | UnwindData |  |
| 15 | `AppxCreateSharedLocalFolderForFamilyName` | `0x7B520` | 71 | UnwindData |  |
| 7 | `AppxDeletePackageFiles` | `0x7B570` | 149 | UnwindData |  |
| 19 | `AppxDestagePackage` | `0x7B610` | 1,149 | UnwindData |  |
| 70 | `AppxDoesSharedLocalFolderExistForFamilyName` | `0x7BAA0` | 349 | UnwindData |  |
| 18 | `AppxGetPackageInstalledLocation` | `0x7BC10` | 701 | UnwindData |  |
| 21 | `AppxGetStagedPackageFullNameFromFamilyName` | `0x7BEE0` | 1,813 | UnwindData |  |
| 22 | `AppxIsStagedPackageStoreSigned` | `0x7C600` | 312 | UnwindData |  |
| 28 | `AppxPreRegisterAllInboxPackages` | `0x7C740` | 201 | UnwindData |  |
| 12 | `AppxPreRegisterPackage` | `0x7C810` | 257 | UnwindData |  |
| 11 | `AppxPreStageCleanupRunTask` | `0x7C920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `AppxRegisterPackage` | `0x7C930` | 349 | UnwindData |  |
| 74 | `AppxRemoveAllPackagesForUserSid` | `0x7CAA0` | 907 | UnwindData |  |
| 30 | `AppxRemovePackageForAllUsers` | `0x7CE40` | 431 | UnwindData |  |
| 37 | `AppxRemovePackageForUserSid` | `0x7D000` | 1,883 | UnwindData |  |
| 8 | `AppxRequestRemovePackageForUser` | `0x7D770` | 61 | UnwindData |  |
| 78 | `AppxResetPackage` | `0x7D7C0` | 496 | UnwindData |  |
| 17 | `AppxStagePackage` | `0x7D9C0` | 2,420 | UnwindData |  |
| 105 | `AppxStagePackage2` | `0x7E340` | 2,644 | UnwindData |  |
| 85 | `AppxSvcPrepareForSysprepGeneralize` | `0x7EDA0` | 55 | UnwindData |  |
| 71 | `AppxValidatePackages` | `0x7EDE0` | 20 | UnwindData |  |
| 61 | `CheckAppInstallerUpdateAvailability` | `0x7EE00` | 111 | UnwindData |  |
| 75 | `CheckForUpdatesAndWaitForInstallerIfNeeded` | `0x7EE80` | 346 | UnwindData |  |
| 73 | `CleanupProfileForUser` | `0x7EFE0` | 320 | UnwindData |  |
| 94 | `ClientExistsAnyPackageToBeInstalledForUser` | `0x7F130` | 229 | UnwindData |  |
| 38 | `CreateCanonicalPriFile` | `0x7F220` | 159 | UnwindData |  |
| 81 | `DeleteAutoUpdateSettings` | `0x7F2D0` | 76 | UnwindData |  |
| 100 | `ExistPackagesPendingDeferredRemovalForUser` | `0x7F330` | 147 | UnwindData |  |
| 99 | `FreeApplicationSecret` | `0x7F3D0` | 17 | UnwindData |  |
| 16 | *Ordinal Only* | `0x7F3F0` | 110 | UnwindData |  |
| 34 | `GeneratePreInstalledPriFiles` | `0x7F470` | 93 | UnwindData |  |
| 96 | `GetApplicationSecret` | `0x7F4E0` | 93 | UnwindData |  |
| 48 | `GetBundleApplicablePackages` | `0x7F550` | 2,878 | UnwindData |  |
| 25 | `GetNotificationPayload` | `0x800A0` | 53 | UnwindData |  |
| 72 | `HasPackageFamilyBeenRegisteredForUser` | `0x800E0` | 581 | UnwindData |  |
| 9 | `IsPackageInstalled` | `0x80330` | 128 | UnwindData |  |
| 64 | `IsPackageMetadataUnderSystemMetadata` | `0x803C0` | 61 | UnwindData |  |
| 84 | `MSIXForceReRegisterPackage` | `0x80410` | 475 | UnwindData |  |
| 108 | `MsixAppxAllUserStoreIsInboxPackage` | `0x80690` | 332 | UnwindData |  |
| 109 | `MsixEnsurePackageIsRegistered` | `0x807F0` | 212 | UnwindData |  |
| 104 | `MsixGetOutdatedPackagesForUser` | `0x808D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `MsixIsPackageRegistrationPending` | `0x808E0` | 414 | UnwindData |  |
| 86 | `MsixPackageVolumeIsRepairNeeded` | `0x80A90` | 60 | UnwindData |  |
| 87 | `MsixPackageVolumeRepair` | `0x80AE0` | 62 | UnwindData |  |
| 103 | `MsixPreRegisterPackagesIfNeeded` | `0x80B30` | 640 | UnwindData |  |
| 92 | `MsixPreRegisterUupProducts` | `0x80DC0` | 519 | UnwindData |  |
| 91 | `MsixRemovePackageByUriAsync` | `0x80FD0` | 289 | UnwindData |  |
| 90 | `MsixRepairPackageAsync` | `0x81100` | 329 | UnwindData |  |
| 89 | `MsixResetPackageAsync` | `0x81250` | 329 | UnwindData |  |
| 82 | `PauseAutoUpdateSettings` | `0x813A0` | 87 | UnwindData |  |
| 35 | `PopulateProtocolAndFTA` | `0x81400` | 250 | UnwindData |  |
| 10 | `RDSRecoverRequests` | `0x81500` | 167 | UnwindData |  |
| 13 | `ReArmAppxPreStageCleanupTask` | `0x815B0` | 19 | UnwindData |  |
| 101 | `RemoveDeferredPackages` | `0x815D0` | 285 | UnwindData |  |
| 43 | `RepairPackageFileAcls` | `0x81700` | 100 | UnwindData |  |
| 31 | `RequestContentGroups` | `0x81770` | 82 | UnwindData |  |
| 33 | `RequestContentGroupsForFullTrust` | `0x817D0` | 82 | UnwindData |  |
| 98 | `ResetApplicationSecrets` | `0x81830` | 51 | UnwindData |  |
| 83 | `ScheduleAppInstallerBackgroundUpdate` | `0x81870` | 44 | UnwindData |  |
| 97 | `SetApplicationSecret` | `0x818B0` | 93 | UnwindData |  |
| 53 | `UpdateAgentCancelAllDownloads` | `0x81920` | 51 | UnwindData |  |
| 76 | `UpdateAgentCancelDownload` | `0x81960` | 54 | UnwindData |  |
| 51 | `UpdateAgentCreateDownload` | `0x819A0` | 144 | UnwindData |  |
| 62 | `UpdateAgentFreeDownloadRanges` | `0x81A40` | 37 | UnwindData |  |
| 79 | `UpdateAgentGetDownloadPackageReturnValue` | `0x81A70` | 105 | UnwindData |  |
| 52 | `UpdateAgentGetDownloadRanges` | `0x81AE0` | 71 | UnwindData |  |
| 69 | `UpdateAgentGetDownloadingPackageCount` | `0x81B30` | 71 | UnwindData |  |
| 80 | `UpdateAppInstallerSettings` | `0x81B80` | 302 | UnwindData |  |
| 55 | `UpdateDataSourceAddRange` | `0x81CC0` | 105 | UnwindData |  |
| 57 | `UpdateDataSourceCancelRun` | `0x81D30` | 71 | UnwindData |  |
| 54 | `UpdateDataSourceRegister` | `0x81D80` | 100 | UnwindData |  |
| 56 | `UpdateDataSourceRun` | `0x81DF0` | 71 | UnwindData |  |
| 27 | `VerifyPackage` | `0x81E40` | 83 | UnwindData |  |
