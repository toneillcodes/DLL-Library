# Binary Specification: BdeHdCfgLib.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\BdeHdCfgLib.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `28f4dbd98ffc3b86cd9a5354a7f6732e23e10eae0f12877ddea01cf40e217cb9`
* **Total Exported Functions:** 114

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `??0CBcdStore@@IEAA@XZ` | `0x1AB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0CBcdStore@@QEAA@$$QEAV0@@Z` | `0x1AE0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0CBcdStore@@QEAA@AEBV0@@Z` | `0x1AE0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `??0CBcdWmiWrapper@@QEAA@AEBV0@@Z` | `0x1B20` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `??0CBdeCfgLibraryLoader@@QEAA@AEBV0@@Z` | `0x1B60` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `??4CBdeCfgLibraryLoader@@QEAAAEAV0@AEBV0@@Z` | `0x1B60` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `??0CDriveConfiguration@@QEAA@AEBV0@@Z` | `0x1BA0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `??4CDriveConfiguration@@QEAAAEAV0@AEBV0@@Z` | `0x1BA0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `??1CBcdStore@@UEAA@XZ` | `0x1CF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `??4CBcdStore@@QEAAAEAV0@$$QEAV0@@Z` | `0x1D00` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `??4CBcdStore@@QEAAAEAV0@AEBV0@@Z` | `0x1D00` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `??4CBcdWmiWrapper@@QEAAAEAV0@AEBV0@@Z` | `0x1D00` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `?GetConfigurationResult@CDriveConfiguration@@QEAAJXZ` | `0x1E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `?GetInitializationResult@CDriveConfiguration@@QEAAJXZ` | `0x1E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `?Initialized@CDriveConfiguration@@QEAA_NXZ` | `0x1E70` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `BdeCfgCanCreateActivePartOnDisk` | `0x2000` | 212 | UnwindData |  |
| 26 | `BdeCfgCheckAndGetBootVolume` | `0x20E0` | 57 | UnwindData |  |
| 27 | `BdeCfgCheckGPTRecoveryPartition` | `0x2120` | 423 | UnwindData |  |
| 28 | `BdeCfgCheckVolumeAsCandidate` | `0x22D0` | 960 | UnwindData |  |
| 30 | `BdeCfgCountGPTPartitions` | `0x2A90` | 310 | UnwindData |  |
| 31 | `BdeCfgCreateWinREPartitionGPT` | `0x2EA0` | 542 | UnwindData |  |
| 35 | `BdeCfgFindBasicVolumeExtent` | `0x3210` | 468 | UnwindData |  |
| 36 | `BdeCfgFindCandidateVolumes` | `0x33F0` | 1,171 | UnwindData |  |
| 37 | `BdeCfgFindGPTRecoveryPartitionCandidate` | `0x3890` | 472 | UnwindData |  |
| 38 | `BdeCfgFindLargestUnallocatedExtent` | `0x3A70` | 303 | UnwindData |  |
| 39 | `BdeCfgFindRecoveryPartitionGPT` | `0x3BB0` | 538 | UnwindData |  |
| 40 | `BdeCfgFindVolumeWithName` | `0x3DD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `BdeCfgFindVolumeWithProp` | `0x3DF0` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `BdeCfgGetBootVolume` | `0x3F70` | 138 | UnwindData |  |
| 43 | `BdeCfgGetDeviceNameFromVolume` | `0x4000` | 164 | UnwindData |  |
| 44 | `BdeCfgGetMaxShrinkSize` | `0x40B0` | 123 | UnwindData |  |
| 45 | `BdeCfgGetNtfsVolumeSize` | `0x4140` | 352 | UnwindData |  |
| 46 | `BdeCfgGetVolumeDisk` | `0x42B0` | 485 | UnwindData |  |
| 48 | `BdeCfgGetVolumeFromId` | `0x44A0` | 148 | UnwindData |  |
| 49 | `BdeCfgInitialize` | `0x4650` | 297 | UnwindData |  |
| 50 | `BdeCfgIsDiskConfiguredForBitLocker` | `0x4780` | 194 | UnwindData |  |
| 52 | `BdeCfgIsWinREOnOSVolume` | `0x4960` | 350 | UnwindData |  |
| 56 | `BdeCfgMoveWinRE` | `0x4AD0` | 98 | UnwindData |  |
| 58 | `BdeCfgSecureFormatPartition` | `0x4B40` | 311 | UnwindData |  |
| 59 | `BdeCfgShrinkSimpleVolume` | `0x4DC0` | 179 | UnwindData |  |
| 60 | `BdeCfgUninitialize` | `0x4E80` | 44 | UnwindData |  |
| 24 | `BdeCfgCalculateSizeRequirements` | `0x6E70` | 286 | UnwindData |  |
| 29 | `BdeCfgCleanupOldBootFiles` | `0x6FA0` | 230 | UnwindData |  |
| 32 | `BdeCfgDetectWinRESize` | `0x7090` | 174 | UnwindData |  |
| 33 | `BdeCfgDetectWinREVolumeName` | `0x7150` | 617 | UnwindData |  |
| 34 | `BdeCfgDisableWinRE` | `0x73C0` | 34 | UnwindData |  |
| 47 | `BdeCfgGetVolumeDriveLetter` | `0x73F0` | 444 | UnwindData |  |
| 51 | `BdeCfgIsElevated` | `0x7780` | 267 | UnwindData |  |
| 53 | `BdeCfgLoadErrorString` | `0x79F0` | 505 | UnwindData |  |
| 54 | `BdeCfgLoadResourceString` | `0x7BF0` | 339 | UnwindData |  |
| 55 | `BdeCfgMigrateBootHive` | `0x7D50` | 675 | UnwindData |  |
| 57 | `BdeCfgRestart` | `0x8000` | 102 | UnwindData |  |
| 4 | `??0CBcdWmiWrapper@@IEAA@XZ` | `0x9F70` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `??1CBcdWmiWrapper@@MEAA@XZ` | `0xA010` | 104 | UnwindData |  |
| 66 | `?CreateClass@CBcdStore@@SAJPEAPEAV1@@Z` | `0xA380` | 157 | UnwindData |  |
| 67 | `?CreateInParams@CBcdWmiWrapper@@IEAAJPEBGPEAPEAUIWbemClassObject@@@Z` | `0xA430` | 200 | UnwindData |  |
| 70 | `?ExecuteMethod@CBcdWmiWrapper@@IEAAJPEBGPEAUIWbemClassObject@@PEAPEAU2@@Z` | `0xA920` | 390 | UnwindData |  |
| 71 | `?ExportSystemStore@CBcdStore@@QEAAJPEBG@Z` | `0xAAB0` | 274 | UnwindData |  |
| 75 | `?GetNamespace@CBcdWmiWrapper@@IEAAPEAUIWbemServices@@XZ` | `0xBDE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `?ImportSystemStore@CBcdStore@@QEAAJPEBG@Z` | `0xBDF0` | 274 | UnwindData |  |
| 89 | `?InitializeClass@CBcdWmiWrapper@@IEAAJPEBG@Z` | `0xBF10` | 147 | UnwindData |  |
| 92 | `?InitializeInstance@CBcdWmiWrapper@@IEAAJPEAUIWbemServices@@PEAUIWbemClassObject@@@Z` | `0xBFB0` | 512 | UnwindData |  |
| 93 | `?InitializeNamespace@CBcdWmiWrapper@@AEAAJXZ` | `0xC1C0` | 308 | UnwindData |  |
| 98 | `?OpenStore@CBcdStore@@QEAAJPEBGPEAPEAV1@@Z` | `0xC300` | 688 | UnwindData |  |
| 100 | `?RemapObjectDevices@CBcdStore@@QEAAJPEBG0@Z` | `0xC990` | 888 | UnwindData |  |
| 7 | `??0CBdeCfgLibraryLoader@@QEAA@XZ` | `0xDD80` | 47 | UnwindData |  |
| 12 | `??1CBdeCfgLibraryLoader@@QEAA@XZ` | `0xDDC0` | 100 | UnwindData |  |
| 86 | `?InitializeAndHoldLibrary@CBdeCfgLibraryLoader@@AEAAJXZ` | `0xDE30` | 36 | UnwindData |  |
| 87 | `?InitializeAndHoldLibraryEntry@CBdeCfgLibraryLoader@@CAXPEAX@Z` | `0xDE60` | 144 | UnwindData |  |
| 88 | `?InitializeAndHoldLibrary_Thread@CBdeCfgLibraryLoader@@AEAAJXZ` | `0xDF00` | 109 | UnwindData |  |
| 96 | `?LibraryLoaded@CBdeCfgLibraryLoader@@QEAA_NXZ` | `0xDF80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `?Load@CBdeCfgLibraryLoader@@QEAAJXZ` | `0xDF90` | 233 | UnwindData |  |
| 104 | `?Unload@CBdeCfgLibraryLoader@@QEAAXXZ` | `0xE080` | 82 | UnwindData |  |
| 105 | `BdeCfgLogCandidateDrive` | `0xE1E0` | 488 | UnwindData |  |
| 106 | `BdeCfgLogClose` | `0xE3D0` | 56 | UnwindData |  |
| 107 | `BdeCfgLogCommandLineParams` | `0xE410` | 739 | UnwindData |  |
| 108 | `BdeCfgLogDetectedWinRE` | `0xE700` | 506 | UnwindData |  |
| 109 | `BdeCfgLogEnumExtent` | `0xE900` | 35 | UnwindData |  |
| 110 | `BdeCfgLogError` | `0xE930` | 563 | UnwindData |  |
| 111 | `BdeCfgLogFailedTarget` | `0xEB70` | 581 | UnwindData |  |
| 112 | `BdeCfgLogFoundUnallocatedExtent` | `0xEDC0` | 56 | UnwindData |  |
| 113 | `BdeCfgLogInit` | `0xEE00` | 53 | UnwindData |  |
| 114 | `BdeCfgLogWarning` | `0xF1D0` | 335 | UnwindData |  |
| 9 | `??0CDriveConfiguration@@QEAA@XZ` | `0xF7E0` | 114 | UnwindData |  |
| 13 | `??1CDriveConfiguration@@QEAA@XZ` | `0xF860` | 138 | UnwindData |  |
| 21 | `?ActionRequiresCreate@CDriveConfiguration@@QEAA_NXZ` | `0xF8F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `?ActionRequiresMerge@CDriveConfiguration@@QEAA_NXZ` | `0xF910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `?ActionRequiresShrink@CDriveConfiguration@@QEAA_NXZ` | `0xF920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `?CancelConfiguration@CDriveConfiguration@@QEAAJXZ` | `0xF930` | 40 | UnwindData |  |
| 62 | `?CancelConfigurationEntry@CDriveConfiguration@@CAXPEAX@Z` | `0xF960` | 60 | UnwindData |  |
| 63 | `?CancelConfiguration_Thread@CDriveConfiguration@@AEAAJXZ` | `0xF9B0` | 255 | UnwindData |  |
| 64 | `?Cleanup@CDriveConfiguration@@AEAAXXZ` | `0xFAC0` | 147 | UnwindData |  |
| 65 | `?ConfigureDrive@CDriveConfiguration@@QEAAJXZ` | `0xFB60` | 36 | UnwindData |  |
| 68 | `?DetectTargetDrive@CDriveConfiguration@@AEAAJPEAUIVdsVolume@@@Z` | `0xFB90` | 1,114 | UnwindData |  |
| 69 | `?DriveConfigurationEntry@CDriveConfiguration@@CAXPEAX@Z` | `0xFFF0` | 56 | UnwindData |  |
| 72 | `?GetActionType@CDriveConfiguration@@QEAA?AW4BDECFG_ACTION_TYPE@@XZ` | `0x10030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `?GetNewDriveLetter@CDriveConfiguration@@QEAAGXZ` | `0x10040` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `?GetNumberOfSteps@CDriveConfiguration@@QEAAKXZ` | `0x10070` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `?GetShrinkSize@CDriveConfiguration@@QEAA_KXZ` | `0x100B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `?GetStepExecutionOrder@CDriveConfiguration@@QEAAKW4_BDECFG_STEP_ID@@@Z` | `0x100C0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `?GetTargetDiskNumber@CDriveConfiguration@@QEAAKXZ` | `0x10120` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `?GetTargetDriveLetter@CDriveConfiguration@@QEAAGXZ` | `0x10150` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `?GetTargetPartitionNumber@CDriveConfiguration@@QEAAKXZ` | `0x10180` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `?GetTargetPartitionSize@CDriveConfiguration@@QEAA_KXZ` | `0x101B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `?Initialize@CDriveConfiguration@@QEAAJPEBU_BDECFG_PARAMS@@QEAU_BDECFG_SIZE_REQUIREMENTS@@PEAVIConfigurationProgress@@@Z` | `0x101E0` | 126 | UnwindData |  |
| 90 | `?InitializeEntry@CDriveConfiguration@@CAXPEAX@Z` | `0x10270` | 56 | UnwindData |  |
| 91 | `?InitializeFromParams@CDriveConfiguration@@AEAAJPEAUIVdsVolume@@@Z` | `0x102B0` | 1,234 | UnwindData |  |
| 95 | `?IsMergeTargetWinRE@CDriveConfiguration@@QEAAJPEAH@Z` | `0x10790` | 48 | UnwindData |  |
| 99 | `?QueryStepPercentComplete@CDriveConfiguration@@QEAAJPEAK@Z` | `0x107D0` | 132 | UnwindData |  |
| 101 | `?SetConfigurationStep@CDriveConfiguration@@AEAAJW4_BDECFG_STEP_ID@@@Z` | `0x10860` | 126 | UnwindData |  |
| 102 | `?Thread_ConfigureDrive@CDriveConfiguration@@AEAAJXZ` | `0x108F0` | 1,478 | UnwindData |  |
| 103 | `?Thread_Initialize@CDriveConfiguration@@AEAAJXZ` | `0x10EC0` | 432 | UnwindData |  |
| 19 | `??_7CBcdStore@@6B@` | `0x14010` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `??_7CBcdWmiWrapper@@6B@` | `0x14018` | 0 | Indeterminate |  |
