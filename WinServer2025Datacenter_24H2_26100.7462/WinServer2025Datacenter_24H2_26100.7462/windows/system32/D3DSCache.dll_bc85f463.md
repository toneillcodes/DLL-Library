# Binary Specification: D3DSCache.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\D3DSCache.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `bc85f463716f8c7157d1dba64a33adbcf18ad10adcd54f3fba4606991ae1a913`
* **Total Exported Functions:** 23

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 14 | `ShaderCache_FindValue` | `0x9C70` | 119 | UnwindData |  |
| 6 | `ShaderCache_Create` | `0xB430` | 163 | UnwindData |  |
| 10 | `ShaderCache_Destroy` | `0xC070` | 104 | UnwindData |  |
| 17 | `ShaderCache_FreeValue` | `0xC880` | 146 | UnwindData |  |
| 3 | `ShaderCache_AddValue` | `0xC9C0` | 121 | UnwindData |  |
| 5 | `ShaderCache_Clear` | `0xDAA0` | 97 | UnwindData |  |
| 20 | `ShaderCache_GetDesc` | `0xEDF0` | 110 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0xF570` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0xFAD0` | 35,600 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `ShaderCache_AddValue1` | `0x185E0` | 352 | UnwindData |  |
| 7 | `ShaderCache_Delete` | `0x18750` | 109 | UnwindData |  |
| 8 | `ShaderCache_DeleteGroup` | `0x187D0` | 72 | UnwindData |  |
| 9 | `ShaderCache_DeleteValue` | `0x18820` | 72 | UnwindData |  |
| 11 | `ShaderCache_FindGroup` | `0x18870` | 88 | UnwindData |  |
| 12 | `ShaderCache_FindGroupValueKeys` | `0x188D0` | 119 | UnwindData |  |
| 13 | `ShaderCache_FindGroupValues` | `0x18950` | 210 | UnwindData |  |
| 15 | `ShaderCache_FindValue1` | `0x18A30` | 349 | UnwindData |  |
| 16 | `ShaderCache_Flush` | `0x18BA0` | 91 | UnwindData |  |
| 18 | `ShaderCache_GetApplicationIdentity` | `0x18C10` | 89 | UnwindData |  |
| 19 | `ShaderCache_GetCompilerIdentity` | `0x18C70` | 89 | UnwindData |  |
| 21 | `ShaderCache_SetApplicationIdentity` | `0x18CD0` | 76 | UnwindData |  |
| 22 | `ShaderCache_SetCompilerIdentity` | `0x18D30` | 76 | UnwindData |  |
| 23 | `ShaderCache_StoreGroupValueKeys` | `0x18D90` | 132 | UnwindData |  |
