# Binary Specification: odbccu32.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\odbccu32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1d0ef4e60c6c10967cf30a049994db7653453d4e7bc27f8d779b0249646219af`
* **Total Exported Functions:** 37

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 34 | `SQLGetDescRec` | `0xA270` | 709 | UnwindData |  |
| 6 | `ReleaseCLStmtResources` | `0xAAF0` | 248 | UnwindData |  |
| 4 | `SQLBindCol` | `0xB070` | 735 | UnwindData |  |
| 72 | `SQLBindParameter` | `0xB360` | 382 | UnwindData |  |
| 78 | `SQLBulkOperations` | `0xB4F0` | 50 | UnwindData |  |
| 5 | `SQLCancel` | `0xB530` | 489 | UnwindData |  |
| 26 | `SQLCloseCursor` | `0xB720` | 377 | UnwindData |  |
| 29 | `SQLEndTran` | `0xB8A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `SQLExecDirect` | `0xB8B0` | 285 | UnwindData |  |
| 12 | `SQLExecute` | `0xB9E0` | 46 | UnwindData |  |
| 59 | `SQLExtendedFetch` | `0xBA20` | 222 | UnwindData |  |
| 13 | `SQLFetch` | `0xBB10` | 296 | UnwindData |  |
| 30 | `SQLFetchScroll` | `0xBC40` | 314 | UnwindData |  |
| 31 | `SQLFreeHandle` | `0xBD80` | 76 | UnwindData |  |
| 16 | `SQLFreeStmt` | `0xBEB0` | 181 | UnwindData |  |
| 43 | `SQLGetData` | `0xBF70` | 321 | UnwindData |  |
| 33 | `SQLGetDescField` | `0xC0C0` | 124 | UnwindData |  |
| 45 | `SQLGetInfo` | `0xC5C0` | 325 | UnwindData |  |
| 38 | `SQLGetStmtAttr` | `0xC8A0` | 222 | UnwindData |  |
| 46 | `SQLGetStmtOption` | `0xC990` | 948 | UnwindData |  |
| 61 | `SQLMoreResults` | `0xCD50` | 312 | UnwindData |  |
| 62 | `SQLNativeSql` | `0xCE90` | 460 | UnwindData |  |
| 63 | `SQLNumParams` | `0xD070` | 150 | UnwindData |  |
| 48 | `SQLParamData` | `0xD110` | 46 | UnwindData |  |
| 64 | `SQLParamOptions` | `0xD150` | 288 | UnwindData |  |
| 19 | `SQLPrepare` | `0xD280` | 288 | UnwindData |  |
| 49 | `SQLPutData` | `0xD3B0` | 49 | UnwindData |  |
| 20 | `SQLRowCount` | `0xD3F0` | 150 | UnwindData |  |
| 39 | `SQLSetConnectAttr` | `0xD490` | 22 | UnwindData |  |
| 50 | `SQLSetConnectOption` | `0xD4B0` | 25 | UnwindData |  |
| 73 | `SQLSetDescField` | `0xD4D0` | 1,880 | UnwindData |  |
| 74 | `SQLSetDescRec` | `0xDC30` | 1,063 | UnwindData |  |
| 68 | `SQLSetPos` | `0xE060` | 216 | UnwindData |  |
| 69 | `SQLSetScrollOptions` | `0xE140` | 40 | UnwindData |  |
| 76 | `SQLSetStmtAttr` | `0xE1D0` | 772 | UnwindData |  |
| 51 | `SQLSetStmtOption` | `0xE4E0` | 894 | UnwindData |  |
| 23 | `SQLTransact` | `0xE870` | 547 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
