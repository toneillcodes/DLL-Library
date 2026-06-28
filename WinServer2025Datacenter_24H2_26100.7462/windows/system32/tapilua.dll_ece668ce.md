# Binary Specification: tapilua.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\tapilua.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ece668ce457e2e0aede0f03b5ea756104504655c6ff6e84e9e0ca774e73c6bb9`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `GetProxyDllInfo` | `0x2150` | 12,192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x50F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x5120` | 129 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x5280` | 63 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x52D0` | 0 | Indeterminate |  |
