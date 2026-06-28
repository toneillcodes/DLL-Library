# Binary Specification: riched20.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\riched20.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `537634dac88b41632706e872d0ba3fd3a868a42e80e108e5f9e0d36bd0e42b26`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `CreateTextServices` | `0x2CF10` | 312 | UnwindData |  |
| 10 | `RichEditANSIWndProc` | `0x339C0` | 48 | UnwindData |  |
| 9 | `RichEdit10ANSIWndProc` | `0x624F0` | 163 | UnwindData |  |
| 8 | `REExtendedRegisterClass` | `0x75AE0` | 257 | UnwindData |  |
| 7 | `IID_ITextHost2` | `0x96A80` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `IID_ITextServices` | `0x96D30` | 1,592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `IID_ITextHost` | `0x97368` | 1,640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `IID_IRichEditOleCallback` | `0x979D0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `IID_IRichEditOle` | `0x97A50` | 0 | Indeterminate |  |
