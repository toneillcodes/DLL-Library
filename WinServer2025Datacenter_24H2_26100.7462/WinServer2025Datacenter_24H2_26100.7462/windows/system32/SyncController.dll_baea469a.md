# Binary Specification: SyncController.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\SyncController.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `baea469a69b191fd2cd32efa8d4fa3fa2a6b5960bbe620b00c05dcb763d3546c`
* **Total Exported Functions:** 17

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 16 | `DllCanUnloadNow` | `0x9FE0` | 42 | UnwindData |  |
| 17 | `DllGetClassObject` | `0xA010` | 17,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `AccountsMgmtAdviseAccount` | `0xE320` | 576 | UnwindData |  |
| 2 | `AccountsMgmtConvertWebAccountIdFromAppSpecificId` | `0xE570` | 200 | UnwindData |  |
| 3 | `AccountsMgmtConvertWebAccountIdToAppSpecificId` | `0xE640` | 200 | UnwindData |  |
| 4 | `AccountsMgmtCreateAccount` | `0xE710` | 369 | UnwindData |  |
| 5 | `AccountsMgmtDeleteAccount` | `0xE890` | 233 | UnwindData |  |
| 7 | `AccountsMgmtEnumAccounts` | `0xE980` | 245 | UnwindData |  |
| 8 | `AccountsMgmtGetNotifications` | `0xEA80` | 267 | UnwindData |  |
| 10 | `AccountsMgmtQueryAccountProperties` | `0xEBA0` | 387 | UnwindData |  |
| 11 | `AccountsMgmtSaveAccountProperties` | `0xED30` | 368 | UnwindData |  |
| 12 | `AccountsMgmtSyncAccount` | `0xEEB0` | 372 | UnwindData |  |
| 13 | `AccountsMgmtSyncAccountAndWaitForCompletion` | `0xF030` | 368 | UnwindData |  |
| 14 | `AccountsMgmtUnadviseAccount` | `0xF1B0` | 460 | UnwindData |  |
| 6 | `AccountsMgmtDiscoverExchangeServerConfig` | `0x11B20` | 476 | UnwindData |  |
| 15 | `AccountsMgmtVerifyExchangeMailBoxTokenAuth` | `0x11D10` | 234 | UnwindData |  |
| 9 | `AccountsMgmtMayIgnoreInvalidServerCertificate` | `0x13DF0` | 390 | UnwindData |  |
