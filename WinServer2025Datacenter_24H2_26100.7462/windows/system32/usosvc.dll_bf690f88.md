# Binary Specification: usosvc.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\usosvc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `bf690f88cd074e2abb82f6704f9305cd2fc24ccdffbf3cc978820d51f06fc54a`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `ServiceMain` | `0x9FE0` | 178 | UnwindData |  |
| 3 | `SvchostPushServiceGlobals` | `0xA0A0` | 261 | UnwindData |  |
| 4 | `DllCanUnloadNow` | `0xAC80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllGetClassObject` | `0xACA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllMain` | `0xACC0` | 32 | UnwindData |  |
| 1 | `GeneralizeForImaging` | `0xC660` | 333 | UnwindData |  |
