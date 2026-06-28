# Binary Specification: wintrust.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wintrust.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4071778b4487d4b5ad2bbc3578eebada6e2e81a371cdf290c1090130b7c7171e`
* **Total Exported Functions:** 165

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 17 | `CryptCATAdminAcquireContext` | `0x1C80` | 26 | UnwindData |  |
| 39 | `CryptCATClose` | `0x23F0` | 1,329 | UnwindData |  |
| 26 | `CryptCATAdminReleaseContext` | `0x3520` | 272 | UnwindData |  |
| 18 | `CryptCATAdminAcquireContext2` | `0x36C0` | 40 | UnwindData |  |
| 23 | `CryptCATAdminEnumCatalogFromHash` | `0x4780` | 2,383 | UnwindData |  |
| 20 | `CryptCATAdminCalcHashFromFileHandle` | `0x9050` | 88 | UnwindData |  |
| 25 | `CryptCATAdminReleaseCatalogContext` | `0x91D0` | 185 | UnwindData |  |
| 48 | `CryptCATOpen` | `0x9430` | 405 | UnwindData |  |
| 29 | `CryptCATAllocSortedMemberInfo` | `0x95D0` | 201 | UnwindData |  |
| 43 | `CryptCATFreeSortedMemberInfo` | `0xA960` | 56 | UnwindData |  |
| 148 | `WinVerifyTrust` | `0xB400` | 137 | UnwindData |  |
| 38 | `CryptCATCatalogInfoFromContext` | `0xCBC0` | 244 | UnwindData |  |
| 95 | `WTGetSignatureInfo` | `0xCCC0` | 41 | UnwindData |  |
| 93 | `WTGetBioSignatureInfo` | `0xDC00` | 421 | UnwindData |  |
| 117 | `WTValidateBioSignaturePolicy` | `0xE2E0` | 184 | UnwindData |  |
| 70 | `MsCatConstructHashTag` | `0xEBC0` | 60 | UnwindData |  |
| 122 | `WVTAsn1CatNameValueDecode` | `0xEDB0` | 8 | UnwindData |  |
| 140 | `WVTAsn1SpcSigInfoDecode` | `0xF0B0` | 171 | UnwindData |  |
| 134 | `WVTAsn1SpcLinkDecode` | `0xF170` | 215 | UnwindData |  |
| 120 | `WVTAsn1CatMemberInfoDecode` | `0xF250` | 288 | UnwindData |  |
| 144 | `WVTAsn1SpcSpOpusInfoDecode` | `0xF380` | 487 | UnwindData |  |
| 138 | `WVTAsn1SpcPeImageDataDecode` | `0xFA40` | 920 | UnwindData |  |
| 54 | `CryptSIPCreateIndirectData` | `0xFEC0` | 171 | UnwindData |  |
| 60 | `CryptSIPVerifyIndirectData` | `0xFF80` | 283 | UnwindData |  |
| 55 | `CryptSIPGetCaps` | `0x100B0` | 125 | UnwindData |  |
| 57 | `CryptSIPGetSignedDataMsg` | `0x10140` | 73 | UnwindData |  |
| 156 | `WintrustGetRegPolicyFlags` | `0x108B0` | 277 | UnwindData |  |
| 44 | `CryptCATGetAttrInfo` | `0x11840` | 231 | UnwindData |  |
| 42 | `CryptCATEnumerateMember` | `0x11930` | 222 | UnwindData |  |
| 40 | `CryptCATEnumerateAttr` | `0x11A20` | 104 | UnwindData |  |
| 83 | `SoftpubLoadMessage` | `0x11E10` | 52 | UnwindData |  |
| 86 | `TrustDecode` | `0x13DD0` | 231 | UnwindData |  |
| 84 | `SoftpubLoadSignature` | `0x14790` | 298 | UnwindData |  |
| 110 | `WTHelperOpenKnownStores` | `0x16020` | 421 | UnwindData |  |
| 65 | `DriverInitializePolicy` | `0x16350` | 610 | UnwindData |  |
| 157 | `WintrustLoadFunctionPointers` | `0x16650` | 207 | UnwindData |  |
| 90 | `TrustOpenStores` | `0x168C0` | 357 | UnwindData |  |
| 7 | `HTTPSCertificateTrust` | `0x1BE30` | 780 | UnwindData |  |
| 41 | `CryptCATEnumerateCatAttr` | `0x1D790` | 76 | UnwindData |  |
| 45 | `CryptCATGetCatAttrInfo` | `0x1D990` | 67 | UnwindData |  |
| 46 | `CryptCATGetMemberInfo` | `0x1DC20` | 192 | UnwindData |  |
| 5 | `GenericChainCertificateTrust` | `0x1DE90` | 457 | UnwindData |  |
| 68 | `HTTPSFinalProv` | `0x1E060` | 217 | UnwindData |  |
| 76 | `SoftpubAuthenticode` | `0x1E1A0` | 35 | UnwindData |  |
| 104 | `WTHelperGetProvCertFromChain` | `0x1EEA0` | 1,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `WVTAsn1SpcIndirectDataContentDecode` | `0x1F2A0` | 1,461 | UnwindData |  |
| 139 | `WVTAsn1SpcPeImageDataEncode` | `0x1F860` | 463 | UnwindData |  |
| 135 | `WVTAsn1SpcLinkEncode` | `0x1FA40` | 370 | UnwindData |  |
| 82 | `SoftpubInitialize` | `0x22230` | 32 | UnwindData |  |
| 106 | `WTHelperGetProvSignerFromChain` | `0x22440` | 2,992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `SoftpubCleanup` | `0x22FF0` | 186 | UnwindData |  |
| 88 | `TrustFreeDecode` | `0x23F50` | 38 | UnwindData |  |
| 105 | `WTHelperGetProvPrivateDataFromChain` | `0x24050` | 720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `WTHelperGetFileName` | `0x24320` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `WVTAsn1CatMemberInfo2Decode` | `0x244D0` | 395 | UnwindData |  |
| 100 | `WTHelperGetFileHandle` | `0x24A00` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `DriverCleanupPolicy` | `0x24AC0` | 249 | UnwindData |  |
| 77 | `SoftpubCheckCert` | `0x25B40` | 3,216 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `CryptCATAdminCalcHashFromFileHandle2` | `0x267D0` | 120 | UnwindData |  |
| 14 | `CatalogCompactHashDatabase` | `0x274A0` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `MsCatFreeHashTag` | `0x277A0` | 2,384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `CryptCATAdminAddCatalog` | `0x280F0` | 844 | UnwindData |  |
| 69 | `IsCatalogFile` | `0x28680` | 597 | UnwindData |  |
| 47 | `CryptCATHandleFromStore` | `0x28C70` | 3,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `CryptCATStoreFromHandle` | `0x28C70` | 3,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `WTHelperProvDataFromStateData` | `0x28C70` | 3,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `GenericChainFinalProv` | `0x29980` | 690 | UnwindData |  |
| 149 | `WinVerifyTrustEx` | `0x29CA0` | 1,232 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `GetAuthenticodeSha256Hash` | `0x2A170` | 541 | UnwindData |  |
| 27 | `CryptCATAdminRemoveCatalog` | `0x2A3A0` | 69 | UnwindData |  |
| 101 | `WTHelperGetFileHash` | `0x2A620` | 221 | UnwindData |  |
| 22 | `CryptCATAdminCalcHashFromFileHandle3` | `0x2A710` | 93 | UnwindData |  |
| 162 | `mscat32DllRegisterServer` | `0x2A900` | 2,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 163 | `mscat32DllUnregisterServer` | `0x2A900` | 2,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `WTLogConfigCiScriptEvent` | `0x2B2D0` | 99 | UnwindData |  |
| 114 | `WTLogConfigCiScriptEvent2` | `0x2B340` | 3,127 | UnwindData |  |
| 112 | `WTIsFirstConfigCiResultPreferred` | `0x2BF80` | 3,664 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `WTHelperCertIsSelfSigned` | `0x2CDD0` | 441 | UnwindData |  |
| 153 | `WintrustCertificateTrust` | `0x2D870` | 80 | UnwindData |  |
| 15 | `ConfigCiFinalPolicy` | `0x2DED0` | 2,161 | UnwindData |  |
| 16 | `ConfigCiPackageFamilyNameCheck` | `0x2E750` | 614 | UnwindData |  |
| 64 | `DriverFinalPolicy` | `0x2E9C0` | 1,361 | UnwindData |  |
| 141 | `WVTAsn1SpcSigInfoEncode` | `0x327B0` | 105 | UnwindData |  |
| 4 | `CryptSIPGetRegWorkingFlags` | `0x33760` | 21,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `WTHelperCertFindIssuerCertificate` | `0x38AD0` | 58 | UnwindData |  |
| 61 | `DllRegisterServer` | `0x3CF70` | 69 | UnwindData |  |
| 62 | `DllUnregisterServer` | `0x3CFC0` | 69 | UnwindData |  |
| 119 | `WVTAsn1CatMemberInfo2Encode` | `0x3D350` | 178 | UnwindData |  |
| 121 | `WVTAsn1CatMemberInfoEncode` | `0x3D410` | 79 | UnwindData |  |
| 123 | `WVTAsn1CatNameValueEncode` | `0x3D470` | 102 | UnwindData |  |
| 124 | `WVTAsn1IntentToSealAttributeDecode` | `0x3D4E0` | 158 | UnwindData |  |
| 125 | `WVTAsn1IntentToSealAttributeEncode` | `0x3D590` | 57 | UnwindData |  |
| 126 | `WVTAsn1SealingSignatureAttributeDecode` | `0x3D5D0` | 215 | UnwindData |  |
| 127 | `WVTAsn1SealingSignatureAttributeEncode` | `0x3D6B0` | 184 | UnwindData |  |
| 128 | `WVTAsn1SealingTimestampAttributeDecode` | `0x3D770` | 273 | UnwindData |  |
| 129 | `WVTAsn1SealingTimestampAttributeEncode` | `0x3D890` | 85 | UnwindData |  |
| 130 | `WVTAsn1SpcFinancialCriteriaInfoDecode` | `0x3D8F0` | 172 | UnwindData |  |
| 131 | `WVTAsn1SpcFinancialCriteriaInfoEncode` | `0x3D9B0` | 51 | UnwindData |  |
| 133 | `WVTAsn1SpcIndirectDataContentEncode` | `0x3D9F0` | 219 | UnwindData |  |
| 136 | `WVTAsn1SpcMinimalCriteriaInfoDecode` | `0x3DAE0` | 172 | UnwindData |  |
| 137 | `WVTAsn1SpcMinimalCriteriaInfoEncode` | `0x3DBA0` | 43 | UnwindData |  |
| 142 | `WVTAsn1SpcSpAgencyInfoDecode` | `0x3DBE0` | 642 | UnwindData |  |
| 143 | `WVTAsn1SpcSpAgencyInfoEncode` | `0x3DE70` | 455 | UnwindData |  |
| 145 | `WVTAsn1SpcSpOpusInfoEncode` | `0x3E040` | 225 | UnwindData |  |
| 146 | `WVTAsn1SpcStatementTypeDecode` | `0x3E130` | 298 | UnwindData |  |
| 147 | `WVTAsn1SpcStatementTypeEncode` | `0x3E260` | 189 | UnwindData |  |
| 150 | `WintrustAddActionID` | `0x3E360` | 464 | UnwindData |  |
| 158 | `WintrustRemoveActionID` | `0x3E540` | 138 | UnwindData |  |
| 152 | `WintrustAddProviderToProcess` | `0x3E5D0` | 220 | UnwindData |  |
| 160 | `WintrustSetRegPolicyFlags` | `0x3E7D0` | 140 | UnwindData |  |
| 87 | `TrustFindIssuerCertificate` | `0x3F140` | 478 | UnwindData |  |
| 89 | `TrustIsCertificateSelfSigned` | `0x3F330` | 123 | UnwindData |  |
| 151 | `WintrustAddDefaultForUsage` | `0x3F3C0` | 693 | UnwindData |  |
| 154 | `WintrustGetDefaultForUsage` | `0x3F680` | 768 | UnwindData |  |
| 96 | `WTHelperCertCheckValidSignature` | `0x41260` | 27 | UnwindData |  |
| 98 | `WTHelperCheckCertUsage` | `0x41290` | 347 | UnwindData |  |
| 99 | `WTHelperGetAgencyInfo` | `0x41400` | 242 | UnwindData |  |
| 103 | `WTHelperGetKnownUsages` | `0x41500` | 157 | UnwindData |  |
| 107 | `WTHelperIsChainedToMicrosoft` | `0x415B0` | 408 | UnwindData |  |
| 108 | `WTHelperIsChainedToMicrosoftFromStateData` | `0x41750` | 207 | UnwindData |  |
| 109 | `WTHelperIsInRootStore` | `0x41830` | 265 | UnwindData |  |
| 1 | `ComputeFirstPageHash` | `0x41DA0` | 661 | UnwindData |  |
| 2 | `CryptCATVerifyMember` | `0x42980` | 64 | UnwindData |  |
| 49 | `CryptCATPersistStore` | `0x429D0` | 55 | UnwindData |  |
| 50 | `CryptCATPutAttrInfo` | `0x42A10` | 467 | UnwindData |  |
| 51 | `CryptCATPutCatAttrInfo` | `0x42BF0` | 610 | UnwindData |  |
| 52 | `CryptCATPutMemberInfo` | `0x42E60` | 375 | UnwindData |  |
| 24 | `CryptCATAdminPauseServiceForBackup` | `0x43210` | 64 | UnwindData |  |
| 28 | `CryptCATAdminResolveCatalogPath` | `0x43260` | 278 | UnwindData |  |
| 30 | `CryptCATCDFClose` | `0x44A80` | 159 | UnwindData |  |
| 31 | `CryptCATCDFEnumAttributes` | `0x44B30` | 24 | UnwindData |  |
| 32 | `CryptCATCDFEnumAttributesWithCDFTag` | `0x44B50` | 61 | UnwindData |  |
| 33 | `CryptCATCDFEnumCatAttributes` | `0x44BA0` | 267 | UnwindData |  |
| 34 | `CryptCATCDFEnumMembers` | `0x44CC0` | 97 | UnwindData |  |
| 35 | `CryptCATCDFEnumMembersByCDFTag` | `0x44D30` | 26 | UnwindData |  |
| 36 | `CryptCATCDFEnumMembersByCDFTagEx` | `0x44D50` | 67 | UnwindData |  |
| 37 | `CryptCATCDFOpen` | `0x44DA0` | 1,436 | UnwindData |  |
| 3 | `CryptSIPGetInfo` | `0x462A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `CryptSIPGetSealedDigest` | `0x462E0` | 178 | UnwindData |  |
| 58 | `CryptSIPPutSignedDataMsg` | `0x463A0` | 199 | UnwindData |  |
| 59 | `CryptSIPRemoveSignedDataMsg` | `0x46470` | 137 | UnwindData |  |
| 164 | `mssip32DllRegisterServer` | `0x46500` | 691 | UnwindData |  |
| 165 | `mssip32DllUnregisterServer` | `0x467C0` | 404 | UnwindData |  |
| 159 | `WintrustSetDefaultIncludePEPageHashes` | `0x47840` | 4,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `WTGetPluginSignatureInfo` | `0x48990` | 349 | UnwindData |  |
| 72 | `OfficeCleanupPolicy` | `0x496B0` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `OfficeInitializePolicy` | `0x496B0` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `SetMessageDigestInfo` | `0x496B0` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `SoftpubDefCertInit` | `0x49960` | 240 | UnwindData |  |
| 10 | `SoftpubFreeDefUsageCallData` | `0x49A60` | 72 | UnwindData |  |
| 11 | `SoftpubLoadDefUsageCallData` | `0x49AB0` | 315 | UnwindData |  |
| 13 | `AddPersonalTrustDBPages` | `0x49C00` | 29 | UnwindData |  |
| 74 | `OpenPersonalTrustDBDialog` | `0x49C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `OpenPersonalTrustDBDialogEx` | `0x49C40` | 276 | UnwindData |  |
| 91 | `WTConfigCiFreePrivateData` | `0x4EBB0` | 128 | UnwindData |  |
| 92 | `WTConvertCertCtxToChainInfo` | `0x4EC40` | 128 | UnwindData |  |
| 115 | `WTLogConfigCiSignerEvent` | `0x4ECD0` | 648 | UnwindData |  |
| 116 | `WTLogSmartAppControlDefenderInfo` | `0x4EF60` | 455 | UnwindData |  |
| 155 | `WintrustGetHash` | `0x4F130` | 187 | UnwindData |  |
| 161 | `WintrustUserWriteabilityCheck` | `0x4F200` | 84 | UnwindData |  |
| 66 | `FindCertsByIssuer` | `0x50300` | 1,023 | UnwindData |  |
| 79 | `SoftpubDllRegisterServer` | `0x50A70` | 626 | UnwindData |  |
| 80 | `SoftpubDllUnregisterServer` | `0x50CF0` | 367 | UnwindData |  |
| 81 | `SoftpubDumpStructure` | `0x518E0` | 2,407 | UnwindData |  |
| 85 | `SrpCheckSmartlockerEAandProcessToken` | `0x52630` | 27,548 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
