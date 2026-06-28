# Binary Specification: RTWorkQ.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\RTWorkQ.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9eba26af2955e1a01356bca55bafabd0242fab4d8914c76132baea14065e7b4e`
* **Total Exported Functions:** 37

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 22 | `RtwqPutWaitingWorkItem` | `0x27A0` | 168 | UnwindData |  |
| 30 | `RtwqSetLongRunning` | `0x3150` | 137 | UnwindData |  |
| 23 | `RtwqPutWorkItem` | `0x3930` | 391 | UnwindData |  |
| 9 | `RtwqCancelDeadline` | `0x3DA0` | 143 | UnwindData |  |
| 17 | `RtwqInvokeCallback` | `0x44E0` | 1,118 | UnwindData |  |
| 37 | `RtwqUnregisterPlatformFromMMCSS` | `0x7CA0` | 35 | UnwindData |  |
| 25 | `RtwqRegisterPlatformWithMMCSS` | `0x7CD0` | 38 | UnwindData |  |
| 11 | `RtwqCreateAsyncResult` | `0x8150` | 45 | UnwindData |  |
| 20 | `RtwqLockSharedWorkQueue` | `0x9400` | 36 | UnwindData |  |
| 34 | `RtwqUnlockPlatform` | `0x10C50` | 176 | UnwindData |  |
| 19 | `RtwqLockPlatform` | `0x10D30` | 112 | UnwindData |  |
| 27 | `RtwqScheduleWorkItem` | `0x11CB0` | 1,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `RtwqSetDeadline` | `0x120B0` | 5,536 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `RtwqGetWorkQueueMMCSSTaskId` | `0x13650` | 287 | UnwindData |  |
| 5 | `RtwqAllocateSerialWorkQueue` | `0x13780` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `RtwqUnlockWorkQueue` | `0x13BE0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `RtwqStartup` | `0x13C50` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `RtwqGetWorkQueueMMCSSPriority` | `0x13D10` | 294 | UnwindData |  |
| 18 | `RtwqJoinWorkQueue` | `0x13E60` | 281 | UnwindData |  |
| 7 | `RtwqBeginRegisterWorkQueueWithMMCSS` | `0x13FB0` | 265 | UnwindData |  |
| 33 | `RtwqUnjoinWorkQueue` | `0x143C0` | 263 | UnwindData |  |
| 6 | `RtwqAllocateWorkQueue` | `0x146A0` | 1,424 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `RtwqRegisterPlatformEvents` | `0x14C30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `RtwqLockWorkQueue` | `0x14C50` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `RtwqAddPeriodicCallback` | `0x14E70` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `RtwqEndRegisterWorkQueueWithMMCSS` | `0x14FF0` | 69 | UnwindData |  |
| 29 | `RtwqSetDeadline2` | `0x15550` | 8 | UnwindData |  |
| 1 | `RtwqDebugGetOutstandingRefs` | `0x18B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `RtwqDebugSetCleanShutdown` | `0x18B10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `RtwqGetPlatform` | `0x18B20` | 16,064 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `RtwqBeginUnregisterWorkQueueWithMMCSS` | `0x1C9E0` | 149 | UnwindData |  |
| 10 | `RtwqCancelWorkItem` | `0x1CA80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `RtwqEndUnregisterWorkQueueWithMMCSS` | `0x1CAA0` | 38 | UnwindData |  |
| 14 | `RtwqGetWorkQueueMMCSSClass` | `0x1CAD0` | 194 | UnwindData |  |
| 26 | `RtwqRemovePeriodicCallback` | `0x1CBA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `RtwqShutdown` | `0x1CBC0` | 33 | UnwindData |  |
| 36 | `RtwqUnregisterPlatformEvents` | `0x1CBF0` | 8,464 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
