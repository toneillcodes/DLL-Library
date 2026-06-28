# Binary Specification: IMJPKDIC.DLL

## Binary Metadata
* **Original Path:** `C:\Windows\System32\IME\IMEJP\APPLETS\IMJPKDIC.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1dd2d5a50e186acf9975f82094cf77a687061d198ad371de6b64df42eb6d195b`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CreateIImeSkdicInstance` | `0xE950` | 123 | UnwindData |  |
| 2 | `DllCanUnloadNow` | `0xE9E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0xEA00` | 188 | UnwindData |  |
| 4 | `DllRegisterServer` | `0xEAF0` | 400 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0xEC90` | 259 | UnwindData |  |
