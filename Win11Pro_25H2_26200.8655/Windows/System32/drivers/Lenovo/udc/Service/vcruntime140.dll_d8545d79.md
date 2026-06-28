# Binary Specification: vcruntime140.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\drivers\Lenovo\udc\Service\vcruntime140.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d8545d791fc5ba6d1cf6ba398a77792a6044db576c8cfcc0c36ec6f21835f914`
* **Total Exported Functions:** 71

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 22 | `__NLG_Dispatch2` | `0x1180` | 1 | UnwindData |  |
| 23 | `__NLG_Return2` | `0x1190` | 1 | UnwindData |  |
| 41 | `__telemetry_main_invoke_trigger` | `0x2200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `__telemetry_main_return_trigger` | `0x2200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `longjmp` | `0x2210` | 40 | UnwindData |  |
| 54 | `_local_unwind` | `0x2240` | 41 | UnwindData |  |
| 65 | `strchr` | `0x2270` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `strrchr` | `0x22F0` | 315 | UnwindData |  |
| 67 | `strstr` | `0x2430` | 488 | UnwindData |  |
| 69 | `wcschr` | `0x2620` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `wcsrchr` | `0x26A0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `wcsstr` | `0x2750` | 523 | UnwindData |  |
| 19 | `__DestructExceptionObject` | `0x2960` | 109 | UnwindData |  |
| 4 | `_IsExceptionObjectToBeDestroyed` | `0x29E0` | 47 | UnwindData |  |
| 5 | `_SetWinRTOutOfMemoryExceptionCallback` | `0x2A10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `__AdjustPointer` | `0x2A20` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `__FrameUnwindFilter` | `0x2A50` | 101 | UnwindData |  |
| 21 | `__GetPlatformExceptionInfo` | `0x2AC0` | 91 | UnwindData |  |
| 28 | `__current_exception` | `0x2B20` | 18 | UnwindData |  |
| 29 | `__current_exception_context` | `0x2B40` | 18 | UnwindData |  |
| 32 | `__processing_throw` | `0x2B60` | 18 | UnwindData |  |
| 36 | `__std_terminate` | `0x2B80` | 11 | UnwindData |  |
| 53 | `_is_exception_typeof` | `0x2B90` | 166 | UnwindData |  |
| 7 | `__BuildCatchObject` | `0x5BD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `__BuildCatchObjectHelper` | `0x5BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `__TypeMatch` | `0x5BF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `__CxxDetectRethrow` | `0x5C00` | 68 | UnwindData |  |
| 12 | `__CxxExceptionFilter` | `0x5C50` | 489 | UnwindData |  |
| 16 | `__CxxQueryExceptionSize` | `0x5E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `__CxxRegisterExceptionObject` | `0x5E50` | 172 | UnwindData |  |
| 18 | `__CxxUnregisterExceptionObject` | `0x5F00` | 294 | UnwindData |  |
| 24 | `__RTCastToVoid` | `0x65F0` | 93 | UnwindData |  |
| 25 | `__RTDynamicCast` | `0x6650` | 358 | UnwindData |  |
| 26 | `__RTtypeid` | `0x67C0` | 174 | UnwindData |  |
| 34 | `__std_exception_copy` | `0x6870` | 144 | UnwindData |  |
| 35 | `__std_exception_destroy` | `0x6900` | 38 | UnwindData |  |
| 37 | `__std_type_info_compare` | `0x6950` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `__std_type_info_destroy_list` | `0x6980` | 43 | UnwindData |  |
| 39 | `__std_type_info_hash` | `0x69B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `__std_type_info_name` | `0x69F0` | 281 | UnwindData |  |
| 2 | `_CxxThrowException` | `0x6B10` | 167 | UnwindData |  |
| 45 | `__uncaught_exception` | `0x6BC0` | 30 | UnwindData |  |
| 46 | `__uncaught_exceptions` | `0x6BE0` | 27 | UnwindData |  |
| 52 | `_get_unexpected` | `0x6C00` | 34 | UnwindData |  |
| 64 | `set_unexpected` | `0x6C30` | 44 | UnwindData |  |
| 68 | `unexpected` | `0x6C60` | 31 | UnwindData |  |
| 57 | `_set_se_translator` | `0x6C80` | 45 | UnwindData |  |
| 49 | `__vcrt_InitializeCriticalSectionEx` | `0x7260` | 97 | UnwindData |  |
| 47 | `__vcrt_GetModuleFileNameW` | `0x72D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `__vcrt_GetModuleHandleW` | `0x72E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `__vcrt_LoadLibraryExW` | `0x72F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `_get_purecall_handler` | `0x7300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `_purecall` | `0x7310` | 27 | UnwindData |  |
| 56 | `_set_purecall_handler` | `0x7330` | 32,592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `__unDName` | `0xF280` | 39 | UnwindData |  |
| 44 | `__unDNameEx` | `0xF2B0` | 237 | UnwindData |  |
| 10 | `__C_specific_handler_noexcept` | `0xF450` | 76 | UnwindData |  |
| 9 | `__C_specific_handler` | `0xF6A0` | 535 | UnwindData |  |
| 1 | `_CreateFrameInfo` | `0x10340` | 58 | UnwindData |  |
| 3 | `_FindAndUnlinkFrame` | `0x10380` | 82 | UnwindData |  |
| 13 | `__CxxFrameHandler` | `0x10430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `__CxxFrameHandler2` | `0x10430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `__CxxFrameHandler3` | `0x10440` | 134 | UnwindData |  |
| 33 | `__report_gsfailure` | `0x10B10` | 210 | UnwindData |  |
| 30 | `__intrinsic_setjmp` | `0x10DA0` | 144 | UnwindData |  |
| 31 | `__intrinsic_setjmpex` | `0x10E40` | 144 | UnwindData |  |
| 59 | `memchr` | `0x10F20` | 144 | UnwindData |  |
| 60 | `memcmp` | `0x10FC0` | 199 | UnwindData |  |
| 62 | `memmove` | `0x110C0` | 1,645 | UnwindData |  |
| 63 | `memset` | `0x11760` | 904 | UnwindData |  |
| 61 | `memcpy` | `0x12010` | 0 | Indeterminate |  |
