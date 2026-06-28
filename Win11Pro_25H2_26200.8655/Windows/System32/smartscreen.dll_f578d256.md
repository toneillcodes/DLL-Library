# Binary Specification: smartscreen.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\smartscreen.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f578d25612e53b34b1d6ab67d27da5f12d24a553dce667416f6592919278b446`
* **Total Exported Functions:** 17

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 12 | `ReportLaunch` | `0x138660` | 1,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `CheckAppxPackageReputation` | `0x138A60` | 2,195 | UnwindData |  |
| 2 | `CheckFileReputation` | `0x139300` | 1,348 | UnwindData |  |
| 7 | `GetAppControlEnforcementLevel` | `0x139850` | 164 | UnwindData |  |
| 8 | `GetAppReputationEnforcementLevel` | `0x139900` | 163 | UnwindData |  |
| 14 | `SetAppControlEnforcementLevel` | `0x1399B0` | 92 | UnwindData |  |
| 15 | `SetAppReputationEnforcementLevel` | `0x139A10` | 92 | UnwindData |  |
| 3 | `CheckReputation` | `0x13A2F0` | 1,427 | UnwindData |  |
| 4 | `ClearCache` | `0x13A890` | 128 | UnwindData |  |
| 5 | `EventLogger` | `0x13A910` | 562 | UnwindData |  |
| 6 | `FreeExperience` | `0x13AB50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `GetEnforcementLevel` | `0x13AB60` | 178 | UnwindData |  |
| 10 | `GetEnforcementPolicy` | `0x13AC20` | 152 | UnwindData |  |
| 11 | `RegisterEventLogger` | `0x13ACC0` | 178 | UnwindData |  |
| 13 | `ResetLogger` | `0x13AD80` | 33 | UnwindData |  |
| 16 | `SetEnforcementLevel` | `0x13ADB0` | 132 | UnwindData |  |
| 17 | `UriReputationFactory` | `0x13AE40` | 474 | UnwindData |  |
