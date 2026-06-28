# Binary Specification: samsrv.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\samsrv.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `47dec00cdf9ad4f5c4c612267c681396844e9dee84d3ed42a00a33c5b659ff75`
* **Total Exported Functions:** 338

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 99 | `SamIUpdateLogonStatistics` | `0x1870` | 149 | UnwindData |  |
| 257 | `SampReleaseWriteLock` | `0x28B0` | 194 | UnwindData |  |
| 105 | `SampAcquireWriteLock` | `0x2980` | 257 | UnwindData |  |
| 221 | `SampGetUserAccountSettings` | `0x2A90` | 189 | UnwindData |  |
| 211 | `SampGetReverseMembershipTransitive` | `0x3EB0` | 938 | UnwindData |  |
| 48 | `SamIGetUserLogonInformation2` | `0x4260` | 90 | UnwindData |  |
| 320 | `SamrLookupNamesInDomain` | `0x47A0` | 521 | UnwindData |  |
| 321 | `SamrLookupNamesInDomain2` | `0x4C90` | 12 | UnwindData |  |
| 318 | `SamrLookupDomainInSamServer` | `0x4E80` | 10 | UnwindData |  |
| 60 | `SamILookupNamesInDomain` | `0x52D0` | 15 | UnwindData |  |
| 147 | `SampDeleteContext` | `0x7150` | 531 | UnwindData |  |
| 325 | `SamrOpenUser` | `0x7790` | 972 | UnwindData |  |
| 136 | `SampCreateAccountContext2` | `0x82F0` | 215 | UnwindData |  |
| 138 | `SampCreateContextEx` | `0x8FB0` | 101 | UnwindData |  |
| 144 | `SampDeReferenceContext` | `0x96B0` | 38 | UnwindData |  |
| 319 | `SamrLookupIdsInDomain` | `0x9EB0` | 3,808 | UnwindData |  |
| 306 | `SamrCloseHandle` | `0xADD0` | 570 | UnwindData |  |
| 291 | `SampTraceEvent` | `0xB430` | 802 | UnwindData |  |
| 333 | `SamrRidToSid` | `0xC1A0` | 35 | UnwindData |  |
| 133 | `SampConnect` | `0xC5C0` | 92 | UnwindData |  |
| 219 | `SampGetUnicodeStringAttribute` | `0xD5B0` | 576 | UnwindData |  |
| 301 | `SampValidateRegAttributes` | `0xD920` | 50 | UnwindData |  |
| 208 | `SampGetObjectSD` | `0xE1F0` | 49 | UnwindData |  |
| 323 | `SamrOpenDomain` | `0xE430` | 10 | UnwindData |  |
| 284 | `SampSetTransactionDomain` | `0xEE40` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 199 | `SampGetFixedAttributes` | `0xEF20` | 272 | UnwindData |  |
| 266 | `SampRetrieveUserPasswords` | `0xF040` | 142 | UnwindData |  |
| 103 | `SampAcquireReadLock` | `0xFE70` | 13 | UnwindData |  |
| 292 | `SampUpdateAccountDisabledFlag` | `0xFF10` | 1,385 | UnwindData |  |
| 313 | `SamrEnumerateUsersInDomain` | `0x10480` | 1,001 | UnwindData |  |
| 255 | `SampReleaseReadLock` | `0x11E00` | 184 | UnwindData |  |
| 155 | `SampDsIsRunning` | `0x11EC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 247 | `SampQueryInformationUserInternal` | `0x11EE0` | 8,592 | UnwindData |  |
| 331 | `SamrRemoveMemberFromAlias` | `0x158D0` | 12 | UnwindData |  |
| 315 | `SamrGetAliasMembership` | `0x15C30` | 152 | UnwindData |  |
| 42 | `SamIGetAliasMembership` | `0x15CD0` | 284 | UnwindData |  |
| 75 | `SamIQueryRealmList` | `0x16AC0` | 83 | UnwindData |  |
| 9 | `SamIAccountRestrictions` | `0x16F30` | 761 | UnwindData |  |
| 322 | `SamrOpenAlias` | `0x17230` | 728 | UnwindData |  |
| 267 | `SampRetrieveUserV1aFixed` | `0x17660` | 145 | UnwindData |  |
| 251 | `SampReadExtendedAttributes` | `0x17700` | 422 | UnwindData |  |
| 38 | `SamIFree_SAMPR_RETURNED_USTRING_ARRAY` | `0x178B0` | 22 | UnwindData |  |
| 293 | `SampUpdateComputedUserAccountControlBits` | `0x17920` | 35 | UnwindData |  |
| 29 | `SamIFreeRealmList` | `0x17EF0` | 12 | UnwindData |  |
| 39 | `SamIFree_SAMPR_ULONG_ARRAY` | `0x17F90` | 38 | UnwindData |  |
| 312 | `SamrEnumerateDomainsInSamServer` | `0x17FC0` | 1,389 | UnwindData |  |
| 45 | `SamIGetResourceGroupMembershipsTransitive` | `0x18540` | 332 | UnwindData |  |
| 46 | `SamIGetResourceGroupMembershipsTransitive2` | `0x186A0` | 518 | UnwindData |  |
| 145 | `SampDecrementActiveThreads` | `0x188B0` | 51 | UnwindData |  |
| 330 | `SamrQuerySecurityObject` | `0x19C00` | 1,405 | UnwindData |  |
| 223 | `SampImpersonateClient` | `0x1ACA0` | 207 | UnwindData |  |
| 269 | `SampRtlWellKnownPrivilegeCheck` | `0x1AD80` | 589 | UnwindData |  |
| 268 | `SampRevertToSelf` | `0x1AFE0` | 116 | UnwindData |  |
| 176 | `SampFreeUnicodeString` | `0x1B0B0` | 47 | UnwindData |  |
| 197 | `SampGetExtendedAttribute` | `0x1B340` | 17 | UnwindData |  |
| 232 | `SampIsInternetAccount` | `0x1B8F0` | 80 | UnwindData |  |
| 143 | `SampCurrentThreadOwnsLock` | `0x1BE80` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 316 | `SamrGetGroupsForUser` | `0x1BF70` | 6 | UnwindData |  |
| 285 | `SampSetTransactionWithinDomain` | `0x1C7B0` | 1,616 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `SampAuditAnyEvent` | `0x1CE00` | 320 | UnwindData |  |
| 179 | `SampGetAccessAttribute` | `0x1CF50` | 496 | UnwindData |  |
| 27 | `SamIFreeLookupSidsInfo` | `0x1D190` | 18 | UnwindData |  |
| 140 | `SampCreateFullSid` | `0x1D450` | 191 | UnwindData |  |
| 314 | `SamrEnumerateUsersInDomain2` | `0x1D660` | 1,034 | UnwindData |  |
| 288 | `SampSplitSid` | `0x1DB70` | 64 | UnwindData |  |
| 40 | `SamIFree_SAMPR_USER_INFO_BUFFER` | `0x1E890` | 40 | UnwindData |  |
| 5 | `SAM_MIDL_user_allocate` | `0x1EB10` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `SamDsExtAlloc` | `0x1EB10` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 328 | `SamrQueryInformationUser` | `0x1EBC0` | 294 | UnwindData |  |
| 329 | `SamrQueryInformationUser2` | `0x1EBC0` | 294 | UnwindData |  |
| 1 | `RtlDeleteElementGenericTable2` | `0x1ECF0` | 580 | UnwindData |  |
| 31 | `SamIFreeSidAndAttributesList` | `0x1F110` | 95 | UnwindData |  |
| 3 | `RtlInsertElementGenericTable2` | `0x1F200` | 746 | UnwindData |  |
| 32 | `SamIFreeSidArray` | `0x1F540` | 105 | UnwindData |  |
| 238 | `SampNeedUserAccountSettingsDuringQuery` | `0x1F610` | 704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 215 | `SampGetSidArrayAttribute` | `0x1F8D0` | 412 | UnwindData |  |
| 108 | `SampAddDeltaTime` | `0x1FCF0` | 35 | UnwindData |  |
| 277 | `SampSetExtendedAttributeAccess` | `0x1FDA0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 236 | `SampLookupContext` | `0x1FEF0` | 26 | UnwindData |  |
| 4 | `RtlLookupElementGenericTable2` | `0x20E60` | 196 | UnwindData |  |
| 6 | `SAM_MIDL_user_free` | `0x210C0` | 2,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `SamDsExtFree` | `0x210C0` | 2,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `SamIFreeVoid` | `0x210C0` | 2,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `SampDsGetPrimaryDomainStart` | `0x21990` | 2,464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `SamIFreeSecurityAttributesInfo` | `0x22330` | 62 | UnwindData |  |
| 253 | `SampReferenceContext` | `0x22540` | 1,600 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `SampCheckSidType` | `0x22B80` | 449 | UnwindData |  |
| 263 | `SampReplaceUserV1aFixed` | `0x23540` | 110 | UnwindData |  |
| 278 | `SampSetFixedAttributes` | `0x235C0` | 323 | UnwindData |  |
| 104 | `SampAcquireSamLockExclusive` | `0x238D0` | 71 | UnwindData |  |
| 256 | `SampReleaseSamLockExclusive` | `0x23920` | 52 | UnwindData |  |
| 289 | `SampStoreObjectAttributes` | `0x23C40` | 85 | UnwindData |  |
| 165 | `SampDuplicateUnicodeString` | `0x24080` | 122 | UnwindData |  |
| 295 | `SampUpdatePerformanceCounters` | `0x24230` | 60 | UnwindData |  |
| 13 | `SamIConnect` | `0x243B0` | 47 | UnwindData |  |
| 225 | `SampIncrementActiveThreads` | `0x24430` | 46 | UnwindData |  |
| 297 | `SampUsingDsData` | `0x244F0` | 8,848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `SamIAddDSNameToAlias` | `0x26780` | 514 | UnwindData |  |
| 80 | `SamIRemoveDSNameFromAlias` | `0x26990` | 457 | UnwindData |  |
| 124 | `SampChangeAliasAccountName` | `0x27260` | 337 | UnwindData |  |
| 304 | `SamrAddMemberToAlias` | `0x286A0` | 660 | UnwindData |  |
| 309 | `SamrDeleteAlias` | `0x28A40` | 909 | UnwindData |  |
| 317 | `SamrGetMembersInAlias` | `0x28DE0` | 317 | UnwindData |  |
| 334 | `SamrSetInformationAlias` | `0x29030` | 789 | UnwindData |  |
| 112 | `SampAlInvalidateAliasInformation` | `0x2A260` | 67 | UnwindData |  |
| 135 | `SampCopyUserSupplementalCredentialsForDCPromo` | `0x2BA60` | 465 | UnwindData |  |
| 152 | `SampDsConvertReadAttrBlock` | `0x2BD40` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `SampDsMakeAttrBlock` | `0x2BD80` | 228 | UnwindData |  |
| 160 | `SampDsUpdateContextAttributes` | `0x2C000` | 172 | UnwindData |  |
| 216 | `SampGetSidAttribute` | `0x2C290` | 174 | UnwindData |  |
| 218 | `SampGetUlongArrayAttribute` | `0x2C350` | 212 | UnwindData |  |
| 237 | `SampMarkPerAttributeInvalidFromWhichFields` | `0x2C610` | 206 | UnwindData |  |
| 254 | `SampRegObjToDsObj` | `0x2C980` | 574 | UnwindData |  |
| 270 | `SampSetAccessAttribute` | `0x2CBD0` | 96 | UnwindData |  |
| 286 | `SampSetUnicodeStringAttribute` | `0x2CE00` | 127 | UnwindData |  |
| 296 | `SampUpgradeUserParmsActual` | `0x2DBD0` | 289 | UnwindData |  |
| 19 | `SamIDecodeClaimsBlobToAuthz` | `0x2DEC0` | 65 | UnwindData |  |
| 23 | `SamIFreeAuthzSecurityAttributesInfo` | `0x2DF10` | 62 | UnwindData |  |
| 12 | `SamIClaimIsValid` | `0x3F260` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `SamIConvertSecurityAttributesToClaimsBlob` | `0x3F310` | 620 | UnwindData |  |
| 17 | `SamIDecodeClaimsBlob` | `0x3F590` | 65 | UnwindData |  |
| 18 | `SamIDecodeClaimsBlobIntoClaimsSet` | `0x3F5E0` | 121 | UnwindData |  |
| 24 | `SamIFreeClaimsBlob` | `0x3F660` | 49 | UnwindData |  |
| 25 | `SamIFreeDecodedClaimsSet` | `0x3F6A0` | 140 | UnwindData |  |
| 95 | `SamITransformClaims` | `0x3F740` | 114 | UnwindData |  |
| 84 | `SamIRetrieveMultiplePrimaryCredentials` | `0x41280` | 155 | UnwindData |  |
| 85 | `SamIRetrieveNGCKeyCredential` | `0x41330` | 148 | UnwindData |  |
| 86 | `SamIRetrievePrimaryCredentials` | `0x413D0` | 94 | UnwindData |  |
| 94 | `SamIStorePrimaryCredentials` | `0x41440` | 194 | UnwindData |  |
| 146 | `SampDecryptCredentialData` | `0x41830` | 223 | UnwindData |  |
| 167 | `SampEncryptCredentialData` | `0x419A0` | 482 | UnwindData |  |
| 250 | `SampQueryUserSupplementalCredentialsRegistry` | `0x41D20` | 224 | UnwindData |  |
| 265 | `SampRetrieveMultipleCredentials` | `0x41FF0` | 207 | UnwindData |  |
| 131 | `SampCompareDisplayStrings` | `0x426F0` | 122 | UnwindData |  |
| 161 | `SampDuplicateGroupInfo` | `0x42BA0` | 147 | UnwindData |  |
| 162 | `SampDuplicateMachineInfo` | `0x42BA0` | 147 | UnwindData |  |
| 163 | `SampDuplicateOemGroupInfo` | `0x42C40` | 86 | UnwindData |  |
| 164 | `SampDuplicateOemUserInfo` | `0x42C40` | 86 | UnwindData |  |
| 166 | `SampDuplicateUserInfo` | `0x42CA0` | 195 | UnwindData |  |
| 172 | `SampFreeGroupInfo` | `0x42E10` | 32 | UnwindData |  |
| 173 | `SampFreeMachineInfo` | `0x42E10` | 32 | UnwindData |  |
| 174 | `SampFreeOemGroupInfo` | `0x42E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 175 | `SampFreeOemUserInfo` | `0x42E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 177 | `SampFreeUserInfo` | `0x42E50` | 41 | UnwindData |  |
| 326 | `SamrQueryDisplayInformation` | `0x43EC0` | 138 | UnwindData |  |
| 22 | `SamIDoFSMORoleChange` | `0x44960` | 129 | UnwindData |  |
| 59 | `SamILookupNamesBySid` | `0x449F0` | 706 | UnwindData |  |
| 61 | `SamILookupSidsByName` | `0x44CC0` | 699 | UnwindData |  |
| 68 | `SamINotifyRoleChange` | `0x44F90` | 548 | UnwindData |  |
| 76 | `SamIQueryServerRole` | `0x451C0` | 103 | UnwindData |  |
| 77 | `SamIQueryServerRole2` | `0x45230` | 178 | UnwindData |  |
| 137 | `SampCreateAliasInDomain` | `0x45420` | 2,026 | UnwindData |  |
| 141 | `SampCreateGroupInDomain` | `0x45C10` | 2,166 | UnwindData |  |
| 142 | `SampCreateUserInDomain` | `0x46490` | 3,680 | UnwindData |  |
| 213 | `SampGetSerialNumberDomain2` | `0x47710` | 207 | UnwindData |  |
| 283 | `SampSetSerialNumberDomain2` | `0x492C0` | 314 | UnwindData |  |
| 307 | `SamrCreateUser2InDomain` | `0x496B0` | 403 | UnwindData |  |
| 308 | `SamrCreateUserInDomain` | `0x49850` | 356 | UnwindData |  |
| 327 | `SamrQueryInformationDomain` | `0x49C40` | 1,497 | UnwindData |  |
| 64 | `SamIMixedDomain` | `0x4B110` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `SamIMixedDomain2` | `0x4B140` | 195 | UnwindData |  |
| 154 | `SampDsInitializeSingleDomain` | `0x4B4D0` | 594 | UnwindData |  |
| 157 | `SampDsSetBuiltinDomainPolicy` | `0x4B730` | 279 | UnwindData |  |
| 158 | `SampDsSetDomainPolicy` | `0x4B850` | 186 | UnwindData |  |
| 169 | `SampExtendDefinedDomains` | `0x4B910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `SamICreateKrbTgt` | `0x4B920` | 480 | UnwindData |  |
| 121 | `SampBuildDsNameFromSid` | `0x4BB10` | 100 | UnwindData |  |
| 246 | `SampQueryDSRMAccountName` | `0x4BD70` | 442 | UnwindData |  |
| 275 | `SampSetDSRMPasswordWorker` | `0x4BF30` | 457 | UnwindData |  |
| 55 | `SamIIsExtendedSidMode` | `0x4FE30` | 2,816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `RtlInitializeGenericTable2` | `0x50930` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `SampAddAccountToGroupMembers` | `0x50990` | 988 | UnwindData |  |
| 110 | `SampAddSameDomainMemberToGlobalOrUniversalGroup` | `0x50D80` | 246 | UnwindData |  |
| 111 | `SampAddUserToGroup` | `0x50E80` | 183 | UnwindData |  |
| 125 | `SampChangeGroupAccountName` | `0x50F40` | 337 | UnwindData |  |
| 128 | `SampCheckGroupTypeBits` | `0x510A0` | 1,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 258 | `SampRemoveAccountFromGroupMembers` | `0x514E0` | 579 | UnwindData |  |
| 259 | `SampRemoveSameDomainMemberFromGlobalOrUniversalGroup` | `0x51730` | 194 | UnwindData |  |
| 260 | `SampRemoveUserFromGroup` | `0x51800` | 183 | UnwindData |  |
| 264 | `SampRetrieveGroupV1Fixed` | `0x51B20` | 70 | UnwindData |  |
| 303 | `SampWriteGroupType` | `0x51B70` | 221 | UnwindData |  |
| 305 | `SamrAddMemberToGroup` | `0x51C60` | 390 | UnwindData |  |
| 310 | `SamrDeleteGroup` | `0x51DF0` | 1,304 | UnwindData |  |
| 324 | `SamrOpenGroup` | `0x52530` | 294 | UnwindData |  |
| 332 | `SamrRemoveMemberFromGroup` | `0x529B0` | 387 | UnwindData |  |
| 335 | `SamrSetInformationGroup` | `0x52B40` | 1,105 | UnwindData |  |
| 235 | `SampLogPrint` | `0x53CA0` | 222 | UnwindData |  |
| 78 | `SamIRandomizeStoredPassword` | `0x54330` | 94 | UnwindData |  |
| 79 | `SamIRandomizeStoredPasswordWithoutExpirationCheck` | `0x54A90` | 43 | UnwindData |  |
| 83 | `SamIResetBadPwdCountOnPdc` | `0x54AD0` | 64 | UnwindData |  |
| 93 | `SamISetPasswordInfoOnDc` | `0x54B20` | 538 | UnwindData |  |
| 150 | `SampDeltaChangeNotify` | `0x55680` | 281 | UnwindData |  |
| 224 | `SampIncreaseBadPwdCountLoopback` | `0x55870` | 451 | UnwindData |  |
| 242 | `SampPasswordChangeNotify` | `0x562B0` | 158 | UnwindData |  |
| 243 | `SampPasswordChangeNotifyWorker` | `0x56720` | 615 | UnwindData |  |
| 281 | `SampSetPasswordInfoOnPdcByHandle` | `0x57300` | 123 | UnwindData |  |
| 282 | `SampSetPasswordInfoOnPdcByIndex` | `0x57390` | 3,808 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 338 | `SamrValidatePassword` | `0x58270` | 561 | UnwindData |  |
| 20 | `SamIDemote` | `0x58B30` | 159 | UnwindData |  |
| 21 | `SamIDemoteUndo` | `0x58BE0` | 37 | UnwindData |  |
| 58 | `SamILoadDownlevelDatabase` | `0x58C10` | 505 | UnwindData |  |
| 70 | `SamIPromote` | `0x58E10` | 893 | UnwindData |  |
| 71 | `SamIPromoteUndo` | `0x591A0` | 22 | UnwindData |  |
| 81 | `SamIReplaceDownlevelDatabase` | `0x591C0` | 930 | UnwindData |  |
| 97 | `SamIUnLoadDownlevelDatabase` | `0x59570` | 141 | UnwindData |  |
| 107 | `SampAddAccountsAndApplyMemberships` | `0x59610` | 356 | UnwindData |  |
| 109 | `SampAddNonLocalDomainRelativeMemberships` | `0x598D0` | 129 | UnwindData |  |
| 114 | `SampApplyDomainUpdatesForAllDomains` | `0x5A820` | 286 | UnwindData |  |
| 148 | `SampDeleteDsDirsToDeleteKey` | `0x5BD40` | 209 | UnwindData |  |
| 149 | `SampDeleteKeyForPostBootPromote` | `0x5BE20` | 296 | UnwindData |  |
| 178 | `SampGenerateRandomPassword` | `0x5C650` | 89 | UnwindData |  |
| 261 | `SampRenameKrbtgtAccount` | `0x5E500` | 1,058 | UnwindData |  |
| 271 | `SampSetAdminPassword` | `0x5ED00` | 284 | UnwindData |  |
| 279 | `SampSetGlobalDsSids` | `0x5EFB0` | 166 | UnwindData |  |
| 280 | `SampSetPassword` | `0x5F060` | 73 | UnwindData |  |
| 116 | `SampAuditAccountEnableDisableChange` | `0x5F980` | 188 | UnwindData |  |
| 117 | `SampAuditAccountNameChange` | `0x5FA50` | 150 | UnwindData |  |
| 119 | `SampAuditGroupTypeChange` | `0x606A0` | 838 | UnwindData |  |
| 120 | `SampAuditSidHistory` | `0x609F0` | 166 | UnwindData |  |
| 26 | `SamIFreeLookupNamesInfo` | `0x632E0` | 312 | UnwindData |  |
| 34 | `SamIFree_SAMPR_DISPLAY_INFO_BUFFER` | `0x634C0` | 20 | UnwindData |  |
| 35 | `SamIFree_SAMPR_DOMAIN_INFO_BUFFER` | `0x634E0` | 72 | UnwindData |  |
| 36 | `SamIFree_SAMPR_ENUMERATION_BUFFER` | `0x63530` | 102 | UnwindData |  |
| 37 | `SamIFree_SAMPR_GET_GROUPS_BUFFER` | `0x635A0` | 56 | UnwindData |  |
| 41 | `SamIFree_UserInternal6Information` | `0x63610` | 474 | UnwindData |  |
| 53 | `SamIInitialize` | `0x64B70` | 2,921 | UnwindData |  |
| 98 | `SamIUninitialize` | `0x658C0` | 55 | UnwindData |  |
| 229 | `SampIsAuditingEnabled` | `0x67E50` | 52,320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 248 | `SampQueryPolicyValue` | `0x74AB0` | 4,064 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 273 | `SampSetCheckpointInfo` | `0x75A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 276 | `SampSetErrorInfo` | `0x75AA0` | 260 | UnwindData |  |
| 272 | `SampSetAttributeAccess` | `0x770C0` | 65 | UnwindData |  |
| 122 | `SampBuildSamProtection` | `0x77110` | 1,069 | UnwindData |  |
| 204 | `SampGetNewAccountSecurityNt4` | `0x779B0` | 1,708 | UnwindData |  |
| 337 | `SamrSetSecurityObject` | `0x78E60` | 1,352 | UnwindData |  |
| 52 | `SamIImpersonateNullSession` | `0x793B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `SamIRevertNullSession` | `0x793D0` | 50 | UnwindData |  |
| 182 | `SampGetCurrentOwnerAndPrimaryGroup` | `0x7A0E0` | 327 | UnwindData |  |
| 299 | `SampValidateDomainControllerCreation` | `0x7AD30` | 100 | UnwindData |  |
| 300 | `SampValidatePwdSettingAttempt` | `0x7ADA0` | 274 | UnwindData |  |
| 62 | `SamILoopbackConnect` | `0x7B070` | 28 | UnwindData |  |
| 63 | `SamILoopbackConnectEx` | `0x7B0A0` | 330 | UnwindData |  |
| 74 | `SamIQueryCapabilities` | `0x7B1F0` | 42 | UnwindData |  |
| 245 | `SampQueryCapabilities` | `0x7B220` | 653 | UnwindData |  |
| 54 | `SamIIsDownlevelDcUpgrade` | `0x7BBA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `SamIIsRebootAfterPromotion` | `0x7BBB0` | 25 | UnwindData |  |
| 57 | `SamIIsSetupInProgress` | `0x7BBD0` | 12,080 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 195 | `SampGetDomainUpgradeTasks` | `0x7EB00` | 6,352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 252 | `SampRecordSystemSchemaVerisonInRegistry` | `0x803D0` | 423 | UnwindData |  |
| 11 | `SamIChangePasswordForeignUser` | `0x815F0` | 1,046 | UnwindData |  |
| 51 | `SamIHandleObjectUpdate` | `0x81A10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `SamIOpenUserByAlternateId` | `0x81A40` | 258 | UnwindData |  |
| 88 | `SamIScorePassword` | `0x81B50` | 433 | UnwindData |  |
| 90 | `SamISetMachinePassword` | `0x81D10` | 107 | UnwindData |  |
| 91 | `SamISetPasswordForeignUser2` | `0x81D90` | 53 | UnwindData |  |
| 92 | `SamISetPasswordForeignUser3` | `0x81DD0` | 1,511 | UnwindData |  |
| 102 | `SampAccountControlToFlags` | `0x825C0` | 1,440 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `SampAssignPrimaryGroup` | `0x82B60` | 252 | UnwindData |  |
| 123 | `SampCalculateLmAndNtOwfPasswords` | `0x82C70` | 187 | UnwindData |  |
| 126 | `SampChangeUserAccountName` | `0x83C30` | 648 | UnwindData |  |
| 127 | `SampCheckForAccountLockout` | `0x842C0` | 103 | UnwindData |  |
| 132 | `SampComputePasswordExpired` | `0x84FB0` | 50 | UnwindData |  |
| 151 | `SampDsChangePasswordUser` | `0x864A0` | 685 | UnwindData |  |
| 159 | `SampDsSetPasswordUser` | `0x86760` | 751 | UnwindData |  |
| 170 | `SampFlagsToAccountControl` | `0x86BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 171 | `SampFlagsToAccountControlEx` | `0x86BB0` | 430 | UnwindData |  |
| 210 | `SampGetPasswordMustChangeWithUF_UAC` | `0x87660` | 96 | UnwindData |  |
| 220 | `SampGetUserAccountControlComputed` | `0x87790` | 141 | UnwindData |  |
| 262 | `SampReplaceUserLogonHours` | `0x88D40` | 1,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 287 | `SampSetUserAccountControl` | `0x89260` | 1,512 | UnwindData |  |
| 311 | `SamrDeleteUser` | `0x8B2A0` | 1,973 | UnwindData |  |
| 336 | `SamrSetInformationUser` | `0x8C200` | 9,751 | UnwindData |  |
| 15 | `SamICopyCurrentDomainAccountSettings` | `0x8F760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `SamIFreeOidList` | `0x8F780` | 47 | UnwindData |  |
| 43 | `SamIGetConfigurationOidList` | `0x8F7C0` | 284 | UnwindData |  |
| 47 | `SamIGetUserLogonInformation` | `0x8F8F0` | 72 | UnwindData |  |
| 49 | `SamIGetUserLogonInformation3` | `0x8F940` | 97 | UnwindData |  |
| 50 | `SamIGetUserLogonInformationEx` | `0x8F9B0` | 77 | UnwindData |  |
| 67 | `SamINetLogonPing` | `0x8FA10` | 199 | UnwindData |  |
| 72 | `SamIPurgeSecrets` | `0x8FAE0` | 261 | UnwindData |  |
| 73 | `SamIQueryAccountSecretsCachability` | `0x8FBF0` | 293 | UnwindData |  |
| 96 | `SamIUPNFromUserHandle` | `0x8FD20` | 196 | UnwindData |  |
| 44 | `SamIGetDefaultAdministratorName` | `0x90FD0` | 234 | UnwindData |  |
| 66 | `SamINT4UpgradeInProgress` | `0x910C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 203 | `SampGetNT4UpgradeInProgress` | `0x910C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `SamIReplicateAccountData` | `0x910D0` | 320 | UnwindData |  |
| 89 | `SamISetAuditingInformation` | `0x91220` | 96 | UnwindData |  |
| 100 | `SamIValidateAccountName` | `0x91290` | 79 | UnwindData |  |
| 101 | `SamIValidateNewAccountName` | `0x912F0` | 972 | UnwindData |  |
| 113 | `SampAllocateNextCurrentRidFromIndex` | `0x916D0` | 2,528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | `SampCommitBufferedWrites` | `0x920B0` | 276 | UnwindData |  |
| 134 | `SampConvertUiListToApiList` | `0x921D0` | 745 | UnwindData |  |
| 139 | `SampCreateDefaultUPN` | `0x925F0` | 225 | UnwindData |  |
| 168 | `SampExamineSid` | `0x92830` | 249 | UnwindData |  |
| 180 | `SampGetAccountDomainInfo` | `0x92DC0` | 191 | UnwindData |  |
| 181 | `SampGetBehaviorVersion` | `0x92E90` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `SampGetDisableOutboundRSO` | `0x93010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | `SampGetDisableRSOOnPDCForward` | `0x93020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `SampGetDisableResetBadPwdCountForward` | `0x93030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `SampGetDisableSingleObjectRepl` | `0x93040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 187 | `SampGetDnsDomainNameFromIndex` | `0x93050` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 188 | `SampGetDomainContextFromIndex` | `0x93080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 189 | `SampGetDomainObjectFromAccountContext` | `0x930A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `SampGetDomainObjectFromIndex` | `0x930D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 191 | `SampGetDomainServerRoleFromIndex` | `0x93100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 192 | `SampGetDomainSidFromAccountContext` | `0x93120` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 193 | `SampGetDomainSidFromIndex` | `0x93150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 194 | `SampGetDomainSidListForSam` | `0x93170` | 362 | UnwindData |  |
| 196 | `SampGetDownLevelDomainControllersPresent` | `0x932E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 198 | `SampGetExternalNameFromIndex` | `0x93300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 200 | `SampGetHasNeverTime` | `0x93320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | `SampGetIgnoreGCFailures` | `0x93330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | `SampGetLogLevel` | `0x93340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 205 | `SampGetNextUnmodifiedRidFromIndex` | `0x93350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | `SampGetNoGcLogonEnforceKerberosIpCheck` | `0x93370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 207 | `SampGetNoGcLogonEnforceNTLMCheck` | `0x93380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 209 | `SampGetObjectTypeNameFromIndex` | `0x93390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 212 | `SampGetSamSubsystemName` | `0x933B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 214 | `SampGetServerObjectName` | `0x933C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 217 | `SampGetSuccessAccountAuditingEnabled` | `0x933D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `SampGetWillNeverTime` | `0x933E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 226 | `SampIncrementNetlogonChangeLogSerialNumber` | `0x933F0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 227 | `SampInvalidateDomainCache` | `0x93480` | 110 | UnwindData |  |
| 228 | `SampIsAccountBuiltIn` | `0x93500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 230 | `SampIsBuiltinDomain` | `0x93520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 231 | `SampIsDomainHosted` | `0x93540` | 180 | UnwindData |  |
| 233 | `SampIsServiceRunning` | `0x93850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 234 | `SampIsSetupInProgress` | `0x93870` | 731 | UnwindData |  |
| 239 | `SampNetLogonNotificationRequired` | `0x93E80` | 259 | UnwindData |  |
| 240 | `SampNotifyAuditChange` | `0x94070` | 468 | UnwindData |  |
| 241 | `SampNotifyReplicatedInChange` | `0x94380` | 173 | UnwindData |  |
| 244 | `SampPositionOfHighestBit` | `0x94680` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 249 | `SampQueryResourceString` | `0x947B0` | 93 | UnwindData |  |
| 274 | `SampSetComputerObjectDsName` | `0x94CD0` | 61 | UnwindData |  |
| 290 | `SampStringFromGuid` | `0x94FB0` | 73 | UnwindData |  |
| 294 | `SampUpdateMixedModeAndFindDomain` | `0x950F0` | 118 | UnwindData |  |
| 298 | `SampValidateDomainCacheCallback` | `0x95200` | 120 | UnwindData |  |
| 302 | `SampWriteEventLog` | `0x95440` | 1,665 | UnwindData |  |
