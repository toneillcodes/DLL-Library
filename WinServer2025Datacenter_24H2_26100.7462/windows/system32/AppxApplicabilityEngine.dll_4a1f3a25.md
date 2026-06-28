# Binary Specification: AppxApplicabilityEngine.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\AppxApplicabilityEngine.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4a1f3a254d5dc744d5e1315e655c1baa87cbc2c59c87ea78ab086120afe14a52`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `GetApplicabilityContext` | `0xA630` | 191 | UnwindData |  |
| 4 | `CreateApplicabilityContext` | `0xACB0` | 86 | UnwindData |  |
| 7 | `FreeApplicablePackages` | `0xB6B0` | 86 | UnwindData |  |
| 6 | `FreeApplicabilityContext` | `0xB940` | 34 | UnwindData |  |
| 2 | `AddDirectXFeatureLevelToContext` | `0x140E0` | 32 | UnwindData |  |
| 3 | `AddUserLanguagesToContext` | `0x14110` | 32 | UnwindData |  |
| 8 | `GetApplicablePackages` | `0x14140` | 77 | UnwindData |  |
| 9 | `GetApplicablePackagesForUser` | `0x141A0` | 77 | UnwindData |  |
| 10 | `GetApplicablePackagesForUserWithAppChosenResources` | `0x14200` | 478 | UnwindData |  |
| 11 | `GetApplicablePackagesWithAppChosenResources` | `0x143F0` | 650 | UnwindData |  |
| 5 | `CreateApplicabilityContextFromString` | `0x1BE10` | 142 | UnwindData |  |
