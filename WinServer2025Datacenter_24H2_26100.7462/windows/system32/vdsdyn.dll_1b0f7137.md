# Binary Specification: vdsdyn.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\vdsdyn.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1b0f71370ca29457717936120a540dc4803b303096e7b8c5803ce53aee491d07`
* **Total Exported Functions:** 32

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `??0CPrvEnumObject@@QEAA@XZ` | `0x2590` | 121 | UnwindData |  |
| 2 | `??0CRtlSharedLock@@QEAA@XZ` | `0x2610` | 45 | UnwindData |  |
| 3 | `??0CVdsCriticalSection@@QEAA@PEAU_RTL_CRITICAL_SECTION@@@Z` | `0x2650` | 37 | UnwindData |  |
| 4 | `??0CVdsPnPNotificationBase@@QEAA@XZ` | `0x2680` | 75 | UnwindData |  |
| 5 | `??0CVdsUnlockIt@@QEAA@AEAJ@Z` | `0x26E0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `??1CPrvEnumObject@@QEAA@XZ` | `0x2750` | 287 | UnwindData |  |
| 7 | `??1CRtlSharedLock@@QEAA@XZ` | `0x2880` | 23 | UnwindData |  |
| 8 | `??1CVdsCriticalSection@@QEAA@XZ` | `0x28A0` | 26 | UnwindData |  |
| 9 | `??1CVdsPnPNotificationBase@@QEAA@XZ` | `0x28C0` | 39 | UnwindData |  |
| 10 | `??1CVdsUnlockIt@@QEAA@XZ` | `0x28F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `??_FCRtlList@@QEAAXXZ` | `0x2900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `??_FCRtlMap@@QEAAXXZ` | `0x2920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `?AcquireRead@CRtlSharedLock@@AEAAXXZ` | `0x2940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `?AcquireWrite@CRtlSharedLock@@AEAAXXZ` | `0x2960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `?AllowCancel@CVdsAsyncObjectBase@@QEAAXXZ` | `0x2980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `?CurrentThreadIsWriter@CRtlSharedLock@@QEAAHXZ` | `0x2990` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `?DisallowCancel@CVdsAsyncObjectBase@@QEAAXXZ` | `0x29C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `?Downgrade@CRtlSharedLock@@AEAAXXZ` | `0x29D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `?GetOutputType@CVdsAsyncObjectBase@@QEAA?AW4_VDS_ASYNC_OUTPUT_TYPE@@XZ` | `0x29F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `?IsCancelRequested@CVdsAsyncObjectBase@@QEAAHXZ` | `0x2A00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `?Release@CRtlSharedLock@@AEAAXXZ` | `0x2A10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `?SetOutput@CVdsAsyncObjectBase@@QEAAXU_VDS_ASYNC_OUTPUT@@@Z` | `0x2A30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `?SetOutputType@CVdsAsyncObjectBase@@QEAAXW4_VDS_ASYNC_OUTPUT_TYPE@@@Z` | `0x2A50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `?SetPositionToLast@CPrvEnumObject@@QEAAXXZ` | `0x2A60` | 81 | UnwindData |  |
| 25 | `?Upgrade@CRtlSharedLock@@AEAAXXZ` | `0x2AC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `?ZeroAsyncOut@CVdsAsyncObjectBase@@QEAAXXZ` | `0x2AE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `?m_ExtraLogging@CVdsTraceSettings@@QEAAHXZ` | `0x2B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `?m_NoDebuggerLogging@CVdsTraceSettings@@QEAAHXZ` | `0x2B10` | 14,112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `DllCanUnloadNow` | `0x6230` | 63 | UnwindData |  |
| 30 | `DllGetClassObject` | `0x6280` | 117 | UnwindData |  |
| 31 | `DllRegisterServer` | `0x6420` | 491 | UnwindData |  |
| 32 | `DllUnregisterServer` | `0x6620` | 251 | UnwindData |  |
