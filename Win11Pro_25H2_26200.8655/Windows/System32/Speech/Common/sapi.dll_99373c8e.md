# Binary Specification: sapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Speech\Common\sapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `99373c8e7a45579b834eca91eb02fa017aed7db2019b7ab7e45799b0b7b201ec`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x1FF0` | 171,552 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x2BE10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x2BE30` | 90 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x2BE90` | 84 | UnwindData |  |
