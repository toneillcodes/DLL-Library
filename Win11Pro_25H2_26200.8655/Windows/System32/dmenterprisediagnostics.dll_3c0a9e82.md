# Binary Specification: dmenterprisediagnostics.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\dmenterprisediagnostics.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3c0a9e826fdb24624f808a756ce0d9ad73b2cec398f56130c243c7582a73bed7`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CollectDiagnosticsAutoLog` | `0x4150` | 28 | UnwindData |  |
| 2 | `GatherAutoLogEventsFromMobile` | `0x4370` | 91 | UnwindData |  |
| 3 | `RecordDiagnosticsError` | `0x56C0` | 31 | UnwindData |  |
| 4 | `SetupAutoLog` | `0x62A0` | 61 | UnwindData |  |
| 5 | `SetupAutoLogWithTraceLevel` | `0x62F0` | 639 | UnwindData |  |
| 6 | `StartAutoLog` | `0x6960` | 23 | UnwindData |  |
| 7 | `StopAutoLog` | `0x6980` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `TearDownAutoLog` | `0x6B60` | 739 | UnwindData |  |
