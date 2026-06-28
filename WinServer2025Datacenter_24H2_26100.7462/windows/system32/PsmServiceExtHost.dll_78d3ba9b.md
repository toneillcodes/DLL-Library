# Binary Specification: PsmServiceExtHost.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\PsmServiceExtHost.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `78d3ba9bd3f10f2a0001f8fd5ea93d9d9ef52dab0868af562146311e806a7d3d`
* **Total Exported Functions:** 44

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 38 | `PsmHostStateNotification2` | `0x1CD40` | 1,466 | UnwindData |  |
| 44 | `PsmMemoryLimitNotification2` | `0x1DD80` | 258 | UnwindData |  |
| 17 | `CrmpInProcActivityFree` | `0x31A70` | 17 | UnwindData |  |
| 20 | `CrmpInProcActivityStop` | `0x34600` | 17 | UnwindData |  |
| 31 | `PsmHamRegisterProcess` | `0x38750` | 64 | UnwindData |  |
| 30 | `PsmHamReferenceHostId` | `0x41B10` | 46 | UnwindData |  |
| 34 | `PsmHamTerminatePackage` | `0x43B60` | 46 | UnwindData |  |
| 32 | `PsmHamTerminateApplication` | `0x576F0` | 46 | UnwindData |  |
| 29 | `PsmHamGetPackageDebugMode` | `0x5D430` | 36,784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `HampInProcCreateActivity` | `0x663E0` | 88 | UnwindData |  |
| 15 | `BiHamExtHostQueryResourceUsage` | `0x69540` | 367 | UnwindData |  |
| 22 | `CrmpInProcActivityWindowClosedReasonUnsubscribe` | `0x69730` | 17 | UnwindData |  |
| 1 | `HampInProcCloseActivity` | `0x6A1B0` | 1,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `HampInProcStartActivityAsync` | `0x6A840` | 6,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `PsmHamTerminateHost` | `0x6C1B0` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `HampInProcUpdateActivityProperties` | `0x6C3D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `CrmpInProcActivityAllocate` | `0x6C3E0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `CrmpInProcActivityStart` | `0x6C520` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `HampInProcCreateActivityForProcess` | `0x6C640` | 3,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `HampInProcStopActivity` | `0x6D270` | 3,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `PsmCrmSessionUserNotification` | `0x6E030` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `PsmCrmSuspendNotification` | `0x6E200` | 12,832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `HampInProcTerminateActivityHost` | `0x71420` | 1,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `HampInProcCompleteConnection` | `0x71B20` | 944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `HampInProcTerminateApplicationHost` | `0x71ED0` | 20,464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `PsmApplicationStateNotification` | `0x76EC0` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `PsmHangNotification` | `0x76EC0` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `PsmHangNotification2` | `0x76EC0` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `PsmHostStateNotification` | `0x76EC0` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `PsmInitializeServiceExtension` | `0x76EC0` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `PsmInitializeServiceExtension2` | `0x76EC0` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `PsmInitializeServiceExtension3` | `0x76EC0` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `PsmMemoryLimitNotification` | `0x76EC0` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `CrmpInProcActivityQueryWindowClosedReasons` | `0x772A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `CrmpInProcActivityWindowClosedReasonSubscribe` | `0x772B0` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `HampInProcIsHostBeingDebugged` | `0x77800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `HampInProcQueryActivityPendDiagnostics` | `0x77810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `HampInProcResetExternalResourcePriority` | `0x77820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `HampInProcSetExternalResourcePriority` | `0x77830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `HampInProcTerminateHostOnProcessExit` | `0x77840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `PsmCrmCleanup` | `0x77850` | 18 | UnwindData |  |
| 26 | `PsmCrmStart` | `0x77870` | 29 | UnwindData |  |
| 28 | `PsmHamDereferenceHostId` | `0x778A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `PsmInitializeServiceExtension4` | `0x778B0` | 819 | UnwindData |  |
