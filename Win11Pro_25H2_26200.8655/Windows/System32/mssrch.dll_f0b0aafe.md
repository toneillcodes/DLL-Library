# Binary Specification: mssrch.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\mssrch.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f0b0aafe52a6997655feae112782fe0eaa0814bfe88c55b20326ea635b954504`
* **Total Exported Functions:** 24

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `?GetFilterHostProcessPoolManager@CSearchServiceObj@@SAJPEAPEAUIFilterHostProcessPoolManager@@@Z` | `0x87CB0` | 79 | UnwindData |  |
| 5 | `?GetFileChangeClientManagerInstance@@YA?AV?$shared_ptr@UIFileChangeClientManager@ChangeTracking@Windows@@@std@@XZ` | `0x99070` | 24 | UnwindData |  |
| 19 | `DllCanUnloadNow` | `0xA7290` | 136 | UnwindData |  |
| 21 | `DllGetClassObject` | `0xA7320` | 312 | UnwindData |  |
| 20 | `DllGetActivationFactory` | `0xEF600` | 62 | UnwindData |  |
| 22 | `DllRegisterServer` | `0xEF650` | 91 | UnwindData |  |
| 23 | `DllUnregisterServer` | `0xEF6C0` | 5,664 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `??0CSearchServiceObj@@QEAA@XZ` | `0xF0CE0` | 3,888 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??1CSearchServiceObj@@QEAA@XZ` | `0xF1C10` | 71 | UnwindData |  |
| 4 | `?Cleanup@CSearchServiceObj@@SAXXZ` | `0xF2AB0` | 40 | UnwindData |  |
| 7 | `?GetSessionSingleUserContext@CSearchServiceObj@@UEAA_KK@Z` | `0xF3A30` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `?HandleDplKeyChange@CSearchServiceObj@@UEAAJXZ` | `0xF3AD0` | 67 | UnwindData |  |
| 9 | `?Initialize@CSearchServiceObj@@UEAAJ_NW4INDEXER_SETUP_ACTIONS@@KPEBV?$vector@VReIndexPatternInfo@@V?$allocator@VReIndexPatternInfo@@@std@@@std@@@Z` | `0xF3BE0` | 587 | UnwindData |  |
| 10 | `?LogoffNotification@CSearchServiceObj@@UEAAJAEBUSessionUser@@@Z` | `0xF3F70` | 65 | UnwindData |  |
| 11 | `?LogonNotification@CSearchServiceObj@@UEAAJAEBUSessionUser@@@Z` | `0xF3FC0` | 27 | UnwindData |  |
| 12 | `?PostServiceStartup@CSearchServiceObj@@UEAAJXZ` | `0xF3FF0` | 157 | UnwindData |  |
| 13 | `?PostServiceStartupNonBlocking@CSearchServiceObj@@AEAAXXZ` | `0xF40A0` | 114 | UnwindData |  |
| 14 | `?SetRebuildReason@CSearchServiceObj@@UEAAJW4INDEXER_REBUILD_REASON@@@Z` | `0xF4B40` | 37 | UnwindData |  |
| 15 | `?SetServiceStatusObj@CSearchServiceObj@@UEAAJPEAUIDCOMServiceStatus@@@Z` | `0xF4B70` | 21 | UnwindData |  |
| 16 | `?Shutdown@CSearchServiceObj@@UEAAJXZ` | `0xF4B90` | 59 | UnwindData |  |
| 17 | `?Start@CSearchServiceObj@@UEAAJXZ` | `0xF4D30` | 474 | UnwindData |  |
| 18 | `?Stop@CSearchServiceObj@@UEAAJH@Z` | `0xF4F10` | 236 | UnwindData |  |
| 24 | `MSSrch_SysPrep_Cleanup` | `0xF93B0` | 1,936 | UnwindData |  |
| 3 | `??_7CSearchServiceObj@@6B@` | `0x252EE0` | 0 | Indeterminate |  |
