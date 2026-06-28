# Binary Specification: msdtcprx.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\msdtcprx.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `cfafc650681eaeb7027c6756b9a2e6a116b2059a2b6a27aead0115bb4f5e8688`
* **Total Exported Functions:** 37

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 27 | `ContactToNameObject` | `0x6A50` | 1,085 | UnwindData |  |
| 26 | `DllGetDTCUtilObject` | `0xA1E0` | 224 | UnwindData |  |
| 22 | `CreateRemoteProxyTmInstance` | `0xC760` | 298 | UnwindData |  |
| 21 | `CreateLocalTmInstance` | `0xC890` | 135 | UnwindData |  |
| 34 | `DllRegisterServer` | `0x18B90` | 8,656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `DllUnregisterServer` | `0x18B90` | 8,656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `DllGetClassObject` | `0x1AD60` | 395 | UnwindData |  |
| 4 | `DllGetDTCProxy` | `0x1AF00` | 129 | UnwindData |  |
| 8 | `GetDtcLogPath` | `0x1C1A0` | 329 | UnwindData |  |
| 33 | `DllGetTransactionManagerCore` | `0x1F990` | 335 | UnwindData |  |
| 36 | `GetTmInstance` | `0x1FAF0` | 68 | UnwindData |  |
| 6 | `CreateInstance` | `0x20820` | 132 | UnwindData |  |
| 19 | `DTC_XaClose` | `0x2ADD0` | 370 | UnwindData |  |
| 14 | `DTC_XaCommit` | `0x2AF50` | 551 | UnwindData |  |
| 18 | `DTC_XaComplete` | `0x2B180` | 138 | UnwindData |  |
| 12 | `DTC_XaEnd` | `0x2B210` | 571 | UnwindData |  |
| 17 | `DTC_XaForget` | `0x2B460` | 138 | UnwindData |  |
| 10 | `DTC_XaOpen` | `0x2B4F0` | 1,086 | UnwindData |  |
| 13 | `DTC_XaPrepare` | `0x2B940` | 572 | UnwindData |  |
| 16 | `DTC_XaRecover` | `0x2BB90` | 625 | UnwindData |  |
| 15 | `DTC_XaRollback` | `0x2BE10` | 512 | UnwindData |  |
| 11 | `DTC_XaStart` | `0x2C020` | 983 | UnwindData |  |
| 9 | `UpgradeApplySuccess` | `0x46360` | 742 | UnwindData |  |
| 7 | `DllGetDtcConfigManager` | `0x472B0` | 37,008 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `Create` | `0x50340` | 167 | UnwindData |  |
| 28 | `SysPrepDtcCleanup` | `0x53E60` | 405 | UnwindData |  |
| 29 | `SysPrepDtcGeneralize` | `0x54000` | 405 | UnwindData |  |
| 30 | `SysPrepDtcSpecialize` | `0x541A0` | 280 | UnwindData |  |
| 31 | `DeployDtc` | `0x54360` | 676 | UnwindData |  |
| 37 | `InstallContacts` | `0x54610` | 666 | UnwindData |  |
| 38 | `InstallDtc` | `0x548B0` | 2,342 | UnwindData |  |
| 39 | `InstallDtcClient` | `0x551E0` | 45 | UnwindData |  |
| 40 | `RemoveDtc` | `0x55220` | 643 | UnwindData |  |
| 20 | `CreateLegacyTmInstance` | `0x56740` | 193 | UnwindData |  |
| 23 | `CreateTmInstanceForRemoteAdmin` | `0x56810` | 115 | UnwindData |  |
| 25 | `DllGetDTCConnectionManager` | `0x56FF0` | 411 | UnwindData |  |
| 24 | `ShutDownCM` | `0x58CD0` | 183,180 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
