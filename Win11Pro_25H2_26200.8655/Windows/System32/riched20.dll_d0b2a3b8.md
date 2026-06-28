# Binary Specification: riched20.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\riched20.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d0b2a3b8974861dc0c70c7c50f6d9becd8d0201c8400344cf7a08fd56268b779`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `CreateTextServices` | `0x2D0F0` | 312 | UnwindData |  |
| 10 | `RichEditANSIWndProc` | `0x33BA0` | 48 | UnwindData |  |
| 9 | `RichEdit10ANSIWndProc` | `0x62870` | 163 | UnwindData |  |
| 8 | `REExtendedRegisterClass` | `0x75E60` | 257 | UnwindData |  |
| 7 | `IID_ITextHost2` | `0x9DCB0` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `IID_ITextServices` | `0x9DF60` | 1,592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `IID_ITextHost` | `0x9E598` | 2,760 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `IID_IRichEditOleCallback` | `0x9F060` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `IID_IRichEditOle` | `0x9F0E0` | 0 | Indeterminate |  |
