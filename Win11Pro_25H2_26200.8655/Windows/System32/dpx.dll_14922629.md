# Binary Specification: dpx.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\dpx.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `14922629e54a8024e28178da3a575831fa508449bc6043fdd2e879e5d8c161fc`
* **Total Exported Functions:** 19

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 12 | `DpxNewJob` | `0x3F00` | 68 | UnwindData |  |
| 11 | `DpxFreeMemory` | `0x4C4C0` | 20 | UnwindData |  |
| 7 | `DpxCheckJobExists` | `0x542D0` | 56 | UnwindData |  |
| 8 | `DpxCheckJobExistsEx` | `0x54310` | 51 | UnwindData |  |
| 9 | `DpxDeleteJob` | `0x54350` | 53 | UnwindData |  |
| 10 | `DpxDeleteJobEx` | `0x54390` | 51 | UnwindData |  |
| 13 | `DpxNewJobEx` | `0x543D0` | 63 | UnwindData |  |
| 14 | `DpxRestoreJob` | `0x54420` | 68 | UnwindData |  |
| 15 | `DpxRestoreJobEx` | `0x54470` | 63 | UnwindData |  |
| 16 | `DpxRestoreOrNewJob` | `0x544C0` | 67 | UnwindData |  |
| 17 | `DpxRestoreOrNewJobEx` | `0x54510` | 62 | UnwindData |  |
| 1 | `ApplyDeltaB` | `0x6ABF0` | 235 | UnwindData |  |
| 2 | `ApplyDeltaGetReverseB` | `0x6ACF0` | 291 | UnwindData |  |
| 3 | `ApplyDeltaProvidedB` | `0x6AE20` | 290 | UnwindData |  |
| 4 | `CreateDeltaB` | `0x6C410` | 253 | UnwindData |  |
| 5 | `DeltaFree` | `0x6C520` | 20 | UnwindData |  |
| 6 | `DeltaNormalizeProvidedB` | `0x6C7E0` | 41 | UnwindData |  |
| 19 | `GetDeltaSignatureB` | `0x6C810` | 56 | UnwindData |  |
| 18 | `GetDeltaInfoB` | `0x6C880` | 282 | UnwindData |  |
