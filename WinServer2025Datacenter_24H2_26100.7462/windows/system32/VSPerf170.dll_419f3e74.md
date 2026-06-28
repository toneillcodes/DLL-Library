# Binary Specification: VSPerf170.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\VSPerf170.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `419f3e74995c11b3341e5964f1d4109ee65cb55a4c4b871dc981981aa156f9cc`
* **Total Exported Functions:** 66

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 24 | `StartProfile` | `0x7AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `StopProfile` | `0x7AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `SuspendProfile` | `0x7AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `ResumeProfile` | `0x7AD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `MarkProfile` | `0x7AE0` | 79 | UnwindData |  |
| 6 | `CommentMarkProfileA` | `0x7B30` | 161 | UnwindData |  |
| 7 | `CommentMarkProfileW` | `0x7BE0` | 85 | UnwindData |  |
| 5 | `CommentMarkAtProfileW` | `0x7C40` | 107 | UnwindData |  |
| 4 | `CommentMarkAtProfileA` | `0x7CB0` | 176 | UnwindData |  |
| 61 | `vCommentMarkProfileW` | `0x7DA0` | 75 | UnwindData |  |
| 60 | `vCommentMarkAtProfileW` | `0x7DF0` | 92 | UnwindData |  |
| 17 | `NameProfileW` | `0x87F0` | 950 | UnwindData |  |
| 16 | `NameProfileA` | `0x8BB0` | 178 | UnwindData |  |
| 8 | `EmitModuleLoadRecord` | `0x8D50` | 28 | UnwindData |  |
| 9 | `EmitModuleLoadRecord2` | `0x8D70` | 32 | UnwindData |  |
| 10 | `EmitModuleUnloadRecord` | `0x8E70` | 28 | UnwindData |  |
| 11 | `EmitModuleUnloadRecord2` | `0x8E90` | 32 | UnwindData |  |
| 14 | `IsMonitorRunning` | `0x8EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `SimulateThreadAttach` | `0x8EC0` | 58 | UnwindData |  |
| 27 | `WriteAllocationPackage` | `0x8F00` | 226 | UnwindData |  |
| 28 | `WriteDeallocationPackage` | `0x8FF0` | 203 | UnwindData |  |
| 2 | `?NotifyJITStarted@@YAXXZ` | `0x90C0` | 47 | UnwindData |  |
| 1 | `?NotifyJITFinished@@YAXXZ` | `0x90F0` | 65 | UnwindData |  |
| 21 | `SetVspHeaderFlags` | `0x9140` | 297 | UnwindData |  |
| 12 | `EnterFunction` | `0x9270` | 198 | UnwindData |  |
| 13 | `ExitFunction` | `0x9340` | 198 | UnwindData |  |
| 19 | `ObjectAllocated` | `0x9410` | 216 | UnwindData |  |
| 18 | `NameToken` | `0x94F0` | 237 | UnwindData |  |
| 23 | `SourceLine` | `0x95E0` | 193 | UnwindData |  |
| 37 | `_CAP_Nullify_TailMerge` | `0x28020` | 2 | UnwindData |  |
| 53 | `__CAP_Nullify_TailMerge` | `0x28020` | 2 | UnwindData |  |
| 43 | `_CAP_StopProfilingTailMergeBackStop_Managed` | `0x280B0` | 2 | UnwindData |  |
| 58 | `__CAP_StopProfilingTailMergeBackStop_Managed` | `0x280B0` | 2 | UnwindData |  |
| 31 | `_CAP_Enter_CatchOrFinally` | `0x280C0` | 2 | UnwindData |  |
| 47 | `__CAP_Enter_CatchOrFinally` | `0x280C0` | 2 | UnwindData |  |
| 40 | `_CAP_StartProfiling_TailMerge_Managed` | `0x280D0` | 2 | UnwindData |  |
| 41 | `_CAP_Start_Profiling` | `0x28400` | 64 | UnwindData |  |
| 56 | `__CAP_Start_Profiling` | `0x28400` | 64 | UnwindData |  |
| 42 | `_CAP_Start_Profiling_TailMerge` | `0x28450` | 64 | UnwindData |  |
| 57 | `__CAP_Start_Profiling_TailMerge` | `0x28450` | 64 | UnwindData |  |
| 29 | `_CAP_End_Profiling` | `0x284A0` | 64 | UnwindData |  |
| 45 | `__CAP_End_Profiling` | `0x284A0` | 64 | UnwindData |  |
| 30 | `_CAP_End_Profiling_TailMergeBackStop` | `0x284F0` | 64 | UnwindData |  |
| 46 | `__CAP_End_Profiling_TailMergeBackStop` | `0x284F0` | 64 | UnwindData |  |
| 33 | `_CAP_Enter_Function` | `0x28540` | 64 | UnwindData |  |
| 49 | `__CAP_Enter_Function` | `0x28540` | 64 | UnwindData |  |
| 35 | `_CAP_Exit_Function` | `0x28590` | 64 | UnwindData |  |
| 51 | `__CAP_Exit_Function` | `0x28590` | 64 | UnwindData |  |
| 34 | `_CAP_Enter_Function_Managed` | `0x285E0` | 5 | UnwindData |  |
| 50 | `__CAP_Enter_Function_Managed` | `0x285E0` | 5 | UnwindData |  |
| 36 | `_CAP_Exit_Function_Managed` | `0x285F0` | 5 | UnwindData |  |
| 52 | `__CAP_Exit_Function_Managed` | `0x285F0` | 5 | UnwindData |  |
| 39 | `_CAP_StartProfiling_Managed` | `0x28600` | 5 | UnwindData |  |
| 55 | `__CAP_StartProfiling_Managed` | `0x28600` | 5 | UnwindData |  |
| 44 | `_CAP_StopProfiling_Managed` | `0x28610` | 5 | UnwindData |  |
| 59 | `__CAP_StopProfiling_Managed` | `0x28610` | 5 | UnwindData |  |
| 32 | `_CAP_Enter_CatchOrFinally_Managed` | `0x28620` | 5 | UnwindData |  |
| 48 | `__CAP_Enter_CatchOrFinally_Managed` | `0x28620` | 5 | UnwindData |  |
| 64 | `vStartProfile` | `0x28630` | 64 | UnwindData |  |
| 65 | `vStopProfile` | `0x28680` | 64 | UnwindData |  |
| 66 | `vSuspendProfile` | `0x286D0` | 64 | UnwindData |  |
| 63 | `vResumeProfile` | `0x28720` | 64 | UnwindData |  |
| 62 | `vMarkProfile` | `0x28770` | 64 | UnwindData |  |
| 38 | `_CAP_Profiling` | `0x287C0` | 64 | UnwindData |  |
| 54 | `__CAP_Profiling` | `0x287C0` | 64 | UnwindData |  |
| 3 | `ClearProcessSecurityAcl` | `0x2B0D0` | 1,394 | UnwindData |  |
