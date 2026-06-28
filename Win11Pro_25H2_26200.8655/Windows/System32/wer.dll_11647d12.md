# Binary Specification: wer.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wer.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `11647d122caaf3cdd7f324115c905a158b2322684a0c03fe4889bffdfe86404c`
* **Total Exported Functions:** 147

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 8 | `WerpStitchedMinidumpVmPreReadCallback` | `0x5BA0` | 213 | UnwindData |  |
| 36 | `WerpAddFile` | `0x9AD0` | 215 | UnwindData |  |
| 18 | `WerReportAddFile` | `0x9C60` | 368 | UnwindData |  |
| 7 | `WerpStitchedMinidumpVmPostReadCallback` | `0x15100` | 76 | UnwindData |  |
| 44 | `WerpAddTerminationReason` | `0x1D840` | 467 | UnwindData |  |
| 46 | `WerpAuxmdDumpProcessImages` | `0x1E1E0` | 1,213 | UnwindData |  |
| 48 | `WerpAuxmdFree` | `0x235C0` | 127 | UnwindData |  |
| 50 | `WerpAuxmdHashVaRanges` | `0x25BA0` | 528 | UnwindData |  |
| 20 | `WerReportCreate` | `0x29AF0` | 1,928 | UnwindData |  |
| 47 | `WerpAuxmdDumpRegisteredBlocks` | `0x2F250` | 641 | UnwindData |  |
| 13 | `RegisterWaitChainCOMCallback` | `0x30090` | 183 | UnwindData |  |
| 145 | `WerpUnmapProcessViews` | `0x32BA0` | 639 | UnwindData |  |
| 98 | `WerpHasOobeCompleted` | `0x36DB0` | 739 | UnwindData |  |
| 9 | `WerpStitchedMinidumpVmQueryCallback` | `0x371B0` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `WerpGetWerStringData` | `0x37370` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `WerpIsTransportAvailable` | `0x374B0` | 542 | UnwindData |  |
| 147 | `WerpWalkGatherBlocks` | `0x3BD00` | 233 | UnwindData |  |
| 78 | `WerpGetPathOfWERTempDirectory` | `0x3EAF0` | 870 | UnwindData |  |
| 43 | `WerpAddRegisteredMetadataToReport` | `0x3F0C0` | 344 | UnwindData |  |
| 143 | `WerpTraceStitchedDumpWriterStatistics` | `0x435E0` | 71,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `CloseThreadWaitChainSession` | `0x54CD0` | 215 | UnwindData |  |
| 11 | `GetThreadWaitChain` | `0x54DB0` | 647 | UnwindData |  |
| 12 | `OpenThreadWaitChainSession` | `0x55040` | 398 | UnwindData |  |
| 1 | `WerSysprepCleanup` | `0x559F0` | 166 | UnwindData |  |
| 2 | `WerSysprepGeneralize` | `0x55AA0` | 280 | UnwindData |  |
| 3 | `WerUnattendedSetup` | `0x55BC0` | 313 | UnwindData |  |
| 14 | `WerAddExcludedApplication` | `0x56260` | 456 | UnwindData |  |
| 16 | `WerRemoveExcludedApplication` | `0x56430` | 404 | UnwindData |  |
| 17 | `WerReportAddDump` | `0x565D0` | 454 | UnwindData |  |
| 19 | `WerReportCloseHandle` | `0x567A0` | 778 | UnwindData |  |
| 21 | `WerReportSetParameter` | `0x56AB0` | 498 | UnwindData |  |
| 22 | `WerReportSetUIOption` | `0x56CB0` | 191 | UnwindData |  |
| 23 | `WerReportSubmit` | `0x56D80` | 413 | UnwindData |  |
| 4 | `WerpFlushImageCache` | `0x56FA0` | 175 | UnwindData |  |
| 5 | `WerpInitializeImageCache` | `0x57060` | 163 | UnwindData |  |
| 6 | `WerpResetTransientImageCacheStatistics` | `0x57720` | 14,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `WerFreeString` | `0x5AFD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `WerStoreClose` | `0x5AFE0` | 133 | UnwindData |  |
| 25 | `WerStoreGetFirstReportKey` | `0x5B070` | 318 | UnwindData |  |
| 26 | `WerStoreGetNextReportKey` | `0x5B1C0` | 466 | UnwindData |  |
| 27 | `WerStoreGetReportCount` | `0x5B3A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `WerStoreGetSizeOnDisk` | `0x5B3B0` | 141 | UnwindData |  |
| 29 | `WerStoreOpen` | `0x5B450` | 512 | UnwindData |  |
| 30 | `WerStorePurge` | `0x5B660` | 400 | UnwindData |  |
| 31 | `WerStoreQueryReportMetadataV1` | `0x5B800` | 1,012 | UnwindData |  |
| 32 | `WerStoreQueryReportMetadataV2` | `0x5BC00` | 1,220 | UnwindData |  |
| 33 | `WerStoreQueryReportMetadataV3` | `0x5C0D0` | 1,143 | UnwindData |  |
| 34 | `WerStoreUploadReport` | `0x5C550` | 728 | UnwindData |  |
| 35 | `WerpAddAppCompatData` | `0x5C830` | 895 | UnwindData |  |
| 37 | `WerpAddFileBuffer` | `0x5CCD0` | 239 | UnwindData |  |
| 38 | `WerpAddFileCallback` | `0x5CDD0` | 240 | UnwindData |  |
| 39 | `WerpAddIfRegisteredForAppLocalDump` | `0x5CED0` | 470 | UnwindData |  |
| 40 | `WerpAddMemoryBlock` | `0x5D0B0` | 184 | UnwindData |  |
| 41 | `WerpAddRegisteredDataToReport` | `0x5D170` | 800 | UnwindData |  |
| 42 | `WerpAddRegisteredDumpsToReport` | `0x5D4A0` | 434 | UnwindData |  |
| 45 | `WerpArchiveReport` | `0x5D660` | 719 | UnwindData |  |
| 53 | `WerpCancelUpload` | `0x5D940` | 145 | UnwindData |  |
| 54 | `WerpCleanWer` | `0x5D9E0` | 506 | UnwindData |  |
| 55 | `WerpCloseStore` | `0x5DBE0` | 119 | UnwindData |  |
| 56 | `WerpCreateIntegratorReportId` | `0x5DC60` | 168 | UnwindData |  |
| 57 | `WerpCreateMachineStore` | `0x5DD10` | 469 | UnwindData |  |
| 58 | `WerpDeleteReport` | `0x5DEF0` | 92 | UnwindData |  |
| 59 | `WerpDestroyWerString` | `0x5DF60` | 42 | UnwindData |  |
| 60 | `WerpEnumerateStoreNext` | `0x5DF90` | 201 | UnwindData |  |
| 61 | `WerpEnumerateStoreStart` | `0x5E060` | 85 | UnwindData |  |
| 62 | `WerpExtractReportFiles` | `0x5E0C0` | 171 | UnwindData |  |
| 63 | `WerpForceDeferredCollection` | `0x5E180` | 421 | UnwindData |  |
| 64 | `WerpFreeString` | `0x5E330` | 48 | UnwindData |  |
| 65 | `WerpFreeUnmappedVaRanges` | `0x5E370` | 48 | UnwindData |  |
| 66 | `WerpGetBucketId` | `0x5E530` | 327 | UnwindData |  |
| 67 | `WerpGetDynamicParameter` | `0x5E680` | 258 | UnwindData |  |
| 68 | `WerpGetEventType` | `0x5E790` | 111 | UnwindData |  |
| 69 | `WerpGetExtendedDiagData` | `0x5E810` | 682 | UnwindData |  |
| 70 | `WerpGetFileByIndex` | `0x5EAC0` | 267 | UnwindData |  |
| 71 | `WerpGetFilePathByIndex` | `0x5EBE0` | 204 | UnwindData |  |
| 72 | `WerpGetIntegratorReportId` | `0x5ECC0` | 119 | UnwindData |  |
| 73 | `WerpGetLegacyBucketId` | `0x5ED40` | 328 | UnwindData |  |
| 74 | `WerpGetLoadedModuleByIndex` | `0x5EE90` | 211 | UnwindData |  |
| 75 | `WerpGetNumFiles` | `0x5EF70` | 154 | UnwindData |  |
| 76 | `WerpGetNumLoadedModules` | `0x5F010` | 110 | UnwindData |  |
| 77 | `WerpGetNumSigParams` | `0x5F090` | 108 | UnwindData |  |
| 79 | `WerpGetReportConsent` | `0x5F110` | 279 | UnwindData |  |
| 80 | `WerpGetReportCount` | `0x5F230` | 147 | UnwindData |  |
| 81 | `WerpGetReportFinalConsent` | `0x5F2D0` | 105 | UnwindData |  |
| 82 | `WerpGetReportFlags` | `0x5F340` | 126 | UnwindData |  |
| 83 | `WerpGetReportId` | `0x5F3D0` | 271 | UnwindData |  |
| 84 | `WerpGetReportInformation` | `0x5F4F0` | 106 | UnwindData |  |
| 85 | `WerpGetReportSettings` | `0x5F560` | 165 | UnwindData |  |
| 86 | `WerpGetReportTime` | `0x5F610` | 98 | UnwindData |  |
| 87 | `WerpGetReportType` | `0x5F680` | 94 | UnwindData |  |
| 88 | `WerpGetResponseId` | `0x5F6F0` | 142 | UnwindData |  |
| 89 | `WerpGetSigParamByIndex` | `0x5F790` | 129 | UnwindData |  |
| 90 | `WerpGetStoreLocation` | `0x5F820` | 285 | UnwindData |  |
| 91 | `WerpGetStorePath` | `0x5F950` | 673 | UnwindData |  |
| 92 | `WerpGetStoreType` | `0x5FC00` | 200 | UnwindData |  |
| 93 | `WerpGetTextFromReport` | `0x5FCD0` | 114 | UnwindData |  |
| 94 | `WerpGetUIParamByIndex` | `0x5FD50` | 202 | UnwindData |  |
| 95 | `WerpGetUploadTime` | `0x5FE20` | 107 | UnwindData |  |
| 97 | `WerpGetWow64Process` | `0x5FEA0` | 131 | UnwindData |  |
| 99 | `WerpHashApplicationParameters` | `0x5FF30` | 313 | UnwindData |  |
| 100 | `WerpIsDisabled` | `0x60070` | 230 | UnwindData |  |
| 101 | `WerpIsOnBattery` | `0x60160` | 118 | UnwindData |  |
| 103 | `WerpLoadReport` | `0x603F0` | 39 | UnwindData |  |
| 104 | `WerpLoadReportFromBuffer` | `0x60420` | 40 | UnwindData |  |
| 105 | `WerpOpenMachineArchive` | `0x60450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `WerpOpenMachineQueue` | `0x60460` | 443 | UnwindData |  |
| 107 | `WerpPromptUser` | `0x60630` | 94 | UnwindData |  |
| 108 | `WerpPruneStore` | `0x606A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `WerpReportCancel` | `0x606C0` | 149 | UnwindData |  |
| 110 | `WerpReportSetMaxProcessHoldMilliseconds` | `0x60760` | 86 | UnwindData |  |
| 111 | `WerpReportSprintfParameter` | `0x607C0` | 34 | UnwindData |  |
| 112 | `WerpReserveMachineQueueReportDir` | `0x607F0` | 505 | UnwindData |  |
| 113 | `WerpRestartApplication` | `0x609F0` | 2,237 | UnwindData |  |
| 114 | `WerpSetAuxiliaryArchivePath` | `0x612C0` | 117 | UnwindData |  |
| 115 | `WerpSetCallBack` | `0x61340` | 101 | UnwindData |  |
| 116 | `WerpSetDefaultUserConsent` | `0x613B0` | 511 | UnwindData |  |
| 117 | `WerpSetDynamicParameter` | `0x615C0` | 241 | UnwindData |  |
| 118 | `WerpSetEventName` | `0x616C0` | 93 | UnwindData |  |
| 119 | `WerpSetExitListeners` | `0x61730` | 114 | UnwindData |  |
| 120 | `WerpSetIntegratorReportId` | `0x617B0` | 160 | UnwindData |  |
| 121 | `WerpSetIptEnabled` | `0x61860` | 113 | UnwindData |  |
| 122 | `WerpSetProcessTimelines` | `0x618E0` | 105 | UnwindData |  |
| 123 | `WerpSetQuickDumpType` | `0x61950` | 97 | UnwindData |  |
| 124 | `WerpSetReportApplicationIdentity` | `0x619C0` | 104 | UnwindData |  |
| 125 | `WerpSetReportFlags` | `0x61A30` | 86 | UnwindData |  |
| 126 | `WerpSetReportInformation` | `0x61A90` | 133 | UnwindData |  |
| 127 | `WerpSetReportIsFatal` | `0x61B20` | 97 | UnwindData |  |
| 128 | `WerpSetReportNamespaceParameter` | `0x61B90` | 215 | UnwindData |  |
| 129 | `WerpSetReportOption` | `0x61C70` | 152 | UnwindData |  |
| 130 | `WerpSetReportTime` | `0x61D10` | 98 | UnwindData |  |
| 131 | `WerpSetReportUploadContextToken` | `0x61D80` | 160 | UnwindData |  |
| 132 | `WerpSetTelemetryAppParams` | `0x61E30` | 124 | UnwindData |  |
| 133 | `WerpSetTelemetryKernelParams` | `0x61EC0` | 86 | UnwindData |  |
| 134 | `WerpSetTelemetryServiceParams` | `0x61F20` | 155 | UnwindData |  |
| 135 | `WerpSetTtdStatus` | `0x61FD0` | 86 | UnwindData |  |
| 136 | `WerpSetVelocityInformation` | `0x62030` | 98 | UnwindData |  |
| 137 | `WerpShowUpsellUI` | `0x620A0` | 62 | UnwindData |  |
| 138 | `WerpSubmitReportFromStore` | `0x620F0` | 1,553 | UnwindData |  |
| 139 | `WerpTraceAuxMemDumpStatistics` | `0x62710` | 323 | UnwindData |  |
| 140 | `WerpTraceDuration` | `0x62860` | 496 | UnwindData |  |
| 141 | `WerpTraceImageCacheStatistics` | `0x62A60` | 644 | UnwindData |  |
| 142 | `WerpTraceSnapshotStatistics` | `0x62CF0` | 999 | UnwindData |  |
| 144 | `WerpTraceUnmappedVaRangesStatistics` | `0x630E0` | 189 | UnwindData |  |
| 146 | `WerpValidateReportKey` | `0x631B0` | 3,008 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `WerpAuxmdFreeCopyBuffer` | `0x63D70` | 50 | UnwindData |  |
| 51 | `WerpAuxmdInitialize` | `0x63DB0` | 350 | UnwindData |  |
| 52 | `WerpAuxmdMapFile` | `0x63F20` | 324,540 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
