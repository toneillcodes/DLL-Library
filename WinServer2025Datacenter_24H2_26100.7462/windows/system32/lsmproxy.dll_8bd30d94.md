# Binary Specification: lsmproxy.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\lsmproxy.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8bd30d94712954fd1c408b5ff00c019867ab080e52d91623065c12774efcc70c`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllGetClassObject` | `0x1180` | 70 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x19F0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x1A40` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x1A80` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `GetProxyDllInfo` | `0x1AC0` | 0 | Indeterminate |  |
