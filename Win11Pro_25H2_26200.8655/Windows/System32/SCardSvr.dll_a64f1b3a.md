# Binary Specification: SCardSvr.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\SCardSvr.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a64f1b3ac5b596a20ee2d41e8754f18686e1b0ca595d46c0217466053fc1d5fe`
* **Total Exported Functions:** 3

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CalaisMain` | `0x16710` | 1,339 | UnwindData |  |
| 2 | `InitSmartCardService` | `0x210D0` | 36 | UnwindData |  |
| 3 | `SvchostPushServiceGlobals` | `0x21120` | 88,284 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
