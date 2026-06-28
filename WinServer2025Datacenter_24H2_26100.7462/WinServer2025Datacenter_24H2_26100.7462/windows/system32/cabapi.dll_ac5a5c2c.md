# Binary Specification: cabapi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\cabapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ac5a5c2c8871df5aaa20938316576b7ef8647394b21b7ad63a35e196b3c565e6`
* **Total Exported Functions:** 14

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `Cab_CheckForFile` | `0x6F00` | 251 | UnwindData |  |
| 2 | `Cab_CheckIsCabinet` | `0x7010` | 154 | UnwindData |  |
| 3 | `Cab_CreateCab` | `0x70B0` | 438 | UnwindData |  |
| 4 | `Cab_CreateCabSelected` | `0x7270` | 644 | UnwindData |  |
| 5 | `Cab_Extract` | `0x7500` | 309 | UnwindData |  |
| 6 | `Cab_ExtractOne` | `0x7640` | 298 | UnwindData |  |
| 7 | `Cab_ExtractOneToBuffer` | `0x7770` | 277 | UnwindData |  |
| 8 | `Cab_ExtractSelected` | `0x7890` | 325 | UnwindData |  |
| 9 | `Cab_ExtractSelectedToTarget` | `0x79E0` | 347 | UnwindData |  |
| 10 | `Cab_FreeBuffer` | `0x7B50` | 20 | UnwindData |  |
| 11 | `Cab_FreeFileList` | `0x7B70` | 133 | UnwindData |  |
| 12 | `Cab_FreeFileSizeList` | `0x7C00` | 51 | UnwindData |  |
| 13 | `Cab_GetFileList` | `0x7C40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `Cab_GetFileSizeList` | `0x7C60` | 464 | UnwindData |  |
