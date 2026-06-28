# Binary Specification: comcat.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\comcat.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `eef2f80fd712f883e761d10fca77848f62ad84eae472566b78a4acbab5d23aea`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllGetClassObject` | `0x0` | - | Forwarded | Forwarded to: `Ole32.DllGetClassObject` |
| 1 | `DllCanUnloadNow` | `0x1730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x1740` | 0 | Indeterminate |  |
| 4 | `DllUnregisterServer` | `0x1740` | 0 | Indeterminate |  |
