# Binary Specification: MapsStore.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\MapsStore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `faaf730c851117e54e028ee2e60525c748034b9f6e15fe0f23e1e709057a6f97`
* **Total Exported Functions:** 17

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 17 | `MapsStore_SetServiceCallbacks` | `0x11170` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `MapsStore_CancelGetData` | `0x11180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `MapsStore_CancelInstallation` | `0x111A0` | 95 | UnwindData |  |
| 3 | `MapsStore_CheckUpdateAsync` | `0x11210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `MapsStore_DeleteData` | `0x11230` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `MapsStore_FindNearbyPackages` | `0x11250` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `MapsStore_GetCopyright` | `0x11270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `MapsStore_GetData` | `0x11290` | 100 | UnwindData |  |
| 8 | `MapsStore_GetGSCode` | `0x11300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `MapsStore_Initialize` | `0x11320` | 86 | UnwindData |  |
| 10 | `MapsStore_InstallAsync` | `0x11380` | 36 | UnwindData |  |
| 11 | `MapsStore_IsMapFullyInstalled` | `0x113B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `MapsStore_LoadCatalogAsync` | `0x113D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `MapsStore_SuspendInstallation` | `0x113F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `MapsStore_UnInitialize` | `0x11410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `MapsStore_UpdateAsync` | `0x11430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `MapsStore_WaitInstallation` | `0x11450` | 563,116 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
