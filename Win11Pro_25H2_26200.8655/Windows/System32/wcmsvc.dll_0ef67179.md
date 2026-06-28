# Binary Specification: wcmsvc.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wcmsvc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0ef67179d17f7d43389e5f4d06442b637c1939c7816cf6458605b35bae576aed`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `CdeSetParameter` | `0x2A4E0` | 2,584 | UnwindData |  |
| 2 | `CdeQueryParameter` | `0x492E0` | 1,679 | UnwindData |  |
| 1 | `CdeGetProfileList` | `0x7ADE0` | 746 | UnwindData |  |
| 4 | `SvchostPushServiceGlobals` | `0xA6750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `WcmSvcMain` | `0xA6760` | 3,549 | UnwindData |  |
