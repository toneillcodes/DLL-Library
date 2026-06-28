# Binary Specification: gmsaclient.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\gmsaclient.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `cfc6e1ebe0d2233759ebaf69568df2e2d80ebfff77e95f9e23b8360bfb2e5cdf`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `GMSAAdd` | `0xC740` | 343 | UnwindData |  |
| 2 | `GMSACheckIfExistsInAD` | `0xC8A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `GMSACleanup` | `0xC8C0` | 415 | UnwindData |  |
| 4 | `GMSADelete` | `0xCA70` | 970 | UnwindData |  |
| 5 | `GMSAGetPassword` | `0xCE40` | 78 | UnwindData |  |
| 6 | `GMSAInit` | `0xCEA0` | 852 | UnwindData |  |
| 7 | `GMSARefreshPasswords` | `0xD200` | 576 | UnwindData |  |
