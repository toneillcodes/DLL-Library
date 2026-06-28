# Binary Specification: wbemprox.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wbem\wbemprox.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `637fc7d29c2be3d3ff650b18f3ba73668b453be4bbab33c9c4f32e473a260bfc`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllGetClassObject` | `0x5020` | 503 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x5920` | 5,472 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x6E80` | 246 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x6F80` | 145 | UnwindData |  |
