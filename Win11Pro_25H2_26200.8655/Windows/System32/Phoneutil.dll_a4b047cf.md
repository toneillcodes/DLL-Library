# Binary Specification: Phoneutil.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Phoneutil.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a4b047cfd28f6336c817049c99403dbdeb92e5f77178c0e5d83fbd2c47ba4119`
* **Total Exported Functions:** 94

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 64 | `FreeTextReplyPresetMessages` | `0x95D0` | 33 | UnwindData |  |
| 2 | `CheckIfShellReady` | `0xB410` | 902 | UnwindData |  |
| 17 | `GetDefaultWiFiCallingBranding` | `0xBC40` | 165 | UnwindData |  |
| 18 | `GetDialStringFromTelUri` | `0xBCF0` | 319 | UnwindData |  |
| 28 | `GetTelUriFromDialString` | `0xBF80` | 516 | UnwindData |  |
| 34 | `IsEqualWnfStateNameHelper` | `0xC770` | 9,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `CreateCellularApiLineConfig` | `0xECD0` | 287 | UnwindData |  |
| 60 | `CreateCellularPhoneLineConfig` | `0xEE00` | 441 | UnwindData |  |
| 65 | `GetAdjustCDMACallTimeSetting` | `0xEFC0` | 190 | UnwindData |  |
| 72 | `GetMethodFromPropId` | `0xF090` | 208 | UnwindData |  |
| 73 | `GetTextReplyPresetMessages` | `0xF170` | 1,180 | UnwindData |  |
| 74 | `GetTimeDeltaFormat` | `0xF620` | 576 | UnwindData |  |
| 75 | `GetZerothCellularPhoneLineId` | `0xF870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `MaskPhoneNumber` | `0xF890` | 133 | UnwindData |  |
| 82 | `MaskPhoneUri` | `0xF920` | 211 | UnwindData |  |
| 83 | `MaskString` | `0xFA00` | 92 | UnwindData |  |
| 89 | `Phone_FmtText_GlobalFormat` | `0xFAD0` | 683 | UnwindData |  |
| 93 | `UrlEscapeString` | `0xFD90` | 316 | UnwindData |  |
| 3 | `CreateAudioHardwareHelper` | `0x106E0` | 273 | UnwindData |  |
| 4 | `CreateBrandingInfo` | `0x11550` | 218 | UnwindData |  |
| 5 | `CreatePerUserSecurityPolicy` | `0x12500` | 266 | UnwindData |  |
| 6 | `CreatePerUserSecurityToken` | `0x13200` | 198 | UnwindData |  |
| 7 | `CreatePerUserSecurityTokenForRpcClient` | `0x139A0` | 190 | UnwindData |  |
| 10 | `DuplicateSidIfValid` | `0x14150` | 266 | UnwindData |  |
| 25 | `GetRpcClientUser` | `0x142C0` | 775 | UnwindData |  |
| 26 | `GetSidForUserToken` | `0x145D0` | 383 | UnwindData |  |
| 27 | `GetSignedInUserForAppActivation` | `0x14760` | 1,737 | UnwindData |  |
| 29 | `GetUserContextTokenForUser` | `0x14E90` | 547 | UnwindData |  |
| 30 | `GetUserSecurityIdentifierForToken` | `0x150C0` | 329 | UnwindData |  |
| 31 | `GetUserTokenForUser` | `0x15210` | 234 | UnwindData |  |
| 32 | `ImpersonateSignedInUser` | `0x15300` | 441 | UnwindData |  |
| 36 | `IsUserAccountLoggedOn` | `0x154F0` | 1,104 | UnwindData |  |
| 8 | `DeinitDialingPrefixTable` | `0x16130` | 87 | UnwindData |  |
| 9 | `DetectMultiPrefix` | `0x16190` | 484 | UnwindData |  |
| 16 | `GetCountryCodeFromOperatorNum` | `0x16380` | 335 | UnwindData |  |
| 19 | `GetDialingPrefixes` | `0x164E0` | 883 | UnwindData |  |
| 21 | `GetIddPrefix` | `0x16860` | 531 | UnwindData |  |
| 22 | `GetIddPrefixTable` | `0x16A80` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `GetNationalNumberLength` | `0x16AD0` | 379 | UnwindData |  |
| 24 | `GetNddPrefix` | `0x16C60` | 528 | UnwindData |  |
| 33 | `InitDialingPrefixTable` | `0x16FA0` | 689 | UnwindData |  |
| 37 | `MapPlusToDialingPrefix` | `0x17260` | 795 | UnwindData |  |
| 38 | `StripExtraneousNDD` | `0x17A10` | 924 | UnwindData |  |
| 11 | `Get3GGPInCallToneDefaultForRegion` | `0x18B50` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `Get3GPPInCallToneDefault` | `0x18BA0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `Get3GPPInCallToneForTypeAndMcc` | `0x18BE0` | 921 | UnwindData |  |
| 14 | `Get3GPPInCallToneTypeString` | `0x18F80` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `GetDtmfInCallToneTypeString` | `0x18FC0` | 204 | UnwindData |  |
| 15 | `GetAppUserModelIdFromPkgFamilyNameAndUser` | `0x19700` | 2,391 | UnwindData |  |
| 40 | `VoipAppIdentityUtilities_GetApplicationByAumid` | `0x1EB40` | 628 | UnwindData |  |
| 41 | `VoipAppIdentityUtilities_GetApplicationResourceResolverFromApplication` | `0x1EDC0` | 301 | UnwindData |  |
| 42 | `VoipAppIdentityUtilities_GetLifecycleManagerPolicy` | `0x1EF00` | 235 | UnwindData |  |
| 43 | `VoipAppIdentityUtilities_GetRpcClientApplicationUserModelId` | `0x1F000` | 285 | UnwindData |  |
| 44 | `VoipAppIdentityUtilities_GetVoipAppAUMIDFromPFN` | `0x1F130` | 3,606 | UnwindData |  |
| 45 | `AsyncWorkDispatcher_CreateInstance` | `0x213D0` | 271 | UnwindData |  |
| 48 | `CellularApiHelper_CreateInstance` | `0x30D10` | 355 | UnwindData |  |
| 49 | `CellularApiHelper_FreeCountedModemArray` | `0x30E80` | 31 | UnwindData |  |
| 50 | `CellularApiHelper_FreeCountedRegistrationStatusArray` | `0x30E80` | 31 | UnwindData |  |
| 51 | `CellularApiHelper_FreeCountedSimAppArray` | `0x30E80` | 31 | UnwindData |  |
| 52 | `CellularApiHelper_FreeCountedSimArray` | `0x30E80` | 31 | UnwindData |  |
| 53 | `CellularApiHelper_FreeCountedSimLineArray` | `0x30E80` | 31 | UnwindData |  |
| 54 | `CellularApiHelper_FreeCountedSlotArray` | `0x30E80` | 31 | UnwindData |  |
| 55 | `CellularApiHelper_FreeCountedSlotCanAssociationArray` | `0x30E80` | 31 | UnwindData |  |
| 76 | `IsCellularVoiceCapableDevice` | `0x30EB0` | 60 | UnwindData |  |
| 56 | `ComparePhoneNumbers` | `0x310E0` | 258 | UnwindData |  |
| 70 | `GetDisplayNameFromCallInformation` | `0x311F0` | 371 | UnwindData |  |
| 85 | `OptimizedReverseNumberCompare` | `0x31370` | 277 | UnwindData |  |
| 61 | `CreateDialAssist` | `0x338C0` | 343 | UnwindData |  |
| 62 | `FindAreaCode` | `0x33D20` | 808 | UnwindData |  |
| 84 | `OneShotTimer_CreateInstance` | `0x35040` | 236 | UnwindData |  |
| 35 | `IsTTYEnabled` | `0x386F0` | 145 | UnwindData |  |
| 39 | `StripNonDtmfChars` | `0x38C20` | 262 | UnwindData |  |
| 57 | `ConvertPhoneNumberToUINT64` | `0x391B0` | 88 | UnwindData |  |
| 58 | `CopyOnlyCharsetCharacters` | `0x39210` | 139 | UnwindData |  |
| 67 | `GetDialableNumber` | `0x392B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `GetDialableNumberAndDTMF` | `0x392D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `GetDialableNumberEtc` | `0x392F0` | 66 | UnwindData |  |
| 77 | `IsDialableChar` | `0x39340` | 71 | UnwindData |  |
| 78 | `IsDialableCharEx` | `0x39390` | 61 | UnwindData |  |
| 79 | `IsNumberDialable` | `0x393E0` | 126 | UnwindData |  |
| 80 | `IsValidCharacterForCharset` | `0x39470` | 76 | UnwindData |  |
| 91 | `RemoveMetadataFromNumber` | `0x394D0` | 264 | UnwindData |  |
| 94 | `ValidPhoneNumberInplaceStripInvalidCharacters` | `0x395E0` | 221 | UnwindData |  |
| 46 | `CauseCode_GetCodeFriendlyText` | `0x397A0` | 382 | UnwindData |  |
| 47 | `CauseCode_IsCodeRegistered` | `0x39930` | 283 | UnwindData |  |
| 1 | *Ordinal Only* | `0x3E890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `GetCchTailMin` | `0x3E8A0` | 91 | UnwindData |  |
| 63 | `FormatPhoneNumberWithLeftToRightMarker` | `0x3F350` | 133 | UnwindData |  |
| 71 | `GetDisplayNumberWithLeftToRightMarker` | `0x3F3E0` | 132 | UnwindData |  |
| 88 | `Phone_FmtText` | `0x3F470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `Phone_FmtText_NonDialerFormat` | `0x3F480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `PhoneLineIdToString` | `0x3F490` | 127 | UnwindData |  |
| 87 | `PhoneLineIdToUrlEscapedString` | `0x3F520` | 291 | UnwindData |  |
| 92 | `StringToPhoneLineId` | `0x3F650` | 179 | UnwindData |  |
