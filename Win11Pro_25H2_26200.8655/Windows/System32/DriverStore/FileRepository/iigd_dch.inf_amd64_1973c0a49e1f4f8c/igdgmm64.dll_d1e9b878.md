# Binary Specification: igdgmm64.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_1973c0a49e1f4f8c\igdgmm64.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d1e9b878800a35794a5de4ed7648d83ad2af320c9019a5ee43bc58477913857b`
* **Total Exported Functions:** 142

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `??0GmmClientContext@GmmLib@@QEAA@AEBV01@@Z` | `0x1220` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `??0GmmPageTableMgr@GmmLib@@QEAA@AEBV01@@Z` | `0x1330` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `??4GmmClientContext@GmmLib@@QEAAAEAV01@AEBV01@@Z` | `0x14D0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `??4GmmPageTableMgr@GmmLib@@QEAAAEAV01@AEBV01@@Z` | `0x15D0` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `?GetClientContext@GmmPageTableMgr@GmmLib@@UEAAPEAVGmmClientContext@2@XZ` | `0x18D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `?GetClientType@GmmClientContext@GmmLib@@UEAA?AW4GMM_CLIENT_ENUM@@XZ` | `0x18E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `?GetDeviceCallback@GmmClientContext@GmmLib@@QEAAPEAU_GMM_DEVICE_CALLBACKS_INT@@XZ` | `0x18F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `?GetLibContext@GmmClientContext@GmmLib@@UEAAPEAVContext@2@XZ` | `0x1910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `?GetLibContext@GmmPageTableMgr@GmmLib@@AEAAPEAVContext@2@XZ` | `0x1920` | 3,151,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `??0GmmPageTableMgr@GmmLib@@QEAA@XZ` | `0x302E10` | 164 | UnwindData |  |
| 6 | `??0GmmPageTableMgr@GmmLib@@QEAA@PEAU_GMM_DEVICE_CALLBACKS_INT@@IPEAVGmmClientContext@1@@Z` | `0x302EC0` | 1,502 | UnwindData |  |
| 5 | `??0GmmPageTableMgr@GmmLib@@QEAA@PEAU_GMM_DEVICE_CALLBACKS_INT@@IPEAUGMM_TRANSLATIONTABLE_CALLBACKS_REC@@PEAVGmmClientContext@1@@Z` | `0x3034B0` | 149 | UnwindData |  |
| 98 | `?InitGpuBBQueueCallbacks@GmmPageTableMgr@GmmLib@@UEAAXPEAUGMM_TRANSLATIONTABLE_CALLBACKS_REC@@@Z` | `0x303550` | 95 | UnwindData |  |
| 89 | `?GetTRL3TableAddr@GmmPageTableMgr@GmmLib@@UEAA_KXZ` | `0x3035C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `?GetAuxL3TableAddr@GmmPageTableMgr@GmmLib@@UEAA_KXZ` | `0x3035E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `?InitContextAuxTableRegister@GmmPageTableMgr@GmmLib@@UEAA?AW4GMM_STATUS_ENUM@@PEAXW4_GMM_ENGINE_TYPE@@@Z` | `0x303600` | 86 | UnwindData |  |
| 97 | `?InitContextTRTableRegister@GmmPageTableMgr@GmmLib@@UEAA?AW4GMM_STATUS_ENUM@@PEAXW4_GMM_ENGINE_TYPE@@@Z` | `0x303720` | 227 | UnwindData |  |
| 123 | `?ReserveTRGpuVirtualAddress@GmmPageTableMgr@GmmLib@@UEAAJPEAUGMM_UMD_SYNCCONTEXT_REC@@PEAUD3DDDI_RESERVEGPUVIRTUALADDRESS@@E@Z` | `0x303940` | 24 | UnwindData |  |
| 107 | `?MapTRGpuVirtualAddress@GmmPageTableMgr@GmmLib@@UEAAJPEAU_GMM_MAP_TR_GPUVIRTUALADDRESS@@E@Z` | `0x3039E0` | 24 | UnwindData |  |
| 129 | `?UpdateTRGpuVirtualAddress@GmmPageTableMgr@GmmLib@@UEAAJPEAPEAUGMM_UMD_SYNCCONTEXT_REC@@PEBU_GMM_UPADTE_TR_GPUVIRTUALADDRESS_INT@@E@Z` | `0x303A70` | 24 | UnwindData |  |
| 54 | `?FreeTRGpuVirtualAddress@GmmPageTableMgr@GmmLib@@UEAAJPEAUGMM_UMD_SYNCCONTEXT_REC@@PEBTGMM_DDI_FREEGPUVIRTUALADDRSS_INT@@E@Z` | `0x303B10` | 24 | UnwindData |  |
| 127 | `?UpdateAuxTable@GmmPageTableMgr@GmmLib@@UEAA?AW4GMM_STATUS_ENUM@@PEBU__GMM_DDI_UPDATEAUXTABLE@@@Z` | `0x303BB0` | 1,995 | UnwindData |  |
| 136 | `?__ReleaseUnusedPool@GmmPageTableMgr@GmmLib@@UEAAXPEAUGMM_UMD_SYNCCONTEXT_REC@@@Z` | `0x304390` | 23 | UnwindData |  |
| 132 | `?__GetFreePoolNode@GmmPageTableMgr@GmmLib@@UEAAPEAVGmmPageTablePool@2@PEAIW4POOL_TYPE_REC@2@@Z` | `0x304700` | 573 | UnwindData |  |
| 49 | `?EvictPageTablePool@GmmPageTableMgr@GmmLib@@UEAAXPEAIH@Z` | `0x304950` | 14 | UnwindData |  |
| 94 | `?GmmSetCsrHandle@GmmPageTableMgr@GmmLib@@UEAAXPEAX@Z` | `0x304A10` | 9 | UnwindData |  |
| 9 | `??1GmmPageTableMgr@GmmLib@@UEAA@XZ` | `0x304B50` | 541 | UnwindData |  |
| 131 | `?__AllocateNodePool@GmmPageTableMgr@GmmLib@@AEAAPEAVGmmPageTablePool@2@IW4POOL_TYPE_REC@2@@Z` | `0x304D80` | 383 | UnwindData |  |
| 135 | `?__NotifyAuxTChange@GmmPageTableMgr@GmmLib@@AEAAX_KAEA_K1AEAE@Z` | `0x304F10` | 210 | UnwindData |  |
| 2 | `??0GmmClientContext@GmmLib@@QEAA@W4GMM_CLIENT_ENUM@@@Z` | `0x309E20` | 132 | UnwindData |  |
| 3 | `??0GmmClientContext@GmmLib@@QEAA@W4GMM_CLIENT_ENUM@@PEAVContext@1@@Z` | `0x309EB0` | 138 | UnwindData |  |
| 8 | `??1GmmClientContext@GmmLib@@UEAA@XZ` | `0x309F40` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `?CachePolicyGetMemoryObject@GmmClientContext@GmmLib@@UEAA?ATMEMORY_OBJECT_CONTROL_STATE_REC@@PEAVGmmResourceInfoWin@2@W4GMM_RESOURCE_USAGE_TYPE_ENUM@@@Z` | `0x309F70` | 37 | UnwindData |  |
| 24 | `?CachePolicyGetPteType@GmmClientContext@GmmLib@@UEAA?ATGMM_PTE_CACHE_CONTROL_BITS_REC@@W4GMM_RESOURCE_USAGE_TYPE_ENUM@@@Z` | `0x309FA0` | 37 | UnwindData |  |
| 22 | `?CachePolicyGetOriginalMemoryObject@GmmClientContext@GmmLib@@UEAA?ATMEMORY_OBJECT_CONTROL_STATE_REC@@PEAVGmmResourceInfoWin@2@@Z` | `0x309FD0` | 37 | UnwindData |  |
| 25 | `?CachePolicyIsUsagePTECached@GmmClientContext@GmmLib@@UEAAEW4GMM_RESOURCE_USAGE_TYPE_ENUM@@@Z` | `0x30A000` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `?GetSurfaceStateL1CachePolicy@GmmClientContext@GmmLib@@UEAAEW4GMM_RESOURCE_USAGE_TYPE_ENUM@@@Z` | `0x30A030` | 50 | UnwindData |  |
| 19 | `?CachePolicyGetMaxMocsIndex@GmmClientContext@GmmLib@@UEAAIXZ` | `0x30A070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `?CachePolicyGetMaxL1HdcMocsIndex@GmmClientContext@GmmLib@@UEAAIXZ` | `0x30A090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `?CachePolicyGetMaxSpecialMocsIndex@GmmClientContext@GmmLib@@UEAAIXZ` | `0x30A0B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `?GetCachePolicyUsage@GmmClientContext@GmmLib@@UEAAPEAUGMM_CACHE_POLICY_ELEMENT_REC@@XZ` | `0x30A0E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `?GetCacheSizes@GmmClientContext@GmmLib@@UEAAXPEAUGMM_CACHE_SIZES_REC@@@Z` | `0x30A100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `?GetUseGlobalGtt@GmmClientContext@GmmLib@@UEAAEW4GMM_HW_COMMAND_STREAMER_ENUM@@W4GMM_HW_COMMAND_ENUM@@PEAT__D3DDDI_PATCHLOCATIONLIST_DRIVERID@@@Z` | `0x30A120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `?GetCachePolicyElement@GmmClientContext@GmmLib@@UEAA?AUGMM_CACHE_POLICY_ELEMENT_REC@@W4GMM_RESOURCE_USAGE_TYPE_ENUM@@@Z` | `0x30A140` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `?GetCachePolicyTlbElement@GmmClientContext@GmmLib@@UEAA?AUGMM_CACHE_POLICY_TBL_ELEMENT_REC@@I@Z` | `0x30A190` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `?GetPlatformInfo@GmmClientContext@GmmLib@@UEAAAEAU__GMM_PLATFORM_RESOURCE_REC@@XZ` | `0x30A1D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `?GetSkuTable@GmmClientContext@GmmLib@@UEAAAEBU_SKU_FEATURE_TABLE@@XZ` | `0x30A1F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `?GetExtendedTextureAlign@GmmClientContext@GmmLib@@UEAAXIAEAU__TEX_ALIGNMENT@@@Z` | `0x30A210` | 89 | UnwindData |  |
| 101 | `?IsPlanar@GmmClientContext@GmmLib@@UEAAEW4GMM_RESOURCE_FORMAT_ENUM@@@Z` | `0x30A270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `?IsP0xx@GmmClientContext@GmmLib@@UEAAEW4GMM_RESOURCE_FORMAT_ENUM@@@Z` | `0x30A280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `?IsUVPacked@GmmClientContext@GmmLib@@UEAAEW4GMM_RESOURCE_FORMAT_ENUM@@@Z` | `0x30A290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `?IsCompressed@GmmClientContext@GmmLib@@UEAAEW4GMM_RESOURCE_FORMAT_ENUM@@@Z` | `0x30A2A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `?IsYUVPacked@GmmClientContext@GmmLib@@UEAAEW4GMM_RESOURCE_FORMAT_ENUM@@@Z` | `0x30A2E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `?GetSurfaceStateFormat@GmmClientContext@GmmLib@@UEAA?AW4GMM_SURFACESTATE_FORMAT_ENUM@@W4GMM_RESOURCE_FORMAT_ENUM@@@Z` | `0x30A2F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `?GetSurfaceStateCompressionFormat@GmmClientContext@GmmLib@@UEAAEW4GMM_RESOURCE_FORMAT_ENUM@@@Z` | `0x30A330` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `?GetMediaSurfaceStateCompressionFormat@GmmClientContext@GmmLib@@UEAAEW4GMM_RESOURCE_FORMAT_ENUM@@@Z` | `0x30A360` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `?GetLosslessCompressionType@GmmClientContext@GmmLib@@UEAA?AW4GMM_E2ECOMP_FORMAT_ENUM@@W4GMM_RESOURCE_FORMAT_ENUM@@@Z` | `0x30A390` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `?GetInternalGpuVaRangeLimit@GmmClientContext@GmmLib@@UEAA_KXZ` | `0x30A3C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `?CreateResInfoObject@GmmClientContext@GmmLib@@UEAAPEAVGmmResourceInfoWin@2@PEAUGMM_RESCREATE_PARAMS_REC@@@Z` | `0x30A3E0` | 193 | UnwindData |  |
| 27 | `?CopyResInfoObject@GmmClientContext@GmmLib@@UEAAPEAVGmmResourceInfoWin@2@PEAV32@@Z` | `0x30A4B0` | 153 | UnwindData |  |
| 119 | `?ResMemcpy@GmmClientContext@GmmLib@@UEAAXPEAX0@Z` | `0x30A550` | 107 | UnwindData |  |
| 43 | `?DestroyResInfoObject@GmmClientContext@GmmLib@@UEAAXPEAVGmmResourceInfoWin@2@@Z` | `0x30A5D0` | 122 | UnwindData |  |
| 33 | `?CreatePageTblMgrObject@GmmClientContext@GmmLib@@UEAAPEAVGmmPageTableMgr@2@PEAU_GMM_DEVICE_CALLBACKS_INT@@PEAUGMM_TRANSLATIONTABLE_CALLBACKS_REC@@I@Z` | `0x30A650` | 136 | UnwindData |  |
| 31 | `?CreatePageTblMgrObject@GmmClientContext@GmmLib@@UEAAPEAVGmmPageTableMgr@2@PEAUGMM_TRANSLATIONTABLE_CALLBACKS_REC@@I@Z` | `0x30A6E0` | 54 | UnwindData |  |
| 40 | `?DestroyPageTblMgrObject@GmmClientContext@GmmLib@@UEAAXPEAVGmmPageTableMgr@2@@Z` | `0x30A720` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `?CreateResInfoObject@GmmClientContext@GmmLib@@UEAAPEAVGmmResourceInfoWin@2@PEAUGMM_RESCREATE_PARAMS_REC@@PEAU_GmmClientAllocationCallbacks_@@@Z` | `0x30A750` | 54 | UnwindData |  |
| 44 | `?DestroyResInfoObject@GmmClientContext@GmmLib@@UEAAXPEAVGmmResourceInfoWin@2@PEAU_GmmClientAllocationCallbacks_@@@Z` | `0x30A870` | 179 | UnwindData |  |
| 108 | `?MapTileInstancedGpuVirtualAddress@GmmClientContext@GmmLib@@UEAAJPEAU_GMM_MAP_GPUVA_TILE_INSTANCED_RESOURCE@@@Z` | `0x30A930` | 1,288 | UnwindData |  |
| 106 | `?MapGpuVirtualAddress@GmmClientContext@GmmLib@@UEAAJPEAU_GMM_MAP_GPUVIRTUALADDRESS@@@Z` | `0x30AE40` | 3,442 | UnwindData |  |
| 121 | `?ReserveGpuVirtualAddress@GmmClientContext@GmmLib@@UEAAJPEAUD3DDDI_RESERVEGPUVIRTUALADDRESS@@@Z` | `0x30BBC0` | 41 | UnwindData |  |
| 51 | `?FreeGpuVirtualAddress@GmmClientContext@GmmLib@@UEAAJPEBU_GMM_FREEGPUVIRTUALADDRESS@@@Z` | `0x30BC50` | 256 | UnwindData |  |
| 34 | `?CreatePageTblMgrObject@GmmClientContext@GmmLib@@UEAAPEAVGmmPageTableMgr@2@PEAU_GMM_DEVICE_CALLBACKS_INT@@PEAUGMM_TRANSLATIONTABLE_CALLBACKS_REC@@IPEAU_GmmClientAllocationCallbacks_@@@Z` | `0x30BF80` | 200 | UnwindData |  |
| 32 | `?CreatePageTblMgrObject@GmmClientContext@GmmLib@@UEAAPEAVGmmPageTableMgr@2@PEAUGMM_TRANSLATIONTABLE_CALLBACKS_REC@@IPEAU_GmmClientAllocationCallbacks_@@@Z` | `0x30C050` | 59 | UnwindData |  |
| 41 | `?DestroyPageTblMgrObject@GmmClientContext@GmmLib@@UEAAXPEAVGmmPageTableMgr@2@PEAU_GmmClientAllocationCallbacks_@@@Z` | `0x30C0A0` | 105 | UnwindData |  |
| 95 | `?GmmSetDeviceInfo@GmmClientContext@GmmLib@@UEAA?AW4GMM_STATUS_ENUM@@PEAU_GMM_DEVICE_INFO_REC@@@Z` | `0x30C110` | 272 | UnwindData |  |
| 30 | `?CreateCustomResInfoObject@GmmClientContext@GmmLib@@UEAAPEAVGmmResourceInfoWin@2@PEAUGMM_RESCREATE_CUSTOM_PARAMS__REC@@@Z` | `0x30C340` | 152 | UnwindData |  |
| 134 | `?__GetSharedHeapObject@GmmClientContext@GmmLib@@AEAAPEAXTGMM_ESCAPE_HANDLE_REC@@0TGMM_ESCAPE_FUNC_TYPE_REC@@@Z` | `0x30C3E0` | 247 | UnwindData |  |
| 137 | `?__SetSharedHeapObject@GmmClientContext@GmmLib@@AEAAITGMM_ESCAPE_HANDLE_REC@@0PEAPEAXTGMM_ESCAPE_FUNC_TYPE_REC@@@Z` | `0x30C4E0` | 291 | UnwindData |  |
| 82 | `?GetSetProcessGfxPartition@GmmClientContext@GmmLib@@AEAAITGMM_ESCAPE_HANDLE_REC@@0PEAU__GMM_GFX_PARTITIONING@@ETGMM_ESCAPE_FUNC_TYPE_REC@@@Z` | `0x30C610` | 491 | UnwindData |  |
| 133 | `?__GetSetSharedHeapObjectProcessSingleton@GmmClientContext@GmmLib@@AEAAPEAXTGMM_ESCAPE_HANDLE_REC@@0TGMM_ESCAPE_FUNC_TYPE_REC@@@Z` | `0x30C810` | 123 | UnwindData |  |
| 81 | `?GetSetGfxPartitionProcessSingleton@GmmClientContext@GmmLib@@AEAAXTGMM_ESCAPE_HANDLE_REC@@0PEAU__GMM_GFX_PARTITIONING@@ETGMM_ESCAPE_FUNC_TYPE_REC@@@Z` | `0x30C8A0` | 116 | UnwindData |  |
| 122 | `?ReserveSVMGPUVA@GmmClientContext@GmmLib@@AEAA?AW4GMM_STATUS_ENUM@@PEAU_GMM_DEVICE_CALLBACKS_INT@@PEAU__GMM_GFX_PARTITIONING@@@Z` | `0x30CAB0` | 120 | UnwindData |  |
| 78 | `?GetOverrideGfxPartition@GmmClientContext@GmmLib@@AEAA?AU__GMM_GFX_PARTITIONING@@PEAU3@TGMM_ESCAPE_HANDLE_REC@@1TGMM_ESCAPE_FUNC_TYPE_REC@@@Z` | `0x30CDA0` | 242 | UnwindData |  |
| 68 | `?GetGSCBuffer@GmmClientContext@GmmLib@@UEAA?AW4GMM_STATUS_ENUM@@TGMM_ESCAPE_HANDLE_REC@@0PEAPEAXPEAITGMM_ESCAPE_FUNC_TYPE_REC@@@Z` | `0x30D330` | 251 | UnwindData |  |
| 50 | `?FreeGSCBuffer@GmmClientContext@GmmLib@@UEAA?AW4GMM_STATUS_ENUM@@TGMM_ESCAPE_HANDLE_REC@@0PEAXTGMM_ESCAPE_FUNC_TYPE_REC@@@Z` | `0x30D440` | 245 | UnwindData |  |
| 26 | `?ConfigureDeviceAddressSpace@GmmClientContext@GmmLib@@UEAAETGMM_ESCAPE_HANDLE_REC@@0TGMM_ESCAPE_FUNC_TYPE_REC@@_KEEE22@Z` | `0x30D540` | 291 | UnwindData |  |
| 111 | `?OverrideGfxPartition@GmmClientContext@GmmLib@@UEAA?AU__GMM_GFX_PARTITIONING@@XZ` | `0x30D670` | 88 | UnwindData |  |
| 110 | `?OverrideGfxPartition@GmmClientContext@GmmLib@@UEAA?AU__GMM_GFX_PARTITIONING@@PEAU3@TGMM_ESCAPE_HANDLE_REC@@1TGMM_ESCAPE_FUNC_TYPE_REC@@@Z` | `0x30D6D0` | 43 | UnwindData |  |
| 47 | `?EnhancedBufferMap@GmmClientContext@GmmLib@@UEAAETGMM_ESCAPE_HANDLE_REC@@0TGMM_ESCAPE_FUNC_TYPE_REC@@IQEAPEAUGMM_ENHANCED_BUFFER_INFO_REC@@@Z` | `0x30D710` | 317 | UnwindData |  |
| 70 | `?GetHeap32Base@GmmClientContext@GmmLib@@UEAA_KTGMM_ESCAPE_HANDLE_REC@@0PEAITGMM_ESCAPE_FUNC_TYPE_REC@@@Z` | `0x30D860` | 236 | UnwindData |  |
| 92 | `?GetTrashPageGfxAddress@GmmClientContext@GmmLib@@UEAA_KTGMM_ESCAPE_HANDLE_REC@@0TGMM_ESCAPE_FUNC_TYPE_REC@@@Z` | `0x30D960` | 226 | UnwindData |  |
| 126 | `?UmSetupHeap@GmmClientContext@GmmLib@@UEAAPEAUGMM_HEAP_REC@@TGMM_ESCAPE_HANDLE_REC@@0_K1ITGMM_ESCAPE_FUNC_TYPE_REC@@@Z` | `0x30DA50` | 426 | UnwindData |  |
| 125 | `?UmDestroypHeap@GmmClientContext@GmmLib@@UEAA?AW4GMM_STATUS_ENUM@@TGMM_ESCAPE_HANDLE_REC@@0PEAPEAUGMM_HEAP_REC@@TGMM_ESCAPE_FUNC_TYPE_REC@@@Z` | `0x30DC00` | 270 | UnwindData |  |
| 16 | `?AllocateHeapVA@GmmClientContext@GmmLib@@UEAA_KPEAUGMM_HEAP_REC@@_K@Z` | `0x30DD20` | 98 | UnwindData |  |
| 15 | `?AllocateHeapVA@GmmClientContext@GmmLib@@QEAA_KPEAUGMM_HEAP_REC@@_KI@Z` | `0x30DD90` | 105 | UnwindData |  |
| 52 | `?FreeHeapVA@GmmClientContext@GmmLib@@UEAA?AW4GMM_STATUS_ENUM@@PEAUGMM_HEAP_REC@@_K1@Z` | `0x30DE00` | 42 | UnwindData |  |
| 117 | `?ResDestroySvmAllocation@GmmClientContext@GmmLib@@UEAAETGMM_ESCAPE_HANDLE_REC@@0ITGMM_ESCAPE_FUNC_TYPE_REC@@@Z` | `0x30DE30` | 81 | UnwindData |  |
| 80 | `?GetSLMaddressRange@GmmClientContext@GmmLib@@UEAA_KTGMM_ESCAPE_HANDLE_REC@@0_KTGMM_ESCAPE_FUNC_TYPE_REC@@@Z` | `0x30DF50` | 252 | UnwindData |  |
| 64 | `?GetD3dSwizzlePattern@GmmClientContext@GmmLib@@UEAAXPEBU_SWIZZLE_DESCRIPTOR@@EPEAUD3DWDDM2_0DDI_SWIZZLE_PATTERN_DESC@@@Z` | `0x30E060` | 183 | UnwindData |  |
| 65 | `?GetD3dSwizzlePattern@GmmClientContext@GmmLib@@UEAAXPEBU_SWIZZLE_DESCRIPTOR@@EPEAUD3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC@@@Z` | `0x30E120` | 178 | UnwindData |  |
| 63 | `?GetD3dSwizzlePattern@GmmClientContext@GmmLib@@UEAAXPEBU_SWIZZLE_DESCRIPTOR@@EPEAUD3D12DDI_SWIZZLE_PATTERN_DESC_0022@@@Z` | `0x30E1E0` | 178 | UnwindData |  |
| 62 | `?GetD3dSwizzlePattern@GmmClientContext@GmmLib@@UEAAXPEBU_SWIZZLE_DESCRIPTOR@@EPEAUD3D12DDI_SWIZZLE_PATTERN_DESC_0004@@@Z` | `0x30E2A0` | 183 | UnwindData |  |
| 114 | `?PigmsReserveGpuVA@GmmClientContext@GmmLib@@UEAA_KTGMM_ESCAPE_HANDLE_REC@@0_KTGMM_ESCAPE_FUNC_TYPE_REC@@@Z` | `0x30E360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `?PigmsMapGpuVA@GmmClientContext@GmmLib@@UEAAETGMM_ESCAPE_HANDLE_REC@@0_KIPEAVGmmResourceInfoWin@2@TGMM_ESCAPE_FUNC_TYPE_REC@@@Z` | `0x30E370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `?PigmsFreeGpuVa@GmmClientContext@GmmLib@@UEAAETGMM_ESCAPE_HANDLE_REC@@0_K1TGMM_ESCAPE_FUNC_TYPE_REC@@@Z` | `0x30E380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `?ResUpdateAfterSharedOpen@GmmClientContext@GmmLib@@UEAA?AW4GMM_STATUS_ENUM@@PEAX0IPEAVGmmResourceInfoWin@2@TGMM_ESCAPE_FUNC_TYPE_REC@@@Z` | `0x30E390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `?CreateTiledResource@GmmClientContext@GmmLib@@UEAAETGMM_ESCAPE_HANDLE_REC@@0PEAUGMM_UMD_SYNCCONTEXT_REC@@PEAUGMM_TRANSLATIONTABLE_CALLBACKS_REC@@PEAVGmmResourceInfoWin@2@TGMM_ESCAPE_FUNC_TYPE_REC@@I@Z` | `0x30E3A0` | 71 | UnwindData |  |
| 46 | `?DestroyTiledResource@GmmClientContext@GmmLib@@UEAAETGMM_ESCAPE_HANDLE_REC@@0PEAUGMM_UMD_SYNCCONTEXT_REC@@PEAUGMM_TRANSLATIONTABLE_CALLBACKS_REC@@PEAVGmmResourceInfoWin@2@TGMM_ESCAPE_FUNC_TYPE_REC@@I@Z` | `0x30E3F0` | 71 | UnwindData |  |
| 130 | `?UpdateTiledResourceMapping@GmmClientContext@GmmLib@@UEAA?AW4GMM_STATUS_ENUM@@TGMM_ESCAPE_HANDLE_REC@@0UGMM_UPDATE_TILE_MAPPINGS_REC_INT@@EPEAUGMM_UMD_SYNCCONTEXT_REC@@PEAUGMM_TRANSLATIONTABLE_CALLBACKS_REC@@TGMM_ESCAPE_FUNC_TYPE_REC@@PEAU_GMM_DEVICE_CALLBACKS_INT@@IE@Z` | `0x30E440` | 194 | UnwindData |  |
| 128 | `?UpdateSparseResourceOpaqueMapping@GmmClientContext@GmmLib@@UEAA?AW4GMM_STATUS_ENUM@@TGMM_ESCAPE_HANDLE_REC@@0PEAUGMM_UMD_SYNCCONTEXT_REC@@PEAUGMM_TRANSLATIONTABLE_CALLBACKS_REC@@TGMM_ESCAPE_FUNC_TYPE_REC@@EIPEAUGMM_UPDATE_SPARSE_RESOURCE_OPAQUE_MAPPINGS_REC@@@Z` | `0x30E510` | 83 | UnwindData |  |
| 28 | `?CopyTileMappings@GmmClientContext@GmmLib@@UEAA?AW4GMM_STATUS_ENUM@@TGMM_ESCAPE_HANDLE_REC@@0UGMM_COPY_TILE_MAPPINGS_REC_INT@@EPEAUGMM_UMD_SYNCCONTEXT_REC@@PEAUGMM_TRANSLATIONTABLE_CALLBACKS_REC@@TGMM_ESCAPE_FUNC_TYPE_REC@@PEAU_GMM_DEVICE_CALLBACKS_INT@@IE@Z` | `0x30E570` | 169 | UnwindData |  |
| 17 | `?AuxTilePoolSize@GmmClientContext@GmmLib@@UEAA_KPEAVGmmResourceInfoWin@2@I@Z` | `0x30E620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `?GetLogicalTileShape@GmmClientContext@GmmLib@@UEAA?AW4GMM_STATUS_ENUM@@IPEAI00@Z` | `0x30E640` | 41 | UnwindData |  |
| 91 | `?GetTileShape@GmmClientContext@GmmLib@@UEAA?AW4GMM_STATUS_ENUM@@PEAVGmmResourceInfoWin@2@PEAI11@Z` | `0x30E670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `?GetTileGfxAddress@GmmClientContext@GmmLib@@UEAA_KPEAVGmmResourceInfoWin@2@IIII@Z` | `0x30E690` | 36 | UnwindData |  |
| 76 | `?GetMaxGpuVirtualAddressBits@GmmClientContext@GmmLib@@UEAAIPEAVGmmResourceInfoWin@2@@Z` | `0x30E6C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `?CachePolicyGetPATIndex@GmmClientContext@GmmLib@@UEAAIPEAVGmmResourceInfoWin@2@W4GMM_RESOURCE_USAGE_TYPE_ENUM@@@Z` | `0x30E6E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `?GetSurfaceStateL2CachePolicy@GmmClientContext@GmmLib@@UEAAEW4GMM_RESOURCE_USAGE_TYPE_ENUM@@@Z` | `0x30E710` | 50 | UnwindData |  |
| 88 | `?GetSwizzleDesc@GmmClientContext@GmmLib@@UEAAPEBU_SWIZZLE_DESCRIPTOR@@W4_EXTERNAL_SWIZZLE_NAME@@W4_EXTERNAL_RES_TYPE@@E_N@Z` | `0x30E750` | 1,672 | UnwindData |  |
| 35 | `?CreatePool@GmmClientContext@GmmLib@@UEAA?AW4_GMM_RESULT@@AEBU_GMM_CREATE_POOL_DESC_@@IAEAPEAX@Z` | `0x30EEC0` | 188 | UnwindData |  |
| 42 | `?DestroyPool@GmmClientContext@GmmLib@@UEAA?AW4_GMM_RESULT@@PEAX@Z` | `0x30EF90` | 141 | UnwindData |  |
| 14 | `?AllocMemory@GmmClientContext@GmmLib@@UEAA?AW4_GMM_RESULT@@PEAX_KI1PEBXAEAPEAXAEAUGMM_ALLOC_INFO@@@Z` | `0x30F030` | 194 | UnwindData |  |
| 53 | `?FreeMemory@GmmClientContext@GmmLib@@UEAA?AW4_GMM_RESULT@@IPEBQEAXIPEA_K_K@Z` | `0x30F100` | 21 | UnwindData |  |
| 69 | `?GetGpuVA@GmmClientContext@GmmLib@@UEAA_KPEAX@Z` | `0x30F180` | 54 | UnwindData |  |
| 115 | `?PoolTrim@GmmClientContext@GmmLib@@UEAA?AW4_GMM_RESULT@@PEAXIAEA_K@Z` | `0x30F1C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `?Evict@GmmClientContext@GmmLib@@UEAA?AW4_GMM_RESULT@@IPEBQEAXIAEA_K@Z` | `0x30F1D0` | 709 | UnwindData |  |
| 104 | `?MakeResident@GmmClientContext@GmmLib@@UEAA?AW4_GMM_RESULT@@IIPEBQEAXIAEA_K1@Z` | `0x30F4A0` | 153 | UnwindData |  |
| 109 | `?Offer@GmmClientContext@GmmLib@@UEAA?AW4_GMM_RESULT@@IPEBQEAXW4GMM_OFFER_PRIORITY@@I@Z` | `0x30F810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `?Reclaim@GmmClientContext@GmmLib@@UEAA?AW4_GMM_RESULT@@IIPEBQEAXPEAW4GMM_RECLAIM_RESULT@@PEAH_K@Z` | `0x30F820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `?ResetStream@GmmClientContext@GmmLib@@UEAA?AW4_GMM_RESULT@@PEAXPEA_K_K@Z` | `0x30F830` | 93 | UnwindData |  |
| 29 | `?CreateAllocation@GmmClientContext@GmmLib@@UEAA?AW4_GMM_RESULT@@PEAXAEBU_GMM_CREATE_RESOURCE_DESC@@PEBTGMM_INITIAL_DATA@@AEAPEAXPEAPEAX@Z` | `0x30F8A0` | 108 | UnwindData |  |
| 38 | `?CreateResource@GmmClientContext@GmmLib@@UEAA?AW4_GMM_RESULT@@PEAXAEBU_GMM_CREATE_RESOURCE_DESC@@_KAEAPEAX@Z` | `0x30F920` | 270 | UnwindData |  |
| 45 | `?DestroyResource@GmmClientContext@GmmLib@@UEAA?AW4_GMM_RESULT@@PEAXIPEA_K_K@Z` | `0x30FA40` | 349 | UnwindData |  |
| 105 | `?MapCpuVA@GmmClientContext@GmmLib@@UEAA?AW4_GMM_RESULT@@PEAXPEAPEAX@Z` | `0x30FBB0` | 93 | UnwindData |  |
| 118 | `?ResMapGpuVA@GmmClientContext@GmmLib@@UEAA?AW4_GMM_RESULT@@AEAUGMM_RES_MAP_GPUVA_ARG@@@Z` | `0x30FC20` | 179 | UnwindData |  |
| 142 | `OpenGmm` | `0x30FCE0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `InitializeGmm` | `0x30FD20` | 58 | UnwindData |  |
| 138 | `GmmAdapterDestroy` | `0x30FDD0` | 24 | UnwindData |  |
| 140 | `GmmInit` | `0x30FE60` | 67 | UnwindData |  |
| 139 | `GmmDestroy` | `0x30FEB0` | 27 | UnwindData |  |
| 12 | `??_7GmmClientContext@GmmLib@@6B@` | `0x321A20` | 784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `??_7GmmPageTableMgr@GmmLib@@6B@` | `0x321D30` | 0 | Indeterminate |  |
