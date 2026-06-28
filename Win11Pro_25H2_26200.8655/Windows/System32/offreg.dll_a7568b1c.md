# Binary Specification: offreg.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\offreg.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a7568b1c9f72254be1235f0b291885d953eaa976734d522b40fd1bb098bffe7c`
* **Total Exported Functions:** 28

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `ORCloseHive` | `0x2100` | 49 | UnwindData |  |
| 3 | `ORCreateHive` | `0x2200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `ORCreateHiveEx` | `0x2210` | 150 | UnwindData |  |
| 10 | `ORFlushHive` | `0x25E0` | 334 | UnwindData |  |
| 16 | `OROpenHive` | `0x2740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `OROpenHiveByHandle` | `0x2760` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `ORSaveHive` | `0x2A10` | 20 | UnwindData |  |
| 24 | `ORSaveHiveEx` | `0x2A30` | 246 | UnwindData |  |
| 25 | `ORSaveHiveToHandle` | `0x2BD0` | 109 | UnwindData |  |
| 2 | `ORCloseKey` | `0x2DD0` | 128 | UnwindData |  |
| 5 | `ORCreateKey` | `0x2E60` | 1,639 | UnwindData |  |
| 6 | `ORDeleteKey` | `0x34D0` | 465 | UnwindData |  |
| 8 | `OREnumKey` | `0x3700` | 239 | UnwindData |  |
| 14 | `ORGetVirtualFlags` | `0x38A0` | 144 | UnwindData |  |
| 18 | `OROpenKey` | `0x3940` | 289 | UnwindData |  |
| 19 | `ORQueryInfoKey` | `0x3CE0` | 542 | UnwindData |  |
| 20 | `ORQueryInfoKeyEx` | `0x3F10` | 531 | UnwindData |  |
| 22 | `ORRenameKey` | `0x4220` | 48 | UnwindData |  |
| 28 | `ORSetVirtualFlags` | `0x4510` | 184 | UnwindData |  |
| 7 | `ORDeleteValue` | `0x4640` | 246 | UnwindData |  |
| 9 | `OREnumValue` | `0x4740` | 246 | UnwindData |  |
| 12 | `ORGetValue` | `0x4B20` | 483 | UnwindData |  |
| 21 | `ORQueryInfoKeyValueEx` | `0x4ED0` | 232 | UnwindData |  |
| 27 | `ORSetValue` | `0x4FC0` | 23 | UnwindData |  |
| 11 | `ORGetKeySecurity` | `0x5680` | 218 | UnwindData |  |
| 26 | `ORSetKeySecurity` | `0x5760` | 437 | UnwindData |  |
| 13 | `ORGetVersion` | `0x59D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `ORMergeHives` | `0x59F0` | 611 | UnwindData |  |
