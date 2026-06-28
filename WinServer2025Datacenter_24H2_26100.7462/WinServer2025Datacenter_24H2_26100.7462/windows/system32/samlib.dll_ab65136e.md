# Binary Specification: samlib.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\samlib.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ab65136e340c027996d9271a97504762acf3d2243fd71e104bb0b3502da14cbf`
* **Total Exported Functions:** 77

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 20 | `SamEnumerateUsersInDomain` | `0x1010` | 255 | UnwindData |  |
| 21 | `SamEnumerateUsersInDomain2` | `0x1120` | 259 | UnwindData |  |
| 33 | `SamLookupNamesInDomain2` | `0x1230` | 227 | UnwindData |  |
| 32 | `SamLookupNamesInDomain` | `0x1320` | 227 | UnwindData |  |
| 46 | `SamQuerySecurityObject` | `0x16E0` | 483 | UnwindData |  |
| 23 | `SamGetAliasMembership` | `0x18D0` | 603 | UnwindData |  |
| 26 | `SamGetGroupsForUser` | `0x1B40` | 509 | UnwindData |  |
| 18 | `SamEnumerateDomainsInSamServer` | `0x1D50` | 548 | UnwindData |  |
| 30 | `SamLookupDomainInSamServer` | `0x26F0` | 432 | UnwindData |  |
| 37 | `SamOpenUser` | `0x28B0` | 778 | UnwindData |  |
| 52 | `SamRidToSid` | `0x2BC0` | 55 | UnwindData |  |
| 35 | `SamOpenDomain` | `0x2DF0` | 911 | UnwindData |  |
| 43 | `SamQueryInformationUser` | `0x3190` | 439 | UnwindData |  |
| 7 | `SamCloseHandle` | `0x3350` | 571 | UnwindData |  |
| 24 | `SamGetCompatibilityMode` | `0x3A30` | 232 | UnwindData |  |
| 31 | `SamLookupIdsInDomain` | `0x3B20` | 2,719 | UnwindData |  |
| 34 | `SamOpenAlias` | `0x45D0` | 771 | UnwindData |  |
| 40 | `SamQueryInformationAlias` | `0x48E0` | 438 | UnwindData |  |
| 27 | `SamGetMembersInAlias` | `0x4AA0` | 497 | UnwindData |  |
| 39 | `SamQueryDisplayInformation` | `0x4D00` | 793 | UnwindData |  |
| 41 | `SamQueryInformationDomain` | `0x5020` | 488 | UnwindData |  |
| 49 | `SamRemoveMemberFromForeignDomain` | `0x52E0` | 381 | UnwindData |  |
| 8 | `SamConnect` | `0x5580` | 1,829 | UnwindData |  |
| 22 | `SamFreeMemory` | `0x6520` | 29 | UnwindData |  |
| 62 | `SamUnregisterObjectChangeNotification` | `0x7B80` | 174 | UnwindData |  |
| 47 | `SamRegisterObjectChangeNotification` | `0x7C40` | 178 | UnwindData |  |
| 38 | `SamPerformGenericOperation` | `0x7D90` | 283 | UnwindData |  |
| 6 | `SamChangePasswordUser2` | `0x8310` | 621 | UnwindData |  |
| 56 | `SamSetInformationUser` | `0x8CF0` | 3,175 | UnwindData |  |
| 63 | `SamValidatePassword` | `0x9960` | 653 | UnwindData |  |
| 53 | `SamSetInformationAlias` | `0x9C00` | 406 | UnwindData |  |
| 17 | `SamEnumerateAliasesInDomain` | `0x9DA0` | 516 | UnwindData |  |
| 48 | `SamRemoveMemberFromAlias` | `0x9FB0` | 384 | UnwindData |  |
| 68 | `SamiEncryptPasswords` | `0xBAA0` | 649 | UnwindData |  |
| 1 | `OnMachineUILanguageInit` | `0xBE70` | 389 | UnwindData |  |
| 2 | `SamAddMemberToAlias` | `0xCCB0` | 371 | UnwindData |  |
| 3 | `SamAddMemberToGroup` | `0xCE30` | 393 | UnwindData |  |
| 4 | `SamAddMultipleMembersToAlias` | `0xCFC0` | 432 | UnwindData |  |
| 5 | `SamChangePasswordUser` | `0xD180` | 786 | UnwindData |  |
| 10 | `SamCreateAliasInDomain` | `0xD870` | 535 | UnwindData |  |
| 11 | `SamCreateGroupInDomain` | `0xDA90` | 535 | UnwindData |  |
| 12 | `SamCreateUser2InDomain` | `0xDCB0` | 1,011 | UnwindData |  |
| 13 | `SamCreateUserInDomain` | `0xE0B0` | 532 | UnwindData |  |
| 14 | `SamDeleteAlias` | `0xE2D0` | 374 | UnwindData |  |
| 15 | `SamDeleteGroup` | `0xE450` | 374 | UnwindData |  |
| 16 | `SamDeleteUser` | `0xE5D0` | 374 | UnwindData |  |
| 19 | `SamEnumerateGroupsInDomain` | `0xE750` | 509 | UnwindData |  |
| 25 | `SamGetDisplayEnumerationIndex` | `0xE960` | 479 | UnwindData |  |
| 28 | `SamGetMembersInGroup` | `0xEB50` | 515 | UnwindData |  |
| 29 | `SamLapsSysprepCleanup` | `0xED60` | 287 | UnwindData |  |
| 36 | `SamOpenGroup` | `0xEE90` | 503 | UnwindData |  |
| 42 | `SamQueryInformationGroup` | `0xF090` | 560 | UnwindData |  |
| 44 | `SamQueryLapsManagedAccount` | `0xF2D0` | 372 | UnwindData |  |
| 45 | `SamQueryLocalizableAccountsInDomain` | `0xF450` | 465 | UnwindData |  |
| 50 | `SamRemoveMemberFromGroup` | `0xF630` | 375 | UnwindData |  |
| 51 | `SamRemoveMultipleMembersFromAlias` | `0xF7B0` | 432 | UnwindData |  |
| 54 | `SamSetInformationDomain` | `0xF970` | 394 | UnwindData |  |
| 55 | `SamSetInformationGroup` | `0xFB00` | 394 | UnwindData |  |
| 57 | `SamSetMemberAttributesOfGroup` | `0xFC90` | 393 | UnwindData |  |
| 58 | `SamSetSecurityObject` | `0xFE20` | 613 | UnwindData |  |
| 59 | `SamShutdownSamServer` | `0x10090` | 131 | UnwindData |  |
| 60 | `SamTestPrivateFunctionsDomain` | `0x10120` | 58 | UnwindData |  |
| 61 | `SamTestPrivateFunctionsUser` | `0x10160` | 58 | UnwindData |  |
| 64 | `SamiAccountIsDelegateManagedServiceAccount` | `0x101A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `SamiChangeKeys` | `0x101B0` | 1,175 | UnwindData |  |
| 66 | `SamiChangePasswordUser` | `0x10650` | 1,082 | UnwindData |  |
| 67 | `SamiChangePasswordUser2` | `0x10A90` | 1,124 | UnwindData |  |
| 69 | `SamiFindOrCreateShadowAdminAccount` | `0x10F00` | 505 | UnwindData |  |
| 70 | `SamiGetBadPasswordErrorMessage` | `0x11100` | 780 | UnwindData |  |
| 71 | `SamiIsShadowAdminAccount` | `0x11420` | 506 | UnwindData |  |
| 72 | `SamiLmChangePasswordUser` | `0x11620` | 437 | UnwindData |  |
| 73 | `SamiSetBootKeyInformation` | `0x117E0` | 413 | UnwindData |  |
| 74 | `SamiSetDSRMPassword` | `0x11990` | 101 | UnwindData |  |
| 75 | `SamiSetDSRMPasswordOWF` | `0x11A00` | 101 | UnwindData |  |
| 76 | `SamiSyncDSRMPasswordFromAccount` | `0x11A70` | 412 | UnwindData |  |
| 77 | `SamiValidateComputerAccountReuseAttempt` | `0x11C20` | 14,560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `SamConnectWithCreds` | `0x15500` | 502 | UnwindData |  |
