# Binary Specification: InprocLogger.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\InprocLogger.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e081c38342e9138441b9134e599214cb7b0e6eae804b9f70d28e224652ff40d5`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `EnableInProcTracingForProvider` | `0x5460` | 184 | UnwindData |  |
| 2 | `FlushInProcTraceSession` | `0x5520` | 270 | UnwindData |  |
| 3 | `InitializeInProcLogger` | `0x5640` | 52 | UnwindData |  |
| 4 | `InitializeInProcTraceFlushTrigger` | `0x5680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `InitializeInProcTraceSession` | `0x5690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `IsInProcTraceSessionStarted` | `0x56A0` | 181 | UnwindData |  |
| 7 | `ShutdownInProcLogger` | `0x5760` | 377 | UnwindData |  |
| 8 | `ShutdownInProcTraceFlushTrigger` | `0x58E0` | 372 | UnwindData |  |
| 9 | `ShutdownInProcTraceSession` | `0x5A60` | 346 | UnwindData |  |
| 10 | `StartInProcTraceSession` | `0x5BC0` | 228 | UnwindData |  |
| 11 | `StopInProcTraceSession` | `0x5CB0` | 230 | UnwindData |  |
