# Binary Specification: fhsvcctl.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\fhsvcctl.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `477c684883d79885a2b3c2c959e6f7a509d82229be66d3e61a30636f0bfbf137`
* **Total Exported Functions:** 14

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllMain` | `0x2110` | 373 | UnwindData |  |
| 2 | `FhQueryConfiguredUsersCount` | `0x2360` | 614 | UnwindData |  |
| 3 | `FhServiceBlockBackup` | `0x2B40` | 374 | UnwindData |  |
| 4 | `FhServiceClearProtectionState` | `0x2CC0` | 231 | UnwindData |  |
| 5 | `FhServiceClosePipe` | `0x2DB0` | 367 | UnwindData |  |
| 6 | `FhServiceEnterMaintenanceMode` | `0x2F30` | 482 | UnwindData |  |
| 7 | `FhServiceExitMaintenanceMode` | `0x3120` | 222 | UnwindData |  |
| 8 | `FhServiceMigrationFinished` | `0x3210` | 222 | UnwindData |  |
| 9 | `FhServiceMigrationStarting` | `0x3300` | 222 | UnwindData |  |
| 10 | `FhServiceOpenPipe` | `0x33F0` | 1,018 | UnwindData |  |
| 11 | `FhServiceReloadConfiguration` | `0x37F0` | 238 | UnwindData |  |
| 12 | `FhServiceStartBackup` | `0x38F0` | 234 | UnwindData |  |
| 13 | `FhServiceStopBackup` | `0x39E0` | 226 | UnwindData |  |
| 14 | `FhServiceUnblockBackup` | `0x3AD0` | 227 | UnwindData |  |
