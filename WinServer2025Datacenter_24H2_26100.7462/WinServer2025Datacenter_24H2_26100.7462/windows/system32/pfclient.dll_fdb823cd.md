# Binary Specification: pfclient.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\pfclient.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fdb823cd38fb46f44aa81224b565bc772b40cd3452ef5bf0c0f804f8c0c27402`
* **Total Exported Functions:** 57

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 22 | `PfIuHistoryGet` | `0x1ED0` | 289 | UnwindData |  |
| 23 | `PfIuHistoryGetEx` | `0x2000` | 38 | UnwindData |  |
| 24 | `PfIuPredictFirstLongestRange` | `0x2090` | 831 | UnwindData |  |
| 25 | `PfIuPredictionsDataClose` | `0x23E0` | 87 | UnwindData |  |
| 26 | `PfIuPredictionsDataOpen` | `0x2440` | 214 | UnwindData |  |
| 27 | `PfIuRestartAcceptable` | `0x28A0` | 330 | UnwindData |  |
| 28 | `PfIuUptimeStatsGet` | `0x29F0` | 139 | UnwindData |  |
| 29 | `PfRpcSendCommand` | `0x2DC0` | 242 | UnwindData |  |
| 30 | `PfRpcServiceIsRunning` | `0x2EC0` | 880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `PfRpcSyncPrefetchforBoot` | `0x3230` | 256 | UnwindData |  |
| 32 | `PfsForceCrash` | `0x3350` | 136 | UnwindData |  |
| 33 | `PfsGetPageCount` | `0x33E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `SwGetPageCount` | `0x33E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `SwGetPageCount64` | `0x33E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `PfsOfferMemory` | `0x3400` | 439 | UnwindData |  |
| 35 | `PfsOfferableHeapAlloc` | `0x36E0` | 302 | UnwindData |  |
| 36 | `PfsOfferableHeapCleanup` | `0x3820` | 94 | UnwindData |  |
| 37 | `PfsOfferableHeapFree` | `0x3AB0` | 189 | UnwindData |  |
| 38 | `PfsOfferableHeapInitialize` | `0x3B80` | 73 | UnwindData |  |
| 39 | `PfsOfferableHeapOffer` | `0x3BD0` | 86 | UnwindData |  |
| 40 | `PfsOfferableHeapReclaim` | `0x3C30` | 74 | UnwindData |  |
| 41 | `PfsOfferableHeapStart` | `0x3C80` | 413 | UnwindData |  |
| 42 | `PfsSwCtxCleanup` | `0x3F00` | 46 | UnwindData |  |
| 43 | `PfsSwCtxCommitSnapshot` | `0x3F40` | 115 | UnwindData |  |
| 44 | `PfsSwCtxInitialize` | `0x3FC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `PfsSwCtxStart` | `0x3FE0` | 282 | UnwindData |  |
| 46 | `PfsSwCtxUpdateSnapshot` | `0x4100` | 144 | UnwindData |  |
| 47 | `PfsSwGetAverageValue` | `0x41A0` | 185 | UnwindData |  |
| 48 | `PfsSwGetDeltaValue` | `0x4260` | 139 | UnwindData |  |
| 49 | `PfsVaMgrAlloc` | `0x4300` | 524 | UnwindData |  |
| 50 | `PfsVaMgrCleanup` | `0x4520` | 140 | UnwindData |  |
| 51 | `PfsVaMgrFree` | `0x45C0` | 353 | UnwindData |  |
| 52 | `PfsVaMgrInitialize` | `0x4730` | 137 | UnwindData |  |
| 53 | `PfsVaMgrVerify` | `0x4870` | 211 | UnwindData |  |
| 54 | `SmuCacheHitsControl` | `0x4950` | 145 | UnwindData |  |
| 55 | `SmuGetControlDeviceHandle` | `0x49F0` | 211 | UnwindData |  |
| 1 | `MemUtilEmptyProcess` | `0x4AD0` | 198 | UnwindData |  |
| 2 | `MemUtilGetNextRegionInfo` | `0x4BA0` | 218 | UnwindData |  |
| 3 | `MemUtilIsLowMemPolicyActive` | `0x4DC0` | 76 | UnwindData |  |
| 4 | `MemUtilIsProcessGroupTooLargeForSwap` | `0x4E20` | 281 | UnwindData |  |
| 5 | `MemUtilIsWorkingSetTooLargeForSwap` | `0x4F40` | 134 | UnwindData |  |
| 6 | `MemUtilPrioritizeWsPages` | `0x4FD0` | 810 | UnwindData |  |
| 7 | `MemUtilQueryGpuUtilization` | `0x5490` | 154 | UnwindData |  |
| 8 | `MemUtilQueryProcessCommit` | `0x5530` | 233 | UnwindData |  |
| 9 | `MemUtilQueryProcessMetrics` | `0x5620` | 501 | UnwindData |  |
| 10 | `MemUtilVAQueryCtxAdd` | `0x5A50` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `MemUtilVAQueryCtxCleanup` | `0x5A80` | 39 | UnwindData |  |
| 12 | `MemUtilVAQueryCtxComplete` | `0x5AB0` | 27 | UnwindData |  |
| 13 | `MemUtilVAQueryCtxInitialize` | `0x5AE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `MemUtilVAQueryCtxIssue` | `0x5B00` | 131 | UnwindData |  |
| 15 | `MemUtilVAQueryCtxStart` | `0x5B90` | 112 | UnwindData |  |
| 16 | `MemWatcherCleanup` | `0x5C40` | 207 | UnwindData |  |
| 17 | `MemWatcherComputeStandbyLifetime` | `0x5D20` | 485 | UnwindData |  |
| 18 | `MemWatcherInitialize` | `0x5F10` | 105 | UnwindData |  |
| 19 | `MemWatcherQueryMetrics` | `0x6060` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `MemWatcherSetThresholds` | `0x61F0` | 78 | UnwindData |  |
| 21 | `MemWatcherStart` | `0x6250` | 438 | UnwindData |  |
