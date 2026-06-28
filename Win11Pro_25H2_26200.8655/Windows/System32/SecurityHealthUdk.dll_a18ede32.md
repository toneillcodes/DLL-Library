# Binary Specification: SecurityHealthUdk.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\SecurityHealthUdk.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a18ede32ec96e97dd706f79c878b4c573f6d7bafb8f2c8b46935656ba61fbcd6`
* **Total Exported Functions:** 93

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 92 | `DllMain` | `0x4B30` | 295 | UnwindData |  |
| 19 | `Shield_EnumerateImageNames` | `0x6B30` | 697 | UnwindData |  |
| 25 | `Shield_ExportMitigationPoliciesToXmlFile` | `0x6DF0` | 430 | UnwindData |  |
| 34 | `Shield_GetImageMitigationPolicy` | `0x6FB0` | 989 | UnwindData |  |
| 35 | `Shield_GetImageMitigationPolicyEx` | `0x73A0` | 162 | UnwindData |  |
| 39 | `Shield_GetOsDefaultMitigationPolicy` | `0x7450` | 397 | UnwindData |  |
| 40 | `Shield_GetOsDefaultMitigationPolicyEx` | `0x75F0` | 704 | UnwindData |  |
| 53 | `Shield_ImportMitigationPoliciesFromXmlFile` | `0x78C0` | 722 | UnwindData |  |
| 74 | `Shield_RemoveImageNameAndItsMitigationPolicies` | `0x7BA0` | 309 | UnwindData |  |
| 76 | `Shield_SetImageMitigationPolicyEx` | `0x7CE0` | 300 | UnwindData |  |
| 26 | `Shield_FWClosePolicyStore` | `0x7F30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `Shield_FWGetConfig` | `0x7F50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `Shield_FWOpenPolicyStore` | `0x7F70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `Shield_FwActivate` | `0x7F90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `Shield_FwAnalyzeFirewallPolicy` | `0x7FB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `Shield_FwIsGroupPolicyEnforced` | `0x7FD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `Shield_IcfChangeNotificationCreate` | `0x7FF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `Shield_IcfChangeNotificationDestroy` | `0x8010` | 73,376 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `Shield_ApplicationGuardRefreshState` | `0x19EB0` | 17 | UnwindData |  |
| 8 | `Shield_CpmcGetContainerIdForUser` | `0x19ED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `Shield_GetApplicationGuardPolicy` | `0x19EF0` | 244 | UnwindData |  |
| 43 | `Shield_GetStoragePolicySettings` | `0x19FF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `Shield_IsQueryWin32SubsystemHostPresent` | `0x1A010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `Shield_LUAIsShadowAdminEnabled` | `0x1A020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `Shield_LsaLookupUserAccountType` | `0x1A030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `Shield_MpGetWindowsLockdownMode` | `0x1A050` | 86 | UnwindData |  |
| 62 | `Shield_MpIsAccountPasswordLess` | `0x1A0B0` | 79 | UnwindData |  |
| 63 | `Shield_MpIsBrowserReplacementFeaturePresent` | `0x1A110` | 314 | UnwindData |  |
| 64 | `Shield_MpIsWcosProductionConfiguration` | `0x1A250` | 118 | UnwindData |  |
| 65 | `Shield_MpIsWindowsLockdownMode` | `0x1A2D0` | 126 | UnwindData |  |
| 66 | `Shield_MpRegisterWaitForSingleObjectEx` | `0x1A360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `Shield_QueryWin32SubsystemHost` | `0x1A380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `Shield_SetApplicationGuardPolicy` | `0x1A3A0` | 87 | UnwindData |  |
| 91 | `Shield_WldpQueryPolicySettingEnabled2` | `0x1A400` | 7,984 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `Shield_DsrCanCurrentUserProvisionNgcKey` | `0x1C330` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `Shield_DsrFreeCxhScenarioInfo` | `0x1C350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `Shield_DsrFreeJoinInfo` | `0x1C370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `Shield_DsrGetCxhScenarioInfo` | `0x1C390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `Shield_DsrGetJoinInfo` | `0x1C3B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `Shield_DsrIsDeviceJoined` | `0x1C3D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `Shield_NgcEnumContainers` | `0x1C3F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `Shield_NgcFreeEnumState` | `0x1C410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `Shield_NgcIsAnyContainerInVsm` | `0x1C430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `Shield_NgcQueryEnabled` | `0x1C450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `Shield_DriverStoreClose` | `0x1C470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `Shield_DriverStoreFindW` | `0x1C490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `Shield_DriverStoreGetObjectPropertyW` | `0x1C4B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `Shield_DriverStoreOpenW` | `0x1C4D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `Shield_IsUMgrEnumerateSessionUsersPresent` | `0x1C4F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `Shield_IsUMgrQueryUserTokenPresent` | `0x1C4F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `Shield_UMgrEnumerateSessionUsers` | `0x1C500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `Shield_UMgrFreeSessionUsers` | `0x1C520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `Shield_UMgrQueryUserToken` | `0x1C540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `Shield_CmsCloseActivity` | `0x1C560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `Shield_CmsCloseContainer` | `0x1C580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `Shield_CmsCreateActivity` | `0x1C5A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `Shield_CmsOpenContainer` | `0x1C5C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `Shield_CmsRegisterForContainerNotifications` | `0x1C5E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `Shield_CmsStartActivityAsync` | `0x1C600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `Shield_EvtClose` | `0x1C620` | 233 | UnwindData |  |
| 21 | `Shield_EvtCreateRenderContext` | `0x1C710` | 266 | UnwindData |  |
| 22 | `Shield_EvtNext` | `0x1C820` | 308 | UnwindData |  |
| 23 | `Shield_EvtQuery` | `0x1C960` | 288 | UnwindData |  |
| 24 | `Shield_EvtRender` | `0x1CA90` | 325 | UnwindData |  |
| 49 | `Shield_HvciGetConfig` | `0x1CBE0` | 233 | UnwindData |  |
| 50 | `Shield_HvciIsActive` | `0x1CCD0` | 229 | UnwindData |  |
| 77 | `Shield_TpmClearWithPolicyOrPPI` | `0x1CDC0` | 301 | UnwindData |  |
| 78 | `Shield_TpmGatherLogs` | `0x1CF00` | 300 | UnwindData |  |
| 79 | `Shield_TpmGetCapLockoutInfo` | `0x1D040` | 301 | UnwindData |  |
| 80 | `Shield_TpmGetDeviceInformation` | `0x1D180` | 377 | UnwindData |  |
| 84 | `Shield_VbsGetIssues` | `0x1D300` | 202 | UnwindData |  |
| 85 | `Shield_VbsIsCapable` | `0x1D3D0` | 231 | UnwindData |  |
| 86 | `Shield_VbsIsRecommended` | `0x1D4C0` | 231 | UnwindData |  |
| 87 | `Shield_VbsSetScenarioEnable` | `0x1D5B0` | 244 | UnwindData |  |
| 93 | `Shield_KeyCredentialManagerGetOperationErrorStates` | `0x1D6B0` | 316 | UnwindData |  |
| 32 | `Shield_GetAddMsaStatus` | `0x1D860` | 1,275 | UnwindData |  |
| 38 | `Shield_GetOSVolumeEnablementStatus` | `0x1DD70` | 512 | UnwindData |  |
| 36 | `Shield_GetIsBuiltAsScpcUefiVariable` | `0x1E320` | 475 | UnwindData |  |
| 37 | `Shield_GetIsTpmPresent` | `0x1E510` | 300 | UnwindData |  |
| 41 | `Shield_GetPackageInfo` | `0x1E650` | 381 | UnwindData |  |
| 42 | `Shield_GetServices` | `0x1E7E0` | 365 | UnwindData |  |
| 44 | `Shield_HotLoadInformation` | `0x1E960` | 365 | UnwindData |  |
| 45 | `Shield_HspGetActiveVersion` | `0x1EAE0` | 770 | UnwindData |  |
| 46 | `Shield_HspGetPlatRotHealthStatus` | `0x1EDF0` | 429 | UnwindData |  |
| 47 | `Shield_HspGetPlatRotVendorId` | `0x1EFB0` | 441 | UnwindData |  |
| 48 | `Shield_HspIsCapable` | `0x1F170` | 797 | UnwindData |  |
| 54 | `Shield_IsHspPresent` | `0x1F4A0` | 225 | UnwindData |  |
| 55 | `Shield_IsPlutonPresentAndLoaded` | `0x1F590` | 518 | UnwindData |  |
| 71 | `Shield_PlutonFree` | `0x1F7A0` | 24 | UnwindData |  |
| 72 | `Shield_PlutonQueryApiSupported` | `0x1F7C0` | 162 | UnwindData |  |
| 88 | `Shield_WldpChangeVulnerableDriverBlocklistState` | `0x1F870` | 86 | UnwindData |  |
| 89 | `Shield_WldpIsVulnerableDriverBlocklistDisabled` | `0x1F8D0` | 92 | UnwindData |  |
| 90 | `Shield_WldpIsVulnerableDriverBlocklistEligibleToDisable` | `0x1F940` | 89 | UnwindData |  |
