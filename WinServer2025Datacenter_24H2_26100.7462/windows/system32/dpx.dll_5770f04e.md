# Binary Specification: dpx.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\dpx.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5770f04e5a6e3ae68da18a677cf0ff0e2627f771ce9ce0d9083e576ec8ecd141`
* **Total Exported Functions:** 19

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 12 | `DpxNewJob` | `0x3EF0` | 68 | UnwindData |  |
| 11 | `DpxFreeMemory` | `0x4C580` | 20 | UnwindData |  |
| 7 | `DpxCheckJobExists` | `0x542B0` | 56 | UnwindData |  |
| 8 | `DpxCheckJobExistsEx` | `0x542F0` | 51 | UnwindData |  |
| 9 | `DpxDeleteJob` | `0x54330` | 53 | UnwindData |  |
| 10 | `DpxDeleteJobEx` | `0x54370` | 51 | UnwindData |  |
| 13 | `DpxNewJobEx` | `0x543B0` | 63 | UnwindData |  |
| 14 | `DpxRestoreJob` | `0x54400` | 68 | UnwindData |  |
| 15 | `DpxRestoreJobEx` | `0x54450` | 63 | UnwindData |  |
| 16 | `DpxRestoreOrNewJob` | `0x544A0` | 67 | UnwindData |  |
| 17 | `DpxRestoreOrNewJobEx` | `0x544F0` | 62 | UnwindData |  |
| 1 | `ApplyDeltaB` | `0x6ABD0` | 235 | UnwindData |  |
| 2 | `ApplyDeltaGetReverseB` | `0x6ACD0` | 291 | UnwindData |  |
| 3 | `ApplyDeltaProvidedB` | `0x6AE00` | 290 | UnwindData |  |
| 4 | `CreateDeltaB` | `0x6C3F0` | 253 | UnwindData |  |
| 5 | `DeltaFree` | `0x6C500` | 20 | UnwindData |  |
| 6 | `DeltaNormalizeProvidedB` | `0x6C7C0` | 41 | UnwindData |  |
| 19 | `GetDeltaSignatureB` | `0x6C7F0` | 56 | UnwindData |  |
| 18 | `GetDeltaInfoB` | `0x6C860` | 282 | UnwindData |  |
