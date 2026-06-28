# Binary Specification: SecurityHealthUdk.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\SecurityHealthUdk.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d345c2ac7a0ffecdff45aead982879fe09c9dd8eb0f3c0949eeda0144a98f795`
* **Total Exported Functions:** 93

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 92 | `DllMain` | `0x4B20` | 295 | UnwindData |  |
| 19 | `Shield_EnumerateImageNames` | `0x6B20` | 697 | UnwindData |  |
| 25 | `Shield_ExportMitigationPoliciesToXmlFile` | `0x6DE0` | 430 | UnwindData |  |
| 34 | `Shield_GetImageMitigationPolicy` | `0x6FA0` | 989 | UnwindData |  |
| 35 | `Shield_GetImageMitigationPolicyEx` | `0x7390` | 162 | UnwindData |  |
| 39 | `Shield_GetOsDefaultMitigationPolicy` | `0x7440` | 397 | UnwindData |  |
| 40 | `Shield_GetOsDefaultMitigationPolicyEx` | `0x75E0` | 704 | UnwindData |  |
| 53 | `Shield_ImportMitigationPoliciesFromXmlFile` | `0x78B0` | 722 | UnwindData |  |
| 74 | `Shield_RemoveImageNameAndItsMitigationPolicies` | `0x7B90` | 309 | UnwindData |  |
| 76 | `Shield_SetImageMitigationPolicyEx` | `0x7CD0` | 300 | UnwindData |  |
| 26 | `Shield_FWClosePolicyStore` | `0x7F20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `Shield_FWGetConfig` | `0x7F40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `Shield_FWOpenPolicyStore` | `0x7F60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `Shield_FwActivate` | `0x7F80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `Shield_FwAnalyzeFirewallPolicy` | `0x7FA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `Shield_FwIsGroupPolicyEnforced` | `0x7FC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `Shield_IcfChangeNotificationCreate` | `0x7FE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `Shield_IcfChangeNotificationDestroy` | `0x8000` | 73,376 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `Shield_ApplicationGuardRefreshState` | `0x19EA0` | 17 | UnwindData |  |
| 8 | `Shield_CpmcGetContainerIdForUser` | `0x19EC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `Shield_GetApplicationGuardPolicy` | `0x19EE0` | 244 | UnwindData |  |
| 43 | `Shield_GetStoragePolicySettings` | `0x19FE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `Shield_IsQueryWin32SubsystemHostPresent` | `0x1A000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `Shield_LUAIsShadowAdminEnabled` | `0x1A010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `Shield_LsaLookupUserAccountType` | `0x1A020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `Shield_MpGetWindowsLockdownMode` | `0x1A040` | 86 | UnwindData |  |
| 62 | `Shield_MpIsAccountPasswordLess` | `0x1A0A0` | 79 | UnwindData |  |
| 63 | `Shield_MpIsBrowserReplacementFeaturePresent` | `0x1A100` | 28 | UnwindData |  |
| 64 | `Shield_MpIsWcosProductionConfiguration` | `0x1A130` | 118 | UnwindData |  |
| 65 | `Shield_MpIsWindowsLockdownMode` | `0x1A1B0` | 126 | UnwindData |  |
| 66 | `Shield_MpRegisterWaitForSingleObjectEx` | `0x1A240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `Shield_QueryWin32SubsystemHost` | `0x1A260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `Shield_SetApplicationGuardPolicy` | `0x1A280` | 87 | UnwindData |  |
| 91 | `Shield_WldpQueryPolicySettingEnabled2` | `0x1A2E0` | 7,984 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `Shield_DsrCanCurrentUserProvisionNgcKey` | `0x1C210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `Shield_DsrFreeCxhScenarioInfo` | `0x1C230` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `Shield_DsrFreeJoinInfo` | `0x1C250` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `Shield_DsrGetCxhScenarioInfo` | `0x1C270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `Shield_DsrGetJoinInfo` | `0x1C290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `Shield_DsrIsDeviceJoined` | `0x1C2B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `Shield_NgcEnumContainers` | `0x1C2D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `Shield_NgcFreeEnumState` | `0x1C2F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `Shield_NgcIsAnyContainerInVsm` | `0x1C310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `Shield_NgcQueryEnabled` | `0x1C330` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `Shield_DriverStoreClose` | `0x1C350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `Shield_DriverStoreFindW` | `0x1C370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `Shield_DriverStoreGetObjectPropertyW` | `0x1C390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `Shield_DriverStoreOpenW` | `0x1C3B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `Shield_IsUMgrEnumerateSessionUsersPresent` | `0x1C3D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `Shield_IsUMgrQueryUserTokenPresent` | `0x1C3D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `Shield_UMgrEnumerateSessionUsers` | `0x1C3E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `Shield_UMgrFreeSessionUsers` | `0x1C400` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `Shield_UMgrQueryUserToken` | `0x1C420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `Shield_CmsCloseActivity` | `0x1C440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `Shield_CmsCloseContainer` | `0x1C460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `Shield_CmsCreateActivity` | `0x1C480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `Shield_CmsOpenContainer` | `0x1C4A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `Shield_CmsRegisterForContainerNotifications` | `0x1C4C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `Shield_CmsStartActivityAsync` | `0x1C4E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `Shield_EvtClose` | `0x1C500` | 233 | UnwindData |  |
| 21 | `Shield_EvtCreateRenderContext` | `0x1C5F0` | 266 | UnwindData |  |
| 22 | `Shield_EvtNext` | `0x1C700` | 308 | UnwindData |  |
| 23 | `Shield_EvtQuery` | `0x1C840` | 288 | UnwindData |  |
| 24 | `Shield_EvtRender` | `0x1C970` | 325 | UnwindData |  |
| 49 | `Shield_HvciGetConfig` | `0x1CAC0` | 233 | UnwindData |  |
| 50 | `Shield_HvciIsActive` | `0x1CBB0` | 229 | UnwindData |  |
| 77 | `Shield_TpmClearWithPolicyOrPPI` | `0x1CCA0` | 301 | UnwindData |  |
| 78 | `Shield_TpmGatherLogs` | `0x1CDE0` | 300 | UnwindData |  |
| 79 | `Shield_TpmGetCapLockoutInfo` | `0x1CF20` | 301 | UnwindData |  |
| 80 | `Shield_TpmGetDeviceInformation` | `0x1D060` | 377 | UnwindData |  |
| 84 | `Shield_VbsGetIssues` | `0x1D1E0` | 202 | UnwindData |  |
| 85 | `Shield_VbsIsCapable` | `0x1D2B0` | 231 | UnwindData |  |
| 86 | `Shield_VbsIsRecommended` | `0x1D3A0` | 231 | UnwindData |  |
| 87 | `Shield_VbsSetScenarioEnable` | `0x1D490` | 244 | UnwindData |  |
| 93 | `Shield_KeyCredentialManagerGetOperationErrorStates` | `0x1D590` | 316 | UnwindData |  |
| 32 | `Shield_GetAddMsaStatus` | `0x1D740` | 1,275 | UnwindData |  |
| 38 | `Shield_GetOSVolumeEnablementStatus` | `0x1DC50` | 512 | UnwindData |  |
| 36 | `Shield_GetIsBuiltAsScpcUefiVariable` | `0x1E5A0` | 475 | UnwindData |  |
| 37 | `Shield_GetIsTpmPresent` | `0x1E790` | 300 | UnwindData |  |
| 41 | `Shield_GetPackageInfo` | `0x1E8D0` | 409 | UnwindData |  |
| 42 | `Shield_GetServices` | `0x1EA70` | 393 | UnwindData |  |
| 44 | `Shield_HotLoadInformation` | `0x1EC00` | 393 | UnwindData |  |
| 45 | `Shield_HspGetActiveVersion` | `0x1ED90` | 770 | UnwindData |  |
| 46 | `Shield_HspGetPlatRotHealthStatus` | `0x1F0A0` | 429 | UnwindData |  |
| 47 | `Shield_HspGetPlatRotVendorId` | `0x1F260` | 441 | UnwindData |  |
| 48 | `Shield_HspIsCapable` | `0x1F420` | 797 | UnwindData |  |
| 54 | `Shield_IsHspPresent` | `0x1F750` | 225 | UnwindData |  |
| 55 | `Shield_IsPlutonPresentAndLoaded` | `0x1F840` | 546 | UnwindData |  |
| 71 | `Shield_PlutonFree` | `0x1FA70` | 56 | UnwindData |  |
| 72 | `Shield_PlutonQueryApiSupported` | `0x1FAB0` | 189 | UnwindData |  |
| 88 | `Shield_WldpChangeVulnerableDriverBlocklistState` | `0x1FB80` | 86 | UnwindData |  |
| 89 | `Shield_WldpIsVulnerableDriverBlocklistDisabled` | `0x1FBE0` | 92 | UnwindData |  |
| 90 | `Shield_WldpIsVulnerableDriverBlocklistEligibleToDisable` | `0x1FC50` | 89 | UnwindData |  |
