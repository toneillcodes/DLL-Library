# Binary Specification: logoncli.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\logoncli.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a9abdac86a40ba62b6be138abae5fbcdf7c46b7aba9525d84636e9accdd588be`
* **Total Exported Functions:** 90

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 18 | `DsGetDcNameA` | `0x1710` | 51 | UnwindData |  |
| 30 | `DsGetSiteNameW` | `0x1750` | 171 | UnwindData |  |
| 80 | `NetGetDCName` | `0x1810` | 571 | UnwindData |  |
| 20 | `DsGetDcNameWithAccountA` | `0x1A60` | 1,811 | UnwindData |  |
| 19 | `DsGetDcNameW` | `0x2480` | 51 | UnwindData |  |
| 21 | `DsGetDcNameWithAccountW` | `0x24C0` | 2,878 | UnwindData |  |
| 23 | `DsGetDcNextW` | `0x6B30` | 244 | UnwindData |  |
| 25 | `DsGetDcOpenW` | `0x11420` | 40 | UnwindData |  |
| 16 | `DsEnumerateDomainTrustsW` | `0x11760` | 248 | UnwindData |  |
| 87 | `NlBindingAddServerToCache` | `0x11D90` | 373 | UnwindData |  |
| 75 | `I_RpcExtInitializeExtensionPoint` | `0x11F80` | 1,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `I_NetLogonSamLogonWithFlags` | `0x123D0` | 306 | UnwindData |  |
| 71 | `I_NetlogonComputeClientSignature` | `0x13520` | 133 | UnwindData |  |
| 68 | `I_NetServerReqChallenge` | `0x135E0` | 88 | UnwindData |  |
| 49 | `I_NetLogonGetDomainInfo` | `0x13BA0` | 171 | UnwindData |  |
| 74 | `I_NetlogonGetTrustRid` | `0x14360` | 70 | UnwindData |  |
| 84 | `NetLogonSetServiceBits` | `0x143B0` | 83 | UnwindData |  |
| 52 | `I_NetLogonSamLogonEx` | `0x14410` | 314 | UnwindData |  |
| 17 | `DsGetDcCloseW` | `0x14550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `I_NetServerAuthenticate3` | `0x14560` | 136 | UnwindData |  |
| 44 | `I_NetGetDCList` | `0x16160` | 264 | UnwindData |  |
| 9 | `DsAddressToSiteNamesA` | `0x164F0` | 577 | UnwindData |  |
| 10 | `DsAddressToSiteNamesExA` | `0x16740` | 913 | UnwindData |  |
| 11 | `DsAddressToSiteNamesExW` | `0x16AE0` | 625 | UnwindData |  |
| 12 | `DsAddressToSiteNamesW` | `0x16D60` | 373 | UnwindData |  |
| 22 | `DsGetDcNextA` | `0x16EE0` | 278 | UnwindData |  |
| 24 | `DsGetDcOpenA` | `0x17000` | 278 | UnwindData |  |
| 26 | `DsGetDcSiteCoverageA` | `0x17120` | 522 | UnwindData |  |
| 27 | `DsGetDcSiteCoverageW` | `0x17330` | 374 | UnwindData |  |
| 29 | `DsGetSiteNameA` | `0x174B0` | 158 | UnwindData |  |
| 32 | `DsValidateSubnetNameA` | `0x17560` | 77 | UnwindData |  |
| 33 | `DsValidateSubnetNameW` | `0x175C0` | 144 | UnwindData |  |
| 34 | `I_DsUpdateReadOnlyServerDnsRecords` | `0x17660` | 123 | UnwindData |  |
| 79 | `NetGetAnyDCName` | `0x176F0` | 74 | UnwindData |  |
| 90 | `NlSetDsIsCloningPDC` | `0x17740` | 2,528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `I_NetLogonSamLogoff` | `0x18120` | 124 | UnwindData |  |
| 51 | `I_NetLogonSamLogon` | `0x181B0` | 291 | UnwindData |  |
| 54 | `I_NetLogonSendToSam` | `0x182E0` | 111 | UnwindData |  |
| 55 | `I_NetLogonUasLogoff` | `0x18360` | 74 | UnwindData |  |
| 56 | `I_NetLogonUasLogon` | `0x183B0` | 76 | UnwindData |  |
| 88 | `NlBindingRemoveServerFromCache` | `0x186F0` | 91 | UnwindData |  |
| 89 | `NlBindingSetAuthInfo` | `0x18760` | 225 | UnwindData |  |
| 13 | `DsDeregisterDnsHostRecordsA` | `0x18D70` | 238 | UnwindData |  |
| 14 | `DsDeregisterDnsHostRecordsW` | `0x18E70` | 106 | UnwindData |  |
| 15 | `DsEnumerateDomainTrustsA` | `0x18EE0` | 1,106 | UnwindData |  |
| 28 | `DsGetForestTrustInformationW` | `0x19340` | 112 | UnwindData |  |
| 31 | `DsMergeForestTrustInformationW` | `0x193C0` | 94 | UnwindData |  |
| 35 | `I_NetAccountDeltas` | `0x19430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `I_NetAccountSync` | `0x19430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `I_NetDatabaseDeltas` | `0x19430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `I_NetDatabaseRedo` | `0x19430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `I_NetDatabaseSync` | `0x19430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `I_NetDatabaseSync2` | `0x19430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `I_NetChainSetClientAttributes` | `0x19440` | 147 | UnwindData |  |
| 38 | `I_NetChainSetClientAttributes2` | `0x194E0` | 147 | UnwindData |  |
| 43 | `I_NetExtendMachinePasswordExpirationTimeout` | `0x19580` | 60 | UnwindData |  |
| 45 | `I_NetGetForestTrustInformation` | `0x195D0` | 111 | UnwindData |  |
| 46 | `I_NetLogonControl` | `0x19650` | 100 | UnwindData |  |
| 47 | `I_NetLogonControl2` | `0x196C0` | 255 | UnwindData |  |
| 48 | `I_NetLogonGetCapabilities` | `0x197D0` | 111 | UnwindData |  |
| 57 | `I_NetQueryLocatorNameMappings` | `0x19850` | 69 | UnwindData |  |
| 58 | `I_NetQuerySecureChannelDCInfo` | `0x198A0` | 69 | UnwindData |  |
| 59 | `I_NetRequestLocatorNameMappingsUpdate` | `0x198F0` | 69 | UnwindData |  |
| 60 | `I_NetServerAuthenticate` | `0x19940` | 112 | UnwindData |  |
| 61 | `I_NetServerAuthenticate2` | `0x199C0` | 124 | UnwindData |  |
| 63 | `I_NetServerAuthenticateKerberos` | `0x19A50` | 167 | UnwindData |  |
| 64 | `I_NetServerGetTrustInfo` | `0x19B00` | 152 | UnwindData |  |
| 65 | `I_NetServerPasswordGet` | `0x19BA0` | 124 | UnwindData |  |
| 66 | `I_NetServerPasswordSet` | `0x19C30` | 124 | UnwindData |  |
| 67 | `I_NetServerPasswordSet2` | `0x19CC0` | 124 | UnwindData |  |
| 69 | `I_NetServerTrustPasswordsGet` | `0x19D50` | 136 | UnwindData |  |
| 70 | `I_NetlogonComputeClientDigest` | `0x19DE0` | 98 | UnwindData |  |
| 72 | `I_NetlogonComputeServerDigest` | `0x19E50` | 98 | UnwindData |  |
| 73 | `I_NetlogonComputeServerSignature` | `0x19EC0` | 133 | UnwindData |  |
| 78 | `NetEnumerateTrustedDomains` | `0x19F50` | 118 | UnwindData |  |
| 83 | `NetLogonGetTimeServiceParentDomain` | `0x19FD0` | 74 | UnwindData |  |
| 76 | `NetAddServiceAccount` | `0x1A2B0` | 88 | UnwindData |  |
| 77 | `NetEnumerateServiceAccounts` | `0x1A310` | 182 | UnwindData |  |
| 81 | `NetIsServiceAccount` | `0x1A3D0` | 95 | UnwindData |  |
| 82 | `NetIsServiceAccount2` | `0x1A440` | 119 | UnwindData |  |
| 85 | `NetQueryServiceAccount` | `0x1A4C0` | 142 | UnwindData |  |
| 86 | `NetRemoveServiceAccount` | `0x1A560` | 84 | UnwindData |  |
| 1 | `AuthzrExtAccessCheck` | `0x1EBB0` | 98 | UnwindData |  |
| 2 | `AuthzrExtFreeContext` | `0x1EC20` | 87 | UnwindData |  |
| 3 | `AuthzrExtFreeResourceManager` | `0x1EC80` | 27 | UnwindData |  |
| 4 | `AuthzrExtGetInformationFromContext` | `0x1ECB0` | 69 | UnwindData |  |
| 5 | `AuthzrExtInitializeCompoundContext` | `0x1ED00` | 109 | UnwindData |  |
| 6 | `AuthzrExtInitializeContextFromSid` | `0x1ED80` | 116 | UnwindData |  |
| 7 | `AuthzrExtInitializeRemoteResourceManager` | `0x1EE00` | 331 | UnwindData |  |
| 8 | `AuthzrExtModifyClaims` | `0x1EF60` | 85 | UnwindData |  |
