# Binary Specification: Phoneutil.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Phoneutil.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9ac7d032ab5e9d642533c960cd791bf210d0260ccc19547e1e498dacf55652c6`
* **Total Exported Functions:** 94

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 64 | `FreeTextReplyPresetMessages` | `0x95B0` | 33 | UnwindData |  |
| 2 | `CheckIfShellReady` | `0xB3F0` | 902 | UnwindData |  |
| 17 | `GetDefaultWiFiCallingBranding` | `0xBC20` | 165 | UnwindData |  |
| 18 | `GetDialStringFromTelUri` | `0xBCD0` | 319 | UnwindData |  |
| 28 | `GetTelUriFromDialString` | `0xBF60` | 516 | UnwindData |  |
| 34 | `IsEqualWnfStateNameHelper` | `0xC750` | 9,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `CreateCellularApiLineConfig` | `0xECB0` | 287 | UnwindData |  |
| 60 | `CreateCellularPhoneLineConfig` | `0xEDE0` | 441 | UnwindData |  |
| 65 | `GetAdjustCDMACallTimeSetting` | `0xEFA0` | 190 | UnwindData |  |
| 72 | `GetMethodFromPropId` | `0xF070` | 208 | UnwindData |  |
| 73 | `GetTextReplyPresetMessages` | `0xF150` | 1,180 | UnwindData |  |
| 74 | `GetTimeDeltaFormat` | `0xF600` | 576 | UnwindData |  |
| 75 | `GetZerothCellularPhoneLineId` | `0xF850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `MaskPhoneNumber` | `0xF870` | 133 | UnwindData |  |
| 82 | `MaskPhoneUri` | `0xF900` | 211 | UnwindData |  |
| 83 | `MaskString` | `0xF9E0` | 92 | UnwindData |  |
| 89 | `Phone_FmtText_GlobalFormat` | `0xFAB0` | 683 | UnwindData |  |
| 93 | `UrlEscapeString` | `0xFD70` | 316 | UnwindData |  |
| 3 | `CreateAudioHardwareHelper` | `0x106C0` | 273 | UnwindData |  |
| 4 | `CreateBrandingInfo` | `0x11530` | 218 | UnwindData |  |
| 5 | `CreatePerUserSecurityPolicy` | `0x124E0` | 266 | UnwindData |  |
| 6 | `CreatePerUserSecurityToken` | `0x131E0` | 198 | UnwindData |  |
| 7 | `CreatePerUserSecurityTokenForRpcClient` | `0x13980` | 190 | UnwindData |  |
| 10 | `DuplicateSidIfValid` | `0x14130` | 266 | UnwindData |  |
| 25 | `GetRpcClientUser` | `0x142A0` | 775 | UnwindData |  |
| 26 | `GetSidForUserToken` | `0x145B0` | 383 | UnwindData |  |
| 27 | `GetSignedInUserForAppActivation` | `0x14740` | 1,737 | UnwindData |  |
| 29 | `GetUserContextTokenForUser` | `0x14E70` | 547 | UnwindData |  |
| 30 | `GetUserSecurityIdentifierForToken` | `0x150A0` | 329 | UnwindData |  |
| 31 | `GetUserTokenForUser` | `0x151F0` | 234 | UnwindData |  |
| 32 | `ImpersonateSignedInUser` | `0x152E0` | 441 | UnwindData |  |
| 36 | `IsUserAccountLoggedOn` | `0x154D0` | 1,104 | UnwindData |  |
| 8 | `DeinitDialingPrefixTable` | `0x16110` | 87 | UnwindData |  |
| 9 | `DetectMultiPrefix` | `0x16170` | 484 | UnwindData |  |
| 16 | `GetCountryCodeFromOperatorNum` | `0x16360` | 335 | UnwindData |  |
| 19 | `GetDialingPrefixes` | `0x164C0` | 883 | UnwindData |  |
| 21 | `GetIddPrefix` | `0x16840` | 531 | UnwindData |  |
| 22 | `GetIddPrefixTable` | `0x16A60` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `GetNationalNumberLength` | `0x16AB0` | 379 | UnwindData |  |
| 24 | `GetNddPrefix` | `0x16C40` | 528 | UnwindData |  |
| 33 | `InitDialingPrefixTable` | `0x16F80` | 689 | UnwindData |  |
| 37 | `MapPlusToDialingPrefix` | `0x17240` | 795 | UnwindData |  |
| 38 | `StripExtraneousNDD` | `0x179F0` | 924 | UnwindData |  |
| 11 | `Get3GGPInCallToneDefaultForRegion` | `0x18B30` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `Get3GPPInCallToneDefault` | `0x18B80` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `Get3GPPInCallToneForTypeAndMcc` | `0x18BC0` | 921 | UnwindData |  |
| 14 | `Get3GPPInCallToneTypeString` | `0x18F60` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `GetDtmfInCallToneTypeString` | `0x18FA0` | 204 | UnwindData |  |
| 15 | `GetAppUserModelIdFromPkgFamilyNameAndUser` | `0x196E0` | 2,391 | UnwindData |  |
| 40 | `VoipAppIdentityUtilities_GetApplicationByAumid` | `0x1DEA0` | 628 | UnwindData |  |
| 41 | `VoipAppIdentityUtilities_GetApplicationResourceResolverFromApplication` | `0x1E120` | 301 | UnwindData |  |
| 42 | `VoipAppIdentityUtilities_GetLifecycleManagerPolicy` | `0x1E260` | 235 | UnwindData |  |
| 43 | `VoipAppIdentityUtilities_GetRpcClientApplicationUserModelId` | `0x1E360` | 285 | UnwindData |  |
| 44 | `VoipAppIdentityUtilities_GetVoipAppAUMIDFromPFN` | `0x1E490` | 3,606 | UnwindData |  |
| 45 | `AsyncWorkDispatcher_CreateInstance` | `0x206F0` | 271 | UnwindData |  |
| 48 | `CellularApiHelper_CreateInstance` | `0x30030` | 355 | UnwindData |  |
| 49 | `CellularApiHelper_FreeCountedModemArray` | `0x301A0` | 31 | UnwindData |  |
| 50 | `CellularApiHelper_FreeCountedRegistrationStatusArray` | `0x301A0` | 31 | UnwindData |  |
| 51 | `CellularApiHelper_FreeCountedSimAppArray` | `0x301A0` | 31 | UnwindData |  |
| 52 | `CellularApiHelper_FreeCountedSimArray` | `0x301A0` | 31 | UnwindData |  |
| 53 | `CellularApiHelper_FreeCountedSimLineArray` | `0x301A0` | 31 | UnwindData |  |
| 54 | `CellularApiHelper_FreeCountedSlotArray` | `0x301A0` | 31 | UnwindData |  |
| 55 | `CellularApiHelper_FreeCountedSlotCanAssociationArray` | `0x301A0` | 31 | UnwindData |  |
| 76 | `IsCellularVoiceCapableDevice` | `0x301D0` | 60 | UnwindData |  |
| 56 | `ComparePhoneNumbers` | `0x30400` | 258 | UnwindData |  |
| 70 | `GetDisplayNameFromCallInformation` | `0x30510` | 371 | UnwindData |  |
| 85 | `OptimizedReverseNumberCompare` | `0x30690` | 277 | UnwindData |  |
| 61 | `CreateDialAssist` | `0x32BE0` | 343 | UnwindData |  |
| 62 | `FindAreaCode` | `0x33040` | 808 | UnwindData |  |
| 84 | `OneShotTimer_CreateInstance` | `0x33DC0` | 236 | UnwindData |  |
| 35 | `IsTTYEnabled` | `0x37470` | 145 | UnwindData |  |
| 39 | `StripNonDtmfChars` | `0x379A0` | 262 | UnwindData |  |
| 57 | `ConvertPhoneNumberToUINT64` | `0x37F30` | 88 | UnwindData |  |
| 58 | `CopyOnlyCharsetCharacters` | `0x37F90` | 139 | UnwindData |  |
| 67 | `GetDialableNumber` | `0x38030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `GetDialableNumberAndDTMF` | `0x38050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `GetDialableNumberEtc` | `0x38070` | 66 | UnwindData |  |
| 77 | `IsDialableChar` | `0x380C0` | 71 | UnwindData |  |
| 78 | `IsDialableCharEx` | `0x38110` | 61 | UnwindData |  |
| 79 | `IsNumberDialable` | `0x38160` | 126 | UnwindData |  |
| 80 | `IsValidCharacterForCharset` | `0x381F0` | 76 | UnwindData |  |
| 91 | `RemoveMetadataFromNumber` | `0x38250` | 264 | UnwindData |  |
| 94 | `ValidPhoneNumberInplaceStripInvalidCharacters` | `0x38360` | 221 | UnwindData |  |
| 46 | `CauseCode_GetCodeFriendlyText` | `0x38520` | 382 | UnwindData |  |
| 47 | `CauseCode_IsCodeRegistered` | `0x386B0` | 283 | UnwindData |  |
| 1 | *Ordinal Only* | `0x3D610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `GetCchTailMin` | `0x3D620` | 91 | UnwindData |  |
| 63 | `FormatPhoneNumberWithLeftToRightMarker` | `0x3E0D0` | 133 | UnwindData |  |
| 71 | `GetDisplayNumberWithLeftToRightMarker` | `0x3E160` | 132 | UnwindData |  |
| 88 | `Phone_FmtText` | `0x3E1F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `Phone_FmtText_NonDialerFormat` | `0x3E200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `PhoneLineIdToString` | `0x3E210` | 127 | UnwindData |  |
| 87 | `PhoneLineIdToUrlEscapedString` | `0x3E2A0` | 291 | UnwindData |  |
| 92 | `StringToPhoneLineId` | `0x3E3D0` | 179 | UnwindData |  |
