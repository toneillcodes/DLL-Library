# Binary Specification: igfx11cmrt64.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_188be4c1587f7330\igfx11cmrt64.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d1d560e79a4384c0167efed123dfef35f35a4fbd94cfd334a7b3697a871e5750`
* **Total Exported Functions:** 134

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `??0CM_FLAG@@QEAA@XZ` | `0x12B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `CMRT_CreateBuffer` | `0x12C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `CMRT_CreateKernel` | `0x12E0` | 51 | UnwindData |  |
| 93 | `CMRT_CreateQueue` | `0x1320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `CMRT_CreateSurface2D` | `0x1340` | 51 | UnwindData |  |
| 95 | `CMRT_CreateSurface3D` | `0x1380` | 59 | UnwindData |  |
| 96 | `CMRT_CreateTask` | `0x13C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `CMRT_CreateThreadSpace` | `0x13E0` | 40 | UnwindData |  |
| 98 | `CMRT_DestroyBuffer` | `0x1410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `CMRT_DestroyEvent` | `0x1430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `CMRT_DestroyProgram` | `0x1450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `CMRT_DestroySurface2D` | `0x1470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `CMRT_DestroySurface3D` | `0x1490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `CMRT_DestroyTask` | `0x14B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `CMRT_DestroyThreadSpace` | `0x14D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `CMRT_LoadProgram` | `0x14F0` | 51 | UnwindData |  |
| 132 | `GetCmErrorString` | `0x1530` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `??0CM_AVS_STATE_MSG_EX@@QEAA@XZ` | `0x1570` | 1,872 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `?CloneKernel@CmDevice_RT@@UEAAHAEAPEAVCmKernel@@PEAV2@@Z` | `0x1CC0` | 86 | UnwindData |  |
| 4 | `?CreateBuffer@CmDevice_RT@@UEAAHIAEAPEAVCmBuffer@@@Z` | `0x1D20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `?CreateBufferAlias@CmDevice_RT@@UEAAHPEAVCmBuffer@@AEAPEAVSurfaceIndex@@@Z` | `0x1D30` | 88 | UnwindData |  |
| 6 | `?CreateBufferSVM@CmDevice_RT@@UEAAHIAEAPEAXIAEAPEAVCmBufferSVM@@@Z` | `0x1D90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `?CreateBufferStateless@CmDevice_RT@@UEAAH_KIPEAXAEAPEAVCmBufferStateless@@@Z` | `0x1DA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `?CreateBufferUP@CmDevice_RT@@UEAAHIPEAXAEAPEAVCmBufferUP@@@Z` | `0x1DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `?CreateHevcVmeSurfaceG10@CmDevice_RT@@UEAAHPEAVCmSurface2D@@PEAPEAV2@1IIAEAPEAVSurfaceIndex@@@Z` | `0x1DC0` | 134 | UnwindData |  |
| 10 | `?CreateKernel@CmDevice_RT@@UEAAHPEAVCmProgram@@PEBDAEAPEAVCmKernel@@1@Z` | `0x1E50` | 113 | UnwindData |  |
| 11 | `?CreateKernel@CmDevice_RT@@UEAAHPEAVCmProgram@@PEBDPEBXAEAPEAVCmKernel@@1@Z` | `0x1ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `?CreateQueue@CmDevice_RT@@UEAAHAEAPEAVCmQueue@@@Z` | `0x1EE0` | 104 | UnwindData |  |
| 13 | `?CreateQueueEx@CmDevice_RT@@UEAAHAEAPEAVCmQueue@@UCM_QUEUE_CREATE_OPTION@@@Z` | `0x1F50` | 332 | UnwindData |  |
| 14 | `?CreateSampler8x8@CmDevice_RT@@UEAAHAEBUCM_SAMPLER_8X8_DESCR@@AEAPEAVCmSampler8x8@@@Z` | `0x20A0` | 193 | UnwindData |  |
| 15 | `?CreateSampler8x8Surface@CmDevice_RT@@UEAAHPEAVCmSurface2D@@AEAPEAVSurfaceIndex@@W4_CM_SAMPLER8x8_SURFACE_@@W4_CM_SURFACE_ADDRESS_CONTROL_MODE_@@@Z` | `0x2170` | 111 | UnwindData |  |
| 16 | `?CreateSampler8x8SurfaceEx@CmDevice_RT@@UEAAHPEAVCmSurface2D@@AEAPEAVSurfaceIndex@@W4_CM_SAMPLER8x8_SURFACE_@@W4_CM_SURFACE_ADDRESS_CONTROL_MODE_@@PEAUCM_FLAG@@@Z` | `0x21E0` | 124 | UnwindData |  |
| 17 | `?CreateSampler@CmDevice_RT@@UEAAHAEBU_CM_SAMPLER_STATE@@AEAPEAVCmSampler@@@Z` | `0x2260` | 123 | UnwindData |  |
| 18 | `?CreateSamplerEx@CmDevice_RT@@UEAAHAEBU_CM_SAMPLER_STATE_EX@@AEAPEAVCmSampler@@@Z` | `0x22E0` | 142 | UnwindData |  |
| 19 | `?CreateSamplerSurface2D@CmDevice_RT@@UEAAHPEAVCmSurface2D@@AEAPEAVSurfaceIndex@@@Z` | `0x2370` | 96 | UnwindData |  |
| 20 | `?CreateSamplerSurface2DEx@CmDevice_RT@@UEAAHPEAVCmSurface2D@@AEAPEAVSurfaceIndex@@PEAUCM_FLAG@@@Z` | `0x23D0` | 101 | UnwindData |  |
| 21 | `?CreateSamplerSurface2DUP@CmDevice_RT@@UEAAHPEAVCmSurface2DUP@@AEAPEAVSurfaceIndex@@@Z` | `0x2440` | 82 | UnwindData |  |
| 22 | `?CreateSamplerSurface3D@CmDevice_RT@@UEAAHPEAVCmSurface3D@@AEAPEAVSurfaceIndex@@@Z` | `0x24A0` | 82 | UnwindData |  |
| 23 | `?CreateSurface2D@CmDevice_RT@@UEAAHIIW4DXGI_FORMAT@@AEAPEAVCmSurface2D@@@Z` | `0x2500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `?CreateSurface2DAlias@CmDevice_RT@@UEAAHPEAVCmSurface2D@@AEAPEAVSurfaceIndex@@@Z` | `0x2510` | 88 | UnwindData |  |
| 27 | `?CreateSurface2DStateless@CmDevice_RT@@UEAAHIIAEAIAEAPEAVCmSurface2DStateless@@@Z` | `0x2570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `?DestroySurface2DStateless@CmDevice_RT@@UEAAHAEAPEAVCmSurface2DStateless@@@Z` | `0x2570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `?SetResidentGroupAndParallelThreadNum@CmQueue_RT@@UEAAHII@Z` | `0x2570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `?CreateSurface2DUP@CmDevice_RT@@UEAAHIIW4DXGI_FORMAT@@PEAXAEAPEAVCmSurface2DUP@@@Z` | `0x2580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `?CreateSurface3D@CmDevice_RT@@UEAAHIIIW4DXGI_FORMAT@@AEAPEAVCmSurface3D@@@Z` | `0x2590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `?CreateTask@CmDevice_RT@@UEAAHAEAPEAVCmTask@@@Z` | `0x25A0` | 103 | UnwindData |  |
| 33 | `?CreateThreadGroupSpace@CmDevice_RT@@UEAAHIIIIAEAPEAVCmThreadGroupSpace@@@Z` | `0x2610` | 119 | UnwindData |  |
| 34 | `?CreateThreadGroupSpaceEx@CmDevice_RT@@UEAAHIIIIIIAEAPEAVCmThreadGroupSpace@@@Z` | `0x2690` | 125 | UnwindData |  |
| 35 | `?CreateThreadSpace@CmDevice_RT@@UEAAHIIAEAPEAVCmThreadSpace@@@Z` | `0x2710` | 85 | UnwindData |  |
| 36 | `?CreateVebox@CmDevice_RT@@UEAAHAEAPEAVCmVebox@@@Z` | `0x2770` | 75 | UnwindData |  |
| 37 | `?CreateVmeSurfaceG7_5@CmDevice_RT@@UEAAHPEAVCmSurface2D@@PEAPEAV2@1IIAEAPEAVSurfaceIndex@@@Z` | `0x27C0` | 134 | UnwindData |  |
| 38 | `?DestroyBufferSVM@CmDevice_RT@@UEAAHAEAPEAVCmBufferSVM@@@Z` | `0x2850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `?DestroyBufferStateless@CmDevice_RT@@UEAAHAEAPEAVCmBufferStateless@@@Z` | `0x2860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `?DestroyBufferUP@CmDevice_RT@@UEAAHAEAPEAVCmBufferUP@@@Z` | `0x2870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `?DestroyHevcVmeSurfaceG10@CmDevice_RT@@UEAAHAEAPEAVSurfaceIndex@@@Z` | `0x2880` | 85 | UnwindData |  |
| 59 | `?DestroyVmeSurfaceG7_5@CmDevice_RT@@UEAAHAEAPEAVSurfaceIndex@@@Z` | `0x2880` | 85 | UnwindData |  |
| 44 | `?DestroyKernel@CmDevice_RT@@UEAAHAEAPEAVCmKernel@@@Z` | `0x28E0` | 83 | UnwindData |  |
| 45 | `?DestroyProgram@CmDevice_RT@@UEAAHAEAPEAVCmProgram@@@Z` | `0x2940` | 100 | UnwindData |  |
| 46 | `?DestroySampler8x8@CmDevice_RT@@UEAAHAEAPEAVCmSampler8x8@@@Z` | `0x29B0` | 83 | UnwindData |  |
| 47 | `?DestroySampler8x8Surface@CmDevice_RT@@UEAAHAEAPEAVSurfaceIndex@@@Z` | `0x2A10` | 83 | UnwindData |  |
| 48 | `?DestroySampler@CmDevice_RT@@UEAAHAEAPEAVCmSampler@@@Z` | `0x2A70` | 83 | UnwindData |  |
| 49 | `?DestroySamplerSurface@CmDevice_RT@@UEAAHAEAPEAVSurfaceIndex@@@Z` | `0x2AD0` | 62 | UnwindData |  |
| 51 | `?DestroySurface2DUP@CmDevice_RT@@UEAAHAEAPEAVCmSurface2DUP@@@Z` | `0x2B10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `?DestroySurface@CmDevice_RT@@UEAAHAEAPEAVCmBuffer@@@Z` | `0x2B20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `?DestroySurface@CmDevice_RT@@UEAAHAEAPEAVCmSurface2D@@@Z` | `0x2B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `?DestroySurface@CmDevice_RT@@UEAAHAEAPEAVCmSurface3D@@@Z` | `0x2B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `?DestroyTask@CmDevice_RT@@UEAAHAEAPEAVCmTask@@@Z` | `0x2B50` | 116 | UnwindData |  |
| 56 | `?DestroyThreadGroupSpace@CmDevice_RT@@UEAAHAEAPEAVCmThreadGroupSpace@@@Z` | `0x2BD0` | 83 | UnwindData |  |
| 57 | `?DestroyThreadSpace@CmDevice_RT@@UEAAHAEAPEAVCmThreadSpace@@@Z` | `0x2C30` | 83 | UnwindData |  |
| 58 | `?DestroyVebox@CmDevice_RT@@UEAAHAEAPEAVCmVebox@@@Z` | `0x2C90` | 83 | UnwindData |  |
| 60 | `?DispatchTask@CmDevice_RT@@UEAAHXZ` | `0x2CF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `?FlushPrintBuffer@CmDevice_RT@@UEAAHXZ` | `0x2D00` | 60 | UnwindData |  |
| 79 | `?FlushPrintBufferIntoFile@CmDevice_RT@@UEAAHPEBD@Z` | `0x2D40` | 60 | UnwindData |  |
| 80 | `?GetCaps@CmDevice_RT@@UEAAHW4_CM_DEVICE_CAP_NAME@@AEA_KPEAX@Z` | `0x2D80` | 70 | UnwindData |  |
| 82 | `?GetSurface2DInfo@CmDevice_RT@@UEAAHIIW4DXGI_FORMAT@@AEAI1@Z` | `0x2DD0` | 137 | UnwindData |  |
| 83 | `?GetVISAVersion@CmDevice_RT@@UEAAHAEAI0@Z` | `0x2E60` | 120 | UnwindData |  |
| 84 | `?InitPrintBuffer@CmDevice_RT@@UEAAH_K@Z` | `0x2EE0` | 64 | UnwindData |  |
| 85 | `?LoadProgram@CmDevice_RT@@UEAAHPEAXIAEAPEAVCmProgram@@PEBD@Z` | `0x2F20` | 136 | UnwindData |  |
| 86 | `?SetCaps@CmDevice_RT@@UEAAHW4_CM_DEVICE_CAP_NAME@@_KPEAX@Z` | `0x2FB0` | 89 | UnwindData |  |
| 87 | `?SetL3Config@CmDevice_RT@@UEAAHPEBUL3ConfigRegisterValues@@@Z` | `0x3010` | 79 | UnwindData |  |
| 89 | `?SetSuggestedL3Config@CmDevice_RT@@UEAAHW4_L3_SUGGEST_CONFIG@@@Z` | `0x3060` | 56 | UnwindData |  |
| 90 | `?SetVmeSurfaceStateParam@CmDevice_RT@@UEAAHPEAVSurfaceIndex@@PEAUCM_VME_SURFACE_STATE_PARAM@@@Z` | `0x30A0` | 85 | UnwindData |  |
| 106 | `CMRT_Enqueue` | `0x3170` | 21 | UnwindData |  |
| 131 | `DestroyCmDevice` | `0x3190` | 44 | UnwindData |  |
| 41 | `?DestroyEvent@CmQueue_RT@@UEAAHAEAPEAVCmEvent@@@Z` | `0x3980` | 111 | UnwindData |  |
| 42 | `?DestroyEventFast@CmQueue_RT@@UEAAHAEAPEAVCmEvent@@@Z` | `0x39F0` | 111 | UnwindData |  |
| 61 | `?Enqueue@CmQueue_RT@@UEAAHPEAVCmTask@@AEAPEAVCmEvent@@PEBVCmThreadSpace@@@Z` | `0x3A60` | 50 | UnwindData |  |
| 62 | `?EnqueueCopyCPUToCPU@CmQueue_RT@@UEAAHPEAE0IIAEAPEAVCmEvent@@@Z` | `0x3C30` | 213 | UnwindData |  |
| 63 | `?EnqueueCopyCPUToGPU@CmQueue_RT@@UEAAHPEAVCmSurface2D@@PEBEAEAPEAVCmEvent@@@Z` | `0x3D10` | 40 | UnwindData |  |
| 64 | `?EnqueueCopyCPUToGPUFullStride@CmQueue_RT@@UEAAHPEAVCmSurface2D@@PEBEIIIAEAPEAVCmEvent@@@Z` | `0x3D40` | 51 | UnwindData |  |
| 65 | `?EnqueueCopyCPUToGPUFullStrideDup@CmQueue_RT@@UEAAHPEAVCmSurface2D@@PEBEIIIAEAPEAVCmEvent@@@Z` | `0x3D40` | 51 | UnwindData |  |
| 66 | `?EnqueueCopyGPUToCPU@CmQueue_RT@@UEAAHPEAVCmSurface2D@@PEAEAEAPEAVCmEvent@@@Z` | `0x3D80` | 36 | UnwindData |  |
| 67 | `?EnqueueCopyGPUToCPUFullStride@CmQueue_RT@@UEAAHPEAVCmSurface2D@@PEAEIIIAEAPEAVCmEvent@@@Z` | `0x3DB0` | 51 | UnwindData |  |
| 68 | `?EnqueueCopyGPUToCPUFullStrideDup@CmQueue_RT@@UEAAHPEAVCmSurface2D@@PEAEIIIAEAPEAVCmEvent@@@Z` | `0x3DB0` | 51 | UnwindData |  |
| 69 | `?EnqueueCopyGPUToGPU@CmQueue_RT@@UEAAHPEAVCmSurface2D@@0IAEAPEAVCmEvent@@@Z` | `0x3DF0` | 191 | UnwindData |  |
| 70 | `?EnqueueFast@CmQueue_RT@@UEAAHPEAVCmTask@@AEAPEAVCmEvent@@PEBVCmThreadSpace@@@Z` | `0x3EB0` | 50 | UnwindData |  |
| 71 | `?EnqueueInitSurface2D@CmQueue_RT@@UEAAHPEAVCmSurface2D@@IAEAPEAVCmEvent@@@Z` | `0x3F90` | 182 | UnwindData |  |
| 72 | `?EnqueueReadBuffer@CmQueue_RT@@UEAAHPEAVCmBuffer@@_KPEBE1PEAVCmEvent@@AEAPEAV3@I@Z` | `0x4050` | 240 | UnwindData |  |
| 73 | `?EnqueueVebox@CmQueue_RT@@UEAAHPEAVCmVebox@@AEAPEAVCmEvent@@@Z` | `0x4140` | 192 | UnwindData |  |
| 74 | `?EnqueueWithGroup@CmQueue_RT@@UEAAHPEAVCmTask@@AEAPEAVCmEvent@@PEBVCmThreadGroupSpace@@@Z` | `0x4200` | 50 | UnwindData |  |
| 75 | `?EnqueueWithGroupFast@CmQueue_RT@@UEAAHPEAVCmTask@@AEAPEAVCmEvent@@PEBVCmThreadGroupSpace@@@Z` | `0x42E0` | 50 | UnwindData |  |
| 76 | `?EnqueueWithHints@CmQueue_RT@@UEAAHPEAVCmTask@@AEAPEAVCmEvent@@I@Z` | `0x43C0` | 50 | UnwindData |  |
| 77 | `?EnqueueWriteBuffer@CmQueue_RT@@UEAAHPEAVCmBuffer@@_KPEBE1PEAVCmEvent@@AEAPEAV3@I@Z` | `0x44A0` | 244 | UnwindData |  |
| 24 | `?CreateSurface2D@CmDevice_RT@@UEAAHPEAPEAUID3D11Texture2D@@IPEAPEAVCmSurface2D@@@Z` | `0x5490` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `?CreateSurface2D@CmDevice_RT@@UEAAHPEAUID3D11Texture2D@@AEAPEAVCmSurface2D@@@Z` | `0x54A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `?CreateSurface2DSubresource@CmDevice_RT@@UEAAHPEAUID3D11Texture2D@@IPEAPEAVCmSurface2D@@AEAII@Z` | `0x54B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `?CreateSurface2DbySubresourceIndex@CmDevice_RT@@UEAAHPEAUID3D11Texture2D@@IIAEAPEAVCmSurface2D@@@Z` | `0x54C0` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `?GetD3D11Device@CmDevice_RT@@UEAAHAEAPEAUID3D11Device@@@Z` | `0x56C0` | 5,152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `CMRT_GetCompleteTime` | `0x6AE0` | 38 | UnwindData |  |
| 108 | `CMRT_GetEnqueueTime` | `0x6B10` | 38 | UnwindData |  |
| 109 | `CMRT_GetHWEndTime` | `0x6B40` | 38 | UnwindData |  |
| 110 | `CMRT_GetHWStartTime` | `0x6B70` | 36 | UnwindData |  |
| 111 | `CMRT_GetKernelCount` | `0x6BA0` | 55 | UnwindData |  |
| 112 | `CMRT_GetKernelName` | `0x6BE0` | 45 | UnwindData |  |
| 113 | `CMRT_GetKernelThreadSpace` | `0x6C10` | 138 | UnwindData |  |
| 114 | `CMRT_GetSubmitTime` | `0x6CA0` | 38 | UnwindData |  |
| 118 | `CMRT_SetEventCallback` | `0x6CD0` | 38 | UnwindData |  |
| 128 | `CreateCmDevice` | `0x6D00` | 124 | UnwindData |  |
| 129 | `CreateCmDeviceEx` | `0x6D80` | 110 | UnwindData |  |
| 130 | `CreateCmDeviceFromAdapter` | `0x6DF0` | 138 | UnwindData |  |
| 133 | `GetCmSupportedAdapters` | `0x6E80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `QueryCmAdapterInfo` | `0x6E90` | 114 | UnwindData |  |
| 105 | `CMRT_EnableGTPinMarkers` | `0x7230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `CMRT_GetSurfaceDetails` | `0x7240` | 22 | UnwindData |  |
| 117 | `CMRT_PrepareGTPinBuffers` | `0x7260` | 226 | UnwindData |  |
| 119 | `CMRT_SetGTPinArguments` | `0x7350` | 118 | UnwindData |  |
| 120 | `CMRT_SetGTPinCompileMode` | `0x73D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `CmrtCodeMarkerForGTPin_AddKernel` | `0x73E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `CmrtCodeMarkerForGTPin_CreateQueue` | `0x7400` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `CmrtCodeMarkerForGTPin_CreateTask` | `0x7420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `CmrtCodeMarkerForGTPin_DestroyTask` | `0x7440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `CmrtCodeMarkerForGTPin_Enqueue` | `0x7460` | 39 | UnwindData |  |
| 126 | `CmrtCodeMarkerForGTPin_EnqueueWithGroup` | `0x7490` | 39 | UnwindData |  |
| 127 | `CmrtCodeMarkerForGTPin_SetThreadCount` | `0x74C0` | 86,926 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
