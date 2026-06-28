# Binary Specification: Winlangdb.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Winlangdb.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b61ac078494d1eca753f62414037c4bcb7690119339dec58a68a436c8c1cd5d0`
* **Total Exported Functions:** 16

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `Bcp47GetEnglishName` | `0x15AF0` | 312 | UnwindData |  |
| 2 | `Bcp47GetLocalizedName` | `0x15C30` | 312 | UnwindData |  |
| 3 | `Bcp47GetLocalizedScript` | `0x15D70` | 312 | UnwindData |  |
| 4 | `Bcp47GetNativeName` | `0x15EB0` | 312 | UnwindData |  |
| 6 | `GetLanguageNames` | `0x15FF0` | 760 | UnwindData |  |
| 7 | `GetLocaleFromLanguageAndRegion` | `0x162F0` | 680 | UnwindData |  |
| 8 | `GetRegionalFormatList` | `0x165A0` | 895 | UnwindData |  |
| 9 | `IsoScriptGetLocalizedName` | `0x16930` | 251 | UnwindData |  |
| 10 | `LanguagesDatabaseGetChildLanguages` | `0x16A40` | 476 | UnwindData |  |
| 11 | `LanguagesDatabaseGetLeafLanguages` | `0x16C30` | 387 | UnwindData |  |
| 12 | `LanguagesDatabaseHasChildren` | `0x16DC0` | 235 | UnwindData |  |
| 13 | `LanguagesDatabaseHasLocalizedContent` | `0x16EC0` | 122 | UnwindData |  |
| 5 | `EnsureLanguageProfileExists` | `0x183E0` | 1,458 | UnwindData |  |
| 14 | `SetUserLanguages` | `0x189A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `SetUserLanguagesCore` | `0x189B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `SetUserLanguagesNoSpeller` | `0x189D0` | 3,516 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
