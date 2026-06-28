# Binary Specification: scansetting.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\scansetting.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `caa3496bfe0fbb3bac3a0339d8d32e2c0823c004402ad1750001b630eba89a8a`
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
