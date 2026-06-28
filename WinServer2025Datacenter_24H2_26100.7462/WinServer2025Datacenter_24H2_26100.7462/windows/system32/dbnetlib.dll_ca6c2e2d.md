# Binary Specification: dbnetlib.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\dbnetlib.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ca6c2e2df7b7b06e3df5a0664bb6356952a8d635107a4b82bd07152432bcb115`
* **Total Exported Functions:** 31

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `ConnectionRead` | `0x1010` | 3,001 | UnwindData |  |
| 16 | `ConnectionOpenW` | `0x1DD0` | 250 | UnwindData |  |
| 8 | `ConnectionOpen` | `0x1ED0` | 3,949 | UnwindData |  |
| 3 | `ConnectionWrite` | `0x4C70` | 1,317 | UnwindData |  |
| 9 | `ConnectionClose` | `0x5C00` | 439 | UnwindData |  |
| 31 | `GenClientContextEx` | `0x6020` | 1,490 | UnwindData |  |
| 23 | `InitSSPIPackage` | `0x68A0` | 1,009 | UnwindData |  |
| 22 | `CloseEnumServers` | `0x8090` | 167 | UnwindData |  |
| 10 | `ConnectionCheckForData` | `0x8140` | 343 | UnwindData |  |
| 11 | `ConnectionError` | `0x82A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `ConnectionErrorW` | `0x82D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `ConnectionFlushCache` | `0x8310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `ConnectionGetSvrUser` | `0x8330` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `ConnectionMode` | `0x8620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `ConnectionObjectSize` | `0x8630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `ConnectionOption` | `0x8640` | 293 | UnwindData |  |
| 14 | `ConnectionServerEnum` | `0x8A90` | 41 | UnwindData |  |
| 15 | `ConnectionServerEnumW` | `0x8C00` | 94 | UnwindData |  |
| 13 | `ConnectionSqlVer` | `0x8C70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `ConnectionStatus` | `0x8CA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `ConnectionTransact` | `0x8CB0` | 227 | UnwindData |  |
| 12 | `ConnectionVer` | `0x8DA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `ConnectionWriteOOB` | `0x8DB0` | 541 | UnwindData |  |
| 21 | `GetNextEnumeration` | `0x9320` | 1,657 | UnwindData |  |
| 20 | `InitEnumServers` | `0x9A40` | 1,431 | UnwindData |  |
| 27 | `GenClientContext` | `0x138B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `InitSession` | `0x138C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `InitSessionEx` | `0x138D0` | 326 | UnwindData |  |
| 24 | `TermSSPIPackage` | `0x13B70` | 62 | UnwindData |  |
| 26 | `TermSession` | `0x13BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `TermSessionEx` | `0x13BD0` | 167 | UnwindData |  |
