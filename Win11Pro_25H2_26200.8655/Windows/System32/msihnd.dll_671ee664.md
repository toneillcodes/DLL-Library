# Binary Specification: msihnd.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\msihnd.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `671ee6649debdba28590454b1e8bb80f1be3d72f11b3b4eac4485db9a38d066c`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllRegisterServer` | `0x1FBC0` | 30 | UnwindData |  |
| 2 | `DllUnregisterServer` | `0x1FBF0` | 30 | UnwindData |  |
| 3 | `DllCanUnloadNow` | `0x20DE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllGetClassObject` | `0x20E00` | 126,531 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
