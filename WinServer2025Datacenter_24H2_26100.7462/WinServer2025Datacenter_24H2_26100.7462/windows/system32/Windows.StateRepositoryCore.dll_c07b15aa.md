# Binary Specification: Windows.StateRepositoryCore.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Windows.StateRepositoryCore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c07b15aa63ddc3b26456a3d224e97f665bb73d3c3a96da08bb1468b12a2111b4`
* **Total Exported Functions:** 41

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `SRCacheContext_AddToCache` | `0x7270` | 148 | UnwindData |  |
| 2 | `SRCacheContext_CacheInitialize` | `0x7310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `SRCacheContext_CacheReset` | `0x7320` | 88 | UnwindData |  |
| 4 | `SRCacheContext_CacheShutdown` | `0x7380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `SRCacheContext_Close` | `0x7390` | 20 | UnwindData |  |
| 6 | `SRCacheContext_Create` | `0x73B0` | 194 | UnwindData |  |
| 7 | `SRCacheContext_CreateSubContext` | `0x7480` | 251 | UnwindData |  |
| 8 | `SRCacheContext_Delete` | `0x7590` | 111 | UnwindData |  |
| 9 | `SRCacheContext_DeleteField` | `0x7610` | 138 | UnwindData |  |
| 10 | `SRCacheContext_DeleteIfEmpty` | `0x76A0` | 55 | UnwindData |  |
| 11 | `SRCacheContext_EnumerateData` | `0x76E0` | 55 | UnwindData |  |
| 12 | `SRCacheContext_EnumerateIndex` | `0x7720` | 55 | UnwindData |  |
| 13 | `SRCacheContext_GetField_Binary` | `0x7760` | 88 | UnwindData |  |
| 14 | `SRCacheContext_GetField_MultiString` | `0x77C0` | 115 | UnwindData |  |
| 15 | `SRCacheContext_GetField_String` | `0x7840` | 84 | UnwindData |  |
| 16 | `SRCacheContext_GetField_UInt32` | `0x78A0` | 105 | UnwindData |  |
| 17 | `SRCacheContext_GetField_UInt64` | `0x7910` | 105 | UnwindData |  |
| 18 | `SRCacheContext_HasSubKeys` | `0x7980` | 55 | UnwindData |  |
| 19 | `SRCacheContext_IsEmpty` | `0x79C0` | 55 | UnwindData |  |
| 20 | `SRCacheContext_Open` | `0x7A00` | 197 | UnwindData |  |
| 21 | `SRCacheContext_OpenSubContext` | `0x7AD0` | 264 | UnwindData |  |
| 22 | `SRCacheContext_SetField_Binary` | `0x7BE0` | 131 | UnwindData |  |
| 23 | `SRCacheContext_SetField_MultiString` | `0x7C70` | 112 | UnwindData |  |
| 24 | `SRCacheContext_SetField_String` | `0x7CF0` | 111 | UnwindData |  |
| 25 | `SRCacheContext_SetField_UInt32` | `0x7D70` | 122 | UnwindData |  |
| 26 | `SRCacheContext_SetField_UInt64` | `0x7DF0` | 125 | UnwindData |  |
| 27 | `SRCacheManager_Close` | `0xA920` | 20 | UnwindData |  |
| 28 | `SRCacheManager_DeleteContext` | `0xA940` | 122 | UnwindData |  |
| 29 | `SRCacheManager_GetProperty_UInt32` | `0xA9C0` | 116 | UnwindData |  |
| 30 | `SRCacheManager_GetProperty_UInt64` | `0xAA40` | 120 | UnwindData |  |
| 31 | `SRCacheManager_GetRevision` | `0xAAC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `SRCacheManager_Open` | `0xAAD0` | 307 | UnwindData |  |
| 33 | `SRCacheManager_SetProperty_UInt32` | `0xAC10` | 105 | UnwindData |  |
| 34 | `SRCacheManager_SetProperty_UInt64` | `0xAC80` | 108 | UnwindData |  |
| 35 | `SRCache_AllocBuffer` | `0xB1C0` | 64 | UnwindData |  |
| 36 | `SRCache_AllocStringBuffer` | `0xB210` | 53 | UnwindData |  |
| 37 | `SRCache_DuplicateBuffer` | `0xB250` | 132 | UnwindData |  |
| 38 | `SRCache_DuplicateString` | `0xB2E0` | 55 | UnwindData |  |
| 40 | `SRCache_Free` | `0xB320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `SRCache_GetDefaultAccountSid` | `0xB330` | 123 | UnwindData |  |
| 39 | `SRCache_ExpandMacros` | `0xB7C0` | 156 | UnwindData |  |
