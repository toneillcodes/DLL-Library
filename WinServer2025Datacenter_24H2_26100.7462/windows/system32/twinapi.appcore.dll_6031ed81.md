# Binary Specification: twinapi.appcore.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\twinapi.appcore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6031ed81ed4ab381f388ba838bf0fbb5f72d473d19702fe928ea8959237e9f88`
* **Total Exported Functions:** 148

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | *Ordinal Only* | `0x10BE0` | 2,415 | UnwindData |  |
| 9 | *Ordinal Only* | `0x121E0` | 558 | UnwindData |  |
| 8 | *Ordinal Only* | `0x12E30` | 1,263 | UnwindData |  |
| 6 | *Ordinal Only* | `0x13360` | 1,726 | UnwindData |  |
| 83 | `PsmBlockAppStateChangeCompletion` | `0x18610` | 352 | UnwindData |  |
| 137 | `PsmUnblockAppStateChangeCompletion` | `0x1A160` | 402 | UnwindData |  |
| 139 | `PsmWaitForAppResume` | `0x1A620` | 102 | UnwindData |  |
| 504 | *Ordinal Only* | `0x1CE20` | 99 | UnwindData |  |
| 10 | *Ordinal Only* | `0x2A3E0` | 504 | UnwindData |  |
| 102 | `PsmQueryCurrentAppState` | `0x39420` | 105 | UnwindData |  |
| 114 | `PsmRegisterAppStateChangeNotification` | `0x3B700` | 49 | UnwindData |  |
| 132 | `PsmTimerCleanup` | `0x52050` | 109 | UnwindData |  |
| 136 | `PsmTimerStart` | `0x520D0` | 302 | UnwindData |  |
| 2 | *Ordinal Only* | `0x52A00` | 334 | UnwindData |  |
| 81 | `DllGetClassObject` | `0x5D110` | 664 | UnwindData |  |
| 58 | `BiPtQuerySystemStateBroadcastChannels` | `0x5F730` | 142 | UnwindData |  |
| 52 | `BiPtEnumerateWorkItemsForPackageName` | `0x5F7D0` | 199 | UnwindData |  |
| 48 | `BiPtDisassociateWorkItemEx` | `0x5F8A0` | 179 | UnwindData |  |
| 35 | `BiPtActivateInBackgroundEx` | `0x5F960` | 466 | UnwindData |  |
| 63 | `BiPtSignalEventEx` | `0x5FB40` | 223 | UnwindData |  |
| 44 | `BiPtCreateEventForPackageName` | `0x5FC30` | 275 | UnwindData |  |
| 50 | `BiPtEnumerateBrokeredEvents` | `0x5FD50` | 201 | UnwindData |  |
| 45 | `BiPtDeleteEvent` | `0x5FE20` | 142 | UnwindData |  |
| 43 | `BiPtCreateEventForApp` | `0x5FEC0` | 264 | UnwindData |  |
| 37 | `BiPtAssociateActivationProxy` | `0x5FFD0` | 292 | UnwindData |  |
| 59 | `BiPtQueryWorkItem` | `0x60100` | 183 | UnwindData |  |
| 61 | `BiPtQueryWorkItemStatusStateName` | `0x601C0` | 161 | UnwindData |  |
| 57 | `BiPtQueryBrokeredEvent` | `0x60270` | 178 | UnwindData |  |
| 3 | *Ordinal Only* | `0x69040` | 1,037 | UnwindData |  |
| 79 | `DllCanUnloadNow` | `0x69B80` | 113 | UnwindData |  |
| 143 | `UnregisterAppStateChangeNotification` | `0x6A3A0` | 52 | UnwindData |  |
| 138 | `PsmUnregisterAppStateChangeNotification` | `0x6A3E0` | 704 | UnwindData |  |
| 4 | *Ordinal Only* | `0x70B90` | 101 | UnwindData |  |
| 12 | *Ordinal Only* | `0x741B0` | 80 | UnwindData |  |
| 80 | `DllGetActivationFactory` | `0x75610` | 4,496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `BiChangeUserState` | `0x767A0` | 187 | UnwindData |  |
| 30 | `BiNotifyNewSessionComplete` | `0x76870` | 180 | UnwindData |  |
| 18 | `BiChangeApplicationStateForPackageNameForUser` | `0x76A80` | 321 | UnwindData |  |
| 1 | *Ordinal Only* | `0x7FFC0` | 343 | UnwindData |  |
| 134 | `PsmTimerInitialize` | `0x87000` | 7,728 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `BiNotifyNewSession` | `0x88E30` | 294 | UnwindData |  |
| 118 | `PsmRegisterKeyNotification` | `0x89E50` | 198 | UnwindData |  |
| 32 | `BiPlmFreeMemory` | `0x8A130` | 15,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `BiPtFreeMemory` | `0x8A130` | 15,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `BiNotifyNewUser` | `0x8DE00` | 265 | UnwindData |  |
| 77 | `BiUpdateBackgroundAccessApplicationsForUser` | `0x92BD0` | 5,888 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `BiUpdateLockScreenApplications` | `0x92BD0` | 5,888 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `PsmInitializeExtension` | `0x92BD0` | 5,888 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `RegisterAppConstrainedChangeNotification` | `0x92BD0` | 5,888 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `BiChangeApplicationStateForPackageName` | `0x942D0` | 12,576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `BiChangeSessionState` | `0x973F0` | 6,496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `PsmRegisterManagerType` | `0x98D50` | 49,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `UnregisterAppConstrainedChangeNotification` | `0x98D50` | 49,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `PsmShutdownApplication` | `0xA5070` | 126 | UnwindData |  |
| 501 | *Ordinal Only* | `0xB4470` | 169 | UnwindData |  |
| 70 | `BiSessionSinkCleanup` | `0xBC580` | 62,944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `BiSessionSinkCreate` | `0xBC580` | 62,944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `PsmIsProcessInApplication` | `0xCBB60` | 106,416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 502 | *Ordinal Only* | `0xE5B10` | 76 | UnwindData |  |
| 503 | *Ordinal Only* | `0xE5B70` | 122 | UnwindData |  |
| 500 | *Ordinal Only* | `0x1369F0` | 1,190 | UnwindData |  |
| 15 | `ValidateSystemShutdown` | `0x13A7A0` | 426 | UnwindData |  |
| 5 | *Ordinal Only* | `0x151530` | 80 | UnwindData |  |
| 11 | *Ordinal Only* | `0x151930` | 138 | UnwindData |  |
| 13 | *Ordinal Only* | `0x1519C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | *Ordinal Only* | `0x1519D0` | 271 | UnwindData |  |
| 16 | `BiActivateWorkItemForUser` | `0x15E1E0` | 185 | UnwindData |  |
| 19 | `BiChangeApplicationStateForPsmKey` | `0x15E2A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `BiChangeApplicationStateForPsmKeyForUser` | `0x15E2A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `BiEnumerateWorkItemsForPackageNameAndUser` | `0x15E2B0` | 277 | UnwindData |  |
| 24 | `BiGetActiveBackgroundTasksEvent` | `0x15E3D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `BiGetActiveBackgroundTasksEventForUser` | `0x15E3F0` | 385 | UnwindData |  |
| 26 | `BiGetCancellationTimeoutInMs` | `0x15E580` | 131 | UnwindData |  |
| 27 | `BiIsApplicationTerminateSensitive` | `0x15E610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `BiIsApplicationTerminateSensitiveForUser` | `0x15E630` | 317 | UnwindData |  |
| 67 | `BiQueryWorkItemForUser` | `0x15E780` | 230 | UnwindData |  |
| 68 | `BiResetActiveSessionForPackage` | `0x15E870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `BiResetActiveUserForPackage` | `0x15E880` | 142 | UnwindData |  |
| 72 | `BiSetActiveSessionForPackage` | `0x15E920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `BiSetActiveUserForPackage` | `0x15E930` | 157 | UnwindData |  |
| 74 | `BiTerminateApplicationHost` | `0x15E9E0` | 37 | UnwindData |  |
| 75 | `BiTerminateApplicationHost2` | `0x15EA10` | 41 | UnwindData |  |
| 76 | `BiTerminateApplicationHostForUser` | `0x15EA40` | 349 | UnwindData |  |
| 33 | `BiPtActivateDeferredWorkItem` | `0x15EBB0` | 140 | UnwindData |  |
| 34 | `BiPtActivateInBackground` | `0x15EC50` | 101 | UnwindData |  |
| 36 | `BiPtActivateWorkItem` | `0x15ECC0` | 142 | UnwindData |  |
| 38 | `BiPtAssociateApplicationEntryPoint` | `0x15ED60` | 348 | UnwindData |  |
| 39 | `BiPtAssociateApplicationExtensionClass` | `0x15EED0` | 61 | UnwindData |  |
| 40 | `BiPtCancelWorkItem` | `0x15EF20` | 110 | UnwindData |  |
| 41 | `BiPtCancelWorkItemEx` | `0x15EFA0` | 121 | UnwindData |  |
| 42 | `BiPtCreateEvent` | `0x15F020` | 282 | UnwindData |  |
| 46 | `BiPtDisableWorkItem` | `0x15F140` | 158 | UnwindData |  |
| 47 | `BiPtDisassociateWorkItem` | `0x15F1F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `BiPtEnableWorkItem` | `0x15F200` | 142 | UnwindData |  |
| 51 | `BiPtEnumerateBrokeredEventsEx` | `0x15F2A0` | 204 | UnwindData |  |
| 53 | `BiPtEnumerateWorkItemsForPackageNameEx` | `0x15F380` | 204 | UnwindData |  |
| 55 | `BiPtGetStatusStateNameFromBrokerEventId` | `0x15F460` | 159 | UnwindData |  |
| 56 | `BiPtQueryBrokerEventId` | `0x15F510` | 159 | UnwindData |  |
| 60 | `BiPtQueryWorkItemEx` | `0x15F5C0` | 156 | UnwindData |  |
| 62 | `BiPtSignalEvent` | `0x15F670` | 29 | UnwindData |  |
| 64 | `BiPtSignalMultipleEvents` | `0x15F6A0` | 223 | UnwindData |  |
| 65 | `BiPtSignalTriggerEvent` | `0x15F790` | 29 | UnwindData |  |
| 66 | `BiPtSignalTriggerEventEx` | `0x15F7C0` | 223 | UnwindData |  |
| 82 | `PsmApplyTaskCompletion` | `0x1600F0` | 200 | UnwindData |  |
| 85 | `PsmGetSessionInfo` | `0x1601C0` | 182 | UnwindData |  |
| 117 | `PsmRegisterDynamicProcess` | `0x160280` | 180 | UnwindData |  |
| 84 | `PsmDisconnect` | `0x160340` | 42 | UnwindData |  |
| 88 | `PsmIsProcessInApplication2` | `0x160370` | 154 | UnwindData |  |
| 89 | `PsmQueryApplicationInformation` | `0x160410` | 141 | UnwindData |  |
| 90 | `PsmQueryApplicationInformation2` | `0x1604B0` | 353 | UnwindData |  |
| 91 | `PsmQueryApplicationInterferenceCount` | `0x160620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `PsmQueryApplicationInterferenceCount2` | `0x160620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `PsmQueryApplicationProperties` | `0x160620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `PsmQueryApplicationProperties2` | `0x160620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `PsmQueryApplicationProperties3` | `0x160620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `PsmQueryApplicationPropertiesByUser` | `0x160620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `PsmQueryApplicationResourceUsage` | `0x160620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `PsmQueryApplicationResourceUsage2` | `0x160620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `PsmQueryMaxMemoryUsage` | `0x160620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `PsmQueryMaxMemoryUsage2` | `0x160620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `PsmQueryMemoryUsage` | `0x160620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `PsmQueryMemoryUsage2` | `0x160620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `PsmQuerySharedCommitByUser` | `0x160620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `PsmQueryTaskCompletionInformation` | `0x160620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `PsmQueryTaskCompletionInformation2` | `0x160620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `PsmResetMaxMemoryUsage` | `0x160620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `PsmResetMaxMemoryUsage2` | `0x160620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `PsmResetMaxMemoryUsageByUser` | `0x160620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `PsmSetApplicationPriority` | `0x160620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `PsmSetApplicationPriority2` | `0x160620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `PsmSetApplicationProperties` | `0x160620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `PsmSetApplicationProperties2` | `0x160620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `PsmSetApplicationProperties3` | `0x160620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `PsmSetApplicationPropertiesByUser` | `0x160620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `PsmQueryApplicationList` | `0x160630` | 131 | UnwindData |  |
| 94 | `PsmQueryApplicationList2` | `0x1606C0` | 334 | UnwindData |  |
| 107 | `PsmQueryMemoryUsageByUser` | `0x160820` | 244 | UnwindData |  |
| 108 | `PsmQueryProcessList` | `0x160920` | 141 | UnwindData |  |
| 109 | `PsmQueryProcessList2` | `0x1609C0` | 390 | UnwindData |  |
| 115 | `PsmRegisterApplicationNotification` | `0x160B50` | 151 | UnwindData |  |
| 116 | `PsmRegisterApplicationNotification2` | `0x160BF0` | 128 | UnwindData |  |
| 129 | `PsmSetApplicationState` | `0x160C80` | 147 | UnwindData |  |
| 130 | `PsmSetApplicationState2` | `0x160D20` | 394 | UnwindData |  |
| 101 | `PsmQueryApplicationResourceUsageForTimer` | `0x160EB0` | 281 | UnwindData |  |
| 113 | `PsmRegisterAppPriorityNotification` | `0x160FD0` | 256 | UnwindData |  |
| 133 | `PsmTimerElapsedResourceTimeGet` | `0x162690` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `PsmTimerRemainingResourceTimeGet` | `0x1627C0` | 1,152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `RegisterAppStateChangeNotification` | `0x162C40` | 209 | UnwindData |  |
