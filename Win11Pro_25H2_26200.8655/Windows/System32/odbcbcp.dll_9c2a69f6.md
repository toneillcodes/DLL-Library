# Binary Specification: odbcbcp.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\odbcbcp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9c2a69f6b2c1f50695f4671ca520901fe325f8481850b78b152e1095633f73c0`
* **Total Exported Functions:** 28

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 24 | `LibMain` | `0x1FA0` | 493 | UnwindData |  |
| 27 | `SQLCloseEnumServers` | `0x2660` | 97 | UnwindData |  |
| 26 | `SQLGetNextEnumeration` | `0x26D0` | 40 | UnwindData |  |
| 25 | `SQLInitEnumServers` | `0x2700` | 238 | UnwindData |  |
| 23 | `SQLLinkedCatalogsA` | `0x2800` | 180 | UnwindData |  |
| 22 | `SQLLinkedCatalogsW` | `0x2950` | 127 | UnwindData |  |
| 21 | `SQLLinkedServers` | `0x2B50` | 2,848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `bcp_batch` | `0x3670` | 387 | UnwindData |  |
| 3 | `bcp_bind` | `0x3800` | 11 | UnwindData |  |
| 4 | `bcp_colfmt` | `0x3A90` | 14 | UnwindData |  |
| 5 | `bcp_collen` | `0x3D20` | 436 | UnwindData |  |
| 6 | `bcp_colptr` | `0x3EE0` | 439 | UnwindData |  |
| 8 | `bcp_columns` | `0x40A0` | 416 | UnwindData |  |
| 9 | `bcp_control` | `0x4250` | 438 | UnwindData |  |
| 10 | `bcp_done` | `0x4410` | 401 | UnwindData |  |
| 12 | `bcp_exec` | `0x45B0` | 422 | UnwindData |  |
| 28 | `bcp_getcolfmt` | `0x4760` | 11 | UnwindData |  |
| 11 | `bcp_initA` | `0x49B0` | 640 | UnwindData |  |
| 18 | `bcp_initW` | `0x4C40` | 571 | UnwindData |  |
| 13 | `bcp_moretext` | `0x4E90` | 438 | UnwindData |  |
| 15 | `bcp_readfmtA` | `0x5050` | 450 | UnwindData |  |
| 19 | `bcp_readfmtW` | `0x5220` | 419 | UnwindData |  |
| 14 | `bcp_sendrow` | `0x53D0` | 395 | UnwindData |  |
| 29 | `bcp_setcolfmt` | `0x5570` | 8 | UnwindData |  |
| 16 | `bcp_writefmtA` | `0x5780` | 365 | UnwindData |  |
| 20 | `bcp_writefmtW` | `0x5900` | 419 | UnwindData |  |
| 1 | `dbprtypeA` | `0x5AB0` | 870 | UnwindData |  |
| 17 | `dbprtypeW` | `0x5E20` | 0 | Indeterminate |  |
