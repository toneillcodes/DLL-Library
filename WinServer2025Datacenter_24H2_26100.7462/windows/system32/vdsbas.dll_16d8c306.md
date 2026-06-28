# Binary Specification: vdsbas.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\vdsbas.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `16d8c30662994ad13934d368e3f06de25ec205eb724670751c713f9f092accd6`
* **Total Exported Functions:** 87

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 13 | `??0CPrvEnumObject@@QEAA@XZ` | `0x26C0` | 121 | UnwindData |  |
| 14 | `??0CRtlSharedLock@@QEAA@XZ` | `0x2740` | 45 | UnwindData |  |
| 15 | `??0CVdsCriticalSection@@QEAA@PEAU_RTL_CRITICAL_SECTION@@@Z` | `0x2780` | 37 | UnwindData |  |
| 16 | `??0CVdsPnPNotificationBase@@QEAA@XZ` | `0x27B0` | 75 | UnwindData |  |
| 17 | `??0CVdsUnlockIt@@QEAA@AEAJ@Z` | `0x2810` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `??1CPrvEnumObject@@QEAA@XZ` | `0x2870` | 267 | UnwindData |  |
| 31 | `??1CRtlSharedLock@@QEAA@XZ` | `0x2990` | 23 | UnwindData |  |
| 32 | `??1CVdsCriticalSection@@QEAA@XZ` | `0x29B0` | 26 | UnwindData |  |
| 33 | `??1CVdsPnPNotificationBase@@QEAA@XZ` | `0x29D0` | 39 | UnwindData |  |
| 34 | `??1CVdsUnlockIt@@QEAA@XZ` | `0x2A00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `??_FCRtlList@@QEAAXXZ` | `0x2A10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `??_FCRtlMap@@QEAAXXZ` | `0x2A30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `?AcquireRead@CRtlSharedLock@@AEAAXXZ` | `0x2A50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `?AcquireWrite@CRtlSharedLock@@AEAAXXZ` | `0x2A70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `?AllowCancel@CVdsAsyncObjectBase@@QEAAXXZ` | `0x2A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `?CurrentThreadIsWriter@CRtlSharedLock@@QEAAHXZ` | `0x2AA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `?DisallowCancel@CVdsAsyncObjectBase@@QEAAXXZ` | `0x2AD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `?Downgrade@CRtlSharedLock@@AEAAXXZ` | `0x2AE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `?GetOutputType@CVdsAsyncObjectBase@@QEAA?AW4_VDS_ASYNC_OUTPUT_TYPE@@XZ` | `0x2B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `?IsCancelRequested@CVdsAsyncObjectBase@@QEAAHXZ` | `0x2B10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `?Release@CRtlSharedLock@@AEAAXXZ` | `0x2B20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `?SetOutput@CVdsAsyncObjectBase@@QEAAXU_VDS_ASYNC_OUTPUT@@@Z` | `0x2B40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `?SetOutputType@CVdsAsyncObjectBase@@QEAAXW4_VDS_ASYNC_OUTPUT_TYPE@@@Z` | `0x2B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `?SetPositionToLast@CPrvEnumObject@@QEAAXXZ` | `0x2B70` | 81 | UnwindData |  |
| 80 | `?Upgrade@CRtlSharedLock@@AEAAXXZ` | `0x2BD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `?ZeroAsyncOut@CVdsAsyncObjectBase@@QEAAXXZ` | `0x2BF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `?m_ExtraLogging@CVdsTraceSettings@@QEAAHXZ` | `0x2C10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `?m_NoDebuggerLogging@CVdsTraceSettings@@QEAAHXZ` | `0x2C20` | 7,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `??1?$CVdsPtr@E@@QEAA@XZ` | `0x47C0` | 5,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `??1?$CVdsPtr@G@@QEAA@XZ` | `0x47C0` | 5,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `??1?$CVdsPtr@U_AUCTION_THREAD_PARAMETER@@@@QEAA@XZ` | `0x47C0` | 5,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `??1?$CVdsPtr@U_DRIVE_LAYOUT_INFORMATION_EX@@@@QEAA@XZ` | `0x47C0` | 5,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `??1?$CVdsPtr@U_VDS_DRIVE_LAYOUT_INFORMATION_EX@@@@QEAA@XZ` | `0x47C0` | 5,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `DllCanUnloadNow` | `0x5F00` | 73 | UnwindData |  |
| 85 | `DllGetClassObject` | `0x5F50` | 106 | UnwindData |  |
| 86 | `DllRegisterServer` | `0x60D0` | 301 | UnwindData |  |
| 87 | `DllUnregisterServer` | `0x6210` | 235 | UnwindData |  |
| 1 | `??0?$CVdsHandleImpl@$0?0@@QEAA@XZ` | `0x63B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0?$CVdsHandleImpl@$0A@@@QEAA@XZ` | `0x63C0` | 1,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0?$CVdsHeapPtr@E@@QEAA@XZ` | `0x63C0` | 1,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `??0?$CVdsHeapPtr@G@@QEAA@XZ` | `0x63C0` | 1,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `??0?$CVdsHeapPtr@U_AUCTION_THREAD_PARAMETER@@@@QEAA@XZ` | `0x63C0` | 1,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `??0?$CVdsHeapPtr@U_DRIVE_LAYOUT_INFORMATION_EX@@@@QEAA@XZ` | `0x63C0` | 1,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `??0?$CVdsHeapPtr@U_VDS_DRIVE_LAYOUT_INFORMATION_EX@@@@QEAA@XZ` | `0x63C0` | 1,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `??0?$CVdsPtr@E@@QEAA@XZ` | `0x63C0` | 1,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `??0?$CVdsPtr@G@@QEAA@XZ` | `0x63C0` | 1,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `??0?$CVdsPtr@U_AUCTION_THREAD_PARAMETER@@@@QEAA@XZ` | `0x63C0` | 1,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `??0?$CVdsPtr@U_DRIVE_LAYOUT_INFORMATION_EX@@@@QEAA@XZ` | `0x63C0` | 1,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `??0?$CVdsPtr@U_VDS_DRIVE_LAYOUT_INFORMATION_EX@@@@QEAA@XZ` | `0x63C0` | 1,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `??1?$CVdsHandleImpl@$0?0@@QEAA@XZ` | `0x67E0` | 45 | UnwindData |  |
| 19 | `??1?$CVdsHandleImpl@$0A@@@QEAA@XZ` | `0x6820` | 40 | UnwindData |  |
| 20 | `??1?$CVdsHeapPtr@E@@QEAA@XZ` | `0x6850` | 69 | UnwindData |  |
| 21 | `??1?$CVdsHeapPtr@G@@QEAA@XZ` | `0x6850` | 69 | UnwindData |  |
| 22 | `??1?$CVdsHeapPtr@U_AUCTION_THREAD_PARAMETER@@@@QEAA@XZ` | `0x6850` | 69 | UnwindData |  |
| 23 | `??1?$CVdsHeapPtr@U_DRIVE_LAYOUT_INFORMATION_EX@@@@QEAA@XZ` | `0x6850` | 69 | UnwindData |  |
| 24 | `??1?$CVdsHeapPtr@U_VDS_DRIVE_LAYOUT_INFORMATION_EX@@@@QEAA@XZ` | `0x6850` | 69 | UnwindData |  |
| 35 | `??4?$CVdsHandleImpl@$0A@@@QEAAPEAXPEAX@Z` | `0x6E80` | 54 | UnwindData |  |
| 36 | `??4?$CVdsHeapPtr@E@@QEAAPEAEPEAE@Z` | `0x6EC0` | 84 | UnwindData |  |
| 37 | `??4?$CVdsHeapPtr@G@@QEAAPEAGPEAG@Z` | `0x6EC0` | 84 | UnwindData |  |
| 38 | `??4?$CVdsHeapPtr@U_AUCTION_THREAD_PARAMETER@@@@QEAAPEAU_AUCTION_THREAD_PARAMETER@@PEAU1@@Z` | `0x6EC0` | 84 | UnwindData |  |
| 39 | `??4?$CVdsHeapPtr@U_VDS_DRIVE_LAYOUT_INFORMATION_EX@@@@QEAAPEAU_VDS_DRIVE_LAYOUT_INFORMATION_EX@@PEAU1@@Z` | `0x6EC0` | 84 | UnwindData |  |
| 40 | `??8?$CVdsHandleImpl@$0A@@@QEBA_NPEAX@Z` | `0x6F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `??8?$CVdsPtr@E@@QEBA_NPEAE@Z` | `0x6F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `??8?$CVdsPtr@G@@QEBA_NPEAG@Z` | `0x6F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `??8?$CVdsPtr@U_AUCTION_THREAD_PARAMETER@@@@QEBA_NPEAU_AUCTION_THREAD_PARAMETER@@@Z` | `0x6F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `??B?$CVdsHandleImpl@$0?0@@QEAAPEAXXZ` | `0x6F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `??B?$CVdsPtr@E@@QEBAPEAEXZ` | `0x6F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `??B?$CVdsPtr@G@@QEBAPEAGXZ` | `0x6F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `??B?$CVdsPtr@U_AUCTION_THREAD_PARAMETER@@@@QEBAPEAU_AUCTION_THREAD_PARAMETER@@XZ` | `0x6F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `??B?$CVdsPtr@U_DRIVE_LAYOUT_INFORMATION_EX@@@@QEBAPEAU_DRIVE_LAYOUT_INFORMATION_EX@@XZ` | `0x6F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `??B?$CVdsPtr@U_VDS_DRIVE_LAYOUT_INFORMATION_EX@@@@QEBAPEAU_VDS_DRIVE_LAYOUT_INFORMATION_EX@@XZ` | `0x6F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `??C?$CVdsPtr@U_AUCTION_THREAD_PARAMETER@@@@QEBAPEAU_AUCTION_THREAD_PARAMETER@@XZ` | `0x6F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `??C?$CVdsPtr@U_DRIVE_LAYOUT_INFORMATION_EX@@@@QEBAPEAU_DRIVE_LAYOUT_INFORMATION_EX@@XZ` | `0x6F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `??C?$CVdsPtr@U_VDS_DRIVE_LAYOUT_INFORMATION_EX@@@@QEBAPEAU_VDS_DRIVE_LAYOUT_INFORMATION_EX@@XZ` | `0x6F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `??I?$CVdsHandleImpl@$0?0@@QEAAPEAPEAXXZ` | `0x6F40` | 2,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `??I?$CVdsPtr@U_DRIVE_LAYOUT_INFORMATION_EX@@@@QEAAPEAPEAU_DRIVE_LAYOUT_INFORMATION_EX@@XZ` | `0x6F40` | 2,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `??I?$CVdsPtr@U_VDS_DRIVE_LAYOUT_INFORMATION_EX@@@@QEAAPEAPEAU_VDS_DRIVE_LAYOUT_INFORMATION_EX@@XZ` | `0x6F40` | 2,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `?Attach@?$CVdsPtr@G@@QEAAXPEAG@Z` | `0x78C0` | 3,136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `?Attach@?$CVdsPtr@U_DRIVE_LAYOUT_INFORMATION_EX@@@@QEAAXPEAU_DRIVE_LAYOUT_INFORMATION_EX@@@Z` | `0x78C0` | 3,136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `?Attach@?$CVdsPtr@U_VDS_DRIVE_LAYOUT_INFORMATION_EX@@@@QEAAXPEAU_VDS_DRIVE_LAYOUT_INFORMATION_EX@@@Z` | `0x78C0` | 3,136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `?Detach@?$CVdsHandleImpl@$0?0@@QEAAPEAXXZ` | `0x8500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `?Detach@?$CVdsPtr@G@@QEAAPEAGXZ` | `0x8510` | 29,760 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `?Detach@?$CVdsPtr@U_AUCTION_THREAD_PARAMETER@@@@QEAAPEAU_AUCTION_THREAD_PARAMETER@@XZ` | `0x8510` | 29,760 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `?Detach@?$CVdsPtr@U_DRIVE_LAYOUT_INFORMATION_EX@@@@QEAAPEAU_DRIVE_LAYOUT_INFORMATION_EX@@XZ` | `0x8510` | 29,760 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `?Detach@?$CVdsPtr@U_VDS_DRIVE_LAYOUT_INFORMATION_EX@@@@QEAAPEAU_VDS_DRIVE_LAYOUT_INFORMATION_EX@@XZ` | `0x8510` | 29,760 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `?Close@?$CVdsHandleImpl@$0?0@@QEAAXXZ` | `0xF950` | 45 | UnwindData |  |
| 44 | `??9?$CVdsPtr@E@@QEBA_NPEAE@Z` | `0x12680` | 86,751 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
