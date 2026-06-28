# Binary Specification: policymanager.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\policymanager.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `61e60c647c6c20c0f2b404ba92fd04d742fe83e95ae439afdabad924928d4547`
* **Total Exported Functions:** 134

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 91 | `PolicyManager_GetAccountsPolicy_AllowMicrosoftAccountConnection` | `0x3940` | 502 | UnwindData |  |
| 118 | `PolicyManager_GetPolicyString` | `0x47C0` | 969 | UnwindData |  |
| 132 | `PolicyManager_IsPolicySetByMobileDeviceManager` | `0x4F80` | 816 | UnwindData |  |
| 67 | `EnterprisePolicyManagerStore_IsPolicySetByMobileDeviceManager` | `0x5480` | 74 | UnwindData |  |
| 116 | `PolicyManager_GetPolicyInt` | `0x5A00` | 650 | UnwindData |  |
| 113 | `PolicyManager_GetPolicy` | `0x5F80` | 2,414 | UnwindData |  |
| 74 | `EnterprisePolicyManagerStore_ReadPolicyMetadata` | `0x7260` | 148 | UnwindData |  |
| 53 | `EnterprisePolicyManagerStore_GetIntPolicyValue` | `0x9C40` | 375 | UnwindData |  |
| 59 | `EnterprisePolicyManagerStore_GetStringPolicyValue` | `0x9F70` | 9 | UnwindData |  |
| 13 | `EnterprisePolicyManagerStore_CSPResultAreaPolicyGetValue` | `0xB790` | 257 | UnwindData |  |
| 8 | `EnterprisePolicyManagerStore_CSPConfigSourceAreaPolicyCreateNodeInstance` | `0xBA60` | 499 | UnwindData |  |
| 28 | `EnterprisePolicyManagerStore_DoesProviderContextSidAreaPolicyValueExist` | `0xC4A0` | 178 | UnwindData |  |
| 57 | `EnterprisePolicyManagerStore_GetProviderContextSidAreaPolicyValue` | `0xC560` | 1,346 | UnwindData |  |
| 84 | `PolicyManager_FreeBinaryValue` | `0xCAB0` | 29 | UnwindData |  |
| 52 | `EnterprisePolicyManagerStore_GetEnrollmentTypeFromEnrollment` | `0xCAE0` | 159 | UnwindData |  |
| 72 | `EnterprisePolicyManagerStore_PublishAnyDelayedWnfs` | `0xD1B0` | 1,260 | UnwindData |  |
| 66 | `EnterprisePolicyManagerStore_IsPolicyAreaForIngestedAdmx` | `0x12B70` | 95 | UnwindData |  |
| 44 | `EnterprisePolicyManagerStore_GetAllProviderContextSidAreas` | `0x12E60` | 134 | UnwindData |  |
| 51 | `EnterprisePolicyManagerStore_GetEnrollmentState` | `0x13480` | 179 | UnwindData |  |
| 77 | `EnterprisePolicyManagerStore_ReleaseMergeLock` | `0x13E90` | 47 | UnwindData |  |
| 85 | `PolicyManager_FreeGetPolicyData` | `0x15590` | 165 | UnwindData |  |
| 87 | `PolicyManager_FreeStringValue` | `0x15F60` | 31 | UnwindData |  |
| 56 | `EnterprisePolicyManagerStore_GetPolicyTypeFromMetadata` | `0x177A0` | 15 | UnwindData |  |
| 70 | `EnterprisePolicyManagerStore_IsValidPolicy` | `0x181A0` | 283 | UnwindData |  |
| 94 | `PolicyManager_GetBrowserPolicy_AllowBrowser` | `0x18FF0` | 1,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `EnterprisePolicyManagerStore_CSPConfigSourceAreaPolicyGetValue` | `0x194F0` | 129 | UnwindData |  |
| 130 | `PolicyManager_GetWiFiPolicy_AllowManualWiFiConfiguration` | `0x1A1B0` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `EnterprisePolicyManagerStore_GetAllProviderContextSidAreaPolicies` | `0x1A360` | 300 | UnwindData |  |
| 99 | `PolicyManager_GetDeviceLockPolicy_AllowSimpleDevicePassword` | `0x1ABF0` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `PolicyManager_GetWiFiPolicy_AllowInternetSharing` | `0x1ADB0` | 3,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `PolicyManager_GetDeviceLockPolicy_DevicePasswordEnabled` | `0x1B9C0` | 3,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `EnterprisePolicyManagerStore_GetCurrentPolicyValue` | `0x1C670` | 23 | UnwindData |  |
| 37 | `EnterprisePolicyManagerStore_GetAdmxFileData` | `0x1CE50` | 258 | UnwindData |  |
| 109 | `PolicyManager_GetExperiencePolicy_AllowCortana` | `0x1D220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `EnterprisePolicyManagerStore_CSPConfigSourceAreaCreateNodeInstance` | `0x1D240` | 166 | UnwindData |  |
| 49 | `EnterprisePolicyManagerStore_GetBinaryPolicyValue` | `0x1D830` | 342 | UnwindData |  |
| 80 | `EnterprisePolicyManagerStore_SetGlobalValueChangedDirtyFlagInCurrentForArea` | `0x4C6F0` | 219 | UnwindData |  |
| 4 | `EnterprisePolicyManagerStore_AcquireMergeLock` | `0x4C7E0` | 241 | UnwindData |  |
| 46 | `EnterprisePolicyManagerStore_GetAllProviderIds` | `0x4CD60` | 179 | UnwindData |  |
| 83 | `MDMWinsOverGP_IsGPPolicySetByMDMEx` | `0x4F4A0` | 1,550 | UnwindData |  |
| 86 | `PolicyManager_FreeGroupAreaPolicyCollection` | `0x4FCE0` | 226 | UnwindData |  |
| 88 | `PolicyManager_FreeStringValues` | `0x4FDD0` | 117 | UnwindData |  |
| 89 | `PolicyManager_GetAboveLockPolicy_AllowActionCenterNotifications` | `0x4FE50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `PolicyManager_GetAccountsPolicy_AllowAddingNonMicrosoftAccountsManually` | `0x4FE70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `PolicyManager_GetApplicationManagementPolicy_AllowStore` | `0x4FE90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `PolicyManager_GetApplicationManagementPolicy_ApplicationRestrictions` | `0x4FEB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `PolicyManager_GetCameraPolicy_AllowCamera` | `0x4FED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `PolicyManager_GetConnectivityPolicy_AllowNFC` | `0x4FEF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `PolicyManager_GetConnectivityPolicy_AllowUSBConnection` | `0x4FF10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `PolicyManager_GetDeviceLockPolicy_AllowIdleReturnWithoutPassword` | `0x4FF30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `PolicyManager_GetDeviceLockPolicy_AlphanumericDevicePasswordRequired` | `0x4FF50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `PolicyManager_GetDeviceLockPolicy_DevicePasswordExpiration` | `0x4FF70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `PolicyManager_GetDeviceLockPolicy_DevicePasswordHistory` | `0x4FF90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `PolicyManager_GetDeviceLockPolicy_MaxDevicePasswordFailedAttempts` | `0x4FFB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `PolicyManager_GetDeviceLockPolicy_MaxInactivityTimeDeviceLock` | `0x4FFD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `PolicyManager_GetDeviceLockPolicy_MinDevicePasswordComplexCharacters` | `0x4FFF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `PolicyManager_GetDeviceLockPolicy_MinDevicePasswordLength` | `0x50010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `PolicyManager_GetExperiencePolicy_AllowCopyPaste` | `0x50030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `PolicyManager_GetExperiencePolicy_AllowScreenCapture` | `0x50050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `PolicyManager_GetExperiencePolicy_AllowSyncMySettings` | `0x50070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `PolicyManager_GetExperiencePolicy_AllowVoiceRecording` | `0x50090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `PolicyManager_GetGroupAreaPolicyCollectionGivenGroupName` | `0x500B0` | 1,192 | UnwindData |  |
| 114 | `PolicyManager_GetPolicyBinary` | `0x50560` | 31 | UnwindData |  |
| 115 | `PolicyManager_GetPolicyBinaryGivenEnrollmentId` | `0x50590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `PolicyManager_GetPolicyIntGivenEnrollmentId` | `0x505A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `PolicyManager_GetPolicyStringGivenEnrollmentId` | `0x505B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `PolicyManager_GetPolicyStringValues` | `0x505C0` | 319 | UnwindData |  |
| 121 | `PolicyManager_GetSearchPolicy_AllowSearchToUseLocation` | `0x50710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `PolicyManager_GetSearchPolicy_SafeSearchPermissions` | `0x50730` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `PolicyManager_GetSecurityPolicy_AllowManualRootCertificateInstallation` | `0x50750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `PolicyManager_GetSecurityPolicy_RequireDeviceEncryption` | `0x50770` | 73 | UnwindData |  |
| 125 | `PolicyManager_GetSystemPolicy_AllowLocation` | `0x507C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `PolicyManager_GetSystemPolicy_AllowStorageCard` | `0x507E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `PolicyManager_GetSystemPolicy_AllowUserToResetPhone` | `0x50800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `PolicyManager_GetWiFiPolicy_AllowAutoConnectToWiFiSenseHotspots` | `0x50820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `PolicyManager_GetWiFiPolicy_AllowWiFi` | `0x50840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `PolicyManager_PublishPolicyWNFCache` | `0x50860` | 4,368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DeviceManagement_CompareSettingValues` | `0x51970` | 578 | UnwindData |  |
| 35 | `EnterprisePolicyManagerStore_EvaluatePoliciesUpdateCurrent` | `0x53340` | 170 | UnwindData |  |
| 71 | `EnterprisePolicyManagerStore_PerformEvaluatorMerge` | `0x54C40` | 163 | UnwindData |  |
| 79 | `EnterprisePolicyManagerStore_SetEnrollmentDormantState` | `0x54CF0` | 328 | UnwindData |  |
| 6 | `EnterprisePolicyManagerStore_CSPConfigSourceAreaDeleteChild` | `0x56AF0` | 213 | UnwindData |  |
| 7 | `EnterprisePolicyManagerStore_CSPConfigSourceAreaGetChildNodeNames` | `0x56BD0` | 175 | UnwindData |  |
| 10 | `EnterprisePolicyManagerStore_CSPConfigSourceAreaPolicySetValue` | `0x56C90` | 122 | UnwindData |  |
| 11 | `EnterprisePolicyManagerStore_CSPConfigSourceDeleteChild` | `0x56D10` | 127 | UnwindData |  |
| 12 | `EnterprisePolicyManagerStore_CSPResultAreaGetChildNodeNames` | `0x56DA0` | 178 | UnwindData |  |
| 14 | `EnterprisePolicyManagerStore_CSPResultGetAreaChildNodeNames` | `0x56E60` | 130 | UnwindData |  |
| 15 | `EnterprisePolicyManagerStore_CSPStoreLinkedAccount` | `0x56EF0` | 154 | UnwindData |  |
| 30 | `EnterprisePolicyManagerStore_EDPCSPConfigSourceAreaDeleteChild` | `0x56F90` | 327 | UnwindData |  |
| 31 | `EnterprisePolicyManagerStore_EDPCSPConfigSourceAreaPolicyGetValue` | `0x570E0` | 165 | UnwindData |  |
| 32 | `EnterprisePolicyManagerStore_EDPCSPConfigSourceAreaPolicySetValue` | `0x57190` | 82 | UnwindData |  |
| 16 | `EnterprisePolicyManagerStore_CreateProviderHive` | `0x58500` | 70 | UnwindData |  |
| 20 | `EnterprisePolicyManagerStore_DeleteProvider` | `0x58550` | 766 | UnwindData |  |
| 21 | `EnterprisePolicyManagerStore_DeleteProviderContextSidArea` | `0x58860` | 412 | UnwindData |  |
| 22 | `EnterprisePolicyManagerStore_DeleteProviderContextSidAreaPolicy` | `0x58A10` | 1,347 | UnwindData |  |
| 23 | `EnterprisePolicyManagerStore_DeleteProviderIdAndMerge` | `0x58F60` | 117 | UnwindData |  |
| 24 | `EnterprisePolicyManagerStore_DeleteProviderIdAndMergeScopeData` | `0x58FE0` | 33 | UnwindData |  |
| 26 | `EnterprisePolicyManagerStore_DoesProviderContextNameExist` | `0x59010` | 134 | UnwindData |  |
| 27 | `EnterprisePolicyManagerStore_DoesProviderContextSidAreaExist` | `0x590A0` | 117 | UnwindData |  |
| 29 | `EnterprisePolicyManagerStore_DoesProviderExist` | `0x59120` | 103 | UnwindData |  |
| 33 | `EnterprisePolicyManagerStore_EnsureProviderContextNameExist` | `0x59190` | 87 | UnwindData |  |
| 34 | `EnterprisePolicyManagerStore_EnsureProviderContextSidAreaExist` | `0x591F0` | 83 | UnwindData |  |
| 38 | `EnterprisePolicyManagerStore_GetAllCurrentSidAreaPolicies` | `0x59250` | 236 | UnwindData |  |
| 39 | `EnterprisePolicyManagerStore_GetAllCurrentSidAreas` | `0x59350` | 198 | UnwindData |  |
| 40 | `EnterprisePolicyManagerStore_GetAllCurrentSids` | `0x59420` | 212 | UnwindData |  |
| 41 | `EnterprisePolicyManagerStore_GetAllDefaultAreaPolicies` | `0x59500` | 170 | UnwindData |  |
| 42 | `EnterprisePolicyManagerStore_GetAllDefaultAreas` | `0x595B0` | 124 | UnwindData |  |
| 45 | `EnterprisePolicyManagerStore_GetAllProviderContextSids` | `0x59640` | 116 | UnwindData |  |
| 47 | `EnterprisePolicyManagerStore_GetAllProviderPolicyStringValues` | `0x596C0` | 1,090 | UnwindData |  |
| 54 | `EnterprisePolicyManagerStore_GetPolicyDoNotAllowFromMetadata` | `0x59E60` | 278 | UnwindData |  |
| 55 | `EnterprisePolicyManagerStore_GetPolicyLowHighRangeFromMetadata` | `0x59F80` | 322 | UnwindData |  |
| 63 | `EnterprisePolicyManagerStore_IsADMXIngestionAllowed` | `0x5A0D0` | 369 | UnwindData |  |
| 64 | `EnterprisePolicyManagerStore_IsAreaPolicySLAPIAllowed` | `0x5A250` | 393 | UnwindData |  |
| 65 | `EnterprisePolicyManagerStore_IsAreaPolicySLAPIAllowedGivenSLAPIPolicyString` | `0x5A3E0` | 405 | UnwindData |  |
| 69 | `EnterprisePolicyManagerStore_IsValidArea` | `0x5A580` | 165 | UnwindData |  |
| 81 | `EnterprisePolicyManagerStore_SetProviderContextSidAreaPolicyValue` | `0x5A630` | 5,522 | UnwindData |  |
| 134 | `SettingsManagerStore_GetWnfsForSettingPath` | `0x5E120` | 1,276 | UnwindData |  |
| 135 | `SettingsManagerStore_ReleaseWnfNames` | `0x5E630` | 27 | UnwindData |  |
| 25 | `EnterprisePolicyManagerStore_DeleteVirtuallyDeletedHive` | `0x5E660` | 141 | UnwindData |  |
| 36 | `EnterprisePolicyManagerStore_FreeURIsOfProviders` | `0x5ED50` | 117 | UnwindData |  |
| 48 | `EnterprisePolicyManagerStore_GetAllURIsOfProviders` | `0x5EDD0` | 1,811 | UnwindData |  |
| 60 | `EnterprisePolicyManagerStore_GetTrueArea` | `0x5F4F0` | 72 | UnwindData |  |
| 68 | `EnterprisePolicyManagerStore_IsURISetByProvider` | `0x5F540` | 413 | UnwindData |  |
| 75 | `EnterprisePolicyManagerStore_RefreshAll` | `0x5F6F0` | 3,129 | UnwindData |  |
| 76 | `EnterprisePolicyManagerStore_RefreshPerUserPoliciesForMDMEnrollments` | `0x60330` | 1,363 | UnwindData |  |
| 78 | `EnterprisePolicyManagerStore_RemoveRegistryKeypathEASPoliciesIfExchangeDeviceLockPoliciesNotSet` | `0x60890` | 923 | UnwindData |  |
| 58 | `EnterprisePolicyManagerStore_GetSnapshotOfPolicyValue` | `0x62880` | 640 | UnwindData |  |
| 61 | `EnterprisePolicyManagerStore_GetWinningProvider` | `0x62B10` | 70 | UnwindData |  |
| 73 | `EnterprisePolicyManagerStore_PublishPolicyWNFCache` | `0x62B60` | 757 | UnwindData |  |
| 17 | `EnterprisePolicyManagerStore_DeleteEnrollmentAdmxMetadata` | `0x74980` | 83 | UnwindData |  |
| 18 | `EnterprisePolicyManagerStore_DeleteEnrollmentAppAdmxMetadata` | `0x749E0` | 77 | UnwindData |  |
| 19 | `EnterprisePolicyManagerStore_DeleteEnrollmentAppSettingTypeAdmxMetadata` | `0x74A40` | 99 | UnwindData |  |
| 62 | `EnterprisePolicyManagerStore_IngestAdmxTextBlob` | `0x74AB0` | 234 | UnwindData |  |
| 82 | `EnterprisePolicyManagerStore_VerifyAdmxPoliciesAreNotSet` | `0x753F0` | 580 | UnwindData |  |
