# Binary Specification: vcruntime140.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iclsclient.inf_amd64_64ca6dfb781d0707\lib\vcruntime140.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f9e78ee91f0216eb67c788f63223af14467e19f4e532d540d881eb89d53401d1`
* **Total Exported Functions:** 71

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 22 | `__NLG_Dispatch2` | `0x1140` | 1 | UnwindData |  |
| 23 | `__NLG_Return2` | `0x1150` | 1 | UnwindData |  |
| 59 | `memchr` | `0x1170` | 110 | UnwindData |  |
| 60 | `memcmp` | `0x11F0` | 199 | UnwindData |  |
| 61 | `memcpy` | `0x12F0` | 981 | UnwindData |  |
| 62 | `memmove` | `0x12F0` | 981 | UnwindData |  |
| 63 | `memset` | `0x1700` | 400 | UnwindData |  |
| 41 | `__telemetry_main_invoke_trigger` | `0x1890` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `__telemetry_main_return_trigger` | `0x1890` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `longjmp` | `0x1910` | 40 | UnwindData |  |
| 54 | `_local_unwind` | `0x1940` | 41 | UnwindData |  |
| 65 | `strchr` | `0x1970` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `strrchr` | `0x19F0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `strstr` | `0x1B20` | 506 | UnwindData |  |
| 69 | `wcschr` | `0x1D20` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `wcsrchr` | `0x1DA0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `wcsstr` | `0x1E50` | 534 | UnwindData |  |
| 19 | `__DestructExceptionObject` | `0x2070` | 109 | UnwindData |  |
| 4 | `_IsExceptionObjectToBeDestroyed` | `0x20F0` | 47 | UnwindData |  |
| 5 | `_SetWinRTOutOfMemoryExceptionCallback` | `0x2120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `__AdjustPointer` | `0x2130` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `__FrameUnwindFilter` | `0x2160` | 101 | UnwindData |  |
| 21 | `__GetPlatformExceptionInfo` | `0x21D0` | 91 | UnwindData |  |
| 28 | `__current_exception` | `0x2230` | 18 | UnwindData |  |
| 29 | `__current_exception_context` | `0x2250` | 18 | UnwindData |  |
| 32 | `__processing_throw` | `0x2270` | 18 | UnwindData |  |
| 36 | `__std_terminate` | `0x2290` | 11 | UnwindData |  |
| 53 | `_is_exception_typeof` | `0x22A0` | 166 | UnwindData |  |
| 7 | `__BuildCatchObject` | `0x5240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `__BuildCatchObjectHelper` | `0x5250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `__TypeMatch` | `0x5260` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `__CxxDetectRethrow` | `0x5270` | 68 | UnwindData |  |
| 12 | `__CxxExceptionFilter` | `0x52C0` | 493 | UnwindData |  |
| 16 | `__CxxQueryExceptionSize` | `0x54B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `__CxxRegisterExceptionObject` | `0x54C0` | 172 | UnwindData |  |
| 18 | `__CxxUnregisterExceptionObject` | `0x5570` | 294 | UnwindData |  |
| 24 | `__RTCastToVoid` | `0x5C70` | 93 | UnwindData |  |
| 25 | `__RTDynamicCast` | `0x5CD0` | 358 | UnwindData |  |
| 26 | `__RTtypeid` | `0x5E40` | 174 | UnwindData |  |
| 34 | `__std_exception_copy` | `0x5EF0` | 144 | UnwindData |  |
| 35 | `__std_exception_destroy` | `0x5F80` | 38 | UnwindData |  |
| 37 | `__std_type_info_compare` | `0x5FD0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `__std_type_info_destroy_list` | `0x6000` | 43 | UnwindData |  |
| 39 | `__std_type_info_hash` | `0x6030` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `__std_type_info_name` | `0x6070` | 283 | UnwindData |  |
| 2 | `_CxxThrowException` | `0x6190` | 160 | UnwindData |  |
| 45 | `__uncaught_exception` | `0x6230` | 30 | UnwindData |  |
| 46 | `__uncaught_exceptions` | `0x6250` | 27 | UnwindData |  |
| 52 | `_get_unexpected` | `0x6270` | 34 | UnwindData |  |
| 64 | `set_unexpected` | `0x62A0` | 44 | UnwindData |  |
| 68 | `unexpected` | `0x62D0` | 31 | UnwindData |  |
| 57 | `_set_se_translator` | `0x62F0` | 45 | UnwindData |  |
| 49 | `__vcrt_InitializeCriticalSectionEx` | `0x68D0` | 97 | UnwindData |  |
| 47 | `__vcrt_GetModuleFileNameW` | `0x6940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `__vcrt_GetModuleHandleW` | `0x6950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `__vcrt_LoadLibraryExW` | `0x6960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `_get_purecall_handler` | `0x6970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `_purecall` | `0x6980` | 27 | UnwindData |  |
| 56 | `_set_purecall_handler` | `0x69A0` | 30,096 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `__unDName` | `0xDF30` | 39 | UnwindData |  |
| 44 | `__unDNameEx` | `0xDF60` | 306 | UnwindData |  |
| 10 | `__C_specific_handler_noexcept` | `0xE0F0` | 76 | UnwindData |  |
| 9 | `__C_specific_handler` | `0xE340` | 523 | UnwindData |  |
| 1 | `_CreateFrameInfo` | `0xEFC0` | 58 | UnwindData |  |
| 3 | `_FindAndUnlinkFrame` | `0xF000` | 82 | UnwindData |  |
| 13 | `__CxxFrameHandler` | `0xF0B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `__CxxFrameHandler2` | `0xF0B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `__CxxFrameHandler3` | `0xF0C0` | 134 | UnwindData |  |
| 33 | `__report_gsfailure` | `0xF7A0` | 209 | UnwindData |  |
| 30 | `__intrinsic_setjmp` | `0xFA20` | 144 | UnwindData |  |
| 31 | `__intrinsic_setjmpex` | `0xFAE0` | 144 | UnwindData |  |
