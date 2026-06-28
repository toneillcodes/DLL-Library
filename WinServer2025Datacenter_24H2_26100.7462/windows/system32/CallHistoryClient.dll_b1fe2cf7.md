# Binary Specification: CallHistoryClient.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\CallHistoryClient.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b1fe2cf7bf899e276df40bd5a592ad955a182ea946208157ffeb99d0815db4b0`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DoesCallHistoryItemMatchFilter` | `0x9450` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `UdmAreCallEventsEqual` | `0x9570` | 88 | UnwindData |  |
| 10 | `UdmFreeCallHistoryItemSet` | `0x95D0` | 88 | UnwindData |  |
| 4 | `UdmCancelAsyncTask` | `0xA9E0` | 223 | UnwindData |  |
| 7 | `UdmCreateSyncCallbackHandler` | `0xAAD0` | 94 | UnwindData |  |
| 5 | `UdmCreateDataSession` | `0xC5F0` | 60 | UnwindData |  |
| 6 | `UdmCreateDataSessionForUser` | `0xC640` | 228 | UnwindData |  |
| 8 | `UdmDebugModifyNotifyState` | `0xC730` | 101 | UnwindData |  |
| 9 | `UdmFreeCallFavoriteItemSet` | `0xF9F0` | 81 | UnwindData |  |
| 2 | `StringToUdmObjectId` | `0x1ABD0` | 300 | UnwindData |  |
| 11 | `UdmObjectIdToString` | `0x1AD10` | 197 | UnwindData |  |
