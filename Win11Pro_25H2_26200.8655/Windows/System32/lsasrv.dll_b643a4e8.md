# Binary Specification: lsasrv.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\lsasrv.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b643a4e8279d485dadd6ab1be48034e7363426616e4fbaf33a4051b0e512cd0e`
* **Total Exported Functions:** 331

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 267 | `LsapDbReleaseLockEx` | `0x2FD0` | 393 | UnwindData |  |
| 226 | `LsapDbCreateObject` | `0x3160` | 1,139 | UnwindData |  |
| 310 | `LsarCreateSecret` | `0x3A80` | 761 | UnwindData |  |
| 315 | `LsarOpenSecret` | `0x3D80` | 765 | UnwindData |  |
| 248 | `LsapDbGetSecretType` | `0x4130` | 498 | UnwindData |  |
| 220 | `LsapDbApplyTransaction` | `0x4330` | 673 | UnwindData |  |
| 317 | `LsarQueryInformationPolicy` | `0x5BC0` | 44 | UnwindData |  |
| 263 | `LsapDbQueryInformationPolicy` | `0x6540` | 2,288 | UnwindData |  |
| 309 | `LsarClose` | `0x7980` | 51 | UnwindData |  |
| 262 | `LsapDbOpenObject` | `0x9AB0` | 44 | UnwindData |  |
| 229 | `LsapDbDereferenceHandle` | `0xB080` | 814 | UnwindData |  |
| 28 | *Ordinal Only* | `0xB810` | 51 | UnwindData |  |
| 266 | `LsapDbReferenceObject` | `0xB850` | 364 | UnwindData |  |
| 272 | `LsapDbVerifyHandle` | `0xC0C0` | 601 | UnwindData |  |
| 230 | `LsapDbDereferenceObject` | `0xF4C0` | 29 | UnwindData |  |
| 215 | `LsapCloseHandle` | `0xFD50` | 1,065 | UnwindData |  |
| 223 | `LsapDbCloseObject` | `0x10180` | 52 | UnwindData |  |
| 52 | `TracePrintCallerInformation` | `0x13DB0` | 415 | UnwindData |  |
| 51 | `TracePrint` | `0x13F60` | 54 | UnwindData |  |
| 251 | `LsapDbLookupAddListReferencedDomains` | `0x142C0` | 45 | UnwindData |  |
| 216 | `LsapCompareDomainNames` | `0x14530` | 7 | UnwindData |  |
| 253 | `LsapDbLookupGetDomainInfo` | `0x17090` | 120 | UnwindData |  |
| 71 | `LsaIAuditSamEvent` | `0x1C960` | 43 | UnwindData |  |
| 59 | `LsaIAllocateHeapZero` | `0x1EFB0` | 7,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 209 | `LsapAllocateLsaHeap` | `0x1EFB0` | 7,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 210 | `LsapAllocatePrivateHeap` | `0x1EFB0` | 7,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | *Ordinal Only* | `0x1EFB0` | 7,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 281 | `LsapDuplicateString` | `0x20BB0` | 38 | UnwindData |  |
| 284 | `LsapFreeString` | `0x23820` | 64 | UnwindData |  |
| 103 | `LsaIFreeHeap` | `0x24B10` | 5,936 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 282 | `LsapFreeLsaHeap` | `0x24B10` | 5,936 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 283 | `LsapFreePrivateHeap` | `0x24B10` | 5,936 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | *Ordinal Only* | `0x24B10` | 5,936 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 182 | `LsaIRetrieveCurrentUserSid` | `0x26240` | 277 | UnwindData |  |
| 30 | *Ordinal Only* | `0x26C70` | 81 | UnwindData |  |
| 29 | *Ordinal Only* | `0x26D90` | 70 | UnwindData |  |
| 172 | `LsaIQueryPackageAttrInLogonSession` | `0x27770` | 137 | UnwindData |  |
| 289 | `LsapGetLogonSessionAccountInfoEx` | `0x27BC0` | 782 | UnwindData |  |
| 72 | `LsaICallPackage` | `0x30640` | 46 | UnwindData |  |
| 73 | `LsaICallPackageEx` | `0x30680` | 465 | UnwindData |  |
| 104 | `LsaIFreeReturnBuffer` | `0x30980` | 143 | UnwindData |  |
| 130 | `LsaIGetCallInfo` | `0x343F0` | 295 | UnwindData |  |
| 27 | *Ordinal Only* | `0x36420` | 162 | UnwindData |  |
| 24 | *Ordinal Only* | `0x4D190` | 516 | UnwindData |  |
| 106 | `LsaIFree_LSAI_PRIVATE_DATA` | `0x4DC90` | 27 | UnwindData |  |
| 113 | `LsaIFree_LSAPR_PRIVILEGE_SET` | `0x4DC90` | 27 | UnwindData |  |
| 41 | `IsTraceLevelEnabled` | `0x4E9B0` | 5,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 275 | `LsapDbWriteAttributesObject` | `0x4FD70` | 147 | UnwindData |  |
| 228 | `LsapDbDeleteObject` | `0x50850` | 669 | UnwindData |  |
| 268 | `LsapDbSecretIsMachineAcc` | `0x50DE0` | 199 | UnwindData |  |
| 265 | `LsapDbReadAttributesObject` | `0x50F50` | 412 | UnwindData |  |
| 318 | `LsarQuerySecret` | `0x511F0` | 856 | UnwindData |  |
| 307 | `LsapTraceEventWithData` | `0x51550` | 253 | UnwindData |  |
| 193 | `LsaISetUserFlags` | `0x543E0` | 48 | UnwindData |  |
| 77 | `LsaICheckProtectedUserByTokenInfo` | `0x54420` | 195 | UnwindData |  |
| 280 | `LsapDuplicateSid` | `0x55770` | 116 | UnwindData |  |
| 58 | `LsaIAllocateHeap` | `0x57BA0` | 21,536 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | *Ordinal Only* | `0x57BA0` | 21,536 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 219 | `LsapDbAcquireLockEx` | `0x5CFC0` | 330 | UnwindData |  |
| 301 | `LsapRpcCopyUnicodeString` | `0x5D110` | 41 | UnwindData |  |
| 258 | `LsapDbLookupSidsInPrimaryDomain` | `0x5DC90` | 1,249 | UnwindData |  |
| 45 | `LsaLookupPerfCounterAddLargeAmount` | `0x5E570` | 105 | UnwindData |  |
| 48 | `LsaLookupPerfCounterIncrementCount` | `0x5E5E0` | 98 | UnwindData |  |
| 300 | `LsapRpcCopySid` | `0x5F2C0` | 41 | UnwindData |  |
| 306 | `LsapTraceEvent` | `0x5F760` | 165 | UnwindData |  |
| 252 | `LsapDbLookupCreateListReferencedDomains` | `0x67DB0` | 201 | UnwindData |  |
| 254 | `LsapDbLookupListReferencedDomains` | `0x73C60` | 135 | UnwindData |  |
| 80 | `LsaIContextToHandleNoRef` | `0x77790` | 632 | UnwindData |  |
| 204 | `LsaIWasLogonNotifiedOfProfileLoad` | `0x79640` | 65 | UnwindData |  |
| 31 | *Ordinal Only* | `0x7A420` | 540 | UnwindData |  |
| 55 | `LsaIAdjustTokenObjectIntegrity` | `0x7A650` | 305 | UnwindData |  |
| 160 | `LsaIModifyPerformanceCounter` | `0x7B320` | 132 | UnwindData |  |
| 271 | `LsapDbUpdateCountCompUnmappedNames` | `0x7CF40` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `LsaIEventWritePackageNotCacheLogonUser` | `0x7CFF0` | 202 | UnwindData |  |
| 44 | `LsaLookupPerfCounterAddAmount` | `0x7F070` | 101 | UnwindData |  |
| 114 | `LsaIFree_LSAPR_REFERENCED_DOMAIN_LIST` | `0x81F50` | 40 | UnwindData |  |
| 328 | `_fgs__LSAPR_TRUSTED_ENUM_BUFFER` | `0x82040` | 78 | UnwindData |  |
| 330 | `_fgs__LSAPR_TRUST_INFORMATION` | `0x820F0` | 47 | UnwindData |  |
| 111 | `LsaIFree_LSAPR_POLICY_INFORMATION` | `0x82150` | 159 | UnwindData |  |
| 313 | `LsarLookupSids` | `0x82200` | 515 | UnwindData |  |
| 84 | `LsaICryptUnprotectData` | `0x85D30` | 134 | UnwindData |  |
| 109 | `LsaIFree_LSAPR_CR_CIPHER_VALUE` | `0x85FC0` | 3,376 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `LsaIFreeSupplementalTokenInfo` | `0x86CF0` | 45 | UnwindData |  |
| 92 | `LsaIEqualSupplementalTokenInfo` | `0x86EE0` | 63 | UnwindData |  |
| 299 | `LsapRemoveTrailingDot` | `0x87560` | 2,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 200 | `LsaIUpdateLogonSession` | `0x87D30` | 826 | UnwindData |  |
| 188 | `LsaISetLogonInfo` | `0x88070` | 642 | UnwindData |  |
| 38 | *Ordinal Only* | `0x888A0` | 65 | UnwindData |  |
| 54 | `LsaIAddNamesToLogonSession` | `0x88B40` | 392 | UnwindData |  |
| 98 | `LsaIFilterSids` | `0x8AF20` | 3,472 | UnwindData |  |
| 183 | `LsaISafeMode` | `0x8BF70` | 67 | UnwindData |  |
| 161 | `LsaINoConnectedUserPolicy` | `0x8C230` | 13,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 297 | `LsapOpenSam` | `0x8F650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 217 | `LsapCrServerGetSessionKey` | `0x8F660` | 134 | UnwindData |  |
| 136 | `LsaIGetNbAndDnsDomainNames` | `0x901F0` | 538 | UnwindData |  |
| 82 | `LsaICryptProtectData` | `0x91900` | 131 | UnwindData |  |
| 34 | *Ordinal Only* | `0x91A50` | 543 | UnwindData |  |
| 179 | `LsaIRegisterNotification` | `0x92790` | 637 | UnwindData |  |
| 35 | *Ordinal Only* | `0x92EE0` | 35 | UnwindData |  |
| 314 | `LsarOpenPolicy` | `0x92FD0` | 28 | UnwindData |  |
| 66 | `LsaIAuditLogonEx` | `0x93BC0` | 147 | UnwindData |  |
| 134 | `LsaIGetLogonGuid` | `0x94050` | 289 | UnwindData |  |
| 145 | `LsaIImpersonateClient` | `0x94200` | 3,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 158 | `LsaILookupUserAccountType` | `0x95170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 269 | `LsapDbSidToLogicalNameObject` | `0x95190` | 72 | UnwindData |  |
| 249 | `LsapDbInitializeAttribute` | `0x951E0` | 13,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `LsaIIsInEmulatedDomainJoinMode` | `0x984D0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 322 | `LsarSetSecret` | `0x98520` | 126 | UnwindData |  |
| 154 | `LsaIIsSuppressChannelBindingInfo` | `0x98620` | 1,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `LsaIFree_LSAPR_TRANSLATED_NAMES` | `0x98B30` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 171 | `LsaIQueryInformationPolicyTrusted` | `0x98E80` | 1,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `LsaICheckRestrictedMode` | `0x995B0` | 1,504 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `LsaIIsLocalHost` | `0x99B90` | 43 | UnwindData |  |
| 257 | `LsapDbLookupNamesInPrimaryDomain` | `0x9A030` | 1,289 | UnwindData |  |
| 135 | `LsaIGetNameFromLuid` | `0x9B420` | 194 | UnwindData |  |
| 75 | `LsaICancelNotification` | `0x9B860` | 35 | UnwindData |  |
| 36 | *Ordinal Only* | `0x9BC00` | 50 | UnwindData |  |
| 65 | `LsaIAuditKerberosLogon` | `0x9BC40` | 148 | UnwindData |  |
| 23 | *Ordinal Only* | `0x9C6E0` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `LsaIIsTargetPrivate` | `0x9CA30` | 248 | UnwindData |  |
| 142 | `LsaIGetSupplementalTokenInfo` | `0x9EC10` | 187 | UnwindData |  |
| 191 | `LsaISetSupplementalTokenInfo` | `0x9ECE0` | 2,118 | UnwindData |  |
| 62 | `LsaIAuditAccountLogonEx` | `0xA1CD0` | 1,229 | UnwindData |  |
| 67 | `LsaIAuditLogonUsingExplicitCreds` | `0xA21B0` | 1,326 | UnwindData |  |
| 304 | `LsapSetErrorInfo` | `0xB2800` | 183 | UnwindData |  |
| 163 | `LsaINotifyChangeNotification` | `0xB3380` | 316 | UnwindData |  |
| 53 | `LsaDbLookupSidChainRequest` | `0xB3B40` | 151 | UnwindData |  |
| 250 | `LsapDbIsStatusConnectionFailure` | `0xB5270` | 2,400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | *Ordinal Only* | `0xB5BD0` | 2,752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | *Ordinal Only* | `0xB6690` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 231 | `LsapDbEnumerateSids` | `0xB6790` | 548 | UnwindData |  |
| 207 | `LsapAdtGetCallerProcessInfo` | `0xB8BD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 208 | `LsapAdtWriteLog` | `0xB8BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 212 | `LsapAuditFailed` | `0xB8BF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 298 | `LsapQueryClientInfo` | `0xB8C00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 305 | `LsapSidListSize` | `0xB8C10` | 31,888 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `LsaIGetCcgClient` | `0xC08A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `LsaIIsContainerized` | `0xC08B0` | 24,112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `LsaINotifyNewPassword` | `0xC66E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 167 | `LsaINotifyPasswordChanged` | `0xC66F0` | 208 | UnwindData |  |
| 90 | `LsaIEfsAcceptSmartcardCredentials` | `0xC7F00` | 486 | UnwindData |  |
| 93 | `LsaIEventWritePackageNoCredential` | `0xCD200` | 287 | UnwindData |  |
| 178 | `LsaIRegisterLogonSessionCallback` | `0xCD330` | 90 | UnwindData |  |
| 187 | `LsaISetLogonGuidInLogonSession` | `0xCD390` | 320 | UnwindData |  |
| 190 | `LsaISetPackageAttrInLogonSession` | `0xCD4E0` | 48 | UnwindData |  |
| 196 | `LsaIUnregisterLogonSessionCallback` | `0xCD520` | 98 | UnwindData |  |
| 276 | `LsapDomainRenameHandlerForLogonSessions` | `0xCD590` | 648 | UnwindData |  |
| 81 | `LsaICopyToTokenInfoFromHandle` | `0xCF440` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `InitializeLsaExtension` | `0xCF670` | 49 | UnwindData |  |
| 50 | `QueryLsaInterface` | `0xD0070` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `LsaICryptProtectDataEx` | `0xD0170` | 155 | UnwindData |  |
| 85 | `LsaICryptUnprotectDataEx` | `0xD0220` | 157 | UnwindData |  |
| 88 | `LsaIDeriveCredentialKey` | `0xD02D0` | 274 | UnwindData |  |
| 308 | `LsapTruncateUnicodeString` | `0xD05D0` | 10,336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `LsaIAllowProtectedCredLogon` | `0xD2E30` | 218 | UnwindData |  |
| 137 | `LsaIGetNego2Package` | `0xD6280` | 192 | UnwindData |  |
| 199 | `LsaIUpdateKerbMaxTokenSize` | `0xD6350` | 147 | UnwindData |  |
| 86 | `LsaIDereferenceCredHandle` | `0xD89C0` | 46 | UnwindData |  |
| 87 | `LsaIDereferenceCtxtHandle` | `0xD8A00` | 46 | UnwindData |  |
| 176 | `LsaIReferenceCredHandle` | `0xD8A40` | 221 | UnwindData |  |
| 177 | `LsaIReferenceCtxtHandle` | `0xD8B30` | 221 | UnwindData |  |
| 74 | `LsaICallPackagePassthrough` | `0xDAAA0` | 302 | UnwindData |  |
| 91 | `LsaIEqualLogonProcessName` | `0xDABE0` | 81 | UnwindData |  |
| 95 | `LsaIExtractTargetInfo` | `0xDAC40` | 288 | UnwindData |  |
| 139 | `LsaIGetRemoteCredGuardLogonBuffer` | `0xDAD70` | 336 | UnwindData |  |
| 140 | `LsaIGetRemoteCredGuardSupplementalCreds` | `0xDAED0` | 290 | UnwindData |  |
| 201 | `LsaIValidateTargetInfo` | `0xDB000` | 350 | UnwindData |  |
| 138 | `LsaIGetNetworkInfo` | `0xDDF70` | 222 | UnwindData |  |
| 32 | *Ordinal Only* | `0xDF3B0` | 180 | UnwindData |  |
| 151 | `LsaIIsLastInteractiveLogonInfoEnabled` | `0xDF470` | 60,528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `LsaIInitializeNetlogonFuncPtrs` | `0xEE0E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `LsaIIsMachineSecureByDefault` | `0xEE100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 279 | `LsapDssetupInitializeGetPrimaryDomainInformationOpState` | `0xEE110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 293 | `LsapInitLsa` | `0xEE130` | 1,963 | UnwindData |  |
| 39 | *Ordinal Only* | `0xEEC20` | 38 | UnwindData |  |
| 42 | `LsaIIsUserMSA` | `0xEEF50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `LsaIRenewCertificate` | `0xEEF70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `LsaIFlushIdentityCacheForSid` | `0xEEF90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `LsaIGetTokenInformationForLocalUser` | `0xEEFB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `LsaISanitizeSAMName` | `0xEEFC0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `LsaLookupPerfCounterDecrementCount` | `0xEF0F0` | 37 | UnwindData |  |
| 47 | `LsaLookupPerfCounterDecrementLargeCount` | `0xEF120` | 38 | UnwindData |  |
| 49 | `LsaLookupPerfCounterIncrementLargeCount` | `0xEF150` | 38 | UnwindData |  |
| 56 | `LsaIAdtAuditingEnabledByCategory` | `0xF0B50` | 118 | UnwindData |  |
| 57 | `LsaIAdtAuditingEnabledBySubCategory` | `0xF0BD0` | 344 | UnwindData |  |
| 61 | `LsaIAuditAccountLogon` | `0xF0D30` | 56 | UnwindData |  |
| 63 | `LsaIAuditInitializeParametersAndWriteEvent` | `0xF0D70` | 229 | UnwindData |  |
| 64 | `LsaIAuditKdcEvent` | `0xF0E60` | 1,192 | UnwindData |  |
| 68 | `LsaIAuditNotifyPackageLoad` | `0xF1310` | 485 | UnwindData |  |
| 69 | `LsaIAuditPasswordAccessEvent` | `0xF1500` | 527 | UnwindData |  |
| 70 | `LsaIAuditReplay` | `0xF1720` | 1,373 | UnwindData |  |
| 205 | `LsaIWriteAuditEvent` | `0xF1C90` | 228 | UnwindData |  |
| 206 | `LsaIWriteKdcAuthenticationEvent` | `0xF1D80` | 943 | UnwindData |  |
| 107 | `LsaIFree_LSAI_SECRET_ENUM_BUFFER` | `0xF2140` | 82 | UnwindData |  |
| 108 | `LsaIFree_LSAPR_ACCOUNT_ENUM_BUFFER` | `0xF21A0` | 90 | UnwindData |  |
| 110 | `LsaIFree_LSAPR_POLICY_DOMAIN_INFORMATION` | `0xF2200` | 30 | UnwindData |  |
| 112 | `LsaIFree_LSAPR_PRIVILEGE_ENUM_BUFFER` | `0xF2230` | 83 | UnwindData |  |
| 115 | `LsaIFree_LSAPR_SR_SECURITY_DESCRIPTOR` | `0xF2290` | 40 | UnwindData |  |
| 122 | `LsaIFree_LSAPR_UNICODE_STRING` | `0xF2290` | 40 | UnwindData |  |
| 117 | `LsaIFree_LSAPR_TRANSLATED_SIDS` | `0xF22C0` | 36 | UnwindData |  |
| 118 | `LsaIFree_LSAPR_TRUSTED_DOMAIN_INFO` | `0xF22F0` | 45 | UnwindData |  |
| 119 | `LsaIFree_LSAPR_TRUSTED_ENUM_BUFFER` | `0xF2330` | 20 | UnwindData |  |
| 120 | `LsaIFree_LSAPR_TRUSTED_ENUM_BUFFER_EX` | `0xF2350` | 20 | UnwindData |  |
| 121 | `LsaIFree_LSAPR_TRUST_INFORMATION` | `0xF2370` | 40 | UnwindData |  |
| 123 | `LsaIFree_LSAPR_UNICODE_STRING_BUFFER` | `0xF23A0` | 20 | UnwindData |  |
| 18 | *Ordinal Only* | `0xF23C0` | 56 | UnwindData |  |
| 19 | *Ordinal Only* | `0xF23C0` | 56 | UnwindData |  |
| 20 | *Ordinal Only* | `0xF2400` | 110 | UnwindData |  |
| 214 | `LsapCheckBootMode` | `0xF2600` | 304 | UnwindData |  |
| 192 | `LsaISetTokenDacl` | `0xF39F0` | 243 | UnwindData |  |
| 211 | `LsapAuOpenSam` | `0xF54E0` | 1,276 | UnwindData |  |
| 218 | `LsapCrServerGetSessionKeySafe` | `0xF59F0` | 82 | UnwindData |  |
| 286 | `LsapGetCapeNamesForCap` | `0xF64B0` | 438 | UnwindData |  |
| 325 | `ServiceInit` | `0xF71E0` | 374 | UnwindData |  |
| 326 | `_fgs__LSAPR_TRUSTED_DOMAIN_FULL_INFORMATION2` | `0xF7600` | 28 | UnwindData |  |
| 327 | `_fgs__LSAPR_TRUSTED_DOMAIN_INFORMATION_EX2` | `0xF7630` | 60 | UnwindData |  |
| 329 | `_fgs__LSAPR_TRUSTED_ENUM_BUFFER_EX` | `0xF7680` | 74 | UnwindData |  |
| 331 | `_fgu__LSAPR_TRUSTED_DOMAIN_INFO` | `0xF76D0` | 173 | UnwindData |  |
| 26 | *Ordinal Only* | `0x100BC0` | 414 | UnwindData |  |
| 25 | *Ordinal Only* | `0x100D70` | 336 | UnwindData |  |
| 168 | `LsaIOpenPolicyTrusted` | `0x101740` | 33 | UnwindData |  |
| 321 | `LsarSetInformationPolicy` | `0x101C40` | 792 | UnwindData |  |
| 255 | `LsapDbLookupMergeDisjointReferencedDomains` | `0x1036C0` | 696 | UnwindData |  |
| 256 | `LsapDbLookupNameChainRequest` | `0x103980` | 151 | UnwindData |  |
| 290 | `LsapGetLookupRestrictIsolatedNameLevel` | `0x103A20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 295 | `LsapIsBuiltinDomain` | `0x103A30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 302 | `LsapRtlValidateControllerTrustedDomain` | `0x103A50` | 417 | UnwindData |  |
| 303 | `LsapRtlValidateControllerTrustedDomainByHandle` | `0x103C00` | 158 | UnwindData |  |
| 76 | `LsaIChangeSecretCipherKey` | `0x1047F0` | 171 | UnwindData |  |
| 79 | `LsaIClearOldSyskey` | `0x1048B0` | 68 | UnwindData |  |
| 144 | `LsaIHealthCheck` | `0x104900` | 196 | UnwindData |  |
| 189 | `LsaISetNewSyskey` | `0x1049D0` | 475 | UnwindData |  |
| 89 | `LsaIDsNotifiedObjectChange` | `0x104BC0` | 138 | UnwindData |  |
| 96 | `LsaIFilterInboundNamespace` | `0x104C50` | 128 | UnwindData |  |
| 97 | `LsaIFilterNamespace` | `0x104CE0` | 125 | UnwindData |  |
| 100 | `LsaIForestTrustFindMatch` | `0x104D70` | 89 | UnwindData |  |
| 101 | `LsaIFreeFilterInboundNamespaceResult` | `0x104DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `LsaIFreeForestTrustInfo` | `0x104DE0` | 47 | UnwindData |  |
| 128 | `LsaIFree_LSA_FOREST_TRUST_COLLISION_INFORMATION` | `0x104E20` | 47 | UnwindData |  |
| 129 | `LsaIFree_LSA_FOREST_TRUST_INFORMATION` | `0x104E60` | 47 | UnwindData |  |
| 132 | `LsaIGetClientOsInfo` | `0x104EA0` | 107 | UnwindData |  |
| 133 | `LsaIGetForestTrustInformation` | `0x104F20` | 60 | UnwindData |  |
| 141 | `LsaIGetSiteName` | `0x104F70` | 60 | UnwindData |  |
| 148 | `LsaIIsDomainWithinForest` | `0x104FC0` | 140 | UnwindData |  |
| 149 | `LsaIIsDsPaused` | `0x105060` | 44 | UnwindData |  |
| 156 | `LsaIIsTrustedDomainsEnabled` | `0x1050A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `LsaIKerberosRegisterTrustNotification` | `0x1050B0` | 73 | UnwindData |  |
| 162 | `LsaINoMoreWin2KDomain` | `0x105100` | 44 | UnwindData |  |
| 164 | `LsaINotifyGCStatusChange` | `0x105140` | 45 | UnwindData |  |
| 169 | `LsaIQueryForestTrustInfo` | `0x105180` | 75 | UnwindData |  |
| 170 | `LsaIQueryForestTrustInformation` | `0x1051E0` | 28 | UnwindData |  |
| 173 | `LsaIQuerySiteInfo` | `0x105210` | 60 | UnwindData |  |
| 174 | `LsaIQuerySubnetInfo` | `0x105260` | 60 | UnwindData |  |
| 175 | `LsaIQueryUpnSuffixes` | `0x1052B0` | 60 | UnwindData |  |
| 181 | `LsaIReplicateClientObject` | `0x105300` | 75 | UnwindData |  |
| 184 | `LsaISamIndicatedDsStarted` | `0x105360` | 73 | UnwindData |  |
| 186 | `LsaISetClientDnsHostName` | `0x1053B0` | 138 | UnwindData |  |
| 198 | `LsaIUpdateForestTrustInformation` | `0x105440` | 91 | UnwindData |  |
| 202 | `LsaIVerifyCachability` | `0x1054B0` | 37 | UnwindData |  |
| 203 | `LsaIVerifyCachabilityEx` | `0x1054E0` | 28 | UnwindData |  |
| 277 | `LsapDsInitializeDsStateInfo` | `0x105510` | 55 | UnwindData |  |
| 278 | `LsapDsUnitializeDsStateInfo` | `0x105550` | 63 | UnwindData |  |
| 124 | `LsaIFree_LSAP_SITENAME_INFO` | `0x105FF0` | 42 | UnwindData |  |
| 125 | `LsaIFree_LSAP_SITE_INFO` | `0x106020` | 72 | UnwindData |  |
| 127 | `LsaIFree_LSAP_UPN_SUFFIXES` | `0x106020` | 72 | UnwindData |  |
| 126 | `LsaIFree_LSAP_SUBNET_INFO` | `0x106070` | 98 | UnwindData |  |
| 165 | `LsaINotifyNetlogonParametersChangeW` | `0x1060E0` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `LsaILookupWellKnownName` | `0x1063E0` | 31 | UnwindData |  |
| 180 | `LsaIRegisterPolicyChangeNotificationCallback` | `0x106BE0` | 307 | UnwindData |  |
| 195 | `LsaIUnregisterAllPolicyChangeNotificationCallback` | `0x106D20` | 355 | UnwindData |  |
| 197 | `LsaIUnregisterPolicyChangeNotificationCallback` | `0x106E90` | 301 | UnwindData |  |
| 311 | `LsarDeleteObject` | `0x107090` | 49 | UnwindData |  |
| 194 | `LsaITransformAuthorizationData` | `0x1070D0` | 445 | UnwindData |  |
| 213 | `LsapBuildPrivilegeAuditString` | `0x1078B0` | 529 | UnwindData |  |
| 221 | `LsapDbBuildObjectCaches` | `0x10A550` | 34 | UnwindData |  |
| 222 | `LsapDbCloseHandle` | `0x10A5D0` | 180 | UnwindData |  |
| 227 | `LsapDbDeleteAttributesObject` | `0x10AB00` | 174 | UnwindData |  |
| 224 | `LsapDbCopyUnicodeAttribute` | `0x10B180` | 175 | UnwindData |  |
| 225 | `LsapDbCopyUnicodeAttributeNoAlloc` | `0x10B240` | 105 | UnwindData |  |
| 244 | `LsapDbFreeAttributes` | `0x10B2B0` | 77 | UnwindData |  |
| 259 | `LsapDbMakeGuidAttribute` | `0x10B310` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 260 | `LsapDbMakeSidAttribute` | `0x10B370` | 138 | UnwindData |  |
| 261 | `LsapDbMakeUnicodeAttribute` | `0x10B400` | 257 | UnwindData |  |
| 264 | `LsapDbReadAttribute` | `0x10B510` | 328 | UnwindData |  |
| 232 | `LsapDbEnumerateTrustedDomainsEx` | `0x10BB40` | 487 | UnwindData |  |
| 245 | `LsapDbFreeTrustedDomainsEx` | `0x10BD30` | 71 | UnwindData |  |
| 270 | `LsapDbSlowEnumerateTrustedDomains` | `0x10BD80` | 281 | UnwindData |  |
| 312 | `LsarEnumerateTrustedDomainsEx` | `0x10C000` | 186 | UnwindData |  |
| 319 | `LsarQueryTrustedDomainInfoByName` | `0x10C170` | 733 | UnwindData |  |
| 323 | `LsarSetTrustedDomainInfoByName` | `0x10C460` | 558 | UnwindData |  |
| 233 | `LsapDbExpAcquireReadLockTrustedDomainList` | `0x10C6A0` | 42 | UnwindData |  |
| 234 | `LsapDbExpAcquireWriteLockTrustedDomainList` | `0x10C6D0` | 42 | UnwindData |  |
| 235 | `LsapDbExpConvertReadLockTrustedDomainListToExclusive` | `0x10C700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 236 | `LsapDbExpConvertWriteLockTrustedDomainListToShared` | `0x10C720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 237 | `LsapDbExpIsCacheBuilding` | `0x10C740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 238 | `LsapDbExpIsCacheValid` | `0x10C760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 239 | `LsapDbExpIsLockedTrustedDomainList` | `0x10C780` | 64 | UnwindData |  |
| 240 | `LsapDbExpMakeCacheBuilding` | `0x10C7D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 241 | `LsapDbExpMakeCacheInvalid` | `0x10C7F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 242 | `LsapDbExpMakeCacheValid` | `0x10C810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 243 | `LsapDbExpReleaseLockTrustedDomainList` | `0x10C830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 246 | `LsapDbGetDbObjectTypeName` | `0x10C850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 247 | `LsapDbGetDbPolicyHandle` | `0x10C870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 273 | `LsapDbVerifyInfoQueryTrustedDomain` | `0x10C880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 274 | `LsapDbVerifyInfoSetTrustedDomain` | `0x10C8A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 285 | `LsapGetAccountDomainHandle` | `0x10C8C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 287 | `LsapGetGlobalRestrictAnonymous` | `0x10C8D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 288 | `LsapGetHourlyLogLevel` | `0x10C8E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 291 | `LsapGetPolicyHandle` | `0x10C8F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 292 | `LsapGetWellKnownSid` | `0x10C910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 294 | `LsapInitializeLsaDb` | `0x10C930` | 110 | UnwindData |  |
| 296 | `LsapIsSamOpened` | `0x10C9B0` | 7,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 316 | `LsarQueryDomainInformationPolicy` | `0x10E6F0` | 272 | UnwindData |  |
| 320 | `LsarRetrievePrivateData` | `0x10F0B0` | 169 | UnwindData |  |
| 324 | `LsarStorePrivateData` | `0x10F260` | 246 | UnwindData |  |
| 15 | *Ordinal Only* | `0x195F60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | *Ordinal Only* | `0x195F70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | *Ordinal Only* | `0x195F80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | *Ordinal Only* | `0x195F90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | *Ordinal Only* | `0x195FA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | *Ordinal Only* | `0x195FB0` | 18,180 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | *Ordinal Only* | `0x19A6B4` | 60 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | *Ordinal Only* | `0x19A6F0` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | *Ordinal Only* | `0x19A6F4` | 1,356 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | *Ordinal Only* | `0x19AC40` | 184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | *Ordinal Only* | `0x19ACF8` | 120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | *Ordinal Only* | `0x19AD70` | 7,368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | *Ordinal Only* | `0x19CA38` | 2,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | *Ordinal Only* | `0x19D3F0` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | *Ordinal Only* | `0x19D418` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | *Ordinal Only* | `0x19D768` | 0 | Indeterminate |  |
