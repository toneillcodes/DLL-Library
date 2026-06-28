# Binary Specification: dbnmpntw.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\dbnmpntw.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f5adf1662bec755ef2ec6e4066aaacb8b4ce19fcc776d0157c6b5daa273e1387`
* **Total Exported Functions:** 16

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 13 | `ConnectionCheckForData` | `0x1910` | 464 | UnwindData |  |
| 4 | `ConnectionClose` | `0x1AF0` | 204 | UnwindData |  |
| 5 | `ConnectionError` | `0x1DC0` | 66 | UnwindData |  |
| 15 | `ConnectionErrorW` | `0x1F40` | 25 | UnwindData |  |
| 9 | `ConnectionMode` | `0x20F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `ConnectionObjectSize` | `0x2110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `ConnectionOpen` | `0x2120` | 325 | UnwindData |  |
| 14 | `ConnectionOpenW` | `0x2680` | 396 | UnwindData |  |
| 2 | `ConnectionRead` | `0x2820` | 1,710 | UnwindData |  |
| 12 | `ConnectionServerEnum` | `0x2EE0` | 82 | UnwindData |  |
| 16 | `ConnectionServerEnumW` | `0x3140` | 80 | UnwindData |  |
| 10 | `ConnectionStatus` | `0x33B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `ConnectionTransact` | `0x33D0` | 1,019 | UnwindData |  |
| 6 | `ConnectionVer` | `0x37E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `ConnectionWrite` | `0x37F0` | 644 | UnwindData |  |
| 8 | `ConnectionWriteOOB` | `0x3A80` | 713 | UnwindData |  |
