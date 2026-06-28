# Binary Specification: InprocLogger.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\InprocLogger.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `45666c8af4c0bb2f1028d97a3f9ad7544494be338541bb5d5c4f8a4528bea15f`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `EnableInProcTracingForProvider` | `0x5450` | 184 | UnwindData |  |
| 2 | `FlushInProcTraceSession` | `0x5510` | 270 | UnwindData |  |
| 3 | `InitializeInProcLogger` | `0x5630` | 52 | UnwindData |  |
| 4 | `InitializeInProcTraceFlushTrigger` | `0x5670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `InitializeInProcTraceSession` | `0x5680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `IsInProcTraceSessionStarted` | `0x5690` | 181 | UnwindData |  |
| 7 | `ShutdownInProcLogger` | `0x5750` | 377 | UnwindData |  |
| 8 | `ShutdownInProcTraceFlushTrigger` | `0x58D0` | 372 | UnwindData |  |
| 9 | `ShutdownInProcTraceSession` | `0x5A50` | 346 | UnwindData |  |
| 10 | `StartInProcTraceSession` | `0x5BB0` | 228 | UnwindData |  |
| 11 | `StopInProcTraceSession` | `0x5CA0` | 230 | UnwindData |  |
