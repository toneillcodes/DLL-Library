# Binary Specification: BCP47mrm.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\BCP47mrm.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `29a0e18c3c18d1a762ca7463b6371fa3161b81e2d12205af6e62d72796c5640d`
* **Total Exported Functions:** 17

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `Bcp47IsValid` | `0x1010` | 146 | UnwindData |  |
| 8 | `GetApplicationLayoutDirection` | `0x1460` | 301 | UnwindData |  |
| 12 | `GetLanguageDirectionality` | `0x1630` | 265 | UnwindData |  |
| 7 | `GetApplicationLanguagesWithUserLanguagesFallback` | `0x5620` | 482 | UnwindData |  |
| 11 | `GetDistanceOfClosestLanguageInList` | `0x8310` | 78 | UnwindData |  |
| 17 | `IsWellFormedTag` | `0x8540` | 189 | UnwindData |  |
| 4 | `CompareBcp47Tags` | `0xF280` | 325 | UnwindData |  |
| 16 | `IsValidUnIsoRegionTag` | `0x10070` | 29 | UnwindData |  |
| 1 | `Bcp47GetDistanceCString` | `0x160E0` | 71 | UnwindData |  |
| 2 | `Bcp47GetNeutralFormCString` | `0x16130` | 191 | UnwindData |  |
| 13 | `GetMrtDisplayLanguageList` | `0x16200` | 1,371 | UnwindData |  |
| 5 | `FormatLanguageList` | `0x17080` | 224 | UnwindData |  |
| 6 | `FormatLanguageTag` | `0x17170` | 137 | UnwindData |  |
| 9 | `GetClosenessOfUnIsoRegionTags` | `0x17200` | 94 | UnwindData |  |
| 10 | `GetCompositeRegionCode` | `0x17270` | 46 | UnwindData |  |
| 14 | `GetParentCompositeRegionCode` | `0x172B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `IsValidTag` | `0x172C0` | 13,871 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
