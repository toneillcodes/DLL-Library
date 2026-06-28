# Binary Specification: imecfm.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\IME\SHARED\imecfm.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `be30c2c634e43ef58015cf9b0269be2e434fb1291752274c892ff8d0340a0bfe`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xCAD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0xCAF0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0xCB40` | 138 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0xCBD0` | 24 | UnwindData |  |
