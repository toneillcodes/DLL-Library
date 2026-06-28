# Binary Specification: KernelBase.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\KernelBase.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c7a7123a06c728989606c8caba989e68a59180aa8eb8bc712eebb3d59db6e3a1`
* **Total Exported Functions:** 2034

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
| 874 | `GetTraceEnableFlags` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.EtwGetTraceEnableFlags` |
| 875 | `GetTraceEnableLevel` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.EtwGetTraceEnableLevel` |
| 876 | `GetTraceLoggerHandle` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.EtwGetTraceLoggerHandle` |
| 919 | `HeapAlloc` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlAllocateHeap` |
| 923 | `HeapFree` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlFreeHeap` |
| 926 | `HeapReAlloc` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlReAllocateHeap` |
| 928 | `HeapSize` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlSizeHeap` |
| 944 | `InitOnceInitialize` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlRunOnceInitialize` |
| 946 | `InitializeConditionVariable` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlInitializeConditionVariable` |
| 949 | `InitializeCriticalSection` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlInitializeCriticalSection` |
| 955 | `InitializeSListHead` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlInitializeSListHead` |
| 956 | `InitializeSRWLock` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlInitializeSRWLock` |
| 961 | `InterlockedFlushSList` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlInterlockedFlushSList` |
| 962 | `InterlockedPopEntrySList` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlInterlockedPopEntrySList` |
| 963 | `InterlockedPushEntrySList` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlInterlockedPushEntrySList` |
| 964 | `InterlockedPushListSList` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlInterlockedPushListSList` |
| 965 | `InterlockedPushListSListEx` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlInterlockedPushListSListEx` |
| 1015 | `IsThreadpoolTimerSet` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpIsTimerSet` |
| 1066 | `LeaveCriticalSection` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlLeaveCriticalSection` |
| 1067 | `LeaveCriticalSectionWhenCallbackReturns` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpCallbackLeaveCriticalSectionOnCompletion` |
| 1130 | `NotifyFeatureToggleUsage` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlNotifyFeatureToggleUsage` |
| 1367 | `QueryDepthSList` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlQueryDepthSList` |
| 1380 | `QueryPerformanceCounter` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlQueryPerformanceCounter` |
| 1381 | `QueryPerformanceFrequency` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlQueryPerformanceFrequency` |
| 1391 | `QueryUnbiasedInterruptTime` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlQueryUnbiasedInterruptTime` |
| 1505 | `RegisterTraceGuidsW` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.EtwRegisterTraceGuidsW` |
| 1509 | `ReleaseMutexWhenCallbackReturns` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpCallbackReleaseMutexOnCompletion` |
| 1512 | `ReleaseSRWLockExclusive` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlReleaseSRWLockExclusive` |
| 1513 | `ReleaseSRWLockShared` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlReleaseSRWLockShared` |
| 1515 | `ReleaseSemaphoreWhenCallbackReturns` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpCallbackReleaseSemaphoreOnCompletion` |
| 1528 | `RemoveVectoredContinueHandler` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlRemoveVectoredContinueHandler` |
| 1529 | `RemoveVectoredExceptionHandler` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlRemoveVectoredExceptionHandler` |
| 1540 | `RestoreLastError` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlRestoreLastWin32Error` |
| 1616 | `SetCriticalSectionSpinCount` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlSetCriticalSectionSpinCount` |
| 1628 | `SetEventWhenCallbackReturns` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpCallbackSetEventOnCompletion` |
| 1649 | `SetLastError` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlSetLastWin32Error` |
| 1710 | `SetThreadpoolThreadMaximum` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpSetPoolMaxThreads` |
| 1712 | `SetThreadpoolTimer` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpSetTimer` |
| 1713 | `SetThreadpoolTimerEx` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpSetTimerEx` |
| 1714 | `SetThreadpoolWait` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpSetWait` |
| 1715 | `SetThreadpoolWaitEx` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpSetWaitEx` |
| 1733 | `StartThreadpoolIo` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpStartAsyncIoOperation` |
| 1795 | `SubmitThreadpoolWork` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpPostWork` |
| 1823 | `TraceEvent` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.EtwLogTraceEvent` |
| 1824 | `TraceMessage` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.EtwTraceMessage` |
| 1825 | `TraceMessageVa` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.EtwTraceMessageVa` |
| 1828 | `TryAcquireSRWLockExclusive` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlTryAcquireSRWLockExclusive` |
| 1829 | `TryAcquireSRWLockShared` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlTryAcquireSRWLockShared` |
| 1832 | `TryEnterCriticalSection` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlTryEnterCriticalSection` |
| 1847 | `UnregisterTraceGuids` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.EtwUnregisterTraceGuids` |
| 1890 | `VerSetConditionMask` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.VerSetConditionMask` |
| 1932 | `WaitForThreadpoolIoCallbacks` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpWaitForIoCompletion` |
| 1933 | `WaitForThreadpoolTimerCallbacks` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpWaitForTimer` |
| 1934 | `WaitForThreadpoolWaitCallbacks` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpWaitForWait` |
| 1935 | `WaitForThreadpoolWorkCallbacks` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpWaitForWork` |
| 1939 | `WakeAllConditionVariable` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlWakeAllConditionVariable` |
| 1940 | `WakeByAddressAll` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlWakeAddressAll` |
| 1941 | `WakeByAddressSingle` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlWakeAddressSingle` |
| 1942 | `WakeConditionVariable` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlWakeConditionVariable` |
| 1994 | `__C_specific_handler` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.__C_specific_handler` |
| 2001 | `__chkstk` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.__chkstk` |
| 2003 | `__misaligned_access` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.__misaligned_access` |
| 2013 | `_local_unwind` | `0x0` | - | Forwarded | Forwarded to: `NTDLL._local_unwind` |
| 1229 | `PathFindFileNameW` | `0x3A70` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1830 | `TryCreatePackageDependency` | `0x3B20` | 109 | UnwindData |  |
| 1831 | `TryCreatePackageDependency2` | `0x3C30` | 429 | UnwindData |  |
| 1270 | `PathRelativePathToW` | `0x3EB0` | 607 | UnwindData |  |
| 1231 | `PathFindNextComponentW` | `0x4120` | 91 | UnwindData |  |
| 1243 | `PathIsPrefixW` | `0x4340` | 86 | UnwindData |  |
| 1220 | `PathCommonPrefixW` | `0x43A0` | 74 | UnwindData |  |
| 1249 | `PathIsSameRootW` | `0x4560` | 116 | UnwindData |  |
| 1272 | `PathRemoveBackslashW` | `0x45E0` | 149 | UnwindData |  |
| 137 | `CharPrevW` | `0x4680` | 194 | UnwindData |  |
| 1284 | `PathSkipRootW` | `0x53D0` | 74 | UnwindData |  |
| 1278 | `PathRemoveFileSpecW` | `0x5420` | 328 | UnwindData |  |
| 1214 | `PathCchSkipRoot` | `0x5570` | 683 | UnwindData |  |
| 1209 | `PathCchRemoveBackslash` | `0x5830` | 108 | UnwindData |  |
| 1212 | `PathCchRemoveFileSpec` | `0x58B0` | 43 | UnwindData |  |
| 1210 | `PathCchRemoveBackslashEx` | `0x5C50` | 111 | UnwindData |  |
| 1208 | `PathCchIsRoot` | `0x5D20` | 636 | UnwindData |  |
| 1200 | `PathCchAddExtension` | `0x66C0` | 348 | UnwindData |  |
| 1207 | `PathCchFindExtension` | `0x6830` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `CheckIfStateChangeNotificationExists` | `0x6AB0` | 151 | UnwindData |  |
| 255 | `CreateStateLock` | `0x6E30` | 124 | UnwindData |  |
| 1471 | `RegLoadAppKeyW` | `0x7670` | 572 | UnwindData |  |
| 812 | `GetSystemAppDataFolder` | `0x79E0` | 191 | UnwindData |  |
| 732 | `GetPackagedDataForFile` | `0x7BA0` | 248 | UnwindData |  |
| 253 | `CreateStateChangeNotification` | `0x7E90` | 124 | UnwindData |  |
| 467 | `GetAppDataFolder` | `0x80C0` | 191 | UnwindData |  |
| 1725 | `SharedLocalIsEnabled` | `0x86A0` | 129 | UnwindData |  |
| 75 | `AppXPreCreationExtension` | `0x88C0` | 679 | UnwindData |  |
| 2017 | `atexit` | `0x96C0` | 24 | UnwindData |  |
| 2014 | `_onexit` | `0x97D0` | 76 | UnwindData |  |
| 942 | `InitOnceComplete` | `0x9860` | 42 | UnwindData |  |
| 2002 | `__dllonexit3` | `0x99C0` | 84 | UnwindData |  |
| 803 | `GetStateRootFolderBase` | `0x9DF0` | 191 | UnwindData |  |
| 813 | `GetSystemAppDataKey` | `0xA060` | 205 | UnwindData |  |
| 801 | `GetStateFolder` | `0xA420` | 204 | UnwindData |  |
| 802 | `GetStateRootFolder` | `0xA830` | 191 | UnwindData |  |
| 771 | `GetPublisherCacheFolder` | `0xAE40` | 128 | UnwindData |  |
| 34 | `AddPackageNameAliasesByPackageFullName` | `0xB3E0` | 365 | UnwindData |  |
| 1899 | `VerifyPackageName` | `0xBA80` | 93 | UnwindData |  |
| 781 | `GetSecureSystemAppDataFolder` | `0xC200` | 191 | UnwindData |  |
| 772 | `GetPublisherRootFolder` | `0xC520` | 191 | UnwindData |  |
| 1443 | `RegDeleteKeyExA` | `0xCB80` | 21 | UnwindData |  |
| 1444 | `RegDeleteKeyExInternalA` | `0xCBA0` | 152 | UnwindData |  |
| 296 | `DeleteStateContainer` | `0xCC40` | 159 | UnwindData |  |
| 1449 | `RegDeleteTreeA` | `0xCDB0` | 96 | UnwindData |  |
| 297 | `DeleteStateContainerValue` | `0xCE20` | 176 | UnwindData |  |
| 1450 | `RegDeleteTreeW` | `0xD3D0` | 811 | UnwindData |  |
| 1446 | `RegDeleteKeyExW` | `0xD710` | 21 | UnwindData |  |
| 1445 | `RegDeleteKeyExInternalW` | `0xD730` | 325 | UnwindData |  |
| 1448 | `RegDeleteKeyValueW` | `0xDD90` | 92 | UnwindData |  |
| 1452 | `RegDeleteValueW` | `0xDE00` | 621 | UnwindData |  |
| 1817 | `TestUnlockData` | `0xE640` | 90 | UnwindData |  |
| 644 | `GetLengthSid` | `0x13D90` | 43 | UnwindData |  |
| 51 | `AppContainerFreeMemory` | `0x13E60` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `AppXFreeMemory` | `0x13E60` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1814 | `TestQueryData` | `0x13FF0` | 68 | UnwindData |  |
| 423 | `FindPackagesByPackageFamily` | `0x164D0` | 51 | UnwindData |  |
| 798 | `GetStagedPackagePathByFullName2` | `0x165D0` | 87 | UnwindData |  |
| 796 | `GetStagedPackageOrigin` | `0x166D0` | 121 | UnwindData |  |
| 445 | `FreeEnvironmentStringsA` | `0x1E640` | 4,864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 446 | `FreeEnvironmentStringsW` | `0x1E640` | 4,864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1989 | `WriteStateContainerValue` | `0x1F940` | 215 | UnwindData |  |
| 256 | `CreateStateSubcontainer` | `0x1FEB0` | 201 | UnwindData |  |
| 1430 | `ReadStateAtomValue` | `0x20460` | 352 | UnwindData |  |
| 1431 | `ReadStateContainerValue` | `0x20740` | 328 | UnwindData |  |
| 1457 | `RegEnumValueW` | `0x20F30` | 565 | UnwindData |  |
| 1388 | `QueryStateContainerItemInfo` | `0x21DA0` | 146 | UnwindData |  |
| 1560 | `SHRegEnumUSValueW` | `0x22B80` | 566 | UnwindData |  |
| 1562 | `SHRegGetBoolUSValueW` | `0x22EA0` | 698 | UnwindData |  |
| 1564 | `SHRegGetUSValueW` | `0x23160` | 302 | UnwindData |  |
| 1566 | `SHRegOpenUSKeyW` | `0x232A0` | 59 | UnwindData |  |
| 1570 | `SHRegQueryUSValueW` | `0x237B0` | 516 | UnwindData |  |
| 1550 | `SHRegCloseUSKey` | `0x239C0` | 132 | UnwindData |  |
| 370 | `EnumerateStateContainerItems` | `0x23C20` | 216 | UnwindData |  |
| 1574 | `SHRegWriteUSValueW` | `0x23E20` | 295 | UnwindData |  |
| 254 | `CreateStateContainer` | `0x23F50` | 111 | UnwindData |  |
| 324 | `DuplicateStateContainerHandle` | `0x24230` | 106 | UnwindData |  |
| 1439 | `RegCreateKeyExA` | `0x244B0` | 81 | UnwindData |  |
| 1494 | `RegSetKeyValueA` | `0x24510` | 198 | UnwindData |  |
| 1440 | `RegCreateKeyExInternalA` | `0x245E0` | 906 | UnwindData |  |
| 1496 | `RegSetValueExA` | `0x24970` | 790 | UnwindData |  |
| 1497 | `RegSetValueExW` | `0x24C90` | 1,317 | UnwindData |  |
| 1483 | `RegQueryInfoKeyA` | `0x25470` | 899 | UnwindData |  |
| 1495 | `RegSetKeyValueW` | `0x25980` | 192 | UnwindData |  |
| 1442 | `RegCreateKeyExW` | `0x25D70` | 85 | UnwindData |  |
| 1484 | `RegQueryInfoKeyW` | `0x26440` | 1,422 | UnwindData |  |
| 1441 | `RegCreateKeyExInternalW` | `0x269E0` | 1,464 | UnwindData |  |
| 1476 | `RegNotifyChangeKeyValue` | `0x276E0` | 51 | UnwindData |  |
| 1455 | `RegEnumKeyExW` | `0x27CD0` | 1,023 | UnwindData |  |
| 1481 | `RegOpenKeyExW` | `0x280E0` | 34 | UnwindData |  |
| 1480 | `RegOpenKeyExInternalW` | `0x28110` | 1,124 | UnwindData |  |
| 1102 | `MapPredefinedHandleInternal` | `0x28580` | 91 | UnwindData |  |
| 117 | `CLOSE_LOCAL_HANDLE_INTERNAL` | `0x29D30` | 11 | UnwindData |  |
| 1437 | `RegCloseKey` | `0x2A010` | 670 | UnwindData |  |
| 1461 | `RegGetValueW` | `0x2A840` | 65 | UnwindData |  |
| 1488 | `RegQueryValueExW` | `0x2B1A0` | 568 | UnwindData |  |
| 1454 | `RegEnumKeyExA` | `0x2E580` | 932 | UnwindData |  |
| 1304 | `PcwRegisterCounterSet` | `0x310C0` | 90 | UnwindData |  |
| 414 | `FindNLSString` | `0x324E0` | 569 | UnwindData |  |
| 2024 | `lstrcmpi` | `0x32720` | 1,262 | UnwindData |  |
| 2025 | `lstrcmpiA` | `0x32720` | 1,262 | UnwindData |  |
| 150 | `ChrCmpIA` | `0x32C20` | 115 | UnwindData |  |
| 1699 | `SetThreadLocale` | `0x33AE0` | 238 | UnwindData |  |
| 141 | `CharUpperW` | `0x33CA0` | 96 | UnwindData |  |
| 128 | `CharLowerA` | `0x33D90` | 31 | UnwindData |  |
| 2023 | `lstrcmpW` | `0x33F00` | 775 | UnwindData |  |
| 130 | `CharLowerBuffW` | `0x34210` | 101 | UnwindData |  |
| 140 | `CharUpperBuffW` | `0x342A0` | 101 | UnwindData |  |
| 1264 | `PathMatchSpecW` | `0x34470` | 290 | UnwindData |  |
| 1064 | `LCMapStringW` | `0x349E0` | 367 | UnwindData |  |
| 1063 | `LCMapStringEx` | `0x34B60` | 5,969 | UnwindData |  |
| 675 | `GetNamedLocaleHashNode` | `0x36AC0` | 182 | UnwindData |  |
| 1931 | `WaitForSingleObjectEx` | `0x37600` | 344 | UnwindData |  |
| 175 | `CompareStringA` | `0x37D20` | 104 | UnwindData |  |
| 1116 | `MultiByteToWideChar` | `0x392B0` | 7,154 | UnwindData |  |
| 1626 | `SetErrorMode` | `0x3BDC0` | 167 | UnwindData |  |
| 476 | `GetCPHashNode` | `0x3BE70` | 51 | UnwindData |  |
| 1074 | `LoadLibraryExW` | `0x3C960` | 482 | UnwindData |  |
| 449 | `FreeLibrary` | `0x3CB50` | 85 | UnwindData |  |
| 1079 | `LoadStringBaseExW` | `0x3CC40` | 187 | UnwindData |  |
| 694 | `GetOverlappedResultEx` | `0x3CDB0` | 319 | UnwindData |  |
| 756 | `GetProcessMitigationPolicy` | `0x3CF00` | 1,112 | UnwindData |  |
| 693 | `GetOverlappedResult` | `0x3D360` | 279 | UnwindData |  |
| 1368 | `QueryDosDeviceW` | `0x3D480` | 2,482 | UnwindData |  |
| 1928 | `WaitForMultipleObjects` | `0x3DE40` | 23 | UnwindData |  |
| 1929 | `WaitForMultipleObjectsEx` | `0x3DE60` | 523 | UnwindData |  |
| 932 | `HeapWalk` | `0x3E080` | 426 | UnwindData |  |
| 1730 | `SleepConditionVariableSRW` | `0x3E230` | 106 | UnwindData |  |
| 1426 | `ReadFile` | `0x3E2A0` | 545 | UnwindData |  |
| 1161 | `OpenThreadToken` | `0x3E4D0` | 42 | UnwindData |  |
| 773 | `GetQueuedCompletionStatus` | `0x3E500` | 260 | UnwindData |  |
| 941 | `InitOnceBeginInitialize` | `0x3E610` | 68 | UnwindData |  |
| 627 | `GetFullPathNameW` | `0x3E6A0` | 59 | UnwindData |  |
| 1920 | `VirtualUnlock` | `0x3E6F0` | 75 | UnwindData |  |
| 1108 | `MapViewOfFileExNuma` | `0x3E750` | 479 | UnwindData |  |
| 1146 | `OpenMutexW` | `0x3E940` | 54 | UnwindData |  |
| 873 | `GetTokenInformation` | `0x3EBD0` | 130 | UnwindData |  |
| 1637 | `SetFilePointer` | `0x3EC60` | 507 | UnwindData |  |
| 305 | `DeviceIoControl` | `0x3EE70` | 509 | UnwindData |  |
| 1104 | `MapViewOfFile` | `0x3F080` | 430 | UnwindData |  |
| 1707 | `SetThreadToken` | `0x3F240` | 83 | UnwindData |  |
| 1729 | `SleepConditionVariableCS` | `0x3F2A0` | 106 | UnwindData |  |
| 1151 | `OpenProcess` | `0x3F310` | 120 | UnwindData |  |
| 1095 | `LockFileEx` | `0x3F390` | 204 | UnwindData |  |
| 670 | `GetModuleHandleExW` | `0x3F470` | 104 | UnwindData |  |
| 761 | `GetProcessVersion` | `0x3F5D0` | 314 | UnwindData |  |
| 1152 | `OpenProcessToken` | `0x3F710` | 46 | UnwindData |  |
| 603 | `GetFileAttributesExW` | `0x3F750` | 116 | UnwindData |  |
| 606 | `GetFileInformationByHandleEx` | `0x3F900` | 202 | UnwindData |  |
| 1937 | `WaitNamedPipeW` | `0x3FC40` | 111 | UnwindData |  |
| 1081 | `LoadStringW` | `0x400E0` | 184 | UnwindData |  |
| 590 | `GetErrorMode` | `0x40240` | 88 | UnwindData |  |
| 1638 | `SetFilePointerEx` | `0x402A0` | 347 | UnwindData |  |
| 1514 | `ReleaseSemaphore` | `0x40410` | 42 | UnwindData |  |
| 575 | `GetDriveTypeW` | `0x40BD0` | 390 | UnwindData |  |
| 154 | `CloseHandle` | `0x41EB0` | 229 | UnwindData |  |
| 217 | `CreateFileA` | `0x41FA0` | 336 | UnwindData |  |
| 897 | `GetVolumeNameForVolumeMountPointW` | `0x42100` | 534 | UnwindData |  |
| 214 | `CreateFile2` | `0x42C50` | 55 | UnwindData |  |
| 223 | `CreateFileW` | `0x43280` | 210 | UnwindData |  |
| 1731 | `SleepEx` | `0x43360` | 236 | UnwindData |  |
| 460 | `GetAce` | `0x43F40` | 46 | UnwindData |  |
| 1028 | `IsWellKnownSid` | `0x43F80` | 76 | UnwindData |  |
| 625 | `GetFinalPathNameByHandleW` | `0x44640` | 115 | UnwindData |  |
| 706 | `GetPackageFullName` | `0x45710` | 225 | UnwindData |  |
| 707 | `GetPackageFullNameFromToken` | `0x46B60` | 217 | UnwindData |  |
| 702 | `GetPackageFamilyName` | `0x46F00` | 328 | UnwindData |  |
| 579 | `GetEffectivePackageStatusForUser` | `0x477F0` | 114 | UnwindData |  |
| 727 | `GetPackageStatus` | `0x47870` | 1,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1174 | `PackageIdFromFullName` | `0x47E40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 826 | `GetSystemMetadataPathForPackage` | `0x47E60` | 119 | UnwindData |  |
| 1895 | `VerifyPackageFullName` | `0x48010` | 112 | UnwindData |  |
| 1166 | `PackageFamilyNameFromFullName` | `0x486E0` | 98 | UnwindData |  |
| 1178 | `PackageNameAndPublisherIdFromFamilyName` | `0x4B5A0` | 819 | UnwindData |  |
| 1197 | `PathCanonicalizeW` | `0x4C9A0` | 93 | UnwindData |  |
| 1195 | `PathAppendW` | `0x4CA40` | 223 | UnwindData |  |
| 1216 | `PathCchStripToRoot` | `0x4CB30` | 920 | UnwindData |  |
| 1201 | `PathCchAppend` | `0x4CED0` | 241 | UnwindData |  |
| 1205 | `PathCchCombine` | `0x4D220` | 20 | UnwindData |  |
| 1193 | `PathAllocCombine` | `0x4D240` | 303 | UnwindData |  |
| 1883 | `UrlUnescapeW` | `0x4D480` | 97 | UnwindData |  |
| 1202 | `PathCchAppendEx` | `0x4DCB0` | 283 | UnwindData |  |
| 1206 | `PathCchCombineEx` | `0x4DDE0` | 90 | UnwindData |  |
| 671 | `GetModuleHandleW` | `0x4F390` | 12 | UnwindData |  |
| 742 | `GetProcAddress` | `0x4F420` | 13 | UnwindData |  |
| 1086 | `LocalFree` | `0x4F580` | 349 | UnwindData |  |
| 1767 | `StrDupW` | `0x4F780` | 24 | UnwindData |  |
| 1082 | `LocalAlloc` | `0x4F840` | 542 | UnwindData |  |
| 1227 | `PathFindExtensionW` | `0x50320` | 119 | UnwindData |  |
| 2032 | `lstrlenW` | `0x503A0` | 35 | UnwindData |  |
| 151 | `ChrCmpIW` | `0x503D0` | 66 | UnwindData |  |
| 1549 | `SHLoadIndirectStringInternal` | `0x50640` | 178 | UnwindData |  |
| 1782 | `StrStrIW` | `0x50D60` | 42 | UnwindData |  |
| 966 | `InternalLcidToName` | `0x51200` | 504 | UnwindData |  |
| 178 | `CompareStringW` | `0x54470` | 3,298 | UnwindData |  |
| 176 | `CompareStringEx` | `0x55170` | 466 | UnwindData |  |
| 471 | `GetApplicationUserModelId` | `0x57470` | 180 | UnwindData |  |
| 472 | `GetApplicationUserModelIdFromToken` | `0x57530` | 176 | UnwindData |  |
| 705 | `GetPackageFamilyNameFromToken` | `0x57E60` | 829 | UnwindData |  |
| 794 | `GetSidSubAuthority` | `0x581B0` | 56 | UnwindData |  |
| 197 | `CreateAppContainerToken` | `0x581F0` | 35 | UnwindData |  |
| 1475 | `RegLoadMUIStringW` | `0x5A450` | 121 | UnwindData |  |
| 1548 | `SHLoadIndirectString` | `0x5A7C0` | 509 | UnwindData |  |
| 1080 | `LoadStringByReference` | `0x5A9D0` | 3,729 | UnwindData |  |
| 1993 | `_OpenMuiStringCache` | `0x5B870` | 645 | UnwindData |  |
| 1225 | `PathFileExistsW` | `0x5BD10` | 78 | UnwindData |  |
| 655 | `GetLongPathNameW` | `0x5BD70` | 2,037 | UnwindData |  |
| 410 | `FindFirstFileW` | `0x5C570` | 50 | UnwindData |  |
| 408 | `FindFirstFileExW` | `0x5C5B0` | 45 | UnwindData |  |
| 401 | `FindClose` | `0x5CD10` | 281 | UnwindData |  |
| 600 | `GetFileAttributesA` | `0x5CE30` | 156 | UnwindData |  |
| 604 | `GetFileAttributesW` | `0x5CEE0` | 375 | UnwindData |  |
| 1992 | `_GetMUIStringFromCache` | `0x5D120` | 789 | UnwindData |  |
| 791 | `GetShortPathNameW` | `0x5D440` | 1,207 | UnwindData |  |
| 1153 | `OpenRegKey` | `0x5DC90` | 783 | UnwindData |  |
| 1889 | `VerQueryValueW` | `0x5E510` | 23 | UnwindData |  |
| 1744 | `StrChrIW` | `0x5EBA0` | 691 | UnwindData |  |
| 1752 | `StrCmpIW` | `0x5EE60` | 50 | UnwindData |  |
| 888 | `GetUserOverrideString` | `0x5F810` | 116 | UnwindData |  |
| 889 | `GetUserOverrideWord` | `0x60030` | 233 | UnwindData |  |
| 1125 | `NlsIsUserDefaultLocale` | `0x602D0` | 32 | UnwindData |  |
| 881 | `GetUserDefaultLCID` | `0x60300` | 74 | UnwindData |  |
| 2026 | `lstrcmpiW` | `0x60350` | 1,268 | UnwindData |  |
| 810 | `GetStringTypeExW` | `0x60850` | 3,848 | UnwindData |  |
| 1128 | `NlsValidateLocale` | `0x63180` | 545 | UnwindData |  |
| 1962 | `WideCharToMultiByte` | `0x63E90` | 6,395 | UnwindData |  |
| 1871 | `UrlGetLocationW` | `0x66880` | 132 | UnwindData |  |
| 1881 | `UrlIsW` | `0x66DA0` | 49 | UnwindData |  |
| 1759 | `StrCmpNICW` | `0x67390` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1866 | `UrlCreateFromPathW` | `0x67590` | 189 | UnwindData |  |
| 1258 | `PathIsURLW` | `0x67F00` | 18 | UnwindData |  |
| 1256 | `PathIsUNCW` | `0x68190` | 21 | UnwindData |  |
| 1873 | `UrlGetPartW` | `0x682D0` | 791 | UnwindData |  |
| 1223 | `PathCreateFromUrlW` | `0x685F0` | 29 | UnwindData |  |
| 131 | `CharLowerW` | `0x69380` | 96 | UnwindData |  |
| 1868 | `UrlEscapeW` | `0x6A5B0` | 29 | UnwindData |  |
| 1862 | `UrlCombineW` | `0x6B750` | 43 | UnwindData |  |
| 1860 | `UrlCanonicalizeW` | `0x6B800` | 537 | UnwindData |  |
| 1882 | `UrlUnescapeA` | `0x6FFC0` | 361 | UnwindData |  |
| 1217 | `PathCombineA` | `0x702D0` | 56 | UnwindData |  |
| 1287 | `PathStripToRootA` | `0x70310` | 34 | UnwindData |  |
| 1738 | `StrCatBuffA` | `0x70340` | 43 | UnwindData |  |
| 1196 | `PathCanonicalizeA` | `0x70450` | 82 | UnwindData |  |
| 1279 | `PathRenameExtensionA` | `0x704B0` | 113 | UnwindData |  |
| 1226 | `PathFindExtensionA` | `0x70530` | 68 | UnwindData |  |
| 1766 | `StrDupA` | `0x705B0` | 102 | UnwindData |  |
| 1861 | `UrlCombineA` | `0x70820` | 43 | UnwindData |  |
| 1262 | `PathMatchSpecExA` | `0x70860` | 37 | UnwindData |  |
| 1277 | `PathRemoveFileSpecA` | `0x70890` | 90 | UnwindData |  |
| 981 | `IsCharAlphaA` | `0x70E70` | 234 | UnwindData |  |
| 982 | `IsCharAlphaNumericA` | `0x71110` | 239 | UnwindData |  |
| 138 | `CharUpperA` | `0x71210` | 251 | UnwindData |  |
| 139 | `CharUpperBuffA` | `0x71360` | 351 | UnwindData |  |
| 1872 | `UrlGetPartA` | `0x714D0` | 576 | UnwindData |  |
| 1194 | `PathAppendA` | `0x718B0` | 86 | UnwindData |  |
| 1754 | `StrCmpNA` | `0x71A50` | 116 | UnwindData |  |
| 135 | `CharPrevA` | `0x72390` | 68 | UnwindData |  |
| 1780 | `StrStrA` | `0x72450` | 280 | UnwindData |  |
| 1236 | `PathGetDriveNumberA` | `0x72570` | 77 | UnwindData |  |
| 1781 | `StrStrIA` | `0x725D0` | 220 | UnwindData |  |
| 1228 | `PathFindFileNameA` | `0x726C0` | 28 | UnwindData |  |
| 1743 | `StrChrIA` | `0x727E0` | 1,376 | UnwindData |  |
| 996 | `IsDBCSLeadByte` | `0x72D50` | 81 | UnwindData |  |
| 1742 | `StrChrA_MB` | `0x72FC0` | 120 | UnwindData |  |
| 1741 | `StrChrA` | `0x73040` | 526 | UnwindData |  |
| 132 | `CharNextA` | `0x73260` | 140 | UnwindData |  |
| 2030 | `lstrlen` | `0x73370` | 35 | UnwindData |  |
| 2031 | `lstrlenA` | `0x73370` | 35 | UnwindData |  |
| 477 | `GetCPInfo` | `0x733A0` | 528 | UnwindData |  |
| 458 | `GetAcceptLanguagesA` | `0x737F0` | 243 | UnwindData |  |
| 1145 | `OpenGlobalizationUserSettingsKey` | `0x73C50` | 193 | UnwindData |  |
| 1493 | `RegSetKeySecurity` | `0x73D20` | 1,712 | UnwindData |  |
| 1460 | `RegGetValueA` | `0x74410` | 1,157 | UnwindData |  |
| 1487 | `RegQueryValueExA` | `0x74BE0` | 1,047 | UnwindData |  |
| 1478 | `RegOpenKeyExA` | `0x75000` | 34 | UnwindData |  |
| 1479 | `RegOpenKeyExInternalA` | `0x75030` | 765 | UnwindData |  |
| 306 | `DisablePredefinedHandleTableInternal` | `0x75340` | 156 | UnwindData |  |
| 1453 | `RegDisablePredefinedCacheEx` | `0x75440` | 29 | UnwindData |  |
| 823 | `GetSystemInfo` | `0x77810` | 197 | UnwindData |  |
| 1508 | `ReleaseMutex` | `0x77A40` | 44 | UnwindData |  |
| 1500 | `RegisterApplicationRestart` | `0x78190` | 396 | UnwindData |  |
| 1842 | `UnregisterApplicationRestart` | `0x78330` | 335 | UnwindData |  |
| 1030 | `IsWow64Process` | `0x78D80` | 94 | UnwindData |  |
| 1913 | `VirtualFreeEx` | `0x791E0` | 212 | UnwindData |  |
| 750 | `GetProcessId` | `0x79C40` | 85 | UnwindData |  |
| 323 | `DuplicateHandle` | `0x79CA0` | 155 | UnwindData |  |
| 855 | `GetThreadId` | `0x79DC0` | 85 | UnwindData |  |
| 1987 | `WriteProcessMemory` | `0x79E20` | 875 | UnwindData |  |
| 364 | `EnumSystemLocalesW` | `0x7A1A0` | 34 | UnwindData |  |
| 807 | `GetStringScripts` | `0x7A3C0` | 598 | UnwindData |  |
| 362 | `EnumSystemLocalesA` | `0x7A670` | 33 | UnwindData |  |
| 363 | `EnumSystemLocalesEx` | `0x7A6A0` | 51 | UnwindData |  |
| 1539 | `ResolveLocaleName` | `0x7A770` | 1,471 | UnwindData |  |
| 972 | `Internal_EnumSystemLocales` | `0x7B110` | 2,327 | UnwindData |  |
| 354 | `EnumResourceNamesW` | `0x7BFA0` | 34 | UnwindData |  |
| 1887 | `VerLanguageNameW` | `0x7C2D0` | 236 | UnwindData |  |
| 353 | `EnumResourceNamesExW` | `0x7C600` | 38 | UnwindData |  |
| 478 | `GetCPInfoExW` | `0x7C630` | 502 | UnwindData |  |
| 808 | `GetStringTableEntry` | `0x7C830` | 664 | UnwindData |  |
| 424 | `FindResourceExW` | `0x7E4D0` | 354 | UnwindData |  |
| 92 | `BaseDllMapResourceIdW` | `0x7E640` | 347 | UnwindData |  |
| 91 | `BaseDllFreeResourceId` | `0x7E7B0` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1077 | `LoadResource` | `0x7E920` | 124 | UnwindData |  |
| 350 | `EnumResourceLanguagesExW` | `0x7F730` | 51 | UnwindData |  |
| 417 | `FindNextFileA` | `0x7F770` | 336 | UnwindData |  |
| 419 | `FindNextFileW` | `0x7FB60` | 750 | UnwindData |  |
| 576 | `GetDurationFormatEx` | `0x7FF30` | 165 | UnwindData |  |
| 338 | `EnumDateFormatsExEx` | `0x800B0` | 89 | UnwindData |  |
| 968 | `Internal_EnumDateFormats` | `0x80110` | 429 | UnwindData |  |
| 365 | `EnumTimeFormatsEx` | `0x802D0` | 84 | UnwindData |  |
| 973 | `Internal_EnumTimeFormats` | `0x80330` | 176 | UnwindData |  |
| 480 | `GetCalendar` | `0x80A10` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1122 | `NlsDispatchAnsiEnumProc` | `0x80A70` | 437 | UnwindData |  |
| 974 | `Internal_EnumUILanguages` | `0x80C30` | 2,031 | UnwindData |  |
| 335 | `EnumCalendarInfoExEx` | `0x815C0` | 117 | UnwindData |  |
| 967 | `Internal_EnumCalendarInfo` | `0x81640` | 4,007 | UnwindData |  |
| 589 | `GetEraNameCountedString` | `0x82620` | 291 | UnwindData |  |
| 438 | `FoldStringW` | `0x827B0` | 773 | UnwindData |  |
| 870 | `GetTimeFormatW` | `0x83120` | 264 | UnwindData |  |
| 560 | `GetDateFormatEx` | `0x83420` | 329 | UnwindData |  |
| 869 | `GetTimeFormatEx` | `0x83570` | 255 | UnwindData |  |
| 475 | `GetCPFileNameFromRegistry` | `0x83680` | 358 | UnwindData |  |
| 1020 | `IsValidCodePage` | `0x837F0` | 210 | UnwindData |  |
| 1062 | `LCMapStringA` | `0x83AA0` | 1,182 | UnwindData |  |
| 632 | `GetGeoInfoW` | `0x83F50` | 40 | UnwindData |  |
| 817 | `GetSystemDefaultLocaleName` | `0x84340` | 180 | UnwindData |  |
| 481 | `GetCalendarInfoEx` | `0x84870` | 131 | UnwindData |  |
| 646 | `GetLocaleInfoA` | `0x85410` | 62 | UnwindData |  |
| 649 | `GetLocaleInfoW` | `0x85990` | 297 | UnwindData |  |
| 647 | `GetLocaleInfoEx` | `0x85AC0` | 95 | UnwindData |  |
| 648 | `GetLocaleInfoHelper` | `0x85B30` | 16,416 | UnwindData |  |
| 262 | `CreateThreadpoolTimer` | `0x8B8C0` | 72 | UnwindData |  |
| 86 | `ArmFeatureUsageSubscriberFlushNotification` | `0x8C9F0` | 92 | UnwindData |  |
| 1813 | `TestOpen` | `0x8CF80` | 188 | UnwindData |  |
| 1812 | `TestCreate` | `0x8D1E0` | 210 | UnwindData |  |
| 153 | `ClearCommError` | `0x8DEC0` | 553 | UnwindData |  |
| 250 | `CreateSemaphoreExW` | `0x8E2A0` | 72 | UnwindData |  |
| 251 | `CreateSemaphoreW` | `0x8EC00` | 322 | UnwindData |  |
| 95 | `BaseFormatObjectAttributes` | `0x8ED50` | 599 | UnwindData |  |
| 209 | `CreateEventExA` | `0x8EFE0` | 50 | UnwindData |  |
| 230 | `CreateMutexExA` | `0x8F220` | 131 | UnwindData |  |
| 208 | `CreateEventA` | `0x8F2B0` | 66 | UnwindData |  |
| 907 | `GlobalAlloc` | `0x8F9B0` | 600 | UnwindData |  |
| 909 | `GlobalFree` | `0x8FC10` | 343 | UnwindData |  |
| 211 | `CreateEventW` | `0x8FD70` | 384 | UnwindData |  |
| 229 | `CreateMutexA` | `0x8FF00` | 142 | UnwindData |  |
| 210 | `CreateEventExW` | `0x8FFA0` | 76 | UnwindData |  |
| 1144 | `OpenFileMappingW` | `0x90140` | 54 | UnwindData |  |
| 231 | `CreateMutexExW` | `0x902B0` | 73 | UnwindData |  |
| 232 | `CreateMutexW` | `0x907B0` | 344 | UnwindData |  |
| 1154 | `OpenSemaphoreW` | `0x90910` | 246 | UnwindData |  |
| 98 | `BaseGetNamedObjectDirectory` | `0x90A10` | 87 | UnwindData |  |
| 203 | `CreateDirectoryA` | `0x91490` | 79 | UnwindData |  |
| 206 | `CreateDirectoryW` | `0x914F0` | 125 | UnwindData |  |
| 222 | `CreateFileMappingW` | `0x91600` | 672 | UnwindData |  |
| 601 | `GetFileAttributesExA` | `0x918B0` | 92 | UnwindData |  |
| 221 | `CreateFileMappingNumaW` | `0x91920` | 715 | UnwindData |  |
| 405 | `FindFirstFileA` | `0x91C00` | 424 | UnwindData |  |
| 1140 | `OpenEventA` | `0x91DB0` | 193 | UnwindData |  |
| 1141 | `OpenEventW` | `0x91E80` | 54 | UnwindData |  |
| 568 | `GetDiskFreeSpaceExA` | `0x92110` | 120 | UnwindData |  |
| 1632 | `SetFileAttributesA` | `0x92190` | 77 | UnwindData |  |
| 289 | `DeleteFileA` | `0x921F0` | 73 | UnwindData |  |
| 574 | `GetDriveTypeA` | `0x92240` | 100 | UnwindData |  |
| 569 | `GetDiskFreeSpaceExW` | `0x925D0` | 609 | UnwindData |  |
| 492 | `GetCompressedFileSizeA` | `0x92840` | 80 | UnwindData |  |
| 493 | `GetCompressedFileSizeW` | `0x928A0` | 486 | UnwindData |  |
| 611 | `GetFileSize` | `0x92A90` | 195 | UnwindData |  |
| 616 | `GetFileVersionInfoByHandle` | `0x92B60` | 691 | UnwindData |  |
| 1840 | `UnmapViewOfFile2` | `0x92E20` | 171 | UnwindData |  |
| 1634 | `SetFileAttributesW` | `0x92EE0` | 45 | UnwindData |  |
| 239 | `CreateProcessA` | `0x931F0` | 108 | UnwindData |  |
| 242 | `CreateProcessInternalA` | `0x93270` | 1,357 | UnwindData |  |
| 244 | `CreateProcessW` | `0x937D0` | 108 | UnwindData |  |
| 241 | `CreateProcessAsUserW` | `0x93850` | 105 | UnwindData |  |
| 243 | `CreateProcessInternalW` | `0x938C0` | 25,379 | UnwindData |  |
| 713 | `GetPackageInfo2` | `0x99BF0` | 54 | UnwindData |  |
| 712 | `GetPackageInfo` | `0x99C30` | 420 | UnwindData |  |
| 714 | `GetPackageInfo3` | `0x99DE0` | 556 | UnwindData |  |
| 809 | `GetStringTypeA` | `0x9A400` | 238 | UnwindData |  |
| 811 | `GetStringTypeW` | `0x9A500` | 46 | UnwindData |  |
| 1785 | `StrStrW` | `0x9A980` | 451 | UnwindData |  |
| 1761 | `StrCmpNW` | `0x9AB50` | 38 | UnwindData |  |
| 177 | `CompareStringOrdinal` | `0x9AD00` | 97 | UnwindData |  |
| 1363 | `QISearch` | `0x9C020` | 66 | UnwindData |  |
| 536 | `GetCurrentPackageApplicationContext` | `0x9C1F0` | 150 | UnwindData |  |
| 54 | `AppContainerRegisterSid` | `0x9C4A0` | 480 | UnwindData |  |
| 52 | `AppContainerLookupDisplayNameMrtReference` | `0x9CAC0` | 262 | UnwindData |  |
| 53 | `AppContainerLookupMoniker` | `0x9D090` | 154 | UnwindData |  |
| 548 | `GetCurrentPackagePath2` | `0x9D3E0` | 408 | UnwindData |  |
| 50 | `AppContainerDeriveSidFromMoniker` | `0x9E2D0` | 258 | UnwindData |  |
| 1158 | `OpenStateExplicitForUserSid` | `0x9E3E0` | 136 | UnwindData |  |
| 1967 | `WilFailureWatcherUnsubscribe` | `0x9FDF0` | 81 | UnwindData |  |
| 1963 | `WilFailureNotifyWatchers` | `0xA0790` | 31 | UnwindData |  |
| 557 | `GetCurrentThreadId` | `0xA0810` | 784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 998 | `IsDebuggerPresent` | `0xA0B20` | 9,264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 540 | `GetCurrentPackageFullName` | `0xA2F50` | 206 | UnwindData |  |
| 544 | `GetCurrentPackageInfo2` | `0xA4040` | 63 | UnwindData |  |
| 543 | `GetCurrentPackageInfo` | `0xA4090` | 66 | UnwindData |  |
| 545 | `GetCurrentPackageInfo3` | `0xA40E0` | 689 | UnwindData |  |
| 731 | `GetPackageVolumeSisPath` | `0xA46C0` | 524 | UnwindData |  |
| 894 | `GetVolumeInformationA` | `0xA49A0` | 763 | UnwindData |  |
| 896 | `GetVolumeInformationW` | `0xA4CB0` | 169 | UnwindData |  |
| 895 | `GetVolumeInformationByHandleW` | `0xA5030` | 805 | UnwindData |  |
| 605 | `GetFileInformationByHandle` | `0xA5360` | 128 | UnwindData |  |
| 1318 | `PerfIncrementULongLongCounterValue` | `0xA7D40` | 213 | UnwindData |  |
| 1316 | `PerfDeleteInstance` | `0xA7E20` | 133 | UnwindData |  |
| 1313 | `PerfCreateInstance` | `0xA7F40` | 207 | UnwindData |  |
| 1320 | `PerfSetCounterRefValue` | `0xA8020` | 211 | UnwindData |  |
| 1322 | `PerfSetULongCounterValue` | `0xA8100` | 234 | UnwindData |  |
| 1314 | `PerfDecrementULongCounterValue` | `0xA81F0` | 247 | UnwindData |  |
| 1293 | `PcwAddQueryItem` | `0xA8740` | 153 | UnwindData |  |
| 1309 | `PcwSetQueryItemUserData` | `0xA87E0` | 73 | UnwindData |  |
| 1300 | `PcwEnumerateInstances` | `0xA8830` | 106 | UnwindData |  |
| 1307 | `PcwSendStatelessNotification` | `0xA88A0` | 133 | UnwindData |  |
| 1306 | `PcwSendNotification` | `0xA8930` | 115 | UnwindData |  |
| 1296 | `PcwCompleteNotification` | `0xA89B0` | 84 | UnwindData |  |
| 1321 | `PerfSetCounterSetInfo` | `0xA8C60` | 158 | UnwindData |  |
| 1298 | `PcwCreateQuery` | `0xA8D10` | 61 | UnwindData |  |
| 1303 | `PcwReadNotificationData` | `0xA8FA0` | 48 | UnwindData |  |
| 1325 | `PerfStartProviderEx` | `0xA8FE0` | 158 | UnwindData |  |
| 1315 | `PerfDecrementULongLongCounterValue` | `0xA9380` | 207 | UnwindData |  |
| 1299 | `PcwDisconnectCounterSet` | `0xA9520` | 65 | UnwindData |  |
| 1323 | `PerfSetULongLongCounterValue` | `0xA99A0` | 362 | UnwindData |  |
| 1326 | `PerfStopProvider` | `0xA9E10` | 82 | UnwindData |  |
| 1297 | `PcwCreateNotifier` | `0xA9E70` | 87 | UnwindData |  |
| 1305 | `PcwRemoveQueryItem` | `0xA9ED0` | 69 | UnwindData |  |
| 1324 | `PerfStartProvider` | `0xA9F20` | 50 | UnwindData |  |
| 1317 | `PerfIncrementULongCounterValue` | `0xA9F60` | 364 | UnwindData |  |
| 1097 | `LogStagedFeatureUsage` | `0xAA190` | 134 | UnwindData |  |
| 16 | `AddAccessAllowedAceEx` | `0xAA5B0` | 75 | UnwindData |  |
| 1090 | `LocalSystemTimeToLocalFileTime` | `0xAA610` | 157 | UnwindData |  |
| 1084 | `LocalFileTimeToLocalSystemTime` | `0xAA810` | 136 | UnwindData |  |
| 1682 | `SetSecurityDescriptorOwner` | `0xAA8A0` | 42 | UnwindData |  |
| 1681 | `SetSecurityDescriptorGroup` | `0xAA8D0` | 42 | UnwindData |  |
| 371 | `EqualDomainSid` | `0xAB0A0` | 498 | UnwindData |  |
| 269 | `CreateWellKnownSid` | `0xAB2A0` | 874 | UnwindData |  |
| 373 | `EqualSid` | `0xAB610` | 63 | UnwindData |  |
| 900 | `GetWindowsAccountDomainSid` | `0xAB660` | 348 | UnwindData |  |
| 1680 | `SetSecurityDescriptorDacl` | `0xAB7D0` | 42 | UnwindData |  |
| 957 | `InitializeSecurityDescriptor` | `0xAB800` | 42 | UnwindData |  |
| 945 | `InitializeAcl` | `0xAB830` | 42 | UnwindData |  |
| 975 | `InternetTimeFromSystemTimeA` | `0xAB900` | 327 | UnwindData |  |
| 868 | `GetTimeFormatA` | `0xABA50` | 340 | UnwindData |  |
| 1805 | `SystemTimeToTzSpecificLocalTimeEx` | `0xABC80` | 733 | UnwindData |  |
| 1834 | `TzSpecificLocalTimeToSystemTime` | `0xAC0A0` | 750 | UnwindData |  |
| 577 | `GetDynamicTimeZoneInformation` | `0xAC3A0` | 539 | UnwindData |  |
| 1804 | `SystemTimeToTzSpecificLocalTime` | `0xAC5D0` | 384 | UnwindData |  |
| 645 | `GetLocalTime` | `0xAD4A0` | 373 | UnwindData |  |
| 872 | `GetTimeZoneInformationForYear` | `0xAEB20` | 171 | UnwindData |  |
| 1585 | `SetClientDynamicTimeZoneInformation` | `0xAECF0` | 97 | UnwindData |  |
| 342 | `EnumDynamicTimeZoneInformation` | `0xAEFE0` | 153 | UnwindData |  |
| 830 | `GetSystemTime` | `0xAF4E0` | 158 | UnwindData |  |
| 1061 | `LCIDToLocaleName` | `0xAF640` | 374 | UnwindData |  |
| 136 | `CharPrevExA` | `0xAFBF0` | 118 | UnwindData |  |
| 133 | `CharNextExA` | `0xAFC70` | 56 | UnwindData |  |
| 997 | `IsDBCSLeadByteEx` | `0xAFCB0` | 266 | UnwindData |  |
| 426 | `FindStringOrdinal` | `0xB0A30` | 1,700 | UnwindData |  |
| 1199 | `PathCchAddBackslashEx` | `0xB1140` | 68 | UnwindData |  |
| 1358 | `PssWalkSnapshot` | `0xB13A0` | 745 | UnwindData |  |
| 1984 | `WriteFile` | `0xB19E0` | 491 | UnwindData |  |
| 430 | `FlsGetValue` | `0xB1BE0` | 100 | UnwindData |  |
| 1803 | `SystemTimeToFileTime` | `0xB1C50` | 189 | UnwindData |  |
| 943 | `InitOnceExecuteOnce` | `0xB28F0` | 53 | UnwindData |  |
| 432 | `FlsSetValue` | `0xB2930` | 42 | UnwindData |  |
| 415 | `FindNLSStringEx` | `0xB2960` | 436 | UnwindData |  |
| 1115 | `MulDiv` | `0xB2B20` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 856 | `GetThreadIdealProcessorEx` | `0xB2B90` | 84 | UnwindData |  |
| 1377 | `QueryMemoryResourceNotification` | `0xB2BF0` | 124 | UnwindData |  |
| 1802 | `SwitchToThread` | `0xB2D00` | 49 | UnwindData |  |
| 395 | `FileTimeToSystemTime` | `0xB2D40` | 213 | UnwindData |  |
| 866 | `GetTickCount` | `0xB2E20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1126 | `NlsUpdateLocale` | `0xB2E40` | 433 | UnwindData |  |
| 1751 | `StrCmpICW` | `0xB34E0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 834 | `GetSystemTimePreciseAsFileTime` | `0xB3530` | 37 | UnwindData |  |
| 1721 | `SetWaitableTimer` | `0xB3730` | 367 | UnwindData |  |
| 1722 | `SetWaitableTimerEx` | `0xB38B0` | 322 | UnwindData |  |
| 667 | `GetModuleFileNameW` | `0xB3CB0` | 53 | UnwindData |  |
| 1014 | `IsThreadAFiber` | `0xB3D80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1389 | `QueryThreadCycleTime` | `0xB3DA0` | 116 | UnwindData |  |
| 1771 | `StrPBrkW` | `0xB3F00` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 867 | `GetTickCount64` | `0xB3F50` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1254 | `PathIsUNCServerShareW` | `0xB3F80` | 266 | UnwindData |  |
| 1255 | `PathIsUNCServerW` | `0xB4090` | 230 | UnwindData |  |
| 1747 | `StrChrW` | `0xB4180` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 309 | `DiscardVirtualMemory` | `0xB41B0` | 217 | UnwindData |  |
| 743 | `GetProcAddressForCaller` | `0xB4530` | 11 | UnwindData |  |
| 171 | `CommandLineToArgvW` | `0xB4680` | 417 | UnwindData |  |
| 833 | `GetSystemTimeAsFileTime` | `0xB4AF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 359 | `EnumSystemGeoID` | `0xB4B10` | 51 | UnwindData |  |
| 1341 | `PsmGetAumidFromKey` | `0xB4BF0` | 213 | UnwindData |  |
| 1345 | `PsmGetPackageFullNameFromKey` | `0xB4CD0` | 202 | UnwindData |  |
| 1340 | `PsmGetApplicationNameFromKey` | `0xB4DA0` | 225 | UnwindData |  |
| 643 | `GetLastError` | `0xB5100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1627 | `SetEvent` | `0xB5110` | 44 | UnwindData |  |
| 1260 | `PathIsValidCharW` | `0xB5150` | 1,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 442 | `FormatMessageA` | `0xB5650` | 648 | UnwindData |  |
| 443 | `FormatMessageW` | `0xB58E0` | 61 | UnwindData |  |
| 1088 | `LocalReAlloc` | `0xB5F40` | 718 | UnwindData |  |
| 748 | `GetProcessHeap` | `0xB62C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1906 | `VirtualAlloc` | `0xB62E0` | 118 | UnwindData |  |
| 1749 | `StrCmpCW` | `0xB6360` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 662 | `GetModuleBaseNameA` | `0xB63A0` | 167 | UnwindData |  |
| 1045 | `K32GetModuleBaseNameA` | `0xB63A0` | 167 | UnwindData |  |
| 663 | `GetModuleBaseNameW` | `0xB6450` | 663 | UnwindData |  |
| 1046 | `K32GetModuleBaseNameW` | `0xB6450` | 663 | UnwindData |  |
| 665 | `GetModuleFileNameExA` | `0xB66F0` | 171 | UnwindData |  |
| 1047 | `K32GetModuleFileNameExA` | `0xB66F0` | 171 | UnwindData |  |
| 666 | `GetModuleFileNameExW` | `0xB67B0` | 52 | UnwindData |  |
| 1048 | `K32GetModuleFileNameExW` | `0xB67B0` | 52 | UnwindData |  |
| 672 | `GetModuleInformation` | `0xB6C20` | 803 | UnwindData |  |
| 1049 | `K32GetModuleInformation` | `0xB6C20` | 803 | UnwindData |  |
| 593 | `GetExtensionApplicationUserModelId` | `0xB7280` | 1,416 | UnwindData |  |
| 1676 | `SetProtocolProperty` | `0xB7810` | 40 | UnwindData |  |
| 1007 | `IsOnDemandRegistrationSupportedForExtensionCategory` | `0xB7840` | 75 | UnwindData |  |
| 368 | `EnumerateExtensionNames` | `0xB78A0` | 672 | UnwindData |  |
| 596 | `GetExtensionProperty2` | `0xB7B50` | 697 | UnwindData |  |
| 1629 | `SetExtensionProperty` | `0xB7E10` | 691 | UnwindData |  |
| 595 | `GetExtensionProperty` | `0xB80D0` | 863 | UnwindData |  |
| 29 | `AddExtensionProgId` | `0xB8970` | 1,764 | UnwindData |  |
| 1429 | `ReadProcessMemory` | `0xB91F0` | 83 | UnwindData |  |
| 1438 | `RegCopyTreeW` | `0xB9250` | 79 | UnwindData |  |
| 1459 | `RegGetKeySecurity` | `0xB9C00` | 631 | UnwindData |  |
| 1916 | `VirtualProtectEx` | `0xBA680` | 186 | UnwindData |  |
| 134 | `CharNextW` | `0xBA740` | 149 | UnwindData |  |
| 1777 | `StrRStrIW` | `0xBA7E0` | 252 | UnwindData |  |
| 1760 | `StrCmpNIW` | `0xBA970` | 38 | UnwindData |  |
| 1910 | `VirtualAllocExNuma` | `0xBAB60` | 142 | UnwindData |  |
| 104 | `BasepAdjustObjectAttributesForPrivateNamespace` | `0xBAC40` | 72 | UnwindData |  |
| 857 | `GetThreadInformation` | `0xBAD80` | 207 | UnwindData |  |
| 597 | `GetFallbackDisplayName` | `0xBAED0` | 63 | UnwindData |  |
| 1700 | `SetThreadPreferredUILanguages` | `0xBAF20` | 135 | UnwindData |  |
| 1701 | `SetThreadPreferredUILanguages2` | `0xBAFB0` | 157 | UnwindData |  |
| 1708 | `SetThreadUILanguage` | `0xBB0F0` | 357 | UnwindData |  |
| 865 | `GetThreadUILanguage` | `0xBB260` | 38 | UnwindData |  |
| 884 | `GetUserDefaultUILanguage` | `0xBB540` | 67 | UnwindData |  |
| 520 | `GetConsoleOutputCP` | `0xBB720` | 311 | UnwindData |  |
| 347 | `EnumProcessModulesEx` | `0xBB860` | 382 | UnwindData |  |
| 1037 | `K32EnumProcessModulesEx` | `0xBB860` | 382 | UnwindData |  |
| 346 | `EnumProcessModules` | `0xBBD80` | 23 | UnwindData |  |
| 1036 | `K32EnumProcessModules` | `0xBBD80` | 23 | UnwindData |  |
| 1822 | `TlsSetValue` | `0xBC060` | 42 | UnwindData |  |
| 738 | `GetPhysicallyInstalledSystemMemory` | `0xBC0C0` | 1,144 | UnwindData |  |
| 912 | `GlobalMemoryStatusEx` | `0xBC540` | 157 | UnwindData |  |
| 822 | `GetSystemFirmwareTable` | `0xBC820` | 307 | UnwindData |  |
| 1525 | `RemovePackageDependency` | `0xBD1F0` | 341 | UnwindData |  |
| 59 | `AppPolicyGetMediaFoundationCodecLoading` | `0xBD750` | 133 | UnwindData |  |
| 58 | `AppPolicyGetLifecycleManagement` | `0xBD7E0` | 136 | UnwindData |  |
| 711 | `GetPackageId` | `0xBDBF0` | 256 | UnwindData |  |
| 56 | `AppPolicyGetClrCompat` | `0xBDD00` | 149 | UnwindData |  |
| 32 | `AddPackageDependency2` | `0xBDDA0` | 2,007 | UnwindData |  |
| 62 | `AppPolicyGetThreadInitializationType` | `0xBE580` | 137 | UnwindData |  |
| 60 | `AppPolicyGetProcessTerminationMethod` | `0xBE610` | 137 | UnwindData |  |
| 63 | `AppPolicyGetWindowingModel` | `0xBEBF0` | 153 | UnwindData |  |
| 1619 | `SetCurrentDirectoryW` | `0xC00A0` | 107 | UnwindData |  |
| 1155 | `OpenState` | `0xC0120` | 116 | UnwindData |  |
| 539 | `GetCurrentPackageFamilyName` | `0xC02C0` | 278 | UnwindData |  |
| 1912 | `VirtualFree` | `0xC14B0` | 202 | UnwindData |  |
| 1392 | `QueryUnbiasedInterruptTimePrecise` | `0xC15F0` | 83 | UnwindData |  |
| 1327 | `PoolPerAppKeyStateInternal` | `0xC1650` | 32 | UnwindData |  |
| 592 | `GetExitCodeThread` | `0xC16E0` | 94 | UnwindData |  |
| 1533 | `ResetEvent` | `0xC17B0` | 42 | UnwindData |  |
| 1909 | `VirtualAllocEx` | `0xC17E0` | 117 | UnwindData |  |
| 1107 | `MapViewOfFileEx` | `0xC1860` | 435 | UnwindData |  |
| 918 | `HashData` | `0xC1A80` | 64 | UnwindData |  |
| 1726 | `SignalObjectAndWait` | `0xC22B0` | 356 | UnwindData |  |
| 1793 | `StrTrimW` | `0xC27B0` | 37 | UnwindData |  |
| 1312 | `PeekNamedPipe` | `0xC28C0` | 562 | UnwindData |  |
| 1329 | `PostQueuedCompletionStatus` | `0xC2B00` | 64 | UnwindData |  |
| 399 | `FindActCtxSectionGuid` | `0xC2BF0` | 109 | UnwindData |  |
| 1579 | `ScrollConsoleScreenBufferW` | `0xC2D20` | 30 | UnwindData |  |
| 1598 | `SetConsoleCP` | `0xC2E20` | 108 | UnwindData |  |
| 533 | `GetCurrentConsoleFontEx` | `0xC2EA0` | 198 | UnwindData |  |
| 642 | `GetLargestConsoleWindowSize` | `0xC2F70` | 107 | UnwindData |  |
| 524 | `GetConsoleSelectionInfo` | `0xC2FF0` | 112 | UnwindData |  |
| 1609 | `SetConsoleOutputCP` | `0xC3070` | 118 | UnwindData |  |
| 1600 | `SetConsoleCursorInfo` | `0xC30F0` | 134 | UnwindData |  |
| 511 | `GetConsoleCursorInfo` | `0xC3180` | 135 | UnwindData |  |
| 466 | `GetAppContainerNamedObjectPath` | `0xC3210` | 255 | UnwindData |  |
| 527 | `GetConsoleWindow` | `0xC3320` | 97 | UnwindData |  |
| 506 | `GetConsoleCP` | `0xC3390` | 87 | UnwindData |  |
| 1617 | `SetCurrentConsoleFontEx` | `0xC33F0` | 198 | UnwindData |  |
| 1601 | `SetConsoleCursorPosition` | `0xC3530` | 124 | UnwindData |  |
| 1606 | `SetConsoleMode` | `0xC35C0` | 91 | UnwindData |  |
| 1612 | `SetConsoleTextAttribute` | `0xC3630` | 124 | UnwindData |  |
| 522 | `GetConsoleScreenBufferInfo` | `0xC36C0` | 116 | UnwindData |  |
| 523 | `GetConsoleScreenBufferInfoEx` | `0xC3740` | 298 | UnwindData |  |
| 1930 | `WaitForSingleObject` | `0xC3990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 911 | `GlobalLock` | `0xC39A0` | 304 | UnwindData |  |
| 915 | `GlobalUnlock` | `0xC3B60` | 195 | UnwindData |  |
| 1758 | `StrCmpNICA` | `0xC3C30` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1334 | `ProcessIdToSessionId` | `0xC3D20` | 355 | UnwindData |  |
| 755 | `GetProcessMemoryInfo` | `0xC3E90` | 369 | UnwindData |  |
| 1053 | `K32GetProcessMemoryInfo` | `0xC3E90` | 369 | UnwindData |  |
| 1915 | `VirtualProtect` | `0xC4010` | 179 | UnwindData |  |
| 835 | `GetSystemTimes` | `0xC40D0` | 1,035 | UnwindData |  |
| 864 | `GetThreadTimes` | `0xC44F0` | 167 | UnwindData |  |
| 1839 | `UnmapViewOfFile` | `0xC4DD0` | 127 | UnwindData |  |
| 774 | `GetQueuedCompletionStatusEx` | `0xC4E60` | 403 | UnwindData |  |
| 1728 | `Sleep` | `0xC5000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1016 | `IsTimeZoneRedirectionEnabled` | `0xC5010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1187 | `ParseURLW` | `0xC5030` | 41 | UnwindData |  |
| 173 | `CompareFileTime` | `0xC5230` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `AccessCheckByType` | `0xC5270` | 186 | UnwindData |  |
| 1211 | `PathCchRemoveExtension` | `0xC5330` | 228 | UnwindData |  |
| 4 | `AccessCheck` | `0xC5420` | 154 | UnwindData |  |
| 528 | `GetCurrencyFormatEx` | `0xC54C0` | 127 | UnwindData |  |
| 687 | `GetNumberFormatW` | `0xC61C0` | 135 | UnwindData |  |
| 686 | `GetNumberFormatEx` | `0xC6250` | 129 | UnwindData |  |
| 261 | `CreateThreadpoolIo` | `0xC7100` | 546 | UnwindData |  |
| 1164 | `OutputDebugStringW` | `0xC7330` | 270 | UnwindData |  |
| 1163 | `OutputDebugStringA` | `0xC7450` | 833 | UnwindData |  |
| 1410 | `RaiseException` | `0xC77A0` | 178 | UnwindData |  |
| 1087 | `LocalLock` | `0xC7860` | 267 | UnwindData |  |
| 71 | `AppXGetPackageSid` | `0xC7980` | 965 | UnwindData |  |
| 194 | `CopySid` | `0xC7D50` | 42 | UnwindData |  |
| 1023 | `IsValidLocaleName` | `0xC7DD0` | 170 | UnwindData |  |
| 1720 | `SetUserGeoName` | `0xC8260` | 127 | UnwindData |  |
| 1651 | `SetLocaleInfoW` | `0xC8620` | 213 | UnwindData |  |
| 143 | `CheckGroupPolicyEnabled` | `0xC8700` | 533 | UnwindData |  |
| 631 | `GetGeoInfoEx` | `0xC8F20` | 108 | UnwindData |  |
| 880 | `GetUserDefaultGeoName` | `0xC8FA0` | 240 | UnwindData |  |
| 885 | `GetUserGeoID` | `0xC90A0` | 102 | UnwindData |  |
| 1991 | `_AddMUIStringToCache` | `0xC9570` | 33 | UnwindData |  |
| 1698 | `SetThreadInformation` | `0xC9690` | 206 | UnwindData |  |
| 610 | `GetFileSecurityW` | `0xC9770` | 184 | UnwindData |  |
| 892 | `GetVersionExA` | `0xC9A80` | 352 | UnwindData |  |
| 893 | `GetVersionExW` | `0xC9BF0` | 224 | UnwindData |  |
| 1401 | `QuirkIsEnabled` | `0xC9CE0` | 47 | UnwindData |  |
| 1027 | `IsValidSid` | `0xCA070` | 56 | UnwindData |  |
| 1109 | `MapViewOfFileFromApp` | `0xCA0B0` | 205 | UnwindData |  |
| 840 | `GetSystemWow64DirectoryA` | `0xCA190` | 44 | UnwindData |  |
| 841 | `GetSystemWow64DirectoryW` | `0xCA1D0` | 44 | UnwindData |  |
| 1973 | `Wow64SetThreadDefaultGuestMachine` | `0xCA210` | 83 | UnwindData |  |
| 951 | `InitializeCriticalSectionEx` | `0xCA840` | 42 | UnwindData |  |
| 1838 | `UnlockFileEx` | `0xCA870` | 112 | UnwindData |  |
| 1370 | `QueryFullProcessImageNameW` | `0xCA8F0` | 97 | UnwindData |  |
| 412 | `FindFirstStreamW` | `0xCAA70` | 888 | UnwindData |  |
| 409 | `FindFirstFileNameW` | `0xCADF0` | 1,078 | UnwindData |  |
| 418 | `FindNextFileNameW` | `0xCB2F0` | 406 | UnwindData |  |
| 614 | `GetFileType` | `0xCB700` | 350 | UnwindData |  |
| 270 | `CtrlRoutine` | `0xCB870` | 596 | UnwindData |  |
| 1702 | `SetThreadPriority` | `0xCBAD0` | 170 | UnwindData |  |
| 494 | `GetComputerNameExA` | `0xCC160` | 286 | UnwindData |  |
| 495 | `GetComputerNameExW` | `0xCC290` | 60 | UnwindData |  |
| 388 | `ExpandEnvironmentStringsW` | `0xCCF80` | 155 | UnwindData |  |
| 1092 | `LocaleNameToLCID` | `0xCDB40` | 123 | UnwindData |  |
| 1864 | `UrlCompareW` | `0xCDBD0` | 437 | UnwindData |  |
| 1762 | `StrCmpW` | `0xCDD90` | 36 | UnwindData |  |
| 1841 | `UnmapViewOfFileEx` | `0xCDF30` | 163 | UnwindData |  |
| 950 | `InitializeCriticalSectionAndSpinCount` | `0xCDFE0` | 27 | UnwindData |  |
| 913 | `GlobalReAlloc` | `0xCE010` | 1,079 | UnwindData |  |
| 760 | `GetProcessTimes` | `0xCE450` | 167 | UnwindData |  |
| 620 | `GetFileVersionInfoSizeExA` | `0xCE7F0` | 135 | UnwindData |  |
| 619 | `GetFileVersionInfoSizeA` | `0xCE910` | 131 | UnwindData |  |
| 621 | `GetFileVersionInfoSizeExW` | `0xCE9A0` | 633 | UnwindData |  |
| 612 | `GetFileSizeEx` | `0xCEF20` | 147 | UnwindData |  |
| 992 | `IsCharSpaceW` | `0xCF0A0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1757 | `StrCmpNIA` | `0xCF120` | 128 | UnwindData |  |
| 1251 | `PathIsUNCEx` | `0xCF1B0` | 207 | UnwindData |  |
| 1791 | `StrToIntW` | `0xCF290` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 910 | `GlobalHandle` | `0xCF2F0` | 192 | UnwindData |  |
| 267 | `CreateWaitableTimerExW` | `0xCF3C0` | 371 | UnwindData |  |
| 1091 | `LocalUnlock` | `0xCF540` | 218 | UnwindData |  |
| 860 | `GetThreadPriority` | `0xCF620` | 115 | UnwindData |  |
| 783 | `GetSecurityDescriptorDacl` | `0xCF730` | 104 | UnwindData |  |
| 1753 | `StrCmpLogicalW` | `0xCF7A0` | 204 | UnwindData |  |
| 387 | `ExpandEnvironmentStringsA` | `0xCF880` | 605 | UnwindData |  |
| 248 | `CreateRemoteThreadEx` | `0xCFAF0` | 2,083 | UnwindData |  |
| 1286 | `PathStripPathW` | `0xD1050` | 320 | UnwindData |  |
| 1276 | `PathRemoveExtensionW` | `0xD11A0` | 152 | UnwindData |  |
| 1750 | `StrCmpICA` | `0xD1240` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1427 | `ReadFileEx` | `0xD1290` | 489 | UnwindData |  |
| 1424 | `ReadDirectoryChangesExW` | `0xD1480` | 534 | UnwindData |  |
| 1425 | `ReadDirectoryChangesW` | `0xD16A0` | 466 | UnwindData |  |
| 1985 | `WriteFileEx` | `0xD1880` | 260 | UnwindData |  |
| 1396 | `QueueUserAPC` | `0xD1B80` | 231 | UnwindData |  |
| 5 | `AccessCheckAndAuditAlarmW` | `0xD1C70` | 323 | UnwindData |  |
| 1816 | `TestReport` | `0xD1DC0` | 39 | UnwindData |  |
| 668 | `GetModuleHandleA` | `0xD2730` | 92 | UnwindData |  |
| 45 | `AllocateAndInitializeSid` | `0xD28A0` | 121 | UnwindData |  |
| 125 | `CancelWaitableTimer` | `0xD2920` | 48 | UnwindData |  |
| 1919 | `VirtualQueryEx` | `0xD2960` | 72 | UnwindData |  |
| 1918 | `VirtualQuery` | `0xD30C0` | 79 | UnwindData |  |
| 1397 | `QueueUserAPC2` | `0xD3120` | 78 | UnwindData |  |
| 326 | `DuplicateTokenEx` | `0xD3250` | 214 | UnwindData |  |
| 148 | `CheckTokenMembership` | `0xD3330` | 98 | UnwindData |  |
| 680 | `GetNativeSystemInfo` | `0xD33A0` | 197 | UnwindData |  |
| 120 | `CallbackMayRunLong` | `0xD3620` | 49 | UnwindData |  |
| 1342 | `PsmGetDynamicIdFromKey` | `0xD3660` | 137 | UnwindData |  |
| 1348 | `PsmIsValidKey` | `0xD36F0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 586 | `GetEnvironmentStringsW` | `0xD3790` | 218 | UnwindData |  |
| 264 | `CreateThreadpoolWork` | `0xD3870` | 72 | UnwindData |  |
| 1198 | `PathCchAddBackslash` | `0xD38C0` | 2,624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `BasepCopyFileCallback` | `0xD4300` | 176 | UnwindData |  |
| 101 | `BaseMarkFileForDelete` | `0xD4560` | 231 | UnwindData |  |
| 1532 | `ReplaceFileW` | `0xD4A80` | 75 | UnwindData |  |
| 1530 | `ReplaceFileExInternal` | `0xD4AE0` | 6,272 | UnwindData |  |
| 291 | `DeleteFileW` | `0xD70A0` | 47 | UnwindData |  |
| 107 | `BasepNotifyTrackingService` | `0xD7450` | 843 | UnwindData |  |
| 1482 | `RegOpenUserClassesRoot` | `0xDE8F0` | 660 | UnwindData |  |
| 664 | `GetModuleFileNameA` | `0xDEB90` | 552 | UnwindData |  |
| 1543 | `RevertToSelf` | `0xDEDC0` | 73 | UnwindData |  |
| 1160 | `OpenThread` | `0xDEE10` | 120 | UnwindData |  |
| 1237 | `PathGetDriveNumberW` | `0xDEE90` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 272 | `DeactivateActCtx` | `0xDEF00` | 60 | UnwindData |  |
| 591 | `GetExitCodeProcess` | `0xDEF50` | 94 | UnwindData |  |
| 14 | `ActivateActCtx` | `0xDEFC0` | 81 | UnwindData |  |
| 1239 | `PathIsFileSpecW` | `0xDF050` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 394 | `FileTimeToLocalFileTime` | `0xDF080` | 183 | UnwindData |  |
| 1266 | `PathParseIconLocationW` | `0xDF140` | 214 | UnwindData |  |
| 1274 | `PathRemoveBlanksW` | `0xDF220` | 10 | UnwindData |  |
| 1292 | `PathUnquoteSpacesW` | `0xDF310` | 88 | UnwindData |  |
| 185 | `ConvertThreadToFiber` | `0xDF370` | 308 | UnwindData |  |
| 1784 | `StrStrNW` | `0xDF4B0` | 158 | UnwindData |  |
| 1746 | `StrChrNW` | `0xDF560` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1694 | `SetThreadErrorMode` | `0xDF5A0` | 181 | UnwindData |  |
| 650 | `GetLogicalDriveStringsW` | `0xDF660` | 249 | UnwindData |  |
| 651 | `GetLogicalDrives` | `0xDF760` | 106 | UnwindData |  |
| 588 | `GetEnvironmentVariableW` | `0xDF7D0` | 155 | UnwindData |  |
| 1938 | `WaitOnAddress` | `0xDF880` | 125 | UnwindData |  |
| 1118 | `NamedPipeEventSelect` | `0xDF910` | 254 | UnwindData |  |
| 1117 | `NamedPipeEventEnum` | `0xDFA20` | 249 | UnwindData |  |
| 677 | `GetNamedPipeClientComputerNameW` | `0xDFB20` | 286 | UnwindData |  |
| 676 | `GetNamedPipeAttribute` | `0xDFC50` | 332 | UnwindData |  |
| 820 | `GetSystemDirectoryW` | `0xDFE00` | 81 | UnwindData |  |
| 1727 | `SizeofResource` | `0xDFE60` | 120 | UnwindData |  |
| 1124 | `NlsGetCacheUpdateCount` | `0xDFEE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1848 | `UnregisterWaitEx` | `0xDFF00` | 87 | UnwindData |  |
| 1423 | `ReadConsoleW` | `0xDFFF0` | 81 | UnwindData |  |
| 1352 | `PssQuerySnapshot` | `0xE0440` | 776 | UnwindData |  |
| 587 | `GetEnvironmentVariableA` | `0xE0750` | 13 | UnwindData |  |
| 1775 | `StrRChrW` | `0xE0950` | 90 | UnwindData |  |
| 1756 | `StrCmpNCW` | `0xE09B0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 858 | `GetThreadLocale` | `0xE0AC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 740 | `GetPriorityClass` | `0xE0AE0` | 188 | UnwindData |  |
| 1737 | `StrCSpnW` | `0xE0BB0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 937 | `ImpersonateLoggedOnUser` | `0xE0CA0` | 386 | UnwindData |  |
| 658 | `GetMappedFileNameW` | `0xE0E30` | 136 | UnwindData |  |
| 1044 | `K32GetMappedFileNameW` | `0xE0E30` | 136 | UnwindData |  |
| 1361 | `PulseEvent` | `0xE0F50` | 44 | UnwindData |  |
| 400 | `FindActCtxSectionStringW` | `0xE0F90` | 109 | UnwindData |  |
| 617 | `GetFileVersionInfoExA` | `0xE1010` | 163 | UnwindData |  |
| 615 | `GetFileVersionInfoA` | `0xE10C0` | 161 | UnwindData |  |
| 623 | `GetFileVersionInfoW` | `0xE1170` | 34 | UnwindData |  |
| 618 | `GetFileVersionInfoExW` | `0xE11A0` | 782 | UnwindData |  |
| 1545 | `SHCoCreateInstance` | `0xE1950` | 104 | UnwindData |  |
| 1965 | `WilFailureWatcherSubscribe` | `0xE19C0` | 78 | UnwindData |  |
| 186 | `ConvertThreadToFiberEx` | `0xE1C00` | 21 | UnwindData |  |
| 669 | `GetModuleHandleExA` | `0xE1D60` | 486 | UnwindData |  |
| 1464 | `RegKrnGetClassesEnumTableAddressInternal` | `0xE2150` | 49 | UnwindData |  |
| 871 | `GetTimeZoneInformation` | `0xE2190` | 475 | UnwindData |  |
| 1332 | `PrivilegeCheck` | `0xE2440` | 65 | UnwindData |  |
| 435 | `FlushInstructionCache` | `0xE2620` | 91 | UnwindData |  |
| 1129 | `NormalizeString` | `0xE26C0` | 146 | UnwindData |  |
| 1017 | `IsTokenRestricted` | `0xE2760` | 63 | UnwindData |  |
| 933 | `IdnToAscii` | `0xE2A30` | 117 | UnwindData |  |
| 21 | `AddAce` | `0xE2AB0` | 50 | UnwindData |  |
| 1486 | `RegQueryMultipleValuesW` | `0xE2AF0` | 972 | UnwindData |  |
| 1547 | `SHExpandEnvironmentStringsW` | `0xE3010` | 218 | UnwindData |  |
| 1245 | `PathIsRelativeW` | `0xE30F0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `CheckTokenCapability` | `0xE3150` | 95 | UnwindData |  |
| 1447 | `RegDeleteKeyValueA` | `0xE31C0` | 94 | UnwindData |  |
| 1451 | `RegDeleteValueA` | `0xE3230` | 247 | UnwindData |  |
| 1059 | `KernelBaseGetGlobalData` | `0xE34D0` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 999 | `IsDeveloperModeEnabled` | `0xE36A0` | 164 | UnwindData |  |
| 1000 | `IsDeveloperModePolicyApplied` | `0xE3DB0` | 128 | UnwindData |  |
| 737 | `GetPersistedRegistryValueW` | `0xE3E40` | 505 | UnwindData |  |
| 613 | `GetFileTime` | `0xE4040` | 175 | UnwindData |  |
| 754 | `GetProcessInformation` | `0xE4150` | 484 | UnwindData |  |
| 850 | `GetThreadDescription` | `0xE45D0` | 294 | UnwindData |  |
| 883 | `GetUserDefaultLocaleName` | `0xE4860` | 247 | UnwindData |  |
| 1089 | `LocalSize` | `0xE4960` | 365 | UnwindData |  |
| 1801 | `SwitchToFiber` | `0xE4AE0` | 60 | UnwindData |  |
| 1142 | `OpenFileById` | `0xE4B30` | 482 | UnwindData |  |
| 1403 | `QuirkIsEnabled3` | `0xE4D20` | 57 | UnwindData |  |
| 70 | `AppXGetPackageCapabilities` | `0xE4D60` | 595 | UnwindData |  |
| 914 | `GlobalSize` | `0xE53B0` | 370 | UnwindData |  |
| 1385 | `QuerySecurityAccessMask` | `0xE5570` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2019 | `hgets` | `0xE55E0` | 454 | UnwindData |  |
| 899 | `GetVolumePathNamesForVolumeNameW` | `0xE5830` | 1,202 | UnwindData |  |
| 162 | `CloseStateContainer` | `0xE5CF0` | 161 | UnwindData |  |
| 1354 | `PssWalkMarkerFree` | `0xE5DA0` | 86 | UnwindData |  |
| 1357 | `PssWalkMarkerSetPosition` | `0xE5E00` | 64 | UnwindData |  |
| 1355 | `PssWalkMarkerGetPosition` | `0xE5E50` | 67 | UnwindData |  |
| 1356 | `PssWalkMarkerSeekToBeginning` | `0xE5EA0` | 56 | UnwindData |  |
| 461 | `GetAclInformation` | `0xE5FF0` | 42 | UnwindData |  |
| 1580 | `SearchPathA` | `0xE6020` | 772 | UnwindData |  |
| 1282 | `PathSearchAndQualifyW` | `0xE6330` | 230 | UnwindData |  |
| 1581 | `SearchPathW` | `0xE6420` | 572 | UnwindData |  |
| 1073 | `LoadLibraryExA` | `0xE6670` | 178 | UnwindData |  |
| 159 | `CloseState` | `0xE6730` | 36 | UnwindData |  |
| 1343 | `PsmGetKeyFromProcess` | `0xE69F0` | 116 | UnwindData |  |
| 1344 | `PsmGetKeyFromToken` | `0xE6A70` | 407 | UnwindData |  |
| 1336 | `PsmCreateKey` | `0xE6C10` | 148 | UnwindData |  |
| 252 | `CreateStateAtom` | `0xE6ED0` | 112 | UnwindData |  |
| 1156 | `OpenStateAtom` | `0xE7030` | 136 | UnwindData |  |
| 160 | `CloseStateAtom` | `0xE75E0` | 36 | UnwindData |  |
| 753 | `GetProcessImageFileNameW` | `0xE7690` | 204 | UnwindData |  |
| 1052 | `K32GetProcessImageFileNameW` | `0xE7690` | 204 | UnwindData |  |
| 1026 | `IsValidSecurityDescriptor` | `0xE7770` | 45 | UnwindData |  |
| 1009 | `IsProcessInJob` | `0xE77B0` | 97 | UnwindData |  |
| 792 | `GetSidIdentifierAuthority` | `0xE7920` | 43 | UnwindData |  |
| 751 | `GetProcessIdOfThread` | `0xE7960` | 81 | UnwindData |  |
| 1031 | `IsWow64Process2` | `0xE7AC0` | 42 | UnwindData |  |
| 1369 | `QueryFullProcessImageNameA` | `0xE7AF0` | 536 | UnwindData |  |
| 1189 | `PathAddBackslashW` | `0xE7D10` | 229 | UnwindData |  |
| 1693 | `SetThreadDescription` | `0xE7E00` | 79 | UnwindData |  |
| 903 | `GetWriteWatch` | `0xE7EB0` | 77 | UnwindData |  |
| 736 | `GetPersistedRegistryLocationW` | `0xE7F10` | 62 | UnwindData |  |
| 815 | `GetSystemDefaultLCID` | `0xE8020` | 40 | UnwindData |  |
| 1058 | `K32QueryWorkingSetEx` | `0xE80C0` | 79 | UnwindData |  |
| 1395 | `QueryWorkingSetEx` | `0xE80C0` | 79 | UnwindData |  |
| 413 | `FindFirstVolumeW` | `0xE84D0` | 543 | UnwindData |  |
| 421 | `FindNextVolumeW` | `0xE8700` | 841 | UnwindData |  |
| 1914 | `VirtualLock` | `0xE9460` | 71 | UnwindData |  |
| 129 | `CharLowerBuffA` | `0xE94B0` | 398 | UnwindData |  |
| 939 | `ImpersonateSelf` | `0xE9650` | 42 | UnwindData |  |
| 1703 | `SetThreadPriorityBoost` | `0xE9680` | 68 | UnwindData |  |
| 1386 | `QueryStateAtomValueInfo` | `0xE9890` | 171 | UnwindData |  |
| 1100 | `MakeSelfRelativeSD` | `0xE9A00` | 54 | UnwindData |  |
| 1422 | `ReadConsoleOutputW` | `0xE9A40` | 30 | UnwindData |  |
| 1982 | `WriteConsoleOutputW` | `0xE9DF0` | 30 | UnwindData |  |
| 788 | `GetSecurityDescriptorSacl` | `0xEA3D0` | 92 | UnwindData |  |
| 1833 | `TrySubmitThreadpoolCallback` | `0xEA440` | 49 | UnwindData |  |
| 838 | `GetSystemWow64Directory2A` | `0xEA480` | 371 | UnwindData |  |
| 839 | `GetSystemWow64Directory2W` | `0xEA770` | 228 | UnwindData |  |
| 837 | `GetSystemWindowsDirectoryW` | `0xEA860` | 88 | UnwindData |  |
| 266 | `CreateTimerQueueTimer` | `0xEA8C0` | 156 | UnwindData |  |
| 640 | `GetKernelObjectSecurity` | `0xEAA00` | 52 | UnwindData |  |
| 325 | `DuplicateToken` | `0xEAAB0` | 167 | UnwindData |  |
| 1643 | `SetHandleInformation` | `0xEABB0` | 274 | UnwindData |  |
| 233 | `CreateNamedPipeW` | `0xEACD0` | 931 | UnwindData |  |
| 183 | `ConvertFiberToThread` | `0xEB080` | 106 | UnwindData |  |
| 1718 | `SetUnhandledExceptionFilter` | `0xEB0F0` | 515 | UnwindData |  |
| 782 | `GetSecurityDescriptorControl` | `0xEB450` | 42 | UnwindData |  |
| 1907 | `VirtualAlloc2` | `0xEB5C0` | 146 | UnwindData |  |
| 1558 | `SHRegEnumUSKeyW` | `0xEB660` | 523 | UnwindData |  |
| 535 | `GetCurrentDirectoryW` | `0xEB880` | 26 | UnwindData |  |
| 1769 | `StrIsIntlEqualW` | `0xEB8A0` | 57 | UnwindData |  |
| 149 | `CheckTokenMembershipEx` | `0xEB8E0` | 88 | UnwindData |  |
| 828 | `GetSystemPreferredUILanguages` | `0xEB940` | 89 | UnwindData |  |
| 1477 | `RegOpenCurrentUser` | `0xEB9A0` | 50 | UnwindData |  |
| 1098 | `MakeAbsoluteSD` | `0xEB9E0` | 141 | UnwindData |  |
| 1290 | `PathUnExpandEnvStringsW` | `0xEBA80` | 26 | UnwindData |  |
| 806 | `GetStdHandle` | `0xEBF60` | 162 | UnwindData |  |
| 1837 | `UnlockFile` | `0xEC010` | 183 | UnwindData |  |
| 795 | `GetSidSubAuthorityCount` | `0xEC0D0` | 43 | UnwindData |  |
| 42 | `AdjustTokenPrivileges` | `0xEC110` | 61 | UnwindData |  |
| 1111 | `MoveFileExW` | `0xEC160` | 66 | UnwindData |  |
| 1114 | `MoveFileWithProgressW` | `0xEC1B0` | 59 | UnwindData |  |
| 1113 | `MoveFileWithProgressTransactedW` | `0xEC200` | 3,948 | UnwindData |  |
| 1535 | `ResetWriteWatch` | `0xEDCA0` | 50 | UnwindData |  |
| 307 | `DisableThreadLibraryCalls` | `0xEDCE0` | 47 | UnwindData |  |
| 566 | `GetDeviceDriverFileNameW` | `0xEDD20` | 148 | UnwindData |  |
| 1042 | `K32GetDeviceDriverFileNameW` | `0xEDD20` | 148 | UnwindData |  |
| 564 | `GetDeviceDriverBaseNameW` | `0xEDDC0` | 148 | UnwindData |  |
| 1040 | `K32GetDeviceDriverBaseNameW` | `0xEDDC0` | 148 | UnwindData |  |
| 565 | `GetDeviceDriverFileNameA` | `0xEDE60` | 148 | UnwindData |  |
| 1041 | `K32GetDeviceDriverFileNameA` | `0xEDE60` | 148 | UnwindData |  |
| 563 | `GetDeviceDriverBaseNameA` | `0xEDF00` | 171 | UnwindData |  |
| 1039 | `K32GetDeviceDriverBaseNameA` | `0xEDF00` | 171 | UnwindData |  |
| 237 | `CreatePrivateObjectSecurityEx` | `0xEE190` | 84 | UnwindData |  |
| 434 | `FlushFileBuffers` | `0xEE1F0` | 132 | UnwindData |  |
| 1387 | `QueryStateContainerCreatedNew` | `0xEE280` | 71 | UnwindData |  |
| 846 | `GetTempPath2W` | `0xEE2D0` | 677 | UnwindData |  |
| 848 | `GetTempPathW` | `0xEE660` | 613 | UnwindData |  |
| 263 | `CreateThreadpoolWait` | `0xEE930` | 69 | UnwindData |  |
| 15 | `AddAccessAllowedAce` | `0xEE9D0` | 42 | UnwindData |  |
| 766 | `GetProductInfo` | `0xEEA00` | 41 | UnwindData |  |
| 530 | `GetCurrentActCtx` | `0xEEA30` | 57 | UnwindData |  |
| 1568 | `SHRegQueryInfoUSKeyW` | `0xEEA70` | 518 | UnwindData |  |
| 626 | `GetFullPathNameA` | `0xEEC80` | 752 | UnwindData |  |
| 280 | `DelayLoadFailureHook` | `0xEEF80` | 83 | UnwindData |  |
| 281 | `DelayLoadFailureHookLookup` | `0xEEFE0` | 90 | UnwindData |  |
| 1671 | `SetProcessValidCallTargets` | `0xEF200` | 312 | UnwindData |  |
| 938 | `ImpersonateNamedPipeClient` | `0xEF340` | 269 | UnwindData |  |
| 561 | `GetDateFormatW` | `0xEF460` | 309 | UnwindData |  |
| 1614 | `SetConsoleTitleW` | `0xEF5A0` | 61 | UnwindData |  |
| 1420 | `ReadConsoleOutputCharacterA` | `0xEF690` | 41 | UnwindData |  |
| 526 | `GetConsoleTitleW` | `0xEF7E0` | 97 | UnwindData |  |
| 1980 | `WriteConsoleOutputCharacterA` | `0xEF910` | 41 | UnwindData |  |
| 457 | `GetACP` | `0xEFBF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1398 | `QueueUserWorkItem` | `0xEFC00` | 42 | UnwindData |  |
| 1507 | `ReleaseActCtx` | `0xF01C0` | 40 | UnwindData |  |
| 1072 | `LoadLibraryA` | `0xF01F0` | 221 | UnwindData |  |
| 1696 | `SetThreadIdealProcessor` | `0xF02E0` | 63 | UnwindData |  |
| 977 | `InternetTimeToSystemTimeA` | `0xF0330` | 58 | UnwindData |  |
| 958 | `InitializeSid` | `0xF07C0` | 42 | UnwindData |  |
| 921 | `HeapCreate` | `0xF07F0` | 122 | UnwindData |  |
| 859 | `GetThreadPreferredUILanguages` | `0xF0870` | 63 | UnwindData |  |
| 1416 | `ReadConsoleInputExW` | `0xF0C90` | 30 | UnwindData |  |
| 1311 | `PeekConsoleInputW` | `0xF0CC0` | 27 | UnwindData |  |
| 1417 | `ReadConsoleInputW` | `0xF0CF0` | 27 | UnwindData |  |
| 1310 | `PeekConsoleInputA` | `0xF0D20` | 27 | UnwindData |  |
| 212 | `CreateFiber` | `0xF0F90` | 28 | UnwindData |  |
| 213 | `CreateFiberEx` | `0xF0FC0` | 672 | UnwindData |  |
| 1295 | `PcwCollectData` | `0xF1440` | 323 | UnwindData |  |
| 235 | `CreatePrivateNamespaceW` | `0xF16C0` | 253 | UnwindData |  |
| 1150 | `OpenPrivateNamespaceW` | `0xF17D0` | 145 | UnwindData |  |
| 425 | `FindResourceW` | `0xF1AF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1635 | `SetFileInformationByHandle` | `0xF1B10` | 228 | UnwindData |  |
| 633 | `GetHandleInformation` | `0xF1DE0` | 183 | UnwindData |  |
| 2027 | `lstrcpyn` | `0xF1EA0` | 96 | UnwindData |  |
| 2028 | `lstrcpynA` | `0xF1EA0` | 96 | UnwindData |  |
| 1542 | `ResumeThread` | `0xF2060` | 52 | UnwindData |  |
| 301 | `DeleteTimerQueueTimer` | `0xF20A0` | 97 | UnwindData |  |
| 1622 | `SetEndOfFile` | `0xF2110` | 192 | UnwindData |  |
| 1085 | `LocalFlags` | `0xF21E0` | 294 | UnwindData |  |
| 2029 | `lstrcpynW` | `0xF2350` | 106 | UnwindData |  |
| 1706 | `SetThreadStackGuarantee` | `0xF23C0` | 376 | UnwindData |  |
| 304 | `DestroyPrivateObjectSecurity` | `0xF2580` | 42 | UnwindData |  |
| 980 | `IsApiSetImplemented` | `0xF26F0` | 27 | UnwindData |  |
| 891 | `GetVersion` | `0xF2720` | 78 | UnwindData |  |
| 849 | `GetThreadContext` | `0xF2780` | 42 | UnwindData |  |
| 729 | `GetPackageStatusForUserSid` | `0xF27B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 580 | `GetEffectivePackageStatusForUserSid` | `0xF27E0` | 132 | UnwindData |  |
| 517 | `GetConsoleMode` | `0xF28E0` | 319 | UnwindData |  |
| 931 | `HeapValidate` | `0xF2A30` | 25 | UnwindData |  |
| 1233 | `PathGetArgsW` | `0xF2B20` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 437 | `FlushViewOfFile` | `0xF2B80` | 91 | UnwindData |  |
| 1375 | `QueryInterruptTimePrecise` | `0xF2BF0` | 42 | UnwindData |  |
| 119 | `CallNamedPipeW` | `0xF2C20` | 389 | UnwindData |  |
| 1826 | `TransactNamedPipe` | `0xF2DB0` | 406 | UnwindData |  |
| 1652 | `SetNamedPipeHandleState` | `0xF2F50` | 272 | UnwindData |  |
| 226 | `CreateIoCompletionPort` | `0xF3070` | 221 | UnwindData |  |
| 1157 | `OpenStateExplicit` | `0xF3160` | 136 | UnwindData |  |
| 688 | `GetNumberOfConsoleInputEvents` | `0xF32B0` | 319 | UnwindData |  |
| 799 | `GetStartupInfoW` | `0xF3400` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `AreFileApisANSI` | `0xF35A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 861 | `GetThreadPriorityBoost` | `0xF35C0` | 80 | UnwindData |  |
| 179 | `ConnectNamedPipe` | `0xF3620` | 207 | UnwindData |  |
| 728 | `GetPackageStatusForUser` | `0xF3700` | 301 | UnwindData |  |
| 1789 | `StrToIntExA` | `0xF3840` | 44 | UnwindData |  |
| 1786 | `StrToInt64ExA` | `0xF3880` | 258 | UnwindData |  |
| 1790 | `StrToIntExW` | `0xF3990` | 44 | UnwindData |  |
| 1787 | `StrToInt64ExW` | `0xF39D0` | 348 | UnwindData |  |
| 199 | `CreateBoundaryDescriptorW` | `0xF3B40` | 77 | UnwindData |  |
| 1800 | `SuspendThread` | `0xF3F60` | 52 | UnwindData |  |
| 638 | `GetIsEdpEnabled` | `0xF3FA0` | 109 | UnwindData |  |
| 902 | `GetWindowsDirectoryW` | `0xF4020` | 147 | UnwindData |  |
| 2010 | `_initterm` | `0xF4420` | 55 | UnwindData |  |
| 1647 | `SetKernelObjectSecurity` | `0xF4460` | 42 | UnwindData |  |
| 87 | `AttachConsole` | `0xF4490` | 151 | UnwindData |  |
| 1135 | `ObjectOpenAuditAlarmW` | `0xF5850` | 242 | UnwindData |  |
| 491 | `GetCommandLineW` | `0xF5950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 450 | `FreeLibraryAndExitThread` | `0xF5960` | 162 | UnwindData |  |
| 607 | `GetFileInformationByName` | `0xF5A10` | 380 | UnwindData |  |
| 1687 | `SetStdHandleEx` | `0xF5BA0` | 128 | UnwindData |  |
| 35 | `AddRefActCtx` | `0xF5D40` | 40 | UnwindData |  |
| 1364 | `QueryActCtxSettingsW` | `0xF5D70` | 132 | UnwindData |  |
| 1755 | `StrCmpNCA` | `0xF5E00` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1856 | `UpdateProcThreadAttribute` | `0xF5E40` | 812 | UnwindData |  |
| 310 | `DisconnectNamedPipe` | `0xF6180` | 269 | UnwindData |  |
| 1060 | `KernelbasePostInit` | `0xF62A0` | 94 | UnwindData |  |
| 465 | `GetAppContainerAce` | `0xF64F0` | 267 | UnwindData |  |
| 1019 | `IsValidAcl` | `0xF6610` | 52 | UnwindData |  |
| 225 | `CreateHardLinkW` | `0xF6960` | 677 | UnwindData |  |
| 1204 | `PathCchCanonicalizeEx` | `0xF6C10` | 3,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `AppXGetOSMaxVersionTested` | `0xF7810` | 482 | UnwindData |  |
| 2011 | `_initterm_e` | `0xF7A00` | 64 | UnwindData |  |
| 558 | `GetCurrentThreadStackLimits` | `0xF7AB0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1022 | `IsValidLocale` | `0xF7B00` | 148 | UnwindData |  |
| 428 | `FlsAlloc` | `0xF7BA0` | 52 | UnwindData |  |
| 1010 | `IsProcessorFeaturePresent` | `0xF7BE0` | 31 | UnwindData |  |
| 1988 | `WriteStateAtomValue` | `0xF7C10` | 229 | UnwindData |  |
| 189 | `CopyFile2` | `0xF8410` | 584 | UnwindData |  |
| 1331 | `PrivCopyFileExW` | `0xF8660` | 1,150 | UnwindData |  |
| 192 | `CopyFileW` | `0xF8AF0` | 69 | UnwindData |  |
| 190 | `CopyFileExW` | `0xF8B40` | 341 | UnwindData |  |
| 106 | `BasepCopyFileExW` | `0xF8CA0` | 8,371 | UnwindData |  |
| 776 | `GetRegistryValueWithFallbackW` | `0xFAE20` | 228 | UnwindData |  |
| 752 | `GetProcessImageFileNameA` | `0xFAF10` | 249 | UnwindData |  |
| 1051 | `K32GetProcessImageFileNameA` | `0xFAF10` | 249 | UnwindData |  |
| 542 | `GetCurrentPackageId` | `0xFB090` | 285 | UnwindData |  |
| 1506 | `RegisterWaitForSingleObjectEx` | `0xFB1C0` | 147 | UnwindData |  |
| 786 | `GetSecurityDescriptorOwner` | `0xFB260` | 65 | UnwindData |  |
| 1094 | `LockFile` | `0xFB2B0` | 165 | UnwindData |  |
| 1695 | `SetThreadGroupAffinity` | `0xFB440` | 166 | UnwindData |  |
| 784 | `GetSecurityDescriptorGroup` | `0xFB4F0` | 65 | UnwindData |  |
| 1774 | `StrRChrIW` | `0xFB610` | 102 | UnwindData |  |
| 844 | `GetTempFileNameW` | `0xFB710` | 885 | UnwindData |  |
| 302 | `DeleteVolumeMountPointW` | `0xFBA90` | 1,125 | UnwindData |  |
| 1131 | `NotifyMountMgr` | `0xFBF00` | 455 | UnwindData |  |
| 1975 | `WriteConsoleA` | `0xFC0D0` | 47 | UnwindData |  |
| 1983 | `WriteConsoleW` | `0xFC110` | 47 | UnwindData |  |
| 983 | `IsCharAlphaNumericW` | `0xFC2C0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 730 | `GetPackageTargetPlatformProperty` | `0xFC3E0` | 214 | UnwindData |  |
| 163 | `CloseStateLock` | `0xFC4C0` | 70 | UnwindData |  |
| 404 | `FindFirstChangeNotificationW` | `0xFC580` | 439 | UnwindData |  |
| 797 | `GetStagedPackagePathByFullName` | `0xFC740` | 79 | UnwindData |  |
| 122 | `CancelIoEx` | `0xFC7A0` | 55 | UnwindData |  |
| 1640 | `SetFileTime` | `0xFC980` | 172 | UnwindData |  |
| 762 | `GetProcessWorkingSetSize` | `0xFCA40` | 25 | UnwindData |  |
| 763 | `GetProcessWorkingSetSizeEx` | `0xFCA60` | 176 | UnwindData |  |
| 1666 | `SetProcessInformation` | `0xFCBB0` | 555 | UnwindData |  |
| 1149 | `OpenPackageInfoByFullNameForUser` | `0xFCDF0` | 108 | UnwindData |  |
| 1383 | `QueryProcessCycleTime` | `0xFCE70` | 120 | UnwindData |  |
| 673 | `GetNLSVersion` | `0xFCEF0` | 99 | UnwindData |  |
| 674 | `GetNLSVersionEx` | `0xFCF60` | 96 | UnwindData |  |
| 793 | `GetSidLengthRequired` | `0xFD0D0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 984 | `IsCharAlphaW` | `0xFD160` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1657 | `SetPriorityClass` | `0xFD290` | 537 | UnwindData |  |
| 922 | `HeapDestroy` | `0xFD810` | 53 | UnwindData |  |
| 1218 | `PathCombineW` | `0xFD850` | 65 | UnwindData |  |
| 37 | `AddSIDToBoundaryDescriptor` | `0xFD8A0` | 42 | UnwindData |  |
| 1096 | `LockResource` | `0xFD9E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 286 | `DeleteFiber` | `0xFD9F0` | 220 | UnwindData |  |
| 1684 | `SetSecurityDescriptorSacl` | `0xFDB10` | 42 | UnwindData |  |
| 369 | `EnumerateStateAtomValues` | `0xFDBA0` | 191 | UnwindData |  |
| 816 | `GetSystemDefaultLangID` | `0xFE370` | 41 | UnwindData |  |
| 1133 | `ObjectCloseAuditAlarmW` | `0xFE3A0` | 99 | UnwindData |  |
| 453 | `FreeSid` | `0xFE520` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 653 | `GetLogicalProcessorInformationEx` | `0xFE550` | 112 | UnwindData |  |
| 953 | `InitializeProcThreadAttributeList` | `0xFE710` | 137 | UnwindData |  |
| 1788 | `StrToIntA` | `0xFE7D0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 842 | `GetTargetPlatformContext` | `0xFE840` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 567 | `GetDiskFreeSpaceA` | `0xFE880` | 128 | UnwindData |  |
| 570 | `GetDiskFreeSpaceW` | `0xFE910` | 616 | UnwindData |  |
| 1599 | `SetConsoleCtrlHandler` | `0xFED30` | 180 | UnwindData |  |
| 156 | `ClosePackageInfo` | `0xFEF70` | 29 | UnwindData |  |
| 79 | `AreAllAccessesGranted` | `0xFF020` | 25 | UnwindData |  |
| 1288 | `PathStripToRootW` | `0xFF040` | 34 | UnwindData |  |
| 249 | `CreateRestrictedToken` | `0xFF300` | 527 | UnwindData |  |
| 1923 | `WTSIsServerContainer` | `0xFF520` | 27 | UnwindData |  |
| 1667 | `SetProcessMitigationPolicy` | `0xFF5D0` | 412 | UnwindData |  |
| 1235 | `PathGetCharTypeW` | `0xFF7D0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 196 | `CreateActCtxW` | `0xFF850` | 59 | UnwindData |  |
| 1537 | `ResolveDelayLoadedAPI` | `0xFF8A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 927 | `HeapSetInformation` | `0xFF8C0` | 42 | UnwindData |  |
| 295 | `DeleteStateAtomValue` | `0xFF8F0` | 84 | UnwindData |  |
| 1717 | `SetTokenInformation` | `0xFFC30` | 42 | UnwindData |  |
| 789 | `GetSerializedAtomBytes` | `0xFFC60` | 191 | UnwindData |  |
| 890 | `GetUserPreferredUILanguages` | `0xFFE80` | 89 | UnwindData |  |
| 1005 | `IsNLSDefinedString` | `0xFFEE0` | 131 | UnwindData |  |
| 157 | `ClosePrivateNamespace` | `0xFFFA0` | 235 | UnwindData |  |
| 180 | `ContinueDebugEvent` | `0x100130` | 86 | UnwindData |  |
| 46 | `AllocateLocallyUniqueId` | `0x100240` | 42 | UnwindData |  |
| 429 | `FlsFree` | `0x100270` | 42 | UnwindData |  |
| 1330 | `PrefetchVirtualMemory` | `0x1002A0` | 73 | UnwindData |  |
| 2021 | `lstrcmp` | `0x1002F0` | 140 | UnwindData |  |
| 2022 | `lstrcmpA` | `0x1002F0` | 140 | UnwindData |  |
| 1563 | `SHRegGetUSValueA` | `0x100390` | 297 | UnwindData |  |
| 1565 | `SHRegOpenUSKeyA` | `0x1004C0` | 142 | UnwindData |  |
| 1569 | `SHRegQueryUSValueA` | `0x100560` | 384 | UnwindData |  |
| 1257 | `PathIsURLA` | `0x100770` | 58 | UnwindData |  |
| 1186 | `ParseURLA` | `0x1007B0` | 236 | UnwindData |  |
| 1639 | `SetFileSecurityW` | `0x100970` | 448 | UnwindData |  |
| 1678 | `SetSecurityAccessMask` | `0x100B40` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1075 | `LoadLibraryW` | `0x100BD0` | 1,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 989 | `IsCharLowerW` | `0x101080` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 652 | `GetLogicalProcessorInformation` | `0x1010D0` | 142 | UnwindData |  |
| 1541 | `RestoreThreadPreferredUILanguages` | `0x101170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1203 | `PathCchCanonicalize` | `0x101190` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1057 | `K32QueryWorkingSet` | `0x1011F0` | 79 | UnwindData |  |
| 1394 | `QueryWorkingSet` | `0x1011F0` | 79 | UnwindData |  |
| 118 | `CallEnclave` | `0x101370` | 97 | UnwindData |  |
| 854 | `GetThreadIOPendingFlag` | `0x1017B0` | 88 | UnwindData |  |
| 1810 | `TestClose` | `0x101810` | 107 | UnwindData |  |
| 1670 | `SetProcessShutdownParameters` | `0x101890` | 35 | UnwindData |  |
| 785 | `GetSecurityDescriptorLength` | `0x101990` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1818 | `TlsAlloc` | `0x101A60` | 52 | UnwindData |  |
| 1968 | `Wow64DisableWow64FsRedirection` | `0x101AA0` | 50 | UnwindData |  |
| 490 | `GetCommandLineA` | `0x101AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1101 | `MapGenericMask` | `0x101AF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1922 | `WTSGetServiceSessionId` | `0x101B10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1083 | `LocalFileTimeToFileTime` | `0x101B30` | 159 | UnwindData |  |
| 719 | `GetPackagePathByFullName2` | `0x101C30` | 78 | UnwindData |  |
| 260 | `CreateThreadpoolCleanupGroup` | `0x101C90` | 60 | UnwindData |  |
| 1625 | `SetEnvironmentVariableW` | `0x101CE0` | 128 | UnwindData |  |
| 228 | `CreateMemoryResourceNotification` | `0x101D70` | 181 | UnwindData |  |
| 831 | `GetSystemTimeAdjustment` | `0x101E30` | 145 | UnwindData |  |
| 1412 | `ReOpenFile` | `0x101ED0` | 570 | UnwindData |  |
| 1624 | `SetEnvironmentVariableA` | `0x102110` | 293 | UnwindData |  |
| 622 | `GetFileVersionInfoSizeW` | `0x102240` | 3,472 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `CancelIo` | `0x102FD0` | 55 | UnwindData |  |
| 1006 | `IsNormalizedString` | `0x103010` | 114 | UnwindData |  |
| 898 | `GetVolumePathNameW` | `0x103090` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 583 | `GetEnabledXStateFeatures` | `0x103100` | 41 | UnwindData |  |
| 259 | `CreateThreadpool` | `0x1031B0` | 63 | UnwindData |  |
| 1572 | `SHRegSetUSValueW` | `0x103230` | 200 | UnwindData |  |
| 1552 | `SHRegCreateUSKeyW` | `0x103300` | 217 | UnwindData |  |
| 257 | `CreateSymbolicLinkW` | `0x103860` | 1,137 | UnwindData |  |
| 279 | `DefineDosDeviceW` | `0x103D00` | 449 | UnwindData |  |
| 127 | `ChangeTimerQueueTimer` | `0x104040` | 78 | UnwindData |  |
| 726 | `GetPackageSecurityProperty` | `0x104190` | 177 | UnwindData |  |
| 146 | `CheckRemoteDebuggerPresent` | `0x104270` | 119 | UnwindData |  |
| 1406 | `QuirkIsEnabledForPackage3` | `0x1042F0` | 104 | UnwindData |  |
| 1458 | `RegFlushKey` | `0x1044C0` | 233 | UnwindData |  |
| 145 | `CheckIsMSIXPackage` | `0x1045B0` | 396 | UnwindData |  |
| 1807 | `TerminateProcess` | `0x104750` | 98 | UnwindData |  |
| 234 | `CreatePipe` | `0x1047C0` | 609 | UnwindData |  |
| 74 | `AppXPostSuccessExtension` | `0x104A30` | 298 | UnwindData |  |
| 1374 | `QueryInterruptTime` | `0x104C30` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1365 | `QueryActCtxW` | `0x104CD0` | 132 | UnwindData |  |
| 936 | `ImpersonateAnonymousToken` | `0x104D60` | 42 | UnwindData |  |
| 1748 | `StrCmpCA` | `0x104D90` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1503 | `RegisterStateChangeNotification` | `0x104F20` | 200 | UnwindData |  |
| 549 | `GetCurrentPackageResourcesContext` | `0x105200` | 232 | UnwindData |  |
| 195 | `CouldMultiUserAppsBehaviorBePossibleForPackage` | `0x105350` | 191 | UnwindData |  |
| 1191 | `PathAddExtensionW` | `0x105420` | 135 | UnwindData |  |
| 1148 | `OpenPackageInfoByFullNameForMachine` | `0x1054B0` | 123 | UnwindData |  |
| 818 | `GetSystemDefaultUILanguage` | `0x105AD0` | 75 | UnwindData |  |
| 1029 | `IsWow64GuestMachineSupported` | `0x105B30` | 57 | UnwindData |  |
| 238 | `CreatePrivateObjectSecurityWithMultipleInheritance` | `0x105C30` | 101 | UnwindData |  |
| 1466 | `RegKrnGetTermsrvRegistryExtensionFlags` | `0x105CA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1522 | `RemoveDirectoryW` | `0x105CB0` | 47 | UnwindData |  |
| 1472 | `RegLoadKeyA` | `0x106050` | 468 | UnwindData |  |
| 1473 | `RegLoadKeyW` | `0x106230` | 319 | UnwindData |  |
| 559 | `GetDateFormatA` | `0x106540` | 322 | UnwindData |  |
| 182 | `ConvertDefaultLocale` | `0x106690` | 39 | UnwindData |  |
| 552 | `GetCurrentProcessId` | `0x1066C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 935 | `IdnToUnicode` | `0x1066E0` | 95 | UnwindData |  |
| 1468 | `RegKrnSetDllHasThreadStateGlobal` | `0x106750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 747 | `GetProcessHandleCount` | `0x106760` | 80 | UnwindData |  |
| 1799 | `SubscribeWdagEnabledStateChange` | `0x106800` | 220 | UnwindData |  |
| 1224 | `PathFileExistsA` | `0x106980` | 82 | UnwindData |  |
| 1796 | `SubscribeEdpEnabledStateChange` | `0x106B70` | 220 | UnwindData |  |
| 582 | `GetEightBitStringToUnicodeStringRoutine` | `0x106C60` | 1,008 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 485 | `GetCommModemStatus` | `0x107050` | 225 | UnwindData |  |
| 1819 | `TlsFree` | `0x107140` | 42 | UnwindData |  |
| 1798 | `SubscribeStateChangeNotification` | `0x107340` | 163 | UnwindData |  |
| 1711 | `SetThreadpoolThreadMinimum` | `0x107670` | 49 | UnwindData |  |
| 541 | `GetCurrentPackageGlobalizationContext` | `0x1076B0` | 174 | UnwindData |  |
| 1679 | `SetSecurityDescriptorControl` | `0x107840` | 42 | UnwindData |  |
| 1949 | `WerRegisterMemoryBlock` | `0x107930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 639 | `GetIsWdagEnabled` | `0x107940` | 109 | UnwindData |  |
| 299 | `DeleteTimerQueue` | `0x107B50` | 26 | UnwindData |  |
| 300 | `DeleteTimerQueueEx` | `0x107B70` | 85 | UnwindData |  |
| 1794 | `SubmitIoRing` | `0x107BD0` | 118 | UnwindData |  |
| 111 | `BuildIoRingReadFile` | `0x107C50` | 518 | UnwindData |  |
| 634 | `GetHivePath` | `0x108300` | 205 | UnwindData |  |
| 947 | `InitializeContext` | `0x108550` | 90 | UnwindData |  |
| 948 | `InitializeContext2` | `0x1085B0` | 258 | UnwindData |  |
| 1159 | `OpenStateExplicitForUserSidString` | `0x1086C0` | 136 | UnwindData |  |
| 1888 | `VerQueryValueA` | `0x108AF0` | 20 | UnwindData |  |
| 877 | `GetUILanguageInfo` | `0x108BA0` | 127 | UnwindData |  |
| 416 | `FindNextChangeNotification` | `0x108C30` | 99 | UnwindData |  |
| 303 | `DeriveCapabilitySidsFromName` | `0x108CA0` | 285 | UnwindData |  |
| 1502 | `RegisterGPNotificationInternal` | `0x108DD0` | 67 | UnwindData |  |
| 1184 | `ParseApplicationUserModelId` | `0x108ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1328 | `PopIoRingCompletion` | `0x108EE0` | 224 | UnwindData |  |
| 1069 | `LoadEnclaveData` | `0x109100` | 103 | UnwindData |  |
| 1247 | `PathIsRootW` | `0x109210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 733 | `GetPackagesByPackageFamily` | `0x109230` | 50 | UnwindData |  |
| 1347 | `PsmIsDynamicKey` | `0x109270` | 33 | UnwindData |  |
| 994 | `IsCharUpperW` | `0x1092A0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 537 | `GetCurrentPackageApplicationResourcesContext` | `0x109300` | 258 | UnwindData |  |
| 718 | `GetPackagePathByFullName` | `0x109410` | 77 | UnwindData |  |
| 692 | `GetOsSafeBootMode` | `0x109470` | 224 | UnwindData |  |
| 1986 | `WriteFileGather` | `0x109560` | 191 | UnwindData |  |
| 1384 | `QueryProtectedPolicy` | `0x109630` | 42 | UnwindData |  |
| 1242 | `PathIsPrefixA` | `0x1096B0` | 86 | UnwindData |  |
| 1219 | `PathCommonPrefixA` | `0x109710` | 408 | UnwindData |  |
| 268 | `CreateWaitableTimerW` | `0x109900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1404 | `QuirkIsEnabledForPackage` | `0x109920` | 94 | UnwindData |  |
| 853 | `GetThreadGroupAffinity` | `0x109990` | 61 | UnwindData |  |
| 879 | `GetUnicodeStringToEightBitStringRoutine` | `0x1099E0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 679 | `GetNamedPipeInfo` | `0x109B30` | 222 | UnwindData |  |
| 678 | `GetNamedPipeHandleStateW` | `0x109C20` | 396 | UnwindData |  |
| 427 | `FindVolumeClose` | `0x109E40` | 45 | UnwindData |  |
| 174 | `CompareObjectHandles` | `0x109E80` | 42 | UnwindData |  |
| 41 | `AdjustTokenGroups` | `0x10A490` | 61 | UnwindData |  |
| 724 | `GetPackageResourcesProperty` | `0x10A580` | 216 | UnwindData |  |
| 734 | `GetPerformanceInfo` | `0x10A6B0` | 745 | UnwindData |  |
| 1050 | `K32GetPerformanceInfo` | `0x10A6B0` | 745 | UnwindData |  |
| 96 | `BaseFreeAppCompatDataForProcess` | `0x10A9A0` | 40 | UnwindData |  |
| 407 | `FindFirstFileExFromAppW` | `0x10A9D0` | 311 | UnwindData |  |
| 602 | `GetFileAttributesExFromAppW` | `0x10AB10` | 172 | UnwindData |  |
| 215 | `CreateFile2FromAppW` | `0x10AC30` | 207 | UnwindData |  |
| 265 | `CreateTimerQueue` | `0x10AE50` | 53 | UnwindData |  |
| 534 | `GetCurrentDirectoryA` | `0x10AEB0` | 400 | UnwindData |  |
| 1241 | `PathIsLFNFileSpecW` | `0x10B090` | 143 | UnwindData |  |
| 1674 | `SetProcessWorkingSetSizeEx` | `0x10B130` | 250 | UnwindData |  |
| 327 | `EmptyWorkingSet` | `0x10B230` | 193 | UnwindData |  |
| 1032 | `K32EmptyWorkingSet` | `0x10B230` | 193 | UnwindData |  |
| 341 | `EnumDeviceDrivers` | `0x10B430` | 456 | UnwindData |  |
| 1033 | `K32EnumDeviceDrivers` | `0x10B430` | 456 | UnwindData |  |
| 1734 | `StrCSpnA` | `0x10B600` | 89 | UnwindData |  |
| 1948 | `WerRegisterFile` | `0x10B660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 372 | `EqualPrefixSid` | `0x10B670` | 63 | UnwindData |  |
| 220 | `CreateFileMappingFromApp` | `0x10B770` | 204 | UnwindData |  |
| 1763 | `StrCpyNW` | `0x10B880` | 24 | UnwindData |  |
| 1765 | `StrCpyNXW` | `0x10B8A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1407 | `QuirkIsEnabledForPackage4` | `0x10B8E0` | 102 | UnwindData |  |
| 1844 | `UnregisterGPNotificationInternal` | `0x10B9D0` | 57 | UnwindData |  |
| 682 | `GetNumaHighestNodeNumber` | `0x10BA10` | 109 | UnwindData |  |
| 709 | `GetPackageGlobalizationProperty` | `0x10BA90` | 132 | UnwindData |  |
| 787 | `GetSecurityDescriptorRMControl` | `0x10BB20` | 34 | UnwindData |  |
| 1263 | `PathMatchSpecExW` | `0x10BE20` | 37 | UnwindData |  |
| 1428 | `ReadFileScatter` | `0x10BE50` | 193 | UnwindData |  |
| 690 | `GetOEMCP` | `0x10BF20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1605 | `SetConsoleInputExeNameW` | `0x10BF30` | 142 | UnwindData |  |
| 76 | `AppXReleaseAppXContext` | `0x10BFD0` | 38 | UnwindData |  |
| 282 | `DeleteAce` | `0x10C000` | 42 | UnwindData |  |
| 1620 | `SetDefaultDllDirectories` | `0x10C030` | 42 | UnwindData |  |
| 1078 | `LoadStringA` | `0x10C1F0` | 152 | UnwindData |  |
| 531 | `GetCurrentApplicationUserModelId` | `0x10C430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 925 | `HeapQueryInformation` | `0x10C450` | 52 | UnwindData |  |
| 1686 | `SetStdHandle` | `0x10C490` | 99 | UnwindData |  |
| 1958 | `WerUnregisterMemoryBlock` | `0x10C500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 684 | `GetNumaNodeProcessorMaskEx` | `0x10C510` | 156 | UnwindData |  |
| 578 | `GetDynamicTimeZoneInformationEffectiveYears` | `0x10C5C0` | 290 | UnwindData |  |
| 609 | `GetFileMUIPath` | `0x10C790` | 99 | UnwindData |  |
| 901 | `GetWindowsDirectoryA` | `0x10C800` | 67 | UnwindData |  |
| 836 | `GetSystemWindowsDirectoryA` | `0x10C850` | 134 | UnwindData |  |
| 440 | `FormatApplicationUserModelId` | `0x10C8E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 765 | `GetProcessorSystemCycleTime` | `0x10C8F0` | 114 | UnwindData |  |
| 1589 | `SetCommMask` | `0x10C980` | 271 | UnwindData |  |
| 28 | `AddDllDirectory` | `0x10CAA0` | 86 | UnwindData |  |
| 1851 | `UnsubscribeStateChangeNotification` | `0x10CB00` | 70 | UnwindData |  |
| 1783 | `StrStrNIW` | `0x10CBC0` | 158 | UnwindData |  |
| 1745 | `StrChrNIW` | `0x10CC70` | 100 | UnwindData |  |
| 908 | `GlobalFlags` | `0x10CCE0` | 338 | UnwindData |  |
| 1797 | `SubscribeFeatureUsageFlush` | `0x10D250` | 1,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1697 | `SetThreadIdealProcessorEx` | `0x10D770` | 80 | UnwindData |  |
| 406 | `FindFirstFileExA` | `0x10D7D0` | 434 | UnwindData |  |
| 852 | `GetThreadErrorMode` | `0x10D990` | 61 | UnwindData |  |
| 332 | `EnterCriticalPolicySectionInternal` | `0x10DAB0` | 55 | UnwindData |  |
| 1641 | `SetFileValidData` | `0x10DB20` | 77 | UnwindData |  |
| 2005 | `__wgetmainargs` | `0x10DB80` | 77 | UnwindData |  |
| 1683 | `SetSecurityDescriptorRMControl` | `0x10E6C0` | 24 | UnwindData |  |
| 1192 | `PathAllocCanonicalize` | `0x10E6E0` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1957 | `WerUnregisterFile` | `0x10E930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `AddMandatoryAce` | `0x10E940` | 57 | UnwindData |  |
| 1004 | `IsMrtResourceRedirectionEnabled` | `0x10EAD0` | 391 | UnwindData |  |
| 1492 | `RegSaveKeyExW` | `0x10ED20` | 427 | UnwindData |  |
| 1411 | `RaiseFailFastException` | `0x10F110` | 465 | UnwindData |  |
| 725 | `GetPackageSecurityContext` | `0x10F610` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `BaseIsAppcompatInfrastructureDisabled` | `0x10F830` | 40 | UnwindData |  |
| 624 | `GetFinalPathNameByHandleA` | `0x10FB70` | 431 | UnwindData |  |
| 1971 | `Wow64RevertWow64FsRedirection` | `0x10FDA0` | 53 | UnwindData |  |
| 1692 | `SetThreadContext` | `0x10FDE0` | 42 | UnwindData |  |
| 1849 | `UnsubscribeEdpEnabledStateChange` | `0x10FFD0` | 75 | UnwindData |  |
| 1852 | `UnsubscribeWdagEnabledStateChange` | `0x10FFD0` | 75 | UnwindData |  |
| 1669 | `SetProcessPriorityBoost` | `0x110030` | 68 | UnwindData |  |
| 102 | `BaseReadAppCompatDataForProcess` | `0x110080` | 75 | UnwindData |  |
| 161 | `CloseStateChangeNotification` | `0x1100E0` | 36 | UnwindData |  |
| 819 | `GetSystemDirectoryA` | `0x110240` | 134 | UnwindData |  |
| 367 | `EnumUILanguagesW` | `0x110560` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1065 | `LeaveCriticalPolicySectionInternal` | `0x1106A0` | 57 | UnwindData |  |
| 656 | `GetMachineTypeAttributes` | `0x1106E0` | 247 | UnwindData |  |
| 1215 | `PathCchStripPrefix` | `0x110840` | 246 | UnwindData |  |
| 1106 | `MapViewOfFile3FromApp` | `0x110A30` | 228 | UnwindData |  |
| 1105 | `MapViewOfFile3` | `0x110B20` | 225 | UnwindData |  |
| 204 | `CreateDirectoryExW` | `0x110C10` | 4,401 | UnwindData |  |
| 283 | `DeleteBoundaryDescriptor` | `0x111D80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1162 | `OpenWaitableTimerW` | `0x111DA0` | 218 | UnwindData |  |
| 1405 | `QuirkIsEnabledForPackage2` | `0x111E80` | 104 | UnwindData |  |
| 1002 | `IsInternetESCEnabled` | `0x111EF0` | 172 | UnwindData |  |
| 882 | `GetUserDefaultLangID` | `0x112110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 488 | `GetCommState` | `0x112120` | 605 | UnwindData |  |
| 1280 | `PathRenameExtensionW` | `0x112390` | 122 | UnwindData |  |
| 1018 | `IsUserCetAvailableInEnvironment` | `0x112410` | 67 | UnwindData |  |
| 1132 | `NotifyRedirectedStringChange` | `0x112460` | 283 | UnwindData |  |
| 1433 | `RecordFeatureUsage2` | `0x112B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1499 | `RegUnLoadKeyW` | `0x112B70` | 318 | UnwindData |  |
| 1093 | `LocateXStateFeature` | `0x112CF0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 358 | `EnumSystemFirmwareTables` | `0x112DF0` | 295 | UnwindData |  |
| 1946 | `WerRegisterCustomMetadata` | `0x112F20` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 236 | `CreatePrivateObjectSecurity` | `0x112F60` | 62 | UnwindData |  |
| 1120 | `NeedCurrentDirectoryForExePathW` | `0x113030` | 46 | UnwindData |  |
| 770 | `GetPtrCalDataArray` | `0x113420` | 86 | UnwindData |  |
| 345 | `EnumPageFilesW` | `0x1134C0` | 348 | UnwindData |  |
| 1035 | `K32EnumPageFilesW` | `0x1134C0` | 348 | UnwindData |  |
| 1893 | `VerifyPackageFamilyName` | `0x113630` | 61 | UnwindData |  |
| 482 | `GetCalendarInfoW` | `0x113680` | 129 | UnwindData |  |
| 1244 | `PathIsRelativeA` | `0x113710` | 44 | UnwindData |  |
| 769 | `GetPtrCalData` | `0x113750` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 459 | `GetAcceptLanguagesW` | `0x113780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 924 | `HeapLock` | `0x113790` | 25 | UnwindData |  |
| 479 | `GetCachedSigningLevel` | `0x113840` | 85 | UnwindData |  |
| 360 | `EnumSystemGeoNames` | `0x1138E0` | 260 | UnwindData |  |
| 13 | `AcquireStateLock` | `0x113D00` | 167 | UnwindData |  |
| 1776 | `StrRStrIA` | `0x113DB0` | 198 | UnwindData |  |
| 1143 | `OpenFileMappingFromApp` | `0x113E80` | 124 | UnwindData |  |
| 1273 | `PathRemoveBlanksA` | `0x113F30` | 132 | UnwindData |  |
| 356 | `EnumResourceTypesExW` | `0x113FC0` | 30 | UnwindData |  |
| 1668 | `SetProcessPreferredUILanguages` | `0x115110` | 63 | UnwindData |  |
| 487 | `GetCommProperties` | `0x1151C0` | 266 | UnwindData |  |
| 1285 | `PathStripPathA` | `0x115700` | 69 | UnwindData |  |
| 1232 | `PathGetArgsA` | `0x115750` | 90 | UnwindData |  |
| 1925 | `WaitForDebugEvent` | `0x1157B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1147 | `OpenPackageInfoByFullName` | `0x1157C0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1950 | `WerRegisterRuntimeExceptionModule` | `0x1158C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1836 | `UnhandledExceptionFilter` | `0x1158D0` | 1,464 | UnwindData |  |
| 1924 | `WaitCommEvent` | `0x115EB0` | 195 | UnwindData |  |
| 717 | `GetPackagePath` | `0x115F80` | 168 | UnwindData |  |
| 1353 | `PssWalkMarkerCreate` | `0x116030` | 104 | UnwindData |  |
| 1591 | `SetCommTimeouts` | `0x1160A0` | 288 | UnwindData |  |
| 930 | `HeapUnlock` | `0x1161D0` | 25 | UnwindData |  |
| 1768 | `StrIsIntlEqualA` | `0x116460` | 57 | UnwindData |  |
| 1792 | `StrTrimA` | `0x1164A0` | 225 | UnwindData |  |
| 1076 | `LoadPackagedLibrary` | `0x116590` | 159 | UnwindData |  |
| 1618 | `SetCurrentDirectoryA` | `0x116640` | 208 | UnwindData |  |
| 843 | `GetTempFileNameA` | `0x116720` | 143 | UnwindData |  |
| 152 | `ClearCommBreak` | `0x1167F0` | 76 | UnwindData |  |
| 1362 | `PurgeComm` | `0x116850` | 222 | UnwindData |  |
| 1168 | `PackageFamilyNameFromId` | `0x116940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1969 | `Wow64EnableWow64FsRedirection` | `0x116950` | 39 | UnwindData |  |
| 402 | `FindCloseChangeNotification` | `0x116980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1222 | `PathCreateFromUrlAlloc` | `0x116990` | 201 | UnwindData |  |
| 746 | `GetProcessGroupAffinity` | `0x116A60` | 103 | UnwindData |  |
| 313 | `DsCrackNamesW` | `0x116E90` | 133 | UnwindData |  |
| 1623 | `SetEnvironmentStringsW` | `0x116F20` | 192 | UnwindData |  |
| 1583 | `SetCachedSigningLevel` | `0x116FF0` | 60 | UnwindData |  |
| 1350 | `PssDuplicateSnapshot` | `0x117040` | 130 | UnwindData |  |
| 1372 | `QueryIdleProcessorCycleTime` | `0x117160` | 75 | UnwindData |  |
| 452 | `FreeResource` | `0x1171C0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1732 | `SpecialMBToWC` | `0x1171C0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1250 | `PathIsUNCA` | `0x117230` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1523 | `RemoveDllDirectory` | `0x117260` | 42 | UnwindData |  |
| 1723 | `SetXStateFeaturesMask` | `0x117490` | 229 | UnwindData |  |
| 1859 | `UrlCanonicalizeA` | `0x117580` | 157 | UnwindData |  |
| 1516 | `ReleaseStateLock` | `0x1177A0` | 172 | UnwindData |  |
| 1171 | `PackageFullNameFromId` | `0x117890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1408 | `QuirkIsEnabledForProcess` | `0x1178A0` | 76 | UnwindData |  |
| 757 | `GetProcessPreferredUILanguages` | `0x117900` | 63 | UnwindData |  |
| 847 | `GetTempPathA` | `0x117950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 584 | `GetEnvironmentStrings` | `0x117960` | 336 | UnwindData |  |
| 585 | `GetEnvironmentStringsA` | `0x117960` | 336 | UnwindData |  |
| 420 | `FindNextStreamW` | `0x117C10` | 146 | UnwindData |  |
| 1878 | `UrlIsNoHistoryW` | `0x117CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 758 | `GetProcessPriorityBoost` | `0x117CC0` | 80 | UnwindData |  |
| 1351 | `PssFreeSnapshot` | `0x117E40` | 87 | UnwindData |  |
| 240 | `CreateProcessAsUserA` | `0x117EA0` | 105 | UnwindData |  |
| 315 | `DsFreeNameResultW` | `0x117F10` | 45 | UnwindData |  |
| 339 | `EnumDateFormatsExW` | `0x117FA0` | 80 | UnwindData |  |
| 920 | `HeapCompact` | `0x118000` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 698 | `GetPackageApplicationPropertyString` | `0x118150` | 93 | UnwindData |  |
| 337 | `EnumCalendarInfoW` | `0x1181E0` | 96 | UnwindData |  |
| 1261 | `PathMatchSpecA` | `0x118250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1673 | `SetProcessWorkingSetSize` | `0x118260` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `AppContainerUnregisterSid` | `0x118360` | 70 | UnwindData |  |
| 1951 | `WerSetFlags` | `0x1183B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1544 | `RsopLoggingEnabledInternal` | `0x1183C0` | 37 | UnwindData |  |
| 636 | `GetIntegratedDisplaySize` | `0x118610` | 150 | UnwindData |  |
| 1809 | `TerminateThread` | `0x1186B0` | 288 | UnwindData |  |
| 1911 | `VirtualAllocFromApp` | `0x1187E0` | 65 | UnwindData |  |
| 703 | `GetPackageFamilyNameFromFilePath` | `0x118830` | 58 | UnwindData |  |
| 1850 | `UnsubscribeFeatureUsageFlush` | `0x118870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1974 | `Wow64SuspendThread` | `0x118880` | 52 | UnwindData |  |
| 1099 | `MakeAbsoluteSD2` | `0x1188C0` | 42 | UnwindData |  |
| 123 | `CancelSynchronousIo` | `0x1188F0` | 57 | UnwindData |  |
| 1275 | `PathRemoveExtensionA` | `0x118930` | 53 | UnwindData |  |
| 1901 | `VerifyPackagePublisher` | `0x118AB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1959 | `WerUnregisterRuntimeExceptionModule` | `0x118AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1858 | `UrlApplySchemeW` | `0x118AF0` | 196 | UnwindData |  |
| 31 | `AddPackageDependency` | `0x118CA0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1001 | `IsEnclaveTypeSupported` | `0x118D60` | 63 | UnwindData |  |
| 940 | `IncrementPackageStatusVersion` | `0x118E30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1811 | `TestControlReporting` | `0x118E40` | 115 | UnwindData |  |
| 1943 | `WerGetFlags` | `0x118F80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1665 | `SetProcessGroupAffinity` | `0x118F90` | 166 | UnwindData |  |
| 207 | `CreateEnclave` | `0x119040` | 109 | UnwindData |  |
| 99 | `BaseInitAppcompatCacheSupport` | `0x1190C0` | 37 | UnwindData |  |
| 735 | `GetPersistedFileLocationW` | `0x1191E0` | 65 | UnwindData |  |
| 275 | `DebugBreak` | `0x119480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1970 | `Wow64GetThreadContext` | `0x119490` | 42 | UnwindData |  |
| 1268 | `PathQuoteSpacesW` | `0x1194F0` | 131 | UnwindData |  |
| 696 | `GetPackageApplicationIds` | `0x11A170` | 585 | UnwindData |  |
| 1660 | `SetProcessAffinityUpdateMode` | `0x11A620` | 83 | UnwindData |  |
| 1183 | `PackageSidFromFamilyName` | `0x11A680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1675 | `SetProtectedPolicy` | `0x11A690` | 42 | UnwindData |  |
| 1378 | `QueryOptionalDelayLoadedAPI` | `0x11A6C0` | 54 | UnwindData |  |
| 18 | `AddAccessDeniedAce` | `0x11A800` | 42 | UnwindData |  |
| 1926 | `WaitForDebugEventEx` | `0x11A830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 641 | `GetLargePageMinimum` | `0x11A840` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1071 | `LoadEnclaveImageW` | `0x11A8D0` | 83 | UnwindData |  |
| 312 | `DsBindWithSpnExW` | `0x11A930` | 122 | UnwindData |  |
| 878 | `GetUnicodeStringToEightBitSizeRoutine` | `0x11B0A0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 827 | `GetSystemMetadataPathForPackageFamily` | `0x11B140` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 538 | `GetCurrentPackageContext` | `0x11B380` | 133 | UnwindData |  |
| 1952 | `WerSetMaxProcessHoldMilliseconds` | `0x11B5E0` | 1,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 952 | `InitializeEnclave` | `0x11BBB0` | 52 | UnwindData |  |
| 697 | `GetPackageApplicationProperty` | `0x11BBF0` | 922 | UnwindData |  |
| 44 | `AllocConsoleWithOptions` | `0x11C0F0` | 229 | UnwindData |  |
| 521 | `GetConsoleProcessList` | `0x11C240` | 187 | UnwindData |  |
| 374 | `EscapeCommFunction` | `0x11C310` | 339 | UnwindData |  |
| 2018 | `exit` | `0x11D9A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1349 | `PssCaptureSnapshot` | `0x11D9C0` | 53 | UnwindData |  |
| 470 | `GetApplicationRestartSettings` | `0x11DA00` | 784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `AddDependencyToProcessPackageGraph` | `0x11DD10` | 3,203 | UnwindData |  |
| 1526 | `RemovePackageStatus` | `0x11E9A0` | 51 | UnwindData |  |
| 1853 | `UpdatePackageStatus` | `0x11E9E0` | 128 | UnwindData |  |
| 1996 | `__FC_Query_System` | `0x121DA0` | 44 | UnwindData |  |
| 294 | `DeleteProcThreadAttributeList` | `0x124610` | 5,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1068 | `LoadAppInitDlls` | `0x124610` | 5,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2006 | `_amsg_exit` | `0x124610` | 5,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `CeipIsOptedIn` | `0x125AE0` | 43 | UnwindData |  |
| 245 | `CreatePseudoConsole` | `0x1292B0` | 42 | UnwindData |  |
| 246 | `CreatePseudoConsoleAsUser` | `0x1292E0` | 560 | UnwindData |  |
| 344 | `EnumPageFilesA` | `0x1295C0` | 70 | UnwindData |  |
| 1034 | `K32EnumPageFilesA` | `0x1295C0` | 70 | UnwindData |  |
| 551 | `GetCurrentProcess` | `0x1299F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 556 | `GetCurrentThread` | `0x129A00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 462 | `GetAdjustObjectAttributesForPrivateNamespaceRoutine` | `0x129A10` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 200 | `CreateConsoleScreenBuffer` | `0x129AA0` | 697 | UnwindData |  |
| 581 | `GetEightBitStringToUnicodeSizeRoutine` | `0x129E10` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1642 | `SetHandleCount` | `0x129E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1465 | `RegKrnGetHKEY_ClassesRootAddress` | `0x129E60` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `BaseGetConsoleReference` | `0x129ED0` | 1,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 515 | `GetConsoleInputExeNameA` | `0x12A400` | 228 | UnwindData |  |
| 516 | `GetConsoleInputExeNameW` | `0x12A4F0` | 128 | UnwindData |  |
| 1604 | `SetConsoleInputExeNameA` | `0x12A600` | 142 | UnwindData |  |
| 1470 | `RegLoadAppKeyA` | `0x12A730` | 132 | UnwindData |  |
| 512 | `GetConsoleDisplayMode` | `0x12AAB0` | 109 | UnwindData |  |
| 1520 | `RemoveDirectoryA` | `0x12AC50` | 69 | UnwindData |  |
| 1511 | `ReleasePseudoConsole` | `0x12AD30` | 54 | UnwindData |  |
| 397 | `FillConsoleOutputCharacterA` | `0x12AD70` | 39 | UnwindData |  |
| 1421 | `ReadConsoleOutputCharacterW` | `0x12ADA0` | 41 | UnwindData |  |
| 1608 | `SetConsoleNumberOfCommandsW` | `0x12ADD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 390 | `ExpungeConsoleCommandHistoryW` | `0x12ADE0` | 800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2012 | `_invalid_parameter` | `0x12B100` | 258 | UnwindData |  |
| 2015 | `_purecall` | `0x12B350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2016 | `_time64` | `0x12B370` | 98 | UnwindData |  |
| 2033 | `time` | `0x12B3E0` | 16,816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1884 | `VerFindFileA` | `0x12F590` | 716 | UnwindData |  |
| 84 | `AreThereVisibleLogoffScriptsInternal` | `0x12F870` | 60 | UnwindData |  |
| 85 | `AreThereVisibleShutdownScriptsInternal` | `0x12F8C0` | 60 | UnwindData |  |
| 439 | `ForceSyncFgPolicyInternal` | `0x12F910` | 60 | UnwindData |  |
| 447 | `FreeGPOListInternalA` | `0x12F960` | 57 | UnwindData |  |
| 448 | `FreeGPOListInternalW` | `0x12F9A0` | 57 | UnwindData |  |
| 456 | `GenerateGPNotificationInternal` | `0x12F9E0` | 86 | UnwindData |  |
| 473 | `GetAppliedGPOListInternalA` | `0x12FA40` | 112 | UnwindData |  |
| 474 | `GetAppliedGPOListInternalW` | `0x12FAC0` | 112 | UnwindData |  |
| 628 | `GetGPOListInternalA` | `0x12FB40` | 119 | UnwindData |  |
| 629 | `GetGPOListInternalW` | `0x12FBC0` | 119 | UnwindData |  |
| 681 | `GetNextFgPolicyRefreshInfoInternal` | `0x12FC40` | 72 | UnwindData |  |
| 739 | `GetPreviousFgPolicyRefreshInfoInternal` | `0x12FC90` | 72 | UnwindData |  |
| 917 | `HasPolicyForegroundProcessingCompletedInternal` | `0x12FCE0` | 112 | UnwindData |  |
| 1013 | `IsSyncForegroundPolicyRefresh` | `0x12FD60` | 76 | UnwindData |  |
| 1435 | `RefreshPolicyExInternal` | `0x12FDC0` | 65 | UnwindData |  |
| 1436 | `RefreshPolicyInternal` | `0x12FE10` | 55 | UnwindData |  |
| 1927 | `WaitForMachinePolicyForegroundProcessingInternal` | `0x12FE50` | 50 | UnwindData |  |
| 1936 | `WaitForUserPolicyForegroundProcessingInternal` | `0x12FE90` | 50 | UnwindData |  |
| 1885 | `VerFindFileW` | `0x130100` | 856 | UnwindData |  |
| 314 | `DsFreeDomainControllerInfoW` | `0x130460` | 67 | UnwindData |  |
| 316 | `DsFreeNgcKey` | `0x1304B0` | 40 | UnwindData |  |
| 317 | `DsFreePasswordCredentials` | `0x1304E0` | 40 | UnwindData |  |
| 318 | `DsGetDomainControllerInfoW` | `0x130510` | 114 | UnwindData |  |
| 319 | `DsMakePasswordCredentialsW` | `0x130590` | 104 | UnwindData |  |
| 320 | `DsReadNgcKeyW` | `0x130600` | 104 | UnwindData |  |
| 321 | `DsUnBindW` | `0x130670` | 60 | UnwindData |  |
| 322 | `DsWriteNgcKeyW` | `0x1306C0` | 104 | UnwindData |  |
| 1990 | `ZombifyActCtx` | `0x130730` | 57 | UnwindData |  |
| 88 | `BaseCheckAppcompatCache` | `0x130770` | 91 | UnwindData |  |
| 89 | `BaseCheckAppcompatCacheEx` | `0x1307E0` | 158 | UnwindData |  |
| 90 | `BaseCleanupAppcompatCacheSupport` | `0x130890` | 45 | UnwindData |  |
| 93 | `BaseDumpAppcompatCache` | `0x1308D0` | 31 | UnwindData |  |
| 94 | `BaseFlushAppcompatCache` | `0x130900` | 37 | UnwindData |  |
| 103 | `BaseUpdateAppcompatCache` | `0x130930` | 75 | UnwindData |  |
| 469 | `GetApplicationRecoveryCallback` | `0x130990` | 171 | UnwindData |  |
| 1944 | `WerRegisterAdditionalProcess` | `0x130A50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1945 | `WerRegisterAppLocalDump` | `0x130A60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1947 | `WerRegisterExcludedMemoryBlock` | `0x130A70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1953 | `WerUnregisterAdditionalProcess` | `0x130A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1954 | `WerUnregisterAppLocalDump` | `0x130AA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1955 | `WerUnregisterCustomMetadata` | `0x130AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1956 | `WerUnregisterExcludedMemoryBlock` | `0x130AD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `AppXGetOSMinVersion` | `0x130AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `AppXUpdatePackageCapabilities` | `0x130AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 391 | `ExtensionProgIdExists` | `0x130AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 464 | `GetApiSetModuleBaseName` | `0x130AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 594 | `GetExtensionProgIds` | `0x130AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 704 | `GetPackageFamilyNameFromProgId` | `0x130AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `MsixIsSystemPackageByAppUserModelId` | `0x130AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1960 | `WerpNotifyLoadStringResource` | `0x130AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1961 | `WerpNotifyUseStringResource` | `0x130AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 988 | `IsCharLowerA` | `0x130AF0` | 120 | UnwindData |  |
| 993 | `IsCharUpperA` | `0x130B70` | 118 | UnwindData |  |
| 142 | `CheckAllowDecryptedRemoteDestinationPolicy` | `0x130DF0` | 216 | UnwindData |  |
| 1735 | `StrCSpnIA` | `0x131060` | 89 | UnwindData |  |
| 1736 | `StrCSpnIW` | `0x1310C0` | 98 | UnwindData |  |
| 1739 | `StrCatBuffW` | `0x131130` | 43 | UnwindData |  |
| 1740 | `StrCatChainW` | `0x131170` | 112 | UnwindData |  |
| 1764 | `StrCpyNXA` | `0x1311F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1770 | `StrPBrkA` | `0x131230` | 86 | UnwindData |  |
| 1772 | `StrRChrA` | `0x131290` | 111 | UnwindData |  |
| 1773 | `StrRChrIA` | `0x131310` | 127 | UnwindData |  |
| 1778 | `StrSpnA` | `0x1313A0` | 141 | UnwindData |  |
| 1779 | `StrSpnW` | `0x131440` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 985 | `IsCharBlankW` | `0x131490` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 986 | `IsCharCntrlW` | `0x1314D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 987 | `IsCharDigitW` | `0x131500` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 990 | `IsCharPunctW` | `0x131550` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 991 | `IsCharSpaceA` | `0x1315A0` | 73 | UnwindData |  |
| 995 | `IsCharXDigitW` | `0x1315F0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 293 | `DeletePersistedRegistryValue` | `0x131650` | 544 | UnwindData |  |
| 1653 | `SetPersistedRegistryBOOL` | `0x131880` | 40 | UnwindData |  |
| 1654 | `SetPersistedRegistryDWORD` | `0x131880` | 40 | UnwindData |  |
| 1655 | `SetPersistedRegistryString` | `0x1318B0` | 105 | UnwindData |  |
| 1656 | `SetPersistedRegistryValue` | `0x131920` | 630 | UnwindData |  |
| 1399 | `QuirkGetData` | `0x131BA0` | 60 | UnwindData |  |
| 1400 | `QuirkGetData2` | `0x131BF0` | 62 | UnwindData |  |
| 1402 | `QuirkIsEnabled2` | `0x131C40` | 57 | UnwindData |  |
| 188 | `CopyContext` | `0x131C80` | 49 | UnwindData |  |
| 328 | `EnableProcessOptionalXStateFeatures` | `0x131CC0` | 111 | UnwindData |  |
| 851 | `GetThreadEnabledXStateFeatures` | `0x131D40` | 40 | UnwindData |  |
| 906 | `GetXStateFeaturesMask` | `0x131D70` | 192 | UnwindData |  |
| 630 | `GetGamingDeviceModelInformation` | `0x131E40` | 316 | UnwindData |  |
| 191 | `CopyFileFromAppW` | `0x131FF0` | 154 | UnwindData |  |
| 205 | `CreateDirectoryFromAppW` | `0x132090` | 149 | UnwindData |  |
| 218 | `CreateFileFromAppW` | `0x132130` | 130 | UnwindData |  |
| 290 | `DeleteFileFromAppW` | `0x1321C0` | 143 | UnwindData |  |
| 1112 | `MoveFileFromAppW` | `0x132260` | 167 | UnwindData |  |
| 1521 | `RemoveDirectoryFromAppW` | `0x132310` | 143 | UnwindData |  |
| 1531 | `ReplaceFileFromAppW` | `0x1323B0` | 188 | UnwindData |  |
| 1633 | `SetFileAttributesFromAppW` | `0x132480` | 149 | UnwindData |  |
| 1213 | `PathCchRenameExtension` | `0x132610` | 306 | UnwindData |  |
| 1551 | `SHRegCreateUSKeyA` | `0x1328D0` | 142 | UnwindData |  |
| 1553 | `SHRegDeleteEmptyUSKeyA` | `0x132970` | 141 | UnwindData |  |
| 1554 | `SHRegDeleteEmptyUSKeyW` | `0x132A10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1555 | `SHRegDeleteUSValueA` | `0x132A30` | 138 | UnwindData |  |
| 1556 | `SHRegDeleteUSValueW` | `0x132AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1561 | `SHRegGetBoolUSValueA` | `0x132AD0` | 173 | UnwindData |  |
| 1221 | `PathCreateFromUrlA` | `0x132F70` | 340 | UnwindData |  |
| 1857 | `UrlApplySchemeA` | `0x1330D0` | 340 | UnwindData |  |
| 1863 | `UrlCompareA` | `0x133230` | 390 | UnwindData |  |
| 1865 | `UrlCreateFromPathA` | `0x1333C0` | 336 | UnwindData |  |
| 1867 | `UrlEscapeA` | `0x133520` | 354 | UnwindData |  |
| 1869 | `UrlFixupW` | `0x133690` | 859 | UnwindData |  |
| 1870 | `UrlGetLocationA` | `0x133A00` | 190 | UnwindData |  |
| 1874 | `UrlHashA` | `0x133AD0` | 81 | UnwindData |  |
| 1875 | `UrlHashW` | `0x133B30` | 165 | UnwindData |  |
| 1876 | `UrlIsA` | `0x133BE0` | 254 | UnwindData |  |
| 1877 | `UrlIsNoHistoryA` | `0x133CF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1879 | `UrlIsOpaqueA` | `0x133D00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1880 | `UrlIsOpaqueW` | `0x133D10` | 17,392 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1964 | `WilFailureWatcherResume` | `0x138100` | 41 | UnwindData |  |
| 1966 | `WilFailureWatcherSuspend` | `0x138130` | 41 | UnwindData |  |
| 976 | `InternetTimeFromSystemTimeW` | `0x138300` | 285 | UnwindData |  |
| 978 | `InternetTimeToSystemTimeW` | `0x138430` | 238 | UnwindData |  |
| 109 | `BuildIoRingCancelRequest` | `0x138C40` | 198 | UnwindData |  |
| 110 | `BuildIoRingFlushFile` | `0x138D10` | 283 | UnwindData |  |
| 112 | `BuildIoRingReadFileScatter` | `0x138E40` | 281 | UnwindData |  |
| 113 | `BuildIoRingRegisterBuffers` | `0x138F60` | 169 | UnwindData |  |
| 114 | `BuildIoRingRegisterFileHandles` | `0x139010` | 200 | UnwindData |  |
| 115 | `BuildIoRingWriteFile` | `0x1390E0` | 339 | UnwindData |  |
| 116 | `BuildIoRingWriteFileGather` | `0x139240` | 323 | UnwindData |  |
| 155 | `CloseIoRing` | `0x139390` | 52 | UnwindData |  |
| 227 | `CreateIoRing` | `0x1393D0` | 250 | UnwindData |  |
| 637 | `GetIoRingInfo` | `0x1394D0` | 79 | UnwindData |  |
| 1003 | `IsIoRingOpSupported` | `0x139530` | 53 | UnwindData |  |
| 1376 | `QueryIoRingCapabilities` | `0x139570` | 150 | UnwindData |  |
| 1644 | `SetIoRingCompletionEvent` | `0x139610` | 169 | UnwindData |  |
| 1123 | `NlsGetACPFromLocale` | `0x1396C0` | 94 | UnwindData |  |
| 886 | `GetUserInfo` | `0x139830` | 36 | UnwindData |  |
| 887 | `GetUserInfoWord` | `0x139860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1021 | `IsValidLanguageGroup` | `0x139880` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1121 | `NlsCheckPolicy` | `0x1398C0` | 72 | UnwindData |  |
| 1127 | `NlsUpdateSystemLocale` | `0x139910` | 129 | UnwindData |  |
| 1584 | `SetCalendarInfoW` | `0x139C80` | 353 | UnwindData |  |
| 1886 | `VerLanguageNameA` | `0x13A100` | 239 | UnwindData |  |
| 336 | `EnumCalendarInfoExW` | `0x13A200` | 97 | UnwindData |  |
| 340 | `EnumDateFormatsW` | `0x13A270` | 77 | UnwindData |  |
| 343 | `EnumLanguageGroupLocalesW` | `0x13A2D0` | 23 | UnwindData |  |
| 357 | `EnumSystemCodePagesW` | `0x13A2F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 361 | `EnumSystemLanguageGroupsW` | `0x13A310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 366 | `EnumTimeFormatsW` | `0x13A330` | 75 | UnwindData |  |
| 969 | `Internal_EnumLanguageGroupLocales` | `0x13A390` | 885 | UnwindData |  |
| 970 | `Internal_EnumSystemCodePages` | `0x13A710` | 633 | UnwindData |  |
| 971 | `Internal_EnumSystemLanguageGroups` | `0x13A990` | 348 | UnwindData |  |
| 529 | `GetCurrencyFormatW` | `0x13CEC0` | 135 | UnwindData |  |
| 608 | `GetFileMUIInfo` | `0x13CFA0` | 1,660 | UnwindData |  |
| 934 | `IdnToNameprepUnicode` | `0x13D690` | 95 | UnwindData |  |
| 1905 | `VerifyScripts` | `0x13D700` | 600 | UnwindData |  |
| 1719 | `SetUserGeoID` | `0x13DC00` | 21 | UnwindData |  |
| 1024 | `IsValidNLSVersion` | `0x13DCA0` | 108 | UnwindData |  |
| 83 | `AreShortNamesEnabled` | `0x13E090` | 288 | UnwindData |  |
| 654 | `GetLongPathNameA` | `0x13E640` | 547 | UnwindData |  |
| 1821 | `TlsGetValue2` | `0x13E870` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 691 | `GetOsManufacturingMode` | `0x13E930` | 302 | UnwindData |  |
| 1390 | `QueryThreadpoolStackInformation` | `0x13EAA0` | 49 | UnwindData |  |
| 1709 | `SetThreadpoolStackInformation` | `0x13EAE0` | 49 | UnwindData |  |
| 1371 | `QueryGlobalizationUserSettingsStatus` | `0x13EB20` | 136 | UnwindData |  |
| 2007 | `_c_exit` | `0x13EBB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2008 | `_cexit` | `0x13EBD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2009 | `_exit` | `0x13EBF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2020 | `hwprintf` | `0x13EC10` | 34 | UnwindData |  |
| 2034 | `wprintf` | `0x13EE20` | 46 | UnwindData |  |
| 1188 | `PathAddBackslashA` | `0x13F120` | 45 | UnwindData |  |
| 1252 | `PathIsUNCServerA` | `0x13F160` | 74 | UnwindData |  |
| 1253 | `PathIsUNCServerShareA` | `0x13F1B0` | 92 | UnwindData |  |
| 1265 | `PathParseIconLocationA` | `0x13F220` | 128 | UnwindData |  |
| 1267 | `PathQuoteSpacesA` | `0x13F2B0` | 125 | UnwindData |  |
| 1289 | `PathUnExpandEnvStringsA` | `0x13F340` | 26 | UnwindData |  |
| 1291 | `PathUnquoteSpacesA` | `0x13F360` | 78 | UnwindData |  |
| 1546 | `SHExpandEnvironmentStringsA` | `0x13F3C0` | 89 | UnwindData |  |
| 1575 | `SHTruncateString` | `0x13F420` | 132 | UnwindData |  |
| 1190 | `PathAddExtensionA` | `0x13F4B0` | 124 | UnwindData |  |
| 1230 | `PathFindNextComponentA` | `0x13F540` | 77 | UnwindData |  |
| 1234 | `PathGetCharTypeA` | `0x13F5A0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1238 | `PathIsFileSpecA` | `0x13F610` | 52 | UnwindData |  |
| 1240 | `PathIsLFNFileSpecA` | `0x13F650` | 127 | UnwindData |  |
| 1246 | `PathIsRootA` | `0x13F6E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1248 | `PathIsSameRootA` | `0x13F6F0` | 111 | UnwindData |  |
| 1259 | `PathIsValidCharA` | `0x13F770` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1269 | `PathRelativePathToA` | `0x13F830` | 402 | UnwindData |  |
| 1271 | `PathRemoveBackslashA` | `0x13F9D0` | 74 | UnwindData |  |
| 1281 | `PathSearchAndQualifyA` | `0x13FA20` | 161 | UnwindData |  |
| 1283 | `PathSkipRootA` | `0x13FAD0` | 71 | UnwindData |  |
| 1557 | `SHRegEnumUSKeyA` | `0x13FB20` | 338 | UnwindData |  |
| 1559 | `SHRegEnumUSValueA` | `0x13FC80` | 412 | UnwindData |  |
| 1567 | `SHRegQueryInfoUSKeyA` | `0x13FE30` | 365 | UnwindData |  |
| 1571 | `SHRegSetUSValueA` | `0x13FFB0` | 141 | UnwindData |  |
| 1573 | `SHRegWriteUSValueA` | `0x140050` | 403 | UnwindData |  |
| 1517 | `RemapPredefinedHandleInternal` | `0x1402F0` | 381 | UnwindData |  |
| 775 | `GetRegistryExtensionFlags` | `0x140480` | 367 | UnwindData |  |
| 1462 | `RegKrnGetAppKeyEventAddressInternal` | `0x140600` | 49 | UnwindData |  |
| 1463 | `RegKrnGetAppKeyLoaded` | `0x140640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1467 | `RegKrnResetAppKeyLoaded` | `0x140650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1469 | `RegKrnSetTermsrvRegistryExtensionFlags` | `0x140670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1456 | `RegEnumValueA` | `0x140680` | 2,252 | UnwindData |  |
| 1498 | `RegUnLoadKeyA` | `0x140F60` | 400 | UnwindData |  |
| 1474 | `RegLoadMUIStringA` | `0x141100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1485 | `RegQueryMultipleValuesA` | `0x141110` | 1,853 | UnwindData |  |
| 1489 | `RegRestoreKeyA` | `0x141860` | 322 | UnwindData |  |
| 1490 | `RegRestoreKeyW` | `0x1419B0` | 263 | UnwindData |  |
| 1491 | `RegSaveKeyExA` | `0x141AC0` | 475 | UnwindData |  |
| 348 | `EnumProcesses` | `0x141E70` | 487 | UnwindData |  |
| 1038 | `K32EnumProcesses` | `0x141E70` | 487 | UnwindData |  |
| 904 | `GetWsChanges` | `0x142060` | 32 | UnwindData |  |
| 1054 | `K32GetWsChanges` | `0x142060` | 32 | UnwindData |  |
| 905 | `GetWsChangesEx` | `0x142090` | 31 | UnwindData |  |
| 1055 | `K32GetWsChangesEx` | `0x142090` | 31 | UnwindData |  |
| 954 | `InitializeProcessForWsWatch` | `0x1420C0` | 81 | UnwindData |  |
| 1056 | `K32InitializeProcessForWsWatch` | `0x1420C0` | 81 | UnwindData |  |
| 657 | `GetMappedFileNameA` | `0x142120` | 187 | UnwindData |  |
| 1043 | `K32GetMappedFileNameA` | `0x142120` | 187 | UnwindData |  |
| 1337 | `PsmCreateKeyWithDynamicId` | `0x1421F0` | 266 | UnwindData |  |
| 1338 | `PsmEqualApplication` | `0x142300` | 230 | UnwindData |  |
| 1339 | `PsmEqualPackage` | `0x1423F0` | 131 | UnwindData |  |
| 1346 | `PsmIsChildKey` | `0x142480` | 77 | UnwindData |  |
| 172 | `CommitStateAtom` | `0x142B60` | 327 | UnwindData |  |
| 463 | `GetAlternatePackageRoots` | `0x142CB0` | 29 | UnwindData |  |
| 829 | `GetSystemStateRootFolder` | `0x142CB0` | 29 | UnwindData |  |
| 1576 | `SaveAlternatePackageRootPath` | `0x142CB0` | 29 | UnwindData |  |
| 1577 | `SaveStateRootFolderPath` | `0x142CB0` | 29 | UnwindData |  |
| 779 | `GetRoamingLastObservedChangeTime` | `0x142CE0` | 159 | UnwindData |  |
| 790 | `GetSharedLocalFolder` | `0x142D90` | 191 | UnwindData |  |
| 800 | `GetStateContainerDepth` | `0x142E60` | 133 | UnwindData |  |
| 804 | `GetStateSettingsFolder` | `0x142EF0` | 191 | UnwindData |  |
| 805 | `GetStateVersion` | `0x142FC0` | 172 | UnwindData |  |
| 1165 | `OverrideRoamingDataModificationTimesInRange` | `0x143080` | 186 | UnwindData |  |
| 1359 | `PublishStateChangeNotification` | `0x143140` | 147 | UnwindData |  |
| 1504 | `RegisterStateLock` | `0x1431E0` | 172 | UnwindData |  |
| 1534 | `ResetState` | `0x1432A0` | 172 | UnwindData |  |
| 1677 | `SetRoamingLastObservedChangeTime` | `0x143360` | 192 | UnwindData |  |
| 1685 | `SetStateVersion` | `0x143430` | 159 | UnwindData |  |
| 1845 | `UnregisterStateChangeNotification` | `0x1434E0` | 172 | UnwindData |  |
| 1846 | `UnregisterStateLock` | `0x1435A0` | 172 | UnwindData |  |
| 2 | `MsixIsSystemPackageByPackageFullName` | `0x146CD0` | 580 | UnwindData |  |
| 3 | `PackageSidFromProductId` | `0x147210` | 751 | UnwindData |  |
| 33 | `AddPackageNameAliasesByPackageDependency` | `0x14E020` | 250 | UnwindData |  |
| 292 | `DeletePackageDependency` | `0x14E120` | 326 | UnwindData |  |
| 422 | `FindPackageDependency` | `0x14E270` | 137 | UnwindData |  |
| 546 | `GetCurrentPackageInfo_PackageNameAliases` | `0x14E300` | 204 | UnwindData |  |
| 635 | `GetIdForPackageDependencyContext` | `0x14E3E0` | 95 | UnwindData |  |
| 701 | `GetPackageDependencyInformation` | `0x14E450` | 251 | UnwindData |  |
| 710 | `GetPackageGraphRevisionId` | `0x14E560` | 48 | UnwindData |  |
| 715 | `GetPackageNameAliasesByPackageFullName` | `0x14E5A0` | 335 | UnwindData |  |
| 764 | `GetProcessesUsingPackageDependency` | `0x14E700` | 121 | UnwindData |  |
| 777 | `GetResolvedPackageFullNameForPackageDependency` | `0x14E780` | 95 | UnwindData |  |
| 778 | `GetResolvedPackageFullNameForPackageDependency2` | `0x14E7F0` | 95 | UnwindData |  |
| 1434 | `RefreshPackageInfo` | `0x14E860` | 874 | UnwindData |  |
| 1524 | `RemoveExtensionProgIds` | `0x14FBD0` | 3,625 | UnwindData |  |
| 57 | `AppPolicyGetCreateFileAccess` | `0x150F00` | 95 | UnwindData |  |
| 61 | `AppPolicyGetShowDeveloperDiagnostic` | `0x150F70` | 95 | UnwindData |  |
| 78 | `ApplicationUserModelIdFromProductId` | `0x150FE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1173 | `PackageFullNameFromProductId` | `0x150FE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1176 | `PackageIdFromProductId` | `0x150FE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1182 | `PackageRelativeApplicationIdFromProductId` | `0x150FE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1335 | `ProductIdFromPackageFamilyName` | `0x150FE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1170 | `PackageFamilyNameFromProductId` | `0x150FF0` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1177 | `PackageIsEffectiveSupportedUsersMultiple` | `0x151180` | 244 | UnwindData |  |
| 441 | `FormatApplicationUserModelIdA` | `0x151280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1167 | `PackageFamilyNameFromFullNameA` | `0x151290` | 130 | UnwindData |  |
| 1169 | `PackageFamilyNameFromIdA` | `0x151320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1172 | `PackageFullNameFromIdA` | `0x151330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1175 | `PackageIdFromFullNameA` | `0x151340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1179 | `PackageNameAndPublisherIdFromFamilyNameA` | `0x151360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1180 | `PackagePublisherAddUserIfNecessary` | `0x151370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1181 | `PackagePublisherIdFromPublisher` | `0x151380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1185 | `ParseApplicationUserModelIdA` | `0x151390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1891 | `VerifyApplicationUserModelId` | `0x1513A0` | 62 | UnwindData |  |
| 1892 | `VerifyApplicationUserModelIdA` | `0x1513F0` | 54 | UnwindData |  |
| 1894 | `VerifyPackageFamilyNameA` | `0x151430` | 62 | UnwindData |  |
| 1896 | `VerifyPackageFullNameA` | `0x151480` | 110 | UnwindData |  |
| 1897 | `VerifyPackageId` | `0x151500` | 110 | UnwindData |  |
| 1898 | `VerifyPackageIdA` | `0x151580` | 110 | UnwindData |  |
| 1900 | `VerifyPackageNameA` | `0x151600` | 88 | UnwindData |  |
| 1902 | `VerifyPackagePublisherA` | `0x151660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1903 | `VerifyPackageRelativeApplicationId` | `0x151670` | 58 | UnwindData |  |
| 1904 | `VerifyPackageRelativeApplicationIdA` | `0x1516B0` | 58 | UnwindData |  |
| 468 | `GetAppModelVersion` | `0x1516F0` | 281 | UnwindData |  |
| 979 | `InvalidateAppModelVersionCache` | `0x151810` | 1,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 550 | `GetCurrentPackageSecurityContext` | `0x151C40` | 108 | UnwindData |  |
| 555 | `GetCurrentTargetPlatformContext` | `0x151CC0` | 111 | UnwindData |  |
| 695 | `GetPackageApplicationContext` | `0x151D40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 699 | `GetPackageApplicationResourcesContext` | `0x151D60` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 700 | `GetPackageContext` | `0x151DB0` | 58 | UnwindData |  |
| 708 | `GetPackageGlobalizationContext` | `0x151DF0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 716 | `GetPackageOSMaxVersionTested` | `0x151E40` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 721 | `GetPackageProperty` | `0x151E80` | 808 | UnwindData |  |
| 722 | `GetPackagePropertyString` | `0x1521B0` | 93 | UnwindData |  |
| 723 | `GetPackageResourcesContext` | `0x152220` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 547 | `GetCurrentPackagePath` | `0x152290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1527 | `RemovePackageStatusForUser` | `0x1522B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1854 | `UpdatePackageStatusForUser` | `0x1522D0` | 196 | UnwindData |  |
| 1855 | `UpdatePackageStatusForUserSid` | `0x1523A0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 720 | `GetPackagePathOnVolume` | `0x1524E0` | 326 | UnwindData |  |
| 767 | `GetProtocolAumid` | `0x152630` | 33 | UnwindData |  |
| 768 | `GetProtocolProperty` | `0x152660` | 48 | UnwindData |  |
| 825 | `GetSystemMetadataPath` | `0x1526A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1360 | `PublisherFromPackageFullName` | `0x1526B0` | 612 | UnwindData |  |
| 66 | `AppXGetApplicationData` | `0x1545A0` | 491 | UnwindData |  |
| 67 | `AppXGetDevelopmentMode` | `0x1547A0` | 239 | UnwindData |  |
| 72 | `AppXLookupDisplayName` | `0x1548A0` | 130 | UnwindData |  |
| 73 | `AppXLookupMoniker` | `0x154930` | 130 | UnwindData |  |
| 64 | `AppXCheckPplSupport` | `0x158160` | 316 | UnwindData |  |
| 1510 | `ReleasePackagedDataForFile` | `0x15AB30` | 33 | UnwindData |  |
| 1011 | `IsSideloadingEnabled` | `0x15B220` | 80 | UnwindData |  |
| 1012 | `IsSideloadingPolicyApplied` | `0x15B280` | 57 | UnwindData |  |
| 1645 | `SetIsDeveloperModeEnabled` | `0x15B2C0` | 69 | UnwindData |  |
| 1646 | `SetIsSideloadingEnabled` | `0x15B310` | 69 | UnwindData |  |
| 1294 | `PcwClearCounterSetSecurity` | `0x15B610` | 88 | UnwindData |  |
| 1301 | `PcwIsNotifierAlive` | `0x15B670` | 72 | UnwindData |  |
| 1302 | `PcwQueryCounterSetSecurity` | `0x15B6C0` | 83 | UnwindData |  |
| 1308 | `PcwSetCounterSetSecurity` | `0x15B720` | 86 | UnwindData |  |
| 1319 | `PerfQueryInstance` | `0x15B7F0` | 207 | UnwindData |  |
| 25 | `AddConsoleAliasA` | `0x15C260` | 87 | UnwindData |  |
| 26 | `AddConsoleAliasW` | `0x15C400` | 94 | UnwindData |  |
| 389 | `ExpungeConsoleCommandHistoryA` | `0x15C470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 496 | `GetConsoleAliasA` | `0x15C480` | 56 | UnwindData |  |
| 497 | `GetConsoleAliasExesA` | `0x15C4C0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 498 | `GetConsoleAliasExesLengthA` | `0x15C590` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 499 | `GetConsoleAliasExesLengthW` | `0x15C610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 500 | `GetConsoleAliasExesW` | `0x15C620` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 501 | `GetConsoleAliasW` | `0x15C760` | 63 | UnwindData |  |
| 502 | `GetConsoleAliasesA` | `0x15C7B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 503 | `GetConsoleAliasesLengthA` | `0x15C7C0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 504 | `GetConsoleAliasesLengthW` | `0x15C8A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 505 | `GetConsoleAliasesW` | `0x15C8B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 507 | `GetConsoleCommandHistoryA` | `0x15C8C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 508 | `GetConsoleCommandHistoryLengthA` | `0x15C8D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 509 | `GetConsoleCommandHistoryLengthW` | `0x15C8E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 510 | `GetConsoleCommandHistoryW` | `0x15C8F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 518 | `GetConsoleOriginalTitleA` | `0x15C900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 519 | `GetConsoleOriginalTitleW` | `0x15C920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 525 | `GetConsoleTitleA` | `0x15C940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1607 | `SetConsoleNumberOfCommandsA` | `0x15C960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1613 | `SetConsoleTitleA` | `0x15C970` | 58 | UnwindData |  |
| 43 | `AllocConsole` | `0x15C9B0` | 85 | UnwindData |  |
| 444 | `FreeConsole` | `0x15CA10` | 109 | UnwindData |  |
| 158 | `ClosePseudoConsole` | `0x15CAC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1536 | `ResizePseudoConsole` | `0x15CAD0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 396 | `FillConsoleOutputAttribute` | `0x15CC00` | 36 | UnwindData |  |
| 398 | `FillConsoleOutputCharacterW` | `0x15CC30` | 36 | UnwindData |  |
| 1414 | `ReadConsoleInputA` | `0x15CC60` | 26 | UnwindData |  |
| 1415 | `ReadConsoleInputExA` | `0x15CC80` | 30 | UnwindData |  |
| 1418 | `ReadConsoleOutputA` | `0x15CCB0` | 30 | UnwindData |  |
| 1419 | `ReadConsoleOutputAttribute` | `0x15CCE0` | 44 | UnwindData |  |
| 1976 | `WriteConsoleInputA` | `0x15CD20` | 20 | UnwindData |  |
| 1977 | `WriteConsoleInputW` | `0x15CE20` | 20 | UnwindData |  |
| 1978 | `WriteConsoleOutputA` | `0x15CE40` | 30 | UnwindData |  |
| 1979 | `WriteConsoleOutputAttribute` | `0x15CE70` | 44 | UnwindData |  |
| 1981 | `WriteConsoleOutputCharacterW` | `0x15CEB0` | 41 | UnwindData |  |
| 1648 | `SetLastConsoleEventActive` | `0x15CEE0` | 54 | UnwindData |  |
| 433 | `FlushConsoleInputBuffer` | `0x15CF20` | 101 | UnwindData |  |
| 455 | `GenerateConsoleCtrlEvent` | `0x15CF90` | 164 | UnwindData |  |
| 513 | `GetConsoleFontSize` | `0x15D040` | 123 | UnwindData |  |
| 514 | `GetConsoleHistoryInfo` | `0x15D0D0` | 136 | UnwindData |  |
| 532 | `GetCurrentConsoleFont` | `0x15D160` | 130 | UnwindData |  |
| 689 | `GetNumberOfConsoleMouseButtons` | `0x15D1F0` | 109 | UnwindData |  |
| 1578 | `ScrollConsoleScreenBufferA` | `0x15D270` | 30 | UnwindData |  |
| 1597 | `SetConsoleActiveScreenBuffer` | `0x15D2A0` | 101 | UnwindData |  |
| 1602 | `SetConsoleDisplayMode` | `0x15D310` | 145 | UnwindData |  |
| 1603 | `SetConsoleHistoryInfo` | `0x15D3B0` | 136 | UnwindData |  |
| 1610 | `SetConsoleScreenBufferInfoEx` | `0x15D440` | 264 | UnwindData |  |
| 1611 | `SetConsoleScreenBufferSize` | `0x15D550` | 122 | UnwindData |  |
| 1615 | `SetConsoleWindowInfo` | `0x15D5D0` | 145 | UnwindData |  |
| 1413 | `ReadConsoleA` | `0x15D670` | 76 | UnwindData |  |
| 1815 | `TestRecoverResults` | `0x173E10` | 37,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1995 | `__FC_Query_Config` | `0x17CF50` | 75 | UnwindData |  |
| 1997 | `__FC_Report` | `0x17CFB0` | 179 | UnwindData |  |
| 1998 | `__FC_Subscribe` | `0x17D070` | 204 | UnwindData |  |
| 1999 | `__FC_Unsubscribe` | `0x17D150` | 40 | UnwindData |  |
| 7 | `AccessCheckByTypeAndAuditAlarmW` | `0x17D240` | 333 | UnwindData |  |
| 8 | `AccessCheckByTypeResultList` | `0x17D3A0` | 177 | UnwindData |  |
| 9 | `AccessCheckByTypeResultListAndAuditAlarmByHandleW` | `0x17D460` | 369 | UnwindData |  |
| 10 | `AccessCheckByTypeResultListAndAuditAlarmW` | `0x17D5E0` | 340 | UnwindData |  |
| 17 | `AddAccessAllowedObjectAce` | `0x17D740` | 101 | UnwindData |  |
| 19 | `AddAccessDeniedAceEx` | `0x17D7B0` | 78 | UnwindData |  |
| 20 | `AddAccessDeniedObjectAce` | `0x17D810` | 101 | UnwindData |  |
| 22 | `AddAuditAccessAce` | `0x17D880` | 58 | UnwindData |  |
| 23 | `AddAuditAccessAceEx` | `0x17D8C0` | 97 | UnwindData |  |
| 24 | `AddAuditAccessObjectAce` | `0x17D930` | 129 | UnwindData |  |
| 36 | `AddResourceAttributeAce` | `0x17D9C0` | 75 | UnwindData |  |
| 38 | `AddScopedPolicyIDAce` | `0x17DA20` | 52 | UnwindData |  |
| 80 | `AreAnyAccessesGranted` | `0x17DA60` | 25 | UnwindData |  |
| 187 | `ConvertToAutoInheritPrivateObjectSecurity` | `0x17DA80` | 60 | UnwindData |  |
| 271 | `CveEventWrite` | `0x17DAD0` | 271 | UnwindData |  |
| 411 | `FindFirstFreeAce` | `0x17DBF0` | 52 | UnwindData |  |
| 741 | `GetPrivateObjectSecurity` | `0x17DC30` | 52 | UnwindData |  |
| 960 | `InstallELAMCertificateInfo` | `0x17DC70` | 68 | UnwindData |  |
| 1025 | `IsValidRelativeSecurityDescriptor` | `0x17DCC0` | 45 | UnwindData |  |
| 1134 | `ObjectDeleteAuditAlarmW` | `0x17DD00` | 99 | UnwindData |  |
| 1136 | `ObjectPrivilegeAuditAlarmW` | `0x17DD70` | 132 | UnwindData |  |
| 1333 | `PrivilegedServiceAuditAlarmW` | `0x17DE00` | 154 | UnwindData |  |
| 1582 | `SetAclInformation` | `0x17DEA0` | 42 | UnwindData |  |
| 1658 | `SetPrivateObjectSecurity` | `0x17DED0` | 52 | UnwindData |  |
| 1659 | `SetPrivateObjectSecurityEx` | `0x17DF10` | 62 | UnwindData |  |
| 349 | `EnumResourceLanguagesExA` | `0x17E080` | 196 | UnwindData |  |
| 351 | `EnumResourceNamesA` | `0x17E150` | 30 | UnwindData |  |
| 352 | `EnumResourceNamesExA` | `0x17E180` | 137 | UnwindData |  |
| 355 | `EnumResourceTypesExA` | `0x17E210` | 33 | UnwindData |  |
| 1538 | `ResolveDelayLoadsFromDll` | `0x17E320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `AllocateUserPhysicalPages` | `0x17E340` | 42 | UnwindData |  |
| 48 | `AllocateUserPhysicalPages2` | `0x17E370` | 109 | UnwindData |  |
| 49 | `AllocateUserPhysicalPagesNuma` | `0x17E3F0` | 240 | UnwindData |  |
| 454 | `FreeUserPhysicalPages` | `0x17E510` | 42 | UnwindData |  |
| 659 | `GetMemoryErrorHandlingCapabilities` | `0x17E540` | 137 | UnwindData |  |
| 660 | `GetMemoryNumaClosestInitiatorNode` | `0x17E5D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 661 | `GetMemoryNumaPerformanceInformation` | `0x17E5D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 821 | `GetSystemFileCacheSize` | `0x17E5E0` | 172 | UnwindData |  |
| 1103 | `MapUserPhysicalPages` | `0x17E6A0` | 42 | UnwindData |  |
| 1137 | `OfferVirtualMemory` | `0x17E6D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1139 | `OpenDedicatedMemoryPartition` | `0x17E6F0` | 94 | UnwindData |  |
| 1379 | `QueryPartitionInformation` | `0x17E760` | 82 | UnwindData |  |
| 1393 | `QueryVirtualMemoryInformation` | `0x17E7C0` | 80 | UnwindData |  |
| 1432 | `ReclaimVirtualMemory` | `0x17E820` | 339 | UnwindData |  |
| 1501 | `RegisterBadMemoryNotification` | `0x17E980` | 82 | UnwindData |  |
| 1672 | `SetProcessValidCallTargetsForMappedView` | `0x17E9E0` | 45 | UnwindData |  |
| 1688 | `SetSystemFileCacheSize` | `0x17EA20` | 212 | UnwindData |  |
| 1843 | `UnregisterBadMemoryNotification` | `0x17EB00` | 42 | UnwindData |  |
| 1908 | `VirtualAlloc2FromApp` | `0x17EB30` | 54 | UnwindData |  |
| 1917 | `VirtualProtectFromApp` | `0x17EB70` | 139 | UnwindData |  |
| 1921 | `VirtualUnlockEx` | `0x17EC10` | 67 | UnwindData |  |
| 81 | `AreExternalFeatureDependenciesEnabled` | `0x17EC60` | 200 | UnwindData |  |
| 1630 | `SetFileApisToANSI` | `0x185E30` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1631 | `SetFileApisToOEM` | `0x185E70` | 1,664 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `Beep` | `0x1864F0` | 278 | UnwindData |  |
| 285 | `DeleteEnclave` | `0x186610` | 42 | UnwindData |  |
| 1070 | `LoadEnclaveImageA` | `0x186640` | 72 | UnwindData |  |
| 1806 | `TerminateEnclave` | `0x186690` | 58 | UnwindData |  |
| 298 | `DeleteSynchronizationBarrier` | `0x1866D0` | 27 | UnwindData |  |
| 334 | `EnterSynchronizationBarrier` | `0x186700` | 102 | UnwindData |  |
| 959 | `InitializeSynchronizationBarrier` | `0x186770` | 60 | UnwindData |  |
| 273 | `DebugActiveProcess` | `0x186850` | 123 | UnwindData |  |
| 274 | `DebugActiveProcessStop` | `0x1868E0` | 108 | UnwindData |  |
| 483 | `GetCommConfig` | `0x186A70` | 603 | UnwindData |  |
| 484 | `GetCommMask` | `0x186CE0` | 225 | UnwindData |  |
| 486 | `GetCommPorts` | `0x186DD0` | 710 | UnwindData |  |
| 489 | `GetCommTimeouts` | `0x1870A0` | 311 | UnwindData |  |
| 1138 | `OpenCommPort` | `0x1871E0` | 294 | UnwindData |  |
| 1587 | `SetCommBreak` | `0x187310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1588 | `SetCommConfig` | `0x187320` | 251 | UnwindData |  |
| 1590 | `SetCommState` | `0x187430` | 1,087 | UnwindData |  |
| 1724 | `SetupComm` | `0x187880` | 289 | UnwindData |  |
| 1827 | `TransmitCommChar` | `0x1879B0` | 221 | UnwindData |  |
| 181 | `ConvertAuxiliaryCounterToPerformanceCounter` | `0x187AA0` | 94 | UnwindData |  |
| 184 | `ConvertPerformanceCounterToAuxiliaryCounter` | `0x187B10` | 94 | UnwindData |  |
| 824 | `GetSystemLeapSecondInformation` | `0x187B80` | 112 | UnwindData |  |
| 832 | `GetSystemTimeAdjustmentPrecise` | `0x187C00` | 139 | UnwindData |  |
| 1366 | `QueryAuxiliaryCounterFrequency` | `0x187CA0` | 62 | UnwindData |  |
| 1586 | `SetClientTimeZoneInformation` | `0x187CF0` | 369 | UnwindData |  |
| 1621 | `SetDynamicTimeZoneInformation` | `0x187E70` | 202 | UnwindData |  |
| 1650 | `SetLocalTime` | `0x187F40` | 255 | UnwindData |  |
| 1689 | `SetSystemTime` | `0x188050` | 262 | UnwindData |  |
| 1690 | `SetSystemTimeAdjustment` | `0x188160` | 69 | UnwindData |  |
| 1691 | `SetSystemTimeAdjustmentPrecise` | `0x1881B0` | 102 | UnwindData |  |
| 1716 | `SetTimeZoneInformation` | `0x188220` | 435 | UnwindData |  |
| 1835 | `TzSpecificLocalTimeToSystemTimeEx` | `0x1883E0` | 622 | UnwindData |  |
| 247 | `CreateRemoteThread` | `0x188660` | 60 | UnwindData |  |
| 258 | `CreateThread` | `0x1886B0` | 65 | UnwindData |  |
| 862 | `GetThreadSelectedCpuSetMasks` | `0x188700` | 209 | UnwindData |  |
| 863 | `GetThreadSelectedCpuSets` | `0x1887E0` | 211 | UnwindData |  |
| 1704 | `SetThreadSelectedCpuSetMasks` | `0x1888C0` | 210 | UnwindData |  |
| 1705 | `SetThreadSelectedCpuSets` | `0x1889A0` | 208 | UnwindData |  |
| 1972 | `Wow64SetThreadContext` | `0x188A80` | 42 | UnwindData |  |
| 198 | `CreateAppSiloToken` | `0x188AB0` | 493 | UnwindData |  |
| 201 | `CreateDirectory2A` | `0x188CB0` | 121 | UnwindData |  |
| 202 | `CreateDirectory2W` | `0x188D30` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1518 | `RemoveDirectory2A` | `0x188F70` | 73 | UnwindData |  |
| 1519 | `RemoveDirectory2W` | `0x188FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 216 | `CreateFile3` | `0x188FD0` | 33 | UnwindData |  |
| 219 | `CreateFileMapping2` | `0x189000` | 421 | UnwindData |  |
| 1110 | `MapViewOfFileNuma2` | `0x1891B0` | 185 | UnwindData |  |
| 224 | `CreateHardLinkA` | `0x189270` | 156 | UnwindData |  |
| 1636 | `SetFileIoOverlappedRange` | `0x189320` | 114 | UnwindData |  |
| 392 | `FatalAppExitA` | `0x189A60` | 137 | UnwindData |  |
| 393 | `FatalAppExitW` | `0x189AF0` | 139 | UnwindData |  |
| 744 | `GetProcessDefaultCpuSetMasks` | `0x189F80` | 209 | UnwindData |  |
| 745 | `GetProcessDefaultCpuSets` | `0x18A060` | 211 | UnwindData |  |
| 759 | `GetProcessShutdownParameters` | `0x18A140` | 152 | UnwindData |  |
| 780 | `GetRuntimeAttestationReport` | `0x18A1E0` | 258 | UnwindData |  |
| 814 | `GetSystemCpuSetInformation` | `0x18A2F0` | 105 | UnwindData |  |
| 1008 | `IsProcessCritical` | `0x18A360` | 88 | UnwindData |  |
| 1119 | `NeedCurrentDirectoryForExePathA` | `0x18A3C0` | 46 | UnwindData |  |
| 1382 | `QueryProcessAffinityUpdateMode` | `0x18A540` | 87 | UnwindData |  |
| 1661 | `SetProcessDefaultCpuSetMasks` | `0x18A5A0` | 210 | UnwindData |  |
| 1662 | `SetProcessDefaultCpuSets` | `0x18A680` | 208 | UnwindData |  |
| 1663 | `SetProcessDynamicEHContinuationTargets` | `0x18A760` | 74 | UnwindData |  |
| 1664 | `SetProcessDynamicEnforcedCetCompatibleRanges` | `0x18A7B0` | 74 | UnwindData |  |
| 287 | `DeleteFile2A` | `0x18AAC0` | 73 | UnwindData |  |
| 288 | `DeleteFile2W` | `0x18AB10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 311 | `DnsHostnameToComputerNameExW` | `0x18AB20` | 263 | UnwindData |  |
| 1592 | `SetComputerNameA` | `0x18AC90` | 161 | UnwindData |  |
| 1593 | `SetComputerNameEx2W` | `0x18AD40` | 276 | UnwindData |  |
| 1594 | `SetComputerNameExA` | `0x18AE60` | 123 | UnwindData |  |
| 1595 | `SetComputerNameExW` | `0x18AEF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1596 | `SetComputerNameW` | `0x18AF00` | 206 | UnwindData |  |
| 403 | `FindFirstChangeNotificationA` | `0x18B040` | 96 | UnwindData |  |
| 562 | `GetDeveloperDriveEnablementState` | `0x18B170` | 159 | UnwindData |  |
| 571 | `GetDiskSpaceInformationA` | `0x18B600` | 108 | UnwindData |  |
| 572 | `GetDiskSpaceInformationW` | `0x18B680` | 450 | UnwindData |  |
| 573 | `GetDiskSpaceInformationWCOS` | `0x18B850` | 590 | UnwindData |  |
| 845 | `GetTempPath2A` | `0x18BAB0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 683 | `GetNumaNodeProcessorMask2` | `0x18BB70` | 436 | UnwindData |  |
| 685 | `GetNumaProximityNodeEx` | `0x18BD30` | 88 | UnwindData |  |
| 749 | `GetProcessHeaps` | `0x18BEB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 929 | `HeapSummary` | `0x18BED0` | 200 | UnwindData |  |
| 916 | `GuardCheckLongJumpTarget` | `0x18BFA0` | 100 | UnwindData |  |
| 1373 | `QueryIdleProcessorCycleTimeEx` | `0x18C010` | 98 | UnwindData |  |
| 1409 | `RaiseCustomSystemEventTrigger` | `0x18C080` | 26 | UnwindData |  |
| 1808 | `TerminateProcessOnMemoryExhaustion` | `0x18C0F0` | 490 | UnwindData |  |
| 1820 | `TlsGetValue` | `0x192930` | 107 | UnwindData |  |
| 2004 | `__wargv` | `0x399180` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2000 | `__argc` | `0x399188` | 0 | Indeterminate |  |
