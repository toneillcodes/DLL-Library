# Binary Specification: StorageUsage.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\StorageUsage.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `34fe5dd434b556ac113e396dd48d604c41cae1306aea81ae8cbf772942e78a88`
* **Total Exported Functions:** 63

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `CloseFindStorage` | `0x6B10` | 492 | UnwindData |  |
| 5 | `CloseFindStorageSearch` | `0x6D10` | 493 | UnwindData |  |
| 12 | `FindNextStorageType` | `0x6F10` | 568 | UnwindData |  |
| 13 | `FindNextStorageTypeEx` | `0x7150` | 601 | UnwindData |  |
| 14 | `FindNextStorageTypeExAsync` | `0x73B0` | 606 | UnwindData |  |
| 1 | `DllRegisterServer` | `0x7620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllUnregisterServer` | `0x7620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `GetAppSize` | `0x7620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `TriggerBlinkCleanup` | `0x7620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `TriggerDownloadsCleanup` | `0x7620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `TriggerStorageTypeRefresh` | `0x7620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `TriggerTempFileCleanup` | `0x7620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `GetStorageDebugInfo` | `0x7630` | 543 | UnwindData |  |
| 24 | `GetStorageExecutionInfo` | `0x7860` | 566 | UnwindData |  |
| 32 | `GetSystemFilesInfo` | `0x7AA0` | 551 | UnwindData |  |
| 33 | `GetTopFolders` | `0x7CD0` | 580 | UnwindData |  |
| 34 | `MIDL_user_allocate` | `0x7F20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `MIDL_user_free` | `0x7F40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `OpenStorageTypeSearch` | `0x7F60` | 576 | UnwindData |  |
| 47 | `RunStorageGroveler` | `0x81B0` | 541 | UnwindData |  |
| 49 | `SelectStorageVolume` | `0x83E0` | 626 | UnwindData |  |
| 50 | `SelectStorageVolumeEx` | `0x8660` | 651 | UnwindData |  |
| 6 | `DismountVolume` | `0x8B80` | 563 | UnwindData |  |
| 9 | `ExecuteDehydrateUserFiles` | `0x8DC0` | 558 | UnwindData |  |
| 10 | `ExecuteRemoveUserFiles` | `0x9000` | 558 | UnwindData |  |
| 11 | `FinalizeVolume` | `0x9240` | 560 | UnwindData |  |
| 15 | `FormatVolume` | `0x9480` | 559 | UnwindData |  |
| 17 | `GetLastFailedSaveLocationPath` | `0x96C0` | 553 | UnwindData |  |
| 18 | `GetSmartAttributes` | `0x98F0` | 558 | UnwindData |  |
| 20 | `GetStorageDeviceInfo` | `0x9B30` | 658 | UnwindData |  |
| 21 | `GetStorageDeviceLowDiskState` | `0x9DD0` | 610 | UnwindData |  |
| 22 | `GetStorageDeviceLowDiskState2` | `0xA040` | 637 | UnwindData |  |
| 23 | `GetStorageDeviceSize` | `0xA2D0` | 575 | UnwindData |  |
| 25 | `GetStorageInstanceCount` | `0xA520` | 558 | UnwindData |  |
| 26 | `GetStorageInstanceCountForMaps` | `0xA760` | 558 | UnwindData |  |
| 27 | `GetStoragePoliciesLastTriggerTime` | `0xA9A0` | 553 | UnwindData |  |
| 28 | `GetStoragePolicyDefaultValue` | `0xABD0` | 558 | UnwindData |  |
| 29 | `GetStoragePolicySettings` | `0xAE10` | 563 | UnwindData |  |
| 30 | `GetStorageSettings` | `0xB050` | 575 | UnwindData |  |
| 31 | `GetStorageStateName` | `0xB2A0` | 575 | UnwindData |  |
| 36 | `MountVolume` | `0xB4F0` | 561 | UnwindData |  |
| 37 | `MoveFileInheritSecurityW` | `0xB730` | 597 | UnwindData |  |
| 39 | `PredictStorageHealth` | `0xBB70` | 558 | UnwindData |  |
| 40 | `ProcessStorageCardChange` | `0xBDB0` | 534 | UnwindData |  |
| 41 | `ProvisionForAppInstall` | `0xBFD0` | 555 | UnwindData |  |
| 43 | `RebootToFlashingMode` | `0xC210` | 558 | UnwindData |  |
| 44 | `RebootToUosFlashing` | `0xC450` | 558 | UnwindData |  |
| 46 | `ResetStoragePolicySettings` | `0xC690` | 534 | UnwindData |  |
| 48 | `ScanVolume` | `0xC8B0` | 633 | UnwindData |  |
| 51 | `SetStoragePoliciesLastTriggerTime` | `0xCB30` | 553 | UnwindData |  |
| 52 | `SetStoragePolicySettings` | `0xCD60` | 563 | UnwindData |  |
| 53 | `SetStorageSettings` | `0xCFA0` | 575 | UnwindData |  |
| 54 | `SilentCleanupTaskGetEnabledState` | `0xD1F0` | 553 | UnwindData |  |
| 55 | `SilentCleanupTaskSetEnabledState` | `0xD420` | 554 | UnwindData |  |
| 58 | `TriggerLowStorageNotification` | `0xD650` | 558 | UnwindData |  |
| 59 | `TriggerStorageCleanup` | `0xD890` | 553 | UnwindData |  |
| 60 | `TriggerStorageOptimization` | `0xDAC0` | 553 | UnwindData |  |
| 61 | `TriggerStoragePolicies` | `0xDCF0` | 553 | UnwindData |  |
| 45 | `ResetPhoneEx` | `0xDF20` | 109 | UnwindData |  |
| 3 | `GetStorageUsageInfo` | `0x12B20` | 2,211 | UnwindData |  |
| 7 | `DllCanUnloadNow` | `0x179A0` | 42 | UnwindData |  |
| 8 | `DllGetClassObject` | `0x179D0` | 65 | UnwindData |  |
| 42 | `QueryStorageReserveEx` | `0x26F70` | 45,716 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
