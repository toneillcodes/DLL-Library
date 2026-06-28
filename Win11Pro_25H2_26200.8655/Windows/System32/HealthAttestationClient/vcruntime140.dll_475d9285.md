# Binary Specification: vcruntime140.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\HealthAttestationClient\vcruntime140.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `475d9285d7a98ce3767e08b2e83fdbb2e66ea92993d3d274827435f668308045`
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
| 53 | `_is_exception_typeof` | `0x1240` | 177 | UnwindData |  |
| 7 | `__BuildCatchObject` | `0x42E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `__BuildCatchObjectHelper` | `0x42F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `__TypeMatch` | `0x4300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `__CxxDetectRethrow` | `0x4310` | 77 | UnwindData |  |
| 12 | `__CxxExceptionFilter` | `0x4360` | 502 | UnwindData |  |
| 16 | `__CxxQueryExceptionSize` | `0x4560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `__CxxRegisterExceptionObject` | `0x4570` | 188 | UnwindData |  |
| 18 | `__CxxUnregisterExceptionObject` | `0x4630` | 294 | UnwindData |  |
| 24 | `__RTCastToVoid` | `0x4D40` | 90 | UnwindData |  |
| 25 | `__RTDynamicCast` | `0x4DA0` | 358 | UnwindData |  |
| 26 | `__RTtypeid` | `0x4F10` | 174 | UnwindData |  |
| 34 | `__std_exception_copy` | `0x4FC0` | 137 | UnwindData |  |
| 35 | `__std_exception_destroy` | `0x5050` | 41 | UnwindData |  |
| 37 | `__std_type_info_compare` | `0x50A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `__std_type_info_destroy_list` | `0x50D0` | 43 | UnwindData |  |
| 39 | `__std_type_info_hash` | `0x5100` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `__std_type_info_name` | `0x5140` | 275 | UnwindData |  |
| 2 | `_CxxThrowException` | `0x5260` | 167 | UnwindData |  |
| 45 | `__uncaught_exception` | `0x5310` | 30 | UnwindData |  |
| 46 | `__uncaught_exceptions` | `0x5330` | 27 | UnwindData |  |
| 52 | `_get_unexpected` | `0x5350` | 34 | UnwindData |  |
| 64 | `set_unexpected` | `0x5380` | 44 | UnwindData |  |
| 68 | `unexpected` | `0x53B0` | 31 | UnwindData |  |
| 57 | `_set_se_translator` | `0x53D0` | 45 | UnwindData |  |
| 49 | `__vcrt_InitializeCriticalSectionEx` | `0x59D0` | 97 | UnwindData |  |
| 47 | `__vcrt_GetModuleFileNameW` | `0x5A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `__vcrt_GetModuleHandleW` | `0x5A50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `__vcrt_LoadLibraryExW` | `0x5A60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `_get_purecall_handler` | `0x5A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `_purecall` | `0x5A80` | 27 | UnwindData |  |
| 56 | `_set_purecall_handler` | `0x5AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `__telemetry_main_invoke_trigger` | `0x5AB0` | 36,352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `__telemetry_main_return_trigger` | `0x5AB0` | 36,352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `__unDName` | `0xE8B0` | 42 | UnwindData |  |
| 44 | `__unDNameEx` | `0xE8E0` | 219 | UnwindData |  |
| 58 | `longjmp` | `0xEAF0` | 40 | UnwindData |  |
| 54 | `_local_unwind` | `0xEB20` | 42 | UnwindData |  |
| 65 | `strchr` | `0xEB50` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `strrchr` | `0xEBD0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `strstr` | `0xED00` | 499 | UnwindData |  |
| 69 | `wcschr` | `0xEF00` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `wcsrchr` | `0xEF80` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `wcsstr` | `0xF030` | 532 | UnwindData |  |
| 10 | `__C_specific_handler_noexcept` | `0xF250` | 76 | UnwindData |  |
| 9 | `__C_specific_handler` | `0xF4A0` | 535 | UnwindData |  |
| 1 | `_CreateFrameInfo` | `0x10190` | 58 | UnwindData |  |
| 3 | `_FindAndUnlinkFrame` | `0x101D0` | 82 | UnwindData |  |
| 13 | `__CxxFrameHandler` | `0x10280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `__CxxFrameHandler2` | `0x10280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `__CxxFrameHandler3` | `0x10290` | 134 | UnwindData |  |
| 22 | `__NLG_Dispatch2` | `0x10610` | 1 | UnwindData |  |
| 23 | `__NLG_Return2` | `0x10620` | 1 | UnwindData |  |
| 33 | `__report_gsfailure` | `0x11BD0` | 211 | UnwindData |  |
| 30 | `__intrinsic_setjmp` | `0x11E60` | 144 | UnwindData |  |
| 31 | `__intrinsic_setjmpex` | `0x11F00` | 144 | UnwindData |  |
| 59 | `memchr` | `0x11FE0` | 144 | UnwindData |  |
| 60 | `memcmp` | `0x12080` | 199 | UnwindData |  |
| 62 | `memmove` | `0x12180` | 1,645 | UnwindData |  |
| 63 | `memset` | `0x12820` | 904 | UnwindData |  |
| 61 | `memcpy` | `0x14010` | 0 | Indeterminate |  |
