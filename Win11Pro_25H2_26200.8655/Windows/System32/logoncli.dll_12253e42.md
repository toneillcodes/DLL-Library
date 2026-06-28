# Binary Specification: logoncli.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\logoncli.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `12253e42f93d9c2a941ad3b35fda9cdfcb2f24f54c1d40bd5da12d70a7194ad6`
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
| 25 | `DsGetDcOpenW` | `0x10F90` | 40 | UnwindData |  |
| 16 | `DsEnumerateDomainTrustsW` | `0x112D0` | 248 | UnwindData |  |
| 87 | `NlBindingAddServerToCache` | `0x11900` | 373 | UnwindData |  |
| 75 | `I_RpcExtInitializeExtensionPoint` | `0x11AF0` | 2,640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `I_NetLogonSamLogonWithFlags` | `0x12540` | 306 | UnwindData |  |
| 71 | `I_NetlogonComputeClientSignature` | `0x13690` | 133 | UnwindData |  |
| 68 | `I_NetServerReqChallenge` | `0x13750` | 88 | UnwindData |  |
| 49 | `I_NetLogonGetDomainInfo` | `0x13D10` | 171 | UnwindData |  |
| 74 | `I_NetlogonGetTrustRid` | `0x144D0` | 70 | UnwindData |  |
| 84 | `NetLogonSetServiceBits` | `0x14520` | 83 | UnwindData |  |
| 52 | `I_NetLogonSamLogonEx` | `0x14580` | 314 | UnwindData |  |
| 17 | `DsGetDcCloseW` | `0x146C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `I_NetServerAuthenticate3` | `0x146D0` | 136 | UnwindData |  |
| 44 | `I_NetGetDCList` | `0x162D0` | 264 | UnwindData |  |
| 9 | `DsAddressToSiteNamesA` | `0x16660` | 577 | UnwindData |  |
| 10 | `DsAddressToSiteNamesExA` | `0x168B0` | 913 | UnwindData |  |
| 11 | `DsAddressToSiteNamesExW` | `0x16C50` | 625 | UnwindData |  |
| 12 | `DsAddressToSiteNamesW` | `0x16ED0` | 373 | UnwindData |  |
| 22 | `DsGetDcNextA` | `0x17050` | 278 | UnwindData |  |
| 24 | `DsGetDcOpenA` | `0x17170` | 278 | UnwindData |  |
| 26 | `DsGetDcSiteCoverageA` | `0x17290` | 522 | UnwindData |  |
| 27 | `DsGetDcSiteCoverageW` | `0x174A0` | 374 | UnwindData |  |
| 29 | `DsGetSiteNameA` | `0x17620` | 158 | UnwindData |  |
| 32 | `DsValidateSubnetNameA` | `0x176D0` | 77 | UnwindData |  |
| 33 | `DsValidateSubnetNameW` | `0x17730` | 144 | UnwindData |  |
| 34 | `I_DsUpdateReadOnlyServerDnsRecords` | `0x177D0` | 123 | UnwindData |  |
| 79 | `NetGetAnyDCName` | `0x17860` | 74 | UnwindData |  |
| 90 | `NlSetDsIsCloningPDC` | `0x178B0` | 2,528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `I_NetLogonSamLogoff` | `0x18290` | 124 | UnwindData |  |
| 51 | `I_NetLogonSamLogon` | `0x18320` | 291 | UnwindData |  |
| 54 | `I_NetLogonSendToSam` | `0x18450` | 111 | UnwindData |  |
| 55 | `I_NetLogonUasLogoff` | `0x184D0` | 74 | UnwindData |  |
| 56 | `I_NetLogonUasLogon` | `0x18520` | 76 | UnwindData |  |
| 88 | `NlBindingRemoveServerFromCache` | `0x18870` | 91 | UnwindData |  |
| 89 | `NlBindingSetAuthInfo` | `0x188E0` | 225 | UnwindData |  |
| 13 | `DsDeregisterDnsHostRecordsA` | `0x193D0` | 238 | UnwindData |  |
| 14 | `DsDeregisterDnsHostRecordsW` | `0x194D0` | 106 | UnwindData |  |
| 15 | `DsEnumerateDomainTrustsA` | `0x19540` | 1,106 | UnwindData |  |
| 28 | `DsGetForestTrustInformationW` | `0x199A0` | 112 | UnwindData |  |
| 31 | `DsMergeForestTrustInformationW` | `0x19A20` | 94 | UnwindData |  |
| 35 | `I_NetAccountDeltas` | `0x19A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `I_NetAccountSync` | `0x19A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `I_NetDatabaseDeltas` | `0x19A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `I_NetDatabaseRedo` | `0x19A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `I_NetDatabaseSync` | `0x19A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `I_NetDatabaseSync2` | `0x19A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `I_NetChainSetClientAttributes` | `0x19AA0` | 147 | UnwindData |  |
| 38 | `I_NetChainSetClientAttributes2` | `0x19B40` | 147 | UnwindData |  |
| 43 | `I_NetExtendMachinePasswordExpirationTimeout` | `0x19BE0` | 60 | UnwindData |  |
| 45 | `I_NetGetForestTrustInformation` | `0x19C30` | 111 | UnwindData |  |
| 46 | `I_NetLogonControl` | `0x19CB0` | 100 | UnwindData |  |
| 47 | `I_NetLogonControl2` | `0x19D20` | 255 | UnwindData |  |
| 48 | `I_NetLogonGetCapabilities` | `0x19E30` | 111 | UnwindData |  |
| 57 | `I_NetQueryLocatorNameMappings` | `0x19EB0` | 69 | UnwindData |  |
| 58 | `I_NetQuerySecureChannelDCInfo` | `0x19F00` | 69 | UnwindData |  |
| 59 | `I_NetRequestLocatorNameMappingsUpdate` | `0x19F50` | 69 | UnwindData |  |
| 60 | `I_NetServerAuthenticate` | `0x19FA0` | 112 | UnwindData |  |
| 61 | `I_NetServerAuthenticate2` | `0x1A020` | 124 | UnwindData |  |
| 63 | `I_NetServerAuthenticateKerberos` | `0x1A0B0` | 167 | UnwindData |  |
| 64 | `I_NetServerGetTrustInfo` | `0x1A160` | 152 | UnwindData |  |
| 65 | `I_NetServerPasswordGet` | `0x1A200` | 124 | UnwindData |  |
| 66 | `I_NetServerPasswordSet` | `0x1A290` | 124 | UnwindData |  |
| 67 | `I_NetServerPasswordSet2` | `0x1A320` | 124 | UnwindData |  |
| 69 | `I_NetServerTrustPasswordsGet` | `0x1A3B0` | 136 | UnwindData |  |
| 70 | `I_NetlogonComputeClientDigest` | `0x1A440` | 98 | UnwindData |  |
| 72 | `I_NetlogonComputeServerDigest` | `0x1A4B0` | 98 | UnwindData |  |
| 73 | `I_NetlogonComputeServerSignature` | `0x1A520` | 133 | UnwindData |  |
| 78 | `NetEnumerateTrustedDomains` | `0x1A5B0` | 118 | UnwindData |  |
| 83 | `NetLogonGetTimeServiceParentDomain` | `0x1A630` | 74 | UnwindData |  |
| 76 | `NetAddServiceAccount` | `0x1A910` | 88 | UnwindData |  |
| 77 | `NetEnumerateServiceAccounts` | `0x1A970` | 182 | UnwindData |  |
| 81 | `NetIsServiceAccount` | `0x1AA30` | 95 | UnwindData |  |
| 82 | `NetIsServiceAccount2` | `0x1AAA0` | 119 | UnwindData |  |
| 85 | `NetQueryServiceAccount` | `0x1AB20` | 142 | UnwindData |  |
| 86 | `NetRemoveServiceAccount` | `0x1ABC0` | 84 | UnwindData |  |
| 1 | `AuthzrExtAccessCheck` | `0x1F260` | 98 | UnwindData |  |
| 2 | `AuthzrExtFreeContext` | `0x1F2D0` | 87 | UnwindData |  |
| 3 | `AuthzrExtFreeResourceManager` | `0x1F330` | 27 | UnwindData |  |
| 4 | `AuthzrExtGetInformationFromContext` | `0x1F360` | 69 | UnwindData |  |
| 5 | `AuthzrExtInitializeCompoundContext` | `0x1F3B0` | 109 | UnwindData |  |
| 6 | `AuthzrExtInitializeContextFromSid` | `0x1F430` | 116 | UnwindData |  |
| 7 | `AuthzrExtInitializeRemoteResourceManager` | `0x1F4B0` | 331 | UnwindData |  |
| 8 | `AuthzrExtModifyClaims` | `0x1F610` | 85 | UnwindData |  |
