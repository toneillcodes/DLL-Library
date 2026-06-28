# Binary Specification: timesync.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\timesync.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fba5f96d15ca9a7b20696a798f23f90128044e079ca68c736c04604ac9a0a1a5`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DisableNTPSync` | `0x7850` | 364 | UnwindData |  |
| 2 | `FreeTimeStatusInfo` | `0x79D0` | 203 | UnwindData |  |
| 3 | `GetLastGoodSampleInfo` | `0x7AB0` | 119 | UnwindData |  |
| 4 | `GetTimeStatusInfo` | `0x7B30` | 207 | UnwindData |  |
| 5 | `GetW32timeParameterSz` | `0x7C10` | 560 | UnwindData |  |
| 6 | `IsNTPSyncEnabled` | `0x7E50` | 187 | UnwindData |  |
| 7 | `ReadLastKnownGoodTimeFromRegistry` | `0x7F20` | 611 | UnwindData |  |
| 8 | `SetNTPSync` | `0x8190` | 384 | UnwindData |  |
| 9 | `StartTimeService` | `0x8320` | 840 | UnwindData |  |
| 10 | `StopTimeService` | `0x8670` | 266 | UnwindData |  |
| 11 | `SyncW32Time` | `0x8780` | 786 | UnwindData |  |
