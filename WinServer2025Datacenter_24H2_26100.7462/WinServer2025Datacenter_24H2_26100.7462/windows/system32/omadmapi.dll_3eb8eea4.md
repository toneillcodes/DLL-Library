# Binary Specification: omadmapi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\omadmapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3eb8eea4c0e345a001e86120ceeae23b96e7e4a87460e7551910a126611b7885`
* **Total Exported Functions:** 99

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 114 | `FreeCommandLineOptions` | `0x5490` | 121 | UnwindData |  |
| 64 | `ProcessCommandLine` | `0x5510` | 1,160 | UnwindData |  |
| 97 | `ProcessCommandLineOption` | `0x59A0` | 278 | UnwindData |  |
| 116 | `ReleaseOmaDmClientMutex` | `0x60E0` | 47 | UnwindData |  |
| 62 | `Base64StringToHexString` | `0x63B0` | 226 | UnwindData |  |
| 3 | `CalcHash` | `0x64A0` | 687 | UnwindData |  |
| 123 | `DmCreateSecurityAccount` | `0x6760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `DmGetHighestTemplateGroup` | `0x6760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `DmSecRoleToGroupSID` | `0x6760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `DmSecGroupSIDToRole` | `0x6780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `DmSecurityAccountInGroup` | `0x6780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | `OmaDmCreateSecurityAccount` | `0x6780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 162 | `OmaDmCreateSessionPolicy` | `0x6780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 174 | `SyncDmGroupMembershipToPolicy` | `0x6780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `DmSecurityRoleFromAccountName` | `0x6790` | 103 | UnwindData |  |
| 108 | `FindEndOfHeader` | `0x6800` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `FindHeaderValue` | `0x6890` | 422 | UnwindData |  |
| 112 | `GetStructFromRegistry` | `0x6A40` | 446 | UnwindData |  |
| 45 | `HashCert` | `0x6C10` | 226 | UnwindData |  |
| 63 | `HexStringToBase64String` | `0x6D00` | 190 | UnwindData |  |
| 111 | `SaveStructInRegistry` | `0x6DD0` | 265 | UnwindData |  |
| 107 | `Trim` | `0x6EE0` | 125 | UnwindData |  |
| 65 | `TruncateTextToLength` | `0x6F70` | 609 | UnwindData |  |
| 113 | `ValidateStringAsFloat` | `0x71E0` | 256 | UnwindData |  |
| 117 | `AcquireConfigRefreshMutex` | `0x9570` | 299 | UnwindData |  |
| 115 | `AcquireOmaDmClientMutex` | `0x96B0` | 179 | UnwindData |  |
| 119 | `IsConfigRefreshSemaphoreSignaled` | `0xD5F0` | 190 | UnwindData |  |
| 141 | `OmaDmCloseSession_Impl` | `0xE720` | 132 | UnwindData |  |
| 35 | `OmaDmGetFirstMatchingAccountID` | `0xF1A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `OmaDmGetNextSessionIDToUse` | `0xF1B0` | 177 | UnwindData |  |
| 18 | `OmaDmWaitForAllSessionsCompletion` | `0xF2F0` | 223 | UnwindData |  |
| 118 | `ReleaseConfigRefreshMutex` | `0x10F30` | 121 | UnwindData |  |
| 4 | `MdmSendAlert` | `0x14F00` | 291 | UnwindData |  |
| 76 | `OmaDmAbortSession` | `0x15030` | 379 | UnwindData |  |
| 144 | `OmaDmAbortSession_Impl` | `0x151C0` | 175 | UnwindData |  |
| 21 | `OmaDmCalcTriggerDigest` | `0x15280` | 1,548 | UnwindData |  |
| 164 | `OmaDmClearAcctInfo` | `0x158A0` | 2,480 | UnwindData |  |
| 27 | `OmaDmClearAcctInfoValues` | `0x16260` | 97 | UnwindData |  |
| 40 | `OmaDmCloseSession` | `0x162D0` | 407 | UnwindData |  |
| 37 | `OmaDmCreateInternalAcctID` | `0x16470` | 159 | UnwindData |  |
| 25 | `OmaDmDeleteAcctInfo` | `0x16520` | 869 | UnwindData |  |
| 19 | `OmaDmDeleteAcctInfoWaitForCompletion` | `0x16890` | 1,079 | UnwindData |  |
| 143 | `OmaDmDeleteAcctInfo_Impl` | `0x16CD0` | 331 | UnwindData |  |
| 152 | `OmaDmDeleteSecurityAccount` | `0x16E30` | 778 | UnwindData |  |
| 163 | `OmaDmDeleteSessionPolicy` | `0x17140` | 82 | UnwindData |  |
| 88 | `OmaDmDeleteUserInfo` | `0x171A0` | 346 | UnwindData |  |
| 26 | `OmaDmEnumerateAccounts` | `0x17300` | 83 | UnwindData |  |
| 41 | `OmaDmEnumerateInitiationInfo` | `0x17360` | 1,201 | UnwindData |  |
| 36 | `OmaDmEnumerateSessions` | `0x17820` | 74 | UnwindData |  |
| 48 | `OmaDmFindAppAuthIndex` | `0x17870` | 148 | UnwindData |  |
| 23 | `OmaDmFreeAcctInfo` | `0x17910` | 710 | UnwindData |  |
| 102 | `OmaDmFreeAlertInfo` | `0x17BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `OmaDmFreeInitiationInfo` | `0x17BF0` | 311 | UnwindData |  |
| 89 | `OmaDmFreeUserInfo` | `0x17D30` | 51 | UnwindData |  |
| 99 | `OmaDmGetAcctIDFromAcctUID` | `0x17D70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `OmaDmGetAcctInfo` | `0x17D90` | 169 | UnwindData |  |
| 43 | `OmaDmGetAcctInfoFromKey` | `0x17E40` | 2,992 | UnwindData |  |
| 57 | `OmaDmGetAcctMemberInfo` | `0x18A00` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `OmaDmGetAllAcctInfo` | `0x18A40` | 143 | UnwindData |  |
| 98 | `OmaDmGetDefaultAcctUID` | `0x18AE0` | 194 | UnwindData |  |
| 38 | `OmaDmGetInitiationInfo` | `0x18BB0` | 1,275 | UnwindData |  |
| 44 | `OmaDmGetInternalAcctID` | `0x190C0` | 66 | UnwindData |  |
| 150 | `OmaDmGetInternalAcctSID` | `0x19110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `OmaDmGetUserInfo` | `0x19120` | 524 | UnwindData |  |
| 54 | `OmaDmGetValueFromStruct` | `0x19340` | 234 | UnwindData |  |
| 20 | `OmaDmInitiateSession` | `0x19430` | 46 | UnwindData |  |
| 104 | `OmaDmInitiateSessionAsDevice` | `0x19470` | 436 | UnwindData |  |
| 103 | `OmaDmInitiateSessionAsUser` | `0x19630` | 461 | UnwindData |  |
| 34 | `OmaDmInitiateSessionEx` | `0x19810` | 503 | UnwindData |  |
| 105 | `OmaDmInitiateSessionFullSync` | `0x19A10` | 453 | UnwindData |  |
| 101 | `OmaDmInitiateSessionWithSessionID` | `0x19BE0` | 352 | UnwindData |  |
| 140 | `OmaDmInitiateSession_Impl` | `0x19D50` | 269 | UnwindData |  |
| 75 | `OmaDmIsInformativeServerSessionActive` | `0x1AC00` | 295 | UnwindData |  |
| 51 | `OmaDmIsNodePresent` | `0x1AD30` | 225 | UnwindData |  |
| 52 | `OmaDmIsNodeValuePresent` | `0x1AE20` | 191 | UnwindData |  |
| 42 | `OmaDmSaveAcctInfoToKey` | `0x1AEF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `OmaDmSendAlertNotification` | `0x1AF00` | 313 | UnwindData |  |
| 79 | `OmaDmSendAlertNotification3` | `0x1B040` | 370 | UnwindData |  |
| 78 | `OmaDmSendAlertNotificationEx` | `0x1B1C0` | 319 | UnwindData |  |
| 24 | `OmaDmSetAcctInfo` | `0x1B310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `OmaDmSetAcctInfoAllowed_Impl` | `0x1B320` | 389 | UnwindData |  |
| 142 | `OmaDmSetAcctInfo_Impl` | `0x1B4B0` | 1,154 | UnwindData |  |
| 50 | `OmaDmSetInitiationInfo` | `0x1B940` | 1,175 | UnwindData |  |
| 55 | `OmaDmSetNodePresence` | `0x1BDE0` | 218 | UnwindData |  |
| 56 | `OmaDmSetNodeValuePresence` | `0x1BEC0` | 207 | UnwindData |  |
| 87 | `OmaDmSetUserInfo` | `0x1BFA0` | 354 | UnwindData |  |
| 90 | `OmaDmSetUserInfoNodeValuePresence` | `0x1C110` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `OmaDmSetUserInfoValueInStruct` | `0x1C160` | 257 | UnwindData |  |
| 53 | `OmaDmSetValueInStruct` | `0x1C270` | 619 | UnwindData |  |
| 49 | `OmaDmUnsetNodePresence` | `0x1C4F0` | 204 | UnwindData |  |
| 69 | `OmaDmValidateSslCertCriteria` | `0x1C5D0` | 628 | UnwindData |  |
| 166 | `URIEncodeSegment` | `0x1C850` | 1,298 | UnwindData |  |
| 29 | `ReadBSTRFromStream` | `0x1D830` | 253 | UnwindData |  |
| 85 | `ReadStringFromStream` | `0x1D940` | 315 | UnwindData |  |
| 31 | `ReadVariantFromStream` | `0x1DA90` | 516 | UnwindData |  |
| 28 | `WriteBSTRToStream` | `0x1DCA0` | 168 | UnwindData |  |
| 84 | `WriteStringToStream` | `0x1DD50` | 291 | UnwindData |  |
| 30 | `WriteVariantToStream` | `0x1DE80` | 445 | UnwindData |  |
| 165 | `OmaDmSetAcctInfoEx` | `0x1E2B0` | 1,068 | UnwindData |  |
