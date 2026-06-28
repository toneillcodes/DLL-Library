# Binary Specification: AppXDeploymentServer.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\AppXDeploymentServer.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4b56d04b0c0becb8cbe85d7127599a8f291dfaefadc41d8c7203d646c2119dbc`
* **Total Exported Functions:** 39

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 9 | `EnumVisibilityByPackageFullNameInternal` | `0x4CD00` | 1,127 | UnwindData |  |
| 5 | `EnumPackagesByUserSidInternal` | `0x4D4B0` | 299 | UnwindData |  |
| 13 | `GetApplicability5Implementation` | `0x4D5F0` | 1,873 | UnwindData |  |
| 7 | `EnumPackagesByUserSidPackageFamilyNameInternal` | `0x4DE10` | 1,415 | UnwindData |  |
| 10 | `FindPackageByUserSidPackageFullNameInternal` | `0x4E4C0` | 1,144 | UnwindData |  |
| 18 | `GetSessionIdsOwnedByUser` | `0x87500` | 408 | UnwindData |  |
| 22 | `PackageRepositoryAllocate` | `0x99570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `PackageRepositoryFree` | `0x99580` | 403,440 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `MergeSystemResourceFilesImplementation` | `0xFBD70` | 328 | UnwindData |  |
| 17 | `GetPackageFilesDiskUsagePerVolumeImplementation` | `0x10A5D0` | 2,797 | UnwindData |  |
| 6 | `EnumPackagesByUserSidNamePublisherInternal` | `0x10B2A0` | 363 | UnwindData |  |
| 32 | `SetPackageStatusBlockingForUserImplementation` | `0x10ECF0` | 1,361 | UnwindData |  |
| 8 | `EnumProvisionedPackagesInternal` | `0x147A30` | 318 | UnwindData |  |
| 1 | `AppXApplyTrustLabelToFolder` | `0x16F2F0` | 3,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `AppXSetTrustLabelOnPackage` | `0x170240` | 1,190 | UnwindData |  |
| 39 | `SvchostPushServiceGlobals` | `0x192FA0` | 218,544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `CreateCanonicalPriFileImplementation` | `0x1C8550` | 128 | UnwindData |  |
| 15 | `GetDeploymentError` | `0x1F0040` | 41 | UnwindData |  |
| 20 | `IsPackagingExtensionBeingServiced` | `0x1F0070` | 41 | UnwindData |  |
| 31 | `SetDeploymentError` | `0x1F01E0` | 44 | UnwindData |  |
| 37 | `DllCanUnloadNow` | `0x1F02B0` | 84 | UnwindData |  |
| 38 | `DllGetActivationFactory` | `0x1F0310` | 193 | UnwindData |  |
| 14 | `GetApplicabilityImplementation` | `0x1F1A30` | 112 | UnwindData |  |
| 19 | `IsPackageInstalledInternal` | `0x1F25A0` | 474 | UnwindData |  |
| 11 | `GenerateBytecodeForPackageImplementation` | `0x1F2780` | 922 | UnwindData |  |
| 12 | `GenerateBytecodeForPackagesImplementation` | `0x1F2B20` | 343 | UnwindData |  |
| 28 | `RequestPackageOperationImplementation` | `0x1F2FD0` | 782 | UnwindData |  |
| 16 | `GetPackageFilesDiskUsageImplementation` | `0x1FB450` | 280 | UnwindData |  |
| 2 | `CancelDeploymentImplementation` | `0x1FCF80` | 231 | UnwindData |  |
| 4 | `CreateWnfStateNameImplementation` | `0x1FDAE0` | 46 | UnwindData |  |
| 24 | `PackageStatusOperationImplementation` | `0x1FFE30` | 190 | UnwindData |  |
| 25 | `PackageVolumeStatusImplementation` | `0x1FFF00` | 168 | UnwindData |  |
| 26 | `RDSRecoverRequestsImplementation` | `0x200380` | 195 | UnwindData |  |
| 27 | `RepairResourcesPriAclsImplementation` | `0x200520` | 81 | UnwindData |  |
| 29 | `ServerSideRequestContentGroupsImplementation` | `0x20A880` | 1,254 | UnwindData |  |
| 33 | `SetPackageStatusBlockingImplementation` | `0x20BE50` | 610 | UnwindData |  |
| 34 | `StartDeploymentImplementation` | `0x20C2D0` | 385 | UnwindData |  |
| 30 | `ServiceMain` | `0x20FCA0` | 624 | UnwindData |  |
| 35 | `AddToPurgeList` | `0x2E0D60` | 1,169,946 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
