# Binary Specification: sxproxy.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\sxproxy.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a128e1dfc38500830db629af0b793f65cc2ea803f5c6d9097df632fdace50170`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x1740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x1760` | 70 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x17E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x1820` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `GetProxyDllInfo` | `0x1860` | 0 | Indeterminate |  |
