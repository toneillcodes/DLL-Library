# Binary Specification: vdsbas.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\vdsbas.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0a8b19fbab3678cc3994bb180c49b3c63aa1b590682ab273a526dc931974c92c`
* **Total Exported Functions:** 87

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 13 | `??0CPrvEnumObject@@QEAA@XZ` | `0x2950` | 121 | UnwindData |  |
| 14 | `??0CRtlSharedLock@@QEAA@XZ` | `0x29D0` | 45 | UnwindData |  |
| 15 | `??0CVdsCriticalSection@@QEAA@PEAU_RTL_CRITICAL_SECTION@@@Z` | `0x2A10` | 37 | UnwindData |  |
| 16 | `??0CVdsPnPNotificationBase@@QEAA@XZ` | `0x2A40` | 75 | UnwindData |  |
| 17 | `??0CVdsUnlockIt@@QEAA@AEAJ@Z` | `0x2AA0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `??1CPrvEnumObject@@QEAA@XZ` | `0x2B00` | 267 | UnwindData |  |
| 31 | `??1CRtlSharedLock@@QEAA@XZ` | `0x2C20` | 23 | UnwindData |  |
| 32 | `??1CVdsCriticalSection@@QEAA@XZ` | `0x2C40` | 26 | UnwindData |  |
| 33 | `??1CVdsPnPNotificationBase@@QEAA@XZ` | `0x2C60` | 39 | UnwindData |  |
| 34 | `??1CVdsUnlockIt@@QEAA@XZ` | `0x2C90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `??_FCRtlList@@QEAAXXZ` | `0x2CA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `??_FCRtlMap@@QEAAXXZ` | `0x2CC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `?AcquireRead@CRtlSharedLock@@AEAAXXZ` | `0x2CE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `?AcquireWrite@CRtlSharedLock@@AEAAXXZ` | `0x2D00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `?AllowCancel@CVdsAsyncObjectBase@@QEAAXXZ` | `0x2D20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `?CurrentThreadIsWriter@CRtlSharedLock@@QEAAHXZ` | `0x2D30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `?DisallowCancel@CVdsAsyncObjectBase@@QEAAXXZ` | `0x2D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `?Downgrade@CRtlSharedLock@@AEAAXXZ` | `0x2D70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `?GetOutputType@CVdsAsyncObjectBase@@QEAA?AW4_VDS_ASYNC_OUTPUT_TYPE@@XZ` | `0x2D90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `?IsCancelRequested@CVdsAsyncObjectBase@@QEAAHXZ` | `0x2DA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `?Release@CRtlSharedLock@@AEAAXXZ` | `0x2DB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `?SetOutput@CVdsAsyncObjectBase@@QEAAXU_VDS_ASYNC_OUTPUT@@@Z` | `0x2DD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `?SetOutputType@CVdsAsyncObjectBase@@QEAAXW4_VDS_ASYNC_OUTPUT_TYPE@@@Z` | `0x2DF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `?SetPositionToLast@CPrvEnumObject@@QEAAXXZ` | `0x2E00` | 81 | UnwindData |  |
| 80 | `?Upgrade@CRtlSharedLock@@AEAAXXZ` | `0x2E60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `?ZeroAsyncOut@CVdsAsyncObjectBase@@QEAAXXZ` | `0x2E80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `?m_ExtraLogging@CVdsTraceSettings@@QEAAHXZ` | `0x2EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `?m_NoDebuggerLogging@CVdsTraceSettings@@QEAAHXZ` | `0x2EB0` | 7,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `??1?$CVdsPtr@E@@QEAA@XZ` | `0x4A50` | 5,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `??1?$CVdsPtr@G@@QEAA@XZ` | `0x4A50` | 5,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `??1?$CVdsPtr@U_AUCTION_THREAD_PARAMETER@@@@QEAA@XZ` | `0x4A50` | 5,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `??1?$CVdsPtr@U_DRIVE_LAYOUT_INFORMATION_EX@@@@QEAA@XZ` | `0x4A50` | 5,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `??1?$CVdsPtr@U_VDS_DRIVE_LAYOUT_INFORMATION_EX@@@@QEAA@XZ` | `0x4A50` | 5,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `DllCanUnloadNow` | `0x6190` | 73 | UnwindData |  |
| 85 | `DllGetClassObject` | `0x61E0` | 106 | UnwindData |  |
| 86 | `DllRegisterServer` | `0x6360` | 301 | UnwindData |  |
| 87 | `DllUnregisterServer` | `0x64A0` | 235 | UnwindData |  |
| 1 | `??0?$CVdsHandleImpl@$0?0@@QEAA@XZ` | `0x7180` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0?$CVdsHandleImpl@$0A@@@QEAA@XZ` | `0x7190` | 2,160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0?$CVdsHeapPtr@E@@QEAA@XZ` | `0x7190` | 2,160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `??0?$CVdsHeapPtr@G@@QEAA@XZ` | `0x7190` | 2,160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `??0?$CVdsHeapPtr@U_AUCTION_THREAD_PARAMETER@@@@QEAA@XZ` | `0x7190` | 2,160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `??0?$CVdsHeapPtr@U_DRIVE_LAYOUT_INFORMATION_EX@@@@QEAA@XZ` | `0x7190` | 2,160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `??0?$CVdsHeapPtr@U_VDS_DRIVE_LAYOUT_INFORMATION_EX@@@@QEAA@XZ` | `0x7190` | 2,160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `??0?$CVdsPtr@E@@QEAA@XZ` | `0x7190` | 2,160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `??0?$CVdsPtr@G@@QEAA@XZ` | `0x7190` | 2,160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `??0?$CVdsPtr@U_AUCTION_THREAD_PARAMETER@@@@QEAA@XZ` | `0x7190` | 2,160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `??0?$CVdsPtr@U_DRIVE_LAYOUT_INFORMATION_EX@@@@QEAA@XZ` | `0x7190` | 2,160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `??0?$CVdsPtr@U_VDS_DRIVE_LAYOUT_INFORMATION_EX@@@@QEAA@XZ` | `0x7190` | 2,160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `??1?$CVdsHandleImpl@$0?0@@QEAA@XZ` | `0x7A00` | 45 | UnwindData |  |
| 19 | `??1?$CVdsHandleImpl@$0A@@@QEAA@XZ` | `0x7A40` | 40 | UnwindData |  |
| 20 | `??1?$CVdsHeapPtr@E@@QEAA@XZ` | `0x7A70` | 69 | UnwindData |  |
| 21 | `??1?$CVdsHeapPtr@G@@QEAA@XZ` | `0x7A70` | 69 | UnwindData |  |
| 22 | `??1?$CVdsHeapPtr@U_AUCTION_THREAD_PARAMETER@@@@QEAA@XZ` | `0x7A70` | 69 | UnwindData |  |
| 23 | `??1?$CVdsHeapPtr@U_DRIVE_LAYOUT_INFORMATION_EX@@@@QEAA@XZ` | `0x7A70` | 69 | UnwindData |  |
| 24 | `??1?$CVdsHeapPtr@U_VDS_DRIVE_LAYOUT_INFORMATION_EX@@@@QEAA@XZ` | `0x7A70` | 69 | UnwindData |  |
| 35 | `??4?$CVdsHandleImpl@$0A@@@QEAAPEAXPEAX@Z` | `0x8880` | 54 | UnwindData |  |
| 36 | `??4?$CVdsHeapPtr@E@@QEAAPEAEPEAE@Z` | `0x88C0` | 84 | UnwindData |  |
| 37 | `??4?$CVdsHeapPtr@G@@QEAAPEAGPEAG@Z` | `0x88C0` | 84 | UnwindData |  |
| 38 | `??4?$CVdsHeapPtr@U_AUCTION_THREAD_PARAMETER@@@@QEAAPEAU_AUCTION_THREAD_PARAMETER@@PEAU1@@Z` | `0x88C0` | 84 | UnwindData |  |
| 39 | `??4?$CVdsHeapPtr@U_VDS_DRIVE_LAYOUT_INFORMATION_EX@@@@QEAAPEAU_VDS_DRIVE_LAYOUT_INFORMATION_EX@@PEAU1@@Z` | `0x88C0` | 84 | UnwindData |  |
| 40 | `??8?$CVdsHandleImpl@$0A@@@QEBA_NPEAX@Z` | `0x8920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `??8?$CVdsPtr@E@@QEBA_NPEAE@Z` | `0x8920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `??8?$CVdsPtr@G@@QEBA_NPEAG@Z` | `0x8920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `??8?$CVdsPtr@U_AUCTION_THREAD_PARAMETER@@@@QEBA_NPEAU_AUCTION_THREAD_PARAMETER@@@Z` | `0x8920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `??B?$CVdsHandleImpl@$0?0@@QEAAPEAXXZ` | `0x8930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `??B?$CVdsPtr@E@@QEBAPEAEXZ` | `0x8930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `??B?$CVdsPtr@G@@QEBAPEAGXZ` | `0x8930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `??B?$CVdsPtr@U_AUCTION_THREAD_PARAMETER@@@@QEBAPEAU_AUCTION_THREAD_PARAMETER@@XZ` | `0x8930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `??B?$CVdsPtr@U_DRIVE_LAYOUT_INFORMATION_EX@@@@QEBAPEAU_DRIVE_LAYOUT_INFORMATION_EX@@XZ` | `0x8930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `??B?$CVdsPtr@U_VDS_DRIVE_LAYOUT_INFORMATION_EX@@@@QEBAPEAU_VDS_DRIVE_LAYOUT_INFORMATION_EX@@XZ` | `0x8930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `??C?$CVdsPtr@U_AUCTION_THREAD_PARAMETER@@@@QEBAPEAU_AUCTION_THREAD_PARAMETER@@XZ` | `0x8930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `??C?$CVdsPtr@U_DRIVE_LAYOUT_INFORMATION_EX@@@@QEBAPEAU_DRIVE_LAYOUT_INFORMATION_EX@@XZ` | `0x8930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `??C?$CVdsPtr@U_VDS_DRIVE_LAYOUT_INFORMATION_EX@@@@QEBAPEAU_VDS_DRIVE_LAYOUT_INFORMATION_EX@@XZ` | `0x8930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `??I?$CVdsHandleImpl@$0?0@@QEAAPEAPEAXXZ` | `0x8940` | 3,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `??I?$CVdsPtr@U_DRIVE_LAYOUT_INFORMATION_EX@@@@QEAAPEAPEAU_DRIVE_LAYOUT_INFORMATION_EX@@XZ` | `0x8940` | 3,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `??I?$CVdsPtr@U_VDS_DRIVE_LAYOUT_INFORMATION_EX@@@@QEAAPEAPEAU_VDS_DRIVE_LAYOUT_INFORMATION_EX@@XZ` | `0x8940` | 3,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `?Attach@?$CVdsPtr@G@@QEAAXPEAG@Z` | `0x9700` | 3,856 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `?Attach@?$CVdsPtr@U_DRIVE_LAYOUT_INFORMATION_EX@@@@QEAAXPEAU_DRIVE_LAYOUT_INFORMATION_EX@@@Z` | `0x9700` | 3,856 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `?Attach@?$CVdsPtr@U_VDS_DRIVE_LAYOUT_INFORMATION_EX@@@@QEAAXPEAU_VDS_DRIVE_LAYOUT_INFORMATION_EX@@@Z` | `0x9700` | 3,856 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `?Detach@?$CVdsHandleImpl@$0?0@@QEAAPEAXXZ` | `0xA610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `?Detach@?$CVdsPtr@G@@QEAAPEAGXZ` | `0xA620` | 53,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `?Detach@?$CVdsPtr@U_AUCTION_THREAD_PARAMETER@@@@QEAAPEAU_AUCTION_THREAD_PARAMETER@@XZ` | `0xA620` | 53,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `?Detach@?$CVdsPtr@U_DRIVE_LAYOUT_INFORMATION_EX@@@@QEAAPEAU_DRIVE_LAYOUT_INFORMATION_EX@@XZ` | `0xA620` | 53,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `?Detach@?$CVdsPtr@U_VDS_DRIVE_LAYOUT_INFORMATION_EX@@@@QEAAPEAU_VDS_DRIVE_LAYOUT_INFORMATION_EX@@XZ` | `0xA620` | 53,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `?Close@?$CVdsHandleImpl@$0?0@@QEAAXXZ` | `0x17540` | 45 | UnwindData |  |
| 44 | `??9?$CVdsPtr@E@@QEBA_NPEAE@Z` | `0x1A1F0` | 90,652 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
