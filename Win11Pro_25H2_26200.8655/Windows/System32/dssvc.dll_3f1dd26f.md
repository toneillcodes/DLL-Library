# Binary Specification: dssvc.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\dssvc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3f1dd26f2931e52cd2d781dadcbfc60bdc2a3e4c4c84ed664ba5b7e01878a7ee`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `InitializeService` | `0xB9F0` | 153 | UnwindData |  |
| 2 | `ServiceMain` | `0xBBA0` | 459 | UnwindData |  |
| 3 | `SvchostPushServiceGlobals` | `0xBF90` | 15,776 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DSSCreateSharedFileTokenEx` | `0xFD30` | 1,045 | UnwindData |  |
| 5 | `DSSFreeToken` | `0x10150` | 24 | UnwindData |  |
