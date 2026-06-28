# Binary Specification: scecli.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\scecli.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2d5c7ace43277094504d0c8ca57f5ad8ce5856bb4d9465060334f6ba497bc7ca`
* **Total Exported Functions:** 75

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DeltaNotify` | `0x4890` | 799 | UnwindData |  |
| 37 | `SceGetAreas` | `0x99C0` | 658 | UnwindData |  |
| 46 | `SceIsSystemDatabase` | `0x10010` | 405 | UnwindData |  |
| 33 | `SceFreeMemory` | `0x10900` | 1,406 | UnwindData |  |
| 34 | `SceFreeProfileMemory` | `0x10E90` | 86 | UnwindData |  |
| 14 | `SceAddToNameList` | `0x12320` | 20 | UnwindData |  |
| 15 | `SceAddToNameStatusList` | `0x12340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `SceAddToObjectList` | `0x12350` | 36 | UnwindData |  |
| 22 | `SceCompareNameList` | `0x12380` | 184 | UnwindData |  |
| 23 | `SceCompareSecurityDescriptors` | `0x12440` | 113 | UnwindData |  |
| 26 | `SceCreateDirectory` | `0x124C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `SceEnumerateServices` | `0x124D0` | 750 | UnwindData |  |
| 47 | `SceLookupPrivRightName` | `0x127D0` | 131 | UnwindData |  |
| 1 | `ConvertSecurityDescriptorToText` | `0x12DE0` | 164 | UnwindData |  |
| 66 | `SceSvcGetInformationTemplate` | `0x194B0` | 115 | UnwindData |  |
| 18 | `SceAppendSecurityProfileInfo` | `0x1C9F0` | 32 | UnwindData |  |
| 69 | `SceSvcSetInformationTemplate` | `0x1CA20` | 455 | UnwindData |  |
| 75 | `SceWriteSecurityProfileInfo` | `0x1CBF0` | 26 | UnwindData |  |
| 5 | `SceGenerateGroupPolicy` | `0x1EF50` | 259 | UnwindData |  |
| 8 | `SceProcessSecurityPolicyGPO` | `0x1F060` | 519 | UnwindData |  |
| 9 | `SceProcessSecurityPolicyGPOEx` | `0x1F270` | 782 | UnwindData |  |
| 3 | `InitializeChangeNotify` | `0x20970` | 115 | UnwindData |  |
| 6 | `SceNotifyPolicyDelta` | `0x209F0` | 156 | UnwindData |  |
| 7 | `SceOpenPolicy` | `0x20AA0` | 183 | UnwindData |  |
| 17 | `SceAnalyzeSystem` | `0x25790` | 635 | UnwindData |  |
| 19 | `SceBrowseDatabaseTable` | `0x25A20` | 339 | UnwindData |  |
| 20 | `SceCloseProfile` | `0x25BE0` | 104 | UnwindData |  |
| 21 | `SceCommitTransaction` | `0x25C50` | 77 | UnwindData |  |
| 24 | `SceConfigureSystem` | `0x25CB0` | 482 | UnwindData |  |
| 25 | `SceCopyBaseProfile` | `0x25EA0` | 964 | UnwindData |  |
| 35 | `SceGenerateRollback` | `0x26270` | 434 | UnwindData |  |
| 36 | `SceGetAnalysisAreaSummary` | `0x26430` | 93 | UnwindData |  |
| 38 | `SceGetDatabaseSetting` | `0x264A0` | 259 | UnwindData |  |
| 39 | `SceGetDbTime` | `0x265B0` | 376 | UnwindData |  |
| 40 | `SceGetObjectChildren` | `0x26730` | 248 | UnwindData |  |
| 41 | `SceGetObjectSecurity` | `0x26830` | 196 | UnwindData |  |
| 42 | `SceGetScpProfileDescription` | `0x26900` | 62 | UnwindData |  |
| 43 | `SceGetSecurityProfileInfo` | `0x26950` | 758 | UnwindData |  |
| 44 | `SceGetServerProductType` | `0x26C50` | 239 | UnwindData |  |
| 45 | `SceGetTimeStamp` | `0x26D50` | 919 | UnwindData |  |
| 48 | `SceOpenProfile` | `0x270F0` | 480 | UnwindData |  |
| 49 | `SceRegisterRegValues` | `0x272E0` | 1,199 | UnwindData |  |
| 50 | `SceRollbackTransaction` | `0x277A0` | 77 | UnwindData |  |
| 51 | `SceSetDatabaseSetting` | `0x27800` | 181 | UnwindData |  |
| 62 | `SceStartTransaction` | `0x278C0` | 77 | UnwindData |  |
| 70 | `SceSvcUpdateInfo` | `0x27920` | 99 | UnwindData |  |
| 71 | `SceUpdateObjectInfo` | `0x27990` | 563 | UnwindData |  |
| 72 | `SceUpdateSecurityProfile` | `0x27BD0` | 571 | UnwindData |  |
| 12 | `DllRegisterServer` | `0x28280` | 1,467 | UnwindData |  |
| 13 | `DllUnregisterServer` | `0x28850` | 113 | UnwindData |  |
| 4 | `SceConfigureConvertedFileSecurity` | `0x2CDF0` | 232 | UnwindData |  |
| 10 | `SceSysPrep` | `0x2D2D0` | 379 | UnwindData |  |
| 11 | `SceSysPrepOffline` | `0x2D460` | 47 | UnwindData |  |
| 27 | `SceDcPromoCreateGPOsInSysvol` | `0x31B40` | 31 | UnwindData |  |
| 28 | `SceDcPromoCreateGPOsInSysvolEx` | `0x31B70` | 775 | UnwindData |  |
| 29 | `SceDcPromoteSecurity` | `0x31E80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `SceDcPromoteSecurityEx` | `0x31EA0` | 277 | UnwindData |  |
| 31 | `SceEnforceSecurityPolicyPropagation` | `0x31FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `SceSetupBackupSecurity` | `0x31FD0` | 2,263 | UnwindData |  |
| 53 | `SceSetupConfigureServices` | `0x328B0` | 276 | UnwindData |  |
| 54 | `SceSetupGenerateTemplate` | `0x329D0` | 390 | UnwindData |  |
| 55 | `SceSetupMoveSecurityFile` | `0x32B60` | 269 | UnwindData |  |
| 56 | `SceSetupRootSecurity` | `0x32C80` | 2,025 | UnwindData |  |
| 57 | `SceSetupSystemByInfName` | `0x33470` | 1,903 | UnwindData |  |
| 58 | `SceSetupUnwindSecurityFile` | `0x33BF0` | 209 | UnwindData |  |
| 59 | `SceSetupUpdateSecurityFile` | `0x33CD0` | 152 | UnwindData |  |
| 60 | `SceSetupUpdateSecurityKey` | `0x33D70` | 864 | UnwindData |  |
| 61 | `SceSetupUpdateSecurityService` | `0x340E0` | 153 | UnwindData |  |
| 63 | `SceSvcConvertSDToText` | `0x34490` | 20 | UnwindData |  |
| 64 | `SceSvcConvertTextToSD` | `0x344B0` | 20 | UnwindData |  |
| 65 | `SceSvcFree` | `0x344D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `SceSvcQueryInfo` | `0x344E0` | 518 | UnwindData |  |
| 68 | `SceSvcSetInfo` | `0x346F0` | 478 | UnwindData |  |
| 73 | `SceWrapperExportSecurityProfile` | `0x348E0` | 115 | UnwindData |  |
| 74 | `SceWrapperImportSecurityProfile` | `0x34960` | 222 | UnwindData |  |
