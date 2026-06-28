# Binary Specification: aclui.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\aclui.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9d1a806b65705fed4aecd7e1fd00b96fb3c66336aa7220b28acd69007bb07378`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `GetLocalizedStringForCondition` | `0x224E0` | 478 | UnwindData |  |
| 3 | `EditSecurityAdvanced` | `0x281A0` | 256 | UnwindData |  |
| 7 | `GetTlsIndexForClaimDictionary` | `0x359F0` | 67,232 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `EditConditionalAceClaims` | `0x46090` | 1,367 | UnwindData |  |
| 4 | `EditResourceCondition` | `0x465F0` | 37 | UnwindData |  |
| 1 | `CreateSecurityPage` | `0x4F460` | 293 | UnwindData |  |
| 2 | `EditSecurity` | `0x4F590` | 382 | UnwindData |  |
| 16 | `IID_ISecurityInformation` | `0x6CEE0` | 0 | Indeterminate |  |
