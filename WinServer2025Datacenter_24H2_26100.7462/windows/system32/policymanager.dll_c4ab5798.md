# Binary Specification: policymanager.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\policymanager.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c4ab57984c3fd5a13f7d47cb19e96db857bf6213e418ef2da48acce671e75788`
* **Total Exported Functions:** 134

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 118 | `PolicyManager_GetPolicyString` | `0x6E60` | 969 | UnwindData |  |
| 132 | `PolicyManager_IsPolicySetByMobileDeviceManager` | `0x7620` | 816 | UnwindData |  |
| 67 | `EnterprisePolicyManagerStore_IsPolicySetByMobileDeviceManager` | `0x7AC0` | 74 | UnwindData |  |
| 116 | `PolicyManager_GetPolicyInt` | `0x8040` | 650 | UnwindData |  |
| 113 | `PolicyManager_GetPolicy` | `0x85C0` | 2,414 | UnwindData |  |
| 74 | `EnterprisePolicyManagerStore_ReadPolicyMetadata` | `0x9400` | 148 | UnwindData |  |
| 53 | `EnterprisePolicyManagerStore_GetIntPolicyValue` | `0xC060` | 375 | UnwindData |  |
| 59 | `EnterprisePolicyManagerStore_GetStringPolicyValue` | `0xC390` | 9 | UnwindData |  |
| 13 | `EnterprisePolicyManagerStore_CSPResultAreaPolicyGetValue` | `0xDBB0` | 257 | UnwindData |  |
| 8 | `EnterprisePolicyManagerStore_CSPConfigSourceAreaPolicyCreateNodeInstance` | `0xDE80` | 499 | UnwindData |  |
| 28 | `EnterprisePolicyManagerStore_DoesProviderContextSidAreaPolicyValueExist` | `0xE8C0` | 178 | UnwindData |  |
| 57 | `EnterprisePolicyManagerStore_GetProviderContextSidAreaPolicyValue` | `0xE980` | 1,346 | UnwindData |  |
| 84 | `PolicyManager_FreeBinaryValue` | `0xEED0` | 29 | UnwindData |  |
| 52 | `EnterprisePolicyManagerStore_GetEnrollmentTypeFromEnrollment` | `0xEF00` | 159 | UnwindData |  |
| 72 | `EnterprisePolicyManagerStore_PublishAnyDelayedWnfs` | `0xF5D0` | 1,260 | UnwindData |  |
| 91 | `PolicyManager_GetAccountsPolicy_AllowMicrosoftAccountConnection` | `0x11A70` | 502 | UnwindData |  |
| 66 | `EnterprisePolicyManagerStore_IsPolicyAreaForIngestedAdmx` | `0x12C80` | 95 | UnwindData |  |
| 44 | `EnterprisePolicyManagerStore_GetAllProviderContextSidAreas` | `0x12F70` | 134 | UnwindData |  |
| 51 | `EnterprisePolicyManagerStore_GetEnrollmentState` | `0x13590` | 179 | UnwindData |  |
| 77 | `EnterprisePolicyManagerStore_ReleaseMergeLock` | `0x13FA0` | 47 | UnwindData |  |
| 85 | `PolicyManager_FreeGetPolicyData` | `0x156A0` | 165 | UnwindData |  |
| 87 | `PolicyManager_FreeStringValue` | `0x16070` | 31 | UnwindData |  |
| 56 | `EnterprisePolicyManagerStore_GetPolicyTypeFromMetadata` | `0x17800` | 15 | UnwindData |  |
| 70 | `EnterprisePolicyManagerStore_IsValidPolicy` | `0x184D0` | 283 | UnwindData |  |
| 94 | `PolicyManager_GetBrowserPolicy_AllowBrowser` | `0x19320` | 1,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `EnterprisePolicyManagerStore_CSPConfigSourceAreaPolicyGetValue` | `0x19820` | 129 | UnwindData |  |
| 130 | `PolicyManager_GetWiFiPolicy_AllowManualWiFiConfiguration` | `0x1A4E0` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `EnterprisePolicyManagerStore_GetAllProviderContextSidAreaPolicies` | `0x1A690` | 300 | UnwindData |  |
| 99 | `PolicyManager_GetDeviceLockPolicy_AllowSimpleDevicePassword` | `0x1AF20` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `PolicyManager_GetWiFiPolicy_AllowInternetSharing` | `0x1B0E0` | 3,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `PolicyManager_GetDeviceLockPolicy_DevicePasswordEnabled` | `0x1BCF0` | 3,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `EnterprisePolicyManagerStore_GetCurrentPolicyValue` | `0x1C9A0` | 23 | UnwindData |  |
| 37 | `EnterprisePolicyManagerStore_GetAdmxFileData` | `0x1D180` | 258 | UnwindData |  |
| 109 | `PolicyManager_GetExperiencePolicy_AllowCortana` | `0x1D550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `EnterprisePolicyManagerStore_CSPConfigSourceAreaCreateNodeInstance` | `0x1D570` | 166 | UnwindData |  |
| 49 | `EnterprisePolicyManagerStore_GetBinaryPolicyValue` | `0x1DB60` | 342 | UnwindData |  |
| 80 | `EnterprisePolicyManagerStore_SetGlobalValueChangedDirtyFlagInCurrentForArea` | `0x4C970` | 219 | UnwindData |  |
| 4 | `EnterprisePolicyManagerStore_AcquireMergeLock` | `0x4CA60` | 241 | UnwindData |  |
| 46 | `EnterprisePolicyManagerStore_GetAllProviderIds` | `0x4CF30` | 179 | UnwindData |  |
| 83 | `MDMWinsOverGP_IsGPPolicySetByMDMEx` | `0x4F650` | 1,550 | UnwindData |  |
| 86 | `PolicyManager_FreeGroupAreaPolicyCollection` | `0x4FE90` | 226 | UnwindData |  |
| 88 | `PolicyManager_FreeStringValues` | `0x4FF80` | 117 | UnwindData |  |
| 89 | `PolicyManager_GetAboveLockPolicy_AllowActionCenterNotifications` | `0x50000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `PolicyManager_GetAccountsPolicy_AllowAddingNonMicrosoftAccountsManually` | `0x50020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `PolicyManager_GetApplicationManagementPolicy_AllowStore` | `0x50040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `PolicyManager_GetApplicationManagementPolicy_ApplicationRestrictions` | `0x50060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `PolicyManager_GetCameraPolicy_AllowCamera` | `0x50080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `PolicyManager_GetConnectivityPolicy_AllowNFC` | `0x500A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `PolicyManager_GetConnectivityPolicy_AllowUSBConnection` | `0x500C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `PolicyManager_GetDeviceLockPolicy_AllowIdleReturnWithoutPassword` | `0x500E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `PolicyManager_GetDeviceLockPolicy_AlphanumericDevicePasswordRequired` | `0x50100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `PolicyManager_GetDeviceLockPolicy_DevicePasswordExpiration` | `0x50120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `PolicyManager_GetDeviceLockPolicy_DevicePasswordHistory` | `0x50140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `PolicyManager_GetDeviceLockPolicy_MaxDevicePasswordFailedAttempts` | `0x50160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `PolicyManager_GetDeviceLockPolicy_MaxInactivityTimeDeviceLock` | `0x50180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `PolicyManager_GetDeviceLockPolicy_MinDevicePasswordComplexCharacters` | `0x501A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `PolicyManager_GetDeviceLockPolicy_MinDevicePasswordLength` | `0x501C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `PolicyManager_GetExperiencePolicy_AllowCopyPaste` | `0x501E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `PolicyManager_GetExperiencePolicy_AllowScreenCapture` | `0x50200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `PolicyManager_GetExperiencePolicy_AllowSyncMySettings` | `0x50220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `PolicyManager_GetExperiencePolicy_AllowVoiceRecording` | `0x50240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `PolicyManager_GetGroupAreaPolicyCollectionGivenGroupName` | `0x50260` | 1,192 | UnwindData |  |
| 114 | `PolicyManager_GetPolicyBinary` | `0x50710` | 31 | UnwindData |  |
| 115 | `PolicyManager_GetPolicyBinaryGivenEnrollmentId` | `0x50740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `PolicyManager_GetPolicyIntGivenEnrollmentId` | `0x50750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `PolicyManager_GetPolicyStringGivenEnrollmentId` | `0x50760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `PolicyManager_GetPolicyStringValues` | `0x50770` | 319 | UnwindData |  |
| 121 | `PolicyManager_GetSearchPolicy_AllowSearchToUseLocation` | `0x508C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `PolicyManager_GetSearchPolicy_SafeSearchPermissions` | `0x508E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `PolicyManager_GetSecurityPolicy_AllowManualRootCertificateInstallation` | `0x50900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `PolicyManager_GetSecurityPolicy_RequireDeviceEncryption` | `0x50920` | 73 | UnwindData |  |
| 125 | `PolicyManager_GetSystemPolicy_AllowLocation` | `0x50970` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `PolicyManager_GetSystemPolicy_AllowStorageCard` | `0x50990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `PolicyManager_GetSystemPolicy_AllowUserToResetPhone` | `0x509B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `PolicyManager_GetWiFiPolicy_AllowAutoConnectToWiFiSenseHotspots` | `0x509D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `PolicyManager_GetWiFiPolicy_AllowWiFi` | `0x509F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `PolicyManager_PublishPolicyWNFCache` | `0x50A10` | 4,368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DeviceManagement_CompareSettingValues` | `0x51B20` | 578 | UnwindData |  |
| 35 | `EnterprisePolicyManagerStore_EvaluatePoliciesUpdateCurrent` | `0x534F0` | 170 | UnwindData |  |
| 71 | `EnterprisePolicyManagerStore_PerformEvaluatorMerge` | `0x54DF0` | 163 | UnwindData |  |
| 79 | `EnterprisePolicyManagerStore_SetEnrollmentDormantState` | `0x54EA0` | 328 | UnwindData |  |
| 6 | `EnterprisePolicyManagerStore_CSPConfigSourceAreaDeleteChild` | `0x56990` | 213 | UnwindData |  |
| 7 | `EnterprisePolicyManagerStore_CSPConfigSourceAreaGetChildNodeNames` | `0x56A70` | 175 | UnwindData |  |
| 10 | `EnterprisePolicyManagerStore_CSPConfigSourceAreaPolicySetValue` | `0x56B30` | 122 | UnwindData |  |
| 11 | `EnterprisePolicyManagerStore_CSPConfigSourceDeleteChild` | `0x56BB0` | 127 | UnwindData |  |
| 12 | `EnterprisePolicyManagerStore_CSPResultAreaGetChildNodeNames` | `0x56C40` | 178 | UnwindData |  |
| 14 | `EnterprisePolicyManagerStore_CSPResultGetAreaChildNodeNames` | `0x56D00` | 130 | UnwindData |  |
| 15 | `EnterprisePolicyManagerStore_CSPStoreLinkedAccount` | `0x56D90` | 154 | UnwindData |  |
| 30 | `EnterprisePolicyManagerStore_EDPCSPConfigSourceAreaDeleteChild` | `0x56E30` | 327 | UnwindData |  |
| 31 | `EnterprisePolicyManagerStore_EDPCSPConfigSourceAreaPolicyGetValue` | `0x56F80` | 165 | UnwindData |  |
| 32 | `EnterprisePolicyManagerStore_EDPCSPConfigSourceAreaPolicySetValue` | `0x57030` | 82 | UnwindData |  |
| 16 | `EnterprisePolicyManagerStore_CreateProviderHive` | `0x583A0` | 70 | UnwindData |  |
| 20 | `EnterprisePolicyManagerStore_DeleteProvider` | `0x583F0` | 766 | UnwindData |  |
| 21 | `EnterprisePolicyManagerStore_DeleteProviderContextSidArea` | `0x58700` | 412 | UnwindData |  |
| 22 | `EnterprisePolicyManagerStore_DeleteProviderContextSidAreaPolicy` | `0x588B0` | 1,347 | UnwindData |  |
| 23 | `EnterprisePolicyManagerStore_DeleteProviderIdAndMerge` | `0x58E00` | 117 | UnwindData |  |
| 24 | `EnterprisePolicyManagerStore_DeleteProviderIdAndMergeScopeData` | `0x58E80` | 33 | UnwindData |  |
| 26 | `EnterprisePolicyManagerStore_DoesProviderContextNameExist` | `0x58EB0` | 134 | UnwindData |  |
| 27 | `EnterprisePolicyManagerStore_DoesProviderContextSidAreaExist` | `0x58F40` | 117 | UnwindData |  |
| 29 | `EnterprisePolicyManagerStore_DoesProviderExist` | `0x58FC0` | 103 | UnwindData |  |
| 33 | `EnterprisePolicyManagerStore_EnsureProviderContextNameExist` | `0x59030` | 87 | UnwindData |  |
| 34 | `EnterprisePolicyManagerStore_EnsureProviderContextSidAreaExist` | `0x59090` | 83 | UnwindData |  |
| 38 | `EnterprisePolicyManagerStore_GetAllCurrentSidAreaPolicies` | `0x590F0` | 236 | UnwindData |  |
| 39 | `EnterprisePolicyManagerStore_GetAllCurrentSidAreas` | `0x591F0` | 198 | UnwindData |  |
| 40 | `EnterprisePolicyManagerStore_GetAllCurrentSids` | `0x592C0` | 212 | UnwindData |  |
| 41 | `EnterprisePolicyManagerStore_GetAllDefaultAreaPolicies` | `0x593A0` | 170 | UnwindData |  |
| 42 | `EnterprisePolicyManagerStore_GetAllDefaultAreas` | `0x59450` | 124 | UnwindData |  |
| 45 | `EnterprisePolicyManagerStore_GetAllProviderContextSids` | `0x594E0` | 116 | UnwindData |  |
| 47 | `EnterprisePolicyManagerStore_GetAllProviderPolicyStringValues` | `0x59560` | 1,090 | UnwindData |  |
| 54 | `EnterprisePolicyManagerStore_GetPolicyDoNotAllowFromMetadata` | `0x59D00` | 278 | UnwindData |  |
| 55 | `EnterprisePolicyManagerStore_GetPolicyLowHighRangeFromMetadata` | `0x59E20` | 322 | UnwindData |  |
| 63 | `EnterprisePolicyManagerStore_IsADMXIngestionAllowed` | `0x59F70` | 369 | UnwindData |  |
| 64 | `EnterprisePolicyManagerStore_IsAreaPolicySLAPIAllowed` | `0x5A0F0` | 393 | UnwindData |  |
| 65 | `EnterprisePolicyManagerStore_IsAreaPolicySLAPIAllowedGivenSLAPIPolicyString` | `0x5A280` | 405 | UnwindData |  |
| 69 | `EnterprisePolicyManagerStore_IsValidArea` | `0x5A420` | 165 | UnwindData |  |
| 81 | `EnterprisePolicyManagerStore_SetProviderContextSidAreaPolicyValue` | `0x5A4D0` | 5,522 | UnwindData |  |
| 134 | `SettingsManagerStore_GetWnfsForSettingPath` | `0x5D9D0` | 1,276 | UnwindData |  |
| 135 | `SettingsManagerStore_ReleaseWnfNames` | `0x5DEE0` | 27 | UnwindData |  |
| 25 | `EnterprisePolicyManagerStore_DeleteVirtuallyDeletedHive` | `0x5DF10` | 141 | UnwindData |  |
| 36 | `EnterprisePolicyManagerStore_FreeURIsOfProviders` | `0x5E600` | 117 | UnwindData |  |
| 48 | `EnterprisePolicyManagerStore_GetAllURIsOfProviders` | `0x5E680` | 1,811 | UnwindData |  |
| 60 | `EnterprisePolicyManagerStore_GetTrueArea` | `0x5EDA0` | 72 | UnwindData |  |
| 68 | `EnterprisePolicyManagerStore_IsURISetByProvider` | `0x5EDF0` | 413 | UnwindData |  |
| 75 | `EnterprisePolicyManagerStore_RefreshAll` | `0x5EFA0` | 3,129 | UnwindData |  |
| 76 | `EnterprisePolicyManagerStore_RefreshPerUserPoliciesForMDMEnrollments` | `0x5FBE0` | 1,363 | UnwindData |  |
| 78 | `EnterprisePolicyManagerStore_RemoveRegistryKeypathEASPoliciesIfExchangeDeviceLockPoliciesNotSet` | `0x60140` | 923 | UnwindData |  |
| 58 | `EnterprisePolicyManagerStore_GetSnapshotOfPolicyValue` | `0x634F0` | 640 | UnwindData |  |
| 61 | `EnterprisePolicyManagerStore_GetWinningProvider` | `0x63780` | 70 | UnwindData |  |
| 73 | `EnterprisePolicyManagerStore_PublishPolicyWNFCache` | `0x637D0` | 757 | UnwindData |  |
| 17 | `EnterprisePolicyManagerStore_DeleteEnrollmentAdmxMetadata` | `0x74AB0` | 83 | UnwindData |  |
| 18 | `EnterprisePolicyManagerStore_DeleteEnrollmentAppAdmxMetadata` | `0x74B10` | 77 | UnwindData |  |
| 19 | `EnterprisePolicyManagerStore_DeleteEnrollmentAppSettingTypeAdmxMetadata` | `0x74B70` | 99 | UnwindData |  |
| 62 | `EnterprisePolicyManagerStore_IngestAdmxTextBlob` | `0x74BE0` | 234 | UnwindData |  |
| 82 | `EnterprisePolicyManagerStore_VerifyAdmxPoliciesAreNotSet` | `0x75520` | 580 | UnwindData |  |
