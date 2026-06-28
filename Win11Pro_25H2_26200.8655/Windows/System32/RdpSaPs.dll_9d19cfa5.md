# Binary Specification: RdpSaPs.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\RdpSaPs.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9d19cfa5c31bdea9e341d0730b119f815cb4e94fb626f83293d3334d4151e1ce`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x1FA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x1FC0` | 70 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x2040` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x2080` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `GetProxyDllInfo` | `0x20C0` | 0 | Indeterminate |  |
