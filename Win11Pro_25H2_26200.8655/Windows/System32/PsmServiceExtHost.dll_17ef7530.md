# Binary Specification: PsmServiceExtHost.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\PsmServiceExtHost.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `17ef7530fa0917623002c3568c4b08c55f4561b32c1202bbab1a9e4ab85594af`
* **Total Exported Functions:** 44

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 38 | `PsmHostStateNotification2` | `0x1CCD0` | 1,466 | UnwindData |  |
| 44 | `PsmMemoryLimitNotification2` | `0x1DD10` | 258 | UnwindData |  |
| 17 | `CrmpInProcActivityFree` | `0x31A00` | 17 | UnwindData |  |
| 20 | `CrmpInProcActivityStop` | `0x34590` | 17 | UnwindData |  |
| 31 | `PsmHamRegisterProcess` | `0x386E0` | 64 | UnwindData |  |
| 30 | `PsmHamReferenceHostId` | `0x41AA0` | 46 | UnwindData |  |
| 34 | `PsmHamTerminatePackage` | `0x43AF0` | 46 | UnwindData |  |
| 32 | `PsmHamTerminateApplication` | `0x57680` | 46 | UnwindData |  |
| 29 | `PsmHamGetPackageDebugMode` | `0x5D450` | 36,672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `HampInProcCreateActivity` | `0x66390` | 88 | UnwindData |  |
| 15 | `BiHamExtHostQueryResourceUsage` | `0x693F0` | 367 | UnwindData |  |
| 22 | `CrmpInProcActivityWindowClosedReasonUnsubscribe` | `0x695E0` | 17 | UnwindData |  |
| 1 | `HampInProcCloseActivity` | `0x6A060` | 1,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `HampInProcStartActivityAsync` | `0x6A6F0` | 6,416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `PsmHamTerminateHost` | `0x6C000` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `HampInProcUpdateActivityProperties` | `0x6C1D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `CrmpInProcActivityAllocate` | `0x6C1E0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `CrmpInProcActivityStart` | `0x6C320` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `HampInProcCreateActivityForProcess` | `0x6C440` | 3,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `HampInProcStopActivity` | `0x6D070` | 3,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `PsmCrmSessionUserNotification` | `0x6DE30` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `PsmCrmSuspendNotification` | `0x6E000` | 13,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `HampInProcTerminateActivityHost` | `0x71330` | 1,888 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `HampInProcCompleteConnection` | `0x71A90` | 976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `HampInProcTerminateApplicationHost` | `0x71E60` | 20,864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `PsmApplicationStateNotification` | `0x76FE0` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `PsmHangNotification` | `0x76FE0` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `PsmHangNotification2` | `0x76FE0` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `PsmHostStateNotification` | `0x76FE0` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `PsmInitializeServiceExtension` | `0x76FE0` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `PsmInitializeServiceExtension2` | `0x76FE0` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `PsmInitializeServiceExtension3` | `0x76FE0` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `PsmMemoryLimitNotification` | `0x76FE0` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `CrmpInProcActivityQueryWindowClosedReasons` | `0x773C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `CrmpInProcActivityWindowClosedReasonSubscribe` | `0x773D0` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `HampInProcIsHostBeingDebugged` | `0x77920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `HampInProcQueryActivityPendDiagnostics` | `0x77930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `HampInProcResetExternalResourcePriority` | `0x77940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `HampInProcSetExternalResourcePriority` | `0x77950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `HampInProcTerminateHostOnProcessExit` | `0x77960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `PsmCrmCleanup` | `0x77970` | 18 | UnwindData |  |
| 26 | `PsmCrmStart` | `0x77990` | 29 | UnwindData |  |
| 28 | `PsmHamDereferenceHostId` | `0x779C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `PsmInitializeServiceExtension4` | `0x779D0` | 819 | UnwindData |  |
