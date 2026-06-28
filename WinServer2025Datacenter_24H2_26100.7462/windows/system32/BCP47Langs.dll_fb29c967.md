# Binary Specification: BCP47Langs.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\BCP47Langs.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fb29c96720a96cf7d181f5bba044cbaca5b5d5a2b261b5d2defce28d2531e988`
* **Total Exported Functions:** 71

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 36 | `GetAppropriateUserLocaleForUserLanguages` | `0x1AE0` | 264 | UnwindData |  |
| 45 | `GetSerializedUserLanguageProfile` | `0x1E40` | 334 | UnwindData |  |
| 20 | `Bcp47GetNlsForm` | `0x37B0` | 392 | UnwindData |  |
| 35 | `GetApplicationManifestLanguages` | `0x4330` | 206 | UnwindData |  |
| 33 | `GetApplicationLanguageOverride` | `0x4670` | 200 | UnwindData |  |
| 62 | `SetApplicationManifestLanguages` | `0x4970` | 234 | UnwindData |  |
| 1 | `GetUnIsoRegionCode` | `0x4B50` | 163 | UnwindData |  |
| 59 | `RemoveUserLanguageInputMethods` | `0x4C00` | 218 | UnwindData |  |
| 19 | `Bcp47GetNeutralForm` | `0x4FD0` | 392 | UnwindData |  |
| 4 | `AppendUserLanguages` | `0x5210` | 219 | UnwindData |  |
| 16 | `Bcp47GetIsoScriptCode` | `0x5490` | 386 | UnwindData |  |
| 56 | `LanguageListAsMuiForm` | `0x5620` | 497 | UnwindData |  |
| 6 | `Bcp47FindClosestLanguage` | `0x5980` | 413 | UnwindData |  |
| 12 | `Bcp47GetDistance` | `0x5CC0` | 276 | UnwindData |  |
| 18 | `Bcp47GetMuiForm` | `0x6910` | 392 | UnwindData |  |
| 37 | `GetAppropriateUserPreferredAndDisplayLanguagesForUser` | `0x75C0` | 1,594 | UnwindData |  |
| 34 | `GetApplicationLanguages` | `0x85B0` | 269 | UnwindData |  |
| 51 | `GetUserLanguages` | `0xAB70` | 219 | UnwindData |  |
| 55 | `IsTransientLcid` | `0xB300` | 105 | UnwindData |  |
| 8 | `Bcp47FromHkl` | `0xB950` | 592 | UnwindData |  |
| 14 | `Bcp47GetExtensionSubstring` | `0xD450` | 724 | UnwindData |  |
| 24 | `Bcp47Normalize` | `0xE820` | 670 | UnwindData |  |
| 23 | `Bcp47IsWellFormed` | `0x10850` | 171 | UnwindData |  |
| 7 | `Bcp47FromCompactTagInternal` | `0x11000` | 389 | UnwindData |  |
| 10 | `Bcp47GetAbbreviation` | `0x11710` | 392 | UnwindData |  |
| 17 | `Bcp47GetLanguageName` | `0x11C30` | 308 | UnwindData |  |
| 70 | `SetUserLanguagesInternalCore` | `0x12140` | 240 | UnwindData |  |
| 57 | `LcidFromBcp47` | `0x13810` | 162 | UnwindData |  |
| 58 | `RemoveInputsForAllLanguagesInternal` | `0x14310` | 300 | UnwindData |  |
| 60 | `ResolveLanguages` | `0x16B50` | 186 | UnwindData |  |
| 5 | `Bcp47BufferFromLcid` | `0x16D00` | 672 | UnwindData |  |
| 9 | `Bcp47FromLcid` | `0x17020` | 770 | UnwindData |  |
| 40 | `GetFontFallbackLanguageList` | `0x17330` | 203 | UnwindData |  |
| 26 | `ClearApplicationManifestLanguages` | `0x1C990` | 221 | UnwindData |  |
| 53 | `GetUserLanguagesForUser` | `0x1CB90` | 800 | UnwindData |  |
| 43 | `GetPendingUserDisplayLanguage` | `0x1CFF0` | 652 | UnwindData |  |
| 30 | `CompactTagFromBcp47Internal` | `0x1D860` | 145 | UnwindData |  |
| 11 | `Bcp47GetDirectionality` | `0x1D9C0` | 146 | UnwindData |  |
| 46 | `GetSerializedUserLanguagesForUser` | `0x1DDF0` | 324 | UnwindData |  |
| 25 | `ClearApplicationLanguageOverride` | `0x1ED30` | 194 | UnwindData |  |
| 61 | `SetApplicationLanguageOverride` | `0x1F2E0` | 200 | UnwindData |  |
| 52 | `GetUserLanguagesForAllUsers` | `0x1F7B0` | 587 | UnwindData |  |
| 50 | `GetUserLanguageInputMethodsForUser` | `0x1FAD0` | 976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `SetUserLanguagesInternal` | `0x1FEA0` | 211 | UnwindData |  |
| 42 | `GetInputMethodOverrideForUser` | `0x201B0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `AppendUserLanguageInputMethods` | `0x20200` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `GetUserLanguageInputMethods` | `0x203F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `Bcp47GetUnIsoRegionCode` | `0x20430` | 386 | UnwindData |  |
| 44 | `GetRelevantLocalesFromLanguageTags` | `0x207D0` | 881 | UnwindData |  |
| 48 | `GetUserDisplayLanguageOverride` | `0x21990` | 1,081 | UnwindData |  |
| 38 | `GetClosestMatchingUserLanguage` | `0x23590` | 308 | UnwindData |  |
| 31 | `DllGetActivationFactory` | `0x280A0` | 45 | UnwindData |  |
| 32 | `DllGetClassObject` | `0x280E0` | 65 | UnwindData |  |
| 3 | `AppendUserLanguageInternal` | `0x2BE10` | 173 | UnwindData |  |
| 27 | `ClearHttpAcceptLanguageOptOut` | `0x2BED0` | 212 | UnwindData |  |
| 28 | `ClearUserDisplayLanguageOverride` | `0x2BFB0` | 591 | UnwindData |  |
| 29 | `ClearUserLocaleFromLanguageProfileOptOut` | `0x2C210` | 126 | UnwindData |  |
| 39 | `GetDisplayLanguagesForAllUsers` | `0x2C2A0` | 501 | UnwindData |  |
| 41 | `GetHttpAcceptLanguageOptOut` | `0x2C4A0` | 152 | UnwindData |  |
| 47 | `GetStartingUserDisplayLanguage` | `0x2C540` | 276 | UnwindData |  |
| 54 | `GetUserLocaleFromLanguageProfileOptOut` | `0x2C660` | 137 | UnwindData |  |
| 63 | `SetHttpAcceptLanguageOptOut` | `0x2C6F0` | 187 | UnwindData |  |
| 64 | `SetInputMethodOverride` | `0x2C7C0` | 377 | UnwindData |  |
| 65 | `SetPreviousUserDisplayLanguages` | `0x2C940` | 34 | UnwindData |  |
| 66 | `SetStartingUserDisplayLanguage` | `0x2CA80` | 170 | UnwindData |  |
| 67 | `SetUserDisplayLanguageOverride` | `0x2CB30` | 556 | UnwindData |  |
| 68 | `SetUserLanguageInputMethods` | `0x2CD70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `SetUserLocaleFromLanguageProfileOptOut` | `0x2CD80` | 131 | UnwindData |  |
| 13 | `Bcp47GetExtensionSingletons` | `0x2F9E0` | 386 | UnwindData |  |
| 15 | `Bcp47GetIsoLanguageCode` | `0x2FB70` | 386 | UnwindData |  |
| 21 | `Bcp47GetSubtagMapInternal` | `0x2FD00` | 142 | UnwindData |  |
