# Binary Specification: vcruntime140_clr0400.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\vcruntime140_clr0400.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7fc846abd97d7112d6cd1973d5c9f250331a1413a57a1e1456ae55308ca843c0`
* **Total Exported Functions:** 71

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 22 | `__NLG_Dispatch2` | `0x1140` | 1 | UnwindData |  |
| 23 | `__NLG_Return2` | `0x1150` | 1 | UnwindData |  |
| 59 | `memchr` | `0x1170` | 110 | UnwindData |  |
| 60 | `memcmp` | `0x11F0` | 199 | UnwindData |  |
| 61 | `memcpy` | `0x12F0` | 1,653 | UnwindData |  |
| 62 | `memmove` | `0x12F0` | 1,653 | UnwindData |  |
| 63 | `memset` | `0x19A0` | 904 | UnwindData |  |
| 41 | `__telemetry_main_invoke_trigger` | `0x1D30` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `__telemetry_main_return_trigger` | `0x1D30` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `longjmp` | `0x1DB0` | 40 | UnwindData |  |
| 54 | `_local_unwind` | `0x1DE0` | 41 | UnwindData |  |
| 65 | `strchr` | `0x1E10` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `strrchr` | `0x1E90` | 315 | UnwindData |  |
| 67 | `strstr` | `0x1FD0` | 502 | UnwindData |  |
| 69 | `wcschr` | `0x21D0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `wcsrchr` | `0x2250` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `wcsstr` | `0x2300` | 530 | UnwindData |  |
| 19 | `__DestructExceptionObject` | `0x2520` | 109 | UnwindData |  |
| 4 | `_IsExceptionObjectToBeDestroyed` | `0x25A0` | 47 | UnwindData |  |
| 5 | `_SetWinRTOutOfMemoryExceptionCallback` | `0x25D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `__AdjustPointer` | `0x25E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `__FrameUnwindFilter` | `0x2610` | 101 | UnwindData |  |
| 21 | `__GetPlatformExceptionInfo` | `0x2680` | 91 | UnwindData |  |
| 28 | `__current_exception` | `0x26E0` | 18 | UnwindData |  |
| 29 | `__current_exception_context` | `0x2700` | 18 | UnwindData |  |
| 32 | `__processing_throw` | `0x2720` | 18 | UnwindData |  |
| 36 | `__std_terminate` | `0x2740` | 11 | UnwindData |  |
| 53 | `_is_exception_typeof` | `0x2750` | 166 | UnwindData |  |
| 7 | `__BuildCatchObject` | `0x56E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `__BuildCatchObjectHelper` | `0x56F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `__TypeMatch` | `0x5700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `__CxxDetectRethrow` | `0x5710` | 68 | UnwindData |  |
| 12 | `__CxxExceptionFilter` | `0x5760` | 493 | UnwindData |  |
| 16 | `__CxxQueryExceptionSize` | `0x5950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `__CxxRegisterExceptionObject` | `0x5960` | 172 | UnwindData |  |
| 18 | `__CxxUnregisterExceptionObject` | `0x5A10` | 294 | UnwindData |  |
| 24 | `__RTCastToVoid` | `0x6110` | 93 | UnwindData |  |
| 25 | `__RTDynamicCast` | `0x6170` | 358 | UnwindData |  |
| 26 | `__RTtypeid` | `0x62E0` | 174 | UnwindData |  |
| 34 | `__std_exception_copy` | `0x6390` | 144 | UnwindData |  |
| 35 | `__std_exception_destroy` | `0x6420` | 38 | UnwindData |  |
| 37 | `__std_type_info_compare` | `0x6470` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `__std_type_info_destroy_list` | `0x64A0` | 43 | UnwindData |  |
| 39 | `__std_type_info_hash` | `0x64D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `__std_type_info_name` | `0x6510` | 284 | UnwindData |  |
| 2 | `_CxxThrowException` | `0x6630` | 160 | UnwindData |  |
| 45 | `__uncaught_exception` | `0x66D0` | 30 | UnwindData |  |
| 46 | `__uncaught_exceptions` | `0x66F0` | 27 | UnwindData |  |
| 52 | `_get_unexpected` | `0x6710` | 34 | UnwindData |  |
| 64 | `set_unexpected` | `0x6740` | 44 | UnwindData |  |
| 68 | `unexpected` | `0x6770` | 31 | UnwindData |  |
| 57 | `_set_se_translator` | `0x6790` | 45 | UnwindData |  |
| 49 | `__vcrt_InitializeCriticalSectionEx` | `0x6D80` | 97 | UnwindData |  |
| 47 | `__vcrt_GetModuleFileNameW` | `0x6DF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `__vcrt_GetModuleHandleW` | `0x6E00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `__vcrt_LoadLibraryExW` | `0x6E10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `_get_purecall_handler` | `0x6E20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `_purecall` | `0x6E30` | 27 | UnwindData |  |
| 56 | `_set_purecall_handler` | `0x6E50` | 31,904 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `__unDName` | `0xEAF0` | 39 | UnwindData |  |
| 44 | `__unDNameEx` | `0xEB20` | 306 | UnwindData |  |
| 10 | `__C_specific_handler_noexcept` | `0xED00` | 76 | UnwindData |  |
| 9 | `__C_specific_handler` | `0xEF50` | 503 | UnwindData |  |
| 1 | `_CreateFrameInfo` | `0xFBD0` | 58 | UnwindData |  |
| 3 | `_FindAndUnlinkFrame` | `0xFC10` | 82 | UnwindData |  |
| 13 | `__CxxFrameHandler` | `0xFCC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `__CxxFrameHandler2` | `0xFCC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `__CxxFrameHandler3` | `0xFCD0` | 134 | UnwindData |  |
| 33 | `__report_gsfailure` | `0x103A0` | 210 | UnwindData |  |
| 30 | `__intrinsic_setjmp` | `0x10620` | 144 | UnwindData |  |
| 31 | `__intrinsic_setjmpex` | `0x106E0` | 144 | UnwindData |  |
