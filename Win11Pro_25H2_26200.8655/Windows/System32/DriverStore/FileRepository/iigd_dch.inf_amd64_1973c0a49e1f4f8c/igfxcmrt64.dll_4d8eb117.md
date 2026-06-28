# Binary Specification: igfxcmrt64.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_1973c0a49e1f4f8c\igfxcmrt64.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4d8eb117cb55f0b1afbc3683055bc92d6fe34a68aca7bebe4314c910f0303ec3`
* **Total Exported Functions:** 129

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `??0CM_FLAG@@QEAA@XZ` | `0x12B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `CMRT_CreateBuffer` | `0x12C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `CMRT_DestroyEvent` | `0x12C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `CMRT_CreateKernel` | `0x12E0` | 51 | UnwindData |  |
| 91 | `CMRT_CreateQueue` | `0x1320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `CMRT_CreateSurface2D` | `0x1340` | 51 | UnwindData |  |
| 93 | `CMRT_CreateSurface3D` | `0x1380` | 59 | UnwindData |  |
| 94 | `CMRT_CreateTask` | `0x13C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `CMRT_CreateThreadSpace` | `0x13E0` | 40 | UnwindData |  |
| 96 | `CMRT_DestroyBuffer` | `0x1410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `CMRT_DestroyProgram` | `0x1430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `CMRT_DestroySurface2D` | `0x1450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `CMRT_DestroySurface3D` | `0x1470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `CMRT_DestroyTask` | `0x1490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `CMRT_DestroyThreadSpace` | `0x14B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `CMRT_LoadProgram` | `0x14D0` | 51 | UnwindData |  |
| 129 | `GetCmErrorString` | `0x1510` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `??0CM_AVS_STATE_MSG_EX@@QEAA@XZ` | `0x1550` | 1,872 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `?CloneKernel@CmDevice_RT@@UEAAHAEAPEAVCmKernel@@PEAV2@@Z` | `0x1CA0` | 86 | UnwindData |  |
| 4 | `?CreateBuffer@CmDevice_RT@@UEAAHIAEAPEAVCmBuffer@@@Z` | `0x1D00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `?CreateBufferAlias@CmDevice_RT@@UEAAHPEAVCmBuffer@@AEAPEAVSurfaceIndex@@@Z` | `0x1D10` | 88 | UnwindData |  |
| 6 | `?CreateBufferSVM@CmDevice_RT@@UEAAHIAEAPEAXIAEAPEAVCmBufferSVM@@@Z` | `0x1D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `?CreateBufferStateless@CmDevice_RT@@UEAAH_KIPEAXAEAPEAVCmBufferStateless@@@Z` | `0x1D80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `?CreateBufferUP@CmDevice_RT@@UEAAHIPEAXAEAPEAVCmBufferUP@@@Z` | `0x1D90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `?CreateHevcVmeSurfaceG10@CmDevice_RT@@UEAAHPEAVCmSurface2D@@PEAPEAV2@1IIAEAPEAVSurfaceIndex@@@Z` | `0x1DA0` | 134 | UnwindData |  |
| 10 | `?CreateKernel@CmDevice_RT@@UEAAHPEAVCmProgram@@PEBDAEAPEAVCmKernel@@1@Z` | `0x1E30` | 113 | UnwindData |  |
| 11 | `?CreateKernel@CmDevice_RT@@UEAAHPEAVCmProgram@@PEBDPEBXAEAPEAVCmKernel@@1@Z` | `0x1EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `?CreateQueue@CmDevice_RT@@UEAAHAEAPEAVCmQueue@@@Z` | `0x1EC0` | 104 | UnwindData |  |
| 13 | `?CreateQueueEx@CmDevice_RT@@UEAAHAEAPEAVCmQueue@@UCM_QUEUE_CREATE_OPTION@@@Z` | `0x1F30` | 332 | UnwindData |  |
| 14 | `?CreateSampler8x8@CmDevice_RT@@UEAAHAEBUCM_SAMPLER_8X8_DESCR@@AEAPEAVCmSampler8x8@@@Z` | `0x2080` | 190 | UnwindData |  |
| 15 | `?CreateSampler8x8Surface@CmDevice_RT@@UEAAHPEAVCmSurface2D@@AEAPEAVSurfaceIndex@@W4_CM_SAMPLER8x8_SURFACE_@@W4_CM_SURFACE_ADDRESS_CONTROL_MODE_@@@Z` | `0x2140` | 111 | UnwindData |  |
| 16 | `?CreateSampler8x8SurfaceEx@CmDevice_RT@@UEAAHPEAVCmSurface2D@@AEAPEAVSurfaceIndex@@W4_CM_SAMPLER8x8_SURFACE_@@W4_CM_SURFACE_ADDRESS_CONTROL_MODE_@@PEAUCM_FLAG@@@Z` | `0x21B0` | 124 | UnwindData |  |
| 17 | `?CreateSampler@CmDevice_RT@@UEAAHAEBU_CM_SAMPLER_STATE@@AEAPEAVCmSampler@@@Z` | `0x2230` | 131 | UnwindData |  |
| 18 | `?CreateSamplerEx@CmDevice_RT@@UEAAHAEBU_CM_SAMPLER_STATE_EX@@AEAPEAVCmSampler@@@Z` | `0x22C0` | 143 | UnwindData |  |
| 19 | `?CreateSamplerSurface2D@CmDevice_RT@@UEAAHPEAVCmSurface2D@@AEAPEAVSurfaceIndex@@@Z` | `0x2350` | 96 | UnwindData |  |
| 20 | `?CreateSamplerSurface2DEx@CmDevice_RT@@UEAAHPEAVCmSurface2D@@AEAPEAVSurfaceIndex@@PEAUCM_FLAG@@@Z` | `0x23B0` | 101 | UnwindData |  |
| 21 | `?CreateSamplerSurface2DUP@CmDevice_RT@@UEAAHPEAVCmSurface2DUP@@AEAPEAVSurfaceIndex@@@Z` | `0x2420` | 82 | UnwindData |  |
| 22 | `?CreateSamplerSurface3D@CmDevice_RT@@UEAAHPEAVCmSurface3D@@AEAPEAVSurfaceIndex@@@Z` | `0x2480` | 82 | UnwindData |  |
| 23 | `?CreateSurface2D@CmDevice_RT@@UEAAHIIW4_D3DFORMAT@@AEAPEAVCmSurface2D@@@Z` | `0x24E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `?CreateSurface2DAlias@CmDevice_RT@@UEAAHPEAVCmSurface2D@@AEAPEAVSurfaceIndex@@@Z` | `0x24F0` | 88 | UnwindData |  |
| 27 | `?CreateSurface2DStateless@CmDevice_RT@@UEAAHIIAEAIAEAPEAVCmSurface2DStateless@@@Z` | `0x2550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `?DestroySurface2DStateless@CmDevice_RT@@UEAAHAEAPEAVCmSurface2DStateless@@@Z` | `0x2550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `?SetResidentGroupAndParallelThreadNum@CmQueue_RT@@UEAAHII@Z` | `0x2550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `?CreateSurface2DUP@CmDevice_RT@@UEAAHIIW4_D3DFORMAT@@PEAXAEAPEAVCmSurface2DUP@@@Z` | `0x2560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `?CreateSurface3D@CmDevice_RT@@UEAAHIIIW4_D3DFORMAT@@AEAPEAVCmSurface3D@@@Z` | `0x2570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `?CreateTask@CmDevice_RT@@UEAAHAEAPEAVCmTask@@@Z` | `0x2580` | 103 | UnwindData |  |
| 31 | `?CreateThreadGroupSpace@CmDevice_RT@@UEAAHIIIIAEAPEAVCmThreadGroupSpace@@@Z` | `0x25F0` | 119 | UnwindData |  |
| 32 | `?CreateThreadGroupSpaceEx@CmDevice_RT@@UEAAHIIIIIIAEAPEAVCmThreadGroupSpace@@@Z` | `0x2670` | 125 | UnwindData |  |
| 33 | `?CreateThreadSpace@CmDevice_RT@@UEAAHIIAEAPEAVCmThreadSpace@@@Z` | `0x26F0` | 85 | UnwindData |  |
| 34 | `?CreateVebox@CmDevice_RT@@UEAAHAEAPEAVCmVebox@@@Z` | `0x2750` | 75 | UnwindData |  |
| 35 | `?CreateVmeSurfaceG7_5@CmDevice_RT@@UEAAHPEAVCmSurface2D@@PEAPEAV2@1IIAEAPEAVSurfaceIndex@@@Z` | `0x27A0` | 134 | UnwindData |  |
| 36 | `?DestroyBufferSVM@CmDevice_RT@@UEAAHAEAPEAVCmBufferSVM@@@Z` | `0x2830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `?DestroyBufferStateless@CmDevice_RT@@UEAAHAEAPEAVCmBufferStateless@@@Z` | `0x2840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `?DestroyBufferUP@CmDevice_RT@@UEAAHAEAPEAVCmBufferUP@@@Z` | `0x2850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `?DestroyHevcVmeSurfaceG10@CmDevice_RT@@UEAAHAEAPEAVSurfaceIndex@@@Z` | `0x2860` | 85 | UnwindData |  |
| 57 | `?DestroyVmeSurfaceG7_5@CmDevice_RT@@UEAAHAEAPEAVSurfaceIndex@@@Z` | `0x2860` | 85 | UnwindData |  |
| 42 | `?DestroyKernel@CmDevice_RT@@UEAAHAEAPEAVCmKernel@@@Z` | `0x28C0` | 83 | UnwindData |  |
| 43 | `?DestroyProgram@CmDevice_RT@@UEAAHAEAPEAVCmProgram@@@Z` | `0x2920` | 100 | UnwindData |  |
| 44 | `?DestroySampler8x8@CmDevice_RT@@UEAAHAEAPEAVCmSampler8x8@@@Z` | `0x2990` | 83 | UnwindData |  |
| 45 | `?DestroySampler8x8Surface@CmDevice_RT@@UEAAHAEAPEAVSurfaceIndex@@@Z` | `0x29F0` | 83 | UnwindData |  |
| 46 | `?DestroySampler@CmDevice_RT@@UEAAHAEAPEAVCmSampler@@@Z` | `0x2A50` | 83 | UnwindData |  |
| 47 | `?DestroySamplerSurface@CmDevice_RT@@UEAAHAEAPEAVSurfaceIndex@@@Z` | `0x2AB0` | 62 | UnwindData |  |
| 49 | `?DestroySurface2DUP@CmDevice_RT@@UEAAHAEAPEAVCmSurface2DUP@@@Z` | `0x2AF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `?DestroySurface@CmDevice_RT@@UEAAHAEAPEAVCmBuffer@@@Z` | `0x2B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `?DestroySurface@CmDevice_RT@@UEAAHAEAPEAVCmSurface2D@@@Z` | `0x2B10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `?DestroySurface@CmDevice_RT@@UEAAHAEAPEAVCmSurface3D@@@Z` | `0x2B20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `?DestroyTask@CmDevice_RT@@UEAAHAEAPEAVCmTask@@@Z` | `0x2B30` | 116 | UnwindData |  |
| 54 | `?DestroyThreadGroupSpace@CmDevice_RT@@UEAAHAEAPEAVCmThreadGroupSpace@@@Z` | `0x2BB0` | 83 | UnwindData |  |
| 55 | `?DestroyThreadSpace@CmDevice_RT@@UEAAHAEAPEAVCmThreadSpace@@@Z` | `0x2C10` | 83 | UnwindData |  |
| 56 | `?DestroyVebox@CmDevice_RT@@UEAAHAEAPEAVCmVebox@@@Z` | `0x2C70` | 83 | UnwindData |  |
| 58 | `?DispatchTask@CmDevice_RT@@UEAAHXZ` | `0x2CD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `?FlushPrintBuffer@CmDevice_RT@@UEAAHXZ` | `0x2CE0` | 60 | UnwindData |  |
| 77 | `?FlushPrintBufferIntoFile@CmDevice_RT@@UEAAHPEBD@Z` | `0x2D20` | 60 | UnwindData |  |
| 78 | `?GetCaps@CmDevice_RT@@UEAAHW4_CM_DEVICE_CAP_NAME@@AEA_KPEAX@Z` | `0x2D60` | 70 | UnwindData |  |
| 80 | `?GetSurface2DInfo@CmDevice_RT@@UEAAHIIW4_D3DFORMAT@@AEAI1@Z` | `0x2DB0` | 137 | UnwindData |  |
| 81 | `?GetVISAVersion@CmDevice_RT@@UEAAHAEAI0@Z` | `0x2E40` | 120 | UnwindData |  |
| 82 | `?InitPrintBuffer@CmDevice_RT@@UEAAH_K@Z` | `0x2EC0` | 64 | UnwindData |  |
| 83 | `?LoadProgram@CmDevice_RT@@UEAAHPEAXIAEAPEAVCmProgram@@PEBD@Z` | `0x2F00` | 136 | UnwindData |  |
| 84 | `?SetCaps@CmDevice_RT@@UEAAHW4_CM_DEVICE_CAP_NAME@@_KPEAX@Z` | `0x2F90` | 89 | UnwindData |  |
| 85 | `?SetL3Config@CmDevice_RT@@UEAAHPEBUL3ConfigRegisterValues@@@Z` | `0x2FF0` | 79 | UnwindData |  |
| 87 | `?SetSuggestedL3Config@CmDevice_RT@@UEAAHW4_L3_SUGGEST_CONFIG@@@Z` | `0x3040` | 56 | UnwindData |  |
| 88 | `?SetVmeSurfaceStateParam@CmDevice_RT@@UEAAHPEAVSurfaceIndex@@PEAUCM_VME_SURFACE_STATE_PARAM@@@Z` | `0x3080` | 85 | UnwindData |  |
| 104 | `CMRT_Enqueue` | `0x3150` | 21 | UnwindData |  |
| 128 | `DestroyCmDevice` | `0x3170` | 44 | UnwindData |  |
| 39 | `?DestroyEvent@CmQueue_RT@@UEAAHAEAPEAVCmEvent@@@Z` | `0x3960` | 111 | UnwindData |  |
| 40 | `?DestroyEventFast@CmQueue_RT@@UEAAHAEAPEAVCmEvent@@@Z` | `0x39D0` | 111 | UnwindData |  |
| 59 | `?Enqueue@CmQueue_RT@@UEAAHPEAVCmTask@@AEAPEAVCmEvent@@PEBVCmThreadSpace@@@Z` | `0x3A40` | 50 | UnwindData |  |
| 60 | `?EnqueueCopyCPUToCPU@CmQueue_RT@@UEAAHPEAE0IIAEAPEAVCmEvent@@@Z` | `0x3C10` | 213 | UnwindData |  |
| 61 | `?EnqueueCopyCPUToGPU@CmQueue_RT@@UEAAHPEAVCmSurface2D@@PEBEAEAPEAVCmEvent@@@Z` | `0x3CF0` | 40 | UnwindData |  |
| 62 | `?EnqueueCopyCPUToGPUFullStride@CmQueue_RT@@UEAAHPEAVCmSurface2D@@PEBEIIIAEAPEAVCmEvent@@@Z` | `0x3D20` | 51 | UnwindData |  |
| 63 | `?EnqueueCopyCPUToGPUFullStrideDup@CmQueue_RT@@UEAAHPEAVCmSurface2D@@PEBEIIIAEAPEAVCmEvent@@@Z` | `0x3D20` | 51 | UnwindData |  |
| 64 | `?EnqueueCopyGPUToCPU@CmQueue_RT@@UEAAHPEAVCmSurface2D@@PEAEAEAPEAVCmEvent@@@Z` | `0x3D60` | 36 | UnwindData |  |
| 65 | `?EnqueueCopyGPUToCPUFullStride@CmQueue_RT@@UEAAHPEAVCmSurface2D@@PEAEIIIAEAPEAVCmEvent@@@Z` | `0x3D90` | 51 | UnwindData |  |
| 66 | `?EnqueueCopyGPUToCPUFullStrideDup@CmQueue_RT@@UEAAHPEAVCmSurface2D@@PEAEIIIAEAPEAVCmEvent@@@Z` | `0x3D90` | 51 | UnwindData |  |
| 67 | `?EnqueueCopyGPUToGPU@CmQueue_RT@@UEAAHPEAVCmSurface2D@@0IAEAPEAVCmEvent@@@Z` | `0x3DD0` | 191 | UnwindData |  |
| 68 | `?EnqueueFast@CmQueue_RT@@UEAAHPEAVCmTask@@AEAPEAVCmEvent@@PEBVCmThreadSpace@@@Z` | `0x3E90` | 50 | UnwindData |  |
| 69 | `?EnqueueInitSurface2D@CmQueue_RT@@UEAAHPEAVCmSurface2D@@IAEAPEAVCmEvent@@@Z` | `0x3F70` | 182 | UnwindData |  |
| 70 | `?EnqueueReadBuffer@CmQueue_RT@@UEAAHPEAVCmBuffer@@_KPEBE1PEAVCmEvent@@AEAPEAV3@I@Z` | `0x4030` | 240 | UnwindData |  |
| 71 | `?EnqueueVebox@CmQueue_RT@@UEAAHPEAVCmVebox@@AEAPEAVCmEvent@@@Z` | `0x4120` | 192 | UnwindData |  |
| 72 | `?EnqueueWithGroup@CmQueue_RT@@UEAAHPEAVCmTask@@AEAPEAVCmEvent@@PEBVCmThreadGroupSpace@@@Z` | `0x41E0` | 50 | UnwindData |  |
| 73 | `?EnqueueWithGroupFast@CmQueue_RT@@UEAAHPEAVCmTask@@AEAPEAVCmEvent@@PEBVCmThreadGroupSpace@@@Z` | `0x42C0` | 50 | UnwindData |  |
| 74 | `?EnqueueWithHints@CmQueue_RT@@UEAAHPEAVCmTask@@AEAPEAVCmEvent@@I@Z` | `0x43A0` | 50 | UnwindData |  |
| 75 | `?EnqueueWriteBuffer@CmQueue_RT@@UEAAHPEAVCmBuffer@@_KPEBE1PEAVCmEvent@@AEAPEAV3@I@Z` | `0x4480` | 244 | UnwindData |  |
| 24 | `?CreateSurface2D@CmDevice_RT@@UEAAHPEAPEAUIDirect3DSurface9@@IPEAPEAVCmSurface2D@@@Z` | `0x5820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `?CreateSurface2D@CmDevice_RT@@UEAAHPEAUIDirect3DSurface9@@AEAPEAVCmSurface2D@@@Z` | `0x5830` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `?GetD3DDeviceManager@CmDevice_RT@@UEAAHAEAPEAUIDirect3DDeviceManager9@@@Z` | `0x5A70` | 3,232 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `CMRT_GetCompleteTime` | `0x6710` | 38 | UnwindData |  |
| 106 | `CMRT_GetEnqueueTime` | `0x6740` | 38 | UnwindData |  |
| 107 | `CMRT_GetHWEndTime` | `0x6770` | 38 | UnwindData |  |
| 108 | `CMRT_GetHWStartTime` | `0x67A0` | 36 | UnwindData |  |
| 109 | `CMRT_GetKernelCount` | `0x67D0` | 55 | UnwindData |  |
| 110 | `CMRT_GetKernelName` | `0x6810` | 45 | UnwindData |  |
| 111 | `CMRT_GetKernelThreadSpace` | `0x6840` | 138 | UnwindData |  |
| 112 | `CMRT_GetSubmitTime` | `0x68D0` | 38 | UnwindData |  |
| 116 | `CMRT_SetEventCallback` | `0x6900` | 38 | UnwindData |  |
| 126 | `CreateCmDevice` | `0x6930` | 115 | UnwindData |  |
| 127 | `CreateCmDeviceEx` | `0x69B0` | 110 | UnwindData |  |
| 103 | `CMRT_EnableGTPinMarkers` | `0x6D30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `CMRT_GetSurfaceDetails` | `0x6D40` | 22 | UnwindData |  |
| 115 | `CMRT_PrepareGTPinBuffers` | `0x6D60` | 226 | UnwindData |  |
| 117 | `CMRT_SetGTPinArguments` | `0x6E50` | 118 | UnwindData |  |
| 118 | `CMRT_SetGTPinCompileMode` | `0x6ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `CmrtCodeMarkerForGTPin_AddKernel` | `0x6EE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `CmrtCodeMarkerForGTPin_CreateQueue` | `0x6F00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `CmrtCodeMarkerForGTPin_CreateTask` | `0x6F20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `CmrtCodeMarkerForGTPin_DestroyTask` | `0x6F40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `CmrtCodeMarkerForGTPin_Enqueue` | `0x6F60` | 39 | UnwindData |  |
| 124 | `CmrtCodeMarkerForGTPin_EnqueueWithGroup` | `0x6F90` | 39 | UnwindData |  |
| 125 | `CmrtCodeMarkerForGTPin_SetThreadCount` | `0x6FC0` | 85,934 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
