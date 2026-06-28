# Binary Specification: vcruntime140d.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\vcruntime140d.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ab6d0cc02fa70bb739fbae00e5de7544cb2dad33a563731a91fb692158d21160`
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
| 7 | `__BuildCatchObject` | `0x6FA0` | 55 | UnwindData |  |
| 8 | `__BuildCatchObjectHelper` | `0x6FE0` | 54 | UnwindData |  |
| 27 | `__TypeMatch` | `0x7020` | 44 | UnwindData |  |
| 11 | `__CxxDetectRethrow` | `0x7050` | 159 | UnwindData |  |
| 12 | `__CxxExceptionFilter` | `0x70F0` | 878 | UnwindData |  |
| 16 | `__CxxQueryExceptionSize` | `0x7460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `__CxxRegisterExceptionObject` | `0x7470` | 376 | UnwindData |  |
| 18 | `__CxxUnregisterExceptionObject` | `0x75F0` | 413 | UnwindData |  |
| 24 | `__RTCastToVoid` | `0x8570` | 73 | UnwindData |  |
| 25 | `__RTDynamicCast` | `0x85C0` | 509 | UnwindData |  |
| 26 | `__RTtypeid` | `0x87C0` | 220 | UnwindData |  |
| 34 | `__std_exception_copy` | `0x89C0` | 319 | UnwindData |  |
| 35 | `__std_exception_destroy` | `0x8B00` | 63 | UnwindData |  |
| 37 | `__std_type_info_compare` | `0x8E90` | 61 | UnwindData |  |
| 38 | `__std_type_info_destroy_list` | `0x8ED0` | 82 | UnwindData |  |
| 39 | `__std_type_info_hash` | `0x8F30` | 174 | UnwindData |  |
| 40 | `__std_type_info_name` | `0x8FE0` | 649 | UnwindData |  |
| 2 | `_CxxThrowException` | `0x9270` | 315 | UnwindData |  |
| 45 | `__uncaught_exception` | `0x93B0` | 79 | UnwindData |  |
| 46 | `__uncaught_exceptions` | `0x9400` | 53 | UnwindData |  |
| 52 | `_get_unexpected` | `0x9480` | 22 | UnwindData |  |
| 64 | `set_unexpected` | `0x94A0` | 58 | UnwindData |  |
| 68 | `unexpected` | `0x94E0` | 60 | UnwindData |  |
| 57 | `_set_se_translator` | `0x9520` | 47 | UnwindData |  |
| 49 | `__vcrt_InitializeCriticalSectionEx` | `0x9C00` | 43 | UnwindData |  |
| 47 | `__vcrt_GetModuleFileNameW` | `0x9C30` | 45 | UnwindData |  |
| 48 | `__vcrt_GetModuleHandleW` | `0x9C60` | 25 | UnwindData |  |
| 50 | `__vcrt_LoadLibraryExW` | `0x9C80` | 45 | UnwindData |  |
| 51 | `_get_purecall_handler` | `0x9CF0` | 21 | UnwindData |  |
| 55 | `_purecall` | `0x9D10` | 56 | UnwindData |  |
| 56 | `_set_purecall_handler` | `0x9D50` | 31 | UnwindData |  |
| 41 | `__telemetry_main_invoke_trigger` | `0x9D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `__telemetry_main_return_trigger` | `0x9D80` | 76,224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `__unDName` | `0x1C740` | 82 | UnwindData |  |
| 44 | `__unDNameEx` | `0x1C7A0` | 185 | UnwindData |  |
| 58 | `longjmp` | `0x1CBC0` | 43 | UnwindData |  |
| 54 | `_local_unwind` | `0x1CBF0` | 42 | UnwindData |  |
| 65 | `strchr` | `0x1CC20` | 386 | UnwindData |  |
| 66 | `strrchr` | `0x1CDB0` | 1,059 | UnwindData |  |
| 67 | `strstr` | `0x1D1E0` | 1,588 | UnwindData |  |
| 69 | `wcschr` | `0x1D820` | 332 | UnwindData |  |
| 70 | `wcsrchr` | `0x1D970` | 525 | UnwindData |  |
| 71 | `wcsstr` | `0x1DB80` | 1,615 | UnwindData |  |
| 10 | `__C_specific_handler_noexcept` | `0x1E1D0` | 132 | UnwindData |  |
| 9 | `__C_specific_handler` | `0x1E6D0` | 1,132 | UnwindData |  |
| 1 | `_CreateFrameInfo` | `0x1FD80` | 106 | UnwindData |  |
| 3 | `_FindAndUnlinkFrame` | `0x1FDF0` | 128 | UnwindData |  |
| 13 | `__CxxFrameHandler` | `0x1FEF0` | 54 | UnwindData |  |
| 14 | `__CxxFrameHandler2` | `0x1FF30` | 54 | UnwindData |  |
| 15 | `__CxxFrameHandler3` | `0x1FF70` | 209 | UnwindData |  |
| 22 | `__NLG_Dispatch2` | `0x20450` | 1 | UnwindData |  |
| 23 | `__NLG_Return2` | `0x20460` | 1 | UnwindData |  |
| 33 | `__report_gsfailure` | `0x225C0` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `__intrinsic_setjmp` | `0x22730` | 144 | UnwindData |  |
| 31 | `__intrinsic_setjmpex` | `0x227D0` | 144 | UnwindData |  |
| 59 | `memchr` | `0x228B0` | 144 | UnwindData |  |
| 62 | `memmove` | `0x22A50` | 1,661 | UnwindData |  |
| 60 | `memcmp` | `0x24010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `memcpy` | `0x24020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `memset` | `0x24030` | 0 | Indeterminate |  |
