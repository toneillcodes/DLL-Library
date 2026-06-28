# Binary Specification: WMSPDMOE.DLL

## Binary Metadata
* **Original Path:** `C:\Windows\System32\WMSPDMOE.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7797f7c54dccf01b885b430e49c7b1bb110c6678394493f392e200d31979ea76`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `DllRegisterServer` | `0x26E90` | 188 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x26F60` | 1,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `CreateInstance` | `0x27680` | 121 | UnwindData |  |
| 2 | `DllCanUnloadNow` | `0x27700` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0x27730` | 231 | UnwindData |  |
