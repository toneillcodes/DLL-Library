# Binary Specification: PhoneService.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\PhoneService.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `bdeb0ee810101a2da860181833f130c36cc652ef4c639fec38d3c4075c2fc6c8`
* **Total Exported Functions:** 3

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CreateInProcPhoneService` | `0x7740` | 380 | UnwindData |  |
| 2 | `ServiceMain` | `0x94A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `SvchostPushServiceGlobals` | `0x94B0` | 536,876 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
