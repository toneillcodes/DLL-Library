# Binary Specification: aclui.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\aclui.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e8b368a40b9644c8fb63f60dd17068bbf17eb26bb8ddf9aa5ebe97ba53671189`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `GetLocalizedStringForCondition` | `0x1FCF0` | 478 | UnwindData |  |
| 3 | `EditSecurityAdvanced` | `0x22CB0` | 256 | UnwindData |  |
| 7 | `GetTlsIndexForClaimDictionary` | `0x33450` | 67,232 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `EditConditionalAceClaims` | `0x43AF0` | 1,367 | UnwindData |  |
| 4 | `EditResourceCondition` | `0x44050` | 37 | UnwindData |  |
| 1 | `CreateSecurityPage` | `0x4CDD0` | 293 | UnwindData |  |
| 2 | `EditSecurity` | `0x4CF00` | 382 | UnwindData |  |
| 16 | `IID_ISecurityInformation` | `0x69E90` | 0 | Indeterminate |  |
