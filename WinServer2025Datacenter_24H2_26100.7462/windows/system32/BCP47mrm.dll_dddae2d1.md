# Binary Specification: BCP47mrm.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\BCP47mrm.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `dddae2d1128709a1623daf2297ad01e270c1fb250ae2d9823d9054f5399881c5`
* **Total Exported Functions:** 17

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `GetApplicationLanguagesWithUserLanguagesFallback` | `0x6B10` | 482 | UnwindData |  |
| 11 | `GetDistanceOfClosestLanguageInList` | `0x9800` | 78 | UnwindData |  |
| 17 | `IsWellFormedTag` | `0x9A30` | 189 | UnwindData |  |
| 8 | `GetApplicationLayoutDirection` | `0xD440` | 301 | UnwindData |  |
| 12 | `GetLanguageDirectionality` | `0xD610` | 265 | UnwindData |  |
| 3 | `Bcp47IsValid` | `0xD9E0` | 146 | UnwindData |  |
| 4 | `CompareBcp47Tags` | `0xF3F0` | 325 | UnwindData |  |
| 16 | `IsValidUnIsoRegionTag` | `0x10330` | 29 | UnwindData |  |
| 1 | `Bcp47GetDistanceCString` | `0x16090` | 71 | UnwindData |  |
| 2 | `Bcp47GetNeutralFormCString` | `0x160E0` | 191 | UnwindData |  |
| 13 | `GetMrtDisplayLanguageList` | `0x161B0` | 1,371 | UnwindData |  |
| 5 | `FormatLanguageList` | `0x17090` | 224 | UnwindData |  |
| 6 | `FormatLanguageTag` | `0x17180` | 137 | UnwindData |  |
| 9 | `GetClosenessOfUnIsoRegionTags` | `0x17210` | 94 | UnwindData |  |
| 10 | `GetCompositeRegionCode` | `0x17280` | 46 | UnwindData |  |
| 14 | `GetParentCompositeRegionCode` | `0x172C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `IsValidTag` | `0x172D0` | 13,877 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
