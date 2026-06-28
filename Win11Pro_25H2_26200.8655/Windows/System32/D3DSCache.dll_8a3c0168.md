# Binary Specification: D3DSCache.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\D3DSCache.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8a3c016849c764b7e92aa0dfcc07699f419b0311b1058b6435309accee78f590`
* **Total Exported Functions:** 23

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 14 | `ShaderCache_FindValue` | `0x9CA0` | 119 | UnwindData |  |
| 6 | `ShaderCache_Create` | `0xB460` | 163 | UnwindData |  |
| 10 | `ShaderCache_Destroy` | `0xC0A0` | 104 | UnwindData |  |
| 17 | `ShaderCache_FreeValue` | `0xC8B0` | 146 | UnwindData |  |
| 3 | `ShaderCache_AddValue` | `0xC9F0` | 121 | UnwindData |  |
| 5 | `ShaderCache_Clear` | `0xDAD0` | 97 | UnwindData |  |
| 20 | `ShaderCache_GetDesc` | `0xEE20` | 110 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0xF4A0` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0xFA70` | 36,032 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `ShaderCache_AddValue1` | `0x18730` | 352 | UnwindData |  |
| 7 | `ShaderCache_Delete` | `0x188A0` | 109 | UnwindData |  |
| 8 | `ShaderCache_DeleteGroup` | `0x18920` | 72 | UnwindData |  |
| 9 | `ShaderCache_DeleteValue` | `0x18970` | 72 | UnwindData |  |
| 11 | `ShaderCache_FindGroup` | `0x189C0` | 88 | UnwindData |  |
| 12 | `ShaderCache_FindGroupValueKeys` | `0x18A20` | 119 | UnwindData |  |
| 13 | `ShaderCache_FindGroupValues` | `0x18AA0` | 210 | UnwindData |  |
| 15 | `ShaderCache_FindValue1` | `0x18B80` | 349 | UnwindData |  |
| 16 | `ShaderCache_Flush` | `0x18CF0` | 91 | UnwindData |  |
| 18 | `ShaderCache_GetApplicationIdentity` | `0x18D60` | 89 | UnwindData |  |
| 19 | `ShaderCache_GetCompilerIdentity` | `0x18DC0` | 89 | UnwindData |  |
| 21 | `ShaderCache_SetApplicationIdentity` | `0x18E20` | 76 | UnwindData |  |
| 22 | `ShaderCache_SetCompilerIdentity` | `0x18E80` | 76 | UnwindData |  |
| 23 | `ShaderCache_StoreGroupValueKeys` | `0x18EE0` | 132 | UnwindData |  |
