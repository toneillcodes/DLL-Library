# Binary Specification: ProximityService.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ProximityService.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `11d92fc3d65b340c45975e56ac9f954809b768da4f670dad8b76bf6cf7861bb1`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 11 | `SessionChangedEvent` | `0x4A00` | 29 | UnwindData |  |
| 15 | `InitProximityServiceEx` | `0x4CB0` | 29 | UnwindData |  |
| 14 | *Ordinal Only* | `0x4DD0` | 8 | UnwindData |  |
| 12 | `GetProximityClientCount` | `0x4FD0` | 51 | UnwindData |  |
| 10 | `InitProximityService` | `0x50B0` | 135 | UnwindData |  |
| 13 | `CleanupProximityService` | `0x6D80` | 137 | UnwindData |  |
| 16 | `ServiceMain` | `0x71E0` | 1,811 | UnwindData |  |
| 17 | `SvchostPushServiceGlobals` | `0x7D00` | 252,796 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
