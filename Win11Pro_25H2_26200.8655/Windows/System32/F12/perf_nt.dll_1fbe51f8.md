# Binary Specification: perf_nt.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\F12\perf_nt.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1fbe51f8d780aaa9c86726e1ccb27eb9c0c85c025b329ac0f56e65f730b775ac`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllRegisterServer` | `0x68AF0` | 10,384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x68AF0` | 10,384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x6B380` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x6B3B0` | 282,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `QueryModernApplicationData` | `0xB04E0` | 428,793 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
