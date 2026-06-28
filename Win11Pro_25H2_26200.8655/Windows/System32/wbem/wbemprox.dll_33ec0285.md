# Binary Specification: wbemprox.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wbem\wbemprox.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `33ec0285ca9f4bed619c66ed6c216273183072db4dab1f7b5c958353d4c0702d`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllGetClassObject` | `0x5020` | 503 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x5920` | 5,472 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x6E80` | 246 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x6F80` | 145 | UnwindData |  |
