# Binary Specification: smartscreen.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\smartscreen.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `40ed038d75c558cdfd92ab2ed2a4ec0869f5d16a2f7978b48493f827047f365c`
* **Total Exported Functions:** 17

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 12 | `ReportLaunch` | `0x138C40` | 1,008 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `CheckAppxPackageReputation` | `0x139030` | 2,217 | UnwindData |  |
| 2 | `CheckFileReputation` | `0x1398E0` | 1,386 | UnwindData |  |
| 7 | `GetAppControlEnforcementLevel` | `0x139E50` | 164 | UnwindData |  |
| 8 | `GetAppReputationEnforcementLevel` | `0x139F00` | 163 | UnwindData |  |
| 14 | `SetAppControlEnforcementLevel` | `0x139FB0` | 120 | UnwindData |  |
| 15 | `SetAppReputationEnforcementLevel` | `0x13A030` | 120 | UnwindData |  |
| 3 | `CheckReputation` | `0x13AA10` | 1,480 | UnwindData |  |
| 4 | `ClearCache` | `0x13AFE0` | 98 | UnwindData |  |
| 5 | `EventLogger` | `0x13B050` | 578 | UnwindData |  |
| 6 | `FreeExperience` | `0x13B2A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `GetEnforcementLevel` | `0x13B2B0` | 178 | UnwindData |  |
| 10 | `GetEnforcementPolicy` | `0x13B370` | 152 | UnwindData |  |
| 11 | `RegisterEventLogger` | `0x13B410` | 117 | UnwindData |  |
| 13 | `ResetLogger` | `0x13B490` | 33 | UnwindData |  |
| 16 | `SetEnforcementLevel` | `0x13B4C0` | 132 | UnwindData |  |
| 17 | `UriReputationFactory` | `0x13B550` | 390 | UnwindData |  |
