# Binary Specification: UserDataService.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\UserDataService.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `820987c924e24f4dc1729eeed74ab18165c4f8263b1537386410ec38b2393fc2`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CleanupUDSGlobals` | `0x43B90` | 803 | UnwindData |  |
| 4 | `SvchostPushServiceGlobals` | `0x6FFC0` | 55,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CreateInprocConnectionHandle` | `0x7D6E0` | 537 | UnwindData |  |
| 3 | `ServiceMain` | `0x7D900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `TeardownInprocConnectionHandle` | `0x7D910` | 34 | UnwindData |  |
