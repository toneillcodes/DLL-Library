# Binary Specification: ze_loader.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_1973c0a49e1f4f8c\ze_loader.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1b72788a14279c05248627666df02acaca5d10b6c3947f13cb09e362cfcfd7fd`
* **Total Exported Functions:** 458

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `zeCommandListAppendBarrier` | `0x35B0` | 44 | UnwindData |  |
| 2 | `zeCommandListAppendEventReset` | `0x35E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `zeCommandListAppendImageCopy` | `0x3600` | 68 | UnwindData |  |
| 4 | `zeCommandListAppendImageCopyFromMemory` | `0x3650` | 81 | UnwindData |  |
| 5 | `zeCommandListAppendImageCopyRegion` | `0x36B0` | 100 | UnwindData |  |
| 6 | `zeCommandListAppendImageCopyToMemory` | `0x3720` | 81 | UnwindData |  |
| 7 | `zeCommandListAppendLaunchCooperativeKernel` | `0x3780` | 68 | UnwindData |  |
| 8 | `zeCommandListAppendLaunchKernel` | `0x37D0` | 68 | UnwindData |  |
| 9 | `zeCommandListAppendLaunchKernelIndirect` | `0x3820` | 68 | UnwindData |  |
| 10 | `zeCommandListAppendLaunchMultipleKernelsIndirect` | `0x3870` | 100 | UnwindData |  |
| 11 | `zeCommandListAppendMemAdvise` | `0x38E0` | 58 | UnwindData |  |
| 12 | `zeCommandListAppendMemoryCopy` | `0x3920` | 81 | UnwindData |  |
| 13 | `zeCommandListAppendMemoryCopyFromContext` | `0x3980` | 100 | UnwindData |  |
| 14 | `zeCommandListAppendMemoryCopyRegion` | `0x39F0` | 149 | UnwindData |  |
| 15 | `zeCommandListAppendMemoryFill` | `0x3A90` | 100 | UnwindData |  |
| 16 | `zeCommandListAppendMemoryPrefetch` | `0x3B00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `zeCommandListAppendMemoryRangesBarrier` | `0x3B20` | 81 | UnwindData |  |
| 18 | `zeCommandListAppendQueryKernelTimestamps` | `0x3B80` | 100 | UnwindData |  |
| 19 | `zeCommandListAppendSignalEvent` | `0x3BF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `zeCommandListAppendWaitOnEvents` | `0x3C10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `zeCommandListAppendWriteGlobalTimestamp` | `0x3C30` | 60 | UnwindData |  |
| 22 | `zeCommandListClose` | `0x3C70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `zeCommandListCreate` | `0x3C90` | 44 | UnwindData |  |
| 24 | `zeCommandListCreateImmediate` | `0x3CC0` | 44 | UnwindData |  |
| 25 | `zeCommandListDestroy` | `0x3CF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `zeCommandListReset` | `0x3D10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `zeCommandQueueCreate` | `0x3D30` | 44 | UnwindData |  |
| 28 | `zeCommandQueueDestroy` | `0x3D60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `zeCommandQueueExecuteCommandLists` | `0x3D80` | 44 | UnwindData |  |
| 30 | `zeCommandQueueSynchronize` | `0x3DB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `zeContextCreate` | `0x3DD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `zeContextCreateEx` | `0x3DF0` | 60 | UnwindData |  |
| 33 | `zeContextDestroy` | `0x3E30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `zeContextEvictImage` | `0x3E50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `zeContextEvictMemory` | `0x3E70` | 44 | UnwindData |  |
| 36 | `zeContextGetStatus` | `0x3EA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `zeContextMakeImageResident` | `0x3EC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `zeContextMakeMemoryResident` | `0x3EE0` | 44 | UnwindData |  |
| 39 | `zeContextSystemBarrier` | `0x3F10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `zeDeviceCanAccessPeer` | `0x3F30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `zeDeviceGet` | `0x3F50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `zeDeviceGetCacheProperties` | `0x3F70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `zeDeviceGetCommandQueueGroupProperties` | `0x3F90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `zeDeviceGetComputeProperties` | `0x3FB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `zeDeviceGetExternalMemoryProperties` | `0x3FD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `zeDeviceGetGlobalTimestamps` | `0x3FF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `zeDeviceGetImageProperties` | `0x4010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `zeDeviceGetMemoryAccessProperties` | `0x4030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `zeDeviceGetMemoryProperties` | `0x4050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `zeDeviceGetModuleProperties` | `0x4070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `zeDeviceGetP2PProperties` | `0x4090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `zeDeviceGetProperties` | `0x40B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `zeDeviceGetStatus` | `0x40D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `zeDeviceGetSubDevices` | `0x40F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `zeDeviceReserveCacheExt` | `0x4110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `zeDeviceSetCacheAdviceExt` | `0x4130` | 44 | UnwindData |  |
| 57 | `zeDriverGet` | `0x4160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `zeDriverGetApiVersion` | `0x4180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `zeDriverGetExtensionFunctionAddress` | `0x41A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `zeDriverGetExtensionProperties` | `0x41C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `zeDriverGetIpcProperties` | `0x41E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `zeDriverGetProperties` | `0x4200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `zeEventCreate` | `0x4220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `zeEventDestroy` | `0x4240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `zeEventHostReset` | `0x4260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `zeEventHostSignal` | `0x4280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `zeEventHostSynchronize` | `0x42A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `zeEventPoolCloseIpcHandle` | `0x42C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `zeEventPoolCreate` | `0x42E0` | 60 | UnwindData |  |
| 70 | `zeEventPoolDestroy` | `0x4320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `zeEventPoolGetIpcHandle` | `0x4340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `zeEventPoolOpenIpcHandle` | `0x4360` | 84 | UnwindData |  |
| 73 | `zeEventQueryKernelTimestamp` | `0x43C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `zeEventQueryStatus` | `0x43E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `zeEventQueryTimestampsExp` | `0x4400` | 44 | UnwindData |  |
| 76 | `zeFenceCreate` | `0x4430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `zeFenceDestroy` | `0x4450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `zeFenceHostSynchronize` | `0x4470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `zeFenceQueryStatus` | `0x4490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `zeFenceReset` | `0x44B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `zeImageCreate` | `0x44D0` | 44 | UnwindData |  |
| 102 | `zeImageDestroy` | `0x4500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `zeImageGetMemoryPropertiesExp` | `0x4520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `zeImageGetProperties` | `0x4540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `zeImageViewCreateExp` | `0x4560` | 60 | UnwindData |  |
| 106 | `zeInit` | `0x45A0` | 177 | UnwindData |  |
| 107 | `zeKernelCreate` | `0x4660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `zeKernelDestroy` | `0x4680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `zeKernelGetIndirectAccess` | `0x46A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `zeKernelGetName` | `0x46C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `zeKernelGetProperties` | `0x46E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `zeKernelGetSourceAttributes` | `0x4700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `zeKernelSchedulingHintExp` | `0x4720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `zeKernelSetArgumentValue` | `0x4740` | 44 | UnwindData |  |
| 115 | `zeKernelSetCacheConfig` | `0x4770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `zeKernelSetGlobalOffsetExp` | `0x4790` | 44 | UnwindData |  |
| 117 | `zeKernelSetGroupSize` | `0x47C0` | 44 | UnwindData |  |
| 118 | `zeKernelSetIndirectAccess` | `0x47F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `zeKernelSuggestGroupSize` | `0x4810` | 83 | UnwindData |  |
| 120 | `zeKernelSuggestMaxCooperativeGroupCount` | `0x4870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `zeMemAllocDevice` | `0x4890` | 70 | UnwindData |  |
| 124 | `zeMemAllocHost` | `0x48E0` | 60 | UnwindData |  |
| 125 | `zeMemAllocShared` | `0x4920` | 83 | UnwindData |  |
| 126 | `zeMemCloseIpcHandle` | `0x4980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `zeMemFree` | `0x49A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `zeMemGetAddressRange` | `0x49C0` | 44 | UnwindData |  |
| 129 | `zeMemGetAllocProperties` | `0x49F0` | 44 | UnwindData |  |
| 130 | `zeMemGetIpcHandle` | `0x4A20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `zeMemOpenIpcHandle` | `0x4A40` | 107 | UnwindData |  |
| 132 | `zeModuleBuildLogDestroy` | `0x4AB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `zeModuleBuildLogGetString` | `0x4AD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `zeModuleCreate` | `0x4AF0` | 60 | UnwindData |  |
| 135 | `zeModuleDestroy` | `0x4B30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `zeModuleDynamicLink` | `0x4B50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `zeModuleGetFunctionPointer` | `0x4B70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `zeModuleGetGlobalPointer` | `0x4B90` | 44 | UnwindData |  |
| 139 | `zeModuleGetKernelNames` | `0x4BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `zeModuleGetNativeBinary` | `0x4BE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `zeModuleGetProperties` | `0x4C00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `zePhysicalMemCreate` | `0x4C20` | 44 | UnwindData |  |
| 143 | `zePhysicalMemDestroy` | `0x4C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `zeSamplerCreate` | `0x4C70` | 44 | UnwindData |  |
| 145 | `zeSamplerDestroy` | `0x4CA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `zeVirtualMemFree` | `0x4CC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `zeVirtualMemGetAccessAttribute` | `0x4CE0` | 60 | UnwindData |  |
| 148 | `zeVirtualMemMap` | `0x4D20` | 68 | UnwindData |  |
| 149 | `zeVirtualMemQueryPageSize` | `0x4D70` | 44 | UnwindData |  |
| 150 | `zeVirtualMemReserve` | `0x4DA0` | 44 | UnwindData |  |
| 151 | `zeVirtualMemSetAccessAttribute` | `0x4DD0` | 44 | UnwindData |  |
| 152 | `zeVirtualMemUnmap` | `0x4E00` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 407 | `zetCommandListAppendMetricMemoryBarrier` | `0x5000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 408 | `zetCommandListAppendMetricQueryBegin` | `0x5020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 409 | `zetCommandListAppendMetricQueryEnd` | `0x5040` | 60 | UnwindData |  |
| 410 | `zetCommandListAppendMetricStreamerMarker` | `0x5080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 411 | `zetContextActivateMetricGroups` | `0x50A0` | 44 | UnwindData |  |
| 412 | `zetDebugAcknowledgeEvent` | `0x50D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 413 | `zetDebugAttach` | `0x50F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 414 | `zetDebugDetach` | `0x5110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 415 | `zetDebugGetRegisterSetProperties` | `0x5130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 416 | `zetDebugInterrupt` | `0x5150` | 57 | UnwindData |  |
| 417 | `zetDebugReadEvent` | `0x5190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 418 | `zetDebugReadMemory` | `0x51B0` | 73 | UnwindData |  |
| 419 | `zetDebugReadRegisters` | `0x5200` | 87 | UnwindData |  |
| 420 | `zetDebugResume` | `0x5260` | 57 | UnwindData |  |
| 421 | `zetDebugWriteMemory` | `0x52A0` | 73 | UnwindData |  |
| 422 | `zetDebugWriteRegisters` | `0x52F0` | 87 | UnwindData |  |
| 423 | `zetDeviceGetDebugProperties` | `0x5350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 437 | `zetKernelGetProfileInfo` | `0x5370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 438 | `zetMetricGet` | `0x5390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 439 | `zetMetricGetProperties` | `0x53B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 440 | `zetMetricGroupCalculateMetricValues` | `0x53D0` | 70 | UnwindData |  |
| 441 | `zetMetricGroupCalculateMultipleMetricValuesExp` | `0x5420` | 102 | UnwindData |  |
| 442 | `zetMetricGroupGet` | `0x5490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 443 | `zetMetricGroupGetProperties` | `0x54B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 444 | `zetMetricQueryCreate` | `0x54D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 445 | `zetMetricQueryDestroy` | `0x54F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 446 | `zetMetricQueryGetData` | `0x5510` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 447 | `zetMetricQueryPoolCreate` | `0x5530` | 60 | UnwindData |  |
| 448 | `zetMetricQueryPoolDestroy` | `0x5570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 449 | `zetMetricQueryReset` | `0x5590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 450 | `zetMetricStreamerClose` | `0x55B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 451 | `zetMetricStreamerOpen` | `0x55D0` | 70 | UnwindData |  |
| 452 | `zetMetricStreamerReadData` | `0x5620` | 44 | UnwindData |  |
| 453 | `zetModuleGetDebugInfo` | `0x5650` | 44 | UnwindData |  |
| 454 | `zetTracerExpCreate` | `0x5680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 455 | `zetTracerExpDestroy` | `0x56A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 456 | `zetTracerExpSetEnabled` | `0x56C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 457 | `zetTracerExpSetEpilogues` | `0x56E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 458 | `zetTracerExpSetPrologues` | `0x5700` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 291 | `zesDeviceEnumDiagnosticTestSuites` | `0x5860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 292 | `zesDeviceEnumEngineGroups` | `0x5880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 293 | `zesDeviceEnumFabricPorts` | `0x58A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 294 | `zesDeviceEnumFans` | `0x58C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 295 | `zesDeviceEnumFirmwares` | `0x58E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 296 | `zesDeviceEnumFrequencyDomains` | `0x5900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 297 | `zesDeviceEnumLeds` | `0x5920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 298 | `zesDeviceEnumMemoryModules` | `0x5940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 299 | `zesDeviceEnumPerformanceFactorDomains` | `0x5960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 300 | `zesDeviceEnumPowerDomains` | `0x5980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 301 | `zesDeviceEnumPsus` | `0x59A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 302 | `zesDeviceEnumRasErrorSets` | `0x59C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 303 | `zesDeviceEnumSchedulers` | `0x59E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 304 | `zesDeviceEnumStandbyDomains` | `0x5A00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 305 | `zesDeviceEnumTemperatureSensors` | `0x5A20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 306 | `zesDeviceEventRegister` | `0x5A40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 307 | `zesDeviceGetProperties` | `0x5A60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 308 | `zesDeviceGetState` | `0x5A80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 309 | `zesDevicePciGetBars` | `0x5AA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 310 | `zesDevicePciGetProperties` | `0x5AC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 311 | `zesDevicePciGetState` | `0x5AE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 312 | `zesDevicePciGetStats` | `0x5B00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 313 | `zesDeviceProcessesGetState` | `0x5B20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 314 | `zesDeviceReset` | `0x5B40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 315 | `zesDiagnosticsGetProperties` | `0x5B60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 316 | `zesDiagnosticsGetTests` | `0x5B80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 317 | `zesDiagnosticsRunTests` | `0x5BA0` | 44 | UnwindData |  |
| 318 | `zesDriverEventListen` | `0x5BD0` | 70 | UnwindData |  |
| 319 | `zesDriverEventListenEx` | `0x5C20` | 70 | UnwindData |  |
| 320 | `zesEngineGetActivity` | `0x5C70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 321 | `zesEngineGetProperties` | `0x5C90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 322 | `zesFabricPortGetConfig` | `0x5CB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 323 | `zesFabricPortGetLinkType` | `0x5CD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 324 | `zesFabricPortGetProperties` | `0x5CF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 325 | `zesFabricPortGetState` | `0x5D10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 326 | `zesFabricPortGetThroughput` | `0x5D30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 327 | `zesFabricPortSetConfig` | `0x5D50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 328 | `zesFanGetConfig` | `0x5D70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 329 | `zesFanGetProperties` | `0x5D90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 330 | `zesFanGetState` | `0x5DB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 331 | `zesFanSetDefaultMode` | `0x5DD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 332 | `zesFanSetFixedSpeedMode` | `0x5DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 333 | `zesFanSetSpeedTableMode` | `0x5E10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 334 | `zesFirmwareFlash` | `0x5E30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 335 | `zesFirmwareGetProperties` | `0x5E50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 336 | `zesFrequencyGetAvailableClocks` | `0x5E70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 337 | `zesFrequencyGetProperties` | `0x5E90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 338 | `zesFrequencyGetRange` | `0x5EB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 339 | `zesFrequencyGetState` | `0x5ED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 340 | `zesFrequencyGetThrottleTime` | `0x5EF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 341 | `zesFrequencyOcGetCapabilities` | `0x5F10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 342 | `zesFrequencyOcGetFrequencyTarget` | `0x5F30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 343 | `zesFrequencyOcGetIccMax` | `0x5F50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 344 | `zesFrequencyOcGetMode` | `0x5F70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 345 | `zesFrequencyOcGetTjMax` | `0x5F90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 346 | `zesFrequencyOcGetVoltageTarget` | `0x5FB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 347 | `zesFrequencyOcSetFrequencyTarget` | `0x5FD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 348 | `zesFrequencyOcSetIccMax` | `0x5FF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 349 | `zesFrequencyOcSetMode` | `0x6010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 350 | `zesFrequencyOcSetTjMax` | `0x6030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 351 | `zesFrequencyOcSetVoltageTarget` | `0x6050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 352 | `zesFrequencySetRange` | `0x6070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 370 | `zesLedGetProperties` | `0x6090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 371 | `zesLedGetState` | `0x60B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 372 | `zesLedSetColor` | `0x60D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 373 | `zesLedSetState` | `0x60F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 374 | `zesMemoryGetBandwidth` | `0x6110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 375 | `zesMemoryGetProperties` | `0x6130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 376 | `zesMemoryGetState` | `0x6150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 377 | `zesPerformanceFactorGetConfig` | `0x6170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 378 | `zesPerformanceFactorGetProperties` | `0x6190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 379 | `zesPerformanceFactorSetConfig` | `0x61B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 380 | `zesPowerGetEnergyCounter` | `0x61D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 381 | `zesPowerGetEnergyThreshold` | `0x61F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 382 | `zesPowerGetLimits` | `0x6210` | 44 | UnwindData |  |
| 383 | `zesPowerGetProperties` | `0x6240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 384 | `zesPowerSetEnergyThreshold` | `0x6260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 385 | `zesPowerSetLimits` | `0x6280` | 44 | UnwindData |  |
| 386 | `zesPsuGetProperties` | `0x62B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 387 | `zesPsuGetState` | `0x62D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 388 | `zesRasGetConfig` | `0x62F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 389 | `zesRasGetProperties` | `0x6310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 390 | `zesRasGetState` | `0x6330` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 391 | `zesRasSetConfig` | `0x6350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 392 | `zesSchedulerGetCurrentMode` | `0x6370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 393 | `zesSchedulerGetProperties` | `0x6390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 394 | `zesSchedulerGetTimeoutModeProperties` | `0x63B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 395 | `zesSchedulerGetTimesliceModeProperties` | `0x63D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 396 | `zesSchedulerSetComputeUnitDebugMode` | `0x63F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 397 | `zesSchedulerSetExclusiveMode` | `0x6410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 398 | `zesSchedulerSetTimeoutMode` | `0x6430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 399 | `zesSchedulerSetTimesliceMode` | `0x6450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 400 | `zesStandbyGetMode` | `0x6470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 401 | `zesStandbyGetProperties` | `0x6490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 402 | `zesStandbySetMode` | `0x64B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 403 | `zesTemperatureGetConfig` | `0x64D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 404 | `zesTemperatureGetProperties` | `0x64F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 405 | `zesTemperatureGetState` | `0x6510` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 406 | `zesTemperatureSetConfig` | `0x6530` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 195 | `zelTracerCreate` | `0x66F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 196 | `zelTracerDestroy` | `0x6710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 281 | `zelTracerSetEnabled` | `0x6730` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 282 | `zelTracerSetEpilogues` | `0x6750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 283 | `zelTracerSetPrologues` | `0x6770` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `zelLoaderGetVersions` | `0x6860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `zelTracerCommandListAppendBarrierRegisterCallback` | `0x6870` | 111 | UnwindData |  |
| 157 | `zelTracerCommandListAppendEventResetRegisterCallback` | `0x68E0` | 111 | UnwindData |  |
| 158 | `zelTracerCommandListAppendImageCopyFromMemoryRegisterCallback` | `0x6950` | 111 | UnwindData |  |
| 159 | `zelTracerCommandListAppendImageCopyRegionRegisterCallback` | `0x69C0` | 111 | UnwindData |  |
| 160 | `zelTracerCommandListAppendImageCopyRegisterCallback` | `0x6A30` | 111 | UnwindData |  |
| 161 | `zelTracerCommandListAppendImageCopyToMemoryRegisterCallback` | `0x6AA0` | 111 | UnwindData |  |
| 162 | `zelTracerCommandListAppendLaunchCooperativeKernelRegisterCallback` | `0x6B10` | 111 | UnwindData |  |
| 163 | `zelTracerCommandListAppendLaunchKernelIndirectRegisterCallback` | `0x6B80` | 111 | UnwindData |  |
| 164 | `zelTracerCommandListAppendLaunchKernelRegisterCallback` | `0x6BF0` | 111 | UnwindData |  |
| 165 | `zelTracerCommandListAppendLaunchMultipleKernelsIndirectRegisterCallback` | `0x6C60` | 111 | UnwindData |  |
| 166 | `zelTracerCommandListAppendMemAdviseRegisterCallback` | `0x6CD0` | 111 | UnwindData |  |
| 167 | `zelTracerCommandListAppendMemoryCopyFromContextRegisterCallback` | `0x6D40` | 111 | UnwindData |  |
| 168 | `zelTracerCommandListAppendMemoryCopyRegionRegisterCallback` | `0x6DB0` | 111 | UnwindData |  |
| 169 | `zelTracerCommandListAppendMemoryCopyRegisterCallback` | `0x6E20` | 111 | UnwindData |  |
| 170 | `zelTracerCommandListAppendMemoryFillRegisterCallback` | `0x6E90` | 111 | UnwindData |  |
| 171 | `zelTracerCommandListAppendMemoryPrefetchRegisterCallback` | `0x6F00` | 111 | UnwindData |  |
| 172 | `zelTracerCommandListAppendMemoryRangesBarrierRegisterCallback` | `0x6F70` | 111 | UnwindData |  |
| 173 | `zelTracerCommandListAppendQueryKernelTimestampsRegisterCallback` | `0x6FE0` | 111 | UnwindData |  |
| 174 | `zelTracerCommandListAppendSignalEventRegisterCallback` | `0x7050` | 111 | UnwindData |  |
| 175 | `zelTracerCommandListAppendWaitOnEventsRegisterCallback` | `0x70C0` | 111 | UnwindData |  |
| 176 | `zelTracerCommandListAppendWriteGlobalTimestampRegisterCallback` | `0x7130` | 111 | UnwindData |  |
| 177 | `zelTracerCommandListCloseRegisterCallback` | `0x71A0` | 111 | UnwindData |  |
| 178 | `zelTracerCommandListCreateImmediateRegisterCallback` | `0x7210` | 111 | UnwindData |  |
| 179 | `zelTracerCommandListCreateRegisterCallback` | `0x7280` | 111 | UnwindData |  |
| 180 | `zelTracerCommandListDestroyRegisterCallback` | `0x72F0` | 111 | UnwindData |  |
| 181 | `zelTracerCommandListResetRegisterCallback` | `0x7360` | 111 | UnwindData |  |
| 182 | `zelTracerCommandQueueCreateRegisterCallback` | `0x73D0` | 111 | UnwindData |  |
| 183 | `zelTracerCommandQueueDestroyRegisterCallback` | `0x7440` | 111 | UnwindData |  |
| 184 | `zelTracerCommandQueueExecuteCommandListsRegisterCallback` | `0x74B0` | 111 | UnwindData |  |
| 185 | `zelTracerCommandQueueSynchronizeRegisterCallback` | `0x7520` | 111 | UnwindData |  |
| 186 | `zelTracerContextCreateExRegisterCallback` | `0x7590` | 111 | UnwindData |  |
| 187 | `zelTracerContextCreateRegisterCallback` | `0x7600` | 111 | UnwindData |  |
| 188 | `zelTracerContextDestroyRegisterCallback` | `0x7670` | 111 | UnwindData |  |
| 189 | `zelTracerContextEvictImageRegisterCallback` | `0x76E0` | 111 | UnwindData |  |
| 190 | `zelTracerContextEvictMemoryRegisterCallback` | `0x7750` | 111 | UnwindData |  |
| 191 | `zelTracerContextGetStatusRegisterCallback` | `0x77C0` | 111 | UnwindData |  |
| 192 | `zelTracerContextMakeImageResidentRegisterCallback` | `0x7830` | 111 | UnwindData |  |
| 193 | `zelTracerContextMakeMemoryResidentRegisterCallback` | `0x78A0` | 111 | UnwindData |  |
| 194 | `zelTracerContextSystemBarrierRegisterCallback` | `0x7910` | 111 | UnwindData |  |
| 197 | `zelTracerDeviceCanAccessPeerRegisterCallback` | `0x7980` | 111 | UnwindData |  |
| 198 | `zelTracerDeviceGetCachePropertiesRegisterCallback` | `0x79F0` | 111 | UnwindData |  |
| 199 | `zelTracerDeviceGetCommandQueueGroupPropertiesRegisterCallback` | `0x7A60` | 111 | UnwindData |  |
| 200 | `zelTracerDeviceGetComputePropertiesRegisterCallback` | `0x7AD0` | 111 | UnwindData |  |
| 201 | `zelTracerDeviceGetExternalMemoryPropertiesRegisterCallback` | `0x7B40` | 111 | UnwindData |  |
| 202 | `zelTracerDeviceGetGlobalTimestampsRegisterCallback` | `0x7BB0` | 111 | UnwindData |  |
| 203 | `zelTracerDeviceGetImagePropertiesRegisterCallback` | `0x7C20` | 111 | UnwindData |  |
| 204 | `zelTracerDeviceGetMemoryAccessPropertiesRegisterCallback` | `0x7C90` | 111 | UnwindData |  |
| 205 | `zelTracerDeviceGetMemoryPropertiesRegisterCallback` | `0x7D00` | 111 | UnwindData |  |
| 206 | `zelTracerDeviceGetModulePropertiesRegisterCallback` | `0x7D70` | 111 | UnwindData |  |
| 207 | `zelTracerDeviceGetP2PPropertiesRegisterCallback` | `0x7DE0` | 111 | UnwindData |  |
| 208 | `zelTracerDeviceGetPropertiesRegisterCallback` | `0x7E50` | 111 | UnwindData |  |
| 209 | `zelTracerDeviceGetRegisterCallback` | `0x7EC0` | 111 | UnwindData |  |
| 210 | `zelTracerDeviceGetStatusRegisterCallback` | `0x7F30` | 111 | UnwindData |  |
| 211 | `zelTracerDeviceGetSubDevicesRegisterCallback` | `0x7FA0` | 111 | UnwindData |  |
| 212 | `zelTracerDeviceReserveCacheExtRegisterCallback` | `0x8010` | 111 | UnwindData |  |
| 213 | `zelTracerDeviceSetCacheAdviceExtRegisterCallback` | `0x8080` | 111 | UnwindData |  |
| 214 | `zelTracerDriverGetApiVersionRegisterCallback` | `0x80F0` | 111 | UnwindData |  |
| 215 | `zelTracerDriverGetExtensionFunctionAddressRegisterCallback` | `0x8160` | 111 | UnwindData |  |
| 216 | `zelTracerDriverGetExtensionPropertiesRegisterCallback` | `0x81D0` | 111 | UnwindData |  |
| 217 | `zelTracerDriverGetIpcPropertiesRegisterCallback` | `0x8240` | 111 | UnwindData |  |
| 218 | `zelTracerDriverGetPropertiesRegisterCallback` | `0x82B0` | 111 | UnwindData |  |
| 219 | `zelTracerDriverGetRegisterCallback` | `0x8320` | 111 | UnwindData |  |
| 220 | `zelTracerEventCreateRegisterCallback` | `0x8390` | 111 | UnwindData |  |
| 221 | `zelTracerEventDestroyRegisterCallback` | `0x8400` | 111 | UnwindData |  |
| 222 | `zelTracerEventHostResetRegisterCallback` | `0x8470` | 111 | UnwindData |  |
| 223 | `zelTracerEventHostSignalRegisterCallback` | `0x84E0` | 111 | UnwindData |  |
| 224 | `zelTracerEventHostSynchronizeRegisterCallback` | `0x8550` | 111 | UnwindData |  |
| 225 | `zelTracerEventPoolCloseIpcHandleRegisterCallback` | `0x85C0` | 111 | UnwindData |  |
| 226 | `zelTracerEventPoolCreateRegisterCallback` | `0x8630` | 111 | UnwindData |  |
| 227 | `zelTracerEventPoolDestroyRegisterCallback` | `0x86A0` | 111 | UnwindData |  |
| 228 | `zelTracerEventPoolGetIpcHandleRegisterCallback` | `0x8710` | 111 | UnwindData |  |
| 229 | `zelTracerEventPoolOpenIpcHandleRegisterCallback` | `0x8780` | 111 | UnwindData |  |
| 230 | `zelTracerEventQueryKernelTimestampRegisterCallback` | `0x87F0` | 111 | UnwindData |  |
| 231 | `zelTracerEventQueryStatusRegisterCallback` | `0x8860` | 111 | UnwindData |  |
| 232 | `zelTracerEventQueryTimestampsExpRegisterCallback` | `0x88D0` | 111 | UnwindData |  |
| 233 | `zelTracerFenceCreateRegisterCallback` | `0x8940` | 111 | UnwindData |  |
| 234 | `zelTracerFenceDestroyRegisterCallback` | `0x89B0` | 111 | UnwindData |  |
| 235 | `zelTracerFenceHostSynchronizeRegisterCallback` | `0x8A20` | 111 | UnwindData |  |
| 236 | `zelTracerFenceQueryStatusRegisterCallback` | `0x8A90` | 111 | UnwindData |  |
| 237 | `zelTracerFenceResetRegisterCallback` | `0x8B00` | 111 | UnwindData |  |
| 238 | `zelTracerImageCreateRegisterCallback` | `0x8B70` | 111 | UnwindData |  |
| 239 | `zelTracerImageDestroyRegisterCallback` | `0x8BE0` | 111 | UnwindData |  |
| 240 | `zelTracerImageGetMemoryPropertiesExpRegisterCallback` | `0x8C50` | 111 | UnwindData |  |
| 241 | `zelTracerImageGetPropertiesRegisterCallback` | `0x8CC0` | 111 | UnwindData |  |
| 242 | `zelTracerImageViewCreateExpRegisterCallback` | `0x8D30` | 111 | UnwindData |  |
| 243 | `zelTracerInitRegisterCallback` | `0x8DA0` | 111 | UnwindData |  |
| 244 | `zelTracerKernelCreateRegisterCallback` | `0x8E10` | 111 | UnwindData |  |
| 245 | `zelTracerKernelDestroyRegisterCallback` | `0x8E80` | 111 | UnwindData |  |
| 246 | `zelTracerKernelGetIndirectAccessRegisterCallback` | `0x8EF0` | 111 | UnwindData |  |
| 247 | `zelTracerKernelGetNameRegisterCallback` | `0x8F60` | 111 | UnwindData |  |
| 248 | `zelTracerKernelGetPropertiesRegisterCallback` | `0x8FD0` | 111 | UnwindData |  |
| 249 | `zelTracerKernelGetSourceAttributesRegisterCallback` | `0x9040` | 111 | UnwindData |  |
| 250 | `zelTracerKernelSchedulingHintExpRegisterCallback` | `0x90B0` | 111 | UnwindData |  |
| 251 | `zelTracerKernelSetArgumentValueRegisterCallback` | `0x9120` | 111 | UnwindData |  |
| 252 | `zelTracerKernelSetCacheConfigRegisterCallback` | `0x9190` | 111 | UnwindData |  |
| 253 | `zelTracerKernelSetGlobalOffsetExpRegisterCallback` | `0x9200` | 111 | UnwindData |  |
| 254 | `zelTracerKernelSetGroupSizeRegisterCallback` | `0x9270` | 111 | UnwindData |  |
| 255 | `zelTracerKernelSetIndirectAccessRegisterCallback` | `0x92E0` | 111 | UnwindData |  |
| 256 | `zelTracerKernelSuggestGroupSizeRegisterCallback` | `0x9350` | 111 | UnwindData |  |
| 257 | `zelTracerKernelSuggestMaxCooperativeGroupCountRegisterCallback` | `0x93C0` | 111 | UnwindData |  |
| 258 | `zelTracerMemAllocDeviceRegisterCallback` | `0x9430` | 111 | UnwindData |  |
| 259 | `zelTracerMemAllocHostRegisterCallback` | `0x94A0` | 111 | UnwindData |  |
| 260 | `zelTracerMemAllocSharedRegisterCallback` | `0x9510` | 111 | UnwindData |  |
| 261 | `zelTracerMemCloseIpcHandleRegisterCallback` | `0x9580` | 111 | UnwindData |  |
| 262 | `zelTracerMemFreeRegisterCallback` | `0x95F0` | 111 | UnwindData |  |
| 263 | `zelTracerMemGetAddressRangeRegisterCallback` | `0x9660` | 111 | UnwindData |  |
| 264 | `zelTracerMemGetAllocPropertiesRegisterCallback` | `0x96D0` | 111 | UnwindData |  |
| 265 | `zelTracerMemGetIpcHandleRegisterCallback` | `0x9740` | 111 | UnwindData |  |
| 266 | `zelTracerMemOpenIpcHandleRegisterCallback` | `0x97B0` | 111 | UnwindData |  |
| 267 | `zelTracerModuleBuildLogDestroyRegisterCallback` | `0x9820` | 111 | UnwindData |  |
| 268 | `zelTracerModuleBuildLogGetStringRegisterCallback` | `0x9890` | 111 | UnwindData |  |
| 269 | `zelTracerModuleCreateRegisterCallback` | `0x9900` | 111 | UnwindData |  |
| 270 | `zelTracerModuleDestroyRegisterCallback` | `0x9970` | 111 | UnwindData |  |
| 271 | `zelTracerModuleDynamicLinkRegisterCallback` | `0x99E0` | 111 | UnwindData |  |
| 272 | `zelTracerModuleGetFunctionPointerRegisterCallback` | `0x9A50` | 111 | UnwindData |  |
| 273 | `zelTracerModuleGetGlobalPointerRegisterCallback` | `0x9AC0` | 111 | UnwindData |  |
| 274 | `zelTracerModuleGetKernelNamesRegisterCallback` | `0x9B30` | 111 | UnwindData |  |
| 275 | `zelTracerModuleGetNativeBinaryRegisterCallback` | `0x9BA0` | 111 | UnwindData |  |
| 276 | `zelTracerModuleGetPropertiesRegisterCallback` | `0x9C10` | 111 | UnwindData |  |
| 277 | `zelTracerPhysicalMemCreateRegisterCallback` | `0x9C80` | 111 | UnwindData |  |
| 278 | `zelTracerPhysicalMemDestroyRegisterCallback` | `0x9CF0` | 111 | UnwindData |  |
| 279 | `zelTracerSamplerCreateRegisterCallback` | `0x9D60` | 111 | UnwindData |  |
| 280 | `zelTracerSamplerDestroyRegisterCallback` | `0x9DD0` | 111 | UnwindData |  |
| 284 | `zelTracerVirtualMemFreeRegisterCallback` | `0x9E40` | 111 | UnwindData |  |
| 285 | `zelTracerVirtualMemGetAccessAttributeRegisterCallback` | `0x9EB0` | 111 | UnwindData |  |
| 286 | `zelTracerVirtualMemMapRegisterCallback` | `0x9F20` | 111 | UnwindData |  |
| 287 | `zelTracerVirtualMemQueryPageSizeRegisterCallback` | `0x9F90` | 111 | UnwindData |  |
| 288 | `zelTracerVirtualMemReserveRegisterCallback` | `0xA000` | 111 | UnwindData |  |
| 289 | `zelTracerVirtualMemSetAccessAttributeRegisterCallback` | `0xA070` | 111 | UnwindData |  |
| 290 | `zelTracerVirtualMemUnmapRegisterCallback` | `0xA0E0` | 111 | UnwindData |  |
| 121 | `zeLoaderGetTracingHandle` | `0xB630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `zeLoaderInit` | `0xB640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `zelLoaderGetVersionsInternal` | `0xB650` | 141 | UnwindData |  |
| 81 | `zeGetCommandListProcAddrTable` | `0xF900` | 904 | UnwindData |  |
| 82 | `zeGetCommandQueueProcAddrTable` | `0xFC90` | 514 | UnwindData |  |
| 83 | `zeGetContextProcAddrTable` | `0xFEA0` | 607 | UnwindData |  |
| 84 | `zeGetDeviceProcAddrTable` | `0x10100` | 737 | UnwindData |  |
| 85 | `zeGetDriverProcAddrTable` | `0x103F0` | 536 | UnwindData |  |
| 86 | `zeGetEventExpProcAddrTable` | `0x10610` | 101 | UnwindData |  |
| 87 | `zeGetEventPoolProcAddrTable` | `0x107C0` | 539 | UnwindData |  |
| 88 | `zeGetEventProcAddrTable` | `0x109E0` | 573 | UnwindData |  |
| 89 | `zeGetFenceProcAddrTable` | `0x10C20` | 539 | UnwindData |  |
| 90 | `zeGetGlobalProcAddrTable` | `0x10E40` | 456 | UnwindData |  |
| 91 | `zeGetImageExpProcAddrTable` | `0x11010` | 98 | UnwindData |  |
| 92 | `zeGetImageProcAddrTable` | `0x111D0` | 505 | UnwindData |  |
| 93 | `zeGetKernelExpProcAddrTable` | `0x113D0` | 98 | UnwindData |  |
| 94 | `zeGetKernelProcAddrTable` | `0x11590` | 653 | UnwindData |  |
| 95 | `zeGetMemProcAddrTable` | `0x11820` | 607 | UnwindData |  |
| 96 | `zeGetModuleBuildLogProcAddrTable` | `0x11A80` | 478 | UnwindData |  |
| 97 | `zeGetModuleProcAddrTable` | `0x11C60` | 582 | UnwindData |  |
| 98 | `zeGetPhysicalMemProcAddrTable` | `0x11EB0` | 478 | UnwindData |  |
| 99 | `zeGetSamplerProcAddrTable` | `0x12090` | 478 | UnwindData |  |
| 100 | `zeGetVirtualMemProcAddrTable` | `0x12270` | 573 | UnwindData |  |
| 424 | `zetGetCommandListProcAddrTable` | `0x13050` | 458 | UnwindData |  |
| 425 | `zetGetContextProcAddrTable` | `0x13220` | 407 | UnwindData |  |
| 426 | `zetGetDebugProcAddrTable` | `0x133C0` | 585 | UnwindData |  |
| 427 | `zetGetDeviceProcAddrTable` | `0x13610` | 407 | UnwindData |  |
| 428 | `zetGetKernelProcAddrTable` | `0x137B0` | 407 | UnwindData |  |
| 429 | `zetGetMetricGroupExpProcAddrTable` | `0x13950` | 101 | UnwindData |  |
| 430 | `zetGetMetricGroupProcAddrTable` | `0x13AD0` | 449 | UnwindData |  |
| 431 | `zetGetMetricProcAddrTable` | `0x13CA0` | 423 | UnwindData |  |
| 432 | `zetGetMetricQueryPoolProcAddrTable` | `0x13E50` | 423 | UnwindData |  |
| 433 | `zetGetMetricQueryProcAddrTable` | `0x14000` | 458 | UnwindData |  |
| 434 | `zetGetMetricStreamerProcAddrTable` | `0x141D0` | 449 | UnwindData |  |
| 435 | `zetGetModuleProcAddrTable` | `0x143A0` | 407 | UnwindData |  |
| 436 | `zetGetTracerExpProcAddrTable` | `0x14540` | 483 | UnwindData |  |
| 353 | `zesGetDeviceProcAddrTable` | `0x15CE0` | 815 | UnwindData |  |
| 354 | `zesGetDiagnosticsProcAddrTable` | `0x16010` | 449 | UnwindData |  |
| 355 | `zesGetDriverProcAddrTable` | `0x161E0` | 423 | UnwindData |  |
| 356 | `zesGetEngineProcAddrTable` | `0x16390` | 423 | UnwindData |  |
| 357 | `zesGetFabricPortProcAddrTable` | `0x16540` | 492 | UnwindData |  |
| 358 | `zesGetFanProcAddrTable` | `0x16730` | 492 | UnwindData |  |
| 359 | `zesGetFirmwareProcAddrTable` | `0x16920` | 423 | UnwindData |  |
| 360 | `zesGetFrequencyProcAddrTable` | `0x16AD0` | 696 | UnwindData |  |
| 361 | `zesGetLedProcAddrTable` | `0x16D90` | 458 | UnwindData |  |
| 362 | `zesGetMemoryProcAddrTable` | `0x16F60` | 449 | UnwindData |  |
| 363 | `zesGetPerformanceFactorProcAddrTable` | `0x17130` | 449 | UnwindData |  |
| 364 | `zesGetPowerProcAddrTable` | `0x17300` | 492 | UnwindData |  |
| 365 | `zesGetPsuProcAddrTable` | `0x174F0` | 423 | UnwindData |  |
| 366 | `zesGetRasProcAddrTable` | `0x176A0` | 458 | UnwindData |  |
| 367 | `zesGetSchedulerProcAddrTable` | `0x17870` | 526 | UnwindData |  |
| 368 | `zesGetStandbyProcAddrTable` | `0x17A80` | 449 | UnwindData |  |
| 369 | `zesGetTemperatureProcAddrTable` | `0x17C50` | 458 | UnwindData |  |
| 153 | `zelGetTracerApiProcAddrTable` | `0x17E20` | 178 | UnwindData |  |
