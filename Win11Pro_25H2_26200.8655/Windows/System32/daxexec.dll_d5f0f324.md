# Binary Specification: daxexec.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\daxexec.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d5f0f32424bd651d5778631dc6bbecd4c159c7ba02d0be1046cd157acf8faac5`
* **Total Exported Functions:** 67

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 8 | `CloseAppExecutionAlias` | `0x10280` | 2,576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `FreeAppExecutionAliasInfo` | `0x10280` | 2,576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `FreeAppExecutionAliasInfoWithLicenseRundown` | `0x10280` | 2,576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `DllCanUnloadNow` | `0x10C90` | 100 | UnwindData |  |
| 22 | `DllGetActivationFactory` | `0x10D00` | 466 | UnwindData |  |
| 23 | `DllGetClassObject` | `0x10EE0` | 357 | UnwindData |  |
| 2 | `AddLookaside` | `0x132E0` | 33 | UnwindData |  |
| 60 | `RemoveLookaside` | `0x13310` | 33 | UnwindData |  |
| 61 | `RemoveLookasidePackage` | `0x13340` | 63 | UnwindData |  |
| 3 | `AddProcessToHeliumContainer` | `0x20120` | 21 | UnwindData |  |
| 4 | `BeginCreatingHeliumContainerForDesktopAppXActivation` | `0x20140` | 239 | UnwindData |  |
| 5 | `CAMHandlePackagedProcessLaunch` | `0x20240` | 473 | UnwindData |  |
| 6 | `CheckAppXPackageBreakaway` | `0x20420` | 70 | UnwindData |  |
| 7 | `CheckApplicationInCurrentPackage` | `0x20470` | 302 | UnwindData |  |
| 10 | `CompleteAppExecutionAliasProcessCreation` | `0x205B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `EnsureDesktopAppXPackageShutdown` | `0x205C0` | 124 | UnwindData |  |
| 30 | `EraseExtendedAttributeAUMIDForAutoIdentity` | `0x20650` | 92 | UnwindData |  |
| 34 | `FreeDesktopAppXLaunchContext` | `0x206C0` | 38 | UnwindData |  |
| 42 | `GetExtendedAttributeAUMIDForAutoIdentity` | `0x206F0` | 322 | UnwindData |  |
| 11 | `CreateAppExecutionAlias` | `0x20840` | 1,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `GetAppExecutionAliasApplicationUserModelId` | `0x20840` | 1,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `GetAppExecutionAliasExecutable` | `0x20840` | 1,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `GetAppExecutionAliasPackageFamilyName` | `0x20840` | 1,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `GetAppExecutionAliasPackageFullName` | `0x20840` | 1,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `GetPackageFamilyNameFromFile` | `0x20840` | 1,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `LoadAppExecutionAliasInfo` | `0x20840` | 1,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `OpenAppExecutionAlias` | `0x20840` | 1,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `OpenAppExecutionAliasForUser` | `0x20840` | 1,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `PersistAppExecutionAliasToFile` | `0x20840` | 1,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `PerformAppxLicenseRundown` | `0x20ED0` | 46 | UnwindData |  |
| 54 | `PostCreateProcessDesktopAppXActivation` | `0x20F10` | 1,521 | UnwindData |  |
| 62 | `RundownHeliumContainerForDesktopAppXActivation` | `0x21510` | 16 | UnwindData |  |
| 65 | `SetExtendedAttributeAUMIDForAutoIdentity` | `0x21530` | 364 | UnwindData |  |
| 67 | `VerifyFileIsTrustedAndInPackage` | `0x216B0` | 575 | UnwindData |  |
| 12 | `CreateDesktopAppXActivationInfo` | `0x23070` | 260 | UnwindData |  |
| 33 | `FreeDesktopAppXActivationInfo` | `0x23180` | 38 | UnwindData |  |
| 64 | `SetDesktopAppXMetadataForPackage` | `0x33630` | 7,728 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `CreateDesktopAppXLocalCacheStructure` | `0x35460` | 18 | UnwindData |  |
| 14 | `CreateDesktopAppXTombstoneFile` | `0x35480` | 537 | UnwindData |  |
| 49 | `MigrateWritablePackageRootData` | `0x35820` | 1,169 | UnwindData |  |
| 59 | `RemoveDesktopAppXMetadataForFolder` | `0x36120` | 126 | UnwindData |  |
| 63 | `SetDesktopAppXMetadataForFolder` | `0x361B0` | 544 | UnwindData |  |
| 17 | `CreatePackagedProcessByLaunchContract` | `0x363E0` | 116 | UnwindData |  |
| 19 | `DetokenizeDesktopAppXOfflineRegistry` | `0x37960` | 1,263 | UnwindData |  |
| 24 | `DoesPackageHaveElevationCapability` | `0x3FAC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `DoesPackageHaveUIAccessCapability` | `0x3FAE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `GetApplicationExecutableRelativePath` | `0x3FB00` | 587 | UnwindData |  |
| 56 | `RegisterDesktopAppXPackageFamily` | `0x3FD60` | 33 | UnwindData |  |
| 57 | `RegisterDesktopAppXPackageFamilyIfNecessary` | `0x3FD90` | 1,951 | UnwindData |  |
| 41 | `GetDesktopAppXComRootHandle` | `0x40540` | 330 | UnwindData |  |
| 46 | `GetRegistryPathDetokenizer` | `0x40920` | 380 | UnwindData |  |
| 1 | `ActivatePackageVirtualizationContext` | `0x7A6B0` | 68 | UnwindData |  |
| 16 | `CreatePackageVirtualizationContext` | `0x7A700` | 384 | UnwindData |  |
| 18 | `DeactivatePackageVirtualizationContext` | `0x7A890` | 194 | UnwindData |  |
| 27 | `DuplicatePackageVirtualizationContext` | `0x7A960` | 223 | UnwindData |  |
| 40 | `GetCurrentPackageVirtualizationContext` | `0x7AA50` | 285 | UnwindData |  |
| 45 | `GetProcessesInVirtualizationContext` | `0x7AB80` | 21 | UnwindData |  |
| 58 | `ReleasePackageVirtualizationContext` | `0x7ABA0` | 52 | UnwindData |  |
| 9 | `CloseJitvSilo` | `0x7C450` | 177 | UnwindData |  |
| 15 | `CreateJitvSilo` | `0x7C510` | 724 | UnwindData |  |
| 44 | `GetProcessesFromJitvSilos` | `0x7C7F0` | 438 | UnwindData |  |
| 47 | `JitvSiloRunDown` | `0x7C9B0` | 164 | UnwindData |  |
| 26 | `DoesPluginSupportCentennial` | `0x932E0` | 104 | UnwindData |  |
| 66 | `TryActivateDesktopAppXApplication` | `0x93350` | 3,469 | UnwindData |  |
| 55 | `PrepareDesktopAppXActivation` | `0x940F0` | 21 | UnwindData |  |
| 20 | `DisableDesktopAppXDebuggingForPackage` | `0x962E0` | 235 | UnwindData |  |
| 28 | `EnableDesktopAppXDebuggingForPackage` | `0x963E0` | 434 | UnwindData |  |
