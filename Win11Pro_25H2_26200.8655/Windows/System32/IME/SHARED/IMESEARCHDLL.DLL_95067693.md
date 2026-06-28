# Binary Specification: IMESEARCHDLL.DLL

## Binary Metadata
* **Original Path:** `C:\Windows\System32\IME\SHARED\IMESEARCHDLL.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9506769318c83168b1590424f26a4879521296e903083a6aa66a141ab60bdb91`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x7420` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x7450` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x7480` | 92 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x74F0` | 89 | UnwindData |  |
