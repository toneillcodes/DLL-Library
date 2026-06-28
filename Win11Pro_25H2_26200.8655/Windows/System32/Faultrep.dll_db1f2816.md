# Binary Specification: Faultrep.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Faultrep.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `db1f28160ea982b84f0164d8705fac7a756038ba1b841a698dd0cb379475ebc2`
* **Total Exported Functions:** 18

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `DllCanUnloadNow` | `0x7060` | 52 | UnwindData |  |
| 7 | `DllGetClassObject` | `0x70A0` | 157 | UnwindData |  |
| 5 | `CheckPerUserCrossProcessThrottle` | `0xE560` | 136 | UnwindData |  |
| 8 | `UpdatePerUserLastCrossProcessCollectionTime` | `0xE5F0` | 307 | UnwindData |  |
| 11 | `CancelHangReporting` | `0xF1A0` | 202 | UnwindData |  |
| 1 | *Ordinal Only* | `0xF270` | 44 | UnwindData |  |
| 12 | `ReportCoreHang` | `0xF2B0` | 51 | UnwindData |  |
| 14 | `ReportHang` | `0xF2F0` | 33 | UnwindData |  |
| 2 | *Ordinal Only* | `0xF320` | 44 | UnwindData |  |
| 15 | `WerReportHang` | `0xF360` | 99 | UnwindData |  |
| 3 | `BasepReportFault` | `0xF3D0` | 48 | UnwindData |  |
| 4 | `CheckForReadOnlyResourceFilter` | `0xF410` | 5,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `AddERExcludedApplicationA` | `0x10B50` | 157 | UnwindData |  |
| 10 | `AddERExcludedApplicationW` | `0x10C00` | 32 | UnwindData |  |
| 13 | `ReportFault` | `0x10C30` | 79 | UnwindData |  |
| 17 | `WerpInitiateCrashReporting` | `0x10D30` | 1,659 | UnwindData |  |
| 16 | `WerpGetDebugger` | `0x1F160` | 1,379 | UnwindData |  |
| 18 | `WerpLaunchAeDebug` | `0x1FCD0` | 2,764 | UnwindData |  |
