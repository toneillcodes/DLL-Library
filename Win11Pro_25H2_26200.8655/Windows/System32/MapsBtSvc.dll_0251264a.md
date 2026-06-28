# Binary Specification: MapsBtSvc.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\MapsBtSvc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0251264a878db16563870d5347fd55e4bfe7d707095a5054aaa0299eb2c4c458`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 12 | `MapsBackgroundTransferService_SetServiceCallbacks` | `0x3610` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `MapsBackgroundTransferClassFactory_Register` | `0x39F0` | 239 | UnwindData |  |
| 2 | `MapsBackgroundTransferClassFactory_Revoke` | `0x3AF0` | 103 | UnwindData |  |
| 3 | `MapsBackgroundTransferService_CreateOrFindJob` | `0x4C30` | 1,746 | UnwindData |  |
| 4 | `MapsBackgroundTransferService_FreeJob` | `0x5310` | 101 | UnwindData |  |
| 5 | `MapsBackgroundTransferService_GetIsAnyJobWaiting` | `0x5380` | 330 | UnwindData |  |
| 6 | `MapsBackgroundTransferService_RegisterCallbacks` | `0x54D0` | 428 | UnwindData |  |
| 7 | `MapsBackgroundTransferService_SetNetworkCostPolicy` | `0x58D0` | 81 | UnwindData |  |
| 8 | `MapsBackgroundTransferService_SetPowerPolicy` | `0x5930` | 81 | UnwindData |  |
| 9 | `MapsBackgroundTransferService_SetPriority` | `0x5990` | 81 | UnwindData |  |
| 10 | `MapsBackgroundTransferService_TakeBitsSnapshot` | `0x59F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `MapsBackgroundTransferService_UnregisterCallbacks` | `0x5A00` | 333 | UnwindData |  |
