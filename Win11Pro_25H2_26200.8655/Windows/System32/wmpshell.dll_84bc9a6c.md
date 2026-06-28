# Binary Specification: wmpshell.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wmpshell.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `84bc9a6c49cb81528b73bfafe84f844e2f04e61025d3602dd3341638f812339d`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x80C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x80E0` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x82A0` | 52 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x82E0` | 297 | UnwindData |  |
