# Binary Specification: StorageUsage.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\StorageUsage.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6b894ec32c58042ba710f7c7d3fc3bbf6cafcea2cf153a0afd6f2a3cf2d733c7`
* **Total Exported Functions:** 63

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `CloseFindStorage` | `0x6B50` | 492 | UnwindData |  |
| 5 | `CloseFindStorageSearch` | `0x6D50` | 493 | UnwindData |  |
| 12 | `FindNextStorageType` | `0x6F50` | 568 | UnwindData |  |
| 13 | `FindNextStorageTypeEx` | `0x7190` | 601 | UnwindData |  |
| 14 | `FindNextStorageTypeExAsync` | `0x73F0` | 606 | UnwindData |  |
| 1 | `DllRegisterServer` | `0x7660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllUnregisterServer` | `0x7660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `GetAppSize` | `0x7660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `TriggerBlinkCleanup` | `0x7660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `TriggerDownloadsCleanup` | `0x7660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `TriggerStorageTypeRefresh` | `0x7660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `TriggerTempFileCleanup` | `0x7660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `GetStorageDebugInfo` | `0x7670` | 543 | UnwindData |  |
| 24 | `GetStorageExecutionInfo` | `0x78A0` | 566 | UnwindData |  |
| 32 | `GetSystemFilesInfo` | `0x7AE0` | 551 | UnwindData |  |
| 33 | `GetTopFolders` | `0x7D10` | 580 | UnwindData |  |
| 34 | `MIDL_user_allocate` | `0x7F60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `MIDL_user_free` | `0x7F80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `OpenStorageTypeSearch` | `0x7FA0` | 555 | UnwindData |  |
| 47 | `RunStorageGroveler` | `0x81E0` | 541 | UnwindData |  |
| 49 | `SelectStorageVolume` | `0x8410` | 626 | UnwindData |  |
| 50 | `SelectStorageVolumeEx` | `0x8690` | 651 | UnwindData |  |
| 6 | `DismountVolume` | `0x8BB0` | 672 | UnwindData |  |
| 9 | `ExecuteDehydrateUserFiles` | `0x8E60` | 669 | UnwindData |  |
| 10 | `ExecuteRemoveUserFiles` | `0x9110` | 669 | UnwindData |  |
| 11 | `FinalizeVolume` | `0x93F0` | 666 | UnwindData |  |
| 15 | `FormatVolume` | `0x9690` | 668 | UnwindData |  |
| 17 | `GetLastFailedSaveLocationPath` | `0x9940` | 642 | UnwindData |  |
| 18 | `GetSmartAttributes` | `0x9BD0` | 666 | UnwindData |  |
| 20 | `GetStorageDeviceInfo` | `0x9E70` | 772 | UnwindData |  |
| 21 | `GetStorageDeviceLowDiskState` | `0xA180` | 701 | UnwindData |  |
| 22 | `GetStorageDeviceLowDiskState2` | `0xA450` | 737 | UnwindData |  |
| 23 | `GetStorageDeviceSize` | `0xA740` | 682 | UnwindData |  |
| 25 | `GetStorageInstanceCount` | `0xA9F0` | 666 | UnwindData |  |
| 26 | `GetStorageInstanceCountForMaps` | `0xAC90` | 666 | UnwindData |  |
| 27 | `GetStoragePoliciesLastTriggerTime` | `0xAF30` | 642 | UnwindData |  |
| 28 | `GetStoragePolicyDefaultValue` | `0xB1C0` | 666 | UnwindData |  |
| 29 | `GetStoragePolicySettings` | `0xB460` | 672 | UnwindData |  |
| 30 | `GetStorageSettings` | `0xB710` | 679 | UnwindData |  |
| 31 | `GetStorageStateName` | `0xB9C0` | 679 | UnwindData |  |
| 36 | `MountVolume` | `0xBC70` | 672 | UnwindData |  |
| 37 | `MoveFileInheritSecurityW` | `0xBF20` | 694 | UnwindData |  |
| 39 | `PredictStorageHealth` | `0xC3B0` | 669 | UnwindData |  |
| 40 | `ProcessStorageCardChange` | `0xC660` | 621 | UnwindData |  |
| 41 | `ProvisionForAppInstall` | `0xC8E0` | 663 | UnwindData |  |
| 43 | `RebootToFlashingMode` | `0xCB80` | 667 | UnwindData |  |
| 44 | `RebootToUosFlashing` | `0xCE30` | 667 | UnwindData |  |
| 46 | `ResetStoragePolicySettings` | `0xD0E0` | 621 | UnwindData |  |
| 48 | `ScanVolume` | `0xD360` | 739 | UnwindData |  |
| 51 | `SetStoragePoliciesLastTriggerTime` | `0xD650` | 642 | UnwindData |  |
| 52 | `SetStoragePolicySettings` | `0xD8E0` | 672 | UnwindData |  |
| 53 | `SetStorageSettings` | `0xDB90` | 680 | UnwindData |  |
| 54 | `SilentCleanupTaskGetEnabledState` | `0xDE40` | 642 | UnwindData |  |
| 55 | `SilentCleanupTaskSetEnabledState` | `0xE0D0` | 642 | UnwindData |  |
| 58 | `TriggerLowStorageNotification` | `0xEB90` | 666 | UnwindData |  |
| 59 | `TriggerStorageCleanup` | `0xEE30` | 642 | UnwindData |  |
| 60 | `TriggerStorageOptimization` | `0xF0C0` | 642 | UnwindData |  |
| 61 | `TriggerStoragePolicies` | `0xF350` | 642 | UnwindData |  |
| 45 | `ResetPhoneEx` | `0x10030` | 109 | UnwindData |  |
| 3 | `GetStorageUsageInfo` | `0x14C40` | 2,211 | UnwindData |  |
| 7 | `DllCanUnloadNow` | `0x19AC0` | 42 | UnwindData |  |
| 8 | `DllGetClassObject` | `0x19AF0` | 65 | UnwindData |  |
| 42 | `QueryStorageReserveEx` | `0x290D0` | 47,332 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
