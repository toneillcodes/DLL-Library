# Binary Specification: DismApi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\DismApi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `feb55d1c2fa6030b23cec8e0d0bf3077f3ed3f4c9dd0a60442b4b15221249e45`
* **Total Exported Functions:** 122

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 9 | `DismCloseSession` | `0xB140` | 97 | UnwindData |  |
| 29 | `DismInitialize` | `0xB9D0` | 578 | UnwindData |  |
| 31 | `DismOpenSession` | `0x25B10` | 185 | UnwindData |  |
| 15 | `DismGetCapabilityInfo` | `0x25C10` | 31 | UnwindData |  |
| 11 | `DismDelete` | `0x2E970` | 12,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DismAddCapability` | `0x31850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DismAddDriver` | `0x31860` | 185 | UnwindData |  |
| 3 | `DismAddLanguage` | `0x31920` | 242 | UnwindData |  |
| 4 | `DismAddPackage` | `0x31A20` | 252 | UnwindData |  |
| 6 | `DismApplyUnattend` | `0x31B30` | 162 | UnwindData |  |
| 7 | `DismCheckImageHealth` | `0x31BE0` | 153 | UnwindData |  |
| 8 | `DismCleanupMountpoints` | `0x31C80` | 78 | UnwindData |  |
| 10 | `DismCommitImage` | `0x31CE0` | 143 | UnwindData |  |
| 12 | `DismDisableFeature` | `0x31D80` | 212 | UnwindData |  |
| 13 | `DismEnableFeature` | `0x31E60` | 264 | UnwindData |  |
| 14 | `DismGetCapabilities` | `0x31F70` | 38 | UnwindData |  |
| 16 | `DismGetDriverInfo` | `0x31FA0` | 189 | UnwindData |  |
| 17 | `DismGetDrivers` | `0x32070` | 133 | UnwindData |  |
| 18 | `DismGetFeatureInfo` | `0x32100` | 189 | UnwindData |  |
| 19 | `DismGetFeatureParent` | `0x321D0` | 199 | UnwindData |  |
| 20 | `DismGetFeatures` | `0x322A0` | 145 | UnwindData |  |
| 21 | `DismGetImageInfo` | `0x32340` | 152 | UnwindData |  |
| 22 | `DismGetLastErrorMessage` | `0x323E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `DismGetMountedImageInfo` | `0x323F0` | 99 | UnwindData |  |
| 24 | `DismGetPackageInfo` | `0x32460` | 179 | UnwindData |  |
| 26 | `DismGetPackages` | `0x32520` | 121 | UnwindData |  |
| 28 | `DismGetReservedStorageState` | `0x325A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `DismMountImage` | `0x325B0` | 230 | UnwindData |  |
| 32 | `DismRemountImage` | `0x326A0` | 130 | UnwindData |  |
| 33 | `DismRemoveCapability` | `0x32730` | 36 | UnwindData |  |
| 34 | `DismRemoveDriver` | `0x32760` | 156 | UnwindData |  |
| 35 | `DismRemoveLanguage` | `0x32810` | 194 | UnwindData |  |
| 36 | `DismRemovePackage` | `0x328E0` | 204 | UnwindData |  |
| 38 | `DismRestoreImageHealth` | `0x329C0` | 168 | UnwindData |  |
| 39 | `DismSetReservedStorageState` | `0x32A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `DismShutdown` | `0x32A80` | 83 | UnwindData |  |
| 41 | `DismUnmountImage` | `0x32AE0` | 177 | UnwindData |  |
| 5 | `DismAddProvisionedAppxPackage` | `0x32F30` | 280 | UnwindData |  |
| 49 | `_DismAddProvisionedAppxPackage` | `0x32F30` | 280 | UnwindData |  |
| 27 | `DismGetProvisionedAppxPackages` | `0x33050` | 119 | UnwindData |  |
| 81 | `_DismGetProvisionedAppxPackages` | `0x33050` | 119 | UnwindData |  |
| 37 | `DismRemoveProvisionedAppxPackage` | `0x330D0` | 169 | UnwindData |  |
| 102 | `_DismRemoveProvisionedAppxPackage` | `0x330D0` | 169 | UnwindData |  |
| 42 | `_DismAddAppxPackageFamilyToUninstallBlocklist` | `0x3AE80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `_DismAddPackageFamilyToUninstallBlocklist` | `0x3AE80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `_DismAddDriverEx` | `0x3AE90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `_DismAddGenericAppPackage` | `0x3AEA0` | 198 | UnwindData |  |
| 45 | `_DismAddNetAdapter` | `0x3AF70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `_DismAddPackageEx` | `0x3AF80` | 181 | UnwindData |  |
| 48 | `_DismAddProvisionedAppSharedPackageContainer` | `0x3B040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `_DismAddProvisionedAppxPackageEx` | `0x3B050` | 121 | UnwindData |  |
| 51 | `_DismApplyCustomDataImage` | `0x3B0D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `_DismApplyFfuImage` | `0x3B0E0` | 15 | UnwindData |  |
| 53 | `_DismApplyOsImage` | `0x3B100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `_DismApplyProvisioningPackage` | `0x3B110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `_DismCaptureOsImage` | `0x3B120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `_DismCaptureSoftwareInventory` | `0x3B130` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `_DismCleanImage` | `0x3B140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `_DismEnableDisableFeature` | `0x3B150` | 110 | UnwindData |  |
| 59 | `_DismExportDriver` | `0x3B1D0` | 145 | UnwindData |  |
| 60 | `_DismExportOsImage` | `0x3B270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `_DismExportSource` | `0x3B280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `_DismGetCapabilitiesEx` | `0x3B290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `_DismGetCapabilityInfoEx` | `0x3B2A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `_DismGetCurrentEdition` | `0x3B2B0` | 103 | UnwindData |  |
| 65 | `_DismGetDriversEx` | `0x3B320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `_DismGetEffectiveSystemUILanguage` | `0x3B330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `_DismGetFeaturesEx` | `0x3B340` | 155 | UnwindData |  |
| 68 | `_DismGetInstallLanguage` | `0x3B3F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `_DismGetKCacheBinaryValue` | `0x3B400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `_DismGetKCacheDwordValue` | `0x3B410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `_DismGetKCacheStringValue` | `0x3B420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `_DismGetLastCBSSessionID` | `0x3B430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `_DismGetNonRemovableAppsPolicy` | `0x3B440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `_DismGetNonRemovableAppxAppsPolicy` | `0x3B440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `_DismGetOSUninstallWindow` | `0x3B450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `_DismGetOsInfo` | `0x3B460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `DismGetPackageInfoEx` | `0x3B470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `_DismGetPackageInfoEx` | `0x3B470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `_DismGetPackagesEx` | `0x3B480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `_DismGetProductKeyInfo` | `0x3B490` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `_DismGetProvisionedAppSharedPackageContainers` | `0x3B4A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `_DismGetProvisioningPackageInfo` | `0x3B4B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `_DismGetRegistryMountPoint` | `0x3B4C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `_DismGetStateFromCBSSessionID` | `0x3B4D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `_DismGetTargetCompositionEditions` | `0x3B4E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `_DismGetTargetEditions` | `0x3B4F0` | 119 | UnwindData |  |
| 87 | `_DismGetTargetVirtualEditions` | `0x3B570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `_DismGetTemplateAbsolutePath` | `0x3B580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `_DismGetTemplateString` | `0x3B590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `_DismGetUsedSpace` | `0x3B5A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `_DismInitiateOSUninstall` | `0x3B5B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `_DismOpenSessionEx` | `0x3B5C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `_DismOptimizeImage` | `0x3B5D0` | 143 | UnwindData |  |
| 94 | `_DismOptimizeProvisionedAppxPackages` | `0x3B670` | 97 | UnwindData |  |
| 95 | `_DismRemoveAppxPackageFamilyFromUninstallBlocklist` | `0x3B6E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `_DismRemovePackageFamilyFromUninstallBlocklist` | `0x3B6E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `_DismRemoveCapabilityEx` | `0x3B6F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `_DismRemoveLanguageEx` | `0x3B700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `_DismRemoveOSUninstall` | `0x3B710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `_DismRemovePackageEx` | `0x3B720` | 212 | UnwindData |  |
| 101 | `_DismRemoveProvisionedAppSharedPackageContainer` | `0x3B800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `_DismRemoveProvisionedAppxPackageAllUsers` | `0x3B810` | 168 | UnwindData |  |
| 104 | `_DismRevertPendingActions` | `0x3B8C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `_DismSetAllIntlSettings` | `0x3B8D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `_DismSetAppXProvisionedDataFile` | `0x3B8E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `_DismSetAppxProvisionedDataFile` | `0x3B8E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `_DismSetEdition` | `0x3B8F0` | 160 | UnwindData |  |
| 109 | `_DismSetEdition2` | `0x3B9A0` | 46 | UnwindData |  |
| 110 | `_DismSetFirstBootCommandLine` | `0x3B9E0` | 119 | UnwindData |  |
| 111 | `_DismSetIntlSettings` | `0x3BA60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `_DismSetMachineName` | `0x3BA70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `_DismSetOSUninstallWindow` | `0x3BA80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `_DismSetProductKey` | `0x3BA90` | 103 | UnwindData |  |
| 115 | `_DismSetSkuIntlDefaults` | `0x3BB00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `_DismSetTemplateString` | `0x3BB10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `_DismSplitFfuImage` | `0x3BB20` | 15 | UnwindData |  |
| 118 | `_DismStage` | `0x3BB40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `_DismSysprepCleanup` | `0x3BB50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `_DismSysprepGeneralize` | `0x3BB60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `_DismSysprepSpecialize` | `0x3BB70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `_DismValidateProductKey` | `0x3BB80` | 539,292 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
