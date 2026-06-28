# Binary Specification: vcruntime140.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\vcruntime140.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d5e4d9a3e835fa679450145d6a7d94e36573a509317111904d9b3712c30d9066`
* **Total Exported Functions:** 71

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 19 | `__DestructExceptionObject` | `0x1000` | 116 | UnwindData |  |
| 4 | `_IsExceptionObjectToBeDestroyed` | `0x1080` | 47 | UnwindData |  |
| 5 | `_SetWinRTOutOfMemoryExceptionCallback` | `0x10B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `__AdjustPointer` | `0x10C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `__FrameUnwindFilter` | `0x10F0` | 101 | UnwindData |  |
| 21 | `__GetPlatformExceptionInfo` | `0x1160` | 97 | UnwindData |  |
| 28 | `__current_exception` | `0x11D0` | 18 | UnwindData |  |
| 29 | `__current_exception_context` | `0x11F0` | 18 | UnwindData |  |
| 32 | `__processing_throw` | `0x1210` | 18 | UnwindData |  |
| 36 | `__std_terminate` | `0x1230` | 11 | UnwindData |  |
| 53 | `_is_exception_typeof` | `0x1240` | 182 | UnwindData |  |
| 7 | `__BuildCatchObject` | `0x42C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `__BuildCatchObjectHelper` | `0x42D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `__TypeMatch` | `0x42E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `__CxxDetectRethrow` | `0x42F0` | 77 | UnwindData |  |
| 12 | `__CxxExceptionFilter` | `0x4340` | 502 | UnwindData |  |
| 16 | `__CxxQueryExceptionSize` | `0x4540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `__CxxRegisterExceptionObject` | `0x4550` | 188 | UnwindData |  |
| 18 | `__CxxUnregisterExceptionObject` | `0x4610` | 294 | UnwindData |  |
| 24 | `__RTCastToVoid` | `0x4D30` | 90 | UnwindData |  |
| 25 | `__RTDynamicCast` | `0x4D90` | 357 | UnwindData |  |
| 26 | `__RTtypeid` | `0x4F00` | 174 | UnwindData |  |
| 34 | `__std_exception_copy` | `0x4FB0` | 129 | UnwindData |  |
| 35 | `__std_exception_destroy` | `0x5040` | 41 | UnwindData |  |
| 37 | `__std_type_info_compare` | `0x5090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `__std_type_info_destroy_list` | `0x50B0` | 43 | UnwindData |  |
| 39 | `__std_type_info_hash` | `0x50E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `__std_type_info_name` | `0x5120` | 270 | UnwindData |  |
| 2 | `_CxxThrowException` | `0x5230` | 167 | UnwindData |  |
| 45 | `__uncaught_exception` | `0x52E0` | 30 | UnwindData |  |
| 46 | `__uncaught_exceptions` | `0x5300` | 27 | UnwindData |  |
| 52 | `_get_unexpected` | `0x5320` | 34 | UnwindData |  |
| 64 | `set_unexpected` | `0x5350` | 44 | UnwindData |  |
| 68 | `unexpected` | `0x5380` | 31 | UnwindData |  |
| 57 | `_set_se_translator` | `0x53A0` | 45 | UnwindData |  |
| 49 | `__vcrt_InitializeCriticalSectionEx` | `0x5990` | 97 | UnwindData |  |
| 47 | `__vcrt_GetModuleFileNameW` | `0x5A00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `__vcrt_GetModuleHandleW` | `0x5A10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `__vcrt_LoadLibraryExW` | `0x5A20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `_get_purecall_handler` | `0x5A30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `_purecall` | `0x5A40` | 27 | UnwindData |  |
| 56 | `_set_purecall_handler` | `0x5A60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `__telemetry_main_invoke_trigger` | `0x5A70` | 36,224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `__telemetry_main_return_trigger` | `0x5A70` | 36,224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `__unDName` | `0xE7F0` | 42 | UnwindData |  |
| 44 | `__unDNameEx` | `0xE820` | 219 | UnwindData |  |
| 58 | `longjmp` | `0xEA30` | 40 | UnwindData |  |
| 54 | `_local_unwind` | `0xEA60` | 42 | UnwindData |  |
| 65 | `strchr` | `0xEA90` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `strrchr` | `0xEB10` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `strstr` | `0xEC40` | 499 | UnwindData |  |
| 69 | `wcschr` | `0xEE40` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `wcsrchr` | `0xEEC0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `wcsstr` | `0xEF70` | 532 | UnwindData |  |
| 10 | `__C_specific_handler_noexcept` | `0xF190` | 76 | UnwindData |  |
| 9 | `__C_specific_handler` | `0xF3E0` | 535 | UnwindData |  |
| 1 | `_CreateFrameInfo` | `0x100D0` | 58 | UnwindData |  |
| 3 | `_FindAndUnlinkFrame` | `0x10110` | 82 | UnwindData |  |
| 13 | `__CxxFrameHandler` | `0x101C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `__CxxFrameHandler2` | `0x101C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `__CxxFrameHandler3` | `0x101D0` | 134 | UnwindData |  |
| 22 | `__NLG_Dispatch2` | `0x10550` | 1 | UnwindData |  |
| 23 | `__NLG_Return2` | `0x10560` | 1 | UnwindData |  |
| 33 | `__report_gsfailure` | `0x11B10` | 211 | UnwindData |  |
| 30 | `__intrinsic_setjmp` | `0x11DB0` | 144 | UnwindData |  |
| 31 | `__intrinsic_setjmpex` | `0x11E50` | 144 | UnwindData |  |
| 59 | `memchr` | `0x11F30` | 144 | UnwindData |  |
| 60 | `memcmp` | `0x11FD0` | 199 | UnwindData |  |
| 62 | `memmove` | `0x120D0` | 1,645 | UnwindData |  |
| 63 | `memset` | `0x12770` | 904 | UnwindData |  |
| 61 | `memcpy` | `0x13010` | 0 | Indeterminate |  |
