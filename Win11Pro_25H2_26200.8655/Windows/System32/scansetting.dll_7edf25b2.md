# Binary Specification: scansetting.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\scansetting.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7edf25b2d10c8fdf50e56bad9f282324c8e1a4381ed731a81af2a1ac012d74ba`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `DllMain` | `0x13D0` | 381 | UnwindData |  |
| 2 | `GetImageDialog` | `0x12940` | 891 | UnwindData |  |
| 3 | `ProfilesDialog` | `0x12F30` | 270 | UnwindData |  |
| 5 | `DllCanUnloadNow` | `0x13060` | 30,608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `GetDefaultProfileScan` | `0x1A7F0` | 1,563 | UnwindData |  |
| 4 | `ProgDlgTakeFgIfShowing` | `0x1AE20` | 129 | UnwindData |  |
