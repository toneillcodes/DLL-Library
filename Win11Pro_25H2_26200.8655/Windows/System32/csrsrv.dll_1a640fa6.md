# Binary Specification: csrsrv.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\csrsrv.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1a640fa61c02bd643524d022c2158e2f19054f9147ee7adb92143ce4401d53dd`
* **Total Exported Functions:** 33

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `CsrConnectToUser` | `0x1470` | 161 | UnwindData |  |
| 18 | `CsrLockThreadByClientId` | `0x18A0` | 221 | UnwindData |  |
| 6 | `CsrCreateThread` | `0x1E40` | 233 | UnwindData |  |
| 25 | `CsrServerInitialization` | `0x2960` | 1,336 | UnwindData |  |
| 4 | `CsrCreateProcess` | `0x42B0` | 35 | UnwindData |  |
| 9 | `CsrDereferenceThread` | `0x48E0` | 43 | UnwindData |  |
| 31 | `CsrUnlockThread` | `0x4960` | 36 | UnwindData |  |
| 30 | `CsrUnlockProcess` | `0x4B00` | 72 | UnwindData |  |
| 11 | `CsrDestroyThread` | `0x4C50` | 186 | UnwindData |  |
| 1 | `CsrAddStaticServerThread` | `0x57F0` | 171 | UnwindData |  |
| 12 | `CsrExecServerThread` | `0x58B0` | 302 | UnwindData |  |
| 32 | `CsrValidateMessageBuffer` | `0x5A60` | 220 | UnwindData |  |
| 15 | `CsrImpersonateClient` | `0x5B50` | 88 | UnwindData |  |
| 8 | `CsrDereferenceProcess` | `0x5D80` | 102 | UnwindData |  |
| 14 | `CsrGetProcessLuid` | `0x5DF0` | 116 | UnwindData |  |
| 24 | `CsrRevertToSelf` | `0x6090` | 467 | UnwindData |  |
| 17 | `CsrLockProcessByClientId` | `0x6270` | 129 | UnwindData |  |
| 19 | `CsrLockedReferenceProcess` | `0x6300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `CsrShutdownProcesses` | `0x6310` | 490 | UnwindData |  |
| 2 | `CsrCallServerFromServer` | `0x6C90` | 286 | UnwindData |  |
| 21 | `CsrReferenceThread` | `0x6DF0` | 1,904 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `CsrDeferredCreateProcess` | `0x7560` | 1,536 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `CsrQueryApiPort` | `0x7B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `CsrRegisterClientThreadSetup` | `0x7B70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `CsrReplyToMessage` | `0x7B90` | 62 | UnwindData |  |
| 26 | `CsrSetBackgroundPriority` | `0x7F90` | 2,192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `CsrSetForegroundPriority` | `0x7F90` | 2,192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `CsrFlushToBlackBoxRecorder` | `0x8820` | 77 | UnwindData |  |
| 29 | `CsrUnhandledExceptionFilter` | `0x8CC0` | 411 | UnwindData |  |
| 33 | `CsrValidateMessageString` | `0x9B40` | 145 | UnwindData |  |
| 5 | `CsrCreateRemoteThread` | `0x9BE0` | 370 | UnwindData |  |
| 10 | `CsrDestroyProcess` | `0x9D60` | 107 | UnwindData |  |
| 16 | `CsrIsClientSandboxed` | `0x9DE0` | 58 | UnwindData |  |
