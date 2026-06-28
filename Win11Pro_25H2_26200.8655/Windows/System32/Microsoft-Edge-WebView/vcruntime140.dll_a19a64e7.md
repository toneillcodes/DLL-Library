# Binary Specification: vcruntime140.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Microsoft-Edge-WebView\vcruntime140.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a19a64e758853fd18d4631e68d02fed21269233f5e18c7f183a5a623eec3961f`
* **Total Exported Functions:** 71

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 19 | `__DestructExceptionObject` | `0x1000` | 109 | UnwindData |  |
| 4 | `_IsExceptionObjectToBeDestroyed` | `0x1080` | 47 | UnwindData |  |
| 5 | `_SetWinRTOutOfMemoryExceptionCallback` | `0x10B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `__AdjustPointer` | `0x10C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `__FrameUnwindFilter` | `0x10F0` | 101 | UnwindData |  |
| 21 | `__GetPlatformExceptionInfo` | `0x1160` | 97 | UnwindData |  |
| 28 | `__current_exception` | `0x11D0` | 18 | UnwindData |  |
| 29 | `__current_exception_context` | `0x11F0` | 18 | UnwindData |  |
| 32 | `__processing_throw` | `0x1210` | 18 | UnwindData |  |
| 36 | `__std_terminate` | `0x1230` | 11 | UnwindData |  |
| 53 | `_is_exception_typeof` | `0x1240` | 181 | UnwindData |  |
| 7 | `__BuildCatchObject` | `0x42A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `__BuildCatchObjectHelper` | `0x42B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `__TypeMatch` | `0x42C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `__CxxDetectRethrow` | `0x42D0` | 68 | UnwindData |  |
| 12 | `__CxxExceptionFilter` | `0x4320` | 488 | UnwindData |  |
| 16 | `__CxxQueryExceptionSize` | `0x4510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `__CxxRegisterExceptionObject` | `0x4520` | 181 | UnwindData |  |
| 18 | `__CxxUnregisterExceptionObject` | `0x45E0` | 294 | UnwindData |  |
| 24 | `__RTCastToVoid` | `0x4CD0` | 90 | UnwindData |  |
| 25 | `__RTDynamicCast` | `0x4D30` | 358 | UnwindData |  |
| 26 | `__RTtypeid` | `0x4EA0` | 174 | UnwindData |  |
| 34 | `__std_exception_copy` | `0x4F50` | 137 | UnwindData |  |
| 35 | `__std_exception_destroy` | `0x4FE0` | 41 | UnwindData |  |
| 37 | `__std_type_info_compare` | `0x5030` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `__std_type_info_destroy_list` | `0x5060` | 43 | UnwindData |  |
| 39 | `__std_type_info_hash` | `0x5090` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `__std_type_info_name` | `0x50D0` | 272 | UnwindData |  |
| 2 | `_CxxThrowException` | `0x51E0` | 167 | UnwindData |  |
| 45 | `__uncaught_exception` | `0x5290` | 30 | UnwindData |  |
| 46 | `__uncaught_exceptions` | `0x52B0` | 27 | UnwindData |  |
| 52 | `_get_unexpected` | `0x52D0` | 34 | UnwindData |  |
| 64 | `set_unexpected` | `0x5300` | 44 | UnwindData |  |
| 68 | `unexpected` | `0x5330` | 31 | UnwindData |  |
| 57 | `_set_se_translator` | `0x5350` | 45 | UnwindData |  |
| 49 | `__vcrt_InitializeCriticalSectionEx` | `0x56C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `__vcrt_GetModuleFileNameW` | `0x56D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `__vcrt_GetModuleHandleW` | `0x56E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `__vcrt_LoadLibraryExW` | `0x56F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `_get_purecall_handler` | `0x5700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `_purecall` | `0x5710` | 27 | UnwindData |  |
| 56 | `_set_purecall_handler` | `0x5730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `__telemetry_main_invoke_trigger` | `0x5740` | 37,264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `__telemetry_main_return_trigger` | `0x5740` | 37,264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `__unDName` | `0xE8D0` | 42 | UnwindData |  |
| 44 | `__unDNameEx` | `0xE900` | 219 | UnwindData |  |
| 58 | `longjmp` | `0xEB10` | 40 | UnwindData |  |
| 54 | `_local_unwind` | `0xEB40` | 42 | UnwindData |  |
| 65 | `strchr` | `0xEB70` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `strrchr` | `0xEBF0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `strstr` | `0xED20` | 509 | UnwindData |  |
| 69 | `wcschr` | `0xEF20` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `wcsrchr` | `0xEFA0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `wcsstr` | `0xF050` | 543 | UnwindData |  |
| 10 | `__C_specific_handler_noexcept` | `0xF270` | 76 | UnwindData |  |
| 9 | `__C_specific_handler` | `0xF4C0` | 517 | UnwindData |  |
| 1 | `_CreateFrameInfo` | `0x101A0` | 58 | UnwindData |  |
| 3 | `_FindAndUnlinkFrame` | `0x101E0` | 82 | UnwindData |  |
| 13 | `__CxxFrameHandler` | `0x10290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `__CxxFrameHandler2` | `0x10290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `__CxxFrameHandler3` | `0x102A0` | 134 | UnwindData |  |
| 22 | `__NLG_Dispatch2` | `0x10620` | 1 | UnwindData |  |
| 23 | `__NLG_Return2` | `0x10630` | 1 | UnwindData |  |
| 33 | `__report_gsfailure` | `0x11BB0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `__intrinsic_setjmp` | `0x11D10` | 144 | UnwindData |  |
| 31 | `__intrinsic_setjmpex` | `0x11DB0` | 144 | UnwindData |  |
| 59 | `memchr` | `0x11E90` | 144 | UnwindData |  |
| 60 | `memcmp` | `0x11F30` | 199 | UnwindData |  |
| 62 | `memmove` | `0x12030` | 1,661 | UnwindData |  |
| 63 | `memset` | `0x126E0` | 904 | UnwindData |  |
| 61 | `memcpy` | `0x13010` | 0 | Indeterminate |  |
