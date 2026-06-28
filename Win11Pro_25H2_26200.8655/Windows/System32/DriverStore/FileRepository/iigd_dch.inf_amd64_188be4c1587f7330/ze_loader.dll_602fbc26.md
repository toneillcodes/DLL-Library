# Binary Specification: ze_loader.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_188be4c1587f7330\ze_loader.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `602fbc264dc64b22bf007dee691c02851b4305c9679b77f182d9e6c9b71ccb81`
* **Total Exported Functions:** 474

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `zeCommandListAppendBarrier` | `0x35B0` | 44 | UnwindData |  |
| 2 | `zeCommandListAppendEventReset` | `0x35E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `zeCommandListAppendImageCopy` | `0x3600` | 68 | UnwindData |  |
| 4 | `zeCommandListAppendImageCopyFromMemory` | `0x3650` | 81 | UnwindData |  |
| 5 | `zeCommandListAppendImageCopyFromMemoryExt` | `0x36B0` | 109 | UnwindData |  |
| 6 | `zeCommandListAppendImageCopyRegion` | `0x3720` | 100 | UnwindData |  |
| 7 | `zeCommandListAppendImageCopyToMemory` | `0x3790` | 81 | UnwindData |  |
| 8 | `zeCommandListAppendImageCopyToMemoryExt` | `0x37F0` | 109 | UnwindData |  |
| 9 | `zeCommandListAppendLaunchCooperativeKernel` | `0x3860` | 68 | UnwindData |  |
| 10 | `zeCommandListAppendLaunchKernel` | `0x38B0` | 68 | UnwindData |  |
| 11 | `zeCommandListAppendLaunchKernelIndirect` | `0x3900` | 68 | UnwindData |  |
| 12 | `zeCommandListAppendLaunchMultipleKernelsIndirect` | `0x3950` | 100 | UnwindData |  |
| 13 | `zeCommandListAppendMemAdvise` | `0x39C0` | 58 | UnwindData |  |
| 14 | `zeCommandListAppendMemoryCopy` | `0x3A00` | 81 | UnwindData |  |
| 15 | `zeCommandListAppendMemoryCopyFromContext` | `0x3A60` | 100 | UnwindData |  |
| 16 | `zeCommandListAppendMemoryCopyRegion` | `0x3AD0` | 149 | UnwindData |  |
| 17 | `zeCommandListAppendMemoryFill` | `0x3B70` | 100 | UnwindData |  |
| 18 | `zeCommandListAppendMemoryPrefetch` | `0x3BE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `zeCommandListAppendMemoryRangesBarrier` | `0x3C00` | 81 | UnwindData |  |
| 20 | `zeCommandListAppendQueryKernelTimestamps` | `0x3C60` | 100 | UnwindData |  |
| 21 | `zeCommandListAppendSignalEvent` | `0x3CD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `zeCommandListAppendWaitOnEvents` | `0x3CF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `zeCommandListAppendWriteGlobalTimestamp` | `0x3D10` | 60 | UnwindData |  |
| 24 | `zeCommandListClose` | `0x3D50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `zeCommandListCreate` | `0x3D70` | 44 | UnwindData |  |
| 26 | `zeCommandListCreateImmediate` | `0x3DA0` | 44 | UnwindData |  |
| 27 | `zeCommandListDestroy` | `0x3DD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `zeCommandListReset` | `0x3DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `zeCommandQueueCreate` | `0x3E10` | 44 | UnwindData |  |
| 30 | `zeCommandQueueDestroy` | `0x3E40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `zeCommandQueueExecuteCommandLists` | `0x3E60` | 44 | UnwindData |  |
| 32 | `zeCommandQueueSynchronize` | `0x3E90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `zeContextCreate` | `0x3EB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `zeContextCreateEx` | `0x3ED0` | 60 | UnwindData |  |
| 35 | `zeContextDestroy` | `0x3F10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `zeContextEvictImage` | `0x3F30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `zeContextEvictMemory` | `0x3F50` | 44 | UnwindData |  |
| 38 | `zeContextGetStatus` | `0x3F80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `zeContextMakeImageResident` | `0x3FA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `zeContextMakeMemoryResident` | `0x3FC0` | 44 | UnwindData |  |
| 41 | `zeContextSystemBarrier` | `0x3FF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `zeDeviceCanAccessPeer` | `0x4010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `zeDeviceGet` | `0x4030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `zeDeviceGetCacheProperties` | `0x4050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `zeDeviceGetCommandQueueGroupProperties` | `0x4070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `zeDeviceGetComputeProperties` | `0x4090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `zeDeviceGetExternalMemoryProperties` | `0x40B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `zeDeviceGetGlobalTimestamps` | `0x40D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `zeDeviceGetImageProperties` | `0x40F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `zeDeviceGetMemoryAccessProperties` | `0x4110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `zeDeviceGetMemoryProperties` | `0x4130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `zeDeviceGetModuleProperties` | `0x4150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `zeDeviceGetP2PProperties` | `0x4170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `zeDeviceGetProperties` | `0x4190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `zeDeviceGetStatus` | `0x41B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `zeDeviceGetSubDevices` | `0x41D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `zeDevicePciGetPropertiesExt` | `0x41F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `zeDeviceReserveCacheExt` | `0x4210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `zeDeviceSetCacheAdviceExt` | `0x4230` | 44 | UnwindData |  |
| 60 | `zeDriverGet` | `0x4260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `zeDriverGetApiVersion` | `0x4280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `zeDriverGetExtensionFunctionAddress` | `0x42A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `zeDriverGetExtensionProperties` | `0x42C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `zeDriverGetIpcProperties` | `0x42E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `zeDriverGetProperties` | `0x4300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `zeEventCreate` | `0x4320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `zeEventDestroy` | `0x4340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `zeEventHostReset` | `0x4360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `zeEventHostSignal` | `0x4380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `zeEventHostSynchronize` | `0x43A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `zeEventPoolCloseIpcHandle` | `0x43C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `zeEventPoolCreate` | `0x43E0` | 60 | UnwindData |  |
| 73 | `zeEventPoolDestroy` | `0x4420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `zeEventPoolGetIpcHandle` | `0x4440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `zeEventPoolOpenIpcHandle` | `0x4460` | 84 | UnwindData |  |
| 76 | `zeEventQueryKernelTimestamp` | `0x44C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `zeEventQueryStatus` | `0x44E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `zeEventQueryTimestampsExp` | `0x4500` | 44 | UnwindData |  |
| 79 | `zeFenceCreate` | `0x4530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `zeFenceDestroy` | `0x4550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `zeFenceHostSynchronize` | `0x4570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `zeFenceQueryStatus` | `0x4590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `zeFenceReset` | `0x45B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `zeImageCreate` | `0x45D0` | 44 | UnwindData |  |
| 105 | `zeImageDestroy` | `0x4600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `zeImageGetAllocPropertiesExt` | `0x4620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `zeImageGetMemoryPropertiesExp` | `0x4640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `zeImageGetProperties` | `0x4660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `zeImageViewCreateExp` | `0x4680` | 60 | UnwindData |  |
| 110 | `zeInit` | `0x46C0` | 154 | UnwindData |  |
| 111 | `zeKernelCreate` | `0x4760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `zeKernelDestroy` | `0x4780` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `zeKernelGetIndirectAccess` | `0x47A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `zeKernelGetName` | `0x47C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `zeKernelGetProperties` | `0x47E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `zeKernelGetSourceAttributes` | `0x4800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `zeKernelSchedulingHintExp` | `0x4820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `zeKernelSetArgumentValue` | `0x4840` | 44 | UnwindData |  |
| 119 | `zeKernelSetCacheConfig` | `0x4870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `zeKernelSetGlobalOffsetExp` | `0x4890` | 44 | UnwindData |  |
| 121 | `zeKernelSetGroupSize` | `0x48C0` | 44 | UnwindData |  |
| 122 | `zeKernelSetIndirectAccess` | `0x48F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `zeKernelSuggestGroupSize` | `0x4910` | 83 | UnwindData |  |
| 124 | `zeKernelSuggestMaxCooperativeGroupCount` | `0x4970` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `zeMemAllocDevice` | `0x4990` | 70 | UnwindData |  |
| 128 | `zeMemAllocHost` | `0x49E0` | 60 | UnwindData |  |
| 129 | `zeMemAllocShared` | `0x4A20` | 83 | UnwindData |  |
| 130 | `zeMemCloseIpcHandle` | `0x4A80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `zeMemFree` | `0x4AA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `zeMemFreeExt` | `0x4AC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `zeMemGetAddressRange` | `0x4AE0` | 44 | UnwindData |  |
| 134 | `zeMemGetAllocProperties` | `0x4B10` | 44 | UnwindData |  |
| 135 | `zeMemGetIpcHandle` | `0x4B40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `zeMemOpenIpcHandle` | `0x4B60` | 107 | UnwindData |  |
| 137 | `zeModuleBuildLogDestroy` | `0x4BD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `zeModuleBuildLogGetString` | `0x4BF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `zeModuleCreate` | `0x4C10` | 60 | UnwindData |  |
| 140 | `zeModuleDestroy` | `0x4C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `zeModuleDynamicLink` | `0x4C70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `zeModuleGetFunctionPointer` | `0x4C90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `zeModuleGetGlobalPointer` | `0x4CB0` | 44 | UnwindData |  |
| 144 | `zeModuleGetKernelNames` | `0x4CE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `zeModuleGetNativeBinary` | `0x4D00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `zeModuleGetProperties` | `0x4D20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `zeModuleInspectLinkageExt` | `0x4D40` | 44 | UnwindData |  |
| 148 | `zePhysicalMemCreate` | `0x4D70` | 44 | UnwindData |  |
| 149 | `zePhysicalMemDestroy` | `0x4DA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `zeSamplerCreate` | `0x4DC0` | 44 | UnwindData |  |
| 151 | `zeSamplerDestroy` | `0x4DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `zeVirtualMemFree` | `0x4E10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `zeVirtualMemGetAccessAttribute` | `0x4E30` | 60 | UnwindData |  |
| 154 | `zeVirtualMemMap` | `0x4E70` | 68 | UnwindData |  |
| 155 | `zeVirtualMemQueryPageSize` | `0x4EC0` | 44 | UnwindData |  |
| 156 | `zeVirtualMemReserve` | `0x4EF0` | 44 | UnwindData |  |
| 157 | `zeVirtualMemSetAccessAttribute` | `0x4F20` | 44 | UnwindData |  |
| 158 | `zeVirtualMemUnmap` | `0x4F50` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 423 | `zetCommandListAppendMetricMemoryBarrier` | `0x5150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 424 | `zetCommandListAppendMetricQueryBegin` | `0x5170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 425 | `zetCommandListAppendMetricQueryEnd` | `0x5190` | 60 | UnwindData |  |
| 426 | `zetCommandListAppendMetricStreamerMarker` | `0x51D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 427 | `zetContextActivateMetricGroups` | `0x51F0` | 44 | UnwindData |  |
| 428 | `zetDebugAcknowledgeEvent` | `0x5220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 429 | `zetDebugAttach` | `0x5240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 430 | `zetDebugDetach` | `0x5260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 431 | `zetDebugGetRegisterSetProperties` | `0x5280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 432 | `zetDebugInterrupt` | `0x52A0` | 57 | UnwindData |  |
| 433 | `zetDebugReadEvent` | `0x52E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 434 | `zetDebugReadMemory` | `0x5300` | 73 | UnwindData |  |
| 435 | `zetDebugReadRegisters` | `0x5350` | 87 | UnwindData |  |
| 436 | `zetDebugResume` | `0x53B0` | 57 | UnwindData |  |
| 437 | `zetDebugWriteMemory` | `0x53F0` | 73 | UnwindData |  |
| 438 | `zetDebugWriteRegisters` | `0x5440` | 87 | UnwindData |  |
| 439 | `zetDeviceGetDebugProperties` | `0x54A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 453 | `zetKernelGetProfileInfo` | `0x54C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 454 | `zetMetricGet` | `0x54E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 455 | `zetMetricGetProperties` | `0x5500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 456 | `zetMetricGroupCalculateMetricValues` | `0x5520` | 70 | UnwindData |  |
| 457 | `zetMetricGroupCalculateMultipleMetricValuesExp` | `0x5570` | 102 | UnwindData |  |
| 458 | `zetMetricGroupGet` | `0x55E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 459 | `zetMetricGroupGetProperties` | `0x5600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 460 | `zetMetricQueryCreate` | `0x5620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 461 | `zetMetricQueryDestroy` | `0x5640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 462 | `zetMetricQueryGetData` | `0x5660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 463 | `zetMetricQueryPoolCreate` | `0x5680` | 60 | UnwindData |  |
| 464 | `zetMetricQueryPoolDestroy` | `0x56C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 465 | `zetMetricQueryReset` | `0x56E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 466 | `zetMetricStreamerClose` | `0x5700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 467 | `zetMetricStreamerOpen` | `0x5720` | 70 | UnwindData |  |
| 468 | `zetMetricStreamerReadData` | `0x5770` | 44 | UnwindData |  |
| 469 | `zetModuleGetDebugInfo` | `0x57A0` | 44 | UnwindData |  |
| 470 | `zetTracerExpCreate` | `0x57D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 471 | `zetTracerExpDestroy` | `0x57F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 472 | `zetTracerExpSetEnabled` | `0x5810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 473 | `zetTracerExpSetEpilogues` | `0x5830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 474 | `zetTracerExpSetPrologues` | `0x5850` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 306 | `zesDeviceEnumDiagnosticTestSuites` | `0x59B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 307 | `zesDeviceEnumEngineGroups` | `0x59D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 308 | `zesDeviceEnumFabricPorts` | `0x59F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 309 | `zesDeviceEnumFans` | `0x5A10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 310 | `zesDeviceEnumFirmwares` | `0x5A30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 311 | `zesDeviceEnumFrequencyDomains` | `0x5A50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 312 | `zesDeviceEnumLeds` | `0x5A70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 313 | `zesDeviceEnumMemoryModules` | `0x5A90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 314 | `zesDeviceEnumPerformanceFactorDomains` | `0x5AB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 315 | `zesDeviceEnumPowerDomains` | `0x5AD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 316 | `zesDeviceEnumPsus` | `0x5AF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 317 | `zesDeviceEnumRasErrorSets` | `0x5B10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 318 | `zesDeviceEnumSchedulers` | `0x5B30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 319 | `zesDeviceEnumStandbyDomains` | `0x5B50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 320 | `zesDeviceEnumTemperatureSensors` | `0x5B70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 321 | `zesDeviceEventRegister` | `0x5B90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 322 | `zesDeviceGetCardPowerDomain` | `0x5BB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 323 | `zesDeviceGetProperties` | `0x5BD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 324 | `zesDeviceGetState` | `0x5BF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 325 | `zesDevicePciGetBars` | `0x5C10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 326 | `zesDevicePciGetProperties` | `0x5C30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 327 | `zesDevicePciGetState` | `0x5C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 328 | `zesDevicePciGetStats` | `0x5C70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 329 | `zesDeviceProcessesGetState` | `0x5C90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 330 | `zesDeviceReset` | `0x5CB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 331 | `zesDiagnosticsGetProperties` | `0x5CD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 332 | `zesDiagnosticsGetTests` | `0x5CF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 333 | `zesDiagnosticsRunTests` | `0x5D10` | 44 | UnwindData |  |
| 334 | `zesDriverEventListen` | `0x5D40` | 70 | UnwindData |  |
| 335 | `zesDriverEventListenEx` | `0x5D90` | 70 | UnwindData |  |
| 336 | `zesEngineGetActivity` | `0x5DE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 337 | `zesEngineGetProperties` | `0x5E00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 338 | `zesFabricPortGetConfig` | `0x5E20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 339 | `zesFabricPortGetLinkType` | `0x5E40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 340 | `zesFabricPortGetProperties` | `0x5E60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 341 | `zesFabricPortGetState` | `0x5E80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 342 | `zesFabricPortGetThroughput` | `0x5EA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 343 | `zesFabricPortSetConfig` | `0x5EC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 344 | `zesFanGetConfig` | `0x5EE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 345 | `zesFanGetProperties` | `0x5F00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 346 | `zesFanGetState` | `0x5F20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 347 | `zesFanSetDefaultMode` | `0x5F40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 348 | `zesFanSetFixedSpeedMode` | `0x5F60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 349 | `zesFanSetSpeedTableMode` | `0x5F80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 350 | `zesFirmwareFlash` | `0x5FA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 351 | `zesFirmwareGetProperties` | `0x5FC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 352 | `zesFrequencyGetAvailableClocks` | `0x5FE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 353 | `zesFrequencyGetProperties` | `0x6000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 354 | `zesFrequencyGetRange` | `0x6020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 355 | `zesFrequencyGetState` | `0x6040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 356 | `zesFrequencyGetThrottleTime` | `0x6060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 357 | `zesFrequencyOcGetCapabilities` | `0x6080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 358 | `zesFrequencyOcGetFrequencyTarget` | `0x60A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 359 | `zesFrequencyOcGetIccMax` | `0x60C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 360 | `zesFrequencyOcGetMode` | `0x60E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 361 | `zesFrequencyOcGetTjMax` | `0x6100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 362 | `zesFrequencyOcGetVoltageTarget` | `0x6120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 363 | `zesFrequencyOcSetFrequencyTarget` | `0x6140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 364 | `zesFrequencyOcSetIccMax` | `0x6160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 365 | `zesFrequencyOcSetMode` | `0x6180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 366 | `zesFrequencyOcSetTjMax` | `0x61A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 367 | `zesFrequencyOcSetVoltageTarget` | `0x61C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 368 | `zesFrequencySetRange` | `0x61E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 386 | `zesLedGetProperties` | `0x6200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 387 | `zesLedGetState` | `0x6220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 388 | `zesLedSetColor` | `0x6240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 389 | `zesLedSetState` | `0x6260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 390 | `zesMemoryGetBandwidth` | `0x6280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 391 | `zesMemoryGetProperties` | `0x62A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 392 | `zesMemoryGetState` | `0x62C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 393 | `zesPerformanceFactorGetConfig` | `0x62E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 394 | `zesPerformanceFactorGetProperties` | `0x6300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 395 | `zesPerformanceFactorSetConfig` | `0x6320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 396 | `zesPowerGetEnergyCounter` | `0x6340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 397 | `zesPowerGetEnergyThreshold` | `0x6360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 398 | `zesPowerGetLimits` | `0x6380` | 44 | UnwindData |  |
| 399 | `zesPowerGetProperties` | `0x63B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 400 | `zesPowerSetEnergyThreshold` | `0x63D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 401 | `zesPowerSetLimits` | `0x63F0` | 44 | UnwindData |  |
| 402 | `zesPsuGetProperties` | `0x6420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 403 | `zesPsuGetState` | `0x6440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 404 | `zesRasGetConfig` | `0x6460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 405 | `zesRasGetProperties` | `0x6480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 406 | `zesRasGetState` | `0x64A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 407 | `zesRasSetConfig` | `0x64C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 408 | `zesSchedulerGetCurrentMode` | `0x64E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 409 | `zesSchedulerGetProperties` | `0x6500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 410 | `zesSchedulerGetTimeoutModeProperties` | `0x6520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 411 | `zesSchedulerGetTimesliceModeProperties` | `0x6540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 412 | `zesSchedulerSetComputeUnitDebugMode` | `0x6560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 413 | `zesSchedulerSetExclusiveMode` | `0x6580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 414 | `zesSchedulerSetTimeoutMode` | `0x65A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 415 | `zesSchedulerSetTimesliceMode` | `0x65C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 416 | `zesStandbyGetMode` | `0x65E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 417 | `zesStandbyGetProperties` | `0x6600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 418 | `zesStandbySetMode` | `0x6620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 419 | `zesTemperatureGetConfig` | `0x6640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 420 | `zesTemperatureGetProperties` | `0x6660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 421 | `zesTemperatureGetState` | `0x6680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 422 | `zesTemperatureSetConfig` | `0x66A0` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | `zelTracerCreate` | `0x6860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 207 | `zelTracerDestroy` | `0x6880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 296 | `zelTracerSetEnabled` | `0x68A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 297 | `zelTracerSetEpilogues` | `0x68C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 298 | `zelTracerSetPrologues` | `0x68E0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 161 | `zelLoaderGetVersions` | `0x69E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 163 | `zelLoaderTranslateHandle` | `0x69F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 165 | `zelTracerCommandListAppendBarrierRegisterCallback` | `0x6A00` | 111 | UnwindData |  |
| 166 | `zelTracerCommandListAppendEventResetRegisterCallback` | `0x6A70` | 111 | UnwindData |  |
| 167 | `zelTracerCommandListAppendImageCopyFromMemoryExtRegisterCallback` | `0x6AE0` | 111 | UnwindData |  |
| 168 | `zelTracerCommandListAppendImageCopyFromMemoryRegisterCallback` | `0x6B50` | 111 | UnwindData |  |
| 169 | `zelTracerCommandListAppendImageCopyRegionRegisterCallback` | `0x6BC0` | 111 | UnwindData |  |
| 170 | `zelTracerCommandListAppendImageCopyRegisterCallback` | `0x6C30` | 111 | UnwindData |  |
| 171 | `zelTracerCommandListAppendImageCopyToMemoryExtRegisterCallback` | `0x6CA0` | 111 | UnwindData |  |
| 172 | `zelTracerCommandListAppendImageCopyToMemoryRegisterCallback` | `0x6D10` | 111 | UnwindData |  |
| 173 | `zelTracerCommandListAppendLaunchCooperativeKernelRegisterCallback` | `0x6D80` | 111 | UnwindData |  |
| 174 | `zelTracerCommandListAppendLaunchKernelIndirectRegisterCallback` | `0x6DF0` | 111 | UnwindData |  |
| 175 | `zelTracerCommandListAppendLaunchKernelRegisterCallback` | `0x6E60` | 111 | UnwindData |  |
| 176 | `zelTracerCommandListAppendLaunchMultipleKernelsIndirectRegisterCallback` | `0x6ED0` | 111 | UnwindData |  |
| 177 | `zelTracerCommandListAppendMemAdviseRegisterCallback` | `0x6F40` | 111 | UnwindData |  |
| 178 | `zelTracerCommandListAppendMemoryCopyFromContextRegisterCallback` | `0x6FB0` | 111 | UnwindData |  |
| 179 | `zelTracerCommandListAppendMemoryCopyRegionRegisterCallback` | `0x7020` | 111 | UnwindData |  |
| 180 | `zelTracerCommandListAppendMemoryCopyRegisterCallback` | `0x7090` | 111 | UnwindData |  |
| 181 | `zelTracerCommandListAppendMemoryFillRegisterCallback` | `0x7100` | 111 | UnwindData |  |
| 182 | `zelTracerCommandListAppendMemoryPrefetchRegisterCallback` | `0x7170` | 111 | UnwindData |  |
| 183 | `zelTracerCommandListAppendMemoryRangesBarrierRegisterCallback` | `0x71E0` | 111 | UnwindData |  |
| 184 | `zelTracerCommandListAppendQueryKernelTimestampsRegisterCallback` | `0x7250` | 111 | UnwindData |  |
| 185 | `zelTracerCommandListAppendSignalEventRegisterCallback` | `0x72C0` | 111 | UnwindData |  |
| 186 | `zelTracerCommandListAppendWaitOnEventsRegisterCallback` | `0x7330` | 111 | UnwindData |  |
| 187 | `zelTracerCommandListAppendWriteGlobalTimestampRegisterCallback` | `0x73A0` | 111 | UnwindData |  |
| 188 | `zelTracerCommandListCloseRegisterCallback` | `0x7410` | 111 | UnwindData |  |
| 189 | `zelTracerCommandListCreateImmediateRegisterCallback` | `0x7480` | 111 | UnwindData |  |
| 190 | `zelTracerCommandListCreateRegisterCallback` | `0x74F0` | 111 | UnwindData |  |
| 191 | `zelTracerCommandListDestroyRegisterCallback` | `0x7560` | 111 | UnwindData |  |
| 192 | `zelTracerCommandListResetRegisterCallback` | `0x75D0` | 111 | UnwindData |  |
| 193 | `zelTracerCommandQueueCreateRegisterCallback` | `0x7640` | 111 | UnwindData |  |
| 194 | `zelTracerCommandQueueDestroyRegisterCallback` | `0x76B0` | 111 | UnwindData |  |
| 195 | `zelTracerCommandQueueExecuteCommandListsRegisterCallback` | `0x7720` | 111 | UnwindData |  |
| 196 | `zelTracerCommandQueueSynchronizeRegisterCallback` | `0x7790` | 111 | UnwindData |  |
| 197 | `zelTracerContextCreateExRegisterCallback` | `0x7800` | 111 | UnwindData |  |
| 198 | `zelTracerContextCreateRegisterCallback` | `0x7870` | 111 | UnwindData |  |
| 199 | `zelTracerContextDestroyRegisterCallback` | `0x78E0` | 111 | UnwindData |  |
| 200 | `zelTracerContextEvictImageRegisterCallback` | `0x7950` | 111 | UnwindData |  |
| 201 | `zelTracerContextEvictMemoryRegisterCallback` | `0x79C0` | 111 | UnwindData |  |
| 202 | `zelTracerContextGetStatusRegisterCallback` | `0x7A30` | 111 | UnwindData |  |
| 203 | `zelTracerContextMakeImageResidentRegisterCallback` | `0x7AA0` | 111 | UnwindData |  |
| 204 | `zelTracerContextMakeMemoryResidentRegisterCallback` | `0x7B10` | 111 | UnwindData |  |
| 205 | `zelTracerContextSystemBarrierRegisterCallback` | `0x7B80` | 111 | UnwindData |  |
| 208 | `zelTracerDeviceCanAccessPeerRegisterCallback` | `0x7BF0` | 111 | UnwindData |  |
| 209 | `zelTracerDeviceGetCachePropertiesRegisterCallback` | `0x7C60` | 111 | UnwindData |  |
| 210 | `zelTracerDeviceGetCommandQueueGroupPropertiesRegisterCallback` | `0x7CD0` | 111 | UnwindData |  |
| 211 | `zelTracerDeviceGetComputePropertiesRegisterCallback` | `0x7D40` | 111 | UnwindData |  |
| 212 | `zelTracerDeviceGetExternalMemoryPropertiesRegisterCallback` | `0x7DB0` | 111 | UnwindData |  |
| 213 | `zelTracerDeviceGetGlobalTimestampsRegisterCallback` | `0x7E20` | 111 | UnwindData |  |
| 214 | `zelTracerDeviceGetImagePropertiesRegisterCallback` | `0x7E90` | 111 | UnwindData |  |
| 215 | `zelTracerDeviceGetMemoryAccessPropertiesRegisterCallback` | `0x7F00` | 111 | UnwindData |  |
| 216 | `zelTracerDeviceGetMemoryPropertiesRegisterCallback` | `0x7F70` | 111 | UnwindData |  |
| 217 | `zelTracerDeviceGetModulePropertiesRegisterCallback` | `0x7FE0` | 111 | UnwindData |  |
| 218 | `zelTracerDeviceGetP2PPropertiesRegisterCallback` | `0x8050` | 111 | UnwindData |  |
| 219 | `zelTracerDeviceGetPropertiesRegisterCallback` | `0x80C0` | 111 | UnwindData |  |
| 220 | `zelTracerDeviceGetRegisterCallback` | `0x8130` | 111 | UnwindData |  |
| 221 | `zelTracerDeviceGetStatusRegisterCallback` | `0x81A0` | 111 | UnwindData |  |
| 222 | `zelTracerDeviceGetSubDevicesRegisterCallback` | `0x8210` | 111 | UnwindData |  |
| 223 | `zelTracerDevicePciGetPropertiesExtRegisterCallback` | `0x8280` | 111 | UnwindData |  |
| 224 | `zelTracerDeviceReserveCacheExtRegisterCallback` | `0x82F0` | 111 | UnwindData |  |
| 225 | `zelTracerDeviceSetCacheAdviceExtRegisterCallback` | `0x8360` | 111 | UnwindData |  |
| 226 | `zelTracerDriverGetApiVersionRegisterCallback` | `0x83D0` | 111 | UnwindData |  |
| 227 | `zelTracerDriverGetExtensionFunctionAddressRegisterCallback` | `0x8440` | 111 | UnwindData |  |
| 228 | `zelTracerDriverGetExtensionPropertiesRegisterCallback` | `0x84B0` | 111 | UnwindData |  |
| 229 | `zelTracerDriverGetIpcPropertiesRegisterCallback` | `0x8520` | 111 | UnwindData |  |
| 230 | `zelTracerDriverGetPropertiesRegisterCallback` | `0x8590` | 111 | UnwindData |  |
| 231 | `zelTracerDriverGetRegisterCallback` | `0x8600` | 111 | UnwindData |  |
| 232 | `zelTracerEventCreateRegisterCallback` | `0x8670` | 111 | UnwindData |  |
| 233 | `zelTracerEventDestroyRegisterCallback` | `0x86E0` | 111 | UnwindData |  |
| 234 | `zelTracerEventHostResetRegisterCallback` | `0x8750` | 111 | UnwindData |  |
| 235 | `zelTracerEventHostSignalRegisterCallback` | `0x87C0` | 111 | UnwindData |  |
| 236 | `zelTracerEventHostSynchronizeRegisterCallback` | `0x8830` | 111 | UnwindData |  |
| 237 | `zelTracerEventPoolCloseIpcHandleRegisterCallback` | `0x88A0` | 111 | UnwindData |  |
| 238 | `zelTracerEventPoolCreateRegisterCallback` | `0x8910` | 111 | UnwindData |  |
| 239 | `zelTracerEventPoolDestroyRegisterCallback` | `0x8980` | 111 | UnwindData |  |
| 240 | `zelTracerEventPoolGetIpcHandleRegisterCallback` | `0x89F0` | 111 | UnwindData |  |
| 241 | `zelTracerEventPoolOpenIpcHandleRegisterCallback` | `0x8A60` | 111 | UnwindData |  |
| 242 | `zelTracerEventQueryKernelTimestampRegisterCallback` | `0x8AD0` | 111 | UnwindData |  |
| 243 | `zelTracerEventQueryStatusRegisterCallback` | `0x8B40` | 111 | UnwindData |  |
| 244 | `zelTracerEventQueryTimestampsExpRegisterCallback` | `0x8BB0` | 111 | UnwindData |  |
| 245 | `zelTracerFenceCreateRegisterCallback` | `0x8C20` | 111 | UnwindData |  |
| 246 | `zelTracerFenceDestroyRegisterCallback` | `0x8C90` | 111 | UnwindData |  |
| 247 | `zelTracerFenceHostSynchronizeRegisterCallback` | `0x8D00` | 111 | UnwindData |  |
| 248 | `zelTracerFenceQueryStatusRegisterCallback` | `0x8D70` | 111 | UnwindData |  |
| 249 | `zelTracerFenceResetRegisterCallback` | `0x8DE0` | 111 | UnwindData |  |
| 250 | `zelTracerImageCreateRegisterCallback` | `0x8E50` | 111 | UnwindData |  |
| 251 | `zelTracerImageDestroyRegisterCallback` | `0x8EC0` | 111 | UnwindData |  |
| 252 | `zelTracerImageGetAllocPropertiesExtRegisterCallback` | `0x8F30` | 111 | UnwindData |  |
| 253 | `zelTracerImageGetMemoryPropertiesExpRegisterCallback` | `0x8FA0` | 111 | UnwindData |  |
| 254 | `zelTracerImageGetPropertiesRegisterCallback` | `0x9010` | 111 | UnwindData |  |
| 255 | `zelTracerImageViewCreateExpRegisterCallback` | `0x9080` | 111 | UnwindData |  |
| 256 | `zelTracerInitRegisterCallback` | `0x90F0` | 111 | UnwindData |  |
| 257 | `zelTracerKernelCreateRegisterCallback` | `0x9160` | 111 | UnwindData |  |
| 258 | `zelTracerKernelDestroyRegisterCallback` | `0x91D0` | 111 | UnwindData |  |
| 259 | `zelTracerKernelGetIndirectAccessRegisterCallback` | `0x9240` | 111 | UnwindData |  |
| 260 | `zelTracerKernelGetNameRegisterCallback` | `0x92B0` | 111 | UnwindData |  |
| 261 | `zelTracerKernelGetPropertiesRegisterCallback` | `0x9320` | 111 | UnwindData |  |
| 262 | `zelTracerKernelGetSourceAttributesRegisterCallback` | `0x9390` | 111 | UnwindData |  |
| 263 | `zelTracerKernelSchedulingHintExpRegisterCallback` | `0x9400` | 111 | UnwindData |  |
| 264 | `zelTracerKernelSetArgumentValueRegisterCallback` | `0x9470` | 111 | UnwindData |  |
| 265 | `zelTracerKernelSetCacheConfigRegisterCallback` | `0x94E0` | 111 | UnwindData |  |
| 266 | `zelTracerKernelSetGlobalOffsetExpRegisterCallback` | `0x9550` | 111 | UnwindData |  |
| 267 | `zelTracerKernelSetGroupSizeRegisterCallback` | `0x95C0` | 111 | UnwindData |  |
| 268 | `zelTracerKernelSetIndirectAccessRegisterCallback` | `0x9630` | 111 | UnwindData |  |
| 269 | `zelTracerKernelSuggestGroupSizeRegisterCallback` | `0x96A0` | 111 | UnwindData |  |
| 270 | `zelTracerKernelSuggestMaxCooperativeGroupCountRegisterCallback` | `0x9710` | 111 | UnwindData |  |
| 271 | `zelTracerMemAllocDeviceRegisterCallback` | `0x9780` | 111 | UnwindData |  |
| 272 | `zelTracerMemAllocHostRegisterCallback` | `0x97F0` | 111 | UnwindData |  |
| 273 | `zelTracerMemAllocSharedRegisterCallback` | `0x9860` | 111 | UnwindData |  |
| 274 | `zelTracerMemCloseIpcHandleRegisterCallback` | `0x98D0` | 111 | UnwindData |  |
| 275 | `zelTracerMemFreeExtRegisterCallback` | `0x9940` | 111 | UnwindData |  |
| 276 | `zelTracerMemFreeRegisterCallback` | `0x99B0` | 111 | UnwindData |  |
| 277 | `zelTracerMemGetAddressRangeRegisterCallback` | `0x9A20` | 111 | UnwindData |  |
| 278 | `zelTracerMemGetAllocPropertiesRegisterCallback` | `0x9A90` | 111 | UnwindData |  |
| 279 | `zelTracerMemGetIpcHandleRegisterCallback` | `0x9B00` | 111 | UnwindData |  |
| 280 | `zelTracerMemOpenIpcHandleRegisterCallback` | `0x9B70` | 111 | UnwindData |  |
| 281 | `zelTracerModuleBuildLogDestroyRegisterCallback` | `0x9BE0` | 111 | UnwindData |  |
| 282 | `zelTracerModuleBuildLogGetStringRegisterCallback` | `0x9C50` | 111 | UnwindData |  |
| 283 | `zelTracerModuleCreateRegisterCallback` | `0x9CC0` | 111 | UnwindData |  |
| 284 | `zelTracerModuleDestroyRegisterCallback` | `0x9D30` | 111 | UnwindData |  |
| 285 | `zelTracerModuleDynamicLinkRegisterCallback` | `0x9DA0` | 111 | UnwindData |  |
| 286 | `zelTracerModuleGetFunctionPointerRegisterCallback` | `0x9E10` | 111 | UnwindData |  |
| 287 | `zelTracerModuleGetGlobalPointerRegisterCallback` | `0x9E80` | 111 | UnwindData |  |
| 288 | `zelTracerModuleGetKernelNamesRegisterCallback` | `0x9EF0` | 111 | UnwindData |  |
| 289 | `zelTracerModuleGetNativeBinaryRegisterCallback` | `0x9F60` | 111 | UnwindData |  |
| 290 | `zelTracerModuleGetPropertiesRegisterCallback` | `0x9FD0` | 111 | UnwindData |  |
| 291 | `zelTracerModuleInspectLinkageExtRegisterCallback` | `0xA040` | 111 | UnwindData |  |
| 292 | `zelTracerPhysicalMemCreateRegisterCallback` | `0xA0B0` | 111 | UnwindData |  |
| 293 | `zelTracerPhysicalMemDestroyRegisterCallback` | `0xA120` | 111 | UnwindData |  |
| 294 | `zelTracerSamplerCreateRegisterCallback` | `0xA190` | 111 | UnwindData |  |
| 295 | `zelTracerSamplerDestroyRegisterCallback` | `0xA200` | 111 | UnwindData |  |
| 299 | `zelTracerVirtualMemFreeRegisterCallback` | `0xA270` | 111 | UnwindData |  |
| 300 | `zelTracerVirtualMemGetAccessAttributeRegisterCallback` | `0xA2E0` | 111 | UnwindData |  |
| 301 | `zelTracerVirtualMemMapRegisterCallback` | `0xA350` | 111 | UnwindData |  |
| 302 | `zelTracerVirtualMemQueryPageSizeRegisterCallback` | `0xA3C0` | 111 | UnwindData |  |
| 303 | `zelTracerVirtualMemReserveRegisterCallback` | `0xA430` | 111 | UnwindData |  |
| 304 | `zelTracerVirtualMemSetAccessAttributeRegisterCallback` | `0xA4A0` | 111 | UnwindData |  |
| 305 | `zelTracerVirtualMemUnmapRegisterCallback` | `0xA510` | 111 | UnwindData |  |
| 125 | `zeLoaderGetTracingHandle` | `0xC500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `zeLoaderInit` | `0xC510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 160 | `zelLoaderDriverCheck` | `0xC520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 162 | `zelLoaderGetVersionsInternal` | `0xC530` | 141 | UnwindData |  |
| 164 | `zelLoaderTranslateHandleInternal` | `0xC5C0` | 18,560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `zeGetCommandListProcAddrTable` | `0x10E40` | 912 | UnwindData |  |
| 85 | `zeGetCommandQueueProcAddrTable` | `0x111D0` | 499 | UnwindData |  |
| 86 | `zeGetContextProcAddrTable` | `0x113D0` | 592 | UnwindData |  |
| 87 | `zeGetDeviceProcAddrTable` | `0x11620` | 734 | UnwindData |  |
| 88 | `zeGetDriverProcAddrTable` | `0x11900` | 521 | UnwindData |  |
| 89 | `zeGetEventExpProcAddrTable` | `0x11B10` | 123 | UnwindData |  |
| 90 | `zeGetEventPoolProcAddrTable` | `0x11CD0` | 524 | UnwindData |  |
| 91 | `zeGetEventProcAddrTable` | `0x11EE0` | 558 | UnwindData |  |
| 92 | `zeGetFenceProcAddrTable` | `0x12110` | 524 | UnwindData |  |
| 93 | `zeGetGlobalProcAddrTable` | `0x12320` | 440 | UnwindData |  |
| 94 | `zeGetImageExpProcAddrTable` | `0x124E0` | 123 | UnwindData |  |
| 95 | `zeGetImageProcAddrTable` | `0x126B0` | 499 | UnwindData |  |
| 96 | `zeGetKernelExpProcAddrTable` | `0x128B0` | 123 | UnwindData |  |
| 97 | `zeGetKernelProcAddrTable` | `0x12A80` | 638 | UnwindData |  |
| 98 | `zeGetMemProcAddrTable` | `0x12D00` | 601 | UnwindData |  |
| 99 | `zeGetModuleBuildLogProcAddrTable` | `0x12F60` | 462 | UnwindData |  |
| 100 | `zeGetModuleProcAddrTable` | `0x13130` | 592 | UnwindData |  |
| 101 | `zeGetPhysicalMemProcAddrTable` | `0x13380` | 462 | UnwindData |  |
| 102 | `zeGetSamplerProcAddrTable` | `0x13550` | 462 | UnwindData |  |
| 103 | `zeGetVirtualMemProcAddrTable` | `0x13720` | 558 | UnwindData |  |
| 440 | `zetGetCommandListProcAddrTable` | `0x144F0` | 443 | UnwindData |  |
| 441 | `zetGetContextProcAddrTable` | `0x146B0` | 391 | UnwindData |  |
| 442 | `zetGetDebugProcAddrTable` | `0x14840` | 570 | UnwindData |  |
| 443 | `zetGetDeviceProcAddrTable` | `0x14A80` | 391 | UnwindData |  |
| 444 | `zetGetKernelProcAddrTable` | `0x14C10` | 391 | UnwindData |  |
| 445 | `zetGetMetricGroupExpProcAddrTable` | `0x14DA0` | 124 | UnwindData |  |
| 446 | `zetGetMetricGroupProcAddrTable` | `0x14F20` | 434 | UnwindData |  |
| 447 | `zetGetMetricProcAddrTable` | `0x150E0` | 407 | UnwindData |  |
| 448 | `zetGetMetricQueryPoolProcAddrTable` | `0x15280` | 407 | UnwindData |  |
| 449 | `zetGetMetricQueryProcAddrTable` | `0x15420` | 443 | UnwindData |  |
| 450 | `zetGetMetricStreamerProcAddrTable` | `0x155E0` | 434 | UnwindData |  |
| 451 | `zetGetModuleProcAddrTable` | `0x157A0` | 391 | UnwindData |  |
| 452 | `zetGetTracerExpProcAddrTable` | `0x15930` | 468 | UnwindData |  |
| 369 | `zesGetDeviceProcAddrTable` | `0x17140` | 819 | UnwindData |  |
| 370 | `zesGetDiagnosticsProcAddrTable` | `0x17480` | 434 | UnwindData |  |
| 371 | `zesGetDriverProcAddrTable` | `0x17640` | 407 | UnwindData |  |
| 372 | `zesGetEngineProcAddrTable` | `0x177E0` | 407 | UnwindData |  |
| 373 | `zesGetFabricPortProcAddrTable` | `0x17980` | 477 | UnwindData |  |
| 374 | `zesGetFanProcAddrTable` | `0x17B60` | 477 | UnwindData |  |
| 375 | `zesGetFirmwareProcAddrTable` | `0x17D40` | 407 | UnwindData |  |
| 376 | `zesGetFrequencyProcAddrTable` | `0x17EE0` | 681 | UnwindData |  |
| 377 | `zesGetLedProcAddrTable` | `0x18190` | 443 | UnwindData |  |
| 378 | `zesGetMemoryProcAddrTable` | `0x18350` | 434 | UnwindData |  |
| 379 | `zesGetPerformanceFactorProcAddrTable` | `0x18510` | 434 | UnwindData |  |
| 380 | `zesGetPowerProcAddrTable` | `0x186D0` | 477 | UnwindData |  |
| 381 | `zesGetPsuProcAddrTable` | `0x188B0` | 407 | UnwindData |  |
| 382 | `zesGetRasProcAddrTable` | `0x18A50` | 443 | UnwindData |  |
| 383 | `zesGetSchedulerProcAddrTable` | `0x18C10` | 511 | UnwindData |  |
| 384 | `zesGetStandbyProcAddrTable` | `0x18E10` | 434 | UnwindData |  |
| 385 | `zesGetTemperatureProcAddrTable` | `0x18FD0` | 443 | UnwindData |  |
| 159 | `zelGetTracerApiProcAddrTable` | `0x19190` | 178 | UnwindData |  |
