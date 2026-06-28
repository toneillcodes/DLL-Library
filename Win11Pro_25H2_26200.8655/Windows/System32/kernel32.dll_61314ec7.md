# Binary Specification: kernel32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\kernel32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `61314ec71059dc533b45f01cb8bf487c648eaa783e83d924245da37470c8fde6`
* **Total Exported Functions:** 1693

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `AcquireSRWLockExclusive` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlAcquireSRWLockExclusive` |
| 2 | `AcquireSRWLockShared` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlAcquireSRWLockShared` |
| 10 | `AddDllDirectory` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-libraryloader-l1-1-0.AddDllDirectory` |
| 20 | `AddVectoredContinueHandler` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlAddVectoredContinueHandler` |
| 21 | `AddVectoredExceptionHandler` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlAddVectoredExceptionHandler` |
| 27 | `AppPolicyGetClrCompat` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.AppPolicyGetClrCompat` |
| 28 | `AppPolicyGetCreateFileAccess` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.AppPolicyGetCreateFileAccess` |
| 29 | `AppPolicyGetLifecycleManagement` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.AppPolicyGetLifecycleManagement` |
| 30 | `AppPolicyGetMediaFoundationCodecLoading` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.AppPolicyGetMediaFoundationCodecLoading` |
| 31 | `AppPolicyGetProcessTerminationMethod` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.AppPolicyGetProcessTerminationMethod` |
| 32 | `AppPolicyGetShowDeveloperDiagnostic` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.AppPolicyGetShowDeveloperDiagnostic` |
| 33 | `AppPolicyGetThreadInitializationType` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.AppPolicyGetThreadInitializationType` |
| 34 | `AppPolicyGetWindowingModel` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.AppPolicyGetWindowingModel` |
| 35 | `AppXGetOSMaxVersionTested` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.AppXGetOSMaxVersionTested` |
| 126 | `BuildIoRingCancelRequest` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-ioring-l1-1-0.BuildIoRingCancelRequest` |
| 127 | `BuildIoRingFlushFile` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-ioring-l1-1-1.BuildIoRingFlushFile` |
| 128 | `BuildIoRingReadFile` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-ioring-l1-1-0.BuildIoRingReadFile` |
| 129 | `BuildIoRingReadFileScatter` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-ioring-l1-1-2.BuildIoRingReadFileScatter` |
| 130 | `BuildIoRingRegisterBuffers` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-ioring-l1-1-0.BuildIoRingRegisterBuffers` |
| 131 | `BuildIoRingRegisterFileHandles` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-ioring-l1-1-0.BuildIoRingRegisterFileHandles` |
| 132 | `BuildIoRingWriteFile` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-ioring-l1-1-1.BuildIoRingWriteFile` |
| 133 | `BuildIoRingWriteFileGather` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-ioring-l1-1-2.BuildIoRingWriteFileGather` |
| 141 | `CancelThreadpoolIo` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpCancelAsyncIoOperation` |
| 144 | `CeipIsOptedIn` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.CeipIsOptedIn` |
| 160 | `CloseIoRing` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-ioring-l1-1-0.CloseIoRing` |
| 161 | `ClosePackageInfo` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.ClosePackageInfo` |
| 165 | `CloseState` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.CloseState` |
| 166 | `CloseThreadpool` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpReleasePool` |
| 167 | `CloseThreadpoolCleanupGroup` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpReleaseCleanupGroup` |
| 168 | `CloseThreadpoolCleanupGroupMembers` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpReleaseCleanupGroupMembers` |
| 169 | `CloseThreadpoolIo` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpReleaseIoCompletion` |
| 170 | `CloseThreadpoolTimer` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpReleaseTimer` |
| 171 | `CloseThreadpoolWait` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpReleaseWait` |
| 172 | `CloseThreadpoolWork` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpReleaseWork` |
| 215 | `CreateEnclave` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-enclave-l1-1-0.CreateEnclave` |
| 226 | `CreateFileMappingFromApp` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-memory-l1-1-1.CreateFileMappingFromApp` |
| 238 | `CreateIoRing` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-ioring-l1-1-0.CreateIoRing` |
| 263 | `CreateRemoteThreadEx` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-0.CreateRemoteThreadEx` |
| 289 | `CtrlRoutine` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.CtrlRoutine` |
| 298 | `DecodePointer` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlDecodePointer` |
| 299 | `DecodeSystemPointer` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlDecodeSystemPointer` |
| 305 | `DeleteCriticalSection` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlDeleteCriticalSection` |
| 313 | `DeleteProcThreadAttributeList` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-0.DeleteProcThreadAttributeList` |
| 326 | `DisassociateCurrentThreadFromCallback` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpDisassociateCallback` |
| 327 | `DiscardVirtualMemory` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-memory-l1-1-2.DiscardVirtualMemory` |
| 341 | `EncodePointer` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlEncodePointer` |
| 342 | `EncodeSystemPointer` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlEncodeSystemPointer` |
| 345 | `EnterCriticalSection` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlEnterCriticalSection` |
| 393 | `ExitThread` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlExitUserThread` |
| 428 | `FindFirstStreamW` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-file-l1-2-2.FindFirstStreamW` |
| 439 | `FindNextStreamW` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-file-l1-2-2.FindNextStreamW` |
| 444 | `FindPackagesByPackageFamily` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.FindPackagesByPackageFamily` |
| 455 | `FlsGetValue2` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.FlsGetValue2` |
| 460 | `FlushProcessWriteBuffers` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.NtFlushProcessWriteBuffers` |
| 464 | `FormatApplicationUserModelId` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.FormatApplicationUserModelId` |
| 472 | `FreeLibraryWhenCallbackReturns` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpCallbackUnloadDllOnCompletion` |
| 486 | `GetApplicationUserModelId` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetApplicationUserModelId` |
| 546 | `GetConsoleInputExeNameA` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetConsoleInputExeNameA` |
| 547 | `GetConsoleInputExeNameW` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetConsoleInputExeNameW` |
| 568 | `GetCurrentApplicationUserModelId` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetCurrentApplicationUserModelId` |
| 573 | `GetCurrentPackageFamilyName` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetCurrentPackageFamilyName` |
| 574 | `GetCurrentPackageFullName` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetCurrentPackageFullName` |
| 575 | `GetCurrentPackageId` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetCurrentPackageId` |
| 576 | `GetCurrentPackageInfo` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetCurrentPackageInfo` |
| 577 | `GetCurrentPackagePath` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetCurrentPackagePath` |
| 581 | `GetCurrentProcessorNumber` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlGetCurrentProcessorNumber` |
| 582 | `GetCurrentProcessorNumberEx` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlGetCurrentProcessorNumberEx` |
| 585 | `GetCurrentThreadStackLimits` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-0.GetCurrentThreadStackLimits` |
| 599 | `GetDiskSpaceInformationA` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-file-l1-2-3.GetDiskSpaceInformationA` |
| 600 | `GetDiskSpaceInformationW` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-file-l1-2-3.GetDiskSpaceInformationW` |
| 652 | `GetIoRingInfo` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-ioring-l1-1-0.GetIoRingInfo` |
| 664 | `GetLogicalProcessorInformationEx` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-sysinfo-l1-1-0.GetLogicalProcessorInformationEx` |
| 669 | `GetMachineTypeAttributes` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-7.GetMachineTypeAttributes` |
| 689 | `GetNamedPipeInfo` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-namedpipe-l1-2-1.GetNamedPipeInfo` |
| 700 | `GetNumaNodeProcessorMask2` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-systemtopology-l1-1-2.GetNumaNodeProcessorMask2` |
| 714 | `GetOverlappedResultEx` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-io-l1-1-1.GetOverlappedResultEx` |
| 715 | `GetPackageApplicationIds` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetPackageApplicationIds` |
| 716 | `GetPackageFamilyName` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetPackageFamilyName` |
| 717 | `GetPackageFullName` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetPackageFullName` |
| 718 | `GetPackageId` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetPackageId` |
| 719 | `GetPackageInfo` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetPackageInfo` |
| 720 | `GetPackagePath` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetPackagePath` |
| 721 | `GetPackagePathByFullName` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetPackagePathByFullName` |
| 722 | `GetPackagesByPackageFamily` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetPackagesByPackageFamily` |
| 738 | `GetProcessDefaultCpuSetMasks` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-6.GetProcessDefaultCpuSetMasks` |
| 739 | `GetProcessDefaultCpuSets` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-3.GetProcessDefaultCpuSets` |
| 748 | `GetProcessMitigationPolicy` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-1.GetProcessMitigationPolicy` |
| 757 | `GetProcessorSystemCycleTime` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-sysinfo-l1-2-2.GetProcessorSystemCycleTime` |
| 769 | `GetStagedPackagePathByFullName` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetStagedPackagePathByFullName` |
| 772 | `GetStateFolder` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetStateFolder` |
| 779 | `GetSystemAppDataKey` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetSystemAppDataKey` |
| 780 | `GetSystemCpuSetInformation` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-3.GetSystemCpuSetInformation` |
| 813 | `GetThreadDescription` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-3.GetThreadDescription` |
| 825 | `GetThreadSelectedCpuSetMasks` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-6.GetThreadSelectedCpuSetMasks` |
| 826 | `GetThreadSelectedCpuSets` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-3.GetThreadSelectedCpuSets` |
| 894 | `HeapAlloc` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlAllocateHeap` |
| 901 | `HeapReAlloc` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlReAllocateHeap` |
| 903 | `HeapSize` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlSizeHeap` |
| 912 | `InitOnceBeginInitialize` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-synch-l1-2-0.InitOnceBeginInitialize` |
| 913 | `InitOnceComplete` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-synch-l1-2-0.InitOnceComplete` |
| 914 | `InitOnceExecuteOnce` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-synch-l1-2-0.InitOnceExecuteOnce` |
| 915 | `InitOnceInitialize` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlRunOnceInitialize` |
| 916 | `InitializeConditionVariable` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlInitializeConditionVariable` |
| 919 | `InitializeCriticalSection` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlInitializeCriticalSection` |
| 922 | `InitializeEnclave` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-enclave-l1-1-0.InitializeEnclave` |
| 923 | `InitializeProcThreadAttributeList` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-0.InitializeProcThreadAttributeList` |
| 924 | `InitializeSListHead` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlInitializeSListHead` |
| 925 | `InitializeSRWLock` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlInitializeSRWLock` |
| 927 | `InstallELAMCertificateInfo` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-sysinfo-l1-2-1.InstallELAMCertificateInfo` |
| 928 | `InterlockedFlushSList` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlInterlockedFlushSList` |
| 929 | `InterlockedPopEntrySList` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlInterlockedPopEntrySList` |
| 930 | `InterlockedPushEntrySList` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlInterlockedPushEntrySList` |
| 931 | `InterlockedPushListSList` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlInterlockedPushListSList` |
| 932 | `InterlockedPushListSListEx` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlInterlockedPushListSListEx` |
| 947 | `IsEnclaveTypeSupported` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-enclave-l1-1-0.IsEnclaveTypeSupported` |
| 948 | `IsIoRingOpSupported` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-ioring-l1-1-0.IsIoRingOpSupported` |
| 952 | `IsProcessCritical` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-2.IsProcessCritical` |
| 957 | `IsThreadpoolTimerSet` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpIsTimerSet` |
| 958 | `IsUserCetAvailableInEnvironment` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-sysinfo-l1-2-6.IsUserCetAvailableInEnvironment` |
| 965 | `IsWow64GuestMachineSupported` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-wow64-l1-1-2.IsWow64GuestMachineSupported` |
| 967 | `IsWow64Process2` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-wow64-l1-1-1.IsWow64Process2` |
| 1010 | `LeaveCriticalSection` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlLeaveCriticalSection` |
| 1011 | `LeaveCriticalSectionWhenCallbackReturns` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpCallbackLeaveCriticalSectionOnCompletion` |
| 1013 | `LoadEnclaveData` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-enclave-l1-1-0.LoadEnclaveData` |
| 1026 | `LocalFileTimeToLocalSystemTime` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-timezone-l1-1-1.LocalFileTimeToLocalSystemTime` |
| 1034 | `LocalSystemTimeToLocalFileTime` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-timezone-l1-1-1.LocalSystemTimeToLocalFileTime` |
| 1041 | `LogUnexpectedCodepath` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlLogUnexpectedCodepath` |
| 1047 | `MapViewOfFileFromApp` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-memory-l1-1-1.MapViewOfFileFromApp` |
| 1073 | `OfferVirtualMemory` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-memory-l1-1-2.OfferVirtualMemory` |
| 1086 | `OpenPackageInfoByFullName` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.OpenPackageInfoByFullName` |
| 1090 | `OpenProcessToken` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-0.OpenProcessToken` |
| 1094 | `OpenState` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.OpenState` |
| 1095 | `OpenStateExplicit` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.OpenStateExplicit` |
| 1097 | `OpenThreadToken` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-0.OpenThreadToken` |
| 1102 | `PackageFamilyNameFromFullName` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.PackageFamilyNameFromFullName` |
| 1103 | `PackageFamilyNameFromId` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.PackageFamilyNameFromId` |
| 1104 | `PackageFullNameFromId` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.PackageFullNameFromId` |
| 1105 | `PackageIdFromFullName` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.PackageIdFromFullName` |
| 1106 | `PackageNameAndPublisherIdFromFamilyName` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.PackageNameAndPublisherIdFromFamilyName` |
| 1107 | `ParseApplicationUserModelId` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.ParseApplicationUserModelId` |
| 1111 | `PopIoRingCompletion` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-ioring-l1-1-0.PopIoRingCompletion` |
| 1116 | `PrefetchVirtualMemory` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-memory-l1-1-1.PrefetchVirtualMemory` |
| 1144 | `QueryDepthSList` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlQueryDepthSList` |
| 1153 | `QueryIoRingCapabilities` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-ioring-l1-1-0.QueryIoRingCapabilities` |
| 1159 | `QueryProtectedPolicy` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-2.QueryProtectedPolicy` |
| 1166 | `QueueUserAPC2` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-5.QueueUserAPC2` |
| 1179 | `RaiseFailFastException` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.RaiseFailFastException` |
| 1184 | `ReadConsoleInputExA` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.ReadConsoleInputExA` |
| 1185 | `ReadConsoleInputExW` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.ReadConsoleInputExW` |
| 1200 | `ReclaimVirtualMemory` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-memory-l1-1-2.ReclaimVirtualMemory` |
| 1257 | `ReleaseMutexWhenCallbackReturns` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpCallbackReleaseMutexOnCompletion` |
| 1260 | `ReleaseSRWLockExclusive` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlReleaseSRWLockExclusive` |
| 1261 | `ReleaseSRWLockShared` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlReleaseSRWLockShared` |
| 1263 | `ReleaseSemaphoreWhenCallbackReturns` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpCallbackReleaseSemaphoreOnCompletion` |
| 1270 | `RemoveDllDirectory` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-libraryloader-l1-1-0.RemoveDllDirectory` |
| 1274 | `RemoveVectoredContinueHandler` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlRemoveVectoredContinueHandler` |
| 1275 | `RemoveVectoredExceptionHandler` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlRemoveVectoredExceptionHandler` |
| 1285 | `ResolveDelayLoadedAPI` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.LdrResolveDelayLoadedAPI` |
| 1286 | `ResolveDelayLoadsFromDll` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.LdrResolveDelayLoadsFromDll` |
| 1288 | `RestoreLastError` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlRestoreLastWin32Error` |
| 1292 | `RtlCaptureStackBackTrace` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlCaptureStackBackTrace` |
| 1298 | `RtlIsEcCode` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlIsEcCode` |
| 1308 | `RtlZeroMemory` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlZeroMemory` |
| 1339 | `SetConsoleInputExeNameA` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.SetConsoleInputExeNameA` |
| 1340 | `SetConsoleInputExeNameW` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.SetConsoleInputExeNameW` |
| 1358 | `SetCriticalSectionSpinCount` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlSetCriticalSectionSpinCount` |
| 1364 | `SetDefaultDllDirectories` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-libraryloader-l1-1-0.SetDefaultDllDirectories` |
| 1375 | `SetEventWhenCallbackReturns` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpCallbackSetEventOnCompletion` |
| 1400 | `SetIoRingCompletionEvent` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-ioring-l1-1-0.SetIoRingCompletionEvent` |
| 1401 | `SetLastConsoleEventActive` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.SetLastConsoleEventActive` |
| 1416 | `SetProcessDefaultCpuSetMasks` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-6.SetProcessDefaultCpuSetMasks` |
| 1417 | `SetProcessDefaultCpuSets` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-3.SetProcessDefaultCpuSets` |
| 1418 | `SetProcessDynamicEHContinuationTargets` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-4.SetProcessDynamicEHContinuationTargets` |
| 1419 | `SetProcessDynamicEnforcedCetCompatibleRanges` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-6.SetProcessDynamicEnforcedCetCompatibleRanges` |
| 1421 | `SetProcessMitigationPolicy` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-1.SetProcessMitigationPolicy` |
| 1427 | `SetProtectedPolicy` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-2.SetProtectedPolicy` |
| 1440 | `SetThreadDescription` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-3.SetThreadDescription` |
| 1451 | `SetThreadSelectedCpuSetMasks` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-6.SetThreadSelectedCpuSetMasks` |
| 1452 | `SetThreadSelectedCpuSets` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-3.SetThreadSelectedCpuSets` |
| 1454 | `SetThreadToken` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-0.SetThreadToken` |
| 1457 | `SetThreadpoolThreadMaximum` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpSetPoolMaxThreads` |
| 1459 | `SetThreadpoolTimer` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpSetTimer` |
| 1460 | `SetThreadpoolTimerEx` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpSetTimerEx` |
| 1461 | `SetThreadpoolWait` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpSetWait` |
| 1462 | `SetThreadpoolWaitEx` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpSetWaitEx` |
| 1476 | `SetWaitableTimerEx` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-synch-l1-1-0.SetWaitableTimerEx` |
| 1483 | `SleepConditionVariableCS` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-synch-l1-2-0.SleepConditionVariableCS` |
| 1484 | `SleepConditionVariableSRW` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-synch-l1-2-0.SleepConditionVariableSRW` |
| 1488 | `StartThreadpoolIo` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpStartAsyncIoOperation` |
| 1489 | `SubmitIoRing` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-ioring-l1-1-0.SubmitIoRing` |
| 1490 | `SubmitThreadpoolWork` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpPostWork` |
| 1496 | `SystemTimeToTzSpecificLocalTimeEx` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-timezone-l1-1-0.SystemTimeToTzSpecificLocalTimeEx` |
| 1519 | `TlsGetValue2` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.TlsGetValue2` |
| 1524 | `TryAcquireSRWLockExclusive` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlTryAcquireSRWLockExclusive` |
| 1525 | `TryAcquireSRWLockShared` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlTryAcquireSRWLockShared` |
| 1526 | `TryEnterCriticalSection` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlTryEnterCriticalSection` |
| 1529 | `TzSpecificLocalTimeToSystemTimeEx` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-timezone-l1-1-0.TzSpecificLocalTimeToSystemTimeEx` |
| 1537 | `UnmapViewOfFileEx` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-memory-l1-1-1.UnmapViewOfFileEx` |
| 1546 | `UpdateProcThreadAttribute` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-0.UpdateProcThreadAttribute` |
| 1553 | `VerSetConditionMask` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.VerSetConditionMask` |
| 1572 | `WaitForDebugEventEx` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-debug-l1-1-2.WaitForDebugEventEx` |
| 1577 | `WaitForThreadpoolIoCallbacks` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpWaitForIoCompletion` |
| 1578 | `WaitForThreadpoolTimerCallbacks` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpWaitForTimer` |
| 1579 | `WaitForThreadpoolWaitCallbacks` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpWaitForWait` |
| 1580 | `WaitForThreadpoolWorkCallbacks` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpWaitForWork` |
| 1583 | `WakeAllConditionVariable` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlWakeAllConditionVariable` |
| 1584 | `WakeConditionVariable` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlWakeConditionVariable` |
| 1651 | `__C_specific_handler` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.__C_specific_handler` |
| 1652 | `__chkstk` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.__chkstk` |
| 1653 | `__misaligned_access` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.__misaligned_access` |
| 1659 | `_local_unwind` | `0x0` | - | Forwarded | Forwarded to: `NTDLL._local_unwind` |
| 1053 | `MoveFileExA` | `0xACF0` | 32 | UnwindData |  |
| 858 | `GetVolumePathNameA` | `0xADF0` | 405 | UnwindData |  |
| 243 | `CreateMailslotW` | `0xAF90` | 434 | UnwindData |  |
| 242 | `CreateMailslotA` | `0xB150` | 111 | UnwindData |  |
| 134 | `CallNamedPipeA` | `0xB1D0` | 151 | UnwindData |  |
| 768 | `GetShortPathNameW` | `0xB270` | 1,177 | UnwindData |  |
| 264 | `CreateSemaphoreA` | `0xB710` | 167 | UnwindData |  |
| 265 | `CreateSemaphoreExA` | `0xB880` | 157 | UnwindData |  |
| 767 | `GetShortPathNameA` | `0xB930` | 595 | UnwindData |  |
| 665 | `GetLongPathNameA` | `0xBB90` | 593 | UnwindData |  |
| 668 | `GetLongPathNameW` | `0xBDF0` | 1,601 | UnwindData |  |
| 860 | `GetVolumePathNamesForVolumeNameA` | `0xC4A0` | 436 | UnwindData |  |
| 1145 | `QueryDosDeviceA` | `0xC660` | 520 | UnwindData |  |
| 1092 | `OpenSemaphoreA` | `0xC870` | 116 | UnwindData |  |
| 1581 | `WaitNamedPipeA` | `0xC8F0` | 84 | UnwindData |  |
| 1080 | `OpenFileMappingA` | `0xC950` | 121 | UnwindData |  |
| 249 | `CreateNamedPipeA` | `0xC9D0` | 164 | UnwindData |  |
| 225 | `CreateFileMappingA` | `0xCA80` | 186 | UnwindData |  |
| 80 | `Basep8BitStringToDynamicUnicodeString` | `0xCB40` | 119 | UnwindData |  |
| 1084 | `OpenMutexA` | `0xCBC0` | 114 | UnwindData |  |
| 1542 | `UnregisterWait` | `0xCC40` | 73 | UnwindData |  |
| 791 | `GetSystemPowerStatus` | `0xCC90` | 366 | UnwindData |  |
| 1442 | `SetThreadExecutionState` | `0xCE10` | 51 | UnwindData |  |
| 702 | `GetNumaProcessorNode` | `0xCE50` | 111 | UnwindData |  |
| 703 | `GetNumaProcessorNodeEx` | `0xCED0` | 194 | UnwindData |  |
| 446 | `FindResourceExA` | `0xCFA0` | 234 | UnwindData |  |
| 107 | `BasepMapModuleHandle` | `0xD1A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 642 | `GetFirmwareEnvironmentVariableW` | `0xD1D0` | 21 | UnwindData |  |
| 641 | `GetFirmwareEnvironmentVariableExW` | `0xD1F0` | 235 | UnwindData |  |
| 1640 | `WritePrivateProfileStringW` | `0xD2F0` | 100 | UnwindData |  |
| 488 | `GetAtomNameW` | `0xD360` | 31 | UnwindData |  |
| 879 | `GlobalGetAtomNameW` | `0xD390` | 31 | UnwindData |  |
| 670 | `GetMailslotInfo` | `0xD8B0` | 247 | UnwindData |  |
| 1438 | `SetThreadAffinityMask` | `0xD9B0` | 186 | UnwindData |  |
| 747 | `GetProcessIoCounters` | `0xDA70` | 61 | UnwindData |  |
| 1514 | `Thread32First` | `0xDAC0` | 253 | UnwindData |  |
| 736 | `GetProcessAffinityMask` | `0xDBD0` | 175 | UnwindData |  |
| 567 | `GetCurrentActCtxWorker` | `0xDEC0` | 59 | UnwindData |  |
| 1141 | `QueryActCtxSettingsWWorker` | `0xDF10` | 460 | UnwindData |  |
| 1151 | `QueryInformationJobObject` | `0xE0F0` | 339 | UnwindData |  |
| 662 | `GetLogicalDrives` | `0xE250` | 106 | UnwindData |  |
| 332 | `DosDateTimeToFileTime` | `0xE2C0` | 191 | UnwindData |  |
| 291 | `DeactivateActCtxWorker` | `0xE390` | 52 | UnwindData |  |
| 1515 | `Thread32Next` | `0xE3D0` | 260 | UnwindData |  |
| 4 | `ActivateActCtxWorker` | `0xE4E0` | 63 | UnwindData |  |
| 412 | `FindActCtxSectionStringWWorker` | `0xE6B0` | 414 | UnwindData |  |
| 402 | `FileTimeToDosDateTime` | `0xE860` | 215 | UnwindData |  |
| 409 | `FindActCtxSectionGuidWorker` | `0xE940` | 381 | UnwindData |  |
| 74 | `BaseSetLastNTError` | `0xEAD0` | 43 | UnwindData |  |
| 730 | `GetPrivateProfileSectionW` | `0xF0B0` | 196 | UnwindData |  |
| 55 | `BaseDllReadWriteIniFile` | `0xF180` | 786 | UnwindData |  |
| 1501 | `TermsrvConvertSysRootToUserDir` | `0x113A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1513 | `TermsrvSyncUserIniFileExt` | `0x113C0` | 5,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 454 | `FlsGetValue` | `0x12A00` | 101 | UnwindData |  |
| 937 | `IsBadReadPtr` | `0x12A70` | 127 | UnwindData |  |
| 831 | `GetTickCount64` | `0x12B00` | 2,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 496 | `GetCalendarDateFormat` | `0x13360` | 139 | UnwindData |  |
| 847 | `GetUserGeoID` | `0x13A70` | 251 | UnwindData |  |
| 842 | `GetUserDefaultGeoName` | `0x13EA0` | 235 | UnwindData |  |
| 648 | `GetGeoInfoA` | `0x13FA0` | 199 | UnwindData |  |
| 22 | `AdjustCalendarDate` | `0x140C0` | 640 | UnwindData |  |
| 498 | `GetCalendarDaysInMonth` | `0x14640` | 209 | UnwindData |  |
| 650 | `GetGeoInfoW` | `0x14830` | 634 | UnwindData |  |
| 497 | `GetCalendarDateFormatEx` | `0x14F20` | 840 | UnwindData |  |
| 1545 | `UpdateCalendarDayOfWeek` | `0x15270` | 181 | UnwindData |  |
| 959 | `IsValidCalDateTime` | `0x15500` | 222 | UnwindData |  |
| 836 | `GetTimeFormatWWorker` | `0x15990` | 554 | UnwindData |  |
| 591 | `GetDateFormatWWorker` | `0x16710` | 1,637 | UnwindData |  |
| 1122 | `Process32Next` | `0x181E0` | 279 | UnwindData |  |
| 1123 | `Process32NextW` | `0x18300` | 39 | UnwindData |  |
| 830 | `GetTickCount` | `0x18600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 584 | `GetCurrentThreadId` | `0x18620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 655 | `GetLastError` | `0x18640` | 9,648 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1175 | `QuirkIsEnabledForPackageWorker` | `0x1ABF0` | 156 | UnwindData |  |
| 1173 | `QuirkIsEnabledForPackage3Worker` | `0x1AD70` | 63 | UnwindData |  |
| 1174 | `QuirkIsEnabledForPackage4Worker` | `0x1ADC0` | 140 | UnwindData |  |
| 1171 | `QuirkIsEnabled3Worker` | `0x1AE60` | 357 | UnwindData |  |
| 1177 | `QuirkIsEnabledWorker` | `0x1B5D0` | 363 | UnwindData |  |
| 111 | `BasepQueryAppCompat` | `0x1CF00` | 632 | UnwindData |  |
| 51 | `BaseCheckElevation` | `0x216A0` | 528 | UnwindData |  |
| 147 | `CheckElevation` | `0x225D0` | 332 | UnwindData |  |
| 85 | `BasepCheckAppCompat` | `0x22730` | 216 | UnwindData |  |
| 98 | `BasepGetExeArchType` | `0x22810` | 527 | UnwindData |  |
| 1684 | `timeGetSystemTime` | `0x231C0` | 49 | UnwindData |  |
| 1685 | `timeGetTime` | `0x23200` | 90 | UnwindData |  |
| 997 | `LCMapStringEx` | `0x23260` | 84 | UnwindData |  |
| 323 | `DeviceIoControl` | `0x232C0` | 244 | UnwindData |  |
| 1682 | `timeEndPeriod` | `0x23420` | 351 | UnwindData |  |
| 583 | `GetCurrentThread` | `0x23590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `CompareStringEx` | `0x235A0` | 84 | UnwindData |  |
| 1681 | `timeBeginPeriod` | `0x23600` | 64 | UnwindData |  |
| 580 | `GetCurrentProcessId` | `0x23760` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1654 | `_hread` | `0x23BC0` | 53 | UnwindData |  |
| 1661 | `_lread` | `0x23BC0` | 53 | UnwindData |  |
| 877 | `GlobalFree` | `0x23FC0` | 61 | UnwindData |  |
| 742 | `GetProcessHeap` | `0x24010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1155 | `QueryPerformanceCounter` | `0x24030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1176 | `QuirkIsEnabledForProcessWorker` | `0x24050` | 696 | UnwindData |  |
| 1050 | `Module32Next` | `0x24410` | 322 | UnwindData |  |
| 1051 | `Module32NextW` | `0x24560` | 348 | UnwindData |  |
| 1508 | `TermsrvOpenRegEntry` | `0x246D0` | 800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 579 | `GetCurrentProcess` | `0x249F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 898 | `HeapFree` | `0x24A00` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 203 | `CreateActCtxWWorker` | `0x24CF0` | 3,685 | UnwindData |  |
| 115 | `BasepReleaseSxsCreateProcessUtilityStruct` | `0x26FA0` | 132 | UnwindData |  |
| 89 | `BasepConstructSxsCreateProcessMessage` | `0x27C40` | 1,878 | UnwindData |  |
| 1306 | `RtlVirtualUnwind` | `0x28D40` | 67 | UnwindData |  |
| 1402 | `SetLastError` | `0x28E30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 617 | `GetExitCodeProcess` | `0x28E50` | 100 | UnwindData |  |
| 1249 | `RegisterWaitForSingleObject` | `0x28F90` | 140 | UnwindData |  |
| 1487 | `SortGetHandle` | `0x29030` | 160 | UnwindData |  |
| 1520 | `TlsSetValue` | `0x29CE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 434 | `FindNLSStringEx` | `0x29D00` | 96 | UnwindData |  |
| 1655 | `_hwrite` | `0x2BCB0` | 72 | UnwindData |  |
| 1662 | `_lwrite` | `0x2BCB0` | 72 | UnwindData |  |
| 1557 | `VerifyVersionInfoW` | `0x2E150` | 69 | UnwindData |  |
| 75 | `BaseThreadInitThunk` | `0x2E940` | 77 | UnwindData |  |
| 765 | `GetQueuedCompletionStatus` | `0x2F030` | 6,864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1663 | `lstrcat` | `0x30B00` | 41 | UnwindData |  |
| 1664 | `lstrcatA` | `0x30B00` | 41 | UnwindData |  |
| 819 | `GetThreadIdealProcessorEx` | `0x30B30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 938 | `IsBadStringPtrA` | `0x30B50` | 76 | UnwindData |  |
| 96 | `BasepGetAppCompatData` | `0x30BB0` | 1,311 | UnwindData |  |
| 64 | `BaseGenerateAppCompatData` | `0x315E0` | 124 | UnwindData |  |
| 1482 | `Sleep` | `0x31A10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 796 | `GetSystemTimeAsFileTime` | `0x31A30` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1493 | `SwitchToThread` | `0x31C40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1120 | `Process32First` | `0x31C60` | 279 | UnwindData |  |
| 1121 | `Process32FirstW` | `0x31D80` | 342 | UnwindData |  |
| 1505 | `TermsrvGetPreSetValue` | `0x31EE0` | 34 | UnwindData |  |
| 414 | `FindAtomW` | `0x31F10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 286 | `CreateWaitableTimerExA` | `0x31F30` | 140 | UnwindData |  |
| 1658 | `_llseek` | `0x32010` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1061 | `MultiByteToWideChar` | `0x32050` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 956 | `IsThreadAFiber` | `0x320D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1680 | `lstrlenW` | `0x320F0` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `BackupReadEx` | `0x322C0` | 917 | UnwindData |  |
| 1614 | `WideCharToMultiByte` | `0x33130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 998 | `LCMapStringW` | `0x33150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 180 | `CompareStringOrdinal` | `0x33170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 273 | `CreateThread` | `0x33190` | 72 | UnwindData |  |
| 1164 | `QueryUnbiasedInterruptTime` | `0x331E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1672 | `lstrcpy` | `0x33200` | 28 | UnwindData |  |
| 1673 | `lstrcpyA` | `0x33200` | 28 | UnwindData |  |
| 1512 | `TermsrvSetValueKey` | `0x33230` | 49 | UnwindData |  |
| 1156 | `QueryPerformanceFrequency` | `0x33270` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1048 | `Module32First` | `0x33490` | 343 | UnwindData |  |
| 1049 | `Module32FirstW` | `0x335F0` | 353 | UnwindData |  |
| 108 | `BasepNotifyLoadStringResource` | `0x33760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1612 | `WerpNotifyLoadStringResourceWorker` | `0x33760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1613 | `WerpNotifyUseStringResourceWorker` | `0x33760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1154 | `QueryMemoryResourceNotification` | `0x33770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1072 | `OOBEComplete` | `0x33790` | 170 | UnwindData |  |
| 285 | `CreateWaitableTimerA` | `0x33C40` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1089 | `OpenProcess` | `0x33CE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 735 | `GetProcAddress` | `0x33D00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1558 | `VirtualAlloc` | `0x33D20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 713 | `GetOverlappedResult` | `0x33D40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1112 | `PostQueuedCompletionStatus` | `0x33D60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1671 | `lstrcmpiW` | `0x33D80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1687 | `uaw_lstrcmpiW` | `0x33D80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1674 | `lstrcpyW` | `0x33DA0` | 32 | UnwindData |  |
| 88 | `BasepCheckWinSaferRestrictions` | `0x33DD0` | 2,579 | UnwindData |  |
| 279 | `CreateThreadpoolWork` | `0x347F0` | 74 | UnwindData |  |
| 1028 | `LocalFree` | `0x34B20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 828 | `GetThreadTimes` | `0x34B40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1502 | `TermsrvCreateRegEntry` | `0x34B60` | 39 | UnwindData |  |
| 1012 | `LoadAppInitDlls` | `0x34B90` | 282 | UnwindData |  |
| 1665 | `lstrcatW` | `0x35060` | 46 | UnwindData |  |
| 960 | `IsValidCodePage` | `0x350A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 870 | `GlobalAlloc` | `0x350C0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1124 | `ProcessIdToSessionId` | `0x35150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 744 | `GetProcessId` | `0x35170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 882 | `GlobalMemoryStatus` | `0x35190` | 239 | UnwindData |  |
| 1556 | `VerifyVersionInfoA` | `0x35340` | 248 | UnwindData |  |
| 95 | `BasepFreeAppCompatData` | `0x35440` | 68 | UnwindData |  |
| 117 | `BasepSetFileEncryptionCompression` | `0x354B0` | 1,639 | UnwindData |  |
| 1504 | `TermsrvDeleteValue` | `0x35B20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1561 | `VirtualFree` | `0x35B40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 288 | `CreateWaitableTimerW` | `0x35B60` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 777 | `GetStringTypeExW` | `0x35B90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1070 | `NotifyUILanguageChange` | `0x35BB0` | 620 | UnwindData |  |
| 939 | `IsBadStringPtrW` | `0x36BE0` | 80 | UnwindData |  |
| 1503 | `TermsrvDeleteKey` | `0x36C40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1138 | `PulseEvent` | `0x36C60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 872 | `GlobalDeleteAtom` | `0x36C80` | 53 | UnwindData |  |
| 1507 | `TermsrvGetWindowsDirectoryW` | `0x36CC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 277 | `CreateThreadpoolTimer` | `0x36CE0` | 74 | UnwindData |  |
| 1447 | `SetThreadLocale` | `0x36D30` | 1,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1449 | `SetThreadPriority` | `0x374D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 794 | `GetSystemTime` | `0x374F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 823 | `GetThreadPriority` | `0x37510` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1678 | `lstrlen` | `0x37530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1679 | `lstrlenA` | `0x37530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 503 | `GetCalendarMonthsInYear` | `0x37550` | 228 | UnwindData |  |
| 504 | `GetCalendarSupportedDateRange` | `0x37640` | 525 | UnwindData |  |
| 189 | `ConvertSystemTimeToCalDateTime` | `0x37860` | 225 | UnwindData |  |
| 1509 | `TermsrvOpenUserClasses` | `0x379A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1096 | `OpenThread` | `0x379C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1023 | `LocalAlloc` | `0x379E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 821 | `GetThreadLocale` | `0x37A00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1160 | `QueryThreadCycleTime` | `0x37A20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 874 | `GlobalFindAtomW` | `0x37A40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1656 | `_lclose` | `0x37A60` | 33 | UnwindData |  |
| 456 | `FlsSetValue` | `0x37A90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1494 | `SystemTimeToFileTime` | `0x37AB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1301 | `RtlPcToFileHeader` | `0x37AD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `ActivateActCtx` | `0x37AF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 618 | `GetExitCodeThread` | `0x37B10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1110 | `PeekNamedPipe` | `0x37B30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1398 | `SetInformationJobObject` | `0x37B50` | 422 | UnwindData |  |
| 940 | `IsBadWritePtr` | `0x37D00` | 127 | UnwindData |  |
| 656 | `GetLocalTime` | `0x37D90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 778 | `GetStringTypeW` | `0x37DB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 907 | `HeapWalk` | `0x37DD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1383 | `SetFileCompletionNotificationModes` | `0x37DF0` | 112 | UnwindData |  |
| 7 | `AddAtomW` | `0x37E70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 671 | `GetMaximumProcessorCount` | `0x37E90` | 178 | UnwindData |  |
| 479 | `GetActiveProcessorGroupCount` | `0x37F50` | 87 | UnwindData |  |
| 672 | `GetMaximumProcessorGroupCount` | `0x37FB0` | 87 | UnwindData |  |
| 478 | `GetActiveProcessorCount` | `0x38010` | 182 | UnwindData |  |
| 629 | `GetFileInformationByHandleEx` | `0x381C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 966 | `IsWow64Process` | `0x381E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1564 | `VirtualProtect` | `0x38200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 752 | `GetProcessTimes` | `0x38220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1566 | `VirtualQuery` | `0x38240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1044 | `MapViewOfFile` | `0x38260` | 1,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1036 | `LocaleNameToLCID` | `0x386F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1143 | `QueryActCtxWWorker` | `0x38710` | 397 | UnwindData |  |
| 106 | `BasepIsProcessAllowed` | `0x388B0` | 370 | UnwindData |  |
| 1114 | `PowerCreateRequest` | `0x38A30` | 134 | UnwindData |  |
| 1536 | `UnmapViewOfFile` | `0x38DA0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `CompareStringW` | `0x38ED0` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `BasepCheckWebBladeHashes` | `0x390D0` | 278 | UnwindData |  |
| 833 | `GetTimeFormatAWorker` | `0x391F0` | 630 | UnwindData |  |
| 588 | `GetDateFormatAWorker` | `0x39470` | 624 | UnwindData |  |
| 375 | `EnumSystemGeoID` | `0x39850` | 238 | UnwindData |  |
| 843 | `GetUserDefaultLCID` | `0x39950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 685 | `GetNamedPipeClientProcessId` | `0x39970` | 56 | UnwindData |  |
| 1668 | `lstrcmpW` | `0x399B0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1686 | `uaw_lstrcmpW` | `0x399B0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1669 | `lstrcmpi` | `0x39A00` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1670 | `lstrcmpiA` | `0x39A00` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 818 | `GetThreadId` | `0x39C10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1582 | `WaitNamedPipeW` | `0x39C30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 303 | `DeleteAtom` | `0x39C50` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 989 | `K32GetProcessMemoryInfo` | `0x39D10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1511 | `TermsrvSetKeySecurity` | `0x39D30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 766 | `GetQueuedCompletionStatusEx` | `0x39D50` | 1,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 431 | `FindFirstVolumeMountPointW` | `0x3A170` | 663 | UnwindData |  |
| 1543 | `UnregisterWaitEx` | `0x3A9F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1567 | `VirtualQueryEx` | `0x3AA10` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 729 | `GetPrivateProfileSectionNamesW` | `0x3AC30` | 34 | UnwindData |  |
| 726 | `GetPrivateProfileIntW` | `0x3AC60` | 246 | UnwindData |  |
| 732 | `GetPrivateProfileStringW` | `0x3AD60` | 395 | UnwindData |  |
| 883 | `GlobalMemoryStatusEx` | `0x3AF00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 477 | `GetACP` | `0x3AF20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 290 | `DeactivateActCtx` | `0x3AF40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 616 | `GetErrorMode` | `0x3AF60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 257 | `CreateProcessAsUserW` | `0x3AF80` | 107 | UnwindData |  |
| 229 | `CreateFileMappingW` | `0x3B040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1178 | `RaiseException` | `0x3B060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1165 | `QueueUserAPC` | `0x3B080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 995 | `LCIDToLocaleName` | `0x3B0A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 893 | `Heap32Next` | `0x3B0C0` | 723 | UnwindData |  |
| 679 | `GetModuleHandleW` | `0x3B3A0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 459 | `FlushInstructionCache` | `0x3B4A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 448 | `FindResourceW` | `0x3B4C0` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1516 | `TlsAlloc` | `0x3B650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `BaseElevationPostProcessing` | `0x3B670` | 71 | UnwindData |  |
| 1366 | `SetDllDirectoryW` | `0x3B6C0` | 149 | UnwindData |  |
| 1255 | `ReleaseActCtxWorker` | `0x3B760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1198 | `ReadProcessMemory` | `0x3B780` | 1,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 519 | `GetComputerNameA` | `0x3BBB0` | 299 | UnwindData |  |
| 522 | `GetComputerNameW` | `0x3BDC0` | 987 | UnwindData |  |
| 408 | `FindActCtxSectionGuid` | `0x3C360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 240 | `CreateJobObjectW` | `0x3C380` | 189 | UnwindData |  |
| 1373 | `SetErrorMode` | `0x3C450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1480 | `SignalObjectAndWait` | `0x3C470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1289 | `ResumeThread` | `0x3C490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 869 | `GlobalAddAtomW` | `0x3C4B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 675 | `GetModuleFileNameW` | `0x3C4D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1568 | `VirtualUnlock` | `0x3C4F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 944 | `IsDBCSLeadByte` | `0x3C510` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 676 | `GetModuleHandleA` | `0x3C530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1016 | `LoadLibraryExW` | `0x3C550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 470 | `FreeLibrary` | `0x3C570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `AddRefActCtxWorker` | `0x3C590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1299 | `RtlLookupFunctionEntry` | `0x3C5B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 260 | `CreateProcessW` | `0x3C5D0` | 95 | UnwindData |  |
| 812 | `GetThreadContext` | `0x3C640` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1481 | `SizeofResource` | `0x3C680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 868 | `GlobalAddAtomExW` | `0x3C6A0` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `BasepFinishPackageActivationForSxS` | `0x3C860` | 46 | UnwindData |  |
| 798 | `GetSystemTimes` | `0x3CF90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 659 | `GetLocaleInfoW` | `0x3CFB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1441 | `SetThreadErrorMode` | `0x3CFD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 396 | `ExpandEnvironmentStringsW` | `0x3CFF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1148 | `QueryFullProcessImageNameW` | `0x3D010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 881 | `GlobalLock` | `0x3D030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 889 | `GlobalWire` | `0x3D030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `BaseReadAppCompatDataForProcessWorker` | `0x3D050` | 657 | UnwindData |  |
| 880 | `GlobalHandle` | `0x3D530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1020 | `LoadResource` | `0x3D550` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 790 | `GetSystemInfo` | `0x3D740` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1527 | `TrySubmitThreadpoolCallback` | `0x3D8B0` | 54 | UnwindData |  |
| 946 | `IsDebuggerPresent` | `0x3D8F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1248 | `RegisterWaitForInputIdle` | `0x3D910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 954 | `IsProcessorFeaturePresent` | `0x3D920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 724 | `GetPriorityClass` | `0x3D940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 658 | `GetLocaleInfoEx` | `0x3D960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 886 | `GlobalUnWire` | `0x3D980` | 2,608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 888 | `GlobalUnlock` | `0x3D980` | 2,608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 447 | `FindResourceExW` | `0x3E3B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 445 | `FindResourceA` | `0x3E3D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 614 | `GetEnvironmentVariableW` | `0x3E3F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 771 | `GetStartupInfoW` | `0x3E410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1057 | `MoveFileW` | `0x3E430` | 36 | UnwindData |  |
| 678 | `GetModuleHandleExW` | `0x3E460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 770 | `GetStartupInfoA` | `0x3E480` | 788 | UnwindData |  |
| 1500 | `TermsrvAppInstallMode` | `0x3E7A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1491 | `SuspendThread` | `0x3E7C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1569 | `WTSGetActiveConsoleSessionId` | `0x3E7E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 864 | `GetWriteWatch` | `0x3E800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 466 | `FormatMessageW` | `0x3E820` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1068 | `NormalizeString` | `0x3E8D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 278 | `CreateThreadpoolWait` | `0x3E8F0` | 74 | UnwindData |  |
| 572 | `GetCurrentDirectoryW` | `0x3EB10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1450 | `SetThreadPriorityBoost` | `0x3EB30` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 784 | `GetSystemDefaultLocaleName` | `0x3ED40` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `AreFileApisANSI` | `0x3EFC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `AssignProcessToJobObject` | `0x3EFE0` | 47 | UnwindData |  |
| 471 | `FreeLibraryAndExitThread` | `0x3F020` | 17 | UnwindData |  |
| 1517 | `TlsFree` | `0x3F040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1115 | `PowerSetRequest` | `0x3F060` | 149 | UnwindData |  |
| 745 | `GetProcessIdOfThread` | `0x3F100` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1437 | `SetTermsrvAppInstallMode` | `0x3F1C0` | 317 | UnwindData |  |
| 1683 | `timeGetDevCaps` | `0x3F3B0` | 93 | UnwindData |  |
| 984 | `K32GetModuleFileNameExW` | `0x3F5A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1444 | `SetThreadIdealProcessor` | `0x3F5C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 690 | `GetNamedPipeServerProcessId` | `0x3F5E0` | 53 | UnwindData |  |
| 1495 | `SystemTimeToTzSpecificLocalTime` | `0x3F620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1113 | `PowerClearRequest` | `0x3F640` | 148 | UnwindData |  |
| 787 | `GetSystemDirectoryW` | `0x3F6E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 945 | `IsDBCSLeadByteEx` | `0x3F6F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1017 | `LoadLibraryW` | `0x3F710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 980 | `K32GetMappedFileNameW` | `0x3F730` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 602 | `GetDllDirectoryW` | `0x3F780` | 136 | UnwindData |  |
| 660 | `GetLogicalDriveStringsA` | `0x3F810` | 189 | UnwindData |  |
| 613 | `GetEnvironmentVariableA` | `0x3F8E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1040 | `LockResource` | `0x3F900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1029 | `LocalHandle` | `0x3F920` | 175 | UnwindData |  |
| 824 | `GetThreadPriorityBoost` | `0x3F9E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 852 | `GetVersionExW` | `0x3FA00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 953 | `IsProcessInJob` | `0x3FA20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1305 | `RtlUnwindEx` | `0x3FA40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 783 | `GetSystemDefaultLangID` | `0x3FA60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 773 | `GetStdHandle` | `0x3FA80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 237 | `CreateIoCompletionPort` | `0x3FAA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 845 | `GetUserDefaultLocaleName` | `0x3FAC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1015 | `LoadLibraryExA` | `0x3FAE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 674 | `GetModuleFileNameA` | `0x3FB00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 692 | `GetNativeSystemInfo` | `0x3FB20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 452 | `FlsAlloc` | `0x3FB40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 331 | `DnsHostnameToComputerNameW` | `0x3FB60` | 208 | UnwindData |  |
| 1081 | `OpenFileMappingW` | `0x3FC40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 988 | `K32GetProcessImageFileNameW` | `0x3FC60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 413 | `FindAtomA` | `0x3FC80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1101 | `OutputDebugStringW` | `0x3FCA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1194 | `ReadDirectoryChangesW` | `0x3FCC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1591 | `WerRegisterFile` | `0x3FCE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1563 | `VirtualLock` | `0x3FD00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 733 | `GetPrivateProfileStructA` | `0x3FD20` | 396 | UnwindData |  |
| 763 | `GetProfileStringA` | `0x3FEC0` | 29 | UnwindData |  |
| 725 | `GetPrivateProfileIntA` | `0x3FEF0` | 150 | UnwindData |  |
| 731 | `GetPrivateProfileStringA` | `0x3FF90` | 452 | UnwindData |  |
| 782 | `GetSystemDefaultLCID` | `0x40160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `CancelIoEx` | `0x40180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `BasepFreeActivationTokenInfo` | `0x401A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1045 | `MapViewOfFileEx` | `0x401B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1167 | `QueueUserWorkItem` | `0x401D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 513 | `GetCommandLineA` | `0x401F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1018 | `LoadModule` | `0x40210` | 1,251 | UnwindData |  |
| 491 | `GetBinaryTypeW` | `0x40700` | 859 | UnwindData |  |
| 708 | `GetNumberFormatW` | `0x40A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 934 | `IsBadCodePtr` | `0x40A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 178 | `CompareStringA` | `0x40A90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1643 | `WriteProcessMemory` | `0x40AB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | `CreateActCtxA` | `0x40AD0` | 848 | UnwindData |  |
| 1304 | `RtlUnwind` | `0x40E30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 514 | `GetCommandLineW` | `0x40E50` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 461 | `FlushViewOfFile` | `0x40F20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `BackupRead` | `0x40F40` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1666 | `lstrcmp` | `0x40F80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1667 | `lstrcmpA` | `0x40F80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1497 | `TerminateJobObject` | `0x40F90` | 47 | UnwindData |  |
| 182 | `ConnectNamedPipe` | `0x40FD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `CheckNameLegalDOS8Dot3W` | `0x40FF0` | 290 | UnwindData |  |
| 1293 | `RtlCompareMemory` | `0x41120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1078 | `OpenFile` | `0x41140` | 1,414 | UnwindData |  |
| 392 | `ExitProcess` | `0x417F0` | 17 | UnwindData |  |
| 401 | `FatalExit` | `0x417F0` | 17 | UnwindData |  |
| 906 | `HeapValidate` | `0x41810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 492 | `GetCPInfo` | `0x41830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 317 | `DeleteTimerQueueTimer` | `0x41850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `BasepAppXExtension` | `0x41870` | 47 | UnwindData |  |
| 850 | `GetVersion` | `0x41AB0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 837 | `GetTimeZoneInformation` | `0x41B30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1283 | `ResetWriteWatch` | `0x41B50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 677 | `GetModuleHandleExA` | `0x41B70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 612 | `GetEnvironmentStringsW` | `0x41B90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 449 | `FindStringOrdinal` | `0x41BB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 281 | `CreateTimerQueueTimer` | `0x41BD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1453 | `SetThreadStackGuarantee` | `0x41BF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1100 | `OutputDebugStringA` | `0x41C10` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 993 | `K32QueryWorkingSet` | `0x41E80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1603 | `WerUnregisterFile` | `0x41EA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `CallbackMayRunLong` | `0x41EC0` | 54 | UnwindData |  |
| 324 | `DisableThreadLibraryCalls` | `0x41F00` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1412 | `SetPriorityClass` | `0x422E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `CancelIo` | `0x42300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 250 | `CreateNamedPipeW` | `0x42320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1565 | `VirtualProtectEx` | `0x42340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1408 | `SetMailslotInfo` | `0x42360` | 128 | UnwindData |  |
| 896 | `HeapCreate` | `0x423F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 863 | `GetWindowsDirectoryW` | `0x42410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 817 | `GetThreadIOPendingFlag` | `0x42430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1088 | `OpenPrivateNamespaceW` | `0x42450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 866 | `GlobalAddAtomA` | `0x42470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 453 | `FlsFree` | `0x42490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 851 | `GetVersionExA` | `0x424B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 469 | `FreeEnvironmentStringsW` | `0x424D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1498 | `TerminateProcess` | `0x424F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 657 | `GetLocaleInfoA` | `0x42510` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `BasepGetComputerNameFromNtPath` | `0x42530` | 1,321 | UnwindData |  |
| 1411 | `SetNamedPipeHandleState` | `0x42A60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 566 | `GetCurrentActCtx` | `0x42A80` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 994 | `K32QueryWorkingSetEx` | `0x42B10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1276 | `ReplaceFile` | `0x42B30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1278 | `ReplaceFileW` | `0x42B30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1522 | `TransactNamedPipe` | `0x42B50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 885 | `GlobalSize` | `0x42B70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1079 | `OpenFileById` | `0x42B90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 275 | `CreateThreadpoolCleanupGroup` | `0x42BB0` | 65 | UnwindData |  |
| 363 | `EnumResourceLanguagesW` | `0x42C00` | 47 | UnwindData |  |
| 643 | `GetFirmwareType` | `0x42C40` | 135 | UnwindData |  |
| 1014 | `LoadLibraryA` | `0x42CD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1172 | `QuirkIsEnabledForPackage2Worker` | `0x42CF0` | 39 | UnwindData |  |
| 985 | `K32GetModuleInformation` | `0x42D20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1147 | `QueryFullProcessImageNameA` | `0x42D40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 262 | `CreateRemoteThread` | `0x42D60` | 67 | UnwindData |  |
| 205 | `CreateBoundaryDescriptorW` | `0x42DB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 687 | `GetNamedPipeHandleStateA` | `0x42DD0` | 406 | UnwindData |  |
| 1424 | `SetProcessShutdownParameters` | `0x42F70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 148 | `CheckElevationEnabled` | `0x42F90` | 65 | UnwindData |  |
| 1158 | `QueryProcessCycleTime` | `0x42FE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1528 | `TzSpecificLocalTimeToSystemTime` | `0x43000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 235 | `CreateHardLinkTransactedW` | `0x43020` | 189 | UnwindData |  |
| 892 | `Heap32ListNext` | `0x430F0` | 235 | UnwindData |  |
| 897 | `HeapDestroy` | `0x431F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 983 | `K32GetModuleFileNameExA` | `0x43210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1639 | `WritePrivateProfileStringA` | `0x43230` | 100 | UnwindData |  |
| 304 | `DeleteBoundaryDescriptor` | `0x432A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 440 | `FindNextVolumeA` | `0x432C0` | 352 | UnwindData |  |
| 1559 | `VirtualAllocEx` | `0x43430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 844 | `GetUserDefaultLangID` | `0x43450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 328 | `DisconnectNamedPipe` | `0x43470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 835 | `GetTimeFormatW` | `0x43490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 873 | `GlobalFindAtomA` | `0x434B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1506 | `TermsrvGetWindowsDirectoryA` | `0x434D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 972 | `K32EnumProcessModules` | `0x434F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1371 | `SetEnvironmentVariableA` | `0x43510` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1616 | `Wow64DisableWow64FsRedirection` | `0x43530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1466 | `SetUnhandledExceptionFilter` | `0x43550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 173 | `CmdBatNotification` | `0x43570` | 122 | UnwindData |  |
| 727 | `GetPrivateProfileSectionA` | `0x43660` | 183 | UnwindData |  |
| 1054 | `MoveFileExW` | `0x43720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 987 | `K32GetProcessImageFileNameA` | `0x43740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 758 | `GetProductInfo` | `0x43760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `AddSIDToBoundaryDescriptor` | `0x43780` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1458 | `SetThreadpoolThreadMinimum` | `0x437A0` | 54 | UnwindData |  |
| 1595 | `WerRegisterRuntimeExceptionModule` | `0x437E0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1372 | `SetEnvironmentVariableW` | `0x43890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 663 | `GetLogicalProcessorInformation` | `0x438B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1413 | `SetProcessAffinityMask` | `0x438D0` | 62 | UnwindData |  |
| 786 | `GetSystemDirectoryA` | `0x43920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 741 | `GetProcessHandleCount` | `0x43930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 465 | `FormatMessageA` | `0x43950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1212 | `RegEnumKeyExA` | `0x43970` | 67 | UnwindData |  |
| 982 | `K32GetModuleBaseNameW` | `0x439C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 274 | `CreateThreadpool` | `0x439E0` | 68 | UnwindData |  |
| 521 | `GetComputerNameExW` | `0x43A30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1361 | `SetCurrentDirectoryW` | `0x43A50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `BasepAppContainerEnvironmentExtension` | `0x43A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 902 | `HeapSetInformation` | `0x43A80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1552 | `VerLanguageNameW` | `0x43AA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `BaseFreeAppCompatDataForProcessWorker` | `0x43AC0` | 45 | UnwindData |  |
| 1677 | `lstrcpynW` | `0x43B00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 846 | `GetUserDefaultUILanguage` | `0x43B20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 962 | `IsValidLocale` | `0x43B40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 607 | `GetDynamicTimeZoneInformation` | `0x43B60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 890 | `Heap32First` | `0x43B80` | 640 | UnwindData |  |
| 1443 | `SetThreadGroupAffinity` | `0x43E10` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 589 | `GetDateFormatEx` | `0x43E90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 974 | `K32EnumProcesses` | `0x43EB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1486 | `SortCloseHandle` | `0x43ED0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1296 | `RtlFillMemory` | `0x43F00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 518 | `GetCompressedFileSizeW` | `0x43F20` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 231 | `CreateFileTransactedW` | `0x43F70` | 352 | UnwindData |  |
| 1396 | `SetHandleCount` | `0x440E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 350 | `EnumCalendarInfoExEx` | `0x440F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `BindIoCompletionCallback` | `0x44110` | 42 | UnwindData |  |
| 594 | `GetDevicePowerState` | `0x44140` | 77 | UnwindData |  |
| 1605 | `WerUnregisterMemoryBlock` | `0x441A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `BasepPostSuccessAppXExtension` | `0x441C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1642 | `WritePrivateProfileStructW` | `0x441E0` | 360 | UnwindData |  |
| 590 | `GetDateFormatW` | `0x44800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1142 | `QueryActCtxW` | `0x44820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1118 | `PrivCopyFileExW` | `0x44840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 834 | `GetTimeFormatEx` | `0x44860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 822 | `GetThreadPreferredUILanguages` | `0x44880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 973 | `K32EnumProcessModulesEx` | `0x448A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1593 | `WerRegisterMemoryBlock` | `0x448C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | `CreateActCtxW` | `0x448E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 712 | `GetOEMCP` | `0x44900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `BasepReleaseAppXContext` | `0x44920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 951 | `IsNormalizedString` | `0x44940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 789 | `GetSystemFirmwareTable` | `0x44960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1181 | `ReOpenFile` | `0x44980` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1455 | `SetThreadUILanguage` | `0x44A20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 996 | `LCMapStringA` | `0x44A40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 760 | `GetProfileIntW` | `0x44A60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1571 | `WaitForDebugEvent` | `0x44A70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1031 | `LocalReAlloc` | `0x44A90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 800 | `GetSystemWindowsDirectoryW` | `0x44AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 244 | `CreateMemoryResourceNotification` | `0x44AC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 280 | `CreateTimerQueue` | `0x44AE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `BaseCheckAppcompatCacheExWorker` | `0x44B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `BaseCheckAppcompatCacheWorker` | `0x44B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `BaseIsAppcompatInfrastructureDisabled` | `0x44B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `BaseIsAppcompatInfrastructureDisabledWorker` | `0x44B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1554 | `VerifyConsoleIoHandle` | `0x44B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1037 | `LocateXStateFeature` | `0x44B10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 862 | `GetWindowsDirectoryA` | `0x44B30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 463 | `FoldStringW` | `0x44B50` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1675 | `lstrcpyn` | `0x44BE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1676 | `lstrcpynA` | `0x44BE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1287 | `ResolveLocaleName` | `0x44C00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 884 | `GlobalReAlloc` | `0x44C20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `CancelDeviceWakeupRequest` | `0x44C40` | 22 | UnwindData |  |
| 1280 | `RequestDeviceWakeup` | `0x44C40` | 22 | UnwindData |  |
| 1281 | `RequestWakeupLatency` | `0x44C40` | 22 | UnwindData |  |
| 1409 | `SetMessageWaitingIndicator` | `0x44C40` | 22 | UnwindData |  |
| 474 | `FreeResource` | `0x44C60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1589 | `WerRegisterCustomMetadata` | `0x44C80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1201 | `RegCloseKey` | `0x44CA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 188 | `ConvertNLSDayOfWeekToWin32DayOfWeek` | `0x44CC0` | 49 | UnwindData |  |
| 697 | `GetNumaHighestNodeNumber` | `0x44D00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 955 | `IsSystemResumeAutomatic` | `0x44D20` | 25 | UnwindData |  |
| 1219 | `RegGetValueW` | `0x44E10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 411 | `FindActCtxSectionStringW` | `0x44E30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1312 | `SearchPathW` | `0x44E50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1254 | `ReleaseActCtx` | `0x44E70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1242 | `RegisterApplicationRecoveryCallback` | `0x44E90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 255 | `CreateProcessA` | `0x44EC0` | 95 | UnwindData |  |
| 795 | `GetSystemTimeAdjustment` | `0x44F30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 162 | `ClosePrivateNamespace` | `0x44F50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 981 | `K32GetModuleBaseNameA` | `0x44F70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 785 | `GetSystemDefaultUILanguage` | `0x44F90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 816 | `GetThreadGroupAffinity` | `0x44FB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `BaseGetNamedObjectDirectory` | `0x44FD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1213 | `RegEnumKeyExW` | `0x44FF0` | 67 | UnwindData |  |
| 1439 | `SetThreadContext` | `0x45040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 632 | `GetFileMUIPath` | `0x45060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1227 | `RegOpenKeyExW` | `0x45080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1428 | `SetSearchPathMode` | `0x450A0` | 42 | UnwindData |  |
| 1225 | `RegOpenCurrentUser` | `0x450D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1448 | `SetThreadPreferredUILanguages` | `0x450F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1232 | `RegQueryValueExW` | `0x45110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `AddIntegrityLabelToBoundaryDescriptor` | `0x45130` | 42 | UnwindData |  |
| 1562 | `VirtualFreeEx` | `0x45160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `CheckRemoteDebuggerPresent` | `0x45180` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `ConvertDefaultLocale` | `0x45480` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 815 | `GetThreadErrorMode` | `0x45550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 691 | `GetNamedPipeServerSessionId` | `0x45570` | 53 | UnwindData |  |
| 1560 | `VirtualAllocExNuma` | `0x455B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 316 | `DeleteTimerQueueEx` | `0x455D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1607 | `WerUnregisterRuntimeExceptionModule` | `0x455F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 986 | `K32GetPerformanceInfo` | `0x45610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 848 | `GetUserPreferredUILanguages` | `0x45630` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `AddAtomA` | `0x45820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 196 | `CopyFileExW` | `0x45840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1083 | `OpenJobObjectW` | `0x45860` | 217 | UnwindData |  |
| 1193 | `ReadDirectoryChangesExW` | `0x45940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1290 | `RtlAddFunctionTable` | `0x45960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 429 | `FindFirstVolumeA` | `0x45980` | 353 | UnwindData |  |
| 362 | `EnumResourceLanguagesExW` | `0x45AF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 383 | `EnumTimeFormatsEx` | `0x45B10` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `ChangeTimerQueueTimer` | `0x45BF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 252 | `CreatePipe` | `0x45C10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1137 | `PssWalkSnapshot` | `0x45C30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1620 | `Wow64RevertWow64FsRedirection` | `0x45C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1445 | `SetThreadIdealProcessorEx` | `0x45C70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 686 | `GetNamedPipeClientSessionId` | `0x45C90` | 77 | UnwindData |  |
| 1499 | `TerminateThread` | `0x45CF0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 775 | `GetStringTypeA` | `0x45E00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 776 | `GetStringTypeExA` | `0x45E00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 571 | `GetCurrentDirectoryA` | `0x45E20` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 908 | `IdnToAscii` | `0x45F40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 494 | `GetCPInfoExW` | `0x45F60` | 1,968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `BasepGetPackagedAppInfoForFile` | `0x46710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 876 | `GlobalFlags` | `0x46730` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 968 | `K32EmptyWorkingSet` | `0x46750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 380 | `EnumSystemLocalesEx` | `0x46770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 762 | `GetProfileSectionW` | `0x46790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 759 | `GetProfileIntA` | `0x467A0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1647 | `WriteProfileStringW` | `0x46830` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 236 | `CreateHardLinkW` | `0x46920` | 1,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1231 | `RegQueryValueExA` | `0x46E40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 723 | `GetPhysicallyInstalledSystemMemory` | `0x46E60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 899 | `HeapLock` | `0x46E80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1226 | `RegOpenKeyExA` | `0x46EA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 799 | `GetSystemWindowsDirectoryA` | `0x46EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1204 | `RegCreateKeyExW` | `0x46ED0` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 976 | `K32GetDeviceDriverBaseNameW` | `0x47220` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | `ContinueDebugEvent` | `0x472E0` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 355 | `EnumDateFormatsExEx` | `0x474D0` | 1,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 917 | `InitializeContext` | `0x47970` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 608 | `GetEnabledXStateFeatures` | `0x47B60` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1230 | `RegQueryInfoKeyW` | `0x47D70` | 121 | UnwindData |  |
| 1597 | `WerSetFlags` | `0x47DF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1598 | `WerSetFlagsWorker` | `0x47DF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 900 | `HeapQueryInformation` | `0x47E00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 829 | `GetThreadUILanguage` | `0x47E20` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 653 | `GetLargePageMinimum` | `0x48040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1295 | `RtlDeleteFunctionTable` | `0x48060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 755 | `GetProcessWorkingSetSizeEx` | `0x48080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1477 | `SetXStateFeaturesMask` | `0x480A0` | 11,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 282 | `CreateToolhelp32Snapshot` | `0x4ABF0` | 934 | UnwindData |  |
| 1610 | `WerpInitiateRemoteRecovery` | `0x4BAB0` | 17 | UnwindData |  |
| 619 | `GetExpandedNameA` | `0x4CD20` | 244 | UnwindData |  |
| 1404 | `SetLocalPrimaryComputerNameW` | `0x4D070` | 886 | UnwindData |  |
| 271 | `CreateSymbolicLinkW` | `0x4DFE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1243 | `RegisterApplicationRestart` | `0x4E000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 740 | `GetProcessGroupAffinity` | `0x4E020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 673 | `GetMemoryErrorHandlingCapabilities` | `0x4E040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `BasepGetPackageActivationTokenForFilePath2` | `0x4E060` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1228 | `RegOpenUserClassesRoot` | `0x4E070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1585 | `WerGetFlags` | `0x4E090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1586 | `WerGetFlagsWorker` | `0x4E090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 495 | `GetCachedSigningLevel` | `0x4E0A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 379 | `EnumSystemLocalesA` | `0x4E0C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 374 | `EnumSystemFirmwareTables` | `0x4E0E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1423 | `SetProcessPriorityBoost` | `0x4E100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1313 | `SetCachedSigningLevel` | `0x4E120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 949 | `IsNLSDefinedString` | `0x4E140` | 1,504 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1007 | `LZRead` | `0x4E720` | 646 | UnwindData |  |
| 688 | `GetNamedPipeHandleStateW` | `0x4ED00` | 2,176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 395 | `ExpandEnvironmentStringsA` | `0x4F580` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `Beep` | `0x4F7E0` | 45 | UnwindData |  |
| 1297 | `RtlInstallFunctionTableCallback` | `0x4F980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 895 | `HeapCompact` | `0x4F9A0` | 800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `BasepGetPackageActivationTokenForSxS2` | `0x4FCC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 707 | `GetNumberFormatEx` | `0x4FCE0` | 832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1303 | `RtlRestoreContext` | `0x50020` | 720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 753 | `GetProcessVersion` | `0x502F0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 680 | `GetNLSVersion` | `0x50360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1618 | `Wow64GetThreadContext` | `0x50380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1539 | `UnregisterApplicationRestart` | `0x503A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1224 | `RegNotifyChangeKeyValue` | `0x503C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1239 | `RegSetValueExW` | `0x503E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 681 | `GetNLSVersionEx` | `0x50400` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 706 | `GetNumberFormatA` | `0x504A0` | 899 | UnwindData |  |
| 905 | `HeapUnlock` | `0x50D10` | 3,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 462 | `FoldStringA` | `0x51980` | 650 | UnwindData |  |
| 975 | `K32GetDeviceDriverBaseNameA` | `0x51D90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1033 | `LocalSize` | `0x51DB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 500 | `GetCalendarInfoA` | `0x51DE0` | 595 | UnwindData |  |
| 1058 | `MoveFileWithProgressA` | `0x527B0` | 29 | UnwindData |  |
| 593 | `GetDefaultCommConfigW` | `0x527E0` | 316 | UnwindData |  |
| 1223 | `RegLoadMUIStringW` | `0x52C40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `BeginUpdateResourceW` | `0x52C60` | 633 | UnwindData |  |
| 112 | `BasepQueryModuleChpeSettings` | `0x52EE0` | 594 | UnwindData |  |
| 1382 | `SetFileBandwidthReservation` | `0x532B0` | 322 | UnwindData |  |
| 918 | `InitializeContext2` | `0x53400` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 977 | `K32GetDeviceDriverFileNameA` | `0x53670` | 2,448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 394 | `ExitVDM` | `0x54000` | 168 | UnwindData |  |
| 78 | `BaseUpdateVDMEntry` | `0x54240` | 267 | UnwindData |  |
| 276 | `CreateThreadpoolIo` | `0x54360` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `AreShortNamesEnabled` | `0x54440` | 304 | UnwindData |  |
| 175 | `CommConfigDialogW` | `0x54A90` | 329 | UnwindData |  |
| 792 | `GetSystemPreferredUILanguages` | `0x54CF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 587 | `GetDateFormatA` | `0x54D10` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1429 | `SetStdHandle` | `0x54E80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 295 | `DebugBreak` | `0x54EA0` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 270 | `CreateSymbolicLinkTransactedW` | `0x55050` | 175 | UnwindData |  |
| 1251 | `RegisterWaitUntilOOBECompleted` | `0x55110` | 388 | UnwindData |  |
| 493 | `GetCPInfoExA` | `0x553A0` | 225 | UnwindData |  |
| 44 | `BackupSeek` | `0x55490` | 497 | UnwindData |  |
| 506 | `GetComPlusPackageInstallStatus` | `0x55690` | 66 | UnwindData |  |
| 90 | `BasepCopyEncryption` | `0x557D0` | 228 | UnwindData |  |
| 336 | `DuplicateEncryptionInfoFileExt` | `0x55F10` | 237 | UnwindData |  |
| 1149 | `QueryIdleProcessorCycleTime` | `0x56250` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | `CheckNameLegalDOS8Dot3A` | `0x56270` | 173 | UnwindData |  |
| 254 | `CreatePrivateNamespaceW` | `0x56330` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 520 | `GetComputerNameExA` | `0x56350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 978 | `K32GetDeviceDriverFileNameW` | `0x56370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1250 | `RegisterWaitForSingleObjectEx` | `0x56390` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 382 | `EnumTimeFormatsA` | `0x56470` | 112 | UnwindData |  |
| 1098 | `OpenWaitableTimerA` | `0x56710` | 114 | UnwindData |  |
| 999 | `LZClose` | `0x56790` | 185 | UnwindData |  |
| 911 | `InitAtomTable` | `0x56850` | 109 | UnwindData |  |
| 377 | `EnumSystemLanguageGroupsA` | `0x568D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1211 | `RegDisablePredefinedCacheEx` | `0x568F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1590 | `WerRegisterExcludedMemoryBlock` | `0x56910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1407 | `SetLocaleInfoW` | `0x56930` | 832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1291 | `RtlCaptureContext` | `0x56C70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1300 | `RtlMoveMemory` | `0x56CA0` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `BaseFormatObjectAttributes` | `0x56E30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 857 | `GetVolumeNameForVolumeMountPointW` | `0x56E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 746 | `GetProcessInformation` | `0x56E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 820 | `GetThreadInformation` | `0x56E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1420 | `SetProcessInformation` | `0x56E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1446 | `SetThreadInformation` | `0x56E80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 754 | `GetProcessWorkingSetSize` | `0x56E90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1425 | `SetProcessWorkingSetSize` | `0x56EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `CloseHandle` | `0x56EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 337 | `DuplicateHandle` | `0x56EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 651 | `GetHandleInformation` | `0x56ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1397 | `SetHandleInformation` | `0x56EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `CancelWaitableTimer` | `0x56EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 216 | `CreateEventA` | `0x56F00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 217 | `CreateEventExA` | `0x56F10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 218 | `CreateEventExW` | `0x56F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 219 | `CreateEventW` | `0x56F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 245 | `CreateMutexA` | `0x56F40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 246 | `CreateMutexExA` | `0x56F50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 247 | `CreateMutexExW` | `0x56F60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 248 | `CreateMutexW` | `0x56F70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 266 | `CreateSemaphoreExW` | `0x56F80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 267 | `CreateSemaphoreW` | `0x56F90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 287 | `CreateWaitableTimerExW` | `0x56FA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 920 | `InitializeCriticalSectionAndSpinCount` | `0x56FB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 921 | `InitializeCriticalSectionEx` | `0x56FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1076 | `OpenEventA` | `0x56FD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1077 | `OpenEventW` | `0x56FE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1085 | `OpenMutexW` | `0x56FF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1093 | `OpenSemaphoreW` | `0x57000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1099 | `OpenWaitableTimerW` | `0x57010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1256 | `ReleaseMutex` | `0x57020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1262 | `ReleaseSemaphore` | `0x57030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1282 | `ResetEvent` | `0x57040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1374 | `SetEvent` | `0x57050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1475 | `SetWaitableTimer` | `0x57060` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1485 | `SleepEx` | `0x57070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1573 | `WaitForMultipleObjects` | `0x57080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1574 | `WaitForMultipleObjectsEx` | `0x57090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1575 | `WaitForSingleObject` | `0x570A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1576 | `WaitForSingleObjectEx` | `0x570B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 177 | `CompareFileTime` | `0x570E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 207 | `CreateDirectory2A` | `0x570F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 208 | `CreateDirectory2W` | `0x57100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 209 | `CreateDirectoryA` | `0x57110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 214 | `CreateDirectoryW` | `0x57120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `CreateFile2` | `0x57130` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 223 | `CreateFile3` | `0x57140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 224 | `CreateFileA` | `0x57150` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 232 | `CreateFileW` | `0x57160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 301 | `DefineDosDeviceW` | `0x57170` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 307 | `DeleteFile2A` | `0x57180` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 308 | `DeleteFile2W` | `0x57190` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 309 | `DeleteFileA` | `0x571A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 312 | `DeleteFileW` | `0x571B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 321 | `DeleteVolumeMountPointW` | `0x571C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 403 | `FileTimeToLocalFileTime` | `0x571D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 415 | `FindClose` | `0x571E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 416 | `FindCloseChangeNotification` | `0x571F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 417 | `FindFirstChangeNotificationA` | `0x57200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 418 | `FindFirstChangeNotificationW` | `0x57210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 419 | `FindFirstFileA` | `0x57220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 420 | `FindFirstFileExA` | `0x57230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 421 | `FindFirstFileExW` | `0x57240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 423 | `FindFirstFileNameW` | `0x57250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 426 | `FindFirstFileW` | `0x57260` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 432 | `FindFirstVolumeW` | `0x57270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 435 | `FindNextChangeNotification` | `0x57280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 436 | `FindNextFileA` | `0x57290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 437 | `FindNextFileNameW` | `0x572A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 438 | `FindNextFileW` | `0x572B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 443 | `FindNextVolumeW` | `0x572C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 450 | `FindVolumeClose` | `0x572D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 458 | `FlushFileBuffers` | `0x572E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 595 | `GetDiskFreeSpaceA` | `0x572F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 596 | `GetDiskFreeSpaceExA` | `0x57300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 597 | `GetDiskFreeSpaceExW` | `0x57310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 598 | `GetDiskFreeSpaceW` | `0x57320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 603 | `GetDriveTypeA` | `0x57330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 604 | `GetDriveTypeW` | `0x57340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 621 | `GetFileAttributesA` | `0x57350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 622 | `GetFileAttributesExA` | `0x57360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 623 | `GetFileAttributesExW` | `0x57370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 626 | `GetFileAttributesW` | `0x57380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 628 | `GetFileInformationByHandle` | `0x57390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 633 | `GetFileSize` | `0x573A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 634 | `GetFileSizeEx` | `0x573B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 635 | `GetFileTime` | `0x573C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 636 | `GetFileType` | `0x573D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 637 | `GetFinalPathNameByHandleA` | `0x573E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 638 | `GetFinalPathNameByHandleW` | `0x573F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 644 | `GetFullPathNameA` | `0x57400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 647 | `GetFullPathNameW` | `0x57410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 661 | `GetLogicalDriveStringsW` | `0x57420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 806 | `GetTempFileNameA` | `0x57430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 807 | `GetTempFileNameW` | `0x57440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 808 | `GetTempPath2A` | `0x57450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 809 | `GetTempPath2W` | `0x57460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 810 | `GetTempPathA` | `0x57470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 811 | `GetTempPathW` | `0x57480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 853 | `GetVolumeInformationA` | `0x57490` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 854 | `GetVolumeInformationByHandleW` | `0x574A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 855 | `GetVolumeInformationW` | `0x574B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 859 | `GetVolumePathNameW` | `0x574C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 861 | `GetVolumePathNamesForVolumeNameW` | `0x574D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1025 | `LocalFileTimeToFileTime` | `0x574E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1038 | `LockFile` | `0x574F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1039 | `LockFileEx` | `0x57500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1146 | `QueryDosDeviceW` | `0x57510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1195 | `ReadFile` | `0x57520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1196 | `ReadFileEx` | `0x57530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1197 | `ReadFileScatter` | `0x57540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1264 | `RemoveDirectory2A` | `0x57550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1265 | `RemoveDirectory2W` | `0x57560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1266 | `RemoveDirectoryA` | `0x57570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1269 | `RemoveDirectoryW` | `0x57580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1368 | `SetEndOfFile` | `0x57590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1378 | `SetFileAttributesA` | `0x575A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1381 | `SetFileAttributesW` | `0x575B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1384 | `SetFileInformationByHandle` | `0x575C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1386 | `SetFilePointer` | `0x575D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1387 | `SetFilePointerEx` | `0x575E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1390 | `SetFileTime` | `0x575F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1391 | `SetFileValidData` | `0x57600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1534 | `UnlockFile` | `0x57610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1535 | `UnlockFileEx` | `0x57620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1634 | `WriteFile` | `0x57630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1635 | `WriteFileEx` | `0x57640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1636 | `WriteFileGather` | `0x57650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 315 | `DeleteTimerQueue` | `0x57660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1060 | `MulDiv` | `0x57670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 364 | `EnumResourceNamesA` | `0x57680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 367 | `EnumResourceNamesW` | `0x57690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1019 | `LoadPackagedLibrary` | `0x576A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `CallNamedPipeW` | `0x576B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 797 | `GetSystemTimePreciseAsFileTime` | `0x576C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 404 | `FileTimeToSystemTime` | `0x576D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 501 | `GetCalendarInfoEx` | `0x576E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 502 | `GetCalendarInfoW` | `0x576F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 611 | `GetEnvironmentStringsA` | `0x57700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `ClearCommBreak` | `0x57710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `ClearCommError` | `0x57720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 390 | `EscapeCommFunction` | `0x57730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 507 | `GetCommConfig` | `0x57740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 508 | `GetCommMask` | `0x57750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 509 | `GetCommModemStatus` | `0x57760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 510 | `GetCommProperties` | `0x57770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 511 | `GetCommState` | `0x57780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 512 | `GetCommTimeouts` | `0x57790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1139 | `PurgeComm` | `0x577A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1317 | `SetCommBreak` | `0x577B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1318 | `SetCommConfig` | `0x577C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1319 | `SetCommMask` | `0x577D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1320 | `SetCommState` | `0x577E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1321 | `SetCommTimeouts` | `0x577F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1478 | `SetupComm` | `0x57800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1523 | `TransmitCommChar` | `0x57810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1570 | `WaitCommEvent` | `0x57820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 801 | `GetSystemWow64DirectoryA` | `0x57830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 802 | `GetSystemWow64DirectoryW` | `0x57840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1617 | `Wow64EnableWow64FsRedirection` | `0x57850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 199 | `CopyFileW` | `0x57860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 187 | `ConvertFiberToThread` | `0x57870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `ConvertThreadToFiber` | `0x57880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 191 | `ConvertThreadToFiberEx` | `0x57890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 220 | `CreateFiber` | `0x578A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 221 | `CreateFiberEx` | `0x578B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 306 | `DeleteFiber` | `0x578C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1492 | `SwitchToFiber` | `0x578D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1064 | `NlsCheckPolicy` | `0x578E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1065 | `NlsGetCacheUpdateCount` | `0x578F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1066 | `NlsUpdateLocale` | `0x57900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1067 | `NlsUpdateSystemLocale` | `0x57910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `AllocConsole` | `0x57920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `AllocConsoleWithOptions` | `0x57930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `AttachConsole` | `0x57940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 164 | `ClosePseudoConsole` | `0x57950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 261 | `CreatePseudoConsole` | `0x57960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 467 | `FreeConsole` | `0x57970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 533 | `GetConsoleCP` | `0x57980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 551 | `GetConsoleMode` | `0x57990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 555 | `GetConsoleOutputCP` | `0x579A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 710 | `GetNumberOfConsoleInputEvents` | `0x579B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1108 | `PeekConsoleInputA` | `0x579C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1109 | `PeekConsoleInputW` | `0x579D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1182 | `ReadConsoleA` | `0x579E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1183 | `ReadConsoleInputA` | `0x579F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1186 | `ReadConsoleInputW` | `0x57A00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1192 | `ReadConsoleW` | `0x57A10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1259 | `ReleasePseudoConsole` | `0x57A20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1284 | `ResizePseudoConsole` | `0x57A30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1329 | `SetConsoleCtrlHandler` | `0x57A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1345 | `SetConsoleMode` | `0x57A50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1623 | `WriteConsoleA` | `0x57A60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1633 | `WriteConsoleW` | `0x57A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | `CreateConsoleScreenBuffer` | `0x57A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 405 | `FillConsoleOutputAttribute` | `0x57A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 406 | `FillConsoleOutputCharacterA` | `0x57AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 407 | `FillConsoleOutputCharacterW` | `0x57AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 457 | `FlushConsoleInputBuffer` | `0x57AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 476 | `GenerateConsoleCtrlEvent` | `0x57AD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 539 | `GetConsoleCursorInfo` | `0x57AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 553 | `GetConsoleOriginalTitleA` | `0x57AF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 554 | `GetConsoleOriginalTitleW` | `0x57B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 557 | `GetConsoleScreenBufferInfo` | `0x57B10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 558 | `GetConsoleScreenBufferInfoEx` | `0x57B20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 560 | `GetConsoleTitleA` | `0x57B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 561 | `GetConsoleTitleW` | `0x57B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 654 | `GetLargestConsoleWindowSize` | `0x57B50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1187 | `ReadConsoleOutputA` | `0x57B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1188 | `ReadConsoleOutputAttribute` | `0x57B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1189 | `ReadConsoleOutputCharacterA` | `0x57B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1190 | `ReadConsoleOutputCharacterW` | `0x57B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1191 | `ReadConsoleOutputW` | `0x57BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1309 | `ScrollConsoleScreenBufferA` | `0x57BB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1310 | `ScrollConsoleScreenBufferW` | `0x57BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1327 | `SetConsoleActiveScreenBuffer` | `0x57BD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1328 | `SetConsoleCP` | `0x57BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1331 | `SetConsoleCursorInfo` | `0x57BF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1333 | `SetConsoleCursorPosition` | `0x57C00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1350 | `SetConsoleOutputCP` | `0x57C10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1352 | `SetConsoleScreenBufferInfoEx` | `0x57C20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1353 | `SetConsoleScreenBufferSize` | `0x57C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1354 | `SetConsoleTextAttribute` | `0x57C40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1355 | `SetConsoleTitleA` | `0x57C50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1356 | `SetConsoleTitleW` | `0x57C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1357 | `SetConsoleWindowInfo` | `0x57C70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1624 | `WriteConsoleInputA` | `0x57C80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1627 | `WriteConsoleInputW` | `0x57C90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1628 | `WriteConsoleOutputA` | `0x57CA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1629 | `WriteConsoleOutputAttribute` | `0x57CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1630 | `WriteConsoleOutputCharacterA` | `0x57CC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1631 | `WriteConsoleOutputCharacterW` | `0x57CD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1632 | `WriteConsoleOutputW` | `0x57CE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `AddConsoleAliasA` | `0x57CF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `AddConsoleAliasW` | `0x57D00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 397 | `ExpungeConsoleCommandHistoryA` | `0x57D10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 398 | `ExpungeConsoleCommandHistoryW` | `0x57D20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 523 | `GetConsoleAliasA` | `0x57D30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 524 | `GetConsoleAliasExesA` | `0x57D40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 525 | `GetConsoleAliasExesLengthA` | `0x57D50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 526 | `GetConsoleAliasExesLengthW` | `0x57D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 527 | `GetConsoleAliasExesW` | `0x57D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 528 | `GetConsoleAliasW` | `0x57D80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 529 | `GetConsoleAliasesA` | `0x57D90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 530 | `GetConsoleAliasesLengthA` | `0x57DA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 531 | `GetConsoleAliasesLengthW` | `0x57DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 532 | `GetConsoleAliasesW` | `0x57DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 535 | `GetConsoleCommandHistoryA` | `0x57DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 536 | `GetConsoleCommandHistoryLengthA` | `0x57DE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 537 | `GetConsoleCommandHistoryLengthW` | `0x57DF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 538 | `GetConsoleCommandHistoryW` | `0x57E00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 541 | `GetConsoleDisplayMode` | `0x57E10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 543 | `GetConsoleFontSize` | `0x57E20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 545 | `GetConsoleHistoryInfo` | `0x57E30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 556 | `GetConsoleProcessList` | `0x57E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 559 | `GetConsoleSelectionInfo` | `0x57E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 562 | `GetConsoleWindow` | `0x57E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 569 | `GetCurrentConsoleFont` | `0x57E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 570 | `GetCurrentConsoleFontEx` | `0x57E80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 711 | `GetNumberOfConsoleMouseButtons` | `0x57E90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1334 | `SetConsoleDisplayMode` | `0x57EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1337 | `SetConsoleHistoryInfo` | `0x57EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1347 | `SetConsoleNumberOfCommandsA` | `0x57EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1348 | `SetConsoleNumberOfCommandsW` | `0x57ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1359 | `SetCurrentConsoleFontEx` | `0x57EE0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `ActivatePackageVirtualizationContext` | `0x57FD0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 251 | `CreatePackageVirtualizationContext` | `0x58070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 292 | `DeactivatePackageVirtualizationContext` | `0x58090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 338 | `DuplicatePackageVirtualizationContext` | `0x580B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 578 | `GetCurrentPackageVirtualizationContext` | `0x580D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 756 | `GetProcessesInVirtualizationContext` | `0x580F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1258 | `ReleasePackageVirtualizationContext` | `0x58110` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1688 | `uaw_lstrlenW` | `0x58280` | 28 | UnwindData |  |
| 1689 | `uaw_wcschr` | `0x582B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1690 | `uaw_wcscpy` | `0x582E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1691 | `uaw_wcsicmp` | `0x58310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1692 | `uaw_wcslen` | `0x58330` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1693 | `uaw_wcsrchr` | `0x58360` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 950 | `IsNativeVhdBoot` | `0x583F0` | 271 | UnwindData |  |
| 200 | `CopyLZFile` | `0x58510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1001 | `LZCopy` | `0x58520` | 259 | UnwindData |  |
| 57 | `BaseDumpAppcompatCacheWorker` | `0x58630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1003 | `LZDone` | `0x58630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1531 | `UTUnRegister` | `0x58630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `BaseCleanupAppcompatCacheSupportWorker` | `0x58640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `BaseInitAppcompatCacheSupportWorker` | `0x58640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 163 | `CloseProfileUserMapping` | `0x58640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1009 | `LZStart` | `0x58640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1091 | `OpenProfileUserMapping` | `0x58640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1343 | `SetConsoleMaximumWindowSize` | `0x58640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 645 | `GetFullPathNameTransactedA` | `0x58650` | 182 | UnwindData |  |
| 1434 | `SetSystemTimeAdjustment` | `0x58710` | 69 | UnwindData |  |
| 296 | `DebugBreakProcess` | `0x58760` | 42 | UnwindData |  |
| 297 | `DebugSetProcessKillOnExit` | `0x58790` | 105 | UnwindData |  |
| 1619 | `Wow64GetThreadSelectorEntry` | `0x58800` | 106 | UnwindData |  |
| 212 | `CreateDirectoryTransactedA` | `0x58870` | 168 | UnwindData |  |
| 1267 | `RemoveDirectoryTransactedA` | `0x58920` | 75 | UnwindData |  |
| 422 | `FindFirstFileNameTransactedW` | `0x58980` | 187 | UnwindData |  |
| 424 | `FindFirstFileTransactedA` | `0x58A50` | 205 | UnwindData |  |
| 427 | `FindFirstStreamTransactedW` | `0x58B30` | 187 | UnwindData |  |
| 627 | `GetFileBandwidthReservation` | `0x58C00` | 190 | UnwindData |  |
| 1388 | `SetFileShortNameA` | `0x58CD0` | 72 | UnwindData |  |
| 1389 | `SetFileShortNameW` | `0x58D20` | 317 | UnwindData |  |
| 609 | `GetEncryptedFileVersionExt` | `0x590A0` | 237 | UnwindData |  |
| 19 | `AddSecureMemoryCacheCallback` | `0x591A0` | 42 | UnwindData |  |
| 871 | `GlobalCompact` | `0x591D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1024 | `LocalCompact` | `0x591D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1032 | `LocalShrink` | `0x591D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 875 | `GlobalFix` | `0x591F0` | 28 | UnwindData |  |
| 887 | `GlobalUnfix` | `0x59220` | 28 | UnwindData |  |
| 1252 | `RegisterWowBaseHandlers` | `0x59250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1273 | `RemoveSecureMemoryCacheCallback` | `0x59260` | 25 | UnwindData |  |
| 1022 | `LoadStringBaseW` | `0x59280` | 29 | UnwindData |  |
| 360 | `EnumResourceLanguagesA` | `0x592B0` | 47 | UnwindData |  |
| 368 | `EnumResourceTypesA` | `0x592F0` | 33 | UnwindData |  |
| 371 | `EnumResourceTypesW` | `0x59320` | 33 | UnwindData |  |
| 601 | `GetDllDirectoryA` | `0x59350` | 393 | UnwindData |  |
| 1530 | `UTRegister` | `0x594F0` | 135 | UnwindData |  |
| 1410 | `SetNamedPipeAttribute` | `0x59580` | 528 | UnwindData |  |
| 695 | `GetNumaAvailableMemoryNode` | `0x597A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 698 | `GetNumaNodeNumberFromHandle` | `0x597B0` | 99 | UnwindData |  |
| 704 | `GetNumaProximityNode` | `0x59820` | 59 | UnwindData |  |
| 86 | `BasepCheckPplSupport` | `0x59870` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `BasepFinishPackageActivation` | `0x598B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `BasepGetPackageActivationTokenForFilePath` | `0x598C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `BasepGetPackageActivationTokenForSxS` | `0x598C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `BasepProcessInvalidImage` | `0x598D0` | 1,821 | UnwindData |  |
| 114 | `BasepReleasePackagedAppInfo` | `0x5A000` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 737 | `GetProcessDEPPolicy` | `0x5A1F0` | 76 | UnwindData |  |
| 781 | `GetSystemDEPPolicy` | `0x5A250` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 793 | `GetSystemRegistryQuota` | `0x5A290` | 134 | UnwindData |  |
| 935 | `IsBadHugeReadPtr` | `0x5A320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 936 | `IsBadHugeWritePtr` | `0x5A330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1071 | `NtVdm64CreateProcessInternalW` | `0x5A340` | 513 | UnwindData |  |
| 1180 | `RaiseInvalid16BitExeError` | `0x5A550` | 278 | UnwindData |  |
| 1415 | `SetProcessDEPPolicy` | `0x5A670` | 51 | UnwindData |  |
| 1279 | `ReplacePartitionUnit` | `0x5A6B0` | 125 | UnwindData |  |
| 14 | `AddRefActCtx` | `0x5A740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `AddResourceAttributeAce` | `0x5A760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `AddScopedPolicyIDAce` | `0x5A780` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `AllocateUserPhysicalPagesNuma` | `0x5A7A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `AllocateUserPhysicalPages` | `0x5A7C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `BaseCheckAppcompatCacheEx` | `0x5A7E0` | 85 | UnwindData |  |
| 47 | `BaseCheckAppcompatCache` | `0x5A840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `BaseCleanupAppcompatCacheSupport` | `0x5A860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `BaseDumpAppcompatCache` | `0x5A880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `BaseFlushAppcompatCache` | `0x5A8A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `BaseInitAppcompatCacheSupport` | `0x5A8C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `BaseUpdateAppcompatCache` | `0x5A8E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `CancelSynchronousIo` | `0x5A900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `CheckAllowDecryptedRemoteDestinationPolicy` | `0x5A920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `CheckTokenCapability` | `0x5A940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `CheckTokenMembershipEx` | `0x5A960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 192 | `CopyContext` | `0x5A980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 193 | `CopyFile2` | `0x5A9A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 211 | `CreateDirectoryExW` | `0x5A9C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 228 | `CreateFileMappingNumaW` | `0x5A9E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 233 | `CreateHardLinkA` | `0x5AA00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 256 | `CreateProcessAsUserA` | `0x5AA20` | 107 | UnwindData |  |
| 258 | `CreateProcessInternalA` | `0x5AAA0` | 119 | UnwindData |  |
| 259 | `CreateProcessInternalW` | `0x5AB20` | 119 | UnwindData |  |
| 294 | `DebugActiveProcessStop` | `0x5ABA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 293 | `DebugActiveProcess` | `0x5ABC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 302 | `DelayLoadFailureHook` | `0x5ABE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 314 | `DeleteSynchronizationBarrier` | `0x5AC00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 330 | `DnsHostnameToComputerNameExW` | `0x5AC20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 339 | `EnableProcessOptionalXStateFeatures` | `0x5AC40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 346 | `EnterSynchronizationBarrier` | `0x5AC60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 351 | `EnumCalendarInfoExW` | `0x5AC80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 352 | `EnumCalendarInfoW` | `0x5ACA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 356 | `EnumDateFormatsExW` | `0x5ACC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 357 | `EnumDateFormatsW` | `0x5ACE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 359 | `EnumLanguageGroupLocalesW` | `0x5AD00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 361 | `EnumResourceLanguagesExA` | `0x5AD20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 365 | `EnumResourceNamesExA` | `0x5AD40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 366 | `EnumResourceNamesExW` | `0x5AD60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 369 | `EnumResourceTypesExA` | `0x5AD80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 370 | `EnumResourceTypesExW` | `0x5ADA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 373 | `EnumSystemCodePagesW` | `0x5ADC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 378 | `EnumSystemLanguageGroupsW` | `0x5ADE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 381 | `EnumSystemLocalesW` | `0x5AE00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 384 | `EnumTimeFormatsW` | `0x5AE20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 386 | `EnumUILanguagesW` | `0x5AE40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 399 | `FatalAppExitA` | `0x5AE60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 400 | `FatalAppExitW` | `0x5AE80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 433 | `FindNLSString` | `0x5AEA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 468 | `FreeEnvironmentStringsA` | `0x5AEC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 475 | `FreeUserPhysicalPages` | `0x5AEE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 480 | `GetAppContainerAce` | `0x5AF00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 481 | `GetAppContainerNamedObjectPath` | `0x5AF20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 482 | `GetApplicationRecoveryCallback` | `0x5AF40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 484 | `GetApplicationRestartSettings` | `0x5AF60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 515 | `GetCompressedFileSizeA` | `0x5AF80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 564 | `GetCurrencyFormatEx` | `0x5AFA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 565 | `GetCurrencyFormatW` | `0x5AFC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 606 | `GetDurationFormatEx` | `0x5AFD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 610 | `GetEnvironmentStrings` | `0x5AFF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 615 | `GetEraNameCountedString` | `0x5B010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 630 | `GetFileInformationByName` | `0x5B030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 631 | `GetFileMUIInfo` | `0x5B050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 682 | `GetNamedPipeAttribute` | `0x5B070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 684 | `GetNamedPipeClientComputerNameW` | `0x5B090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 701 | `GetNumaNodeProcessorMaskEx` | `0x5B0B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 705 | `GetNumaProximityNodeEx` | `0x5B0D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 743 | `GetProcessHeaps` | `0x5B0F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 749 | `GetProcessPreferredUILanguages` | `0x5B110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 750 | `GetProcessPriorityBoost` | `0x5B130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 751 | `GetProcessShutdownParameters` | `0x5B150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 774 | `GetStringScripts` | `0x5B170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 788 | `GetSystemFileCacheSize` | `0x5B190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 814 | `GetThreadEnabledXStateFeatures` | `0x5B1B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 832 | `GetTimeFormatA` | `0x5B1D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 838 | `GetTimeZoneInformationForYear` | `0x5B1F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 839 | `GetUILanguageInfo` | `0x5B210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 865 | `GetXStateFeaturesMask` | `0x5B230` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 904 | `HeapSummary` | `0x5B250` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 909 | `IdnToNameprepUnicode` | `0x5B270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 910 | `IdnToUnicode` | `0x5B290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 926 | `InitializeSynchronizationBarrier` | `0x5B2B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 961 | `IsValidLanguageGroup` | `0x5B2D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 963 | `IsValidLocaleName` | `0x5B2F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 964 | `IsValidNLSVersion` | `0x5B310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 969 | `K32EnumDeviceDrivers` | `0x5B330` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 970 | `K32EnumPageFilesA` | `0x5B350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 971 | `K32EnumPageFilesW` | `0x5B370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 979 | `K32GetMappedFileNameA` | `0x5B390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 991 | `K32GetWsChangesEx` | `0x5B3B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 990 | `K32GetWsChanges` | `0x5B3D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 992 | `K32InitializeProcessForWsWatch` | `0x5B3F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1021 | `LoadStringBaseExW` | `0x5B410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1027 | `LocalFlags` | `0x5B430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1030 | `LocalLock` | `0x5B450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1035 | `LocalUnlock` | `0x5B470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1042 | `MapUserPhysicalPages` | `0x5B490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1046 | `MapViewOfFileExNuma` | `0x5B4B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1059 | `MoveFileWithProgressW` | `0x5B4D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1062 | `NeedCurrentDirectoryForExePathA` | `0x5B4F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1063 | `NeedCurrentDirectoryForExePathW` | `0x5B510` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1069 | `NotifyMountMgr` | `0x5B530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1075 | `OpenConsoleWStub` | `0x5B550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1125 | `PssCaptureSnapshot` | `0x5B560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1126 | `PssDuplicateSnapshot` | `0x5B580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1127 | `PssFreeSnapshot` | `0x5B5A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1128 | `PssQuerySnapshot` | `0x5B5C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1129 | `PssWalkMarkerCreate` | `0x5B5E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1130 | `PssWalkMarkerFree` | `0x5B600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1131 | `PssWalkMarkerGetPosition` | `0x5B620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1136 | `PssWalkMarkerTell` | `0x5B620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1132 | `PssWalkMarkerRewind` | `0x5B640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1134 | `PssWalkMarkerSeekToBeginning` | `0x5B640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1133 | `PssWalkMarkerSeek` | `0x5B660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1135 | `PssWalkMarkerSetPosition` | `0x5B660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1140 | `QueryActCtxSettingsW` | `0x5B680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1150 | `QueryIdleProcessorCycleTimeEx` | `0x5B6A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1157 | `QueryProcessAffinityUpdateMode` | `0x5B6C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1162 | `QueryThreadpoolStackInformation` | `0x5B6E0` | 54 | UnwindData |  |
| 1202 | `RegCopyTreeW` | `0x5B720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1203 | `RegCreateKeyExA` | `0x5B740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1205 | `RegDeleteKeyExA` | `0x5B760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1206 | `RegDeleteKeyExW` | `0x5B780` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1207 | `RegDeleteTreeA` | `0x5B7A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1208 | `RegDeleteTreeW` | `0x5B7C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1209 | `RegDeleteValueA` | `0x5B7E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1210 | `RegDeleteValueW` | `0x5B800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1214 | `RegEnumValueA` | `0x5B820` | 67 | UnwindData |  |
| 1215 | `RegEnumValueW` | `0x5B870` | 67 | UnwindData |  |
| 1216 | `RegFlushKey` | `0x5B8C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1217 | `RegGetKeySecurity` | `0x5B8E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1218 | `RegGetValueA` | `0x5B900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1220 | `RegLoadKeyA` | `0x5B920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1221 | `RegLoadKeyW` | `0x5B940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1222 | `RegLoadMUIStringA` | `0x5B960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1229 | `RegQueryInfoKeyA` | `0x5B980` | 121 | UnwindData |  |
| 1233 | `RegRestoreKeyA` | `0x5BA00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1234 | `RegRestoreKeyW` | `0x5BA20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1235 | `RegSaveKeyExA` | `0x5BA40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1236 | `RegSaveKeyExW` | `0x5BA60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1237 | `RegSetKeySecurity` | `0x5BA80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1238 | `RegSetValueExA` | `0x5BAA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1240 | `RegUnLoadKeyA` | `0x5BAC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1241 | `RegUnLoadKeyW` | `0x5BAE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1244 | `RegisterBadMemoryNotification` | `0x5BB00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1294 | `RtlCopyMemory` | `0x5BB20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1302 | `RtlRaiseException` | `0x5BB30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1307 | `RtlVirtualUnwind2` | `0x5BB50` | 132 | UnwindData |  |
| 1311 | `SearchPathA` | `0x5BBE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1315 | `SetCalendarInfoW` | `0x5BC00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1322 | `SetComputerNameA` | `0x5BC20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1323 | `SetComputerNameEx2W` | `0x5BC40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1324 | `SetComputerNameExA` | `0x5BC60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1325 | `SetComputerNameExW` | `0x5BC80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1326 | `SetComputerNameW` | `0x5BCA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1360 | `SetCurrentDirectoryA` | `0x5BCC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1367 | `SetDynamicTimeZoneInformation` | `0x5BCE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1370 | `SetEnvironmentStringsW` | `0x5BD00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1376 | `SetFileApisToANSI` | `0x5BD20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1377 | `SetFileApisToOEM` | `0x5BD40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1385 | `SetFileIoOverlappedRange` | `0x5BD60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1405 | `SetLocalTime` | `0x5BD80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1414 | `SetProcessAffinityUpdateMode` | `0x5BDA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1422 | `SetProcessPreferredUILanguages` | `0x5BDC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1426 | `SetProcessWorkingSetSizeEx` | `0x5BDE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1430 | `SetStdHandleEx` | `0x5BE00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1431 | `SetSystemFileCacheSize` | `0x5BE20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1433 | `SetSystemTime` | `0x5BE40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1456 | `SetThreadpoolStackInformation` | `0x5BE60` | 54 | UnwindData |  |
| 1463 | `SetTimeZoneInformation` | `0x5BEA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1474 | `SetVolumeMountPointWStub` | `0x5BEC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1533 | `UnhandledExceptionFilter` | `0x5BED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1540 | `UnregisterBadMemoryNotification` | `0x5BEF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1551 | `VerLanguageNameA` | `0x5BF10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1555 | `VerifyScripts` | `0x5BF30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1587 | `WerRegisterAdditionalProcess` | `0x5BF50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1588 | `WerRegisterAppLocalDump` | `0x5BF70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1599 | `WerUnregisterAdditionalProcess` | `0x5BF90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1600 | `WerUnregisterAppLocalDump` | `0x5BFB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1601 | `WerUnregisterCustomMetadata` | `0x5BFD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1602 | `WerUnregisterExcludedMemoryBlock` | `0x5BFF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1621 | `Wow64SetThreadContext` | `0x5C010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1622 | `Wow64SuspendThread` | `0x5C030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1649 | `ZombifyActCtx` | `0x5C050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `CheckForReadOnlyResourceFilter` | `0x5C070` | 79 | UnwindData |  |
| 1521 | `Toolhelp32ReadProcessMemory` | `0x5C0D0` | 132 | UnwindData |  |
| 620 | `GetExpandedNameW` | `0x5C200` | 285 | UnwindData |  |
| 1000 | `LZCloseFile` | `0x5C330` | 205 | UnwindData |  |
| 1002 | `LZCreateFileW` | `0x5C410` | 316 | UnwindData |  |
| 1004 | `LZInit` | `0x5C560` | 479 | UnwindData |  |
| 1005 | `LZOpenFileA` | `0x5C750` | 219 | UnwindData |  |
| 1006 | `LZOpenFileW` | `0x5C840` | 181 | UnwindData |  |
| 1008 | `LZSeek` | `0x5C900` | 204 | UnwindData |  |
| 174 | `CommConfigDialogA` | `0x5C9E0` | 144 | UnwindData |  |
| 592 | `GetDefaultCommConfigA` | `0x5CA80` | 144 | UnwindData |  |
| 1362 | `SetDefaultCommConfigA` | `0x5CBB0` | 144 | UnwindData |  |
| 1363 | `SetDefaultCommConfigW` | `0x5CC50` | 329 | UnwindData |  |
| 54 | `BaseDestroyVDMEnvironment` | `0x5E980` | 61 | UnwindData |  |
| 666 | `GetLongPathNameTransactedA` | `0x5EC90` | 168 | UnwindData |  |
| 694 | `GetNextVDMCommand` | `0x5ED40` | 2,402 | UnwindData |  |
| 849 | `GetVDMCurrentDirectories` | `0x5F6B0` | 384 | UnwindData |  |
| 1253 | `RegisterWowExec` | `0x5FC50` | 118 | UnwindData |  |
| 1469 | `SetVDMCurrentDirectories` | `0x5FCD0` | 316 | UnwindData |  |
| 1550 | `VDMOperationStarted` | `0x5FF70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 283 | `CreateUmsCompletionList` | `0x5FF90` | 29 | UnwindData |  |
| 284 | `CreateUmsThreadContext` | `0x5FF90` | 29 | UnwindData |  |
| 318 | `DeleteUmsCompletionList` | `0x5FF90` | 29 | UnwindData |  |
| 319 | `DeleteUmsThreadContext` | `0x5FF90` | 29 | UnwindData |  |
| 322 | `DequeueUmsCompletionListItems` | `0x5FF90` | 29 | UnwindData |  |
| 347 | `EnterUmsSchedulingMode` | `0x5FF90` | 29 | UnwindData |  |
| 586 | `GetCurrentUmsThread` | `0x5FF90` | 29 | UnwindData |  |
| 693 | `GetNextUmsListItem` | `0x5FF90` | 29 | UnwindData |  |
| 840 | `GetUmsCompletionListEvent` | `0x5FF90` | 29 | UnwindData |  |
| 841 | `GetUmsSystemThreadInformation` | `0x5FF90` | 29 | UnwindData |  |
| 1163 | `QueryUmsThreadInformation` | `0x5FF90` | 29 | UnwindData |  |
| 1465 | `SetUmsThreadInformation` | `0x5FF90` | 29 | UnwindData |  |
| 391 | `ExecuteUmsThread` | `0x5FFC0` | 29 | UnwindData |  |
| 1532 | `UmsThreadYield` | `0x5FFC0` | 29 | UnwindData |  |
| 122 | `BuildCommDCBA` | `0x60000` | 90 | UnwindData |  |
| 123 | `BuildCommDCBAndTimeoutsA` | `0x60060` | 43 | UnwindData |  |
| 124 | `BuildCommDCBAndTimeoutsW` | `0x600A0` | 140 | UnwindData |  |
| 125 | `BuildCommDCBW` | `0x60140` | 126 | UnwindData |  |
| 272 | `CreateTapePartition` | `0x60F30` | 83 | UnwindData |  |
| 389 | `EraseTape` | `0x60F90` | 53 | UnwindData |  |
| 804 | `GetTapePosition` | `0x60FD0` | 135 | UnwindData |  |
| 805 | `GetTapeStatus` | `0x61060` | 37 | UnwindData |  |
| 1117 | `PrepareTape` | `0x61090` | 53 | UnwindData |  |
| 1435 | `SetTapeParameters` | `0x610D0` | 66 | UnwindData |  |
| 1436 | `SetTapePosition` | `0x61120` | 119 | UnwindData |  |
| 1648 | `WriteTapemark` | `0x611A0` | 89 | UnwindData |  |
| 234 | `CreateHardLinkTransactedA` | `0x61200` | 171 | UnwindData |  |
| 103 | `BasepGetPackageActivationTokenForSxS3` | `0x612C0` | 656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1650 | `ZombifyActCtxWorker` | `0x61550` | 42 | UnwindData |  |
| 1316 | `SetComPlusPackageInstallStatus` | `0x61DF0` | 76 | UnwindData |  |
| 36 | `ApplicationRecoveryFinished` | `0x61E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `ApplicationRecoveryInProgress` | `0x61E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 483 | `GetApplicationRecoveryCallbackWorker` | `0x61E70` | 173 | UnwindData |  |
| 485 | `GetApplicationRestartSettingsWorker` | `0x61F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1538 | `UnregisterApplicationRecoveryCallback` | `0x61F40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1592 | `WerRegisterFileWorker` | `0x61F60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1594 | `WerRegisterMemoryBlockWorker` | `0x61F70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1596 | `WerRegisterRuntimeExceptionModuleWorker` | `0x61F80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1604 | `WerUnregisterFileWorker` | `0x61F90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1606 | `WerUnregisterMemoryBlockWorker` | `0x61FA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1608 | `WerUnregisterRuntimeExceptionModuleWorker` | `0x61FB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1043 | `MapUserPhysicalPagesScatter` | `0x61FC0` | 42 | UnwindData |  |
| 142 | `CancelTimerQueueTimer` | `0x61FF0` | 34 | UnwindData |  |
| 1464 | `SetTimerQueueTimer` | `0x62020` | 83 | UnwindData |  |
| 116 | `BasepReportFault` | `0x62080` | 43 | UnwindData |  |
| 325 | `DisableThreadProfiling` | `0x620C0` | 46 | UnwindData |  |
| 340 | `EnableThreadProfiling` | `0x62100` | 46 | UnwindData |  |
| 1161 | `QueryThreadProfiling` | `0x62140` | 46 | UnwindData |  |
| 1199 | `ReadThreadProfilingData` | `0x62180` | 46 | UnwindData |  |
| 119 | `BeginUpdateResourceA` | `0x635D0` | 101 | UnwindData |  |
| 343 | `EndUpdateResourceA` | `0x63640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 344 | `EndUpdateResourceW` | `0x63650` | 623 | UnwindData |  |
| 1547 | `UpdateResourceA` | `0x638D0` | 385 | UnwindData |  |
| 1548 | `UpdateResourceW` | `0x63A60` | 627 | UnwindData |  |
| 176 | `CompareCalendarDates` | `0x63CE0` | 163 | UnwindData |  |
| 185 | `ConvertCalDateTimeToSystemTime` | `0x63D90` | 441 | UnwindData |  |
| 499 | `GetCalendarDifferenceInDays` | `0x640A0` | 450 | UnwindData |  |
| 505 | `GetCalendarWeekNumber` | `0x64270` | 243 | UnwindData |  |
| 941 | `IsCalendarLeapDay` | `0x64550` | 393 | UnwindData |  |
| 942 | `IsCalendarLeapMonth` | `0x646E0` | 270 | UnwindData |  |
| 943 | `IsCalendarLeapYear` | `0x64800` | 236 | UnwindData |  |
| 348 | `EnumCalendarInfoA` | `0x64900` | 146 | UnwindData |  |
| 349 | `EnumCalendarInfoExA` | `0x649A0` | 150 | UnwindData |  |
| 353 | `EnumDateFormatsA` | `0x64A40` | 90 | UnwindData |  |
| 354 | `EnumDateFormatsExA` | `0x64AA0` | 94 | UnwindData |  |
| 358 | `EnumLanguageGroupLocalesA` | `0x64B10` | 27 | UnwindData |  |
| 372 | `EnumSystemCodePagesA` | `0x64B40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 385 | `EnumUILanguagesA` | `0x64B60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 563 | `GetCurrencyFormatA` | `0x64B80` | 1,018 | UnwindData |  |
| 1314 | `SetCalendarInfoA` | `0x64F80` | 226 | UnwindData |  |
| 1406 | `SetLocaleInfoA` | `0x65070` | 242 | UnwindData |  |
| 605 | `GetDurationFormat` | `0x652E0` | 132 | UnwindData |  |
| 376 | `EnumSystemGeoNames` | `0x68360` | 294 | UnwindData |  |
| 649 | `GetGeoInfoEx` | `0x68490` | 106 | UnwindData |  |
| 1467 | `SetUserGeoID` | `0x68500` | 21 | UnwindData |  |
| 1468 | `SetUserGeoName` | `0x68520` | 134 | UnwindData |  |
| 62 | `BaseFormatTimeOut` | `0x695A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `BasepAnsiStringToDynamicUnicodeString` | `0x695D0` | 114 | UnwindData |  |
| 81 | `BasepAllocateActivationContextActivationBlock` | `0x69650` | 387 | UnwindData |  |
| 93 | `BasepFreeActivationContextActivationBlock` | `0x697E0` | 76 | UnwindData |  |
| 487 | `GetAtomNameA` | `0x699F0` | 31 | UnwindData |  |
| 867 | `GlobalAddAtomExA` | `0x69A20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 878 | `GlobalGetAtomNameA` | `0x69A40` | 31 | UnwindData |  |
| 12 | `AddLocalAlternateComputerNameA` | `0x69A70` | 82 | UnwindData |  |
| 13 | `AddLocalAlternateComputerNameW` | `0x69AD0` | 310 | UnwindData |  |
| 329 | `DnsHostnameToComputerNameA` | `0x6A7E0` | 249 | UnwindData |  |
| 387 | `EnumerateLocalComputerNamesA` | `0x6A8E0` | 280 | UnwindData |  |
| 388 | `EnumerateLocalComputerNamesW` | `0x6AA00` | 510 | UnwindData |  |
| 1271 | `RemoveLocalAlternateComputerNameA` | `0x6AC10` | 82 | UnwindData |  |
| 1272 | `RemoveLocalAlternateComputerNameW` | `0x6AC70` | 330 | UnwindData |  |
| 1403 | `SetLocalPrimaryComputerNameA` | `0x6ADC0` | 82 | UnwindData |  |
| 239 | `CreateJobObjectA` | `0x6B3A0` | 100 | UnwindData |  |
| 241 | `CreateJobSet` | `0x6B410` | 42 | UnwindData |  |
| 473 | `FreeMemoryJobObject` | `0x6B440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1082 | `OpenJobObjectA` | `0x6B450` | 114 | UnwindData |  |
| 1152 | `QueryIoRateControlInformationJobObject` | `0x6B4D0` | 270 | UnwindData |  |
| 1399 | `SetIoRateControlInformationJobObject` | `0x6B730` | 514 | UnwindData |  |
| 45 | `BackupWrite` | `0x6BD60` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `BackupWriteEx` | `0x6BEF0` | 817 | UnwindData |  |
| 71 | `BaseMarkProcessTokenForInstallers` | `0x6CAB0` | 287 | UnwindData |  |
| 79 | `BaseWriteErrorElevationRequiredEvent` | `0x6CCE0` | 96 | UnwindData |  |
| 728 | `GetPrivateProfileSectionNamesA` | `0x6D000` | 34 | UnwindData |  |
| 734 | `GetPrivateProfileStructW` | `0x6D030` | 407 | UnwindData |  |
| 761 | `GetProfileSectionA` | `0x6D1D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 764 | `GetProfileStringW` | `0x6D1E0` | 29 | UnwindData |  |
| 1637 | `WritePrivateProfileSectionA` | `0x6D210` | 93 | UnwindData |  |
| 1638 | `WritePrivateProfileSectionW` | `0x6D280` | 93 | UnwindData |  |
| 1641 | `WritePrivateProfileStructA` | `0x6D2F0` | 348 | UnwindData |  |
| 1644 | `WriteProfileSectionA` | `0x6D460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1645 | `WriteProfileSectionW` | `0x6D470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1646 | `WriteProfileStringA` | `0x6D480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `BaseIsDosApplication` | `0x6D490` | 269 | UnwindData |  |
| 489 | `GetBinaryType` | `0x6D5B0` | 75 | UnwindData |  |
| 490 | `GetBinaryTypeA` | `0x6D5B0` | 75 | UnwindData |  |
| 667 | `GetLongPathNameTransactedW` | `0x6D610` | 168 | UnwindData |  |
| 683 | `GetNamedPipeClientComputerNameA` | `0x6D6C0` | 310 | UnwindData |  |
| 149 | `CheckForReadOnlyResource` | `0x6D800` | 477 | UnwindData |  |
| 204 | `CreateBoundaryDescriptorA` | `0x6D9F0` | 101 | UnwindData |  |
| 253 | `CreatePrivateNamespaceA` | `0x6DA60` | 118 | UnwindData |  |
| 1087 | `OpenPrivateNamespaceA` | `0x6DAE0` | 100 | UnwindData |  |
| 194 | `CopyFileA` | `0x6DB50` | 170 | UnwindData |  |
| 195 | `CopyFileExA` | `0x6DC00` | 190 | UnwindData |  |
| 197 | `CopyFileTransactedA` | `0x6DCD0` | 196 | UnwindData |  |
| 198 | `CopyFileTransactedW` | `0x6DDA0` | 217 | UnwindData |  |
| 230 | `CreateFileTransactedA` | `0x6DE80` | 185 | UnwindData |  |
| 1277 | `ReplaceFileA` | `0x6DF40` | 306 | UnwindData |  |
| 210 | `CreateDirectoryExA` | `0x6E080` | 151 | UnwindData |  |
| 213 | `CreateDirectoryTransactedW` | `0x6E120` | 200 | UnwindData |  |
| 1268 | `RemoveDirectoryTransactedW` | `0x6E1F0` | 156 | UnwindData |  |
| 227 | `CreateFileMappingNumaA` | `0x6E2A0` | 189 | UnwindData |  |
| 268 | `CreateSymbolicLinkA` | `0x6E540` | 190 | UnwindData |  |
| 269 | `CreateSymbolicLinkTransactedA` | `0x6E610` | 198 | UnwindData |  |
| 310 | `DeleteFileTransactedA` | `0x6E6E0` | 75 | UnwindData |  |
| 311 | `DeleteFileTransactedW` | `0x6E740` | 142 | UnwindData |  |
| 516 | `GetCompressedFileSizeTransactedA` | `0x6E7E0` | 95 | UnwindData |  |
| 517 | `GetCompressedFileSizeTransactedW` | `0x6E850` | 161 | UnwindData |  |
| 624 | `GetFileAttributesTransactedA` | `0x6E900` | 103 | UnwindData |  |
| 625 | `GetFileAttributesTransactedW` | `0x6E970` | 189 | UnwindData |  |
| 1052 | `MoveFileA` | `0x6EA40` | 35 | UnwindData |  |
| 1055 | `MoveFileTransactedA` | `0x6EA70` | 188 | UnwindData |  |
| 1056 | `MoveFileTransactedW` | `0x6EB40` | 195 | UnwindData |  |
| 1119 | `PrivMoveFileIdentityW` | `0x6EC10` | 1,232 | UnwindData |  |
| 1379 | `SetFileAttributesTransactedA` | `0x6F0F0` | 88 | UnwindData |  |
| 1380 | `SetFileAttributesTransactedW` | `0x6F150` | 158 | UnwindData |  |
| 891 | `Heap32ListFirst` | `0x6F200` | 242 | UnwindData |  |
| 300 | `DefineDosDeviceA` | `0x6F300` | 158 | UnwindData |  |
| 320 | `DeleteVolumeMountPointA` | `0x6F3B0` | 76 | UnwindData |  |
| 430 | `FindFirstVolumeMountPointA` | `0x6F410` | 418 | UnwindData |  |
| 441 | `FindNextVolumeMountPointA` | `0x6F5C0` | 348 | UnwindData |  |
| 442 | `FindNextVolumeMountPointW` | `0x6F730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 451 | `FindVolumeMountPointClose` | `0x6F740` | 109 | UnwindData |  |
| 856 | `GetVolumeNameForVolumeMountPointA` | `0x6F7C0` | 405 | UnwindData |  |
| 1472 | `SetVolumeMountPointA` | `0x6FB70` | 129 | UnwindData |  |
| 1473 | `SetVolumeMountPointW` | `0x6FC00` | 1,399 | UnwindData |  |
| 333 | `DosPathToSessionPathA` | `0x703D0` | 479 | UnwindData |  |
| 334 | `DosPathToSessionPathW` | `0x705C0` | 398 | UnwindData |  |
| 410 | `FindActCtxSectionStringA` | `0x70760` | 153 | UnwindData |  |
| 425 | `FindFirstFileTransactedW` | `0x70800` | 205 | UnwindData |  |
| 1365 | `SetDllDirectoryA` | `0x708E0` | 173 | UnwindData |  |
| 1615 | `WinExec` | `0x709A0` | 521 | UnwindData |  |
| 1432 | `SetSystemPowerState` | `0x70BB0` | 74 | UnwindData |  |
| 639 | `GetFirmwareEnvironmentVariableA` | `0x70C00` | 21 | UnwindData |  |
| 640 | `GetFirmwareEnvironmentVariableExA` | `0x70C20` | 306 | UnwindData |  |
| 1392 | `SetFirmwareEnvironmentVariableA` | `0x70D60` | 23 | UnwindData |  |
| 1393 | `SetFirmwareEnvironmentVariableExA` | `0x70D80` | 304 | UnwindData |  |
| 1394 | `SetFirmwareEnvironmentVariableExW` | `0x70EC0` | 233 | UnwindData |  |
| 1395 | `SetFirmwareEnvironmentVariableW` | `0x70FB0` | 23 | UnwindData |  |
| 646 | `GetFullPathNameTransactedW` | `0x70FD0` | 196 | UnwindData |  |
| 1470 | `SetVolumeLabelA` | `0x710A0` | 161 | UnwindData |  |
| 1471 | `SetVolumeLabelW` | `0x71150` | 975 | UnwindData |  |
| 696 | `GetNumaAvailableMemoryNodeEx` | `0x71530` | 150 | UnwindData |  |
| 699 | `GetNumaNodeProcessorMask` | `0x715D0` | 118 | UnwindData |  |
| 803 | `GetTapeParameters` | `0x71650` | 88 | UnwindData |  |
| 827 | `GetThreadSelectorEntry` | `0x716B0` | 22 | UnwindData |  |
| 1544 | `UnregisterWaitUntilOOBECompleted` | `0x71700` | 104 | UnwindData |  |
| 1369 | `SetEnvironmentStringsA` | `0x71770` | 235 | UnwindData |  |
| 1510 | `TermsrvRestoreKey` | `0x72920` | 1,440 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1657 | `_lcreat` | `0x72EC0` | 92 | UnwindData |  |
| 1660 | `_lopen` | `0x72F30` | 111 | UnwindData |  |
| 158 | `CloseConsoleHandle` | `0x72FB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 335 | `DuplicateConsoleHandle` | `0x72FD0` | 74 | UnwindData |  |
| 548 | `GetConsoleInputWaitHandle` | `0x73020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1074 | `OpenConsoleW` | `0x73040` | 78 | UnwindData |  |
| 183 | `ConsoleMenuControl` | `0x730A0` | 138 | UnwindData |  |
| 544 | `GetConsoleHardwareState` | `0x73130` | 143 | UnwindData |  |
| 1247 | `RegisterConsoleVDM` | `0x731D0` | 213 | UnwindData |  |
| 1330 | `SetConsoleCursor` | `0x732B0` | 124 | UnwindData |  |
| 1336 | `SetConsoleHardwareState` | `0x73340` | 138 | UnwindData |  |
| 1341 | `SetConsoleKeyShortcuts` | `0x733D0` | 203 | UnwindData |  |
| 1344 | `SetConsoleMenuClose` | `0x734B0` | 108 | UnwindData |  |
| 1351 | `SetConsolePalette` | `0x73530` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1479 | `ShowConsoleCursor` | `0x735D0` | 88 | UnwindData |  |
| 1625 | `WriteConsoleInputVDMA` | `0x73630` | 187 | UnwindData |  |
| 1626 | `WriteConsoleInputVDMW` | `0x73700` | 198 | UnwindData |  |
| 534 | `GetConsoleCharType` | `0x737D0` | 140 | UnwindData |  |
| 540 | `GetConsoleCursorMode` | `0x73870` | 145 | UnwindData |  |
| 552 | `GetConsoleNlsMode` | `0x73910` | 125 | UnwindData |  |
| 1245 | `RegisterConsoleIME` | `0x739A0` | 29 | UnwindData |  |
| 1541 | `UnregisterConsoleIME` | `0x739A0` | 29 | UnwindData |  |
| 1246 | `RegisterConsoleOS2` | `0x739D0` | 108 | UnwindData |  |
| 1332 | `SetConsoleCursorMode` | `0x73A50` | 144 | UnwindData |  |
| 1342 | `SetConsoleLocalEUDC` | `0x73AF0` | 240 | UnwindData |  |
| 1346 | `SetConsoleNlsMode` | `0x73BF0` | 122 | UnwindData |  |
| 1349 | `SetConsoleOS2OemFormat` | `0x73C70` | 108 | UnwindData |  |
| 542 | `GetConsoleFontInfo` | `0x73CF0` | 230 | UnwindData |  |
| 549 | `GetConsoleKeyboardLayoutNameA` | `0x73DE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 550 | `GetConsoleKeyboardLayoutNameW` | `0x73E00` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 709 | `GetNumberOfConsoleFonts` | `0x73F10` | 96 | UnwindData |  |
| 1335 | `SetConsoleFont` | `0x73F80` | 122 | UnwindData |  |
| 1338 | `SetConsoleIcon` | `0x74000` | 108 | UnwindData |  |
| 933 | `InvalidateConsoleDIBits` | `0x74080` | 127 | UnwindData |  |
| 1549 | `VDMConsoleOperation` | `0x74110` | 212 | UnwindData |  |
| 1609 | `WerpGetDebugger` | `0x75C70` | 1,350 | UnwindData |  |
| 1611 | `WerpLaunchAeDebug` | `0x767A0` | 2,352 | UnwindData |  |
| 60 | `BaseFlushAppcompatCacheWorker` | `0x789E0` | 72 | UnwindData |  |
| 77 | `BaseUpdateAppcompatCacheWorker` | `0x78A30` | 29 | UnwindData |  |
| 105 | `BasepInitAppCompatData` | `0x78AA0` | 124 | UnwindData |  |
| 72 | `BaseQueryModuleData` | `0x78B70` | 154 | UnwindData |  |
| 1168 | `QuirkGetData2Worker` | `0x78C10` | 193 | UnwindData |  |
| 1169 | `QuirkGetDataWorker` | `0x78CE0` | 169 | UnwindData |  |
| 1170 | `QuirkIsEnabled2Worker` | `0x78D90` | 293 | UnwindData |  |
| 1518 | `TlsGetValue` | `0x844F0` | 107 | UnwindData |  |
