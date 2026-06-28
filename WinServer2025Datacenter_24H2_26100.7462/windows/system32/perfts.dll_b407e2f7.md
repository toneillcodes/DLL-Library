# Binary Specification: perfts.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\perfts.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b407e2f7ea7818d6a91321753e04e2e4ddf0faeb6b1db9079e249fb184cd4b42`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `CloseTSObject` | `0x28D0` | 239 | UnwindData |  |
| 2 | `CollectTSObjectData` | `0x29D0` | 2,311 | UnwindData |  |
| 1 | `OpenTSObject` | `0x3800` | 78 | UnwindData |  |
| 5 | `CollectLagPerfData` | `0x3CA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `OpenLagPerfData` | `0x3CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `CloseLagPerfData` | `0x3CC0` | 23,004 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
