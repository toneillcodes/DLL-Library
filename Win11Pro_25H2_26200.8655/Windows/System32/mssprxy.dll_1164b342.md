# Binary Specification: mssprxy.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\mssprxy.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1164b3420e245a30507fbabcd2f22a6674ec898521675b21fc020fa3379c8eb2`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllGetClassObject` | `0x1010` | 73 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x1060` | 4,960 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x23C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x2400` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `GetProxyDllInfo` | `0x2440` | 0 | Indeterminate |  |
