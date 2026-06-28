# Binary Specification: msdtcprx.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\msdtcprx.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `948729db87a484249663d9090dc020bd4cfaedd33e57cd0ea4f056cd70066a49`
* **Total Exported Functions:** 37

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 27 | `ContactToNameObject` | `0x6A90` | 1,117 | UnwindData |  |
| 26 | `DllGetDTCUtilObject` | `0xA380` | 224 | UnwindData |  |
| 22 | `CreateRemoteProxyTmInstance` | `0xC850` | 298 | UnwindData |  |
| 21 | `CreateLocalTmInstance` | `0xC980` | 135 | UnwindData |  |
| 34 | `DllRegisterServer` | `0x124C0` | 8,672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `DllUnregisterServer` | `0x124C0` | 8,672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `DllGetClassObject` | `0x146A0` | 395 | UnwindData |  |
| 4 | `DllGetDTCProxy` | `0x14840` | 129 | UnwindData |  |
| 8 | `GetDtcLogPath` | `0x15AE0` | 329 | UnwindData |  |
| 33 | `DllGetTransactionManagerCore` | `0x18C00` | 335 | UnwindData |  |
| 36 | `GetTmInstance` | `0x18D60` | 68 | UnwindData |  |
| 6 | `CreateInstance` | `0x196A0` | 132 | UnwindData |  |
| 19 | `DTC_XaClose` | `0x23C50` | 370 | UnwindData |  |
| 14 | `DTC_XaCommit` | `0x23DD0` | 551 | UnwindData |  |
| 18 | `DTC_XaComplete` | `0x24000` | 138 | UnwindData |  |
| 12 | `DTC_XaEnd` | `0x24090` | 571 | UnwindData |  |
| 17 | `DTC_XaForget` | `0x242E0` | 138 | UnwindData |  |
| 10 | `DTC_XaOpen` | `0x24370` | 1,086 | UnwindData |  |
| 13 | `DTC_XaPrepare` | `0x247C0` | 572 | UnwindData |  |
| 16 | `DTC_XaRecover` | `0x24A10` | 625 | UnwindData |  |
| 15 | `DTC_XaRollback` | `0x24C90` | 512 | UnwindData |  |
| 11 | `DTC_XaStart` | `0x24EA0` | 983 | UnwindData |  |
| 9 | `UpgradeApplySuccess` | `0x3F1D0` | 742 | UnwindData |  |
| 7 | `DllGetDtcConfigManager` | `0x40120` | 35,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `Create` | `0x48C90` | 167 | UnwindData |  |
| 28 | `SysPrepDtcCleanup` | `0x4C7B0` | 405 | UnwindData |  |
| 29 | `SysPrepDtcGeneralize` | `0x4C950` | 405 | UnwindData |  |
| 30 | `SysPrepDtcSpecialize` | `0x4CAF0` | 280 | UnwindData |  |
| 31 | `DeployDtc` | `0x4CCB0` | 676 | UnwindData |  |
| 37 | `InstallContacts` | `0x4CF60` | 666 | UnwindData |  |
| 38 | `InstallDtc` | `0x4D200` | 2,342 | UnwindData |  |
| 39 | `InstallDtcClient` | `0x4DB30` | 45 | UnwindData |  |
| 40 | `RemoveDtc` | `0x4DB70` | 643 | UnwindData |  |
| 20 | `CreateLegacyTmInstance` | `0x4EF90` | 193 | UnwindData |  |
| 23 | `CreateTmInstanceForRemoteAdmin` | `0x4F060` | 115 | UnwindData |  |
| 25 | `DllGetDTCConnectionManager` | `0x4F840` | 411 | UnwindData |  |
| 24 | `ShutDownCM` | `0x51520` | 214,604 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
