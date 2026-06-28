# Binary Specification: mstask.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\mstask.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ee292dcdb1fc86ef5f01e504e6fd687413a3fde00043703ee4a1409b24758aec`
* **Total Exported Functions:** 13

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllGetClassObject` | `0x7C20` | 227 | UnwindData |  |
| 2 | `DllCanUnloadNow` | `0x89B0` | 6,080 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `SASetAccountInformation` | `0xA170` | 60 | UnwindData |  |
| 5 | `NetrJobAdd` | `0xBA20` | 47 | UnwindData |  |
| 6 | `NetrJobDel` | `0xBA60` | 48 | UnwindData |  |
| 7 | `NetrJobEnum` | `0xBAA0` | 63 | UnwindData |  |
| 8 | `NetrJobGetInfo` | `0xBAF0` | 48 | UnwindData |  |
| 9 | `SAGetAccountInformation` | `0xBB30` | 54 | UnwindData |  |
| 10 | `SAGetNSAccountInformation` | `0xBB70` | 48 | UnwindData |  |
| 12 | `SASetNSAccountInformation` | `0xBBB0` | 49 | UnwindData |  |
| 1 | `ConvertAtJobsToTasks` | `0xC080` | 834 | UnwindData |  |
| 4 | `GetNetScheduleAccountInformation` | `0xC3D0` | 32 | UnwindData |  |
| 13 | `SetNetScheduleAccountInformation` | `0xC400` | 32 | UnwindData |  |
