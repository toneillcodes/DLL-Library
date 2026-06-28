# Binary Specification: SyncController.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\SyncController.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6d7ba9ac223e9ebeaa2510451e097ff66e0c374a67f2870e934b752413ba8a12`
* **Total Exported Functions:** 17

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 16 | `DllCanUnloadNow` | `0x9FA0` | 42 | UnwindData |  |
| 17 | `DllGetClassObject` | `0x9FD0` | 17,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `AccountsMgmtAdviseAccount` | `0xE2E0` | 576 | UnwindData |  |
| 2 | `AccountsMgmtConvertWebAccountIdFromAppSpecificId` | `0xE530` | 200 | UnwindData |  |
| 3 | `AccountsMgmtConvertWebAccountIdToAppSpecificId` | `0xE600` | 200 | UnwindData |  |
| 4 | `AccountsMgmtCreateAccount` | `0xE6D0` | 369 | UnwindData |  |
| 5 | `AccountsMgmtDeleteAccount` | `0xE850` | 233 | UnwindData |  |
| 7 | `AccountsMgmtEnumAccounts` | `0xE940` | 245 | UnwindData |  |
| 8 | `AccountsMgmtGetNotifications` | `0xEA40` | 267 | UnwindData |  |
| 10 | `AccountsMgmtQueryAccountProperties` | `0xEB60` | 387 | UnwindData |  |
| 11 | `AccountsMgmtSaveAccountProperties` | `0xECF0` | 368 | UnwindData |  |
| 12 | `AccountsMgmtSyncAccount` | `0xEE70` | 372 | UnwindData |  |
| 13 | `AccountsMgmtSyncAccountAndWaitForCompletion` | `0xEFF0` | 368 | UnwindData |  |
| 14 | `AccountsMgmtUnadviseAccount` | `0xF170` | 460 | UnwindData |  |
| 6 | `AccountsMgmtDiscoverExchangeServerConfig` | `0x11AE0` | 476 | UnwindData |  |
| 15 | `AccountsMgmtVerifyExchangeMailBoxTokenAuth` | `0x11CD0` | 234 | UnwindData |  |
| 9 | `AccountsMgmtMayIgnoreInvalidServerCertificate` | `0x13DB0` | 390 | UnwindData |  |
