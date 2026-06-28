# Binary Specification: UserDataService.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\UserDataService.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `22be2543b4c08d3a8bade91256bb9569ad2c44887fc21d5658d7435f7091cc47`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CleanupUDSGlobals` | `0x43B80` | 803 | UnwindData |  |
| 4 | `SvchostPushServiceGlobals` | `0x6FFB0` | 55,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CreateInprocConnectionHandle` | `0x7D6C0` | 537 | UnwindData |  |
| 3 | `ServiceMain` | `0x7D8E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `TeardownInprocConnectionHandle` | `0x7D8F0` | 34 | UnwindData |  |
