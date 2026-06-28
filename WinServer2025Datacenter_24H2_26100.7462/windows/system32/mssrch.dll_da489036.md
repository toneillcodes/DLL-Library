# Binary Specification: mssrch.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\mssrch.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `da489036fb74496b6ad28120849871f26d6df7aec32cd4b7aba6b2e93e70a0a1`
* **Total Exported Functions:** 24

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `?GetFilterHostProcessPoolManager@CSearchServiceObj@@SAJPEAPEAUIFilterHostProcessPoolManager@@@Z` | `0x8ABD0` | 79 | UnwindData |  |
| 5 | `?GetFileChangeClientManagerInstance@@YA?AV?$shared_ptr@UIFileChangeClientManager@ChangeTracking@Windows@@@std@@XZ` | `0x9B490` | 24 | UnwindData |  |
| 19 | `DllCanUnloadNow` | `0xA9A60` | 136 | UnwindData |  |
| 21 | `DllGetClassObject` | `0xA9AF0` | 312 | UnwindData |  |
| 20 | `DllGetActivationFactory` | `0xEB210` | 62 | UnwindData |  |
| 22 | `DllRegisterServer` | `0xEB260` | 91 | UnwindData |  |
| 23 | `DllUnregisterServer` | `0xEB2D0` | 5,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `??0CSearchServiceObj@@QEAA@XZ` | `0xEC7B0` | 3,888 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??1CSearchServiceObj@@QEAA@XZ` | `0xED6E0` | 76 | UnwindData |  |
| 4 | `?Cleanup@CSearchServiceObj@@SAXXZ` | `0xEE580` | 40 | UnwindData |  |
| 7 | `?GetSessionSingleUserContext@CSearchServiceObj@@UEAA_KK@Z` | `0xEFFE0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `?HandleDplKeyChange@CSearchServiceObj@@UEAAJXZ` | `0xF0080` | 67 | UnwindData |  |
| 9 | `?Initialize@CSearchServiceObj@@UEAAJ_NW4INDEXER_SETUP_ACTIONS@@KPEBV?$vector@VReIndexPatternInfo@@V?$allocator@VReIndexPatternInfo@@@std@@@std@@@Z` | `0xF0190` | 340 | UnwindData |  |
| 10 | `?LogoffNotification@CSearchServiceObj@@UEAAJAEBUSessionUser@@@Z` | `0xF0430` | 65 | UnwindData |  |
| 11 | `?LogonNotification@CSearchServiceObj@@UEAAJAEBUSessionUser@@@Z` | `0xF0480` | 27 | UnwindData |  |
| 12 | `?PostServiceStartup@CSearchServiceObj@@UEAAJXZ` | `0xF04B0` | 198 | UnwindData |  |
| 13 | `?PostServiceStartupNonBlocking@CSearchServiceObj@@AEAAXXZ` | `0xF0580` | 114 | UnwindData |  |
| 14 | `?SetRebuildReason@CSearchServiceObj@@UEAAJW4INDEXER_REBUILD_REASON@@@Z` | `0xF12B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `?SetServiceStatusObj@CSearchServiceObj@@UEAAJPEAUIDCOMServiceStatus@@@Z` | `0xF12C0` | 75 | UnwindData |  |
| 16 | `?Shutdown@CSearchServiceObj@@UEAAJXZ` | `0xF1320` | 59 | UnwindData |  |
| 17 | `?Start@CSearchServiceObj@@UEAAJXZ` | `0xF14C0` | 547 | UnwindData |  |
| 18 | `?Stop@CSearchServiceObj@@UEAAJH@Z` | `0xF16F0` | 252 | UnwindData |  |
| 24 | `MSSrch_SysPrep_Cleanup` | `0xF5BD0` | 1,936 | UnwindData |  |
| 3 | `??_7CSearchServiceObj@@6B@` | `0x234EE0` | 0 | Indeterminate |  |
