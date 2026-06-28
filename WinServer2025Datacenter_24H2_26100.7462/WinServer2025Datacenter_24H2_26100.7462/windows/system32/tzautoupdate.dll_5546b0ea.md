# Binary Specification: tzautoupdate.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\tzautoupdate.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5546b0ea4f1dabad082716f6e34c63abc0d018fc0989e35b2e59b60f979b4918`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `AttemptToUpdateTimeZone` | `0xC1C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `AttemptToUpdateTimeZoneAndEnableChangeDetection` | `0xC1D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DisableTimeZoneAutoUpdate` | `0xC1E0` | 771 | UnwindData |  |
| 9 | `EnableTimeZoneAutoUpdate` | `0xC4F0` | 1,222 | UnwindData |  |
| 10 | `IsTimeZoneAutoUpdateEnabled` | `0xC9C0` | 286 | UnwindData |  |
| 11 | `ReadOneSettingsData` | `0xCAF0` | 725 | UnwindData |  |
| 1 | `ServiceMain` | `0x15EE0` | 765 | UnwindData |  |
| 2 | `SvchostPushServiceGlobals` | `0x162B0` | 12,960 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllCanUnloadNow` | `0x19550` | 32 | UnwindData |  |
| 7 | `DllGetActivationFactory` | `0x19580` | 45 | UnwindData |  |
| 8 | `DllGetClassObject` | `0x195C0` | 65 | UnwindData |  |
