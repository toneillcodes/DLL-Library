# Binary Specification: BootMenuUX.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\BootMenuUX.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `eac9d355727ae406cc1a097ad8b8fbeff50a084e5b85a0c9389a54b0aad2a3c0`
* **Total Exported Functions:** 93

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 92 | `UtilBcdCloseSystemStore` | `0x93E0` | 50 | UnwindData |  |
| 93 | `UtilGetCurrentKeyboardLayout` | `0xA7B0` | 215 | UnwindData |  |
| 1 | `CreateAdvancedOptionsButton` | `0xE020` | 148 | UnwindData |  |
| 2 | `CreateAdvancedRecoveryToolsButtonCollection` | `0xE0C0` | 81 | UnwindData |  |
| 3 | `CreateAdvancedStartupButton` | `0xE120` | 197 | UnwindData |  |
| 4 | `CreateAdvancedStartupLaunchPage` | `0xE1F0` | 126 | UnwindData |  |
| 5 | `CreateBareMetalRecoveryButton` | `0xE280` | 407 | UnwindData |  |
| 6 | `CreateBasicResetFinalChecksPage` | `0xE420` | 114 | UnwindData |  |
| 78 | `CreateWiFiInitPage` | `0xE420` | 114 | UnwindData |  |
| 7 | `CreateBasicResetLandingPage` | `0xE4A0` | 167 | UnwindData |  |
| 8 | `CreateBasicSystemResetButton` | `0xE550` | 155 | UnwindData |  |
| 9 | `CreateBasicSystemResetLaunchPage` | `0xE600` | 251 | UnwindData |  |
| 10 | `CreateBitlockerLandingPage` | `0xE710` | 175 | UnwindData |  |
| 11 | `CreateBlackWallpaperButton` | `0xE7D0` | 153 | UnwindData |  |
| 12 | `CreateBootableDeviceButtonCollection` | `0xE930` | 83 | UnwindData |  |
| 13 | `CreateBootableOSButtonCollection` | `0xE990` | 111 | UnwindData |  |
| 14 | `CreateCPITRFinalPage` | `0xEA10` | 133 | UnwindData |  |
| 15 | `CreateCSRTFinalPage` | `0xEAA0` | 109 | UnwindData |  |
| 16 | `CreateClearWallpaperPage` | `0xEB20` | 133 | UnwindData |  |
| 17 | `CreateDefaultOSButton` | `0xEBB0` | 250 | UnwindData |  |
| 18 | `CreateDefaultOSButtonCollection` | `0xECB0` | 111 | UnwindData |  |
| 19 | `CreateDefaultOSListButton` | `0xED30` | 233 | UnwindData |  |
| 20 | `CreateDeviceListButton` | `0xEE20` | 247 | UnwindData |  |
| 21 | `CreateDirectFactoryResetButton` | `0xEF20` | 198 | UnwindData |  |
| 22 | `CreateDownloadCloudPBRConfirmButton` | `0xEFF0` | 151 | UnwindData |  |
| 23 | `CreateFactoryResetFinalChecksPage` | `0xF090` | 111 | UnwindData |  |
| 31 | `CreateFlightRemovalProgressPage` | `0xF090` | 111 | UnwindData |  |
| 24 | `CreateFactoryResetLandingPage` | `0xF110` | 167 | UnwindData |  |
| 25 | `CreateFactorySystemResetButton` | `0xF1C0` | 155 | UnwindData |  |
| 26 | `CreateFactorySystemResetLaunchPage` | `0xF270` | 251 | UnwindData |  |
| 27 | `CreateFirmwareSettingsButton` | `0xF380` | 157 | UnwindData |  |
| 28 | `CreateFiveMinuteTimeoutAction` | `0xF430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `CreateFiveSecondTimeoutAction` | `0xF450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `CreateFlightRemovalConfirmButton` | `0xF470` | 151 | UnwindData |  |
| 32 | `CreateGenericWiFiNetworksCollection` | `0xF510` | 149 | UnwindData |  |
| 33 | `CreateKeyboardLayoutButtonCollection` | `0xF5B0` | 1,103 | UnwindData |  |
| 34 | `CreateLanguageButtonCollection` | `0xFA10` | 381 | UnwindData |  |
| 35 | `CreateOSListButton` | `0xFBA0` | 242 | UnwindData |  |
| 36 | `CreateOneMinuteTimeoutAction` | `0xFCA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `CreatePBRCancelButton` | `0xFCC0` | 153 | UnwindData |  |
| 38 | `CreatePBRErrorPage` | `0xFD60` | 109 | UnwindData |  |
| 39 | `CreatePBRFactoryResetKeepPackagesButton` | `0xFDE0` | 150 | UnwindData |  |
| 40 | `CreatePBRFactoryResetNotKeepPackagesButton` | `0xFE80` | 150 | UnwindData |  |
| 41 | `CreatePBRFinalPage` | `0xFF20` | 167 | UnwindData |  |
| 42 | `CreatePBRResetButtonCollection` | `0xFFD0` | 81 | UnwindData |  |
| 43 | `CreatePBRResetPage` | `0x10030` | 153 | UnwindData |  |
| 44 | `CreatePBRUsePayloadButton` | `0x100D0` | 150 | UnwindData |  |
| 45 | `CreatePBRUseReconstructionButton` | `0x10170` | 150 | UnwindData |  |
| 46 | `CreatePBRfactoryResetAllVolumesButton` | `0x10210` | 150 | UnwindData |  |
| 47 | `CreatePBRfactoryResetBareMetalDisabled` | `0x102B0` | 150 | UnwindData |  |
| 48 | `CreatePBRfactoryResetBareMetalEnabled` | `0x10350` | 150 | UnwindData |  |
| 49 | `CreatePBRfactoryResetCancelOperationButton` | `0x103F0` | 150 | UnwindData |  |
| 50 | `CreatePBRfactoryResetContinueChecksButton` | `0x10490` | 150 | UnwindData |  |
| 51 | `CreatePBRfactoryResetDataEraseDisabled` | `0x10530` | 150 | UnwindData |  |
| 52 | `CreatePBRfactoryResetDataEraseEnabled` | `0x105D0` | 150 | UnwindData |  |
| 53 | `CreatePBRfactoryResetOsOnlyButton` | `0x10670` | 150 | UnwindData |  |
| 54 | `CreatePasswordButton` | `0x10710` | 150 | UnwindData |  |
| 55 | `CreatePasswordPage` | `0x107B0` | 114 | UnwindData |  |
| 56 | `CreatePayloadWiFiNetworksCollection` | `0x10830` | 149 | UnwindData |  |
| 57 | `CreateRecoveryToolsListButton` | `0x108D0` | 229 | UnwindData |  |
| 58 | `CreateRestartButton` | `0x109C0` | 154 | UnwindData |  |
| 59 | `CreateSelectOSPage` | `0x10A60` | 111 | UnwindData |  |
| 60 | `CreateSetWallpaperPage` | `0x10AE0` | 130 | UnwindData |  |
| 61 | `CreateShutdownButton` | `0x10B70` | 196 | UnwindData |  |
| 62 | `CreateSkippableSelectOSPage` | `0x10C40` | 114 | UnwindData |  |
| 63 | `CreateSnapshotApplyButton` | `0x10CC0` | 177 | UnwindData |  |
| 64 | `CreateSnapshotsCollection` | `0x10D80` | 166 | UnwindData |  |
| 65 | `CreateSrtAcceptConsentButton` | `0x10E30` | 150 | UnwindData |  |
| 66 | `CreateSrtCountdownActionButton` | `0x10ED0` | 150 | UnwindData |  |
| 67 | `CreateSrtRetryCloudButton` | `0x10F70` | 150 | UnwindData |  |
| 68 | `CreateTenSecondTimeoutAction` | `0x11010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `CreateThirtySecondTimeoutAction` | `0x11030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `CreateTopLevelRecoveryToolsButtonCollection` | `0x11050` | 82 | UnwindData |  |
| 71 | `CreateTopLevelRecoveryToolsPage` | `0x110B0` | 152 | UnwindData |  |
| 72 | `CreateUninstallPage` | `0x11150` | 153 | UnwindData |  |
| 73 | `CreateUninstallQualityUpdateConfirmButton` | `0x111F0` | 151 | UnwindData |  |
| 74 | `CreateUninstallToolsButtonCollection` | `0x11290` | 81 | UnwindData |  |
| 75 | `CreateUserNameButtonCollection` | `0x112F0` | 141 | UnwindData |  |
| 76 | `CreateUserSelectionPage` | `0x11390` | 113 | UnwindData |  |
| 77 | `CreateWiFiConnectButton` | `0x11410` | 150 | UnwindData |  |
| 79 | `CreateWiFiNetworkButtonCollection` | `0x114B0` | 149 | UnwindData |  |
| 80 | `CreateWinReSkipPage` | `0x11550` | 109 | UnwindData |  |
| 81 | `CreateWinReTargetOSButtonCollection` | `0x115D0` | 148 | UnwindData |  |
| 82 | `CreateWinReTargetOSPage` | `0x11670` | 189 | UnwindData |  |
| 83 | `CreateZeroSecondTimeoutAction` | `0x11740` | 1,904 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `InitializeGenericInterface` | `0x11EB0` | 114 | UnwindData |  |
| 85 | `InitializePITRInterface` | `0x11F30` | 65 | UnwindData |  |
| 86 | `InitializePasswordDatabase` | `0x11F80` | 46 | UnwindData |  |
| 87 | `InitializePostUnlockInterface` | `0x11FC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `InitializeSRTSyncInterface` | `0x11FE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `InitializeSyncInterface` | `0x12010` | 72 | UnwindData |  |
| 90 | `SetPBRErrorCode` | `0x12200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `SetPBRErrorPhase` | `0x12210` | 104,967 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
