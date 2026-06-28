# Binary Specification: nlmproxy.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\nlmproxy.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2b7d51a8e767928a7237a69b786512e1e1a21898cdfbb565f0eb901c72081f1a`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x2110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x2130` | 70 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x21B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x21F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `GetProxyDllInfo` | `0x2230` | 0 | Indeterminate |  |
