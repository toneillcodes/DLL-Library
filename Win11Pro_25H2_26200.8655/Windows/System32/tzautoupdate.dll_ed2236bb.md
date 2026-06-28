# Binary Specification: tzautoupdate.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\tzautoupdate.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ed2236bb4f2d3e9e804fb5ee4ebae24c2315855cdb8f1d287aed421ed24fc53c`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `AttemptToUpdateTimeZone` | `0xC2D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `AttemptToUpdateTimeZoneAndEnableChangeDetection` | `0xC2E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DisableTimeZoneAutoUpdate` | `0xC2F0` | 771 | UnwindData |  |
| 9 | `EnableTimeZoneAutoUpdate` | `0xC600` | 1,222 | UnwindData |  |
| 10 | `IsTimeZoneAutoUpdateEnabled` | `0xCAD0` | 286 | UnwindData |  |
| 11 | `ReadOneSettingsData` | `0xCC00` | 725 | UnwindData |  |
| 1 | `ServiceMain` | `0x14BA0` | 765 | UnwindData |  |
| 2 | `SvchostPushServiceGlobals` | `0x14F70` | 12,960 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllCanUnloadNow` | `0x18210` | 32 | UnwindData |  |
| 7 | `DllGetActivationFactory` | `0x18240` | 45 | UnwindData |  |
| 8 | `DllGetClassObject` | `0x18280` | 65 | UnwindData |  |
