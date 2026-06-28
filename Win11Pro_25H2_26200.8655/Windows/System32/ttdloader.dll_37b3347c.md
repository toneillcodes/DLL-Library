# Binary Specification: ttdloader.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ttdloader.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `37b3347cc16763a39645d90004ceb6de45bd0524ea263c6f27528e83dca79872`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `GetCfgPointers` | `0x1040` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `InjectThread` | `0x1210` | 102 | UnwindData |  |
| 3 | `GetCurrentProcessId` | `0x3810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `GetCurrentThreadId` | `0x3830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `GetCurrentProcess` | `0x3850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `GetLastError` | `0x3860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `GetTickCount` | `0x3880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `QueryPerformanceCounter` | `0x38A0` | 24 | UnwindData |  |
| 10 | `StubDllEntry` | `0x38C0` | 13,560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `ntdllLdrInitializeThunk` | `0x6DB8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `ParametersBlock` | `0x6DC8` | 0 | Indeterminate |  |
