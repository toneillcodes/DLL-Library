# Binary Specification: igdgmm64.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_188be4c1587f7330\igdgmm64.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b066b9db4972485c6ed21fe4062ba135b957dc38ecbfd69a57ad61d71690247a`
* **Total Exported Functions:** 153

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `??0GmmClientContext@GmmLib@@QEAA@AEBV01@@Z` | `0x1220` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0GmmPageTableMgr@GmmLib@@QEAA@AEBV01@@Z` | `0x13B0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `??4GmmClientContext@GmmLib@@QEAAAEAV01@AEBV01@@Z` | `0x1550` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `??4GmmPageTableMgr@GmmLib@@QEAAAEAV01@AEBV01@@Z` | `0x16D0` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `?GetClientContext@GmmPageTableMgr@GmmLib@@UEAAPEAVGmmClientContext@2@XZ` | `0x19D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `?GetClientType@GmmClientContext@GmmLib@@UEAA?AW4GMM_CLIENT_ENUM@@XZ` | `0x19E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `?GetDeviceCallback@GmmClientContext@GmmLib@@QEAAPEAU_GMM_DEVICE_CALLBACKS_INT@@XZ` | `0x19F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `?GetLibContext@GmmClientContext@GmmLib@@UEAAPEAVContext@2@XZ` | `0x1A10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `?GetLibContext@GmmPageTableMgr@GmmLib@@AEAAPEAVContext@2@XZ` | `0x1A20` | 3,426,320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `??0GmmPageTableMgr@GmmLib@@QEAA@XZ` | `0x346230` | 164 | UnwindData |  |
| 5 | `??0GmmPageTableMgr@GmmLib@@QEAA@PEAU_GMM_DEVICE_CALLBACKS_INT@@IPEAVGmmClientContext@1@@Z` | `0x3462E0` | 1,498 | UnwindData |  |
| 4 | `??0GmmPageTableMgr@GmmLib@@QEAA@PEAU_GMM_DEVICE_CALLBACKS_INT@@IPEAUGMM_TRANSLATIONTABLE_CALLBACKS_REC@@PEAVGmmClientContext@1@@Z` | `0x3468C0` | 149 | UnwindData |  |
| 105 | `?InitGpuBBQueueCallbacks@GmmPageTableMgr@GmmLib@@UEAAXPEAUGMM_TRANSLATIONTABLE_CALLBACKS_REC@@@Z` | `0x346960` | 95 | UnwindData |  |
| 93 | `?GetTRL3TableAddr@GmmPageTableMgr@GmmLib@@UEAA_KXZ` | `0x3469D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `?GetAuxL3TableAddr@GmmPageTableMgr@GmmLib@@UEAA_KXZ` | `0x3469F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `?InitContextAuxTableRegister@GmmPageTableMgr@GmmLib@@UEAA?AW4GMM_STATUS_ENUM@@PEAXW4_GMM_ENGINE_TYPE@@@Z` | `0x346A10` | 86 | UnwindData |  |
| 104 | `?InitContextTRTableRegister@GmmPageTableMgr@GmmLib@@UEAA?AW4GMM_STATUS_ENUM@@PEAXW4_GMM_ENGINE_TYPE@@@Z` | `0x346B30` | 227 | UnwindData |  |
| 132 | `?ReserveTRGpuVirtualAddress@GmmPageTableMgr@GmmLib@@UEAAJPEAUGMM_UMD_SYNCCONTEXT_REC@@PEAUD3DDDI_RESERVEGPUVIRTUALADDRESS@@E@Z` | `0x346D50` | 17 | UnwindData |  |
| 115 | `?MapTRGpuVirtualAddress@GmmPageTableMgr@GmmLib@@UEAAJPEAU_GMM_MAP_TR_GPUVIRTUALADDRESS@@E@Z` | `0x346DF0` | 24 | UnwindData |  |
| 143 | `?UpdateTRGpuVirtualAddress@GmmPageTableMgr@GmmLib@@UEAAJPEAPEAUGMM_UMD_SYNCCONTEXT_REC@@PEBU_GMM_UPADTE_TR_GPUVIRTUALADDRESS_INT@@E@Z` | `0x346E90` | 17 | UnwindData |  |
| 56 | `?FreeTRGpuVirtualAddress@GmmPageTableMgr@GmmLib@@UEAAJPEAUGMM_UMD_SYNCCONTEXT_REC@@PEBTGMM_DDI_FREEGPUVIRTUALADDRSS_INT@@E@Z` | `0x346F30` | 17 | UnwindData |  |
| 140 | `?UpdateAuxTable@GmmPageTableMgr@GmmLib@@UEAA?AW4GMM_STATUS_ENUM@@PEBU__GMM_DDI_UPDATEAUXTABLE@@@Z` | `0x346FD0` | 1,887 | UnwindData |  |
| 150 | `?__ReleaseUnusedPool@GmmPageTableMgr@GmmLib@@UEAAXPEAUGMM_UMD_SYNCCONTEXT_REC@@@Z` | `0x347740` | 23 | UnwindData |  |
| 146 | `?__GetFreePoolNode@GmmPageTableMgr@GmmLib@@UEAAPEAVGmmPageTablePool@2@PEAIW4POOL_TYPE_REC@2@@Z` | `0x347AB0` | 573 | UnwindData |  |
| 51 | `?EvictPageTablePool@GmmPageTableMgr@GmmLib@@UEAAXPEAIH@Z` | `0x347D00` | 17 | UnwindData |  |
| 100 | `?GmmSetCsrHandle@GmmPageTableMgr@GmmLib@@UEAAXPEAX@Z` | `0x347DE0` | 6 | UnwindData |  |
| 8 | `??1GmmPageTableMgr@GmmLib@@UEAA@XZ` | `0x347F40` | 553 | UnwindData |  |
| 145 | `?__AllocateNodePool@GmmPageTableMgr@GmmLib@@AEAAPEAVGmmPageTablePool@2@IW4POOL_TYPE_REC@2@@Z` | `0x348170` | 430 | UnwindData |  |
| 149 | `?__NotifyAuxTChange@GmmPageTableMgr@GmmLib@@AEAAX_KAEA_K1AEAE@Z` | `0x348330` | 210 | UnwindData |  |
| 2 | `??0GmmClientContext@GmmLib@@QEAA@W4GMM_CLIENT_ENUM@@PEAVContext@1@@Z` | `0x34D3F0` | 158 | UnwindData |  |
| 7 | `??1GmmClientContext@GmmLib@@UEAA@XZ` | `0x34D4A0` | 68 | UnwindData |  |
| 20 | `?CachePolicyGetMemoryObject@GmmClientContext@GmmLib@@UEAA?ATMEMORY_OBJECT_CONTROL_STATE_REC@@PEAVGmmResourceInfoWin@2@W4GMM_RESOURCE_USAGE_TYPE_ENUM@@@Z` | `0x34D4F0` | 37 | UnwindData |  |
| 23 | `?CachePolicyGetPteType@GmmClientContext@GmmLib@@UEAA?ATGMM_PTE_CACHE_CONTROL_BITS_REC@@W4GMM_RESOURCE_USAGE_TYPE_ENUM@@@Z` | `0x34D520` | 37 | UnwindData |  |
| 21 | `?CachePolicyGetOriginalMemoryObject@GmmClientContext@GmmLib@@UEAA?ATMEMORY_OBJECT_CONTROL_STATE_REC@@PEAVGmmResourceInfoWin@2@@Z` | `0x34D550` | 37 | UnwindData |  |
| 24 | `?CachePolicyIsUsagePTECached@GmmClientContext@GmmLib@@UEAAEW4GMM_RESOURCE_USAGE_TYPE_ENUM@@@Z` | `0x34D580` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `?GetSurfaceStateL1CachePolicy@GmmClientContext@GmmLib@@UEAAEW4GMM_RESOURCE_USAGE_TYPE_ENUM@@@Z` | `0x34D5B0` | 50 | UnwindData |  |
| 18 | `?CachePolicyGetMaxMocsIndex@GmmClientContext@GmmLib@@UEAAIXZ` | `0x34D5F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `?CachePolicyGetMaxL1HdcMocsIndex@GmmClientContext@GmmLib@@UEAAIXZ` | `0x34D610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `?CachePolicyGetMaxSpecialMocsIndex@GmmClientContext@GmmLib@@UEAAIXZ` | `0x34D630` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `?GetCachePolicyUsage@GmmClientContext@GmmLib@@UEAAPEAUGMM_CACHE_POLICY_ELEMENT_REC@@XZ` | `0x34D660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `?GetCacheSizes@GmmClientContext@GmmLib@@UEAAXPEAUGMM_CACHE_SIZES_REC@@@Z` | `0x34D680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `?GetUseGlobalGtt@GmmClientContext@GmmLib@@UEAAEW4GMM_HW_COMMAND_STREAMER_ENUM@@W4GMM_HW_COMMAND_ENUM@@PEAT__D3DDDI_PATCHLOCATIONLIST_DRIVERID@@@Z` | `0x34D6A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `?GetCachePolicyElement@GmmClientContext@GmmLib@@UEAA?AUGMM_CACHE_POLICY_ELEMENT_REC@@W4GMM_RESOURCE_USAGE_TYPE_ENUM@@@Z` | `0x34D6C0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `?GetCachePolicyTlbElement@GmmClientContext@GmmLib@@UEAA?AUGMM_CACHE_POLICY_TBL_ELEMENT_REC@@I@Z` | `0x34D710` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `?GetPlatformInfo@GmmClientContext@GmmLib@@UEAAAEAU__GMM_PLATFORM_RESOURCE_REC@@XZ` | `0x34D740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `?GetSkuTable@GmmClientContext@GmmLib@@UEAAAEBU_SKU_FEATURE_TABLE@@XZ` | `0x34D760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `?GetExtendedTextureAlign@GmmClientContext@GmmLib@@UEAAXIAEAU__TEX_ALIGNMENT@@@Z` | `0x34D780` | 89 | UnwindData |  |
| 109 | `?IsPlanar@GmmClientContext@GmmLib@@UEAAEW4GMM_RESOURCE_FORMAT_ENUM@@@Z` | `0x34D7E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `?IsP0xx@GmmClientContext@GmmLib@@UEAAEW4GMM_RESOURCE_FORMAT_ENUM@@@Z` | `0x34D7F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `?IsUVPacked@GmmClientContext@GmmLib@@UEAAEW4GMM_RESOURCE_FORMAT_ENUM@@@Z` | `0x34D800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `?IsCompressed@GmmClientContext@GmmLib@@UEAAEW4GMM_RESOURCE_FORMAT_ENUM@@@Z` | `0x34D810` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `?IsYUVPacked@GmmClientContext@GmmLib@@UEAAEW4GMM_RESOURCE_FORMAT_ENUM@@@Z` | `0x34D850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `?GetSurfaceStateFormat@GmmClientContext@GmmLib@@UEAA?AW4GMM_SURFACESTATE_FORMAT_ENUM@@W4GMM_RESOURCE_FORMAT_ENUM@@@Z` | `0x34D860` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `?GetSurfaceStateCompressionFormat@GmmClientContext@GmmLib@@UEAAEW4GMM_RESOURCE_FORMAT_ENUM@@@Z` | `0x34D8A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `?GetMediaSurfaceStateCompressionFormat@GmmClientContext@GmmLib@@UEAAEW4GMM_RESOURCE_FORMAT_ENUM@@@Z` | `0x34D8D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `?GetLosslessCompressionType@GmmClientContext@GmmLib@@UEAA?AW4GMM_E2ECOMP_FORMAT_ENUM@@W4GMM_RESOURCE_FORMAT_ENUM@@@Z` | `0x34D900` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `?GetInternalGpuVaRangeLimit@GmmClientContext@GmmLib@@UEAA_KXZ` | `0x34D930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `?CreateResInfoObject@GmmClientContext@GmmLib@@UEAAPEAVGmmResourceInfoWin@2@PEAUGMM_RESCREATE_PARAMS_REC@@@Z` | `0x34D950` | 193 | UnwindData |  |
| 27 | `?CopyResInfoObject@GmmClientContext@GmmLib@@UEAAPEAVGmmResourceInfoWin@2@PEAV32@@Z` | `0x34DA20` | 153 | UnwindData |  |
| 128 | `?ResMemcpy@GmmClientContext@GmmLib@@UEAAXPEAX0@Z` | `0x34DAC0` | 107 | UnwindData |  |
| 44 | `?DestroyResInfoObject@GmmClientContext@GmmLib@@UEAAXPEAVGmmResourceInfoWin@2@@Z` | `0x34DB40` | 122 | UnwindData |  |
| 34 | `?CreatePageTblMgrObject@GmmClientContext@GmmLib@@UEAAPEAVGmmPageTableMgr@2@PEAU_GMM_DEVICE_CALLBACKS_INT@@PEAUGMM_TRANSLATIONTABLE_CALLBACKS_REC@@I@Z` | `0x34DBC0` | 136 | UnwindData |  |
| 32 | `?CreatePageTblMgrObject@GmmClientContext@GmmLib@@UEAAPEAVGmmPageTableMgr@2@PEAUGMM_TRANSLATIONTABLE_CALLBACKS_REC@@I@Z` | `0x34DC50` | 54 | UnwindData |  |
| 41 | `?DestroyPageTblMgrObject@GmmClientContext@GmmLib@@UEAAXPEAVGmmPageTableMgr@2@@Z` | `0x34DC90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `?CopyResInfoObject@GmmClientContext@GmmLib@@QEAAPEAVGmmResourceInfoWin@2@PEAV32@PEAU_GmmClientAllocationCallbacks_@@@Z` | `0x34DCC0` | 104 | UnwindData |  |
| 38 | `?CreateResInfoObject@GmmClientContext@GmmLib@@UEAAPEAVGmmResourceInfoWin@2@PEAUGMM_RESCREATE_PARAMS_REC@@PEAU_GmmClientAllocationCallbacks_@@@Z` | `0x34DD30` | 54 | UnwindData |  |
| 45 | `?DestroyResInfoObject@GmmClientContext@GmmLib@@UEAAXPEAVGmmResourceInfoWin@2@PEAU_GmmClientAllocationCallbacks_@@@Z` | `0x34DE50` | 179 | UnwindData |  |
| 116 | `?MapTileInstancedGpuVirtualAddress@GmmClientContext@GmmLib@@UEAAJPEAU_GMM_MAP_GPUVA_TILE_INSTANCED_RESOURCE@@@Z` | `0x34DF10` | 1,335 | UnwindData |  |
| 114 | `?MapGpuVirtualAddress@GmmClientContext@GmmLib@@UEAAJPEAU_GMM_MAP_GPUVIRTUALADDRESS@@@Z` | `0x34E450` | 3,723 | UnwindData |  |
| 130 | `?ReserveGpuVirtualAddress@GmmClientContext@GmmLib@@UEAAJPEAUD3DDDI_RESERVEGPUVIRTUALADDRESS@@@Z` | `0x34F2F0` | 41 | UnwindData |  |
| 53 | `?FreeGpuVirtualAddress@GmmClientContext@GmmLib@@UEAAJPEBU_GMM_FREEGPUVIRTUALADDRESS@@@Z` | `0x34F380` | 344 | UnwindData |  |
| 71 | `?GetFreeSpeedFrameIndex@GmmClientContext@GmmLib@@UEAAKXZ` | `0x34F720` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `?UpdateSpeedFrameUsage@GmmClientContext@GmmLib@@UEAAXKE@Z` | `0x34F750` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `?SpeedFrameInit@GmmClientContext@GmmLib@@UEAAJXZ` | `0x34F7B0` | 631 | UnwindData |  |
| 136 | `?SpeedFrameDeInit@GmmClientContext@GmmLib@@UEAAJXZ` | `0x34FA30` | 36 | UnwindData |  |
| 134 | `?SpeedFrameAlloc@GmmClientContext@GmmLib@@UEAA?AW4GMM_STATUS_ENUM@@IPEAUGMM_RESCREATE_PARAMS_SPEEDFRAME_REC@@@Z` | `0x34FB10` | 411 | UnwindData |  |
| 135 | `?SpeedFrameDeAlloc@GmmClientContext@GmmLib@@UEAA?AW4GMM_STATUS_ENUM@@IPEAI@Z` | `0x350520` | 33 | UnwindData |  |
| 99 | `?GmmReverseEscapeListener@GmmClientContext@GmmLib@@UEAAJXZ` | `0x3507C0` | 631 | UnwindData |  |
| 35 | `?CreatePageTblMgrObject@GmmClientContext@GmmLib@@UEAAPEAVGmmPageTableMgr@2@PEAU_GMM_DEVICE_CALLBACKS_INT@@PEAUGMM_TRANSLATIONTABLE_CALLBACKS_REC@@IPEAU_GmmClientAllocationCallbacks_@@@Z` | `0x350A40` | 200 | UnwindData |  |
| 33 | `?CreatePageTblMgrObject@GmmClientContext@GmmLib@@UEAAPEAVGmmPageTableMgr@2@PEAUGMM_TRANSLATIONTABLE_CALLBACKS_REC@@IPEAU_GmmClientAllocationCallbacks_@@@Z` | `0x350B10` | 59 | UnwindData |  |
| 42 | `?DestroyPageTblMgrObject@GmmClientContext@GmmLib@@UEAAXPEAVGmmPageTableMgr@2@PEAU_GmmClientAllocationCallbacks_@@@Z` | `0x350B60` | 105 | UnwindData |  |
| 101 | `?GmmSetDeviceInfo@GmmClientContext@GmmLib@@UEAA?AW4GMM_STATUS_ENUM@@PEAU_GMM_DEVICE_INFO_REC@@@Z` | `0x350BD0` | 265 | UnwindData |  |
| 30 | `?CreateCustomResInfoObject@GmmClientContext@GmmLib@@UEAAPEAVGmmResourceInfoWin@2@PEAUGMM_RESCREATE_CUSTOM_PARAMS__REC@@@Z` | `0x350E40` | 152 | UnwindData |  |
| 98 | `?GmmLogUmdEvent@GmmClientContext@GmmLib@@UEAAXPEAU_GMM_ARG_LOG_UMD_EVENT@@@Z` | `0x350EE0` | 22 | UnwindData |  |
| 148 | `?__GetSharedHeapObject@GmmClientContext@GmmLib@@AEAAPEAXTGMM_ESCAPE_HANDLE_REC@@0TGMM_ESCAPE_FUNC_TYPE_REC@@@Z` | `0x351240` | 250 | UnwindData |  |
| 151 | `?__SetSharedHeapObject@GmmClientContext@GmmLib@@AEAAITGMM_ESCAPE_HANDLE_REC@@0PEAPEAXTGMM_ESCAPE_FUNC_TYPE_REC@@@Z` | `0x351340` | 294 | UnwindData |  |
| 86 | `?GetSetProcessGfxPartition@GmmClientContext@GmmLib@@AEAAITGMM_ESCAPE_HANDLE_REC@@0PEAU__GMM_GFX_PARTITIONING@@ETGMM_ESCAPE_FUNC_TYPE_REC@@@Z` | `0x351470` | 519 | UnwindData |  |
| 147 | `?__GetSetSharedHeapObjectProcessSingleton@GmmClientContext@GmmLib@@AEAAPEAXTGMM_ESCAPE_HANDLE_REC@@0TGMM_ESCAPE_FUNC_TYPE_REC@@@Z` | `0x351680` | 123 | UnwindData |  |
| 85 | `?GetSetGfxPartitionProcessSingleton@GmmClientContext@GmmLib@@AEAAXTGMM_ESCAPE_HANDLE_REC@@0PEAU__GMM_GFX_PARTITIONING@@ETGMM_ESCAPE_FUNC_TYPE_REC@@@Z` | `0x351710` | 116 | UnwindData |  |
| 131 | `?ReserveSVMGPUVA@GmmClientContext@GmmLib@@AEAA?AW4GMM_STATUS_ENUM@@PEAU_GMM_DEVICE_CALLBACKS_INT@@PEAU__GMM_GFX_PARTITIONING@@@Z` | `0x351940` | 120 | UnwindData |  |
| 82 | `?GetOverrideGfxPartition@GmmClientContext@GmmLib@@AEAA?AU__GMM_GFX_PARTITIONING@@PEAU3@TGMM_ESCAPE_HANDLE_REC@@1TGMM_ESCAPE_FUNC_TYPE_REC@@@Z` | `0x351C30` | 226 | UnwindData |  |
| 72 | `?GetGSCBuffer@GmmClientContext@GmmLib@@UEAA?AW4GMM_STATUS_ENUM@@TGMM_ESCAPE_HANDLE_REC@@0PEAPEAXPEAITGMM_ESCAPE_FUNC_TYPE_REC@@@Z` | `0x3521B0` | 251 | UnwindData |  |
| 52 | `?FreeGSCBuffer@GmmClientContext@GmmLib@@UEAA?AW4GMM_STATUS_ENUM@@TGMM_ESCAPE_HANDLE_REC@@0PEAXTGMM_ESCAPE_FUNC_TYPE_REC@@@Z` | `0x3522C0` | 245 | UnwindData |  |
| 25 | `?ConfigureDeviceAddressSpace@GmmClientContext@GmmLib@@UEAAETGMM_ESCAPE_HANDLE_REC@@0TGMM_ESCAPE_FUNC_TYPE_REC@@_KEEE22@Z` | `0x3523C0` | 294 | UnwindData |  |
| 124 | `?QueryCpuVisibleLMEMBytes@GmmClientContext@GmmLib@@UEAA?AW4GMM_STATUS_ENUM@@TGMM_ESCAPE_HANDLE_REC@@0TGMM_ESCAPE_FUNC_TYPE_REC@@PEA_K2@Z` | `0x3524F0` | 297 | UnwindData |  |
| 119 | `?OverrideGfxPartition@GmmClientContext@GmmLib@@UEAA?AU__GMM_GFX_PARTITIONING@@XZ` | `0x352620` | 69 | UnwindData |  |
| 118 | `?OverrideGfxPartition@GmmClientContext@GmmLib@@UEAA?AU__GMM_GFX_PARTITIONING@@PEAU3@TGMM_ESCAPE_HANDLE_REC@@1TGMM_ESCAPE_FUNC_TYPE_REC@@@Z` | `0x352670` | 43 | UnwindData |  |
| 49 | `?EnhancedBufferMap@GmmClientContext@GmmLib@@UEAAETGMM_ESCAPE_HANDLE_REC@@0TGMM_ESCAPE_FUNC_TYPE_REC@@IQEAPEAUGMM_ENHANCED_BUFFER_INFO_REC@@@Z` | `0x3526B0` | 317 | UnwindData |  |
| 74 | `?GetHeap32Base@GmmClientContext@GmmLib@@UEAA_KTGMM_ESCAPE_HANDLE_REC@@0PEAITGMM_ESCAPE_FUNC_TYPE_REC@@@Z` | `0x352800` | 236 | UnwindData |  |
| 96 | `?GetTrashPageGfxAddress@GmmClientContext@GmmLib@@UEAA_KTGMM_ESCAPE_HANDLE_REC@@0TGMM_ESCAPE_FUNC_TYPE_REC@@@Z` | `0x352900` | 226 | UnwindData |  |
| 139 | `?UmSetupHeap@GmmClientContext@GmmLib@@UEAAPEAUGMM_HEAP_REC@@TGMM_ESCAPE_HANDLE_REC@@0_K1ITGMM_ESCAPE_FUNC_TYPE_REC@@@Z` | `0x3529F0` | 426 | UnwindData |  |
| 138 | `?UmDestroypHeap@GmmClientContext@GmmLib@@UEAA?AW4GMM_STATUS_ENUM@@TGMM_ESCAPE_HANDLE_REC@@0PEAPEAUGMM_HEAP_REC@@TGMM_ESCAPE_FUNC_TYPE_REC@@@Z` | `0x352BA0` | 270 | UnwindData |  |
| 15 | `?AllocateHeapVA@GmmClientContext@GmmLib@@UEAA_KPEAUGMM_HEAP_REC@@_K@Z` | `0x352CC0` | 98 | UnwindData |  |
| 14 | `?AllocateHeapVA@GmmClientContext@GmmLib@@QEAA_KPEAUGMM_HEAP_REC@@_KI@Z` | `0x352D30` | 105 | UnwindData |  |
| 54 | `?FreeHeapVA@GmmClientContext@GmmLib@@UEAA?AW4GMM_STATUS_ENUM@@PEAUGMM_HEAP_REC@@_K1@Z` | `0x352DA0` | 42 | UnwindData |  |
| 126 | `?ResDestroySvmAllocation@GmmClientContext@GmmLib@@UEAAETGMM_ESCAPE_HANDLE_REC@@0ITGMM_ESCAPE_FUNC_TYPE_REC@@@Z` | `0x352DD0` | 81 | UnwindData |  |
| 84 | `?GetSLMaddressRange@GmmClientContext@GmmLib@@UEAA_KTGMM_ESCAPE_HANDLE_REC@@0_KTGMM_ESCAPE_FUNC_TYPE_REC@@@Z` | `0x352EF0` | 252 | UnwindData |  |
| 66 | `?GetD3dSwizzlePattern@GmmClientContext@GmmLib@@UEAAXPEBU_SWIZZLE_DESCRIPTOR@@EPEAUD3DWDDM2_0DDI_SWIZZLE_PATTERN_DESC@@@Z` | `0x353000` | 183 | UnwindData |  |
| 67 | `?GetD3dSwizzlePattern@GmmClientContext@GmmLib@@UEAAXPEBU_SWIZZLE_DESCRIPTOR@@EPEAUD3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC@@@Z` | `0x3530C0` | 178 | UnwindData |  |
| 65 | `?GetD3dSwizzlePattern@GmmClientContext@GmmLib@@UEAAXPEBU_SWIZZLE_DESCRIPTOR@@EPEAUD3D12DDI_SWIZZLE_PATTERN_DESC_0022@@@Z` | `0x353180` | 178 | UnwindData |  |
| 64 | `?GetD3dSwizzlePattern@GmmClientContext@GmmLib@@UEAAXPEBU_SWIZZLE_DESCRIPTOR@@EPEAUD3D12DDI_SWIZZLE_PATTERN_DESC_0004@@@Z` | `0x353240` | 183 | UnwindData |  |
| 122 | `?PigmsReserveGpuVA@GmmClientContext@GmmLib@@UEAA_KTGMM_ESCAPE_HANDLE_REC@@0_KTGMM_ESCAPE_FUNC_TYPE_REC@@@Z` | `0x353300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `?PigmsMapGpuVA@GmmClientContext@GmmLib@@UEAAETGMM_ESCAPE_HANDLE_REC@@0_KIPEAVGmmResourceInfoWin@2@TGMM_ESCAPE_FUNC_TYPE_REC@@@Z` | `0x353310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `?PigmsFreeGpuVa@GmmClientContext@GmmLib@@UEAAETGMM_ESCAPE_HANDLE_REC@@0_K1TGMM_ESCAPE_FUNC_TYPE_REC@@@Z` | `0x353320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `?ResUpdateAfterSharedOpen@GmmClientContext@GmmLib@@UEAA?AW4GMM_STATUS_ENUM@@PEAX0IPEAVGmmResourceInfoWin@2@TGMM_ESCAPE_FUNC_TYPE_REC@@@Z` | `0x353330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `?CreateTiledResource@GmmClientContext@GmmLib@@UEAAETGMM_ESCAPE_HANDLE_REC@@0PEAUGMM_UMD_SYNCCONTEXT_REC@@PEAUGMM_TRANSLATIONTABLE_CALLBACKS_REC@@PEAVGmmResourceInfoWin@2@TGMM_ESCAPE_FUNC_TYPE_REC@@I@Z` | `0x353340` | 71 | UnwindData |  |
| 48 | `?DestroyTiledResource@GmmClientContext@GmmLib@@UEAAETGMM_ESCAPE_HANDLE_REC@@0PEAUGMM_UMD_SYNCCONTEXT_REC@@PEAUGMM_TRANSLATIONTABLE_CALLBACKS_REC@@PEAVGmmResourceInfoWin@2@TGMM_ESCAPE_FUNC_TYPE_REC@@I@Z` | `0x353390` | 71 | UnwindData |  |
| 47 | `?DestroyTiledResource@GmmClientContext@GmmLib@@QEAAETGMM_ESCAPE_HANDLE_REC@@0PEAUGMM_UMD_SYNCCONTEXT_REC@@PEAUGMM_TRANSLATIONTABLE_CALLBACKS_REC@@PEAVGmmResourceInfoWin@2@TGMM_ESCAPE_FUNC_TYPE_REC@@IPEAU_GmmClientAllocationCallbacks_@@@Z` | `0x3533E0` | 35 | UnwindData |  |
| 144 | `?UpdateTiledResourceMapping@GmmClientContext@GmmLib@@UEAA?AW4GMM_STATUS_ENUM@@TGMM_ESCAPE_HANDLE_REC@@0UGMM_UPDATE_TILE_MAPPINGS_REC_INT@@EPEAUGMM_UMD_SYNCCONTEXT_REC@@PEAUGMM_TRANSLATIONTABLE_CALLBACKS_REC@@TGMM_ESCAPE_FUNC_TYPE_REC@@PEAU_GMM_DEVICE_CALLBACKS_INT@@IE@Z` | `0x3534A0` | 194 | UnwindData |  |
| 141 | `?UpdateSparseResourceOpaqueMapping@GmmClientContext@GmmLib@@UEAA?AW4GMM_STATUS_ENUM@@TGMM_ESCAPE_HANDLE_REC@@0PEAUGMM_UMD_SYNCCONTEXT_REC@@PEAUGMM_TRANSLATIONTABLE_CALLBACKS_REC@@TGMM_ESCAPE_FUNC_TYPE_REC@@EIPEAUGMM_UPDATE_SPARSE_RESOURCE_OPAQUE_MAPPINGS_REC@@@Z` | `0x353570` | 83 | UnwindData |  |
| 28 | `?CopyTileMappings@GmmClientContext@GmmLib@@UEAA?AW4GMM_STATUS_ENUM@@TGMM_ESCAPE_HANDLE_REC@@0UGMM_COPY_TILE_MAPPINGS_REC_INT@@EPEAUGMM_UMD_SYNCCONTEXT_REC@@PEAUGMM_TRANSLATIONTABLE_CALLBACKS_REC@@TGMM_ESCAPE_FUNC_TYPE_REC@@PEAU_GMM_DEVICE_CALLBACKS_INT@@IE@Z` | `0x3535D0` | 169 | UnwindData |  |
| 16 | `?AuxTilePoolSize@GmmClientContext@GmmLib@@UEAA_KPEAVGmmResourceInfoWin@2@I@Z` | `0x353680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `?GetLogicalTileShape@GmmClientContext@GmmLib@@UEAA?AW4GMM_STATUS_ENUM@@IPEAI00@Z` | `0x3536A0` | 41 | UnwindData |  |
| 95 | `?GetTileShape@GmmClientContext@GmmLib@@UEAA?AW4GMM_STATUS_ENUM@@PEAVGmmResourceInfoWin@2@PEAI11@Z` | `0x3536D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `?GetTileGfxAddress@GmmClientContext@GmmLib@@UEAA_KPEAVGmmResourceInfoWin@2@IIII@Z` | `0x3536F0` | 36 | UnwindData |  |
| 80 | `?GetMaxGpuVirtualAddressBits@GmmClientContext@GmmLib@@UEAAIPEAVGmmResourceInfoWin@2@@Z` | `0x353720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `?CachePolicyGetPATIndex@GmmClientContext@GmmLib@@UEAAIPEAVGmmResourceInfoWin@2@W4GMM_RESOURCE_USAGE_TYPE_ENUM@@@Z` | `0x353740` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `?GetSurfaceStateL2CachePolicy@GmmClientContext@GmmLib@@UEAAEW4GMM_RESOURCE_USAGE_TYPE_ENUM@@@Z` | `0x353770` | 50 | UnwindData |  |
| 92 | `?GetSwizzleDesc@GmmClientContext@GmmLib@@UEAAPEBU_SWIZZLE_DESCRIPTOR@@W4_EXTERNAL_SWIZZLE_NAME@@W4_EXTERNAL_RES_TYPE@@E_N@Z` | `0x3537B0` | 1,672 | UnwindData |  |
| 31 | `?CreateCustomResInfoObject_2@GmmClientContext@GmmLib@@UEAAPEAVGmmResourceInfoWin@2@PEAUGMM_RESCREATE_CUSTOM_PARAMS_2_REC@@@Z` | `0x353E40` | 152 | UnwindData |  |
| 36 | `?CreatePool@GmmClientContext@GmmLib@@UEAAJAEBU_GMM_CREATE_POOL_DESC_@@IAEAPEAX@Z` | `0x354170` | 217 | UnwindData |  |
| 43 | `?DestroyPool@GmmClientContext@GmmLib@@UEAAJPEAX@Z` | `0x354250` | 153 | UnwindData |  |
| 13 | `?AllocMemory@GmmClientContext@GmmLib@@UEAAJPEAX_KI1PEBUGMM_INITIAL_DATA@@AEAPEAXAEAUGMM_ALLOC_INFO@@@Z` | `0x3542F0` | 207 | UnwindData |  |
| 55 | `?FreeMemory@GmmClientContext@GmmLib@@UEAAJIPEBQEAXIPEA_K_K@Z` | `0x3543D0` | 37 | UnwindData |  |
| 73 | `?GetGpuVA@GmmClientContext@GmmLib@@UEAA_KPEAX@Z` | `0x354460` | 54 | UnwindData |  |
| 123 | `?PoolTrim@GmmClientContext@GmmLib@@UEAAJPEAXIAEA_K@Z` | `0x3544A0` | 151 | UnwindData |  |
| 50 | `?Evict@GmmClientContext@GmmLib@@UEAAJIPEBQEAXIAEA_K@Z` | `0x354540` | 827 | UnwindData |  |
| 112 | `?MakeResident@GmmClientContext@GmmLib@@UEAAJIIPEBQEAXIAEA_K1@Z` | `0x354890` | 164 | UnwindData |  |
| 117 | `?Offer@GmmClientContext@GmmLib@@UEAAJIPEBQEAXW4GMM_OFFER_PRIORITY@@I@Z` | `0x354C70` | 99 | UnwindData |  |
| 125 | `?Reclaim@GmmClientContext@GmmLib@@UEAAJIIPEBQEAXPEAW4GMM_RECLAIM_RESULT@@PEAHAEA_K@Z` | `0x355030` | 122 | UnwindData |  |
| 133 | `?ResetStream@GmmClientContext@GmmLib@@UEAAJPEAXPEA_K_K@Z` | `0x355480` | 111 | UnwindData |  |
| 29 | `?CreateAllocation@GmmClientContext@GmmLib@@UEAAJPEAXAEBU_GMM_CREATE_RESOURCE_DESC@@PEBUGMM_INITIAL_DATA@@AEAPEAXPEAPEAX@Z` | `0x355500` | 142 | UnwindData |  |
| 39 | `?CreateResource@GmmClientContext@GmmLib@@UEAAJPEAXAEBU_GMM_CREATE_RESOURCE_DESC@@_KAEAPEAX@Z` | `0x3555A0` | 337 | UnwindData |  |
| 46 | `?DestroyResource@GmmClientContext@GmmLib@@UEAAJPEAXIPEA_K_K@Z` | `0x355700` | 680 | UnwindData |  |
| 113 | `?MapCpuVA@GmmClientContext@GmmLib@@UEAAJPEAXPEAPEAX@Z` | `0x3559B0` | 105 | UnwindData |  |
| 127 | `?ResMapGpuVA@GmmClientContext@GmmLib@@UEAAJAEAUGMM_RES_MAP_GPUVA_ARG@@@Z` | `0x355A20` | 191 | UnwindData |  |
| 68 | `?GetDebugAllocationInfo@GmmClientContext@GmmLib@@UEAAJIPEBQEAXPEAIPEATGMM_GPU_VA_INFO@@1PEATGMM_KMT_ALLOCATION_INFO@@@Z` | `0x355AF0` | 94 | UnwindData |  |
| 102 | `?GmmSetResidencyPriority@GmmClientContext@GmmLib@@UEAAJPEAXI@Z` | `0x355F10` | 160 | UnwindData |  |
| 107 | `?IsNonTrivialResourcePoolingEnabled@GmmClientContext@GmmLib@@UEAA_NXZ` | `0x355FC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `InitializeGmm` | `0x355FE0` | 58 | UnwindData |  |
| 152 | `GmmAdapterDestroy` | `0x356090` | 24 | UnwindData |  |
| 11 | `??_7GmmClientContext@GmmLib@@6B@` | `0x367A80` | 888 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `??_7GmmPageTableMgr@GmmLib@@6B@` | `0x367DF8` | 0 | Indeterminate |  |
