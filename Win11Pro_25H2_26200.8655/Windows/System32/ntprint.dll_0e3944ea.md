# Binary Specification: ntprint.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ntprint.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0e3944eab0c40dfaa1848bbb1b63c51fc42c7ca319015b7c32c8185c21b51172`
* **Total Exported Functions:** 62

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 103 | *Ordinal Only* | `0xD3B0` | 528 | UnwindData |  |
| 120 | `PSetupInstallDriverPackageFromConnection` | `0xD5D0` | 55 | UnwindData |  |
| 147 | `PSetupInstallICMProfiles` | `0x11A30` | 700 | UnwindData |  |
| 148 | `PSetupInstallInboxDriverSilently` | `0x11D00` | 50 | UnwindData |  |
| 150 | `PSetupInstallPrinterDriver` | `0x11D40` | 2,119 | UnwindData |  |
| 107 | *Ordinal Only* | `0x12590` | 91 | UnwindData |  |
| 154 | `PSetupParseInfAndCommitFileQueue` | `0x12600` | 1,848 | UnwindData |  |
| 163 | `PSetupShowBlockedDriverUI` | `0x12D40` | 235 | UnwindData |  |
| 105 | `ClassInstall32` | `0x13C60` | 595 | UnwindData |  |
| 123 | `PSetupAssociateICMProfiles` | `0x176A0` | 330 | UnwindData |  |
| 134 | `PSetupDisassociateICMProfiles` | `0x177F0` | 359 | UnwindData |  |
| 156 | `PSetupProcessPrinterAdded` | `0x17960` | 899 | UnwindData |  |
| 128 | `PSetupCreateMonitorInfo` | `0x18570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `PSetupDestroyMonitorInfo` | `0x18580` | 142 | UnwindData |  |
| 138 | `PSetupEnumMonitor` | `0x18620` | 126 | UnwindData |  |
| 149 | `PSetupInstallMonitor` | `0x186B0` | 788 | UnwindData |  |
| 109 | `PSetupCheckForDriversInDriverStore` | `0x1BB40` | 857 | UnwindData |  |
| 137 | `PSetupDriverStoreAddDriverPackage` | `0x229F0` | 773 | UnwindData |  |
| 140 | `PSetupFreeDrvField` | `0x22D00` | 37 | UnwindData |  |
| 130 | `PSetupDestroyDriverInfo3` | `0x22D30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `PSetupFreeMem` | `0x22D30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `PSetupGetInfDriverStoreLocation` | `0x22D50` | 154 | UnwindData |  |
| 144 | `PSetupGetLocalDataField` | `0x22DF0` | 497 | UnwindData |  |
| 145 | `PSetupGetPathToSearch` | `0x22FF0` | 240 | UnwindData |  |
| 152 | `PSetupIsDriverInstalled` | `0x230F0` | 429 | UnwindData |  |
| 153 | `PSetupIsTheDriverFoundInInfInstalled` | `0x233D0` | 433 | UnwindData |  |
| 161 | `PSetupSetNonInteractiveMode` | `0x23590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 164 | `PSetupThisPlatform` | `0x235B0` | 16,320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `PSetupDriverStoreFindDriverPackageW` | `0x27570` | 73 | UnwindData |  |
| 104 | *Ordinal Only* | `0x27800` | 469 | UnwindData |  |
| 118 | `PSetupGetActualInstallSection` | `0x279E0` | 245 | UnwindData |  |
| 124 | `PSetupBuildDriverList` | `0x29950` | 65 | UnwindData |  |
| 125 | `PSetupBuildDriversFromPath` | `0x299A0` | 336 | UnwindData |  |
| 127 | `PSetupCreateDrvSetupPage` | `0x29B00` | 120 | UnwindData |  |
| 129 | `PSetupCreatePrinterDeviceInfoList` | `0x29B80` | 90 | UnwindData |  |
| 132 | `PSetupDestroyPrinterDeviceInfoList` | `0x29BE0` | 42 | UnwindData |  |
| 133 | `PSetupDestroySelectedDriverInfo` | `0x29C10` | 20 | UnwindData |  |
| 135 | `PSetupDriverInfoFromDeviceID` | `0x29C30` | 61 | UnwindData |  |
| 136 | `PSetupDriverInfoFromName` | `0x29C80` | 61 | UnwindData |  |
| 139 | `PSetupFindCompatibleDriverFromName` | `0x29CD0` | 587 | UnwindData |  |
| 146 | `PSetupGetSelectedDriverInfo` | `0x29F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `PSetupPreSelectDriver` | `0x29F40` | 82 | UnwindData |  |
| 157 | `PSetupSelectDeviceButtons` | `0x29FA0` | 255 | UnwindData |  |
| 158 | `PSetupSelectDriver` | `0x2A0B0` | 97 | UnwindData |  |
| 159 | `PSetupSetCoreInboxDriverPath` | `0x2A120` | 109 | UnwindData |  |
| 160 | `PSetupSetDriverPlatform` | `0x2A1A0` | 453 | UnwindData |  |
| 162 | `PSetupSetSelectDevTitleAndInstructions` | `0x2A370` | 386 | UnwindData |  |
| 108 | *Ordinal Only* | `0x2A500` | 852 | UnwindData |  |
| 122 | `ServerInstallW` | `0x2B430` | 232 | UnwindData |  |
| 151 | `PSetupIsCompatibleDriver` | `0x2C650` | 156 | UnwindData |  |
| 112 | `PSetupElevateAndCallDriverStoreAddDriverPackage` | `0x2E100` | 952 | UnwindData |  |
| 113 | `PSetupElevatedDriverStoreAddDriverPackageW` | `0x2E4C0` | 193 | UnwindData |  |
| 114 | `PSetupElevatedInstallDownloadedLegacyDriverW` | `0x2E590` | 272 | UnwindData |  |
| 115 | `PSetupElevatedInstallDriverPackageFromConnectionW` | `0x2E6B0` | 221 | UnwindData |  |
| 116 | `PSetupElevatedInstallPrinterDriverFromTheWebW` | `0x2E7A0` | 292 | UnwindData |  |
| 117 | `PSetupElevatedLegacyPrintDriverInstallW` | `0x2E8D0` | 776 | UnwindData |  |
| 121 | `PSetupWebPnpGenerateDownLevelInfForInboxDriver` | `0x2F840` | 327 | UnwindData |  |
| 142 | `PSetupGetDriverInfo3` | `0x30FF0` | 5,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `PSetupDownloadAndInstallLegacyDriverW` | `0x32630` | 190 | UnwindData |  |
| 119 | `PSetupGetCatalogNameFromInfW` | `0x33CE0` | 563 | UnwindData |  |
| 126 | `PSetupCopyDriverPackageFiles` | `0x33F20` | 775 | UnwindData |  |
| 106 | *Ordinal Only* | `0x37670` | 753 | UnwindData |  |
