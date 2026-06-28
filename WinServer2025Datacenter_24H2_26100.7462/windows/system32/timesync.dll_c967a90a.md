# Binary Specification: timesync.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\timesync.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c967a90a1bc201875e37d2f2ffd1f86d3a9b7afd221db5754948bf13e3881932`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DisableNTPSync` | `0x7840` | 364 | UnwindData |  |
| 2 | `FreeTimeStatusInfo` | `0x79C0` | 203 | UnwindData |  |
| 3 | `GetLastGoodSampleInfo` | `0x7AA0` | 119 | UnwindData |  |
| 4 | `GetTimeStatusInfo` | `0x7B20` | 207 | UnwindData |  |
| 5 | `GetW32timeParameterSz` | `0x7C00` | 560 | UnwindData |  |
| 6 | `IsNTPSyncEnabled` | `0x7E40` | 187 | UnwindData |  |
| 7 | `ReadLastKnownGoodTimeFromRegistry` | `0x7F10` | 611 | UnwindData |  |
| 8 | `SetNTPSync` | `0x8180` | 384 | UnwindData |  |
| 9 | `StartTimeService` | `0x8310` | 840 | UnwindData |  |
| 10 | `StopTimeService` | `0x8660` | 266 | UnwindData |  |
| 11 | `SyncW32Time` | `0x8770` | 786 | UnwindData |  |
