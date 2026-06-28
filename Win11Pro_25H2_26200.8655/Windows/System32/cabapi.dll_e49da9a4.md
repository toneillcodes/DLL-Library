# Binary Specification: cabapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\cabapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e49da9a45bc34a36fc10b65475f795cbc137dfe1125655ccfd99556e1a90193d`
* **Total Exported Functions:** 14

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `Cab_CheckForFile` | `0x6F10` | 251 | UnwindData |  |
| 2 | `Cab_CheckIsCabinet` | `0x7020` | 154 | UnwindData |  |
| 3 | `Cab_CreateCab` | `0x70C0` | 438 | UnwindData |  |
| 4 | `Cab_CreateCabSelected` | `0x7280` | 644 | UnwindData |  |
| 5 | `Cab_Extract` | `0x7510` | 309 | UnwindData |  |
| 6 | `Cab_ExtractOne` | `0x7650` | 298 | UnwindData |  |
| 7 | `Cab_ExtractOneToBuffer` | `0x7780` | 277 | UnwindData |  |
| 8 | `Cab_ExtractSelected` | `0x78A0` | 325 | UnwindData |  |
| 9 | `Cab_ExtractSelectedToTarget` | `0x79F0` | 347 | UnwindData |  |
| 10 | `Cab_FreeBuffer` | `0x7B60` | 20 | UnwindData |  |
| 11 | `Cab_FreeFileList` | `0x7B80` | 133 | UnwindData |  |
| 12 | `Cab_FreeFileSizeList` | `0x7C10` | 51 | UnwindData |  |
| 13 | `Cab_GetFileList` | `0x7C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `Cab_GetFileSizeList` | `0x7C70` | 464 | UnwindData |  |
