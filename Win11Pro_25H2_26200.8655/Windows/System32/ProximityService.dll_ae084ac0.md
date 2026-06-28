# Binary Specification: ProximityService.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ProximityService.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ae084ac0c2d993b27ec38347b95df7868a38bde81bde49d69e0deba0b47bade5`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 11 | `SessionChangedEvent` | `0x49B0` | 29 | UnwindData |  |
| 15 | `InitProximityServiceEx` | `0x4C60` | 29 | UnwindData |  |
| 14 | *Ordinal Only* | `0x4D80` | 8 | UnwindData |  |
| 12 | `GetProximityClientCount` | `0x4F80` | 51 | UnwindData |  |
| 10 | `InitProximityService` | `0x5060` | 135 | UnwindData |  |
| 13 | `CleanupProximityService` | `0x6D30` | 137 | UnwindData |  |
| 16 | `ServiceMain` | `0x7190` | 1,811 | UnwindData |  |
| 17 | `SvchostPushServiceGlobals` | `0x7CB0` | 246,652 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
