# Binary Specification: vcruntime140.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\lenovofnandfunctionkeys.inf_amd64_5e21bf389d23855a\vcruntime140.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `56444ea6c3f7593de179a274fa9c359d1c84e00b476e5440211cf6cf5e2f4c4f`
* **Total Exported Functions:** 71

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 59 | `memchr` | `0x10C0` | 110 | UnwindData |  |
| 60 | `memcmp` | `0x1140` | 199 | UnwindData |  |
| 61 | `memcpy` | `0x1240` | 1,061 | UnwindData |  |
| 62 | `memmove` | `0x1240` | 1,061 | UnwindData |  |
| 63 | `memset` | `0x16A0` | 400 | UnwindData |  |
| 22 | `__NLG_Dispatch2` | `0x1860` | 1 | UnwindData |  |
| 23 | `__NLG_Return2` | `0x1870` | 1 | UnwindData |  |
| 41 | `__telemetry_main_invoke_trigger` | `0x1880` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `__telemetry_main_return_trigger` | `0x1880` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `longjmp` | `0x1900` | 40 | UnwindData |  |
| 65 | `strchr` | `0x1930` | 137 | UnwindData |  |
| 66 | `strrchr` | `0x19C0` | 329 | UnwindData |  |
| 67 | `strstr` | `0x1B10` | 512 | UnwindData |  |
| 69 | `wcschr` | `0x1D10` | 145 | UnwindData |  |
| 70 | `wcsrchr` | `0x1DB0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `wcsstr` | `0x1E70` | 540 | UnwindData |  |
| 54 | `_local_unwind` | `0x2090` | 41 | UnwindData |  |
| 19 | `__DestructExceptionObject` | `0x20C0` | 114 | UnwindData |  |
| 4 | `_IsExceptionObjectToBeDestroyed` | `0x2140` | 47 | UnwindData |  |
| 5 | `_SetWinRTOutOfMemoryExceptionCallback` | `0x2170` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `__AdjustPointer` | `0x2180` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `__FrameUnwindFilter` | `0x21B0` | 73 | UnwindData |  |
| 21 | `__GetPlatformExceptionInfo` | `0x2200` | 91 | UnwindData |  |
| 28 | `__current_exception` | `0x2260` | 18 | UnwindData |  |
| 29 | `__current_exception_context` | `0x2280` | 18 | UnwindData |  |
| 32 | `__processing_throw` | `0x22A0` | 18 | UnwindData |  |
| 36 | `__std_terminate` | `0x22C0` | 11 | UnwindData |  |
| 53 | `_is_exception_typeof` | `0x22D0` | 166 | UnwindData |  |
| 7 | `__BuildCatchObject` | `0x3850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `__BuildCatchObjectHelper` | `0x3860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `__TypeMatch` | `0x3870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `__CxxDetectRethrow` | `0x3880` | 68 | UnwindData |  |
| 12 | `__CxxExceptionFilter` | `0x38D0` | 476 | UnwindData |  |
| 16 | `__CxxQueryExceptionSize` | `0x3AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `__CxxRegisterExceptionObject` | `0x3AC0` | 172 | UnwindData |  |
| 18 | `__CxxUnregisterExceptionObject` | `0x3B70` | 294 | UnwindData |  |
| 24 | `__RTCastToVoid` | `0x4290` | 93 | UnwindData |  |
| 25 | `__RTDynamicCast` | `0x42F0` | 358 | UnwindData |  |
| 26 | `__RTtypeid` | `0x4460` | 174 | UnwindData |  |
| 34 | `__std_exception_copy` | `0x4510` | 144 | UnwindData |  |
| 35 | `__std_exception_destroy` | `0x45A0` | 38 | UnwindData |  |
| 37 | `__std_type_info_compare` | `0x45F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `__std_type_info_destroy_list` | `0x4620` | 43 | UnwindData |  |
| 39 | `__std_type_info_hash` | `0x4650` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `__std_type_info_name` | `0x4690` | 288 | UnwindData |  |
| 2 | `_CxxThrowException` | `0x47B0` | 191 | UnwindData |  |
| 45 | `__uncaught_exception` | `0x4870` | 30 | UnwindData |  |
| 46 | `__uncaught_exceptions` | `0x4890` | 27 | UnwindData |  |
| 52 | `_get_unexpected` | `0x48B0` | 34 | UnwindData |  |
| 64 | `set_unexpected` | `0x48E0` | 44 | UnwindData |  |
| 68 | `unexpected` | `0x4910` | 31 | UnwindData |  |
| 57 | `_set_se_translator` | `0x4930` | 45 | UnwindData |  |
| 49 | `__vcrt_InitializeCriticalSectionEx` | `0x4FD0` | 97 | UnwindData |  |
| 47 | `__vcrt_GetModuleFileNameW` | `0x50B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `__vcrt_GetModuleHandleW` | `0x50C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `__vcrt_LoadLibraryExW` | `0x50D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `_get_purecall_handler` | `0x50E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `_purecall` | `0x5100` | 47 | UnwindData |  |
| 56 | `_set_purecall_handler` | `0x5130` | 25,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `__unDName` | `0xB690` | 39 | UnwindData |  |
| 44 | `__unDNameEx` | `0xB6C0` | 306 | UnwindData |  |
| 9 | `__C_specific_handler` | `0xB850` | 523 | UnwindData |  |
| 1 | `_CreateFrameInfo` | `0xBFF0` | 58 | UnwindData |  |
| 3 | `_FindAndUnlinkFrame` | `0xC030` | 82 | UnwindData |  |
| 13 | `__CxxFrameHandler` | `0xC0E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `__CxxFrameHandler2` | `0xC0E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `__CxxFrameHandler3` | `0xC0F0` | 125 | UnwindData |  |
| 10 | `__C_specific_handler_noexcept` | `0xC170` | 46 | UnwindData |  |
| 33 | `__report_gsfailure` | `0xC700` | 209 | UnwindData |  |
| 30 | `__intrinsic_setjmp` | `0xC980` | 144 | UnwindData |  |
| 31 | `__intrinsic_setjmpex` | `0xCA40` | 144 | UnwindData |  |
