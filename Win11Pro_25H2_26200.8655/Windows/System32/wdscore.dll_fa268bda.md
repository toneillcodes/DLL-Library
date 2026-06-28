# Binary Specification: wdscore.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wdscore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fa268bdaf5436462f7de41733bd2076a34b3135255ce8ca943f0c69f4682ef3a`
* **Total Exported Functions:** 99

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 84 | `WdsSeqFree` | `0x2550` | 52 | UnwindData |  |
| 59 | `WdsInitializeCallbackArray` | `0x6250` | 260 | UnwindData |  |
| 1 | `WdsGetPointer` | `0xA1A0` | 7,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `WdsAddModule` | `0xC090` | 177 | UnwindData |  |
| 24 | `WdsAllocCollection` | `0xC150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `WdsCollectionAddValue` | `0xC170` | 122 | UnwindData |  |
| 26 | `WdsCollectionGetValue` | `0xC1F0` | 90 | UnwindData |  |
| 31 | `WdsDeleteEvent` | `0xC250` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `WdsDuplicateData` | `0xC270` | 298 | UnwindData |  |
| 35 | `WdsEnableExit` | `0xC3A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `WdsEnableExitEx` | `0xC3C0` | 177 | UnwindData |  |
| 38 | `WdsEnumFirstCollectionValue` | `0xC480` | 24 | UnwindData |  |
| 40 | `WdsEnumNextCollectionValue` | `0xC4A0` | 24 | UnwindData |  |
| 41 | `WdsExecuteWorkQueue` | `0xC4C0` | 1,757 | UnwindData |  |
| 42 | `WdsExecuteWorkQueue2` | `0xCBB0` | 1,878 | UnwindData |  |
| 43 | `WdsExecuteWorkQueueEx` | `0xD310` | 53 | UnwindData |  |
| 44 | `WdsExitImmediately` | `0xD350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `WdsExitImmediatelyEx` | `0xD370` | 177 | UnwindData |  |
| 46 | `WdsFreeCollection` | `0xD430` | 74 | UnwindData |  |
| 47 | `WdsFreeData` | `0xD480` | 101 | UnwindData |  |
| 55 | `WdsGetCurrentExecutionGroup` | `0xD4F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `WdsGetTempDir` | `0xD520` | 387 | UnwindData |  |
| 58 | `WdsInitialize` | `0xD6B0` | 434 | UnwindData |  |
| 60 | `WdsInitializeDataBinary` | `0xD870` | 138 | UnwindData |  |
| 61 | `WdsInitializeDataStringA` | `0xD900` | 141 | UnwindData |  |
| 62 | `WdsInitializeDataStringW` | `0xD9A0` | 141 | UnwindData |  |
| 63 | `WdsInitializeDataUInt32` | `0xDA40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `WdsInitializeDataUInt64` | `0xDA60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `WdsIterateOfflineQueue` | `0xDA80` | 270 | UnwindData |  |
| 67 | `WdsIterateQueue` | `0xDBA0` | 78 | UnwindData |  |
| 69 | `WdsLockExecutionGroup` | `0xDC00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `WdsPackCollection` | `0xDC20` | 497 | UnwindData |  |
| 78 | `WdsPublish` | `0xDE20` | 68 | UnwindData |  |
| 79 | `WdsPublishEx` | `0xDE70` | 74 | UnwindData |  |
| 80 | `WdsPublishImmediateAsync` | `0xDEC0` | 65 | UnwindData |  |
| 81 | `WdsPublishImmediateEx` | `0xDF10` | 55 | UnwindData |  |
| 82 | `WdsPublishOffline` | `0xDF50` | 353 | UnwindData |  |
| 83 | `WdsSeqAlloc` | `0xE0C0` | 97 | UnwindData |  |
| 87 | `WdsSetNextExecutionGroup` | `0xE130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `WdsSetUILanguage` | `0xE150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `WdsSubscribeEx` | `0xE170` | 58 | UnwindData |  |
| 94 | `WdsTerminate` | `0xE1B0` | 90 | UnwindData |  |
| 95 | `WdsUnlockExecutionGroup` | `0xE210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `WdsUnpackCollection` | `0xE230` | 820 | UnwindData |  |
| 97 | `WdsUnsubscribe` | `0xE570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `WdsUnsubscribeEx` | `0xE590` | 45 | UnwindData |  |
| 21 | `WdsAbortBlackboardItemEnum` | `0x18DE0` | 178 | UnwindData |  |
| 27 | `WdsCopyBlackboardItems` | `0x18EA0` | 26 | UnwindData |  |
| 28 | `WdsCopyBlackboardItemsEx` | `0x18EC0` | 690 | UnwindData |  |
| 29 | `WdsCreateBlackboard` | `0x19180` | 83 | UnwindData |  |
| 30 | `WdsDeleteBlackboardValue` | `0x191E0` | 224 | UnwindData |  |
| 32 | `WdsDestroyBlackboard` | `0x192D0` | 71 | UnwindData |  |
| 37 | `WdsEnumFirstBlackboardItem` | `0x19320` | 506 | UnwindData |  |
| 39 | `WdsEnumNextBlackboardItem` | `0x19520` | 161 | UnwindData |  |
| 50 | `WdsGetBlackboardBinaryData` | `0x195D0` | 386 | UnwindData |  |
| 51 | `WdsGetBlackboardStringA` | `0x19760` | 518 | UnwindData |  |
| 52 | `WdsGetBlackboardStringW` | `0x19970` | 409 | UnwindData |  |
| 53 | `WdsGetBlackboardUintPtr` | `0x19B10` | 335 | UnwindData |  |
| 54 | `WdsGetBlackboardValue` | `0x19C70` | 278 | UnwindData |  |
| 68 | `WdsLockBlackboardValue` | `0x19D90` | 286 | UnwindData |  |
| 86 | `WdsSetBlackboardValue` | `0x19EC0` | 535 | UnwindData |  |
| 99 | `WdsValidBlackboard` | `0x1A0E0` | 153 | UnwindData |  |
| 4 | `ConstructPartialMsgIfA` | `0x227C0` | 50 | UnwindData |  |
| 5 | `ConstructPartialMsgIfW` | `0x22800` | 50 | UnwindData |  |
| 6 | `ConstructPartialMsgVA` | `0x22840` | 337 | UnwindData |  |
| 7 | `ConstructPartialMsgVW` | `0x229A0` | 511 | UnwindData |  |
| 8 | `CurrentIP` | `0x22BB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `DecrementPartialMsgIndent` | `0x22BC0` | 37 | UnwindData |  |
| 10 | `DestructPartialMsg` | `0x22BF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `EndMajorTask` | `0x22C00` | 54 | UnwindData |  |
| 12 | `EndMinorTask` | `0x22C40` | 68 | UnwindData |  |
| 13 | `GetMajorTask` | `0x22C90` | 73 | UnwindData |  |
| 14 | `GetMajorTaskA` | `0x22CE0` | 75 | UnwindData |  |
| 15 | `GetMinorTask` | `0x22D40` | 93 | UnwindData |  |
| 16 | `GetMinorTaskA` | `0x22DB0` | 95 | UnwindData |  |
| 17 | `GetPartialMsgIndent` | `0x22E20` | 30 | UnwindData |  |
| 18 | `IncrementPartialMsgIndent` | `0x22E50` | 38 | UnwindData |  |
| 19 | `StartMajorTask` | `0x22E80` | 233 | UnwindData |  |
| 20 | `StartMinorTask` | `0x22F70` | 138 | UnwindData |  |
| 23 | `WdsAddUsmtLogStack` | `0x23000` | 1,522 | UnwindData |  |
| 34 | `WdsEnableDiagnosticMode` | `0x23600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `WdsGenericSetupLogInit` | `0x23610` | 1,020 | UnwindData |  |
| 49 | `WdsGetAssertFlags` | `0x23A20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `WdsGetSetupLog` | `0x23A40` | 149 | UnwindData |  |
| 65 | `WdsIsDiagnosticModeEnabled` | `0x23AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `WdsLogStructuredException` | `0x23AF0` | 577 | UnwindData |  |
| 85 | `WdsSetAssertFlags` | `0x23D40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `WdsSetupLogDestroy` | `0x23D60` | 125 | UnwindData |  |
| 90 | `WdsSetupLogInit` | `0x23DF0` | 3,544 | UnwindData |  |
| 91 | `WdsSetupLogMessageA` | `0x24BD0` | 838 | UnwindData |  |
| 92 | `WdsSetupLogMessageW` | `0x24F20` | 1,067 | UnwindData |  |
| 70 | `WdsLogCreate` | `0x27DD0` | 129 | UnwindData |  |
| 71 | `WdsLogDestroy` | `0x27E60` | 20 | UnwindData |  |
| 72 | `WdsLogRegStockProviders` | `0x28450` | 167 | UnwindData |  |
| 73 | `WdsLogRegisterProvider` | `0x28500` | 305 | UnwindData |  |
| 75 | `WdsLogUnRegStockProviders` | `0x28640` | 111 | UnwindData |  |
| 76 | `WdsLogUnRegisterProvider` | `0x286C0` | 194 | UnwindData |  |
| 2 | `g_Kernel32` | `0x45000` | 1,364 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `g_bEnableDiagnosticMode` | `0x45554` | 0 | Indeterminate |  |
