# Binary Specification: rmclient.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\rmclient.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `71ad628bb5d0e11122785639ceb1048435e45c8d5e5fcb7a3f8cfe049a79ba11`
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
| 14 | `CrmRegister` | `0x89A0` | 160 | UnwindData |  |
| 16 | `CrmUnregister` | `0x8D80` | 49 | UnwindData |  |
| 3 | `CrmActivityAllocate` | `0x8F20` | 248 | UnwindData |  |
| 5 | `CrmActivityFreeWindowClosedReasons` | `0x91F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `DestroyActivityCoordinatorPolicy` | `0x91F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `HamFreeBuffer` | `0x91F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `CrmActivityFree` | `0x9220` | 49 | UnwindData |  |
| 69 | `HamHostIdInitializeKey` | `0x93E0` | 78 | UnwindData |  |
| 41 | `HamCreateActivityForProcess` | `0x9610` | 477 | UnwindData |  |
| 39 | `HamCreateActivity` | `0x9800` | 34 | UnwindData |  |
| 40 | `HamCreateActivityEx` | `0x9830` | 662 | UnwindData |  |
| 78 | `HamPopulateActivityPropertiesByClass` | `0x9C40` | 94 | UnwindData |  |
| 28 | `HamCloseActivity` | `0x9F90` | 563 | UnwindData |  |
| 77 | `HamPopulateActivityProperties` | `0xA7B0` | 491 | UnwindData |  |
| 68 | `HamHostIdFindOrCreate` | `0xABC0` | 538 | UnwindData |  |
| 84 | `HamQueryPackageUsageInfo` | `0xB410` | 36 | UnwindData |  |
| 22 | `DllGetActivationFactory` | `0xBD60` | 146 | UnwindData |  |
| 43 | `HamCreateExtendedExecution` | `0xC7C0` | 280 | UnwindData |  |
| 61 | `HamGetApplicationInterruptiveUIState` | `0xCD20` | 722 | UnwindData |  |
| 81 | `HamQueryCallerTerminateReason` | `0xD000` | 234 | UnwindData |  |
| 65 | `HamGetStateSnapshotForAumid` | `0xD7F0` | 697 | UnwindData |  |
| 86 | `HamRegisterDesktopProcessWithAppContainerToken` | `0xDAB0` | 1,484 | UnwindData |  |
| 112 | `HamUpdateActivityProperties` | `0xE920` | 108 | UnwindData |  |
| 21 | `DllCanUnloadNow` | `0xE9A0` | 81 | UnwindData |  |
| 100 | `HamStartActivityAsync` | `0xEA00` | 128 | UnwindData |  |
| 114 | `RmAccessCheck` | `0xEDA0` | 157 | UnwindData |  |
| 1 | `AppModelQueryLifecyclePolicy` | `0xF010` | 279 | UnwindData |  |
| 62 | `HamGetApplicationStateForPsmKey` | `0xF4E0` | 203 | UnwindData |  |
| 66 | `HamHostIdCreateSingleUse` | `0xF5C0` | 490 | UnwindData |  |
| 139 | `RmGetNotification` | `0xFB10` | 74 | UnwindData |  |
| 118 | `RmAcquireResources` | `0xFB60` | 186 | UnwindData |  |
| 146 | `RmReleaseResources` | `0xFC20` | 61 | UnwindData |  |
| 11 | `CrmActivityStop` | `0x10070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `HamTerminateActivityHost` | `0x10080` | 30 | UnwindData |  |
| 104 | `HamTerminateActivityHostEx` | `0x100B0` | 198 | UnwindData |  |
| 10 | `CrmActivityStart` | `0x102D0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `HamStopActivity` | `0x10320` | 105 | UnwindData |  |
| 92 | `HamServicingOpenPackageHandle` | `0x10820` | 197 | UnwindData |  |
| 71 | `HamInitializeActivityAutoRestartProperties` | `0x10C50` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `HamInitializeStateChangeFlags` | `0x10C50` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `RmActivityImportanceInitialize` | `0x10C50` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `HamDebugOpenPackageHandle` | `0x10F00` | 182 | UnwindData |  |
| 93 | `HamServicingQueryActiveAppsInPackage` | `0x10FE0` | 155 | UnwindData |  |
| 111 | `HamTryEstimateRemainingQuiesceTime` | `0x11220` | 79 | UnwindData |  |
| 105 | `HamTerminateApplicationHost` | `0x11280` | 270 | UnwindData |  |
| 90 | `HamServicingClosePackageHandle` | `0x113A0` | 79 | UnwindData |  |
| 72 | `HamInitializeActivityDynamicProperties` | `0x11450` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `HamPlmNotifyNewSession` | `0x11650` | 672 | UnwindData |  |
| 37 | `HamConnectToServer` | `0x11A80` | 34 | UnwindData |  |
| 38 | `HamConnectToServerEx` | `0x11AB0` | 449 | UnwindData |  |
| 6 | `CrmActivityQueryWindowClosedReasons` | `0x11E90` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `HamDebugClosePackageHandle` | `0x11F00` | 79 | UnwindData |  |
| 47 | `HamDebugQueryPackageState` | `0x12030` | 179 | UnwindData |  |
| 126 | `RmEnableLimits` | `0x12150` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `HamStartExtendedExecutionAsync` | `0x123F0` | 79 | UnwindData |  |
| 30 | `HamCompleteExtendedExecution` | `0x12950` | 188 | UnwindData |  |
| 109 | `HamTerminateSelfEx` | `0x12A30` | 78 | UnwindData |  |
| 74 | `HamIsHostBeingDebugged` | `0x12A90` | 309 | UnwindData |  |
| 7 | `CrmActivityRenew` | `0x12BD0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `CrmWorkStart` | `0x12BD0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `CrmWorkStop` | `0x12BD0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `HamServicingEnableServicing` | `0x12C40` | 224 | UnwindData |  |
| 8 | `CrmActivityRequest` | `0x12D50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `CrmActivityWindowClosedReasonUnsubscribe` | `0x12D60` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `HamSessionStateLogoffSession` | `0x12DD0` | 78 | UnwindData |  |
| 83 | `HamQueryPackageStateSummary` | `0x13330` | 176 | UnwindData |  |
| 130 | `RmGameModeInitializeResourceRequest` | `0x134D0` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `CrmActivityWindowClosedReasonSubscribe` | `0x13740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `HamDisconnectForDebugging` | `0x13760` | 5,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `HamDisconnectForExtendedExecution` | `0x13760` | 5,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `HamDisconnectForFullTrust` | `0x13760` | 5,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `HamDisconnectForServicing` | `0x13760` | 5,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `HamDisconnectForSessionState` | `0x13760` | 5,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `HamDisconnectForStateChangeNotifications` | `0x13760` | 5,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `CrmSubscribe` | `0x14C10` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `CrmUnsubscribe` | `0x14C10` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `RmAcquireResourceSet` | `0x14C10` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `RmAcquireResourceSetEx` | `0x14C10` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `RmApplyResourceSet` | `0x14C10` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `RmApplyResourceSetToHost` | `0x14C10` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `RmConnectToResourceManager` | `0x14C10` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `RmDisconnectFromResourceManager` | `0x14C10` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `RmQueryHostMemoryLimitValues` | `0x14C10` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `RmRegisterActivityHostCallbacks` | `0x14C10` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `RmReleaseResourceSet` | `0x14C10` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `RmReleaseResourceSetEx` | `0x14C10` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `RmSetHostLimit` | `0x14C10` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | `RmUnregisterActivityHost` | `0x14C10` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `RmUnregisterActivityHostCallbacks` | `0x14C10` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `RmUpdateResourceSetProperties` | `0x15160` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `DllGetClassObject` | `0x15350` | 65 | UnwindData |  |
| 127 | `RmGameModeDisableForRegisteredProcess` | `0x153A0` | 180 | UnwindData |  |
| 128 | `RmGameModeDisableForRegisteredProcessById` | `0x15460` | 178 | UnwindData |  |
| 131 | `RmGameModeReenableForRegisteredProcess` | `0x15520` | 180 | UnwindData |  |
| 132 | `RmGameModeReenableForRegisteredProcessById` | `0x155E0` | 178 | UnwindData |  |
| 133 | `RmGameModeRegisterPairedAuxiliaryProcess` | `0x156A0` | 237 | UnwindData |  |
| 134 | `RmGameModeRegisterPairedAuxiliaryProcessById` | `0x157A0` | 237 | UnwindData |  |
| 136 | `RmGameModeRegisterProcessById` | `0x158A0` | 223 | UnwindData |  |
| 137 | `RmGameModeUnregisterProcess` | `0x15990` | 180 | UnwindData |  |
| 138 | `RmGameModeUnregisterProcessById` | `0x15A50` | 178 | UnwindData |  |
| 142 | `RmRegisterForGameMode` | `0x15B10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `RmUnregisterForGameMode` | `0x15B10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `RmActivityImportanceTakeMostImportant` | `0x15B20` | 25 | UnwindData |  |
| 147 | `RmResourceLimitFlagsInitialize` | `0x15B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 148 | `RmResourceLimitsInitialize` | `0x15B50` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `RmResourceSetPropertiesInitialize` | `0x15B80` | 56 | UnwindData |  |
| 115 | `RmAccessCheckOnSelf` | `0x19800` | 47 | UnwindData |  |
| 123 | `RmAvailabilityCheck` | `0x19840` | 112 | UnwindData |  |
| 143 | `RmRegisterResource` | `0x198C0` | 91 | UnwindData |  |
| 25 | `HamAddDependency` | `0x1A3F0` | 84 | UnwindData |  |
| 26 | `HamAddHostDependency` | `0x1A450` | 88 | UnwindData |  |
| 27 | `HamAssociateActivityContext` | `0x1A4B0` | 513 | UnwindData |  |
| 33 | `HamConnectForFullTrust` | `0x1A6C0` | 124 | UnwindData |  |
| 45 | `HamDebugModeEnable` | `0x1A750` | 79 | UnwindData |  |
| 48 | `HamDebugSuspendPackage` | `0x1A7B0` | 84 | UnwindData |  |
| 49 | `HamDebugTerminatePackage` | `0x1A810` | 94 | UnwindData |  |
| 58 | `HamFullTrustClosePackageHandle` | `0x1A880` | 79 | UnwindData |  |
| 59 | `HamFullTrustOpenPackageHandle` | `0x1A8E0` | 195 | UnwindData |  |
| 60 | `HamFullTrustTerminatePackage` | `0x1A9B0` | 88 | UnwindData |  |
| 64 | `HamGetPackageInterruptiveUIState` | `0x1AA10` | 310 | UnwindData |  |
| 75 | `HamPendDiagnosticsToWaitTimeout` | `0x1AB50` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `HamQueryActivityPendDiagnostics` | `0x1AB90` | 112 | UnwindData |  |
| 80 | `HamQueryApplicationUsageInfo` | `0x1AC10` | 313 | UnwindData |  |
| 82 | `HamQueryHostStateSummary` | `0x1AD50` | 291 | UnwindData |  |
| 85 | `HamQueryTaskCompletionsForTerminateGraph` | `0x1AE80` | 121 | UnwindData |  |
| 87 | `HamRemoveDependency` | `0x1AF00` | 84 | UnwindData |  |
| 88 | `HamRemoveHostDependency` | `0x1AF60` | 84 | UnwindData |  |
| 89 | `HamResetExternalResourcePriority` | `0x1AFC0` | 124 | UnwindData |  |
| 94 | `HamServicingQueryPackageState` | `0x1B050` | 179 | UnwindData |  |
| 95 | `HamServicingTerminatePackage` | `0x1B110` | 94 | UnwindData |  |
| 97 | `HamSessionStateLogoffUser` | `0x1B180` | 133 | UnwindData |  |
| 98 | `HamSetCommitProperties` | `0x1B210` | 281 | UnwindData |  |
| 99 | `HamSetExternalResourcePriority` | `0x1B330` | 121 | UnwindData |  |
| 106 | `HamTerminateHostOnProcessExit` | `0x1B3B0` | 177 | UnwindData |  |
| 107 | `HamTerminateIfSuspendedByProcess` | `0x1B470` | 84 | UnwindData |  |
| 108 | `HamTerminateSelf` | `0x1B4D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `HamTerminateSelfOnProcessExit` | `0x1B4E0` | 92 | UnwindData |  |
| 9 | `CrmActivityRequestAndWait` | `0x1B800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CreateActivityCoordinatorPolicy` | `0x1B810` | 115 | UnwindData |  |
| 24 | `GetActivityCoordinatorPolicyResourceCondition` | `0x1B890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `IsActivityCoordinatorResourceSupported` | `0x1B8B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `SetActivityCoordinatorPolicyResourceCondition` | `0x1B8D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `SubscribeActivityCoordinatorPolicy` | `0x1B900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `UnsubscribeActivityCoordinatorPolicy` | `0x1B910` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `HamCreateAutoRestartActivity` | `0x1BD70` | 224 | UnwindData |  |
