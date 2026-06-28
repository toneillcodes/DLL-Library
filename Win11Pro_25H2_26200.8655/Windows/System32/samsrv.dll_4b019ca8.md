# Binary Specification: samsrv.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\samsrv.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4b019ca82e93cb4cee1ec240b00fd51984d51972727c8674d8e9f5557e7fa031`
* **Total Exported Functions:** 338

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 99 | `SamIUpdateLogonStatistics` | `0x1880` | 149 | UnwindData |  |
| 257 | `SampReleaseWriteLock` | `0x28C0` | 194 | UnwindData |  |
| 105 | `SampAcquireWriteLock` | `0x2990` | 257 | UnwindData |  |
| 221 | `SampGetUserAccountSettings` | `0x2AA0` | 189 | UnwindData |  |
| 211 | `SampGetReverseMembershipTransitive` | `0x3EC0` | 938 | UnwindData |  |
| 48 | `SamIGetUserLogonInformation2` | `0x4270` | 90 | UnwindData |  |
| 320 | `SamrLookupNamesInDomain` | `0x47B0` | 521 | UnwindData |  |
| 321 | `SamrLookupNamesInDomain2` | `0x4CA0` | 12 | UnwindData |  |
| 318 | `SamrLookupDomainInSamServer` | `0x4E90` | 10 | UnwindData |  |
| 60 | `SamILookupNamesInDomain` | `0x52E0` | 15 | UnwindData |  |
| 147 | `SampDeleteContext` | `0x7240` | 531 | UnwindData |  |
| 325 | `SamrOpenUser` | `0x7880` | 972 | UnwindData |  |
| 136 | `SampCreateAccountContext2` | `0x83E0` | 215 | UnwindData |  |
| 138 | `SampCreateContextEx` | `0x90A0` | 101 | UnwindData |  |
| 144 | `SampDeReferenceContext` | `0x97A0` | 38 | UnwindData |  |
| 319 | `SamrLookupIdsInDomain` | `0x9FA0` | 3,808 | UnwindData |  |
| 306 | `SamrCloseHandle` | `0xAEC0` | 570 | UnwindData |  |
| 291 | `SampTraceEvent` | `0xB520` | 802 | UnwindData |  |
| 333 | `SamrRidToSid` | `0xC290` | 35 | UnwindData |  |
| 219 | `SampGetUnicodeStringAttribute` | `0xD470` | 576 | UnwindData |  |
| 301 | `SampValidateRegAttributes` | `0xD7E0` | 50 | UnwindData |  |
| 208 | `SampGetObjectSD` | `0xDBA0` | 49 | UnwindData |  |
| 284 | `SampSetTransactionDomain` | `0xE170` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 199 | `SampGetFixedAttributes` | `0xE250` | 272 | UnwindData |  |
| 266 | `SampRetrieveUserPasswords` | `0xE370` | 142 | UnwindData |  |
| 330 | `SamrQuerySecurityObject` | `0xEF10` | 1,405 | UnwindData |  |
| 316 | `SamrGetGroupsForUser` | `0xF4A0` | 6 | UnwindData |  |
| 103 | `SampAcquireReadLock` | `0xFCF0` | 13 | UnwindData |  |
| 292 | `SampUpdateAccountDisabledFlag` | `0xFD90` | 1,385 | UnwindData |  |
| 313 | `SamrEnumerateUsersInDomain` | `0x10300` | 1,001 | UnwindData |  |
| 255 | `SampReleaseReadLock` | `0x11C80` | 184 | UnwindData |  |
| 155 | `SampDsIsRunning` | `0x11D40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 247 | `SampQueryInformationUserInternal` | `0x11D60` | 8,592 | UnwindData |  |
| 331 | `SamrRemoveMemberFromAlias` | `0x15750` | 12 | UnwindData |  |
| 315 | `SamrGetAliasMembership` | `0x15AB0` | 152 | UnwindData |  |
| 42 | `SamIGetAliasMembership` | `0x15B50` | 284 | UnwindData |  |
| 75 | `SamIQueryRealmList` | `0x16940` | 83 | UnwindData |  |
| 9 | `SamIAccountRestrictions` | `0x16DB0` | 761 | UnwindData |  |
| 322 | `SamrOpenAlias` | `0x170B0` | 728 | UnwindData |  |
| 267 | `SampRetrieveUserV1aFixed` | `0x174E0` | 145 | UnwindData |  |
| 251 | `SampReadExtendedAttributes` | `0x17580` | 422 | UnwindData |  |
| 38 | `SamIFree_SAMPR_RETURNED_USTRING_ARRAY` | `0x17730` | 22 | UnwindData |  |
| 293 | `SampUpdateComputedUserAccountControlBits` | `0x177A0` | 35 | UnwindData |  |
| 29 | `SamIFreeRealmList` | `0x17D70` | 12 | UnwindData |  |
| 39 | `SamIFree_SAMPR_ULONG_ARRAY` | `0x17E10` | 38 | UnwindData |  |
| 312 | `SamrEnumerateDomainsInSamServer` | `0x17E40` | 1,389 | UnwindData |  |
| 45 | `SamIGetResourceGroupMembershipsTransitive` | `0x183C0` | 332 | UnwindData |  |
| 46 | `SamIGetResourceGroupMembershipsTransitive2` | `0x18520` | 518 | UnwindData |  |
| 145 | `SampDecrementActiveThreads` | `0x18730` | 51 | UnwindData |  |
| 223 | `SampImpersonateClient` | `0x1A590` | 207 | UnwindData |  |
| 269 | `SampRtlWellKnownPrivilegeCheck` | `0x1A670` | 589 | UnwindData |  |
| 268 | `SampRevertToSelf` | `0x1A8D0` | 116 | UnwindData |  |
| 176 | `SampFreeUnicodeString` | `0x1A9A0` | 47 | UnwindData |  |
| 197 | `SampGetExtendedAttribute` | `0x1A9E0` | 17 | UnwindData |  |
| 232 | `SampIsInternetAccount` | `0x1AF90` | 80 | UnwindData |  |
| 143 | `SampCurrentThreadOwnsLock` | `0x1B520` | 1,472 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 285 | `SampSetTransactionWithinDomain` | `0x1BAE0` | 1,616 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `SampAuditAnyEvent` | `0x1C130` | 320 | UnwindData |  |
| 179 | `SampGetAccessAttribute` | `0x1C280` | 496 | UnwindData |  |
| 323 | `SamrOpenDomain` | `0x1C760` | 468 | UnwindData |  |
| 133 | `SampConnect` | `0x1CAC0` | 1,290 | UnwindData |  |
| 27 | `SamIFreeLookupSidsInfo` | `0x1D020` | 18 | UnwindData |  |
| 140 | `SampCreateFullSid` | `0x1D2E0` | 191 | UnwindData |  |
| 314 | `SamrEnumerateUsersInDomain2` | `0x1D4F0` | 1,039 | UnwindData |  |
| 288 | `SampSplitSid` | `0x1DA10` | 64 | UnwindData |  |
| 40 | `SamIFree_SAMPR_USER_INFO_BUFFER` | `0x1E560` | 40 | UnwindData |  |
| 5 | `SAM_MIDL_user_allocate` | `0x1E7E0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `SamDsExtAlloc` | `0x1E7E0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 328 | `SamrQueryInformationUser` | `0x1E890` | 294 | UnwindData |  |
| 329 | `SamrQueryInformationUser2` | `0x1E890` | 294 | UnwindData |  |
| 1 | `RtlDeleteElementGenericTable2` | `0x1E9C0` | 580 | UnwindData |  |
| 31 | `SamIFreeSidAndAttributesList` | `0x1EDE0` | 95 | UnwindData |  |
| 3 | `RtlInsertElementGenericTable2` | `0x1EED0` | 746 | UnwindData |  |
| 32 | `SamIFreeSidArray` | `0x1F210` | 105 | UnwindData |  |
| 238 | `SampNeedUserAccountSettingsDuringQuery` | `0x1F2E0` | 704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 215 | `SampGetSidArrayAttribute` | `0x1F5A0` | 412 | UnwindData |  |
| 108 | `SampAddDeltaTime` | `0x1F9C0` | 35 | UnwindData |  |
| 277 | `SampSetExtendedAttributeAccess` | `0x1FA70` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 236 | `SampLookupContext` | `0x1FBC0` | 26 | UnwindData |  |
| 4 | `RtlLookupElementGenericTable2` | `0x20890` | 196 | UnwindData |  |
| 6 | `SAM_MIDL_user_free` | `0x20AF0` | 2,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `SamDsExtFree` | `0x20AF0` | 2,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `SamIFreeVoid` | `0x20AF0` | 2,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `SampDsGetPrimaryDomainStart` | `0x213C0` | 1,872 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `SamIFreeSecurityAttributesInfo` | `0x21B10` | 62 | UnwindData |  |
| 253 | `SampReferenceContext` | `0x21D20` | 1,600 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `SampCheckSidType` | `0x22360` | 449 | UnwindData |  |
| 263 | `SampReplaceUserV1aFixed` | `0x22FB0` | 110 | UnwindData |  |
| 278 | `SampSetFixedAttributes` | `0x23030` | 323 | UnwindData |  |
| 104 | `SampAcquireSamLockExclusive` | `0x23210` | 71 | UnwindData |  |
| 256 | `SampReleaseSamLockExclusive` | `0x23260` | 52 | UnwindData |  |
| 289 | `SampStoreObjectAttributes` | `0x23580` | 85 | UnwindData |  |
| 165 | `SampDuplicateUnicodeString` | `0x239C0` | 122 | UnwindData |  |
| 295 | `SampUpdatePerformanceCounters` | `0x23B70` | 60 | UnwindData |  |
| 13 | `SamIConnect` | `0x23CF0` | 47 | UnwindData |  |
| 225 | `SampIncrementActiveThreads` | `0x23D70` | 46 | UnwindData |  |
| 297 | `SampUsingDsData` | `0x23EC0` | 8,848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `SamIAddDSNameToAlias` | `0x26150` | 514 | UnwindData |  |
| 80 | `SamIRemoveDSNameFromAlias` | `0x26360` | 457 | UnwindData |  |
| 124 | `SampChangeAliasAccountName` | `0x26C30` | 337 | UnwindData |  |
| 304 | `SamrAddMemberToAlias` | `0x28070` | 660 | UnwindData |  |
| 309 | `SamrDeleteAlias` | `0x28410` | 909 | UnwindData |  |
| 317 | `SamrGetMembersInAlias` | `0x287B0` | 317 | UnwindData |  |
| 334 | `SamrSetInformationAlias` | `0x28A00` | 789 | UnwindData |  |
| 112 | `SampAlInvalidateAliasInformation` | `0x29C30` | 67 | UnwindData |  |
| 135 | `SampCopyUserSupplementalCredentialsForDCPromo` | `0x2B430` | 465 | UnwindData |  |
| 152 | `SampDsConvertReadAttrBlock` | `0x2B710` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `SampDsMakeAttrBlock` | `0x2B750` | 228 | UnwindData |  |
| 160 | `SampDsUpdateContextAttributes` | `0x2B9D0` | 172 | UnwindData |  |
| 216 | `SampGetSidAttribute` | `0x2BC60` | 174 | UnwindData |  |
| 218 | `SampGetUlongArrayAttribute` | `0x2BD20` | 212 | UnwindData |  |
| 237 | `SampMarkPerAttributeInvalidFromWhichFields` | `0x2BFE0` | 206 | UnwindData |  |
| 254 | `SampRegObjToDsObj` | `0x2C350` | 574 | UnwindData |  |
| 270 | `SampSetAccessAttribute` | `0x2C5A0` | 96 | UnwindData |  |
| 286 | `SampSetUnicodeStringAttribute` | `0x2C7D0` | 127 | UnwindData |  |
| 296 | `SampUpgradeUserParmsActual` | `0x2D5A0` | 289 | UnwindData |  |
| 19 | `SamIDecodeClaimsBlobToAuthz` | `0x2D890` | 65 | UnwindData |  |
| 23 | `SamIFreeAuthzSecurityAttributesInfo` | `0x2D8E0` | 62 | UnwindData |  |
| 12 | `SamIClaimIsValid` | `0x3ECC0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `SamIConvertSecurityAttributesToClaimsBlob` | `0x3ED70` | 620 | UnwindData |  |
| 17 | `SamIDecodeClaimsBlob` | `0x3EFF0` | 65 | UnwindData |  |
| 18 | `SamIDecodeClaimsBlobIntoClaimsSet` | `0x3F040` | 121 | UnwindData |  |
| 24 | `SamIFreeClaimsBlob` | `0x3F0C0` | 49 | UnwindData |  |
| 25 | `SamIFreeDecodedClaimsSet` | `0x3F100` | 140 | UnwindData |  |
| 95 | `SamITransformClaims` | `0x3F1A0` | 114 | UnwindData |  |
| 84 | `SamIRetrieveMultiplePrimaryCredentials` | `0x40D00` | 155 | UnwindData |  |
| 85 | `SamIRetrieveNGCKeyCredential` | `0x40DB0` | 148 | UnwindData |  |
| 86 | `SamIRetrievePrimaryCredentials` | `0x40E50` | 94 | UnwindData |  |
| 94 | `SamIStorePrimaryCredentials` | `0x40EC0` | 194 | UnwindData |  |
| 146 | `SampDecryptCredentialData` | `0x412B0` | 223 | UnwindData |  |
| 167 | `SampEncryptCredentialData` | `0x41420` | 482 | UnwindData |  |
| 250 | `SampQueryUserSupplementalCredentialsRegistry` | `0x417A0` | 224 | UnwindData |  |
| 265 | `SampRetrieveMultipleCredentials` | `0x41A70` | 207 | UnwindData |  |
| 131 | `SampCompareDisplayStrings` | `0x42170` | 122 | UnwindData |  |
| 161 | `SampDuplicateGroupInfo` | `0x42620` | 147 | UnwindData |  |
| 162 | `SampDuplicateMachineInfo` | `0x42620` | 147 | UnwindData |  |
| 163 | `SampDuplicateOemGroupInfo` | `0x426C0` | 86 | UnwindData |  |
| 164 | `SampDuplicateOemUserInfo` | `0x426C0` | 86 | UnwindData |  |
| 166 | `SampDuplicateUserInfo` | `0x42720` | 195 | UnwindData |  |
| 172 | `SampFreeGroupInfo` | `0x42890` | 32 | UnwindData |  |
| 173 | `SampFreeMachineInfo` | `0x42890` | 32 | UnwindData |  |
| 174 | `SampFreeOemGroupInfo` | `0x428C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 175 | `SampFreeOemUserInfo` | `0x428C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 177 | `SampFreeUserInfo` | `0x428D0` | 41 | UnwindData |  |
| 326 | `SamrQueryDisplayInformation` | `0x43940` | 138 | UnwindData |  |
| 22 | `SamIDoFSMORoleChange` | `0x44420` | 129 | UnwindData |  |
| 59 | `SamILookupNamesBySid` | `0x444B0` | 706 | UnwindData |  |
| 61 | `SamILookupSidsByName` | `0x44780` | 699 | UnwindData |  |
| 68 | `SamINotifyRoleChange` | `0x44A50` | 548 | UnwindData |  |
| 76 | `SamIQueryServerRole` | `0x44C80` | 103 | UnwindData |  |
| 77 | `SamIQueryServerRole2` | `0x44CF0` | 178 | UnwindData |  |
| 137 | `SampCreateAliasInDomain` | `0x44EE0` | 2,026 | UnwindData |  |
| 141 | `SampCreateGroupInDomain` | `0x456D0` | 2,166 | UnwindData |  |
| 142 | `SampCreateUserInDomain` | `0x45F50` | 3,680 | UnwindData |  |
| 213 | `SampGetSerialNumberDomain2` | `0x471D0` | 207 | UnwindData |  |
| 283 | `SampSetSerialNumberDomain2` | `0x48D80` | 314 | UnwindData |  |
| 307 | `SamrCreateUser2InDomain` | `0x49170` | 403 | UnwindData |  |
| 308 | `SamrCreateUserInDomain` | `0x49310` | 356 | UnwindData |  |
| 327 | `SamrQueryInformationDomain` | `0x49700` | 1,497 | UnwindData |  |
| 64 | `SamIMixedDomain` | `0x4AC10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `SamIMixedDomain2` | `0x4AC40` | 195 | UnwindData |  |
| 154 | `SampDsInitializeSingleDomain` | `0x4AFD0` | 594 | UnwindData |  |
| 157 | `SampDsSetBuiltinDomainPolicy` | `0x4B230` | 279 | UnwindData |  |
| 158 | `SampDsSetDomainPolicy` | `0x4B350` | 186 | UnwindData |  |
| 169 | `SampExtendDefinedDomains` | `0x4B410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `SamICreateKrbTgt` | `0x4B420` | 480 | UnwindData |  |
| 121 | `SampBuildDsNameFromSid` | `0x4B610` | 100 | UnwindData |  |
| 246 | `SampQueryDSRMAccountName` | `0x4B950` | 442 | UnwindData |  |
| 275 | `SampSetDSRMPasswordWorker` | `0x4BB10` | 457 | UnwindData |  |
| 55 | `SamIIsExtendedSidMode` | `0x4FA10` | 2,816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `RtlInitializeGenericTable2` | `0x50510` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `SampAddAccountToGroupMembers` | `0x50570` | 988 | UnwindData |  |
| 110 | `SampAddSameDomainMemberToGlobalOrUniversalGroup` | `0x50960` | 246 | UnwindData |  |
| 111 | `SampAddUserToGroup` | `0x50A60` | 183 | UnwindData |  |
| 125 | `SampChangeGroupAccountName` | `0x50B20` | 337 | UnwindData |  |
| 128 | `SampCheckGroupTypeBits` | `0x50C80` | 1,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 258 | `SampRemoveAccountFromGroupMembers` | `0x510C0` | 579 | UnwindData |  |
| 259 | `SampRemoveSameDomainMemberFromGlobalOrUniversalGroup` | `0x51310` | 194 | UnwindData |  |
| 260 | `SampRemoveUserFromGroup` | `0x513E0` | 183 | UnwindData |  |
| 264 | `SampRetrieveGroupV1Fixed` | `0x51700` | 70 | UnwindData |  |
| 303 | `SampWriteGroupType` | `0x51750` | 221 | UnwindData |  |
| 305 | `SamrAddMemberToGroup` | `0x51840` | 390 | UnwindData |  |
| 310 | `SamrDeleteGroup` | `0x519D0` | 1,304 | UnwindData |  |
| 324 | `SamrOpenGroup` | `0x52110` | 294 | UnwindData |  |
| 332 | `SamrRemoveMemberFromGroup` | `0x52590` | 387 | UnwindData |  |
| 335 | `SamrSetInformationGroup` | `0x52720` | 1,105 | UnwindData |  |
| 235 | `SampLogPrint` | `0x53880` | 222 | UnwindData |  |
| 78 | `SamIRandomizeStoredPassword` | `0x53F10` | 94 | UnwindData |  |
| 79 | `SamIRandomizeStoredPasswordWithoutExpirationCheck` | `0x54670` | 43 | UnwindData |  |
| 83 | `SamIResetBadPwdCountOnPdc` | `0x546B0` | 64 | UnwindData |  |
| 93 | `SamISetPasswordInfoOnDc` | `0x54700` | 538 | UnwindData |  |
| 150 | `SampDeltaChangeNotify` | `0x55260` | 281 | UnwindData |  |
| 224 | `SampIncreaseBadPwdCountLoopback` | `0x55450` | 451 | UnwindData |  |
| 242 | `SampPasswordChangeNotify` | `0x55E90` | 158 | UnwindData |  |
| 243 | `SampPasswordChangeNotifyWorker` | `0x56300` | 615 | UnwindData |  |
| 281 | `SampSetPasswordInfoOnPdcByHandle` | `0x56EE0` | 123 | UnwindData |  |
| 282 | `SampSetPasswordInfoOnPdcByIndex` | `0x56F70` | 3,808 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 338 | `SamrValidatePassword` | `0x57E50` | 561 | UnwindData |  |
| 20 | `SamIDemote` | `0x58710` | 159 | UnwindData |  |
| 21 | `SamIDemoteUndo` | `0x587C0` | 37 | UnwindData |  |
| 58 | `SamILoadDownlevelDatabase` | `0x587F0` | 505 | UnwindData |  |
| 70 | `SamIPromote` | `0x589F0` | 893 | UnwindData |  |
| 71 | `SamIPromoteUndo` | `0x58D80` | 22 | UnwindData |  |
| 81 | `SamIReplaceDownlevelDatabase` | `0x58DA0` | 930 | UnwindData |  |
| 97 | `SamIUnLoadDownlevelDatabase` | `0x59150` | 141 | UnwindData |  |
| 107 | `SampAddAccountsAndApplyMemberships` | `0x591F0` | 356 | UnwindData |  |
| 109 | `SampAddNonLocalDomainRelativeMemberships` | `0x594B0` | 129 | UnwindData |  |
| 114 | `SampApplyDomainUpdatesForAllDomains` | `0x5A400` | 286 | UnwindData |  |
| 148 | `SampDeleteDsDirsToDeleteKey` | `0x5B920` | 209 | UnwindData |  |
| 149 | `SampDeleteKeyForPostBootPromote` | `0x5BA00` | 296 | UnwindData |  |
| 178 | `SampGenerateRandomPassword` | `0x5C230` | 89 | UnwindData |  |
| 261 | `SampRenameKrbtgtAccount` | `0x5E0E0` | 1,058 | UnwindData |  |
| 271 | `SampSetAdminPassword` | `0x5E8E0` | 284 | UnwindData |  |
| 279 | `SampSetGlobalDsSids` | `0x5EB90` | 166 | UnwindData |  |
| 280 | `SampSetPassword` | `0x5EC40` | 73 | UnwindData |  |
| 116 | `SampAuditAccountEnableDisableChange` | `0x5F560` | 188 | UnwindData |  |
| 117 | `SampAuditAccountNameChange` | `0x5F630` | 150 | UnwindData |  |
| 119 | `SampAuditGroupTypeChange` | `0x60280` | 838 | UnwindData |  |
| 120 | `SampAuditSidHistory` | `0x605D0` | 166 | UnwindData |  |
| 26 | `SamIFreeLookupNamesInfo` | `0x62F10` | 312 | UnwindData |  |
| 34 | `SamIFree_SAMPR_DISPLAY_INFO_BUFFER` | `0x630F0` | 20 | UnwindData |  |
| 35 | `SamIFree_SAMPR_DOMAIN_INFO_BUFFER` | `0x63110` | 72 | UnwindData |  |
| 36 | `SamIFree_SAMPR_ENUMERATION_BUFFER` | `0x63160` | 102 | UnwindData |  |
| 37 | `SamIFree_SAMPR_GET_GROUPS_BUFFER` | `0x631D0` | 56 | UnwindData |  |
| 41 | `SamIFree_UserInternal6Information` | `0x63240` | 474 | UnwindData |  |
| 53 | `SamIInitialize` | `0x647A0` | 2,921 | UnwindData |  |
| 98 | `SamIUninitialize` | `0x654F0` | 55 | UnwindData |  |
| 229 | `SampIsAuditingEnabled` | `0x67A80` | 52,320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 248 | `SampQueryPolicyValue` | `0x746E0` | 4,064 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 273 | `SampSetCheckpointInfo` | `0x756C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 276 | `SampSetErrorInfo` | `0x756D0` | 260 | UnwindData |  |
| 272 | `SampSetAttributeAccess` | `0x76CF0` | 65 | UnwindData |  |
| 122 | `SampBuildSamProtection` | `0x76D40` | 1,069 | UnwindData |  |
| 204 | `SampGetNewAccountSecurityNt4` | `0x775E0` | 1,708 | UnwindData |  |
| 337 | `SamrSetSecurityObject` | `0x78A90` | 1,352 | UnwindData |  |
| 52 | `SamIImpersonateNullSession` | `0x78FE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `SamIRevertNullSession` | `0x79000` | 50 | UnwindData |  |
| 182 | `SampGetCurrentOwnerAndPrimaryGroup` | `0x79D10` | 327 | UnwindData |  |
| 299 | `SampValidateDomainControllerCreation` | `0x7A960` | 100 | UnwindData |  |
| 300 | `SampValidatePwdSettingAttempt` | `0x7A9D0` | 274 | UnwindData |  |
| 62 | `SamILoopbackConnect` | `0x7ACE0` | 28 | UnwindData |  |
| 63 | `SamILoopbackConnectEx` | `0x7AD10` | 330 | UnwindData |  |
| 74 | `SamIQueryCapabilities` | `0x7AE60` | 42 | UnwindData |  |
| 245 | `SampQueryCapabilities` | `0x7AE90` | 653 | UnwindData |  |
| 54 | `SamIIsDownlevelDcUpgrade` | `0x7B810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `SamIIsRebootAfterPromotion` | `0x7B820` | 25 | UnwindData |  |
| 57 | `SamIIsSetupInProgress` | `0x7B840` | 12,080 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 195 | `SampGetDomainUpgradeTasks` | `0x7E770` | 6,352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 252 | `SampRecordSystemSchemaVerisonInRegistry` | `0x80040` | 423 | UnwindData |  |
| 11 | `SamIChangePasswordForeignUser` | `0x81220` | 1,046 | UnwindData |  |
| 51 | `SamIHandleObjectUpdate` | `0x81640` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `SamIOpenUserByAlternateId` | `0x81670` | 258 | UnwindData |  |
| 88 | `SamIScorePassword` | `0x81780` | 433 | UnwindData |  |
| 90 | `SamISetMachinePassword` | `0x81940` | 107 | UnwindData |  |
| 91 | `SamISetPasswordForeignUser2` | `0x819C0` | 53 | UnwindData |  |
| 92 | `SamISetPasswordForeignUser3` | `0x81A00` | 1,511 | UnwindData |  |
| 102 | `SampAccountControlToFlags` | `0x821F0` | 1,440 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `SampAssignPrimaryGroup` | `0x82790` | 252 | UnwindData |  |
| 123 | `SampCalculateLmAndNtOwfPasswords` | `0x828A0` | 187 | UnwindData |  |
| 126 | `SampChangeUserAccountName` | `0x83860` | 648 | UnwindData |  |
| 127 | `SampCheckForAccountLockout` | `0x83EF0` | 103 | UnwindData |  |
| 132 | `SampComputePasswordExpired` | `0x84BE0` | 50 | UnwindData |  |
| 151 | `SampDsChangePasswordUser` | `0x860D0` | 685 | UnwindData |  |
| 159 | `SampDsSetPasswordUser` | `0x86390` | 751 | UnwindData |  |
| 170 | `SampFlagsToAccountControl` | `0x867D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 171 | `SampFlagsToAccountControlEx` | `0x867E0` | 430 | UnwindData |  |
| 210 | `SampGetPasswordMustChangeWithUF_UAC` | `0x87290` | 96 | UnwindData |  |
| 220 | `SampGetUserAccountControlComputed` | `0x873C0` | 141 | UnwindData |  |
| 262 | `SampReplaceUserLogonHours` | `0x889F0` | 1,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 287 | `SampSetUserAccountControl` | `0x88F10` | 1,512 | UnwindData |  |
| 311 | `SamrDeleteUser` | `0x8AF30` | 1,973 | UnwindData |  |
| 336 | `SamrSetInformationUser` | `0x8BE90` | 9,751 | UnwindData |  |
| 15 | `SamICopyCurrentDomainAccountSettings` | `0x8F430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `SamIFreeOidList` | `0x8F450` | 47 | UnwindData |  |
| 43 | `SamIGetConfigurationOidList` | `0x8F490` | 284 | UnwindData |  |
| 47 | `SamIGetUserLogonInformation` | `0x8F5C0` | 72 | UnwindData |  |
| 49 | `SamIGetUserLogonInformation3` | `0x8F610` | 97 | UnwindData |  |
| 50 | `SamIGetUserLogonInformationEx` | `0x8F680` | 77 | UnwindData |  |
| 67 | `SamINetLogonPing` | `0x8F6E0` | 199 | UnwindData |  |
| 72 | `SamIPurgeSecrets` | `0x8F7B0` | 345 | UnwindData |  |
| 73 | `SamIQueryAccountSecretsCachability` | `0x8F910` | 361 | UnwindData |  |
| 96 | `SamIUPNFromUserHandle` | `0x8FA80` | 196 | UnwindData |  |
| 44 | `SamIGetDefaultAdministratorName` | `0x90D30` | 234 | UnwindData |  |
| 66 | `SamINT4UpgradeInProgress` | `0x90E20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 203 | `SampGetNT4UpgradeInProgress` | `0x90E20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `SamIReplicateAccountData` | `0x90E30` | 320 | UnwindData |  |
| 89 | `SamISetAuditingInformation` | `0x90F80` | 96 | UnwindData |  |
| 100 | `SamIValidateAccountName` | `0x90FF0` | 79 | UnwindData |  |
| 101 | `SamIValidateNewAccountName` | `0x91050` | 972 | UnwindData |  |
| 113 | `SampAllocateNextCurrentRidFromIndex` | `0x91430` | 2,528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | `SampCommitBufferedWrites` | `0x91E10` | 276 | UnwindData |  |
| 134 | `SampConvertUiListToApiList` | `0x91F30` | 745 | UnwindData |  |
| 139 | `SampCreateDefaultUPN` | `0x92350` | 225 | UnwindData |  |
| 168 | `SampExamineSid` | `0x92590` | 249 | UnwindData |  |
| 180 | `SampGetAccountDomainInfo` | `0x92B20` | 191 | UnwindData |  |
| 181 | `SampGetBehaviorVersion` | `0x92BF0` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `SampGetDisableOutboundRSO` | `0x92D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | `SampGetDisableRSOOnPDCForward` | `0x92D80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `SampGetDisableResetBadPwdCountForward` | `0x92D90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `SampGetDisableSingleObjectRepl` | `0x92DA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 187 | `SampGetDnsDomainNameFromIndex` | `0x92DB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 188 | `SampGetDomainContextFromIndex` | `0x92DE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 189 | `SampGetDomainObjectFromAccountContext` | `0x92E00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `SampGetDomainObjectFromIndex` | `0x92E30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 191 | `SampGetDomainServerRoleFromIndex` | `0x92E60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 192 | `SampGetDomainSidFromAccountContext` | `0x92E80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 193 | `SampGetDomainSidFromIndex` | `0x92EB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 194 | `SampGetDomainSidListForSam` | `0x92ED0` | 362 | UnwindData |  |
| 196 | `SampGetDownLevelDomainControllersPresent` | `0x93040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 198 | `SampGetExternalNameFromIndex` | `0x93060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 200 | `SampGetHasNeverTime` | `0x93080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | `SampGetIgnoreGCFailures` | `0x93090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | `SampGetLogLevel` | `0x930A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 205 | `SampGetNextUnmodifiedRidFromIndex` | `0x930B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | `SampGetNoGcLogonEnforceKerberosIpCheck` | `0x930D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 207 | `SampGetNoGcLogonEnforceNTLMCheck` | `0x930E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 209 | `SampGetObjectTypeNameFromIndex` | `0x930F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 212 | `SampGetSamSubsystemName` | `0x93110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 214 | `SampGetServerObjectName` | `0x93120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 217 | `SampGetSuccessAccountAuditingEnabled` | `0x93130` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `SampGetWillNeverTime` | `0x93140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 226 | `SampIncrementNetlogonChangeLogSerialNumber` | `0x93150` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 227 | `SampInvalidateDomainCache` | `0x931E0` | 110 | UnwindData |  |
| 228 | `SampIsAccountBuiltIn` | `0x93260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 230 | `SampIsBuiltinDomain` | `0x93280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 231 | `SampIsDomainHosted` | `0x932A0` | 180 | UnwindData |  |
| 233 | `SampIsServiceRunning` | `0x935B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 234 | `SampIsSetupInProgress` | `0x935D0` | 731 | UnwindData |  |
| 239 | `SampNetLogonNotificationRequired` | `0x93BE0` | 259 | UnwindData |  |
| 240 | `SampNotifyAuditChange` | `0x93DD0` | 468 | UnwindData |  |
| 241 | `SampNotifyReplicatedInChange` | `0x940E0` | 173 | UnwindData |  |
| 244 | `SampPositionOfHighestBit` | `0x943E0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 249 | `SampQueryResourceString` | `0x94510` | 93 | UnwindData |  |
| 274 | `SampSetComputerObjectDsName` | `0x94A30` | 61 | UnwindData |  |
| 290 | `SampStringFromGuid` | `0x94D10` | 73 | UnwindData |  |
| 294 | `SampUpdateMixedModeAndFindDomain` | `0x94E50` | 118 | UnwindData |  |
| 298 | `SampValidateDomainCacheCallback` | `0x94F60` | 120 | UnwindData |  |
| 302 | `SampWriteEventLog` | `0x951A0` | 1,665 | UnwindData |  |
