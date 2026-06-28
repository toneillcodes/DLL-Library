# Binary Specification: nlmproxy.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\nlmproxy.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `535f7579c724449f471ac12acb80bb817a51a16aac6210d9c147ac673093f10d`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x2110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x2130` | 70 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x21B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x21F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `GetProxyDllInfo` | `0x2230` | 0 | Indeterminate |  |
