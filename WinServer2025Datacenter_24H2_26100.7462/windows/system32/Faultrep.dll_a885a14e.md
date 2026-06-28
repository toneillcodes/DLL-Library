# Binary Specification: Faultrep.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Faultrep.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a885a14e2fa9304b70d9b603b541efff0e23cd459b1c858a57b7678b96b8a5bd`
* **Total Exported Functions:** 18

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `DllCanUnloadNow` | `0x70B0` | 52 | UnwindData |  |
| 7 | `DllGetClassObject` | `0x70F0` | 157 | UnwindData |  |
| 5 | `CheckPerUserCrossProcessThrottle` | `0xE5B0` | 136 | UnwindData |  |
| 8 | `UpdatePerUserLastCrossProcessCollectionTime` | `0xE640` | 307 | UnwindData |  |
| 11 | `CancelHangReporting` | `0xF1F0` | 202 | UnwindData |  |
| 1 | *Ordinal Only* | `0xF2C0` | 44 | UnwindData |  |
| 12 | `ReportCoreHang` | `0xF300` | 51 | UnwindData |  |
| 14 | `ReportHang` | `0xF340` | 33 | UnwindData |  |
| 2 | *Ordinal Only* | `0xF370` | 44 | UnwindData |  |
| 15 | `WerReportHang` | `0xF3B0` | 99 | UnwindData |  |
| 3 | `BasepReportFault` | `0xF420` | 48 | UnwindData |  |
| 4 | `CheckForReadOnlyResourceFilter` | `0xF460` | 5,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `AddERExcludedApplicationA` | `0x10BA0` | 157 | UnwindData |  |
| 10 | `AddERExcludedApplicationW` | `0x10C50` | 32 | UnwindData |  |
| 13 | `ReportFault` | `0x10C80` | 79 | UnwindData |  |
| 17 | `WerpInitiateCrashReporting` | `0x10D80` | 1,659 | UnwindData |  |
| 16 | `WerpGetDebugger` | `0x1F1B0` | 1,379 | UnwindData |  |
| 18 | `WerpLaunchAeDebug` | `0x1FD20` | 2,764 | UnwindData |  |
