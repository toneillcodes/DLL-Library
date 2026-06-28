# Binary Specification: mscms.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\mscms.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7e1035676e201caed790040251126ff8150c2bfe9145fb68142d16446391c6eb`
* **Total Exported Functions:** 126

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 204 | `InternalSetDeviceTemperature` | `0x7020` | 39 | UnwindData |  |
| 6 | `CloseColorProfile` | `0x9330` | 109 | UnwindData |  |
| 70 | `OpenColorProfileW` | `0x9690` | 38 | UnwindData |  |
| 101 | `WcsOpenColorProfileW` | `0x96C0` | 50 | UnwindData |  |
| 68 | `IsColorProfileValid` | `0xAE60` | 304 | UnwindData |  |
| 34 | `DeleteColorTransform` | `0xB0F0` | 169 | UnwindData |  |
| 45 | `GetColorProfileElement` | `0xBDB0` | 529 | UnwindData |  |
| 48 | `GetColorProfileHeader` | `0xBFD0` | 123 | UnwindData |  |
| 234 | `ColorProfileGetDisplayDefault` | `0xDDA0` | 1,037 | UnwindData |  |
| 95 | `WcsGetDefaultColorProfile` | `0xE1C0` | 90 | UnwindData |  |
| 55 | `GetStandardColorSpaceProfileW` | `0xE220` | 35 | UnwindData |  |
| 96 | `WcsGetDefaultColorProfileSize` | `0xE360` | 44 | UnwindData |  |
| 97 | `WcsGetDefaultRenderingIntent` | `0xEF40` | 536 | UnwindData |  |
| 44 | `GetColorDirectoryW` | `0xFF70` | 144 | UnwindData |  |
| 71 | `OpenDisplay` | `0x10420` | 1,069 | UnwindData |  |
| 83 | `TranslateColors` | `0x12230` | 548 | UnwindData |  |
| 82 | `TranslateBitmapBits` | `0x12460` | 969 | UnwindData |  |
| 67 | `IsColorProfileTagPresent` | `0x12D20` | 224 | UnwindData |  |
| 49 | `GetCountColorProfileElements` | `0x12F40` | 317 | UnwindData |  |
| 47 | `GetColorProfileFromHandle` | `0x1CAB0` | 295 | UnwindData |  |
| 7 | `CloseDisplay` | `0x1F2F0` | 48 | UnwindData |  |
| 93 | `WcsEnumColorProfilesSize` | `0x1F630` | 87 | UnwindData |  |
| 40 | `EnumColorProfilesW` | `0x1F690` | 69 | UnwindData |  |
| 28 | `CreateProfileFromLogColorSpaceW` | `0x21230` | 137 | UnwindData |  |
| 63 | `InternalRefreshCalibration` | `0x22770` | 927 | UnwindData |  |
| 206 | `InternalGetDeviceGammaCapability` | `0x22EF0` | 784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `WcsGetUsePerUserProfiles` | `0x23200` | 72 | UnwindData |  |
| 94 | `WcsGetCalibrationManagementState` | `0x25C90` | 480 | UnwindData |  |
| 12 | `ColorCplInitialize` | `0x270F0` | 94 | UnwindData |  |
| 240 | `GetCalibrationDataFromProfile` | `0x27860` | 976 | UnwindData |  |
| 250 | `InternalGetChromaticAdaptationMatrixForDisplay` | `0x27C70` | 1,049 | UnwindData |  |
| 38 | `DllGetClassObject` | `0x29BF0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `InternalGetDeviceConfig` | `0x29CD0` | 225 | UnwindData |  |
| 74 | `SelectCMM` | `0x29F60` | 103 | UnwindData |  |
| 208 | `InternalSetDeviceGDIGammaRamp` | `0x2A850` | 205 | UnwindData |  |
| 103 | `WcsSetDefaultColorProfile` | `0x2B280` | 3,968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `InternalWcsAssociateColorProfileWithDevice` | `0x2C200` | 28 | UnwindData |  |
| 59 | `InternalGetPS2CSAFromLCS` | `0x34D60` | 922 | UnwindData |  |
| 60 | `InternalGetPS2ColorRenderingDictionary` | `0x35100` | 39 | UnwindData |  |
| 200 | `InternalGetPS2ColorRenderingDictionary2` | `0x35130` | 576 | UnwindData |  |
| 61 | `InternalGetPS2ColorSpaceArray` | `0x354C0` | 49 | UnwindData |  |
| 202 | `InternalGetPS2ColorSpaceArray2` | `0x35500` | 971 | UnwindData |  |
| 62 | `InternalGetPS2PreviewCRD` | `0x358E0` | 55 | UnwindData |  |
| 201 | `InternalGetPS2PreviewCRD2` | `0x35920` | 2,564 | UnwindData |  |
| 21 | `ConvertColorNameToIndex` | `0x3A200` | 341 | UnwindData |  |
| 22 | `ConvertIndexToColorName` | `0x3A360` | 341 | UnwindData |  |
| 25 | `CreateDeviceLinkProfile` | `0x3A4C0` | 421 | UnwindData |  |
| 27 | `CreateProfileFromLogColorSpaceA` | `0x3A670` | 275 | UnwindData |  |
| 46 | `GetColorProfileElementTag` | `0x3A790` | 158 | UnwindData |  |
| 50 | `GetNamedProfileInfo` | `0x3A840` | 304 | UnwindData |  |
| 51 | `GetPS2ColorRenderingDictionary` | `0x3A980` | 429 | UnwindData |  |
| 52 | `GetPS2ColorRenderingIntent` | `0x3AB40` | 405 | UnwindData |  |
| 53 | `GetPS2ColorSpaceArray` | `0x3ACE0` | 451 | UnwindData |  |
| 69 | `OpenColorProfileA` | `0x3AEB0` | 310 | UnwindData |  |
| 75 | `SetColorProfileElement` | `0x3AFF0` | 426 | UnwindData |  |
| 76 | `SetColorProfileElementReference` | `0x3B1A0` | 387 | UnwindData |  |
| 77 | `SetColorProfileElementSize` | `0x3B330` | 749 | UnwindData |  |
| 78 | `SetColorProfileHeader` | `0x3B630` | 237 | UnwindData |  |
| 100 | `WcsOpenColorProfileA` | `0x3B730` | 302 | UnwindData |  |
| 4 | `CheckBitmapBits` | `0x3C560` | 464 | UnwindData |  |
| 5 | `CheckColors` | `0x3C740` | 244 | UnwindData |  |
| 23 | `CreateColorTransformA` | `0x3C840` | 320 | UnwindData |  |
| 24 | `CreateColorTransformW` | `0x3C990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `CreateMultiProfileTransform` | `0x3C9A0` | 916 | UnwindData |  |
| 42 | `GetCMMInfo` | `0x3CD40` | 91 | UnwindData |  |
| 72 | `RegisterCMMA` | `0x3CDB0` | 144 | UnwindData |  |
| 73 | `RegisterCMMW` | `0x3CE50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `UnregisterCMMA` | `0x3CE60` | 93 | UnwindData |  |
| 87 | `UnregisterCMMW` | `0x3CED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `WcsCheckColors` | `0x3CEE0` | 221 | UnwindData |  |
| 106 | `WcsTranslateColors` | `0x3CFD0` | 496 | UnwindData |  |
| 2 | `DeviceRenameEvent` | `0x3F0F0` | 528 | UnwindData |  |
| 1 | `AssociateColorProfileWithDeviceA` | `0x427E0` | 251 | UnwindData |  |
| 3 | `AssociateColorProfileWithDeviceW` | `0x428F0` | 140 | UnwindData |  |
| 35 | `DisassociateColorProfileFromDeviceA` | `0x42990` | 240 | UnwindData |  |
| 36 | `DisassociateColorProfileFromDeviceW` | `0x42A90` | 118 | UnwindData |  |
| 39 | `EnumColorProfilesA` | `0x42B10` | 540 | UnwindData |  |
| 41 | `GenerateCopyFilePaths` | `0x42D40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `GetColorDirectoryA` | `0x42D50` | 368 | UnwindData |  |
| 54 | `GetStandardColorSpaceProfileA` | `0x42ED0` | 441 | UnwindData |  |
| 56 | `InstallColorProfileA` | `0x43090` | 120 | UnwindData |  |
| 57 | `InstallColorProfileW` | `0x43110` | 540 | UnwindData |  |
| 64 | `InternalSetDeviceConfig` | `0x43340` | 50 | UnwindData |  |
| 66 | `InternalWcsDisassociateColorProfileWithDevice` | `0x43380` | 23 | UnwindData |  |
| 79 | `SetStandardColorSpaceProfileA` | `0x433A0` | 122 | UnwindData |  |
| 80 | `SetStandardColorSpaceProfileW` | `0x43420` | 339 | UnwindData |  |
| 81 | `SpoolerCopyFileEvent` | `0x43580` | 686 | UnwindData |  |
| 84 | `UninstallColorProfileA` | `0x43840` | 126 | UnwindData |  |
| 85 | `UninstallColorProfileW` | `0x438D0` | 639 | UnwindData |  |
| 88 | `WcsAssociateColorProfileWithDevice` | `0x43B60` | 125 | UnwindData |  |
| 91 | `WcsDisassociateColorProfileFromDevice` | `0x43BF0` | 90 | UnwindData |  |
| 92 | `WcsEnumColorProfiles` | `0x43C50` | 73 | UnwindData |  |
| 104 | `WcsSetDefaultRenderingIntent` | `0x43CA0` | 246 | UnwindData |  |
| 105 | `WcsSetUsePerUserProfiles` | `0x43DA0` | 928 | UnwindData |  |
| 8 | `ColorCplGetDefaultProfileScope` | `0x44F30` | 294 | UnwindData |  |
| 9 | `ColorCplGetDefaultRenderingIntentScope` | `0x45060` | 107 | UnwindData |  |
| 10 | `ColorCplGetProfileProperties` | `0x450E0` | 40 | UnwindData |  |
| 11 | `ColorCplHasSystemWideAssociationListChanged` | `0x45110` | 189 | UnwindData |  |
| 13 | `ColorCplLoadAssociationList` | `0x451E0` | 1,270 | UnwindData |  |
| 14 | `ColorCplMergeAssociationLists` | `0x456E0` | 184 | UnwindData |  |
| 15 | `ColorCplOverwritePerUserAssociationList` | `0x457A0` | 296 | UnwindData |  |
| 16 | `ColorCplReleaseProfileProperties` | `0x458D0` | 35 | UnwindData |  |
| 17 | `ColorCplResetSystemWideAssociationListChangedWarning` | `0x45900` | 145 | UnwindData |  |
| 18 | `ColorCplSaveAssociationList` | `0x459A0` | 598 | UnwindData |  |
| 19 | `ColorCplSetUsePerUserProfiles` | `0x45C00` | 382 | UnwindData |  |
| 20 | `ColorCplUninitialize` | `0x45D90` | 37 | UnwindData |  |
| 99 | `WcsGpCanInstallOrUninstallProfiles` | `0x463F0` | 235 | UnwindData |  |
| 270 | `InternalRefreshCalibrationFromColorServer` | `0x4A550` | 74 | UnwindData |  |
| 102 | `WcsSetCalibrationManagementState` | `0x4A5A0` | 883 | UnwindData |  |
| 37 | `DllCanUnloadNow` | `0x4ADD0` | 42 | UnwindData |  |
| 29 | `DccwCreateDisplayProfileAssociationList` | `0x4AEF0` | 68 | UnwindData |  |
| 30 | `DccwGetDisplayProfileAssociationList` | `0x4AF40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `DccwReleaseDisplayProfileAssociationList` | `0x4AF50` | 41 | UnwindData |  |
| 33 | `DccwSetDisplayProfileAssociationList` | `0x4AF80` | 115 | UnwindData |  |
| 207 | `InternalGetAppliedGDIGammaRamp` | `0x4B460` | 36 | UnwindData |  |
| 205 | `InternalGetAppliedGammaRamp` | `0x4B490` | 36 | UnwindData |  |
| 203 | `InternalSetDeviceGammaRamp` | `0x4B4C0` | 359 | UnwindData |  |
| 260 | `InternalSetAccessibilityColorMatrix` | `0x4B9D0` | 765 | UnwindData |  |
| 230 | `ColorProfileAddDisplayAssociation` | `0x4BDB0` | 183 | UnwindData |  |
| 236 | `ColorProfileGetDeviceCapabilities` | `0x4BE70` | 1,134 | UnwindData |  |
| 233 | `ColorProfileGetDisplayList` | `0x4C2F0` | 541 | UnwindData |  |
| 235 | `ColorProfileGetDisplayUserScope` | `0x4C520` | 191 | UnwindData |  |
| 231 | `ColorProfileRemoveDisplayAssociation` | `0x4C5F0` | 173 | UnwindData |  |
| 232 | `ColorProfileSetDisplayDefaultAssociation` | `0x4C6B0` | 184 | UnwindData |  |
| 31 | `DccwGetGamutSize` | `0x4D7C0` | 528 | UnwindData |  |
| 90 | `WcsCreateIccProfile` | `0x4EF20` | 1,472 | UnwindData |  |
