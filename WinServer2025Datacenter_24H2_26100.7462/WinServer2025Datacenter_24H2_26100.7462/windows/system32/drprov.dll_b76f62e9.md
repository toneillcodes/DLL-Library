# Binary Specification: drprov.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\drprov.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b76f62e97b1321ec658ead63ca4cbe1b733775c62ebb701752e7f2f8f1f12367`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 10 | `NPGetUniversalName` | `0x1010` | 94 | UnwindData |  |
| 7 | `NPGetConnection` | `0x1250` | 540 | UnwindData |  |
| 8 | `NPGetResourceInformation` | `0x1480` | 78 | UnwindData |  |
| 6 | `NPGetCaps` | `0x1E70` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `NPOpenEnum` | `0x1F10` | 893 | UnwindData |  |
| 5 | `NPEnumResource` | `0x23D0` | 106 | UnwindData |  |
| 3 | `NPCancelConnection` | `0x26B0` | 29 | UnwindData |  |
| 4 | `NPCloseEnum` | `0x2B00` | 125 | UnwindData |  |
| 1 | `NPAddConnection` | `0x37B0` | 31 | UnwindData |  |
| 2 | `NPAddConnection3` | `0x37E0` | 514 | UnwindData |  |
| 49 | `NPGetConnectionPerformance` | `0x39F0` | 39 | UnwindData |  |
| 9 | `NPGetResourceParent` | `0x3A20` | 603 | UnwindData |  |
