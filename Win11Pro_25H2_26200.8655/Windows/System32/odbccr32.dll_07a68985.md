# Binary Specification: odbccr32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\odbccr32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `07a689851cf275d03039fac0de253dce9e0a9638aae1df3d7f0ce5905776828d`
* **Total Exported Functions:** 37

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 34 | `SQLGetDescRec` | `0x9D90` | 708 | UnwindData |  |
| 6 | `ReleaseCLStmtResources` | `0xA610` | 248 | UnwindData |  |
| 4 | `SQLBindCol` | `0xAB90` | 735 | UnwindData |  |
| 72 | `SQLBindParameter` | `0xAE80` | 382 | UnwindData |  |
| 78 | `SQLBulkOperations` | `0xB010` | 50 | UnwindData |  |
| 5 | `SQLCancel` | `0xB050` | 489 | UnwindData |  |
| 26 | `SQLCloseCursor` | `0xB240` | 377 | UnwindData |  |
| 29 | `SQLEndTran` | `0xB3C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `SQLExecDirect` | `0xB3D0` | 285 | UnwindData |  |
| 12 | `SQLExecute` | `0xB500` | 46 | UnwindData |  |
| 59 | `SQLExtendedFetch` | `0xB540` | 222 | UnwindData |  |
| 13 | `SQLFetch` | `0xB630` | 296 | UnwindData |  |
| 30 | `SQLFetchScroll` | `0xB760` | 314 | UnwindData |  |
| 31 | `SQLFreeHandle` | `0xB8A0` | 76 | UnwindData |  |
| 16 | `SQLFreeStmt` | `0xB9D0` | 181 | UnwindData |  |
| 43 | `SQLGetData` | `0xBA90` | 321 | UnwindData |  |
| 33 | `SQLGetDescField` | `0xBBE0` | 124 | UnwindData |  |
| 45 | `SQLGetInfo` | `0xC0E0` | 323 | UnwindData |  |
| 38 | `SQLGetStmtAttr` | `0xC3C0` | 222 | UnwindData |  |
| 46 | `SQLGetStmtOption` | `0xC4B0` | 948 | UnwindData |  |
| 61 | `SQLMoreResults` | `0xC870` | 312 | UnwindData |  |
| 62 | `SQLNativeSql` | `0xC9B0` | 460 | UnwindData |  |
| 63 | `SQLNumParams` | `0xCB90` | 150 | UnwindData |  |
| 48 | `SQLParamData` | `0xCC30` | 46 | UnwindData |  |
| 64 | `SQLParamOptions` | `0xCC70` | 288 | UnwindData |  |
| 19 | `SQLPrepare` | `0xCDA0` | 288 | UnwindData |  |
| 49 | `SQLPutData` | `0xCED0` | 49 | UnwindData |  |
| 20 | `SQLRowCount` | `0xCF10` | 150 | UnwindData |  |
| 39 | `SQLSetConnectAttr` | `0xCFB0` | 22 | UnwindData |  |
| 50 | `SQLSetConnectOption` | `0xCFD0` | 25 | UnwindData |  |
| 73 | `SQLSetDescField` | `0xCFF0` | 1,868 | UnwindData |  |
| 74 | `SQLSetDescRec` | `0xD750` | 1,063 | UnwindData |  |
| 68 | `SQLSetPos` | `0xDB80` | 216 | UnwindData |  |
| 69 | `SQLSetScrollOptions` | `0xDC60` | 40 | UnwindData |  |
| 76 | `SQLSetStmtAttr` | `0xDCF0` | 772 | UnwindData |  |
| 51 | `SQLSetStmtOption` | `0xE000` | 894 | UnwindData |  |
| 23 | `SQLTransact` | `0xE390` | 1,363 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
