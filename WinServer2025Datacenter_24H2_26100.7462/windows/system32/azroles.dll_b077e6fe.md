# Binary Specification: azroles.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\azroles.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b077e6feb0dd65f50b32fada18b9d8fa2e296b6502d6100413a555da06dede71`
* **Total Exported Functions:** 44

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 41 | `DllCanUnloadNow` | `0xB020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `DllGetClassObject` | `0xB040` | 281 | UnwindData |  |
| 43 | `DllRegisterServer` | `0xB2B0` | 243 | UnwindData |  |
| 44 | `DllUnregisterServer` | `0xB3B0` | 197 | UnwindData |  |
| 7 | `AzAuthorizationStoreDelete` | `0x27230` | 161 | UnwindData |  |
| 8 | `AzCloseHandle` | `0x272E0` | 373 | UnwindData |  |
| 12 | `AzFreeMemory` | `0x279D0` | 27 | UnwindData |  |
| 13 | `AzGetProperty` | `0x27A00` | 26 | UnwindData |  |
| 18 | `AzInitialize` | `0x27A20` | 577 | UnwindData |  |
| 34 | `AzSetProperty` | `0x27D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `AzUpdateCache` | `0x27D80` | 112 | UnwindData |  |
| 2 | `AzApplicationClose` | `0x29090` | 405 | UnwindData |  |
| 3 | `AzApplicationCreate` | `0x29230` | 45 | UnwindData |  |
| 4 | `AzApplicationDelete` | `0x29270` | 40 | UnwindData |  |
| 5 | `AzApplicationEnum` | `0x292A0` | 39 | UnwindData |  |
| 6 | `AzApplicationOpen` | `0x292D0` | 192 | UnwindData |  |
| 9 | `AzContextAccessCheck` | `0x32820` | 4,283 | UnwindData |  |
| 10 | `AzContextGetAssignedScopesPage` | `0x338F0` | 1,390 | UnwindData |  |
| 11 | `AzContextGetRoles` | `0x346C0` | 48 | UnwindData |  |
| 19 | `AzInitializeContextFromName` | `0x35440` | 1,337 | UnwindData |  |
| 20 | `AzInitializeContextFromToken` | `0x35DA0` | 864 | UnwindData |  |
| 1 | `AzAddPropertyItem` | `0x38C90` | 444 | UnwindData |  |
| 25 | `AzRemovePropertyItem` | `0x38E60` | 562 | UnwindData |  |
| 14 | `AzGroupCreate` | `0x3CD00` | 115 | UnwindData |  |
| 15 | `AzGroupDelete` | `0x3CD80` | 98 | UnwindData |  |
| 16 | `AzGroupEnum` | `0x3CDF0` | 126 | UnwindData |  |
| 17 | `AzGroupOpen` | `0x3CE80` | 115 | UnwindData |  |
| 26 | `AzRoleCreate` | `0x3E120` | 115 | UnwindData |  |
| 27 | `AzRoleDelete` | `0x3E1A0` | 98 | UnwindData |  |
| 28 | `AzRoleEnum` | `0x3E210` | 108 | UnwindData |  |
| 29 | `AzRoleOpen` | `0x3E290` | 115 | UnwindData |  |
| 30 | `AzScopeCreate` | `0x4A9B0` | 48 | UnwindData |  |
| 31 | `AzScopeDelete` | `0x4A9F0` | 43 | UnwindData |  |
| 32 | `AzScopeEnum` | `0x4AA30` | 42 | UnwindData |  |
| 33 | `AzScopeOpen` | `0x4AA60` | 150 | UnwindData |  |
| 36 | `AzTaskCreate` | `0x4AFB0` | 115 | UnwindData |  |
| 37 | `AzTaskDelete` | `0x4B030` | 98 | UnwindData |  |
| 38 | `AzTaskEnum` | `0x4B0A0` | 108 | UnwindData |  |
| 39 | `AzTaskOpen` | `0x4B120` | 115 | UnwindData |  |
| 21 | `AzOperationCreate` | `0x4C250` | 48 | UnwindData |  |
| 22 | `AzOperationDelete` | `0x4C290` | 43 | UnwindData |  |
| 23 | `AzOperationEnum` | `0x4C2D0` | 42 | UnwindData |  |
| 24 | `AzOperationOpen` | `0x4C300` | 48 | UnwindData |  |
| 35 | `AzSubmit` | `0x4FD00` | 207 | UnwindData |  |
