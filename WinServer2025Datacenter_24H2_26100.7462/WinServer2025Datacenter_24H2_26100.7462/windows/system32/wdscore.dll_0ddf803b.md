# Binary Specification: wdscore.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wdscore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0ddf803b747a036c3081343fa66259d57c94ded3aee2d3fd9814258f0f25f642`
* **Total Exported Functions:** 99

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 84 | `WdsSeqFree` | `0x2320` | 52 | UnwindData |  |
| 59 | `WdsInitializeCallbackArray` | `0x6020` | 260 | UnwindData |  |
| 1 | `WdsGetPointer` | `0x9F70` | 7,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `WdsAddModule` | `0xBE60` | 177 | UnwindData |  |
| 24 | `WdsAllocCollection` | `0xBF20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `WdsCollectionAddValue` | `0xBF40` | 122 | UnwindData |  |
| 26 | `WdsCollectionGetValue` | `0xBFC0` | 90 | UnwindData |  |
| 31 | `WdsDeleteEvent` | `0xC020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `WdsDuplicateData` | `0xC040` | 298 | UnwindData |  |
| 35 | `WdsEnableExit` | `0xC170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `WdsEnableExitEx` | `0xC190` | 177 | UnwindData |  |
| 38 | `WdsEnumFirstCollectionValue` | `0xC250` | 24 | UnwindData |  |
| 40 | `WdsEnumNextCollectionValue` | `0xC270` | 24 | UnwindData |  |
| 41 | `WdsExecuteWorkQueue` | `0xC290` | 1,757 | UnwindData |  |
| 42 | `WdsExecuteWorkQueue2` | `0xC980` | 1,878 | UnwindData |  |
| 43 | `WdsExecuteWorkQueueEx` | `0xD0E0` | 53 | UnwindData |  |
| 44 | `WdsExitImmediately` | `0xD120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `WdsExitImmediatelyEx` | `0xD140` | 177 | UnwindData |  |
| 46 | `WdsFreeCollection` | `0xD200` | 74 | UnwindData |  |
| 47 | `WdsFreeData` | `0xD250` | 101 | UnwindData |  |
| 55 | `WdsGetCurrentExecutionGroup` | `0xD2C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `WdsGetTempDir` | `0xD2F0` | 387 | UnwindData |  |
| 58 | `WdsInitialize` | `0xD480` | 434 | UnwindData |  |
| 60 | `WdsInitializeDataBinary` | `0xD640` | 138 | UnwindData |  |
| 61 | `WdsInitializeDataStringA` | `0xD6D0` | 141 | UnwindData |  |
| 62 | `WdsInitializeDataStringW` | `0xD770` | 141 | UnwindData |  |
| 63 | `WdsInitializeDataUInt32` | `0xD810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `WdsInitializeDataUInt64` | `0xD830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `WdsIterateOfflineQueue` | `0xD850` | 270 | UnwindData |  |
| 67 | `WdsIterateQueue` | `0xD970` | 78 | UnwindData |  |
| 69 | `WdsLockExecutionGroup` | `0xD9D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `WdsPackCollection` | `0xD9F0` | 497 | UnwindData |  |
| 78 | `WdsPublish` | `0xDBF0` | 68 | UnwindData |  |
| 79 | `WdsPublishEx` | `0xDC40` | 74 | UnwindData |  |
| 80 | `WdsPublishImmediateAsync` | `0xDC90` | 65 | UnwindData |  |
| 81 | `WdsPublishImmediateEx` | `0xDCE0` | 55 | UnwindData |  |
| 82 | `WdsPublishOffline` | `0xDD20` | 353 | UnwindData |  |
| 83 | `WdsSeqAlloc` | `0xDE90` | 97 | UnwindData |  |
| 87 | `WdsSetNextExecutionGroup` | `0xDF00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `WdsSetUILanguage` | `0xDF20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `WdsSubscribeEx` | `0xDF40` | 58 | UnwindData |  |
| 94 | `WdsTerminate` | `0xDF80` | 90 | UnwindData |  |
| 95 | `WdsUnlockExecutionGroup` | `0xDFE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `WdsUnpackCollection` | `0xE000` | 820 | UnwindData |  |
| 97 | `WdsUnsubscribe` | `0xE340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `WdsUnsubscribeEx` | `0xE360` | 45 | UnwindData |  |
| 21 | `WdsAbortBlackboardItemEnum` | `0x18BB0` | 178 | UnwindData |  |
| 27 | `WdsCopyBlackboardItems` | `0x18C70` | 26 | UnwindData |  |
| 28 | `WdsCopyBlackboardItemsEx` | `0x18C90` | 690 | UnwindData |  |
| 29 | `WdsCreateBlackboard` | `0x18F50` | 83 | UnwindData |  |
| 30 | `WdsDeleteBlackboardValue` | `0x18FB0` | 224 | UnwindData |  |
| 32 | `WdsDestroyBlackboard` | `0x190A0` | 71 | UnwindData |  |
| 37 | `WdsEnumFirstBlackboardItem` | `0x190F0` | 506 | UnwindData |  |
| 39 | `WdsEnumNextBlackboardItem` | `0x192F0` | 161 | UnwindData |  |
| 50 | `WdsGetBlackboardBinaryData` | `0x193A0` | 386 | UnwindData |  |
| 51 | `WdsGetBlackboardStringA` | `0x19530` | 518 | UnwindData |  |
| 52 | `WdsGetBlackboardStringW` | `0x19740` | 409 | UnwindData |  |
| 53 | `WdsGetBlackboardUintPtr` | `0x198E0` | 335 | UnwindData |  |
| 54 | `WdsGetBlackboardValue` | `0x19A40` | 278 | UnwindData |  |
| 68 | `WdsLockBlackboardValue` | `0x19B60` | 286 | UnwindData |  |
| 86 | `WdsSetBlackboardValue` | `0x19C90` | 535 | UnwindData |  |
| 99 | `WdsValidBlackboard` | `0x19EB0` | 153 | UnwindData |  |
| 4 | `ConstructPartialMsgIfA` | `0x1B790` | 50 | UnwindData |  |
| 5 | `ConstructPartialMsgIfW` | `0x1B7D0` | 50 | UnwindData |  |
| 6 | `ConstructPartialMsgVA` | `0x1B810` | 337 | UnwindData |  |
| 7 | `ConstructPartialMsgVW` | `0x1B970` | 562 | UnwindData |  |
| 8 | `CurrentIP` | `0x1BBB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `DecrementPartialMsgIndent` | `0x1BBC0` | 37 | UnwindData |  |
| 10 | `DestructPartialMsg` | `0x1BBF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `EndMajorTask` | `0x1BC00` | 54 | UnwindData |  |
| 12 | `EndMinorTask` | `0x1BC40` | 68 | UnwindData |  |
| 13 | `GetMajorTask` | `0x1BC90` | 73 | UnwindData |  |
| 14 | `GetMajorTaskA` | `0x1BCE0` | 75 | UnwindData |  |
| 15 | `GetMinorTask` | `0x1BD40` | 93 | UnwindData |  |
| 16 | `GetMinorTaskA` | `0x1BDB0` | 95 | UnwindData |  |
| 17 | `GetPartialMsgIndent` | `0x1BE20` | 30 | UnwindData |  |
| 18 | `IncrementPartialMsgIndent` | `0x1BE50` | 38 | UnwindData |  |
| 19 | `StartMajorTask` | `0x1BE80` | 233 | UnwindData |  |
| 20 | `StartMinorTask` | `0x1BF70` | 138 | UnwindData |  |
| 23 | `WdsAddUsmtLogStack` | `0x1C000` | 1,522 | UnwindData |  |
| 34 | `WdsEnableDiagnosticMode` | `0x1C600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `WdsGenericSetupLogInit` | `0x1C610` | 1,020 | UnwindData |  |
| 49 | `WdsGetAssertFlags` | `0x1CA20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `WdsGetSetupLog` | `0x1CA40` | 149 | UnwindData |  |
| 65 | `WdsIsDiagnosticModeEnabled` | `0x1CAE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `WdsLogStructuredException` | `0x1CAF0` | 577 | UnwindData |  |
| 85 | `WdsSetAssertFlags` | `0x1CD40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `WdsSetupLogDestroy` | `0x1CD60` | 125 | UnwindData |  |
| 90 | `WdsSetupLogInit` | `0x1CDF0` | 3,544 | UnwindData |  |
| 91 | `WdsSetupLogMessageA` | `0x1DBD0` | 838 | UnwindData |  |
| 92 | `WdsSetupLogMessageW` | `0x1DF20` | 1,067 | UnwindData |  |
| 70 | `WdsLogCreate` | `0x20540` | 129 | UnwindData |  |
| 71 | `WdsLogDestroy` | `0x205D0` | 20 | UnwindData |  |
| 72 | `WdsLogRegStockProviders` | `0x20BC0` | 167 | UnwindData |  |
| 73 | `WdsLogRegisterProvider` | `0x20C70` | 305 | UnwindData |  |
| 75 | `WdsLogUnRegStockProviders` | `0x20DB0` | 111 | UnwindData |  |
| 76 | `WdsLogUnRegisterProvider` | `0x20E30` | 194 | UnwindData |  |
| 2 | `g_Kernel32` | `0x3C000` | 1,044 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `g_bEnableDiagnosticMode` | `0x3C414` | 0 | Indeterminate |  |
