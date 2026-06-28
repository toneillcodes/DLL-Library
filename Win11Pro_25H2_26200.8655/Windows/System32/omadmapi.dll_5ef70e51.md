# Binary Specification: omadmapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\omadmapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5ef70e51ddc93e4d8ea2d43f6919c3c199d3b1b7d3b10755ff81db62e6b73032`
* **Total Exported Functions:** 99

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 114 | `FreeCommandLineOptions` | `0x54A0` | 121 | UnwindData |  |
| 64 | `ProcessCommandLine` | `0x5520` | 1,160 | UnwindData |  |
| 97 | `ProcessCommandLineOption` | `0x59B0` | 278 | UnwindData |  |
| 116 | `ReleaseOmaDmClientMutex` | `0x60F0` | 47 | UnwindData |  |
| 62 | `Base64StringToHexString` | `0x63C0` | 226 | UnwindData |  |
| 3 | `CalcHash` | `0x64B0` | 687 | UnwindData |  |
| 123 | `DmCreateSecurityAccount` | `0x6770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `DmGetHighestTemplateGroup` | `0x6770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `DmSecRoleToGroupSID` | `0x6770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `DmSecGroupSIDToRole` | `0x6790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `DmSecurityAccountInGroup` | `0x6790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | `OmaDmCreateSecurityAccount` | `0x6790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 162 | `OmaDmCreateSessionPolicy` | `0x6790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 174 | `SyncDmGroupMembershipToPolicy` | `0x6790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `DmSecurityRoleFromAccountName` | `0x67A0` | 103 | UnwindData |  |
| 108 | `FindEndOfHeader` | `0x6810` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `FindHeaderValue` | `0x68A0` | 422 | UnwindData |  |
| 112 | `GetStructFromRegistry` | `0x6A50` | 446 | UnwindData |  |
| 45 | `HashCert` | `0x6C20` | 226 | UnwindData |  |
| 63 | `HexStringToBase64String` | `0x6D10` | 190 | UnwindData |  |
| 111 | `SaveStructInRegistry` | `0x6DE0` | 265 | UnwindData |  |
| 107 | `Trim` | `0x6EF0` | 125 | UnwindData |  |
| 65 | `TruncateTextToLength` | `0x6F80` | 609 | UnwindData |  |
| 113 | `ValidateStringAsFloat` | `0x71F0` | 256 | UnwindData |  |
| 117 | `AcquireConfigRefreshMutex` | `0x9580` | 299 | UnwindData |  |
| 115 | `AcquireOmaDmClientMutex` | `0x96C0` | 179 | UnwindData |  |
| 119 | `IsConfigRefreshSemaphoreSignaled` | `0xC570` | 190 | UnwindData |  |
| 141 | `OmaDmCloseSession_Impl` | `0xD6A0` | 132 | UnwindData |  |
| 35 | `OmaDmGetFirstMatchingAccountID` | `0xE120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `OmaDmGetNextSessionIDToUse` | `0xE130` | 177 | UnwindData |  |
| 18 | `OmaDmWaitForAllSessionsCompletion` | `0xE270` | 223 | UnwindData |  |
| 118 | `ReleaseConfigRefreshMutex` | `0xFFA0` | 121 | UnwindData |  |
| 4 | `MdmSendAlert` | `0x13CF0` | 291 | UnwindData |  |
| 76 | `OmaDmAbortSession` | `0x13E20` | 379 | UnwindData |  |
| 144 | `OmaDmAbortSession_Impl` | `0x13FB0` | 175 | UnwindData |  |
| 21 | `OmaDmCalcTriggerDigest` | `0x14070` | 1,548 | UnwindData |  |
| 164 | `OmaDmClearAcctInfo` | `0x14690` | 2,480 | UnwindData |  |
| 27 | `OmaDmClearAcctInfoValues` | `0x15050` | 97 | UnwindData |  |
| 40 | `OmaDmCloseSession` | `0x150C0` | 407 | UnwindData |  |
| 37 | `OmaDmCreateInternalAcctID` | `0x15260` | 159 | UnwindData |  |
| 25 | `OmaDmDeleteAcctInfo` | `0x15310` | 869 | UnwindData |  |
| 19 | `OmaDmDeleteAcctInfoWaitForCompletion` | `0x15680` | 1,079 | UnwindData |  |
| 143 | `OmaDmDeleteAcctInfo_Impl` | `0x15AC0` | 331 | UnwindData |  |
| 152 | `OmaDmDeleteSecurityAccount` | `0x15C20` | 778 | UnwindData |  |
| 163 | `OmaDmDeleteSessionPolicy` | `0x15F30` | 82 | UnwindData |  |
| 88 | `OmaDmDeleteUserInfo` | `0x15F90` | 346 | UnwindData |  |
| 26 | `OmaDmEnumerateAccounts` | `0x160F0` | 83 | UnwindData |  |
| 41 | `OmaDmEnumerateInitiationInfo` | `0x16150` | 1,201 | UnwindData |  |
| 36 | `OmaDmEnumerateSessions` | `0x16610` | 74 | UnwindData |  |
| 48 | `OmaDmFindAppAuthIndex` | `0x16660` | 148 | UnwindData |  |
| 23 | `OmaDmFreeAcctInfo` | `0x16700` | 710 | UnwindData |  |
| 102 | `OmaDmFreeAlertInfo` | `0x169D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `OmaDmFreeInitiationInfo` | `0x169E0` | 311 | UnwindData |  |
| 89 | `OmaDmFreeUserInfo` | `0x16B20` | 51 | UnwindData |  |
| 99 | `OmaDmGetAcctIDFromAcctUID` | `0x16B60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `OmaDmGetAcctInfo` | `0x16B80` | 169 | UnwindData |  |
| 43 | `OmaDmGetAcctInfoFromKey` | `0x16C30` | 2,992 | UnwindData |  |
| 57 | `OmaDmGetAcctMemberInfo` | `0x177F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `OmaDmGetAllAcctInfo` | `0x17830` | 143 | UnwindData |  |
| 98 | `OmaDmGetDefaultAcctUID` | `0x178D0` | 194 | UnwindData |  |
| 38 | `OmaDmGetInitiationInfo` | `0x179A0` | 1,275 | UnwindData |  |
| 44 | `OmaDmGetInternalAcctID` | `0x17EB0` | 66 | UnwindData |  |
| 150 | `OmaDmGetInternalAcctSID` | `0x17F00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `OmaDmGetUserInfo` | `0x17F10` | 524 | UnwindData |  |
| 54 | `OmaDmGetValueFromStruct` | `0x18130` | 234 | UnwindData |  |
| 20 | `OmaDmInitiateSession` | `0x18220` | 46 | UnwindData |  |
| 104 | `OmaDmInitiateSessionAsDevice` | `0x18260` | 436 | UnwindData |  |
| 103 | `OmaDmInitiateSessionAsUser` | `0x18420` | 461 | UnwindData |  |
| 34 | `OmaDmInitiateSessionEx` | `0x18600` | 503 | UnwindData |  |
| 105 | `OmaDmInitiateSessionFullSync` | `0x18800` | 453 | UnwindData |  |
| 101 | `OmaDmInitiateSessionWithSessionID` | `0x189D0` | 352 | UnwindData |  |
| 140 | `OmaDmInitiateSession_Impl` | `0x18B40` | 269 | UnwindData |  |
| 75 | `OmaDmIsInformativeServerSessionActive` | `0x199F0` | 295 | UnwindData |  |
| 51 | `OmaDmIsNodePresent` | `0x19B20` | 225 | UnwindData |  |
| 52 | `OmaDmIsNodeValuePresent` | `0x19C10` | 191 | UnwindData |  |
| 42 | `OmaDmSaveAcctInfoToKey` | `0x19CE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `OmaDmSendAlertNotification` | `0x19CF0` | 313 | UnwindData |  |
| 79 | `OmaDmSendAlertNotification3` | `0x19E30` | 370 | UnwindData |  |
| 78 | `OmaDmSendAlertNotificationEx` | `0x19FB0` | 319 | UnwindData |  |
| 24 | `OmaDmSetAcctInfo` | `0x1A100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `OmaDmSetAcctInfoAllowed_Impl` | `0x1A110` | 389 | UnwindData |  |
| 142 | `OmaDmSetAcctInfo_Impl` | `0x1A2A0` | 1,154 | UnwindData |  |
| 50 | `OmaDmSetInitiationInfo` | `0x1A730` | 1,175 | UnwindData |  |
| 55 | `OmaDmSetNodePresence` | `0x1ABD0` | 218 | UnwindData |  |
| 56 | `OmaDmSetNodeValuePresence` | `0x1ACB0` | 207 | UnwindData |  |
| 87 | `OmaDmSetUserInfo` | `0x1AD90` | 354 | UnwindData |  |
| 90 | `OmaDmSetUserInfoNodeValuePresence` | `0x1AF00` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `OmaDmSetUserInfoValueInStruct` | `0x1AF50` | 257 | UnwindData |  |
| 53 | `OmaDmSetValueInStruct` | `0x1B060` | 619 | UnwindData |  |
| 49 | `OmaDmUnsetNodePresence` | `0x1B2E0` | 204 | UnwindData |  |
| 69 | `OmaDmValidateSslCertCriteria` | `0x1B3C0` | 628 | UnwindData |  |
| 166 | `URIEncodeSegment` | `0x1B640` | 1,298 | UnwindData |  |
| 29 | `ReadBSTRFromStream` | `0x1C620` | 253 | UnwindData |  |
| 85 | `ReadStringFromStream` | `0x1C730` | 315 | UnwindData |  |
| 31 | `ReadVariantFromStream` | `0x1C880` | 516 | UnwindData |  |
| 28 | `WriteBSTRToStream` | `0x1CA90` | 168 | UnwindData |  |
| 84 | `WriteStringToStream` | `0x1CB40` | 291 | UnwindData |  |
| 30 | `WriteVariantToStream` | `0x1CC70` | 445 | UnwindData |  |
| 165 | `OmaDmSetAcctInfoEx` | `0x1D0A0` | 1,068 | UnwindData |  |
