# Binary Specification: wintrust.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wintrust.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1a42f52dc63d80013c49f9ac78773346c28519817e6966ab5a75696d4908388a`
* **Total Exported Functions:** 165

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 17 | `CryptCATAdminAcquireContext` | `0x1C10` | 26 | UnwindData |  |
| 39 | `CryptCATClose` | `0x2380` | 1,329 | UnwindData |  |
| 26 | `CryptCATAdminReleaseContext` | `0x34B0` | 272 | UnwindData |  |
| 18 | `CryptCATAdminAcquireContext2` | `0x3650` | 40 | UnwindData |  |
| 23 | `CryptCATAdminEnumCatalogFromHash` | `0x4710` | 2,383 | UnwindData |  |
| 20 | `CryptCATAdminCalcHashFromFileHandle` | `0x8FE0` | 88 | UnwindData |  |
| 25 | `CryptCATAdminReleaseCatalogContext` | `0x9160` | 185 | UnwindData |  |
| 48 | `CryptCATOpen` | `0x93C0` | 405 | UnwindData |  |
| 29 | `CryptCATAllocSortedMemberInfo` | `0x9560` | 201 | UnwindData |  |
| 43 | `CryptCATFreeSortedMemberInfo` | `0xA8F0` | 56 | UnwindData |  |
| 148 | `WinVerifyTrust` | `0xB390` | 137 | UnwindData |  |
| 38 | `CryptCATCatalogInfoFromContext` | `0xCAC0` | 244 | UnwindData |  |
| 95 | `WTGetSignatureInfo` | `0xCBC0` | 41 | UnwindData |  |
| 93 | `WTGetBioSignatureInfo` | `0xDB00` | 421 | UnwindData |  |
| 117 | `WTValidateBioSignaturePolicy` | `0xE1E0` | 184 | UnwindData |  |
| 70 | `MsCatConstructHashTag` | `0xEAC0` | 60 | UnwindData |  |
| 122 | `WVTAsn1CatNameValueDecode` | `0xECB0` | 8 | UnwindData |  |
| 140 | `WVTAsn1SpcSigInfoDecode` | `0xEFB0` | 171 | UnwindData |  |
| 134 | `WVTAsn1SpcLinkDecode` | `0xF070` | 215 | UnwindData |  |
| 120 | `WVTAsn1CatMemberInfoDecode` | `0xF150` | 288 | UnwindData |  |
| 144 | `WVTAsn1SpcSpOpusInfoDecode` | `0xF280` | 487 | UnwindData |  |
| 138 | `WVTAsn1SpcPeImageDataDecode` | `0xF940` | 920 | UnwindData |  |
| 54 | `CryptSIPCreateIndirectData` | `0xFDC0` | 171 | UnwindData |  |
| 60 | `CryptSIPVerifyIndirectData` | `0xFE80` | 283 | UnwindData |  |
| 55 | `CryptSIPGetCaps` | `0xFFB0` | 125 | UnwindData |  |
| 57 | `CryptSIPGetSignedDataMsg` | `0x10040` | 73 | UnwindData |  |
| 156 | `WintrustGetRegPolicyFlags` | `0x107B0` | 277 | UnwindData |  |
| 44 | `CryptCATGetAttrInfo` | `0x11740` | 231 | UnwindData |  |
| 42 | `CryptCATEnumerateMember` | `0x11830` | 222 | UnwindData |  |
| 40 | `CryptCATEnumerateAttr` | `0x11920` | 104 | UnwindData |  |
| 83 | `SoftpubLoadMessage` | `0x11D10` | 52 | UnwindData |  |
| 86 | `TrustDecode` | `0x13CD0` | 231 | UnwindData |  |
| 84 | `SoftpubLoadSignature` | `0x14690` | 298 | UnwindData |  |
| 110 | `WTHelperOpenKnownStores` | `0x15F20` | 421 | UnwindData |  |
| 65 | `DriverInitializePolicy` | `0x16250` | 610 | UnwindData |  |
| 157 | `WintrustLoadFunctionPointers` | `0x16550` | 207 | UnwindData |  |
| 90 | `TrustOpenStores` | `0x167C0` | 357 | UnwindData |  |
| 7 | `HTTPSCertificateTrust` | `0x1BD30` | 780 | UnwindData |  |
| 41 | `CryptCATEnumerateCatAttr` | `0x1D690` | 76 | UnwindData |  |
| 45 | `CryptCATGetCatAttrInfo` | `0x1D890` | 67 | UnwindData |  |
| 46 | `CryptCATGetMemberInfo` | `0x1DB20` | 192 | UnwindData |  |
| 5 | `GenericChainCertificateTrust` | `0x1DD90` | 457 | UnwindData |  |
| 68 | `HTTPSFinalProv` | `0x1DF60` | 217 | UnwindData |  |
| 76 | `SoftpubAuthenticode` | `0x1E0A0` | 35 | UnwindData |  |
| 104 | `WTHelperGetProvCertFromChain` | `0x1EDA0` | 1,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `WVTAsn1SpcIndirectDataContentDecode` | `0x1F1A0` | 1,461 | UnwindData |  |
| 139 | `WVTAsn1SpcPeImageDataEncode` | `0x1F760` | 463 | UnwindData |  |
| 135 | `WVTAsn1SpcLinkEncode` | `0x1F940` | 370 | UnwindData |  |
| 82 | `SoftpubInitialize` | `0x218B0` | 32 | UnwindData |  |
| 106 | `WTHelperGetProvSignerFromChain` | `0x21AC0` | 2,992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `SoftpubCleanup` | `0x22670` | 186 | UnwindData |  |
| 88 | `TrustFreeDecode` | `0x235D0` | 38 | UnwindData |  |
| 105 | `WTHelperGetProvPrivateDataFromChain` | `0x236D0` | 720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `WTHelperGetFileName` | `0x239A0` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `WVTAsn1CatMemberInfo2Decode` | `0x23B50` | 395 | UnwindData |  |
| 100 | `WTHelperGetFileHandle` | `0x24080` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `DriverCleanupPolicy` | `0x24140` | 249 | UnwindData |  |
| 77 | `SoftpubCheckCert` | `0x251C0` | 3,216 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `CryptCATAdminCalcHashFromFileHandle2` | `0x25E50` | 120 | UnwindData |  |
| 14 | `CatalogCompactHashDatabase` | `0x26500` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `MsCatFreeHashTag` | `0x26800` | 3,872 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `CryptCATAdminAddCatalog` | `0x27720` | 844 | UnwindData |  |
| 69 | `IsCatalogFile` | `0x27CB0` | 597 | UnwindData |  |
| 47 | `CryptCATHandleFromStore` | `0x285A0` | 3,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `CryptCATStoreFromHandle` | `0x285A0` | 3,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `WTHelperProvDataFromStateData` | `0x285A0` | 3,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `GenericChainFinalProv` | `0x29490` | 690 | UnwindData |  |
| 149 | `WinVerifyTrustEx` | `0x297B0` | 1,552 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `GetAuthenticodeSha256Hash` | `0x29DC0` | 541 | UnwindData |  |
| 27 | `CryptCATAdminRemoveCatalog` | `0x29FF0` | 69 | UnwindData |  |
| 101 | `WTHelperGetFileHash` | `0x2A270` | 221 | UnwindData |  |
| 22 | `CryptCATAdminCalcHashFromFileHandle3` | `0x2A360` | 93 | UnwindData |  |
| 162 | `mscat32DllRegisterServer` | `0x2A610` | 2,576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 163 | `mscat32DllUnregisterServer` | `0x2A610` | 2,576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `WTLogConfigCiScriptEvent` | `0x2B020` | 99 | UnwindData |  |
| 114 | `WTLogConfigCiScriptEvent2` | `0x2B090` | 3,127 | UnwindData |  |
| 112 | `WTIsFirstConfigCiResultPreferred` | `0x2BCD0` | 4,032 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `WTHelperCertIsSelfSigned` | `0x2CC90` | 441 | UnwindData |  |
| 153 | `WintrustCertificateTrust` | `0x2D850` | 80 | UnwindData |  |
| 15 | `ConfigCiFinalPolicy` | `0x2DEB0` | 2,368 | UnwindData |  |
| 16 | `ConfigCiPackageFamilyNameCheck` | `0x2E800` | 963 | UnwindData |  |
| 64 | `DriverFinalPolicy` | `0x2EBD0` | 1,361 | UnwindData |  |
| 141 | `WVTAsn1SpcSigInfoEncode` | `0x32AC0` | 105 | UnwindData |  |
| 4 | `CryptSIPGetRegWorkingFlags` | `0x33AF0` | 21,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `WTHelperCertFindIssuerCertificate` | `0x38E60` | 58 | UnwindData |  |
| 61 | `DllRegisterServer` | `0x3D4E0` | 69 | UnwindData |  |
| 62 | `DllUnregisterServer` | `0x3D530` | 69 | UnwindData |  |
| 119 | `WVTAsn1CatMemberInfo2Encode` | `0x3D8C0` | 178 | UnwindData |  |
| 121 | `WVTAsn1CatMemberInfoEncode` | `0x3D980` | 79 | UnwindData |  |
| 123 | `WVTAsn1CatNameValueEncode` | `0x3D9E0` | 102 | UnwindData |  |
| 124 | `WVTAsn1IntentToSealAttributeDecode` | `0x3DA50` | 158 | UnwindData |  |
| 125 | `WVTAsn1IntentToSealAttributeEncode` | `0x3DB00` | 57 | UnwindData |  |
| 126 | `WVTAsn1SealingSignatureAttributeDecode` | `0x3DB40` | 215 | UnwindData |  |
| 127 | `WVTAsn1SealingSignatureAttributeEncode` | `0x3DC20` | 184 | UnwindData |  |
| 128 | `WVTAsn1SealingTimestampAttributeDecode` | `0x3DCE0` | 273 | UnwindData |  |
| 129 | `WVTAsn1SealingTimestampAttributeEncode` | `0x3DE00` | 85 | UnwindData |  |
| 130 | `WVTAsn1SpcFinancialCriteriaInfoDecode` | `0x3DE60` | 172 | UnwindData |  |
| 131 | `WVTAsn1SpcFinancialCriteriaInfoEncode` | `0x3DF20` | 51 | UnwindData |  |
| 133 | `WVTAsn1SpcIndirectDataContentEncode` | `0x3DF60` | 219 | UnwindData |  |
| 136 | `WVTAsn1SpcMinimalCriteriaInfoDecode` | `0x3E050` | 172 | UnwindData |  |
| 137 | `WVTAsn1SpcMinimalCriteriaInfoEncode` | `0x3E110` | 43 | UnwindData |  |
| 142 | `WVTAsn1SpcSpAgencyInfoDecode` | `0x3E150` | 642 | UnwindData |  |
| 143 | `WVTAsn1SpcSpAgencyInfoEncode` | `0x3E3E0` | 455 | UnwindData |  |
| 145 | `WVTAsn1SpcSpOpusInfoEncode` | `0x3E5B0` | 225 | UnwindData |  |
| 146 | `WVTAsn1SpcStatementTypeDecode` | `0x3E6A0` | 298 | UnwindData |  |
| 147 | `WVTAsn1SpcStatementTypeEncode` | `0x3E7D0` | 189 | UnwindData |  |
| 150 | `WintrustAddActionID` | `0x3E8D0` | 464 | UnwindData |  |
| 158 | `WintrustRemoveActionID` | `0x3EAB0` | 138 | UnwindData |  |
| 152 | `WintrustAddProviderToProcess` | `0x3EB40` | 220 | UnwindData |  |
| 160 | `WintrustSetRegPolicyFlags` | `0x3ED40` | 140 | UnwindData |  |
| 87 | `TrustFindIssuerCertificate` | `0x3F6B0` | 478 | UnwindData |  |
| 89 | `TrustIsCertificateSelfSigned` | `0x3F8A0` | 123 | UnwindData |  |
| 151 | `WintrustAddDefaultForUsage` | `0x3F930` | 693 | UnwindData |  |
| 154 | `WintrustGetDefaultForUsage` | `0x3FBF0` | 768 | UnwindData |  |
| 96 | `WTHelperCertCheckValidSignature` | `0x410B0` | 27 | UnwindData |  |
| 98 | `WTHelperCheckCertUsage` | `0x410E0` | 347 | UnwindData |  |
| 99 | `WTHelperGetAgencyInfo` | `0x41250` | 242 | UnwindData |  |
| 103 | `WTHelperGetKnownUsages` | `0x41350` | 157 | UnwindData |  |
| 107 | `WTHelperIsChainedToMicrosoft` | `0x41400` | 408 | UnwindData |  |
| 108 | `WTHelperIsChainedToMicrosoftFromStateData` | `0x415A0` | 207 | UnwindData |  |
| 109 | `WTHelperIsInRootStore` | `0x41680` | 265 | UnwindData |  |
| 1 | `ComputeFirstPageHash` | `0x41BF0` | 661 | UnwindData |  |
| 2 | `CryptCATVerifyMember` | `0x427D0` | 64 | UnwindData |  |
| 49 | `CryptCATPersistStore` | `0x42820` | 55 | UnwindData |  |
| 50 | `CryptCATPutAttrInfo` | `0x42860` | 467 | UnwindData |  |
| 51 | `CryptCATPutCatAttrInfo` | `0x42A40` | 610 | UnwindData |  |
| 52 | `CryptCATPutMemberInfo` | `0x42CB0` | 375 | UnwindData |  |
| 24 | `CryptCATAdminPauseServiceForBackup` | `0x43060` | 64 | UnwindData |  |
| 28 | `CryptCATAdminResolveCatalogPath` | `0x430B0` | 278 | UnwindData |  |
| 30 | `CryptCATCDFClose` | `0x448D0` | 159 | UnwindData |  |
| 31 | `CryptCATCDFEnumAttributes` | `0x44980` | 24 | UnwindData |  |
| 32 | `CryptCATCDFEnumAttributesWithCDFTag` | `0x449A0` | 61 | UnwindData |  |
| 33 | `CryptCATCDFEnumCatAttributes` | `0x449F0` | 267 | UnwindData |  |
| 34 | `CryptCATCDFEnumMembers` | `0x44B10` | 97 | UnwindData |  |
| 35 | `CryptCATCDFEnumMembersByCDFTag` | `0x44B80` | 26 | UnwindData |  |
| 36 | `CryptCATCDFEnumMembersByCDFTagEx` | `0x44BA0` | 67 | UnwindData |  |
| 37 | `CryptCATCDFOpen` | `0x44BF0` | 1,436 | UnwindData |  |
| 3 | `CryptSIPGetInfo` | `0x460F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `CryptSIPGetSealedDigest` | `0x46130` | 178 | UnwindData |  |
| 58 | `CryptSIPPutSignedDataMsg` | `0x461F0` | 199 | UnwindData |  |
| 59 | `CryptSIPRemoveSignedDataMsg` | `0x462C0` | 137 | UnwindData |  |
| 164 | `mssip32DllRegisterServer` | `0x46350` | 691 | UnwindData |  |
| 165 | `mssip32DllUnregisterServer` | `0x46610` | 404 | UnwindData |  |
| 159 | `WintrustSetDefaultIncludePEPageHashes` | `0x47690` | 4,608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `WTGetPluginSignatureInfo` | `0x48890` | 349 | UnwindData |  |
| 72 | `OfficeCleanupPolicy` | `0x495B0` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `OfficeInitializePolicy` | `0x495B0` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `SetMessageDigestInfo` | `0x495B0` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `SoftpubDefCertInit` | `0x49860` | 240 | UnwindData |  |
| 10 | `SoftpubFreeDefUsageCallData` | `0x49960` | 72 | UnwindData |  |
| 11 | `SoftpubLoadDefUsageCallData` | `0x499B0` | 315 | UnwindData |  |
| 13 | `AddPersonalTrustDBPages` | `0x49B00` | 29 | UnwindData |  |
| 74 | `OpenPersonalTrustDBDialog` | `0x49B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `OpenPersonalTrustDBDialogEx` | `0x49B40` | 276 | UnwindData |  |
| 91 | `WTConfigCiFreePrivateData` | `0x4F450` | 128 | UnwindData |  |
| 92 | `WTConvertCertCtxToChainInfo` | `0x4F4E0` | 128 | UnwindData |  |
| 115 | `WTLogConfigCiSignerEvent` | `0x4F570` | 648 | UnwindData |  |
| 116 | `WTLogSmartAppControlDefenderInfo` | `0x4F800` | 455 | UnwindData |  |
| 155 | `WintrustGetHash` | `0x4F9D0` | 187 | UnwindData |  |
| 161 | `WintrustUserWriteabilityCheck` | `0x4FAA0` | 84 | UnwindData |  |
| 66 | `FindCertsByIssuer` | `0x50BF0` | 1,023 | UnwindData |  |
| 79 | `SoftpubDllRegisterServer` | `0x51360` | 626 | UnwindData |  |
| 80 | `SoftpubDllUnregisterServer` | `0x515E0` | 367 | UnwindData |  |
| 81 | `SoftpubDumpStructure` | `0x521D0` | 2,407 | UnwindData |  |
| 85 | `SrpCheckSmartlockerEAandProcessToken` | `0x52F20` | 30,428 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
