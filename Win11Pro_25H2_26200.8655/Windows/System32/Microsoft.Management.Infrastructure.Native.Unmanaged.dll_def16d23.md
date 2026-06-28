# Binary Specification: Microsoft.Management.Infrastructure.Native.Unmanaged.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Microsoft.Management.Infrastructure.Native.Unmanaged.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `def16d2337d3f3532d2fcc5d04ef7551e778a800c853d9e44d391da2e66f37b3`
* **Total Exported Functions:** 31

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 13 | `MI_ApplicationWrapper_Initialize` | `0x1810` | 527 | UnwindData |  |
| 14 | `MI_ApplicationWrapper_ScheduleCleanupCallback` | `0x1A30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `MI_ApplicationWrapper_SetAppDomainIsUnloading` | `0x1A50` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `GetAddr_OperationCallbacks_ClassObjectNeededCallback` | `0x1B20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `GetAddr_OperationCallbacks_FreeIncludedFileBufferCallback` | `0x1B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `GetAddr_OperationCallbacks_GetIncludedFileBufferCallback` | `0x1B40` | 1,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `GetAddr_OperationCallbacks_NativeClassCallback` | `0x21D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `GetAddr_OperationCallbacks_NativeIndicationCallback` | `0x21E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `GetAddr_OperationCallbacks_NativeInstanceCallback` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `GetAddr_OperationCallbacks_NativePromptUserCallback` | `0x2200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `GetAddr_OperationCallbacks_NativeStreamedParameterResultCallback` | `0x2210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `GetAddr_OperationCallbacks_NativeWriteErrorCallback` | `0x2220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `GetAddr_OperationCallbacks_NativeWriteMessageCallback` | `0x2230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `GetAddr_OperationCallbacks_NativeWriteProgressCallback` | `0x2240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `MI_OperationWrapper_DecrementCount_AndDontWorryAboutLifetimeOfMiDotNetDll` | `0x2250` | 59 | UnwindData |  |
| 21 | `MI_OperationWrapper_DecrementCount_AndManageLifetimeOfMiDotNetDll` | `0x22A0` | 118 | UnwindData |  |
| 22 | `MI_OperationWrapper_GetClass` | `0x2320` | 112 | UnwindData |  |
| 23 | `MI_OperationWrapper_GetIndication` | `0x23A0` | 156 | UnwindData |  |
| 24 | `MI_OperationWrapper_GetInstance` | `0x2450` | 112 | UnwindData |  |
| 25 | `MI_OperationWrapper_Initialize` | `0x24D0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `MI_OperationWrapper_ScheduleDrainingWorkIfNeeded` | `0x2530` | 31 | UnwindData |  |
| 27 | `MI_OperationWrapper_SetupDrainingIfNeeded` | `0x2560` | 142 | UnwindData |  |
| 12 | `GetAddr_SessionHandle_OnReleaseHandleCompleted` | `0x26C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `MI_Helpers_GetCurrentSecurityToken` | `0x26D0` | 112 | UnwindData |  |
| 17 | `MI_Helpers_IsClrShuttingDown` | `0x2750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `MI_Helpers_SetClrIsNotShuttingDown` | `0x2770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `MI_Helpers_SetClrIsShuttingDown` | `0x2780` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `UnmanagedMI_GetMiClientFT_V1` | `0x27A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `UnmanagedMI_GetMiEvaluatorFT_V1` | `0x27C0` | 0 | Indeterminate |  |
| 30 | `UnmanagedMI_GetMiMonitoringFT_V1` | `0x27C0` | 0 | Indeterminate |  |
| 31 | `UnmanagedMI_GetMiReactiveExtensionsFT_V1` | `0x27C0` | 0 | Indeterminate |  |
