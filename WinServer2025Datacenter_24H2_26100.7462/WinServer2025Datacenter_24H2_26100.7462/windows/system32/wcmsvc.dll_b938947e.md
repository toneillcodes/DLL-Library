# Binary Specification: wcmsvc.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wcmsvc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b938947eb3bbf97f18661c2b580c0b27702a8fbbc5bca7509bba4046fc336d71`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `CdeSetParameter` | `0x33170` | 2,584 | UnwindData |  |
| 2 | `CdeQueryParameter` | `0x4B230` | 1,679 | UnwindData |  |
| 1 | `CdeGetProfileList` | `0x7F530` | 746 | UnwindData |  |
| 4 | `SvchostPushServiceGlobals` | `0xAB9D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `WcmSvcMain` | `0xAB9E0` | 3,549 | UnwindData |  |
