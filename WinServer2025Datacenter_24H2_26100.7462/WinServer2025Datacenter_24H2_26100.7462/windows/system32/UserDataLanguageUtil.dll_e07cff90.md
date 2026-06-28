# Binary Specification: UserDataLanguageUtil.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\UserDataLanguageUtil.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e07cff90f9e4d32b3af90c49ea96315156e6873ea7fda5d41229d8186c0387e4`
* **Total Exported Functions:** 35

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CHSPinYinHelper_CreateInstance` | `0x1F90` | 220 | UnwindData |  |
| 2 | `CHSPinYinHelper_HasPossibleCHSPinYin` | `0x2080` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `CHSPinYinHelper_HasPossiblePinYin` | `0x20B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `CHSPinYinHelper_Initialize` | `0x20F0` | 84 | UnwindData |  |
| 5 | `CanConvertStringFromUnicode` | `0x3270` | 214 | UnwindData |  |
| 6 | `ConvertToMultiByte` | `0x3350` | 708 | UnwindData |  |
| 7 | `ConvertToWideStream` | `0x3620` | 806 | UnwindData |  |
| 8 | `ConvertWideStreamToMultiByte` | `0x3950` | 818 | UnwindData |  |
| 16 | `GetNarrowSzCodepage` | `0x3C90` | 372 | UnwindData |  |
| 18 | `GetWideSz` | `0x3EB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `GetWideSzAlloc` | `0x3ED0` | 399 | UnwindData |  |
| 9 | `DecomposeHangulSyllables` | `0x47B0` | 1,446 | UnwindData |  |
| 10 | `DetermineStringEALangId` | `0x4D60` | 194 | UnwindData |  |
| 11 | `DetermineStringEALangIdNLS` | `0x4E30` | 658 | UnwindData |  |
| 12 | `GetCodepageName` | `0x50D0` | 626 | UnwindData |  |
| 14 | `GetCurrentLangIdForMatching` | `0x5350` | 141 | UnwindData |  |
| 15 | `GetMultiLanguage2` | `0x53F0` | 198 | UnwindData |  |
| 17 | `GetSystemDefaultCodepage` | `0x54C0` | 193 | UnwindData |  |
| 20 | `InitializeLanguageUtil` | `0x55C0` | 85 | UnwindData |  |
| 21 | `IsAltChar` | `0x5620` | 73 | UnwindData |  |
| 22 | `IsCHNChar` | `0x5670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `IsEAChar` | `0x5690` | 68 | UnwindData |  |
| 24 | `IsHangulSyllable` | `0x56E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `IsJPNChar` | `0x5700` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `IsLocalePseudoLoc` | `0x5740` | 74 | UnwindData |  |
| 31 | `IsSkippableCharacter` | `0x5790` | 340 | UnwindData |  |
| 32 | `IsSupportedCodepage` | `0x58F0` | 136 | UnwindData |  |
| 33 | `MapCharToBaseChar` | `0x5A10` | 305 | UnwindData |  |
| 34 | `MapStringToBaseCharacters` | `0x5B50` | 40 | UnwindData |  |
| 35 | `UninitializeLanguageUtil` | `0x5B80` | 120 | UnwindData |  |
| 13 | `GetConvertedTextForMatching` | `0x6100` | 375 | UnwindData |  |
| 27 | `IsMatchingEAPrefix` | `0x64B0` | 31 | UnwindData |  |
| 28 | `IsMatchingEAPrefixEx` | `0x64E0` | 1,662 | UnwindData |  |
| 29 | `IsMatchingPrefix` | `0x6B70` | 21 | UnwindData |  |
| 30 | `IsMatchingPrefixEx` | `0x6B90` | 1,615 | UnwindData |  |
