# Binary Specification: osbaseln.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\osbaseln.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `cd97fcd8a4005d5b1098ca9204b63e46cd40f3558d063634f50500bc4033d3b9`
* **Total Exported Functions:** 15

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `EnumOsBaselineComponentsA` | `0x1920` | 173 | UnwindData |  |
| 5 | `EnumOsOutOfDateComponentsA` | `0x19E0` | 173 | UnwindData |  |
| 7 | `GetOsBaselineComponentInfoA` | `0x1AA0` | 330 | UnwindData |  |
| 9 | `GetOsInstalledComponentInfoA` | `0x1BF0` | 229 | UnwindData |  |
| 2 | `CloseOsBaseline` | `0x2810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `EnumOsBaselineComponentsW` | `0x2830` | 173 | UnwindData |  |
| 6 | `EnumOsOutOfDateComponentsW` | `0x28F0` | 173 | UnwindData |  |
| 8 | `GetOsBaselineComponentInfoW` | `0x29B0` | 330 | UnwindData |  |
| 10 | `GetOsInstalledComponentInfoW` | `0x2B00` | 229 | UnwindData |  |
| 11 | `GetOsLatestBaselineServicePack` | `0x2BF0` | 110 | UnwindData |  |
| 12 | `OpenOsBaseline` | `0x2C70` | 123 | UnwindData |  |
| 1 | *Ordinal Only* | `0x2D00` | 1,338 | UnwindData |  |
| 13 | `pGetOsBaselineCurrentVersion` | `0x3860` | 429 | UnwindData |  |
| 14 | `pGetOsCurrentBaselineServicePack` | `0x3EB0` | 201 | UnwindData |  |
| 15 | `pOpenOsBaselineByVersion` | `0x4070` | 501 | UnwindData |  |
