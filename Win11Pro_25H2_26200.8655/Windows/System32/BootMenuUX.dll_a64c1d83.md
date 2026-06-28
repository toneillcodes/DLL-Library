# Binary Specification: BootMenuUX.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\BootMenuUX.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a64c1d836d23523dfb8b0265f382f2a6dee771502c502fce3509a791a695f45a`
* **Total Exported Functions:** 102

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 101 | `UtilBcdCloseSystemStore` | `0x9DC0` | 50 | UnwindData |  |
| 102 | `UtilGetCurrentKeyboardLayout` | `0xB3B0` | 215 | UnwindData |  |
| 1 | `CreateAdvancedOptionsButton` | `0xF2A0` | 148 | UnwindData |  |
| 2 | `CreateAdvancedRecoveryToolsButtonCollection` | `0xF340` | 81 | UnwindData |  |
| 3 | `CreateAdvancedStartupButton` | `0xF3A0` | 197 | UnwindData |  |
| 4 | `CreateAdvancedStartupLaunchPage` | `0xF470` | 126 | UnwindData |  |
| 5 | `CreateBareMetalRecoveryButton` | `0xF500` | 407 | UnwindData |  |
| 6 | `CreateBasicResetFinalChecksPage` | `0xF6A0` | 114 | UnwindData |  |
| 81 | `CreateWiFiInitPage` | `0xF6A0` | 114 | UnwindData |  |
| 7 | `CreateBasicResetLandingPage` | `0xF720` | 167 | UnwindData |  |
| 8 | `CreateBasicSystemResetButton` | `0xF7D0` | 155 | UnwindData |  |
| 9 | `CreateBasicSystemResetLaunchPage` | `0xF880` | 251 | UnwindData |  |
| 10 | `CreateBitlockerLandingPage` | `0xF990` | 175 | UnwindData |  |
| 11 | `CreateBlackWallpaperButton` | `0xFA50` | 153 | UnwindData |  |
| 12 | `CreateBootableDeviceButtonCollection` | `0xFBB0` | 83 | UnwindData |  |
| 13 | `CreateBootableOSButtonCollection` | `0xFC10` | 111 | UnwindData |  |
| 14 | `CreateCPITRFinalPage` | `0xFC90` | 133 | UnwindData |  |
| 15 | `CreateCSRTFinalPage` | `0xFD20` | 109 | UnwindData |  |
| 16 | `CreateClearWallpaperPage` | `0xFDA0` | 133 | UnwindData |  |
| 17 | `CreateDefaultOSButton` | `0xFE30` | 250 | UnwindData |  |
| 18 | `CreateDefaultOSButtonCollection` | `0xFF30` | 111 | UnwindData |  |
| 19 | `CreateDefaultOSListButton` | `0xFFB0` | 233 | UnwindData |  |
| 20 | `CreateDeviceListButton` | `0x100A0` | 247 | UnwindData |  |
| 21 | `CreateDeviceRebuildPage` | `0x101A0` | 133 | UnwindData |  |
| 22 | `CreateDirectFactoryResetButton` | `0x10230` | 198 | UnwindData |  |
| 23 | `CreateDownloadCloudPBRConfirmButton` | `0x10300` | 151 | UnwindData |  |
| 24 | `CreateErrorRetryButton` | `0x103A0` | 174 | UnwindData |  |
| 25 | `CreateFactoryResetFinalChecksPage` | `0x10460` | 111 | UnwindData |  |
| 33 | `CreateFlightRemovalProgressPage` | `0x10460` | 111 | UnwindData |  |
| 26 | `CreateFactoryResetLandingPage` | `0x104E0` | 167 | UnwindData |  |
| 27 | `CreateFactorySystemResetButton` | `0x10590` | 155 | UnwindData |  |
| 28 | `CreateFactorySystemResetLaunchPage` | `0x10640` | 251 | UnwindData |  |
| 29 | `CreateFirmwareSettingsButton` | `0x10750` | 157 | UnwindData |  |
| 30 | `CreateFiveMinuteTimeoutAction` | `0x10800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `CreateFiveSecondTimeoutAction` | `0x10820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `CreateFlightRemovalConfirmButton` | `0x10840` | 151 | UnwindData |  |
| 34 | `CreateGenericWiFiNetworksCollection` | `0x108E0` | 149 | UnwindData |  |
| 35 | `CreateKeyboardLayoutButtonCollection` | `0x10980` | 1,103 | UnwindData |  |
| 36 | `CreateLanguageButtonCollection` | `0x10DE0` | 381 | UnwindData |  |
| 37 | `CreateOSListButton` | `0x10F70` | 242 | UnwindData |  |
| 38 | `CreateOneMinuteTimeoutAction` | `0x11070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `CreatePBRCancelButton` | `0x11090` | 153 | UnwindData |  |
| 40 | `CreatePBRErrorPage` | `0x11130` | 109 | UnwindData |  |
| 41 | `CreatePBRFactoryResetKeepPackagesButton` | `0x111B0` | 150 | UnwindData |  |
| 42 | `CreatePBRFactoryResetNotKeepPackagesButton` | `0x11250` | 150 | UnwindData |  |
| 43 | `CreatePBRFinalPage` | `0x112F0` | 167 | UnwindData |  |
| 44 | `CreatePBRResetButtonCollection` | `0x113A0` | 81 | UnwindData |  |
| 45 | `CreatePBRResetPage` | `0x11400` | 153 | UnwindData |  |
| 46 | `CreatePBRUsePayloadButton` | `0x114A0` | 150 | UnwindData |  |
| 47 | `CreatePBRUseReconstructionButton` | `0x11540` | 150 | UnwindData |  |
| 48 | `CreatePBRfactoryResetAllVolumesButton` | `0x115E0` | 150 | UnwindData |  |
| 49 | `CreatePBRfactoryResetBareMetalDisabled` | `0x11680` | 150 | UnwindData |  |
| 50 | `CreatePBRfactoryResetBareMetalEnabled` | `0x11720` | 150 | UnwindData |  |
| 51 | `CreatePBRfactoryResetCancelOperationButton` | `0x117C0` | 150 | UnwindData |  |
| 52 | `CreatePBRfactoryResetContinueChecksButton` | `0x11860` | 150 | UnwindData |  |
| 53 | `CreatePBRfactoryResetDataEraseDisabled` | `0x11900` | 150 | UnwindData |  |
| 54 | `CreatePBRfactoryResetDataEraseEnabled` | `0x119A0` | 150 | UnwindData |  |
| 55 | `CreatePBRfactoryResetOsOnlyButton` | `0x11A40` | 150 | UnwindData |  |
| 56 | `CreatePasswordButton` | `0x11AE0` | 150 | UnwindData |  |
| 57 | `CreatePasswordPage` | `0x11B80` | 114 | UnwindData |  |
| 58 | `CreatePayloadWiFiNetworksCollection` | `0x11C00` | 149 | UnwindData |  |
| 59 | `CreateRecoveryToolsListButton` | `0x11CA0` | 359 | UnwindData |  |
| 60 | `CreateRestartButton` | `0x11E10` | 154 | UnwindData |  |
| 61 | `CreateRestartNoTrustButton` | `0x11EB0` | 181 | UnwindData |  |
| 62 | `CreateSelectOSPage` | `0x11F70` | 111 | UnwindData |  |
| 63 | `CreateSetWallpaperPage` | `0x11FF0` | 130 | UnwindData |  |
| 64 | `CreateShutdownButton` | `0x12080` | 196 | UnwindData |  |
| 65 | `CreateSkippableSelectOSPage` | `0x12150` | 114 | UnwindData |  |
| 66 | `CreateSnapshotApplyButton` | `0x121D0` | 177 | UnwindData |  |
| 67 | `CreateSnapshotsCollection` | `0x12290` | 166 | UnwindData |  |
| 68 | `CreateSrtAcceptConsentButton` | `0x12340` | 150 | UnwindData |  |
| 69 | `CreateSrtCountdownActionButton` | `0x123E0` | 150 | UnwindData |  |
| 70 | `CreateSrtRetryCloudButton` | `0x12480` | 150 | UnwindData |  |
| 71 | `CreateTenSecondTimeoutAction` | `0x12520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `CreateThirtySecondTimeoutAction` | `0x12540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `CreateTopLevelRecoveryToolsButtonCollection` | `0x12560` | 82 | UnwindData |  |
| 74 | `CreateTopLevelRecoveryToolsPage` | `0x125C0` | 152 | UnwindData |  |
| 75 | `CreateUninstallPage` | `0x12660` | 153 | UnwindData |  |
| 76 | `CreateUninstallQualityUpdateConfirmButton` | `0x12700` | 151 | UnwindData |  |
| 77 | `CreateUninstallToolsButtonCollection` | `0x127A0` | 81 | UnwindData |  |
| 78 | `CreateUserNameButtonCollection` | `0x12800` | 141 | UnwindData |  |
| 79 | `CreateUserSelectionPage` | `0x128A0` | 113 | UnwindData |  |
| 80 | `CreateWiFiConnectButton` | `0x12920` | 150 | UnwindData |  |
| 82 | `CreateWiFiNetworkButtonCollection` | `0x129C0` | 149 | UnwindData |  |
| 83 | `CreateWinREErrorPage` | `0x12A60` | 133 | UnwindData |  |
| 84 | `CreateWinReSkipPage` | `0x12AF0` | 109 | UnwindData |  |
| 85 | `CreateWinReTargetOSButtonCollection` | `0x12B70` | 148 | UnwindData |  |
| 86 | `CreateWinReTargetOSPage` | `0x12C10` | 189 | UnwindData |  |
| 87 | `CreateZeroSecondTimeoutAction` | `0x12CE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `FindButtonById` | `0x12D00` | 558 | UnwindData |  |
| 89 | `GetUxClassTable` | `0x131F0` | 550 | UnwindData |  |
| 90 | `InitializeErrorPageInterface` | `0x135B0` | 65 | UnwindData |  |
| 91 | `InitializeGenericInterface` | `0x13600` | 114 | UnwindData |  |
| 92 | `InitializePITRInterface` | `0x13680` | 65 | UnwindData |  |
| 93 | `InitializePasswordDatabase` | `0x136D0` | 46 | UnwindData |  |
| 94 | `InitializePostUnlockInterface` | `0x13710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `InitializeRebuildInterface` | `0x13730` | 65 | UnwindData |  |
| 96 | `InitializeSRTSyncInterface` | `0x13780` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `InitializeSyncInterface` | `0x137B0` | 72 | UnwindData |  |
| 98 | `SetPBRErrorCode` | `0x13B20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `SetPBRErrorPhase` | `0x13B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `SyncSelectedSnapshot` | `0x13B40` | 158 | UnwindData |  |
