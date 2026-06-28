# Binary Specification: enterpriseresourcemanager.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\enterpriseresourcemanager.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `dcc287bac8cf56e0a99088ed652d14dc4148462826552ec8fa4397b968aff947`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `EnterpriseResourceManagerStore_DeleteResource` | `0x4960` | 789 | UnwindData |  |
| 2 | `EnterpriseResourceManagerStore_DeleteTrackedResourcesForEnrollment` | `0x4C80` | 166 | UnwindData |  |
| 3 | `EnterpriseResourceManagerStore_GenerateWmiResourcePath` | `0x4D30` | 835 | UnwindData |  |
| 4 | `EnterpriseResourceManagerStore_IsResourceProvisioned` | `0x53F0` | 1,651 | UnwindData |  |
| 5 | `EnterpriseResourceManagerStore_NormalizeURI` | `0x5A70` | 283 | UnwindData |  |
| 6 | `EnterpriseResourceManagerStore_RemoveAllIgnoredUri` | `0x5BA0` | 406 | UnwindData |  |
| 7 | `EnterpriseResourceManagerStore_ReplaceResourceNodePath` | `0x5D40` | 84 | UnwindData |  |
| 8 | `EnterpriseResourceManagerStore_SaveIgnoredURI` | `0x5DA0` | 945 | UnwindData |  |
| 9 | `EnterpriseResourceManagerStore_WriteResourceNodePath` | `0x6160` | 963 | UnwindData |  |
| 10 | `EnterpriseResourceManager_ScopeData_IsValid` | `0x6530` | 50,732 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
