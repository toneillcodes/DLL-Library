# Binary Specification: winsetup.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\oobe\winsetup.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d4df77acb14b603c00188f980535a15d9ee27159705a7010fce11846f25e6d0b`
* **Total Exported Functions:** 66

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `FreeResourceHandle` | `0xD130` | 115 | UnwindData |  |
| 7 | `InstallWindows` | `0xD530` | 15,667 | UnwindData |  |
| 62 | `SetResourceHandle` | `0x12680` | 416 | UnwindData |  |
| 41 | `Module_Init_MungeBootEntries` | `0x153A0` | 340 | UnwindData |  |
| 10 | `Module_Init_BootPrepare` | `0x1A1B0` | 621 | UnwindData |  |
| 11 | `Module_Init_Bootstrap` | `0x1C820` | 172 | UnwindData |  |
| 12 | `Module_Init_CBS` | `0x1E5B0` | 335 | UnwindData |  |
| 16 | `Module_Init_ConfigOfflineImage` | `0x1E7D0` | 177 | UnwindData |  |
| 13 | `Module_Init_Cleanup` | `0x1ECB0` | 524 | UnwindData |  |
| 44 | `Module_Init_ParseCmdLine` | `0x1F360` | 135 | UnwindData |  |
| 14 | `Module_Init_Compliance` | `0x23620` | 689 | UnwindData |  |
| 15 | `Module_Init_ComputerName` | `0x25A50` | 371 | UnwindData |  |
| 17 | `Module_Init_ConfigSet` | `0x27650` | 311 | UnwindData |  |
| 18 | `Module_Init_CopyImages` | `0x288E0` | 133 | UnwindData |  |
| 19 | `Module_Init_CopyPrivates` | `0x29960` | 291 | UnwindData |  |
| 20 | `Module_Init_CopySetupFiles` | `0x2B5D0` | 561 | UnwindData |  |
| 58 | `SetFileCopyErrorResult` | `0x2C700` | 182 | UnwindData |  |
| 59 | `SetFileCopyErrorResultFromStruct` | `0x2C7C0` | 147 | UnwindData |  |
| 22 | `Module_Init_DeployImages` | `0x31160` | 327 | UnwindData |  |
| 23 | `Module_Init_DiskConfiguration` | `0x353A0` | 226 | UnwindData |  |
| 31 | `Module_Init_GatherDiskInfo` | `0x375C0` | 355 | UnwindData |  |
| 57 | `PublishDiskInfoOnBlackboard` | `0x37730` | 3,869 | UnwindData |  |
| 4 | `GetSpaceNeededForWinPE` | `0x3AC30` | 1,077 | UnwindData |  |
| 24 | `Module_Init_DiskSpace` | `0x3B070` | 303 | UnwindData |  |
| 1 | `??4DUMgr@@QEAAAEAV0@AEBV0@@Z` | `0x3B9C0` | 3,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `?GetModuleId@DUMgr@@QEAAAEBQEAXXZ` | `0x3C740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `InstallCopyCodeUpdate` | `0x3C750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `InstallSetupUpdates` | `0x3C760` | 285 | UnwindData |  |
| 8 | `?Instance@DUMgr@@SAPEAV1@XZ` | `0x3C890` | 57 | UnwindData |  |
| 9 | `?IsCancelled@DUMgr@@AEAAHXZ` | `0x3C8D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `Module_Init_DU` | `0x3C8E0` | 1,220 | UnwindData |  |
| 60 | `?SetModuleId@DUMgr@@QEAAXPEAX@Z` | `0x3CE60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `?SetPhase@DUMgr@@AEAAXW4DUPhase@@@Z` | `0x3CE70` | 1,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `Module_Init_Ems` | `0x3D3B0` | 230 | UnwindData |  |
| 26 | `Module_Init_Engine` | `0x3F1A0` | 1,576 | UnwindData |  |
| 27 | `Module_Init_ErrorHandler` | `0x3FD60` | 132 | UnwindData |  |
| 37 | `Module_Init_License` | `0x423B0` | 541 | UnwindData |  |
| 28 | `Module_Init_ExternalDrivers` | `0x47370` | 502 | UnwindData |  |
| 29 | `Module_Init_Finalize_Image` | `0x4A540` | 392 | UnwindData |  |
| 30 | `Module_Init_FixBBPaths` | `0x4BB20` | 489 | UnwindData |  |
| 33 | `Module_Init_ImageInstall` | `0x4E6D0` | 515 | UnwindData |  |
| 34 | `Module_Init_ImageTransfer` | `0x57080` | 604 | UnwindData |  |
| 35 | `Module_Init_Internal` | `0x58C70` | 135 | UnwindData |  |
| 36 | `Module_Init_LanguagePack` | `0x5DF30` | 782 | UnwindData |  |
| 38 | `Module_Init_Locale` | `0x613E0` | 528 | UnwindData |  |
| 39 | `Module_Init_ModuleLoader` | `0x62590` | 458 | UnwindData |  |
| 40 | `Module_Init_MountedDevices` | `0x637E0` | 234 | UnwindData |  |
| 43 | `Module_Init_PageFile` | `0x64870` | 338 | UnwindData |  |
| 47 | `Module_Init_Productkey` | `0x69B00` | 569 | UnwindData |  |
| 46 | `Module_Init_PrepareInstallDrive` | `0x6BF60` | 385 | UnwindData |  |
| 48 | `Module_Init_QFE` | `0x6D850` | 1,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `Module_Init_RestartSetup` | `0x6DC50` | 175 | UnwindData |  |
| 50 | `Module_Init_Rollback` | `0x72ED0` | 613 | UnwindData |  |
| 66 | `GetCleanInstallCheckpointSequence` | `0x74350` | 83 | UnwindData |  |
| 51 | `Module_Init_ScenarioDetect` | `0x74C60` | 234 | UnwindData |  |
| 42 | `Module_Init_OnlineSettings` | `0x74D80` | 172 | UnwindData |  |
| 52 | `Module_Init_SourceMedia` | `0x77120` | 512 | UnwindData |  |
| 53 | `Module_Init_StorageConfiguration` | `0x78A80` | 226 | UnwindData |  |
| 54 | `Module_Init_Sysprep` | `0x7A060` | 284 | UnwindData |  |
| 55 | `Module_Init_SystemRestore` | `0x7A3F0` | 176 | UnwindData |  |
| 45 | `Module_Init_PickTempDrive` | `0x7CF20` | 618 | UnwindData |  |
| 56 | `Module_Init_Unattend` | `0x80880` | 1,228 | UnwindData |  |
| 63 | `UnattendErrorFromResults` | `0x819C0` | 1,398 | UnwindData |  |
| 32 | `Module_Init_HWRequirements` | `0x82750` | 295 | UnwindData |  |
| 65 | `g_pUnattendCtxIBS` | `0x2B8520` | 13,728 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `g_hwCompatParams` | `0x2BBAC0` | 0 | Indeterminate |  |
