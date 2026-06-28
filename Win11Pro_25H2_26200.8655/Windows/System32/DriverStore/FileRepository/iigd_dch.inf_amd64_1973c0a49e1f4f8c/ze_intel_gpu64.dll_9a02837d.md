# Binary Specification: ze_intel_gpu64.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_1973c0a49e1f4f8c\ze_intel_gpu64.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9a02837da7b32a94cad5d4f206a52320032cb2755ae86c3077ee141204741495`
* **Total Exported Functions:** 465

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `zeCommandListAppendBarrier_Tracing` | `0x79A20` | 137 | UnwindData |  |
| 35 | `zeCommandListAppendMemoryRangesBarrier_Tracing` | `0x79DD0` | 191 | UnwindData |  |
| 37 | `zeCommandListAppendQueryKernelTimestamps_Tracing` | `0x7C7E0` | 219 | UnwindData |  |
| 43 | `zeCommandListAppendWriteGlobalTimestamp_Tracing` | `0x7CC00` | 157 | UnwindData |  |
| 45 | `zeCommandListClose_Tracing` | `0x7CFE0` | 113 | UnwindData |  |
| 48 | `zeCommandListCreateImmediate_Tracing` | `0x7D340` | 137 | UnwindData |  |
| 49 | `zeCommandListCreate_Tracing` | `0x7D6F0` | 137 | UnwindData |  |
| 51 | `zeCommandListDestroy_Tracing` | `0x7DAA0` | 113 | UnwindData |  |
| 53 | `zeCommandListReset_Tracing` | `0x7DE00` | 113 | UnwindData |  |
| 55 | `zeCommandQueueCreate_Tracing` | `0x7F6A0` | 137 | UnwindData |  |
| 57 | `zeCommandQueueDestroy_Tracing` | `0x7FA50` | 113 | UnwindData |  |
| 59 | `zeCommandQueueExecuteCommandLists_Tracing` | `0x7FDB0` | 135 | UnwindData |  |
| 61 | `zeCommandQueueSynchronize_Tracing` | `0x80160` | 121 | UnwindData |  |
| 8 | `zeCommandListAppendImageCopyFromMemory_Tracing` | `0x83FA0` | 193 | UnwindData |  |
| 10 | `zeCommandListAppendImageCopyRegion_Tracing` | `0x843C0` | 221 | UnwindData |  |
| 12 | `zeCommandListAppendImageCopyToMemory_Tracing` | `0x847F0` | 193 | UnwindData |  |
| 13 | `zeCommandListAppendImageCopy_Tracing` | `0x84C10` | 169 | UnwindData |  |
| 23 | `zeCommandListAppendMemAdvise_Tracing` | `0x85000` | 149 | UnwindData |  |
| 26 | `zeCommandListAppendMemoryCopyFromContext_Tracing` | `0x853D0` | 208 | UnwindData |  |
| 28 | `zeCommandListAppendMemoryCopyRegion_Tracing` | `0x85800` | 288 | UnwindData |  |
| 29 | `zeCommandListAppendMemoryCopy_Tracing` | `0x85CD0` | 193 | UnwindData |  |
| 31 | `zeCommandListAppendMemoryFill_Tracing` | `0x860F0` | 208 | UnwindData |  |
| 33 | `zeCommandListAppendMemoryPrefetch_Tracing` | `0x86520` | 129 | UnwindData |  |
| 80 | `zeDeviceCanAccessPeer_Tracing` | `0x8B770` | 129 | UnwindData |  |
| 83 | `zeDeviceGetCacheProperties_Tracing` | `0x8BB10` | 129 | UnwindData |  |
| 85 | `zeDeviceGetCommandQueueGroupProperties_Tracing` | `0x8BEB0` | 129 | UnwindData |  |
| 87 | `zeDeviceGetComputeProperties_Tracing` | `0x8C250` | 121 | UnwindData |  |
| 89 | `zeDeviceGetExternalMemoryProperties_Tracing` | `0x8C5D0` | 121 | UnwindData |  |
| 92 | `zeDeviceGetImageProperties_Tracing` | `0x8C960` | 121 | UnwindData |  |
| 94 | `zeDeviceGetMemoryAccessProperties_Tracing` | `0x8CCE0` | 121 | UnwindData |  |
| 96 | `zeDeviceGetMemoryProperties_Tracing` | `0x8D060` | 129 | UnwindData |  |
| 98 | `zeDeviceGetModuleProperties_Tracing` | `0x8D400` | 121 | UnwindData |  |
| 100 | `zeDeviceGetP2PProperties_Tracing` | `0x8D780` | 129 | UnwindData |  |
| 102 | `zeDeviceGetProperties_Tracing` | `0x8DB20` | 121 | UnwindData |  |
| 104 | `zeDeviceGetStatus_Tracing` | `0x8DEA0` | 113 | UnwindData |  |
| 106 | `zeDeviceGetSubDevices_Tracing` | `0x8E200` | 129 | UnwindData |  |
| 107 | `zeDeviceGet_Tracing` | `0x8E5A0` | 129 | UnwindData |  |
| 202 | `zeKernelSetCacheConfig_Tracing` | `0x8E940` | 119 | UnwindData |  |
| 112 | `zeDriverGetApiVersion_Tracing` | `0x906E0` | 121 | UnwindData |  |
| 115 | `zeDriverGetExtensionProperties_Tracing` | `0x90A60` | 129 | UnwindData |  |
| 117 | `zeDriverGetIpcProperties_Tracing` | `0x90E00` | 121 | UnwindData |  |
| 119 | `zeDriverGetProperties_Tracing` | `0x91180` | 121 | UnwindData |  |
| 120 | `zeDriverGet_Tracing` | `0x91500` | 121 | UnwindData |  |
| 5 | `zeCommandListAppendEventReset_Tracing` | `0x96760` | 121 | UnwindData |  |
| 39 | `zeCommandListAppendSignalEvent_Tracing` | `0x96AF0` | 121 | UnwindData |  |
| 41 | `zeCommandListAppendWaitOnEvents_Tracing` | `0x96E80` | 127 | UnwindData |  |
| 122 | `zeEventCreate_Tracing` | `0x97220` | 129 | UnwindData |  |
| 124 | `zeEventDestroy_Tracing` | `0x975C0` | 113 | UnwindData |  |
| 126 | `zeEventHostReset_Tracing` | `0x97920` | 113 | UnwindData |  |
| 128 | `zeEventHostSignal_Tracing` | `0x97C80` | 113 | UnwindData |  |
| 130 | `zeEventHostSynchronize_Tracing` | `0x97FE0` | 121 | UnwindData |  |
| 132 | `zeEventPoolCloseIpcHandle_Tracing` | `0x98370` | 113 | UnwindData |  |
| 134 | `zeEventPoolCreate_Tracing` | `0x986D0` | 157 | UnwindData |  |
| 136 | `zeEventPoolDestroy_Tracing` | `0x98AB0` | 113 | UnwindData |  |
| 138 | `zeEventPoolGetIpcHandle_Tracing` | `0x98E10` | 121 | UnwindData |  |
| 140 | `zeEventPoolOpenIpcHandle_Tracing` | `0x991A0` | 165 | UnwindData |  |
| 142 | `zeEventQueryKernelTimestamp_Tracing` | `0x99550` | 121 | UnwindData |  |
| 144 | `zeEventQueryStatus_Tracing` | `0x998E0` | 113 | UnwindData |  |
| 147 | `zeFenceCreate_Tracing` | `0x9B650` | 129 | UnwindData |  |
| 149 | `zeFenceDestroy_Tracing` | `0x9B9F0` | 113 | UnwindData |  |
| 151 | `zeFenceHostSynchronize_Tracing` | `0x9BD50` | 121 | UnwindData |  |
| 153 | `zeFenceQueryStatus_Tracing` | `0x9C0E0` | 113 | UnwindData |  |
| 155 | `zeFenceReset_Tracing` | `0x9C440` | 113 | UnwindData |  |
| 185 | `zeInit_Tracing` | `0x9CCD0` | 109 | UnwindData |  |
| 255 | `zeSamplerCreate_Tracing` | `0x9DAD0` | 137 | UnwindData |  |
| 257 | `zeSamplerDestroy_Tracing` | `0x9DE80` | 113 | UnwindData |  |
| 64 | `zeContextCreate_Tracing` | `0xA0C40` | 129 | UnwindData |  |
| 66 | `zeContextDestroy_Tracing` | `0xA0FE0` | 113 | UnwindData |  |
| 68 | `zeContextEvictImage_Tracing` | `0xA1340` | 129 | UnwindData |  |
| 70 | `zeContextEvictMemory_Tracing` | `0xA16E0` | 137 | UnwindData |  |
| 72 | `zeContextGetStatus_Tracing` | `0xA1A90` | 113 | UnwindData |  |
| 74 | `zeContextMakeImageResident_Tracing` | `0xA1DF0` | 129 | UnwindData |  |
| 76 | `zeContextMakeMemoryResident_Tracing` | `0xA2190` | 137 | UnwindData |  |
| 78 | `zeContextSystemBarrier_Tracing` | `0xA2540` | 121 | UnwindData |  |
| 177 | `zeImageCreate_Tracing` | `0xA38C0` | 137 | UnwindData |  |
| 179 | `zeImageDestroy_Tracing` | `0xA3C70` | 113 | UnwindData |  |
| 182 | `zeImageGetProperties_Tracing` | `0xA3FD0` | 129 | UnwindData |  |
| 213 | `zeMemAllocDevice_Tracing` | `0xAA5C0` | 181 | UnwindData |  |
| 215 | `zeMemAllocHost_Tracing` | `0xAA9B0` | 157 | UnwindData |  |
| 217 | `zeMemAllocShared_Tracing` | `0xAAD90` | 193 | UnwindData |  |
| 219 | `zeMemCloseIpcHandle_Tracing` | `0xAB1B0` | 121 | UnwindData |  |
| 221 | `zeMemFree_Tracing` | `0xAB540` | 121 | UnwindData |  |
| 223 | `zeMemGetAddressRange_Tracing` | `0xAB8D0` | 137 | UnwindData |  |
| 225 | `zeMemGetAllocProperties_Tracing` | `0xABC80` | 137 | UnwindData |  |
| 227 | `zeMemGetIpcHandle_Tracing` | `0xAC030` | 129 | UnwindData |  |
| 229 | `zeMemOpenIpcHandle_Tracing` | `0xAC3D0` | 194 | UnwindData |  |
| 251 | `zePhysicalMemCreate_Tracing` | `0xAC7C0` | 137 | UnwindData |  |
| 253 | `zePhysicalMemDestroy_Tracing` | `0xACB70` | 121 | UnwindData |  |
| 259 | `zeVirtualMemFree_Tracing` | `0xACF00` | 129 | UnwindData |  |
| 261 | `zeVirtualMemGetAccessAttribute_Tracing` | `0xAD2A0` | 157 | UnwindData |  |
| 263 | `zeVirtualMemMap_Tracing` | `0xAD680` | 161 | UnwindData |  |
| 265 | `zeVirtualMemQueryPageSize_Tracing` | `0xADA70` | 137 | UnwindData |  |
| 267 | `zeVirtualMemReserve_Tracing` | `0xADE20` | 137 | UnwindData |  |
| 269 | `zeVirtualMemSetAccessAttribute_Tracing` | `0xAE1D0` | 137 | UnwindData |  |
| 271 | `zeVirtualMemUnmap_Tracing` | `0xAE580` | 129 | UnwindData |  |
| 15 | `zeCommandListAppendLaunchCooperativeKernel_Tracing` | `0xB6FF0` | 169 | UnwindData |  |
| 18 | `zeCommandListAppendLaunchKernelIndirect_Tracing` | `0xB73E0` | 169 | UnwindData |  |
| 19 | `zeCommandListAppendLaunchKernel_Tracing` | `0xB77D0` | 169 | UnwindData |  |
| 21 | `zeCommandListAppendLaunchMultipleKernelsIndirect_Tracing` | `0xB7BC0` | 219 | UnwindData |  |
| 187 | `zeKernelCreate_Tracing` | `0xB7FE0` | 129 | UnwindData |  |
| 189 | `zeKernelDestroy_Tracing` | `0xB8380` | 113 | UnwindData |  |
| 191 | `zeKernelGetIndirectAccess_Tracing` | `0xB86E0` | 121 | UnwindData |  |
| 193 | `zeKernelGetName_Tracing` | `0xB8A70` | 129 | UnwindData |  |
| 195 | `zeKernelGetProperties_Tracing` | `0xB8E10` | 121 | UnwindData |  |
| 197 | `zeKernelGetSourceAttributes_Tracing` | `0xB91A0` | 129 | UnwindData |  |
| 200 | `zeKernelSetArgumentValue_Tracing` | `0xB9540` | 135 | UnwindData |  |
| 205 | `zeKernelSetGroupSize_Tracing` | `0xB98F0` | 135 | UnwindData |  |
| 207 | `zeKernelSetIndirectAccess_Tracing` | `0xB9CA0` | 119 | UnwindData |  |
| 209 | `zeKernelSuggestGroupSize_Tracing` | `0xBA030` | 204 | UnwindData |  |
| 211 | `zeKernelSuggestMaxCooperativeGroupCount_Tracing` | `0xBA440` | 121 | UnwindData |  |
| 231 | `zeModuleBuildLogDestroy_Tracing` | `0xBA7D0` | 113 | UnwindData |  |
| 233 | `zeModuleBuildLogGetString_Tracing` | `0xBAB30` | 129 | UnwindData |  |
| 235 | `zeModuleCreate_Tracing` | `0xBAED0` | 157 | UnwindData |  |
| 237 | `zeModuleDestroy_Tracing` | `0xBB2B0` | 113 | UnwindData |  |
| 239 | `zeModuleDynamicLink_Tracing` | `0xBB610` | 128 | UnwindData |  |
| 241 | `zeModuleGetFunctionPointer_Tracing` | `0xBB9B0` | 129 | UnwindData |  |
| 243 | `zeModuleGetGlobalPointer_Tracing` | `0xBBD50` | 137 | UnwindData |  |
| 245 | `zeModuleGetKernelNames_Tracing` | `0xBC100` | 129 | UnwindData |  |
| 247 | `zeModuleGetNativeBinary_Tracing` | `0xBC4A0` | 129 | UnwindData |  |
| 249 | `zeModuleGetProperties_Tracing` | `0xBC840` | 121 | UnwindData |  |
| 1 | `?zeDeviceSystemBarrier@@YA?AW4_ze_result_t@@PEAU_ze_device_handle_t@@@Z` | `0xD68D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `zeCommandListAppendBarrier` | `0xD6900` | 38 | UnwindData |  |
| 34 | `zeCommandListAppendMemoryRangesBarrier` | `0xD6930` | 82 | UnwindData |  |
| 36 | `zeCommandListAppendQueryKernelTimestamps` | `0xD6990` | 104 | UnwindData |  |
| 42 | `zeCommandListAppendWriteGlobalTimestamp` | `0xD6A00` | 57 | UnwindData |  |
| 44 | `zeCommandListClose` | `0xD6A40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `zeCommandListCreate` | `0xD6A60` | 25 | UnwindData |  |
| 47 | `zeCommandListCreateImmediate` | `0xD6A80` | 25 | UnwindData |  |
| 50 | `zeCommandListDestroy` | `0xD6AA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `zeCommandListReset` | `0xD6AC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `zeCommandQueueCreate` | `0xD6AF0` | 25 | UnwindData |  |
| 56 | `zeCommandQueueDestroy` | `0xD6B10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `zeCommandQueueExecuteCommandLists` | `0xD6B30` | 43 | UnwindData |  |
| 60 | `zeCommandQueueSynchronize` | `0xD6B60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `zeContextCreate` | `0xD6B80` | 33 | UnwindData |  |
| 63 | `zeContextCreateEx` | `0xD6BB0` | 32 | UnwindData |  |
| 65 | `zeContextDestroy` | `0xD6BD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `zeContextEvictImage` | `0xD6BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `zeContextEvictMemory` | `0xD6BF0` | 22 | UnwindData |  |
| 71 | `zeContextGetStatus` | `0xD6C10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `zeContextMakeImageResident` | `0xD6C20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `zeContextMakeMemoryResident` | `0xD6C30` | 22 | UnwindData |  |
| 77 | `zeContextSystemBarrier` | `0xD6C50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 250 | `zePhysicalMemCreate` | `0xD6C60` | 25 | UnwindData |  |
| 252 | `zePhysicalMemDestroy` | `0xD6C80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 258 | `zeVirtualMemFree` | `0xD6CA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 260 | `zeVirtualMemGetAccessAttribute` | `0xD6CC0` | 35 | UnwindData |  |
| 262 | `zeVirtualMemMap` | `0xD6CF0` | 45 | UnwindData |  |
| 264 | `zeVirtualMemQueryPageSize` | `0xD6D20` | 25 | UnwindData |  |
| 266 | `zeVirtualMemReserve` | `0xD6D40` | 25 | UnwindData |  |
| 268 | `zeVirtualMemSetAccessAttribute` | `0xD6D60` | 25 | UnwindData |  |
| 270 | `zeVirtualMemUnmap` | `0xD6D80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `zeCommandListAppendImageCopy` | `0xD6DA0` | 71 | UnwindData |  |
| 7 | `zeCommandListAppendImageCopyFromMemory` | `0xD6DF0` | 84 | UnwindData |  |
| 9 | `zeCommandListAppendImageCopyRegion` | `0xD6E50` | 103 | UnwindData |  |
| 11 | `zeCommandListAppendImageCopyToMemory` | `0xD6EC0` | 84 | UnwindData |  |
| 22 | `zeCommandListAppendMemAdvise` | `0xD6F20` | 54 | UnwindData |  |
| 24 | `zeCommandListAppendMemoryCopy` | `0xD6F60` | 84 | UnwindData |  |
| 25 | `zeCommandListAppendMemoryCopyFromContext` | `0xD6FC0` | 106 | UnwindData |  |
| 27 | `zeCommandListAppendMemoryCopyRegion` | `0xD7030` | 149 | UnwindData |  |
| 30 | `zeCommandListAppendMemoryFill` | `0xD70D0` | 106 | UnwindData |  |
| 32 | `zeCommandListAppendMemoryPrefetch` | `0xD7140` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `zeGetCommandListProcAddrTable` | `0xD7170` | 928 | UnwindData |  |
| 157 | `zeGetCommandQueueProcAddrTable` | `0xD7510` | 270 | UnwindData |  |
| 158 | `zeGetContextProcAddrTable` | `0xD7620` | 404 | UnwindData |  |
| 159 | `zeGetDeviceProcAddrTable` | `0xD77C0` | 612 | UnwindData |  |
| 160 | `zeGetDriverProcAddrTable` | `0xD7A30` | 314 | UnwindData |  |
| 161 | `zeGetEventExpProcAddrTable` | `0xD7B70` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 162 | `zeGetEventPoolProcAddrTable` | `0xD7BB0` | 305 | UnwindData |  |
| 163 | `zeGetEventProcAddrTable` | `0xD7CF0` | 360 | UnwindData |  |
| 164 | `zeGetFenceProcAddrTable` | `0xD7E60` | 305 | UnwindData |  |
| 165 | `zeGetGlobalProcAddrTable` | `0xD7FA0` | 191 | UnwindData |  |
| 166 | `zeGetImageExpProcAddrTable` | `0xD8060` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 167 | `zeGetImageProcAddrTable` | `0xD80B0` | 250 | UnwindData |  |
| 168 | `zeGetKernelExpProcAddrTable` | `0xD81B0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `zeGetKernelProcAddrTable` | `0xD8200` | 494 | UnwindData |  |
| 170 | `zeGetMemProcAddrTable` | `0xD83F0` | 415 | UnwindData |  |
| 171 | `zeGetModuleBuildLogProcAddrTable` | `0xD8590` | 215 | UnwindData |  |
| 172 | `zeGetModuleProcAddrTable` | `0xD8670` | 380 | UnwindData |  |
| 173 | `zeGetPhysicalMemProcAddrTable` | `0xD87F0` | 215 | UnwindData |  |
| 174 | `zeGetSamplerProcAddrTable` | `0xD88D0` | 215 | UnwindData |  |
| 175 | `zeGetVirtualMemProcAddrTable` | `0xD89B0` | 360 | UnwindData |  |
| 79 | `zeDeviceCanAccessPeer` | `0xD8B20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `zeDeviceGet` | `0xD8B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `zeDeviceGetCacheProperties` | `0xD8B50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `zeDeviceGetCommandQueueGroupProperties` | `0xD8B70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `zeDeviceGetComputeProperties` | `0xD8BA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `zeDeviceGetExternalMemoryProperties` | `0xD8BC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `zeDeviceGetGlobalTimestamps` | `0xD8BF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `zeDeviceGetImageProperties` | `0xD8C20` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `zeDeviceGetMemoryAccessProperties` | `0xD8C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `zeDeviceGetMemoryProperties` | `0xD8C70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `zeDeviceGetModuleProperties` | `0xD8C90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `zeDeviceGetP2PProperties` | `0xD8CB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `zeDeviceGetProperties` | `0xD8CD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `zeDeviceGetStatus` | `0xD8CF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `zeDeviceGetSubDevices` | `0xD8D00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `zeDeviceReserveCacheExt` | `0xD8D20` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `zeDeviceSetCacheAdviceExt` | `0xD8D50` | 41 | UnwindData |  |
| 110 | `zeDriverGet` | `0xD8D80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `zeDriverGetApiVersion` | `0xD8D90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `zeDriverGetExtensionFunctionAddress` | `0xD8DA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `zeDriverGetExtensionProperties` | `0xD8DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `zeDriverGetIpcProperties` | `0xD8DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `zeDriverGetProperties` | `0xD8DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | `zeInit` | `0xD8DE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `zeCommandListAppendEventReset` | `0xD8DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `zeCommandListAppendSignalEvent` | `0xD8E10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `zeCommandListAppendWaitOnEvents` | `0xD8E40` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `zeEventCreate` | `0xD8E70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `zeEventDestroy` | `0xD8E90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `zeEventHostReset` | `0xD8EB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `zeEventHostSignal` | `0xD8ED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `zeEventHostSynchronize` | `0xD8EF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `zeEventPoolCloseIpcHandle` | `0xD8F10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `zeEventPoolCreate` | `0xD8F30` | 35 | UnwindData |  |
| 135 | `zeEventPoolDestroy` | `0xD8F60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `zeEventPoolGetIpcHandle` | `0xD8F80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `zeEventPoolOpenIpcHandle` | `0xD8FA0` | 65 | UnwindData |  |
| 141 | `zeEventQueryKernelTimestamp` | `0xD8FF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `zeEventQueryStatus` | `0xD9010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `zeFenceCreate` | `0xD9030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 148 | `zeFenceDestroy` | `0xD9050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `zeFenceHostSynchronize` | `0xD9070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `zeFenceQueryStatus` | `0xD9090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `zeFenceReset` | `0xD90B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `zeImageCreate` | `0xD90D0` | 25 | UnwindData |  |
| 178 | `zeImageDestroy` | `0xD90F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `zeImageGetProperties` | `0xD9110` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 212 | `zeMemAllocDevice` | `0xD9140` | 48 | UnwindData |  |
| 214 | `zeMemAllocHost` | `0xD9170` | 32 | UnwindData |  |
| 216 | `zeMemAllocShared` | `0xD9190` | 61 | UnwindData |  |
| 218 | `zeMemCloseIpcHandle` | `0xD91D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 220 | `zeMemFree` | `0xD91E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `zeMemGetAddressRange` | `0xD91F0` | 22 | UnwindData |  |
| 224 | `zeMemGetAllocProperties` | `0xD9210` | 25 | UnwindData |  |
| 226 | `zeMemGetIpcHandle` | `0xD9230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 228 | `zeMemOpenIpcHandle` | `0xD9240` | 85 | UnwindData |  |
| 14 | `zeCommandListAppendLaunchCooperativeKernel` | `0xD92A0` | 71 | UnwindData |  |
| 16 | `zeCommandListAppendLaunchKernel` | `0xD92F0` | 71 | UnwindData |  |
| 17 | `zeCommandListAppendLaunchKernelIndirect` | `0xD9340` | 71 | UnwindData |  |
| 20 | `zeCommandListAppendLaunchMultipleKernelsIndirect` | `0xD9390` | 101 | UnwindData |  |
| 186 | `zeKernelCreate` | `0xD9400` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 188 | `zeKernelDestroy` | `0xD9420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `zeKernelGetIndirectAccess` | `0xD9440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 192 | `zeKernelGetName` | `0xD9460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 194 | `zeKernelGetProperties` | `0xD9480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 196 | `zeKernelGetSourceAttributes` | `0xD94A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 198 | `zeKernelSchedulingHintExp` | `0xD94C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 199 | `zeKernelSetArgumentValue` | `0xD94F0` | 38 | UnwindData |  |
| 201 | `zeKernelSetCacheConfig` | `0xD9520` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 204 | `zeKernelSetGroupSize` | `0xD9550` | 38 | UnwindData |  |
| 206 | `zeKernelSetIndirectAccess` | `0xD9580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 208 | `zeKernelSuggestGroupSize` | `0xD95A0` | 84 | UnwindData |  |
| 210 | `zeKernelSuggestMaxCooperativeGroupCount` | `0xD9600` | 44 | UnwindData |  |
| 230 | `zeModuleBuildLogDestroy` | `0xD9630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 232 | `zeModuleBuildLogGetString` | `0xD9650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 234 | `zeModuleCreate` | `0xD9670` | 35 | UnwindData |  |
| 236 | `zeModuleDestroy` | `0xD96A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 238 | `zeModuleDynamicLink` | `0xD96C0` | 51 | UnwindData |  |
| 240 | `zeModuleGetFunctionPointer` | `0xD9700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 242 | `zeModuleGetGlobalPointer` | `0xD9720` | 38 | UnwindData |  |
| 244 | `zeModuleGetKernelNames` | `0xD9750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 246 | `zeModuleGetNativeBinary` | `0xD9770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 248 | `zeModuleGetProperties` | `0xD9790` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 254 | `zeSamplerCreate` | `0xD97B0` | 25 | UnwindData |  |
| 256 | `zeSamplerDestroy` | `0xD97D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 461 | `zexGetCommandGraphProcAddrTable` | `0xD97F0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 462 | `zexGetCommandListProcAddrTable` | `0xD9870` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 463 | `zexGetCommandQueueProcAddrTable` | `0xD98F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 464 | `zexGetGlobalProcAddrTable` | `0xD9920` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 439 | `zexCommandGraphClose` | `0xD9950` | 64 | UnwindData |  |
| 440 | `zexCommandGraphCloseNode` | `0xD9990` | 221 | UnwindData |  |
| 441 | `zexCommandGraphCreate` | `0xD9A70` | 99 | UnwindData |  |
| 442 | `zexCommandGraphCreateLoadRegImemNode` | `0xD9AE0` | 123 | UnwindData |  |
| 443 | `zexCommandGraphCreateNode` | `0xD9B60` | 125 | UnwindData |  |
| 444 | `zexCommandGraphCreateStoreRegImemNode` | `0xD9BE0` | 123 | UnwindData |  |
| 445 | `zexCommandGraphDestroy` | `0xD9C60` | 65 | UnwindData |  |
| 446 | `zexCommandGraphNodeAddChildren` | `0xD9CB0` | 82 | UnwindData |  |
| 447 | `zexCommandGraphOpenNode` | `0xD9D10` | 90 | UnwindData |  |
| 448 | `zexCommandListAppendMILoadRegImm` | `0xD9D70` | 68 | UnwindData |  |
| 449 | `zexCommandListAppendMILoadRegMem` | `0xD9DC0` | 68 | UnwindData |  |
| 450 | `zexCommandListAppendMILoadRegReg` | `0xD9E10` | 68 | UnwindData |  |
| 451 | `zexCommandListAppendMIMath` | `0xD9E60` | 68 | UnwindData |  |
| 452 | `zexCommandListAppendMIStoreRegMem` | `0xD9EB0` | 68 | UnwindData |  |
| 453 | `zexCommandListAppendPipeControl` | `0xD9F00` | 68 | UnwindData |  |
| 454 | `zexCommandListAppendWaitOnMemory` | `0xD9F50` | 84 | UnwindData |  |
| 455 | `zexCommandListAppendWriteToMemory` | `0xD9FB0` | 68 | UnwindData |  |
| 456 | `zexCommandListReserveSpace` | `0xDA000` | 93 | UnwindData |  |
| 457 | `zexCommandQueueExecuteCommandGraphs` | `0xDA060` | 77 | UnwindData |  |
| 458 | `zexDriverGetHostPointerBaseAddress` | `0xDA0B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 459 | `zexDriverImportExternalPointer` | `0xDA0D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 460 | `zexDriverReleaseImportedPointer` | `0xDA0F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 465 | `zexInit` | `0xDA110` | 41 | UnwindData |  |
| 434 | `zetTracerExpCreate` | `0xDA140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 435 | `zetTracerExpDestroy` | `0xDA150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 436 | `zetTracerExpSetEnabled` | `0xDA170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 437 | `zetTracerExpSetEpilogues` | `0xDA190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 438 | `zetTracerExpSetPrologues` | `0xDA1B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 334 | `zesGetDeviceProcAddrTable` | `0xDA1D0` | 592 | UnwindData |  |
| 335 | `zesGetDiagnosticsProcAddrTable` | `0xDA420` | 241 | UnwindData |  |
| 336 | `zesGetDriverProcAddrTable` | `0xDA520` | 206 | UnwindData |  |
| 337 | `zesGetEngineProcAddrTable` | `0xDA5F0` | 206 | UnwindData |  |
| 338 | `zesGetFabricPortProcAddrTable` | `0xDA6C0` | 266 | UnwindData |  |
| 339 | `zesGetFanProcAddrTable` | `0xDA7D0` | 266 | UnwindData |  |
| 340 | `zesGetFirmwareProcAddrTable` | `0xDA8E0` | 206 | UnwindData |  |
| 341 | `zesGetFrequencyProcAddrTable` | `0xDA9B0` | 408 | UnwindData |  |
| 342 | `zesGetLedProcAddrTable` | `0xDAB50` | 240 | UnwindData |  |
| 343 | `zesGetMemoryProcAddrTable` | `0xDAC40` | 241 | UnwindData |  |
| 344 | `zesGetPerformanceFactorProcAddrTable` | `0xDAD40` | 241 | UnwindData |  |
| 345 | `zesGetPowerProcAddrTable` | `0xDAE40` | 266 | UnwindData |  |
| 346 | `zesGetPsuProcAddrTable` | `0xDAF50` | 206 | UnwindData |  |
| 347 | `zesGetRasProcAddrTable` | `0xDB020` | 240 | UnwindData |  |
| 348 | `zesGetSchedulerProcAddrTable` | `0xDB110` | 292 | UnwindData |  |
| 349 | `zesGetStandbyProcAddrTable` | `0xDB240` | 241 | UnwindData |  |
| 350 | `zesGetTemperatureProcAddrTable` | `0xDB340` | 240 | UnwindData |  |
| 272 | `zesDeviceEnumDiagnosticTestSuites` | `0xDB430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 273 | `zesDeviceEnumEngineGroups` | `0xDB440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 274 | `zesDeviceEnumFabricPorts` | `0xDB450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 275 | `zesDeviceEnumFans` | `0xDB460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 276 | `zesDeviceEnumFirmwares` | `0xDB470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 277 | `zesDeviceEnumFrequencyDomains` | `0xDB480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 278 | `zesDeviceEnumLeds` | `0xDB490` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 279 | `zesDeviceEnumMemoryModules` | `0xDB4A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 280 | `zesDeviceEnumPerformanceFactorDomains` | `0xDB4B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 281 | `zesDeviceEnumPowerDomains` | `0xDB4C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 282 | `zesDeviceEnumPsus` | `0xDB4D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 283 | `zesDeviceEnumRasErrorSets` | `0xDB4E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 284 | `zesDeviceEnumSchedulers` | `0xDB4F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 285 | `zesDeviceEnumStandbyDomains` | `0xDB500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 286 | `zesDeviceEnumTemperatureSensors` | `0xDB510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 287 | `zesDeviceEventRegister` | `0xDB520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 288 | `zesDeviceGetProperties` | `0xDB530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 289 | `zesDeviceGetState` | `0xDB540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 290 | `zesDevicePciGetBars` | `0xDB550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 291 | `zesDevicePciGetProperties` | `0xDB560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 292 | `zesDevicePciGetState` | `0xDB570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 293 | `zesDevicePciGetStats` | `0xDB580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 294 | `zesDeviceProcessesGetState` | `0xDB590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 295 | `zesDeviceReset` | `0xDB5A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 296 | `zesDiagnosticsGetProperties` | `0xDB5B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 297 | `zesDiagnosticsGetTests` | `0xDB5C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 298 | `zesDiagnosticsRunTests` | `0xDB5D0` | 22 | UnwindData |  |
| 299 | `zesDriverEventListen` | `0xDB5F0` | 42 | UnwindData |  |
| 300 | `zesDriverEventListenEx` | `0xDB620` | 42 | UnwindData |  |
| 301 | `zesEngineGetActivity` | `0xDB650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 302 | `zesEngineGetProperties` | `0xDB660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 303 | `zesFabricPortGetConfig` | `0xDB670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 304 | `zesFabricPortGetLinkType` | `0xDB680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 305 | `zesFabricPortGetProperties` | `0xDB690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 306 | `zesFabricPortGetState` | `0xDB6A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 307 | `zesFabricPortGetThroughput` | `0xDB6B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 308 | `zesFabricPortSetConfig` | `0xDB6C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 309 | `zesFanGetConfig` | `0xDB6D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 310 | `zesFanGetProperties` | `0xDB6E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 311 | `zesFanGetState` | `0xDB6F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 312 | `zesFanSetDefaultMode` | `0xDB700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 313 | `zesFanSetFixedSpeedMode` | `0xDB710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 314 | `zesFanSetSpeedTableMode` | `0xDB720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 315 | `zesFirmwareFlash` | `0xDB730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 316 | `zesFirmwareGetProperties` | `0xDB740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 317 | `zesFrequencyGetAvailableClocks` | `0xDB750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 318 | `zesFrequencyGetProperties` | `0xDB760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 319 | `zesFrequencyGetRange` | `0xDB770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 320 | `zesFrequencyGetState` | `0xDB780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 321 | `zesFrequencyGetThrottleTime` | `0xDB790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 322 | `zesFrequencyOcGetCapabilities` | `0xDB7A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 323 | `zesFrequencyOcGetFrequencyTarget` | `0xDB7B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 324 | `zesFrequencyOcGetIccMax` | `0xDB7C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 325 | `zesFrequencyOcGetMode` | `0xDB7D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 326 | `zesFrequencyOcGetTjMax` | `0xDB7E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 327 | `zesFrequencyOcGetVoltageTarget` | `0xDB800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 328 | `zesFrequencyOcSetFrequencyTarget` | `0xDB810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 329 | `zesFrequencyOcSetIccMax` | `0xDB820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 330 | `zesFrequencyOcSetMode` | `0xDB830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 331 | `zesFrequencyOcSetTjMax` | `0xDB840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 332 | `zesFrequencyOcSetVoltageTarget` | `0xDB860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 333 | `zesFrequencySetRange` | `0xDB870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 351 | `zesLedGetProperties` | `0xDB880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 352 | `zesLedGetState` | `0xDB890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 353 | `zesLedSetColor` | `0xDB8A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 354 | `zesLedSetState` | `0xDB8B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 355 | `zesMemoryGetBandwidth` | `0xDB8C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 356 | `zesMemoryGetProperties` | `0xDB8D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 357 | `zesMemoryGetState` | `0xDB8E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 358 | `zesPerformanceFactorGetConfig` | `0xDB8F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 359 | `zesPerformanceFactorGetProperties` | `0xDB900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 360 | `zesPerformanceFactorSetConfig` | `0xDB910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 361 | `zesPowerGetEnergyCounter` | `0xDB920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 362 | `zesPowerGetEnergyThreshold` | `0xDB940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 363 | `zesPowerGetLimits` | `0xDB960` | 38 | UnwindData |  |
| 364 | `zesPowerGetProperties` | `0xDB990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 365 | `zesPowerSetEnergyThreshold` | `0xDB9B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 366 | `zesPowerSetLimits` | `0xDB9D0` | 38 | UnwindData |  |
| 367 | `zesPsuGetProperties` | `0xDBA00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 368 | `zesPsuGetState` | `0xDBA10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 369 | `zesRasGetConfig` | `0xDBA20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 370 | `zesRasGetProperties` | `0xDBA30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 371 | `zesRasGetState` | `0xDBA40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 372 | `zesRasSetConfig` | `0xDBA60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 373 | `zesSchedulerGetCurrentMode` | `0xDBA70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 374 | `zesSchedulerGetProperties` | `0xDBA80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 375 | `zesSchedulerGetTimeoutModeProperties` | `0xDBA90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 376 | `zesSchedulerGetTimesliceModeProperties` | `0xDBAA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 377 | `zesSchedulerSetComputeUnitDebugMode` | `0xDBAB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 378 | `zesSchedulerSetExclusiveMode` | `0xDBAC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 379 | `zesSchedulerSetTimeoutMode` | `0xDBAD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 380 | `zesSchedulerSetTimesliceMode` | `0xDBAE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 381 | `zesStandbyGetMode` | `0xDBAF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 382 | `zesStandbyGetProperties` | `0xDBB00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 383 | `zesStandbySetMode` | `0xDBB10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 384 | `zesTemperatureGetConfig` | `0xDBB20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 385 | `zesTemperatureGetProperties` | `0xDBB30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 386 | `zesTemperatureGetState` | `0xDBB40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 387 | `zesTemperatureSetConfig` | `0xDBB50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 405 | `zetGetCommandListProcAddrTable` | `0xDBB60` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 406 | `zetGetContextProcAddrTable` | `0xDBBC0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 407 | `zetGetDebugProcAddrTable` | `0xDBC00` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 408 | `zetGetDeviceProcAddrTable` | `0xDBCB0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 409 | `zetGetKernelProcAddrTable` | `0xDBCF0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 410 | `zetGetMetricGroupProcAddrTable` | `0xDBD30` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 411 | `zetGetMetricProcAddrTable` | `0xDBD80` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 412 | `zetGetMetricQueryPoolProcAddrTable` | `0xDBDD0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 413 | `zetGetMetricQueryProcAddrTable` | `0xDBE20` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 414 | `zetGetMetricStreamerProcAddrTable` | `0xDBE80` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 415 | `zetGetModuleProcAddrTable` | `0xDBED0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 416 | `zetGetTracerExpProcAddrTable` | `0xDBF10` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 393 | `zetDebugAcknowledgeEvent` | `0xDBF80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 394 | `zetDebugAttach` | `0xDBF90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 395 | `zetDebugDetach` | `0xDBFA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 396 | `zetDebugGetRegisterSetProperties` | `0xDBFB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 397 | `zetDebugInterrupt` | `0xDBFC0` | 27 | UnwindData |  |
| 398 | `zetDebugReadEvent` | `0xDBFE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 399 | `zetDebugReadMemory` | `0xDBFF0` | 37 | UnwindData |  |
| 400 | `zetDebugReadRegisters` | `0xDC020` | 45 | UnwindData |  |
| 401 | `zetDebugResume` | `0xDC050` | 27 | UnwindData |  |
| 402 | `zetDebugWriteMemory` | `0xDC070` | 37 | UnwindData |  |
| 403 | `zetDebugWriteRegisters` | `0xDC0A0` | 45 | UnwindData |  |
| 404 | `zetDeviceGetDebugProperties` | `0xDC0D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 388 | `zetCommandListAppendMetricMemoryBarrier` | `0xDC100` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 389 | `zetCommandListAppendMetricQueryBegin` | `0xDC130` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 390 | `zetCommandListAppendMetricQueryEnd` | `0xDC160` | 57 | UnwindData |  |
| 391 | `zetCommandListAppendMetricStreamerMarker` | `0xDC1A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 392 | `zetContextActivateMetricGroups` | `0xDC1D0` | 25 | UnwindData |  |
| 418 | `zetMetricGet` | `0xDC1F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 419 | `zetMetricGetProperties` | `0xDC210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 420 | `zetMetricGroupCalculateMetricValues` | `0xDC230` | 71 | UnwindData |  |
| 422 | `zetMetricGroupGet` | `0xDC280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 423 | `zetMetricGroupGetProperties` | `0xDC290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 424 | `zetMetricQueryCreate` | `0xDC2B0` | 55 | UnwindData |  |
| 425 | `zetMetricQueryDestroy` | `0xDC2F0` | 33 | UnwindData |  |
| 426 | `zetMetricQueryGetData` | `0xDC320` | 57 | UnwindData |  |
| 427 | `zetMetricQueryPoolCreate` | `0xDC360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 428 | `zetMetricQueryPoolDestroy` | `0xDC370` | 33 | UnwindData |  |
| 429 | `zetMetricQueryReset` | `0xDC3A0` | 33 | UnwindData |  |
| 430 | `zetMetricStreamerClose` | `0xDC3D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 431 | `zetMetricStreamerOpen` | `0xDC3F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 432 | `zetMetricStreamerReadData` | `0xDC400` | 38 | UnwindData |  |
| 417 | `zetKernelGetProfileInfo` | `0xDC430` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 433 | `zetModuleGetDebugInfo` | `0xDC460` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `zeEventQueryTimestampsExp` | `0xDC490` | 55 | UnwindData |  |
| 180 | `zeImageGetMemoryPropertiesExp` | `0xDC4D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `zeImageViewCreateExp` | `0xDC4F0` | 55 | UnwindData |  |
| 203 | `zeKernelSetGlobalOffsetExp` | `0xDC530` | 38 | UnwindData |  |
| 421 | `zetMetricGroupCalculateMultipleMetricValuesExp` | `0xDC560` | 103 | UnwindData |  |
