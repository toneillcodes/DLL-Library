# Binary Specification: Windows.StateRepositoryCore.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Windows.StateRepositoryCore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8a7456bbf5341108e11a0f71bd08ecc69a2470f01b98be49ffa2e630089f4ca8`
* **Total Exported Functions:** 41

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `SRCacheContext_AddToCache` | `0xB890` | 148 | UnwindData |  |
| 2 | `SRCacheContext_CacheInitialize` | `0xB930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `SRCacheContext_CacheReset` | `0xB940` | 90 | UnwindData |  |
| 4 | `SRCacheContext_CacheShutdown` | `0xB9A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `SRCacheContext_Close` | `0xB9B0` | 20 | UnwindData |  |
| 6 | `SRCacheContext_Create` | `0xB9D0` | 194 | UnwindData |  |
| 7 | `SRCacheContext_CreateSubContext` | `0xBAA0` | 251 | UnwindData |  |
| 8 | `SRCacheContext_Delete` | `0xBBB0` | 111 | UnwindData |  |
| 9 | `SRCacheContext_DeleteField` | `0xBC30` | 138 | UnwindData |  |
| 10 | `SRCacheContext_DeleteIfEmpty` | `0xBCC0` | 55 | UnwindData |  |
| 11 | `SRCacheContext_EnumerateData` | `0xBD00` | 55 | UnwindData |  |
| 12 | `SRCacheContext_EnumerateIndex` | `0xBD40` | 55 | UnwindData |  |
| 13 | `SRCacheContext_GetField_Binary` | `0xBD80` | 88 | UnwindData |  |
| 14 | `SRCacheContext_GetField_MultiString` | `0xBDE0` | 115 | UnwindData |  |
| 15 | `SRCacheContext_GetField_String` | `0xBE60` | 84 | UnwindData |  |
| 16 | `SRCacheContext_GetField_UInt32` | `0xBEC0` | 105 | UnwindData |  |
| 17 | `SRCacheContext_GetField_UInt64` | `0xBF30` | 105 | UnwindData |  |
| 18 | `SRCacheContext_HasSubKeys` | `0xBFA0` | 55 | UnwindData |  |
| 19 | `SRCacheContext_IsEmpty` | `0xBFE0` | 55 | UnwindData |  |
| 20 | `SRCacheContext_Open` | `0xC020` | 197 | UnwindData |  |
| 21 | `SRCacheContext_OpenSubContext` | `0xC0F0` | 264 | UnwindData |  |
| 22 | `SRCacheContext_SetField_Binary` | `0xC200` | 131 | UnwindData |  |
| 23 | `SRCacheContext_SetField_MultiString` | `0xC290` | 112 | UnwindData |  |
| 24 | `SRCacheContext_SetField_String` | `0xC310` | 111 | UnwindData |  |
| 25 | `SRCacheContext_SetField_UInt32` | `0xC390` | 122 | UnwindData |  |
| 26 | `SRCacheContext_SetField_UInt64` | `0xC410` | 125 | UnwindData |  |
| 27 | `SRCacheManager_Close` | `0xC6B0` | 20 | UnwindData |  |
| 28 | `SRCacheManager_DeleteContext` | `0xC6D0` | 122 | UnwindData |  |
| 29 | `SRCacheManager_GetProperty_UInt32` | `0xC750` | 116 | UnwindData |  |
| 30 | `SRCacheManager_GetProperty_UInt64` | `0xC7D0` | 120 | UnwindData |  |
| 31 | `SRCacheManager_GetRevision` | `0xC850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `SRCacheManager_Open` | `0xC860` | 307 | UnwindData |  |
| 33 | `SRCacheManager_SetProperty_UInt32` | `0xC9A0` | 105 | UnwindData |  |
| 34 | `SRCacheManager_SetProperty_UInt64` | `0xCA10` | 108 | UnwindData |  |
| 35 | `SRCache_AllocBuffer` | `0xCD40` | 64 | UnwindData |  |
| 36 | `SRCache_AllocStringBuffer` | `0xCD90` | 53 | UnwindData |  |
| 37 | `SRCache_DuplicateBuffer` | `0xCDD0` | 132 | UnwindData |  |
| 38 | `SRCache_DuplicateString` | `0xCE60` | 55 | UnwindData |  |
| 40 | `SRCache_Free` | `0xCEA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `SRCache_GetDefaultAccountSid` | `0xCEB0` | 136 | UnwindData |  |
| 39 | `SRCache_ExpandMacros` | `0xD350` | 156 | UnwindData |  |
