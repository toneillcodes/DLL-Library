# Binary Specification: DismApi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DismApi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `632952071fef4e92d845a153d70a358691f914cd24adf5caad27f836d9f77179`
* **Total Exported Functions:** 133

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 9 | `DismCloseSession` | `0xB190` | 97 | UnwindData |  |
| 29 | `DismInitialize` | `0xBA20` | 578 | UnwindData |  |
| 31 | `DismOpenSession` | `0x24BB0` | 185 | UnwindData |  |
| 15 | `DismGetCapabilityInfo` | `0x24CB0` | 31 | UnwindData |  |
| 11 | `DismDelete` | `0x2EFA0` | 41,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DismAddCapability` | `0x39120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DismAddDriver` | `0x39130` | 185 | UnwindData |  |
| 3 | `DismAddLanguage` | `0x391F0` | 242 | UnwindData |  |
| 4 | `DismAddPackage` | `0x392F0` | 252 | UnwindData |  |
| 6 | `DismApplyUnattend` | `0x39400` | 162 | UnwindData |  |
| 7 | `DismCheckImageHealth` | `0x394B0` | 153 | UnwindData |  |
| 8 | `DismCleanupMountpoints` | `0x39550` | 78 | UnwindData |  |
| 10 | `DismCommitImage` | `0x395B0` | 143 | UnwindData |  |
| 12 | `DismDisableFeature` | `0x39650` | 212 | UnwindData |  |
| 13 | `DismEnableFeature` | `0x39730` | 264 | UnwindData |  |
| 14 | `DismGetCapabilities` | `0x39840` | 38 | UnwindData |  |
| 16 | `DismGetDriverInfo` | `0x39870` | 189 | UnwindData |  |
| 17 | `DismGetDrivers` | `0x39940` | 133 | UnwindData |  |
| 18 | `DismGetFeatureInfo` | `0x399D0` | 189 | UnwindData |  |
| 19 | `DismGetFeatureParent` | `0x39AA0` | 199 | UnwindData |  |
| 20 | `DismGetFeatures` | `0x39B70` | 145 | UnwindData |  |
| 21 | `DismGetImageInfo` | `0x39C10` | 152 | UnwindData |  |
| 22 | `DismGetLastErrorMessage` | `0x39CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `DismGetMountedImageInfo` | `0x39CC0` | 99 | UnwindData |  |
| 24 | `DismGetPackageInfo` | `0x39D30` | 179 | UnwindData |  |
| 26 | `DismGetPackages` | `0x39DF0` | 121 | UnwindData |  |
| 28 | `DismGetReservedStorageState` | `0x39E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `DismMountImage` | `0x39E80` | 230 | UnwindData |  |
| 32 | `DismRemountImage` | `0x39F70` | 130 | UnwindData |  |
| 33 | `DismRemoveCapability` | `0x3A000` | 36 | UnwindData |  |
| 34 | `DismRemoveDriver` | `0x3A030` | 156 | UnwindData |  |
| 35 | `DismRemoveLanguage` | `0x3A0E0` | 194 | UnwindData |  |
| 36 | `DismRemovePackage` | `0x3A1B0` | 204 | UnwindData |  |
| 38 | `DismRestoreImageHealth` | `0x3A290` | 168 | UnwindData |  |
| 39 | `DismSetReservedStorageState` | `0x3A340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `DismShutdown` | `0x3A350` | 83 | UnwindData |  |
| 41 | `DismUnmountImage` | `0x3A3B0` | 177 | UnwindData |  |
| 5 | `DismAddProvisionedAppxPackage` | `0x3A800` | 475 | UnwindData |  |
| 50 | `_DismAddProvisionedAppxPackage` | `0x3A800` | 475 | UnwindData |  |
| 27 | `DismGetProvisionedAppxPackages` | `0x3A9F0` | 119 | UnwindData |  |
| 84 | `_DismGetProvisionedAppxPackages` | `0x3A9F0` | 119 | UnwindData |  |
| 37 | `DismRemoveProvisionedAppxPackage` | `0x3AA70` | 169 | UnwindData |  |
| 109 | `_DismRemoveProvisionedAppxPackage` | `0x3AA70` | 169 | UnwindData |  |
| 42 | `_DismAddAppxPackageFamilyToUninstallBlocklist` | `0x3CD10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `_DismAddPackageFamilyToUninstallBlocklist` | `0x3CD10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `_DismAddDriverEx` | `0x3CD20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `_DismAddGenericAppPackage` | `0x3CD30` | 498 | UnwindData |  |
| 45 | `_DismAddGenericAppPackage2` | `0x3CF30` | 210 | UnwindData |  |
| 46 | `_DismAddNetAdapter` | `0x3D010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `_DismAddPackageEx` | `0x3D020` | 181 | UnwindData |  |
| 49 | `_DismAddProvisionedAppSharedPackageContainer` | `0x3D0E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `_DismAddProvisionedAppxPackageEx` | `0x3D0F0` | 306 | UnwindData |  |
| 52 | `_DismAddProvisionedAppxPackageEx2` | `0x3D230` | 133 | UnwindData |  |
| 53 | `_DismApplyCustomDataImage` | `0x3D2C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `_DismApplyFfuImage` | `0x3D2D0` | 15 | UnwindData |  |
| 55 | `_DismApplyOsImage` | `0x3D2F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `_DismApplyProvisioningPackage` | `0x3D300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `_DismCaptureOsImage` | `0x3D310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `_DismCaptureSoftwareInventory` | `0x3D320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `_DismCleanImage` | `0x3D330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `_DismEnableDisableFeature` | `0x3D340` | 110 | UnwindData |  |
| 61 | `_DismEnumerateRRMPs` | `0x3D3C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `_DismExportDriver` | `0x3D3D0` | 145 | UnwindData |  |
| 63 | `_DismExportOsImage` | `0x3D470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `_DismExportSource` | `0x3D480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `_DismGetCapabilitiesEx` | `0x3D490` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `_DismGetCapabilityInfoEx` | `0x3D4A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `_DismGetCurrentEdition` | `0x3D4B0` | 103 | UnwindData |  |
| 68 | `_DismGetDriversEx` | `0x3D520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `_DismGetEffectiveSystemUILanguage` | `0x3D530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `_DismGetFeaturesEx` | `0x3D540` | 155 | UnwindData |  |
| 71 | `_DismGetInstallLanguage` | `0x3D5F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `_DismGetKCacheBinaryValue` | `0x3D600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `_DismGetKCacheDwordValue` | `0x3D610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `_DismGetKCacheStringValue` | `0x3D620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `_DismGetLastCBSSessionID` | `0x3D630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `_DismGetNonRemovableAppsPolicy` | `0x3D640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `_DismGetNonRemovableAppxAppsPolicy` | `0x3D640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `_DismGetOSUninstallWindow` | `0x3D650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `_DismGetOsInfo` | `0x3D660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `DismGetPackageInfoEx` | `0x3D670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `_DismGetPackageInfoEx` | `0x3D670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `_DismGetPackagesEx` | `0x3D680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `_DismGetProductKeyInfo` | `0x3D690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `_DismGetProvisionedAppSharedPackageContainers` | `0x3D6A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `_DismGetProvisioningPackageInfo` | `0x3D6B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `_DismGetRRMPAltitude` | `0x3D6C0` | 119 | UnwindData |  |
| 87 | `_DismGetRRMPInfo` | `0x3D740` | 119 | UnwindData |  |
| 88 | `_DismGetRegistryMountPoint` | `0x3D7C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `_DismGetRemoteManagementStatus` | `0x3D7D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `_DismGetStateFromCBSSessionID` | `0x3D7E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `_DismGetTargetCompositionEditions` | `0x3D7F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `_DismGetTargetEditions` | `0x3D800` | 119 | UnwindData |  |
| 93 | `_DismGetTargetVirtualEditions` | `0x3D880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `_DismGetTemplateAbsolutePath` | `0x3D890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `_DismGetTemplateString` | `0x3D8A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `_DismGetUsedSpace` | `0x3D8B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `_DismInitiateOSUninstall` | `0x3D8C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `_DismOpenSessionEx` | `0x3D8D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `_DismOptimizeImage` | `0x3D8E0` | 143 | UnwindData |  |
| 100 | `_DismOptimizeProvisionedAppxPackages` | `0x3D980` | 97 | UnwindData |  |
| 101 | `_DismRegisterRRMP` | `0x3D9F0` | 166 | UnwindData |  |
| 102 | `_DismRemoveAppxPackageFamilyFromUninstallBlocklist` | `0x3DAA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `_DismRemovePackageFamilyFromUninstallBlocklist` | `0x3DAA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `_DismRemoveCapabilityEx` | `0x3DAB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `_DismRemoveLanguageEx` | `0x3DAC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `_DismRemoveOSUninstall` | `0x3DAD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `_DismRemovePackageEx` | `0x3DAE0` | 212 | UnwindData |  |
| 108 | `_DismRemoveProvisionedAppSharedPackageContainer` | `0x3DBC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `_DismRemoveProvisionedAppxPackageAllUsers` | `0x3DBD0` | 168 | UnwindData |  |
| 111 | `_DismRemoveRRMPAltitude` | `0x3DC80` | 101 | UnwindData |  |
| 112 | `_DismRevertPendingActions` | `0x3DCF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `_DismSetAllIntlSettings` | `0x3DD00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `_DismSetAppXProvisionedDataFile` | `0x3DD10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `_DismSetAppxProvisionedDataFile` | `0x3DD10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `_DismSetEdition` | `0x3DD20` | 160 | UnwindData |  |
| 117 | `_DismSetEdition2` | `0x3DDD0` | 46 | UnwindData |  |
| 118 | `_DismSetFirstBootCommandLine` | `0x3DE10` | 119 | UnwindData |  |
| 119 | `_DismSetIntlSettings` | `0x3DE90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `_DismSetMachineName` | `0x3DEA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `_DismSetOSUninstallWindow` | `0x3DEB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `_DismSetProductKey` | `0x3DEC0` | 103 | UnwindData |  |
| 123 | `_DismSetRRMPAltitude` | `0x3DF30` | 119 | UnwindData |  |
| 124 | `_DismSetRemoteManagementStatus` | `0x3DFB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `_DismSetSkuIntlDefaults` | `0x3DFC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `_DismSetTemplateString` | `0x3DFD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `_DismSplitFfuImage` | `0x3DFE0` | 15 | UnwindData |  |
| 128 | `_DismStage` | `0x3E000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `_DismSysprepCleanup` | `0x3E010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | `_DismSysprepGeneralize` | `0x3E020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `_DismSysprepSpecialize` | `0x3E030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `_DismUnregisterRRMP` | `0x3E040` | 101 | UnwindData |  |
| 133 | `_DismValidateProductKey` | `0x3E0B0` | 576,748 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
