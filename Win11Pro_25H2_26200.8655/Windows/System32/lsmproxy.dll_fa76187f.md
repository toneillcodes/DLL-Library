# Binary Specification: lsmproxy.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\lsmproxy.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fa76187f95d9eaf20fcf120f421284546c53dd6815dcbc0426f41fa9d4b421d3`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllGetClassObject` | `0x1180` | 70 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x21D0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x2220` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x2260` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `GetProxyDllInfo` | `0x22A0` | 0 | Indeterminate |  |
