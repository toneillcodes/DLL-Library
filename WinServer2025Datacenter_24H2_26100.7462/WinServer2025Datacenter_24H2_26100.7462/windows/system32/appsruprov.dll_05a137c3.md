# Binary Specification: appsruprov.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\appsruprov.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `05a137c3dabe3ebf23b1771060bd65d9758077ac2c7e3955094fb47d48b3a807`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllMain` | `0x4CD0` | 174 | UnwindData |  |
| 7 | `SruInitializeProvider` | `0x7980` | 1,250 | UnwindData |  |
| 8 | `SruUninitializeProvider` | `0x7E70` | 489 | UnwindData |  |
| 1 | `LogMemoryPerfCounters` | `0x12750` | 5,768 | UnwindData |  |
| 3 | `LogMemoryPerfCountersPeriodically` | `0x18040` | 177 | UnwindData |  |
| 4 | `PsmQueryApplicationPerformanceInformation` | `0x22270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `PsmQueryApplicationPerformanceInformation2` | `0x22290` | 226 | UnwindData |  |
| 6 | `PsmQueryQuotaInformation` | `0x22380` | 143 | UnwindData |  |
