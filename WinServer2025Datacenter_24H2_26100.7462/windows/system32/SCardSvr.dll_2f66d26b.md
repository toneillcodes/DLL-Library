# Binary Specification: SCardSvr.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\SCardSvr.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2f66d26b66b0b49c8373e825406d71eac01d8da90e68ab4a9a1f0dfcfb501966`
* **Total Exported Functions:** 3

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CalaisMain` | `0x166B0` | 1,339 | UnwindData |  |
| 2 | `InitSmartCardService` | `0x235C0` | 36 | UnwindData |  |
| 3 | `SvchostPushServiceGlobals` | `0x25CC0` | 70,828 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
