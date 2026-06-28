# Binary Specification: csrsrv.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\csrsrv.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5a800f84f057c62f9aeac00edafb9e4dba2b39dee44cdaeb78f68213c7b658f3`
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
| 26 | `CsrSetBackgroundPriority` | `0x7FC0` | 57 | UnwindData |  |
| 13 | `CsrFlushToBlackBoxRecorder` | `0x8880` | 77 | UnwindData |  |
| 29 | `CsrUnhandledExceptionFilter` | `0x8D20` | 411 | UnwindData |  |
| 33 | `CsrValidateMessageString` | `0x9BA0` | 145 | UnwindData |  |
| 5 | `CsrCreateRemoteThread` | `0xA5E0` | 370 | UnwindData |  |
| 10 | `CsrDestroyProcess` | `0xA760` | 107 | UnwindData |  |
| 16 | `CsrIsClientSandboxed` | `0xA7E0` | 58 | UnwindData |  |
| 27 | `CsrSetForegroundPriority` | `0xADD0` | 58 | UnwindData |  |
