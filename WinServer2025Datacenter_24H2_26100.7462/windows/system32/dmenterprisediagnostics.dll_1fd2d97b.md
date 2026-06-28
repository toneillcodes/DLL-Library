# Binary Specification: dmenterprisediagnostics.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\dmenterprisediagnostics.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1fd2d97b2c991f07b0a6825c9698efafd00bf3cfe3226a516879b612f47ce58e`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CollectDiagnosticsAutoLog` | `0x4150` | 28 | UnwindData |  |
| 2 | `GatherAutoLogEventsFromMobile` | `0x4370` | 91 | UnwindData |  |
| 3 | `RecordDiagnosticsError` | `0x56A0` | 31 | UnwindData |  |
| 4 | `SetupAutoLog` | `0x6280` | 61 | UnwindData |  |
| 5 | `SetupAutoLogWithTraceLevel` | `0x62D0` | 639 | UnwindData |  |
| 6 | `StartAutoLog` | `0x6940` | 23 | UnwindData |  |
| 7 | `StopAutoLog` | `0x6960` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `TearDownAutoLog` | `0x6B40` | 739 | UnwindData |  |
