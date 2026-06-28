# Binary Specification: IMESEARCHDLL.DLL

## Binary Metadata
* **Original Path:** `c:\windows\system32\IME\SHARED\IMESEARCHDLL.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `15c9d08ad47f2432f185baca443f0e7379fc7e7e803e1b5ec1048d3728450a24`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x7420` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x7450` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x7480` | 92 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x74F0` | 89 | UnwindData |  |
