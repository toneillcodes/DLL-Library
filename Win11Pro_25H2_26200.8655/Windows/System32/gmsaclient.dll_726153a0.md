# Binary Specification: gmsaclient.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\gmsaclient.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `726153a099eb29da88fb76594be72f6d175f504aadf397f3f613698a6cc51b5b`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `GMSAAdd` | `0xC850` | 343 | UnwindData |  |
| 2 | `GMSACheckIfExistsInAD` | `0xC9B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `GMSACleanup` | `0xC9D0` | 415 | UnwindData |  |
| 4 | `GMSADelete` | `0xCB80` | 970 | UnwindData |  |
| 5 | `GMSAGetPassword` | `0xCF50` | 78 | UnwindData |  |
| 6 | `GMSAInit` | `0xCFB0` | 852 | UnwindData |  |
| 7 | `GMSARefreshPasswords` | `0xD310` | 576 | UnwindData |  |
