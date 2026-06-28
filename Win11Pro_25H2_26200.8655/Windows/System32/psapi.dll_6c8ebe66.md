# Binary Specification: psapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\psapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6c8ebe6621224d11ded0c920873d67b5255fd515e8c4ea803cd587c8232bee5c`
* **Total Exported Functions:** 27

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 22 | `GetProcessMemoryInfo` | `0x1010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `GetModuleBaseNameW` | `0x1030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `GetModuleInformation` | `0x1050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `GetModuleFileNameExW` | `0x1070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `EnumProcessModules` | `0x1090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `GetProcessImageFileNameW` | `0x10B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `EnumProcesses` | `0x10D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `QueryWorkingSetEx` | `0x10F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `GetModuleFileNameExA` | `0x1110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `GetMappedFileNameW` | `0x1130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `EnumProcessModulesEx` | `0x1150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `GetProcessImageFileNameA` | `0x1170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `GetPerformanceInfo` | `0x1190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `EmptyWorkingSet` | `0x11B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `GetModuleBaseNameA` | `0x11D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `QueryWorkingSet` | `0x11F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `GetDeviceDriverBaseNameW` | `0x1210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `GetDeviceDriverFileNameW` | `0x1230` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `EnumDeviceDrivers` | `0x1250` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `GetMappedFileNameA` | `0x1270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `GetDeviceDriverBaseNameA` | `0x1290` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `EnumPageFilesA` | `0x1530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `EnumPageFilesW` | `0x1550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `GetDeviceDriverFileNameA` | `0x1570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `GetWsChangesEx` | `0x1590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `GetWsChanges` | `0x15B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `InitializeProcessForWsWatch` | `0x15D0` | 0 | Indeterminate |  |
