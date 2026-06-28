# Binary Specification: winsetup.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\oobe\winsetup.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `501eda452c06bcf64a8d3b28fcd3f3602398025171b98999c4af69cdbca21002`
* **Total Exported Functions:** 66

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `FreeResourceHandle` | `0xD080` | 115 | UnwindData |  |
| 7 | `InstallWindows` | `0xD480` | 15,667 | UnwindData |  |
| 62 | `SetResourceHandle` | `0x125D0` | 416 | UnwindData |  |
| 41 | `Module_Init_MungeBootEntries` | `0x152F0` | 340 | UnwindData |  |
| 10 | `Module_Init_BootPrepare` | `0x1A100` | 621 | UnwindData |  |
| 11 | `Module_Init_Bootstrap` | `0x1C770` | 172 | UnwindData |  |
| 12 | `Module_Init_CBS` | `0x1E500` | 335 | UnwindData |  |
| 16 | `Module_Init_ConfigOfflineImage` | `0x1E720` | 177 | UnwindData |  |
| 13 | `Module_Init_Cleanup` | `0x1EC00` | 524 | UnwindData |  |
| 44 | `Module_Init_ParseCmdLine` | `0x1F2B0` | 135 | UnwindData |  |
| 14 | `Module_Init_Compliance` | `0x23570` | 689 | UnwindData |  |
| 15 | `Module_Init_ComputerName` | `0x259A0` | 371 | UnwindData |  |
| 17 | `Module_Init_ConfigSet` | `0x27580` | 311 | UnwindData |  |
| 18 | `Module_Init_CopyImages` | `0x28850` | 133 | UnwindData |  |
| 19 | `Module_Init_CopyPrivates` | `0x298D0` | 291 | UnwindData |  |
| 20 | `Module_Init_CopySetupFiles` | `0x2B540` | 561 | UnwindData |  |
| 58 | `SetFileCopyErrorResult` | `0x2C670` | 182 | UnwindData |  |
| 59 | `SetFileCopyErrorResultFromStruct` | `0x2C730` | 147 | UnwindData |  |
| 22 | `Module_Init_DeployImages` | `0x310D0` | 327 | UnwindData |  |
| 23 | `Module_Init_DiskConfiguration` | `0x35310` | 226 | UnwindData |  |
| 31 | `Module_Init_GatherDiskInfo` | `0x37530` | 355 | UnwindData |  |
| 57 | `PublishDiskInfoOnBlackboard` | `0x376A0` | 3,869 | UnwindData |  |
| 4 | `GetSpaceNeededForWinPE` | `0x3ABA0` | 1,077 | UnwindData |  |
| 24 | `Module_Init_DiskSpace` | `0x3AFE0` | 303 | UnwindData |  |
| 1 | `??4DUMgr@@QEAAAEAV0@AEBV0@@Z` | `0x3B930` | 3,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `?GetModuleId@DUMgr@@QEAAAEBQEAXXZ` | `0x3C6B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `InstallCopyCodeUpdate` | `0x3C6C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `InstallSetupUpdates` | `0x3C6D0` | 285 | UnwindData |  |
| 8 | `?Instance@DUMgr@@SAPEAV1@XZ` | `0x3C800` | 57 | UnwindData |  |
| 9 | `?IsCancelled@DUMgr@@AEAAHXZ` | `0x3C840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `Module_Init_DU` | `0x3C850` | 1,220 | UnwindData |  |
| 60 | `?SetModuleId@DUMgr@@QEAAXPEAX@Z` | `0x3CDD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `?SetPhase@DUMgr@@AEAAXW4DUPhase@@@Z` | `0x3CDE0` | 1,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `Module_Init_Ems` | `0x3D320` | 230 | UnwindData |  |
| 26 | `Module_Init_Engine` | `0x3F110` | 1,576 | UnwindData |  |
| 27 | `Module_Init_ErrorHandler` | `0x3FCD0` | 132 | UnwindData |  |
| 37 | `Module_Init_License` | `0x42320` | 541 | UnwindData |  |
| 28 | `Module_Init_ExternalDrivers` | `0x472E0` | 502 | UnwindData |  |
| 29 | `Module_Init_Finalize_Image` | `0x4A4B0` | 392 | UnwindData |  |
| 30 | `Module_Init_FixBBPaths` | `0x4BA90` | 489 | UnwindData |  |
| 33 | `Module_Init_ImageInstall` | `0x4E640` | 515 | UnwindData |  |
| 34 | `Module_Init_ImageTransfer` | `0x56FF0` | 604 | UnwindData |  |
| 35 | `Module_Init_Internal` | `0x58BE0` | 135 | UnwindData |  |
| 36 | `Module_Init_LanguagePack` | `0x5DEA0` | 782 | UnwindData |  |
| 38 | `Module_Init_Locale` | `0x61350` | 528 | UnwindData |  |
| 39 | `Module_Init_ModuleLoader` | `0x62500` | 458 | UnwindData |  |
| 40 | `Module_Init_MountedDevices` | `0x63750` | 234 | UnwindData |  |
| 43 | `Module_Init_PageFile` | `0x647E0` | 338 | UnwindData |  |
| 47 | `Module_Init_Productkey` | `0x69A70` | 569 | UnwindData |  |
| 46 | `Module_Init_PrepareInstallDrive` | `0x6BED0` | 385 | UnwindData |  |
| 48 | `Module_Init_QFE` | `0x6D7C0` | 1,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `Module_Init_RestartSetup` | `0x6DBC0` | 175 | UnwindData |  |
| 50 | `Module_Init_Rollback` | `0x72E40` | 613 | UnwindData |  |
| 66 | `GetCleanInstallCheckpointSequence` | `0x742C0` | 83 | UnwindData |  |
| 51 | `Module_Init_ScenarioDetect` | `0x74BD0` | 234 | UnwindData |  |
| 42 | `Module_Init_OnlineSettings` | `0x74CF0` | 172 | UnwindData |  |
| 52 | `Module_Init_SourceMedia` | `0x77090` | 512 | UnwindData |  |
| 53 | `Module_Init_StorageConfiguration` | `0x789F0` | 226 | UnwindData |  |
| 54 | `Module_Init_Sysprep` | `0x79FD0` | 284 | UnwindData |  |
| 55 | `Module_Init_SystemRestore` | `0x7A360` | 176 | UnwindData |  |
| 45 | `Module_Init_PickTempDrive` | `0x7CE90` | 618 | UnwindData |  |
| 56 | `Module_Init_Unattend` | `0x807F0` | 1,228 | UnwindData |  |
| 63 | `UnattendErrorFromResults` | `0x81930` | 1,398 | UnwindData |  |
| 32 | `Module_Init_HWRequirements` | `0x826C0` | 295 | UnwindData |  |
| 65 | `g_pUnattendCtxIBS` | `0x2B8558` | 13,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `g_hwCompatParams` | `0x2BBB00` | 0 | Indeterminate |  |
