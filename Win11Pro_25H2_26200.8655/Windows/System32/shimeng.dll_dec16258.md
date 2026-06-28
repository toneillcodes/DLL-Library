# Binary Specification: shimeng.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\shimeng.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `dec162584ac84ddc2b7caa0f523cf81431df958b1f02288b9406301ec5a913b2`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `SE_DllLoaded` | `0x0` | - | Forwarded | Forwarded to: `APPHELP.SE_DllLoaded` |
| 2 | `SE_DllUnloaded` | `0x0` | - | Forwarded | Forwarded to: `APPHELP.SE_DllUnloaded` |
| 3 | `SE_DynamicShim` | `0x0` | - | Forwarded | Forwarded to: `APPHELP.SE_DynamicShim` |
| 4 | `SE_GetHookAPIs` | `0x0` | - | Forwarded | Forwarded to: `APPHELP.SE_GetHookAPIs` |
| 5 | `SE_GetMaxShimCount` | `0x0` | - | Forwarded | Forwarded to: `APPHELP.SE_GetMaxShimCount` |
| 6 | `SE_GetProcAddressIgnoreIncExc` | `0x0` | - | Forwarded | Forwarded to: `APPHELP.SE_GetProcAddressIgnoreIncExc` |
| 7 | `SE_GetShimCount` | `0x0` | - | Forwarded | Forwarded to: `APPHELP.SE_GetShimCount` |
| 8 | `SE_InstallAfterInit` | `0x0` | - | Forwarded | Forwarded to: `APPHELP.SE_InstallAfterInit` |
| 9 | `SE_InstallBeforeInit` | `0x0` | - | Forwarded | Forwarded to: `APPHELP.SE_InstallBeforeInit` |
| 10 | `SE_IsShimDll` | `0x0` | - | Forwarded | Forwarded to: `APPHELP.SE_IsShimDll` |
| 11 | `SE_ProcessDying` | `0x0` | - | Forwarded | Forwarded to: `APPHELP.SE_ProcessDying` |
