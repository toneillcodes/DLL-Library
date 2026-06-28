# Binary Specification: wow64.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wow64.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `73f03cf82bfd8040ff6a6e54d8bc3fa2f6023c9fd9f7925a8b695d8b6bd4efe2`
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
| 31 | `Wow64ValidateUserCallTarget` | `0x7740` | 313 | UnwindData |  |
| 30 | `Wow64SystemServiceEx` | `0x8C30` | 751 | UnwindData |  |
| 26 | `Wow64ShallowThunkSIZE_T32TO64` | `0x99C0` | 23 | UnwindData |  |
| 2 | `RedirectDosPathUnicode` | `0x99E0` | 466 | UnwindData |  |
| 16 | `Wow64LdrpInitialize` | `0x11ED0` | 812 | UnwindData |  |
| 15 | `Wow64KiUserCallbackDispatcher` | `0x12400` | 811 | UnwindData |  |
| 5 | `Wow64AllocateHeap` | `0x138F0` | 1,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `Wow64FreeHeap` | `0x13F10` | 1,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `Wow64AllocThreadHeap` | `0x14420` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `Wow64IsStackExtentsCheckEnforced` | `0x146A0` | 108 | UnwindData |  |
| 12 | `Wow64FreeThreadHeap` | `0x14CD0` | 165 | UnwindData |  |
| 19 | `Wow64PassExceptionToGuest` | `0x1B350` | 419 | UnwindData |  |
| 8 | `Wow64CheckIfNXEnabled` | `0x1BAB0` | 164 | UnwindData |  |
| 7 | `Wow64ApcRoutine` | `0x205A0` | 42 | UnwindData |  |
| 3 | `RedirectObjectName` | `0x22D20` | 158 | UnwindData |  |
| 9 | `Wow64DispatchExceptionCHPE` | `0x2A630` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `Wow64RaiseException` | `0x2A7C0` | 192 | UnwindData |  |
| 18 | `Wow64NotifyUnsimulateComplete` | `0x2AA30` | 135 | UnwindData |  |
| 28 | `Wow64SuspendLocalProcess` | `0x2AF50` | 762 | UnwindData |  |
| 29 | `Wow64SuspendLocalThread` | `0x2B250` | 1,689 | UnwindData |  |
| 20 | `Wow64PrepareForDebuggerAttach` | `0x2BB50` | 27 | UnwindData |  |
| 10 | `Wow64EmulateAtlThunk` | `0x2BC60` | 546 | UnwindData |  |
| 32 | `Wow64ValidateUserCallTargetFilter` | `0x2BE90` | 156 | UnwindData |  |
| 22 | `Wow64ProcessPendingCrossProcessItems` | `0x2C460` | 529 | UnwindData |  |
| 21 | `Wow64PrepareForException` | `0x36E00` | 119 | UnwindData |  |
