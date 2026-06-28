# Binary Specification: ze_tracing_layer.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_1973c0a49e1f4f8c\ze_tracing_layer.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d1f8541bf3d95801b9e5d323dc0cae759fec5640748e908abc30724e69683d0a`
* **Total Exported Functions:** 157

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `zeGetCommandListProcAddrTable` | `0x218D0` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `zeGetCommandQueueProcAddrTable` | `0x21B80` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `zeGetContextProcAddrTable` | `0x21C10` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `zeGetDeviceProcAddrTable` | `0x21D10` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `zeGetDriverProcAddrTable` | `0x21ED0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `zeGetEventExpProcAddrTable` | `0x21F90` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `zeGetEventPoolProcAddrTable` | `0x21FE0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `zeGetEventProcAddrTable` | `0x22080` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `zeGetFenceProcAddrTable` | `0x22150` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `zeGetGlobalProcAddrTable` | `0x221F0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `zeGetImageExpProcAddrTable` | `0x22240` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `zeGetImageProcAddrTable` | `0x222A0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `zeGetKernelExpProcAddrTable` | `0x22310` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `zeGetKernelProcAddrTable` | `0x22370` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `zeGetMemProcAddrTable` | `0x224B0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `zeGetModuleBuildLogProcAddrTable` | `0x225B0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `zeGetModuleProcAddrTable` | `0x22610` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `zeGetPhysicalMemProcAddrTable` | `0x22700` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `zeGetSamplerProcAddrTable` | `0x22760` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `zeGetVirtualMemProcAddrTable` | `0x227C0` | 22,768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `zelGetTracerApiProcAddrTable` | `0x280B0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `zelLoaderGetVersion` | `0x28110` | 73 | UnwindData |  |
| 62 | `zelTracerCreate` | `0x28160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `zelTracerDestroy` | `0x28170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 148 | `zelTracerSetEnabled` | `0x28190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `zelTracerSetEpilogues` | `0x281B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `zelTracerSetPrologues` | `0x281D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `zelTracerCommandListAppendBarrierRegisterCallback` | `0x281F0` | 71 | UnwindData |  |
| 24 | `zelTracerCommandListAppendEventResetRegisterCallback` | `0x28240` | 71 | UnwindData |  |
| 25 | `zelTracerCommandListAppendImageCopyFromMemoryRegisterCallback` | `0x28290` | 71 | UnwindData |  |
| 26 | `zelTracerCommandListAppendImageCopyRegionRegisterCallback` | `0x282E0` | 71 | UnwindData |  |
| 27 | `zelTracerCommandListAppendImageCopyRegisterCallback` | `0x28330` | 71 | UnwindData |  |
| 28 | `zelTracerCommandListAppendImageCopyToMemoryRegisterCallback` | `0x28380` | 71 | UnwindData |  |
| 29 | `zelTracerCommandListAppendLaunchCooperativeKernelRegisterCallback` | `0x283D0` | 71 | UnwindData |  |
| 30 | `zelTracerCommandListAppendLaunchKernelIndirectRegisterCallback` | `0x28420` | 71 | UnwindData |  |
| 31 | `zelTracerCommandListAppendLaunchKernelRegisterCallback` | `0x28470` | 71 | UnwindData |  |
| 32 | `zelTracerCommandListAppendLaunchMultipleKernelsIndirectRegisterCallback` | `0x284C0` | 71 | UnwindData |  |
| 33 | `zelTracerCommandListAppendMemAdviseRegisterCallback` | `0x28510` | 71 | UnwindData |  |
| 34 | `zelTracerCommandListAppendMemoryCopyFromContextRegisterCallback` | `0x28560` | 71 | UnwindData |  |
| 35 | `zelTracerCommandListAppendMemoryCopyRegionRegisterCallback` | `0x285B0` | 71 | UnwindData |  |
| 36 | `zelTracerCommandListAppendMemoryCopyRegisterCallback` | `0x28600` | 71 | UnwindData |  |
| 37 | `zelTracerCommandListAppendMemoryFillRegisterCallback` | `0x28650` | 71 | UnwindData |  |
| 38 | `zelTracerCommandListAppendMemoryPrefetchRegisterCallback` | `0x286A0` | 71 | UnwindData |  |
| 39 | `zelTracerCommandListAppendMemoryRangesBarrierRegisterCallback` | `0x286F0` | 71 | UnwindData |  |
| 40 | `zelTracerCommandListAppendQueryKernelTimestampsRegisterCallback` | `0x28740` | 71 | UnwindData |  |
| 41 | `zelTracerCommandListAppendSignalEventRegisterCallback` | `0x28790` | 71 | UnwindData |  |
| 42 | `zelTracerCommandListAppendWaitOnEventsRegisterCallback` | `0x287E0` | 71 | UnwindData |  |
| 43 | `zelTracerCommandListAppendWriteGlobalTimestampRegisterCallback` | `0x28830` | 71 | UnwindData |  |
| 44 | `zelTracerCommandListCloseRegisterCallback` | `0x28880` | 71 | UnwindData |  |
| 45 | `zelTracerCommandListCreateImmediateRegisterCallback` | `0x288D0` | 71 | UnwindData |  |
| 46 | `zelTracerCommandListCreateRegisterCallback` | `0x28920` | 71 | UnwindData |  |
| 47 | `zelTracerCommandListDestroyRegisterCallback` | `0x28970` | 71 | UnwindData |  |
| 48 | `zelTracerCommandListResetRegisterCallback` | `0x289C0` | 71 | UnwindData |  |
| 49 | `zelTracerCommandQueueCreateRegisterCallback` | `0x28A10` | 71 | UnwindData |  |
| 50 | `zelTracerCommandQueueDestroyRegisterCallback` | `0x28A60` | 71 | UnwindData |  |
| 51 | `zelTracerCommandQueueExecuteCommandListsRegisterCallback` | `0x28AB0` | 71 | UnwindData |  |
| 52 | `zelTracerCommandQueueSynchronizeRegisterCallback` | `0x28B00` | 71 | UnwindData |  |
| 53 | `zelTracerContextCreateExRegisterCallback` | `0x28B50` | 71 | UnwindData |  |
| 54 | `zelTracerContextCreateRegisterCallback` | `0x28BA0` | 71 | UnwindData |  |
| 55 | `zelTracerContextDestroyRegisterCallback` | `0x28BF0` | 71 | UnwindData |  |
| 56 | `zelTracerContextEvictImageRegisterCallback` | `0x28C40` | 71 | UnwindData |  |
| 57 | `zelTracerContextEvictMemoryRegisterCallback` | `0x28C90` | 71 | UnwindData |  |
| 58 | `zelTracerContextGetStatusRegisterCallback` | `0x28CE0` | 71 | UnwindData |  |
| 59 | `zelTracerContextMakeImageResidentRegisterCallback` | `0x28D30` | 71 | UnwindData |  |
| 60 | `zelTracerContextMakeMemoryResidentRegisterCallback` | `0x28D80` | 71 | UnwindData |  |
| 61 | `zelTracerContextSystemBarrierRegisterCallback` | `0x28DD0` | 71 | UnwindData |  |
| 64 | `zelTracerDeviceCanAccessPeerRegisterCallback` | `0x28E20` | 71 | UnwindData |  |
| 65 | `zelTracerDeviceGetCachePropertiesRegisterCallback` | `0x28E70` | 68 | UnwindData |  |
| 66 | `zelTracerDeviceGetCommandQueueGroupPropertiesRegisterCallback` | `0x28EC0` | 68 | UnwindData |  |
| 67 | `zelTracerDeviceGetComputePropertiesRegisterCallback` | `0x28F10` | 68 | UnwindData |  |
| 68 | `zelTracerDeviceGetExternalMemoryPropertiesRegisterCallback` | `0x28F60` | 71 | UnwindData |  |
| 69 | `zelTracerDeviceGetGlobalTimestampsRegisterCallback` | `0x28FB0` | 71 | UnwindData |  |
| 70 | `zelTracerDeviceGetImagePropertiesRegisterCallback` | `0x29000` | 71 | UnwindData |  |
| 71 | `zelTracerDeviceGetMemoryAccessPropertiesRegisterCallback` | `0x29050` | 68 | UnwindData |  |
| 72 | `zelTracerDeviceGetMemoryPropertiesRegisterCallback` | `0x290A0` | 68 | UnwindData |  |
| 73 | `zelTracerDeviceGetModulePropertiesRegisterCallback` | `0x290F0` | 68 | UnwindData |  |
| 74 | `zelTracerDeviceGetP2PPropertiesRegisterCallback` | `0x29140` | 71 | UnwindData |  |
| 75 | `zelTracerDeviceGetPropertiesRegisterCallback` | `0x29190` | 68 | UnwindData |  |
| 76 | `zelTracerDeviceGetRegisterCallback` | `0x291E0` | 68 | UnwindData |  |
| 77 | `zelTracerDeviceGetStatusRegisterCallback` | `0x29230` | 71 | UnwindData |  |
| 78 | `zelTracerDeviceGetSubDevicesRegisterCallback` | `0x29280` | 68 | UnwindData |  |
| 79 | `zelTracerDeviceReserveCacheExtRegisterCallback` | `0x292D0` | 71 | UnwindData |  |
| 80 | `zelTracerDeviceSetCacheAdviceExtRegisterCallback` | `0x29320` | 71 | UnwindData |  |
| 81 | `zelTracerDriverGetApiVersionRegisterCallback` | `0x29370` | 68 | UnwindData |  |
| 82 | `zelTracerDriverGetExtensionFunctionAddressRegisterCallback` | `0x293C0` | 68 | UnwindData |  |
| 83 | `zelTracerDriverGetExtensionPropertiesRegisterCallback` | `0x29410` | 68 | UnwindData |  |
| 84 | `zelTracerDriverGetIpcPropertiesRegisterCallback` | `0x29460` | 68 | UnwindData |  |
| 85 | `zelTracerDriverGetPropertiesRegisterCallback` | `0x294B0` | 68 | UnwindData |  |
| 86 | `zelTracerDriverGetRegisterCallback` | `0x29500` | 68 | UnwindData |  |
| 87 | `zelTracerEventCreateRegisterCallback` | `0x29550` | 71 | UnwindData |  |
| 88 | `zelTracerEventDestroyRegisterCallback` | `0x295A0` | 71 | UnwindData |  |
| 89 | `zelTracerEventHostResetRegisterCallback` | `0x295F0` | 71 | UnwindData |  |
| 90 | `zelTracerEventHostSignalRegisterCallback` | `0x29640` | 71 | UnwindData |  |
| 91 | `zelTracerEventHostSynchronizeRegisterCallback` | `0x29690` | 71 | UnwindData |  |
| 92 | `zelTracerEventPoolCloseIpcHandleRegisterCallback` | `0x296E0` | 71 | UnwindData |  |
| 93 | `zelTracerEventPoolCreateRegisterCallback` | `0x29730` | 71 | UnwindData |  |
| 94 | `zelTracerEventPoolDestroyRegisterCallback` | `0x29780` | 71 | UnwindData |  |
| 95 | `zelTracerEventPoolGetIpcHandleRegisterCallback` | `0x297D0` | 71 | UnwindData |  |
| 96 | `zelTracerEventPoolOpenIpcHandleRegisterCallback` | `0x29820` | 71 | UnwindData |  |
| 97 | `zelTracerEventQueryKernelTimestampRegisterCallback` | `0x29870` | 71 | UnwindData |  |
| 98 | `zelTracerEventQueryStatusRegisterCallback` | `0x298C0` | 71 | UnwindData |  |
| 99 | `zelTracerEventQueryTimestampsExpRegisterCallback` | `0x29910` | 71 | UnwindData |  |
| 100 | `zelTracerFenceCreateRegisterCallback` | `0x29960` | 71 | UnwindData |  |
| 101 | `zelTracerFenceDestroyRegisterCallback` | `0x299B0` | 71 | UnwindData |  |
| 102 | `zelTracerFenceHostSynchronizeRegisterCallback` | `0x29A00` | 71 | UnwindData |  |
| 103 | `zelTracerFenceQueryStatusRegisterCallback` | `0x29A50` | 71 | UnwindData |  |
| 104 | `zelTracerFenceResetRegisterCallback` | `0x29AA0` | 71 | UnwindData |  |
| 105 | `zelTracerImageCreateRegisterCallback` | `0x29AF0` | 71 | UnwindData |  |
| 106 | `zelTracerImageDestroyRegisterCallback` | `0x29B40` | 71 | UnwindData |  |
| 107 | `zelTracerImageGetMemoryPropertiesExpRegisterCallback` | `0x29B90` | 71 | UnwindData |  |
| 108 | `zelTracerImageGetPropertiesRegisterCallback` | `0x29BE0` | 71 | UnwindData |  |
| 109 | `zelTracerImageViewCreateExpRegisterCallback` | `0x29C30` | 71 | UnwindData |  |
| 110 | `zelTracerInitRegisterCallback` | `0x29C80` | 67 | UnwindData |  |
| 111 | `zelTracerKernelCreateRegisterCallback` | `0x29CD0` | 71 | UnwindData |  |
| 112 | `zelTracerKernelDestroyRegisterCallback` | `0x29D20` | 71 | UnwindData |  |
| 113 | `zelTracerKernelGetIndirectAccessRegisterCallback` | `0x29D70` | 71 | UnwindData |  |
| 114 | `zelTracerKernelGetNameRegisterCallback` | `0x29DC0` | 71 | UnwindData |  |
| 115 | `zelTracerKernelGetPropertiesRegisterCallback` | `0x29E10` | 71 | UnwindData |  |
| 116 | `zelTracerKernelGetSourceAttributesRegisterCallback` | `0x29E60` | 71 | UnwindData |  |
| 117 | `zelTracerKernelSchedulingHintExpRegisterCallback` | `0x29EB0` | 71 | UnwindData |  |
| 118 | `zelTracerKernelSetArgumentValueRegisterCallback` | `0x29F00` | 71 | UnwindData |  |
| 119 | `zelTracerKernelSetCacheConfigRegisterCallback` | `0x29F50` | 71 | UnwindData |  |
| 120 | `zelTracerKernelSetGlobalOffsetExpRegisterCallback` | `0x29FA0` | 71 | UnwindData |  |
| 121 | `zelTracerKernelSetGroupSizeRegisterCallback` | `0x29FF0` | 71 | UnwindData |  |
| 122 | `zelTracerKernelSetIndirectAccessRegisterCallback` | `0x2A040` | 71 | UnwindData |  |
| 123 | `zelTracerKernelSuggestGroupSizeRegisterCallback` | `0x2A090` | 71 | UnwindData |  |
| 124 | `zelTracerKernelSuggestMaxCooperativeGroupCountRegisterCallback` | `0x2A0E0` | 71 | UnwindData |  |
| 125 | `zelTracerMemAllocDeviceRegisterCallback` | `0x2A130` | 71 | UnwindData |  |
| 126 | `zelTracerMemAllocHostRegisterCallback` | `0x2A180` | 71 | UnwindData |  |
| 127 | `zelTracerMemAllocSharedRegisterCallback` | `0x2A1D0` | 71 | UnwindData |  |
| 128 | `zelTracerMemCloseIpcHandleRegisterCallback` | `0x2A220` | 71 | UnwindData |  |
| 129 | `zelTracerMemFreeRegisterCallback` | `0x2A270` | 71 | UnwindData |  |
| 130 | `zelTracerMemGetAddressRangeRegisterCallback` | `0x2A2C0` | 71 | UnwindData |  |
| 131 | `zelTracerMemGetAllocPropertiesRegisterCallback` | `0x2A310` | 71 | UnwindData |  |
| 132 | `zelTracerMemGetIpcHandleRegisterCallback` | `0x2A360` | 71 | UnwindData |  |
| 133 | `zelTracerMemOpenIpcHandleRegisterCallback` | `0x2A3B0` | 71 | UnwindData |  |
| 134 | `zelTracerModuleBuildLogDestroyRegisterCallback` | `0x2A400` | 71 | UnwindData |  |
| 135 | `zelTracerModuleBuildLogGetStringRegisterCallback` | `0x2A450` | 71 | UnwindData |  |
| 136 | `zelTracerModuleCreateRegisterCallback` | `0x2A4A0` | 71 | UnwindData |  |
| 137 | `zelTracerModuleDestroyRegisterCallback` | `0x2A4F0` | 71 | UnwindData |  |
| 138 | `zelTracerModuleDynamicLinkRegisterCallback` | `0x2A540` | 71 | UnwindData |  |
| 139 | `zelTracerModuleGetFunctionPointerRegisterCallback` | `0x2A590` | 71 | UnwindData |  |
| 140 | `zelTracerModuleGetGlobalPointerRegisterCallback` | `0x2A5E0` | 71 | UnwindData |  |
| 141 | `zelTracerModuleGetKernelNamesRegisterCallback` | `0x2A630` | 71 | UnwindData |  |
| 142 | `zelTracerModuleGetNativeBinaryRegisterCallback` | `0x2A680` | 71 | UnwindData |  |
| 143 | `zelTracerModuleGetPropertiesRegisterCallback` | `0x2A6D0` | 71 | UnwindData |  |
| 144 | `zelTracerPhysicalMemCreateRegisterCallback` | `0x2A720` | 71 | UnwindData |  |
| 145 | `zelTracerPhysicalMemDestroyRegisterCallback` | `0x2A770` | 71 | UnwindData |  |
| 146 | `zelTracerSamplerCreateRegisterCallback` | `0x2A7C0` | 71 | UnwindData |  |
| 147 | `zelTracerSamplerDestroyRegisterCallback` | `0x2A810` | 71 | UnwindData |  |
| 151 | `zelTracerVirtualMemFreeRegisterCallback` | `0x2A860` | 71 | UnwindData |  |
| 152 | `zelTracerVirtualMemGetAccessAttributeRegisterCallback` | `0x2A8B0` | 71 | UnwindData |  |
| 153 | `zelTracerVirtualMemMapRegisterCallback` | `0x2A900` | 71 | UnwindData |  |
| 154 | `zelTracerVirtualMemQueryPageSizeRegisterCallback` | `0x2A950` | 71 | UnwindData |  |
| 155 | `zelTracerVirtualMemReserveRegisterCallback` | `0x2A9A0` | 71 | UnwindData |  |
| 156 | `zelTracerVirtualMemSetAccessAttributeRegisterCallback` | `0x2A9F0` | 71 | UnwindData |  |
| 157 | `zelTracerVirtualMemUnmapRegisterCallback` | `0x2AA40` | 71 | UnwindData |  |
