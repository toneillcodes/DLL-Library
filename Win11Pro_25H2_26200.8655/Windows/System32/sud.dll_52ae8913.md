# Binary Specification: sud.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\sud.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `52ae8913ff359014bf6e83eea79f76f909a8c09818d1fd3e99ba49c6f07e5b0c`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xDCE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0xDD00` | 26 | UnwindData |  |
| 3 | `DllRegisterServer` | `0xDD20` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0xDD50` | 49,468 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
