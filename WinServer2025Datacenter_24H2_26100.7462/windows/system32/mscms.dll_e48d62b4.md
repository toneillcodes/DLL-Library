# Binary Specification: mscms.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\mscms.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e48d62b4c46401764c7be690f789983d567b2c761a0b5389be3981d69b957cf5`
* **Total Exported Functions:** 126

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 204 | `InternalSetDeviceTemperature` | `0x70A0` | 39 | UnwindData |  |
| 6 | `CloseColorProfile` | `0x9320` | 109 | UnwindData |  |
| 70 | `OpenColorProfileW` | `0x9680` | 38 | UnwindData |  |
| 101 | `WcsOpenColorProfileW` | `0x96B0` | 50 | UnwindData |  |
| 68 | `IsColorProfileValid` | `0xAE50` | 304 | UnwindData |  |
| 34 | `DeleteColorTransform` | `0xB0E0` | 169 | UnwindData |  |
| 45 | `GetColorProfileElement` | `0xBDA0` | 529 | UnwindData |  |
| 48 | `GetColorProfileHeader` | `0xBFC0` | 123 | UnwindData |  |
| 234 | `ColorProfileGetDisplayDefault` | `0xDD90` | 1,037 | UnwindData |  |
| 95 | `WcsGetDefaultColorProfile` | `0xE1B0` | 90 | UnwindData |  |
| 55 | `GetStandardColorSpaceProfileW` | `0xE210` | 35 | UnwindData |  |
| 96 | `WcsGetDefaultColorProfileSize` | `0xE350` | 44 | UnwindData |  |
| 97 | `WcsGetDefaultRenderingIntent` | `0xEF30` | 536 | UnwindData |  |
| 44 | `GetColorDirectoryW` | `0xFFF0` | 144 | UnwindData |  |
| 71 | `OpenDisplay` | `0x104A0` | 1,069 | UnwindData |  |
| 83 | `TranslateColors` | `0x122B0` | 548 | UnwindData |  |
| 82 | `TranslateBitmapBits` | `0x124E0` | 969 | UnwindData |  |
| 67 | `IsColorProfileTagPresent` | `0x12DA0` | 224 | UnwindData |  |
| 49 | `GetCountColorProfileElements` | `0x12FC0` | 317 | UnwindData |  |
| 47 | `GetColorProfileFromHandle` | `0x1CDE0` | 295 | UnwindData |  |
| 7 | `CloseDisplay` | `0x1F690` | 48 | UnwindData |  |
| 93 | `WcsEnumColorProfilesSize` | `0x1F9D0` | 87 | UnwindData |  |
| 40 | `EnumColorProfilesW` | `0x1FA30` | 69 | UnwindData |  |
| 28 | `CreateProfileFromLogColorSpaceW` | `0x21580` | 137 | UnwindData |  |
| 63 | `InternalRefreshCalibration` | `0x22C90` | 895 | UnwindData |  |
| 206 | `InternalGetDeviceGammaCapability` | `0x233F0` | 784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `WcsGetUsePerUserProfiles` | `0x23700` | 72 | UnwindData |  |
| 94 | `WcsGetCalibrationManagementState` | `0x260E0` | 480 | UnwindData |  |
| 12 | `ColorCplInitialize` | `0x27540` | 94 | UnwindData |  |
| 240 | `GetCalibrationDataFromProfile` | `0x27920` | 952 | UnwindData |  |
| 250 | `InternalGetChromaticAdaptationMatrixForDisplay` | `0x27D10` | 1,049 | UnwindData |  |
| 38 | `DllGetClassObject` | `0x29CC0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `InternalGetDeviceConfig` | `0x29DA0` | 225 | UnwindData |  |
| 74 | `SelectCMM` | `0x2A030` | 103 | UnwindData |  |
| 208 | `InternalSetDeviceGDIGammaRamp` | `0x2A920` | 205 | UnwindData |  |
| 103 | `WcsSetDefaultColorProfile` | `0x2B350` | 3,968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `InternalWcsAssociateColorProfileWithDevice` | `0x2C2D0` | 28 | UnwindData |  |
| 59 | `InternalGetPS2CSAFromLCS` | `0x34E30` | 922 | UnwindData |  |
| 60 | `InternalGetPS2ColorRenderingDictionary` | `0x351D0` | 39 | UnwindData |  |
| 200 | `InternalGetPS2ColorRenderingDictionary2` | `0x35200` | 576 | UnwindData |  |
| 61 | `InternalGetPS2ColorSpaceArray` | `0x35590` | 49 | UnwindData |  |
| 202 | `InternalGetPS2ColorSpaceArray2` | `0x355D0` | 971 | UnwindData |  |
| 62 | `InternalGetPS2PreviewCRD` | `0x359B0` | 55 | UnwindData |  |
| 201 | `InternalGetPS2PreviewCRD2` | `0x359F0` | 2,564 | UnwindData |  |
| 21 | `ConvertColorNameToIndex` | `0x3A2D0` | 341 | UnwindData |  |
| 22 | `ConvertIndexToColorName` | `0x3A430` | 341 | UnwindData |  |
| 25 | `CreateDeviceLinkProfile` | `0x3A590` | 421 | UnwindData |  |
| 27 | `CreateProfileFromLogColorSpaceA` | `0x3A740` | 275 | UnwindData |  |
| 46 | `GetColorProfileElementTag` | `0x3A860` | 158 | UnwindData |  |
| 50 | `GetNamedProfileInfo` | `0x3A910` | 304 | UnwindData |  |
| 51 | `GetPS2ColorRenderingDictionary` | `0x3AA50` | 429 | UnwindData |  |
| 52 | `GetPS2ColorRenderingIntent` | `0x3AC10` | 405 | UnwindData |  |
| 53 | `GetPS2ColorSpaceArray` | `0x3ADB0` | 451 | UnwindData |  |
| 69 | `OpenColorProfileA` | `0x3AF80` | 310 | UnwindData |  |
| 75 | `SetColorProfileElement` | `0x3B0C0` | 426 | UnwindData |  |
| 76 | `SetColorProfileElementReference` | `0x3B270` | 387 | UnwindData |  |
| 77 | `SetColorProfileElementSize` | `0x3B400` | 749 | UnwindData |  |
| 78 | `SetColorProfileHeader` | `0x3B700` | 237 | UnwindData |  |
| 100 | `WcsOpenColorProfileA` | `0x3B800` | 302 | UnwindData |  |
| 4 | `CheckBitmapBits` | `0x3C630` | 464 | UnwindData |  |
| 5 | `CheckColors` | `0x3C810` | 244 | UnwindData |  |
| 23 | `CreateColorTransformA` | `0x3C910` | 320 | UnwindData |  |
| 24 | `CreateColorTransformW` | `0x3CA60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `CreateMultiProfileTransform` | `0x3CA70` | 916 | UnwindData |  |
| 42 | `GetCMMInfo` | `0x3CE10` | 91 | UnwindData |  |
| 72 | `RegisterCMMA` | `0x3CE80` | 144 | UnwindData |  |
| 73 | `RegisterCMMW` | `0x3CF20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `UnregisterCMMA` | `0x3CF30` | 93 | UnwindData |  |
| 87 | `UnregisterCMMW` | `0x3CFA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `WcsCheckColors` | `0x3CFB0` | 221 | UnwindData |  |
| 106 | `WcsTranslateColors` | `0x3D0A0` | 496 | UnwindData |  |
| 2 | `DeviceRenameEvent` | `0x3F170` | 528 | UnwindData |  |
| 1 | `AssociateColorProfileWithDeviceA` | `0x43790` | 251 | UnwindData |  |
| 3 | `AssociateColorProfileWithDeviceW` | `0x438A0` | 140 | UnwindData |  |
| 35 | `DisassociateColorProfileFromDeviceA` | `0x43940` | 240 | UnwindData |  |
| 36 | `DisassociateColorProfileFromDeviceW` | `0x43A40` | 118 | UnwindData |  |
| 39 | `EnumColorProfilesA` | `0x43AC0` | 540 | UnwindData |  |
| 41 | `GenerateCopyFilePaths` | `0x43CF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `GetColorDirectoryA` | `0x43D00` | 368 | UnwindData |  |
| 54 | `GetStandardColorSpaceProfileA` | `0x43E80` | 441 | UnwindData |  |
| 56 | `InstallColorProfileA` | `0x44040` | 120 | UnwindData |  |
| 57 | `InstallColorProfileW` | `0x440C0` | 540 | UnwindData |  |
| 64 | `InternalSetDeviceConfig` | `0x442F0` | 50 | UnwindData |  |
| 66 | `InternalWcsDisassociateColorProfileWithDevice` | `0x44330` | 23 | UnwindData |  |
| 79 | `SetStandardColorSpaceProfileA` | `0x44350` | 122 | UnwindData |  |
| 80 | `SetStandardColorSpaceProfileW` | `0x443D0` | 339 | UnwindData |  |
| 81 | `SpoolerCopyFileEvent` | `0x44530` | 686 | UnwindData |  |
| 84 | `UninstallColorProfileA` | `0x447F0` | 126 | UnwindData |  |
| 85 | `UninstallColorProfileW` | `0x44880` | 639 | UnwindData |  |
| 88 | `WcsAssociateColorProfileWithDevice` | `0x44B10` | 125 | UnwindData |  |
| 91 | `WcsDisassociateColorProfileFromDevice` | `0x44BA0` | 90 | UnwindData |  |
| 92 | `WcsEnumColorProfiles` | `0x44C00` | 73 | UnwindData |  |
| 104 | `WcsSetDefaultRenderingIntent` | `0x44C50` | 246 | UnwindData |  |
| 105 | `WcsSetUsePerUserProfiles` | `0x44D50` | 928 | UnwindData |  |
| 8 | `ColorCplGetDefaultProfileScope` | `0x45EE0` | 294 | UnwindData |  |
| 9 | `ColorCplGetDefaultRenderingIntentScope` | `0x46010` | 107 | UnwindData |  |
| 10 | `ColorCplGetProfileProperties` | `0x46090` | 40 | UnwindData |  |
| 11 | `ColorCplHasSystemWideAssociationListChanged` | `0x460C0` | 189 | UnwindData |  |
| 13 | `ColorCplLoadAssociationList` | `0x46190` | 1,270 | UnwindData |  |
| 14 | `ColorCplMergeAssociationLists` | `0x46690` | 184 | UnwindData |  |
| 15 | `ColorCplOverwritePerUserAssociationList` | `0x46750` | 296 | UnwindData |  |
| 16 | `ColorCplReleaseProfileProperties` | `0x46880` | 35 | UnwindData |  |
| 17 | `ColorCplResetSystemWideAssociationListChangedWarning` | `0x468B0` | 145 | UnwindData |  |
| 18 | `ColorCplSaveAssociationList` | `0x46950` | 598 | UnwindData |  |
| 19 | `ColorCplSetUsePerUserProfiles` | `0x46BB0` | 382 | UnwindData |  |
| 20 | `ColorCplUninitialize` | `0x46D40` | 37 | UnwindData |  |
| 99 | `WcsGpCanInstallOrUninstallProfiles` | `0x473A0` | 235 | UnwindData |  |
| 270 | `InternalRefreshCalibrationFromColorServer` | `0x4B090` | 74 | UnwindData |  |
| 102 | `WcsSetCalibrationManagementState` | `0x4B0E0` | 860 | UnwindData |  |
| 37 | `DllCanUnloadNow` | `0x4B8F0` | 42 | UnwindData |  |
| 29 | `DccwCreateDisplayProfileAssociationList` | `0x4BA10` | 68 | UnwindData |  |
| 30 | `DccwGetDisplayProfileAssociationList` | `0x4BA60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `DccwReleaseDisplayProfileAssociationList` | `0x4BA70` | 41 | UnwindData |  |
| 33 | `DccwSetDisplayProfileAssociationList` | `0x4BAA0` | 115 | UnwindData |  |
| 207 | `InternalGetAppliedGDIGammaRamp` | `0x4BF80` | 36 | UnwindData |  |
| 205 | `InternalGetAppliedGammaRamp` | `0x4BFB0` | 36 | UnwindData |  |
| 203 | `InternalSetDeviceGammaRamp` | `0x4BFE0` | 359 | UnwindData |  |
| 260 | `InternalSetAccessibilityColorMatrix` | `0x4C4F0` | 765 | UnwindData |  |
| 230 | `ColorProfileAddDisplayAssociation` | `0x4C8D0` | 183 | UnwindData |  |
| 236 | `ColorProfileGetDeviceCapabilities` | `0x4C990` | 1,134 | UnwindData |  |
| 233 | `ColorProfileGetDisplayList` | `0x4CE10` | 541 | UnwindData |  |
| 235 | `ColorProfileGetDisplayUserScope` | `0x4D040` | 191 | UnwindData |  |
| 231 | `ColorProfileRemoveDisplayAssociation` | `0x4D110` | 173 | UnwindData |  |
| 232 | `ColorProfileSetDisplayDefaultAssociation` | `0x4D1D0` | 184 | UnwindData |  |
| 31 | `DccwGetGamutSize` | `0x4ECF0` | 528 | UnwindData |  |
| 90 | `WcsCreateIccProfile` | `0x50450` | 1,472 | UnwindData |  |
