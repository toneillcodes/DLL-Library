# Binary Specification: tprtdll.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\tprtdll.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `01ce4373d7d175ad4716465366c9d71b76807fb650505a47fd12fb805169d964`
* **Total Exported Functions:** 164

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 8 | `DbgBreakPoint` | `0x1310` | 2 | UnwindData |  |
| 74 | `RtlCaptureContext` | `0x1410` | 175 | UnwindData |  |
| 163 | `swprintf_s` | `0x1BA0` | 30 | UnwindData |  |
| 164 | `vswprintf_s` | `0x1BD0` | 82 | UnwindData |  |
| 153 | `__C_specific_handler` | `0x28B0` | 455 | UnwindData |  |
| 154 | `__imp__stricmp` | `0x2AD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `__imp__wcsicmp` | `0x2AE0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `__imp_strchr` | `0x2B40` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `__imp_toupper` | `0x2BD0` | 97 | UnwindData |  |
| 158 | `__imp_wcstoul` | `0x2E60` | 43 | UnwindData |  |
| 47 | `LdrInitializeThunk` | `0x4DB0` | 73 | UnwindData |  |
| 120 | `RtlUserThreadStart` | `0x4E00` | 41 | UnwindData |  |
| 94 | `RtlLookupFunctionEntry` | `0x5360` | 612 | UnwindData |  |
| 117 | `RtlUnwind` | `0x55D0` | 199 | UnwindData |  |
| 118 | `RtlUnwindEx` | `0x56A0` | 1,255 | UnwindData |  |
| 69 | `RtlAcquireReleaseSRWLockExclusive` | `0x5E50` | 49 | UnwindData |  |
| 1 | `AcquireSRWLockExclusive` | `0x5E90` | 23 | UnwindData |  |
| 70 | `RtlAcquireSRWLockExclusive` | `0x5E90` | 23 | UnwindData |  |
| 2 | `AcquireSRWLockShared` | `0x5EB0` | 32 | UnwindData |  |
| 71 | `RtlAcquireSRWLockShared` | `0x5EB0` | 32 | UnwindData |  |
| 41 | `InitializeSRWLock` | `0x5EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `RtlInitializeSRWLock` | `0x5EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `RtlRunOnceInitialize` | `0x5EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `ReleaseSRWLockExclusive` | `0x5EF0` | 67 | UnwindData |  |
| 104 | `RtlReleaseSRWLockExclusive` | `0x5EF0` | 67 | UnwindData |  |
| 66 | `ReleaseSRWLockShared` | `0x5F40` | 184 | UnwindData |  |
| 105 | `RtlReleaseSRWLockShared` | `0x5F40` | 184 | UnwindData |  |
| 113 | `RtlTryAcquireSRWLockExclusive` | `0x6000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `TryAcquireSRWLockExclusive` | `0x6000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `RtlTryAcquireSRWLockShared` | `0x6020` | 126 | UnwindData |  |
| 137 | `TryAcquireSRWLockShared` | `0x6020` | 126 | UnwindData |  |
| 119 | `RtlUpdateClonedSRWLock` | `0x60B0` | 1,264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `DeleteCriticalSection` | `0x65A0` | 372 | UnwindData |  |
| 14 | `EnterCriticalSection` | `0x6720` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `InitializeCriticalSection` | `0x6760` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `RtlInitializeCriticalSectionAndSpinCount` | `0x67B0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `LeaveCriticalSection` | `0x68C0` | 337 | UnwindData |  |
| 108 | `RtlSetCriticalSectionSpinCount` | `0x6A20` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `SetCriticalSectionSpinCount` | `0x6A20` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `TryEnterCriticalSection` | `0x6A70` | 2,848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `HeapAlloc` | `0x7590` | 360 | UnwindData |  |
| 72 | `RtlAllocateHeap` | `0x7590` | 360 | UnwindData |  |
| 30 | `HeapFree` | `0x7700` | 566 | UnwindData |  |
| 81 | `RtlFreeHeap` | `0x7700` | 566 | UnwindData |  |
| 33 | `HeapReAlloc` | `0x7940` | 192 | UnwindData |  |
| 103 | `RtlReAllocateHeap` | `0x7940` | 192 | UnwindData |  |
| 35 | `HeapSize` | `0x7A10` | 78 | UnwindData |  |
| 112 | `RtlSizeHeap` | `0x7A10` | 78 | UnwindData |  |
| 28 | `HeapCreate` | `0x7AB0` | 40 | UnwindData |  |
| 78 | `RtlCreateHeap` | `0x7AB0` | 40 | UnwindData |  |
| 29 | `HeapDestroy` | `0x7AE0` | 758 | UnwindData |  |
| 80 | `RtlDestroyHeap` | `0x7AE0` | 758 | UnwindData |  |
| 75 | `RtlCompactHeap` | `0xE2A0` | 275 | UnwindData |  |
| 83 | `RtlGetUserInfoHeap` | `0xE3C0` | 770 | UnwindData |  |
| 31 | `HeapLock` | `0xE940` | 105 | UnwindData |  |
| 93 | `RtlLockHeap` | `0xE940` | 105 | UnwindData |  |
| 32 | `HeapQueryInformation` | `0xE9B0` | 301 | UnwindData |  |
| 97 | `RtlQueryHeapInformation` | `0xE9B0` | 301 | UnwindData |  |
| 34 | `HeapSetInformation` | `0xEBC0` | 508 | UnwindData |  |
| 109 | `RtlSetHeapInformation` | `0xEBC0` | 508 | UnwindData |  |
| 110 | `RtlSetUserFlagsHeap` | `0xEDD0` | 739 | UnwindData |  |
| 111 | `RtlSetUserValueHeap` | `0xF0C0` | 620 | UnwindData |  |
| 36 | `HeapUnlock` | `0xF3B0` | 112 | UnwindData |  |
| 116 | `RtlUnlockHeap` | `0xF3B0` | 112 | UnwindData |  |
| 37 | `HeapValidate` | `0xF4D0` | 433 | UnwindData |  |
| 121 | `RtlValidateHeap` | `0xF4D0` | 433 | UnwindData |  |
| 125 | `RtlWalkHeap` | `0xF690` | 19,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `RtlInitializeSListHead` | `0x14110` | 32 | UnwindData |  |
| 43 | `InterlockedFlushSList` | `0x14140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `RtlInterlockedFlushSList` | `0x14140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `InterlockedPushEntrySList` | `0x14150` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `RtlInterlockedPushEntrySList` | `0x14150` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `RtlQueryDepthSList` | `0x14160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `QueryPerformanceCounter` | `0x14170` | 215 | UnwindData |  |
| 64 | `QueryPerformanceFrequency` | `0x14250` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `RtlBarrier` | `0x14270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `RtlInitBarrier` | `0x14280` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `RtlCreateUserThread` | `0x143B0` | 104 | UnwindData |  |
| 82 | `RtlGetCurrentServiceSessionId` | `0x146B0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `RtlInitUnicodeString` | `0x147A0` | 66 | UnwindData |  |
| 92 | `RtlIsProcessorFeaturePresent` | `0x14840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `RtlPcToFileHeader` | `0x14860` | 89 | UnwindData |  |
| 98 | `RtlQueryResourcePolicy` | `0x148C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `RtlRandom` | `0x148E0` | 143 | UnwindData |  |
| 100 | `RtlRandomEx` | `0x14980` | 186 | UnwindData |  |
| 101 | `RtlRbInsertNodeEx` | `0x14B30` | 1,121 | UnwindData |  |
| 102 | `RtlRbRemoveNode` | `0x14FA0` | 2,482 | UnwindData |  |
| 106 | `RtlRunOnceExecuteOnce` | `0x15B40` | 199 | UnwindData |  |
| 115 | `RtlUnhandledExceptionFilter` | `0x15C10` | 1,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `RtlVirtualUnwind` | `0x16010` | 199 | UnwindData |  |
| 123 | `RtlWaitOnAddress` | `0x17580` | 31 | UnwindData |  |
| 124 | `RtlWakeAddressAll` | `0x175B0` | 20 | UnwindData |  |
| 9 | `DbgUiRemoteBreakin` | `0x34610` | 62 | UnwindData |  |
| 3 | `CloseHandle` | `0x35B10` | 149 | UnwindData |  |
| 13 | `DuplicateHandle` | `0x35BB0` | 143 | UnwindData |  |
| 4 | `CreateEventW` | `0x35D30` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `CreateSemaphoreExW` | `0x35E10` | 223 | UnwindData |  |
| 6 | `CreateSemaphoreW` | `0x35F00` | 28 | UnwindData |  |
| 12 | `DeleteSynchronizationBarrier` | `0x35F30` | 55 | UnwindData |  |
| 15 | `EnterSynchronizationBarrier` | `0x35F70` | 87 | UnwindData |  |
| 39 | `InitializeCriticalSectionAndSpinCount` | `0x35FD0` | 20 | UnwindData |  |
| 40 | `InitializeCriticalSectionEx` | `0x35FF0` | 38 | UnwindData |  |
| 42 | `InitializeSynchronizationBarrier` | `0x36020` | 60 | UnwindData |  |
| 67 | `ReleaseSemaphore` | `0x36190` | 35 | UnwindData |  |
| 68 | `ResetEvent` | `0x361C0` | 35 | UnwindData |  |
| 127 | `SetEvent` | `0x361F0` | 37 | UnwindData |  |
| 143 | `WaitForMultipleObjects` | `0x36220` | 15 | UnwindData |  |
| 144 | `WaitForSingleObject` | `0x36370` | 1,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `CreateThread` | `0x36810` | 56 | UnwindData |  |
| 19 | `GetCurrentThread` | `0x36850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `GetCurrentThreadId` | `0x36860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `GetExitCodeThread` | `0x36880` | 87 | UnwindData |  |
| 25 | `GetThreadId` | `0x368E0` | 74 | UnwindData |  |
| 129 | `Sleep` | `0x36930` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `TerminateThread` | `0x36990` | 245 | UnwindData |  |
| 132 | `TlsAlloc` | `0x36A90` | 45 | UnwindData |  |
| 133 | `TlsFree` | `0x36AD0` | 35 | UnwindData |  |
| 135 | `TlsSetValue` | `0x36B00` | 35 | UnwindData |  |
| 10 | `DebugBreak` | `0x36DD0` | 880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `OutputDebugStringW` | `0x37140` | 218 | UnwindData |  |
| 17 | `GetCurrentProcess` | `0x37220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `GetCurrentProcessId` | `0x37230` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | `TerminateProcess` | `0x37250` | 77 | UnwindData |  |
| 23 | `GetLastError` | `0x372B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `GetProcessHeap` | `0x372C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `SetLastError` | `0x372E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `VirtualAlloc` | `0x372F0` | 115 | UnwindData |  |
| 140 | `VirtualFree` | `0x37370` | 175 | UnwindData |  |
| 141 | `VirtualProtect` | `0x37430` | 149 | UnwindData |  |
| 142 | `VirtualQuery` | `0x374D0` | 72 | UnwindData |  |
| 16 | `ExitThread` | `0x38DB0` | 79 | UnwindData |  |
| 21 | `GetEnabledXStateFeatures` | `0x38F60` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `GetXStateFeaturesMask` | `0x38F90` | 194 | UnwindData |  |
| 50 | `LocateXStateFeature` | `0x390B0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `LdrDisableThreadCalloutsForDll` | `0x39180` | 82 | UnwindData |  |
| 48 | `LdrLoadDll` | `0x39660` | 463 | UnwindData |  |
| 152 | `ZwSetInformationThread` | `0x485E0` | 24 | UnwindData |  |
| 60 | `NtSetEvent` | `0x48600` | 24 | UnwindData |  |
| 52 | `NtClose` | `0x48620` | 24 | UnwindData |  |
| 145 | `ZwClose` | `0x48620` | 24 | UnwindData |  |
| 147 | `ZwOpenKey` | `0x48680` | 24 | UnwindData |  |
| 150 | `ZwQueryValueKey` | `0x48720` | 24 | UnwindData |  |
| 57 | `NtQueryInformationProcess` | `0x48760` | 24 | UnwindData |  |
| 146 | `ZwFreeVirtualMemory` | `0x48800` | 24 | UnwindData |  |
| 151 | `ZwQueryVirtualMemory` | `0x488A0` | 24 | UnwindData |  |
| 58 | `NtQueryInformationThread` | `0x488E0` | 24 | UnwindData |  |
| 61 | `NtTerminateProcess` | `0x489C0` | 24 | UnwindData |  |
| 54 | `NtDelayExecution` | `0x48AC0` | 24 | UnwindData |  |
| 149 | `ZwQuerySystemInformation` | `0x48B00` | 24 | UnwindData |  |
| 53 | `NtCreateEvent` | `0x48D40` | 24 | UnwindData |  |
| 148 | `ZwProtectVirtualMemory` | `0x48E40` | 24 | UnwindData |  |
| 51 | `NtAllocateVirtualMemoryEx` | `0x49330` | 24 | UnwindData |  |
| 55 | `NtFlushProcessWriteBuffers` | `0x4A290` | 24 | UnwindData |  |
| 56 | `NtGetNextThread` | `0x4A450` | 24 | UnwindData |  |
| 59 | `NtResetEvent` | `0x4B510` | 24 | UnwindData |  |
| 45 | `KiUserExceptionDispatcher` | `0x4C190` | 65 | UnwindData |  |
| 76 | `RtlCompareMemory` | `0x4C240` | 122 | UnwindData |  |
| 77 | `RtlCompareMemoryUlong` | `0x4C2C0` | 36 | UnwindData |  |
| 90 | `RtlInterlockedPopEntrySList` | `0x4C540` | 52 | UnwindData |  |
| 134 | `TlsGetValue` | `0x4C860` | 107 | UnwindData |  |
| 160 | `memcpy` | `0x4CC40` | 682 | UnwindData |  |
| 161 | `memmove` | `0x4CC40` | 682 | UnwindData |  |
| 162 | `memset` | `0x4F020` | 7,008 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `_fltused` | `0x50B80` | 0 | Indeterminate |  |
