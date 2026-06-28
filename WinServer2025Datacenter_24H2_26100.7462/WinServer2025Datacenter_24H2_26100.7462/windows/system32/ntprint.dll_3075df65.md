# Binary Specification: ntprint.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ntprint.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3075df6585ac8ba7ab67cfadca6cca14349525cc06f771de27dc5b80ca5c3d46`
* **Total Exported Functions:** 62

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 103 | *Ordinal Only* | `0xD370` | 528 | UnwindData |  |
| 120 | `PSetupInstallDriverPackageFromConnection` | `0xD590` | 55 | UnwindData |  |
| 147 | `PSetupInstallICMProfiles` | `0x119F0` | 700 | UnwindData |  |
| 148 | `PSetupInstallInboxDriverSilently` | `0x11CC0` | 50 | UnwindData |  |
| 150 | `PSetupInstallPrinterDriver` | `0x11D00` | 2,119 | UnwindData |  |
| 107 | *Ordinal Only* | `0x12550` | 91 | UnwindData |  |
| 154 | `PSetupParseInfAndCommitFileQueue` | `0x125C0` | 1,848 | UnwindData |  |
| 163 | `PSetupShowBlockedDriverUI` | `0x12D00` | 235 | UnwindData |  |
| 105 | `ClassInstall32` | `0x13C20` | 595 | UnwindData |  |
| 123 | `PSetupAssociateICMProfiles` | `0x17660` | 330 | UnwindData |  |
| 134 | `PSetupDisassociateICMProfiles` | `0x177B0` | 359 | UnwindData |  |
| 156 | `PSetupProcessPrinterAdded` | `0x17920` | 899 | UnwindData |  |
| 128 | `PSetupCreateMonitorInfo` | `0x18530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `PSetupDestroyMonitorInfo` | `0x18540` | 142 | UnwindData |  |
| 138 | `PSetupEnumMonitor` | `0x185E0` | 126 | UnwindData |  |
| 149 | `PSetupInstallMonitor` | `0x18670` | 788 | UnwindData |  |
| 109 | `PSetupCheckForDriversInDriverStore` | `0x1BB00` | 857 | UnwindData |  |
| 137 | `PSetupDriverStoreAddDriverPackage` | `0x229B0` | 773 | UnwindData |  |
| 140 | `PSetupFreeDrvField` | `0x22CC0` | 37 | UnwindData |  |
| 130 | `PSetupDestroyDriverInfo3` | `0x22CF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `PSetupFreeMem` | `0x22CF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `PSetupGetInfDriverStoreLocation` | `0x22D10` | 154 | UnwindData |  |
| 144 | `PSetupGetLocalDataField` | `0x22DB0` | 497 | UnwindData |  |
| 145 | `PSetupGetPathToSearch` | `0x22FB0` | 240 | UnwindData |  |
| 152 | `PSetupIsDriverInstalled` | `0x230B0` | 429 | UnwindData |  |
| 153 | `PSetupIsTheDriverFoundInInfInstalled` | `0x23390` | 433 | UnwindData |  |
| 161 | `PSetupSetNonInteractiveMode` | `0x23550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 164 | `PSetupThisPlatform` | `0x23570` | 16,320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `PSetupDriverStoreFindDriverPackageW` | `0x27530` | 73 | UnwindData |  |
| 104 | *Ordinal Only* | `0x277C0` | 469 | UnwindData |  |
| 118 | `PSetupGetActualInstallSection` | `0x279A0` | 245 | UnwindData |  |
| 124 | `PSetupBuildDriverList` | `0x29910` | 65 | UnwindData |  |
| 125 | `PSetupBuildDriversFromPath` | `0x29960` | 336 | UnwindData |  |
| 127 | `PSetupCreateDrvSetupPage` | `0x29AC0` | 120 | UnwindData |  |
| 129 | `PSetupCreatePrinterDeviceInfoList` | `0x29B40` | 90 | UnwindData |  |
| 132 | `PSetupDestroyPrinterDeviceInfoList` | `0x29BA0` | 42 | UnwindData |  |
| 133 | `PSetupDestroySelectedDriverInfo` | `0x29BD0` | 20 | UnwindData |  |
| 135 | `PSetupDriverInfoFromDeviceID` | `0x29BF0` | 61 | UnwindData |  |
| 136 | `PSetupDriverInfoFromName` | `0x29C40` | 61 | UnwindData |  |
| 139 | `PSetupFindCompatibleDriverFromName` | `0x29C90` | 587 | UnwindData |  |
| 146 | `PSetupGetSelectedDriverInfo` | `0x29EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `PSetupPreSelectDriver` | `0x29F00` | 82 | UnwindData |  |
| 157 | `PSetupSelectDeviceButtons` | `0x29F60` | 255 | UnwindData |  |
| 158 | `PSetupSelectDriver` | `0x2A070` | 97 | UnwindData |  |
| 159 | `PSetupSetCoreInboxDriverPath` | `0x2A0E0` | 109 | UnwindData |  |
| 160 | `PSetupSetDriverPlatform` | `0x2A160` | 453 | UnwindData |  |
| 162 | `PSetupSetSelectDevTitleAndInstructions` | `0x2A330` | 386 | UnwindData |  |
| 108 | *Ordinal Only* | `0x2A4C0` | 852 | UnwindData |  |
| 122 | `ServerInstallW` | `0x2B3F0` | 232 | UnwindData |  |
| 151 | `PSetupIsCompatibleDriver` | `0x2C610` | 156 | UnwindData |  |
| 112 | `PSetupElevateAndCallDriverStoreAddDriverPackage` | `0x2E0C0` | 952 | UnwindData |  |
| 113 | `PSetupElevatedDriverStoreAddDriverPackageW` | `0x2E480` | 193 | UnwindData |  |
| 114 | `PSetupElevatedInstallDownloadedLegacyDriverW` | `0x2E550` | 272 | UnwindData |  |
| 115 | `PSetupElevatedInstallDriverPackageFromConnectionW` | `0x2E670` | 221 | UnwindData |  |
| 116 | `PSetupElevatedInstallPrinterDriverFromTheWebW` | `0x2E760` | 292 | UnwindData |  |
| 117 | `PSetupElevatedLegacyPrintDriverInstallW` | `0x2E890` | 776 | UnwindData |  |
| 121 | `PSetupWebPnpGenerateDownLevelInfForInboxDriver` | `0x2F800` | 327 | UnwindData |  |
| 142 | `PSetupGetDriverInfo3` | `0x30FB0` | 5,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `PSetupDownloadAndInstallLegacyDriverW` | `0x326D0` | 190 | UnwindData |  |
| 119 | `PSetupGetCatalogNameFromInfW` | `0x33DA0` | 563 | UnwindData |  |
| 126 | `PSetupCopyDriverPackageFiles` | `0x33FE0` | 775 | UnwindData |  |
| 106 | *Ordinal Only* | `0x37730` | 753 | UnwindData |  |
