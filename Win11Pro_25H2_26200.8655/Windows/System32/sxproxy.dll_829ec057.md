# Binary Specification: sxproxy.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\sxproxy.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `829ec0571ca7c08fd5c8dbfa2c850014676a181132584102b5d4924c604aa3a2`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x1740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x1760` | 70 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x17E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x1820` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `GetProxyDllInfo` | `0x1860` | 0 | Indeterminate |  |
