# Binary Specification: ReAgent.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ReAgent.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `74dbda7c17b6588297da92b895dbd1d495975b8b5c800ccf1f4e4a5ec96dba11`
* **Total Exported Functions:** 78

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 14 | `WinReClearError` | `0xCF30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `WinReGetConfig` | `0xCF40` | 153 | UnwindData |  |
| 27 | `WinReGetError` | `0xD630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `WinReIsWinPE` | `0xD640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `WinReSetError` | `0xD650` | 42,976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `WinRE_Specialize` | `0x17E30` | 161 | UnwindData |  |
| 2 | `WinRE_Specialize_Offline` | `0x17EE0` | 419 | UnwindData |  |
| 4 | `WinReInstallTarget` | `0x18750` | 1,807 | UnwindData |  |
| 37 | `WinReInstall` | `0x19420` | 174 | UnwindData |  |
| 38 | `WinReInstallOnTargetOS` | `0x194E0` | 282 | UnwindData |  |
| 39 | `WinReInstallOnTargetOSEx` | `0x19600` | 327 | UnwindData |  |
| 48 | `WinReReinstall` | `0x19750` | 296 | UnwindData |  |
| 66 | `WinReSetupInstall` | `0x19880` | 1,006 | UnwindData |  |
| 3 | `WinReClearOemImagePath` | `0x1D590` | 489 | UnwindData |  |
| 5 | `WinReRegisterRecoveryBoot` | `0x1DC50` | 428 | UnwindData |  |
| 7 | `WinRECheckGuid` | `0x1F640` | 254 | UnwindData |  |
| 8 | `WinREUpdateWinREHash` | `0x1F750` | 115 | UnwindData |  |
| 9 | `WinREUseNewPBRImage` | `0x1F960` | 126 | UnwindData |  |
| 10 | `WinRE_Generalize` | `0x1FCE0` | 70 | UnwindData |  |
| 11 | `WinReAddTrustedBootApp` | `0x1FD30` | 171 | UnwindData |  |
| 12 | `WinReClearAllSettings` | `0x1FDF0` | 333 | UnwindData |  |
| 13 | `WinReClearBootApp` | `0x1FF50` | 152 | UnwindData |  |
| 15 | `WinReClearRecoveryTestMode` | `0x1FFF0` | 620 | UnwindData |  |
| 16 | `WinReClearSetting` | `0x20270` | 766 | UnwindData |  |
| 17 | `WinReClearSettingEx` | `0x20580` | 810 | UnwindData |  |
| 18 | `WinReConfigureTask` | `0x208B0` | 1,715 | UnwindData |  |
| 19 | `WinReCopyDiagnosticFiles` | `0x20F70` | 162 | UnwindData |  |
| 24 | `WinReDumpSettings` | `0x21020` | 1,792 | UnwindData |  |
| 26 | `WinReGetCustomization` | `0x21730` | 713 | UnwindData |  |
| 29 | `WinReGetRecoveryTestMode` | `0x21B60` | 1,711 | UnwindData |  |
| 30 | `WinReGetSetting` | `0x22220` | 1,069 | UnwindData |  |
| 31 | `WinReGetTrustedBootApps` | `0x22660` | 168 | UnwindData |  |
| 32 | `WinReGetWIMInfo` | `0x22710` | 533 | UnwindData |  |
| 33 | `WinReGetWimVersion` | `0x22930` | 660 | UnwindData |  |
| 34 | `WinReHashBootApp` | `0x22BD0` | 163 | UnwindData |  |
| 35 | `WinReHashWimFile` | `0x22C80` | 128 | UnwindData |  |
| 36 | `WinReInitiateOfflineScanning` | `0x22D10` | 1,046 | UnwindData |  |
| 40 | `WinReIsInstalledOnSystemPartition` | `0x23130` | 135 | UnwindData |  |
| 41 | `WinReIsSettingManaged` | `0x23560` | 905 | UnwindData |  |
| 42 | `WinReIsWimBootEnabled` | `0x238F0` | 142 | UnwindData |  |
| 44 | `WinReOobeInstall` | `0x23990` | 503 | UnwindData |  |
| 46 | `WinRePostBCDRepair` | `0x23B90` | 980 | UnwindData |  |
| 47 | `WinReQueueRecoveryBoot` | `0x23F70` | 370 | UnwindData |  |
| 49 | `WinReRemoveTrustedBootApp` | `0x240F0` | 155 | UnwindData |  |
| 50 | `WinReRepair` | `0x241A0` | 1,427 | UnwindData |  |
| 51 | `WinReRepairEx` | `0x24740` | 947 | UnwindData |  |
| 53 | `WinReSetBootApp` | `0x24B00` | 168 | UnwindData |  |
| 54 | `WinReSetConfig` | `0x24BB0` | 148 | UnwindData |  |
| 55 | `WinReSetCustomization` | `0x252B0` | 158 | UnwindData |  |
| 57 | `WinReSetNarratorScheduled` | `0x25660` | 505 | UnwindData |  |
| 58 | `WinReSetRecoveryAction` | `0x25860` | 983 | UnwindData |  |
| 59 | `WinReSetRecoveryTestMode` | `0x25C40` | 1,088 | UnwindData |  |
| 60 | `WinReSetSetting` | `0x26090` | 1,191 | UnwindData |  |
| 61 | `WinReSetSettingEx` | `0x26540` | 1,230 | UnwindData |  |
| 62 | `WinReSetSettings` | `0x26A20` | 1,455 | UnwindData |  |
| 73 | `WinReUnInstall` | `0x26FE0` | 164 | UnwindData |  |
| 75 | `WinReValidateRecoveryWim` | `0x27090` | 105 | UnwindData |  |
| 76 | `WinReValidateWimFile` | `0x27530` | 144 | UnwindData |  |
| 6 | `WinReRestoreConfigAfterPBR` | `0x294B0` | 3,594 | UnwindData |  |
| 20 | `WinReCopyLogFilesToRamdisk` | `0x2AC20` | 153 | UnwindData |  |
| 21 | `WinReCreateLogInstance` | `0x2ACC0` | 44 | UnwindData |  |
| 22 | `WinReCreateLogInstanceEx` | `0x2AD00` | 324 | UnwindData |  |
| 23 | `WinReDeleteLogFiles` | `0x2AE50` | 101 | UnwindData |  |
| 28 | `WinReGetLogDirPath` | `0x2AF50` | 71 | UnwindData |  |
| 45 | `WinReOpenLogInstance` | `0x2B290` | 650 | UnwindData |  |
| 52 | `WinReRestoreLogFiles` | `0x2B520` | 150 | UnwindData |  |
| 63 | `WinReSetTriggerFile` | `0x2B5C0` | 671 | UnwindData |  |
| 74 | `WinReUpdateLogInstance` | `0x2B870` | 611 | UnwindData |  |
| 64 | `WinReSetupBackupWinRE` | `0x2E300` | 3,406 | UnwindData |  |
| 65 | `WinReSetupCheckWinRE` | `0x2F060` | 341 | UnwindData |  |
| 67 | `WinReSetupMigrateData` | `0x2F1C0` | 791 | UnwindData |  |
| 68 | `WinReSetupMigrateOEMTools` | `0x2F4E0` | 541 | UnwindData |  |
| 69 | `WinReSetupRemoveWinRE` | `0x2F710` | 460 | UnwindData |  |
| 70 | `WinReSetupRestoreWinREEx` | `0x2F8F0` | 298 | UnwindData |  |
| 71 | `WinReSetupSaveWinREPartitionInfo` | `0x2FA20` | 679 | UnwindData |  |
| 72 | `WinReSetupSetImage` | `0x2FCD0` | 2,988 | UnwindData |  |
| 77 | `winreFindInstallMedia` | `0x30890` | 819 | UnwindData |  |
| 78 | `winreGetBinaryArch` | `0x31A50` | 397 | UnwindData |  |
