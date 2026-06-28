# Binary Specification: AppXDeploymentServer.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\AppXDeploymentServer.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a67bdfbb3aee89ab4f98298b96c9cf544898ad010a783dec7869f1ba32969de8`
* **Total Exported Functions:** 39

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 9 | `EnumVisibilityByPackageFullNameInternal` | `0x1C270` | 1,140 | UnwindData |  |
| 5 | `EnumPackagesByUserSidInternal` | `0x1CA30` | 299 | UnwindData |  |
| 13 | `GetApplicability5Implementation` | `0x1CB70` | 1,873 | UnwindData |  |
| 7 | `EnumPackagesByUserSidPackageFamilyNameInternal` | `0x1DA90` | 1,415 | UnwindData |  |
| 10 | `FindPackageByUserSidPackageFullNameInternal` | `0x1E160` | 1,144 | UnwindData |  |
| 18 | `GetSessionIdsOwnedByUser` | `0x74C00` | 408 | UnwindData |  |
| 22 | `PackageRepositoryAllocate` | `0x8A0B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `PackageRepositoryFree` | `0x8A0C0` | 440,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `MergeSystemResourceFilesImplementation` | `0xF5A60` | 328 | UnwindData |  |
| 17 | `GetPackageFilesDiskUsagePerVolumeImplementation` | `0x103D30` | 2,797 | UnwindData |  |
| 6 | `EnumPackagesByUserSidNamePublisherInternal` | `0x104950` | 363 | UnwindData |  |
| 32 | `SetPackageStatusBlockingForUserImplementation` | `0x108550` | 1,361 | UnwindData |  |
| 8 | `EnumProvisionedPackagesInternal` | `0x142B90` | 318 | UnwindData |  |
| 1 | `AppXApplyTrustLabelToFolder` | `0x16DB10` | 5,968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `AppXSetTrustLabelOnPackage` | `0x16F260` | 1,190 | UnwindData |  |
| 39 | `SvchostPushServiceGlobals` | `0x1907F0` | 250,016 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `CreateCanonicalPriFileImplementation` | `0x1CD890` | 128 | UnwindData |  |
| 15 | `GetDeploymentError` | `0x1F3F70` | 41 | UnwindData |  |
| 20 | `IsPackagingExtensionBeingServiced` | `0x1F3FA0` | 41 | UnwindData |  |
| 31 | `SetDeploymentError` | `0x1F4080` | 44 | UnwindData |  |
| 37 | `DllCanUnloadNow` | `0x1F4110` | 84 | UnwindData |  |
| 38 | `DllGetActivationFactory` | `0x1F4170` | 193 | UnwindData |  |
| 14 | `GetApplicabilityImplementation` | `0x1F5890` | 112 | UnwindData |  |
| 19 | `IsPackageInstalledInternal` | `0x1F6420` | 474 | UnwindData |  |
| 11 | `GenerateBytecodeForPackageImplementation` | `0x1F6600` | 922 | UnwindData |  |
| 12 | `GenerateBytecodeForPackagesImplementation` | `0x1F69A0` | 343 | UnwindData |  |
| 28 | `RequestPackageOperationImplementation` | `0x1F6E50` | 782 | UnwindData |  |
| 16 | `GetPackageFilesDiskUsageImplementation` | `0x1FED50` | 280 | UnwindData |  |
| 2 | `CancelDeploymentImplementation` | `0x201180` | 231 | UnwindData |  |
| 4 | `CreateWnfStateNameImplementation` | `0x2021C0` | 46 | UnwindData |  |
| 24 | `PackageStatusOperationImplementation` | `0x205E20` | 190 | UnwindData |  |
| 25 | `PackageVolumeStatusImplementation` | `0x205EF0` | 168 | UnwindData |  |
| 26 | `RDSRecoverRequestsImplementation` | `0x206370` | 195 | UnwindData |  |
| 27 | `RepairResourcesPriAclsImplementation` | `0x206560` | 81 | UnwindData |  |
| 29 | `ServerSideRequestContentGroupsImplementation` | `0x2114B0` | 1,254 | UnwindData |  |
| 33 | `SetPackageStatusBlockingImplementation` | `0x212CD0` | 610 | UnwindData |  |
| 34 | `StartDeploymentImplementation` | `0x213080` | 385 | UnwindData |  |
| 30 | `ServiceMain` | `0x217F00` | 789 | UnwindData |  |
| 35 | `AddToPurgeList` | `0x2F4970` | 1,187,050 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
