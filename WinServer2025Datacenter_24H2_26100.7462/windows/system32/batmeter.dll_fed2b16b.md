# Binary Specification: batmeter.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\batmeter.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fed2b16b95520069699e9f39101a774273d00a68e2ad92d45988f9046c1ab9fb`
* **Total Exported Functions:** 29

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1012 | `GetBatteryStatusText` | `0x1070` | 352 | UnwindData |  |
| 1005 | `GetBatMeterIconAnimationState` | `0x1700` | 808 | UnwindData |  |
| 1010 | `GetBatteryImmersiveIcon` | `0x3D60` | 2,688 | UnwindData |  |
| 1007 | `GetBatMeterIconAnimationUpdate` | `0x47F0` | 61 | UnwindData |  |
| 1001 | `BatMeterIconThemeReset` | `0x5480` | 104 | UnwindData |  |
| 1004 | `CreateBatteryData` | `0x61C0` | 74 | UnwindData |  |
| 1024 | `SubscribeBatteryUpdateNotification` | `0x6210` | 104 | UnwindData |  |
| 1003 | `CleanupBatteryData` | `0x6570` | 109 | UnwindData |  |
| 1027 | `UpdateBatteryDataAsync` | `0x75C0` | 591 | UnwindData |  |
| 1022 | `SetBatteryLevel` | `0x99D0` | 1,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1023 | `SetBatteryWorkingState` | `0xA080` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1013 | `GetBatteryWorkingState` | `0xA190` | 912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1019 | `PowerCapabilities` | `0xA520` | 186 | UnwindData |  |
| 1000 | `BatMeterIconAnimationReset` | `0xA660` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1020 | `QueryBatteryData` | `0xA7E0` | 573 | UnwindData |  |
| 1025 | `UnsubscribeBatteryUpdateNotification` | `0xAA80` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1002 | `BatMeterOnDeviceChange` | `0xAB00` | 191 | UnwindData |  |
| 1006 | `GetBatMeterIconAnimationTimeDelay` | `0xAD00` | 6,976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1014 | `IsBatteryBad` | `0xC840` | 14,816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 999 | *Ordinal Only* | `0x10220` | 274 | UnwindData |  |
| 1008 | `GetBatteryCapacityInfo` | `0x10340` | 192 | UnwindData |  |
| 1011 | `GetBatteryInfo` | `0x10410` | 190 | UnwindData |  |
| 1015 | `IsBatteryHealthWarningEnabled` | `0x104E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1021 | `SetBatteryHealthWarningState` | `0x104E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1016 | `IsBatteryLevelCritical` | `0x104F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1017 | `IsBatteryLevelLow` | `0x10510` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1018 | `IsBatteryLevelReserve` | `0x10530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1026 | `UpdateBatteryData` | `0x10550` | 45 | UnwindData |  |
| 1009 | `GetBatteryDetails` | `0x10F80` | 274 | UnwindData |  |
