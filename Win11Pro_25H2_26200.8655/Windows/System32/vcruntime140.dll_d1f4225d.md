# Binary Specification: vcruntime140.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\vcruntime140.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d1f4225df2cd877dbf130d5668a021dce3f94118455ff5ec952061c30afc9ce7`
* **Total Exported Functions:** 71

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 19 | `__DestructExceptionObject` | `0x1000` | 109 | UnwindData |  |
| 4 | `_IsExceptionObjectToBeDestroyed` | `0x1080` | 56 | UnwindData |  |
| 5 | `_SetWinRTOutOfMemoryExceptionCallback` | `0x10C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `__AdjustPointer` | `0x10D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `__FrameUnwindFilter` | `0x1100` | 100 | UnwindData |  |
| 21 | `__GetPlatformExceptionInfo` | `0x1170` | 101 | UnwindData |  |
| 28 | `__current_exception` | `0x11E0` | 18 | UnwindData |  |
| 29 | `__current_exception_context` | `0x1200` | 18 | UnwindData |  |
| 32 | `__processing_throw` | `0x1220` | 18 | UnwindData |  |
| 36 | `__std_terminate` | `0x1240` | 11 | UnwindData |  |
| 53 | `_is_exception_typeof` | `0x1250` | 75 | UnwindData |  |
| 7 | `__BuildCatchObject` | `0x4520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `__BuildCatchObjectHelper` | `0x4530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `__TypeMatch` | `0x4540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `__CxxDetectRethrow` | `0x4550` | 71 | UnwindData |  |
| 12 | `__CxxExceptionFilter` | `0x45A0` | 523 | UnwindData |  |
| 16 | `__CxxQueryExceptionSize` | `0x47B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `__CxxRegisterExceptionObject` | `0x47C0` | 4 | UnwindData |  |
| 18 | `__CxxUnregisterExceptionObject` | `0x4880` | 294 | UnwindData |  |
| 24 | `__RTCastToVoid` | `0x4FC0` | 96 | UnwindData |  |
| 25 | `__RTDynamicCast` | `0x5020` | 343 | UnwindData |  |
| 26 | `__RTtypeid` | `0x5180` | 174 | UnwindData |  |
| 34 | `__std_exception_copy` | `0x5230` | 30 | UnwindData |  |
| 35 | `__std_exception_destroy` | `0x52D0` | 58 | UnwindData |  |
| 37 | `__std_type_info_compare` | `0x5330` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `__std_type_info_destroy_list` | `0x5360` | 15 | UnwindData |  |
| 39 | `__std_type_info_hash` | `0x53A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `__std_type_info_name` | `0x53E0` | 31 | UnwindData |  |
| 2 | `_CxxThrowException` | `0x5510` | 169 | UnwindData |  |
| 45 | `__uncaught_exception` | `0x55C0` | 35 | UnwindData |  |
| 46 | `__uncaught_exceptions` | `0x55F0` | 27 | UnwindData |  |
| 52 | `_get_unexpected` | `0x5610` | 32 | UnwindData |  |
| 64 | `set_unexpected` | `0x5630` | 45 | UnwindData |  |
| 68 | `unexpected` | `0x5660` | 31 | UnwindData |  |
| 57 | `_set_se_translator` | `0x5680` | 45 | UnwindData |  |
| 49 | `__vcrt_InitializeCriticalSectionEx` | `0x5B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `__vcrt_GetModuleFileNameW` | `0x5BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `__vcrt_GetModuleHandleW` | `0x5BB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `__vcrt_LoadLibraryExW` | `0x5BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `_get_purecall_handler` | `0x5BD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `_purecall` | `0x5BE0` | 27 | UnwindData |  |
| 56 | `_set_purecall_handler` | `0x5C00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `__telemetry_main_invoke_trigger` | `0x5C10` | 81,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `__telemetry_main_return_trigger` | `0x5C10` | 81,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `__unDName` | `0x19920` | 42 | UnwindData |  |
| 44 | `__unDNameEx` | `0x19950` | 166 | UnwindData |  |
| 58 | `longjmp` | `0x19B50` | 40 | UnwindData |  |
| 54 | `_local_unwind` | `0x19B80` | 42 | UnwindData |  |
| 65 | `strchr` | `0x19BB0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `strrchr` | `0x19C40` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `strstr` | `0x19D80` | 314 | UnwindData |  |
| 69 | `wcschr` | `0x1A050` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `wcsrchr` | `0x1A0E0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `wcsstr` | `0x1A1C0` | 805 | UnwindData |  |
| 10 | `__C_specific_handler_noexcept` | `0x1A4F0` | 76 | UnwindData |  |
| 9 | `__C_specific_handler` | `0x1A920` | 538 | UnwindData |  |
| 1 | `_CreateFrameInfo` | `0x1B760` | 58 | UnwindData |  |
| 3 | `_FindAndUnlinkFrame` | `0x1B7A0` | 82 | UnwindData |  |
| 13 | `__CxxFrameHandler` | `0x1B880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `__CxxFrameHandler2` | `0x1B880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `__CxxFrameHandler3` | `0x1B890` | 113 | UnwindData |  |
| 22 | `__NLG_Dispatch2` | `0x1BC20` | 1 | UnwindData |  |
| 23 | `__NLG_Return2` | `0x1BC30` | 1 | UnwindData |  |
| 33 | `__report_gsfailure` | `0x1CFA0` | 2,112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `__intrinsic_setjmp` | `0x1D7E0` | 144 | UnwindData |  |
| 31 | `__intrinsic_setjmpex` | `0x1D880` | 144 | UnwindData |  |
| 59 | `memchr` | `0x1D960` | 144 | UnwindData |  |
| 62 | `memmove` | `0x1DB00` | 1,661 | UnwindData |  |
| 60 | `memcmp` | `0x1F010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `memcpy` | `0x1F020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `memset` | `0x1F030` | 0 | Indeterminate |  |
