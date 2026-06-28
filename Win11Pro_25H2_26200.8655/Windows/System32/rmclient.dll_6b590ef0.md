# Binary Specification: rmclient.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\rmclient.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6b590ef098c1f0760237946686cb3bf33b2e2e31099a4ae9f9d548219c77069c`
* **Total Exported Functions:** 157

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 29 | `HamCompleteActivityRestore` | `0x27C0` | 605 | UnwindData |  |
| 63 | `HamGetInterruptiveUIStateForAumid` | `0x2A30` | 269 | UnwindData |  |
| 67 | `HamHostIdFind` | `0x2B50` | 177 | UnwindData |  |
| 135 | `RmGameModeRegisterProcess` | `0x2D40` | 229 | UnwindData |  |
| 36 | `HamConnectForStateChangeNotifications` | `0x2E60` | 269 | UnwindData |  |
| 34 | `HamConnectForServicing` | `0x4240` | 223 | UnwindData |  |
| 32 | `HamConnectForExtendedExecution` | `0x4330` | 256 | UnwindData |  |
| 56 | `HamDisconnectFromServer` | `0x5090` | 143 | UnwindData |  |
| 35 | `HamConnectForSessionState` | `0x53F0` | 97 | UnwindData |  |
| 31 | `HamConnectForDebugging` | `0x5510` | 124 | UnwindData |  |
| 129 | `RmGameModeGetLargestValidResourceRequest` | `0x55A0` | 180 | UnwindData |  |
| 70 | `HamHostIdRetrieveDynamicId` | `0x5760` | 198 | UnwindData |  |
| 14 | `CrmRegister` | `0x8640` | 160 | UnwindData |  |
| 16 | `CrmUnregister` | `0x8A20` | 49 | UnwindData |  |
| 3 | `CrmActivityAllocate` | `0x8BC0` | 248 | UnwindData |  |
| 5 | `CrmActivityFreeWindowClosedReasons` | `0x8E90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `DestroyActivityCoordinatorPolicy` | `0x8E90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `HamFreeBuffer` | `0x8E90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `CrmActivityFree` | `0x8EC0` | 49 | UnwindData |  |
| 69 | `HamHostIdInitializeKey` | `0x9080` | 78 | UnwindData |  |
| 41 | `HamCreateActivityForProcess` | `0x92B0` | 477 | UnwindData |  |
| 39 | `HamCreateActivity` | `0x94A0` | 34 | UnwindData |  |
| 40 | `HamCreateActivityEx` | `0x94D0` | 662 | UnwindData |  |
| 78 | `HamPopulateActivityPropertiesByClass` | `0x98E0` | 94 | UnwindData |  |
| 28 | `HamCloseActivity` | `0x9C30` | 563 | UnwindData |  |
| 77 | `HamPopulateActivityProperties` | `0xA490` | 491 | UnwindData |  |
| 68 | `HamHostIdFindOrCreate` | `0xA8A0` | 538 | UnwindData |  |
| 84 | `HamQueryPackageUsageInfo` | `0xB0F0` | 36 | UnwindData |  |
| 22 | `DllGetActivationFactory` | `0xBA40` | 146 | UnwindData |  |
| 43 | `HamCreateExtendedExecution` | `0xC4C0` | 280 | UnwindData |  |
| 61 | `HamGetApplicationInterruptiveUIState` | `0xC7D0` | 722 | UnwindData |  |
| 81 | `HamQueryCallerTerminateReason` | `0xCAB0` | 234 | UnwindData |  |
| 65 | `HamGetStateSnapshotForAumid` | `0xD2A0` | 697 | UnwindData |  |
| 86 | `HamRegisterDesktopProcessWithAppContainerToken` | `0xD560` | 1,484 | UnwindData |  |
| 112 | `HamUpdateActivityProperties` | `0xE3C0` | 108 | UnwindData |  |
| 21 | `DllCanUnloadNow` | `0xE440` | 81 | UnwindData |  |
| 100 | `HamStartActivityAsync` | `0xE4A0` | 128 | UnwindData |  |
| 114 | `RmAccessCheck` | `0xE840` | 157 | UnwindData |  |
| 1 | `AppModelQueryLifecyclePolicy` | `0xEAB0` | 279 | UnwindData |  |
| 62 | `HamGetApplicationStateForPsmKey` | `0xEF30` | 203 | UnwindData |  |
| 66 | `HamHostIdCreateSingleUse` | `0xF010` | 490 | UnwindData |  |
| 139 | `RmGetNotification` | `0xF560` | 74 | UnwindData |  |
| 118 | `RmAcquireResources` | `0xF5B0` | 186 | UnwindData |  |
| 146 | `RmReleaseResources` | `0xF670` | 61 | UnwindData |  |
| 11 | `CrmActivityStop` | `0xFA20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `HamTerminateActivityHost` | `0xFA30` | 30 | UnwindData |  |
| 104 | `HamTerminateActivityHostEx` | `0xFA60` | 198 | UnwindData |  |
| 10 | `CrmActivityStart` | `0xFC80` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `HamStopActivity` | `0xFCD0` | 105 | UnwindData |  |
| 92 | `HamServicingOpenPackageHandle` | `0x101D0` | 197 | UnwindData |  |
| 71 | `HamInitializeActivityAutoRestartProperties` | `0x105B0` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `HamInitializeStateChangeFlags` | `0x105B0` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `RmActivityImportanceInitialize` | `0x105B0` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `HamDebugOpenPackageHandle` | `0x108B0` | 182 | UnwindData |  |
| 93 | `HamServicingQueryActiveAppsInPackage` | `0x10990` | 155 | UnwindData |  |
| 111 | `HamTryEstimateRemainingQuiesceTime` | `0x10BD0` | 79 | UnwindData |  |
| 105 | `HamTerminateApplicationHost` | `0x10C60` | 270 | UnwindData |  |
| 90 | `HamServicingClosePackageHandle` | `0x10D80` | 79 | UnwindData |  |
| 72 | `HamInitializeActivityDynamicProperties` | `0x10E30` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `HamPlmNotifyNewSession` | `0x11090` | 672 | UnwindData |  |
| 37 | `HamConnectToServer` | `0x11470` | 34 | UnwindData |  |
| 38 | `HamConnectToServerEx` | `0x114A0` | 449 | UnwindData |  |
| 6 | `CrmActivityQueryWindowClosedReasons` | `0x118F0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `HamDebugClosePackageHandle` | `0x11960` | 79 | UnwindData |  |
| 47 | `HamDebugQueryPackageState` | `0x11A90` | 179 | UnwindData |  |
| 126 | `RmEnableLimits` | `0x11BA0` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `HamStartExtendedExecutionAsync` | `0x11E40` | 79 | UnwindData |  |
| 30 | `HamCompleteExtendedExecution` | `0x123A0` | 188 | UnwindData |  |
| 109 | `HamTerminateSelfEx` | `0x12480` | 78 | UnwindData |  |
| 74 | `HamIsHostBeingDebugged` | `0x124E0` | 309 | UnwindData |  |
| 7 | `CrmActivityRenew` | `0x12620` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `CrmWorkStart` | `0x12620` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `CrmWorkStop` | `0x12620` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `HamServicingEnableServicing` | `0x12690` | 224 | UnwindData |  |
| 8 | `CrmActivityRequest` | `0x127A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `CrmActivityWindowClosedReasonUnsubscribe` | `0x127B0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `HamSessionStateLogoffSession` | `0x12820` | 78 | UnwindData |  |
| 83 | `HamQueryPackageStateSummary` | `0x135C0` | 176 | UnwindData |  |
| 130 | `RmGameModeInitializeResourceRequest` | `0x13760` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `CrmActivityWindowClosedReasonSubscribe` | `0x13910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `HamDisconnectForDebugging` | `0x13930` | 5,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `HamDisconnectForExtendedExecution` | `0x13930` | 5,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `HamDisconnectForFullTrust` | `0x13930` | 5,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `HamDisconnectForServicing` | `0x13930` | 5,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `HamDisconnectForSessionState` | `0x13930` | 5,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `HamDisconnectForStateChangeNotifications` | `0x13930` | 5,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `CrmSubscribe` | `0x14DE0` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `CrmUnsubscribe` | `0x14DE0` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `RmAcquireResourceSet` | `0x14DE0` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `RmAcquireResourceSetEx` | `0x14DE0` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `RmApplyResourceSet` | `0x14DE0` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `RmApplyResourceSetToHost` | `0x14DE0` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `RmConnectToResourceManager` | `0x14DE0` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `RmDisconnectFromResourceManager` | `0x14DE0` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `RmQueryHostMemoryLimitValues` | `0x14DE0` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `RmRegisterActivityHostCallbacks` | `0x14DE0` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `RmReleaseResourceSet` | `0x14DE0` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `RmReleaseResourceSetEx` | `0x14DE0` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `RmSetHostLimit` | `0x14DE0` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | `RmUnregisterActivityHost` | `0x14DE0` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `RmUnregisterActivityHostCallbacks` | `0x14DE0` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `RmUpdateResourceSetProperties` | `0x15330` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `DllGetClassObject` | `0x15520` | 65 | UnwindData |  |
| 127 | `RmGameModeDisableForRegisteredProcess` | `0x15570` | 180 | UnwindData |  |
| 128 | `RmGameModeDisableForRegisteredProcessById` | `0x15630` | 178 | UnwindData |  |
| 131 | `RmGameModeReenableForRegisteredProcess` | `0x156F0` | 180 | UnwindData |  |
| 132 | `RmGameModeReenableForRegisteredProcessById` | `0x157B0` | 178 | UnwindData |  |
| 133 | `RmGameModeRegisterPairedAuxiliaryProcess` | `0x15870` | 237 | UnwindData |  |
| 134 | `RmGameModeRegisterPairedAuxiliaryProcessById` | `0x15970` | 237 | UnwindData |  |
| 136 | `RmGameModeRegisterProcessById` | `0x15A70` | 223 | UnwindData |  |
| 137 | `RmGameModeUnregisterProcess` | `0x15B60` | 180 | UnwindData |  |
| 138 | `RmGameModeUnregisterProcessById` | `0x15C20` | 178 | UnwindData |  |
| 142 | `RmRegisterForGameMode` | `0x15CE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `RmUnregisterForGameMode` | `0x15CE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `RmActivityImportanceTakeMostImportant` | `0x15CF0` | 25 | UnwindData |  |
| 147 | `RmResourceLimitFlagsInitialize` | `0x15D10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 148 | `RmResourceLimitsInitialize` | `0x15D20` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `RmResourceSetPropertiesInitialize` | `0x15D50` | 56 | UnwindData |  |
| 115 | `RmAccessCheckOnSelf` | `0x199A0` | 47 | UnwindData |  |
| 123 | `RmAvailabilityCheck` | `0x199E0` | 112 | UnwindData |  |
| 143 | `RmRegisterResource` | `0x19A60` | 91 | UnwindData |  |
| 25 | `HamAddDependency` | `0x1B070` | 84 | UnwindData |  |
| 26 | `HamAddHostDependency` | `0x1B0D0` | 88 | UnwindData |  |
| 27 | `HamAssociateActivityContext` | `0x1B130` | 513 | UnwindData |  |
| 33 | `HamConnectForFullTrust` | `0x1B340` | 124 | UnwindData |  |
| 45 | `HamDebugModeEnable` | `0x1B3D0` | 79 | UnwindData |  |
| 48 | `HamDebugSuspendPackage` | `0x1B430` | 84 | UnwindData |  |
| 49 | `HamDebugTerminatePackage` | `0x1B490` | 94 | UnwindData |  |
| 58 | `HamFullTrustClosePackageHandle` | `0x1B500` | 79 | UnwindData |  |
| 59 | `HamFullTrustOpenPackageHandle` | `0x1B560` | 195 | UnwindData |  |
| 60 | `HamFullTrustTerminatePackage` | `0x1B630` | 88 | UnwindData |  |
| 64 | `HamGetPackageInterruptiveUIState` | `0x1B690` | 310 | UnwindData |  |
| 75 | `HamPendDiagnosticsToWaitTimeout` | `0x1B7D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `HamQueryActivityPendDiagnostics` | `0x1B810` | 112 | UnwindData |  |
| 80 | `HamQueryApplicationUsageInfo` | `0x1B890` | 313 | UnwindData |  |
| 82 | `HamQueryHostStateSummary` | `0x1B9D0` | 291 | UnwindData |  |
| 85 | `HamQueryTaskCompletionsForTerminateGraph` | `0x1BB00` | 121 | UnwindData |  |
| 87 | `HamRemoveDependency` | `0x1BB80` | 84 | UnwindData |  |
| 88 | `HamRemoveHostDependency` | `0x1BBE0` | 84 | UnwindData |  |
| 89 | `HamResetExternalResourcePriority` | `0x1BC40` | 124 | UnwindData |  |
| 94 | `HamServicingQueryPackageState` | `0x1BCD0` | 179 | UnwindData |  |
| 95 | `HamServicingTerminatePackage` | `0x1BD90` | 94 | UnwindData |  |
| 97 | `HamSessionStateLogoffUser` | `0x1BE00` | 133 | UnwindData |  |
| 98 | `HamSetCommitProperties` | `0x1BE90` | 281 | UnwindData |  |
| 99 | `HamSetExternalResourcePriority` | `0x1BFB0` | 121 | UnwindData |  |
| 106 | `HamTerminateHostOnProcessExit` | `0x1C030` | 177 | UnwindData |  |
| 107 | `HamTerminateIfSuspendedByProcess` | `0x1C0F0` | 84 | UnwindData |  |
| 108 | `HamTerminateSelf` | `0x1C150` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `HamTerminateSelfOnProcessExit` | `0x1C160` | 92 | UnwindData |  |
| 9 | `CrmActivityRequestAndWait` | `0x1C480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CreateActivityCoordinatorPolicy` | `0x1C490` | 115 | UnwindData |  |
| 24 | `GetActivityCoordinatorPolicyResourceCondition` | `0x1C510` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `IsActivityCoordinatorResourceSupported` | `0x1C530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `SetActivityCoordinatorPolicyResourceCondition` | `0x1C550` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `SubscribeActivityCoordinatorPolicy` | `0x1C580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `UnsubscribeActivityCoordinatorPolicy` | `0x1C590` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `HamCreateAutoRestartActivity` | `0x1C9F0` | 224 | UnwindData |  |
