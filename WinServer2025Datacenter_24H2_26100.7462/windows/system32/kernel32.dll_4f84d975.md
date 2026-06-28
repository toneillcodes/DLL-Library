# Binary Specification: kernel32.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\kernel32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4f84d975b80158f842426d6c609bf635294e490c0128416a1b5172e6f0a3e45b`
* **Total Exported Functions:** 1692

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
| 125 | `BuildIoRingCancelRequest` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-ioring-l1-1-0.BuildIoRingCancelRequest` |
| 126 | `BuildIoRingFlushFile` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-ioring-l1-1-1.BuildIoRingFlushFile` |
| 127 | `BuildIoRingReadFile` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-ioring-l1-1-0.BuildIoRingReadFile` |
| 128 | `BuildIoRingReadFileScatter` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-ioring-l1-1-2.BuildIoRingReadFileScatter` |
| 129 | `BuildIoRingRegisterBuffers` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-ioring-l1-1-0.BuildIoRingRegisterBuffers` |
| 130 | `BuildIoRingRegisterFileHandles` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-ioring-l1-1-0.BuildIoRingRegisterFileHandles` |
| 131 | `BuildIoRingWriteFile` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-ioring-l1-1-1.BuildIoRingWriteFile` |
| 132 | `BuildIoRingWriteFileGather` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-ioring-l1-1-2.BuildIoRingWriteFileGather` |
| 140 | `CancelThreadpoolIo` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpCancelAsyncIoOperation` |
| 143 | `CeipIsOptedIn` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.CeipIsOptedIn` |
| 159 | `CloseIoRing` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-ioring-l1-1-0.CloseIoRing` |
| 160 | `ClosePackageInfo` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.ClosePackageInfo` |
| 164 | `CloseState` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.CloseState` |
| 165 | `CloseThreadpool` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpReleasePool` |
| 166 | `CloseThreadpoolCleanupGroup` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpReleaseCleanupGroup` |
| 167 | `CloseThreadpoolCleanupGroupMembers` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpReleaseCleanupGroupMembers` |
| 168 | `CloseThreadpoolIo` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpReleaseIoCompletion` |
| 169 | `CloseThreadpoolTimer` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpReleaseTimer` |
| 170 | `CloseThreadpoolWait` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpReleaseWait` |
| 171 | `CloseThreadpoolWork` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpReleaseWork` |
| 214 | `CreateEnclave` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-enclave-l1-1-0.CreateEnclave` |
| 225 | `CreateFileMappingFromApp` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-memory-l1-1-1.CreateFileMappingFromApp` |
| 237 | `CreateIoRing` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-ioring-l1-1-0.CreateIoRing` |
| 262 | `CreateRemoteThreadEx` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-0.CreateRemoteThreadEx` |
| 288 | `CtrlRoutine` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.CtrlRoutine` |
| 297 | `DecodePointer` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlDecodePointer` |
| 298 | `DecodeSystemPointer` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlDecodeSystemPointer` |
| 304 | `DeleteCriticalSection` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlDeleteCriticalSection` |
| 312 | `DeleteProcThreadAttributeList` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-0.DeleteProcThreadAttributeList` |
| 325 | `DisassociateCurrentThreadFromCallback` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpDisassociateCallback` |
| 326 | `DiscardVirtualMemory` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-memory-l1-1-2.DiscardVirtualMemory` |
| 340 | `EncodePointer` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlEncodePointer` |
| 341 | `EncodeSystemPointer` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlEncodeSystemPointer` |
| 344 | `EnterCriticalSection` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlEnterCriticalSection` |
| 392 | `ExitThread` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlExitUserThread` |
| 427 | `FindFirstStreamW` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-file-l1-2-2.FindFirstStreamW` |
| 438 | `FindNextStreamW` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-file-l1-2-2.FindNextStreamW` |
| 443 | `FindPackagesByPackageFamily` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.FindPackagesByPackageFamily` |
| 454 | `FlsGetValue2` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.FlsGetValue2` |
| 459 | `FlushProcessWriteBuffers` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.NtFlushProcessWriteBuffers` |
| 463 | `FormatApplicationUserModelId` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.FormatApplicationUserModelId` |
| 471 | `FreeLibraryWhenCallbackReturns` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpCallbackUnloadDllOnCompletion` |
| 485 | `GetApplicationUserModelId` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetApplicationUserModelId` |
| 545 | `GetConsoleInputExeNameA` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetConsoleInputExeNameA` |
| 546 | `GetConsoleInputExeNameW` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetConsoleInputExeNameW` |
| 567 | `GetCurrentApplicationUserModelId` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetCurrentApplicationUserModelId` |
| 572 | `GetCurrentPackageFamilyName` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetCurrentPackageFamilyName` |
| 573 | `GetCurrentPackageFullName` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetCurrentPackageFullName` |
| 574 | `GetCurrentPackageId` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetCurrentPackageId` |
| 575 | `GetCurrentPackageInfo` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetCurrentPackageInfo` |
| 576 | `GetCurrentPackagePath` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetCurrentPackagePath` |
| 580 | `GetCurrentProcessorNumber` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlGetCurrentProcessorNumber` |
| 581 | `GetCurrentProcessorNumberEx` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlGetCurrentProcessorNumberEx` |
| 584 | `GetCurrentThreadStackLimits` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-0.GetCurrentThreadStackLimits` |
| 598 | `GetDiskSpaceInformationA` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-file-l1-2-3.GetDiskSpaceInformationA` |
| 599 | `GetDiskSpaceInformationW` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-file-l1-2-3.GetDiskSpaceInformationW` |
| 651 | `GetIoRingInfo` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-ioring-l1-1-0.GetIoRingInfo` |
| 663 | `GetLogicalProcessorInformationEx` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-sysinfo-l1-1-0.GetLogicalProcessorInformationEx` |
| 668 | `GetMachineTypeAttributes` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-7.GetMachineTypeAttributes` |
| 688 | `GetNamedPipeInfo` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-namedpipe-l1-2-1.GetNamedPipeInfo` |
| 699 | `GetNumaNodeProcessorMask2` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-systemtopology-l1-1-2.GetNumaNodeProcessorMask2` |
| 713 | `GetOverlappedResultEx` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-io-l1-1-1.GetOverlappedResultEx` |
| 714 | `GetPackageApplicationIds` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetPackageApplicationIds` |
| 715 | `GetPackageFamilyName` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetPackageFamilyName` |
| 716 | `GetPackageFullName` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetPackageFullName` |
| 717 | `GetPackageId` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetPackageId` |
| 718 | `GetPackageInfo` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetPackageInfo` |
| 719 | `GetPackagePath` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetPackagePath` |
| 720 | `GetPackagePathByFullName` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetPackagePathByFullName` |
| 721 | `GetPackagesByPackageFamily` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetPackagesByPackageFamily` |
| 737 | `GetProcessDefaultCpuSetMasks` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-6.GetProcessDefaultCpuSetMasks` |
| 738 | `GetProcessDefaultCpuSets` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-3.GetProcessDefaultCpuSets` |
| 747 | `GetProcessMitigationPolicy` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-1.GetProcessMitigationPolicy` |
| 756 | `GetProcessorSystemCycleTime` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-sysinfo-l1-2-2.GetProcessorSystemCycleTime` |
| 768 | `GetStagedPackagePathByFullName` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetStagedPackagePathByFullName` |
| 771 | `GetStateFolder` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetStateFolder` |
| 778 | `GetSystemAppDataKey` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.GetSystemAppDataKey` |
| 779 | `GetSystemCpuSetInformation` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-3.GetSystemCpuSetInformation` |
| 812 | `GetThreadDescription` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-3.GetThreadDescription` |
| 824 | `GetThreadSelectedCpuSetMasks` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-6.GetThreadSelectedCpuSetMasks` |
| 825 | `GetThreadSelectedCpuSets` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-3.GetThreadSelectedCpuSets` |
| 893 | `HeapAlloc` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlAllocateHeap` |
| 900 | `HeapReAlloc` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlReAllocateHeap` |
| 902 | `HeapSize` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlSizeHeap` |
| 911 | `InitOnceBeginInitialize` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-synch-l1-2-0.InitOnceBeginInitialize` |
| 912 | `InitOnceComplete` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-synch-l1-2-0.InitOnceComplete` |
| 913 | `InitOnceExecuteOnce` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-synch-l1-2-0.InitOnceExecuteOnce` |
| 914 | `InitOnceInitialize` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlRunOnceInitialize` |
| 915 | `InitializeConditionVariable` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlInitializeConditionVariable` |
| 918 | `InitializeCriticalSection` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlInitializeCriticalSection` |
| 921 | `InitializeEnclave` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-enclave-l1-1-0.InitializeEnclave` |
| 922 | `InitializeProcThreadAttributeList` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-0.InitializeProcThreadAttributeList` |
| 923 | `InitializeSListHead` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlInitializeSListHead` |
| 924 | `InitializeSRWLock` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlInitializeSRWLock` |
| 926 | `InstallELAMCertificateInfo` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-sysinfo-l1-2-1.InstallELAMCertificateInfo` |
| 927 | `InterlockedFlushSList` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlInterlockedFlushSList` |
| 928 | `InterlockedPopEntrySList` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlInterlockedPopEntrySList` |
| 929 | `InterlockedPushEntrySList` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlInterlockedPushEntrySList` |
| 930 | `InterlockedPushListSList` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlInterlockedPushListSList` |
| 931 | `InterlockedPushListSListEx` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlInterlockedPushListSListEx` |
| 946 | `IsEnclaveTypeSupported` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-enclave-l1-1-0.IsEnclaveTypeSupported` |
| 947 | `IsIoRingOpSupported` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-ioring-l1-1-0.IsIoRingOpSupported` |
| 951 | `IsProcessCritical` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-2.IsProcessCritical` |
| 956 | `IsThreadpoolTimerSet` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpIsTimerSet` |
| 957 | `IsUserCetAvailableInEnvironment` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-sysinfo-l1-2-6.IsUserCetAvailableInEnvironment` |
| 964 | `IsWow64GuestMachineSupported` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-wow64-l1-1-2.IsWow64GuestMachineSupported` |
| 966 | `IsWow64Process2` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-wow64-l1-1-1.IsWow64Process2` |
| 1009 | `LeaveCriticalSection` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlLeaveCriticalSection` |
| 1010 | `LeaveCriticalSectionWhenCallbackReturns` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpCallbackLeaveCriticalSectionOnCompletion` |
| 1012 | `LoadEnclaveData` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-enclave-l1-1-0.LoadEnclaveData` |
| 1025 | `LocalFileTimeToLocalSystemTime` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-timezone-l1-1-1.LocalFileTimeToLocalSystemTime` |
| 1033 | `LocalSystemTimeToLocalFileTime` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-timezone-l1-1-1.LocalSystemTimeToLocalFileTime` |
| 1040 | `LogUnexpectedCodepath` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlLogUnexpectedCodepath` |
| 1046 | `MapViewOfFileFromApp` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-memory-l1-1-1.MapViewOfFileFromApp` |
| 1072 | `OfferVirtualMemory` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-memory-l1-1-2.OfferVirtualMemory` |
| 1085 | `OpenPackageInfoByFullName` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.OpenPackageInfoByFullName` |
| 1089 | `OpenProcessToken` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-0.OpenProcessToken` |
| 1093 | `OpenState` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.OpenState` |
| 1094 | `OpenStateExplicit` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.OpenStateExplicit` |
| 1096 | `OpenThreadToken` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-0.OpenThreadToken` |
| 1101 | `PackageFamilyNameFromFullName` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.PackageFamilyNameFromFullName` |
| 1102 | `PackageFamilyNameFromId` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.PackageFamilyNameFromId` |
| 1103 | `PackageFullNameFromId` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.PackageFullNameFromId` |
| 1104 | `PackageIdFromFullName` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.PackageIdFromFullName` |
| 1105 | `PackageNameAndPublisherIdFromFamilyName` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.PackageNameAndPublisherIdFromFamilyName` |
| 1106 | `ParseApplicationUserModelId` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.ParseApplicationUserModelId` |
| 1110 | `PopIoRingCompletion` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-ioring-l1-1-0.PopIoRingCompletion` |
| 1115 | `PrefetchVirtualMemory` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-memory-l1-1-1.PrefetchVirtualMemory` |
| 1143 | `QueryDepthSList` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlQueryDepthSList` |
| 1152 | `QueryIoRingCapabilities` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-ioring-l1-1-0.QueryIoRingCapabilities` |
| 1158 | `QueryProtectedPolicy` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-2.QueryProtectedPolicy` |
| 1165 | `QueueUserAPC2` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-5.QueueUserAPC2` |
| 1178 | `RaiseFailFastException` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.RaiseFailFastException` |
| 1183 | `ReadConsoleInputExA` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.ReadConsoleInputExA` |
| 1184 | `ReadConsoleInputExW` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.ReadConsoleInputExW` |
| 1199 | `ReclaimVirtualMemory` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-memory-l1-1-2.ReclaimVirtualMemory` |
| 1256 | `ReleaseMutexWhenCallbackReturns` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpCallbackReleaseMutexOnCompletion` |
| 1259 | `ReleaseSRWLockExclusive` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlReleaseSRWLockExclusive` |
| 1260 | `ReleaseSRWLockShared` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlReleaseSRWLockShared` |
| 1262 | `ReleaseSemaphoreWhenCallbackReturns` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpCallbackReleaseSemaphoreOnCompletion` |
| 1269 | `RemoveDllDirectory` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-libraryloader-l1-1-0.RemoveDllDirectory` |
| 1273 | `RemoveVectoredContinueHandler` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlRemoveVectoredContinueHandler` |
| 1274 | `RemoveVectoredExceptionHandler` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlRemoveVectoredExceptionHandler` |
| 1284 | `ResolveDelayLoadedAPI` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.LdrResolveDelayLoadedAPI` |
| 1285 | `ResolveDelayLoadsFromDll` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.LdrResolveDelayLoadsFromDll` |
| 1287 | `RestoreLastError` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlRestoreLastWin32Error` |
| 1291 | `RtlCaptureStackBackTrace` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlCaptureStackBackTrace` |
| 1297 | `RtlIsEcCode` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlIsEcCode` |
| 1307 | `RtlZeroMemory` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlZeroMemory` |
| 1338 | `SetConsoleInputExeNameA` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.SetConsoleInputExeNameA` |
| 1339 | `SetConsoleInputExeNameW` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.SetConsoleInputExeNameW` |
| 1357 | `SetCriticalSectionSpinCount` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlSetCriticalSectionSpinCount` |
| 1363 | `SetDefaultDllDirectories` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-libraryloader-l1-1-0.SetDefaultDllDirectories` |
| 1374 | `SetEventWhenCallbackReturns` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpCallbackSetEventOnCompletion` |
| 1399 | `SetIoRingCompletionEvent` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-ioring-l1-1-0.SetIoRingCompletionEvent` |
| 1400 | `SetLastConsoleEventActive` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.SetLastConsoleEventActive` |
| 1415 | `SetProcessDefaultCpuSetMasks` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-6.SetProcessDefaultCpuSetMasks` |
| 1416 | `SetProcessDefaultCpuSets` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-3.SetProcessDefaultCpuSets` |
| 1417 | `SetProcessDynamicEHContinuationTargets` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-4.SetProcessDynamicEHContinuationTargets` |
| 1418 | `SetProcessDynamicEnforcedCetCompatibleRanges` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-6.SetProcessDynamicEnforcedCetCompatibleRanges` |
| 1420 | `SetProcessMitigationPolicy` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-1.SetProcessMitigationPolicy` |
| 1426 | `SetProtectedPolicy` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-2.SetProtectedPolicy` |
| 1439 | `SetThreadDescription` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-3.SetThreadDescription` |
| 1450 | `SetThreadSelectedCpuSetMasks` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-6.SetThreadSelectedCpuSetMasks` |
| 1451 | `SetThreadSelectedCpuSets` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-3.SetThreadSelectedCpuSets` |
| 1453 | `SetThreadToken` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-0.SetThreadToken` |
| 1456 | `SetThreadpoolThreadMaximum` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpSetPoolMaxThreads` |
| 1458 | `SetThreadpoolTimer` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpSetTimer` |
| 1459 | `SetThreadpoolTimerEx` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpSetTimerEx` |
| 1460 | `SetThreadpoolWait` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpSetWait` |
| 1461 | `SetThreadpoolWaitEx` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpSetWaitEx` |
| 1475 | `SetWaitableTimerEx` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-synch-l1-1-0.SetWaitableTimerEx` |
| 1482 | `SleepConditionVariableCS` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-synch-l1-2-0.SleepConditionVariableCS` |
| 1483 | `SleepConditionVariableSRW` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-synch-l1-2-0.SleepConditionVariableSRW` |
| 1487 | `StartThreadpoolIo` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpStartAsyncIoOperation` |
| 1488 | `SubmitIoRing` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-ioring-l1-1-0.SubmitIoRing` |
| 1489 | `SubmitThreadpoolWork` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpPostWork` |
| 1495 | `SystemTimeToTzSpecificLocalTimeEx` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-timezone-l1-1-0.SystemTimeToTzSpecificLocalTimeEx` |
| 1518 | `TlsGetValue2` | `0x0` | - | Forwarded | Forwarded to: `kernelbase.TlsGetValue2` |
| 1523 | `TryAcquireSRWLockExclusive` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlTryAcquireSRWLockExclusive` |
| 1524 | `TryAcquireSRWLockShared` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlTryAcquireSRWLockShared` |
| 1525 | `TryEnterCriticalSection` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlTryEnterCriticalSection` |
| 1528 | `TzSpecificLocalTimeToSystemTimeEx` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-timezone-l1-1-0.TzSpecificLocalTimeToSystemTimeEx` |
| 1536 | `UnmapViewOfFileEx` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-memory-l1-1-1.UnmapViewOfFileEx` |
| 1545 | `UpdateProcThreadAttribute` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-processthreads-l1-1-0.UpdateProcThreadAttribute` |
| 1552 | `VerSetConditionMask` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.VerSetConditionMask` |
| 1571 | `WaitForDebugEventEx` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-debug-l1-1-2.WaitForDebugEventEx` |
| 1576 | `WaitForThreadpoolIoCallbacks` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpWaitForIoCompletion` |
| 1577 | `WaitForThreadpoolTimerCallbacks` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpWaitForTimer` |
| 1578 | `WaitForThreadpoolWaitCallbacks` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpWaitForWait` |
| 1579 | `WaitForThreadpoolWorkCallbacks` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.TpWaitForWork` |
| 1582 | `WakeAllConditionVariable` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlWakeAllConditionVariable` |
| 1583 | `WakeConditionVariable` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.RtlWakeConditionVariable` |
| 1650 | `__C_specific_handler` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.__C_specific_handler` |
| 1651 | `__chkstk` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.__chkstk` |
| 1652 | `__misaligned_access` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.__misaligned_access` |
| 1658 | `_local_unwind` | `0x0` | - | Forwarded | Forwarded to: `NTDLL._local_unwind` |
| 1052 | `MoveFileExA` | `0xACF0` | 32 | UnwindData |  |
| 857 | `GetVolumePathNameA` | `0xADF0` | 405 | UnwindData |  |
| 242 | `CreateMailslotW` | `0xAF90` | 434 | UnwindData |  |
| 241 | `CreateMailslotA` | `0xB150` | 111 | UnwindData |  |
| 133 | `CallNamedPipeA` | `0xB1D0` | 151 | UnwindData |  |
| 767 | `GetShortPathNameW` | `0xB270` | 1,177 | UnwindData |  |
| 263 | `CreateSemaphoreA` | `0xB710` | 167 | UnwindData |  |
| 264 | `CreateSemaphoreExA` | `0xB880` | 157 | UnwindData |  |
| 766 | `GetShortPathNameA` | `0xB930` | 595 | UnwindData |  |
| 664 | `GetLongPathNameA` | `0xBB90` | 593 | UnwindData |  |
| 667 | `GetLongPathNameW` | `0xBDF0` | 1,601 | UnwindData |  |
| 859 | `GetVolumePathNamesForVolumeNameA` | `0xC4A0` | 436 | UnwindData |  |
| 1144 | `QueryDosDeviceA` | `0xC660` | 520 | UnwindData |  |
| 1091 | `OpenSemaphoreA` | `0xC870` | 116 | UnwindData |  |
| 1580 | `WaitNamedPipeA` | `0xC8F0` | 84 | UnwindData |  |
| 1079 | `OpenFileMappingA` | `0xC950` | 121 | UnwindData |  |
| 248 | `CreateNamedPipeA` | `0xC9D0` | 164 | UnwindData |  |
| 224 | `CreateFileMappingA` | `0xCA80` | 186 | UnwindData |  |
| 79 | `Basep8BitStringToDynamicUnicodeString` | `0xCB40` | 119 | UnwindData |  |
| 1083 | `OpenMutexA` | `0xCBC0` | 114 | UnwindData |  |
| 1541 | `UnregisterWait` | `0xCC40` | 73 | UnwindData |  |
| 790 | `GetSystemPowerStatus` | `0xCC90` | 366 | UnwindData |  |
| 1441 | `SetThreadExecutionState` | `0xCE10` | 51 | UnwindData |  |
| 701 | `GetNumaProcessorNode` | `0xCE50` | 111 | UnwindData |  |
| 702 | `GetNumaProcessorNodeEx` | `0xCED0` | 194 | UnwindData |  |
| 445 | `FindResourceExA` | `0xCFA0` | 234 | UnwindData |  |
| 106 | `BasepMapModuleHandle` | `0xD1A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 641 | `GetFirmwareEnvironmentVariableW` | `0xD1D0` | 21 | UnwindData |  |
| 640 | `GetFirmwareEnvironmentVariableExW` | `0xD1F0` | 235 | UnwindData |  |
| 1639 | `WritePrivateProfileStringW` | `0xD2F0` | 100 | UnwindData |  |
| 487 | `GetAtomNameW` | `0xD360` | 31 | UnwindData |  |
| 878 | `GlobalGetAtomNameW` | `0xD390` | 31 | UnwindData |  |
| 669 | `GetMailslotInfo` | `0xD8B0` | 247 | UnwindData |  |
| 1437 | `SetThreadAffinityMask` | `0xD9B0` | 186 | UnwindData |  |
| 746 | `GetProcessIoCounters` | `0xDA70` | 61 | UnwindData |  |
| 1513 | `Thread32First` | `0xDAC0` | 253 | UnwindData |  |
| 735 | `GetProcessAffinityMask` | `0xDBD0` | 175 | UnwindData |  |
| 566 | `GetCurrentActCtxWorker` | `0xDEC0` | 59 | UnwindData |  |
| 1140 | `QueryActCtxSettingsWWorker` | `0xDF10` | 460 | UnwindData |  |
| 1150 | `QueryInformationJobObject` | `0xE0F0` | 339 | UnwindData |  |
| 661 | `GetLogicalDrives` | `0xE250` | 106 | UnwindData |  |
| 331 | `DosDateTimeToFileTime` | `0xE2C0` | 191 | UnwindData |  |
| 290 | `DeactivateActCtxWorker` | `0xE390` | 52 | UnwindData |  |
| 1514 | `Thread32Next` | `0xE3D0` | 260 | UnwindData |  |
| 4 | `ActivateActCtxWorker` | `0xE4E0` | 63 | UnwindData |  |
| 411 | `FindActCtxSectionStringWWorker` | `0xE6B0` | 414 | UnwindData |  |
| 401 | `FileTimeToDosDateTime` | `0xE860` | 215 | UnwindData |  |
| 408 | `FindActCtxSectionGuidWorker` | `0xE940` | 381 | UnwindData |  |
| 73 | `BaseSetLastNTError` | `0xEAD0` | 43 | UnwindData |  |
| 729 | `GetPrivateProfileSectionW` | `0xF0B0` | 196 | UnwindData |  |
| 55 | `BaseDllReadWriteIniFile` | `0xF180` | 786 | UnwindData |  |
| 1500 | `TermsrvConvertSysRootToUserDir` | `0x113A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1512 | `TermsrvSyncUserIniFileExt` | `0x113C0` | 5,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 453 | `FlsGetValue` | `0x12A00` | 101 | UnwindData |  |
| 936 | `IsBadReadPtr` | `0x12A70` | 127 | UnwindData |  |
| 830 | `GetTickCount64` | `0x12B00` | 2,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 495 | `GetCalendarDateFormat` | `0x13360` | 139 | UnwindData |  |
| 846 | `GetUserGeoID` | `0x13A70` | 251 | UnwindData |  |
| 841 | `GetUserDefaultGeoName` | `0x13EA0` | 235 | UnwindData |  |
| 647 | `GetGeoInfoA` | `0x13FA0` | 199 | UnwindData |  |
| 22 | `AdjustCalendarDate` | `0x140C0` | 640 | UnwindData |  |
| 497 | `GetCalendarDaysInMonth` | `0x14640` | 209 | UnwindData |  |
| 649 | `GetGeoInfoW` | `0x14830` | 634 | UnwindData |  |
| 496 | `GetCalendarDateFormatEx` | `0x14F20` | 840 | UnwindData |  |
| 1544 | `UpdateCalendarDayOfWeek` | `0x15270` | 181 | UnwindData |  |
| 958 | `IsValidCalDateTime` | `0x15500` | 222 | UnwindData |  |
| 835 | `GetTimeFormatWWorker` | `0x15990` | 554 | UnwindData |  |
| 590 | `GetDateFormatWWorker` | `0x16710` | 1,637 | UnwindData |  |
| 1121 | `Process32Next` | `0x181E0` | 279 | UnwindData |  |
| 1122 | `Process32NextW` | `0x18300` | 39 | UnwindData |  |
| 829 | `GetTickCount` | `0x18600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 583 | `GetCurrentThreadId` | `0x18620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 654 | `GetLastError` | `0x18640` | 9,648 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1174 | `QuirkIsEnabledForPackageWorker` | `0x1ABF0` | 156 | UnwindData |  |
| 1172 | `QuirkIsEnabledForPackage3Worker` | `0x1AD70` | 63 | UnwindData |  |
| 1173 | `QuirkIsEnabledForPackage4Worker` | `0x1ADC0` | 140 | UnwindData |  |
| 1170 | `QuirkIsEnabled3Worker` | `0x1AE60` | 357 | UnwindData |  |
| 1176 | `QuirkIsEnabledWorker` | `0x1B5D0` | 363 | UnwindData |  |
| 110 | `BasepQueryAppCompat` | `0x1CF00` | 632 | UnwindData |  |
| 51 | `BaseCheckElevation` | `0x216A0` | 528 | UnwindData |  |
| 146 | `CheckElevation` | `0x225A0` | 332 | UnwindData |  |
| 84 | `BasepCheckAppCompat` | `0x22700` | 216 | UnwindData |  |
| 97 | `BasepGetExeArchType` | `0x227E0` | 527 | UnwindData |  |
| 1683 | `timeGetSystemTime` | `0x23140` | 49 | UnwindData |  |
| 1684 | `timeGetTime` | `0x23180` | 90 | UnwindData |  |
| 996 | `LCMapStringEx` | `0x231E0` | 84 | UnwindData |  |
| 322 | `DeviceIoControl` | `0x23240` | 244 | UnwindData |  |
| 1681 | `timeEndPeriod` | `0x233A0` | 351 | UnwindData |  |
| 582 | `GetCurrentThread` | `0x23510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 178 | `CompareStringEx` | `0x23520` | 84 | UnwindData |  |
| 1680 | `timeBeginPeriod` | `0x23580` | 64 | UnwindData |  |
| 579 | `GetCurrentProcessId` | `0x236E0` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1653 | `_hread` | `0x23B40` | 53 | UnwindData |  |
| 1660 | `_lread` | `0x23B40` | 53 | UnwindData |  |
| 876 | `GlobalFree` | `0x23F40` | 61 | UnwindData |  |
| 741 | `GetProcessHeap` | `0x23F90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1154 | `QueryPerformanceCounter` | `0x23FB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1175 | `QuirkIsEnabledForProcessWorker` | `0x23FD0` | 696 | UnwindData |  |
| 1049 | `Module32Next` | `0x24390` | 322 | UnwindData |  |
| 1050 | `Module32NextW` | `0x244E0` | 348 | UnwindData |  |
| 1507 | `TermsrvOpenRegEntry` | `0x24650` | 800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 578 | `GetCurrentProcess` | `0x24970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 897 | `HeapFree` | `0x24980` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | `CreateActCtxWWorker` | `0x24C70` | 3,685 | UnwindData |  |
| 114 | `BasepReleaseSxsCreateProcessUtilityStruct` | `0x26F20` | 132 | UnwindData |  |
| 88 | `BasepConstructSxsCreateProcessMessage` | `0x27BC0` | 1,878 | UnwindData |  |
| 1305 | `RtlVirtualUnwind` | `0x28CC0` | 67 | UnwindData |  |
| 1401 | `SetLastError` | `0x28DB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 616 | `GetExitCodeProcess` | `0x28DD0` | 100 | UnwindData |  |
| 1248 | `RegisterWaitForSingleObject` | `0x28F10` | 140 | UnwindData |  |
| 1486 | `SortGetHandle` | `0x28FB0` | 160 | UnwindData |  |
| 1519 | `TlsSetValue` | `0x29C60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 433 | `FindNLSStringEx` | `0x29C80` | 96 | UnwindData |  |
| 1654 | `_hwrite` | `0x2BC30` | 72 | UnwindData |  |
| 1661 | `_lwrite` | `0x2BC30` | 72 | UnwindData |  |
| 1556 | `VerifyVersionInfoW` | `0x2E0D0` | 69 | UnwindData |  |
| 74 | `BaseThreadInitThunk` | `0x2E8C0` | 77 | UnwindData |  |
| 764 | `GetQueuedCompletionStatus` | `0x2EFB0` | 6,864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1662 | `lstrcat` | `0x30A80` | 41 | UnwindData |  |
| 1663 | `lstrcatA` | `0x30A80` | 41 | UnwindData |  |
| 818 | `GetThreadIdealProcessorEx` | `0x30AB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 937 | `IsBadStringPtrA` | `0x30AD0` | 76 | UnwindData |  |
| 95 | `BasepGetAppCompatData` | `0x30B30` | 1,311 | UnwindData |  |
| 64 | `BaseGenerateAppCompatData` | `0x31560` | 124 | UnwindData |  |
| 1481 | `Sleep` | `0x31980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 795 | `GetSystemTimeAsFileTime` | `0x319A0` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1492 | `SwitchToThread` | `0x31BB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1119 | `Process32First` | `0x31BD0` | 279 | UnwindData |  |
| 1120 | `Process32FirstW` | `0x31CF0` | 342 | UnwindData |  |
| 1504 | `TermsrvGetPreSetValue` | `0x31E50` | 34 | UnwindData |  |
| 413 | `FindAtomW` | `0x31E80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 285 | `CreateWaitableTimerExA` | `0x31EA0` | 140 | UnwindData |  |
| 1657 | `_llseek` | `0x31F80` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1060 | `MultiByteToWideChar` | `0x31FC0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 955 | `IsThreadAFiber` | `0x32040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1679 | `lstrlenW` | `0x32060` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `BackupReadEx` | `0x32230` | 917 | UnwindData |  |
| 1613 | `WideCharToMultiByte` | `0x330A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 997 | `LCMapStringW` | `0x330C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `CompareStringOrdinal` | `0x330E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 272 | `CreateThread` | `0x33100` | 72 | UnwindData |  |
| 1163 | `QueryUnbiasedInterruptTime` | `0x33150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1671 | `lstrcpy` | `0x33170` | 28 | UnwindData |  |
| 1672 | `lstrcpyA` | `0x33170` | 28 | UnwindData |  |
| 1511 | `TermsrvSetValueKey` | `0x331A0` | 49 | UnwindData |  |
| 1155 | `QueryPerformanceFrequency` | `0x331E0` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1047 | `Module32First` | `0x33400` | 343 | UnwindData |  |
| 1048 | `Module32FirstW` | `0x33560` | 353 | UnwindData |  |
| 107 | `BasepNotifyLoadStringResource` | `0x336D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1611 | `WerpNotifyLoadStringResourceWorker` | `0x336D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1612 | `WerpNotifyUseStringResourceWorker` | `0x336D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1153 | `QueryMemoryResourceNotification` | `0x336E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1071 | `OOBEComplete` | `0x33700` | 170 | UnwindData |  |
| 284 | `CreateWaitableTimerA` | `0x33BB0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1088 | `OpenProcess` | `0x33C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 734 | `GetProcAddress` | `0x33C70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1557 | `VirtualAlloc` | `0x33C90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 712 | `GetOverlappedResult` | `0x33CB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1111 | `PostQueuedCompletionStatus` | `0x33CD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1670 | `lstrcmpiW` | `0x33CF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1686 | `uaw_lstrcmpiW` | `0x33CF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1673 | `lstrcpyW` | `0x33D10` | 32 | UnwindData |  |
| 87 | `BasepCheckWinSaferRestrictions` | `0x33D40` | 2,579 | UnwindData |  |
| 278 | `CreateThreadpoolWork` | `0x34760` | 74 | UnwindData |  |
| 1027 | `LocalFree` | `0x34BD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 827 | `GetThreadTimes` | `0x34BF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1501 | `TermsrvCreateRegEntry` | `0x34C10` | 39 | UnwindData |  |
| 1011 | `LoadAppInitDlls` | `0x34C40` | 282 | UnwindData |  |
| 1664 | `lstrcatW` | `0x35110` | 46 | UnwindData |  |
| 959 | `IsValidCodePage` | `0x35150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 869 | `GlobalAlloc` | `0x35170` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1123 | `ProcessIdToSessionId` | `0x35200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 743 | `GetProcessId` | `0x35220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 881 | `GlobalMemoryStatus` | `0x35240` | 239 | UnwindData |  |
| 1555 | `VerifyVersionInfoA` | `0x353F0` | 248 | UnwindData |  |
| 94 | `BasepFreeAppCompatData` | `0x354F0` | 68 | UnwindData |  |
| 116 | `BasepSetFileEncryptionCompression` | `0x35560` | 1,639 | UnwindData |  |
| 1503 | `TermsrvDeleteValue` | `0x35BD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1560 | `VirtualFree` | `0x35BF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 287 | `CreateWaitableTimerW` | `0x35C10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 776 | `GetStringTypeExW` | `0x35C40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1069 | `NotifyUILanguageChange` | `0x35C60` | 620 | UnwindData |  |
| 938 | `IsBadStringPtrW` | `0x36C90` | 80 | UnwindData |  |
| 1502 | `TermsrvDeleteKey` | `0x36CF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1137 | `PulseEvent` | `0x36D10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 871 | `GlobalDeleteAtom` | `0x36D30` | 53 | UnwindData |  |
| 1506 | `TermsrvGetWindowsDirectoryW` | `0x36D70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 276 | `CreateThreadpoolTimer` | `0x36D90` | 74 | UnwindData |  |
| 1446 | `SetThreadLocale` | `0x36DE0` | 1,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1448 | `SetThreadPriority` | `0x37580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 793 | `GetSystemTime` | `0x375A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 822 | `GetThreadPriority` | `0x375C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1677 | `lstrlen` | `0x375E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1678 | `lstrlenA` | `0x375E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 502 | `GetCalendarMonthsInYear` | `0x37600` | 228 | UnwindData |  |
| 503 | `GetCalendarSupportedDateRange` | `0x376F0` | 525 | UnwindData |  |
| 188 | `ConvertSystemTimeToCalDateTime` | `0x37910` | 225 | UnwindData |  |
| 1508 | `TermsrvOpenUserClasses` | `0x37A50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1095 | `OpenThread` | `0x37A70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1022 | `LocalAlloc` | `0x37A90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 820 | `GetThreadLocale` | `0x37AB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1159 | `QueryThreadCycleTime` | `0x37AD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 873 | `GlobalFindAtomW` | `0x37AF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1655 | `_lclose` | `0x37B10` | 33 | UnwindData |  |
| 455 | `FlsSetValue` | `0x37B40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1493 | `SystemTimeToFileTime` | `0x37B60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1300 | `RtlPcToFileHeader` | `0x37B80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `ActivateActCtx` | `0x37BA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 617 | `GetExitCodeThread` | `0x37BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1109 | `PeekNamedPipe` | `0x37BE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1397 | `SetInformationJobObject` | `0x37C00` | 422 | UnwindData |  |
| 939 | `IsBadWritePtr` | `0x37DB0` | 127 | UnwindData |  |
| 655 | `GetLocalTime` | `0x37E40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 777 | `GetStringTypeW` | `0x37E60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 906 | `HeapWalk` | `0x37E80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1382 | `SetFileCompletionNotificationModes` | `0x37EA0` | 112 | UnwindData |  |
| 7 | `AddAtomW` | `0x37F20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 670 | `GetMaximumProcessorCount` | `0x37F40` | 178 | UnwindData |  |
| 478 | `GetActiveProcessorGroupCount` | `0x38000` | 87 | UnwindData |  |
| 671 | `GetMaximumProcessorGroupCount` | `0x38060` | 87 | UnwindData |  |
| 477 | `GetActiveProcessorCount` | `0x380C0` | 182 | UnwindData |  |
| 628 | `GetFileInformationByHandleEx` | `0x38270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 965 | `IsWow64Process` | `0x38290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1563 | `VirtualProtect` | `0x382B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 751 | `GetProcessTimes` | `0x382D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1565 | `VirtualQuery` | `0x382F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1043 | `MapViewOfFile` | `0x38310` | 1,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1035 | `LocaleNameToLCID` | `0x387A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1142 | `QueryActCtxWWorker` | `0x387C0` | 397 | UnwindData |  |
| 105 | `BasepIsProcessAllowed` | `0x38960` | 370 | UnwindData |  |
| 1113 | `PowerCreateRequest` | `0x38AE0` | 134 | UnwindData |  |
| 1535 | `UnmapViewOfFile` | `0x38E50` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 180 | `CompareStringW` | `0x38F80` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `BasepCheckWebBladeHashes` | `0x39180` | 278 | UnwindData |  |
| 832 | `GetTimeFormatAWorker` | `0x392A0` | 630 | UnwindData |  |
| 587 | `GetDateFormatAWorker` | `0x39520` | 624 | UnwindData |  |
| 374 | `EnumSystemGeoID` | `0x39900` | 238 | UnwindData |  |
| 842 | `GetUserDefaultLCID` | `0x39A00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 684 | `GetNamedPipeClientProcessId` | `0x39A20` | 56 | UnwindData |  |
| 1667 | `lstrcmpW` | `0x39A60` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1685 | `uaw_lstrcmpW` | `0x39A60` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1668 | `lstrcmpi` | `0x39AB0` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1669 | `lstrcmpiA` | `0x39AB0` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 817 | `GetThreadId` | `0x39CC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1581 | `WaitNamedPipeW` | `0x39CE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 302 | `DeleteAtom` | `0x39D00` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 988 | `K32GetProcessMemoryInfo` | `0x39DC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1510 | `TermsrvSetKeySecurity` | `0x39DE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 765 | `GetQueuedCompletionStatusEx` | `0x39E00` | 1,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 430 | `FindFirstVolumeMountPointW` | `0x3A220` | 663 | UnwindData |  |
| 1542 | `UnregisterWaitEx` | `0x3AAA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1566 | `VirtualQueryEx` | `0x3AAC0` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 728 | `GetPrivateProfileSectionNamesW` | `0x3ACE0` | 34 | UnwindData |  |
| 725 | `GetPrivateProfileIntW` | `0x3AD10` | 246 | UnwindData |  |
| 731 | `GetPrivateProfileStringW` | `0x3AE10` | 395 | UnwindData |  |
| 882 | `GlobalMemoryStatusEx` | `0x3AFB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 476 | `GetACP` | `0x3AFD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 289 | `DeactivateActCtx` | `0x3AFF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 615 | `GetErrorMode` | `0x3B010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 256 | `CreateProcessAsUserW` | `0x3B030` | 107 | UnwindData |  |
| 228 | `CreateFileMappingW` | `0x3B0F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1177 | `RaiseException` | `0x3B110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1164 | `QueueUserAPC` | `0x3B130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 994 | `LCIDToLocaleName` | `0x3B150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 892 | `Heap32Next` | `0x3B170` | 723 | UnwindData |  |
| 678 | `GetModuleHandleW` | `0x3B450` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 458 | `FlushInstructionCache` | `0x3B550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 447 | `FindResourceW` | `0x3B570` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1515 | `TlsAlloc` | `0x3B700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `BaseElevationPostProcessing` | `0x3B720` | 71 | UnwindData |  |
| 1365 | `SetDllDirectoryW` | `0x3B770` | 149 | UnwindData |  |
| 1254 | `ReleaseActCtxWorker` | `0x3B810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1197 | `ReadProcessMemory` | `0x3B830` | 1,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 518 | `GetComputerNameA` | `0x3BC60` | 299 | UnwindData |  |
| 521 | `GetComputerNameW` | `0x3BE70` | 987 | UnwindData |  |
| 407 | `FindActCtxSectionGuid` | `0x3C410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 239 | `CreateJobObjectW` | `0x3C430` | 189 | UnwindData |  |
| 1372 | `SetErrorMode` | `0x3C500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1479 | `SignalObjectAndWait` | `0x3C520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1288 | `ResumeThread` | `0x3C540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 868 | `GlobalAddAtomW` | `0x3C560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 674 | `GetModuleFileNameW` | `0x3C580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1567 | `VirtualUnlock` | `0x3C5A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 943 | `IsDBCSLeadByte` | `0x3C5C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 675 | `GetModuleHandleA` | `0x3C5E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1015 | `LoadLibraryExW` | `0x3C600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 469 | `FreeLibrary` | `0x3C620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `AddRefActCtxWorker` | `0x3C640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1298 | `RtlLookupFunctionEntry` | `0x3C660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 259 | `CreateProcessW` | `0x3C680` | 95 | UnwindData |  |
| 811 | `GetThreadContext` | `0x3C6F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1480 | `SizeofResource` | `0x3C730` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 867 | `GlobalAddAtomExW` | `0x3C750` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `BasepFinishPackageActivationForSxS` | `0x3C910` | 46 | UnwindData |  |
| 797 | `GetSystemTimes` | `0x3D040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 658 | `GetLocaleInfoW` | `0x3D060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1440 | `SetThreadErrorMode` | `0x3D080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 395 | `ExpandEnvironmentStringsW` | `0x3D0A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1147 | `QueryFullProcessImageNameW` | `0x3D0C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 880 | `GlobalLock` | `0x3D0E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 888 | `GlobalWire` | `0x3D0E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `BaseReadAppCompatDataForProcessWorker` | `0x3D100` | 657 | UnwindData |  |
| 879 | `GlobalHandle` | `0x3D5E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1019 | `LoadResource` | `0x3D600` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 789 | `GetSystemInfo` | `0x3D7F0` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1526 | `TrySubmitThreadpoolCallback` | `0x3D960` | 54 | UnwindData |  |
| 945 | `IsDebuggerPresent` | `0x3D9A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1247 | `RegisterWaitForInputIdle` | `0x3D9C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 953 | `IsProcessorFeaturePresent` | `0x3D9D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 723 | `GetPriorityClass` | `0x3D9F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 657 | `GetLocaleInfoEx` | `0x3DA10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 885 | `GlobalUnWire` | `0x3DA30` | 2,608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 887 | `GlobalUnlock` | `0x3DA30` | 2,608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 446 | `FindResourceExW` | `0x3E460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 444 | `FindResourceA` | `0x3E480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 613 | `GetEnvironmentVariableW` | `0x3E4A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 770 | `GetStartupInfoW` | `0x3E4C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1056 | `MoveFileW` | `0x3E4E0` | 36 | UnwindData |  |
| 677 | `GetModuleHandleExW` | `0x3E510` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 769 | `GetStartupInfoA` | `0x3E530` | 788 | UnwindData |  |
| 1499 | `TermsrvAppInstallMode` | `0x3E850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1490 | `SuspendThread` | `0x3E870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1568 | `WTSGetActiveConsoleSessionId` | `0x3E890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 863 | `GetWriteWatch` | `0x3E8B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 465 | `FormatMessageW` | `0x3E8D0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1067 | `NormalizeString` | `0x3E980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 277 | `CreateThreadpoolWait` | `0x3E9A0` | 74 | UnwindData |  |
| 571 | `GetCurrentDirectoryW` | `0x3EBC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1449 | `SetThreadPriorityBoost` | `0x3EBE0` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 783 | `GetSystemDefaultLocaleName` | `0x3EDF0` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `AreFileApisANSI` | `0x3F070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `AssignProcessToJobObject` | `0x3F090` | 47 | UnwindData |  |
| 470 | `FreeLibraryAndExitThread` | `0x3F0D0` | 17 | UnwindData |  |
| 1516 | `TlsFree` | `0x3F0F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1114 | `PowerSetRequest` | `0x3F110` | 149 | UnwindData |  |
| 744 | `GetProcessIdOfThread` | `0x3F1B0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1436 | `SetTermsrvAppInstallMode` | `0x3F270` | 317 | UnwindData |  |
| 1682 | `timeGetDevCaps` | `0x3F460` | 93 | UnwindData |  |
| 983 | `K32GetModuleFileNameExW` | `0x3F650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1443 | `SetThreadIdealProcessor` | `0x3F670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 689 | `GetNamedPipeServerProcessId` | `0x3F690` | 53 | UnwindData |  |
| 1494 | `SystemTimeToTzSpecificLocalTime` | `0x3F6D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1112 | `PowerClearRequest` | `0x3F6F0` | 148 | UnwindData |  |
| 786 | `GetSystemDirectoryW` | `0x3F790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 944 | `IsDBCSLeadByteEx` | `0x3F7A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1016 | `LoadLibraryW` | `0x3F7C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 979 | `K32GetMappedFileNameW` | `0x3F7E0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 601 | `GetDllDirectoryW` | `0x3F830` | 136 | UnwindData |  |
| 659 | `GetLogicalDriveStringsA` | `0x3F8C0` | 189 | UnwindData |  |
| 612 | `GetEnvironmentVariableA` | `0x3F990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1039 | `LockResource` | `0x3F9B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1028 | `LocalHandle` | `0x3F9D0` | 175 | UnwindData |  |
| 823 | `GetThreadPriorityBoost` | `0x3FA90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 851 | `GetVersionExW` | `0x3FAB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 952 | `IsProcessInJob` | `0x3FAD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1304 | `RtlUnwindEx` | `0x3FAF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 782 | `GetSystemDefaultLangID` | `0x3FB10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 772 | `GetStdHandle` | `0x3FB30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 236 | `CreateIoCompletionPort` | `0x3FB50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 844 | `GetUserDefaultLocaleName` | `0x3FB70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1014 | `LoadLibraryExA` | `0x3FB90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 673 | `GetModuleFileNameA` | `0x3FBB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 691 | `GetNativeSystemInfo` | `0x3FBD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 451 | `FlsAlloc` | `0x3FBF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 330 | `DnsHostnameToComputerNameW` | `0x3FC10` | 208 | UnwindData |  |
| 1080 | `OpenFileMappingW` | `0x3FCF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 987 | `K32GetProcessImageFileNameW` | `0x3FD10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 412 | `FindAtomA` | `0x3FD30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1100 | `OutputDebugStringW` | `0x3FD50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1193 | `ReadDirectoryChangesW` | `0x3FD70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1590 | `WerRegisterFile` | `0x3FD90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1562 | `VirtualLock` | `0x3FDB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 732 | `GetPrivateProfileStructA` | `0x3FDD0` | 396 | UnwindData |  |
| 762 | `GetProfileStringA` | `0x3FF70` | 29 | UnwindData |  |
| 724 | `GetPrivateProfileIntA` | `0x3FFA0` | 150 | UnwindData |  |
| 730 | `GetPrivateProfileStringA` | `0x40040` | 452 | UnwindData |  |
| 781 | `GetSystemDefaultLCID` | `0x40210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `CancelIoEx` | `0x40230` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `BasepFreeActivationTokenInfo` | `0x40250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1044 | `MapViewOfFileEx` | `0x40260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1166 | `QueueUserWorkItem` | `0x40280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 512 | `GetCommandLineA` | `0x402A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1017 | `LoadModule` | `0x402C0` | 1,251 | UnwindData |  |
| 490 | `GetBinaryTypeW` | `0x407B0` | 859 | UnwindData |  |
| 707 | `GetNumberFormatW` | `0x40B20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 933 | `IsBadCodePtr` | `0x40B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 177 | `CompareStringA` | `0x40B40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1642 | `WriteProcessMemory` | `0x40B60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 200 | `CreateActCtxA` | `0x40B80` | 848 | UnwindData |  |
| 1303 | `RtlUnwind` | `0x40EE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 513 | `GetCommandLineW` | `0x40F00` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 460 | `FlushViewOfFile` | `0x40FD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `BackupRead` | `0x40FF0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1665 | `lstrcmp` | `0x41030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1666 | `lstrcmpA` | `0x41030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1496 | `TerminateJobObject` | `0x41040` | 47 | UnwindData |  |
| 181 | `ConnectNamedPipe` | `0x41080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | `CheckNameLegalDOS8Dot3W` | `0x410A0` | 290 | UnwindData |  |
| 1292 | `RtlCompareMemory` | `0x411D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1077 | `OpenFile` | `0x411F0` | 1,414 | UnwindData |  |
| 391 | `ExitProcess` | `0x418A0` | 17 | UnwindData |  |
| 400 | `FatalExit` | `0x418A0` | 17 | UnwindData |  |
| 905 | `HeapValidate` | `0x418C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 491 | `GetCPInfo` | `0x418E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 316 | `DeleteTimerQueueTimer` | `0x41900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `BasepAppXExtension` | `0x41920` | 47 | UnwindData |  |
| 849 | `GetVersion` | `0x41B60` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 836 | `GetTimeZoneInformation` | `0x41BE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1282 | `ResetWriteWatch` | `0x41C00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 676 | `GetModuleHandleExA` | `0x41C20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 611 | `GetEnvironmentStringsW` | `0x41C40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 448 | `FindStringOrdinal` | `0x41C60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 280 | `CreateTimerQueueTimer` | `0x41C80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1452 | `SetThreadStackGuarantee` | `0x41CA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1099 | `OutputDebugStringA` | `0x41CC0` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 992 | `K32QueryWorkingSet` | `0x41F30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1602 | `WerUnregisterFile` | `0x41F50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `CallbackMayRunLong` | `0x41F70` | 54 | UnwindData |  |
| 323 | `DisableThreadLibraryCalls` | `0x41FB0` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1411 | `SetPriorityClass` | `0x42390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `CancelIo` | `0x423B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 249 | `CreateNamedPipeW` | `0x423D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1564 | `VirtualProtectEx` | `0x423F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1407 | `SetMailslotInfo` | `0x42410` | 128 | UnwindData |  |
| 895 | `HeapCreate` | `0x424A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 862 | `GetWindowsDirectoryW` | `0x424C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 816 | `GetThreadIOPendingFlag` | `0x424E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1087 | `OpenPrivateNamespaceW` | `0x42500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 865 | `GlobalAddAtomA` | `0x42520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 452 | `FlsFree` | `0x42540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 850 | `GetVersionExA` | `0x42560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 468 | `FreeEnvironmentStringsW` | `0x42580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1497 | `TerminateProcess` | `0x425A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 656 | `GetLocaleInfoA` | `0x425C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `BasepGetComputerNameFromNtPath` | `0x425E0` | 1,321 | UnwindData |  |
| 1410 | `SetNamedPipeHandleState` | `0x42B10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 565 | `GetCurrentActCtx` | `0x42B30` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 993 | `K32QueryWorkingSetEx` | `0x42BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1275 | `ReplaceFile` | `0x42BE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1277 | `ReplaceFileW` | `0x42BE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1521 | `TransactNamedPipe` | `0x42C00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 884 | `GlobalSize` | `0x42C20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1078 | `OpenFileById` | `0x42C40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 274 | `CreateThreadpoolCleanupGroup` | `0x42C60` | 65 | UnwindData |  |
| 362 | `EnumResourceLanguagesW` | `0x42CB0` | 47 | UnwindData |  |
| 642 | `GetFirmwareType` | `0x42CF0` | 135 | UnwindData |  |
| 1013 | `LoadLibraryA` | `0x42D80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1171 | `QuirkIsEnabledForPackage2Worker` | `0x42DA0` | 39 | UnwindData |  |
| 984 | `K32GetModuleInformation` | `0x42DD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1146 | `QueryFullProcessImageNameA` | `0x42DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 261 | `CreateRemoteThread` | `0x42E10` | 67 | UnwindData |  |
| 204 | `CreateBoundaryDescriptorW` | `0x42E60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 686 | `GetNamedPipeHandleStateA` | `0x42E80` | 406 | UnwindData |  |
| 1423 | `SetProcessShutdownParameters` | `0x43020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `CheckElevationEnabled` | `0x43040` | 65 | UnwindData |  |
| 1157 | `QueryProcessCycleTime` | `0x43090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1527 | `TzSpecificLocalTimeToSystemTime` | `0x430B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 234 | `CreateHardLinkTransactedW` | `0x430D0` | 189 | UnwindData |  |
| 891 | `Heap32ListNext` | `0x431A0` | 235 | UnwindData |  |
| 896 | `HeapDestroy` | `0x432A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 982 | `K32GetModuleFileNameExA` | `0x432C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1638 | `WritePrivateProfileStringA` | `0x432E0` | 100 | UnwindData |  |
| 303 | `DeleteBoundaryDescriptor` | `0x43350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 439 | `FindNextVolumeA` | `0x43370` | 352 | UnwindData |  |
| 1558 | `VirtualAllocEx` | `0x434E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 843 | `GetUserDefaultLangID` | `0x43500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 327 | `DisconnectNamedPipe` | `0x43520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 834 | `GetTimeFormatW` | `0x43540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 872 | `GlobalFindAtomA` | `0x43560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1505 | `TermsrvGetWindowsDirectoryA` | `0x43580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 971 | `K32EnumProcessModules` | `0x435A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1370 | `SetEnvironmentVariableA` | `0x435C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1615 | `Wow64DisableWow64FsRedirection` | `0x435E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1465 | `SetUnhandledExceptionFilter` | `0x43600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 172 | `CmdBatNotification` | `0x43620` | 122 | UnwindData |  |
| 726 | `GetPrivateProfileSectionA` | `0x43710` | 183 | UnwindData |  |
| 1053 | `MoveFileExW` | `0x437D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 986 | `K32GetProcessImageFileNameA` | `0x437F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 757 | `GetProductInfo` | `0x43810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `AddSIDToBoundaryDescriptor` | `0x43830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1457 | `SetThreadpoolThreadMinimum` | `0x43850` | 54 | UnwindData |  |
| 1594 | `WerRegisterRuntimeExceptionModule` | `0x43890` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1371 | `SetEnvironmentVariableW` | `0x43940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 662 | `GetLogicalProcessorInformation` | `0x43960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1412 | `SetProcessAffinityMask` | `0x43980` | 62 | UnwindData |  |
| 785 | `GetSystemDirectoryA` | `0x439D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 740 | `GetProcessHandleCount` | `0x439E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 464 | `FormatMessageA` | `0x43A00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1211 | `RegEnumKeyExA` | `0x43A20` | 67 | UnwindData |  |
| 981 | `K32GetModuleBaseNameW` | `0x43A70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 273 | `CreateThreadpool` | `0x43A90` | 68 | UnwindData |  |
| 520 | `GetComputerNameExW` | `0x43AE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1360 | `SetCurrentDirectoryW` | `0x43B00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `BasepAppContainerEnvironmentExtension` | `0x43B20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 901 | `HeapSetInformation` | `0x43B30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1551 | `VerLanguageNameW` | `0x43B50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `BaseFreeAppCompatDataForProcessWorker` | `0x43B70` | 45 | UnwindData |  |
| 1676 | `lstrcpynW` | `0x43BB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 845 | `GetUserDefaultUILanguage` | `0x43BD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 961 | `IsValidLocale` | `0x43BF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 606 | `GetDynamicTimeZoneInformation` | `0x43C10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 889 | `Heap32First` | `0x43C30` | 640 | UnwindData |  |
| 1442 | `SetThreadGroupAffinity` | `0x43EC0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 588 | `GetDateFormatEx` | `0x43F40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 973 | `K32EnumProcesses` | `0x43F60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1485 | `SortCloseHandle` | `0x43F80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1295 | `RtlFillMemory` | `0x43FB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 517 | `GetCompressedFileSizeW` | `0x43FD0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 230 | `CreateFileTransactedW` | `0x44020` | 352 | UnwindData |  |
| 1395 | `SetHandleCount` | `0x44190` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 349 | `EnumCalendarInfoExEx` | `0x441A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `BindIoCompletionCallback` | `0x441C0` | 42 | UnwindData |  |
| 593 | `GetDevicePowerState` | `0x441F0` | 77 | UnwindData |  |
| 1604 | `WerUnregisterMemoryBlock` | `0x44250` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `BasepPostSuccessAppXExtension` | `0x44270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1641 | `WritePrivateProfileStructW` | `0x44290` | 360 | UnwindData |  |
| 589 | `GetDateFormatW` | `0x448B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1141 | `QueryActCtxW` | `0x448D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1117 | `PrivCopyFileExW` | `0x448F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 833 | `GetTimeFormatEx` | `0x44910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 821 | `GetThreadPreferredUILanguages` | `0x44930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 972 | `K32EnumProcessModulesEx` | `0x44950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1592 | `WerRegisterMemoryBlock` | `0x44970` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | `CreateActCtxW` | `0x44990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 711 | `GetOEMCP` | `0x449B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `BasepReleaseAppXContext` | `0x449D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 950 | `IsNormalizedString` | `0x449F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 788 | `GetSystemFirmwareTable` | `0x44A10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1180 | `ReOpenFile` | `0x44A30` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1454 | `SetThreadUILanguage` | `0x44AD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 995 | `LCMapStringA` | `0x44AF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 759 | `GetProfileIntW` | `0x44B10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1570 | `WaitForDebugEvent` | `0x44B20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1030 | `LocalReAlloc` | `0x44B40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 799 | `GetSystemWindowsDirectoryW` | `0x44B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 243 | `CreateMemoryResourceNotification` | `0x44B70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 279 | `CreateTimerQueue` | `0x44B90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `BaseCheckAppcompatCacheExWorker` | `0x44BB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `BaseCheckAppcompatCacheWorker` | `0x44BB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `BaseIsAppcompatInfrastructureDisabled` | `0x44BB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `BaseIsAppcompatInfrastructureDisabledWorker` | `0x44BB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1553 | `VerifyConsoleIoHandle` | `0x44BB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1036 | `LocateXStateFeature` | `0x44BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 861 | `GetWindowsDirectoryA` | `0x44BE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 462 | `FoldStringW` | `0x44C00` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1674 | `lstrcpyn` | `0x44C90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1675 | `lstrcpynA` | `0x44C90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1286 | `ResolveLocaleName` | `0x44CB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 883 | `GlobalReAlloc` | `0x44CD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `CancelDeviceWakeupRequest` | `0x44CF0` | 22 | UnwindData |  |
| 1279 | `RequestDeviceWakeup` | `0x44CF0` | 22 | UnwindData |  |
| 1280 | `RequestWakeupLatency` | `0x44CF0` | 22 | UnwindData |  |
| 1408 | `SetMessageWaitingIndicator` | `0x44CF0` | 22 | UnwindData |  |
| 473 | `FreeResource` | `0x44D10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1588 | `WerRegisterCustomMetadata` | `0x44D30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1200 | `RegCloseKey` | `0x44D50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 187 | `ConvertNLSDayOfWeekToWin32DayOfWeek` | `0x44D70` | 49 | UnwindData |  |
| 696 | `GetNumaHighestNodeNumber` | `0x44DB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 954 | `IsSystemResumeAutomatic` | `0x44DD0` | 25 | UnwindData |  |
| 1218 | `RegGetValueW` | `0x44EC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 410 | `FindActCtxSectionStringW` | `0x44EE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1311 | `SearchPathW` | `0x44F00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1253 | `ReleaseActCtx` | `0x44F20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1241 | `RegisterApplicationRecoveryCallback` | `0x44F40` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 254 | `CreateProcessA` | `0x44F70` | 95 | UnwindData |  |
| 794 | `GetSystemTimeAdjustment` | `0x44FE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 161 | `ClosePrivateNamespace` | `0x45000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 980 | `K32GetModuleBaseNameA` | `0x45020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 784 | `GetSystemDefaultUILanguage` | `0x45040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 815 | `GetThreadGroupAffinity` | `0x45060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `BaseGetNamedObjectDirectory` | `0x45080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1212 | `RegEnumKeyExW` | `0x450A0` | 67 | UnwindData |  |
| 1438 | `SetThreadContext` | `0x450F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 631 | `GetFileMUIPath` | `0x45110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1226 | `RegOpenKeyExW` | `0x45130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1427 | `SetSearchPathMode` | `0x45150` | 42 | UnwindData |  |
| 1224 | `RegOpenCurrentUser` | `0x45180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1447 | `SetThreadPreferredUILanguages` | `0x451A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1231 | `RegQueryValueExW` | `0x451C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `AddIntegrityLabelToBoundaryDescriptor` | `0x451E0` | 42 | UnwindData |  |
| 1561 | `VirtualFreeEx` | `0x45210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `CheckRemoteDebuggerPresent` | `0x45230` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `ConvertDefaultLocale` | `0x45530` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 814 | `GetThreadErrorMode` | `0x45600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 690 | `GetNamedPipeServerSessionId` | `0x45620` | 53 | UnwindData |  |
| 1559 | `VirtualAllocExNuma` | `0x45660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 315 | `DeleteTimerQueueEx` | `0x45680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1606 | `WerUnregisterRuntimeExceptionModule` | `0x456A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 985 | `K32GetPerformanceInfo` | `0x456C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 847 | `GetUserPreferredUILanguages` | `0x456E0` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `AddAtomA` | `0x458D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 195 | `CopyFileExW` | `0x458F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1082 | `OpenJobObjectW` | `0x45910` | 217 | UnwindData |  |
| 1192 | `ReadDirectoryChangesExW` | `0x459F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1289 | `RtlAddFunctionTable` | `0x45A10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 428 | `FindFirstVolumeA` | `0x45A30` | 353 | UnwindData |  |
| 361 | `EnumResourceLanguagesExW` | `0x45BA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 382 | `EnumTimeFormatsEx` | `0x45BC0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `ChangeTimerQueueTimer` | `0x45CA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 251 | `CreatePipe` | `0x45CC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1136 | `PssWalkSnapshot` | `0x45CE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1619 | `Wow64RevertWow64FsRedirection` | `0x45D00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1444 | `SetThreadIdealProcessorEx` | `0x45D20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 685 | `GetNamedPipeClientSessionId` | `0x45D40` | 77 | UnwindData |  |
| 1498 | `TerminateThread` | `0x45DA0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 774 | `GetStringTypeA` | `0x45EB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 775 | `GetStringTypeExA` | `0x45EB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 570 | `GetCurrentDirectoryA` | `0x45ED0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 907 | `IdnToAscii` | `0x45FF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 493 | `GetCPInfoExW` | `0x46010` | 1,968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `BasepGetPackagedAppInfoForFile` | `0x467C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 875 | `GlobalFlags` | `0x467E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 967 | `K32EmptyWorkingSet` | `0x46800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 379 | `EnumSystemLocalesEx` | `0x46820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 761 | `GetProfileSectionW` | `0x46840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 758 | `GetProfileIntA` | `0x46850` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1646 | `WriteProfileStringW` | `0x468E0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 235 | `CreateHardLinkW` | `0x469D0` | 1,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1230 | `RegQueryValueExA` | `0x46EF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 722 | `GetPhysicallyInstalledSystemMemory` | `0x46F10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 898 | `HeapLock` | `0x46F30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1225 | `RegOpenKeyExA` | `0x46F50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 798 | `GetSystemWindowsDirectoryA` | `0x46F70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1203 | `RegCreateKeyExW` | `0x46F80` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 975 | `K32GetDeviceDriverBaseNameW` | `0x472D0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `ContinueDebugEvent` | `0x47390` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 354 | `EnumDateFormatsExEx` | `0x47580` | 1,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 916 | `InitializeContext` | `0x47A20` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 607 | `GetEnabledXStateFeatures` | `0x47C10` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1229 | `RegQueryInfoKeyW` | `0x47E20` | 121 | UnwindData |  |
| 1596 | `WerSetFlags` | `0x47EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1597 | `WerSetFlagsWorker` | `0x47EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 899 | `HeapQueryInformation` | `0x47EB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 828 | `GetThreadUILanguage` | `0x47ED0` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 652 | `GetLargePageMinimum` | `0x480F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1294 | `RtlDeleteFunctionTable` | `0x48110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 754 | `GetProcessWorkingSetSizeEx` | `0x48130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1476 | `SetXStateFeaturesMask` | `0x48150` | 10,816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 281 | `CreateToolhelp32Snapshot` | `0x4AB90` | 934 | UnwindData |  |
| 1609 | `WerpInitiateRemoteRecovery` | `0x4BA50` | 17 | UnwindData |  |
| 618 | `GetExpandedNameA` | `0x4CCC0` | 244 | UnwindData |  |
| 1403 | `SetLocalPrimaryComputerNameW` | `0x4D010` | 886 | UnwindData |  |
| 270 | `CreateSymbolicLinkW` | `0x4DF80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1242 | `RegisterApplicationRestart` | `0x4DFA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 739 | `GetProcessGroupAffinity` | `0x4DFC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 672 | `GetMemoryErrorHandlingCapabilities` | `0x4DFE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `BasepGetPackageActivationTokenForFilePath2` | `0x4E000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1227 | `RegOpenUserClassesRoot` | `0x4E010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1584 | `WerGetFlags` | `0x4E030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1585 | `WerGetFlagsWorker` | `0x4E030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 494 | `GetCachedSigningLevel` | `0x4E040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 378 | `EnumSystemLocalesA` | `0x4E060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 373 | `EnumSystemFirmwareTables` | `0x4E080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1422 | `SetProcessPriorityBoost` | `0x4E0A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1312 | `SetCachedSigningLevel` | `0x4E0C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 948 | `IsNLSDefinedString` | `0x4E0E0` | 1,504 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1006 | `LZRead` | `0x4E6C0` | 646 | UnwindData |  |
| 687 | `GetNamedPipeHandleStateW` | `0x4ECA0` | 2,176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 394 | `ExpandEnvironmentStringsA` | `0x4F520` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `Beep` | `0x4F780` | 45 | UnwindData |  |
| 1296 | `RtlInstallFunctionTableCallback` | `0x4F920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 894 | `HeapCompact` | `0x4F940` | 800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `BasepGetPackageActivationTokenForSxS2` | `0x4FC60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 706 | `GetNumberFormatEx` | `0x4FC80` | 832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1302 | `RtlRestoreContext` | `0x4FFC0` | 720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 752 | `GetProcessVersion` | `0x50290` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 679 | `GetNLSVersion` | `0x50300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1617 | `Wow64GetThreadContext` | `0x50320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1538 | `UnregisterApplicationRestart` | `0x50340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1223 | `RegNotifyChangeKeyValue` | `0x50360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1238 | `RegSetValueExW` | `0x50380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 680 | `GetNLSVersionEx` | `0x503A0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 705 | `GetNumberFormatA` | `0x50440` | 899 | UnwindData |  |
| 904 | `HeapUnlock` | `0x50CB0` | 3,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 461 | `FoldStringA` | `0x51920` | 650 | UnwindData |  |
| 974 | `K32GetDeviceDriverBaseNameA` | `0x51D30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1032 | `LocalSize` | `0x51D50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 499 | `GetCalendarInfoA` | `0x51D70` | 595 | UnwindData |  |
| 1057 | `MoveFileWithProgressA` | `0x52740` | 29 | UnwindData |  |
| 592 | `GetDefaultCommConfigW` | `0x52770` | 316 | UnwindData |  |
| 1222 | `RegLoadMUIStringW` | `0x52BD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `BeginUpdateResourceW` | `0x52BF0` | 633 | UnwindData |  |
| 111 | `BasepQueryModuleChpeSettings` | `0x52E70` | 594 | UnwindData |  |
| 1381 | `SetFileBandwidthReservation` | `0x53240` | 322 | UnwindData |  |
| 917 | `InitializeContext2` | `0x53390` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 976 | `K32GetDeviceDriverFileNameA` | `0x53600` | 2,448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 393 | `ExitVDM` | `0x53F90` | 168 | UnwindData |  |
| 77 | `BaseUpdateVDMEntry` | `0x541D0` | 267 | UnwindData |  |
| 275 | `CreateThreadpoolIo` | `0x542F0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `AreShortNamesEnabled` | `0x543D0` | 304 | UnwindData |  |
| 174 | `CommConfigDialogW` | `0x54A20` | 329 | UnwindData |  |
| 791 | `GetSystemPreferredUILanguages` | `0x54C80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 586 | `GetDateFormatA` | `0x54CA0` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1428 | `SetStdHandle` | `0x54E10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 294 | `DebugBreak` | `0x54E30` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 269 | `CreateSymbolicLinkTransactedW` | `0x54FE0` | 175 | UnwindData |  |
| 1250 | `RegisterWaitUntilOOBECompleted` | `0x550A0` | 388 | UnwindData |  |
| 492 | `GetCPInfoExA` | `0x55330` | 225 | UnwindData |  |
| 44 | `BackupSeek` | `0x55420` | 497 | UnwindData |  |
| 505 | `GetComPlusPackageInstallStatus` | `0x55620` | 66 | UnwindData |  |
| 89 | `BasepCopyEncryption` | `0x55760` | 228 | UnwindData |  |
| 335 | `DuplicateEncryptionInfoFileExt` | `0x55EA0` | 237 | UnwindData |  |
| 1148 | `QueryIdleProcessorCycleTime` | `0x561E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `CheckNameLegalDOS8Dot3A` | `0x56200` | 173 | UnwindData |  |
| 253 | `CreatePrivateNamespaceW` | `0x562C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 519 | `GetComputerNameExA` | `0x562E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 977 | `K32GetDeviceDriverFileNameW` | `0x56300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1249 | `RegisterWaitForSingleObjectEx` | `0x56320` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 381 | `EnumTimeFormatsA` | `0x56400` | 112 | UnwindData |  |
| 1097 | `OpenWaitableTimerA` | `0x566A0` | 114 | UnwindData |  |
| 998 | `LZClose` | `0x56720` | 185 | UnwindData |  |
| 910 | `InitAtomTable` | `0x567E0` | 109 | UnwindData |  |
| 376 | `EnumSystemLanguageGroupsA` | `0x56860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1210 | `RegDisablePredefinedCacheEx` | `0x56880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1589 | `WerRegisterExcludedMemoryBlock` | `0x568A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1406 | `SetLocaleInfoW` | `0x568C0` | 832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1290 | `RtlCaptureContext` | `0x56C00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1299 | `RtlMoveMemory` | `0x56C30` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `BaseFormatObjectAttributes` | `0x56DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 856 | `GetVolumeNameForVolumeMountPointW` | `0x56DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 745 | `GetProcessInformation` | `0x56DE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 819 | `GetThreadInformation` | `0x56DF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1419 | `SetProcessInformation` | `0x56E00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1445 | `SetThreadInformation` | `0x56E10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 753 | `GetProcessWorkingSetSize` | `0x56E20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1424 | `SetProcessWorkingSetSize` | `0x56E30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 158 | `CloseHandle` | `0x56E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 336 | `DuplicateHandle` | `0x56E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 650 | `GetHandleInformation` | `0x56E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1396 | `SetHandleInformation` | `0x56E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `CancelWaitableTimer` | `0x56E80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 215 | `CreateEventA` | `0x56E90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 216 | `CreateEventExA` | `0x56EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 217 | `CreateEventExW` | `0x56EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 218 | `CreateEventW` | `0x56EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 244 | `CreateMutexA` | `0x56ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 245 | `CreateMutexExA` | `0x56EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 246 | `CreateMutexExW` | `0x56EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 247 | `CreateMutexW` | `0x56F00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 265 | `CreateSemaphoreExW` | `0x56F10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 266 | `CreateSemaphoreW` | `0x56F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 286 | `CreateWaitableTimerExW` | `0x56F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 919 | `InitializeCriticalSectionAndSpinCount` | `0x56F40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 920 | `InitializeCriticalSectionEx` | `0x56F50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1075 | `OpenEventA` | `0x56F60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1076 | `OpenEventW` | `0x56F70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1084 | `OpenMutexW` | `0x56F80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1092 | `OpenSemaphoreW` | `0x56F90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1098 | `OpenWaitableTimerW` | `0x56FA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1255 | `ReleaseMutex` | `0x56FB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1261 | `ReleaseSemaphore` | `0x56FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1281 | `ResetEvent` | `0x56FD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1373 | `SetEvent` | `0x56FE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1474 | `SetWaitableTimer` | `0x56FF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1484 | `SleepEx` | `0x57000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1572 | `WaitForMultipleObjects` | `0x57010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1573 | `WaitForMultipleObjectsEx` | `0x57020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1574 | `WaitForSingleObject` | `0x57030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1575 | `WaitForSingleObjectEx` | `0x57040` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `CompareFileTime` | `0x57070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | `CreateDirectory2A` | `0x57080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 207 | `CreateDirectory2W` | `0x57090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 208 | `CreateDirectoryA` | `0x570A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 213 | `CreateDirectoryW` | `0x570B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 221 | `CreateFile2` | `0x570C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `CreateFile3` | `0x570D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 223 | `CreateFileA` | `0x570E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 231 | `CreateFileW` | `0x570F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 300 | `DefineDosDeviceW` | `0x57100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 306 | `DeleteFile2A` | `0x57110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 307 | `DeleteFile2W` | `0x57120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 308 | `DeleteFileA` | `0x57130` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 311 | `DeleteFileW` | `0x57140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 320 | `DeleteVolumeMountPointW` | `0x57150` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 402 | `FileTimeToLocalFileTime` | `0x57160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 414 | `FindClose` | `0x57170` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 415 | `FindCloseChangeNotification` | `0x57180` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 416 | `FindFirstChangeNotificationA` | `0x57190` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 417 | `FindFirstChangeNotificationW` | `0x571A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 418 | `FindFirstFileA` | `0x571B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 419 | `FindFirstFileExA` | `0x571C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 420 | `FindFirstFileExW` | `0x571D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 422 | `FindFirstFileNameW` | `0x571E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 425 | `FindFirstFileW` | `0x571F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 431 | `FindFirstVolumeW` | `0x57200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 434 | `FindNextChangeNotification` | `0x57210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 435 | `FindNextFileA` | `0x57220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 436 | `FindNextFileNameW` | `0x57230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 437 | `FindNextFileW` | `0x57240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 442 | `FindNextVolumeW` | `0x57250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 449 | `FindVolumeClose` | `0x57260` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 457 | `FlushFileBuffers` | `0x57270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 594 | `GetDiskFreeSpaceA` | `0x57280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 595 | `GetDiskFreeSpaceExA` | `0x57290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 596 | `GetDiskFreeSpaceExW` | `0x572A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 597 | `GetDiskFreeSpaceW` | `0x572B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 602 | `GetDriveTypeA` | `0x572C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 603 | `GetDriveTypeW` | `0x572D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 620 | `GetFileAttributesA` | `0x572E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 621 | `GetFileAttributesExA` | `0x572F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 622 | `GetFileAttributesExW` | `0x57300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 625 | `GetFileAttributesW` | `0x57310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 627 | `GetFileInformationByHandle` | `0x57320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 632 | `GetFileSize` | `0x57330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 633 | `GetFileSizeEx` | `0x57340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 634 | `GetFileTime` | `0x57350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 635 | `GetFileType` | `0x57360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 636 | `GetFinalPathNameByHandleA` | `0x57370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 637 | `GetFinalPathNameByHandleW` | `0x57380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 643 | `GetFullPathNameA` | `0x57390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 646 | `GetFullPathNameW` | `0x573A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 660 | `GetLogicalDriveStringsW` | `0x573B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 805 | `GetTempFileNameA` | `0x573C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 806 | `GetTempFileNameW` | `0x573D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 807 | `GetTempPath2A` | `0x573E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 808 | `GetTempPath2W` | `0x573F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 809 | `GetTempPathA` | `0x57400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 810 | `GetTempPathW` | `0x57410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 852 | `GetVolumeInformationA` | `0x57420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 853 | `GetVolumeInformationByHandleW` | `0x57430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 854 | `GetVolumeInformationW` | `0x57440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 858 | `GetVolumePathNameW` | `0x57450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 860 | `GetVolumePathNamesForVolumeNameW` | `0x57460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1024 | `LocalFileTimeToFileTime` | `0x57470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1037 | `LockFile` | `0x57480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1038 | `LockFileEx` | `0x57490` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1145 | `QueryDosDeviceW` | `0x574A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1194 | `ReadFile` | `0x574B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1195 | `ReadFileEx` | `0x574C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1196 | `ReadFileScatter` | `0x574D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1263 | `RemoveDirectory2A` | `0x574E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1264 | `RemoveDirectory2W` | `0x574F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1265 | `RemoveDirectoryA` | `0x57500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1268 | `RemoveDirectoryW` | `0x57510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1367 | `SetEndOfFile` | `0x57520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1377 | `SetFileAttributesA` | `0x57530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1380 | `SetFileAttributesW` | `0x57540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1383 | `SetFileInformationByHandle` | `0x57550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1385 | `SetFilePointer` | `0x57560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1386 | `SetFilePointerEx` | `0x57570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1389 | `SetFileTime` | `0x57580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1390 | `SetFileValidData` | `0x57590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1533 | `UnlockFile` | `0x575A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1534 | `UnlockFileEx` | `0x575B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1633 | `WriteFile` | `0x575C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1634 | `WriteFileEx` | `0x575D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1635 | `WriteFileGather` | `0x575E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 314 | `DeleteTimerQueue` | `0x575F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1059 | `MulDiv` | `0x57600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 363 | `EnumResourceNamesA` | `0x57610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 366 | `EnumResourceNamesW` | `0x57620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1018 | `LoadPackagedLibrary` | `0x57630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `CallNamedPipeW` | `0x57640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 796 | `GetSystemTimePreciseAsFileTime` | `0x57650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 403 | `FileTimeToSystemTime` | `0x57660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 500 | `GetCalendarInfoEx` | `0x57670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 501 | `GetCalendarInfoW` | `0x57680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 610 | `GetEnvironmentStringsA` | `0x57690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `ClearCommBreak` | `0x576A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `ClearCommError` | `0x576B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 389 | `EscapeCommFunction` | `0x576C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 506 | `GetCommConfig` | `0x576D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 507 | `GetCommMask` | `0x576E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 508 | `GetCommModemStatus` | `0x576F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 509 | `GetCommProperties` | `0x57700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 510 | `GetCommState` | `0x57710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 511 | `GetCommTimeouts` | `0x57720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1138 | `PurgeComm` | `0x57730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1316 | `SetCommBreak` | `0x57740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1317 | `SetCommConfig` | `0x57750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1318 | `SetCommMask` | `0x57760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1319 | `SetCommState` | `0x57770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1320 | `SetCommTimeouts` | `0x57780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1477 | `SetupComm` | `0x57790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1522 | `TransmitCommChar` | `0x577A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1569 | `WaitCommEvent` | `0x577B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 800 | `GetSystemWow64DirectoryA` | `0x577C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 801 | `GetSystemWow64DirectoryW` | `0x577D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1616 | `Wow64EnableWow64FsRedirection` | `0x577E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 198 | `CopyFileW` | `0x577F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `ConvertFiberToThread` | `0x57800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 189 | `ConvertThreadToFiber` | `0x57810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `ConvertThreadToFiberEx` | `0x57820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 219 | `CreateFiber` | `0x57830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 220 | `CreateFiberEx` | `0x57840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 305 | `DeleteFiber` | `0x57850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1491 | `SwitchToFiber` | `0x57860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1063 | `NlsCheckPolicy` | `0x57870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1064 | `NlsGetCacheUpdateCount` | `0x57880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1065 | `NlsUpdateLocale` | `0x57890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1066 | `NlsUpdateSystemLocale` | `0x578A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `AllocConsole` | `0x578B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `AllocConsoleWithOptions` | `0x578C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `AttachConsole` | `0x578D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 163 | `ClosePseudoConsole` | `0x578E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 260 | `CreatePseudoConsole` | `0x578F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 466 | `FreeConsole` | `0x57900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 532 | `GetConsoleCP` | `0x57910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 550 | `GetConsoleMode` | `0x57920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 554 | `GetConsoleOutputCP` | `0x57930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 709 | `GetNumberOfConsoleInputEvents` | `0x57940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1107 | `PeekConsoleInputA` | `0x57950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1108 | `PeekConsoleInputW` | `0x57960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1181 | `ReadConsoleA` | `0x57970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1182 | `ReadConsoleInputA` | `0x57980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1185 | `ReadConsoleInputW` | `0x57990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1191 | `ReadConsoleW` | `0x579A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1258 | `ReleasePseudoConsole` | `0x579B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1283 | `ResizePseudoConsole` | `0x579C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1328 | `SetConsoleCtrlHandler` | `0x579D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1344 | `SetConsoleMode` | `0x579E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1622 | `WriteConsoleA` | `0x579F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1632 | `WriteConsoleW` | `0x57A00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 205 | `CreateConsoleScreenBuffer` | `0x57A10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 404 | `FillConsoleOutputAttribute` | `0x57A20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 405 | `FillConsoleOutputCharacterA` | `0x57A30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 406 | `FillConsoleOutputCharacterW` | `0x57A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 456 | `FlushConsoleInputBuffer` | `0x57A50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 475 | `GenerateConsoleCtrlEvent` | `0x57A60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 538 | `GetConsoleCursorInfo` | `0x57A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 552 | `GetConsoleOriginalTitleA` | `0x57A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 553 | `GetConsoleOriginalTitleW` | `0x57A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 556 | `GetConsoleScreenBufferInfo` | `0x57AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 557 | `GetConsoleScreenBufferInfoEx` | `0x57AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 559 | `GetConsoleTitleA` | `0x57AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 560 | `GetConsoleTitleW` | `0x57AD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 653 | `GetLargestConsoleWindowSize` | `0x57AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1186 | `ReadConsoleOutputA` | `0x57AF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1187 | `ReadConsoleOutputAttribute` | `0x57B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1188 | `ReadConsoleOutputCharacterA` | `0x57B10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1189 | `ReadConsoleOutputCharacterW` | `0x57B20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1190 | `ReadConsoleOutputW` | `0x57B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1308 | `ScrollConsoleScreenBufferA` | `0x57B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1309 | `ScrollConsoleScreenBufferW` | `0x57B50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1326 | `SetConsoleActiveScreenBuffer` | `0x57B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1327 | `SetConsoleCP` | `0x57B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1330 | `SetConsoleCursorInfo` | `0x57B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1332 | `SetConsoleCursorPosition` | `0x57B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1349 | `SetConsoleOutputCP` | `0x57BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1351 | `SetConsoleScreenBufferInfoEx` | `0x57BB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1352 | `SetConsoleScreenBufferSize` | `0x57BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1353 | `SetConsoleTextAttribute` | `0x57BD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1354 | `SetConsoleTitleA` | `0x57BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1355 | `SetConsoleTitleW` | `0x57BF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1356 | `SetConsoleWindowInfo` | `0x57C00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1623 | `WriteConsoleInputA` | `0x57C10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1626 | `WriteConsoleInputW` | `0x57C20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1627 | `WriteConsoleOutputA` | `0x57C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1628 | `WriteConsoleOutputAttribute` | `0x57C40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1629 | `WriteConsoleOutputCharacterA` | `0x57C50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1630 | `WriteConsoleOutputCharacterW` | `0x57C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1631 | `WriteConsoleOutputW` | `0x57C70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `AddConsoleAliasA` | `0x57C80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `AddConsoleAliasW` | `0x57C90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 396 | `ExpungeConsoleCommandHistoryA` | `0x57CA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 397 | `ExpungeConsoleCommandHistoryW` | `0x57CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 522 | `GetConsoleAliasA` | `0x57CC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 523 | `GetConsoleAliasExesA` | `0x57CD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 524 | `GetConsoleAliasExesLengthA` | `0x57CE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 525 | `GetConsoleAliasExesLengthW` | `0x57CF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 526 | `GetConsoleAliasExesW` | `0x57D00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 527 | `GetConsoleAliasW` | `0x57D10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 528 | `GetConsoleAliasesA` | `0x57D20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 529 | `GetConsoleAliasesLengthA` | `0x57D30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 530 | `GetConsoleAliasesLengthW` | `0x57D40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 531 | `GetConsoleAliasesW` | `0x57D50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 534 | `GetConsoleCommandHistoryA` | `0x57D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 535 | `GetConsoleCommandHistoryLengthA` | `0x57D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 536 | `GetConsoleCommandHistoryLengthW` | `0x57D80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 537 | `GetConsoleCommandHistoryW` | `0x57D90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 540 | `GetConsoleDisplayMode` | `0x57DA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 542 | `GetConsoleFontSize` | `0x57DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 544 | `GetConsoleHistoryInfo` | `0x57DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 555 | `GetConsoleProcessList` | `0x57DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 558 | `GetConsoleSelectionInfo` | `0x57DE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 561 | `GetConsoleWindow` | `0x57DF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 568 | `GetCurrentConsoleFont` | `0x57E00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 569 | `GetCurrentConsoleFontEx` | `0x57E10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 710 | `GetNumberOfConsoleMouseButtons` | `0x57E20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1333 | `SetConsoleDisplayMode` | `0x57E30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1336 | `SetConsoleHistoryInfo` | `0x57E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1346 | `SetConsoleNumberOfCommandsA` | `0x57E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1347 | `SetConsoleNumberOfCommandsW` | `0x57E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1358 | `SetCurrentConsoleFontEx` | `0x57E70` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `ActivatePackageVirtualizationContext` | `0x57F60` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 250 | `CreatePackageVirtualizationContext` | `0x58000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 291 | `DeactivatePackageVirtualizationContext` | `0x58020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 337 | `DuplicatePackageVirtualizationContext` | `0x58040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 577 | `GetCurrentPackageVirtualizationContext` | `0x58060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 755 | `GetProcessesInVirtualizationContext` | `0x58080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1257 | `ReleasePackageVirtualizationContext` | `0x580A0` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1687 | `uaw_lstrlenW` | `0x58210` | 28 | UnwindData |  |
| 1688 | `uaw_wcschr` | `0x58240` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1689 | `uaw_wcscpy` | `0x58270` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1690 | `uaw_wcsicmp` | `0x582A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1691 | `uaw_wcslen` | `0x582C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1692 | `uaw_wcsrchr` | `0x582F0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 949 | `IsNativeVhdBoot` | `0x58380` | 271 | UnwindData |  |
| 199 | `CopyLZFile` | `0x584A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1000 | `LZCopy` | `0x584B0` | 259 | UnwindData |  |
| 57 | `BaseDumpAppcompatCacheWorker` | `0x585C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1002 | `LZDone` | `0x585C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1530 | `UTUnRegister` | `0x585C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `BaseCleanupAppcompatCacheSupportWorker` | `0x585D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `BaseInitAppcompatCacheSupportWorker` | `0x585D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 162 | `CloseProfileUserMapping` | `0x585D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1008 | `LZStart` | `0x585D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1090 | `OpenProfileUserMapping` | `0x585D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1342 | `SetConsoleMaximumWindowSize` | `0x585D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 644 | `GetFullPathNameTransactedA` | `0x585E0` | 182 | UnwindData |  |
| 1433 | `SetSystemTimeAdjustment` | `0x586A0` | 69 | UnwindData |  |
| 295 | `DebugBreakProcess` | `0x586F0` | 42 | UnwindData |  |
| 296 | `DebugSetProcessKillOnExit` | `0x58720` | 105 | UnwindData |  |
| 1618 | `Wow64GetThreadSelectorEntry` | `0x58790` | 106 | UnwindData |  |
| 211 | `CreateDirectoryTransactedA` | `0x58800` | 168 | UnwindData |  |
| 1266 | `RemoveDirectoryTransactedA` | `0x588B0` | 75 | UnwindData |  |
| 421 | `FindFirstFileNameTransactedW` | `0x58910` | 187 | UnwindData |  |
| 423 | `FindFirstFileTransactedA` | `0x589E0` | 205 | UnwindData |  |
| 426 | `FindFirstStreamTransactedW` | `0x58AC0` | 187 | UnwindData |  |
| 626 | `GetFileBandwidthReservation` | `0x58B90` | 190 | UnwindData |  |
| 1387 | `SetFileShortNameA` | `0x58C60` | 72 | UnwindData |  |
| 1388 | `SetFileShortNameW` | `0x58CB0` | 317 | UnwindData |  |
| 608 | `GetEncryptedFileVersionExt` | `0x59030` | 237 | UnwindData |  |
| 19 | `AddSecureMemoryCacheCallback` | `0x59130` | 42 | UnwindData |  |
| 870 | `GlobalCompact` | `0x59160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1023 | `LocalCompact` | `0x59160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1031 | `LocalShrink` | `0x59160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 874 | `GlobalFix` | `0x59180` | 28 | UnwindData |  |
| 886 | `GlobalUnfix` | `0x591B0` | 28 | UnwindData |  |
| 1251 | `RegisterWowBaseHandlers` | `0x591E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1272 | `RemoveSecureMemoryCacheCallback` | `0x591F0` | 25 | UnwindData |  |
| 1021 | `LoadStringBaseW` | `0x59210` | 29 | UnwindData |  |
| 359 | `EnumResourceLanguagesA` | `0x59240` | 47 | UnwindData |  |
| 367 | `EnumResourceTypesA` | `0x59280` | 33 | UnwindData |  |
| 370 | `EnumResourceTypesW` | `0x592B0` | 33 | UnwindData |  |
| 600 | `GetDllDirectoryA` | `0x592E0` | 393 | UnwindData |  |
| 1529 | `UTRegister` | `0x59480` | 135 | UnwindData |  |
| 1409 | `SetNamedPipeAttribute` | `0x59510` | 528 | UnwindData |  |
| 694 | `GetNumaAvailableMemoryNode` | `0x59730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 697 | `GetNumaNodeNumberFromHandle` | `0x59740` | 99 | UnwindData |  |
| 703 | `GetNumaProximityNode` | `0x597B0` | 59 | UnwindData |  |
| 85 | `BasepCheckPplSupport` | `0x59800` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `BasepFinishPackageActivation` | `0x59840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `BasepGetPackageActivationTokenForFilePath` | `0x59850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `BasepGetPackageActivationTokenForSxS` | `0x59850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `BasepProcessInvalidImage` | `0x59860` | 1,821 | UnwindData |  |
| 113 | `BasepReleasePackagedAppInfo` | `0x59F90` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 736 | `GetProcessDEPPolicy` | `0x5A180` | 76 | UnwindData |  |
| 780 | `GetSystemDEPPolicy` | `0x5A1E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 792 | `GetSystemRegistryQuota` | `0x5A220` | 134 | UnwindData |  |
| 934 | `IsBadHugeReadPtr` | `0x5A2B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 935 | `IsBadHugeWritePtr` | `0x5A2C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1070 | `NtVdm64CreateProcessInternalW` | `0x5A2D0` | 513 | UnwindData |  |
| 1179 | `RaiseInvalid16BitExeError` | `0x5A4E0` | 278 | UnwindData |  |
| 1414 | `SetProcessDEPPolicy` | `0x5A600` | 51 | UnwindData |  |
| 1278 | `ReplacePartitionUnit` | `0x5A640` | 125 | UnwindData |  |
| 14 | `AddRefActCtx` | `0x5A6D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `AddResourceAttributeAce` | `0x5A6F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `AddScopedPolicyIDAce` | `0x5A710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `AllocateUserPhysicalPagesNuma` | `0x5A730` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `AllocateUserPhysicalPages` | `0x5A750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `BaseCheckAppcompatCacheEx` | `0x5A770` | 85 | UnwindData |  |
| 47 | `BaseCheckAppcompatCache` | `0x5A7D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `BaseCleanupAppcompatCacheSupport` | `0x5A7F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `BaseDumpAppcompatCache` | `0x5A810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `BaseFlushAppcompatCache` | `0x5A830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `BaseInitAppcompatCacheSupport` | `0x5A850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `BaseUpdateAppcompatCache` | `0x5A870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `CancelSynchronousIo` | `0x5A890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `CheckAllowDecryptedRemoteDestinationPolicy` | `0x5A8B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `CheckTokenCapability` | `0x5A8D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `CheckTokenMembershipEx` | `0x5A8F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 191 | `CopyContext` | `0x5A910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 192 | `CopyFile2` | `0x5A930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 210 | `CreateDirectoryExW` | `0x5A950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 227 | `CreateFileMappingNumaW` | `0x5A970` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 232 | `CreateHardLinkA` | `0x5A990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 255 | `CreateProcessAsUserA` | `0x5A9B0` | 107 | UnwindData |  |
| 257 | `CreateProcessInternalA` | `0x5AA30` | 119 | UnwindData |  |
| 258 | `CreateProcessInternalW` | `0x5AAB0` | 119 | UnwindData |  |
| 293 | `DebugActiveProcessStop` | `0x5AB30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 292 | `DebugActiveProcess` | `0x5AB50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 301 | `DelayLoadFailureHook` | `0x5AB70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 313 | `DeleteSynchronizationBarrier` | `0x5AB90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 329 | `DnsHostnameToComputerNameExW` | `0x5ABB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 338 | `EnableProcessOptionalXStateFeatures` | `0x5ABD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 345 | `EnterSynchronizationBarrier` | `0x5ABF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 350 | `EnumCalendarInfoExW` | `0x5AC10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 351 | `EnumCalendarInfoW` | `0x5AC30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 355 | `EnumDateFormatsExW` | `0x5AC50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 356 | `EnumDateFormatsW` | `0x5AC70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 358 | `EnumLanguageGroupLocalesW` | `0x5AC90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 360 | `EnumResourceLanguagesExA` | `0x5ACB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 364 | `EnumResourceNamesExA` | `0x5ACD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 365 | `EnumResourceNamesExW` | `0x5ACF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 368 | `EnumResourceTypesExA` | `0x5AD10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 369 | `EnumResourceTypesExW` | `0x5AD30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 372 | `EnumSystemCodePagesW` | `0x5AD50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 377 | `EnumSystemLanguageGroupsW` | `0x5AD70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 380 | `EnumSystemLocalesW` | `0x5AD90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 383 | `EnumTimeFormatsW` | `0x5ADB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 385 | `EnumUILanguagesW` | `0x5ADD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 398 | `FatalAppExitA` | `0x5ADF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 399 | `FatalAppExitW` | `0x5AE10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 432 | `FindNLSString` | `0x5AE30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 467 | `FreeEnvironmentStringsA` | `0x5AE50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 474 | `FreeUserPhysicalPages` | `0x5AE70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 479 | `GetAppContainerAce` | `0x5AE90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 480 | `GetAppContainerNamedObjectPath` | `0x5AEB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 481 | `GetApplicationRecoveryCallback` | `0x5AED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 483 | `GetApplicationRestartSettings` | `0x5AEF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 514 | `GetCompressedFileSizeA` | `0x5AF10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 563 | `GetCurrencyFormatEx` | `0x5AF30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 564 | `GetCurrencyFormatW` | `0x5AF50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 605 | `GetDurationFormatEx` | `0x5AF60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 609 | `GetEnvironmentStrings` | `0x5AF80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 614 | `GetEraNameCountedString` | `0x5AFA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 629 | `GetFileInformationByName` | `0x5AFC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 630 | `GetFileMUIInfo` | `0x5AFE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 681 | `GetNamedPipeAttribute` | `0x5B000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 683 | `GetNamedPipeClientComputerNameW` | `0x5B020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 700 | `GetNumaNodeProcessorMaskEx` | `0x5B040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 704 | `GetNumaProximityNodeEx` | `0x5B060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 742 | `GetProcessHeaps` | `0x5B080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 748 | `GetProcessPreferredUILanguages` | `0x5B0A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 749 | `GetProcessPriorityBoost` | `0x5B0C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 750 | `GetProcessShutdownParameters` | `0x5B0E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 773 | `GetStringScripts` | `0x5B100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 787 | `GetSystemFileCacheSize` | `0x5B120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 813 | `GetThreadEnabledXStateFeatures` | `0x5B140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 831 | `GetTimeFormatA` | `0x5B160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 837 | `GetTimeZoneInformationForYear` | `0x5B180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 838 | `GetUILanguageInfo` | `0x5B1A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 864 | `GetXStateFeaturesMask` | `0x5B1C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 903 | `HeapSummary` | `0x5B1E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 908 | `IdnToNameprepUnicode` | `0x5B200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 909 | `IdnToUnicode` | `0x5B220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 925 | `InitializeSynchronizationBarrier` | `0x5B240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 960 | `IsValidLanguageGroup` | `0x5B260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 962 | `IsValidLocaleName` | `0x5B280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 963 | `IsValidNLSVersion` | `0x5B2A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 968 | `K32EnumDeviceDrivers` | `0x5B2C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 969 | `K32EnumPageFilesA` | `0x5B2E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 970 | `K32EnumPageFilesW` | `0x5B300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 978 | `K32GetMappedFileNameA` | `0x5B320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 990 | `K32GetWsChangesEx` | `0x5B340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 989 | `K32GetWsChanges` | `0x5B360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 991 | `K32InitializeProcessForWsWatch` | `0x5B380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1020 | `LoadStringBaseExW` | `0x5B3A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1026 | `LocalFlags` | `0x5B3C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1029 | `LocalLock` | `0x5B3E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1034 | `LocalUnlock` | `0x5B400` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1041 | `MapUserPhysicalPages` | `0x5B420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1045 | `MapViewOfFileExNuma` | `0x5B440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1058 | `MoveFileWithProgressW` | `0x5B460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1061 | `NeedCurrentDirectoryForExePathA` | `0x5B480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1062 | `NeedCurrentDirectoryForExePathW` | `0x5B4A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1068 | `NotifyMountMgr` | `0x5B4C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1074 | `OpenConsoleWStub` | `0x5B4E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1124 | `PssCaptureSnapshot` | `0x5B4F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1125 | `PssDuplicateSnapshot` | `0x5B510` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1126 | `PssFreeSnapshot` | `0x5B530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1127 | `PssQuerySnapshot` | `0x5B550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1128 | `PssWalkMarkerCreate` | `0x5B570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1129 | `PssWalkMarkerFree` | `0x5B590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1130 | `PssWalkMarkerGetPosition` | `0x5B5B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1135 | `PssWalkMarkerTell` | `0x5B5B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1131 | `PssWalkMarkerRewind` | `0x5B5D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1133 | `PssWalkMarkerSeekToBeginning` | `0x5B5D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1132 | `PssWalkMarkerSeek` | `0x5B5F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1134 | `PssWalkMarkerSetPosition` | `0x5B5F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1139 | `QueryActCtxSettingsW` | `0x5B610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1149 | `QueryIdleProcessorCycleTimeEx` | `0x5B630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1156 | `QueryProcessAffinityUpdateMode` | `0x5B650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1161 | `QueryThreadpoolStackInformation` | `0x5B670` | 54 | UnwindData |  |
| 1201 | `RegCopyTreeW` | `0x5B6B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1202 | `RegCreateKeyExA` | `0x5B6D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1204 | `RegDeleteKeyExA` | `0x5B6F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1205 | `RegDeleteKeyExW` | `0x5B710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1206 | `RegDeleteTreeA` | `0x5B730` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1207 | `RegDeleteTreeW` | `0x5B750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1208 | `RegDeleteValueA` | `0x5B770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1209 | `RegDeleteValueW` | `0x5B790` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1213 | `RegEnumValueA` | `0x5B7B0` | 67 | UnwindData |  |
| 1214 | `RegEnumValueW` | `0x5B800` | 67 | UnwindData |  |
| 1215 | `RegFlushKey` | `0x5B850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1216 | `RegGetKeySecurity` | `0x5B870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1217 | `RegGetValueA` | `0x5B890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1219 | `RegLoadKeyA` | `0x5B8B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1220 | `RegLoadKeyW` | `0x5B8D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1221 | `RegLoadMUIStringA` | `0x5B8F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1228 | `RegQueryInfoKeyA` | `0x5B910` | 121 | UnwindData |  |
| 1232 | `RegRestoreKeyA` | `0x5B990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1233 | `RegRestoreKeyW` | `0x5B9B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1234 | `RegSaveKeyExA` | `0x5B9D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1235 | `RegSaveKeyExW` | `0x5B9F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1236 | `RegSetKeySecurity` | `0x5BA10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1237 | `RegSetValueExA` | `0x5BA30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1239 | `RegUnLoadKeyA` | `0x5BA50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1240 | `RegUnLoadKeyW` | `0x5BA70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1243 | `RegisterBadMemoryNotification` | `0x5BA90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1293 | `RtlCopyMemory` | `0x5BAB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1301 | `RtlRaiseException` | `0x5BAC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1306 | `RtlVirtualUnwind2` | `0x5BAE0` | 132 | UnwindData |  |
| 1310 | `SearchPathA` | `0x5BB70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1314 | `SetCalendarInfoW` | `0x5BB90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1321 | `SetComputerNameA` | `0x5BBB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1322 | `SetComputerNameEx2W` | `0x5BBD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1323 | `SetComputerNameExA` | `0x5BBF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1324 | `SetComputerNameExW` | `0x5BC10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1325 | `SetComputerNameW` | `0x5BC30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1359 | `SetCurrentDirectoryA` | `0x5BC50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1366 | `SetDynamicTimeZoneInformation` | `0x5BC70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1369 | `SetEnvironmentStringsW` | `0x5BC90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1375 | `SetFileApisToANSI` | `0x5BCB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1376 | `SetFileApisToOEM` | `0x5BCD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1384 | `SetFileIoOverlappedRange` | `0x5BCF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1404 | `SetLocalTime` | `0x5BD10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1413 | `SetProcessAffinityUpdateMode` | `0x5BD30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1421 | `SetProcessPreferredUILanguages` | `0x5BD50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1425 | `SetProcessWorkingSetSizeEx` | `0x5BD70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1429 | `SetStdHandleEx` | `0x5BD90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1430 | `SetSystemFileCacheSize` | `0x5BDB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1432 | `SetSystemTime` | `0x5BDD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1455 | `SetThreadpoolStackInformation` | `0x5BDF0` | 54 | UnwindData |  |
| 1462 | `SetTimeZoneInformation` | `0x5BE30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1473 | `SetVolumeMountPointWStub` | `0x5BE50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1532 | `UnhandledExceptionFilter` | `0x5BE60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1539 | `UnregisterBadMemoryNotification` | `0x5BE80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1550 | `VerLanguageNameA` | `0x5BEA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1554 | `VerifyScripts` | `0x5BEC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1586 | `WerRegisterAdditionalProcess` | `0x5BEE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1587 | `WerRegisterAppLocalDump` | `0x5BF00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1598 | `WerUnregisterAdditionalProcess` | `0x5BF20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1599 | `WerUnregisterAppLocalDump` | `0x5BF40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1600 | `WerUnregisterCustomMetadata` | `0x5BF60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1601 | `WerUnregisterExcludedMemoryBlock` | `0x5BF80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1620 | `Wow64SetThreadContext` | `0x5BFA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1621 | `Wow64SuspendThread` | `0x5BFC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1648 | `ZombifyActCtx` | `0x5BFE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `CheckForReadOnlyResourceFilter` | `0x5C000` | 79 | UnwindData |  |
| 1520 | `Toolhelp32ReadProcessMemory` | `0x5C060` | 132 | UnwindData |  |
| 619 | `GetExpandedNameW` | `0x5C190` | 285 | UnwindData |  |
| 999 | `LZCloseFile` | `0x5C2C0` | 205 | UnwindData |  |
| 1001 | `LZCreateFileW` | `0x5C3A0` | 316 | UnwindData |  |
| 1003 | `LZInit` | `0x5C4F0` | 479 | UnwindData |  |
| 1004 | `LZOpenFileA` | `0x5C6E0` | 219 | UnwindData |  |
| 1005 | `LZOpenFileW` | `0x5C7D0` | 181 | UnwindData |  |
| 1007 | `LZSeek` | `0x5C890` | 204 | UnwindData |  |
| 173 | `CommConfigDialogA` | `0x5C970` | 144 | UnwindData |  |
| 591 | `GetDefaultCommConfigA` | `0x5CA10` | 144 | UnwindData |  |
| 1361 | `SetDefaultCommConfigA` | `0x5CB40` | 144 | UnwindData |  |
| 1362 | `SetDefaultCommConfigW` | `0x5CBE0` | 329 | UnwindData |  |
| 54 | `BaseDestroyVDMEnvironment` | `0x5E910` | 61 | UnwindData |  |
| 665 | `GetLongPathNameTransactedA` | `0x5EC20` | 168 | UnwindData |  |
| 693 | `GetNextVDMCommand` | `0x5ECD0` | 2,402 | UnwindData |  |
| 848 | `GetVDMCurrentDirectories` | `0x5F640` | 384 | UnwindData |  |
| 1252 | `RegisterWowExec` | `0x5FBE0` | 118 | UnwindData |  |
| 1468 | `SetVDMCurrentDirectories` | `0x5FC60` | 316 | UnwindData |  |
| 1549 | `VDMOperationStarted` | `0x5FF00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 282 | `CreateUmsCompletionList` | `0x5FF20` | 29 | UnwindData |  |
| 283 | `CreateUmsThreadContext` | `0x5FF20` | 29 | UnwindData |  |
| 317 | `DeleteUmsCompletionList` | `0x5FF20` | 29 | UnwindData |  |
| 318 | `DeleteUmsThreadContext` | `0x5FF20` | 29 | UnwindData |  |
| 321 | `DequeueUmsCompletionListItems` | `0x5FF20` | 29 | UnwindData |  |
| 346 | `EnterUmsSchedulingMode` | `0x5FF20` | 29 | UnwindData |  |
| 585 | `GetCurrentUmsThread` | `0x5FF20` | 29 | UnwindData |  |
| 692 | `GetNextUmsListItem` | `0x5FF20` | 29 | UnwindData |  |
| 839 | `GetUmsCompletionListEvent` | `0x5FF20` | 29 | UnwindData |  |
| 840 | `GetUmsSystemThreadInformation` | `0x5FF20` | 29 | UnwindData |  |
| 1162 | `QueryUmsThreadInformation` | `0x5FF20` | 29 | UnwindData |  |
| 1464 | `SetUmsThreadInformation` | `0x5FF20` | 29 | UnwindData |  |
| 390 | `ExecuteUmsThread` | `0x5FF50` | 29 | UnwindData |  |
| 1531 | `UmsThreadYield` | `0x5FF50` | 29 | UnwindData |  |
| 121 | `BuildCommDCBA` | `0x5FF90` | 90 | UnwindData |  |
| 122 | `BuildCommDCBAndTimeoutsA` | `0x5FFF0` | 43 | UnwindData |  |
| 123 | `BuildCommDCBAndTimeoutsW` | `0x60030` | 140 | UnwindData |  |
| 124 | `BuildCommDCBW` | `0x600D0` | 126 | UnwindData |  |
| 271 | `CreateTapePartition` | `0x60EC0` | 83 | UnwindData |  |
| 388 | `EraseTape` | `0x60F20` | 53 | UnwindData |  |
| 803 | `GetTapePosition` | `0x60F60` | 135 | UnwindData |  |
| 804 | `GetTapeStatus` | `0x60FF0` | 37 | UnwindData |  |
| 1116 | `PrepareTape` | `0x61020` | 53 | UnwindData |  |
| 1434 | `SetTapeParameters` | `0x61060` | 66 | UnwindData |  |
| 1435 | `SetTapePosition` | `0x610B0` | 119 | UnwindData |  |
| 1647 | `WriteTapemark` | `0x61130` | 89 | UnwindData |  |
| 233 | `CreateHardLinkTransactedA` | `0x61190` | 171 | UnwindData |  |
| 102 | `BasepGetPackageActivationTokenForSxS3` | `0x61250` | 656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1649 | `ZombifyActCtxWorker` | `0x614E0` | 42 | UnwindData |  |
| 1315 | `SetComPlusPackageInstallStatus` | `0x61D00` | 76 | UnwindData |  |
| 36 | `ApplicationRecoveryFinished` | `0x61D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `ApplicationRecoveryInProgress` | `0x61D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 482 | `GetApplicationRecoveryCallbackWorker` | `0x61D80` | 173 | UnwindData |  |
| 484 | `GetApplicationRestartSettingsWorker` | `0x61E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1537 | `UnregisterApplicationRecoveryCallback` | `0x61E50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1591 | `WerRegisterFileWorker` | `0x61E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1593 | `WerRegisterMemoryBlockWorker` | `0x61E80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1595 | `WerRegisterRuntimeExceptionModuleWorker` | `0x61E90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1603 | `WerUnregisterFileWorker` | `0x61EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1605 | `WerUnregisterMemoryBlockWorker` | `0x61EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1607 | `WerUnregisterRuntimeExceptionModuleWorker` | `0x61EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1042 | `MapUserPhysicalPagesScatter` | `0x61ED0` | 42 | UnwindData |  |
| 141 | `CancelTimerQueueTimer` | `0x61F00` | 34 | UnwindData |  |
| 1463 | `SetTimerQueueTimer` | `0x61F30` | 83 | UnwindData |  |
| 115 | `BasepReportFault` | `0x61F90` | 43 | UnwindData |  |
| 324 | `DisableThreadProfiling` | `0x61FD0` | 46 | UnwindData |  |
| 339 | `EnableThreadProfiling` | `0x62010` | 46 | UnwindData |  |
| 1160 | `QueryThreadProfiling` | `0x62050` | 46 | UnwindData |  |
| 1198 | `ReadThreadProfilingData` | `0x62090` | 46 | UnwindData |  |
| 118 | `BeginUpdateResourceA` | `0x634E0` | 101 | UnwindData |  |
| 342 | `EndUpdateResourceA` | `0x63550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 343 | `EndUpdateResourceW` | `0x63560` | 623 | UnwindData |  |
| 1546 | `UpdateResourceA` | `0x637E0` | 385 | UnwindData |  |
| 1547 | `UpdateResourceW` | `0x63970` | 627 | UnwindData |  |
| 175 | `CompareCalendarDates` | `0x63BF0` | 163 | UnwindData |  |
| 184 | `ConvertCalDateTimeToSystemTime` | `0x63CA0` | 441 | UnwindData |  |
| 498 | `GetCalendarDifferenceInDays` | `0x63FB0` | 450 | UnwindData |  |
| 504 | `GetCalendarWeekNumber` | `0x64180` | 243 | UnwindData |  |
| 940 | `IsCalendarLeapDay` | `0x64460` | 393 | UnwindData |  |
| 941 | `IsCalendarLeapMonth` | `0x645F0` | 270 | UnwindData |  |
| 942 | `IsCalendarLeapYear` | `0x64710` | 236 | UnwindData |  |
| 347 | `EnumCalendarInfoA` | `0x64810` | 146 | UnwindData |  |
| 348 | `EnumCalendarInfoExA` | `0x648B0` | 150 | UnwindData |  |
| 352 | `EnumDateFormatsA` | `0x64950` | 90 | UnwindData |  |
| 353 | `EnumDateFormatsExA` | `0x649B0` | 94 | UnwindData |  |
| 357 | `EnumLanguageGroupLocalesA` | `0x64A20` | 27 | UnwindData |  |
| 371 | `EnumSystemCodePagesA` | `0x64A50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 384 | `EnumUILanguagesA` | `0x64A70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 562 | `GetCurrencyFormatA` | `0x64A90` | 1,018 | UnwindData |  |
| 1313 | `SetCalendarInfoA` | `0x64E90` | 226 | UnwindData |  |
| 1405 | `SetLocaleInfoA` | `0x64F80` | 242 | UnwindData |  |
| 604 | `GetDurationFormat` | `0x651F0` | 132 | UnwindData |  |
| 375 | `EnumSystemGeoNames` | `0x68270` | 294 | UnwindData |  |
| 648 | `GetGeoInfoEx` | `0x683A0` | 106 | UnwindData |  |
| 1466 | `SetUserGeoID` | `0x68410` | 21 | UnwindData |  |
| 1467 | `SetUserGeoName` | `0x68430` | 134 | UnwindData |  |
| 62 | `BaseFormatTimeOut` | `0x694B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `BasepAnsiStringToDynamicUnicodeString` | `0x694E0` | 114 | UnwindData |  |
| 80 | `BasepAllocateActivationContextActivationBlock` | `0x69560` | 387 | UnwindData |  |
| 92 | `BasepFreeActivationContextActivationBlock` | `0x696F0` | 76 | UnwindData |  |
| 486 | `GetAtomNameA` | `0x69900` | 31 | UnwindData |  |
| 866 | `GlobalAddAtomExA` | `0x69930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 877 | `GlobalGetAtomNameA` | `0x69950` | 31 | UnwindData |  |
| 12 | `AddLocalAlternateComputerNameA` | `0x69980` | 82 | UnwindData |  |
| 13 | `AddLocalAlternateComputerNameW` | `0x699E0` | 310 | UnwindData |  |
| 328 | `DnsHostnameToComputerNameA` | `0x6A6F0` | 249 | UnwindData |  |
| 386 | `EnumerateLocalComputerNamesA` | `0x6A7F0` | 280 | UnwindData |  |
| 387 | `EnumerateLocalComputerNamesW` | `0x6A910` | 510 | UnwindData |  |
| 1270 | `RemoveLocalAlternateComputerNameA` | `0x6AB20` | 82 | UnwindData |  |
| 1271 | `RemoveLocalAlternateComputerNameW` | `0x6AB80` | 330 | UnwindData |  |
| 1402 | `SetLocalPrimaryComputerNameA` | `0x6ACD0` | 82 | UnwindData |  |
| 238 | `CreateJobObjectA` | `0x6B2B0` | 100 | UnwindData |  |
| 240 | `CreateJobSet` | `0x6B320` | 42 | UnwindData |  |
| 472 | `FreeMemoryJobObject` | `0x6B350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1081 | `OpenJobObjectA` | `0x6B360` | 114 | UnwindData |  |
| 1151 | `QueryIoRateControlInformationJobObject` | `0x6B3E0` | 270 | UnwindData |  |
| 1398 | `SetIoRateControlInformationJobObject` | `0x6B640` | 514 | UnwindData |  |
| 45 | `BackupWrite` | `0x6BCA0` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `BackupWriteEx` | `0x6BE30` | 817 | UnwindData |  |
| 78 | `BaseWriteErrorElevationRequiredEvent` | `0x6CB30` | 96 | UnwindData |  |
| 727 | `GetPrivateProfileSectionNamesA` | `0x6CE50` | 34 | UnwindData |  |
| 733 | `GetPrivateProfileStructW` | `0x6CE80` | 407 | UnwindData |  |
| 760 | `GetProfileSectionA` | `0x6D020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 763 | `GetProfileStringW` | `0x6D030` | 29 | UnwindData |  |
| 1636 | `WritePrivateProfileSectionA` | `0x6D060` | 93 | UnwindData |  |
| 1637 | `WritePrivateProfileSectionW` | `0x6D0D0` | 93 | UnwindData |  |
| 1640 | `WritePrivateProfileStructA` | `0x6D140` | 348 | UnwindData |  |
| 1643 | `WriteProfileSectionA` | `0x6D2B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1644 | `WriteProfileSectionW` | `0x6D2C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1645 | `WriteProfileStringA` | `0x6D2D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `BaseIsDosApplication` | `0x6D2E0` | 269 | UnwindData |  |
| 488 | `GetBinaryType` | `0x6D400` | 75 | UnwindData |  |
| 489 | `GetBinaryTypeA` | `0x6D400` | 75 | UnwindData |  |
| 666 | `GetLongPathNameTransactedW` | `0x6D460` | 168 | UnwindData |  |
| 682 | `GetNamedPipeClientComputerNameA` | `0x6D510` | 310 | UnwindData |  |
| 148 | `CheckForReadOnlyResource` | `0x6D650` | 477 | UnwindData |  |
| 203 | `CreateBoundaryDescriptorA` | `0x6D840` | 101 | UnwindData |  |
| 252 | `CreatePrivateNamespaceA` | `0x6D8B0` | 118 | UnwindData |  |
| 1086 | `OpenPrivateNamespaceA` | `0x6D930` | 100 | UnwindData |  |
| 193 | `CopyFileA` | `0x6D9A0` | 170 | UnwindData |  |
| 194 | `CopyFileExA` | `0x6DA50` | 190 | UnwindData |  |
| 196 | `CopyFileTransactedA` | `0x6DB20` | 196 | UnwindData |  |
| 197 | `CopyFileTransactedW` | `0x6DBF0` | 217 | UnwindData |  |
| 229 | `CreateFileTransactedA` | `0x6DCD0` | 185 | UnwindData |  |
| 1276 | `ReplaceFileA` | `0x6DD90` | 306 | UnwindData |  |
| 209 | `CreateDirectoryExA` | `0x6DED0` | 151 | UnwindData |  |
| 212 | `CreateDirectoryTransactedW` | `0x6DF70` | 200 | UnwindData |  |
| 1267 | `RemoveDirectoryTransactedW` | `0x6E040` | 156 | UnwindData |  |
| 226 | `CreateFileMappingNumaA` | `0x6E0F0` | 189 | UnwindData |  |
| 267 | `CreateSymbolicLinkA` | `0x6E390` | 190 | UnwindData |  |
| 268 | `CreateSymbolicLinkTransactedA` | `0x6E460` | 198 | UnwindData |  |
| 309 | `DeleteFileTransactedA` | `0x6E530` | 75 | UnwindData |  |
| 310 | `DeleteFileTransactedW` | `0x6E590` | 142 | UnwindData |  |
| 515 | `GetCompressedFileSizeTransactedA` | `0x6E630` | 95 | UnwindData |  |
| 516 | `GetCompressedFileSizeTransactedW` | `0x6E6A0` | 161 | UnwindData |  |
| 623 | `GetFileAttributesTransactedA` | `0x6E750` | 103 | UnwindData |  |
| 624 | `GetFileAttributesTransactedW` | `0x6E7C0` | 189 | UnwindData |  |
| 1051 | `MoveFileA` | `0x6E890` | 35 | UnwindData |  |
| 1054 | `MoveFileTransactedA` | `0x6E8C0` | 188 | UnwindData |  |
| 1055 | `MoveFileTransactedW` | `0x6E990` | 195 | UnwindData |  |
| 1118 | `PrivMoveFileIdentityW` | `0x6EA60` | 1,232 | UnwindData |  |
| 1378 | `SetFileAttributesTransactedA` | `0x6EF40` | 88 | UnwindData |  |
| 1379 | `SetFileAttributesTransactedW` | `0x6EFA0` | 158 | UnwindData |  |
| 890 | `Heap32ListFirst` | `0x6F050` | 242 | UnwindData |  |
| 299 | `DefineDosDeviceA` | `0x6F150` | 158 | UnwindData |  |
| 319 | `DeleteVolumeMountPointA` | `0x6F200` | 76 | UnwindData |  |
| 429 | `FindFirstVolumeMountPointA` | `0x6F260` | 418 | UnwindData |  |
| 440 | `FindNextVolumeMountPointA` | `0x6F410` | 348 | UnwindData |  |
| 441 | `FindNextVolumeMountPointW` | `0x6F580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 450 | `FindVolumeMountPointClose` | `0x6F590` | 109 | UnwindData |  |
| 855 | `GetVolumeNameForVolumeMountPointA` | `0x6F610` | 405 | UnwindData |  |
| 1471 | `SetVolumeMountPointA` | `0x6F9C0` | 129 | UnwindData |  |
| 1472 | `SetVolumeMountPointW` | `0x6FA50` | 1,399 | UnwindData |  |
| 332 | `DosPathToSessionPathA` | `0x70220` | 479 | UnwindData |  |
| 333 | `DosPathToSessionPathW` | `0x70410` | 398 | UnwindData |  |
| 409 | `FindActCtxSectionStringA` | `0x705B0` | 153 | UnwindData |  |
| 424 | `FindFirstFileTransactedW` | `0x70650` | 205 | UnwindData |  |
| 1364 | `SetDllDirectoryA` | `0x70730` | 173 | UnwindData |  |
| 1614 | `WinExec` | `0x707F0` | 521 | UnwindData |  |
| 1431 | `SetSystemPowerState` | `0x70A00` | 74 | UnwindData |  |
| 638 | `GetFirmwareEnvironmentVariableA` | `0x70A50` | 21 | UnwindData |  |
| 639 | `GetFirmwareEnvironmentVariableExA` | `0x70A70` | 306 | UnwindData |  |
| 1391 | `SetFirmwareEnvironmentVariableA` | `0x70BB0` | 23 | UnwindData |  |
| 1392 | `SetFirmwareEnvironmentVariableExA` | `0x70BD0` | 304 | UnwindData |  |
| 1393 | `SetFirmwareEnvironmentVariableExW` | `0x70D10` | 233 | UnwindData |  |
| 1394 | `SetFirmwareEnvironmentVariableW` | `0x70E00` | 23 | UnwindData |  |
| 645 | `GetFullPathNameTransactedW` | `0x70E20` | 196 | UnwindData |  |
| 1469 | `SetVolumeLabelA` | `0x70EF0` | 161 | UnwindData |  |
| 1470 | `SetVolumeLabelW` | `0x70FA0` | 975 | UnwindData |  |
| 695 | `GetNumaAvailableMemoryNodeEx` | `0x71380` | 150 | UnwindData |  |
| 698 | `GetNumaNodeProcessorMask` | `0x71420` | 118 | UnwindData |  |
| 802 | `GetTapeParameters` | `0x714A0` | 88 | UnwindData |  |
| 826 | `GetThreadSelectorEntry` | `0x71500` | 22 | UnwindData |  |
| 1543 | `UnregisterWaitUntilOOBECompleted` | `0x71550` | 104 | UnwindData |  |
| 1368 | `SetEnvironmentStringsA` | `0x715C0` | 235 | UnwindData |  |
| 1509 | `TermsrvRestoreKey` | `0x72770` | 1,440 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1656 | `_lcreat` | `0x72D10` | 92 | UnwindData |  |
| 1659 | `_lopen` | `0x72D80` | 111 | UnwindData |  |
| 157 | `CloseConsoleHandle` | `0x72E00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 334 | `DuplicateConsoleHandle` | `0x72E20` | 74 | UnwindData |  |
| 547 | `GetConsoleInputWaitHandle` | `0x72E70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1073 | `OpenConsoleW` | `0x72E90` | 78 | UnwindData |  |
| 182 | `ConsoleMenuControl` | `0x72EF0` | 138 | UnwindData |  |
| 543 | `GetConsoleHardwareState` | `0x72F80` | 143 | UnwindData |  |
| 1246 | `RegisterConsoleVDM` | `0x73020` | 213 | UnwindData |  |
| 1329 | `SetConsoleCursor` | `0x73100` | 124 | UnwindData |  |
| 1335 | `SetConsoleHardwareState` | `0x73190` | 138 | UnwindData |  |
| 1340 | `SetConsoleKeyShortcuts` | `0x73220` | 203 | UnwindData |  |
| 1343 | `SetConsoleMenuClose` | `0x73300` | 108 | UnwindData |  |
| 1350 | `SetConsolePalette` | `0x73380` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1478 | `ShowConsoleCursor` | `0x73420` | 88 | UnwindData |  |
| 1624 | `WriteConsoleInputVDMA` | `0x73480` | 187 | UnwindData |  |
| 1625 | `WriteConsoleInputVDMW` | `0x73550` | 198 | UnwindData |  |
| 533 | `GetConsoleCharType` | `0x73620` | 140 | UnwindData |  |
| 539 | `GetConsoleCursorMode` | `0x736C0` | 145 | UnwindData |  |
| 551 | `GetConsoleNlsMode` | `0x73760` | 125 | UnwindData |  |
| 1244 | `RegisterConsoleIME` | `0x737F0` | 29 | UnwindData |  |
| 1540 | `UnregisterConsoleIME` | `0x737F0` | 29 | UnwindData |  |
| 1245 | `RegisterConsoleOS2` | `0x73820` | 108 | UnwindData |  |
| 1331 | `SetConsoleCursorMode` | `0x738A0` | 144 | UnwindData |  |
| 1341 | `SetConsoleLocalEUDC` | `0x73940` | 240 | UnwindData |  |
| 1345 | `SetConsoleNlsMode` | `0x73A40` | 122 | UnwindData |  |
| 1348 | `SetConsoleOS2OemFormat` | `0x73AC0` | 108 | UnwindData |  |
| 541 | `GetConsoleFontInfo` | `0x73B40` | 230 | UnwindData |  |
| 548 | `GetConsoleKeyboardLayoutNameA` | `0x73C30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 549 | `GetConsoleKeyboardLayoutNameW` | `0x73C50` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 708 | `GetNumberOfConsoleFonts` | `0x73D60` | 96 | UnwindData |  |
| 1334 | `SetConsoleFont` | `0x73DD0` | 122 | UnwindData |  |
| 1337 | `SetConsoleIcon` | `0x73E50` | 108 | UnwindData |  |
| 932 | `InvalidateConsoleDIBits` | `0x73ED0` | 127 | UnwindData |  |
| 1548 | `VDMConsoleOperation` | `0x73F60` | 212 | UnwindData |  |
| 1608 | `WerpGetDebugger` | `0x75AC0` | 1,350 | UnwindData |  |
| 1610 | `WerpLaunchAeDebug` | `0x765F0` | 2,352 | UnwindData |  |
| 60 | `BaseFlushAppcompatCacheWorker` | `0x78830` | 72 | UnwindData |  |
| 76 | `BaseUpdateAppcompatCacheWorker` | `0x78880` | 29 | UnwindData |  |
| 104 | `BasepInitAppCompatData` | `0x788F0` | 124 | UnwindData |  |
| 71 | `BaseQueryModuleData` | `0x78980` | 154 | UnwindData |  |
| 1167 | `QuirkGetData2Worker` | `0x78A20` | 193 | UnwindData |  |
| 1168 | `QuirkGetDataWorker` | `0x78AF0` | 169 | UnwindData |  |
| 1169 | `QuirkIsEnabled2Worker` | `0x78BA0` | 293 | UnwindData |  |
| 1517 | `TlsGetValue` | `0x84530` | 107 | UnwindData |  |
