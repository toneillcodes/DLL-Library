# Binary Specification: SCardDlg.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\SCardDlg.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `82a1363d2fa100c8a72998d12ffc967d33b34f02ad03b33cd617a93fe72d82f7`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `GetOpenCardNameA` | `0x3600` | 1,014 | UnwindData |  |
| 2 | `GetOpenCardNameW` | `0x3A00` | 806 | UnwindData |  |
| 3 | `SCardDlgExtendedError` | `0x3D30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `SCardUIDlgSelectCardA` | `0x3D40` | 721 | UnwindData |  |
| 5 | `SCardUIDlgSelectCardW` | `0x4020` | 708 | UnwindData |  |
