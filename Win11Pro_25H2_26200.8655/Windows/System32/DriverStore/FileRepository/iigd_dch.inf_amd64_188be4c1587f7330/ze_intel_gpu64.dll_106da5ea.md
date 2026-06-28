# Binary Specification: ze_intel_gpu64.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_188be4c1587f7330\ze_intel_gpu64.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `106da5eabd32ed923c051d5af22b3d202b22b262a1bc12b8b46e050689b38b41`
* **Total Exported Functions:** 465

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `zeCommandListAppendBarrier_Tracing` | `0x89040` | 137 | UnwindData |  |
| 35 | `zeCommandListAppendMemoryRangesBarrier_Tracing` | `0x89410` | 191 | UnwindData |  |
| 37 | `zeCommandListAppendQueryKernelTimestamps_Tracing` | `0x8BFB0` | 219 | UnwindData |  |
| 43 | `zeCommandListAppendWriteGlobalTimestamp_Tracing` | `0x8C3F0` | 157 | UnwindData |  |
| 45 | `zeCommandListClose_Tracing` | `0x8C7F0` | 113 | UnwindData |  |
| 48 | `zeCommandListCreateImmediate_Tracing` | `0x8CB80` | 137 | UnwindData |  |
| 49 | `zeCommandListCreate_Tracing` | `0x8CF50` | 137 | UnwindData |  |
| 51 | `zeCommandListDestroy_Tracing` | `0x8D320` | 113 | UnwindData |  |
| 53 | `zeCommandListReset_Tracing` | `0x8D6B0` | 113 | UnwindData |  |
| 55 | `zeCommandQueueCreate_Tracing` | `0x8F060` | 137 | UnwindData |  |
| 57 | `zeCommandQueueDestroy_Tracing` | `0x8F430` | 113 | UnwindData |  |
| 59 | `zeCommandQueueExecuteCommandLists_Tracing` | `0x8F7C0` | 135 | UnwindData |  |
| 61 | `zeCommandQueueSynchronize_Tracing` | `0x8FB90` | 121 | UnwindData |  |
| 8 | `zeCommandListAppendImageCopyFromMemory_Tracing` | `0x93B80` | 193 | UnwindData |  |
| 10 | `zeCommandListAppendImageCopyRegion_Tracing` | `0x93FC0` | 221 | UnwindData |  |
| 12 | `zeCommandListAppendImageCopyToMemory_Tracing` | `0x94410` | 193 | UnwindData |  |
| 13 | `zeCommandListAppendImageCopy_Tracing` | `0x94850` | 169 | UnwindData |  |
| 23 | `zeCommandListAppendMemAdvise_Tracing` | `0x94C60` | 149 | UnwindData |  |
| 26 | `zeCommandListAppendMemoryCopyFromContext_Tracing` | `0x95050` | 208 | UnwindData |  |
| 28 | `zeCommandListAppendMemoryCopyRegion_Tracing` | `0x954A0` | 288 | UnwindData |  |
| 29 | `zeCommandListAppendMemoryCopy_Tracing` | `0x95990` | 193 | UnwindData |  |
| 31 | `zeCommandListAppendMemoryFill_Tracing` | `0x95DD0` | 208 | UnwindData |  |
| 33 | `zeCommandListAppendMemoryPrefetch_Tracing` | `0x96220` | 129 | UnwindData |  |
| 80 | `zeDeviceCanAccessPeer_Tracing` | `0x9B850` | 129 | UnwindData |  |
| 83 | `zeDeviceGetCacheProperties_Tracing` | `0x9BC10` | 129 | UnwindData |  |
| 85 | `zeDeviceGetCommandQueueGroupProperties_Tracing` | `0x9BFD0` | 129 | UnwindData |  |
| 87 | `zeDeviceGetComputeProperties_Tracing` | `0x9C390` | 121 | UnwindData |  |
| 89 | `zeDeviceGetExternalMemoryProperties_Tracing` | `0x9C730` | 121 | UnwindData |  |
| 92 | `zeDeviceGetImageProperties_Tracing` | `0x9CAE0` | 121 | UnwindData |  |
| 94 | `zeDeviceGetMemoryAccessProperties_Tracing` | `0x9CE80` | 121 | UnwindData |  |
| 96 | `zeDeviceGetMemoryProperties_Tracing` | `0x9D220` | 129 | UnwindData |  |
| 98 | `zeDeviceGetModuleProperties_Tracing` | `0x9D5E0` | 121 | UnwindData |  |
| 100 | `zeDeviceGetP2PProperties_Tracing` | `0x9D980` | 129 | UnwindData |  |
| 102 | `zeDeviceGetProperties_Tracing` | `0x9DD40` | 121 | UnwindData |  |
| 104 | `zeDeviceGetStatus_Tracing` | `0x9E0E0` | 113 | UnwindData |  |
| 106 | `zeDeviceGetSubDevices_Tracing` | `0x9E470` | 129 | UnwindData |  |
| 107 | `zeDeviceGet_Tracing` | `0x9E830` | 129 | UnwindData |  |
| 204 | `zeKernelSetCacheConfig_Tracing` | `0x9EBF0` | 119 | UnwindData |  |
| 113 | `zeDriverGetApiVersion_Tracing` | `0xA0AF0` | 121 | UnwindData |  |
| 116 | `zeDriverGetExtensionProperties_Tracing` | `0xA0E90` | 129 | UnwindData |  |
| 118 | `zeDriverGetIpcProperties_Tracing` | `0xA1250` | 121 | UnwindData |  |
| 120 | `zeDriverGetProperties_Tracing` | `0xA15F0` | 121 | UnwindData |  |
| 121 | `zeDriverGet_Tracing` | `0xA1990` | 121 | UnwindData |  |
| 5 | `zeCommandListAppendEventReset_Tracing` | `0xA6FA0` | 121 | UnwindData |  |
| 39 | `zeCommandListAppendSignalEvent_Tracing` | `0xA7350` | 121 | UnwindData |  |
| 41 | `zeCommandListAppendWaitOnEvents_Tracing` | `0xA7700` | 127 | UnwindData |  |
| 123 | `zeEventCreate_Tracing` | `0xA7AC0` | 129 | UnwindData |  |
| 125 | `zeEventDestroy_Tracing` | `0xA7E80` | 113 | UnwindData |  |
| 127 | `zeEventHostReset_Tracing` | `0xA8210` | 113 | UnwindData |  |
| 129 | `zeEventHostSignal_Tracing` | `0xA85A0` | 113 | UnwindData |  |
| 131 | `zeEventHostSynchronize_Tracing` | `0xA8930` | 121 | UnwindData |  |
| 133 | `zeEventPoolCloseIpcHandle_Tracing` | `0xA8CE0` | 113 | UnwindData |  |
| 135 | `zeEventPoolCreate_Tracing` | `0xA9070` | 157 | UnwindData |  |
| 137 | `zeEventPoolDestroy_Tracing` | `0xA9470` | 113 | UnwindData |  |
| 139 | `zeEventPoolGetIpcHandle_Tracing` | `0xA9800` | 121 | UnwindData |  |
| 141 | `zeEventPoolOpenIpcHandle_Tracing` | `0xA9BB0` | 165 | UnwindData |  |
| 143 | `zeEventQueryKernelTimestamp_Tracing` | `0xA9F80` | 121 | UnwindData |  |
| 145 | `zeEventQueryStatus_Tracing` | `0xAA330` | 113 | UnwindData |  |
| 148 | `zeFenceCreate_Tracing` | `0xAC210` | 129 | UnwindData |  |
| 150 | `zeFenceDestroy_Tracing` | `0xAC5D0` | 113 | UnwindData |  |
| 152 | `zeFenceHostSynchronize_Tracing` | `0xAC960` | 121 | UnwindData |  |
| 154 | `zeFenceQueryStatus_Tracing` | `0xACD10` | 113 | UnwindData |  |
| 156 | `zeFenceReset_Tracing` | `0xAD0A0` | 113 | UnwindData |  |
| 187 | `zeInit_Tracing` | `0xAD9A0` | 109 | UnwindData |  |
| 258 | `zeSamplerCreate_Tracing` | `0xAE830` | 137 | UnwindData |  |
| 260 | `zeSamplerDestroy_Tracing` | `0xAEC00` | 113 | UnwindData |  |
| 64 | `zeContextCreate_Tracing` | `0xB1BD0` | 129 | UnwindData |  |
| 66 | `zeContextDestroy_Tracing` | `0xB1F90` | 113 | UnwindData |  |
| 68 | `zeContextEvictImage_Tracing` | `0xB2320` | 129 | UnwindData |  |
| 70 | `zeContextEvictMemory_Tracing` | `0xB26E0` | 137 | UnwindData |  |
| 72 | `zeContextGetStatus_Tracing` | `0xB2AB0` | 113 | UnwindData |  |
| 74 | `zeContextMakeImageResident_Tracing` | `0xB2E40` | 129 | UnwindData |  |
| 76 | `zeContextMakeMemoryResident_Tracing` | `0xB3200` | 137 | UnwindData |  |
| 78 | `zeContextSystemBarrier_Tracing` | `0xB35D0` | 121 | UnwindData |  |
| 178 | `zeImageCreate_Tracing` | `0xB4A20` | 137 | UnwindData |  |
| 180 | `zeImageDestroy_Tracing` | `0xB4DF0` | 113 | UnwindData |  |
| 184 | `zeImageGetProperties_Tracing` | `0xB5180` | 129 | UnwindData |  |
| 215 | `zeMemAllocDevice_Tracing` | `0xBBB40` | 181 | UnwindData |  |
| 217 | `zeMemAllocHost_Tracing` | `0xBBF50` | 157 | UnwindData |  |
| 219 | `zeMemAllocShared_Tracing` | `0xBC350` | 193 | UnwindData |  |
| 221 | `zeMemCloseIpcHandle_Tracing` | `0xBC790` | 121 | UnwindData |  |
| 224 | `zeMemFree_Tracing` | `0xBCB40` | 121 | UnwindData |  |
| 226 | `zeMemGetAddressRange_Tracing` | `0xBCEF0` | 137 | UnwindData |  |
| 228 | `zeMemGetAllocProperties_Tracing` | `0xBD2C0` | 137 | UnwindData |  |
| 230 | `zeMemGetIpcHandle_Tracing` | `0xBD690` | 129 | UnwindData |  |
| 232 | `zeMemOpenIpcHandle_Tracing` | `0xBDA50` | 194 | UnwindData |  |
| 254 | `zePhysicalMemCreate_Tracing` | `0xBDE60` | 137 | UnwindData |  |
| 256 | `zePhysicalMemDestroy_Tracing` | `0xBE230` | 121 | UnwindData |  |
| 262 | `zeVirtualMemFree_Tracing` | `0xBE5E0` | 129 | UnwindData |  |
| 264 | `zeVirtualMemGetAccessAttribute_Tracing` | `0xBE9A0` | 157 | UnwindData |  |
| 266 | `zeVirtualMemMap_Tracing` | `0xBEDA0` | 161 | UnwindData |  |
| 268 | `zeVirtualMemQueryPageSize_Tracing` | `0xBF1B0` | 137 | UnwindData |  |
| 270 | `zeVirtualMemReserve_Tracing` | `0xBF580` | 137 | UnwindData |  |
| 272 | `zeVirtualMemSetAccessAttribute_Tracing` | `0xBF950` | 137 | UnwindData |  |
| 274 | `zeVirtualMemUnmap_Tracing` | `0xBFD20` | 129 | UnwindData |  |
| 15 | `zeCommandListAppendLaunchCooperativeKernel_Tracing` | `0xC8D40` | 169 | UnwindData |  |
| 18 | `zeCommandListAppendLaunchKernelIndirect_Tracing` | `0xC9150` | 169 | UnwindData |  |
| 19 | `zeCommandListAppendLaunchKernel_Tracing` | `0xC9560` | 169 | UnwindData |  |
| 21 | `zeCommandListAppendLaunchMultipleKernelsIndirect_Tracing` | `0xC9970` | 219 | UnwindData |  |
| 189 | `zeKernelCreate_Tracing` | `0xC9DB0` | 129 | UnwindData |  |
| 191 | `zeKernelDestroy_Tracing` | `0xCA170` | 113 | UnwindData |  |
| 193 | `zeKernelGetIndirectAccess_Tracing` | `0xCA500` | 121 | UnwindData |  |
| 195 | `zeKernelGetName_Tracing` | `0xCA8B0` | 129 | UnwindData |  |
| 197 | `zeKernelGetProperties_Tracing` | `0xCAC70` | 121 | UnwindData |  |
| 199 | `zeKernelGetSourceAttributes_Tracing` | `0xCB020` | 129 | UnwindData |  |
| 202 | `zeKernelSetArgumentValue_Tracing` | `0xCB3E0` | 135 | UnwindData |  |
| 207 | `zeKernelSetGroupSize_Tracing` | `0xCB7B0` | 135 | UnwindData |  |
| 209 | `zeKernelSetIndirectAccess_Tracing` | `0xCBB80` | 119 | UnwindData |  |
| 211 | `zeKernelSuggestGroupSize_Tracing` | `0xCBF30` | 204 | UnwindData |  |
| 213 | `zeKernelSuggestMaxCooperativeGroupCount_Tracing` | `0xCC360` | 121 | UnwindData |  |
| 234 | `zeModuleBuildLogDestroy_Tracing` | `0xCC710` | 113 | UnwindData |  |
| 236 | `zeModuleBuildLogGetString_Tracing` | `0xCCAA0` | 129 | UnwindData |  |
| 238 | `zeModuleCreate_Tracing` | `0xCCE60` | 157 | UnwindData |  |
| 240 | `zeModuleDestroy_Tracing` | `0xCD260` | 113 | UnwindData |  |
| 242 | `zeModuleDynamicLink_Tracing` | `0xCD5F0` | 128 | UnwindData |  |
| 244 | `zeModuleGetFunctionPointer_Tracing` | `0xCD9B0` | 129 | UnwindData |  |
| 246 | `zeModuleGetGlobalPointer_Tracing` | `0xCDD70` | 137 | UnwindData |  |
| 248 | `zeModuleGetKernelNames_Tracing` | `0xCE140` | 129 | UnwindData |  |
| 250 | `zeModuleGetNativeBinary_Tracing` | `0xCE500` | 129 | UnwindData |  |
| 252 | `zeModuleGetProperties_Tracing` | `0xCE8C0` | 121 | UnwindData |  |
| 1 | `?zeDeviceSystemBarrier@@YA?AW4_ze_result_t@@PEAU_ze_device_handle_t@@@Z` | `0xED950` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `zeCommandListAppendBarrier` | `0xED980` | 38 | UnwindData |  |
| 34 | `zeCommandListAppendMemoryRangesBarrier` | `0xED9B0` | 82 | UnwindData |  |
| 36 | `zeCommandListAppendQueryKernelTimestamps` | `0xEDA10` | 104 | UnwindData |  |
| 42 | `zeCommandListAppendWriteGlobalTimestamp` | `0xEDA80` | 57 | UnwindData |  |
| 44 | `zeCommandListClose` | `0xEDAC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `zeCommandListCreate` | `0xEDAE0` | 25 | UnwindData |  |
| 47 | `zeCommandListCreateImmediate` | `0xEDB00` | 25 | UnwindData |  |
| 50 | `zeCommandListDestroy` | `0xEDB20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `zeCommandListReset` | `0xEDB40` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `zeCommandQueueCreate` | `0xEDB70` | 25 | UnwindData |  |
| 56 | `zeCommandQueueDestroy` | `0xEDB90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `zeCommandQueueExecuteCommandLists` | `0xEDBB0` | 43 | UnwindData |  |
| 60 | `zeCommandQueueSynchronize` | `0xEDBE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `zeContextCreate` | `0xEDC00` | 33 | UnwindData |  |
| 63 | `zeContextCreateEx` | `0xEDC30` | 32 | UnwindData |  |
| 65 | `zeContextDestroy` | `0xEDC50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `zeContextEvictImage` | `0xEDC60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `zeContextEvictMemory` | `0xEDC70` | 22 | UnwindData |  |
| 71 | `zeContextGetStatus` | `0xEDC90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `zeContextMakeImageResident` | `0xEDCA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `zeContextMakeMemoryResident` | `0xEDCB0` | 22 | UnwindData |  |
| 77 | `zeContextSystemBarrier` | `0xEDCD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 253 | `zePhysicalMemCreate` | `0xEDCE0` | 25 | UnwindData |  |
| 255 | `zePhysicalMemDestroy` | `0xEDD00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 261 | `zeVirtualMemFree` | `0xEDD20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 263 | `zeVirtualMemGetAccessAttribute` | `0xEDD40` | 35 | UnwindData |  |
| 265 | `zeVirtualMemMap` | `0xEDD70` | 45 | UnwindData |  |
| 267 | `zeVirtualMemQueryPageSize` | `0xEDDA0` | 25 | UnwindData |  |
| 269 | `zeVirtualMemReserve` | `0xEDDC0` | 25 | UnwindData |  |
| 271 | `zeVirtualMemSetAccessAttribute` | `0xEDDE0` | 25 | UnwindData |  |
| 273 | `zeVirtualMemUnmap` | `0xEDE00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `zeCommandListAppendImageCopy` | `0xEDE20` | 71 | UnwindData |  |
| 7 | `zeCommandListAppendImageCopyFromMemory` | `0xEDE70` | 84 | UnwindData |  |
| 9 | `zeCommandListAppendImageCopyRegion` | `0xEDED0` | 103 | UnwindData |  |
| 11 | `zeCommandListAppendImageCopyToMemory` | `0xEDF40` | 84 | UnwindData |  |
| 22 | `zeCommandListAppendMemAdvise` | `0xEDFA0` | 54 | UnwindData |  |
| 24 | `zeCommandListAppendMemoryCopy` | `0xEDFE0` | 84 | UnwindData |  |
| 25 | `zeCommandListAppendMemoryCopyFromContext` | `0xEE040` | 106 | UnwindData |  |
| 27 | `zeCommandListAppendMemoryCopyRegion` | `0xEE0B0` | 149 | UnwindData |  |
| 30 | `zeCommandListAppendMemoryFill` | `0xEE150` | 106 | UnwindData |  |
| 32 | `zeCommandListAppendMemoryPrefetch` | `0xEE1C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `zeGetCommandListProcAddrTable` | `0xEE1F0` | 924 | UnwindData |  |
| 158 | `zeGetCommandQueueProcAddrTable` | `0xEE590` | 267 | UnwindData |  |
| 159 | `zeGetContextProcAddrTable` | `0xEE6A0` | 401 | UnwindData |  |
| 160 | `zeGetDeviceProcAddrTable` | `0xEE840` | 621 | UnwindData |  |
| 161 | `zeGetDriverProcAddrTable` | `0xEEAB0` | 311 | UnwindData |  |
| 162 | `zeGetEventExpProcAddrTable` | `0xEEBF0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 163 | `zeGetEventPoolProcAddrTable` | `0xEEC30` | 302 | UnwindData |  |
| 164 | `zeGetEventProcAddrTable` | `0xEED60` | 357 | UnwindData |  |
| 165 | `zeGetFenceProcAddrTable` | `0xEEED0` | 302 | UnwindData |  |
| 166 | `zeGetGlobalProcAddrTable` | `0xEF000` | 188 | UnwindData |  |
| 167 | `zeGetImageExpProcAddrTable` | `0xEF0C0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `zeGetImageProcAddrTable` | `0xEF110` | 260 | UnwindData |  |
| 169 | `zeGetKernelExpProcAddrTable` | `0xEF220` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 170 | `zeGetKernelProcAddrTable` | `0xEF270` | 491 | UnwindData |  |
| 171 | `zeGetMemProcAddrTable` | `0xEF460` | 421 | UnwindData |  |
| 172 | `zeGetModuleBuildLogProcAddrTable` | `0xEF610` | 212 | UnwindData |  |
| 173 | `zeGetModuleProcAddrTable` | `0xEF6F0` | 390 | UnwindData |  |
| 174 | `zeGetPhysicalMemProcAddrTable` | `0xEF880` | 212 | UnwindData |  |
| 175 | `zeGetSamplerProcAddrTable` | `0xEF960` | 212 | UnwindData |  |
| 176 | `zeGetVirtualMemProcAddrTable` | `0xEFA40` | 357 | UnwindData |  |
| 79 | `zeDeviceCanAccessPeer` | `0xEFBB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `zeDeviceGet` | `0xEFBD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `zeDeviceGetCacheProperties` | `0xEFBE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `zeDeviceGetCommandQueueGroupProperties` | `0xEFC00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `zeDeviceGetComputeProperties` | `0xEFC30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `zeDeviceGetExternalMemoryProperties` | `0xEFC50` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `zeDeviceGetGlobalTimestamps` | `0xEFC80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `zeDeviceGetImageProperties` | `0xEFCB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `zeDeviceGetMemoryAccessProperties` | `0xEFCE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `zeDeviceGetMemoryProperties` | `0xEFD00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `zeDeviceGetModuleProperties` | `0xEFD20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `zeDeviceGetP2PProperties` | `0xEFD40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `zeDeviceGetProperties` | `0xEFD60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `zeDeviceGetStatus` | `0xEFD80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `zeDeviceGetSubDevices` | `0xEFD90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `zeDevicePciGetPropertiesExt` | `0xEFDB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `zeDeviceReserveCacheExt` | `0xEFDD0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `zeDeviceSetCacheAdviceExt` | `0xEFE00` | 41 | UnwindData |  |
| 111 | `zeDriverGet` | `0xEFE30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `zeDriverGetApiVersion` | `0xEFE40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `zeDriverGetExtensionFunctionAddress` | `0xEFE50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `zeDriverGetExtensionProperties` | `0xEFE60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `zeDriverGetIpcProperties` | `0xEFE70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `zeDriverGetProperties` | `0xEFE80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `zeInit` | `0xEFE90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `zeCommandListAppendEventReset` | `0xEFEA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `zeCommandListAppendSignalEvent` | `0xEFEC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `zeCommandListAppendWaitOnEvents` | `0xEFEF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `zeEventCreate` | `0xEFF20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `zeEventDestroy` | `0xEFF40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `zeEventHostReset` | `0xEFF60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `zeEventHostSignal` | `0xEFF80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | `zeEventHostSynchronize` | `0xEFFA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `zeEventPoolCloseIpcHandle` | `0xEFFC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `zeEventPoolCreate` | `0xEFFE0` | 35 | UnwindData |  |
| 136 | `zeEventPoolDestroy` | `0xF0010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `zeEventPoolGetIpcHandle` | `0xF0030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `zeEventPoolOpenIpcHandle` | `0xF0050` | 65 | UnwindData |  |
| 142 | `zeEventQueryKernelTimestamp` | `0xF00A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `zeEventQueryStatus` | `0xF00C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `zeFenceCreate` | `0xF00E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `zeFenceDestroy` | `0xF0100` | 49 | UnwindData |  |
| 151 | `zeFenceHostSynchronize` | `0xF0140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `zeFenceQueryStatus` | `0xF0160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `zeFenceReset` | `0xF0180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 177 | `zeImageCreate` | `0xF01A0` | 25 | UnwindData |  |
| 179 | `zeImageDestroy` | `0xF01C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `zeImageGetProperties` | `0xF01E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 214 | `zeMemAllocDevice` | `0xF0210` | 48 | UnwindData |  |
| 216 | `zeMemAllocHost` | `0xF0240` | 32 | UnwindData |  |
| 218 | `zeMemAllocShared` | `0xF0260` | 61 | UnwindData |  |
| 220 | `zeMemCloseIpcHandle` | `0xF02A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `zeMemFree` | `0xF02B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 223 | `zeMemFreeExt` | `0xF02C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 225 | `zeMemGetAddressRange` | `0xF02D0` | 22 | UnwindData |  |
| 227 | `zeMemGetAllocProperties` | `0xF02F0` | 25 | UnwindData |  |
| 229 | `zeMemGetIpcHandle` | `0xF0310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 231 | `zeMemOpenIpcHandle` | `0xF0330` | 88 | UnwindData |  |
| 14 | `zeCommandListAppendLaunchCooperativeKernel` | `0xF0390` | 71 | UnwindData |  |
| 16 | `zeCommandListAppendLaunchKernel` | `0xF03E0` | 71 | UnwindData |  |
| 17 | `zeCommandListAppendLaunchKernelIndirect` | `0xF0430` | 71 | UnwindData |  |
| 20 | `zeCommandListAppendLaunchMultipleKernelsIndirect` | `0xF0480` | 101 | UnwindData |  |
| 188 | `zeKernelCreate` | `0xF04F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `zeKernelDestroy` | `0xF0510` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 192 | `zeKernelGetIndirectAccess` | `0xF0530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 194 | `zeKernelGetName` | `0xF0550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 196 | `zeKernelGetProperties` | `0xF0570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 198 | `zeKernelGetSourceAttributes` | `0xF0590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 200 | `zeKernelSchedulingHintExp` | `0xF05B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | `zeKernelSetArgumentValue` | `0xF05E0` | 38 | UnwindData |  |
| 203 | `zeKernelSetCacheConfig` | `0xF0610` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | `zeKernelSetGroupSize` | `0xF0640` | 38 | UnwindData |  |
| 208 | `zeKernelSetIndirectAccess` | `0xF0670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 210 | `zeKernelSuggestGroupSize` | `0xF0690` | 84 | UnwindData |  |
| 212 | `zeKernelSuggestMaxCooperativeGroupCount` | `0xF06F0` | 47 | UnwindData |  |
| 233 | `zeModuleBuildLogDestroy` | `0xF0720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 235 | `zeModuleBuildLogGetString` | `0xF0740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 237 | `zeModuleCreate` | `0xF0760` | 35 | UnwindData |  |
| 239 | `zeModuleDestroy` | `0xF0790` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 241 | `zeModuleDynamicLink` | `0xF07B0` | 51 | UnwindData |  |
| 243 | `zeModuleGetFunctionPointer` | `0xF07F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 245 | `zeModuleGetGlobalPointer` | `0xF0810` | 38 | UnwindData |  |
| 247 | `zeModuleGetKernelNames` | `0xF0840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 249 | `zeModuleGetNativeBinary` | `0xF0860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 251 | `zeModuleGetProperties` | `0xF0880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 257 | `zeSamplerCreate` | `0xF08A0` | 25 | UnwindData |  |
| 259 | `zeSamplerDestroy` | `0xF08C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 462 | `zexDriverGetHostPointerBaseAddress` | `0xF08E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 463 | `zexDriverImportExternalPointer` | `0xF0900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 464 | `zexDriverReleaseImportedPointer` | `0xF0920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 465 | `zexKernelGetBaseAddress` | `0xF0940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 443 | `zexCommandGraphClose` | `0xF0960` | 64 | UnwindData |  |
| 444 | `zexCommandGraphCloseNode` | `0xF09A0` | 222 | UnwindData |  |
| 445 | `zexCommandGraphCreate` | `0xF0A80` | 99 | UnwindData |  |
| 446 | `zexCommandGraphCreateLoadRegImemNode` | `0xF0AF0` | 123 | UnwindData |  |
| 447 | `zexCommandGraphCreateNode` | `0xF0B70` | 125 | UnwindData |  |
| 448 | `zexCommandGraphCreateStoreRegImemNode` | `0xF0BF0` | 123 | UnwindData |  |
| 449 | `zexCommandGraphDestroy` | `0xF0C70` | 65 | UnwindData |  |
| 450 | `zexCommandGraphNodeAddChildren` | `0xF0CC0` | 82 | UnwindData |  |
| 451 | `zexCommandGraphOpenNode` | `0xF0D20` | 90 | UnwindData |  |
| 452 | `zexCommandListAppendMILoadRegImm` | `0xF0D80` | 68 | UnwindData |  |
| 453 | `zexCommandListAppendMILoadRegMem` | `0xF0DD0` | 68 | UnwindData |  |
| 454 | `zexCommandListAppendMILoadRegReg` | `0xF0E20` | 68 | UnwindData |  |
| 455 | `zexCommandListAppendMIMath` | `0xF0E70` | 68 | UnwindData |  |
| 456 | `zexCommandListAppendMIStoreRegMem` | `0xF0EC0` | 68 | UnwindData |  |
| 457 | `zexCommandListAppendPipeControl` | `0xF0F10` | 68 | UnwindData |  |
| 458 | `zexCommandListAppendWaitOnMemory` | `0xF0F60` | 84 | UnwindData |  |
| 459 | `zexCommandListAppendWriteToMemory` | `0xF0FC0` | 68 | UnwindData |  |
| 460 | `zexCommandListReserveSpace` | `0xF1010` | 93 | UnwindData |  |
| 461 | `zexCommandQueueExecuteCommandGraphs` | `0xF1070` | 77 | UnwindData |  |
| 438 | `zetTracerExpCreate` | `0xF10C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 439 | `zetTracerExpDestroy` | `0xF10D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 440 | `zetTracerExpSetEnabled` | `0xF10F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 441 | `zetTracerExpSetEpilogues` | `0xF1110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 442 | `zetTracerExpSetPrologues` | `0xF1130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 337 | `zesGetDeviceProcAddrTable` | `0xF1150` | 594 | UnwindData |  |
| 338 | `zesGetDiagnosticsProcAddrTable` | `0xF13B0` | 241 | UnwindData |  |
| 339 | `zesGetDriverProcAddrTable` | `0xF14B0` | 206 | UnwindData |  |
| 340 | `zesGetEngineProcAddrTable` | `0xF1580` | 206 | UnwindData |  |
| 341 | `zesGetFabricPortProcAddrTable` | `0xF1650` | 266 | UnwindData |  |
| 342 | `zesGetFanProcAddrTable` | `0xF1760` | 266 | UnwindData |  |
| 343 | `zesGetFirmwareProcAddrTable` | `0xF1870` | 206 | UnwindData |  |
| 344 | `zesGetFrequencyProcAddrTable` | `0xF1940` | 408 | UnwindData |  |
| 345 | `zesGetLedProcAddrTable` | `0xF1AE0` | 240 | UnwindData |  |
| 346 | `zesGetMemoryProcAddrTable` | `0xF1BD0` | 241 | UnwindData |  |
| 347 | `zesGetPerformanceFactorProcAddrTable` | `0xF1CD0` | 241 | UnwindData |  |
| 348 | `zesGetPowerProcAddrTable` | `0xF1DD0` | 266 | UnwindData |  |
| 349 | `zesGetPsuProcAddrTable` | `0xF1EE0` | 206 | UnwindData |  |
| 350 | `zesGetRasProcAddrTable` | `0xF1FB0` | 240 | UnwindData |  |
| 351 | `zesGetSchedulerProcAddrTable` | `0xF20A0` | 292 | UnwindData |  |
| 352 | `zesGetStandbyProcAddrTable` | `0xF21D0` | 241 | UnwindData |  |
| 353 | `zesGetTemperatureProcAddrTable` | `0xF22D0` | 240 | UnwindData |  |
| 275 | `zesDeviceEnumDiagnosticTestSuites` | `0xF23C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 276 | `zesDeviceEnumEngineGroups` | `0xF23D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 277 | `zesDeviceEnumFabricPorts` | `0xF23E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 278 | `zesDeviceEnumFans` | `0xF23F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 279 | `zesDeviceEnumFirmwares` | `0xF2400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 280 | `zesDeviceEnumFrequencyDomains` | `0xF2410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 281 | `zesDeviceEnumLeds` | `0xF2420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 282 | `zesDeviceEnumMemoryModules` | `0xF2430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 283 | `zesDeviceEnumPerformanceFactorDomains` | `0xF2440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 284 | `zesDeviceEnumPowerDomains` | `0xF2450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 285 | `zesDeviceEnumPsus` | `0xF2460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 286 | `zesDeviceEnumRasErrorSets` | `0xF2470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 287 | `zesDeviceEnumSchedulers` | `0xF2480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 288 | `zesDeviceEnumStandbyDomains` | `0xF2490` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 289 | `zesDeviceEnumTemperatureSensors` | `0xF24A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 290 | `zesDeviceEventRegister` | `0xF24B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 291 | `zesDeviceGetProperties` | `0xF24C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 292 | `zesDeviceGetState` | `0xF24D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 293 | `zesDevicePciGetBars` | `0xF24E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 294 | `zesDevicePciGetProperties` | `0xF24F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 295 | `zesDevicePciGetState` | `0xF2500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 296 | `zesDevicePciGetStats` | `0xF2510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 297 | `zesDeviceProcessesGetState` | `0xF2520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 298 | `zesDeviceReset` | `0xF2530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 299 | `zesDiagnosticsGetProperties` | `0xF2540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 300 | `zesDiagnosticsGetTests` | `0xF2550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 301 | `zesDiagnosticsRunTests` | `0xF2560` | 22 | UnwindData |  |
| 302 | `zesDriverEventListen` | `0xF2580` | 42 | UnwindData |  |
| 303 | `zesDriverEventListenEx` | `0xF25B0` | 42 | UnwindData |  |
| 304 | `zesEngineGetActivity` | `0xF25E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 305 | `zesEngineGetProperties` | `0xF25F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 306 | `zesFabricPortGetConfig` | `0xF2600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 307 | `zesFabricPortGetLinkType` | `0xF2610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 308 | `zesFabricPortGetProperties` | `0xF2620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 309 | `zesFabricPortGetState` | `0xF2630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 310 | `zesFabricPortGetThroughput` | `0xF2640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 311 | `zesFabricPortSetConfig` | `0xF2650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 312 | `zesFanGetConfig` | `0xF2660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 313 | `zesFanGetProperties` | `0xF2670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 314 | `zesFanGetState` | `0xF2680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 315 | `zesFanSetDefaultMode` | `0xF2690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 316 | `zesFanSetFixedSpeedMode` | `0xF26A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 317 | `zesFanSetSpeedTableMode` | `0xF26B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 318 | `zesFirmwareFlash` | `0xF26C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 319 | `zesFirmwareGetProperties` | `0xF26D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 320 | `zesFrequencyGetAvailableClocks` | `0xF26E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 321 | `zesFrequencyGetProperties` | `0xF26F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 322 | `zesFrequencyGetRange` | `0xF2700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 323 | `zesFrequencyGetState` | `0xF2710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 324 | `zesFrequencyGetThrottleTime` | `0xF2720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 325 | `zesFrequencyOcGetCapabilities` | `0xF2730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 326 | `zesFrequencyOcGetFrequencyTarget` | `0xF2740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 327 | `zesFrequencyOcGetIccMax` | `0xF2750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 328 | `zesFrequencyOcGetMode` | `0xF2760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 329 | `zesFrequencyOcGetTjMax` | `0xF2770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 330 | `zesFrequencyOcGetVoltageTarget` | `0xF2790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 331 | `zesFrequencyOcSetFrequencyTarget` | `0xF27A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 332 | `zesFrequencyOcSetIccMax` | `0xF27B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 333 | `zesFrequencyOcSetMode` | `0xF27C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 334 | `zesFrequencyOcSetTjMax` | `0xF27D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 335 | `zesFrequencyOcSetVoltageTarget` | `0xF27F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 336 | `zesFrequencySetRange` | `0xF2800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 354 | `zesLedGetProperties` | `0xF2810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 355 | `zesLedGetState` | `0xF2820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 356 | `zesLedSetColor` | `0xF2830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 357 | `zesLedSetState` | `0xF2840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 358 | `zesMemoryGetBandwidth` | `0xF2850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 359 | `zesMemoryGetProperties` | `0xF2860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 360 | `zesMemoryGetState` | `0xF2870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 361 | `zesPerformanceFactorGetConfig` | `0xF2880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 362 | `zesPerformanceFactorGetProperties` | `0xF2890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 363 | `zesPerformanceFactorSetConfig` | `0xF28A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 364 | `zesPowerGetEnergyCounter` | `0xF28B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 365 | `zesPowerGetEnergyThreshold` | `0xF28D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 366 | `zesPowerGetLimits` | `0xF28F0` | 38 | UnwindData |  |
| 367 | `zesPowerGetProperties` | `0xF2920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 368 | `zesPowerSetEnergyThreshold` | `0xF2940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 369 | `zesPowerSetLimits` | `0xF2960` | 38 | UnwindData |  |
| 370 | `zesPsuGetProperties` | `0xF2990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 371 | `zesPsuGetState` | `0xF29A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 372 | `zesRasGetConfig` | `0xF29B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 373 | `zesRasGetProperties` | `0xF29C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 374 | `zesRasGetState` | `0xF29D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 375 | `zesRasSetConfig` | `0xF29F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 376 | `zesSchedulerGetCurrentMode` | `0xF2A00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 377 | `zesSchedulerGetProperties` | `0xF2A10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 378 | `zesSchedulerGetTimeoutModeProperties` | `0xF2A20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 379 | `zesSchedulerGetTimesliceModeProperties` | `0xF2A30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 380 | `zesSchedulerSetComputeUnitDebugMode` | `0xF2A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 381 | `zesSchedulerSetExclusiveMode` | `0xF2A50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 382 | `zesSchedulerSetTimeoutMode` | `0xF2A60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 383 | `zesSchedulerSetTimesliceMode` | `0xF2A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 384 | `zesStandbyGetMode` | `0xF2A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 385 | `zesStandbyGetProperties` | `0xF2A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 386 | `zesStandbySetMode` | `0xF2AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 387 | `zesTemperatureGetConfig` | `0xF2AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 388 | `zesTemperatureGetProperties` | `0xF2AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 389 | `zesTemperatureGetState` | `0xF2AD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 390 | `zesTemperatureSetConfig` | `0xF2AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 408 | `zetGetCommandListProcAddrTable` | `0xF2AF0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 409 | `zetGetContextProcAddrTable` | `0xF2B50` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 410 | `zetGetDebugProcAddrTable` | `0xF2B90` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 411 | `zetGetDeviceProcAddrTable` | `0xF2C40` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 412 | `zetGetKernelProcAddrTable` | `0xF2C80` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 413 | `zetGetMetricGroupExpProcAddrTable` | `0xF2CC0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 414 | `zetGetMetricGroupProcAddrTable` | `0xF2D00` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 415 | `zetGetMetricProcAddrTable` | `0xF2D50` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 416 | `zetGetMetricQueryPoolProcAddrTable` | `0xF2DA0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 417 | `zetGetMetricQueryProcAddrTable` | `0xF2DF0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 418 | `zetGetMetricStreamerProcAddrTable` | `0xF2E50` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 419 | `zetGetModuleProcAddrTable` | `0xF2EA0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 420 | `zetGetTracerExpProcAddrTable` | `0xF2EE0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 396 | `zetDebugAcknowledgeEvent` | `0xF2F50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 397 | `zetDebugAttach` | `0xF2F60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 398 | `zetDebugDetach` | `0xF2F70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 399 | `zetDebugGetRegisterSetProperties` | `0xF2F80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 400 | `zetDebugInterrupt` | `0xF2F90` | 27 | UnwindData |  |
| 401 | `zetDebugReadEvent` | `0xF2FB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 402 | `zetDebugReadMemory` | `0xF2FC0` | 37 | UnwindData |  |
| 403 | `zetDebugReadRegisters` | `0xF2FF0` | 45 | UnwindData |  |
| 404 | `zetDebugResume` | `0xF3020` | 27 | UnwindData |  |
| 405 | `zetDebugWriteMemory` | `0xF3040` | 37 | UnwindData |  |
| 406 | `zetDebugWriteRegisters` | `0xF3070` | 45 | UnwindData |  |
| 407 | `zetDeviceGetDebugProperties` | `0xF30A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 391 | `zetCommandListAppendMetricMemoryBarrier` | `0xF30D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 392 | `zetCommandListAppendMetricQueryBegin` | `0xF3100` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 393 | `zetCommandListAppendMetricQueryEnd` | `0xF3130` | 57 | UnwindData |  |
| 394 | `zetCommandListAppendMetricStreamerMarker` | `0xF3170` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 395 | `zetContextActivateMetricGroups` | `0xF31A0` | 25 | UnwindData |  |
| 422 | `zetMetricGet` | `0xF31C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 423 | `zetMetricGetProperties` | `0xF31E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 424 | `zetMetricGroupCalculateMetricValues` | `0xF3200` | 71 | UnwindData |  |
| 426 | `zetMetricGroupGet` | `0xF3250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 427 | `zetMetricGroupGetProperties` | `0xF3260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 428 | `zetMetricQueryCreate` | `0xF3280` | 55 | UnwindData |  |
| 429 | `zetMetricQueryDestroy` | `0xF32C0` | 33 | UnwindData |  |
| 430 | `zetMetricQueryGetData` | `0xF32F0` | 57 | UnwindData |  |
| 431 | `zetMetricQueryPoolCreate` | `0xF3330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 432 | `zetMetricQueryPoolDestroy` | `0xF3340` | 33 | UnwindData |  |
| 433 | `zetMetricQueryReset` | `0xF3370` | 33 | UnwindData |  |
| 434 | `zetMetricStreamerClose` | `0xF33A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 435 | `zetMetricStreamerOpen` | `0xF33C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 436 | `zetMetricStreamerReadData` | `0xF33D0` | 38 | UnwindData |  |
| 421 | `zetKernelGetProfileInfo` | `0xF3400` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 437 | `zetModuleGetDebugInfo` | `0xF3430` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `zeEventQueryTimestampsExp` | `0xF3460` | 55 | UnwindData |  |
| 181 | `zeImageGetAllocPropertiesExt` | `0xF34A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 182 | `zeImageGetMemoryPropertiesExp` | `0xF34D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `zeImageViewCreateExp` | `0xF34F0` | 55 | UnwindData |  |
| 205 | `zeKernelSetGlobalOffsetExp` | `0xF3530` | 38 | UnwindData |  |
| 425 | `zetMetricGroupCalculateMultipleMetricValuesExp` | `0xF3560` | 103 | UnwindData |  |
