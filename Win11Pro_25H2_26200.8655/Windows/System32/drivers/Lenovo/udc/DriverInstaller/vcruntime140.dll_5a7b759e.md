# Binary Specification: vcruntime140.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\drivers\Lenovo\udc\DriverInstaller\vcruntime140.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5a7b759ecbcd79d5e1cdc0f7aef5f03d81a5bde11d6c63e769f830fabcf73676`
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
| 63 | `memset` | `0x19A0` | 400 | UnwindData |  |
| 41 | `__telemetry_main_invoke_trigger` | `0x1B30` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `__telemetry_main_return_trigger` | `0x1B30` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `longjmp` | `0x1BB0` | 40 | UnwindData |  |
| 54 | `_local_unwind` | `0x1BE0` | 41 | UnwindData |  |
| 65 | `strchr` | `0x1C10` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `strrchr` | `0x1C90` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `strstr` | `0x1DC0` | 506 | UnwindData |  |
| 69 | `wcschr` | `0x1FC0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `wcsrchr` | `0x2040` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `wcsstr` | `0x20F0` | 534 | UnwindData |  |
| 19 | `__DestructExceptionObject` | `0x2310` | 109 | UnwindData |  |
| 4 | `_IsExceptionObjectToBeDestroyed` | `0x2390` | 47 | UnwindData |  |
| 5 | `_SetWinRTOutOfMemoryExceptionCallback` | `0x23C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `__AdjustPointer` | `0x23D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `__FrameUnwindFilter` | `0x2400` | 101 | UnwindData |  |
| 21 | `__GetPlatformExceptionInfo` | `0x2470` | 91 | UnwindData |  |
| 28 | `__current_exception` | `0x24D0` | 18 | UnwindData |  |
| 29 | `__current_exception_context` | `0x24F0` | 18 | UnwindData |  |
| 32 | `__processing_throw` | `0x2510` | 18 | UnwindData |  |
| 36 | `__std_terminate` | `0x2530` | 11 | UnwindData |  |
| 53 | `_is_exception_typeof` | `0x2540` | 166 | UnwindData |  |
| 7 | `__BuildCatchObject` | `0x54A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `__BuildCatchObjectHelper` | `0x54B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `__TypeMatch` | `0x54C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `__CxxDetectRethrow` | `0x54D0` | 68 | UnwindData |  |
| 12 | `__CxxExceptionFilter` | `0x5520` | 493 | UnwindData |  |
| 16 | `__CxxQueryExceptionSize` | `0x5710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `__CxxRegisterExceptionObject` | `0x5720` | 172 | UnwindData |  |
| 18 | `__CxxUnregisterExceptionObject` | `0x57D0` | 294 | UnwindData |  |
| 24 | `__RTCastToVoid` | `0x5ED0` | 93 | UnwindData |  |
| 25 | `__RTDynamicCast` | `0x5F30` | 358 | UnwindData |  |
| 26 | `__RTtypeid` | `0x60A0` | 174 | UnwindData |  |
| 34 | `__std_exception_copy` | `0x6150` | 144 | UnwindData |  |
| 35 | `__std_exception_destroy` | `0x61E0` | 38 | UnwindData |  |
| 37 | `__std_type_info_compare` | `0x6230` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `__std_type_info_destroy_list` | `0x6260` | 43 | UnwindData |  |
| 39 | `__std_type_info_hash` | `0x6290` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `__std_type_info_name` | `0x62D0` | 284 | UnwindData |  |
| 2 | `_CxxThrowException` | `0x63F0` | 160 | UnwindData |  |
| 45 | `__uncaught_exception` | `0x6490` | 30 | UnwindData |  |
| 46 | `__uncaught_exceptions` | `0x64B0` | 27 | UnwindData |  |
| 52 | `_get_unexpected` | `0x64D0` | 34 | UnwindData |  |
| 64 | `set_unexpected` | `0x6500` | 44 | UnwindData |  |
| 68 | `unexpected` | `0x6530` | 31 | UnwindData |  |
| 57 | `_set_se_translator` | `0x6550` | 45 | UnwindData |  |
| 49 | `__vcrt_InitializeCriticalSectionEx` | `0x6B30` | 97 | UnwindData |  |
| 47 | `__vcrt_GetModuleFileNameW` | `0x6BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `__vcrt_GetModuleHandleW` | `0x6BB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `__vcrt_LoadLibraryExW` | `0x6BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `_get_purecall_handler` | `0x6BD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `_purecall` | `0x6BE0` | 27 | UnwindData |  |
| 56 | `_set_purecall_handler` | `0x6C00` | 31,776 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `__unDName` | `0xE820` | 39 | UnwindData |  |
| 44 | `__unDNameEx` | `0xE850` | 306 | UnwindData |  |
| 10 | `__C_specific_handler_noexcept` | `0xE9E0` | 76 | UnwindData |  |
| 9 | `__C_specific_handler` | `0xEC30` | 523 | UnwindData |  |
| 1 | `_CreateFrameInfo` | `0xF8B0` | 58 | UnwindData |  |
| 3 | `_FindAndUnlinkFrame` | `0xF8F0` | 82 | UnwindData |  |
| 13 | `__CxxFrameHandler` | `0xF9A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `__CxxFrameHandler2` | `0xF9A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `__CxxFrameHandler3` | `0xF9B0` | 134 | UnwindData |  |
| 33 | `__report_gsfailure` | `0x10080` | 210 | UnwindData |  |
| 30 | `__intrinsic_setjmp` | `0x10300` | 144 | UnwindData |  |
| 31 | `__intrinsic_setjmpex` | `0x103C0` | 144 | UnwindData |  |
