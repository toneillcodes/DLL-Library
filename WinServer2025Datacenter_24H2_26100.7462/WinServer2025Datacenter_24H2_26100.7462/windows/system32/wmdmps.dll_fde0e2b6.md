# Binary Specification: wmdmps.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wmdmps.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fde0e2b65fdd05b03f03739a47487f2c5179c22ff051a16165600f3e28d6b018`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `GetProxyDllInfo` | `0x1170` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x11A0` | 70 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x11F0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x1260` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x12A0` | 544 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
