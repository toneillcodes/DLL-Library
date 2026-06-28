# Binary Specification: WpPortingLibrary.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\WpPortingLibrary.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `dddbb60b90c57eea97fee6757fe1997b6d1da00eb487ec43481ebabbacfe0dab`
* **Total Exported Functions:** 26

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 14 | `PackageFullNameFromProductIdAndVersion` | `0x1C00` | 433 | UnwindData |  |
| 15 | `PackageFullNameFromProductInfo` | `0x1DC0` | 422 | UnwindData |  |
| 16 | `ProductInfoFromPackageFullName` | `0x1F70` | 539 | UnwindData |  |
| 3 | `GetPhoneBuildInfo` | `0x21A0` | 64 | UnwindData |  |
| 17 | `QueryPhoneInformation` | `0x21F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `GetAppStorageFolder` | `0x2220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `GetDeviceUniqueID` | `0x2220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `GetStorageDeviceInfo` | `0x2220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `TaskSchedulerCreateSchedule` | `0x2220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `TaskSchedulerDeinit` | `0x2220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `TaskSchedulerDeleteSchedule` | `0x2220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `TaskSchedulerEnableSchedule` | `0x2220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `TaskSchedulerGetPublishStateName` | `0x2220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `TaskSchedulerGetSchedule` | `0x2220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `TaskSchedulerInit` | `0x2220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `TaskSchedulerFreeSchedule` | `0x2230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `TaskSchedulerFreeScheduleStatistics` | `0x2230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `Is_AppXExecutionServiceReady_Available` | `0x2240` | 0 | Indeterminate |  |
| 6 | `Is_BatterySaverState_Available` | `0x2240` | 0 | Indeterminate |  |
| 7 | `Is_GrantWPNoNetworkingRegistryAccess_Hack_Available` | `0x2240` | 0 | Indeterminate |  |
| 8 | `Is_OsBeginPostBootWorkState_Available` | `0x2240` | 0 | Indeterminate |  |
| 9 | `Is_ProvisioningCompleteState_Available` | `0x2240` | 0 | Indeterminate |  |
| 10 | `Is_ShellReadyInternalState_Available` | `0x2240` | 0 | Indeterminate |  |
| 11 | `Is_ShellStartReady_Available` | `0x2240` | 0 | Indeterminate |  |
| 12 | `Is_TaskScheduler_Available` | `0x2240` | 0 | Indeterminate |  |
| 13 | `Is_VoIPActiveCallState_Available` | `0x2240` | 0 | Indeterminate |  |
