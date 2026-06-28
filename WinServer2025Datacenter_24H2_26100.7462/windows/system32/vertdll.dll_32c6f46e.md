# Binary Specification: vertdll.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\vertdll.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `32c6f46e9fc998060fa8d8bb7aeeb8a9a0b933f420215a6043766db02e272b72`
* **Total Exported Functions:** 196

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `CallEnclave` | `0x1010` | 64 | UnwindData |  |
| 124 | `RtlCaptureContext` | `0x1440` | 175 | UnwindData |  |
| 181 | `__C_specific_handler` | `0x1C50` | 455 | UnwindData |  |
| 183 | `_local_unwind` | `0x1E20` | 40 | UnwindData |  |
| 185 | `_wcsicmp` | `0x1E50` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `_wcsnicmp` | `0x1EB0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 192 | `qsort` | `0x1F30` | 126 | UnwindData |  |
| 193 | `wcscmp` | `0x22F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 195 | `wcsncmp` | `0x2330` | 4,320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 194 | `wcscpy_s` | `0x3410` | 132 | UnwindData |  |
| 196 | `wcsncpy_s` | `0x34A0` | 254 | UnwindData |  |
| 156 | `SetUnhandledExceptionFilter` | `0x3670` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `EnclaveEncryptDataForTrustlet` | `0x37F0` | 230 | UnwindData |  |
| 17 | `EnclaveGetAttestationReport` | `0x38E0` | 193 | UnwindData |  |
| 20 | `EnclaveSealData` | `0x39B0` | 224 | UnwindData |  |
| 21 | `EnclaveUnsealData` | `0x3AA0` | 276 | UnwindData |  |
| 22 | `EnclaveUsesAttestedKeys` | `0x3BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `EnclaveVerifyAttestationReport` | `0x3BD0` | 107 | UnwindData |  |
| 50 | `GetLastError` | `0x3C60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `SetLastError` | `0x3C80` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `GetProcessHeap` | `0x3CD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `GetProcessHeaps` | `0x3CF0` | 50 | UnwindData |  |
| 62 | `HeapCompact` | `0x3D30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `HeapCreate` | `0x3D40` | 81 | UnwindData |  |
| 64 | `HeapDestroy` | `0x3DA0` | 39 | UnwindData |  |
| 66 | `HeapLock` | `0x3DD0` | 18 | UnwindData |  |
| 69 | `HeapUnlock` | `0x3DF0` | 18 | UnwindData |  |
| 49 | `GetFipsModeFromIumKernelState` | `0x3E10` | 109 | UnwindData |  |
| 57 | `GetSeedFromIumKernelState` | `0x3E90` | 147 | UnwindData |  |
| 101 | `OutputDebugStringW` | `0x3F30` | 140 | UnwindData |  |
| 108 | `RaiseException` | `0x3FD0` | 171 | UnwindData |  |
| 14 | `EnclaveCopyIntoEnclave` | `0x4090` | 23 | UnwindData |  |
| 15 | `EnclaveCopyOutOfEnclave` | `0x40B0` | 23 | UnwindData |  |
| 154 | `SetThreadStackGuarantee` | `0x40D0` | 336 | UnwindData |  |
| 170 | `VirtualAlloc` | `0x4230` | 69 | UnwindData |  |
| 171 | `VirtualFree` | `0x4280` | 81 | UnwindData |  |
| 172 | `VirtualProtect` | `0x42E0` | 65 | UnwindData |  |
| 173 | `VirtualQuery` | `0x4330` | 68 | UnwindData |  |
| 13 | `DisableThreadLibraryCalls` | `0x4380` | 38 | UnwindData |  |
| 52 | `GetModuleHandleExW` | `0x43B0` | 211 | UnwindData |  |
| 53 | `GetProcAddress` | `0x4490` | 164 | UnwindData |  |
| 18 | `EnclaveGetEnclaveInformation` | `0x5290` | 60 | UnwindData |  |
| 19 | `EnclaveRestrictContainingProcessAccess` | `0x52E0` | 127 | UnwindData |  |
| 44 | `GetCurrentProcess` | `0x5370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `IsProcessorFeaturePresent` | `0x5380` | 24 | UnwindData |  |
| 159 | `TerminateEnclave` | `0x53A0` | 56 | UnwindData |  |
| 160 | `TerminateProcess` | `0x53E0` | 52 | UnwindData |  |
| 92 | `MultiByteToWideChar` | `0x5420` | 65 | UnwindData |  |
| 180 | `WideCharToMultiByte` | `0x5480` | 65 | UnwindData |  |
| 11 | `DeleteSynchronizationBarrier` | `0x54D0` | 46 | UnwindData |  |
| 25 | `EnterSynchronizationBarrier` | `0x5510` | 88 | UnwindData |  |
| 73 | `InitializeCriticalSectionAndSpinCount` | `0x5570` | 28 | UnwindData |  |
| 74 | `InitializeCriticalSectionEx` | `0x55A0` | 38 | UnwindData |  |
| 77 | `InitializeSynchronizationBarrier` | `0x55D0` | 60 | UnwindData |  |
| 157 | `SleepConditionVariableCS` | `0x5620` | 90 | UnwindData |  |
| 158 | `SleepConditionVariableSRW` | `0x5680` | 90 | UnwindData |  |
| 175 | `WaitOnAddress` | `0x5710` | 123 | UnwindData |  |
| 46 | `GetCurrentThread` | `0x57A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `GetCurrentThreadId` | `0x57B0` | 1,856 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `LdrResolveDelayLoadedAPI` | `0x5EF0` | 138 | UnwindData |  |
| 117 | `ResolveDelayLoadedAPI` | `0x5EF0` | 138 | UnwindData |  |
| 85 | `LdrDisableThreadCalloutsForDll` | `0x6640` | 48 | UnwindData |  |
| 4 | `CloseHandle` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `CloseThreadpoolTimer` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `CreateEventW` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `CreateThreadpoolTimer` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `DelayLoadFailureHook` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `DeviceIoControl` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `EtwEventWrite` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `EtwGetTraceEnableFlags` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `EtwGetTraceEnableLevel` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `EtwGetTraceLoggerHandle` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `EtwTraceMessage` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `EtwUnregisterTraceGuids` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `EventWriteTransfer` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `FreeLibrary` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `GetCurrentProcessId` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `GetModuleFileNameW` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `GetProcessId` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `GetSystemDirectoryW` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `GetSystemInfo` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `I_QueryTagInformation` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `LoadLibraryExW` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `LoadLibraryW` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `LocalFree` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `NtClose` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `NtDeviceIoControlFile` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `NtOpenFile` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `NtOpenKey` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `NtQueryValueKey` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `OpenProcessToken` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `PrivilegeCheck` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `QueryFullProcess` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `QueryFullProcessImageNameW` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `RegCloseKey` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `RegEnumKeyExW` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `RegOpenKeyExW` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `RegQueryInfoKeyW` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `RegQueryValueExW` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `RegisterWaitForSingleObjectEx` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `RtlAcquireResourceExclusive` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `RtlAcquireResourceShared` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `RtlAssert` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `RtlCompareUnicodeString` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `RtlDeleteResource` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `RtlInitializeResource` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `RtlReleaseResource` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `RtlReleaseResourceShared` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `SetThreadpoolTimer` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `UnregisterWaitEx` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 174 | `WaitForThreadpoolTimerCallbacks` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | `_vsnwprintf` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 187 | `_wsplitpath_s` | `0x6C90` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `RtlDllShutdownInProgress` | `0x7FD0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `DbgPrint` | `0x8070` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `EtwEventRegister` | `0x8070` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `EtwEventUnregister` | `0x8070` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `EtwEventWriteTransfer` | `0x8070` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `EtwRegisterTraceGuidsW` | `0x8070` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `EventRegister` | `0x8070` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `EventSetInformation` | `0x8070` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `EventUnregister` | `0x8070` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 161 | `TlsAlloc` | `0x8230` | 241 | UnwindData |  |
| 162 | `TlsFree` | `0x8330` | 209 | UnwindData |  |
| 163 | `TlsGetValue` | `0x8410` | 82 | UnwindData |  |
| 164 | `TlsGetValue2` | `0x8470` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 165 | `TlsSetValue` | `0x84B0` | 157 | UnwindData |  |
| 48 | `GetEnabledXStateFeatures` | `0x85E0` | 34 | UnwindData |  |
| 60 | `GetXStateFeaturesMask` | `0x8610` | 168 | UnwindData |  |
| 91 | `LocateXStateFeature` | `0x86C0` | 1,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `RtlLookupFunctionEntry` | `0x8B60` | 680 | UnwindData |  |
| 149 | `RtlUnwind` | `0x8E10` | 199 | UnwindData |  |
| 150 | `RtlUnwindEx` | `0x8EE0` | 1,232 | UnwindData |  |
| 1 | `AcquireSRWLockExclusive` | `0x9630` | 23 | UnwindData |  |
| 2 | `AcquireSRWLockShared` | `0x9650` | 32 | UnwindData |  |
| 71 | `InitializeConditionVariable` | `0x9680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `InitializeSRWLock` | `0x9680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `ReleaseSRWLockExclusive` | `0x9690` | 67 | UnwindData |  |
| 116 | `ReleaseSRWLockShared` | `0x96E0` | 184 | UnwindData |  |
| 166 | `TryAcquireSRWLockExclusive` | `0x97A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 167 | `TryAcquireSRWLockShared` | `0x97C0` | 126 | UnwindData |  |
| 10 | `DeleteCriticalSection` | `0x9E00` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `RtlDeleteCriticalSection` | `0x9E00` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `EnterCriticalSection` | `0x9E40` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `RtlEnterCriticalSection` | `0x9E40` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `InitializeCriticalSection` | `0x9E80` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `RtlInitializeCriticalSection` | `0x9E80` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `LeaveCriticalSection` | `0x9F70` | 19 | UnwindData |  |
| 140 | `RtlLeaveCriticalSection` | `0x9F70` | 19 | UnwindData |  |
| 152 | `SetCriticalSectionSpinCount` | `0xA030` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `TryEnterCriticalSection` | `0xA080` | 1,856 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `HeapAlloc` | `0xA7C0` | 82 | UnwindData |  |
| 120 | `RtlAllocateHeap` | `0xA7C0` | 82 | UnwindData |  |
| 65 | `HeapFree` | `0xA820` | 98 | UnwindData |  |
| 132 | `RtlFreeHeap` | `0xA820` | 98 | UnwindData |  |
| 67 | `HeapReAlloc` | `0xA890` | 97 | UnwindData |  |
| 68 | `HeapSize` | `0xA900` | 65 | UnwindData |  |
| 176 | `WakeAllConditionVariable` | `0xAD30` | 119 | UnwindData |  |
| 179 | `WakeConditionVariable` | `0xADB0` | 73 | UnwindData |  |
| 75 | `InitializeSListHead` | `0xB0A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `InterlockedFlushSList` | `0xB0B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `InterlockedPushEntrySList` | `0xB0C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `InterlockedPushListSListEx` | `0xB0D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `QueryDepthSList` | `0xB0E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `QueryPerformanceCounter` | `0xB0F0` | 225 | UnwindData |  |
| 107 | `QueryPerformanceFrequency` | `0xB1E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `RtlTimeFieldsToTime` | `0xB200` | 960 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `RtlGetLastNtStatus` | `0xB5C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `RtlNtStatusToDosError` | `0xB5D0` | 45 | UnwindData |  |
| 135 | `RtlGetSystemGlobalData` | `0xB760` | 656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `RtlImageNtHeader` | `0xB9F0` | 41 | UnwindData |  |
| 137 | `RtlInitUnicodeString` | `0xBB90` | 66 | UnwindData |  |
| 143 | `RtlPcToFileHeader` | `0xBC30` | 89 | UnwindData |  |
| 144 | `RtlRaiseStatus` | `0xBEB0` | 107 | UnwindData |  |
| 148 | `RtlUnhandledExceptionFilter` | `0xBF30` | 1,008 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | `RtlVirtualUnwind` | `0xC320` | 199 | UnwindData |  |
| 177 | `WakeByAddressAll` | `0xD870` | 20 | UnwindData |  |
| 178 | `WakeByAddressSingle` | `0xD890` | 20 | UnwindData |  |
| 97 | `NtQueryInformationProcess` | `0x1CAD0` | 11 | UnwindData |  |
| 99 | `NtTerminateProcess` | `0x1CB20` | 11 | UnwindData |  |
| 79 | `InterlockedPopEntrySList` | `0x1CC70` | 52 | UnwindData |  |
| 42 | `ExpInterlockedPopEntrySListResume` | `0x1CC77` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `ExpInterlockedPopEntrySListFault` | `0x1CC87` | 9 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `ExpInterlockedPopEntrySListEnd` | `0x1CC90` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `InterlockedPushListSList` | `0x1CD20` | 51 | UnwindData |  |
| 84 | `KiUserExceptionDispatcher` | `0x1CD70` | 65 | UnwindData |  |
| 129 | `RtlEnclaveCallDispatch` | `0x1CE20` | 128 | UnwindData |  |
| 130 | `RtlEnclaveCallDispatchReturn` | `0x1CE6A` | 70 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `RtlCallEnclave` | `0x1CEB0` | 207 | UnwindData |  |
| 123 | `RtlCallEnclaveReturn` | `0x1CF1B` | 117 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `RtlGetCurrentProcessorNumberEx` | `0x1CF90` | 92 | UnwindData |  |
| 182 | `__chkstk` | `0x1D000` | 77 | UnwindData |  |
| 188 | `memcmp` | `0x1D5A0` | 199 | UnwindData |  |
| 189 | `memcpy` | `0x1D6C0` | 682 | UnwindData |  |
| 190 | `memmove` | `0x1D6C0` | 682 | UnwindData |  |
| 191 | `memset` | `0x1F030` | 0 | Indeterminate |  |
