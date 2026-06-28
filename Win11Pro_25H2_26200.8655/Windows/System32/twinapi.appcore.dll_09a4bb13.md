# Binary Specification: twinapi.appcore.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\twinapi.appcore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `09a4bb13fa4aa35cad12808a4696e9e8659bc44e924f3882f95bc85896e3ed3f`
* **Total Exported Functions:** 148

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | *Ordinal Only* | `0x10C80` | 2,415 | UnwindData |  |
| 9 | *Ordinal Only* | `0x12280` | 558 | UnwindData |  |
| 8 | *Ordinal Only* | `0x12ED0` | 1,263 | UnwindData |  |
| 6 | *Ordinal Only* | `0x13400` | 1,726 | UnwindData |  |
| 83 | `PsmBlockAppStateChangeCompletion` | `0x186D0` | 352 | UnwindData |  |
| 137 | `PsmUnblockAppStateChangeCompletion` | `0x1A240` | 402 | UnwindData |  |
| 139 | `PsmWaitForAppResume` | `0x1A700` | 102 | UnwindData |  |
| 504 | *Ordinal Only* | `0x1CF10` | 99 | UnwindData |  |
| 10 | *Ordinal Only* | `0x25320` | 504 | UnwindData |  |
| 102 | `PsmQueryCurrentAppState` | `0x34860` | 105 | UnwindData |  |
| 114 | `PsmRegisterAppStateChangeNotification` | `0x36B40` | 49 | UnwindData |  |
| 132 | `PsmTimerCleanup` | `0x4D260` | 109 | UnwindData |  |
| 136 | `PsmTimerStart` | `0x4D2E0` | 302 | UnwindData |  |
| 2 | *Ordinal Only* | `0x57D70` | 334 | UnwindData |  |
| 81 | `DllGetClassObject` | `0x5C2E0` | 664 | UnwindData |  |
| 58 | `BiPtQuerySystemStateBroadcastChannels` | `0x5E9C0` | 142 | UnwindData |  |
| 52 | `BiPtEnumerateWorkItemsForPackageName` | `0x5EA60` | 199 | UnwindData |  |
| 48 | `BiPtDisassociateWorkItemEx` | `0x5EB30` | 179 | UnwindData |  |
| 35 | `BiPtActivateInBackgroundEx` | `0x5EBF0` | 466 | UnwindData |  |
| 63 | `BiPtSignalEventEx` | `0x5EDD0` | 223 | UnwindData |  |
| 44 | `BiPtCreateEventForPackageName` | `0x5EEC0` | 275 | UnwindData |  |
| 50 | `BiPtEnumerateBrokeredEvents` | `0x5EFE0` | 201 | UnwindData |  |
| 45 | `BiPtDeleteEvent` | `0x5F0B0` | 142 | UnwindData |  |
| 43 | `BiPtCreateEventForApp` | `0x5F150` | 264 | UnwindData |  |
| 37 | `BiPtAssociateActivationProxy` | `0x5F260` | 292 | UnwindData |  |
| 59 | `BiPtQueryWorkItem` | `0x5F390` | 183 | UnwindData |  |
| 61 | `BiPtQueryWorkItemStatusStateName` | `0x5F450` | 161 | UnwindData |  |
| 57 | `BiPtQueryBrokeredEvent` | `0x5F500` | 178 | UnwindData |  |
| 3 | *Ordinal Only* | `0x68430` | 1,037 | UnwindData |  |
| 79 | `DllCanUnloadNow` | `0x68F70` | 113 | UnwindData |  |
| 143 | `UnregisterAppStateChangeNotification` | `0x698F0` | 52 | UnwindData |  |
| 138 | `PsmUnregisterAppStateChangeNotification` | `0x69930` | 704 | UnwindData |  |
| 4 | *Ordinal Only* | `0x700E0` | 101 | UnwindData |  |
| 12 | *Ordinal Only* | `0x73640` | 80 | UnwindData |  |
| 80 | `DllGetActivationFactory` | `0x74AA0` | 4,720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `BiChangeUserState` | `0x75D10` | 187 | UnwindData |  |
| 30 | `BiNotifyNewSessionComplete` | `0x75DE0` | 180 | UnwindData |  |
| 18 | `BiChangeApplicationStateForPackageNameForUser` | `0x75FF0` | 321 | UnwindData |  |
| 1 | *Ordinal Only* | `0x7F480` | 343 | UnwindData |  |
| 134 | `PsmTimerInitialize` | `0x86780` | 8,592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `BiNotifyNewSession` | `0x88910` | 294 | UnwindData |  |
| 118 | `PsmRegisterKeyNotification` | `0x89940` | 198 | UnwindData |  |
| 32 | `BiPlmFreeMemory` | `0x89C20` | 15,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `BiPtFreeMemory` | `0x89C20` | 15,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `BiNotifyNewUser` | `0x8D9F0` | 265 | UnwindData |  |
| 77 | `BiUpdateBackgroundAccessApplicationsForUser` | `0x92740` | 5,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `BiUpdateLockScreenApplications` | `0x92740` | 5,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `PsmInitializeExtension` | `0x92740` | 5,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `RegisterAppConstrainedChangeNotification` | `0x92740` | 5,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `BiChangeApplicationStateForPackageName` | `0x93DE0` | 12,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `BiChangeSessionState` | `0x96EC0` | 6,704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `PsmRegisterManagerType` | `0x988F0` | 50,352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `UnregisterAppConstrainedChangeNotification` | `0x988F0` | 50,352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `PsmShutdownApplication` | `0xA4DA0` | 126 | UnwindData |  |
| 501 | *Ordinal Only* | `0xB44B0` | 169 | UnwindData |  |
| 70 | `BiSessionSinkCleanup` | `0xBC5D0` | 65,472 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `BiSessionSinkCreate` | `0xBC5D0` | 65,472 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `PsmIsProcessInApplication` | `0xCC590` | 106,528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 502 | *Ordinal Only* | `0xE65B0` | 76 | UnwindData |  |
| 503 | *Ordinal Only* | `0xE6610` | 122 | UnwindData |  |
| 500 | *Ordinal Only* | `0x139160` | 1,190 | UnwindData |  |
| 15 | `ValidateSystemShutdown` | `0x13CF30` | 426 | UnwindData |  |
| 5 | *Ordinal Only* | `0x1563D0` | 80 | UnwindData |  |
| 11 | *Ordinal Only* | `0x1567D0` | 138 | UnwindData |  |
| 13 | *Ordinal Only* | `0x156860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | *Ordinal Only* | `0x156870` | 271 | UnwindData |  |
| 16 | `BiActivateWorkItemForUser` | `0x163320` | 185 | UnwindData |  |
| 19 | `BiChangeApplicationStateForPsmKey` | `0x1633E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `BiChangeApplicationStateForPsmKeyForUser` | `0x1633E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `BiEnumerateWorkItemsForPackageNameAndUser` | `0x1633F0` | 277 | UnwindData |  |
| 24 | `BiGetActiveBackgroundTasksEvent` | `0x163510` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `BiGetActiveBackgroundTasksEventForUser` | `0x163530` | 385 | UnwindData |  |
| 26 | `BiGetCancellationTimeoutInMs` | `0x1636C0` | 131 | UnwindData |  |
| 27 | `BiIsApplicationTerminateSensitive` | `0x163750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `BiIsApplicationTerminateSensitiveForUser` | `0x163770` | 317 | UnwindData |  |
| 67 | `BiQueryWorkItemForUser` | `0x1638C0` | 230 | UnwindData |  |
| 68 | `BiResetActiveSessionForPackage` | `0x1639B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `BiResetActiveUserForPackage` | `0x1639C0` | 142 | UnwindData |  |
| 72 | `BiSetActiveSessionForPackage` | `0x163A60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `BiSetActiveUserForPackage` | `0x163A70` | 157 | UnwindData |  |
| 74 | `BiTerminateApplicationHost` | `0x163B20` | 37 | UnwindData |  |
| 75 | `BiTerminateApplicationHost2` | `0x163B50` | 41 | UnwindData |  |
| 76 | `BiTerminateApplicationHostForUser` | `0x163B80` | 349 | UnwindData |  |
| 33 | `BiPtActivateDeferredWorkItem` | `0x163CF0` | 140 | UnwindData |  |
| 34 | `BiPtActivateInBackground` | `0x163D90` | 101 | UnwindData |  |
| 36 | `BiPtActivateWorkItem` | `0x163E00` | 142 | UnwindData |  |
| 38 | `BiPtAssociateApplicationEntryPoint` | `0x163EA0` | 348 | UnwindData |  |
| 39 | `BiPtAssociateApplicationExtensionClass` | `0x164010` | 61 | UnwindData |  |
| 40 | `BiPtCancelWorkItem` | `0x164060` | 110 | UnwindData |  |
| 41 | `BiPtCancelWorkItemEx` | `0x1640E0` | 121 | UnwindData |  |
| 42 | `BiPtCreateEvent` | `0x164160` | 282 | UnwindData |  |
| 46 | `BiPtDisableWorkItem` | `0x164280` | 158 | UnwindData |  |
| 47 | `BiPtDisassociateWorkItem` | `0x164330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `BiPtEnableWorkItem` | `0x164340` | 142 | UnwindData |  |
| 51 | `BiPtEnumerateBrokeredEventsEx` | `0x1643E0` | 204 | UnwindData |  |
| 53 | `BiPtEnumerateWorkItemsForPackageNameEx` | `0x1644C0` | 204 | UnwindData |  |
| 55 | `BiPtGetStatusStateNameFromBrokerEventId` | `0x1645A0` | 159 | UnwindData |  |
| 56 | `BiPtQueryBrokerEventId` | `0x164650` | 159 | UnwindData |  |
| 60 | `BiPtQueryWorkItemEx` | `0x164700` | 156 | UnwindData |  |
| 62 | `BiPtSignalEvent` | `0x1647B0` | 29 | UnwindData |  |
| 64 | `BiPtSignalMultipleEvents` | `0x1647E0` | 223 | UnwindData |  |
| 65 | `BiPtSignalTriggerEvent` | `0x1648D0` | 29 | UnwindData |  |
| 66 | `BiPtSignalTriggerEventEx` | `0x164900` | 223 | UnwindData |  |
| 82 | `PsmApplyTaskCompletion` | `0x165230` | 200 | UnwindData |  |
| 85 | `PsmGetSessionInfo` | `0x165300` | 182 | UnwindData |  |
| 117 | `PsmRegisterDynamicProcess` | `0x1653C0` | 180 | UnwindData |  |
| 84 | `PsmDisconnect` | `0x165480` | 42 | UnwindData |  |
| 88 | `PsmIsProcessInApplication2` | `0x1654B0` | 154 | UnwindData |  |
| 89 | `PsmQueryApplicationInformation` | `0x165550` | 141 | UnwindData |  |
| 90 | `PsmQueryApplicationInformation2` | `0x1655F0` | 353 | UnwindData |  |
| 91 | `PsmQueryApplicationInterferenceCount` | `0x165760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `PsmQueryApplicationInterferenceCount2` | `0x165760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `PsmQueryApplicationProperties` | `0x165760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `PsmQueryApplicationProperties2` | `0x165760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `PsmQueryApplicationProperties3` | `0x165760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `PsmQueryApplicationPropertiesByUser` | `0x165760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `PsmQueryApplicationResourceUsage` | `0x165760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `PsmQueryApplicationResourceUsage2` | `0x165760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `PsmQueryMaxMemoryUsage` | `0x165760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `PsmQueryMaxMemoryUsage2` | `0x165760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `PsmQueryMemoryUsage` | `0x165760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `PsmQueryMemoryUsage2` | `0x165760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `PsmQuerySharedCommitByUser` | `0x165760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `PsmQueryTaskCompletionInformation` | `0x165760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `PsmQueryTaskCompletionInformation2` | `0x165760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `PsmResetMaxMemoryUsage` | `0x165760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `PsmResetMaxMemoryUsage2` | `0x165760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `PsmResetMaxMemoryUsageByUser` | `0x165760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `PsmSetApplicationPriority` | `0x165760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `PsmSetApplicationPriority2` | `0x165760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `PsmSetApplicationProperties` | `0x165760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `PsmSetApplicationProperties2` | `0x165760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `PsmSetApplicationProperties3` | `0x165760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `PsmSetApplicationPropertiesByUser` | `0x165760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `PsmQueryApplicationList` | `0x165770` | 131 | UnwindData |  |
| 94 | `PsmQueryApplicationList2` | `0x165800` | 334 | UnwindData |  |
| 107 | `PsmQueryMemoryUsageByUser` | `0x165960` | 244 | UnwindData |  |
| 108 | `PsmQueryProcessList` | `0x165A60` | 141 | UnwindData |  |
| 109 | `PsmQueryProcessList2` | `0x165B00` | 390 | UnwindData |  |
| 115 | `PsmRegisterApplicationNotification` | `0x165C90` | 151 | UnwindData |  |
| 116 | `PsmRegisterApplicationNotification2` | `0x165D30` | 128 | UnwindData |  |
| 129 | `PsmSetApplicationState` | `0x165DC0` | 147 | UnwindData |  |
| 130 | `PsmSetApplicationState2` | `0x165E60` | 394 | UnwindData |  |
| 101 | `PsmQueryApplicationResourceUsageForTimer` | `0x165FF0` | 281 | UnwindData |  |
| 113 | `PsmRegisterAppPriorityNotification` | `0x166110` | 256 | UnwindData |  |
| 133 | `PsmTimerElapsedResourceTimeGet` | `0x1677D0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `PsmTimerRemainingResourceTimeGet` | `0x167900` | 1,152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `RegisterAppStateChangeNotification` | `0x167D80` | 209 | UnwindData |  |
