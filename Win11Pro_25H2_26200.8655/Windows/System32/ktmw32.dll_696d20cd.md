# Binary Specification: ktmw32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ktmw32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `696d20cd0da6490091fe6b42d5a44a69aecee5dbe5f8f834b0505d4b13a0ca9c`
* **Total Exported Functions:** 44

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CommitComplete` | `0x1290` | 63 | UnwindData |  |
| 2 | `CommitEnlistment` | `0x12E0` | 63 | UnwindData |  |
| 3 | `CommitTransaction` | `0x1330` | 65 | UnwindData |  |
| 4 | `CommitTransactionAsync` | `0x1380` | 65 | UnwindData |  |
| 5 | `CreateEnlistment` | `0x13D0` | 220 | UnwindData |  |
| 6 | `CreateResourceManager` | `0x14C0` | 287 | UnwindData |  |
| 7 | `CreateTransaction` | `0x15F0` | 47 | UnwindData |  |
| 8 | `CreateTransactionManager` | `0x1630` | 387 | UnwindData |  |
| 9 | `GetCurrentClockTransactionManager` | `0x17C0` | 136 | UnwindData |  |
| 10 | `GetEnlistmentId` | `0x1850` | 152 | UnwindData |  |
| 11 | `GetEnlistmentRecoveryInformation` | `0x18F0` | 76 | UnwindData |  |
| 12 | `GetNotificationResourceManager` | `0x1950` | 139 | UnwindData |  |
| 13 | `GetNotificationResourceManagerAsync` | `0x19F0` | 126 | UnwindData |  |
| 14 | `GetTransactionId` | `0x1A80` | 146 | UnwindData |  |
| 15 | `GetTransactionInformation` | `0x1B20` | 457 | UnwindData |  |
| 16 | `GetTransactionManagerId` | `0x1CF0` | 137 | UnwindData |  |
| 17 | `OpenEnlistment` | `0x1D80` | 154 | UnwindData |  |
| 18 | `OpenResourceManager` | `0x1E20` | 154 | UnwindData |  |
| 19 | `OpenTransaction` | `0x1EC0` | 151 | UnwindData |  |
| 20 | `OpenTransactionManager` | `0x1F60` | 282 | UnwindData |  |
| 21 | `OpenTransactionManagerById` | `0x2080` | 154 | UnwindData |  |
| 22 | `PrePrepareComplete` | `0x2120` | 63 | UnwindData |  |
| 23 | `PrePrepareEnlistment` | `0x2170` | 63 | UnwindData |  |
| 24 | `PrepareComplete` | `0x21C0` | 63 | UnwindData |  |
| 25 | `PrepareEnlistment` | `0x2210` | 63 | UnwindData |  |
| 26 | `PrivCreateTransaction` | `0x2260` | 347 | UnwindData |  |
| 27 | `PrivIsLogWritableTransactionManager` | `0x23D0` | 73 | UnwindData |  |
| 28 | `PrivPropagationComplete` | `0x2420` | 63 | UnwindData |  |
| 29 | `PrivPropagationFailed` | `0x2470` | 66 | UnwindData |  |
| 30 | `PrivRegisterProtocolAddressInformation` | `0x24C0` | 71 | UnwindData |  |
| 31 | `ReadOnlyEnlistment` | `0x2510` | 63 | UnwindData |  |
| 32 | `RecoverEnlistment` | `0x2560` | 63 | UnwindData |  |
| 33 | `RecoverResourceManager` | `0x25B0` | 63 | UnwindData |  |
| 34 | `RecoverTransactionManager` | `0x2600` | 63 | UnwindData |  |
| 35 | `RenameTransactionManager` | `0x2650` | 209 | UnwindData |  |
| 36 | `RollbackComplete` | `0x2730` | 63 | UnwindData |  |
| 37 | `RollbackEnlistment` | `0x2780` | 63 | UnwindData |  |
| 38 | `RollbackTransaction` | `0x27D0` | 65 | UnwindData |  |
| 39 | `RollbackTransactionAsync` | `0x2820` | 65 | UnwindData |  |
| 40 | `RollforwardTransactionManager` | `0x2870` | 63 | UnwindData |  |
| 41 | `SetEnlistmentRecoveryInformation` | `0x28C0` | 71 | UnwindData |  |
| 42 | `SetResourceManagerCompletionPort` | `0x2910` | 88 | UnwindData |  |
| 43 | `SetTransactionInformation` | `0x2970` | 435 | UnwindData |  |
| 44 | `SinglePhaseReject` | `0x2B30` | 63 | UnwindData |  |
