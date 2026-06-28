# Binary Specification: MapsStore.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\MapsStore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ccfa533ad3ecbb545cf5ac36ffcb99752bb03a0536b2bd71146fd8f3cb732828`
* **Total Exported Functions:** 17

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 17 | `MapsStore_SetServiceCallbacks` | `0x11150` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `MapsStore_CancelGetData` | `0x11160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `MapsStore_CancelInstallation` | `0x11180` | 95 | UnwindData |  |
| 3 | `MapsStore_CheckUpdateAsync` | `0x111F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `MapsStore_DeleteData` | `0x11210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `MapsStore_FindNearbyPackages` | `0x11230` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `MapsStore_GetCopyright` | `0x11250` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `MapsStore_GetData` | `0x11270` | 100 | UnwindData |  |
| 8 | `MapsStore_GetGSCode` | `0x112E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `MapsStore_Initialize` | `0x11300` | 86 | UnwindData |  |
| 10 | `MapsStore_InstallAsync` | `0x11360` | 36 | UnwindData |  |
| 11 | `MapsStore_IsMapFullyInstalled` | `0x11390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `MapsStore_LoadCatalogAsync` | `0x113B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `MapsStore_SuspendInstallation` | `0x113D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `MapsStore_UnInitialize` | `0x113F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `MapsStore_UpdateAsync` | `0x11410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `MapsStore_WaitInstallation` | `0x11430` | 563,116 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
