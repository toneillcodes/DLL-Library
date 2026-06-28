# Binary Specification: wer.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wer.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `23d6242223a5c7399baaf3131e630f9acf35e85fe5e5bf180f11849e81e2b34f`
* **Total Exported Functions:** 146

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 8 | `WerpStitchedMinidumpVmPreReadCallback` | `0x5B80` | 213 | UnwindData |  |
| 36 | `WerpAddFile` | `0x9AB0` | 215 | UnwindData |  |
| 18 | `WerReportAddFile` | `0x9C40` | 368 | UnwindData |  |
| 7 | `WerpStitchedMinidumpVmPostReadCallback` | `0x150C0` | 76 | UnwindData |  |
| 44 | `WerpAddTerminationReason` | `0x1DDF0` | 467 | UnwindData |  |
| 46 | `WerpAuxmdDumpProcessImages` | `0x1E790` | 1,213 | UnwindData |  |
| 48 | `WerpAuxmdFree` | `0x23B70` | 127 | UnwindData |  |
| 50 | `WerpAuxmdHashVaRanges` | `0x26150` | 528 | UnwindData |  |
| 20 | `WerReportCreate` | `0x2A0A0` | 1,928 | UnwindData |  |
| 47 | `WerpAuxmdDumpRegisteredBlocks` | `0x2F7D0` | 641 | UnwindData |  |
| 13 | `RegisterWaitChainCOMCallback` | `0x30610` | 183 | UnwindData |  |
| 144 | `WerpUnmapProcessViews` | `0x32C80` | 639 | UnwindData |  |
| 98 | `WerpHasOobeCompleted` | `0x36E00` | 739 | UnwindData |  |
| 9 | `WerpStitchedMinidumpVmQueryCallback` | `0x37210` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `WerpGetWerStringData` | `0x373D0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `WerpIsTransportAvailable` | `0x37510` | 558 | UnwindData |  |
| 146 | `WerpWalkGatherBlocks` | `0x3BD10` | 233 | UnwindData |  |
| 78 | `WerpGetPathOfWERTempDirectory` | `0x3EAE0` | 870 | UnwindData |  |
| 43 | `WerpAddRegisteredMetadataToReport` | `0x3F0B0` | 344 | UnwindData |  |
| 142 | `WerpTraceStitchedDumpWriterStatistics` | `0x43D20` | 70,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `CloseThreadWaitChainSession` | `0x55170` | 215 | UnwindData |  |
| 11 | `GetThreadWaitChain` | `0x55250` | 647 | UnwindData |  |
| 12 | `OpenThreadWaitChainSession` | `0x554E0` | 398 | UnwindData |  |
| 1 | `WerSysprepCleanup` | `0x55E90` | 166 | UnwindData |  |
| 2 | `WerSysprepGeneralize` | `0x55F40` | 280 | UnwindData |  |
| 3 | `WerUnattendedSetup` | `0x56060` | 313 | UnwindData |  |
| 14 | `WerAddExcludedApplication` | `0x56710` | 456 | UnwindData |  |
| 16 | `WerRemoveExcludedApplication` | `0x568E0` | 404 | UnwindData |  |
| 17 | `WerReportAddDump` | `0x56A80` | 454 | UnwindData |  |
| 19 | `WerReportCloseHandle` | `0x56C50` | 778 | UnwindData |  |
| 21 | `WerReportSetParameter` | `0x56F60` | 491 | UnwindData |  |
| 22 | `WerReportSetUIOption` | `0x57160` | 184 | UnwindData |  |
| 23 | `WerReportSubmit` | `0x57220` | 413 | UnwindData |  |
| 4 | `WerpFlushImageCache` | `0x57440` | 175 | UnwindData |  |
| 5 | `WerpInitializeImageCache` | `0x57500` | 163 | UnwindData |  |
| 6 | `WerpResetTransientImageCacheStatistics` | `0x57BC0` | 12,128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `WerFreeString` | `0x5AB20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `WerStoreClose` | `0x5AB30` | 133 | UnwindData |  |
| 25 | `WerStoreGetFirstReportKey` | `0x5ABC0` | 318 | UnwindData |  |
| 26 | `WerStoreGetNextReportKey` | `0x5AD10` | 466 | UnwindData |  |
| 27 | `WerStoreGetReportCount` | `0x5AEF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `WerStoreGetSizeOnDisk` | `0x5AF00` | 141 | UnwindData |  |
| 29 | `WerStoreOpen` | `0x5AFA0` | 512 | UnwindData |  |
| 30 | `WerStorePurge` | `0x5B1B0` | 400 | UnwindData |  |
| 31 | `WerStoreQueryReportMetadataV1` | `0x5B350` | 1,012 | UnwindData |  |
| 32 | `WerStoreQueryReportMetadataV2` | `0x5B750` | 1,220 | UnwindData |  |
| 33 | `WerStoreQueryReportMetadataV3` | `0x5BC20` | 1,143 | UnwindData |  |
| 34 | `WerStoreUploadReport` | `0x5C0A0` | 728 | UnwindData |  |
| 35 | `WerpAddAppCompatData` | `0x5C380` | 895 | UnwindData |  |
| 37 | `WerpAddFileBuffer` | `0x5C820` | 239 | UnwindData |  |
| 38 | `WerpAddFileCallback` | `0x5C920` | 240 | UnwindData |  |
| 39 | `WerpAddIfRegisteredForAppLocalDump` | `0x5CA20` | 470 | UnwindData |  |
| 40 | `WerpAddMemoryBlock` | `0x5CC00` | 184 | UnwindData |  |
| 41 | `WerpAddRegisteredDataToReport` | `0x5CCC0` | 800 | UnwindData |  |
| 42 | `WerpAddRegisteredDumpsToReport` | `0x5CFF0` | 434 | UnwindData |  |
| 45 | `WerpArchiveReport` | `0x5D1B0` | 719 | UnwindData |  |
| 53 | `WerpCancelUpload` | `0x5D490` | 145 | UnwindData |  |
| 54 | `WerpCleanWer` | `0x5D530` | 506 | UnwindData |  |
| 55 | `WerpCloseStore` | `0x5D730` | 119 | UnwindData |  |
| 56 | `WerpCreateIntegratorReportId` | `0x5D7B0` | 168 | UnwindData |  |
| 57 | `WerpCreateMachineStore` | `0x5D860` | 469 | UnwindData |  |
| 58 | `WerpDeleteReport` | `0x5DA40` | 92 | UnwindData |  |
| 59 | `WerpDestroyWerString` | `0x5DAB0` | 42 | UnwindData |  |
| 60 | `WerpEnumerateStoreNext` | `0x5DAE0` | 201 | UnwindData |  |
| 61 | `WerpEnumerateStoreStart` | `0x5DBB0` | 85 | UnwindData |  |
| 62 | `WerpExtractReportFiles` | `0x5DC10` | 171 | UnwindData |  |
| 63 | `WerpForceDeferredCollection` | `0x5DCD0` | 421 | UnwindData |  |
| 64 | `WerpFreeString` | `0x5DE80` | 48 | UnwindData |  |
| 65 | `WerpFreeUnmappedVaRanges` | `0x5DEC0` | 48 | UnwindData |  |
| 66 | `WerpGetBucketId` | `0x5E080` | 327 | UnwindData |  |
| 67 | `WerpGetDynamicParameter` | `0x5E1D0` | 258 | UnwindData |  |
| 68 | `WerpGetEventType` | `0x5E2E0` | 111 | UnwindData |  |
| 69 | `WerpGetExtendedDiagData` | `0x5E360` | 682 | UnwindData |  |
| 70 | `WerpGetFileByIndex` | `0x5E610` | 267 | UnwindData |  |
| 71 | `WerpGetFilePathByIndex` | `0x5E730` | 204 | UnwindData |  |
| 72 | `WerpGetIntegratorReportId` | `0x5E810` | 119 | UnwindData |  |
| 73 | `WerpGetLegacyBucketId` | `0x5E890` | 328 | UnwindData |  |
| 74 | `WerpGetLoadedModuleByIndex` | `0x5E9E0` | 211 | UnwindData |  |
| 75 | `WerpGetNumFiles` | `0x5EAC0` | 154 | UnwindData |  |
| 76 | `WerpGetNumLoadedModules` | `0x5EB60` | 110 | UnwindData |  |
| 77 | `WerpGetNumSigParams` | `0x5EBE0` | 108 | UnwindData |  |
| 79 | `WerpGetReportConsent` | `0x5EC60` | 279 | UnwindData |  |
| 80 | `WerpGetReportCount` | `0x5ED80` | 147 | UnwindData |  |
| 81 | `WerpGetReportFinalConsent` | `0x5EE20` | 105 | UnwindData |  |
| 82 | `WerpGetReportFlags` | `0x5EE90` | 126 | UnwindData |  |
| 83 | `WerpGetReportId` | `0x5EF20` | 271 | UnwindData |  |
| 84 | `WerpGetReportInformation` | `0x5F040` | 106 | UnwindData |  |
| 85 | `WerpGetReportSettings` | `0x5F0B0` | 165 | UnwindData |  |
| 86 | `WerpGetReportTime` | `0x5F160` | 98 | UnwindData |  |
| 87 | `WerpGetReportType` | `0x5F1D0` | 94 | UnwindData |  |
| 88 | `WerpGetResponseId` | `0x5F240` | 142 | UnwindData |  |
| 89 | `WerpGetSigParamByIndex` | `0x5F2E0` | 129 | UnwindData |  |
| 90 | `WerpGetStoreLocation` | `0x5F370` | 285 | UnwindData |  |
| 91 | `WerpGetStorePath` | `0x5F4A0` | 673 | UnwindData |  |
| 92 | `WerpGetStoreType` | `0x5F750` | 200 | UnwindData |  |
| 93 | `WerpGetTextFromReport` | `0x5F820` | 114 | UnwindData |  |
| 94 | `WerpGetUIParamByIndex` | `0x5F8A0` | 202 | UnwindData |  |
| 95 | `WerpGetUploadTime` | `0x5F970` | 107 | UnwindData |  |
| 97 | `WerpGetWow64Process` | `0x5F9F0` | 131 | UnwindData |  |
| 99 | `WerpHashApplicationParameters` | `0x5FA80` | 313 | UnwindData |  |
| 100 | `WerpIsDisabled` | `0x5FBC0` | 230 | UnwindData |  |
| 101 | `WerpIsOnBattery` | `0x5FCB0` | 118 | UnwindData |  |
| 103 | `WerpLoadReport` | `0x5FF40` | 39 | UnwindData |  |
| 104 | `WerpLoadReportFromBuffer` | `0x5FF70` | 40 | UnwindData |  |
| 105 | `WerpOpenMachineArchive` | `0x5FFA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `WerpOpenMachineQueue` | `0x5FFB0` | 443 | UnwindData |  |
| 107 | `WerpPromptUser` | `0x60180` | 94 | UnwindData |  |
| 108 | `WerpPruneStore` | `0x601F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `WerpReportCancel` | `0x60210` | 149 | UnwindData |  |
| 110 | `WerpReportSetMaxProcessHoldMilliseconds` | `0x602B0` | 86 | UnwindData |  |
| 111 | `WerpReportSprintfParameter` | `0x60310` | 34 | UnwindData |  |
| 112 | `WerpReserveMachineQueueReportDir` | `0x60340` | 505 | UnwindData |  |
| 113 | `WerpRestartApplication` | `0x60540` | 2,237 | UnwindData |  |
| 114 | `WerpSetAuxiliaryArchivePath` | `0x60E10` | 117 | UnwindData |  |
| 115 | `WerpSetCallBack` | `0x60E90` | 101 | UnwindData |  |
| 116 | `WerpSetDefaultUserConsent` | `0x60F00` | 511 | UnwindData |  |
| 117 | `WerpSetDynamicParameter` | `0x61110` | 241 | UnwindData |  |
| 118 | `WerpSetEventName` | `0x61210` | 93 | UnwindData |  |
| 119 | `WerpSetExitListeners` | `0x61280` | 114 | UnwindData |  |
| 120 | `WerpSetIntegratorReportId` | `0x61300` | 160 | UnwindData |  |
| 121 | `WerpSetIptEnabled` | `0x613B0` | 113 | UnwindData |  |
| 122 | `WerpSetProcessTimelines` | `0x61430` | 105 | UnwindData |  |
| 123 | `WerpSetQuickDumpType` | `0x614A0` | 97 | UnwindData |  |
| 124 | `WerpSetReportApplicationIdentity` | `0x61510` | 104 | UnwindData |  |
| 125 | `WerpSetReportFlags` | `0x61580` | 86 | UnwindData |  |
| 126 | `WerpSetReportInformation` | `0x615E0` | 133 | UnwindData |  |
| 127 | `WerpSetReportIsFatal` | `0x61670` | 97 | UnwindData |  |
| 128 | `WerpSetReportNamespaceParameter` | `0x616E0` | 215 | UnwindData |  |
| 129 | `WerpSetReportOption` | `0x617C0` | 152 | UnwindData |  |
| 130 | `WerpSetReportTime` | `0x61860` | 98 | UnwindData |  |
| 131 | `WerpSetReportUploadContextToken` | `0x618D0` | 160 | UnwindData |  |
| 132 | `WerpSetTelemetryAppParams` | `0x61980` | 124 | UnwindData |  |
| 133 | `WerpSetTelemetryKernelParams` | `0x61A10` | 86 | UnwindData |  |
| 134 | `WerpSetTelemetryServiceParams` | `0x61A70` | 155 | UnwindData |  |
| 135 | `WerpSetTtdStatus` | `0x61B20` | 86 | UnwindData |  |
| 136 | `WerpShowUpsellUI` | `0x61B80` | 62 | UnwindData |  |
| 137 | `WerpSubmitReportFromStore` | `0x61BD0` | 1,553 | UnwindData |  |
| 138 | `WerpTraceAuxMemDumpStatistics` | `0x621F0` | 323 | UnwindData |  |
| 139 | `WerpTraceDuration` | `0x62340` | 496 | UnwindData |  |
| 140 | `WerpTraceImageCacheStatistics` | `0x62540` | 644 | UnwindData |  |
| 141 | `WerpTraceSnapshotStatistics` | `0x627D0` | 999 | UnwindData |  |
| 143 | `WerpTraceUnmappedVaRangesStatistics` | `0x62BC0` | 189 | UnwindData |  |
| 145 | `WerpValidateReportKey` | `0x62C90` | 3,008 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `WerpAuxmdFreeCopyBuffer` | `0x63850` | 50 | UnwindData |  |
| 51 | `WerpAuxmdInitialize` | `0x63890` | 350 | UnwindData |  |
| 52 | `WerpAuxmdMapFile` | `0x63A00` | 321,132 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
