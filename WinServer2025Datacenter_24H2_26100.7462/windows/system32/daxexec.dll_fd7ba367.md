# Binary Specification: daxexec.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\daxexec.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fd7ba367e2eaf9fc23dd7e0ddd91eac2a88a33b14d71c08a36a1d324f163c05f`
* **Total Exported Functions:** 66

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 8 | `CloseAppExecutionAlias` | `0x10310` | 2,576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `FreeAppExecutionAliasInfo` | `0x10310` | 2,576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `FreeAppExecutionAliasInfoWithLicenseRundown` | `0x10310` | 2,576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `DllCanUnloadNow` | `0x10D20` | 100 | UnwindData |  |
| 21 | `DllGetActivationFactory` | `0x10D90` | 466 | UnwindData |  |
| 22 | `DllGetClassObject` | `0x10F70` | 357 | UnwindData |  |
| 2 | `AddLookaside` | `0x13370` | 33 | UnwindData |  |
| 59 | `RemoveLookaside` | `0x133A0` | 33 | UnwindData |  |
| 60 | `RemoveLookasidePackage` | `0x133D0` | 63 | UnwindData |  |
| 3 | `AddProcessToHeliumContainer` | `0x21DB0` | 21 | UnwindData |  |
| 4 | `BeginCreatingHeliumContainerForDesktopAppXActivation` | `0x21DD0` | 239 | UnwindData |  |
| 5 | `CAMHandlePackagedProcessLaunch` | `0x21ED0` | 473 | UnwindData |  |
| 6 | `CheckAppXPackageBreakaway` | `0x220B0` | 70 | UnwindData |  |
| 7 | `CheckApplicationInCurrentPackage` | `0x22100` | 302 | UnwindData |  |
| 10 | `CompleteAppExecutionAliasProcessCreation` | `0x22240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `EnsureDesktopAppXPackageShutdown` | `0x22250` | 124 | UnwindData |  |
| 29 | `EraseExtendedAttributeAUMIDForAutoIdentity` | `0x222E0` | 92 | UnwindData |  |
| 33 | `FreeDesktopAppXLaunchContext` | `0x22350` | 38 | UnwindData |  |
| 41 | `GetExtendedAttributeAUMIDForAutoIdentity` | `0x22380` | 322 | UnwindData |  |
| 11 | `CreateAppExecutionAlias` | `0x224D0` | 1,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `GetAppExecutionAliasApplicationUserModelId` | `0x224D0` | 1,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `GetAppExecutionAliasExecutable` | `0x224D0` | 1,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `GetAppExecutionAliasPackageFamilyName` | `0x224D0` | 1,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `GetAppExecutionAliasPackageFullName` | `0x224D0` | 1,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `GetPackageFamilyNameFromFile` | `0x224D0` | 1,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `LoadAppExecutionAliasInfo` | `0x224D0` | 1,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `OpenAppExecutionAlias` | `0x224D0` | 1,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `OpenAppExecutionAliasForUser` | `0x224D0` | 1,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `PersistAppExecutionAliasToFile` | `0x224D0` | 1,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `PerformAppxLicenseRundown` | `0x22AF0` | 46 | UnwindData |  |
| 53 | `PostCreateProcessDesktopAppXActivation` | `0x22B30` | 1,653 | UnwindData |  |
| 61 | `RundownHeliumContainerForDesktopAppXActivation` | `0x231B0` | 16 | UnwindData |  |
| 64 | `SetExtendedAttributeAUMIDForAutoIdentity` | `0x231D0` | 364 | UnwindData |  |
| 66 | `VerifyFileIsTrustedAndInPackage` | `0x23350` | 575 | UnwindData |  |
| 12 | `CreateDesktopAppXActivationInfo` | `0x24C70` | 257 | UnwindData |  |
| 32 | `FreeDesktopAppXActivationInfo` | `0x24D80` | 38 | UnwindData |  |
| 63 | `SetDesktopAppXMetadataForPackage` | `0x33BA0` | 7,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `CreateDesktopAppXLocalCacheStructure` | `0x35930` | 18 | UnwindData |  |
| 14 | `CreateDesktopAppXTombstoneFile` | `0x35950` | 537 | UnwindData |  |
| 48 | `MigrateWritablePackageRootData` | `0x35CF0` | 1,219 | UnwindData |  |
| 58 | `RemoveDesktopAppXMetadataForFolder` | `0x36620` | 126 | UnwindData |  |
| 62 | `SetDesktopAppXMetadataForFolder` | `0x366B0` | 607 | UnwindData |  |
| 18 | `DetokenizeDesktopAppXOfflineRegistry` | `0x37E20` | 1,263 | UnwindData |  |
| 23 | `DoesPackageHaveElevationCapability` | `0x3FC60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `DoesPackageHaveUIAccessCapability` | `0x3FC80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `GetApplicationExecutableRelativePath` | `0x3FCA0` | 587 | UnwindData |  |
| 55 | `RegisterDesktopAppXPackageFamily` | `0x3FF00` | 33 | UnwindData |  |
| 56 | `RegisterDesktopAppXPackageFamilyIfNecessary` | `0x3FF30` | 2,128 | UnwindData |  |
| 40 | `GetDesktopAppXComRootHandle` | `0x40790` | 330 | UnwindData |  |
| 45 | `GetRegistryPathDetokenizer` | `0x40B70` | 380 | UnwindData |  |
| 1 | `ActivatePackageVirtualizationContext` | `0x7A740` | 68 | UnwindData |  |
| 16 | `CreatePackageVirtualizationContext` | `0x7A790` | 384 | UnwindData |  |
| 17 | `DeactivatePackageVirtualizationContext` | `0x7A920` | 194 | UnwindData |  |
| 26 | `DuplicatePackageVirtualizationContext` | `0x7A9F0` | 223 | UnwindData |  |
| 39 | `GetCurrentPackageVirtualizationContext` | `0x7AAE0` | 285 | UnwindData |  |
| 44 | `GetProcessesInVirtualizationContext` | `0x7AC10` | 21 | UnwindData |  |
| 57 | `ReleasePackageVirtualizationContext` | `0x7AC30` | 52 | UnwindData |  |
| 9 | `CloseJitvSilo` | `0x7C4E0` | 177 | UnwindData |  |
| 15 | `CreateJitvSilo` | `0x7C5A0` | 724 | UnwindData |  |
| 43 | `GetProcessesFromJitvSilos` | `0x7C880` | 438 | UnwindData |  |
| 46 | `JitvSiloRunDown` | `0x7CA40` | 164 | UnwindData |  |
| 25 | `DoesPluginSupportCentennial` | `0x93370` | 104 | UnwindData |  |
| 65 | `TryActivateDesktopAppXApplication` | `0x933E0` | 3,461 | UnwindData |  |
| 54 | `PrepareDesktopAppXActivation` | `0x94170` | 21 | UnwindData |  |
| 19 | `DisableDesktopAppXDebuggingForPackage` | `0x96360` | 235 | UnwindData |  |
| 27 | `EnableDesktopAppXDebuggingForPackage` | `0x96460` | 434 | UnwindData |  |
