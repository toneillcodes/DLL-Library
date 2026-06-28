# Binary Specification: ze_tracing_layer.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ze_tracing_layer.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `536677fe4be0b56343b17e3bfb04bd4a136e53cf2e9d22cbf69c0360a360f1cd`
* **Total Exported Functions:** 163

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `zeGetCommandListProcAddrTable` | `0x253F0` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `zeGetCommandQueueProcAddrTable` | `0x256E0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `zeGetContextProcAddrTable` | `0x25770` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `zeGetDeviceProcAddrTable` | `0x25870` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `zeGetDriverProcAddrTable` | `0x25A40` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `zeGetEventExpProcAddrTable` | `0x25B00` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `zeGetEventPoolProcAddrTable` | `0x25B50` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `zeGetEventProcAddrTable` | `0x25BF0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `zeGetFenceProcAddrTable` | `0x25CC0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `zeGetGlobalProcAddrTable` | `0x25D60` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `zeGetImageExpProcAddrTable` | `0x25DB0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `zeGetImageProcAddrTable` | `0x25E10` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `zeGetKernelExpProcAddrTable` | `0x25EA0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `zeGetKernelProcAddrTable` | `0x25F00` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `zeGetMemProcAddrTable` | `0x26040` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `zeGetModuleBuildLogProcAddrTable` | `0x26160` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `zeGetModuleProcAddrTable` | `0x261C0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `zeGetPhysicalMemProcAddrTable` | `0x262C0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `zeGetSamplerProcAddrTable` | `0x26320` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `zeGetVirtualMemProcAddrTable` | `0x26380` | 22,672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `zelGetTracerApiProcAddrTable` | `0x2BC10` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `zelLoaderGetVersion` | `0x2BC70` | 82 | UnwindData |  |
| 64 | `zelTracerCreate` | `0x2BCD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `zelTracerDestroy` | `0x2BCE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `zelTracerSetEnabled` | `0x2BD00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `zelTracerSetEpilogues` | `0x2BD20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `zelTracerSetPrologues` | `0x2BD40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `zelTracerCommandListAppendBarrierRegisterCallback` | `0x2BD60` | 71 | UnwindData |  |
| 24 | `zelTracerCommandListAppendEventResetRegisterCallback` | `0x2BDB0` | 71 | UnwindData |  |
| 25 | `zelTracerCommandListAppendImageCopyFromMemoryExtRegisterCallback` | `0x2BE00` | 71 | UnwindData |  |
| 26 | `zelTracerCommandListAppendImageCopyFromMemoryRegisterCallback` | `0x2BE50` | 71 | UnwindData |  |
| 27 | `zelTracerCommandListAppendImageCopyRegionRegisterCallback` | `0x2BEA0` | 71 | UnwindData |  |
| 28 | `zelTracerCommandListAppendImageCopyRegisterCallback` | `0x2BEF0` | 71 | UnwindData |  |
| 29 | `zelTracerCommandListAppendImageCopyToMemoryExtRegisterCallback` | `0x2BF40` | 71 | UnwindData |  |
| 30 | `zelTracerCommandListAppendImageCopyToMemoryRegisterCallback` | `0x2BF90` | 71 | UnwindData |  |
| 31 | `zelTracerCommandListAppendLaunchCooperativeKernelRegisterCallback` | `0x2BFE0` | 71 | UnwindData |  |
| 32 | `zelTracerCommandListAppendLaunchKernelIndirectRegisterCallback` | `0x2C030` | 71 | UnwindData |  |
| 33 | `zelTracerCommandListAppendLaunchKernelRegisterCallback` | `0x2C080` | 71 | UnwindData |  |
| 34 | `zelTracerCommandListAppendLaunchMultipleKernelsIndirectRegisterCallback` | `0x2C0D0` | 71 | UnwindData |  |
| 35 | `zelTracerCommandListAppendMemAdviseRegisterCallback` | `0x2C120` | 71 | UnwindData |  |
| 36 | `zelTracerCommandListAppendMemoryCopyFromContextRegisterCallback` | `0x2C170` | 71 | UnwindData |  |
| 37 | `zelTracerCommandListAppendMemoryCopyRegionRegisterCallback` | `0x2C1C0` | 71 | UnwindData |  |
| 38 | `zelTracerCommandListAppendMemoryCopyRegisterCallback` | `0x2C210` | 71 | UnwindData |  |
| 39 | `zelTracerCommandListAppendMemoryFillRegisterCallback` | `0x2C260` | 71 | UnwindData |  |
| 40 | `zelTracerCommandListAppendMemoryPrefetchRegisterCallback` | `0x2C2B0` | 71 | UnwindData |  |
| 41 | `zelTracerCommandListAppendMemoryRangesBarrierRegisterCallback` | `0x2C300` | 71 | UnwindData |  |
| 42 | `zelTracerCommandListAppendQueryKernelTimestampsRegisterCallback` | `0x2C350` | 71 | UnwindData |  |
| 43 | `zelTracerCommandListAppendSignalEventRegisterCallback` | `0x2C3A0` | 71 | UnwindData |  |
| 44 | `zelTracerCommandListAppendWaitOnEventsRegisterCallback` | `0x2C3F0` | 71 | UnwindData |  |
| 45 | `zelTracerCommandListAppendWriteGlobalTimestampRegisterCallback` | `0x2C440` | 71 | UnwindData |  |
| 46 | `zelTracerCommandListCloseRegisterCallback` | `0x2C490` | 71 | UnwindData |  |
| 47 | `zelTracerCommandListCreateImmediateRegisterCallback` | `0x2C4E0` | 71 | UnwindData |  |
| 48 | `zelTracerCommandListCreateRegisterCallback` | `0x2C530` | 71 | UnwindData |  |
| 49 | `zelTracerCommandListDestroyRegisterCallback` | `0x2C580` | 71 | UnwindData |  |
| 50 | `zelTracerCommandListResetRegisterCallback` | `0x2C5D0` | 71 | UnwindData |  |
| 51 | `zelTracerCommandQueueCreateRegisterCallback` | `0x2C620` | 71 | UnwindData |  |
| 52 | `zelTracerCommandQueueDestroyRegisterCallback` | `0x2C670` | 71 | UnwindData |  |
| 53 | `zelTracerCommandQueueExecuteCommandListsRegisterCallback` | `0x2C6C0` | 71 | UnwindData |  |
| 54 | `zelTracerCommandQueueSynchronizeRegisterCallback` | `0x2C710` | 71 | UnwindData |  |
| 55 | `zelTracerContextCreateExRegisterCallback` | `0x2C760` | 71 | UnwindData |  |
| 56 | `zelTracerContextCreateRegisterCallback` | `0x2C7B0` | 71 | UnwindData |  |
| 57 | `zelTracerContextDestroyRegisterCallback` | `0x2C800` | 71 | UnwindData |  |
| 58 | `zelTracerContextEvictImageRegisterCallback` | `0x2C850` | 71 | UnwindData |  |
| 59 | `zelTracerContextEvictMemoryRegisterCallback` | `0x2C8A0` | 71 | UnwindData |  |
| 60 | `zelTracerContextGetStatusRegisterCallback` | `0x2C8F0` | 71 | UnwindData |  |
| 61 | `zelTracerContextMakeImageResidentRegisterCallback` | `0x2C940` | 71 | UnwindData |  |
| 62 | `zelTracerContextMakeMemoryResidentRegisterCallback` | `0x2C990` | 71 | UnwindData |  |
| 63 | `zelTracerContextSystemBarrierRegisterCallback` | `0x2C9E0` | 71 | UnwindData |  |
| 66 | `zelTracerDeviceCanAccessPeerRegisterCallback` | `0x2CA30` | 71 | UnwindData |  |
| 67 | `zelTracerDeviceGetCachePropertiesRegisterCallback` | `0x2CA80` | 68 | UnwindData |  |
| 68 | `zelTracerDeviceGetCommandQueueGroupPropertiesRegisterCallback` | `0x2CAD0` | 68 | UnwindData |  |
| 69 | `zelTracerDeviceGetComputePropertiesRegisterCallback` | `0x2CB20` | 68 | UnwindData |  |
| 70 | `zelTracerDeviceGetExternalMemoryPropertiesRegisterCallback` | `0x2CB70` | 71 | UnwindData |  |
| 71 | `zelTracerDeviceGetGlobalTimestampsRegisterCallback` | `0x2CBC0` | 71 | UnwindData |  |
| 72 | `zelTracerDeviceGetImagePropertiesRegisterCallback` | `0x2CC10` | 71 | UnwindData |  |
| 73 | `zelTracerDeviceGetMemoryAccessPropertiesRegisterCallback` | `0x2CC60` | 68 | UnwindData |  |
| 74 | `zelTracerDeviceGetMemoryPropertiesRegisterCallback` | `0x2CCB0` | 68 | UnwindData |  |
| 75 | `zelTracerDeviceGetModulePropertiesRegisterCallback` | `0x2CD00` | 68 | UnwindData |  |
| 76 | `zelTracerDeviceGetP2PPropertiesRegisterCallback` | `0x2CD50` | 71 | UnwindData |  |
| 77 | `zelTracerDeviceGetPropertiesRegisterCallback` | `0x2CDA0` | 68 | UnwindData |  |
| 78 | `zelTracerDeviceGetRegisterCallback` | `0x2CDF0` | 68 | UnwindData |  |
| 79 | `zelTracerDeviceGetStatusRegisterCallback` | `0x2CE40` | 71 | UnwindData |  |
| 80 | `zelTracerDeviceGetSubDevicesRegisterCallback` | `0x2CE90` | 68 | UnwindData |  |
| 81 | `zelTracerDevicePciGetPropertiesExtRegisterCallback` | `0x2CEE0` | 71 | UnwindData |  |
| 82 | `zelTracerDeviceReserveCacheExtRegisterCallback` | `0x2CF30` | 71 | UnwindData |  |
| 83 | `zelTracerDeviceSetCacheAdviceExtRegisterCallback` | `0x2CF80` | 71 | UnwindData |  |
| 84 | `zelTracerDriverGetApiVersionRegisterCallback` | `0x2CFD0` | 68 | UnwindData |  |
| 85 | `zelTracerDriverGetExtensionFunctionAddressRegisterCallback` | `0x2D020` | 68 | UnwindData |  |
| 86 | `zelTracerDriverGetExtensionPropertiesRegisterCallback` | `0x2D070` | 68 | UnwindData |  |
| 87 | `zelTracerDriverGetIpcPropertiesRegisterCallback` | `0x2D0C0` | 68 | UnwindData |  |
| 88 | `zelTracerDriverGetPropertiesRegisterCallback` | `0x2D110` | 68 | UnwindData |  |
| 89 | `zelTracerDriverGetRegisterCallback` | `0x2D160` | 68 | UnwindData |  |
| 90 | `zelTracerEventCreateRegisterCallback` | `0x2D1B0` | 71 | UnwindData |  |
| 91 | `zelTracerEventDestroyRegisterCallback` | `0x2D200` | 71 | UnwindData |  |
| 92 | `zelTracerEventHostResetRegisterCallback` | `0x2D250` | 71 | UnwindData |  |
| 93 | `zelTracerEventHostSignalRegisterCallback` | `0x2D2A0` | 71 | UnwindData |  |
| 94 | `zelTracerEventHostSynchronizeRegisterCallback` | `0x2D2F0` | 71 | UnwindData |  |
| 95 | `zelTracerEventPoolCloseIpcHandleRegisterCallback` | `0x2D340` | 71 | UnwindData |  |
| 96 | `zelTracerEventPoolCreateRegisterCallback` | `0x2D390` | 71 | UnwindData |  |
| 97 | `zelTracerEventPoolDestroyRegisterCallback` | `0x2D3E0` | 71 | UnwindData |  |
| 98 | `zelTracerEventPoolGetIpcHandleRegisterCallback` | `0x2D430` | 71 | UnwindData |  |
| 99 | `zelTracerEventPoolOpenIpcHandleRegisterCallback` | `0x2D480` | 71 | UnwindData |  |
| 100 | `zelTracerEventQueryKernelTimestampRegisterCallback` | `0x2D4D0` | 71 | UnwindData |  |
| 101 | `zelTracerEventQueryStatusRegisterCallback` | `0x2D520` | 71 | UnwindData |  |
| 102 | `zelTracerEventQueryTimestampsExpRegisterCallback` | `0x2D570` | 71 | UnwindData |  |
| 103 | `zelTracerFenceCreateRegisterCallback` | `0x2D5C0` | 71 | UnwindData |  |
| 104 | `zelTracerFenceDestroyRegisterCallback` | `0x2D610` | 71 | UnwindData |  |
| 105 | `zelTracerFenceHostSynchronizeRegisterCallback` | `0x2D660` | 71 | UnwindData |  |
| 106 | `zelTracerFenceQueryStatusRegisterCallback` | `0x2D6B0` | 71 | UnwindData |  |
| 107 | `zelTracerFenceResetRegisterCallback` | `0x2D700` | 71 | UnwindData |  |
| 108 | `zelTracerImageCreateRegisterCallback` | `0x2D750` | 71 | UnwindData |  |
| 109 | `zelTracerImageDestroyRegisterCallback` | `0x2D7A0` | 71 | UnwindData |  |
| 110 | `zelTracerImageGetAllocPropertiesExtRegisterCallback` | `0x2D7F0` | 71 | UnwindData |  |
| 111 | `zelTracerImageGetMemoryPropertiesExpRegisterCallback` | `0x2D840` | 71 | UnwindData |  |
| 112 | `zelTracerImageGetPropertiesRegisterCallback` | `0x2D890` | 71 | UnwindData |  |
| 113 | `zelTracerImageViewCreateExpRegisterCallback` | `0x2D8E0` | 71 | UnwindData |  |
| 114 | `zelTracerInitRegisterCallback` | `0x2D930` | 67 | UnwindData |  |
| 115 | `zelTracerKernelCreateRegisterCallback` | `0x2D980` | 71 | UnwindData |  |
| 116 | `zelTracerKernelDestroyRegisterCallback` | `0x2D9D0` | 71 | UnwindData |  |
| 117 | `zelTracerKernelGetIndirectAccessRegisterCallback` | `0x2DA20` | 71 | UnwindData |  |
| 118 | `zelTracerKernelGetNameRegisterCallback` | `0x2DA70` | 71 | UnwindData |  |
| 119 | `zelTracerKernelGetPropertiesRegisterCallback` | `0x2DAC0` | 71 | UnwindData |  |
| 120 | `zelTracerKernelGetSourceAttributesRegisterCallback` | `0x2DB10` | 71 | UnwindData |  |
| 121 | `zelTracerKernelSchedulingHintExpRegisterCallback` | `0x2DB60` | 71 | UnwindData |  |
| 122 | `zelTracerKernelSetArgumentValueRegisterCallback` | `0x2DBB0` | 71 | UnwindData |  |
| 123 | `zelTracerKernelSetCacheConfigRegisterCallback` | `0x2DC00` | 71 | UnwindData |  |
| 124 | `zelTracerKernelSetGlobalOffsetExpRegisterCallback` | `0x2DC50` | 71 | UnwindData |  |
| 125 | `zelTracerKernelSetGroupSizeRegisterCallback` | `0x2DCA0` | 71 | UnwindData |  |
| 126 | `zelTracerKernelSetIndirectAccessRegisterCallback` | `0x2DCF0` | 71 | UnwindData |  |
| 127 | `zelTracerKernelSuggestGroupSizeRegisterCallback` | `0x2DD40` | 71 | UnwindData |  |
| 128 | `zelTracerKernelSuggestMaxCooperativeGroupCountRegisterCallback` | `0x2DD90` | 71 | UnwindData |  |
| 129 | `zelTracerMemAllocDeviceRegisterCallback` | `0x2DDE0` | 71 | UnwindData |  |
| 130 | `zelTracerMemAllocHostRegisterCallback` | `0x2DE30` | 71 | UnwindData |  |
| 131 | `zelTracerMemAllocSharedRegisterCallback` | `0x2DE80` | 71 | UnwindData |  |
| 132 | `zelTracerMemCloseIpcHandleRegisterCallback` | `0x2DED0` | 71 | UnwindData |  |
| 133 | `zelTracerMemFreeExtRegisterCallback` | `0x2DF20` | 71 | UnwindData |  |
| 134 | `zelTracerMemFreeRegisterCallback` | `0x2DF70` | 71 | UnwindData |  |
| 135 | `zelTracerMemGetAddressRangeRegisterCallback` | `0x2DFC0` | 71 | UnwindData |  |
| 136 | `zelTracerMemGetAllocPropertiesRegisterCallback` | `0x2E010` | 71 | UnwindData |  |
| 137 | `zelTracerMemGetIpcHandleRegisterCallback` | `0x2E060` | 71 | UnwindData |  |
| 138 | `zelTracerMemOpenIpcHandleRegisterCallback` | `0x2E0B0` | 71 | UnwindData |  |
| 139 | `zelTracerModuleBuildLogDestroyRegisterCallback` | `0x2E100` | 71 | UnwindData |  |
| 140 | `zelTracerModuleBuildLogGetStringRegisterCallback` | `0x2E150` | 71 | UnwindData |  |
| 141 | `zelTracerModuleCreateRegisterCallback` | `0x2E1A0` | 71 | UnwindData |  |
| 142 | `zelTracerModuleDestroyRegisterCallback` | `0x2E1F0` | 71 | UnwindData |  |
| 143 | `zelTracerModuleDynamicLinkRegisterCallback` | `0x2E240` | 71 | UnwindData |  |
| 144 | `zelTracerModuleGetFunctionPointerRegisterCallback` | `0x2E290` | 71 | UnwindData |  |
| 145 | `zelTracerModuleGetGlobalPointerRegisterCallback` | `0x2E2E0` | 71 | UnwindData |  |
| 146 | `zelTracerModuleGetKernelNamesRegisterCallback` | `0x2E330` | 71 | UnwindData |  |
| 147 | `zelTracerModuleGetNativeBinaryRegisterCallback` | `0x2E380` | 71 | UnwindData |  |
| 148 | `zelTracerModuleGetPropertiesRegisterCallback` | `0x2E3D0` | 71 | UnwindData |  |
| 149 | `zelTracerModuleInspectLinkageExtRegisterCallback` | `0x2E420` | 71 | UnwindData |  |
| 150 | `zelTracerPhysicalMemCreateRegisterCallback` | `0x2E470` | 71 | UnwindData |  |
| 151 | `zelTracerPhysicalMemDestroyRegisterCallback` | `0x2E4C0` | 71 | UnwindData |  |
| 152 | `zelTracerSamplerCreateRegisterCallback` | `0x2E510` | 71 | UnwindData |  |
| 153 | `zelTracerSamplerDestroyRegisterCallback` | `0x2E560` | 71 | UnwindData |  |
| 157 | `zelTracerVirtualMemFreeRegisterCallback` | `0x2E5B0` | 71 | UnwindData |  |
| 158 | `zelTracerVirtualMemGetAccessAttributeRegisterCallback` | `0x2E600` | 71 | UnwindData |  |
| 159 | `zelTracerVirtualMemMapRegisterCallback` | `0x2E650` | 71 | UnwindData |  |
| 160 | `zelTracerVirtualMemQueryPageSizeRegisterCallback` | `0x2E6A0` | 71 | UnwindData |  |
| 161 | `zelTracerVirtualMemReserveRegisterCallback` | `0x2E6F0` | 71 | UnwindData |  |
| 162 | `zelTracerVirtualMemSetAccessAttributeRegisterCallback` | `0x2E740` | 71 | UnwindData |  |
| 163 | `zelTracerVirtualMemUnmapRegisterCallback` | `0x2E790` | 71 | UnwindData |  |
