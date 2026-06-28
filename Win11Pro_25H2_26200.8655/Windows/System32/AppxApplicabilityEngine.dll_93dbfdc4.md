# Binary Specification: AppxApplicabilityEngine.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\AppxApplicabilityEngine.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `93dbfdc41b7dc534dcf22a5f87e80a52ceabc31b03f5dd73be05ec10dc8b6d68`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `GetApplicabilityContext` | `0xA540` | 191 | UnwindData |  |
| 4 | `CreateApplicabilityContext` | `0xABC0` | 86 | UnwindData |  |
| 7 | `FreeApplicablePackages` | `0xB5C0` | 86 | UnwindData |  |
| 6 | `FreeApplicabilityContext` | `0xB850` | 34 | UnwindData |  |
| 2 | `AddDirectXFeatureLevelToContext` | `0x13F10` | 32 | UnwindData |  |
| 3 | `AddUserLanguagesToContext` | `0x13F40` | 32 | UnwindData |  |
| 8 | `GetApplicablePackages` | `0x13F70` | 77 | UnwindData |  |
| 9 | `GetApplicablePackagesForUser` | `0x13FD0` | 77 | UnwindData |  |
| 10 | `GetApplicablePackagesForUserWithAppChosenResources` | `0x14030` | 478 | UnwindData |  |
| 11 | `GetApplicablePackagesWithAppChosenResources` | `0x14220` | 650 | UnwindData |  |
| 5 | `CreateApplicabilityContextFromString` | `0x1BC40` | 142 | UnwindData |  |
