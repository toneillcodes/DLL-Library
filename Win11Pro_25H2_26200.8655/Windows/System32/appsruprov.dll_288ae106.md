# Binary Specification: appsruprov.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\appsruprov.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `288ae106dfaac1bef5de18ec16c696c9a89405f5cf44cb4025d83405ef4f49ef`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllMain` | `0x4CD0` | 174 | UnwindData |  |
| 7 | `SruInitializeProvider` | `0x7980` | 1,250 | UnwindData |  |
| 8 | `SruUninitializeProvider` | `0x7E70` | 489 | UnwindData |  |
| 1 | `LogMemoryPerfCounters` | `0x12770` | 5,768 | UnwindData |  |
| 3 | `LogMemoryPerfCountersPeriodically` | `0x18060` | 177 | UnwindData |  |
| 4 | `PsmQueryApplicationPerformanceInformation` | `0x22290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `PsmQueryApplicationPerformanceInformation2` | `0x222B0` | 226 | UnwindData |  |
| 6 | `PsmQueryQuotaInformation` | `0x223A0` | 143 | UnwindData |  |
