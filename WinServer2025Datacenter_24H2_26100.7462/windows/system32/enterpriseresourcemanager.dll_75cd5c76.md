# Binary Specification: enterpriseresourcemanager.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\enterpriseresourcemanager.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `75cd5c7681bc105666fc82c4f03514787f1e7e4d8c652e96950f3a282ab18f49`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `EnterpriseResourceManagerStore_DeleteResource` | `0x4950` | 789 | UnwindData |  |
| 2 | `EnterpriseResourceManagerStore_DeleteTrackedResourcesForEnrollment` | `0x4C70` | 166 | UnwindData |  |
| 3 | `EnterpriseResourceManagerStore_GenerateWmiResourcePath` | `0x4D20` | 835 | UnwindData |  |
| 4 | `EnterpriseResourceManagerStore_IsResourceProvisioned` | `0x53E0` | 1,651 | UnwindData |  |
| 5 | `EnterpriseResourceManagerStore_NormalizeURI` | `0x5A60` | 283 | UnwindData |  |
| 6 | `EnterpriseResourceManagerStore_RemoveAllIgnoredUri` | `0x5B90` | 406 | UnwindData |  |
| 7 | `EnterpriseResourceManagerStore_ReplaceResourceNodePath` | `0x5D30` | 84 | UnwindData |  |
| 8 | `EnterpriseResourceManagerStore_SaveIgnoredURI` | `0x5D90` | 945 | UnwindData |  |
| 9 | `EnterpriseResourceManagerStore_WriteResourceNodePath` | `0x6150` | 963 | UnwindData |  |
| 10 | `EnterpriseResourceManager_ScopeData_IsValid` | `0x6520` | 50,476 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
