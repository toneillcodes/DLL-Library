# Binary Specification: KernelBase.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\KernelBase.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c0dcbf9232b93e4e9820a6359fa22f508f73f690d689a1c85b7efd68417e34fe`
* **Total Exported Functions:** 2037

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 11 | `AcquireSRWLockExclusive` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlAcquireSRWLockExclusive` |
| 12 | `AcquireSRWLockShared` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlAcquireSRWLockShared` |
| 39 | `AddVectoredContinueHandler` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlAddVectoredContinueHandler` |
| 40 | `AddVectoredExceptionHandler` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlAddVectoredExceptionHandler` |
| 124 | `CancelThreadpoolIo` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpCancelAsyncIoOperation` |
| 164 | `CloseThreadpool` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpReleasePool` |
| 165 | `CloseThreadpoolCleanupGroup` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpReleaseCleanupGroup` |
| 166 | `CloseThreadpoolCleanupGroupMembers` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpReleaseCleanupGroupMembers` |
| 167 | `CloseThreadpoolIo` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpReleaseIoCompletion` |
| 168 | `CloseThreadpoolTimer` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpReleaseTimer` |
| 169 | `CloseThreadpoolWait` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpReleaseWait` |
| 170 | `CloseThreadpoolWork` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpReleaseWork` |
| 193 | `CopyMemoryNonTemporal` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlCopyMemoryNonTemporal` |
| 276 | `DecodePointer` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlDecodePointer` |
| 277 | `DecodeRemotePointer` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlDecodeRemotePointer` |
| 278 | `DecodeSystemPointer` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlDecodeSystemPointer` |
| 284 | `DeleteCriticalSection` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlDeleteCriticalSection` |
| 308 | `DisassociateCurrentThreadFromCallback` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpDisassociateCallback` |
| 329 | `EncodePointer` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlEncodePointer` |
| 330 | `EncodeRemotePointer` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlEncodeRemotePointer` |
| 331 | `EncodeSystemPointer` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlEncodeSystemPointer` |
| 333 | `EnterCriticalSection` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlEnterCriticalSection` |
| 375 | `EventActivityIdControl` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.EtwEventActivityIdControl` |
| 376 | `EventEnabled` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.EtwEventEnabled` |
| 377 | `EventProviderEnabled` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.EtwEventProviderEnabled` |
| 378 | `EventRegister` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.EtwEventRegister` |
| 379 | `EventSetInformation` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.EtwEventSetInformation` |
| 380 | `EventUnregister` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.EtwEventUnregister` |
| 381 | `EventWrite` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.EtwEventWrite` |
| 382 | `EventWriteEx` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.EtwEventWriteEx` |
| 383 | `EventWriteString` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.EtwEventWriteString` |
| 384 | `EventWriteTransfer` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.EtwEventWriteTransfer` |
| 385 | `ExitProcess` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlExitUserProcess` |
| 386 | `ExitThread` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlExitUserThread` |
| 431 | `FlsGetValue2` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlFlsGetValue2` |
| 436 | `FlushProcessWriteBuffers` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.NtFlushProcessWriteBuffers` |
| 451 | `FreeLibraryWhenCallbackReturns` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpCallbackUnloadDllOnCompletion` |
| 553 | `GetCurrentProcessorNumber` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlGetCurrentProcessorNumber` |
| 554 | `GetCurrentProcessorNumberEx` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlGetCurrentProcessorNumberEx` |
| 598 | `GetFeatureToggleConfiguration` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlGetFeatureToggleConfiguration` |
| 599 | `GetFeatureTogglesChangeToken` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlGetFeatureTogglesChangeToken` |
| 875 | `GetTraceEnableFlags` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.EtwGetTraceEnableFlags` |
| 876 | `GetTraceEnableLevel` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.EtwGetTraceEnableLevel` |
| 877 | `GetTraceLoggerHandle` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.EtwGetTraceLoggerHandle` |
| 920 | `HeapAlloc` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlAllocateHeap` |
| 924 | `HeapFree` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlFreeHeap` |
| 927 | `HeapReAlloc` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlReAllocateHeap` |
| 929 | `HeapSize` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlSizeHeap` |
| 945 | `InitOnceInitialize` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlRunOnceInitialize` |
| 947 | `InitializeConditionVariable` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlInitializeConditionVariable` |
| 950 | `InitializeCriticalSection` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlInitializeCriticalSection` |
| 956 | `InitializeSListHead` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlInitializeSListHead` |
| 957 | `InitializeSRWLock` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlInitializeSRWLock` |
| 962 | `InterlockedFlushSList` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlInterlockedFlushSList` |
| 963 | `InterlockedPopEntrySList` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlInterlockedPopEntrySList` |
| 964 | `InterlockedPushEntrySList` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlInterlockedPushEntrySList` |
| 965 | `InterlockedPushListSList` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlInterlockedPushListSList` |
| 966 | `InterlockedPushListSListEx` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlInterlockedPushListSListEx` |
| 1017 | `IsThreadpoolTimerSet` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpIsTimerSet` |
| 1068 | `LeaveCriticalSection` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlLeaveCriticalSection` |
| 1069 | `LeaveCriticalSectionWhenCallbackReturns` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpCallbackLeaveCriticalSectionOnCompletion` |
| 1133 | `NotifyFeatureToggleUsage` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlNotifyFeatureToggleUsage` |
| 1370 | `QueryDepthSList` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlQueryDepthSList` |
| 1383 | `QueryPerformanceCounter` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlQueryPerformanceCounter` |
| 1384 | `QueryPerformanceFrequency` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlQueryPerformanceFrequency` |
| 1394 | `QueryUnbiasedInterruptTime` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlQueryUnbiasedInterruptTime` |
| 1508 | `RegisterTraceGuidsW` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.EtwRegisterTraceGuidsW` |
| 1512 | `ReleaseMutexWhenCallbackReturns` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpCallbackReleaseMutexOnCompletion` |
| 1515 | `ReleaseSRWLockExclusive` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlReleaseSRWLockExclusive` |
| 1516 | `ReleaseSRWLockShared` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlReleaseSRWLockShared` |
| 1518 | `ReleaseSemaphoreWhenCallbackReturns` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpCallbackReleaseSemaphoreOnCompletion` |
| 1531 | `RemoveVectoredContinueHandler` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlRemoveVectoredContinueHandler` |
| 1532 | `RemoveVectoredExceptionHandler` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlRemoveVectoredExceptionHandler` |
| 1543 | `RestoreLastError` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlRestoreLastWin32Error` |
| 1619 | `SetCriticalSectionSpinCount` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlSetCriticalSectionSpinCount` |
| 1631 | `SetEventWhenCallbackReturns` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpCallbackSetEventOnCompletion` |
| 1652 | `SetLastError` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlSetLastWin32Error` |
| 1713 | `SetThreadpoolThreadMaximum` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpSetPoolMaxThreads` |
| 1715 | `SetThreadpoolTimer` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpSetTimer` |
| 1716 | `SetThreadpoolTimerEx` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpSetTimerEx` |
| 1717 | `SetThreadpoolWait` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpSetWait` |
| 1718 | `SetThreadpoolWaitEx` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpSetWaitEx` |
| 1736 | `StartThreadpoolIo` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpStartAsyncIoOperation` |
| 1798 | `SubmitThreadpoolWork` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpPostWork` |
| 1826 | `TraceEvent` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.EtwLogTraceEvent` |
| 1827 | `TraceMessage` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.EtwTraceMessage` |
| 1828 | `TraceMessageVa` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.EtwTraceMessageVa` |
| 1831 | `TryAcquireSRWLockExclusive` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlTryAcquireSRWLockExclusive` |
| 1832 | `TryAcquireSRWLockShared` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlTryAcquireSRWLockShared` |
| 1835 | `TryEnterCriticalSection` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlTryEnterCriticalSection` |
| 1850 | `UnregisterTraceGuids` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.EtwUnregisterTraceGuids` |
| 1893 | `VerSetConditionMask` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.VerSetConditionMask` |
| 1935 | `WaitForThreadpoolIoCallbacks` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpWaitForIoCompletion` |
| 1936 | `WaitForThreadpoolTimerCallbacks` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpWaitForTimer` |
| 1937 | `WaitForThreadpoolWaitCallbacks` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpWaitForWait` |
| 1938 | `WaitForThreadpoolWorkCallbacks` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpWaitForWork` |
| 1942 | `WakeAllConditionVariable` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlWakeAllConditionVariable` |
| 1943 | `WakeByAddressAll` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlWakeAddressAll` |
| 1944 | `WakeByAddressSingle` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlWakeAddressSingle` |
| 1945 | `WakeConditionVariable` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlWakeConditionVariable` |
| 1997 | `__C_specific_handler` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.__C_specific_handler` |
| 2004 | `__chkstk` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.__chkstk` |
| 2006 | `__misaligned_access` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.__misaligned_access` |
| 2016 | `_local_unwind` | `0x0` | - | Forwarded | Forwarded to: `NTDLL._local_unwind` |
| 705 | `GetPackageFamilyNameFromToken` | `0x4ED0` | 829 | UnwindData |  |
| 59 | `AppPolicyGetMediaFoundationCodecLoading` | `0x57A0` | 133 | UnwindData |  |
| 58 | `AppPolicyGetLifecycleManagement` | `0x5830` | 136 | UnwindData |  |
| 156 | `ClosePackageInfo` | `0x58C0` | 29 | UnwindData |  |
| 539 | `GetCurrentPackageFamilyName` | `0x5C30` | 278 | UnwindData |  |
| 1622 | `SetCurrentDirectoryW` | `0x5D70` | 107 | UnwindData |  |
| 711 | `GetPackageId` | `0x5F10` | 256 | UnwindData |  |
| 56 | `AppPolicyGetClrCompat` | `0x6020` | 149 | UnwindData |  |
| 62 | `AppPolicyGetThreadInitializationType` | `0x6320` | 137 | UnwindData |  |
| 60 | `AppPolicyGetProcessTerminationMethod` | `0x63B0` | 137 | UnwindData |  |
| 63 | `AppPolicyGetWindowingModel` | `0x6990` | 153 | UnwindData |  |
| 1151 | `OpenPackageInfoByFullNameForMachine` | `0x70A0` | 123 | UnwindData |  |
| 472 | `GetApplicationUserModelIdFromToken` | `0x72E0` | 176 | UnwindData |  |
| 471 | `GetApplicationUserModelId` | `0x7C70` | 180 | UnwindData |  |
| 706 | `GetPackageFullName` | `0x8270` | 225 | UnwindData |  |
| 707 | `GetPackageFullNameFromToken` | `0x9650` | 217 | UnwindData |  |
| 702 | `GetPackageFamilyName` | `0x99F0` | 328 | UnwindData |  |
| 579 | `GetEffectivePackageStatusForUser` | `0xA390` | 114 | UnwindData |  |
| 727 | `GetPackageStatus` | `0xA410` | 1,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1177 | `PackageIdFromFullName` | `0xA9E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 827 | `GetSystemMetadataPathForPackage` | `0xAA00` | 119 | UnwindData |  |
| 1898 | `VerifyPackageFullName` | `0xABB0` | 112 | UnwindData |  |
| 1169 | `PackageFamilyNameFromFullName` | `0xB280` | 98 | UnwindData |  |
| 1181 | `PackageNameAndPublisherIdFromFamilyName` | `0xE140` | 819 | UnwindData |  |
| 1200 | `PathCanonicalizeW` | `0xF540` | 93 | UnwindData |  |
| 1198 | `PathAppendW` | `0xF5E0` | 223 | UnwindData |  |
| 1219 | `PathCchStripToRoot` | `0xF6D0` | 920 | UnwindData |  |
| 1204 | `PathCchAppend` | `0xFA70` | 241 | UnwindData |  |
| 1208 | `PathCchCombine` | `0xFDC0` | 20 | UnwindData |  |
| 1196 | `PathAllocCombine` | `0xFDE0` | 303 | UnwindData |  |
| 1886 | `UrlUnescapeW` | `0x10020` | 97 | UnwindData |  |
| 1205 | `PathCchAppendEx` | `0x10850` | 283 | UnwindData |  |
| 1209 | `PathCchCombineEx` | `0x10980` | 90 | UnwindData |  |
| 671 | `GetModuleHandleW` | `0x11F30` | 12 | UnwindData |  |
| 742 | `GetProcAddress` | `0x11FC0` | 13 | UnwindData |  |
| 1088 | `LocalFree` | `0x12120` | 349 | UnwindData |  |
| 1770 | `StrDupW` | `0x12320` | 24 | UnwindData |  |
| 1084 | `LocalAlloc` | `0x123E0` | 542 | UnwindData |  |
| 1230 | `PathFindExtensionW` | `0x12EC0` | 119 | UnwindData |  |
| 2035 | `lstrlenW` | `0x12F40` | 35 | UnwindData |  |
| 151 | `ChrCmpIW` | `0x12F70` | 66 | UnwindData |  |
| 1552 | `SHLoadIndirectStringInternal` | `0x131E0` | 178 | UnwindData |  |
| 1785 | `StrStrIW` | `0x13900` | 42 | UnwindData |  |
| 967 | `InternalLcidToName` | `0x13DA0` | 504 | UnwindData |  |
| 178 | `CompareStringW` | `0x17010` | 3,298 | UnwindData |  |
| 176 | `CompareStringEx` | `0x17D10` | 466 | UnwindData |  |
| 1066 | `LCMapStringW` | `0x19F20` | 367 | UnwindData |  |
| 1065 | `LCMapStringEx` | `0x1A0A0` | 5,969 | UnwindData |  |
| 675 | `GetNamedLocaleHashNode` | `0x1B800` | 182 | UnwindData |  |
| 1934 | `WaitForSingleObjectEx` | `0x1C240` | 344 | UnwindData |  |
| 175 | `CompareStringA` | `0x1C960` | 104 | UnwindData |  |
| 1119 | `MultiByteToWideChar` | `0x1DEF0` | 7,154 | UnwindData |  |
| 1629 | `SetErrorMode` | `0x20A00` | 167 | UnwindData |  |
| 476 | `GetCPHashNode` | `0x20AB0` | 51 | UnwindData |  |
| 1076 | `LoadLibraryExW` | `0x215A0` | 482 | UnwindData |  |
| 449 | `FreeLibrary` | `0x21790` | 85 | UnwindData |  |
| 1081 | `LoadStringBaseExW` | `0x21880` | 187 | UnwindData |  |
| 694 | `GetOverlappedResultEx` | `0x219F0` | 319 | UnwindData |  |
| 756 | `GetProcessMitigationPolicy` | `0x21B40` | 1,112 | UnwindData |  |
| 693 | `GetOverlappedResult` | `0x21FA0` | 279 | UnwindData |  |
| 1371 | `QueryDosDeviceW` | `0x220C0` | 2,482 | UnwindData |  |
| 1931 | `WaitForMultipleObjects` | `0x22A80` | 23 | UnwindData |  |
| 1932 | `WaitForMultipleObjectsEx` | `0x22AA0` | 523 | UnwindData |  |
| 933 | `HeapWalk` | `0x22CC0` | 426 | UnwindData |  |
| 1733 | `SleepConditionVariableSRW` | `0x22E70` | 106 | UnwindData |  |
| 1429 | `ReadFile` | `0x22EE0` | 545 | UnwindData |  |
| 1164 | `OpenThreadToken` | `0x23110` | 42 | UnwindData |  |
| 773 | `GetQueuedCompletionStatus` | `0x23140` | 260 | UnwindData |  |
| 942 | `InitOnceBeginInitialize` | `0x23250` | 68 | UnwindData |  |
| 627 | `GetFullPathNameW` | `0x232E0` | 59 | UnwindData |  |
| 1923 | `VirtualUnlock` | `0x23330` | 75 | UnwindData |  |
| 1111 | `MapViewOfFileExNuma` | `0x23390` | 479 | UnwindData |  |
| 1149 | `OpenMutexW` | `0x23580` | 54 | UnwindData |  |
| 874 | `GetTokenInformation` | `0x23810` | 130 | UnwindData |  |
| 1640 | `SetFilePointer` | `0x238A0` | 507 | UnwindData |  |
| 305 | `DeviceIoControl` | `0x23AB0` | 509 | UnwindData |  |
| 1107 | `MapViewOfFile` | `0x23CC0` | 430 | UnwindData |  |
| 1710 | `SetThreadToken` | `0x23E80` | 83 | UnwindData |  |
| 1732 | `SleepConditionVariableCS` | `0x23EE0` | 106 | UnwindData |  |
| 1154 | `OpenProcess` | `0x23F50` | 120 | UnwindData |  |
| 1097 | `LockFileEx` | `0x23FD0` | 204 | UnwindData |  |
| 670 | `GetModuleHandleExW` | `0x240B0` | 104 | UnwindData |  |
| 761 | `GetProcessVersion` | `0x24210` | 314 | UnwindData |  |
| 1155 | `OpenProcessToken` | `0x24350` | 46 | UnwindData |  |
| 603 | `GetFileAttributesExW` | `0x24390` | 116 | UnwindData |  |
| 606 | `GetFileInformationByHandleEx` | `0x24540` | 202 | UnwindData |  |
| 1940 | `WaitNamedPipeW` | `0x24880` | 111 | UnwindData |  |
| 1083 | `LoadStringW` | `0x24D20` | 184 | UnwindData |  |
| 590 | `GetErrorMode` | `0x24E80` | 88 | UnwindData |  |
| 1641 | `SetFilePointerEx` | `0x24EE0` | 347 | UnwindData |  |
| 1517 | `ReleaseSemaphore` | `0x25050` | 42 | UnwindData |  |
| 575 | `GetDriveTypeW` | `0x25810` | 390 | UnwindData |  |
| 154 | `CloseHandle` | `0x26AF0` | 229 | UnwindData |  |
| 217 | `CreateFileA` | `0x26BE0` | 336 | UnwindData |  |
| 898 | `GetVolumeNameForVolumeMountPointW` | `0x26D40` | 534 | UnwindData |  |
| 214 | `CreateFile2` | `0x27890` | 55 | UnwindData |  |
| 223 | `CreateFileW` | `0x27C40` | 210 | UnwindData |  |
| 460 | `GetAce` | `0x28810` | 46 | UnwindData |  |
| 1030 | `IsWellKnownSid` | `0x28850` | 76 | UnwindData |  |
| 625 | `GetFinalPathNameByHandleW` | `0x28F10` | 115 | UnwindData |  |
| 1275 | `PathRemoveBackslashW` | `0x2B540` | 149 | UnwindData |  |
| 137 | `CharPrevW` | `0x2B5E0` | 194 | UnwindData |  |
| 1287 | `PathSkipRootW` | `0x2B6B0` | 74 | UnwindData |  |
| 1281 | `PathRemoveFileSpecW` | `0x2B700` | 328 | UnwindData |  |
| 1217 | `PathCchSkipRoot` | `0x2B850` | 683 | UnwindData |  |
| 1212 | `PathCchRemoveBackslash` | `0x2BB10` | 108 | UnwindData |  |
| 1215 | `PathCchRemoveFileSpec` | `0x2BB90` | 43 | UnwindData |  |
| 1213 | `PathCchRemoveBackslashEx` | `0x2BF30` | 111 | UnwindData |  |
| 1211 | `PathCchIsRoot` | `0x2C000` | 636 | UnwindData |  |
| 145 | `CheckIsMSIXPackage` | `0x2CF10` | 400 | UnwindData |  |
| 194 | `CopySid` | `0x2D0B0` | 42 | UnwindData |  |
| 71 | `AppXGetPackageSid` | `0x2D0E0` | 969 | UnwindData |  |
| 68 | `AppXGetOSMaxVersionTested` | `0x2D4B0` | 494 | UnwindData |  |
| 1152 | `OpenPackageInfoByFullNameForUser` | `0x2D720` | 108 | UnwindData |  |
| 423 | `FindPackagesByPackageFamily` | `0x2E8A0` | 51 | UnwindData |  |
| 445 | `FreeEnvironmentStringsA` | `0x35200` | 14,032 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 446 | `FreeEnvironmentStringsW` | `0x35200` | 14,032 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 644 | `GetLengthSid` | `0x388D0` | 43 | UnwindData |  |
| 51 | `AppContainerFreeMemory` | `0x393F0` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `AppXFreeMemory` | `0x393F0` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1817 | `TestQueryData` | `0x39650` | 68 | UnwindData |  |
| 1813 | `TestClose` | `0x3A8D0` | 107 | UnwindData |  |
| 50 | `AppContainerDeriveSidFromMoniker` | `0x3BBE0` | 258 | UnwindData |  |
| 884 | `GetUserDefaultLocaleName` | `0x3D6A0` | 247 | UnwindData |  |
| 1456 | `RegDisablePredefinedCacheEx` | `0x3D8C0` | 29 | UnwindData |  |
| 306 | `DisablePredefinedHandleTableInternal` | `0x3D8F0` | 156 | UnwindData |  |
| 458 | `GetAcceptLanguagesA` | `0x3D9A0` | 243 | UnwindData |  |
| 1148 | `OpenGlobalizationUserSettingsKey` | `0x3DE00` | 193 | UnwindData |  |
| 1496 | `RegSetKeySecurity` | `0x3DED0` | 1,712 | UnwindData |  |
| 1463 | `RegGetValueA` | `0x3E5C0` | 1,157 | UnwindData |  |
| 1490 | `RegQueryValueExA` | `0x3ED90` | 1,047 | UnwindData |  |
| 1481 | `RegOpenKeyExA` | `0x3F1B0` | 34 | UnwindData |  |
| 1482 | `RegOpenKeyExInternalA` | `0x3F1E0` | 765 | UnwindData |  |
| 824 | `GetSystemInfo` | `0x41800` | 197 | UnwindData |  |
| 1511 | `ReleaseMutex` | `0x41A30` | 44 | UnwindData |  |
| 1503 | `RegisterApplicationRestart` | `0x42180` | 396 | UnwindData |  |
| 1845 | `UnregisterApplicationRestart` | `0x42320` | 335 | UnwindData |  |
| 1734 | `SleepEx` | `0x42A10` | 236 | UnwindData |  |
| 1032 | `IsWow64Process` | `0x42F10` | 94 | UnwindData |  |
| 1916 | `VirtualFreeEx` | `0x43370` | 212 | UnwindData |  |
| 750 | `GetProcessId` | `0x43DD0` | 85 | UnwindData |  |
| 323 | `DuplicateHandle` | `0x43E30` | 155 | UnwindData |  |
| 856 | `GetThreadId` | `0x43F50` | 85 | UnwindData |  |
| 1990 | `WriteProcessMemory` | `0x43FB0` | 875 | UnwindData |  |
| 1874 | `UrlGetLocationW` | `0x44470` | 132 | UnwindData |  |
| 1884 | `UrlIsW` | `0x44990` | 49 | UnwindData |  |
| 1762 | `StrCmpNICW` | `0x44F80` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1869 | `UrlCreateFromPathW` | `0x45180` | 189 | UnwindData |  |
| 1261 | `PathIsURLW` | `0x45AF0` | 18 | UnwindData |  |
| 1259 | `PathIsUNCW` | `0x45D80` | 21 | UnwindData |  |
| 1876 | `UrlGetPartW` | `0x45EC0` | 791 | UnwindData |  |
| 1226 | `PathCreateFromUrlW` | `0x461E0` | 29 | UnwindData |  |
| 131 | `CharLowerW` | `0x46F70` | 96 | UnwindData |  |
| 1871 | `UrlEscapeW` | `0x481A0` | 29 | UnwindData |  |
| 1865 | `UrlCombineW` | `0x49340` | 43 | UnwindData |  |
| 1863 | `UrlCanonicalizeW` | `0x493F0` | 537 | UnwindData |  |
| 1885 | `UrlUnescapeA` | `0x4DBB0` | 361 | UnwindData |  |
| 1220 | `PathCombineA` | `0x4DEC0` | 56 | UnwindData |  |
| 1290 | `PathStripToRootA` | `0x4DF00` | 34 | UnwindData |  |
| 1199 | `PathCanonicalizeA` | `0x4DF30` | 82 | UnwindData |  |
| 1282 | `PathRenameExtensionA` | `0x4DF90` | 113 | UnwindData |  |
| 1229 | `PathFindExtensionA` | `0x4E010` | 68 | UnwindData |  |
| 1864 | `UrlCombineA` | `0x4E1E0` | 43 | UnwindData |  |
| 1260 | `PathIsURLA` | `0x4E2E0` | 58 | UnwindData |  |
| 1189 | `ParseURLA` | `0x4E320` | 236 | UnwindData |  |
| 1280 | `PathRemoveFileSpecA` | `0x4E420` | 90 | UnwindData |  |
| 1875 | `UrlGetPartA` | `0x4EA20` | 576 | UnwindData |  |
| 1197 | `PathAppendA` | `0x4EE00` | 86 | UnwindData |  |
| 1757 | `StrCmpNA` | `0x4EFA0` | 116 | UnwindData |  |
| 135 | `CharPrevA` | `0x4F8E0` | 68 | UnwindData |  |
| 477 | `GetCPInfo` | `0x4FBB0` | 528 | UnwindData |  |
| 1783 | `StrStrA` | `0x4FDD0` | 280 | UnwindData |  |
| 1239 | `PathGetDriveNumberA` | `0x4FEF0` | 77 | UnwindData |  |
| 2033 | `lstrlen` | `0x4FF50` | 35 | UnwindData |  |
| 2034 | `lstrlenA` | `0x4FF50` | 35 | UnwindData |  |
| 1784 | `StrStrIA` | `0x4FF80` | 220 | UnwindData |  |
| 1231 | `PathFindFileNameA` | `0x50070` | 28 | UnwindData |  |
| 1746 | `StrChrIA` | `0x50190` | 1,376 | UnwindData |  |
| 997 | `IsDBCSLeadByte` | `0x50700` | 81 | UnwindData |  |
| 1745 | `StrChrA_MB` | `0x50970` | 120 | UnwindData |  |
| 1744 | `StrChrA` | `0x509F0` | 526 | UnwindData |  |
| 132 | `CharNextA` | `0x50C10` | 140 | UnwindData |  |
| 1788 | `StrStrW` | `0x50D20` | 451 | UnwindData |  |
| 1765 | `StrCmpW` | `0x50EF0` | 36 | UnwindData |  |
| 1764 | `StrCmpNW` | `0x51090` | 38 | UnwindData |  |
| 1756 | `StrCmpLogicalW` | `0x51240` | 204 | UnwindData |  |
| 1763 | `StrCmpNIW` | `0x51320` | 38 | UnwindData |  |
| 2027 | `lstrcmpi` | `0x51510` | 1,262 | UnwindData |  |
| 2028 | `lstrcmpiA` | `0x51510` | 1,262 | UnwindData |  |
| 150 | `ChrCmpIA` | `0x51A10` | 115 | UnwindData |  |
| 2026 | `lstrcmpW` | `0x51F80` | 775 | UnwindData |  |
| 1702 | `SetThreadLocale` | `0x52D40` | 238 | UnwindData |  |
| 1892 | `VerQueryValueW` | `0x52F00` | 23 | UnwindData |  |
| 1747 | `StrChrIW` | `0x53590` | 691 | UnwindData |  |
| 1755 | `StrCmpIW` | `0x53850` | 50 | UnwindData |  |
| 889 | `GetUserOverrideString` | `0x54200` | 116 | UnwindData |  |
| 890 | `GetUserOverrideWord` | `0x54A20` | 233 | UnwindData |  |
| 1128 | `NlsIsUserDefaultLocale` | `0x54CC0` | 32 | UnwindData |  |
| 882 | `GetUserDefaultLCID` | `0x54CF0` | 74 | UnwindData |  |
| 2029 | `lstrcmpiW` | `0x54D40` | 1,268 | UnwindData |  |
| 811 | `GetStringTypeExW` | `0x55240` | 3,848 | UnwindData |  |
| 1131 | `NlsValidateLocale` | `0x57B70` | 545 | UnwindData |  |
| 1965 | `WideCharToMultiByte` | `0x58880` | 6,395 | UnwindData |  |
| 593 | `GetExtensionApplicationUserModelId` | `0x5AF10` | 1,416 | UnwindData |  |
| 1679 | `SetProtocolProperty` | `0x5B4A0` | 40 | UnwindData |  |
| 1008 | `IsOnDemandRegistrationSupportedForExtensionCategory` | `0x5B560` | 75 | UnwindData |  |
| 368 | `EnumerateExtensionNames` | `0x5B5C0` | 672 | UnwindData |  |
| 596 | `GetExtensionProperty2` | `0x5B870` | 697 | UnwindData |  |
| 1632 | `SetExtensionProperty` | `0x5BB30` | 691 | UnwindData |  |
| 595 | `GetExtensionProperty` | `0x5BDF0` | 863 | UnwindData |  |
| 29 | `AddExtensionProgId` | `0x5C6B0` | 1,856 | UnwindData |  |
| 1441 | `RegCopyTreeW` | `0x5D190` | 79 | UnwindData |  |
| 1442 | `RegCreateKeyExA` | `0x5DF80` | 81 | UnwindData |  |
| 1497 | `RegSetKeyValueA` | `0x5DFE0` | 198 | UnwindData |  |
| 1443 | `RegCreateKeyExInternalA` | `0x5E0B0` | 906 | UnwindData |  |
| 1499 | `RegSetValueExA` | `0x5E440` | 790 | UnwindData |  |
| 1500 | `RegSetValueExW` | `0x5E760` | 1,317 | UnwindData |  |
| 1486 | `RegQueryInfoKeyA` | `0x5EF40` | 899 | UnwindData |  |
| 1498 | `RegSetKeyValueW` | `0x5F450` | 192 | UnwindData |  |
| 1445 | `RegCreateKeyExW` | `0x5F840` | 85 | UnwindData |  |
| 1487 | `RegQueryInfoKeyW` | `0x5FF10` | 1,422 | UnwindData |  |
| 1444 | `RegCreateKeyExInternalW` | `0x604B0` | 1,464 | UnwindData |  |
| 1479 | `RegNotifyChangeKeyValue` | `0x611B0` | 51 | UnwindData |  |
| 1458 | `RegEnumKeyExW` | `0x617A0` | 1,023 | UnwindData |  |
| 1484 | `RegOpenKeyExW` | `0x61BB0` | 34 | UnwindData |  |
| 1483 | `RegOpenKeyExInternalW` | `0x61BE0` | 1,124 | UnwindData |  |
| 1105 | `MapPredefinedHandleInternal` | `0x62050` | 91 | UnwindData |  |
| 117 | `CLOSE_LOCAL_HANDLE_INTERNAL` | `0x63800` | 11 | UnwindData |  |
| 1440 | `RegCloseKey` | `0x63AE0` | 670 | UnwindData |  |
| 1464 | `RegGetValueW` | `0x64310` | 65 | UnwindData |  |
| 1491 | `RegQueryValueExW` | `0x64C70` | 568 | UnwindData |  |
| 1457 | `RegEnumKeyExA` | `0x68050` | 932 | UnwindData |  |
| 770 | `GetPtrCalDataArray` | `0x6B140` | 86 | UnwindData |  |
| 337 | `EnumCalendarInfoW` | `0x6B1E0` | 96 | UnwindData |  |
| 339 | `EnumDateFormatsExW` | `0x6B250` | 80 | UnwindData |  |
| 576 | `GetDurationFormatEx` | `0x6B2B0` | 165 | UnwindData |  |
| 335 | `EnumCalendarInfoExEx` | `0x6B360` | 117 | UnwindData |  |
| 968 | `Internal_EnumCalendarInfo` | `0x6B3E0` | 3,835 | UnwindData |  |
| 589 | `GetEraNameCountedString` | `0x6C320` | 291 | UnwindData |  |
| 1125 | `NlsDispatchAnsiEnumProc` | `0x6C4B0` | 437 | UnwindData |  |
| 338 | `EnumDateFormatsExEx` | `0x6C670` | 89 | UnwindData |  |
| 969 | `Internal_EnumDateFormats` | `0x6C6D0` | 429 | UnwindData |  |
| 365 | `EnumTimeFormatsEx` | `0x6C890` | 84 | UnwindData |  |
| 974 | `Internal_EnumTimeFormats` | `0x6C8F0` | 176 | UnwindData |  |
| 480 | `GetCalendar` | `0x6CFD0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 975 | `Internal_EnumUILanguages` | `0x6D110` | 2,031 | UnwindData |  |
| 817 | `GetSystemDefaultLangID` | `0x6DCE0` | 41 | UnwindData |  |
| 1723 | `SetUserGeoName` | `0x6DDA0` | 127 | UnwindData |  |
| 1654 | `SetLocaleInfoW` | `0x6E160` | 213 | UnwindData |  |
| 143 | `CheckGroupPolicyEnabled` | `0x6E240` | 533 | UnwindData |  |
| 631 | `GetGeoInfoEx` | `0x6EA60` | 108 | UnwindData |  |
| 881 | `GetUserDefaultGeoName` | `0x6EAE0` | 240 | UnwindData |  |
| 886 | `GetUserGeoID` | `0x6EBE0` | 102 | UnwindData |  |
| 1994 | `_AddMUIStringToCache` | `0x6F990` | 33 | UnwindData |  |
| 1478 | `RegLoadMUIStringW` | `0x6FEB0` | 121 | UnwindData |  |
| 1551 | `SHLoadIndirectString` | `0x70220` | 509 | UnwindData |  |
| 1082 | `LoadStringByReference` | `0x70430` | 3,450 | UnwindData |  |
| 1996 | `_OpenMuiStringCache` | `0x711B0` | 645 | UnwindData |  |
| 1228 | `PathFileExistsW` | `0x71650` | 78 | UnwindData |  |
| 655 | `GetLongPathNameW` | `0x716B0` | 2,037 | UnwindData |  |
| 410 | `FindFirstFileW` | `0x71EB0` | 50 | UnwindData |  |
| 408 | `FindFirstFileExW` | `0x71EF0` | 45 | UnwindData |  |
| 401 | `FindClose` | `0x72650` | 281 | UnwindData |  |
| 600 | `GetFileAttributesA` | `0x72770` | 156 | UnwindData |  |
| 604 | `GetFileAttributesW` | `0x72820` | 375 | UnwindData |  |
| 1995 | `_GetMUIStringFromCache` | `0x72A60` | 789 | UnwindData |  |
| 791 | `GetShortPathNameW` | `0x72D80` | 1,207 | UnwindData |  |
| 1156 | `OpenRegKey` | `0x735D0` | 783 | UnwindData |  |
| 560 | `GetDateFormatEx` | `0x74040` | 329 | UnwindData |  |
| 870 | `GetTimeFormatEx` | `0x74190` | 255 | UnwindData |  |
| 475 | `GetCPFileNameFromRegistry` | `0x742A0` | 358 | UnwindData |  |
| 1022 | `IsValidCodePage` | `0x74410` | 210 | UnwindData |  |
| 1064 | `LCMapStringA` | `0x746C0` | 1,182 | UnwindData |  |
| 632 | `GetGeoInfoW` | `0x74B70` | 40 | UnwindData |  |
| 818 | `GetSystemDefaultLocaleName` | `0x74F60` | 180 | UnwindData |  |
| 481 | `GetCalendarInfoEx` | `0x75490` | 131 | UnwindData |  |
| 646 | `GetLocaleInfoA` | `0x76030` | 62 | UnwindData |  |
| 649 | `GetLocaleInfoW` | `0x765B0` | 297 | UnwindData |  |
| 647 | `GetLocaleInfoEx` | `0x766E0` | 95 | UnwindData |  |
| 648 | `GetLocaleInfoHelper` | `0x76750` | 16,416 | UnwindData |  |
| 262 | `CreateThreadpoolTimer` | `0x7B150` | 72 | UnwindData |  |
| 86 | `ArmFeatureUsageSubscriberFlushNotification` | `0x7C190` | 92 | UnwindData |  |
| 1816 | `TestOpen` | `0x7C670` | 188 | UnwindData |  |
| 1815 | `TestCreate` | `0x7C8D0` | 210 | UnwindData |  |
| 153 | `ClearCommError` | `0x7D420` | 553 | UnwindData |  |
| 250 | `CreateSemaphoreExW` | `0x7D800` | 72 | UnwindData |  |
| 251 | `CreateSemaphoreW` | `0x7E160` | 322 | UnwindData |  |
| 95 | `BaseFormatObjectAttributes` | `0x7E2B0` | 599 | UnwindData |  |
| 209 | `CreateEventExA` | `0x7E540` | 50 | UnwindData |  |
| 230 | `CreateMutexExA` | `0x7E780` | 131 | UnwindData |  |
| 208 | `CreateEventA` | `0x7E810` | 66 | UnwindData |  |
| 908 | `GlobalAlloc` | `0x7EF10` | 600 | UnwindData |  |
| 910 | `GlobalFree` | `0x7F170` | 343 | UnwindData |  |
| 211 | `CreateEventW` | `0x7F2D0` | 384 | UnwindData |  |
| 229 | `CreateMutexA` | `0x7F460` | 142 | UnwindData |  |
| 210 | `CreateEventExW` | `0x7F500` | 76 | UnwindData |  |
| 1147 | `OpenFileMappingW` | `0x7F6A0` | 54 | UnwindData |  |
| 231 | `CreateMutexExW` | `0x7F810` | 73 | UnwindData |  |
| 232 | `CreateMutexW` | `0x7FD10` | 344 | UnwindData |  |
| 1157 | `OpenSemaphoreW` | `0x7FE70` | 246 | UnwindData |  |
| 98 | `BaseGetNamedObjectDirectory` | `0x7FF70` | 87 | UnwindData |  |
| 203 | `CreateDirectoryA` | `0x809F0` | 79 | UnwindData |  |
| 206 | `CreateDirectoryW` | `0x80A50` | 125 | UnwindData |  |
| 222 | `CreateFileMappingW` | `0x80B60` | 672 | UnwindData |  |
| 601 | `GetFileAttributesExA` | `0x80E10` | 92 | UnwindData |  |
| 221 | `CreateFileMappingNumaW` | `0x80F20` | 715 | UnwindData |  |
| 405 | `FindFirstFileA` | `0x81200` | 424 | UnwindData |  |
| 1143 | `OpenEventA` | `0x813B0` | 193 | UnwindData |  |
| 1144 | `OpenEventW` | `0x81480` | 54 | UnwindData |  |
| 568 | `GetDiskFreeSpaceExA` | `0x81710` | 120 | UnwindData |  |
| 1635 | `SetFileAttributesA` | `0x81790` | 77 | UnwindData |  |
| 289 | `DeleteFileA` | `0x817F0` | 73 | UnwindData |  |
| 574 | `GetDriveTypeA` | `0x81840` | 100 | UnwindData |  |
| 569 | `GetDiskFreeSpaceExW` | `0x81BD0` | 609 | UnwindData |  |
| 492 | `GetCompressedFileSizeA` | `0x81E40` | 80 | UnwindData |  |
| 493 | `GetCompressedFileSizeW` | `0x81EA0` | 486 | UnwindData |  |
| 611 | `GetFileSize` | `0x82090` | 195 | UnwindData |  |
| 616 | `GetFileVersionInfoByHandle` | `0x82160` | 691 | UnwindData |  |
| 1843 | `UnmapViewOfFile2` | `0x82420` | 171 | UnwindData |  |
| 1637 | `SetFileAttributesW` | `0x824E0` | 45 | UnwindData |  |
| 239 | `CreateProcessA` | `0x827F0` | 108 | UnwindData |  |
| 242 | `CreateProcessInternalA` | `0x82870` | 1,357 | UnwindData |  |
| 244 | `CreateProcessW` | `0x82DD0` | 108 | UnwindData |  |
| 241 | `CreateProcessAsUserW` | `0x82E50` | 105 | UnwindData |  |
| 243 | `CreateProcessInternalW` | `0x82EC0` | 26,381 | UnwindData |  |
| 713 | `GetPackageInfo2` | `0x895E0` | 54 | UnwindData |  |
| 712 | `GetPackageInfo` | `0x89620` | 420 | UnwindData |  |
| 714 | `GetPackageInfo3` | `0x897D0` | 556 | UnwindData |  |
| 810 | `GetStringTypeA` | `0x89DF0` | 238 | UnwindData |  |
| 812 | `GetStringTypeW` | `0x89EF0` | 46 | UnwindData |  |
| 364 | `EnumSystemLocalesW` | `0x8A370` | 34 | UnwindData |  |
| 808 | `GetStringScripts` | `0x8A590` | 598 | UnwindData |  |
| 362 | `EnumSystemLocalesA` | `0x8A840` | 33 | UnwindData |  |
| 363 | `EnumSystemLocalesEx` | `0x8A870` | 51 | UnwindData |  |
| 1542 | `ResolveLocaleName` | `0x8A940` | 1,471 | UnwindData |  |
| 973 | `Internal_EnumSystemLocales` | `0x8B2E0` | 2,327 | UnwindData |  |
| 354 | `EnumResourceNamesW` | `0x8C170` | 34 | UnwindData |  |
| 1890 | `VerLanguageNameW` | `0x8C4A0` | 236 | UnwindData |  |
| 353 | `EnumResourceNamesExW` | `0x8C7D0` | 38 | UnwindData |  |
| 478 | `GetCPInfoExW` | `0x8C800` | 502 | UnwindData |  |
| 809 | `GetStringTableEntry` | `0x8CA00` | 664 | UnwindData |  |
| 424 | `FindResourceExW` | `0x8E6A0` | 354 | UnwindData |  |
| 92 | `BaseDllMapResourceIdW` | `0x8E810` | 347 | UnwindData |  |
| 91 | `BaseDllFreeResourceId` | `0x8E980` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1079 | `LoadResource` | `0x8EAF0` | 124 | UnwindData |  |
| 350 | `EnumResourceLanguagesExW` | `0x8F900` | 51 | UnwindData |  |
| 417 | `FindNextFileA` | `0x8F940` | 336 | UnwindData |  |
| 419 | `FindNextFileW` | `0x8FD30` | 750 | UnwindData |  |
| 356 | `EnumResourceTypesExW` | `0x90030` | 30 | UnwindData |  |
| 177 | `CompareStringOrdinal` | `0x91180` | 97 | UnwindData |  |
| 1366 | `QISearch` | `0x924A0` | 66 | UnwindData |  |
| 1991 | `WriteStateAtomValue` | `0x92840` | 128 | UnwindData |  |
| 295 | `DeleteStateAtomValue` | `0x92920` | 82 | UnwindData |  |
| 1434 | `ReadStateContainerValue` | `0x92A70` | 238 | UnwindData |  |
| 717 | `GetPackagePath` | `0x92DE0` | 168 | UnwindData |  |
| 34 | `AddPackageNameAliasesByPackageFullName` | `0x936D0` | 365 | UnwindData |  |
| 1902 | `VerifyPackageName` | `0x93D70` | 93 | UnwindData |  |
| 1474 | `RegLoadAppKeyW` | `0x94FC0` | 572 | UnwindData |  |
| 1446 | `RegDeleteKeyExA` | `0x960F0` | 21 | UnwindData |  |
| 1447 | `RegDeleteKeyExInternalA` | `0x96110` | 152 | UnwindData |  |
| 1555 | `SHRegCreateUSKeyW` | `0x961B0` | 217 | UnwindData |  |
| 1452 | `RegDeleteTreeA` | `0x963E0` | 96 | UnwindData |  |
| 1575 | `SHRegSetUSValueW` | `0x96940` | 200 | UnwindData |  |
| 1451 | `RegDeleteKeyValueW` | `0x96A40` | 92 | UnwindData |  |
| 1455 | `RegDeleteValueW` | `0x96AB0` | 621 | UnwindData |  |
| 1453 | `RegDeleteTreeW` | `0x96D30` | 811 | UnwindData |  |
| 1449 | `RegDeleteKeyExW` | `0x97070` | 21 | UnwindData |  |
| 1448 | `RegDeleteKeyExInternalW` | `0x97090` | 325 | UnwindData |  |
| 1566 | `SHRegGetUSValueA` | `0x976C0` | 297 | UnwindData |  |
| 1568 | `SHRegOpenUSKeyA` | `0x977F0` | 142 | UnwindData |  |
| 1572 | `SHRegQueryUSValueA` | `0x97890` | 384 | UnwindData |  |
| 1577 | `SHRegWriteUSValueW` | `0x97A20` | 295 | UnwindData |  |
| 1565 | `SHRegGetBoolUSValueW` | `0x97B50` | 698 | UnwindData |  |
| 1567 | `SHRegGetUSValueW` | `0x97E10` | 302 | UnwindData |  |
| 1569 | `SHRegOpenUSKeyW` | `0x97F50` | 59 | UnwindData |  |
| 1573 | `SHRegQueryUSValueW` | `0x98460` | 516 | UnwindData |  |
| 1553 | `SHRegCloseUSKey` | `0x98670` | 132 | UnwindData |  |
| 1563 | `SHRegEnumUSValueW` | `0x989B0` | 566 | UnwindData |  |
| 1460 | `RegEnumValueW` | `0x994E0` | 565 | UnwindData |  |
| 1970 | `WilFailureWatcherUnsubscribe` | `0x9BAD0` | 81 | UnwindData |  |
| 1992 | `WriteStateContainerValue` | `0x9C020` | 236 | UnwindData |  |
| 2020 | `atexit` | `0x9C9F0` | 24 | UnwindData |  |
| 2017 | `_onexit` | `0x9CB00` | 76 | UnwindData |  |
| 943 | `InitOnceComplete` | `0x9CB90` | 42 | UnwindData |  |
| 1966 | `WilFailureNotifyWatchers` | `0x9D750` | 31 | UnwindData |  |
| 557 | `GetCurrentThreadId` | `0x9D7D0` | 784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 999 | `IsDebuggerPresent` | `0x9DAE0` | 7,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 796 | `GetStagedPackageOrigin` | `0x9F700` | 190 | UnwindData |  |
| 540 | `GetCurrentPackageFullName` | `0xA0000` | 206 | UnwindData |  |
| 731 | `GetPackageVolumeSisPath` | `0xA1430` | 642 | UnwindData |  |
| 895 | `GetVolumeInformationA` | `0xA16C0` | 763 | UnwindData |  |
| 897 | `GetVolumeInformationW` | `0xA19D0` | 169 | UnwindData |  |
| 896 | `GetVolumeInformationByHandleW` | `0xA1D50` | 805 | UnwindData |  |
| 605 | `GetFileInformationByHandle` | `0xA2080` | 128 | UnwindData |  |
| 1321 | `PerfIncrementULongLongCounterValue` | `0xA45B0` | 213 | UnwindData |  |
| 1319 | `PerfDeleteInstance` | `0xA4690` | 133 | UnwindData |  |
| 1316 | `PerfCreateInstance` | `0xA47B0` | 207 | UnwindData |  |
| 1323 | `PerfSetCounterRefValue` | `0xA4890` | 211 | UnwindData |  |
| 1325 | `PerfSetULongCounterValue` | `0xA4970` | 234 | UnwindData |  |
| 1317 | `PerfDecrementULongCounterValue` | `0xA4A60` | 247 | UnwindData |  |
| 1296 | `PcwAddQueryItem` | `0xA4FB0` | 153 | UnwindData |  |
| 1312 | `PcwSetQueryItemUserData` | `0xA5050` | 73 | UnwindData |  |
| 1303 | `PcwEnumerateInstances` | `0xA50A0` | 106 | UnwindData |  |
| 1310 | `PcwSendStatelessNotification` | `0xA5110` | 133 | UnwindData |  |
| 1309 | `PcwSendNotification` | `0xA51A0` | 115 | UnwindData |  |
| 1299 | `PcwCompleteNotification` | `0xA5220` | 84 | UnwindData |  |
| 1324 | `PerfSetCounterSetInfo` | `0xA54D0` | 158 | UnwindData |  |
| 1301 | `PcwCreateQuery` | `0xA5580` | 61 | UnwindData |  |
| 1306 | `PcwReadNotificationData` | `0xA5810` | 48 | UnwindData |  |
| 1328 | `PerfStartProviderEx` | `0xA5850` | 158 | UnwindData |  |
| 1318 | `PerfDecrementULongLongCounterValue` | `0xA5BF0` | 207 | UnwindData |  |
| 1302 | `PcwDisconnectCounterSet` | `0xA5D90` | 65 | UnwindData |  |
| 1326 | `PerfSetULongLongCounterValue` | `0xA6210` | 362 | UnwindData |  |
| 1307 | `PcwRegisterCounterSet` | `0xA68C0` | 90 | UnwindData |  |
| 1329 | `PerfStopProvider` | `0xA69F0` | 82 | UnwindData |  |
| 1300 | `PcwCreateNotifier` | `0xA6A50` | 87 | UnwindData |  |
| 1308 | `PcwRemoveQueryItem` | `0xA6AB0` | 69 | UnwindData |  |
| 1327 | `PerfStartProvider` | `0xA6B00` | 50 | UnwindData |  |
| 1320 | `PerfIncrementULongCounterValue` | `0xA6B40` | 364 | UnwindData |  |
| 1100 | `LogStagedFeatureUsage` | `0xA6D70` | 134 | UnwindData |  |
| 732 | `GetPackagedDataForFile` | `0xA6E80` | 248 | UnwindData |  |
| 75 | `AppXPreCreationExtension` | `0xA7100` | 679 | UnwindData |  |
| 1728 | `SharedLocalIsEnabled` | `0xA78D0` | 129 | UnwindData |  |
| 16 | `AddAccessAllowedAceEx` | `0xA7DB0` | 75 | UnwindData |  |
| 1092 | `LocalSystemTimeToLocalFileTime` | `0xA7E10` | 157 | UnwindData |  |
| 1833 | `TryCreatePackageDependency` | `0xA7EC0` | 109 | UnwindData |  |
| 1834 | `TryCreatePackageDependency2` | `0xA7F40` | 429 | UnwindData |  |
| 1086 | `LocalFileTimeToLocalSystemTime` | `0xA8560` | 136 | UnwindData |  |
| 1685 | `SetSecurityDescriptorOwner` | `0xA85F0` | 42 | UnwindData |  |
| 1684 | `SetSecurityDescriptorGroup` | `0xA8620` | 42 | UnwindData |  |
| 371 | `EqualDomainSid` | `0xA8DF0` | 498 | UnwindData |  |
| 269 | `CreateWellKnownSid` | `0xA8FF0` | 874 | UnwindData |  |
| 373 | `EqualSid` | `0xA9360` | 63 | UnwindData |  |
| 901 | `GetWindowsAccountDomainSid` | `0xA93B0` | 348 | UnwindData |  |
| 1683 | `SetSecurityDescriptorDacl` | `0xA9520` | 42 | UnwindData |  |
| 958 | `InitializeSecurityDescriptor` | `0xA9550` | 42 | UnwindData |  |
| 946 | `InitializeAcl` | `0xA9580` | 42 | UnwindData |  |
| 976 | `InternetTimeFromSystemTimeA` | `0xA99F0` | 327 | UnwindData |  |
| 869 | `GetTimeFormatA` | `0xA9B40` | 340 | UnwindData |  |
| 1808 | `SystemTimeToTzSpecificLocalTimeEx` | `0xA9D70` | 733 | UnwindData |  |
| 1837 | `TzSpecificLocalTimeToSystemTime` | `0xAA190` | 750 | UnwindData |  |
| 577 | `GetDynamicTimeZoneInformation` | `0xAA490` | 539 | UnwindData |  |
| 1807 | `SystemTimeToTzSpecificLocalTime` | `0xAA6C0` | 384 | UnwindData |  |
| 645 | `GetLocalTime` | `0xAB590` | 373 | UnwindData |  |
| 873 | `GetTimeZoneInformationForYear` | `0xACC10` | 171 | UnwindData |  |
| 1588 | `SetClientDynamicTimeZoneInformation` | `0xACDE0` | 97 | UnwindData |  |
| 342 | `EnumDynamicTimeZoneInformation` | `0xAD0D0` | 153 | UnwindData |  |
| 831 | `GetSystemTime` | `0xAD5D0` | 158 | UnwindData |  |
| 1063 | `LCIDToLocaleName` | `0xAD730` | 374 | UnwindData |  |
| 136 | `CharPrevExA` | `0xADE90` | 118 | UnwindData |  |
| 133 | `CharNextExA` | `0xADF10` | 56 | UnwindData |  |
| 998 | `IsDBCSLeadByteEx` | `0xADF50` | 266 | UnwindData |  |
| 426 | `FindStringOrdinal` | `0xAECD0` | 1,700 | UnwindData |  |
| 1202 | `PathCchAddBackslashEx` | `0xAF3E0` | 68 | UnwindData |  |
| 1361 | `PssWalkSnapshot` | `0xAF640` | 745 | UnwindData |  |
| 1266 | `PathMatchSpecExW` | `0xAFC80` | 37 | UnwindData |  |
| 1267 | `PathMatchSpecW` | `0xAFDF0` | 290 | UnwindData |  |
| 1232 | `PathFindFileNameW` | `0xB03F0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1987 | `WriteFile` | `0xB04A0` | 491 | UnwindData |  |
| 430 | `FlsGetValue` | `0xB06A0` | 100 | UnwindData |  |
| 1203 | `PathCchAddExtension` | `0xB0710` | 348 | UnwindData |  |
| 1210 | `PathCchFindExtension` | `0xB0880` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1806 | `SystemTimeToFileTime` | `0xB09A0` | 189 | UnwindData |  |
| 944 | `InitOnceExecuteOnce` | `0xB1640` | 53 | UnwindData |  |
| 432 | `FlsSetValue` | `0xB1680` | 42 | UnwindData |  |
| 415 | `FindNLSStringEx` | `0xB16B0` | 436 | UnwindData |  |
| 1118 | `MulDiv` | `0xB1870` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 857 | `GetThreadIdealProcessorEx` | `0xB18E0` | 84 | UnwindData |  |
| 1380 | `QueryMemoryResourceNotification` | `0xB1940` | 124 | UnwindData |  |
| 1805 | `SwitchToThread` | `0xB1A50` | 49 | UnwindData |  |
| 395 | `FileTimeToSystemTime` | `0xB1A90` | 213 | UnwindData |  |
| 867 | `GetTickCount` | `0xB1B70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1129 | `NlsUpdateLocale` | `0xB1B90` | 433 | UnwindData |  |
| 1754 | `StrCmpICW` | `0xB2230` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `CharUpperW` | `0xB2280` | 96 | UnwindData |  |
| 835 | `GetSystemTimePreciseAsFileTime` | `0xB2370` | 37 | UnwindData |  |
| 1724 | `SetWaitableTimer` | `0xB2570` | 367 | UnwindData |  |
| 1725 | `SetWaitableTimerEx` | `0xB26F0` | 322 | UnwindData |  |
| 667 | `GetModuleFileNameW` | `0xB2AF0` | 53 | UnwindData |  |
| 1016 | `IsThreadAFiber` | `0xB2BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1392 | `QueryThreadCycleTime` | `0xB2BE0` | 116 | UnwindData |  |
| 1774 | `StrPBrkW` | `0xB2D40` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 868 | `GetTickCount64` | `0xB2D90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1257 | `PathIsUNCServerShareW` | `0xB2DC0` | 266 | UnwindData |  |
| 1258 | `PathIsUNCServerW` | `0xB2ED0` | 230 | UnwindData |  |
| 1750 | `StrChrW` | `0xB2FC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 309 | `DiscardVirtualMemory` | `0xB2FF0` | 217 | UnwindData |  |
| 743 | `GetProcAddressForCaller` | `0xB3370` | 11 | UnwindData |  |
| 171 | `CommandLineToArgvW` | `0xB34C0` | 417 | UnwindData |  |
| 834 | `GetSystemTimeAsFileTime` | `0xB3930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 359 | `EnumSystemGeoID` | `0xB3950` | 51 | UnwindData |  |
| 1344 | `PsmGetAumidFromKey` | `0xB3A30` | 213 | UnwindData |  |
| 1348 | `PsmGetPackageFullNameFromKey` | `0xB3B10` | 202 | UnwindData |  |
| 1343 | `PsmGetApplicationNameFromKey` | `0xB3BE0` | 225 | UnwindData |  |
| 643 | `GetLastError` | `0xB3F40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1630 | `SetEvent` | `0xB3F50` | 44 | UnwindData |  |
| 1263 | `PathIsValidCharW` | `0xB3F90` | 1,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 442 | `FormatMessageA` | `0xB4490` | 648 | UnwindData |  |
| 443 | `FormatMessageW` | `0xB4720` | 61 | UnwindData |  |
| 1090 | `LocalReAlloc` | `0xB4D80` | 718 | UnwindData |  |
| 748 | `GetProcessHeap` | `0xB5100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1909 | `VirtualAlloc` | `0xB5120` | 118 | UnwindData |  |
| 1752 | `StrCmpCW` | `0xB51A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 662 | `GetModuleBaseNameA` | `0xB51E0` | 167 | UnwindData |  |
| 1047 | `K32GetModuleBaseNameA` | `0xB51E0` | 167 | UnwindData |  |
| 663 | `GetModuleBaseNameW` | `0xB5290` | 663 | UnwindData |  |
| 1048 | `K32GetModuleBaseNameW` | `0xB5290` | 663 | UnwindData |  |
| 665 | `GetModuleFileNameExA` | `0xB5530` | 171 | UnwindData |  |
| 1049 | `K32GetModuleFileNameExA` | `0xB5530` | 171 | UnwindData |  |
| 666 | `GetModuleFileNameExW` | `0xB55F0` | 52 | UnwindData |  |
| 1050 | `K32GetModuleFileNameExW` | `0xB55F0` | 52 | UnwindData |  |
| 672 | `GetModuleInformation` | `0xB5A60` | 803 | UnwindData |  |
| 1051 | `K32GetModuleInformation` | `0xB5A60` | 803 | UnwindData |  |
| 1432 | `ReadProcessMemory` | `0xB60C0` | 83 | UnwindData |  |
| 1919 | `VirtualProtectEx` | `0xB6660` | 186 | UnwindData |  |
| 134 | `CharNextW` | `0xB6720` | 149 | UnwindData |  |
| 1913 | `VirtualAllocExNuma` | `0xB6B60` | 142 | UnwindData |  |
| 104 | `BasepAdjustObjectAttributesForPrivateNamespace` | `0xB6C40` | 72 | UnwindData |  |
| 858 | `GetThreadInformation` | `0xB6D80` | 207 | UnwindData |  |
| 597 | `GetFallbackDisplayName` | `0xB6ED0` | 63 | UnwindData |  |
| 1703 | `SetThreadPreferredUILanguages` | `0xB6F20` | 135 | UnwindData |  |
| 1704 | `SetThreadPreferredUILanguages2` | `0xB6FB0` | 157 | UnwindData |  |
| 1711 | `SetThreadUILanguage` | `0xB70F0` | 357 | UnwindData |  |
| 866 | `GetThreadUILanguage` | `0xB7260` | 38 | UnwindData |  |
| 885 | `GetUserDefaultUILanguage` | `0xB7540` | 67 | UnwindData |  |
| 520 | `GetConsoleOutputCP` | `0xB7720` | 311 | UnwindData |  |
| 347 | `EnumProcessModulesEx` | `0xB7860` | 382 | UnwindData |  |
| 1039 | `K32EnumProcessModulesEx` | `0xB7860` | 382 | UnwindData |  |
| 346 | `EnumProcessModules` | `0xB7D80` | 23 | UnwindData |  |
| 1038 | `K32EnumProcessModules` | `0xB7D80` | 23 | UnwindData |  |
| 1825 | `TlsSetValue` | `0xB8060` | 42 | UnwindData |  |
| 738 | `GetPhysicallyInstalledSystemMemory` | `0xB80C0` | 1,144 | UnwindData |  |
| 913 | `GlobalMemoryStatusEx` | `0xB8540` | 157 | UnwindData |  |
| 823 | `GetSystemFirmwareTable` | `0xB8820` | 307 | UnwindData |  |
| 1915 | `VirtualFree` | `0xB8960` | 202 | UnwindData |  |
| 1780 | `StrRStrIW` | `0xB8A30` | 252 | UnwindData |  |
| 1395 | `QueryUnbiasedInterruptTimePrecise` | `0xB8C30` | 83 | UnwindData |  |
| 1330 | `PoolPerAppKeyStateInternal` | `0xB8C90` | 32 | UnwindData |  |
| 592 | `GetExitCodeThread` | `0xB8D20` | 94 | UnwindData |  |
| 1536 | `ResetEvent` | `0xB8DF0` | 42 | UnwindData |  |
| 1912 | `VirtualAllocEx` | `0xB8E20` | 117 | UnwindData |  |
| 1110 | `MapViewOfFileEx` | `0xB8EA0` | 435 | UnwindData |  |
| 919 | `HashData` | `0xB90C0` | 64 | UnwindData |  |
| 1729 | `SignalObjectAndWait` | `0xB98F0` | 356 | UnwindData |  |
| 1796 | `StrTrimW` | `0xB9DF0` | 37 | UnwindData |  |
| 1315 | `PeekNamedPipe` | `0xB9F00` | 562 | UnwindData |  |
| 1332 | `PostQueuedCompletionStatus` | `0xBA140` | 64 | UnwindData |  |
| 1265 | `PathMatchSpecExA` | `0xBA2F0` | 37 | UnwindData |  |
| 982 | `IsCharAlphaA` | `0xBA320` | 234 | UnwindData |  |
| 983 | `IsCharAlphaNumericA` | `0xBA5C0` | 239 | UnwindData |  |
| 138 | `CharUpperA` | `0xBA6C0` | 251 | UnwindData |  |
| 139 | `CharUpperBuffA` | `0xBA810` | 351 | UnwindData |  |
| 1769 | `StrDupA` | `0xBA980` | 102 | UnwindData |  |
| 1741 | `StrCatBuffA` | `0xBA9F0` | 43 | UnwindData |  |
| 399 | `FindActCtxSectionGuid` | `0xBAB00` | 109 | UnwindData |  |
| 1582 | `ScrollConsoleScreenBufferW` | `0xBB7C0` | 30 | UnwindData |  |
| 1601 | `SetConsoleCP` | `0xBB8C0` | 108 | UnwindData |  |
| 533 | `GetCurrentConsoleFontEx` | `0xBB940` | 198 | UnwindData |  |
| 642 | `GetLargestConsoleWindowSize` | `0xBBA10` | 107 | UnwindData |  |
| 524 | `GetConsoleSelectionInfo` | `0xBBA90` | 112 | UnwindData |  |
| 1612 | `SetConsoleOutputCP` | `0xBBB10` | 118 | UnwindData |  |
| 1603 | `SetConsoleCursorInfo` | `0xBBB90` | 134 | UnwindData |  |
| 511 | `GetConsoleCursorInfo` | `0xBBC20` | 135 | UnwindData |  |
| 466 | `GetAppContainerNamedObjectPath` | `0xBBCB0` | 255 | UnwindData |  |
| 527 | `GetConsoleWindow` | `0xBBDC0` | 97 | UnwindData |  |
| 506 | `GetConsoleCP` | `0xBBE30` | 87 | UnwindData |  |
| 1620 | `SetCurrentConsoleFontEx` | `0xBBE90` | 198 | UnwindData |  |
| 1604 | `SetConsoleCursorPosition` | `0xBBFD0` | 124 | UnwindData |  |
| 1609 | `SetConsoleMode` | `0xBC060` | 91 | UnwindData |  |
| 1615 | `SetConsoleTextAttribute` | `0xBC0D0` | 124 | UnwindData |  |
| 522 | `GetConsoleScreenBufferInfo` | `0xBC160` | 116 | UnwindData |  |
| 523 | `GetConsoleScreenBufferInfoEx` | `0xBC1E0` | 298 | UnwindData |  |
| 87 | `AttachConsole` | `0xBC430` | 151 | UnwindData |  |
| 414 | `FindNLSString` | `0xBDE40` | 569 | UnwindData |  |
| 1933 | `WaitForSingleObject` | `0xBE080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 912 | `GlobalLock` | `0xBE090` | 304 | UnwindData |  |
| 916 | `GlobalUnlock` | `0xBE250` | 195 | UnwindData |  |
| 1761 | `StrCmpNICA` | `0xBE320` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1337 | `ProcessIdToSessionId` | `0xBE410` | 355 | UnwindData |  |
| 755 | `GetProcessMemoryInfo` | `0xBE580` | 369 | UnwindData |  |
| 1055 | `K32GetProcessMemoryInfo` | `0xBE580` | 369 | UnwindData |  |
| 1918 | `VirtualProtect` | `0xBE700` | 179 | UnwindData |  |
| 836 | `GetSystemTimes` | `0xBE7C0` | 1,035 | UnwindData |  |
| 865 | `GetThreadTimes` | `0xBEBE0` | 167 | UnwindData |  |
| 1842 | `UnmapViewOfFile` | `0xBEC90` | 127 | UnwindData |  |
| 774 | `GetQueuedCompletionStatusEx` | `0xBED20` | 403 | UnwindData |  |
| 544 | `GetCurrentPackageInfo2` | `0xBEEC0` | 63 | UnwindData |  |
| 543 | `GetCurrentPackageInfo` | `0xBEF10` | 66 | UnwindData |  |
| 545 | `GetCurrentPackageInfo3` | `0xBEF60` | 972 | UnwindData |  |
| 1731 | `Sleep` | `0xBF340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1018 | `IsTimeZoneRedirectionEnabled` | `0xBF350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1190 | `ParseURLW` | `0xBF370` | 41 | UnwindData |  |
| 173 | `CompareFileTime` | `0xBF570` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `AccessCheckByType` | `0xBF5B0` | 186 | UnwindData |  |
| 1214 | `PathCchRemoveExtension` | `0xBF670` | 228 | UnwindData |  |
| 4 | `AccessCheck` | `0xBF760` | 154 | UnwindData |  |
| 528 | `GetCurrencyFormatEx` | `0xBF800` | 127 | UnwindData |  |
| 687 | `GetNumberFormatW` | `0xC0500` | 135 | UnwindData |  |
| 686 | `GetNumberFormatEx` | `0xC0590` | 129 | UnwindData |  |
| 261 | `CreateThreadpoolIo` | `0xC1440` | 546 | UnwindData |  |
| 1167 | `OutputDebugStringW` | `0xC1670` | 270 | UnwindData |  |
| 1166 | `OutputDebugStringA` | `0xC1790` | 833 | UnwindData |  |
| 1413 | `RaiseException` | `0xC1AE0` | 178 | UnwindData |  |
| 1089 | `LocalLock` | `0xC1BA0` | 267 | UnwindData |  |
| 1025 | `IsValidLocaleName` | `0xC1CC0` | 170 | UnwindData |  |
| 1701 | `SetThreadInformation` | `0xC1F20` | 206 | UnwindData |  |
| 610 | `GetFileSecurityW` | `0xC2000` | 184 | UnwindData |  |
| 893 | `GetVersionExA` | `0xC2310` | 352 | UnwindData |  |
| 894 | `GetVersionExW` | `0xC2480` | 224 | UnwindData |  |
| 1404 | `QuirkIsEnabled` | `0xC2570` | 47 | UnwindData |  |
| 1029 | `IsValidSid` | `0xC28F0` | 56 | UnwindData |  |
| 1112 | `MapViewOfFileFromApp` | `0xC2930` | 205 | UnwindData |  |
| 841 | `GetSystemWow64DirectoryA` | `0xC2A10` | 44 | UnwindData |  |
| 842 | `GetSystemWow64DirectoryW` | `0xC2A50` | 44 | UnwindData |  |
| 1976 | `Wow64SetThreadDefaultGuestMachine` | `0xC2A90` | 83 | UnwindData |  |
| 952 | `InitializeCriticalSectionEx` | `0xC2D70` | 42 | UnwindData |  |
| 1841 | `UnlockFileEx` | `0xC2DA0` | 112 | UnwindData |  |
| 1373 | `QueryFullProcessImageNameW` | `0xC2E20` | 97 | UnwindData |  |
| 412 | `FindFirstStreamW` | `0xC2FA0` | 888 | UnwindData |  |
| 409 | `FindFirstFileNameW` | `0xC3320` | 1,078 | UnwindData |  |
| 418 | `FindNextFileNameW` | `0xC3820` | 406 | UnwindData |  |
| 614 | `GetFileType` | `0xC3C30` | 350 | UnwindData |  |
| 270 | `CtrlRoutine` | `0xC3DA0` | 596 | UnwindData |  |
| 1705 | `SetThreadPriority` | `0xC4000` | 170 | UnwindData |  |
| 494 | `GetComputerNameExA` | `0xC4690` | 286 | UnwindData |  |
| 495 | `GetComputerNameExW` | `0xC47C0` | 60 | UnwindData |  |
| 388 | `ExpandEnvironmentStringsW` | `0xC54B0` | 155 | UnwindData |  |
| 1094 | `LocaleNameToLCID` | `0xC5560` | 123 | UnwindData |  |
| 140 | `CharUpperBuffW` | `0xC5F10` | 101 | UnwindData |  |
| 1844 | `UnmapViewOfFileEx` | `0xC5FA0` | 163 | UnwindData |  |
| 951 | `InitializeCriticalSectionAndSpinCount` | `0xC6050` | 27 | UnwindData |  |
| 914 | `GlobalReAlloc` | `0xC6080` | 1,079 | UnwindData |  |
| 760 | `GetProcessTimes` | `0xC64C0` | 167 | UnwindData |  |
| 620 | `GetFileVersionInfoSizeExA` | `0xC6860` | 135 | UnwindData |  |
| 619 | `GetFileVersionInfoSizeA` | `0xC6980` | 131 | UnwindData |  |
| 621 | `GetFileVersionInfoSizeExW` | `0xC6A10` | 633 | UnwindData |  |
| 612 | `GetFileSizeEx` | `0xC6F90` | 147 | UnwindData |  |
| 993 | `IsCharSpaceW` | `0xC7110` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1760 | `StrCmpNIA` | `0xC7190` | 128 | UnwindData |  |
| 1254 | `PathIsUNCEx` | `0xC7220` | 207 | UnwindData |  |
| 1794 | `StrToIntW` | `0xC7300` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 911 | `GlobalHandle` | `0xC7360` | 192 | UnwindData |  |
| 128 | `CharLowerA` | `0xC7430` | 31 | UnwindData |  |
| 129 | `CharLowerBuffA` | `0xC75A0` | 398 | UnwindData |  |
| 267 | `CreateWaitableTimerExW` | `0xC7740` | 371 | UnwindData |  |
| 1093 | `LocalUnlock` | `0xC78C0` | 218 | UnwindData |  |
| 861 | `GetThreadPriority` | `0xC79A0` | 115 | UnwindData |  |
| 783 | `GetSecurityDescriptorDacl` | `0xC7AB0` | 104 | UnwindData |  |
| 387 | `ExpandEnvironmentStringsA` | `0xC7B20` | 605 | UnwindData |  |
| 248 | `CreateRemoteThreadEx` | `0xC7D90` | 2,091 | UnwindData |  |
| 1273 | `PathRelativePathToW` | `0xC9640` | 607 | UnwindData |  |
| 1234 | `PathFindNextComponentW` | `0xC98B0` | 91 | UnwindData |  |
| 1252 | `PathIsSameRootW` | `0xC9920` | 116 | UnwindData |  |
| 1246 | `PathIsPrefixW` | `0xC99A0` | 86 | UnwindData |  |
| 1223 | `PathCommonPrefixW` | `0xC9A00` | 74 | UnwindData |  |
| 1289 | `PathStripPathW` | `0xC9DC0` | 320 | UnwindData |  |
| 1279 | `PathRemoveExtensionW` | `0xC9F10` | 152 | UnwindData |  |
| 1753 | `StrCmpICA` | `0xC9FB0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1430 | `ReadFileEx` | `0xCA000` | 489 | UnwindData |  |
| 1427 | `ReadDirectoryChangesExW` | `0xCA1F0` | 534 | UnwindData |  |
| 1428 | `ReadDirectoryChangesW` | `0xCA410` | 466 | UnwindData |  |
| 1988 | `WriteFileEx` | `0xCA5F0` | 260 | UnwindData |  |
| 1399 | `QueueUserAPC` | `0xCA8F0` | 231 | UnwindData |  |
| 5 | `AccessCheckAndAuditAlarmW` | `0xCA9E0` | 323 | UnwindData |  |
| 536 | `GetCurrentPackageApplicationContext` | `0xCAC40` | 150 | UnwindData |  |
| 548 | `GetCurrentPackagePath2` | `0xCB170` | 408 | UnwindData |  |
| 718 | `GetPackagePathByFullName` | `0xCB8E0` | 77 | UnwindData |  |
| 719 | `GetPackagePathByFullName2` | `0xCBD00` | 78 | UnwindData |  |
| 798 | `GetStagedPackagePathByFullName` | `0xCBD60` | 79 | UnwindData |  |
| 799 | `GetStagedPackagePathByFullName2` | `0xCBDC0` | 87 | UnwindData |  |
| 54 | `AppContainerRegisterSid` | `0xCD860` | 480 | UnwindData |  |
| 1819 | `TestReport` | `0xCDCD0` | 39 | UnwindData |  |
| 668 | `GetModuleHandleA` | `0xCE640` | 92 | UnwindData |  |
| 45 | `AllocateAndInitializeSid` | `0xCE7B0` | 121 | UnwindData |  |
| 125 | `CancelWaitableTimer` | `0xCE830` | 48 | UnwindData |  |
| 1922 | `VirtualQueryEx` | `0xCE870` | 72 | UnwindData |  |
| 1921 | `VirtualQuery` | `0xCEFD0` | 79 | UnwindData |  |
| 189 | `CopyFile2` | `0xCF030` | 584 | UnwindData |  |
| 1334 | `PrivCopyFileExW` | `0xCF280` | 1,150 | UnwindData |  |
| 192 | `CopyFileW` | `0xCF710` | 69 | UnwindData |  |
| 190 | `CopyFileExW` | `0xCF760` | 341 | UnwindData |  |
| 106 | `BasepCopyFileExW` | `0xCF8C0` | 9,147 | UnwindData |  |
| 105 | `BasepCopyFileCallback` | `0xD29A0` | 176 | UnwindData |  |
| 101 | `BaseMarkFileForDelete` | `0xD2C00` | 231 | UnwindData |  |
| 1535 | `ReplaceFileW` | `0xD3120` | 75 | UnwindData |  |
| 1533 | `ReplaceFileExInternal` | `0xD3180` | 6,272 | UnwindData |  |
| 291 | `DeleteFileW` | `0xD5740` | 47 | UnwindData |  |
| 107 | `BasepNotifyTrackingService` | `0xD5AF0` | 843 | UnwindData |  |
| 1400 | `QueueUserAPC2` | `0xDCF90` | 78 | UnwindData |  |
| 326 | `DuplicateTokenEx` | `0xDD0C0` | 214 | UnwindData |  |
| 130 | `CharLowerBuffW` | `0xDD1A0` | 101 | UnwindData |  |
| 148 | `CheckTokenMembership` | `0xDD230` | 98 | UnwindData |  |
| 680 | `GetNativeSystemInfo` | `0xDD2A0` | 197 | UnwindData |  |
| 120 | `CallbackMayRunLong` | `0xDD520` | 49 | UnwindData |  |
| 1345 | `PsmGetDynamicIdFromKey` | `0xDD560` | 137 | UnwindData |  |
| 1351 | `PsmIsValidKey` | `0xDD5F0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 586 | `GetEnvironmentStringsW` | `0xDD690` | 218 | UnwindData |  |
| 264 | `CreateThreadpoolWork` | `0xDD770` | 72 | UnwindData |  |
| 1201 | `PathCchAddBackslash` | `0xDD7C0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1485 | `RegOpenUserClassesRoot` | `0xDD900` | 660 | UnwindData |  |
| 664 | `GetModuleFileNameA` | `0xDDBA0` | 552 | UnwindData |  |
| 1546 | `RevertToSelf` | `0xDDDD0` | 73 | UnwindData |  |
| 1163 | `OpenThread` | `0xDDE20` | 120 | UnwindData |  |
| 1240 | `PathGetDriveNumberW` | `0xDDEA0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 272 | `DeactivateActCtx` | `0xDDF10` | 60 | UnwindData |  |
| 591 | `GetExitCodeProcess` | `0xDDF60` | 94 | UnwindData |  |
| 14 | `ActivateActCtx` | `0xDDFD0` | 81 | UnwindData |  |
| 1242 | `PathIsFileSpecW` | `0xDE030` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 394 | `FileTimeToLocalFileTime` | `0xDE060` | 183 | UnwindData |  |
| 1269 | `PathParseIconLocationW` | `0xDE120` | 214 | UnwindData |  |
| 1277 | `PathRemoveBlanksW` | `0xDE200` | 10 | UnwindData |  |
| 1295 | `PathUnquoteSpacesW` | `0xDE2F0` | 88 | UnwindData |  |
| 185 | `ConvertThreadToFiber` | `0xDE350` | 308 | UnwindData |  |
| 1787 | `StrStrNW` | `0xDE490` | 158 | UnwindData |  |
| 1749 | `StrChrNW` | `0xDE540` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1697 | `SetThreadErrorMode` | `0xDE580` | 181 | UnwindData |  |
| 650 | `GetLogicalDriveStringsW` | `0xDE640` | 249 | UnwindData |  |
| 651 | `GetLogicalDrives` | `0xDE740` | 106 | UnwindData |  |
| 588 | `GetEnvironmentVariableW` | `0xDE7B0` | 155 | UnwindData |  |
| 1941 | `WaitOnAddress` | `0xDE860` | 125 | UnwindData |  |
| 1820 | `TestUnlockData` | `0xDE8F0` | 90 | UnwindData |  |
| 1121 | `NamedPipeEventSelect` | `0xDEE10` | 254 | UnwindData |  |
| 1120 | `NamedPipeEventEnum` | `0xDEF20` | 249 | UnwindData |  |
| 677 | `GetNamedPipeClientComputerNameW` | `0xDF020` | 286 | UnwindData |  |
| 676 | `GetNamedPipeAttribute` | `0xDF150` | 332 | UnwindData |  |
| 821 | `GetSystemDirectoryW` | `0xDF300` | 81 | UnwindData |  |
| 1730 | `SizeofResource` | `0xDF360` | 120 | UnwindData |  |
| 1127 | `NlsGetCacheUpdateCount` | `0xDF3E0` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1851 | `UnregisterWaitEx` | `0xDF7C0` | 87 | UnwindData |  |
| 1426 | `ReadConsoleW` | `0xDF8B0` | 81 | UnwindData |  |
| 1355 | `PssQuerySnapshot` | `0xDFD00` | 776 | UnwindData |  |
| 587 | `GetEnvironmentVariableA` | `0xE0010` | 13 | UnwindData |  |
| 1778 | `StrRChrW` | `0xE0210` | 90 | UnwindData |  |
| 1759 | `StrCmpNCW` | `0xE0270` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 859 | `GetThreadLocale` | `0xE0380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 740 | `GetPriorityClass` | `0xE03A0` | 188 | UnwindData |  |
| 1740 | `StrCSpnW` | `0xE0470` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 938 | `ImpersonateLoggedOnUser` | `0xE04C0` | 386 | UnwindData |  |
| 658 | `GetMappedFileNameW` | `0xE0650` | 136 | UnwindData |  |
| 1046 | `K32GetMappedFileNameW` | `0xE0650` | 136 | UnwindData |  |
| 1364 | `PulseEvent` | `0xE0770` | 44 | UnwindData |  |
| 1462 | `RegGetKeySecurity` | `0xE07B0` | 631 | UnwindData |  |
| 400 | `FindActCtxSectionStringW` | `0xE0CF0` | 109 | UnwindData |  |
| 617 | `GetFileVersionInfoExA` | `0xE0D70` | 163 | UnwindData |  |
| 615 | `GetFileVersionInfoA` | `0xE0E20` | 161 | UnwindData |  |
| 623 | `GetFileVersionInfoW` | `0xE0ED0` | 34 | UnwindData |  |
| 618 | `GetFileVersionInfoExW` | `0xE0F00` | 782 | UnwindData |  |
| 1548 | `SHCoCreateInstance` | `0xE16B0` | 104 | UnwindData |  |
| 1968 | `WilFailureWatcherSubscribe` | `0xE1720` | 78 | UnwindData |  |
| 186 | `ConvertThreadToFiberEx` | `0xE1960` | 21 | UnwindData |  |
| 669 | `GetModuleHandleExA` | `0xE1AC0` | 486 | UnwindData |  |
| 1467 | `RegKrnGetClassesEnumTableAddressInternal` | `0xE1EB0` | 49 | UnwindData |  |
| 872 | `GetTimeZoneInformation` | `0xE1EF0` | 475 | UnwindData |  |
| 1335 | `PrivilegeCheck` | `0xE21A0` | 65 | UnwindData |  |
| 794 | `GetSidSubAuthority` | `0xE2270` | 56 | UnwindData |  |
| 435 | `FlushInstructionCache` | `0xE23C0` | 91 | UnwindData |  |
| 1132 | `NormalizeString` | `0xE2460` | 146 | UnwindData |  |
| 1019 | `IsTokenRestricted` | `0xE2500` | 63 | UnwindData |  |
| 934 | `IdnToAscii` | `0xE27D0` | 117 | UnwindData |  |
| 21 | `AddAce` | `0xE2850` | 50 | UnwindData |  |
| 1489 | `RegQueryMultipleValuesW` | `0xE2890` | 972 | UnwindData |  |
| 1550 | `SHExpandEnvironmentStringsW` | `0xE2DB0` | 218 | UnwindData |  |
| 1248 | `PathIsRelativeW` | `0xE2E90` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `CheckTokenCapability` | `0xE2EF0` | 95 | UnwindData |  |
| 1450 | `RegDeleteKeyValueA` | `0xE2F60` | 94 | UnwindData |  |
| 1454 | `RegDeleteValueA` | `0xE2FD0` | 247 | UnwindData |  |
| 1061 | `KernelBaseGetGlobalData` | `0xE3270` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1000 | `IsDeveloperModeEnabled` | `0xE3440` | 164 | UnwindData |  |
| 1001 | `IsDeveloperModePolicyApplied` | `0xE3B50` | 128 | UnwindData |  |
| 737 | `GetPersistedRegistryValueW` | `0xE3BE0` | 505 | UnwindData |  |
| 613 | `GetFileTime` | `0xE3DE0` | 175 | UnwindData |  |
| 754 | `GetProcessInformation` | `0xE3EF0` | 484 | UnwindData |  |
| 851 | `GetThreadDescription` | `0xE4370` | 294 | UnwindData |  |
| 1091 | `LocalSize` | `0xE4600` | 365 | UnwindData |  |
| 1804 | `SwitchToFiber` | `0xE4950` | 60 | UnwindData |  |
| 1145 | `OpenFileById` | `0xE49A0` | 482 | UnwindData |  |
| 1406 | `QuirkIsEnabled3` | `0xE4B90` | 57 | UnwindData |  |
| 70 | `AppXGetPackageCapabilities` | `0xE4BD0` | 595 | UnwindData |  |
| 915 | `GlobalSize` | `0xE5220` | 370 | UnwindData |  |
| 1388 | `QuerySecurityAccessMask` | `0xE53E0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2022 | `hgets` | `0xE5450` | 454 | UnwindData |  |
| 900 | `GetVolumePathNamesForVolumeNameW` | `0xE56A0` | 1,202 | UnwindData |  |
| 1357 | `PssWalkMarkerFree` | `0xE5B60` | 86 | UnwindData |  |
| 1360 | `PssWalkMarkerSetPosition` | `0xE5BC0` | 64 | UnwindData |  |
| 1358 | `PssWalkMarkerGetPosition` | `0xE5C10` | 67 | UnwindData |  |
| 1359 | `PssWalkMarkerSeekToBeginning` | `0xE5C60` | 56 | UnwindData |  |
| 461 | `GetAclInformation` | `0xE5DB0` | 42 | UnwindData |  |
| 1583 | `SearchPathA` | `0xE5DE0` | 772 | UnwindData |  |
| 1285 | `PathSearchAndQualifyW` | `0xE60F0` | 230 | UnwindData |  |
| 1584 | `SearchPathW` | `0xE61E0` | 572 | UnwindData |  |
| 1075 | `LoadLibraryExA` | `0xE6430` | 178 | UnwindData |  |
| 1346 | `PsmGetKeyFromProcess` | `0xE6560` | 116 | UnwindData |  |
| 1347 | `PsmGetKeyFromToken` | `0xE65E0` | 407 | UnwindData |  |
| 1339 | `PsmCreateKey` | `0xE6780` | 148 | UnwindData |  |
| 753 | `GetProcessImageFileNameW` | `0xE6A40` | 204 | UnwindData |  |
| 1054 | `K32GetProcessImageFileNameW` | `0xE6A40` | 204 | UnwindData |  |
| 1028 | `IsValidSecurityDescriptor` | `0xE71E0` | 45 | UnwindData |  |
| 1011 | `IsProcessInJob` | `0xE7220` | 97 | UnwindData |  |
| 792 | `GetSidIdentifierAuthority` | `0xE7390` | 43 | UnwindData |  |
| 751 | `GetProcessIdOfThread` | `0xE73D0` | 81 | UnwindData |  |
| 1033 | `IsWow64Process2` | `0xE7530` | 42 | UnwindData |  |
| 1372 | `QueryFullProcessImageNameA` | `0xE7560` | 536 | UnwindData |  |
| 1192 | `PathAddBackslashW` | `0xE7780` | 229 | UnwindData |  |
| 1696 | `SetThreadDescription` | `0xE7870` | 79 | UnwindData |  |
| 904 | `GetWriteWatch` | `0xE7920` | 77 | UnwindData |  |
| 162 | `CloseStateContainer` | `0xE7980` | 143 | UnwindData |  |
| 736 | `GetPersistedRegistryLocationW` | `0xE7C40` | 62 | UnwindData |  |
| 816 | `GetSystemDefaultLCID` | `0xE7D50` | 40 | UnwindData |  |
| 1060 | `K32QueryWorkingSetEx` | `0xE7DF0` | 79 | UnwindData |  |
| 1398 | `QueryWorkingSetEx` | `0xE7DF0` | 79 | UnwindData |  |
| 413 | `FindFirstVolumeW` | `0xE8200` | 543 | UnwindData |  |
| 421 | `FindNextVolumeW` | `0xE8430` | 841 | UnwindData |  |
| 1917 | `VirtualLock` | `0xE9190` | 71 | UnwindData |  |
| 940 | `ImpersonateSelf` | `0xE91E0` | 42 | UnwindData |  |
| 1706 | `SetThreadPriorityBoost` | `0xE9210` | 68 | UnwindData |  |
| 1103 | `MakeSelfRelativeSD` | `0xE9420` | 54 | UnwindData |  |
| 1425 | `ReadConsoleOutputW` | `0xE9460` | 30 | UnwindData |  |
| 1985 | `WriteConsoleOutputW` | `0xE9810` | 30 | UnwindData |  |
| 788 | `GetSecurityDescriptorSacl` | `0xE9DF0` | 92 | UnwindData |  |
| 1836 | `TrySubmitThreadpoolCallback` | `0xE9E60` | 49 | UnwindData |  |
| 839 | `GetSystemWow64Directory2A` | `0xE9EA0` | 371 | UnwindData |  |
| 840 | `GetSystemWow64Directory2W` | `0xEA190` | 228 | UnwindData |  |
| 838 | `GetSystemWindowsDirectoryW` | `0xEA280` | 88 | UnwindData |  |
| 266 | `CreateTimerQueueTimer` | `0xEA2E0` | 156 | UnwindData |  |
| 640 | `GetKernelObjectSecurity` | `0xEA420` | 52 | UnwindData |  |
| 325 | `DuplicateToken` | `0xEA4D0` | 167 | UnwindData |  |
| 1646 | `SetHandleInformation` | `0xEA5D0` | 274 | UnwindData |  |
| 233 | `CreateNamedPipeW` | `0xEA6F0` | 931 | UnwindData |  |
| 183 | `ConvertFiberToThread` | `0xEAAA0` | 106 | UnwindData |  |
| 2005 | `__dllonexit3` | `0xEAB10` | 84 | UnwindData |  |
| 1721 | `SetUnhandledExceptionFilter` | `0xEAD50` | 515 | UnwindData |  |
| 782 | `GetSecurityDescriptorControl` | `0xEB0B0` | 42 | UnwindData |  |
| 1910 | `VirtualAlloc2` | `0xEB100` | 146 | UnwindData |  |
| 1561 | `SHRegEnumUSKeyW` | `0xEB1A0` | 523 | UnwindData |  |
| 535 | `GetCurrentDirectoryW` | `0xEB3C0` | 26 | UnwindData |  |
| 1772 | `StrIsIntlEqualW` | `0xEB3E0` | 57 | UnwindData |  |
| 149 | `CheckTokenMembershipEx` | `0xEB420` | 88 | UnwindData |  |
| 829 | `GetSystemPreferredUILanguages` | `0xEB480` | 89 | UnwindData |  |
| 1480 | `RegOpenCurrentUser` | `0xEB4E0` | 50 | UnwindData |  |
| 1101 | `MakeAbsoluteSD` | `0xEB520` | 141 | UnwindData |  |
| 1293 | `PathUnExpandEnvStringsW` | `0xEB5C0` | 26 | UnwindData |  |
| 807 | `GetStdHandle` | `0xEC390` | 162 | UnwindData |  |
| 1840 | `UnlockFile` | `0xEC440` | 183 | UnwindData |  |
| 795 | `GetSidSubAuthorityCount` | `0xEC6B0` | 43 | UnwindData |  |
| 42 | `AdjustTokenPrivileges` | `0xEC6F0` | 61 | UnwindData |  |
| 1114 | `MoveFileExW` | `0xECCA0` | 66 | UnwindData |  |
| 1117 | `MoveFileWithProgressW` | `0xECCF0` | 59 | UnwindData |  |
| 1116 | `MoveFileWithProgressTransactedW` | `0xECD40` | 3,948 | UnwindData |  |
| 1538 | `ResetWriteWatch` | `0xEDCE0` | 50 | UnwindData |  |
| 307 | `DisableThreadLibraryCalls` | `0xEDD20` | 47 | UnwindData |  |
| 566 | `GetDeviceDriverFileNameW` | `0xEDD60` | 148 | UnwindData |  |
| 1044 | `K32GetDeviceDriverFileNameW` | `0xEDD60` | 148 | UnwindData |  |
| 564 | `GetDeviceDriverBaseNameW` | `0xEDE00` | 148 | UnwindData |  |
| 1042 | `K32GetDeviceDriverBaseNameW` | `0xEDE00` | 148 | UnwindData |  |
| 565 | `GetDeviceDriverFileNameA` | `0xEDEA0` | 148 | UnwindData |  |
| 1043 | `K32GetDeviceDriverFileNameA` | `0xEDEA0` | 148 | UnwindData |  |
| 563 | `GetDeviceDriverBaseNameA` | `0xEDF40` | 171 | UnwindData |  |
| 1041 | `K32GetDeviceDriverBaseNameA` | `0xEDF40` | 171 | UnwindData |  |
| 237 | `CreatePrivateObjectSecurityEx` | `0xEE1D0` | 84 | UnwindData |  |
| 434 | `FlushFileBuffers` | `0xEE230` | 132 | UnwindData |  |
| 1390 | `QueryStateContainerCreatedNew` | `0xEE2C0` | 151 | UnwindData |  |
| 871 | `GetTimeFormatW` | `0xEE3C0` | 264 | UnwindData |  |
| 263 | `CreateThreadpoolWait` | `0xEE4D0` | 69 | UnwindData |  |
| 15 | `AddAccessAllowedAce` | `0xEE570` | 42 | UnwindData |  |
| 766 | `GetProductInfo` | `0xEE5A0` | 41 | UnwindData |  |
| 530 | `GetCurrentActCtx` | `0xEE5D0` | 57 | UnwindData |  |
| 1571 | `SHRegQueryInfoUSKeyW` | `0xEE610` | 518 | UnwindData |  |
| 626 | `GetFullPathNameA` | `0xEE820` | 752 | UnwindData |  |
| 280 | `DelayLoadFailureHook` | `0xEEB20` | 83 | UnwindData |  |
| 281 | `DelayLoadFailureHookLookup` | `0xEEB80` | 90 | UnwindData |  |
| 1674 | `SetProcessValidCallTargets` | `0xEEDA0` | 312 | UnwindData |  |
| 939 | `ImpersonateNamedPipeClient` | `0xEEEE0` | 269 | UnwindData |  |
| 561 | `GetDateFormatW` | `0xEF000` | 309 | UnwindData |  |
| 1617 | `SetConsoleTitleW` | `0xEF140` | 61 | UnwindData |  |
| 1423 | `ReadConsoleOutputCharacterA` | `0xEF230` | 41 | UnwindData |  |
| 526 | `GetConsoleTitleW` | `0xEF380` | 97 | UnwindData |  |
| 1983 | `WriteConsoleOutputCharacterA` | `0xEF4B0` | 41 | UnwindData |  |
| 457 | `GetACP` | `0xEF790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1401 | `QueueUserWorkItem` | `0xEF7A0` | 42 | UnwindData |  |
| 1510 | `ReleaseActCtx` | `0xEFD60` | 40 | UnwindData |  |
| 1074 | `LoadLibraryA` | `0xEFD90` | 221 | UnwindData |  |
| 1699 | `SetThreadIdealProcessor` | `0xEFE80` | 63 | UnwindData |  |
| 978 | `InternetTimeToSystemTimeA` | `0xF0050` | 58 | UnwindData |  |
| 959 | `InitializeSid` | `0xF04E0` | 42 | UnwindData |  |
| 922 | `HeapCreate` | `0xF0510` | 122 | UnwindData |  |
| 849 | `GetTempPathW` | `0xF0590` | 613 | UnwindData |  |
| 860 | `GetThreadPreferredUILanguages` | `0xF0800` | 63 | UnwindData |  |
| 1419 | `ReadConsoleInputExW` | `0xF0850` | 30 | UnwindData |  |
| 1314 | `PeekConsoleInputW` | `0xF0880` | 27 | UnwindData |  |
| 1420 | `ReadConsoleInputW` | `0xF08B0` | 27 | UnwindData |  |
| 1313 | `PeekConsoleInputA` | `0xF08E0` | 27 | UnwindData |  |
| 212 | `CreateFiber` | `0xF0B50` | 28 | UnwindData |  |
| 213 | `CreateFiberEx` | `0xF0B80` | 672 | UnwindData |  |
| 1298 | `PcwCollectData` | `0xF1000` | 323 | UnwindData |  |
| 235 | `CreatePrivateNamespaceW` | `0xF1280` | 253 | UnwindData |  |
| 1153 | `OpenPrivateNamespaceW` | `0xF1390` | 145 | UnwindData |  |
| 425 | `FindResourceW` | `0xF16B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1638 | `SetFileInformationByHandle` | `0xF16D0` | 228 | UnwindData |  |
| 633 | `GetHandleInformation` | `0xF19A0` | 183 | UnwindData |  |
| 2030 | `lstrcpyn` | `0xF1A60` | 96 | UnwindData |  |
| 2031 | `lstrcpynA` | `0xF1A60` | 96 | UnwindData |  |
| 1545 | `ResumeThread` | `0xF1C20` | 52 | UnwindData |  |
| 324 | `DuplicateStateContainerHandle` | `0xF1C60` | 106 | UnwindData |  |
| 301 | `DeleteTimerQueueTimer` | `0xF1CD0` | 97 | UnwindData |  |
| 1625 | `SetEndOfFile` | `0xF1D40` | 192 | UnwindData |  |
| 1087 | `LocalFlags` | `0xF1E10` | 294 | UnwindData |  |
| 2032 | `lstrcpynW` | `0xF1F80` | 106 | UnwindData |  |
| 1709 | `SetThreadStackGuarantee` | `0xF1FF0` | 376 | UnwindData |  |
| 304 | `DestroyPrivateObjectSecurity` | `0xF21B0` | 42 | UnwindData |  |
| 981 | `IsApiSetImplemented` | `0xF2320` | 27 | UnwindData |  |
| 892 | `GetVersion` | `0xF2350` | 78 | UnwindData |  |
| 850 | `GetThreadContext` | `0xF23B0` | 42 | UnwindData |  |
| 729 | `GetPackageStatusForUserSid` | `0xF2450` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 580 | `GetEffectivePackageStatusForUserSid` | `0xF2480` | 132 | UnwindData |  |
| 517 | `GetConsoleMode` | `0xF2580` | 319 | UnwindData |  |
| 932 | `HeapValidate` | `0xF26D0` | 25 | UnwindData |  |
| 1236 | `PathGetArgsW` | `0xF27C0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 437 | `FlushViewOfFile` | `0xF2820` | 91 | UnwindData |  |
| 1378 | `QueryInterruptTimePrecise` | `0xF2890` | 42 | UnwindData |  |
| 119 | `CallNamedPipeW` | `0xF28C0` | 389 | UnwindData |  |
| 1829 | `TransactNamedPipe` | `0xF2A50` | 406 | UnwindData |  |
| 1655 | `SetNamedPipeHandleState` | `0xF2BF0` | 272 | UnwindData |  |
| 226 | `CreateIoCompletionPort` | `0xF2D10` | 221 | UnwindData |  |
| 688 | `GetNumberOfConsoleInputEvents` | `0xF2E00` | 319 | UnwindData |  |
| 800 | `GetStartupInfoW` | `0xF2F50` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `AreFileApisANSI` | `0xF30F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 862 | `GetThreadPriorityBoost` | `0xF3110` | 80 | UnwindData |  |
| 179 | `ConnectNamedPipe` | `0xF3170` | 207 | UnwindData |  |
| 728 | `GetPackageStatusForUser` | `0xF3250` | 301 | UnwindData |  |
| 1792 | `StrToIntExA` | `0xF3410` | 44 | UnwindData |  |
| 1789 | `StrToInt64ExA` | `0xF3450` | 258 | UnwindData |  |
| 1793 | `StrToIntExW` | `0xF3560` | 44 | UnwindData |  |
| 1790 | `StrToInt64ExW` | `0xF35A0` | 348 | UnwindData |  |
| 199 | `CreateBoundaryDescriptorW` | `0xF3710` | 77 | UnwindData |  |
| 1803 | `SuspendThread` | `0xF3AD0` | 52 | UnwindData |  |
| 638 | `GetIsEdpEnabled` | `0xF3B10` | 109 | UnwindData |  |
| 903 | `GetWindowsDirectoryW` | `0xF3B90` | 147 | UnwindData |  |
| 2013 | `_initterm` | `0xF4090` | 55 | UnwindData |  |
| 1650 | `SetKernelObjectSecurity` | `0xF40D0` | 42 | UnwindData |  |
| 1138 | `ObjectOpenAuditAlarmW` | `0xF4160` | 242 | UnwindData |  |
| 491 | `GetCommandLineW` | `0xF4260` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 450 | `FreeLibraryAndExitThread` | `0xF4270` | 162 | UnwindData |  |
| 607 | `GetFileInformationByName` | `0xF4320` | 380 | UnwindData |  |
| 1690 | `SetStdHandleEx` | `0xF44B0` | 128 | UnwindData |  |
| 35 | `AddRefActCtx` | `0xF46F0` | 40 | UnwindData |  |
| 1367 | `QueryActCtxSettingsW` | `0xF4740` | 132 | UnwindData |  |
| 1062 | `KernelbasePostInit` | `0xF47D0` | 94 | UnwindData |  |
| 1758 | `StrCmpNCA` | `0xF4A20` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `CloseState` | `0xF4B80` | 143 | UnwindData |  |
| 310 | `DisconnectNamedPipe` | `0xF4C20` | 269 | UnwindData |  |
| 465 | `GetAppContainerAce` | `0xF4D50` | 267 | UnwindData |  |
| 1021 | `IsValidAcl` | `0xF4E70` | 52 | UnwindData |  |
| 438 | `FoldStringW` | `0xF4F00` | 773 | UnwindData |  |
| 225 | `CreateHardLinkW` | `0xF57E0` | 677 | UnwindData |  |
| 1207 | `PathCchCanonicalizeEx` | `0xF5A90` | 3,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2014 | `_initterm_e` | `0xF6690` | 64 | UnwindData |  |
| 1159 | `OpenStateAtom` | `0xF66E0` | 132 | UnwindData |  |
| 558 | `GetCurrentThreadStackLimits` | `0xF67E0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1024 | `IsValidLocale` | `0xF6830` | 148 | UnwindData |  |
| 428 | `FlsAlloc` | `0xF68D0` | 52 | UnwindData |  |
| 1012 | `IsProcessorFeaturePresent` | `0xF6910` | 31 | UnwindData |  |
| 776 | `GetRegistryValueWithFallbackW` | `0xF6AC0` | 228 | UnwindData |  |
| 752 | `GetProcessImageFileNameA` | `0xF6C30` | 249 | UnwindData |  |
| 1053 | `K32GetProcessImageFileNameA` | `0xF6C30` | 249 | UnwindData |  |
| 542 | `GetCurrentPackageId` | `0xF6DB0` | 285 | UnwindData |  |
| 1509 | `RegisterWaitForSingleObjectEx` | `0xF6EE0` | 147 | UnwindData |  |
| 786 | `GetSecurityDescriptorOwner` | `0xF6F80` | 65 | UnwindData |  |
| 1096 | `LockFile` | `0xF6FD0` | 165 | UnwindData |  |
| 1698 | `SetThreadGroupAffinity` | `0xF7160` | 166 | UnwindData |  |
| 784 | `GetSecurityDescriptorGroup` | `0xF7210` | 65 | UnwindData |  |
| 1777 | `StrRChrIW` | `0xF7330` | 102 | UnwindData |  |
| 160 | `CloseStateAtom` | `0xF74F0` | 143 | UnwindData |  |
| 845 | `GetTempFileNameW` | `0xF7590` | 885 | UnwindData |  |
| 302 | `DeleteVolumeMountPointW` | `0xF7910` | 1,125 | UnwindData |  |
| 1134 | `NotifyMountMgr` | `0xF7D80` | 455 | UnwindData |  |
| 1978 | `WriteConsoleA` | `0xF7F50` | 47 | UnwindData |  |
| 1986 | `WriteConsoleW` | `0xF7F90` | 47 | UnwindData |  |
| 984 | `IsCharAlphaNumericW` | `0xF8140` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 730 | `GetPackageTargetPlatformProperty` | `0xF8260` | 214 | UnwindData |  |
| 404 | `FindFirstChangeNotificationW` | `0xF8420` | 439 | UnwindData |  |
| 122 | `CancelIoEx` | `0xF8700` | 55 | UnwindData |  |
| 1643 | `SetFileTime` | `0xF88E0` | 172 | UnwindData |  |
| 762 | `GetProcessWorkingSetSize` | `0xF89A0` | 25 | UnwindData |  |
| 763 | `GetProcessWorkingSetSizeEx` | `0xF89C0` | 176 | UnwindData |  |
| 1669 | `SetProcessInformation` | `0xF9220` | 555 | UnwindData |  |
| 1386 | `QueryProcessCycleTime` | `0xF9620` | 120 | UnwindData |  |
| 673 | `GetNLSVersion` | `0xF96A0` | 99 | UnwindData |  |
| 674 | `GetNLSVersionEx` | `0xF9710` | 96 | UnwindData |  |
| 793 | `GetSidLengthRequired` | `0xF9880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 985 | `IsCharAlphaW` | `0xF98A0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1660 | `SetPriorityClass` | `0xF99D0` | 537 | UnwindData |  |
| 923 | `HeapDestroy` | `0xF9F50` | 53 | UnwindData |  |
| 1221 | `PathCombineW` | `0xF9F90` | 65 | UnwindData |  |
| 37 | `AddSIDToBoundaryDescriptor` | `0xF9FE0` | 42 | UnwindData |  |
| 1098 | `LockResource` | `0xFA080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 286 | `DeleteFiber` | `0xFA090` | 220 | UnwindData |  |
| 1687 | `SetSecurityDescriptorSacl` | `0xFA180` | 42 | UnwindData |  |
| 1136 | `ObjectCloseAuditAlarmW` | `0xFA2F0` | 99 | UnwindData |  |
| 453 | `FreeSid` | `0xFA470` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 653 | `GetLogicalProcessorInformationEx` | `0xFA4A0` | 112 | UnwindData |  |
| 954 | `InitializeProcThreadAttributeList` | `0xFAAA0` | 137 | UnwindData |  |
| 1791 | `StrToIntA` | `0xFAB60` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 843 | `GetTargetPlatformContext` | `0xFABD0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 567 | `GetDiskFreeSpaceA` | `0xFAC10` | 128 | UnwindData |  |
| 570 | `GetDiskFreeSpaceW` | `0xFACA0` | 616 | UnwindData |  |
| 1602 | `SetConsoleCtrlHandler` | `0xFB060` | 180 | UnwindData |  |
| 79 | `AreAllAccessesGranted` | `0xFB460` | 25 | UnwindData |  |
| 1291 | `PathStripToRootW` | `0xFB480` | 34 | UnwindData |  |
| 249 | `CreateRestrictedToken` | `0xFB7A0` | 527 | UnwindData |  |
| 1926 | `WTSIsServerContainer` | `0xFB9C0` | 27 | UnwindData |  |
| 1670 | `SetProcessMitigationPolicy` | `0xFBA70` | 412 | UnwindData |  |
| 1238 | `PathGetCharTypeW` | `0xFBC70` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1867 | `UrlCompareW` | `0xFBCF0` | 437 | UnwindData |  |
| 196 | `CreateActCtxW` | `0xFBEB0` | 59 | UnwindData |  |
| 1540 | `ResolveDelayLoadedAPI` | `0xFBF00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 928 | `HeapSetInformation` | `0xFBF20` | 42 | UnwindData |  |
| 1720 | `SetTokenInformation` | `0xFBF50` | 42 | UnwindData |  |
| 891 | `GetUserPreferredUILanguages` | `0xFBF80` | 89 | UnwindData |  |
| 1006 | `IsNLSDefinedString` | `0xFBFE0` | 131 | UnwindData |  |
| 157 | `ClosePrivateNamespace` | `0xFC0A0` | 235 | UnwindData |  |
| 180 | `ContinueDebugEvent` | `0xFC230` | 86 | UnwindData |  |
| 46 | `AllocateLocallyUniqueId` | `0xFC340` | 42 | UnwindData |  |
| 429 | `FlsFree` | `0xFC370` | 42 | UnwindData |  |
| 1333 | `PrefetchVirtualMemory` | `0xFC3A0` | 73 | UnwindData |  |
| 2024 | `lstrcmp` | `0xFC3F0` | 140 | UnwindData |  |
| 2025 | `lstrcmpA` | `0xFC3F0` | 140 | UnwindData |  |
| 1642 | `SetFileSecurityW` | `0xFC4A0` | 448 | UnwindData |  |
| 1681 | `SetSecurityAccessMask` | `0xFC670` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1077 | `LoadLibraryW` | `0xFC700` | 1,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 990 | `IsCharLowerW` | `0xFCBB0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 652 | `GetLogicalProcessorInformation` | `0xFCC00` | 142 | UnwindData |  |
| 1544 | `RestoreThreadPreferredUILanguages` | `0xFCCA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1206 | `PathCchCanonicalize` | `0xFCCC0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1059 | `K32QueryWorkingSet` | `0xFCD80` | 79 | UnwindData |  |
| 1397 | `QueryWorkingSet` | `0xFCD80` | 79 | UnwindData |  |
| 118 | `CallEnclave` | `0xFCEA0` | 97 | UnwindData |  |
| 855 | `GetThreadIOPendingFlag` | `0xFD2E0` | 88 | UnwindData |  |
| 1673 | `SetProcessShutdownParameters` | `0xFD340` | 35 | UnwindData |  |
| 785 | `GetSecurityDescriptorLength` | `0xFD440` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1821 | `TlsAlloc` | `0xFD510` | 52 | UnwindData |  |
| 1971 | `Wow64DisableWow64FsRedirection` | `0xFD550` | 50 | UnwindData |  |
| 490 | `GetCommandLineA` | `0xFD590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1104 | `MapGenericMask` | `0xFD5A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1925 | `WTSGetServiceSessionId` | `0xFD5C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1085 | `LocalFileTimeToFileTime` | `0xFD5E0` | 159 | UnwindData |  |
| 260 | `CreateThreadpoolCleanupGroup` | `0xFD6E0` | 60 | UnwindData |  |
| 1628 | `SetEnvironmentVariableW` | `0xFD730` | 128 | UnwindData |  |
| 228 | `CreateMemoryResourceNotification` | `0xFD7C0` | 181 | UnwindData |  |
| 832 | `GetSystemTimeAdjustment` | `0xFD880` | 145 | UnwindData |  |
| 1415 | `ReOpenFile` | `0xFDA00` | 570 | UnwindData |  |
| 1627 | `SetEnvironmentVariableA` | `0xFDC40` | 293 | UnwindData |  |
| 622 | `GetFileVersionInfoSizeW` | `0xFDD70` | 3,472 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `CancelIo` | `0xFEB00` | 55 | UnwindData |  |
| 1007 | `IsNormalizedString` | `0xFEB40` | 114 | UnwindData |  |
| 899 | `GetVolumePathNameW` | `0xFEBC0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 583 | `GetEnabledXStateFeatures` | `0xFEC00` | 41 | UnwindData |  |
| 259 | `CreateThreadpool` | `0xFECB0` | 63 | UnwindData |  |
| 257 | `CreateSymbolicLinkW` | `0xFED30` | 1,137 | UnwindData |  |
| 279 | `DefineDosDeviceW` | `0xFF1D0` | 449 | UnwindData |  |
| 127 | `ChangeTimerQueueTimer` | `0xFF510` | 78 | UnwindData |  |
| 726 | `GetPackageSecurityProperty` | `0xFF620` | 177 | UnwindData |  |
| 146 | `CheckRemoteDebuggerPresent` | `0xFF700` | 119 | UnwindData |  |
| 1409 | `QuirkIsEnabledForPackage3` | `0xFF780` | 104 | UnwindData |  |
| 1461 | `RegFlushKey` | `0xFF950` | 233 | UnwindData |  |
| 1810 | `TerminateProcess` | `0xFFA40` | 98 | UnwindData |  |
| 234 | `CreatePipe` | `0xFFAB0` | 609 | UnwindData |  |
| 74 | `AppXPostSuccessExtension` | `0xFFD20` | 298 | UnwindData |  |
| 1377 | `QueryInterruptTime` | `0xFFF20` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1368 | `QueryActCtxW` | `0xFFFC0` | 132 | UnwindData |  |
| 937 | `ImpersonateAnonymousToken` | `0x100290` | 42 | UnwindData |  |
| 1751 | `StrCmpCA` | `0x1002C0` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 549 | `GetCurrentPackageResourcesContext` | `0x1004F0` | 232 | UnwindData |  |
| 195 | `CouldMultiUserAppsBehaviorBePossibleForPackage` | `0x100640` | 191 | UnwindData |  |
| 1194 | `PathAddExtensionW` | `0x100710` | 135 | UnwindData |  |
| 819 | `GetSystemDefaultUILanguage` | `0x100B50` | 75 | UnwindData |  |
| 1031 | `IsWow64GuestMachineSupported` | `0x100BB0` | 57 | UnwindData |  |
| 238 | `CreatePrivateObjectSecurityWithMultipleInheritance` | `0x100BF0` | 101 | UnwindData |  |
| 1469 | `RegKrnGetTermsrvRegistryExtensionFlags` | `0x100C60` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1525 | `RemoveDirectoryW` | `0x100DE0` | 47 | UnwindData |  |
| 296 | `DeleteStateContainer` | `0x101180` | 159 | UnwindData |  |
| 1475 | `RegLoadKeyA` | `0x101230` | 468 | UnwindData |  |
| 1476 | `RegLoadKeyW` | `0x101410` | 319 | UnwindData |  |
| 559 | `GetDateFormatA` | `0x101720` | 322 | UnwindData |  |
| 182 | `ConvertDefaultLocale` | `0x101870` | 39 | UnwindData |  |
| 552 | `GetCurrentProcessId` | `0x1018A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 936 | `IdnToUnicode` | `0x1018C0` | 95 | UnwindData |  |
| 1471 | `RegKrnSetDllHasThreadStateGlobal` | `0x101930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 747 | `GetProcessHandleCount` | `0x101940` | 80 | UnwindData |  |
| 1802 | `SubscribeWdagEnabledStateChange` | `0x1019A0` | 220 | UnwindData |  |
| 1227 | `PathFileExistsA` | `0x101AE0` | 82 | UnwindData |  |
| 1799 | `SubscribeEdpEnabledStateChange` | `0x101CD0` | 220 | UnwindData |  |
| 582 | `GetEightBitStringToUnicodeStringRoutine` | `0x101DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 485 | `GetCommModemStatus` | `0x101DD0` | 225 | UnwindData |  |
| 1822 | `TlsFree` | `0x101EC0` | 42 | UnwindData |  |
| 1714 | `SetThreadpoolThreadMinimum` | `0x1021D0` | 49 | UnwindData |  |
| 541 | `GetCurrentPackageGlobalizationContext` | `0x102210` | 174 | UnwindData |  |
| 1682 | `SetSecurityDescriptorControl` | `0x1023A0` | 42 | UnwindData |  |
| 1952 | `WerRegisterMemoryBlock` | `0x102460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 639 | `GetIsWdagEnabled` | `0x102470` | 109 | UnwindData |  |
| 299 | `DeleteTimerQueue` | `0x102570` | 26 | UnwindData |  |
| 300 | `DeleteTimerQueueEx` | `0x102590` | 85 | UnwindData |  |
| 53 | `AppContainerLookupMoniker` | `0x1025F0` | 154 | UnwindData |  |
| 252 | `CreateStateAtom` | `0x1027C0` | 117 | UnwindData |  |
| 1797 | `SubmitIoRing` | `0x102C00` | 118 | UnwindData |  |
| 111 | `BuildIoRingReadFile` | `0x102C80` | 518 | UnwindData |  |
| 948 | `InitializeContext` | `0x103360` | 90 | UnwindData |  |
| 949 | `InitializeContext2` | `0x1033C0` | 258 | UnwindData |  |
| 1891 | `VerQueryValueA` | `0x103860` | 20 | UnwindData |  |
| 878 | `GetUILanguageInfo` | `0x103880` | 127 | UnwindData |  |
| 416 | `FindNextChangeNotification` | `0x103910` | 99 | UnwindData |  |
| 303 | `DeriveCapabilitySidsFromName` | `0x103980` | 285 | UnwindData |  |
| 1505 | `RegisterGPNotificationInternal` | `0x103AB0` | 67 | UnwindData |  |
| 1506 | `RegisterStateChangeNotification` | `0x103B00` | 159 | UnwindData |  |
| 1187 | `ParseApplicationUserModelId` | `0x103C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1331 | `PopIoRingCompletion` | `0x103C70` | 224 | UnwindData |  |
| 1071 | `LoadEnclaveData` | `0x103E90` | 103 | UnwindData |  |
| 1250 | `PathIsRootW` | `0x104080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 733 | `GetPackagesByPackageFamily` | `0x1040A0` | 50 | UnwindData |  |
| 1350 | `PsmIsDynamicKey` | `0x1040E0` | 33 | UnwindData |  |
| 995 | `IsCharUpperW` | `0x104110` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 537 | `GetCurrentPackageApplicationResourcesContext` | `0x104170` | 258 | UnwindData |  |
| 692 | `GetOsSafeBootMode` | `0x104280` | 224 | UnwindData |  |
| 1989 | `WriteFileGather` | `0x104370` | 191 | UnwindData |  |
| 1387 | `QueryProtectedPolicy` | `0x104440` | 42 | UnwindData |  |
| 1245 | `PathIsPrefixA` | `0x104470` | 86 | UnwindData |  |
| 1222 | `PathCommonPrefixA` | `0x1044D0` | 408 | UnwindData |  |
| 268 | `CreateWaitableTimerW` | `0x1046C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1407 | `QuirkIsEnabledForPackage` | `0x1046E0` | 94 | UnwindData |  |
| 854 | `GetThreadGroupAffinity` | `0x104750` | 61 | UnwindData |  |
| 880 | `GetUnicodeStringToEightBitStringRoutine` | `0x1047A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 679 | `GetNamedPipeInfo` | `0x1047B0` | 222 | UnwindData |  |
| 678 | `GetNamedPipeHandleStateW` | `0x1048A0` | 396 | UnwindData |  |
| 427 | `FindVolumeClose` | `0x104A40` | 45 | UnwindData |  |
| 174 | `CompareObjectHandles` | `0x104A80` | 42 | UnwindData |  |
| 41 | `AdjustTokenGroups` | `0x105090` | 61 | UnwindData |  |
| 724 | `GetPackageResourcesProperty` | `0x105160` | 216 | UnwindData |  |
| 96 | `BaseFreeAppCompatDataForProcess` | `0x105260` | 40 | UnwindData |  |
| 407 | `FindFirstFileExFromAppW` | `0x105290` | 311 | UnwindData |  |
| 602 | `GetFileAttributesExFromAppW` | `0x1053D0` | 172 | UnwindData |  |
| 215 | `CreateFile2FromAppW` | `0x1054F0` | 207 | UnwindData |  |
| 265 | `CreateTimerQueue` | `0x105710` | 53 | UnwindData |  |
| 534 | `GetCurrentDirectoryA` | `0x105770` | 400 | UnwindData |  |
| 1244 | `PathIsLFNFileSpecW` | `0x105950` | 143 | UnwindData |  |
| 1677 | `SetProcessWorkingSetSizeEx` | `0x1059F0` | 250 | UnwindData |  |
| 327 | `EmptyWorkingSet` | `0x105AF0` | 193 | UnwindData |  |
| 1034 | `K32EmptyWorkingSet` | `0x105AF0` | 193 | UnwindData |  |
| 1801 | `SubscribeStateChangeNotification` | `0x105D50` | 159 | UnwindData |  |
| 341 | `EnumDeviceDrivers` | `0x105F30` | 456 | UnwindData |  |
| 1035 | `K32EnumDeviceDrivers` | `0x105F30` | 456 | UnwindData |  |
| 1737 | `StrCSpnA` | `0x106100` | 89 | UnwindData |  |
| 1951 | `WerRegisterFile` | `0x106160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 372 | `EqualPrefixSid` | `0x106170` | 63 | UnwindData |  |
| 220 | `CreateFileMappingFromApp` | `0x106270` | 204 | UnwindData |  |
| 1766 | `StrCpyNW` | `0x106450` | 24 | UnwindData |  |
| 1768 | `StrCpyNXW` | `0x106470` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1410 | `QuirkIsEnabledForPackage4` | `0x1064B0` | 102 | UnwindData |  |
| 1847 | `UnregisterGPNotificationInternal` | `0x1065A0` | 57 | UnwindData |  |
| 682 | `GetNumaHighestNodeNumber` | `0x1065E0` | 109 | UnwindData |  |
| 709 | `GetPackageGlobalizationProperty` | `0x106660` | 132 | UnwindData |  |
| 787 | `GetSecurityDescriptorRMControl` | `0x1066F0` | 34 | UnwindData |  |
| 1431 | `ReadFileScatter` | `0x1069F0` | 193 | UnwindData |  |
| 690 | `GetOEMCP` | `0x106AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1608 | `SetConsoleInputExeNameW` | `0x106AD0` | 142 | UnwindData |  |
| 52 | `AppContainerLookupDisplayNameMrtReference` | `0x106B70` | 262 | UnwindData |  |
| 76 | `AppXReleaseAppXContext` | `0x106DB0` | 38 | UnwindData |  |
| 282 | `DeleteAce` | `0x106DE0` | 42 | UnwindData |  |
| 1623 | `SetDefaultDllDirectories` | `0x106E10` | 42 | UnwindData |  |
| 1080 | `LoadStringA` | `0x106FD0` | 152 | UnwindData |  |
| 531 | `GetCurrentApplicationUserModelId` | `0x1072B0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 926 | `HeapQueryInformation` | `0x1073D0` | 52 | UnwindData |  |
| 1689 | `SetStdHandle` | `0x107410` | 99 | UnwindData |  |
| 1961 | `WerUnregisterMemoryBlock` | `0x107480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 684 | `GetNumaNodeProcessorMaskEx` | `0x107490` | 156 | UnwindData |  |
| 578 | `GetDynamicTimeZoneInformationEffectiveYears` | `0x1075C0` | 290 | UnwindData |  |
| 609 | `GetFileMUIPath` | `0x107790` | 99 | UnwindData |  |
| 902 | `GetWindowsDirectoryA` | `0x107800` | 67 | UnwindData |  |
| 837 | `GetSystemWindowsDirectoryA` | `0x107850` | 134 | UnwindData |  |
| 440 | `FormatApplicationUserModelId` | `0x1078E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 765 | `GetProcessorSystemCycleTime` | `0x1078F0` | 114 | UnwindData |  |
| 1592 | `SetCommMask` | `0x107980` | 271 | UnwindData |  |
| 28 | `AddDllDirectory` | `0x107AA0` | 86 | UnwindData |  |
| 1786 | `StrStrNIW` | `0x107B00` | 158 | UnwindData |  |
| 1748 | `StrChrNIW` | `0x107BB0` | 100 | UnwindData |  |
| 909 | `GlobalFlags` | `0x107C20` | 338 | UnwindData |  |
| 1800 | `SubscribeFeatureUsageFlush` | `0x108190` | 1,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1700 | `SetThreadIdealProcessorEx` | `0x1086B0` | 80 | UnwindData |  |
| 406 | `FindFirstFileExA` | `0x108710` | 434 | UnwindData |  |
| 853 | `GetThreadErrorMode` | `0x1088D0` | 61 | UnwindData |  |
| 332 | `EnterCriticalPolicySectionInternal` | `0x1089F0` | 55 | UnwindData |  |
| 1644 | `SetFileValidData` | `0x108A60` | 77 | UnwindData |  |
| 2008 | `__wgetmainargs` | `0x108AC0` | 77 | UnwindData |  |
| 1686 | `SetSecurityDescriptorRMControl` | `0x109550` | 24 | UnwindData |  |
| 1195 | `PathAllocCanonicalize` | `0x109570` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1960 | `WerUnregisterFile` | `0x1097C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `AddMandatoryAce` | `0x1097D0` | 57 | UnwindData |  |
| 1005 | `IsMrtResourceRedirectionEnabled` | `0x109870` | 402 | UnwindData |  |
| 1495 | `RegSaveKeyExW` | `0x109B40` | 427 | UnwindData |  |
| 1414 | `RaiseFailFastException` | `0x109F30` | 465 | UnwindData |  |
| 725 | `GetPackageSecurityContext` | `0x10A2F0` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `BaseIsAppcompatInfrastructureDisabled` | `0x10A510` | 40 | UnwindData |  |
| 624 | `GetFinalPathNameByHandleA` | `0x10A850` | 431 | UnwindData |  |
| 1974 | `Wow64RevertWow64FsRedirection` | `0x10AA80` | 53 | UnwindData |  |
| 1695 | `SetThreadContext` | `0x10AAC0` | 42 | UnwindData |  |
| 1852 | `UnsubscribeEdpEnabledStateChange` | `0x10ACB0` | 75 | UnwindData |  |
| 1855 | `UnsubscribeWdagEnabledStateChange` | `0x10ACB0` | 75 | UnwindData |  |
| 1672 | `SetProcessPriorityBoost` | `0x10AD10` | 68 | UnwindData |  |
| 102 | `BaseReadAppCompatDataForProcess` | `0x10AD60` | 75 | UnwindData |  |
| 820 | `GetSystemDirectoryA` | `0x10AE50` | 134 | UnwindData |  |
| 367 | `EnumUILanguagesW` | `0x10B170` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1067 | `LeaveCriticalPolicySectionInternal` | `0x10B2B0` | 57 | UnwindData |  |
| 656 | `GetMachineTypeAttributes` | `0x10B2F0` | 247 | UnwindData |  |
| 1218 | `PathCchStripPrefix` | `0x10B450` | 246 | UnwindData |  |
| 1109 | `MapViewOfFile3FromApp` | `0x10B6A0` | 228 | UnwindData |  |
| 1108 | `MapViewOfFile3` | `0x10B790` | 225 | UnwindData |  |
| 204 | `CreateDirectoryExW` | `0x10B880` | 4,401 | UnwindData |  |
| 283 | `DeleteBoundaryDescriptor` | `0x10C9F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1165 | `OpenWaitableTimerW` | `0x10CA10` | 218 | UnwindData |  |
| 1408 | `QuirkIsEnabledForPackage2` | `0x10CAF0` | 104 | UnwindData |  |
| 1003 | `IsInternetESCEnabled` | `0x10CB60` | 172 | UnwindData |  |
| 1854 | `UnsubscribeStateChangeNotification` | `0x10CCE0` | 143 | UnwindData |  |
| 883 | `GetUserDefaultLangID` | `0x10CD80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 488 | `GetCommState` | `0x10CD90` | 605 | UnwindData |  |
| 1283 | `PathRenameExtensionW` | `0x10D000` | 122 | UnwindData |  |
| 1020 | `IsUserCetAvailableInEnvironment` | `0x10D0C0` | 67 | UnwindData |  |
| 1135 | `NotifyRedirectedStringChange` | `0x10D110` | 283 | UnwindData |  |
| 161 | `CloseStateChangeNotification` | `0x10D7E0` | 143 | UnwindData |  |
| 1436 | `RecordFeatureUsage2` | `0x10D940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1502 | `RegUnLoadKeyW` | `0x10D950` | 318 | UnwindData |  |
| 1095 | `LocateXStateFeature` | `0x10DAD0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 358 | `EnumSystemFirmwareTables` | `0x10DBD0` | 295 | UnwindData |  |
| 1949 | `WerRegisterCustomMetadata` | `0x10DD00` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 236 | `CreatePrivateObjectSecurity` | `0x10DD40` | 62 | UnwindData |  |
| 1123 | `NeedCurrentDirectoryForExePathW` | `0x10DE10` | 46 | UnwindData |  |
| 345 | `EnumPageFilesW` | `0x10E200` | 348 | UnwindData |  |
| 1037 | `K32EnumPageFilesW` | `0x10E200` | 348 | UnwindData |  |
| 1896 | `VerifyPackageFamilyName` | `0x10E370` | 61 | UnwindData |  |
| 482 | `GetCalendarInfoW` | `0x10E3C0` | 129 | UnwindData |  |
| 1247 | `PathIsRelativeA` | `0x10E450` | 44 | UnwindData |  |
| 769 | `GetPtrCalData` | `0x10E500` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 459 | `GetAcceptLanguagesW` | `0x10E530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 925 | `HeapLock` | `0x10E540` | 25 | UnwindData |  |
| 479 | `GetCachedSigningLevel` | `0x10E5F0` | 85 | UnwindData |  |
| 1856 | `UpdatePackageStatus` | `0x10E650` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 360 | `EnumSystemGeoNames` | `0x10E6D0` | 260 | UnwindData |  |
| 13 | `AcquireStateLock` | `0x10EAF0` | 162 | UnwindData |  |
| 255 | `CreateStateLock` | `0x10EBA0` | 124 | UnwindData |  |
| 1779 | `StrRStrIA` | `0x10EC30` | 198 | UnwindData |  |
| 1146 | `OpenFileMappingFromApp` | `0x10ED90` | 124 | UnwindData |  |
| 1276 | `PathRemoveBlanksA` | `0x10EE40` | 132 | UnwindData |  |
| 1671 | `SetProcessPreferredUILanguages` | `0x10EED0` | 63 | UnwindData |  |
| 487 | `GetCommProperties` | `0x10EF80` | 266 | UnwindData |  |
| 1288 | `PathStripPathA` | `0x10F4C0` | 69 | UnwindData |  |
| 1235 | `PathGetArgsA` | `0x10F510` | 90 | UnwindData |  |
| 1928 | `WaitForDebugEvent` | `0x10F570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1150 | `OpenPackageInfoByFullName` | `0x10F580` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1953 | `WerRegisterRuntimeExceptionModule` | `0x10F710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1839 | `UnhandledExceptionFilter` | `0x10F720` | 1,464 | UnwindData |  |
| 1927 | `WaitCommEvent` | `0x10FD00` | 195 | UnwindData |  |
| 1356 | `PssWalkMarkerCreate` | `0x10FE00` | 104 | UnwindData |  |
| 1594 | `SetCommTimeouts` | `0x10FE70` | 288 | UnwindData |  |
| 931 | `HeapUnlock` | `0x10FFA0` | 25 | UnwindData |  |
| 1771 | `StrIsIntlEqualA` | `0x110240` | 57 | UnwindData |  |
| 1795 | `StrTrimA` | `0x110280` | 225 | UnwindData |  |
| 1078 | `LoadPackagedLibrary` | `0x110370` | 159 | UnwindData |  |
| 1621 | `SetCurrentDirectoryA` | `0x110420` | 208 | UnwindData |  |
| 844 | `GetTempFileNameA` | `0x110500` | 143 | UnwindData |  |
| 152 | `ClearCommBreak` | `0x1105D0` | 76 | UnwindData |  |
| 1365 | `PurgeComm` | `0x110630` | 222 | UnwindData |  |
| 1171 | `PackageFamilyNameFromId` | `0x110720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1972 | `Wow64EnableWow64FsRedirection` | `0x110730` | 39 | UnwindData |  |
| 402 | `FindCloseChangeNotification` | `0x110760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1225 | `PathCreateFromUrlAlloc` | `0x110770` | 201 | UnwindData |  |
| 746 | `GetProcessGroupAffinity` | `0x110840` | 103 | UnwindData |  |
| 313 | `DsCrackNamesW` | `0x110FB0` | 133 | UnwindData |  |
| 1626 | `SetEnvironmentStringsW` | `0x111040` | 192 | UnwindData |  |
| 163 | `CloseStateLock` | `0x111110` | 143 | UnwindData |  |
| 1586 | `SetCachedSigningLevel` | `0x1111B0` | 60 | UnwindData |  |
| 1353 | `PssDuplicateSnapshot` | `0x111200` | 130 | UnwindData |  |
| 1375 | `QueryIdleProcessorCycleTime` | `0x111320` | 75 | UnwindData |  |
| 452 | `FreeResource` | `0x111380` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1735 | `SpecialMBToWC` | `0x111380` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1253 | `PathIsUNCA` | `0x1113F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1526 | `RemoveDllDirectory` | `0x111420` | 42 | UnwindData |  |
| 1726 | `SetXStateFeaturesMask` | `0x111650` | 229 | UnwindData |  |
| 1862 | `UrlCanonicalizeA` | `0x111740` | 157 | UnwindData |  |
| 1174 | `PackageFullNameFromId` | `0x111800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1411 | `QuirkIsEnabledForProcess` | `0x111810` | 76 | UnwindData |  |
| 757 | `GetProcessPreferredUILanguages` | `0x111870` | 63 | UnwindData |  |
| 848 | `GetTempPathA` | `0x1118C0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 584 | `GetEnvironmentStrings` | `0x111A20` | 336 | UnwindData |  |
| 585 | `GetEnvironmentStringsA` | `0x111A20` | 336 | UnwindData |  |
| 144 | `CheckIfStateChangeNotificationExists` | `0x111BF0` | 151 | UnwindData |  |
| 420 | `FindNextStreamW` | `0x111CB0` | 146 | UnwindData |  |
| 1881 | `UrlIsNoHistoryW` | `0x111D50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 758 | `GetProcessPriorityBoost` | `0x111D60` | 80 | UnwindData |  |
| 1354 | `PssFreeSnapshot` | `0x111FB0` | 87 | UnwindData |  |
| 240 | `CreateProcessAsUserA` | `0x112010` | 105 | UnwindData |  |
| 315 | `DsFreeNameResultW` | `0x112080` | 45 | UnwindData |  |
| 921 | `HeapCompact` | `0x112110` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 698 | `GetPackageApplicationPropertyString` | `0x112140` | 93 | UnwindData |  |
| 1264 | `PathMatchSpecA` | `0x1121D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1676 | `SetProcessWorkingSetSize` | `0x1121E0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `AppContainerUnregisterSid` | `0x112310` | 70 | UnwindData |  |
| 1954 | `WerSetFlags` | `0x112360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1547 | `RsopLoggingEnabledInternal` | `0x112370` | 37 | UnwindData |  |
| 636 | `GetIntegratedDisplaySize` | `0x1125C0` | 150 | UnwindData |  |
| 1812 | `TerminateThread` | `0x112660` | 288 | UnwindData |  |
| 1914 | `VirtualAllocFromApp` | `0x112790` | 65 | UnwindData |  |
| 703 | `GetPackageFamilyNameFromFilePath` | `0x1127E0` | 58 | UnwindData |  |
| 1853 | `UnsubscribeFeatureUsageFlush` | `0x112820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1977 | `Wow64SuspendThread` | `0x112830` | 52 | UnwindData |  |
| 1102 | `MakeAbsoluteSD2` | `0x112870` | 42 | UnwindData |  |
| 123 | `CancelSynchronousIo` | `0x1128A0` | 57 | UnwindData |  |
| 1278 | `PathRemoveExtensionA` | `0x1128E0` | 53 | UnwindData |  |
| 1904 | `VerifyPackagePublisher` | `0x112A60` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1962 | `WerUnregisterRuntimeExceptionModule` | `0x112A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1861 | `UrlApplySchemeW` | `0x112AA0` | 196 | UnwindData |  |
| 31 | `AddPackageDependency` | `0x112C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1002 | `IsEnclaveTypeSupported` | `0x112C70` | 63 | UnwindData |  |
| 941 | `IncrementPackageStatusVersion` | `0x112D40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1814 | `TestControlReporting` | `0x112D50` | 115 | UnwindData |  |
| 1946 | `WerGetFlags` | `0x112E90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1668 | `SetProcessGroupAffinity` | `0x112EA0` | 166 | UnwindData |  |
| 207 | `CreateEnclave` | `0x112F50` | 109 | UnwindData |  |
| 99 | `BaseInitAppcompatCacheSupport` | `0x112FD0` | 37 | UnwindData |  |
| 735 | `GetPersistedFileLocationW` | `0x1130F0` | 65 | UnwindData |  |
| 1519 | `ReleaseStateLock` | `0x113390` | 151 | UnwindData |  |
| 275 | `DebugBreak` | `0x113430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1973 | `Wow64GetThreadContext` | `0x113440` | 42 | UnwindData |  |
| 1271 | `PathQuoteSpacesW` | `0x1134A0` | 131 | UnwindData |  |
| 696 | `GetPackageApplicationIds` | `0x114060` | 585 | UnwindData |  |
| 1663 | `SetProcessAffinityUpdateMode` | `0x114510` | 83 | UnwindData |  |
| 1186 | `PackageSidFromFamilyName` | `0x114570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1678 | `SetProtectedPolicy` | `0x114580` | 42 | UnwindData |  |
| 1381 | `QueryOptionalDelayLoadedAPI` | `0x1145B0` | 54 | UnwindData |  |
| 18 | `AddAccessDeniedAce` | `0x114920` | 42 | UnwindData |  |
| 1929 | `WaitForDebugEventEx` | `0x114950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 641 | `GetLargePageMinimum` | `0x114960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1073 | `LoadEnclaveImageW` | `0x114970` | 83 | UnwindData |  |
| 312 | `DsBindWithSpnExW` | `0x1149D0` | 122 | UnwindData |  |
| 879 | `GetUnicodeStringToEightBitSizeRoutine` | `0x115140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1529 | `RemovePackageStatus` | `0x115150` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 828 | `GetSystemMetadataPathForPackageFamily` | `0x1151F0` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 538 | `GetCurrentPackageContext` | `0x1153C0` | 133 | UnwindData |  |
| 1955 | `WerSetMaxProcessHoldMilliseconds` | `0x115620` | 2,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 953 | `InitializeEnclave` | `0x115DF0` | 52 | UnwindData |  |
| 697 | `GetPackageApplicationProperty` | `0x115E30` | 922 | UnwindData |  |
| 44 | `AllocConsoleWithOptions` | `0x116330` | 229 | UnwindData |  |
| 521 | `GetConsoleProcessList` | `0x116480` | 187 | UnwindData |  |
| 374 | `EscapeCommFunction` | `0x116550` | 339 | UnwindData |  |
| 2021 | `exit` | `0x117D60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1352 | `PssCaptureSnapshot` | `0x117D80` | 53 | UnwindData |  |
| 470 | `GetApplicationRestartSettings` | `0x117DC0` | 1,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 734 | `GetPerformanceInfo` | `0x118270` | 523 | UnwindData |  |
| 1052 | `K32GetPerformanceInfo` | `0x118270` | 523 | UnwindData |  |
| 253 | `CreateStateChangeNotification` | `0x1184D0` | 398 | UnwindData |  |
| 254 | `CreateStateContainer` | `0x118670` | 564 | UnwindData |  |
| 256 | `CreateStateSubcontainer` | `0x1188B0` | 579 | UnwindData |  |
| 297 | `DeleteStateContainerValue` | `0x118B00` | 295 | UnwindData |  |
| 369 | `EnumerateStateAtomValues` | `0x118C30` | 321 | UnwindData |  |
| 370 | `EnumerateStateContainerItems` | `0x118D80` | 341 | UnwindData |  |
| 467 | `GetAppDataFolder` | `0x118EE0` | 305 | UnwindData |  |
| 634 | `GetHivePath` | `0x119020` | 316 | UnwindData |  |
| 771 | `GetPublisherCacheFolder` | `0x119170` | 317 | UnwindData |  |
| 772 | `GetPublisherRootFolder` | `0x1192C0` | 305 | UnwindData |  |
| 781 | `GetSecureSystemAppDataFolder` | `0x119400` | 305 | UnwindData |  |
| 789 | `GetSerializedAtomBytes` | `0x119540` | 305 | UnwindData |  |
| 802 | `GetStateFolder` | `0x119680` | 316 | UnwindData |  |
| 803 | `GetStateRootFolder` | `0x1197D0` | 305 | UnwindData |  |
| 804 | `GetStateRootFolderBase` | `0x119910` | 305 | UnwindData |  |
| 813 | `GetSystemAppDataFolder` | `0x119A50` | 305 | UnwindData |  |
| 814 | `GetSystemAppDataKey` | `0x119B90` | 317 | UnwindData |  |
| 1158 | `OpenState` | `0x119CE0` | 426 | UnwindData |  |
| 1160 | `OpenStateExplicit` | `0x119E90` | 418 | UnwindData |  |
| 1161 | `OpenStateExplicitForUserSid` | `0x11A040` | 418 | UnwindData |  |
| 1162 | `OpenStateExplicitForUserSidString` | `0x11A1F0` | 418 | UnwindData |  |
| 1389 | `QueryStateAtomValueInfo` | `0x11A3A0` | 193 | UnwindData |  |
| 1391 | `QueryStateContainerItemInfo` | `0x11A470` | 180 | UnwindData |  |
| 1433 | `ReadStateAtomValue` | `0x11A530` | 535 | UnwindData |  |
| 27 | `AddDependencyToProcessPackageGraph` | `0x11A890` | 3,351 | UnwindData |  |
| 32 | `AddPackageDependency2` | `0x11B5B0` | 1,841 | UnwindData |  |
| 1528 | `RemovePackageDependency` | `0x11BCF0` | 855 | UnwindData |  |
| 197 | `CreateAppContainerToken` | `0x11D1C0` | 181 | UnwindData |  |
| 1859 | `UpdateProcThreadAttribute` | `0x11D300` | 764 | UnwindData |  |
| 847 | `GetTempPath2W` | `0x11D610` | 525 | UnwindData |  |
| 294 | `DeleteProcThreadAttributeList` | `0x120280` | 5,648 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1070 | `LoadAppInitDlls` | `0x120280` | 5,648 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1099 | `LogFeatureProcessUsage` | `0x120280` | 5,648 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2009 | `_amsg_exit` | `0x120280` | 5,648 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `CeipIsOptedIn` | `0x121890` | 43 | UnwindData |  |
| 245 | `CreatePseudoConsole` | `0x124D70` | 42 | UnwindData |  |
| 246 | `CreatePseudoConsoleAsUser` | `0x124DA0` | 560 | UnwindData |  |
| 344 | `EnumPageFilesA` | `0x125080` | 70 | UnwindData |  |
| 1036 | `K32EnumPageFilesA` | `0x125080` | 70 | UnwindData |  |
| 551 | `GetCurrentProcess` | `0x1254B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 556 | `GetCurrentThread` | `0x1254C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 462 | `GetAdjustObjectAttributesForPrivateNamespaceRoutine` | `0x1254D0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 200 | `CreateConsoleScreenBuffer` | `0x125560` | 697 | UnwindData |  |
| 581 | `GetEightBitStringToUnicodeSizeRoutine` | `0x125970` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1645 | `SetHandleCount` | `0x1259B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1468 | `RegKrnGetHKEY_ClassesRootAddress` | `0x1259C0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `BaseGetConsoleReference` | `0x125A30` | 1,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 515 | `GetConsoleInputExeNameA` | `0x125F60` | 228 | UnwindData |  |
| 516 | `GetConsoleInputExeNameW` | `0x126050` | 128 | UnwindData |  |
| 1607 | `SetConsoleInputExeNameA` | `0x126160` | 142 | UnwindData |  |
| 1473 | `RegLoadAppKeyA` | `0x126290` | 132 | UnwindData |  |
| 512 | `GetConsoleDisplayMode` | `0x126610` | 109 | UnwindData |  |
| 1523 | `RemoveDirectoryA` | `0x126780` | 69 | UnwindData |  |
| 1514 | `ReleasePseudoConsole` | `0x126860` | 54 | UnwindData |  |
| 397 | `FillConsoleOutputCharacterA` | `0x1268A0` | 39 | UnwindData |  |
| 1424 | `ReadConsoleOutputCharacterW` | `0x1268D0` | 41 | UnwindData |  |
| 1611 | `SetConsoleNumberOfCommandsW` | `0x126900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 390 | `ExpungeConsoleCommandHistoryW` | `0x126910` | 800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2015 | `_invalid_parameter` | `0x126C30` | 258 | UnwindData |  |
| 2018 | `_purecall` | `0x126E80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2019 | `_time64` | `0x126EA0` | 98 | UnwindData |  |
| 2036 | `time` | `0x126F10` | 17,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1887 | `VerFindFileA` | `0x12B220` | 716 | UnwindData |  |
| 84 | `AreThereVisibleLogoffScriptsInternal` | `0x12B500` | 60 | UnwindData |  |
| 85 | `AreThereVisibleShutdownScriptsInternal` | `0x12B550` | 60 | UnwindData |  |
| 439 | `ForceSyncFgPolicyInternal` | `0x12B5A0` | 60 | UnwindData |  |
| 447 | `FreeGPOListInternalA` | `0x12B5F0` | 57 | UnwindData |  |
| 448 | `FreeGPOListInternalW` | `0x12B630` | 57 | UnwindData |  |
| 456 | `GenerateGPNotificationInternal` | `0x12B670` | 86 | UnwindData |  |
| 473 | `GetAppliedGPOListInternalA` | `0x12B6D0` | 112 | UnwindData |  |
| 474 | `GetAppliedGPOListInternalW` | `0x12B750` | 112 | UnwindData |  |
| 628 | `GetGPOListInternalA` | `0x12B7D0` | 119 | UnwindData |  |
| 629 | `GetGPOListInternalW` | `0x12B850` | 119 | UnwindData |  |
| 681 | `GetNextFgPolicyRefreshInfoInternal` | `0x12B8D0` | 72 | UnwindData |  |
| 739 | `GetPreviousFgPolicyRefreshInfoInternal` | `0x12B920` | 72 | UnwindData |  |
| 918 | `HasPolicyForegroundProcessingCompletedInternal` | `0x12B970` | 112 | UnwindData |  |
| 1015 | `IsSyncForegroundPolicyRefresh` | `0x12B9F0` | 76 | UnwindData |  |
| 1438 | `RefreshPolicyExInternal` | `0x12BA50` | 65 | UnwindData |  |
| 1439 | `RefreshPolicyInternal` | `0x12BAA0` | 55 | UnwindData |  |
| 1930 | `WaitForMachinePolicyForegroundProcessingInternal` | `0x12BAE0` | 50 | UnwindData |  |
| 1939 | `WaitForUserPolicyForegroundProcessingInternal` | `0x12BB20` | 50 | UnwindData |  |
| 1888 | `VerFindFileW` | `0x12BD90` | 856 | UnwindData |  |
| 314 | `DsFreeDomainControllerInfoW` | `0x12C0F0` | 67 | UnwindData |  |
| 316 | `DsFreeNgcKey` | `0x12C140` | 40 | UnwindData |  |
| 317 | `DsFreePasswordCredentials` | `0x12C170` | 40 | UnwindData |  |
| 318 | `DsGetDomainControllerInfoW` | `0x12C1A0` | 114 | UnwindData |  |
| 319 | `DsMakePasswordCredentialsW` | `0x12C220` | 104 | UnwindData |  |
| 320 | `DsReadNgcKeyW` | `0x12C290` | 104 | UnwindData |  |
| 321 | `DsUnBindW` | `0x12C300` | 60 | UnwindData |  |
| 322 | `DsWriteNgcKeyW` | `0x12C350` | 104 | UnwindData |  |
| 1993 | `ZombifyActCtx` | `0x12C3C0` | 57 | UnwindData |  |
| 88 | `BaseCheckAppcompatCache` | `0x12C400` | 91 | UnwindData |  |
| 89 | `BaseCheckAppcompatCacheEx` | `0x12C470` | 158 | UnwindData |  |
| 90 | `BaseCleanupAppcompatCacheSupport` | `0x12C520` | 45 | UnwindData |  |
| 93 | `BaseDumpAppcompatCache` | `0x12C560` | 31 | UnwindData |  |
| 94 | `BaseFlushAppcompatCache` | `0x12C590` | 37 | UnwindData |  |
| 103 | `BaseUpdateAppcompatCache` | `0x12C5C0` | 75 | UnwindData |  |
| 469 | `GetApplicationRecoveryCallback` | `0x12C620` | 171 | UnwindData |  |
| 1947 | `WerRegisterAdditionalProcess` | `0x12C6E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1948 | `WerRegisterAppLocalDump` | `0x12C6F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1950 | `WerRegisterExcludedMemoryBlock` | `0x12C700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1956 | `WerUnregisterAdditionalProcess` | `0x12C720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1957 | `WerUnregisterAppLocalDump` | `0x12C730` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1958 | `WerUnregisterCustomMetadata` | `0x12C750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1959 | `WerUnregisterExcludedMemoryBlock` | `0x12C760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `AppXGetOSMinVersion` | `0x12C770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `AppXUpdatePackageCapabilities` | `0x12C770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 391 | `ExtensionProgIdExists` | `0x12C770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 594 | `GetExtensionProgIds` | `0x12C770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 704 | `GetPackageFamilyNameFromProgId` | `0x12C770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `MsixIsSystemPackageByAppUserModelId` | `0x12C770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1963 | `WerpNotifyLoadStringResource` | `0x12C770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1964 | `WerpNotifyUseStringResource` | `0x12C770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 989 | `IsCharLowerA` | `0x12C780` | 120 | UnwindData |  |
| 994 | `IsCharUpperA` | `0x12C800` | 118 | UnwindData |  |
| 142 | `CheckAllowDecryptedRemoteDestinationPolicy` | `0x12CA80` | 216 | UnwindData |  |
| 1738 | `StrCSpnIA` | `0x12CD00` | 89 | UnwindData |  |
| 1739 | `StrCSpnIW` | `0x12CD60` | 98 | UnwindData |  |
| 1742 | `StrCatBuffW` | `0x12CDD0` | 43 | UnwindData |  |
| 1743 | `StrCatChainW` | `0x12CE10` | 112 | UnwindData |  |
| 1767 | `StrCpyNXA` | `0x12CE90` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1773 | `StrPBrkA` | `0x12CED0` | 86 | UnwindData |  |
| 1775 | `StrRChrA` | `0x12CF30` | 111 | UnwindData |  |
| 1776 | `StrRChrIA` | `0x12CFB0` | 127 | UnwindData |  |
| 1781 | `StrSpnA` | `0x12D040` | 141 | UnwindData |  |
| 1782 | `StrSpnW` | `0x12D0E0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 986 | `IsCharBlankW` | `0x12D130` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 987 | `IsCharCntrlW` | `0x12D170` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 988 | `IsCharDigitW` | `0x12D1A0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 991 | `IsCharPunctW` | `0x12D1F0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 992 | `IsCharSpaceA` | `0x12D240` | 73 | UnwindData |  |
| 996 | `IsCharXDigitW` | `0x12D290` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 293 | `DeletePersistedRegistryValue` | `0x12D2F0` | 544 | UnwindData |  |
| 1656 | `SetPersistedRegistryBOOL` | `0x12D520` | 40 | UnwindData |  |
| 1657 | `SetPersistedRegistryDWORD` | `0x12D520` | 40 | UnwindData |  |
| 1658 | `SetPersistedRegistryString` | `0x12D550` | 105 | UnwindData |  |
| 1659 | `SetPersistedRegistryValue` | `0x12D5C0` | 630 | UnwindData |  |
| 1402 | `QuirkGetData` | `0x12D840` | 60 | UnwindData |  |
| 1403 | `QuirkGetData2` | `0x12D890` | 62 | UnwindData |  |
| 1405 | `QuirkIsEnabled2` | `0x12D8E0` | 57 | UnwindData |  |
| 188 | `CopyContext` | `0x12D920` | 49 | UnwindData |  |
| 328 | `EnableProcessOptionalXStateFeatures` | `0x12D960` | 111 | UnwindData |  |
| 852 | `GetThreadEnabledXStateFeatures` | `0x12D9E0` | 40 | UnwindData |  |
| 907 | `GetXStateFeaturesMask` | `0x12DA10` | 192 | UnwindData |  |
| 630 | `GetGamingDeviceModelInformation` | `0x12DAE0` | 316 | UnwindData |  |
| 191 | `CopyFileFromAppW` | `0x12DC90` | 154 | UnwindData |  |
| 205 | `CreateDirectoryFromAppW` | `0x12DD30` | 149 | UnwindData |  |
| 218 | `CreateFileFromAppW` | `0x12DDD0` | 130 | UnwindData |  |
| 290 | `DeleteFileFromAppW` | `0x12DE60` | 143 | UnwindData |  |
| 1115 | `MoveFileFromAppW` | `0x12DF00` | 167 | UnwindData |  |
| 1524 | `RemoveDirectoryFromAppW` | `0x12DFB0` | 143 | UnwindData |  |
| 1534 | `ReplaceFileFromAppW` | `0x12E050` | 188 | UnwindData |  |
| 1636 | `SetFileAttributesFromAppW` | `0x12E120` | 149 | UnwindData |  |
| 1216 | `PathCchRenameExtension` | `0x12E2B0` | 306 | UnwindData |  |
| 1554 | `SHRegCreateUSKeyA` | `0x12E570` | 142 | UnwindData |  |
| 1556 | `SHRegDeleteEmptyUSKeyA` | `0x12E610` | 141 | UnwindData |  |
| 1557 | `SHRegDeleteEmptyUSKeyW` | `0x12E6B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1558 | `SHRegDeleteUSValueA` | `0x12E6D0` | 138 | UnwindData |  |
| 1559 | `SHRegDeleteUSValueW` | `0x12E760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1564 | `SHRegGetBoolUSValueA` | `0x12E770` | 173 | UnwindData |  |
| 1224 | `PathCreateFromUrlA` | `0x12EC10` | 340 | UnwindData |  |
| 1860 | `UrlApplySchemeA` | `0x12ED70` | 340 | UnwindData |  |
| 1866 | `UrlCompareA` | `0x12EED0` | 390 | UnwindData |  |
| 1868 | `UrlCreateFromPathA` | `0x12F060` | 336 | UnwindData |  |
| 1870 | `UrlEscapeA` | `0x12F1C0` | 354 | UnwindData |  |
| 1872 | `UrlFixupW` | `0x12F330` | 859 | UnwindData |  |
| 1873 | `UrlGetLocationA` | `0x12F6A0` | 190 | UnwindData |  |
| 1877 | `UrlHashA` | `0x12F770` | 81 | UnwindData |  |
| 1878 | `UrlHashW` | `0x12F7D0` | 165 | UnwindData |  |
| 1879 | `UrlIsA` | `0x12F880` | 254 | UnwindData |  |
| 1880 | `UrlIsNoHistoryA` | `0x12F990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1882 | `UrlIsOpaqueA` | `0x12F9A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1883 | `UrlIsOpaqueW` | `0x12F9B0` | 9,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1967 | `WilFailureWatcherResume` | `0x132010` | 41 | UnwindData |  |
| 1969 | `WilFailureWatcherSuspend` | `0x132040` | 41 | UnwindData |  |
| 977 | `InternetTimeFromSystemTimeW` | `0x132210` | 285 | UnwindData |  |
| 979 | `InternetTimeToSystemTimeW` | `0x132340` | 238 | UnwindData |  |
| 109 | `BuildIoRingCancelRequest` | `0x132B50` | 198 | UnwindData |  |
| 110 | `BuildIoRingFlushFile` | `0x132C20` | 283 | UnwindData |  |
| 112 | `BuildIoRingReadFileScatter` | `0x132D50` | 281 | UnwindData |  |
| 113 | `BuildIoRingRegisterBuffers` | `0x132E70` | 169 | UnwindData |  |
| 114 | `BuildIoRingRegisterFileHandles` | `0x132F20` | 200 | UnwindData |  |
| 115 | `BuildIoRingWriteFile` | `0x132FF0` | 339 | UnwindData |  |
| 116 | `BuildIoRingWriteFileGather` | `0x133150` | 323 | UnwindData |  |
| 155 | `CloseIoRing` | `0x1332A0` | 52 | UnwindData |  |
| 227 | `CreateIoRing` | `0x1332E0` | 250 | UnwindData |  |
| 637 | `GetIoRingInfo` | `0x1333E0` | 79 | UnwindData |  |
| 1004 | `IsIoRingOpSupported` | `0x133440` | 53 | UnwindData |  |
| 1379 | `QueryIoRingCapabilities` | `0x133480` | 150 | UnwindData |  |
| 1647 | `SetIoRingCompletionEvent` | `0x133520` | 169 | UnwindData |  |
| 1126 | `NlsGetACPFromLocale` | `0x1335D0` | 94 | UnwindData |  |
| 887 | `GetUserInfo` | `0x133740` | 36 | UnwindData |  |
| 888 | `GetUserInfoWord` | `0x133770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1023 | `IsValidLanguageGroup` | `0x133790` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1124 | `NlsCheckPolicy` | `0x1337D0` | 72 | UnwindData |  |
| 1130 | `NlsUpdateSystemLocale` | `0x133820` | 129 | UnwindData |  |
| 1587 | `SetCalendarInfoW` | `0x133B90` | 353 | UnwindData |  |
| 1889 | `VerLanguageNameA` | `0x134010` | 239 | UnwindData |  |
| 336 | `EnumCalendarInfoExW` | `0x134110` | 97 | UnwindData |  |
| 340 | `EnumDateFormatsW` | `0x134180` | 77 | UnwindData |  |
| 343 | `EnumLanguageGroupLocalesW` | `0x1341E0` | 23 | UnwindData |  |
| 357 | `EnumSystemCodePagesW` | `0x134200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 361 | `EnumSystemLanguageGroupsW` | `0x134220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 366 | `EnumTimeFormatsW` | `0x134240` | 75 | UnwindData |  |
| 970 | `Internal_EnumLanguageGroupLocales` | `0x1342A0` | 885 | UnwindData |  |
| 971 | `Internal_EnumSystemCodePages` | `0x134620` | 633 | UnwindData |  |
| 972 | `Internal_EnumSystemLanguageGroups` | `0x1348A0` | 348 | UnwindData |  |
| 529 | `GetCurrencyFormatW` | `0x136DD0` | 135 | UnwindData |  |
| 608 | `GetFileMUIInfo` | `0x136EB0` | 1,660 | UnwindData |  |
| 935 | `IdnToNameprepUnicode` | `0x1375A0` | 95 | UnwindData |  |
| 1908 | `VerifyScripts` | `0x137610` | 600 | UnwindData |  |
| 1722 | `SetUserGeoID` | `0x137C40` | 21 | UnwindData |  |
| 1026 | `IsValidNLSVersion` | `0x137CE0` | 108 | UnwindData |  |
| 83 | `AreShortNamesEnabled` | `0x1380D0` | 288 | UnwindData |  |
| 654 | `GetLongPathNameA` | `0x138680` | 547 | UnwindData |  |
| 1824 | `TlsGetValue2` | `0x1388B0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 691 | `GetOsManufacturingMode` | `0x138970` | 302 | UnwindData |  |
| 1393 | `QueryThreadpoolStackInformation` | `0x138AE0` | 49 | UnwindData |  |
| 1712 | `SetThreadpoolStackInformation` | `0x138B20` | 49 | UnwindData |  |
| 1374 | `QueryGlobalizationUserSettingsStatus` | `0x138B60` | 136 | UnwindData |  |
| 2010 | `_c_exit` | `0x138BF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2011 | `_cexit` | `0x138C10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2012 | `_exit` | `0x138C30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2023 | `hwprintf` | `0x138C50` | 34 | UnwindData |  |
| 2037 | `wprintf` | `0x138E60` | 46 | UnwindData |  |
| 1191 | `PathAddBackslashA` | `0x139160` | 45 | UnwindData |  |
| 1255 | `PathIsUNCServerA` | `0x1391A0` | 74 | UnwindData |  |
| 1256 | `PathIsUNCServerShareA` | `0x1391F0` | 92 | UnwindData |  |
| 1268 | `PathParseIconLocationA` | `0x139260` | 128 | UnwindData |  |
| 1270 | `PathQuoteSpacesA` | `0x1392F0` | 125 | UnwindData |  |
| 1292 | `PathUnExpandEnvStringsA` | `0x139380` | 26 | UnwindData |  |
| 1294 | `PathUnquoteSpacesA` | `0x1393A0` | 78 | UnwindData |  |
| 1549 | `SHExpandEnvironmentStringsA` | `0x139400` | 89 | UnwindData |  |
| 1578 | `SHTruncateString` | `0x139460` | 132 | UnwindData |  |
| 1193 | `PathAddExtensionA` | `0x1394F0` | 124 | UnwindData |  |
| 1233 | `PathFindNextComponentA` | `0x139580` | 77 | UnwindData |  |
| 1237 | `PathGetCharTypeA` | `0x1395E0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1241 | `PathIsFileSpecA` | `0x139650` | 52 | UnwindData |  |
| 1243 | `PathIsLFNFileSpecA` | `0x139690` | 127 | UnwindData |  |
| 1249 | `PathIsRootA` | `0x139720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1251 | `PathIsSameRootA` | `0x139730` | 111 | UnwindData |  |
| 1262 | `PathIsValidCharA` | `0x1397B0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1272 | `PathRelativePathToA` | `0x139870` | 402 | UnwindData |  |
| 1274 | `PathRemoveBackslashA` | `0x139A10` | 74 | UnwindData |  |
| 1284 | `PathSearchAndQualifyA` | `0x139A60` | 161 | UnwindData |  |
| 1286 | `PathSkipRootA` | `0x139B10` | 71 | UnwindData |  |
| 1560 | `SHRegEnumUSKeyA` | `0x139B60` | 338 | UnwindData |  |
| 1562 | `SHRegEnumUSValueA` | `0x139CC0` | 412 | UnwindData |  |
| 1570 | `SHRegQueryInfoUSKeyA` | `0x139E70` | 365 | UnwindData |  |
| 1574 | `SHRegSetUSValueA` | `0x139FF0` | 141 | UnwindData |  |
| 1576 | `SHRegWriteUSValueA` | `0x13A090` | 403 | UnwindData |  |
| 1520 | `RemapPredefinedHandleInternal` | `0x13A330` | 381 | UnwindData |  |
| 775 | `GetRegistryExtensionFlags` | `0x13A4C0` | 367 | UnwindData |  |
| 1465 | `RegKrnGetAppKeyEventAddressInternal` | `0x13A640` | 49 | UnwindData |  |
| 1466 | `RegKrnGetAppKeyLoaded` | `0x13A680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1470 | `RegKrnResetAppKeyLoaded` | `0x13A690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1472 | `RegKrnSetTermsrvRegistryExtensionFlags` | `0x13A6B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1459 | `RegEnumValueA` | `0x13A6C0` | 2,252 | UnwindData |  |
| 1501 | `RegUnLoadKeyA` | `0x13AFA0` | 400 | UnwindData |  |
| 1477 | `RegLoadMUIStringA` | `0x13B140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1488 | `RegQueryMultipleValuesA` | `0x13B150` | 1,853 | UnwindData |  |
| 1492 | `RegRestoreKeyA` | `0x13B8A0` | 322 | UnwindData |  |
| 1493 | `RegRestoreKeyW` | `0x13B9F0` | 263 | UnwindData |  |
| 1494 | `RegSaveKeyExA` | `0x13BB00` | 475 | UnwindData |  |
| 348 | `EnumProcesses` | `0x13BEB0` | 434 | UnwindData |  |
| 1040 | `K32EnumProcesses` | `0x13BEB0` | 434 | UnwindData |  |
| 905 | `GetWsChanges` | `0x13C070` | 32 | UnwindData |  |
| 1056 | `K32GetWsChanges` | `0x13C070` | 32 | UnwindData |  |
| 906 | `GetWsChangesEx` | `0x13C0A0` | 31 | UnwindData |  |
| 1057 | `K32GetWsChangesEx` | `0x13C0A0` | 31 | UnwindData |  |
| 955 | `InitializeProcessForWsWatch` | `0x13C0D0` | 81 | UnwindData |  |
| 1058 | `K32InitializeProcessForWsWatch` | `0x13C0D0` | 81 | UnwindData |  |
| 657 | `GetMappedFileNameA` | `0x13C130` | 187 | UnwindData |  |
| 1045 | `K32GetMappedFileNameA` | `0x13C130` | 187 | UnwindData |  |
| 1340 | `PsmCreateKeyWithDynamicId` | `0x13C200` | 266 | UnwindData |  |
| 1341 | `PsmEqualApplication` | `0x13C310` | 230 | UnwindData |  |
| 1342 | `PsmEqualPackage` | `0x13C400` | 131 | UnwindData |  |
| 1349 | `PsmIsChildKey` | `0x13C490` | 77 | UnwindData |  |
| 172 | `CommitStateAtom` | `0x140D70` | 279 | UnwindData |  |
| 463 | `GetAlternatePackageRoots` | `0x140E90` | 29 | UnwindData |  |
| 830 | `GetSystemStateRootFolder` | `0x140E90` | 29 | UnwindData |  |
| 1579 | `SaveAlternatePackageRootPath` | `0x140E90` | 29 | UnwindData |  |
| 1580 | `SaveStateRootFolderPath` | `0x140E90` | 29 | UnwindData |  |
| 779 | `GetRoamingLastObservedChangeTime` | `0x140EC0` | 159 | UnwindData |  |
| 790 | `GetSharedLocalFolder` | `0x140F70` | 305 | UnwindData |  |
| 801 | `GetStateContainerDepth` | `0x1410B0` | 159 | UnwindData |  |
| 805 | `GetStateSettingsFolder` | `0x141160` | 305 | UnwindData |  |
| 806 | `GetStateVersion` | `0x1412A0` | 468 | UnwindData |  |
| 1168 | `OverrideRoamingDataModificationTimesInRange` | `0x141480` | 179 | UnwindData |  |
| 1362 | `PublishStateChangeNotification` | `0x141540` | 151 | UnwindData |  |
| 1507 | `RegisterStateLock` | `0x1415E0` | 151 | UnwindData |  |
| 1537 | `ResetState` | `0x141680` | 151 | UnwindData |  |
| 1680 | `SetRoamingLastObservedChangeTime` | `0x141720` | 159 | UnwindData |  |
| 1688 | `SetStateVersion` | `0x1417D0` | 463 | UnwindData |  |
| 1848 | `UnregisterStateChangeNotification` | `0x1419B0` | 151 | UnwindData |  |
| 1849 | `UnregisterStateLock` | `0x141A50` | 158 | UnwindData |  |
| 2 | `MsixIsSystemPackageByPackageFullName` | `0x146460` | 584 | UnwindData |  |
| 3 | `PackageSidFromProductId` | `0x1469A0` | 751 | UnwindData |  |
| 33 | `AddPackageNameAliasesByPackageDependency` | `0x14D8D0` | 250 | UnwindData |  |
| 292 | `DeletePackageDependency` | `0x14D9D0` | 326 | UnwindData |  |
| 422 | `FindPackageDependency` | `0x14DB20` | 137 | UnwindData |  |
| 546 | `GetCurrentPackageInfo_PackageNameAliases` | `0x14DBB0` | 204 | UnwindData |  |
| 635 | `GetIdForPackageDependencyContext` | `0x14DC90` | 95 | UnwindData |  |
| 701 | `GetPackageDependencyInformation` | `0x14DD00` | 251 | UnwindData |  |
| 710 | `GetPackageGraphRevisionId` | `0x14DE10` | 48 | UnwindData |  |
| 715 | `GetPackageNameAliasesByPackageFullName` | `0x14DE50` | 335 | UnwindData |  |
| 764 | `GetProcessesUsingPackageDependency` | `0x14DFB0` | 121 | UnwindData |  |
| 777 | `GetResolvedPackageFullNameForPackageDependency` | `0x14E030` | 95 | UnwindData |  |
| 778 | `GetResolvedPackageFullNameForPackageDependency2` | `0x14E0A0` | 95 | UnwindData |  |
| 1437 | `RefreshPackageInfo` | `0x14E110` | 1,021 | UnwindData |  |
| 1527 | `RemoveExtensionProgIds` | `0x14EFD0` | 1,496 | UnwindData |  |
| 57 | `AppPolicyGetCreateFileAccess` | `0x14F870` | 95 | UnwindData |  |
| 61 | `AppPolicyGetShowDeveloperDiagnostic` | `0x14F8E0` | 95 | UnwindData |  |
| 78 | `ApplicationUserModelIdFromProductId` | `0x14F950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1176 | `PackageFullNameFromProductId` | `0x14F950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1179 | `PackageIdFromProductId` | `0x14F950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1185 | `PackageRelativeApplicationIdFromProductId` | `0x14F950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1338 | `ProductIdFromPackageFamilyName` | `0x14F950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1173 | `PackageFamilyNameFromProductId` | `0x14F960` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1180 | `PackageIsEffectiveSupportedUsersMultiple` | `0x14FAF0` | 244 | UnwindData |  |
| 441 | `FormatApplicationUserModelIdA` | `0x14FBF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1170 | `PackageFamilyNameFromFullNameA` | `0x14FC00` | 130 | UnwindData |  |
| 1172 | `PackageFamilyNameFromIdA` | `0x14FC90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1175 | `PackageFullNameFromIdA` | `0x14FCA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1178 | `PackageIdFromFullNameA` | `0x14FCB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1182 | `PackageNameAndPublisherIdFromFamilyNameA` | `0x14FCD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1183 | `PackagePublisherAddUserIfNecessary` | `0x14FCE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1184 | `PackagePublisherIdFromPublisher` | `0x14FCF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1188 | `ParseApplicationUserModelIdA` | `0x14FD00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1894 | `VerifyApplicationUserModelId` | `0x14FD10` | 62 | UnwindData |  |
| 1895 | `VerifyApplicationUserModelIdA` | `0x14FD60` | 54 | UnwindData |  |
| 1897 | `VerifyPackageFamilyNameA` | `0x14FDA0` | 62 | UnwindData |  |
| 1899 | `VerifyPackageFullNameA` | `0x14FDF0` | 110 | UnwindData |  |
| 1900 | `VerifyPackageId` | `0x14FE70` | 110 | UnwindData |  |
| 1901 | `VerifyPackageIdA` | `0x14FEF0` | 110 | UnwindData |  |
| 1903 | `VerifyPackageNameA` | `0x14FF70` | 88 | UnwindData |  |
| 1905 | `VerifyPackagePublisherA` | `0x14FFD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1906 | `VerifyPackageRelativeApplicationId` | `0x14FFE0` | 58 | UnwindData |  |
| 1907 | `VerifyPackageRelativeApplicationIdA` | `0x150020` | 58 | UnwindData |  |
| 468 | `GetAppModelVersion` | `0x150060` | 281 | UnwindData |  |
| 980 | `InvalidateAppModelVersionCache` | `0x150180` | 3,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 550 | `GetCurrentPackageSecurityContext` | `0x150E50` | 108 | UnwindData |  |
| 555 | `GetCurrentTargetPlatformContext` | `0x150ED0` | 111 | UnwindData |  |
| 695 | `GetPackageApplicationContext` | `0x150F50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 699 | `GetPackageApplicationResourcesContext` | `0x150F70` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 700 | `GetPackageContext` | `0x150FC0` | 58 | UnwindData |  |
| 708 | `GetPackageGlobalizationContext` | `0x151000` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 716 | `GetPackageOSMaxVersionTested` | `0x151050` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 721 | `GetPackageProperty` | `0x151090` | 742 | UnwindData |  |
| 722 | `GetPackagePropertyString` | `0x151380` | 93 | UnwindData |  |
| 723 | `GetPackageResourcesContext` | `0x1513F0` | 1,152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 547 | `GetCurrentPackagePath` | `0x151870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 797 | `GetStagedPackageOrigin2` | `0x151890` | 470 | UnwindData |  |
| 1009 | `IsPackageFeatureSupported` | `0x151A70` | 34 | UnwindData |  |
| 1530 | `RemovePackageStatusForUser` | `0x151AA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1857 | `UpdatePackageStatusForUser` | `0x151AC0` | 196 | UnwindData |  |
| 1858 | `UpdatePackageStatusForUserSid` | `0x151B90` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 720 | `GetPackagePathOnVolume` | `0x151CC0` | 326 | UnwindData |  |
| 767 | `GetProtocolAumid` | `0x151E10` | 33 | UnwindData |  |
| 768 | `GetProtocolProperty` | `0x151E40` | 48 | UnwindData |  |
| 826 | `GetSystemMetadataPath` | `0x151E80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1363 | `PublisherFromPackageFullName` | `0x151E90` | 616 | UnwindData |  |
| 66 | `AppXGetApplicationData` | `0x153D90` | 491 | UnwindData |  |
| 67 | `AppXGetDevelopmentMode` | `0x153F90` | 239 | UnwindData |  |
| 72 | `AppXLookupDisplayName` | `0x154090` | 130 | UnwindData |  |
| 73 | `AppXLookupMoniker` | `0x154120` | 130 | UnwindData |  |
| 64 | `AppXCheckPplSupport` | `0x157C90` | 316 | UnwindData |  |
| 1513 | `ReleasePackagedDataForFile` | `0x15A6A0` | 33 | UnwindData |  |
| 1013 | `IsSideloadingEnabled` | `0x15AD90` | 80 | UnwindData |  |
| 1014 | `IsSideloadingPolicyApplied` | `0x15ADF0` | 57 | UnwindData |  |
| 1648 | `SetIsDeveloperModeEnabled` | `0x15AE30` | 69 | UnwindData |  |
| 1649 | `SetIsSideloadingEnabled` | `0x15AE80` | 69 | UnwindData |  |
| 1297 | `PcwClearCounterSetSecurity` | `0x15B180` | 88 | UnwindData |  |
| 1304 | `PcwIsNotifierAlive` | `0x15B1E0` | 72 | UnwindData |  |
| 1305 | `PcwQueryCounterSetSecurity` | `0x15B230` | 83 | UnwindData |  |
| 1311 | `PcwSetCounterSetSecurity` | `0x15B290` | 86 | UnwindData |  |
| 1322 | `PerfQueryInstance` | `0x15B360` | 207 | UnwindData |  |
| 25 | `AddConsoleAliasA` | `0x15BDD0` | 87 | UnwindData |  |
| 26 | `AddConsoleAliasW` | `0x15BF70` | 94 | UnwindData |  |
| 389 | `ExpungeConsoleCommandHistoryA` | `0x15BFE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 496 | `GetConsoleAliasA` | `0x15BFF0` | 56 | UnwindData |  |
| 497 | `GetConsoleAliasExesA` | `0x15C030` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 498 | `GetConsoleAliasExesLengthA` | `0x15C100` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 499 | `GetConsoleAliasExesLengthW` | `0x15C180` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 500 | `GetConsoleAliasExesW` | `0x15C190` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 501 | `GetConsoleAliasW` | `0x15C2D0` | 63 | UnwindData |  |
| 502 | `GetConsoleAliasesA` | `0x15C320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 503 | `GetConsoleAliasesLengthA` | `0x15C330` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 504 | `GetConsoleAliasesLengthW` | `0x15C410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 505 | `GetConsoleAliasesW` | `0x15C420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 507 | `GetConsoleCommandHistoryA` | `0x15C430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 508 | `GetConsoleCommandHistoryLengthA` | `0x15C440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 509 | `GetConsoleCommandHistoryLengthW` | `0x15C450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 510 | `GetConsoleCommandHistoryW` | `0x15C460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 518 | `GetConsoleOriginalTitleA` | `0x15C470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 519 | `GetConsoleOriginalTitleW` | `0x15C490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 525 | `GetConsoleTitleA` | `0x15C4B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1610 | `SetConsoleNumberOfCommandsA` | `0x15C4D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1616 | `SetConsoleTitleA` | `0x15C4E0` | 58 | UnwindData |  |
| 43 | `AllocConsole` | `0x15C520` | 85 | UnwindData |  |
| 444 | `FreeConsole` | `0x15C580` | 109 | UnwindData |  |
| 158 | `ClosePseudoConsole` | `0x15C630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1539 | `ResizePseudoConsole` | `0x15C640` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 396 | `FillConsoleOutputAttribute` | `0x15C770` | 36 | UnwindData |  |
| 398 | `FillConsoleOutputCharacterW` | `0x15C7A0` | 36 | UnwindData |  |
| 1417 | `ReadConsoleInputA` | `0x15C7D0` | 26 | UnwindData |  |
| 1418 | `ReadConsoleInputExA` | `0x15C7F0` | 30 | UnwindData |  |
| 1421 | `ReadConsoleOutputA` | `0x15C820` | 30 | UnwindData |  |
| 1422 | `ReadConsoleOutputAttribute` | `0x15C850` | 44 | UnwindData |  |
| 1979 | `WriteConsoleInputA` | `0x15C890` | 20 | UnwindData |  |
| 1980 | `WriteConsoleInputW` | `0x15C990` | 20 | UnwindData |  |
| 1981 | `WriteConsoleOutputA` | `0x15C9B0` | 30 | UnwindData |  |
| 1982 | `WriteConsoleOutputAttribute` | `0x15C9E0` | 44 | UnwindData |  |
| 1984 | `WriteConsoleOutputCharacterW` | `0x15CA20` | 41 | UnwindData |  |
| 1651 | `SetLastConsoleEventActive` | `0x15CA50` | 54 | UnwindData |  |
| 433 | `FlushConsoleInputBuffer` | `0x15CA90` | 101 | UnwindData |  |
| 455 | `GenerateConsoleCtrlEvent` | `0x15CB00` | 164 | UnwindData |  |
| 513 | `GetConsoleFontSize` | `0x15CBB0` | 123 | UnwindData |  |
| 514 | `GetConsoleHistoryInfo` | `0x15CC40` | 136 | UnwindData |  |
| 532 | `GetCurrentConsoleFont` | `0x15CCD0` | 130 | UnwindData |  |
| 689 | `GetNumberOfConsoleMouseButtons` | `0x15CD60` | 109 | UnwindData |  |
| 1581 | `ScrollConsoleScreenBufferA` | `0x15CDE0` | 30 | UnwindData |  |
| 1600 | `SetConsoleActiveScreenBuffer` | `0x15CE10` | 101 | UnwindData |  |
| 1605 | `SetConsoleDisplayMode` | `0x15CE80` | 145 | UnwindData |  |
| 1606 | `SetConsoleHistoryInfo` | `0x15CF20` | 136 | UnwindData |  |
| 1613 | `SetConsoleScreenBufferInfoEx` | `0x15CFB0` | 264 | UnwindData |  |
| 1614 | `SetConsoleScreenBufferSize` | `0x15D0C0` | 122 | UnwindData |  |
| 1618 | `SetConsoleWindowInfo` | `0x15D140` | 145 | UnwindData |  |
| 1416 | `ReadConsoleA` | `0x15D1E0` | 76 | UnwindData |  |
| 1818 | `TestRecoverResults` | `0x174B20` | 37,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1998 | `__FC_Query_Config` | `0x17DD10` | 87 | UnwindData |  |
| 1999 | `__FC_Query_System` | `0x17DD70` | 49 | UnwindData |  |
| 2000 | `__FC_Report` | `0x17DDB0` | 184 | UnwindData |  |
| 2001 | `__FC_Subscribe` | `0x17DE70` | 102 | UnwindData |  |
| 2002 | `__FC_Unsubscribe` | `0x17DEE0` | 52 | UnwindData |  |
| 7 | `AccessCheckByTypeAndAuditAlarmW` | `0x17DFE0` | 333 | UnwindData |  |
| 8 | `AccessCheckByTypeResultList` | `0x17E140` | 177 | UnwindData |  |
| 9 | `AccessCheckByTypeResultListAndAuditAlarmByHandleW` | `0x17E200` | 369 | UnwindData |  |
| 10 | `AccessCheckByTypeResultListAndAuditAlarmW` | `0x17E380` | 340 | UnwindData |  |
| 17 | `AddAccessAllowedObjectAce` | `0x17E4E0` | 101 | UnwindData |  |
| 19 | `AddAccessDeniedAceEx` | `0x17E550` | 78 | UnwindData |  |
| 20 | `AddAccessDeniedObjectAce` | `0x17E5B0` | 101 | UnwindData |  |
| 22 | `AddAuditAccessAce` | `0x17E620` | 58 | UnwindData |  |
| 23 | `AddAuditAccessAceEx` | `0x17E660` | 97 | UnwindData |  |
| 24 | `AddAuditAccessObjectAce` | `0x17E6D0` | 129 | UnwindData |  |
| 36 | `AddResourceAttributeAce` | `0x17E760` | 75 | UnwindData |  |
| 38 | `AddScopedPolicyIDAce` | `0x17E7C0` | 52 | UnwindData |  |
| 80 | `AreAnyAccessesGranted` | `0x17E800` | 25 | UnwindData |  |
| 187 | `ConvertToAutoInheritPrivateObjectSecurity` | `0x17E820` | 60 | UnwindData |  |
| 271 | `CveEventWrite` | `0x17E870` | 271 | UnwindData |  |
| 411 | `FindFirstFreeAce` | `0x17E990` | 52 | UnwindData |  |
| 741 | `GetPrivateObjectSecurity` | `0x17E9D0` | 52 | UnwindData |  |
| 961 | `InstallELAMCertificateInfo` | `0x17EA10` | 68 | UnwindData |  |
| 1027 | `IsValidRelativeSecurityDescriptor` | `0x17EA60` | 45 | UnwindData |  |
| 1137 | `ObjectDeleteAuditAlarmW` | `0x17EAA0` | 99 | UnwindData |  |
| 1139 | `ObjectPrivilegeAuditAlarmW` | `0x17EB10` | 132 | UnwindData |  |
| 1336 | `PrivilegedServiceAuditAlarmW` | `0x17EBA0` | 154 | UnwindData |  |
| 1585 | `SetAclInformation` | `0x17EC40` | 42 | UnwindData |  |
| 1661 | `SetPrivateObjectSecurity` | `0x17EC70` | 52 | UnwindData |  |
| 1662 | `SetPrivateObjectSecurityEx` | `0x17ECB0` | 62 | UnwindData |  |
| 349 | `EnumResourceLanguagesExA` | `0x17EE20` | 196 | UnwindData |  |
| 351 | `EnumResourceNamesA` | `0x17EEF0` | 30 | UnwindData |  |
| 352 | `EnumResourceNamesExA` | `0x17EF20` | 137 | UnwindData |  |
| 355 | `EnumResourceTypesExA` | `0x17EFB0` | 33 | UnwindData |  |
| 1541 | `ResolveDelayLoadsFromDll` | `0x17F0C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `AllocateUserPhysicalPages` | `0x17F0E0` | 42 | UnwindData |  |
| 48 | `AllocateUserPhysicalPages2` | `0x17F110` | 109 | UnwindData |  |
| 49 | `AllocateUserPhysicalPagesNuma` | `0x17F190` | 240 | UnwindData |  |
| 454 | `FreeUserPhysicalPages` | `0x17F2B0` | 42 | UnwindData |  |
| 659 | `GetMemoryErrorHandlingCapabilities` | `0x17F2E0` | 137 | UnwindData |  |
| 660 | `GetMemoryNumaClosestInitiatorNode` | `0x17F370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 661 | `GetMemoryNumaPerformanceInformation` | `0x17F370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 822 | `GetSystemFileCacheSize` | `0x17F380` | 172 | UnwindData |  |
| 1106 | `MapUserPhysicalPages` | `0x17F440` | 42 | UnwindData |  |
| 1140 | `OfferVirtualMemory` | `0x17F470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1142 | `OpenDedicatedMemoryPartition` | `0x17F490` | 94 | UnwindData |  |
| 1382 | `QueryPartitionInformation` | `0x17F500` | 82 | UnwindData |  |
| 1396 | `QueryVirtualMemoryInformation` | `0x17F560` | 80 | UnwindData |  |
| 1435 | `ReclaimVirtualMemory` | `0x17F5C0` | 339 | UnwindData |  |
| 1504 | `RegisterBadMemoryNotification` | `0x17F720` | 82 | UnwindData |  |
| 1675 | `SetProcessValidCallTargetsForMappedView` | `0x17F780` | 45 | UnwindData |  |
| 1691 | `SetSystemFileCacheSize` | `0x17F7C0` | 212 | UnwindData |  |
| 1846 | `UnregisterBadMemoryNotification` | `0x17F8A0` | 42 | UnwindData |  |
| 1911 | `VirtualAlloc2FromApp` | `0x17F8D0` | 54 | UnwindData |  |
| 1920 | `VirtualProtectFromApp` | `0x17F910` | 139 | UnwindData |  |
| 1924 | `VirtualUnlockEx` | `0x17F9B0` | 67 | UnwindData |  |
| 81 | `AreExternalFeatureDependenciesEnabled` | `0x17FA00` | 110 | UnwindData |  |
| 1633 | `SetFileApisToANSI` | `0x187950` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1634 | `SetFileApisToOEM` | `0x187990` | 1,664 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `Beep` | `0x188010` | 278 | UnwindData |  |
| 285 | `DeleteEnclave` | `0x188130` | 42 | UnwindData |  |
| 1072 | `LoadEnclaveImageA` | `0x188160` | 72 | UnwindData |  |
| 1809 | `TerminateEnclave` | `0x1881B0` | 58 | UnwindData |  |
| 298 | `DeleteSynchronizationBarrier` | `0x1881F0` | 27 | UnwindData |  |
| 334 | `EnterSynchronizationBarrier` | `0x188220` | 102 | UnwindData |  |
| 960 | `InitializeSynchronizationBarrier` | `0x188290` | 60 | UnwindData |  |
| 273 | `DebugActiveProcess` | `0x188370` | 123 | UnwindData |  |
| 274 | `DebugActiveProcessStop` | `0x188400` | 108 | UnwindData |  |
| 483 | `GetCommConfig` | `0x188590` | 603 | UnwindData |  |
| 484 | `GetCommMask` | `0x188800` | 225 | UnwindData |  |
| 486 | `GetCommPorts` | `0x1888F0` | 710 | UnwindData |  |
| 489 | `GetCommTimeouts` | `0x188BC0` | 311 | UnwindData |  |
| 1141 | `OpenCommPort` | `0x188D00` | 294 | UnwindData |  |
| 1590 | `SetCommBreak` | `0x188E30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1591 | `SetCommConfig` | `0x188E40` | 251 | UnwindData |  |
| 1593 | `SetCommState` | `0x188F50` | 1,087 | UnwindData |  |
| 1727 | `SetupComm` | `0x1893A0` | 289 | UnwindData |  |
| 1830 | `TransmitCommChar` | `0x1894D0` | 221 | UnwindData |  |
| 181 | `ConvertAuxiliaryCounterToPerformanceCounter` | `0x1895C0` | 94 | UnwindData |  |
| 184 | `ConvertPerformanceCounterToAuxiliaryCounter` | `0x189630` | 94 | UnwindData |  |
| 825 | `GetSystemLeapSecondInformation` | `0x1896A0` | 112 | UnwindData |  |
| 833 | `GetSystemTimeAdjustmentPrecise` | `0x189720` | 139 | UnwindData |  |
| 1369 | `QueryAuxiliaryCounterFrequency` | `0x1897C0` | 62 | UnwindData |  |
| 1589 | `SetClientTimeZoneInformation` | `0x189810` | 369 | UnwindData |  |
| 1624 | `SetDynamicTimeZoneInformation` | `0x189990` | 202 | UnwindData |  |
| 1653 | `SetLocalTime` | `0x189A60` | 255 | UnwindData |  |
| 1692 | `SetSystemTime` | `0x189B70` | 262 | UnwindData |  |
| 1693 | `SetSystemTimeAdjustment` | `0x189C80` | 69 | UnwindData |  |
| 1694 | `SetSystemTimeAdjustmentPrecise` | `0x189CD0` | 102 | UnwindData |  |
| 1719 | `SetTimeZoneInformation` | `0x189D40` | 435 | UnwindData |  |
| 1838 | `TzSpecificLocalTimeToSystemTimeEx` | `0x189F00` | 622 | UnwindData |  |
| 247 | `CreateRemoteThread` | `0x18A180` | 60 | UnwindData |  |
| 258 | `CreateThread` | `0x18A1D0` | 65 | UnwindData |  |
| 863 | `GetThreadSelectedCpuSetMasks` | `0x18A220` | 209 | UnwindData |  |
| 864 | `GetThreadSelectedCpuSets` | `0x18A300` | 211 | UnwindData |  |
| 1707 | `SetThreadSelectedCpuSetMasks` | `0x18A3E0` | 210 | UnwindData |  |
| 1708 | `SetThreadSelectedCpuSets` | `0x18A4C0` | 208 | UnwindData |  |
| 1975 | `Wow64SetThreadContext` | `0x18A5A0` | 42 | UnwindData |  |
| 198 | `CreateAppSiloToken` | `0x18BAD0` | 493 | UnwindData |  |
| 201 | `CreateDirectory2A` | `0x18BD10` | 121 | UnwindData |  |
| 202 | `CreateDirectory2W` | `0x18BD90` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1521 | `RemoveDirectory2A` | `0x18BFD0` | 73 | UnwindData |  |
| 1522 | `RemoveDirectory2W` | `0x18C020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 216 | `CreateFile3` | `0x18C030` | 33 | UnwindData |  |
| 219 | `CreateFileMapping2` | `0x18C060` | 421 | UnwindData |  |
| 1113 | `MapViewOfFileNuma2` | `0x18C210` | 185 | UnwindData |  |
| 224 | `CreateHardLinkA` | `0x18C2D0` | 156 | UnwindData |  |
| 1639 | `SetFileIoOverlappedRange` | `0x18C380` | 114 | UnwindData |  |
| 392 | `FatalAppExitA` | `0x18CAC0` | 137 | UnwindData |  |
| 393 | `FatalAppExitW` | `0x18CB50` | 139 | UnwindData |  |
| 744 | `GetProcessDefaultCpuSetMasks` | `0x18D0A0` | 209 | UnwindData |  |
| 745 | `GetProcessDefaultCpuSets` | `0x18D180` | 211 | UnwindData |  |
| 759 | `GetProcessShutdownParameters` | `0x18D260` | 152 | UnwindData |  |
| 780 | `GetRuntimeAttestationReport` | `0x18D300` | 244 | UnwindData |  |
| 815 | `GetSystemCpuSetInformation` | `0x18D400` | 105 | UnwindData |  |
| 1010 | `IsProcessCritical` | `0x18D470` | 88 | UnwindData |  |
| 1122 | `NeedCurrentDirectoryForExePathA` | `0x18D4D0` | 46 | UnwindData |  |
| 1385 | `QueryProcessAffinityUpdateMode` | `0x18D650` | 87 | UnwindData |  |
| 1664 | `SetProcessDefaultCpuSetMasks` | `0x18D6B0` | 210 | UnwindData |  |
| 1665 | `SetProcessDefaultCpuSets` | `0x18D790` | 208 | UnwindData |  |
| 1666 | `SetProcessDynamicEHContinuationTargets` | `0x18D870` | 74 | UnwindData |  |
| 1667 | `SetProcessDynamicEnforcedCetCompatibleRanges` | `0x18D8C0` | 74 | UnwindData |  |
| 287 | `DeleteFile2A` | `0x18DBD0` | 73 | UnwindData |  |
| 288 | `DeleteFile2W` | `0x18DC20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 311 | `DnsHostnameToComputerNameExW` | `0x18DC30` | 263 | UnwindData |  |
| 1595 | `SetComputerNameA` | `0x18DDA0` | 161 | UnwindData |  |
| 1596 | `SetComputerNameEx2W` | `0x18DE50` | 276 | UnwindData |  |
| 1597 | `SetComputerNameExA` | `0x18DF70` | 123 | UnwindData |  |
| 1598 | `SetComputerNameExW` | `0x18E000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1599 | `SetComputerNameW` | `0x18E010` | 206 | UnwindData |  |
| 403 | `FindFirstChangeNotificationA` | `0x18E150` | 96 | UnwindData |  |
| 464 | `GetApiSetModuleBaseName` | `0x18E200` | 297 | UnwindData |  |
| 562 | `GetDeveloperDriveEnablementState` | `0x18E400` | 159 | UnwindData |  |
| 571 | `GetDiskSpaceInformationA` | `0x18E890` | 108 | UnwindData |  |
| 572 | `GetDiskSpaceInformationW` | `0x18E910` | 450 | UnwindData |  |
| 573 | `GetDiskSpaceInformationWCOS` | `0x18EAE0` | 590 | UnwindData |  |
| 846 | `GetTempPath2A` | `0x18ED40` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 683 | `GetNumaNodeProcessorMask2` | `0x18EE00` | 436 | UnwindData |  |
| 685 | `GetNumaProximityNodeEx` | `0x18EFC0` | 88 | UnwindData |  |
| 749 | `GetProcessHeaps` | `0x18F140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 930 | `HeapSummary` | `0x18F160` | 200 | UnwindData |  |
| 917 | `GuardCheckLongJumpTarget` | `0x18F230` | 100 | UnwindData |  |
| 1376 | `QueryIdleProcessorCycleTimeEx` | `0x18F2A0` | 98 | UnwindData |  |
| 1412 | `RaiseCustomSystemEventTrigger` | `0x18F310` | 26 | UnwindData |  |
| 1811 | `TerminateProcessOnMemoryExhaustion` | `0x18F380` | 490 | UnwindData |  |
| 1823 | `TlsGetValue` | `0x195C40` | 107 | UnwindData |  |
| 2007 | `__wargv` | `0x3A3208` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2003 | `__argc` | `0x3A3210` | 0 | Indeterminate |  |
