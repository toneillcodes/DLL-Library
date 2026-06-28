# Binary Specification: ReAgent.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ReAgent.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `836c9b6df70f5972b04ac497247556d8fe80af9efd27671fb2ba1506dfb722b1`
* **Total Exported Functions:** 76

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 14 | `WinReClearError` | `0xD440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `WinReGetConfig` | `0xD450` | 153 | UnwindData |  |
| 27 | `WinReGetError` | `0xDB40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `WinReIsWinPE` | `0xDB50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `WinReSetError` | `0xDB60` | 41,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `WinRE_Specialize` | `0x17E30` | 151 | UnwindData |  |
| 2 | `WinRE_Specialize_Offline` | `0x17ED0` | 419 | UnwindData |  |
| 4 | `WinReInstallTarget` | `0x18750` | 1,951 | UnwindData |  |
| 36 | `WinReInstall` | `0x194B0` | 166 | UnwindData |  |
| 37 | `WinReInstallOnTargetOS` | `0x19560` | 272 | UnwindData |  |
| 46 | `WinReReinstall` | `0x19680` | 286 | UnwindData |  |
| 64 | `WinReSetupInstall` | `0x197B0` | 995 | UnwindData |  |
| 3 | `WinReClearOemImagePath` | `0x1D940` | 489 | UnwindData |  |
| 5 | `WinReRegisterRecoveryBoot` | `0x1E000` | 428 | UnwindData |  |
| 7 | `WinRECheckGuid` | `0x1FD10` | 254 | UnwindData |  |
| 8 | `WinREUpdateWinREHash` | `0x1FE20` | 152 | UnwindData |  |
| 9 | `WinREUseNewPBRImage` | `0x20050` | 126 | UnwindData |  |
| 10 | `WinRE_Generalize` | `0x203D0` | 70 | UnwindData |  |
| 11 | `WinReAddTrustedBootApp` | `0x20420` | 171 | UnwindData |  |
| 12 | `WinReClearAllSettings` | `0x204E0` | 357 | UnwindData |  |
| 13 | `WinReClearBootApp` | `0x20650` | 152 | UnwindData |  |
| 15 | `WinReClearRecoveryTestMode` | `0x206F0` | 749 | UnwindData |  |
| 16 | `WinReClearSetting` | `0x209F0` | 790 | UnwindData |  |
| 17 | `WinReClearSettingEx` | `0x20D10` | 834 | UnwindData |  |
| 18 | `WinReConfigureTask` | `0x21060` | 1,715 | UnwindData |  |
| 19 | `WinReCopyDiagnosticFiles` | `0x21720` | 162 | UnwindData |  |
| 24 | `WinReDumpSettings` | `0x217D0` | 1,764 | UnwindData |  |
| 26 | `WinReGetCustomization` | `0x21EC0` | 713 | UnwindData |  |
| 29 | `WinReGetRecoveryTestMode` | `0x222F0` | 2,000 | UnwindData |  |
| 30 | `WinReGetSetting` | `0x22AD0` | 1,215 | UnwindData |  |
| 31 | `WinReGetTrustedBootApps` | `0x22FA0` | 168 | UnwindData |  |
| 32 | `WinReGetWIMInfo` | `0x23050` | 533 | UnwindData |  |
| 33 | `WinReHashBootApp` | `0x23270` | 163 | UnwindData |  |
| 34 | `WinReHashWimFile` | `0x23320` | 128 | UnwindData |  |
| 35 | `WinReInitiateOfflineScanning` | `0x233B0` | 1,046 | UnwindData |  |
| 38 | `WinReIsInstalledOnSystemPartition` | `0x237D0` | 135 | UnwindData |  |
| 39 | `WinReIsSettingManaged` | `0x23C00` | 929 | UnwindData |  |
| 40 | `WinReIsWimBootEnabled` | `0x23FB0` | 142 | UnwindData |  |
| 42 | `WinReOobeInstall` | `0x24050` | 495 | UnwindData |  |
| 44 | `WinRePostBCDRepair` | `0x24250` | 980 | UnwindData |  |
| 45 | `WinReQueueRecoveryBoot` | `0x24630` | 370 | UnwindData |  |
| 47 | `WinReRemoveTrustedBootApp` | `0x247B0` | 155 | UnwindData |  |
| 48 | `WinReRepair` | `0x24860` | 1,420 | UnwindData |  |
| 49 | `WinReRepairEx` | `0x24E00` | 947 | UnwindData |  |
| 51 | `WinReSetBootApp` | `0x251C0` | 168 | UnwindData |  |
| 52 | `WinReSetConfig` | `0x25270` | 148 | UnwindData |  |
| 53 | `WinReSetCustomization` | `0x25970` | 158 | UnwindData |  |
| 55 | `WinReSetNarratorScheduled` | `0x25D20` | 505 | UnwindData |  |
| 56 | `WinReSetRecoveryAction` | `0x25F20` | 983 | UnwindData |  |
| 57 | `WinReSetRecoveryTestMode` | `0x26300` | 1,243 | UnwindData |  |
| 58 | `WinReSetSetting` | `0x267F0` | 1,215 | UnwindData |  |
| 59 | `WinReSetSettingEx` | `0x26CC0` | 1,254 | UnwindData |  |
| 60 | `WinReSetSettings` | `0x271B0` | 1,491 | UnwindData |  |
| 71 | `WinReUnInstall` | `0x27790` | 164 | UnwindData |  |
| 73 | `WinReValidateRecoveryWim` | `0x27840` | 105 | UnwindData |  |
| 74 | `WinReValidateWimFile` | `0x27CE0` | 144 | UnwindData |  |
| 6 | `WinReRestoreConfigAfterPBR` | `0x29C80` | 3,594 | UnwindData |  |
| 20 | `WinReCopyLogFilesToRamdisk` | `0x2B3F0` | 153 | UnwindData |  |
| 21 | `WinReCreateLogInstance` | `0x2B490` | 44 | UnwindData |  |
| 22 | `WinReCreateLogInstanceEx` | `0x2B4D0` | 324 | UnwindData |  |
| 23 | `WinReDeleteLogFiles` | `0x2B620` | 101 | UnwindData |  |
| 28 | `WinReGetLogDirPath` | `0x2B720` | 71 | UnwindData |  |
| 43 | `WinReOpenLogInstance` | `0x2BA60` | 650 | UnwindData |  |
| 50 | `WinReRestoreLogFiles` | `0x2BCF0` | 150 | UnwindData |  |
| 61 | `WinReSetTriggerFile` | `0x2BD90` | 671 | UnwindData |  |
| 72 | `WinReUpdateLogInstance` | `0x2C040` | 611 | UnwindData |  |
| 62 | `WinReSetupBackupWinRE` | `0x2E460` | 3,406 | UnwindData |  |
| 63 | `WinReSetupCheckWinRE` | `0x2F1C0` | 341 | UnwindData |  |
| 65 | `WinReSetupMigrateData` | `0x2F320` | 814 | UnwindData |  |
| 66 | `WinReSetupMigrateOEMTools` | `0x2F660` | 541 | UnwindData |  |
| 67 | `WinReSetupRemoveWinRE` | `0x2F890` | 460 | UnwindData |  |
| 68 | `WinReSetupRestoreWinREEx` | `0x2FA70` | 298 | UnwindData |  |
| 69 | `WinReSetupSaveWinREPartitionInfo` | `0x2FBA0` | 679 | UnwindData |  |
| 70 | `WinReSetupSetImage` | `0x2FE50` | 2,988 | UnwindData |  |
| 75 | `winreFindInstallMedia` | `0x30A10` | 819 | UnwindData |  |
| 76 | `winreGetBinaryArch` | `0x31BD0` | 397 | UnwindData |  |
