# Binary Specification: RTWorkQ.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\RTWorkQ.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ecc53be3f81d15b6bed373fc1f7c74d38a400aaefc05012fbfa18cfb66a3b38b`
* **Total Exported Functions:** 37

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 22 | `RtwqPutWaitingWorkItem` | `0x27A0` | 168 | UnwindData |  |
| 30 | `RtwqSetLongRunning` | `0x3150` | 137 | UnwindData |  |
| 23 | `RtwqPutWorkItem` | `0x3930` | 391 | UnwindData |  |
| 9 | `RtwqCancelDeadline` | `0x3D90` | 143 | UnwindData |  |
| 17 | `RtwqInvokeCallback` | `0x44D0` | 1,118 | UnwindData |  |
| 37 | `RtwqUnregisterPlatformFromMMCSS` | `0x7C90` | 35 | UnwindData |  |
| 25 | `RtwqRegisterPlatformWithMMCSS` | `0x7CC0` | 38 | UnwindData |  |
| 11 | `RtwqCreateAsyncResult` | `0x8140` | 45 | UnwindData |  |
| 20 | `RtwqLockSharedWorkQueue` | `0x93F0` | 36 | UnwindData |  |
| 34 | `RtwqUnlockPlatform` | `0x10C40` | 176 | UnwindData |  |
| 19 | `RtwqLockPlatform` | `0x10D20` | 112 | UnwindData |  |
| 27 | `RtwqScheduleWorkItem` | `0x11CA0` | 1,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `RtwqSetDeadline` | `0x120A0` | 5,536 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `RtwqGetWorkQueueMMCSSTaskId` | `0x13640` | 287 | UnwindData |  |
| 5 | `RtwqAllocateSerialWorkQueue` | `0x13770` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `RtwqUnlockWorkQueue` | `0x13BD0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `RtwqStartup` | `0x13C40` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `RtwqGetWorkQueueMMCSSPriority` | `0x13D00` | 294 | UnwindData |  |
| 18 | `RtwqJoinWorkQueue` | `0x13E50` | 281 | UnwindData |  |
| 7 | `RtwqBeginRegisterWorkQueueWithMMCSS` | `0x13FA0` | 265 | UnwindData |  |
| 33 | `RtwqUnjoinWorkQueue` | `0x143B0` | 263 | UnwindData |  |
| 6 | `RtwqAllocateWorkQueue` | `0x14690` | 1,424 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `RtwqRegisterPlatformEvents` | `0x14C20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `RtwqLockWorkQueue` | `0x14C40` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `RtwqAddPeriodicCallback` | `0x14E60` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `RtwqEndRegisterWorkQueueWithMMCSS` | `0x14FE0` | 69 | UnwindData |  |
| 29 | `RtwqSetDeadline2` | `0x15540` | 8 | UnwindData |  |
| 1 | `RtwqDebugGetOutstandingRefs` | `0x18AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `RtwqDebugSetCleanShutdown` | `0x18AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `RtwqGetPlatform` | `0x18AD0` | 16,272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `RtwqBeginUnregisterWorkQueueWithMMCSS` | `0x1CA60` | 149 | UnwindData |  |
| 10 | `RtwqCancelWorkItem` | `0x1CB00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `RtwqEndUnregisterWorkQueueWithMMCSS` | `0x1CB20` | 38 | UnwindData |  |
| 14 | `RtwqGetWorkQueueMMCSSClass` | `0x1CB50` | 194 | UnwindData |  |
| 26 | `RtwqRemovePeriodicCallback` | `0x1CC20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `RtwqShutdown` | `0x1CC40` | 33 | UnwindData |  |
| 36 | `RtwqUnregisterPlatformEvents` | `0x1CC70` | 8,448 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
