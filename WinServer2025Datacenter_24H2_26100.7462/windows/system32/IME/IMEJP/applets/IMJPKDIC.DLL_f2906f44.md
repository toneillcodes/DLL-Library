# Binary Specification: IMJPKDIC.DLL

## Binary Metadata
* **Original Path:** `c:\windows\system32\IME\IMEJP\applets\IMJPKDIC.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f2906f44df839f9334b204bb94c360fff9cd708f65b9c9a029550a653e0f3de4`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CreateIImeSkdicInstance` | `0xE940` | 123 | UnwindData |  |
| 2 | `DllCanUnloadNow` | `0xE9D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0xE9F0` | 188 | UnwindData |  |
| 4 | `DllRegisterServer` | `0xEAE0` | 400 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0xEC80` | 259 | UnwindData |  |
