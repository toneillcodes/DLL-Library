# Binary Specification: ttdrecordcpu.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ttdrecordcpu.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `dd01dee2e4f8d053a45f1ba58da94a62d86bc3a43f274e7125437ffd8b2614d1`
* **Total Exported Functions:** 42

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 18 | `RequestUnhookedFunctions` | `0x13A0` | 247 | UnwindData |  |
| 11 | `InitializeSmartCpuClient` | `0x1710` | 88 | UnwindData |  |
| 8 | `InitializeGlobalState` | `0x1770` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `SetThreadNative` | `0x17C0` | 293 | UnwindData |  |
| 21 | `RunCallbackWithSmartContextForCurrentThread` | `0x18F0` | 54 | UnwindData |  |
| 1 | `ClearClientTlsValueForThreadId` | `0x1930` | 24 | UnwindData |  |
| 4 | `GetClientTlsValueForCurrentThread` | `0x1950` | 23 | UnwindData |  |
| 24 | `StartEmulatingCurrentThread` | `0x1970` | 52 | UnwindData |  |
| 25 | `StopEmulatingCurrentThread` | `0x19B0` | 55 | UnwindData |  |
| 13 | `IsEmulatingCurrentThread` | `0x19F0` | 64 | UnwindData |  |
| 5 | `GetInstructionCounts` | `0x1A40` | 83 | UnwindData |  |
| 19 | `ResetMaxInstructionsToEmulate` | `0x1AA0` | 95 | UnwindData |  |
| 2 | `FlushCodeCaches` | `0x7EC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `ResumeSimulation` | `0x7EE0` | 47 | UnwindData |  |
| 22 | `SetRuntimeOptions` | `0x81F0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `InitializeEmulateOnlyClient` | `0x8330` | 83 | UnwindData |  |
| 17 | `RegisterRecordCallbacks` | `0xE3D0` | 15,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `GetVcpuRegisterMapDefinition` | `0x12200` | 736,464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `GetCfgPointers` | `0xC5ED0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `InjectThread` | `0xC6070` | 44 | UnwindData |  |
| 9 | `InitializeNirvanaClient` | `0xCA1E0` | 522 | UnwindData |  |
| 39 | `TtdWriterStopRecordingCurrentThread` | `0xD1D40` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `TtdWriterResetThrottle` | `0xD1DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `TtdWriterTryPauseRecording` | `0xD1DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `TtdWriterResumeRecording` | `0xD1DD0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `OpenWriter` | `0xD1E30` | 194 | UnwindData |  |
| 10 | `InitializeRecorder` | `0xD2060` | 189 | UnwindData |  |
| 35 | `TtdWriterRelease` | `0xD21D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `TtdWriterGetFileName` | `0xD21E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `TtdWriterDumpSnapshot` | `0xD21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `TtdWriterDumpModuleData` | `0xD2200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `TtdWriterDumpHeaps` | `0xD2210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `TtdWriterAddCustomEvent` | `0xD2220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `TtdWriterStartRecordingCurrentThread` | `0xD2230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `TtdWriterGetThrottleState` | `0xD2240` | 41 | UnwindData |  |
| 33 | `TtdWriterGetState` | `0xD2270` | 57,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `TryPauseSimulation` | `0xE0300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `IsSimulating` | `0xE0320` | 17,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `StubDllEntry` | `0xE48A0` | 39,440 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `g_ttdConstants` | `0xEE2B0` | 657,808 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `ntdllLdrInitializeThunk` | `0x18EC40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `ParametersBlock` | `0x18EC50` | 0 | Indeterminate |  |
