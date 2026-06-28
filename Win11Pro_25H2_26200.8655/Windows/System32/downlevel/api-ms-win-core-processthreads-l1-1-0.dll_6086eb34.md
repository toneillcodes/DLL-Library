# Binary Specification: api-ms-win-core-processthreads-l1-1-0.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\downlevel\api-ms-win-core-processthreads-l1-1-0.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6086eb34da3f8b7f695e658b380ac1c4b02c617dc7395e99967917a09a25dc43`
* **Total Exported Functions:** 49

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CreateProcessA` | `0x0` | - | Forwarded | Forwarded to: `kernel32.CreateProcessA` |
| 2 | `CreateProcessAsUserW` | `0x0` | - | Forwarded | Forwarded to: `advapi32.CreateProcessAsUserW` |
| 3 | `CreateProcessW` | `0x0` | - | Forwarded | Forwarded to: `kernel32.CreateProcessW` |
| 4 | `CreateRemoteThread` | `0x0` | - | Forwarded | Forwarded to: `kernel32.CreateRemoteThread` |
| 5 | `CreateRemoteThreadEx` | `0x0` | - | Forwarded | Forwarded to: `kernel32.CreateRemoteThreadEx` |
| 6 | `CreateThread` | `0x0` | - | Forwarded | Forwarded to: `kernel32.CreateThread` |
| 7 | `DeleteProcThreadAttributeList` | `0x0` | - | Forwarded | Forwarded to: `kernel32.DeleteProcThreadAttributeList` |
| 8 | `ExitProcess` | `0x0` | - | Forwarded | Forwarded to: `kernel32.ExitProcess` |
| 9 | `ExitThread` | `0x0` | - | Forwarded | Forwarded to: `kernel32.ExitThread` |
| 10 | `FlushProcessWriteBuffers` | `0x0` | - | Forwarded | Forwarded to: `kernel32.FlushProcessWriteBuffers` |
| 11 | `GetCurrentProcess` | `0x0` | - | Forwarded | Forwarded to: `kernel32.GetCurrentProcess` |
| 12 | `GetCurrentProcessId` | `0x0` | - | Forwarded | Forwarded to: `kernel32.GetCurrentProcessId` |
| 13 | `GetCurrentThread` | `0x0` | - | Forwarded | Forwarded to: `kernel32.GetCurrentThread` |
| 14 | `GetCurrentThreadId` | `0x0` | - | Forwarded | Forwarded to: `kernel32.GetCurrentThreadId` |
| 15 | `GetExitCodeProcess` | `0x0` | - | Forwarded | Forwarded to: `kernel32.GetExitCodeProcess` |
| 16 | `GetExitCodeThread` | `0x0` | - | Forwarded | Forwarded to: `kernel32.GetExitCodeThread` |
| 17 | `GetPriorityClass` | `0x0` | - | Forwarded | Forwarded to: `kernel32.GetPriorityClass` |
| 18 | `GetProcessId` | `0x0` | - | Forwarded | Forwarded to: `kernel32.GetProcessId` |
| 19 | `GetProcessIdOfThread` | `0x0` | - | Forwarded | Forwarded to: `kernel32.GetProcessIdOfThread` |
| 20 | `GetProcessTimes` | `0x0` | - | Forwarded | Forwarded to: `kernel32.GetProcessTimes` |
| 21 | `GetProcessVersion` | `0x0` | - | Forwarded | Forwarded to: `kernel32.GetProcessVersion` |
| 22 | `GetStartupInfoW` | `0x0` | - | Forwarded | Forwarded to: `kernel32.GetStartupInfoW` |
| 23 | `GetThreadId` | `0x0` | - | Forwarded | Forwarded to: `kernel32.GetThreadId` |
| 24 | `GetThreadPriority` | `0x0` | - | Forwarded | Forwarded to: `kernel32.GetThreadPriority` |
| 25 | `GetThreadPriorityBoost` | `0x0` | - | Forwarded | Forwarded to: `kernel32.GetThreadPriorityBoost` |
| 26 | `InitializeProcThreadAttributeList` | `0x0` | - | Forwarded | Forwarded to: `kernel32.InitializeProcThreadAttributeList` |
| 27 | `OpenProcessToken` | `0x0` | - | Forwarded | Forwarded to: `advapi32.OpenProcessToken` |
| 28 | `OpenThread` | `0x0` | - | Forwarded | Forwarded to: `kernel32.OpenThread` |
| 29 | `OpenThreadToken` | `0x0` | - | Forwarded | Forwarded to: `advapi32.OpenThreadToken` |
| 30 | `ProcessIdToSessionId` | `0x0` | - | Forwarded | Forwarded to: `kernel32.ProcessIdToSessionId` |
| 31 | `QueryProcessAffinityUpdateMode` | `0x0` | - | Forwarded | Forwarded to: `kernel32.QueryProcessAffinityUpdateMode` |
| 32 | `QueueUserAPC` | `0x0` | - | Forwarded | Forwarded to: `kernel32.QueueUserAPC` |
| 33 | `ResumeThread` | `0x0` | - | Forwarded | Forwarded to: `kernel32.ResumeThread` |
| 34 | `SetPriorityClass` | `0x0` | - | Forwarded | Forwarded to: `kernel32.SetPriorityClass` |
| 35 | `SetProcessAffinityUpdateMode` | `0x0` | - | Forwarded | Forwarded to: `kernel32.SetProcessAffinityUpdateMode` |
| 36 | `SetProcessShutdownParameters` | `0x0` | - | Forwarded | Forwarded to: `kernel32.SetProcessShutdownParameters` |
| 37 | `SetThreadPriority` | `0x0` | - | Forwarded | Forwarded to: `kernel32.SetThreadPriority` |
| 38 | `SetThreadPriorityBoost` | `0x0` | - | Forwarded | Forwarded to: `kernel32.SetThreadPriorityBoost` |
| 39 | `SetThreadStackGuarantee` | `0x0` | - | Forwarded | Forwarded to: `kernel32.SetThreadStackGuarantee` |
| 40 | `SetThreadToken` | `0x0` | - | Forwarded | Forwarded to: `advapi32.SetThreadToken` |
| 41 | `SuspendThread` | `0x0` | - | Forwarded | Forwarded to: `kernel32.SuspendThread` |
| 42 | `SwitchToThread` | `0x0` | - | Forwarded | Forwarded to: `kernel32.SwitchToThread` |
| 43 | `TerminateProcess` | `0x0` | - | Forwarded | Forwarded to: `kernel32.TerminateProcess` |
| 44 | `TerminateThread` | `0x0` | - | Forwarded | Forwarded to: `kernel32.TerminateThread` |
| 45 | `TlsAlloc` | `0x0` | - | Forwarded | Forwarded to: `kernel32.TlsAlloc` |
| 46 | `TlsFree` | `0x0` | - | Forwarded | Forwarded to: `kernel32.TlsFree` |
| 47 | `TlsGetValue` | `0x0` | - | Forwarded | Forwarded to: `kernel32.TlsGetValue` |
| 48 | `TlsSetValue` | `0x0` | - | Forwarded | Forwarded to: `kernel32.TlsSetValue` |
| 49 | `UpdateProcThreadAttribute` | `0x0` | - | Forwarded | Forwarded to: `kernel32.UpdateProcThreadAttribute` |
