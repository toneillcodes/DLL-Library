# Binary Specification: vcruntime140d.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\vcruntime140d.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `098a800e8d227b2c683274789b93671a668d76fe0bb7817e4921ee473db4c17e`
* **Total Exported Functions:** 71

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 19 | `__DestructExceptionObject` | `0x1000` | 249 | UnwindData |  |
| 4 | `_IsExceptionObjectToBeDestroyed` | `0x1200` | 78 | UnwindData |  |
| 5 | `_SetWinRTOutOfMemoryExceptionCallback` | `0x1250` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `__AdjustPointer` | `0x1270` | 125 | UnwindData |  |
| 20 | `__FrameUnwindFilter` | `0x12F0` | 166 | UnwindData |  |
| 21 | `__GetPlatformExceptionInfo` | `0x13A0` | 171 | UnwindData |  |
| 28 | `__current_exception` | `0x1450` | 18 | UnwindData |  |
| 29 | `__current_exception_context` | `0x1470` | 18 | UnwindData |  |
| 32 | `__processing_throw` | `0x1490` | 18 | UnwindData |  |
| 36 | `__std_terminate` | `0x14B0` | 16 | UnwindData |  |
| 53 | `_is_exception_typeof` | `0x14C0` | 325 | UnwindData |  |
| 7 | `__BuildCatchObject` | `0x6F80` | 55 | UnwindData |  |
| 8 | `__BuildCatchObjectHelper` | `0x6FC0` | 54 | UnwindData |  |
| 27 | `__TypeMatch` | `0x7000` | 44 | UnwindData |  |
| 11 | `__CxxDetectRethrow` | `0x7050` | 159 | UnwindData |  |
| 12 | `__CxxExceptionFilter` | `0x70F0` | 805 | UnwindData |  |
| 16 | `__CxxQueryExceptionSize` | `0x7420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `__CxxRegisterExceptionObject` | `0x7430` | 376 | UnwindData |  |
| 18 | `__CxxUnregisterExceptionObject` | `0x75B0` | 413 | UnwindData |  |
| 24 | `__RTCastToVoid` | `0x8530` | 73 | UnwindData |  |
| 25 | `__RTDynamicCast` | `0x8580` | 509 | UnwindData |  |
| 26 | `__RTtypeid` | `0x8780` | 220 | UnwindData |  |
| 34 | `__std_exception_copy` | `0x8980` | 319 | UnwindData |  |
| 35 | `__std_exception_destroy` | `0x8AC0` | 63 | UnwindData |  |
| 37 | `__std_type_info_compare` | `0x8E50` | 61 | UnwindData |  |
| 38 | `__std_type_info_destroy_list` | `0x8E90` | 82 | UnwindData |  |
| 39 | `__std_type_info_hash` | `0x8EF0` | 174 | UnwindData |  |
| 40 | `__std_type_info_name` | `0x8FA0` | 649 | UnwindData |  |
| 2 | `_CxxThrowException` | `0x9230` | 315 | UnwindData |  |
| 45 | `__uncaught_exception` | `0x9370` | 79 | UnwindData |  |
| 46 | `__uncaught_exceptions` | `0x93C0` | 53 | UnwindData |  |
| 52 | `_get_unexpected` | `0x9440` | 22 | UnwindData |  |
| 64 | `set_unexpected` | `0x9460` | 58 | UnwindData |  |
| 68 | `unexpected` | `0x94A0` | 60 | UnwindData |  |
| 57 | `_set_se_translator` | `0x94E0` | 47 | UnwindData |  |
| 49 | `__vcrt_InitializeCriticalSectionEx` | `0xA2B0` | 103 | UnwindData |  |
| 47 | `__vcrt_GetModuleFileNameW` | `0xA320` | 45 | UnwindData |  |
| 48 | `__vcrt_GetModuleHandleW` | `0xA350` | 25 | UnwindData |  |
| 50 | `__vcrt_LoadLibraryExW` | `0xA370` | 45 | UnwindData |  |
| 51 | `_get_purecall_handler` | `0xA3E0` | 21 | UnwindData |  |
| 55 | `_purecall` | `0xA400` | 56 | UnwindData |  |
| 56 | `_set_purecall_handler` | `0xA440` | 31 | UnwindData |  |
| 41 | `__telemetry_main_invoke_trigger` | `0xA460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `__telemetry_main_return_trigger` | `0xA470` | 72,944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `__unDName` | `0x1C160` | 82 | UnwindData |  |
| 44 | `__unDNameEx` | `0x1C1C0` | 185 | UnwindData |  |
| 58 | `longjmp` | `0x1C5E0` | 43 | UnwindData |  |
| 54 | `_local_unwind` | `0x1C610` | 42 | UnwindData |  |
| 65 | `strchr` | `0x1C640` | 386 | UnwindData |  |
| 66 | `strrchr` | `0x1C7D0` | 1,059 | UnwindData |  |
| 67 | `strstr` | `0x1CC00` | 1,588 | UnwindData |  |
| 69 | `wcschr` | `0x1D240` | 332 | UnwindData |  |
| 70 | `wcsrchr` | `0x1D390` | 525 | UnwindData |  |
| 71 | `wcsstr` | `0x1D5A0` | 1,615 | UnwindData |  |
| 10 | `__C_specific_handler_noexcept` | `0x1DBF0` | 132 | UnwindData |  |
| 9 | `__C_specific_handler` | `0x1E080` | 1,132 | UnwindData |  |
| 1 | `_CreateFrameInfo` | `0x1F730` | 106 | UnwindData |  |
| 3 | `_FindAndUnlinkFrame` | `0x1F7A0` | 128 | UnwindData |  |
| 13 | `__CxxFrameHandler` | `0x1F8A0` | 54 | UnwindData |  |
| 14 | `__CxxFrameHandler2` | `0x1F8E0` | 54 | UnwindData |  |
| 15 | `__CxxFrameHandler3` | `0x1F920` | 209 | UnwindData |  |
| 22 | `__NLG_Dispatch2` | `0x1FE00` | 1 | UnwindData |  |
| 23 | `__NLG_Return2` | `0x1FE10` | 1 | UnwindData |  |
| 33 | `__report_gsfailure` | `0x218E0` | 211 | UnwindData |  |
| 30 | `__intrinsic_setjmp` | `0x21BE0` | 144 | UnwindData |  |
| 31 | `__intrinsic_setjmpex` | `0x21C80` | 144 | UnwindData |  |
| 59 | `memchr` | `0x21D60` | 144 | UnwindData |  |
| 60 | `memcmp` | `0x21E00` | 199 | UnwindData |  |
| 62 | `memmove` | `0x21F00` | 1,645 | UnwindData |  |
| 63 | `memset` | `0x225A0` | 904 | UnwindData |  |
| 61 | `memcpy` | `0x23010` | 0 | Indeterminate |  |
