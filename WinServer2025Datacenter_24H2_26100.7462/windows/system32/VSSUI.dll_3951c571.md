# Binary Specification: VSSUI.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\VSSUI.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3951c5718aeb7f7d6a0814c5b062b13b7d0b6bdd03a325d86c566cced3c02aad`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x3950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x3970` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x39A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x39C0` | 11,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `ShowDialog` | `0x6620` | 410 | UnwindData |  |
