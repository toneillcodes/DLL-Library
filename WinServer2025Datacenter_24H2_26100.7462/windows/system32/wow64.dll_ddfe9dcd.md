# Binary Specification: wow64.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wow64.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ddfe9dcdf0b69ff02fca6e90dfa02f2719c212143f1f4d7f446ffa0692d858f0`
* **Total Exported Functions:** 32

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 13 | `Wow64IsControlFlowGuardEnforced` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.LdrControlFlowGuardEnforced` |
| 1 | `RedirectDosPath` | `0x1010` | 96 | UnwindData |  |
| 27 | `Wow64ShallowThunkSIZE_T64TO32` | `0x1940` | 7,504 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `Wow64ShallowThunkAllocObjectAttributes32TO64_FNC` | `0x3690` | 1,524 | UnwindData |  |
| 25 | `Wow64ShallowThunkAllocSecurityQualityOfService32TO64_FNC` | `0x3C90` | 179 | UnwindData |  |
| 17 | `Wow64LogPrint` | `0x4140` | 6,832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `Wow64AllocateTemp` | `0x5BF0` | 94 | UnwindData |  |
| 31 | `Wow64ValidateUserCallTarget` | `0x76E0` | 313 | UnwindData |  |
| 30 | `Wow64SystemServiceEx` | `0x8BD0` | 751 | UnwindData |  |
| 26 | `Wow64ShallowThunkSIZE_T32TO64` | `0x9960` | 23 | UnwindData |  |
| 2 | `RedirectDosPathUnicode` | `0x9980` | 466 | UnwindData |  |
| 7 | `Wow64ApcRoutine` | `0x11E70` | 42 | UnwindData |  |
| 16 | `Wow64LdrpInitialize` | `0x12030` | 812 | UnwindData |  |
| 15 | `Wow64KiUserCallbackDispatcher` | `0x12560` | 811 | UnwindData |  |
| 5 | `Wow64AllocateHeap` | `0x13A50` | 1,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `Wow64FreeHeap` | `0x14070` | 1,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `Wow64AllocThreadHeap` | `0x14580` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `Wow64IsStackExtentsCheckEnforced` | `0x14800` | 108 | UnwindData |  |
| 12 | `Wow64FreeThreadHeap` | `0x14E30` | 165 | UnwindData |  |
| 19 | `Wow64PassExceptionToGuest` | `0x1B630` | 419 | UnwindData |  |
| 8 | `Wow64CheckIfNXEnabled` | `0x1BD90` | 164 | UnwindData |  |
| 3 | `RedirectObjectName` | `0x22D40` | 158 | UnwindData |  |
| 9 | `Wow64DispatchExceptionCHPE` | `0x29760` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `Wow64RaiseException` | `0x298F0` | 192 | UnwindData |  |
| 18 | `Wow64NotifyUnsimulateComplete` | `0x29B60` | 135 | UnwindData |  |
| 28 | `Wow64SuspendLocalProcess` | `0x2A080` | 762 | UnwindData |  |
| 29 | `Wow64SuspendLocalThread` | `0x2A380` | 1,689 | UnwindData |  |
| 20 | `Wow64PrepareForDebuggerAttach` | `0x2AC80` | 27 | UnwindData |  |
| 10 | `Wow64EmulateAtlThunk` | `0x2AD50` | 546 | UnwindData |  |
| 32 | `Wow64ValidateUserCallTargetFilter` | `0x2AF80` | 156 | UnwindData |  |
| 22 | `Wow64ProcessPendingCrossProcessItems` | `0x2B550` | 529 | UnwindData |  |
| 21 | `Wow64PrepareForException` | `0x35EF0` | 119 | UnwindData |  |
