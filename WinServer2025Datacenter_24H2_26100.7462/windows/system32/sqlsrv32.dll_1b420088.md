# Binary Specification: sqlsrv32.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\sqlsrv32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1b420088a1b540ef4cd2eeb43a9246c05915cc56804cd535663a2051dcddfa24`
* **Total Exported Functions:** 90

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `SQLCancel` | `0x4E50` | 296 | UnwindData |  |
| 16 | `SQLFreeStmt` | `0x50A0` | 64 | UnwindData |  |
| 72 | `SQLBindParameter` | `0x53F0` | 1,040 | UnwindData |  |
| 12 | `SQLExecute` | `0xC9F0` | 2,208 | UnwindData |  |
| 13 | `SQLFetch` | `0x17900` | 489 | UnwindData |  |
| 111 | `SQLGetDiagRecW` | `0x23E40` | 192 | UnwindData |  |
| 114 | `SQLGetStmtAttrW` | `0x24460` | 1,416 | UnwindData |  |
| 110 | `SQLGetDiagFieldW` | `0x249F0` | 330 | UnwindData |  |
| 11 | `SQLExecDirectW` | `0x28D70` | 8,555 | UnwindData |  |
| 43 | `SQLGetData` | `0x2AEF0` | 4,517 | UnwindData |  |
| 204 | `BCP_batch` | `0x31500` | 800 | UnwindData |  |
| 205 | `BCP_bind` | `0x31830` | 1,902 | UnwindData |  |
| 206 | `BCP_colfmt` | `0x31FB0` | 858 | UnwindData |  |
| 208 | `BCP_collen` | `0x32310` | 598 | UnwindData |  |
| 209 | `BCP_colptr` | `0x32570` | 444 | UnwindData |  |
| 210 | `BCP_columns` | `0x32740` | 808 | UnwindData |  |
| 211 | `BCP_control` | `0x32A70` | 1,626 | UnwindData |  |
| 212 | `BCP_done` | `0x330D0` | 845 | UnwindData |  |
| 214 | `BCP_exec` | `0x33430` | 1,886 | UnwindData |  |
| 226 | `BCP_getcolfmt` | `0x33BA0` | 804 | UnwindData |  |
| 213 | `BCP_init` | `0x33ED0` | 2,103 | UnwindData |  |
| 215 | `BCP_moretext` | `0x34710` | 1,483 | UnwindData |  |
| 217 | `BCP_readfmt` | `0x34CF0` | 3,485 | UnwindData |  |
| 216 | `BCP_sendrow` | `0x35AA0` | 1,573 | UnwindData |  |
| 227 | `BCP_setcolfmt` | `0x360D0` | 2,971 | UnwindData |  |
| 218 | `BCP_writefmt` | `0x36C80` | 2,037 | UnwindData |  |
| 103 | `SQLCloseCursor` | `0x44FB0` | 211 | UnwindData |  |
| 62 | `SQLNativeSqlW` | `0x45090` | 384 | UnwindData |  |
| 48 | `SQLParamData` | `0x45220` | 7,663 | UnwindData |  |
| 19 | `SQLPrepareW` | `0x47020` | 1,247 | UnwindData |  |
| 49 | `SQLPutData` | `0x47510` | 4,751 | UnwindData |  |
| 101 | `SQLAllocHandle` | `0x53D60` | 111 | UnwindData |  |
| 55 | `SQLBrowseConnectW` | `0x53DE0` | 2,710 | UnwindData |  |
| 7 | `SQLConnectW` | `0x54880` | 783 | UnwindData |  |
| 9 | `SQLDisconnect` | `0x54BA0` | 1,034 | UnwindData |  |
| 41 | `SQLDriverConnectW` | `0x54FB0` | 1,642 | UnwindData |  |
| 106 | `SQLFreeHandle` | `0x55820` | 108 | UnwindData |  |
| 24 | `SQLBulkOperations` | `0x57C00` | 1,839 | UnwindData |  |
| 59 | `SQLExtendedFetch` | `0x58340` | 160 | UnwindData |  |
| 121 | `SQLFetchScroll` | `0x583F0` | 297 | UnwindData |  |
| 17 | `SQLGetCursorNameW` | `0x58520` | 449 | UnwindData |  |
| 21 | `SQLSetCursorNameW` | `0x586F0` | 708 | UnwindData |  |
| 68 | `SQLSetPos` | `0x589C0` | 2,561 | UnwindData |  |
| 69 | `SQLSetScrollOptions` | `0x593D0` | 284 | UnwindData |  |
| 203 | `SQLDebug` | `0x5BB60` | 515 | UnwindData |  |
| 56 | `SQLColumnPrivilegesW` | `0x5CE20` | 374 | UnwindData |  |
| 40 | `SQLColumnsW` | `0x5CFA0` | 391 | UnwindData |  |
| 60 | `SQLForeignKeysW` | `0x5D130` | 564 | UnwindData |  |
| 47 | `SQLGetTypeInfoW` | `0x5D370` | 2,327 | UnwindData |  |
| 65 | `SQLPrimaryKeysW` | `0x5DC90` | 332 | UnwindData |  |
| 66 | `SQLProcedureColumnsW` | `0x5DDF0` | 301 | UnwindData |  |
| 67 | `SQLProceduresW` | `0x5DF30` | 272 | UnwindData |  |
| 52 | `SQLSpecialColumnsW` | `0x5E050` | 442 | UnwindData |  |
| 53 | `SQLStatisticsW` | `0x5E210` | 443 | UnwindData |  |
| 70 | `SQLTablePrivilegesW` | `0x5E3E0` | 337 | UnwindData |  |
| 54 | `SQLTablesW` | `0x5E540` | 838 | UnwindData |  |
| 4 | `SQLBindCol` | `0x61AB0` | 415 | UnwindData |  |
| 6 | `SQLColAttributeW` | `0x61C60` | 661 | UnwindData |  |
| 104 | `SQLCopyDesc` | `0x61F00` | 2,079 | UnwindData |  |
| 8 | `SQLDescribeColW` | `0x62730` | 411 | UnwindData |  |
| 58 | `SQLDescribeParam` | `0x628E0` | 761 | UnwindData |  |
| 108 | `SQLGetDescFieldW` | `0x62BE0` | 2,080 | UnwindData |  |
| 109 | `SQLGetDescRecW` | `0x63410` | 646 | UnwindData |  |
| 63 | `SQLNumParams` | `0x636A0` | 96 | UnwindData |  |
| 18 | `SQLNumResultCols` | `0x63710` | 191 | UnwindData |  |
| 64 | `SQLParamOptions` | `0x637E0` | 102 | UnwindData |  |
| 20 | `SQLRowCount` | `0x63850` | 186 | UnwindData |  |
| 117 | `SQLSetDescFieldW` | `0x63910` | 2,461 | UnwindData |  |
| 118 | `SQLSetDescRec` | `0x642C0` | 430 | UnwindData |  |
| 219 | `ConnectDlgProc` | `0x64CF0` | 3,005 | UnwindData |  |
| 224 | `FinishDlgProc` | `0x66C00` | 1,155 | UnwindData |  |
| 225 | `TestDlgProc` | `0x68A20` | 2,637 | UnwindData |  |
| 220 | `WizDSNDlgProc` | `0x69480` | 3,398 | UnwindData |  |
| 222 | `WizDatabaseDlgProc` | `0x6A1D0` | 2,064 | UnwindData |  |
| 221 | `WizIntSecurityDlgProc` | `0x6A9F0` | 3,032 | UnwindData |  |
| 223 | `WizLanguageDlgProc` | `0x6B5D0` | 3,762 | UnwindData |  |
| 44 | `SQLGetFunctions` | `0x6F000` | 130 | UnwindData |  |
| 45 | `SQLGetInfoW` | `0x6F090` | 3,319 | UnwindData |  |
| 107 | `SQLGetConnectAttrW` | `0x71290` | 1,452 | UnwindData |  |
| 42 | `SQLGetConnectOptionW` | `0x71850` | 215 | UnwindData |  |
| 112 | `SQLGetEnvAttr` | `0x71930` | 162 | UnwindData |  |
| 116 | `SQLSetConnectAttrW` | `0x719E0` | 7,212 | UnwindData |  |
| 50 | `SQLSetConnectOptionW` | `0x73620` | 261 | UnwindData |  |
| 119 | `SQLSetEnvAttr` | `0x73730` | 160 | UnwindData |  |
| 120 | `SQLSetStmtAttrW` | `0x737E0` | 1,499 | UnwindData |  |
| 61 | `SQLMoreResults` | `0x74E60` | 1,353 | UnwindData |  |
| 105 | `SQLEndTran` | `0x78400` | 154 | UnwindData |  |
| 200 | `LibMain` | `0x79160` | 305 | UnwindData |  |
| 201 | `ConfigDSNW` | `0x7A600` | 1,332 | UnwindData |  |
| 202 | `ConfigDriverW` | `0x7AB40` | 1,654 | UnwindData |  |
