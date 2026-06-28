# Binary Specification: VSD3DWARPDebug.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\VSD3DWARPDebug.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d1bb8f95d05b9e9d11984c407002fadba4841812bc35e880322be28a2499b007`
* **Total Exported Functions:** 45

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `?ReadThreadRegisterWithSize@WarpDebugInternal@@YAJPEAXIW4VSD3D_REGISTER_SET@@I_KPEAEI@Z` | `0xC510` | 1,449 | UnwindData |  |
| 4 | `?VSD3DAttach@WarpDebugInternal@@YAJKUVSD3D_CONFIG_INFO@@PEAPEAX@Z` | `0xCE10` | 106 | UnwindData |  |
| 3 | `?VSD3DAttach2@WarpDebugInternal@@YAJKPEAXPEAPEAX@Z` | `0xD060` | 114 | UnwindData |  |
| 10 | `?VSD3DDetach@WarpDebugInternal@@YAJPEAXH@Z` | `0xD1F0` | 121 | UnwindData |  |
| 42 | `?VSD3DWaitForDebugEvent@WarpDebugInternal@@YAJPEAUVSD3D_DEBUG_EVENT@@PEAPEAXK@Z` | `0xD270` | 313 | UnwindData |  |
| 8 | `?VSD3DContinueDebugEvent@WarpDebugInternal@@YAJPEAXPEAUVSD3D_SINGLESTEP_INFO@@@Z` | `0xD3B0` | 928 | UnwindData |  |
| 19 | `?VSD3DGetDebugEvent@WarpDebugInternal@@YAJPEAUVSD3D_DEBUG_EVENT@@PEAX@Z` | `0xD760` | 83 | UnwindData |  |
| 5 | `?VSD3DBreak@WarpDebugInternal@@YAJPEAX@Z` | `0xD880` | 134 | UnwindData |  |
| 27 | `?VSD3DGetShaderInfo@WarpDebugInternal@@YAJPEAXPEAUVSD3D_SHADER_INFO@@@Z` | `0xDAE0` | 499 | UnwindData |  |
| 26 | `?VSD3DGetShaderDispatchInfo@WarpDebugInternal@@YAJPEAXPEAUVSD3D_SHADER_DISPATCH_INFO@@@Z` | `0xDCE0` | 414 | UnwindData |  |
| 22 | `?VSD3DGetRegisterInfo@WarpDebugInternal@@YAJPEAXPEAUVSD3D_REGISTER_INFO@@I@Z` | `0xDE90` | 1,352 | UnwindData |  |
| 20 | `?VSD3DGetDeviceInfo@WarpDebugInternal@@YAJPEAXPEAUVSD3D_DEVICE_INFO@@@Z` | `0xE3E0` | 505 | UnwindData |  |
| 25 | `?VSD3DGetShaderDebugData@WarpDebugInternal@@YAJPEAXPEAE_KPEA_K@Z` | `0xE5E0` | 235 | UnwindData |  |
| 28 | `?VSD3DGetShaderInstructions@WarpDebugInternal@@YAJPEAXPEAE_KPEA_K@Z` | `0xE830` | 235 | UnwindData |  |
| 36 | `?VSD3DReadShaderBufferMemory@WarpDebugInternal@@YAJPEAXW4VSD3D_REGISTER_SET@@I_KPEAEI@Z` | `0xEA80` | 1,107 | UnwindData |  |
| 44 | `?VSD3DWriteShaderBufferMemory@WarpDebugInternal@@YAJPEAXW4VSD3D_REGISTER_SET@@I_KPEAEI@Z` | `0xEEE0` | 1,163 | UnwindData |  |
| 14 | `?VSD3DGatherShaderBufferMemory@WarpDebugInternal@@YAJPEAXW4VSD3D_REGISTER_SET@@IPEA_KIIPEAEI@Z` | `0xF380` | 62 | UnwindData |  |
| 23 | `?VSD3DGetResourceInformation@WarpDebugInternal@@YAJPEAXW4VSD3D_REGISTER_SET@@IPEAUD3D11_BOX@@PEAW4DXGI_FORMAT@@@Z` | `0xF4D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `?VSD3DSetShaderBreakPoint@WarpDebugInternal@@YAJPEAXUVSD3D_BREAKPOINT_INFO@@PEAPEAX@Z` | `0xF4E0` | 1,061 | UnwindData |  |
| 17 | `?VSD3DGetBreakPointInfo@WarpDebugInternal@@YAJPEAXPEAUVSD3D_BREAKPOINT_INFO@@@Z` | `0xF910` | 751 | UnwindData |  |
| 24 | `?VSD3DGetShaderBreakPoints@WarpDebugInternal@@YAJPEAXPEAPEAXIPEAI@Z` | `0xFC10` | 75 | UnwindData |  |
| 11 | `?VSD3DEnableShaderBreakPoint@WarpDebugInternal@@YAJPEAX_N@Z` | `0xFD10` | 790 | UnwindData |  |
| 9 | `?VSD3DDeleteShaderBreakPoint@WarpDebugInternal@@YAJPEAX@Z` | `0x10030` | 1,396 | UnwindData |  |
| 16 | `?VSD3DGetActiveGroups@WarpDebugInternal@@YAJPEAXHPEAUVSD3D_GROUP_STATISTICS@@PEAUVSD3D_SHADER_DIMENSION@@IPEAI@Z` | `0x105B0` | 519 | UnwindData |  |
| 32 | `?VSD3DGroupGetThreadsInfo@WarpDebugInternal@@YAJPEAXPEAUVSD3D_THREAD_INFO@@IPEAI@Z` | `0x107C0` | 1,141 | UnwindData |  |
| 34 | `?VSD3DOpenActiveGroup@WarpDebugInternal@@YAJPEAXUVSD3D_SHADER_DIMENSION@@PEAPEAX@Z` | `0x10C40` | 171 | UnwindData |  |
| 6 | `?VSD3DCloseActiveGroup@WarpDebugInternal@@YAJPEAX@Z` | `0x10EF0` | 400 | UnwindData |  |
| 41 | `?VSD3DShaderDispatchGetThreadsInfo@WarpDebugInternal@@YAJPEAXPEAUVSD3D_GROUP_THREADS_INFO@@IPEAI@Z` | `0x11090` | 408 | UnwindData |  |
| 37 | `?VSD3DReadThreadRegister@WarpDebugInternal@@YAJPEAXUVSD3D_SHADER_DIMENSION@@W4VSD3D_REGISTER_SET@@I_KPEAEI@Z` | `0x11230` | 278 | UnwindData |  |
| 15 | `?VSD3DGatherThreadRegister@WarpDebugInternal@@YAJPEAXUVSD3D_SHADER_DIMENSION@@W4VSD3D_REGISTER_SET@@IPEA_KIIPEAEI@Z` | `0x11400` | 812 | UnwindData |  |
| 40 | `?VSD3DSetThreadsFrozen@WarpDebugInternal@@YAJPEAXIH@Z` | `0x11740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `?VSD3DWriteThreadRegister@WarpDebugInternal@@YAJPEAXUVSD3D_SHADER_DIMENSION@@W4VSD3D_REGISTER_SET@@I_KPEAEI@Z` | `0x11750` | 1,751 | UnwindData |  |
| 33 | `?VSD3DGroupReadThreadRegister@WarpDebugInternal@@YAJPEAXW4VSD3D_REGISTER_SET@@I_KIPEAEI@Z` | `0x11E30` | 315 | UnwindData |  |
| 35 | `?VSD3DReadGroupSharedRegister@WarpDebugInternal@@YAJPEAXI_KPEAEI@Z` | `0x12130` | 283 | UnwindData |  |
| 13 | `?VSD3DGatherGroupSharedRegister@WarpDebugInternal@@YAJPEAXIPEA_KIIPEAEI@Z` | `0x123D0` | 90 | UnwindData |  |
| 43 | `?VSD3DWriteGroupSharedRegister@WarpDebugInternal@@YAJPEAXI_KPEAEI@Z` | `0x127A0` | 283 | UnwindData |  |
| 38 | `?VSD3DReleaseDebugString@WarpDebugInternal@@YAJPEAG@Z` | `0x12A50` | 138 | UnwindData |  |
| 18 | `?VSD3DGetConfigInfo@WarpDebugInternal@@YAJPEAUVSD3D_CONFIG_INFO@@@Z` | `0x12AE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `?VSD3DConfig@WarpDebugInternal@@YAJPEAXKPEAUVSD3D_MONITORFUNCS@@PEAUVSD3D_CONFIG_INFO2@@@Z` | `0x12B00` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `?VSD3DGetWarningInfo@WarpDebugInternal@@YAJPEAXPEAUVSD3D_WARNING_INFO@@IPEAI@Z` | `0x12B70` | 142 | UnwindData |  |
| 12 | `?VSD3DEnableWarning@WarpDebugInternal@@YAJPEAXW4VSD3DDebugWarningType@@H@Z` | `0x12CE0` | 124 | UnwindData |  |
| 30 | `?VSD3DGetWarningEnabled@WarpDebugInternal@@YAJPEAXW4VSD3DDebugWarningType@@PEAH@Z` | `0x12DB0` | 103 | UnwindData |  |
| 21 | `?VSD3DGetDispatchDictionary@WarpDebugInternal@@YAJPEAXPEAUVSD3D_NAME_VALUE_PAIR@@IPEAI@Z` | `0x12E20` | 59 | UnwindData |  |
| 29 | `?VSD3DGetSupportedDeviceIds@WarpDebugInternal@@YAJPEAU_LUID@@IPEAI@Z` | `0x12E70` | 150 | UnwindData |  |
| 1 | `InitializeDebugging` | `0x13080` | 554 | UnwindData |  |
