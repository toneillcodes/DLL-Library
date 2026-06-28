# Binary Specification: ttdrecordcpu.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ttdrecordcpu.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4e2b46dabfd8bf318d4d3e5652a28688e1dc74fa5a842fdbdaefaeda90b56c01`
* **Total Exported Functions:** 48

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 24 | `RequestUnhookedFunctions` | `0x1380` | 247 | UnwindData |  |
| 16 | `InitializeSmartCpuClient` | `0x16F0` | 88 | UnwindData |  |
| 13 | `InitializeGlobalState` | `0x1750` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `SetThreadNative` | `0x17A0` | 296 | UnwindData |  |
| 27 | `RunCallbackWithSmartContextForCurrentThread` | `0x18D0` | 54 | UnwindData |  |
| 1 | `ClearClientTlsValueForThreadId` | `0x1910` | 27 | UnwindData |  |
| 4 | `GetClientTlsValueForCurrentThread` | `0x1940` | 23 | UnwindData |  |
| 30 | `StartEmulatingCurrentThread` | `0x1960` | 55 | UnwindData |  |
| 31 | `StopEmulatingCurrentThread` | `0x19A0` | 55 | UnwindData |  |
| 18 | `IsEmulatingCurrentThread` | `0x19E0` | 64 | UnwindData |  |
| 8 | `GetInstructionCounts` | `0x1A30` | 83 | UnwindData |  |
| 25 | `ResetMaxInstructionsToEmulate` | `0x1A90` | 98 | UnwindData |  |
| 2 | `FlushCodeCaches` | `0x7FA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `ResumeSimulation` | `0x7FC0` | 47 | UnwindData |  |
| 28 | `SetRuntimeOptions` | `0x82E0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `InitializeEmulateOnlyClient` | `0x8430` | 83 | UnwindData |  |
| 23 | `RegisterRecordCallbacks` | `0xEA30` | 17,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `GetVcpuRegisterMapDefinition` | `0x12FE0` | 775,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `GetCurrentProcessId` | `0xD0600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `GetCurrentThreadId` | `0xD0620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `GetCurrentProcess` | `0xD0640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `GetLastError` | `0xD0650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `GetTickCount` | `0xD0670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `QueryPerformanceCounter` | `0xD0690` | 24 | UnwindData |  |
| 3 | `GetCfgPointers` | `0xD0950` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `InjectThread` | `0xD0AF0` | 44 | UnwindData |  |
| 14 | `InitializeNirvanaClient` | `0xD4920` | 510 | UnwindData |  |
| 45 | `TtdWriterStopRecordingCurrentThread` | `0xDB800` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `TtdWriterResetThrottle` | `0xDB870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `TtdWriterTryPauseRecording` | `0xDB880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `TtdWriterResumeRecording` | `0xDB890` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `OpenWriter` | `0xDB8F0` | 194 | UnwindData |  |
| 15 | `InitializeRecorder` | `0xDBB20` | 321 | UnwindData |  |
| 41 | `TtdWriterRelease` | `0xDBD10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `TtdWriterGetFileName` | `0xDBD20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `TtdWriterDumpSnapshot` | `0xDBD30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `TtdWriterDumpModuleData` | `0xDBD40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `TtdWriterDumpHeaps` | `0xDBD50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `TtdWriterAddCustomEvent` | `0xDBD60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `TtdWriterStartRecordingCurrentThread` | `0xDBD70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `TtdWriterGetThrottleState` | `0xDBD80` | 41 | UnwindData |  |
| 39 | `TtdWriterGetState` | `0xDBDB0` | 61,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `TryPauseSimulation` | `0xEAD10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `IsSimulating` | `0xEAD30` | 21,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `StubDllEntry` | `0xEFF50` | 37,728 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `g_ttdConstants` | `0xF92B0` | 661,352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `ntdllLdrInitializeThunk` | `0x19AA18` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `ParametersBlock` | `0x19AA28` | 0 | Indeterminate |  |
