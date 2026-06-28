# Binary Specification: PimIndexMaintenanceClient.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\PimIndexMaintenanceClient.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `38cc87faa34494ae1e917962aca178ec58267987810dff78e6b16e849e566560`
* **Total Exported Functions:** 16

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CreateIndexedFilterClient` | `0x2AB0` | 83 | UnwindData |  |
| 3 | `WaitForCookie` | `0x4D20` | 221 | UnwindData |  |
| 4 | `WaitForCookieValueToSet` | `0x4E10` | 156 | UnwindData |  |
| 7 | `PimIMClient_Free` | `0x5370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `PimIMClient_ResetInprocService` | `0x5390` | 102 | UnwindData |  |
| 15 | `PimIM_RpcConnect` | `0x5400` | 121 | UnwindData |  |
| 16 | `PimIM_RpcDisconnect` | `0x5480` | 50 | UnwindData |  |
| 2 | `GetDefaultContactsFilterSupplierSortOrder` | `0x5540` | 112 | UnwindData |  |
| 5 | `CreatePOOMSortedAggregateDataSource` | `0x6820` | 258 | UnwindData |  |
| 6 | `PimIMClient_CacheAggregateCacheFileMapping` | `0xAA10` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `PimIMClient_LoadAggregateCache` | `0xAB20` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `PimIMClient_RebuildAggregateCache` | `0xAB50` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `PimIMClient_Resume` | `0xABA0` | 44 | UnwindData |  |
| 12 | `PimIMClient_Suspend` | `0xAC60` | 44 | UnwindData |  |
| 13 | `PimIMClient_UpdateItems` | `0xACA0` | 44 | UnwindData |  |
| 14 | `PimIMClient_UpdateStores` | `0xACE0` | 42 | UnwindData |  |
