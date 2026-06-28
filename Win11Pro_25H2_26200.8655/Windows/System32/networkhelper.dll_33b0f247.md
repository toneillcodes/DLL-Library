# Binary Specification: networkhelper.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\networkhelper.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `33b0f24722327f16a9aa3efa1fb86f32f4c5529c08f1e2dc56545553fcc9e2a5`
* **Total Exported Functions:** 14

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CreateControlChannelTriggerConnectionManager` | `0x4480` | 177 | UnwindData |  |
| 2 | `GetSerializedAppMetadata` | `0x5B90` | 653 | UnwindData |  |
| 7 | `IsNetworkConnectionCostRestricted` | `0x5F30` | 121 | UnwindData |  |
| 3 | `CHttpTransport_CreateInstance` | `0xF010` | 3,216 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `CheckPdcRenewal` | `0xFCA0` | 52 | UnwindData |  |
| 11 | `SyncPdcReference_WatchdogReport` | `0xFCE0` | 30 | UnwindData |  |
| 12 | `SyncPdcReference_WatchdogsEnabled` | `0xFD10` | 149 | UnwindData |  |
| 13 | `SyncWerReportComponentName` | `0xFDB0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `SyncWerReportGenerator` | `0xFE30` | 412 | UnwindData |  |
| 5 | `GetOrCreateNullPowerDependencyCoordinatorManager` | `0x11110` | 264 | UnwindData |  |
| 6 | `InitializePowerDependencyCoordinatorManager` | `0x11220` | 361 | UnwindData |  |
| 9 | `ReleasePowerDependencyCoordinatorManager` | `0x11480` | 145 | UnwindData |  |
| 8 | `ProgressStatus` | `0x11620` | 75 | UnwindData |  |
| 10 | `ReportSyncProgress` | `0x11680` | 169 | UnwindData |  |
