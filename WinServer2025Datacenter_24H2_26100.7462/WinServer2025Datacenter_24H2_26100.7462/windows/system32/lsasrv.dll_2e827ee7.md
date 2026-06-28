# Binary Specification: lsasrv.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\lsasrv.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2e827ee7cb6ff9d7e9279b0617a7f9312aef7ca2eac04342af8a466557c4ba76`
* **Total Exported Functions:** 331

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 114 | `LsaIFree_LSAPR_REFERENCED_DOMAIN_LIST` | `0x5AC0` | 40 | UnwindData |  |
| 328 | `_fgs__LSAPR_TRUSTED_ENUM_BUFFER` | `0x5BF0` | 78 | UnwindData |  |
| 330 | `_fgs__LSAPR_TRUST_INFORMATION` | `0x6180` | 47 | UnwindData |  |
| 253 | `LsapDbLookupGetDomainInfo` | `0x61C0` | 120 | UnwindData |  |
| 111 | `LsaIFree_LSAPR_POLICY_INFORMATION` | `0x7870` | 159 | UnwindData |  |
| 309 | `LsarClose` | `0x8420` | 67 | UnwindData |  |
| 317 | `LsarQueryInformationPolicy` | `0x85B0` | 44 | UnwindData |  |
| 263 | `LsapDbQueryInformationPolicy` | `0x8F30` | 2,288 | UnwindData |  |
| 230 | `LsapDbDereferenceObject` | `0xC9E0` | 29 | UnwindData |  |
| 215 | `LsapCloseHandle` | `0xD270` | 1,065 | UnwindData |  |
| 223 | `LsapDbCloseObject` | `0xD6A0` | 52 | UnwindData |  |
| 266 | `LsapDbReferenceObject` | `0xE1D0` | 364 | UnwindData |  |
| 272 | `LsapDbVerifyHandle` | `0xEA40` | 601 | UnwindData |  |
| 52 | `TracePrintCallerInformation` | `0x11F80` | 415 | UnwindData |  |
| 51 | `TracePrint` | `0x12130` | 54 | UnwindData |  |
| 262 | `LsapDbOpenObject` | `0x14FB0` | 44 | UnwindData |  |
| 229 | `LsapDbDereferenceHandle` | `0x165F0` | 808 | UnwindData |  |
| 28 | *Ordinal Only* | `0x16D70` | 51 | UnwindData |  |
| 38 | *Ordinal Only* | `0x184D0` | 65 | UnwindData |  |
| 216 | `LsapCompareDomainNames` | `0x19120` | 7 | UnwindData |  |
| 251 | `LsapDbLookupAddListReferencedDomains` | `0x19610` | 45 | UnwindData |  |
| 44 | `LsaLookupPerfCounterAddAmount` | `0x19F90` | 101 | UnwindData |  |
| 136 | `LsaIGetNbAndDnsDomainNames` | `0x1A260` | 538 | UnwindData |  |
| 71 | `LsaIAuditSamEvent` | `0x1BC30` | 43 | UnwindData |  |
| 59 | `LsaIAllocateHeapZero` | `0x1E280` | 17,472 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 209 | `LsapAllocateLsaHeap` | `0x1E280` | 17,472 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 210 | `LsapAllocatePrivateHeap` | `0x1E280` | 17,472 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | *Ordinal Only* | `0x1E280` | 17,472 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 284 | `LsapFreeString` | `0x226C0` | 64 | UnwindData |  |
| 103 | `LsaIFreeHeap` | `0x239B0` | 5,936 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 282 | `LsapFreeLsaHeap` | `0x239B0` | 5,936 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 283 | `LsapFreePrivateHeap` | `0x239B0` | 5,936 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | *Ordinal Only* | `0x239B0` | 5,936 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 182 | `LsaIRetrieveCurrentUserSid` | `0x250E0` | 277 | UnwindData |  |
| 30 | *Ordinal Only* | `0x25B10` | 81 | UnwindData |  |
| 29 | *Ordinal Only* | `0x25C30` | 70 | UnwindData |  |
| 172 | `LsaIQueryPackageAttrInLogonSession` | `0x26620` | 137 | UnwindData |  |
| 289 | `LsapGetLogonSessionAccountInfoEx` | `0x26A70` | 782 | UnwindData |  |
| 72 | `LsaICallPackage` | `0x2FAE0` | 46 | UnwindData |  |
| 73 | `LsaICallPackageEx` | `0x2FB20` | 465 | UnwindData |  |
| 104 | `LsaIFreeReturnBuffer` | `0x2FE20` | 143 | UnwindData |  |
| 130 | `LsaIGetCallInfo` | `0x31920` | 308 | UnwindData |  |
| 281 | `LsapDuplicateString` | `0x340B0` | 38 | UnwindData |  |
| 280 | `LsapDuplicateSid` | `0x35630` | 116 | UnwindData |  |
| 58 | `LsaIAllocateHeap` | `0x37A60` | 16,288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | *Ordinal Only* | `0x37A60` | 16,288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 300 | `LsapRpcCopySid` | `0x3BA00` | 41 | UnwindData |  |
| 254 | `LsapDbLookupListReferencedDomains` | `0x3BB00` | 135 | UnwindData |  |
| 41 | `IsTraceLevelEnabled` | `0x3C510` | 5,376 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `LsaIFree_LSAI_PRIVATE_DATA` | `0x3DA10` | 27 | UnwindData |  |
| 113 | `LsaIFree_LSAPR_PRIVILEGE_SET` | `0x3DA10` | 27 | UnwindData |  |
| 275 | `LsapDbWriteAttributesObject` | `0x3E310` | 147 | UnwindData |  |
| 228 | `LsapDbDeleteObject` | `0x3EA50` | 669 | UnwindData |  |
| 268 | `LsapDbSecretIsMachineAcc` | `0x3F7E0` | 199 | UnwindData |  |
| 318 | `LsarQuerySecret` | `0x3F990` | 856 | UnwindData |  |
| 307 | `LsapTraceEventWithData` | `0x3FCF0` | 253 | UnwindData |  |
| 265 | `LsapDbReadAttributesObject` | `0x40120` | 412 | UnwindData |  |
| 204 | `LsaIWasLogonNotifiedOfProfileLoad` | `0x42B80` | 65 | UnwindData |  |
| 31 | *Ordinal Only* | `0x44550` | 540 | UnwindData |  |
| 55 | `LsaIAdjustTokenObjectIntegrity` | `0x44780` | 305 | UnwindData |  |
| 27 | *Ordinal Only* | `0x469A0` | 162 | UnwindData |  |
| 310 | `LsarCreateSecret` | `0x52200` | 761 | UnwindData |  |
| 315 | `LsarOpenSecret` | `0x52500` | 765 | UnwindData |  |
| 248 | `LsapDbGetSecretType` | `0x528B0` | 498 | UnwindData |  |
| 220 | `LsapDbApplyTransaction` | `0x52AB0` | 673 | UnwindData |  |
| 226 | `LsapDbCreateObject` | `0x52E30` | 1,139 | UnwindData |  |
| 267 | `LsapDbReleaseLockEx` | `0x532B0` | 393 | UnwindData |  |
| 219 | `LsapDbAcquireLockEx` | `0x5F580` | 330 | UnwindData |  |
| 54 | `LsaIAddNamesToLogonSession` | `0x61DD0` | 392 | UnwindData |  |
| 301 | `LsapRpcCopyUnicodeString` | `0x62210` | 41 | UnwindData |  |
| 258 | `LsapDbLookupSidsInPrimaryDomain` | `0x62D90` | 1,249 | UnwindData |  |
| 45 | `LsaLookupPerfCounterAddLargeAmount` | `0x63670` | 105 | UnwindData |  |
| 48 | `LsaLookupPerfCounterIncrementCount` | `0x636E0` | 98 | UnwindData |  |
| 306 | `LsapTraceEvent` | `0x64760` | 165 | UnwindData |  |
| 252 | `LsapDbLookupCreateListReferencedDomains` | `0x6DB50` | 201 | UnwindData |  |
| 80 | `LsaIContextToHandleNoRef` | `0x7D110` | 632 | UnwindData |  |
| 160 | `LsaIModifyPerformanceCounter` | `0x7DD90` | 132 | UnwindData |  |
| 271 | `LsapDbUpdateCountCompUnmappedNames` | `0x81680` | 23,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `LsaICryptUnprotectData` | `0x87080` | 134 | UnwindData |  |
| 109 | `LsaIFree_LSAPR_CR_CIPHER_VALUE` | `0x87310` | 3,376 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `LsaIFreeSupplementalTokenInfo` | `0x88040` | 45 | UnwindData |  |
| 92 | `LsaIEqualSupplementalTokenInfo` | `0x88230` | 63 | UnwindData |  |
| 299 | `LsapRemoveTrailingDot` | `0x888B0` | 8,464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 200 | `LsaIUpdateLogonSession` | `0x8A9C0` | 826 | UnwindData |  |
| 188 | `LsaISetLogonInfo` | `0x8AD00` | 642 | UnwindData |  |
| 98 | `LsaIFilterSids` | `0x8C280` | 3,472 | UnwindData |  |
| 183 | `LsaISafeMode` | `0x8D2D0` | 67 | UnwindData |  |
| 161 | `LsaINoConnectedUserPolicy` | `0x8D590` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 313 | `LsarLookupSids` | `0x8D790` | 515 | UnwindData |  |
| 297 | `LsapOpenSam` | `0x90140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 217 | `LsapCrServerGetSessionKey` | `0x90150` | 134 | UnwindData |  |
| 94 | `LsaIEventWritePackageNotCacheLogonUser` | `0x91450` | 202 | UnwindData |  |
| 82 | `LsaICryptProtectData` | `0x91D10` | 131 | UnwindData |  |
| 193 | `LsaISetUserFlags` | `0x91DA0` | 48 | UnwindData |  |
| 77 | `LsaICheckProtectedUserByTokenInfo` | `0x91E00` | 195 | UnwindData |  |
| 34 | *Ordinal Only* | `0x91F70` | 543 | UnwindData |  |
| 179 | `LsaIRegisterNotification` | `0x92CB0` | 637 | UnwindData |  |
| 35 | *Ordinal Only* | `0x93400` | 35 | UnwindData |  |
| 314 | `LsarOpenPolicy` | `0x934F0` | 28 | UnwindData |  |
| 66 | `LsaIAuditLogonEx` | `0x94460` | 147 | UnwindData |  |
| 134 | `LsaIGetLogonGuid` | `0x948F0` | 289 | UnwindData |  |
| 145 | `LsaIImpersonateClient` | `0x94AA0` | 3,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 158 | `LsaILookupUserAccountType` | `0x95A10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 269 | `LsapDbSidToLogicalNameObject` | `0x95A30` | 72 | UnwindData |  |
| 249 | `LsapDbInitializeAttribute` | `0x95B80` | 13,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `LsaIIsInEmulatedDomainJoinMode` | `0x98F80` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | *Ordinal Only* | `0x98FD0` | 516 | UnwindData |  |
| 322 | `LsarSetSecret` | `0x991E0` | 126 | UnwindData |  |
| 154 | `LsaIIsSuppressChannelBindingInfo` | `0x992E0` | 1,648 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `LsaIFree_LSAPR_TRANSLATED_NAMES` | `0x99950` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 171 | `LsaIQueryInformationPolicyTrusted` | `0x99CA0` | 1,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `LsaICheckRestrictedMode` | `0x9A3C0` | 4,336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `LsaIIsLocalHost` | `0x9B4B0` | 43 | UnwindData |  |
| 257 | `LsapDbLookupNamesInPrimaryDomain` | `0x9CA00` | 1,289 | UnwindData |  |
| 135 | `LsaIGetNameFromLuid` | `0x9E0C0` | 194 | UnwindData |  |
| 75 | `LsaICancelNotification` | `0x9E9D0` | 35 | UnwindData |  |
| 36 | *Ordinal Only* | `0x9EDF0` | 50 | UnwindData |  |
| 65 | `LsaIAuditKerberosLogon` | `0x9EE30` | 148 | UnwindData |  |
| 23 | *Ordinal Only* | `0x9F9F0` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `LsaIIsTargetPrivate` | `0x9FD40` | 248 | UnwindData |  |
| 142 | `LsaIGetSupplementalTokenInfo` | `0xA1C00` | 187 | UnwindData |  |
| 191 | `LsaISetSupplementalTokenInfo` | `0xA1CD0` | 1,398 | UnwindData |  |
| 62 | `LsaIAuditAccountLogonEx` | `0xA3EA0` | 1,229 | UnwindData |  |
| 67 | `LsaIAuditLogonUsingExplicitCreds` | `0xA4380` | 1,326 | UnwindData |  |
| 304 | `LsapSetErrorInfo` | `0xB2E40` | 183 | UnwindData |  |
| 163 | `LsaINotifyChangeNotification` | `0xB39C0` | 316 | UnwindData |  |
| 53 | `LsaDbLookupSidChainRequest` | `0xB4130` | 151 | UnwindData |  |
| 250 | `LsapDbIsStatusConnectionFailure` | `0xB5850` | 2,400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | *Ordinal Only* | `0xB61B0` | 2,800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | *Ordinal Only* | `0xB6CA0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 231 | `LsapDbEnumerateSids` | `0xB6DA0` | 548 | UnwindData |  |
| 207 | `LsapAdtGetCallerProcessInfo` | `0xB9200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 208 | `LsapAdtWriteLog` | `0xB9210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 212 | `LsapAuditFailed` | `0xB9220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 298 | `LsapQueryClientInfo` | `0xB9230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 305 | `LsapSidListSize` | `0xB9240` | 31,600 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `LsaIGetCcgClient` | `0xC0DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `LsaIIsContainerized` | `0xC0DC0` | 24,112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `LsaINotifyNewPassword` | `0xC6BF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 167 | `LsaINotifyPasswordChanged` | `0xC6C00` | 208 | UnwindData |  |
| 90 | `LsaIEfsAcceptSmartcardCredentials` | `0xC8460` | 486 | UnwindData |  |
| 93 | `LsaIEventWritePackageNoCredential` | `0xCE740` | 287 | UnwindData |  |
| 178 | `LsaIRegisterLogonSessionCallback` | `0xCE870` | 90 | UnwindData |  |
| 187 | `LsaISetLogonGuidInLogonSession` | `0xCE8D0` | 320 | UnwindData |  |
| 190 | `LsaISetPackageAttrInLogonSession` | `0xCEA20` | 48 | UnwindData |  |
| 196 | `LsaIUnregisterLogonSessionCallback` | `0xCEA60` | 98 | UnwindData |  |
| 276 | `LsapDomainRenameHandlerForLogonSessions` | `0xCEAD0` | 648 | UnwindData |  |
| 81 | `LsaICopyToTokenInfoFromHandle` | `0xD00E0` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `InitializeLsaExtension` | `0xD0310` | 49 | UnwindData |  |
| 50 | `QueryLsaInterface` | `0xD0D10` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `LsaICryptProtectDataEx` | `0xD0E10` | 155 | UnwindData |  |
| 85 | `LsaICryptUnprotectDataEx` | `0xD0EC0` | 157 | UnwindData |  |
| 88 | `LsaIDeriveCredentialKey` | `0xD0F70` | 274 | UnwindData |  |
| 308 | `LsapTruncateUnicodeString` | `0xD1270` | 10,320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `LsaIAllowProtectedCredLogon` | `0xD3AC0` | 218 | UnwindData |  |
| 137 | `LsaIGetNego2Package` | `0xD6EC0` | 192 | UnwindData |  |
| 199 | `LsaIUpdateKerbMaxTokenSize` | `0xD6F90` | 147 | UnwindData |  |
| 86 | `LsaIDereferenceCredHandle` | `0xD9010` | 46 | UnwindData |  |
| 87 | `LsaIDereferenceCtxtHandle` | `0xD9050` | 46 | UnwindData |  |
| 176 | `LsaIReferenceCredHandle` | `0xD9090` | 221 | UnwindData |  |
| 177 | `LsaIReferenceCtxtHandle` | `0xD9180` | 221 | UnwindData |  |
| 74 | `LsaICallPackagePassthrough` | `0xDB110` | 309 | UnwindData |  |
| 91 | `LsaIEqualLogonProcessName` | `0xDB250` | 81 | UnwindData |  |
| 95 | `LsaIExtractTargetInfo` | `0xDB2B0` | 288 | UnwindData |  |
| 139 | `LsaIGetRemoteCredGuardLogonBuffer` | `0xDB3E0` | 336 | UnwindData |  |
| 140 | `LsaIGetRemoteCredGuardSupplementalCreds` | `0xDB540` | 290 | UnwindData |  |
| 201 | `LsaIValidateTargetInfo` | `0xDB670` | 350 | UnwindData |  |
| 138 | `LsaIGetNetworkInfo` | `0xDE790` | 248 | UnwindData |  |
| 32 | *Ordinal Only* | `0xDF980` | 180 | UnwindData |  |
| 151 | `LsaIIsLastInteractiveLogonInfoEnabled` | `0xDFA40` | 50,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `LsaIInitializeNetlogonFuncPtrs` | `0xEBF40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `LsaIIsMachineSecureByDefault` | `0xEBF60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 279 | `LsapDssetupInitializeGetPrimaryDomainInformationOpState` | `0xEBF70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 293 | `LsapInitLsa` | `0xEBF90` | 1,963 | UnwindData |  |
| 39 | *Ordinal Only* | `0xECA80` | 38 | UnwindData |  |
| 42 | `LsaIIsUserMSA` | `0xECDB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `LsaIRenewCertificate` | `0xECDD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `LsaIFlushIdentityCacheForSid` | `0xECDF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `LsaIGetTokenInformationForLocalUser` | `0xECE10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `LsaISanitizeSAMName` | `0xECE20` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `LsaLookupPerfCounterDecrementCount` | `0xECF50` | 37 | UnwindData |  |
| 47 | `LsaLookupPerfCounterDecrementLargeCount` | `0xECF80` | 38 | UnwindData |  |
| 49 | `LsaLookupPerfCounterIncrementLargeCount` | `0xECFB0` | 38 | UnwindData |  |
| 56 | `LsaIAdtAuditingEnabledByCategory` | `0xEE980` | 118 | UnwindData |  |
| 57 | `LsaIAdtAuditingEnabledBySubCategory` | `0xEEA00` | 344 | UnwindData |  |
| 61 | `LsaIAuditAccountLogon` | `0xEEB60` | 56 | UnwindData |  |
| 63 | `LsaIAuditInitializeParametersAndWriteEvent` | `0xEEBA0` | 229 | UnwindData |  |
| 64 | `LsaIAuditKdcEvent` | `0xEEC90` | 1,192 | UnwindData |  |
| 68 | `LsaIAuditNotifyPackageLoad` | `0xEF140` | 485 | UnwindData |  |
| 69 | `LsaIAuditPasswordAccessEvent` | `0xEF330` | 527 | UnwindData |  |
| 70 | `LsaIAuditReplay` | `0xEF550` | 1,373 | UnwindData |  |
| 205 | `LsaIWriteAuditEvent` | `0xEFAC0` | 228 | UnwindData |  |
| 206 | `LsaIWriteKdcAuthenticationEvent` | `0xEFBB0` | 943 | UnwindData |  |
| 107 | `LsaIFree_LSAI_SECRET_ENUM_BUFFER` | `0xEFF70` | 82 | UnwindData |  |
| 108 | `LsaIFree_LSAPR_ACCOUNT_ENUM_BUFFER` | `0xEFFD0` | 90 | UnwindData |  |
| 110 | `LsaIFree_LSAPR_POLICY_DOMAIN_INFORMATION` | `0xF0030` | 30 | UnwindData |  |
| 112 | `LsaIFree_LSAPR_PRIVILEGE_ENUM_BUFFER` | `0xF0060` | 83 | UnwindData |  |
| 115 | `LsaIFree_LSAPR_SR_SECURITY_DESCRIPTOR` | `0xF00C0` | 40 | UnwindData |  |
| 122 | `LsaIFree_LSAPR_UNICODE_STRING` | `0xF00C0` | 40 | UnwindData |  |
| 117 | `LsaIFree_LSAPR_TRANSLATED_SIDS` | `0xF00F0` | 36 | UnwindData |  |
| 118 | `LsaIFree_LSAPR_TRUSTED_DOMAIN_INFO` | `0xF0120` | 45 | UnwindData |  |
| 119 | `LsaIFree_LSAPR_TRUSTED_ENUM_BUFFER` | `0xF0160` | 20 | UnwindData |  |
| 120 | `LsaIFree_LSAPR_TRUSTED_ENUM_BUFFER_EX` | `0xF0180` | 20 | UnwindData |  |
| 121 | `LsaIFree_LSAPR_TRUST_INFORMATION` | `0xF01A0` | 40 | UnwindData |  |
| 123 | `LsaIFree_LSAPR_UNICODE_STRING_BUFFER` | `0xF01D0` | 20 | UnwindData |  |
| 18 | *Ordinal Only* | `0xF01F0` | 56 | UnwindData |  |
| 19 | *Ordinal Only* | `0xF01F0` | 56 | UnwindData |  |
| 20 | *Ordinal Only* | `0xF0230` | 110 | UnwindData |  |
| 214 | `LsapCheckBootMode` | `0xF0430` | 304 | UnwindData |  |
| 192 | `LsaISetTokenDacl` | `0xF1800` | 243 | UnwindData |  |
| 211 | `LsapAuOpenSam` | `0xF32F0` | 1,276 | UnwindData |  |
| 218 | `LsapCrServerGetSessionKeySafe` | `0xF3800` | 82 | UnwindData |  |
| 286 | `LsapGetCapeNamesForCap` | `0xF42C0` | 438 | UnwindData |  |
| 325 | `ServiceInit` | `0xF4FF0` | 374 | UnwindData |  |
| 326 | `_fgs__LSAPR_TRUSTED_DOMAIN_FULL_INFORMATION2` | `0xF5410` | 28 | UnwindData |  |
| 327 | `_fgs__LSAPR_TRUSTED_DOMAIN_INFORMATION_EX2` | `0xF5440` | 60 | UnwindData |  |
| 329 | `_fgs__LSAPR_TRUSTED_ENUM_BUFFER_EX` | `0xF5490` | 74 | UnwindData |  |
| 331 | `_fgu__LSAPR_TRUSTED_DOMAIN_INFO` | `0xF54E0` | 173 | UnwindData |  |
| 26 | *Ordinal Only* | `0xFED70` | 414 | UnwindData |  |
| 25 | *Ordinal Only* | `0xFEF20` | 336 | UnwindData |  |
| 168 | `LsaIOpenPolicyTrusted` | `0xFFA30` | 33 | UnwindData |  |
| 321 | `LsarSetInformationPolicy` | `0xFFF40` | 792 | UnwindData |  |
| 255 | `LsapDbLookupMergeDisjointReferencedDomains` | `0x101A10` | 696 | UnwindData |  |
| 256 | `LsapDbLookupNameChainRequest` | `0x101CD0` | 151 | UnwindData |  |
| 290 | `LsapGetLookupRestrictIsolatedNameLevel` | `0x101D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 295 | `LsapIsBuiltinDomain` | `0x101D80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 302 | `LsapRtlValidateControllerTrustedDomain` | `0x101DA0` | 417 | UnwindData |  |
| 303 | `LsapRtlValidateControllerTrustedDomainByHandle` | `0x101F50` | 158 | UnwindData |  |
| 76 | `LsaIChangeSecretCipherKey` | `0x102B40` | 171 | UnwindData |  |
| 79 | `LsaIClearOldSyskey` | `0x102C00` | 68 | UnwindData |  |
| 144 | `LsaIHealthCheck` | `0x102C50` | 196 | UnwindData |  |
| 189 | `LsaISetNewSyskey` | `0x102D20` | 475 | UnwindData |  |
| 89 | `LsaIDsNotifiedObjectChange` | `0x102F10` | 138 | UnwindData |  |
| 96 | `LsaIFilterInboundNamespace` | `0x102FA0` | 128 | UnwindData |  |
| 97 | `LsaIFilterNamespace` | `0x103030` | 125 | UnwindData |  |
| 100 | `LsaIForestTrustFindMatch` | `0x1030C0` | 89 | UnwindData |  |
| 101 | `LsaIFreeFilterInboundNamespaceResult` | `0x103120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `LsaIFreeForestTrustInfo` | `0x103130` | 47 | UnwindData |  |
| 128 | `LsaIFree_LSA_FOREST_TRUST_COLLISION_INFORMATION` | `0x103170` | 47 | UnwindData |  |
| 129 | `LsaIFree_LSA_FOREST_TRUST_INFORMATION` | `0x1031B0` | 47 | UnwindData |  |
| 132 | `LsaIGetClientOsInfo` | `0x1031F0` | 107 | UnwindData |  |
| 133 | `LsaIGetForestTrustInformation` | `0x103270` | 60 | UnwindData |  |
| 141 | `LsaIGetSiteName` | `0x1032C0` | 60 | UnwindData |  |
| 148 | `LsaIIsDomainWithinForest` | `0x103310` | 140 | UnwindData |  |
| 149 | `LsaIIsDsPaused` | `0x1033B0` | 44 | UnwindData |  |
| 156 | `LsaIIsTrustedDomainsEnabled` | `0x1033F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `LsaIKerberosRegisterTrustNotification` | `0x103400` | 73 | UnwindData |  |
| 162 | `LsaINoMoreWin2KDomain` | `0x103450` | 44 | UnwindData |  |
| 164 | `LsaINotifyGCStatusChange` | `0x103490` | 45 | UnwindData |  |
| 169 | `LsaIQueryForestTrustInfo` | `0x1034D0` | 75 | UnwindData |  |
| 170 | `LsaIQueryForestTrustInformation` | `0x103530` | 28 | UnwindData |  |
| 173 | `LsaIQuerySiteInfo` | `0x103560` | 60 | UnwindData |  |
| 174 | `LsaIQuerySubnetInfo` | `0x1035B0` | 60 | UnwindData |  |
| 175 | `LsaIQueryUpnSuffixes` | `0x103600` | 60 | UnwindData |  |
| 181 | `LsaIReplicateClientObject` | `0x103650` | 75 | UnwindData |  |
| 184 | `LsaISamIndicatedDsStarted` | `0x1036B0` | 73 | UnwindData |  |
| 186 | `LsaISetClientDnsHostName` | `0x103700` | 138 | UnwindData |  |
| 198 | `LsaIUpdateForestTrustInformation` | `0x103790` | 91 | UnwindData |  |
| 202 | `LsaIVerifyCachability` | `0x103800` | 37 | UnwindData |  |
| 203 | `LsaIVerifyCachabilityEx` | `0x103830` | 28 | UnwindData |  |
| 277 | `LsapDsInitializeDsStateInfo` | `0x103860` | 55 | UnwindData |  |
| 278 | `LsapDsUnitializeDsStateInfo` | `0x1038A0` | 63 | UnwindData |  |
| 124 | `LsaIFree_LSAP_SITENAME_INFO` | `0x104370` | 42 | UnwindData |  |
| 125 | `LsaIFree_LSAP_SITE_INFO` | `0x1043A0` | 72 | UnwindData |  |
| 127 | `LsaIFree_LSAP_UPN_SUFFIXES` | `0x1043A0` | 72 | UnwindData |  |
| 126 | `LsaIFree_LSAP_SUBNET_INFO` | `0x1043F0` | 98 | UnwindData |  |
| 165 | `LsaINotifyNetlogonParametersChangeW` | `0x104460` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `LsaILookupWellKnownName` | `0x104760` | 31 | UnwindData |  |
| 180 | `LsaIRegisterPolicyChangeNotificationCallback` | `0x104F60` | 307 | UnwindData |  |
| 195 | `LsaIUnregisterAllPolicyChangeNotificationCallback` | `0x1050A0` | 355 | UnwindData |  |
| 197 | `LsaIUnregisterPolicyChangeNotificationCallback` | `0x105210` | 301 | UnwindData |  |
| 311 | `LsarDeleteObject` | `0x1056C0` | 65 | UnwindData |  |
| 194 | `LsaITransformAuthorizationData` | `0x105710` | 445 | UnwindData |  |
| 213 | `LsapBuildPrivilegeAuditString` | `0x105EF0` | 529 | UnwindData |  |
| 221 | `LsapDbBuildObjectCaches` | `0x108B90` | 34 | UnwindData |  |
| 222 | `LsapDbCloseHandle` | `0x108C10` | 180 | UnwindData |  |
| 227 | `LsapDbDeleteAttributesObject` | `0x109140` | 174 | UnwindData |  |
| 224 | `LsapDbCopyUnicodeAttribute` | `0x1097F0` | 175 | UnwindData |  |
| 225 | `LsapDbCopyUnicodeAttributeNoAlloc` | `0x1098B0` | 105 | UnwindData |  |
| 244 | `LsapDbFreeAttributes` | `0x109920` | 77 | UnwindData |  |
| 259 | `LsapDbMakeGuidAttribute` | `0x109980` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 260 | `LsapDbMakeSidAttribute` | `0x1099E0` | 138 | UnwindData |  |
| 261 | `LsapDbMakeUnicodeAttribute` | `0x109A70` | 257 | UnwindData |  |
| 264 | `LsapDbReadAttribute` | `0x109B80` | 328 | UnwindData |  |
| 232 | `LsapDbEnumerateTrustedDomainsEx` | `0x10A1B0` | 487 | UnwindData |  |
| 245 | `LsapDbFreeTrustedDomainsEx` | `0x10A3A0` | 71 | UnwindData |  |
| 270 | `LsapDbSlowEnumerateTrustedDomains` | `0x10A3F0` | 281 | UnwindData |  |
| 312 | `LsarEnumerateTrustedDomainsEx` | `0x10A670` | 186 | UnwindData |  |
| 319 | `LsarQueryTrustedDomainInfoByName` | `0x10A7E0` | 733 | UnwindData |  |
| 323 | `LsarSetTrustedDomainInfoByName` | `0x10AAD0` | 558 | UnwindData |  |
| 233 | `LsapDbExpAcquireReadLockTrustedDomainList` | `0x10AD10` | 42 | UnwindData |  |
| 234 | `LsapDbExpAcquireWriteLockTrustedDomainList` | `0x10AD40` | 42 | UnwindData |  |
| 235 | `LsapDbExpConvertReadLockTrustedDomainListToExclusive` | `0x10AD70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 236 | `LsapDbExpConvertWriteLockTrustedDomainListToShared` | `0x10AD90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 237 | `LsapDbExpIsCacheBuilding` | `0x10ADB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 238 | `LsapDbExpIsCacheValid` | `0x10ADD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 239 | `LsapDbExpIsLockedTrustedDomainList` | `0x10ADF0` | 64 | UnwindData |  |
| 240 | `LsapDbExpMakeCacheBuilding` | `0x10AE40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 241 | `LsapDbExpMakeCacheInvalid` | `0x10AE60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 242 | `LsapDbExpMakeCacheValid` | `0x10AE80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 243 | `LsapDbExpReleaseLockTrustedDomainList` | `0x10AEA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 246 | `LsapDbGetDbObjectTypeName` | `0x10AEC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 247 | `LsapDbGetDbPolicyHandle` | `0x10AEE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 273 | `LsapDbVerifyInfoQueryTrustedDomain` | `0x10AEF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 274 | `LsapDbVerifyInfoSetTrustedDomain` | `0x10AF10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 285 | `LsapGetAccountDomainHandle` | `0x10AF30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 287 | `LsapGetGlobalRestrictAnonymous` | `0x10AF40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 288 | `LsapGetHourlyLogLevel` | `0x10AF50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 291 | `LsapGetPolicyHandle` | `0x10AF60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 292 | `LsapGetWellKnownSid` | `0x10AF80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 294 | `LsapInitializeLsaDb` | `0x10AFA0` | 110 | UnwindData |  |
| 296 | `LsapIsSamOpened` | `0x10B020` | 7,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 316 | `LsarQueryDomainInformationPolicy` | `0x10CD60` | 272 | UnwindData |  |
| 320 | `LsarRetrievePrivateData` | `0x10D720` | 169 | UnwindData |  |
| 324 | `LsarStorePrivateData` | `0x10D8D0` | 246 | UnwindData |  |
| 15 | *Ordinal Only* | `0x18EF60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | *Ordinal Only* | `0x18EF70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | *Ordinal Only* | `0x18EF80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | *Ordinal Only* | `0x18EF90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | *Ordinal Only* | `0x18EFA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | *Ordinal Only* | `0x18EFB0` | 18,004 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | *Ordinal Only* | `0x193604` | 60 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | *Ordinal Only* | `0x193640` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | *Ordinal Only* | `0x193644` | 1,356 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | *Ordinal Only* | `0x193B90` | 184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | *Ordinal Only* | `0x193C48` | 120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | *Ordinal Only* | `0x193CC0` | 7,352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | *Ordinal Only* | `0x195978` | 2,384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | *Ordinal Only* | `0x1962C8` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | *Ordinal Only* | `0x1962F0` | 792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | *Ordinal Only* | `0x196608` | 0 | Indeterminate |  |
