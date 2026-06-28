# Binary Specification: Winlangdb.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Winlangdb.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `bf180246dda4b87b42e2b0ab203c4357740a568d70fae64bac81a63975f1b276`
* **Total Exported Functions:** 16

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `Bcp47GetEnglishName` | `0x15AD0` | 312 | UnwindData |  |
| 2 | `Bcp47GetLocalizedName` | `0x15C10` | 312 | UnwindData |  |
| 3 | `Bcp47GetLocalizedScript` | `0x15D50` | 312 | UnwindData |  |
| 4 | `Bcp47GetNativeName` | `0x15E90` | 312 | UnwindData |  |
| 6 | `GetLanguageNames` | `0x15FD0` | 760 | UnwindData |  |
| 7 | `GetLocaleFromLanguageAndRegion` | `0x162D0` | 680 | UnwindData |  |
| 8 | `GetRegionalFormatList` | `0x16580` | 895 | UnwindData |  |
| 9 | `IsoScriptGetLocalizedName` | `0x16910` | 251 | UnwindData |  |
| 10 | `LanguagesDatabaseGetChildLanguages` | `0x16A20` | 476 | UnwindData |  |
| 11 | `LanguagesDatabaseGetLeafLanguages` | `0x16C10` | 387 | UnwindData |  |
| 12 | `LanguagesDatabaseHasChildren` | `0x16DA0` | 235 | UnwindData |  |
| 13 | `LanguagesDatabaseHasLocalizedContent` | `0x16EA0` | 122 | UnwindData |  |
| 5 | `EnsureLanguageProfileExists` | `0x183C0` | 1,458 | UnwindData |  |
| 14 | `SetUserLanguages` | `0x18980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `SetUserLanguagesCore` | `0x18990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `SetUserLanguagesNoSpeller` | `0x189B0` | 3,516 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
