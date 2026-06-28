# Binary Specification: batmeter.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\batmeter.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c3b2eb1faf1c8e9bc9729f11a7261c8da665694a26908604b18921f059f496cc`
* **Total Exported Functions:** 29

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1012 | `GetBatteryStatusText` | `0x1070` | 352 | UnwindData |  |
| 1005 | `GetBatMeterIconAnimationState` | `0x1700` | 808 | UnwindData |  |
| 1010 | `GetBatteryImmersiveIcon` | `0x3D60` | 2,688 | UnwindData |  |
| 1007 | `GetBatMeterIconAnimationUpdate` | `0x47F0` | 61 | UnwindData |  |
| 1001 | `BatMeterIconThemeReset` | `0x5480` | 104 | UnwindData |  |
| 1004 | `CreateBatteryData` | `0x5EA0` | 74 | UnwindData |  |
| 1027 | `UpdateBatteryDataAsync` | `0x6410` | 40 | UnwindData |  |
| 1022 | `SetBatteryLevel` | `0x90F0` | 1,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1023 | `SetBatteryWorkingState` | `0x97A0` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1013 | `GetBatteryWorkingState` | `0x9A00` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1019 | `PowerCapabilities` | `0x9CF0` | 186 | UnwindData |  |
| 1000 | `BatMeterIconAnimationReset` | `0x9E30` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1024 | `SubscribeBatteryUpdateNotification` | `0x9F30` | 29 | UnwindData |  |
| 1025 | `UnsubscribeBatteryUpdateNotification` | `0xA0D0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1006 | `GetBatMeterIconAnimationTimeDelay` | `0xA1F0` | 4,640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1002 | `BatMeterOnDeviceChange` | `0xB410` | 235 | UnwindData |  |
| 1003 | `CleanupBatteryData` | `0xB510` | 539 | UnwindData |  |
| 1020 | `QueryBatteryData` | `0xB740` | 559 | UnwindData |  |
| 1014 | `IsBatteryBad` | `0xCD00` | 15,440 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 999 | *Ordinal Only* | `0x10950` | 274 | UnwindData |  |
| 1008 | `GetBatteryCapacityInfo` | `0x10A70` | 192 | UnwindData |  |
| 1011 | `GetBatteryInfo` | `0x10B40` | 190 | UnwindData |  |
| 1015 | `IsBatteryHealthWarningEnabled` | `0x10C10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1021 | `SetBatteryHealthWarningState` | `0x10C10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1016 | `IsBatteryLevelCritical` | `0x10C20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1017 | `IsBatteryLevelLow` | `0x10C40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1018 | `IsBatteryLevelReserve` | `0x10C60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1026 | `UpdateBatteryData` | `0x10C80` | 45 | UnwindData |  |
| 1009 | `GetBatteryDetails` | `0x116B0` | 274 | UnwindData |  |
