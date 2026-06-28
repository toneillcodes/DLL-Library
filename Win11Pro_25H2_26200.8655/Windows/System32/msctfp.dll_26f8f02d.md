# Binary Specification: msctfp.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\msctfp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `26f8f02d3caf6e74834f258538749963461aaf80b186874ab918e9d69ce4d0b4`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x1D00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x1D20` | 53 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x1D90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x1DC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `GetProxyDllInfo` | `0x1DF0` | 0 | Indeterminate |  |
