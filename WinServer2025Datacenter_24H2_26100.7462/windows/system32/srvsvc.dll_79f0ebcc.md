# Binary Specification: srvsvc.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\srvsvc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `79f0ebccdbf29550890f0ecf15a4fccb96a82cace40334efb32b85bc27ab3740`
* **Total Exported Functions:** 2

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `ServiceMain` | `0x30600` | 3,205 | UnwindData |  |
| 2 | `SvchostPushServiceGlobals` | `0x31290` | 94,540 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
