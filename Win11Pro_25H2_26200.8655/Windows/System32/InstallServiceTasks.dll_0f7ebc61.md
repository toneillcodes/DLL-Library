# Binary Specification: InstallServiceTasks.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\InstallServiceTasks.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0f7ebc61374d902d00705afd9e8d114de4182135c43c1d4f3e2fce7262e973b7`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `ForceAppInUseRestart` | `0xFD60` | 511 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x10290` | 10,752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0x10290` | 10,752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x12C90` | 77 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x12CF0` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `GetSetting` | `0x12ED0` | 215,756 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
