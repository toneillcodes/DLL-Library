# Binary Specification: joinutil.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\joinutil.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `99d442e0f61b2ec123130f1ccb58d5e4ffa20ccdb64bc96e087c8f471bb43841`
* **Total Exported Functions:** 30

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `NetpAvoidNetlogonSpnSet` | `0x1ED0` | 199 | UnwindData |  |
| 2 | `NetpClearFullJoinState` | `0x1FA0` | 72 | UnwindData |  |
| 3 | `NetpCompatibilityMode` | `0x1FF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `NetpControlServices` | `0x2000` | 625 | UnwindData |  |
| 5 | `NetpDNSNameResolutionRequired` | `0x2280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `NetpDoDomainJoinLicensingCheck` | `0x2290` | 148 | UnwindData |  |
| 7 | `NetpFreeJoinStateContents` | `0x17320` | 539 | UnwindData |  |
| 8 | `NetpGenerateDefaultPassword` | `0x17550` | 229 | UnwindData |  |
| 9 | `NetpGetLsaHandle` | `0x17640` | 211 | UnwindData |  |
| 10 | `NetpGetLsaMachineAccountInfo` | `0x17720` | 153 | UnwindData |  |
| 11 | `NetpGetLsaPrimaryDomain` | `0x177C0` | 555 | UnwindData |  |
| 12 | `NetpHandleJoinedStateInfo` | `0x17A00` | 430 | UnwindData |  |
| 13 | `NetpLoadFullJoinState` | `0x17BC0` | 2,979 | UnwindData |  |
| 14 | `NetpLoadParameters` | `0x18770` | 609 | UnwindData |  |
| 15 | `NetpLsaOpenSecret` | `0x18AC0` | 43 | UnwindData |  |
| 16 | `NetpManageLocalGroups` | `0x18B00` | 1,039 | UnwindData |  |
| 17 | `NetpManageMachineSecret` | `0x18F20` | 808 | UnwindData |  |
| 18 | `NetpManageMachineSecret2` | `0x19250` | 552 | UnwindData |  |
| 19 | `NetpMarkLastFullJoinAttempt` | `0x19480` | 468 | UnwindData |  |
| 20 | `NetpQueryService` | `0x19660` | 512 | UnwindData |  |
| 21 | `NetpRemoveInitialDcRecord` | `0x19870` | 193 | UnwindData |  |
| 22 | `NetpSaveFullJoinStateInternal` | `0x19940` | 1,656 | UnwindData |  |
| 23 | `NetpSetLsaHandle` | `0x19FC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `NetpSetLsaMachineAccountInfo` | `0x19FF0` | 153 | UnwindData |  |
| 25 | `NetpSetLsaPrimaryDomain` | `0x1A090` | 263 | UnwindData |  |
| 26 | `NetpSetWinlogonCAD` | `0x1A1A0` | 199 | UnwindData |  |
| 27 | `NetpStopService` | `0x1A270` | 676 | UnwindData |  |
| 28 | `NetpStoreInitialDcRecord` | `0x1A520` | 115 | UnwindData |  |
| 29 | `NetpStoreInitialDcRecordEx` | `0x1A5A0` | 1,040 | UnwindData |  |
| 30 | `NetpUpdateW32timeConfig` | `0x1A9C0` | 195 | UnwindData |  |
