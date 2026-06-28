# Binary Specification: SystemEventsBrokerClient.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\SystemEventsBrokerClient.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e43b7a414c523d283460130a485f65410c264c603b994bbdf5b193251ae41d4f`
* **Total Exported Functions:** 54

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 36 | `SebEnumerateEvents` | `0x1010` | 190 | UnwindData |  |
| 52 | `SebSignalOEMPreInstallEvent` | `0x10E0` | 215 | UnwindData |  |
| 38 | `SebEnumerateEventsByTypeEx` | `0x11C0` | 48 | UnwindData |  |
| 48 | `SebSignalDeviceEvent` | `0x12A0` | 255 | UnwindData |  |
| 49 | `SebSignalEvent` | `0x12A0` | 255 | UnwindData |  |
| 40 | `SebQueryEventData` | `0x13B0` | 178 | UnwindData |  |
| 45 | `SebSignalApplicationTriggerEvent` | `0x1470` | 55 | UnwindData |  |
| 47 | `SebSignalBackgroundTransferCompletionEvent` | `0x1470` | 55 | UnwindData |  |
| 51 | `SebSignalMediaProcessingTriggerEvent` | `0x1470` | 55 | UnwindData |  |
| 37 | `SebEnumerateEventsByType` | `0x1590` | 56 | UnwindData |  |
| 53 | `SebSignalSyncEvent` | `0x1850` | 81 | UnwindData |  |
| 41 | `SebQueryEventPackage` | `0x1B30` | 612 | UnwindData |  |
| 54 | `SebSignalSyncEventEx` | `0x1DA0` | 93 | UnwindData |  |
| 43 | `SebRegisterWellKnownEvent` | `0x2080` | 211 | UnwindData |  |
| 6 | `SebCreateBackgroundTransferCompletionEvent` | `0x2160` | 82 | UnwindData |  |
| 18 | `SebCreateDisplayOnEvent` | `0x21C0` | 85 | UnwindData |  |
| 35 | `SebDeleteEvent` | `0x2480` | 111 | UnwindData |  |
| 1 | `SebCancelEvent` | `0x3EF0` | 148 | UnwindData |  |
| 2 | `SebCreateApplicationTriggerEvent` | `0x3F90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `SebCreateAuthenticatorDeviceAuthEvent` | `0x3FB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `SebCreateBackgroundDownloadEvent` | `0x3FD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `SebCreateBackgroundDownloadEventEx` | `0x3FF0` | 124 | UnwindData |  |
| 7 | `SebCreateBroadcastNotificationEvent` | `0x4080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `SebCreateCachedFileUpdatedEvent` | `0x40A0` | 82 | UnwindData |  |
| 9 | `SebCreateCalendarNotificationEvent` | `0x4100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `SebCreateCallBlockedNotificationEvent` | `0x4120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `SebCreateCallOriginDataRequestedEvent` | `0x4140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `SebCreateChatNotificationEvent` | `0x4160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `SebCreateCommunicationBlockingAppSetAsActiveEvent` | `0x4180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `SebCreateContactNotificationEvent` | `0x41A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `SebCreateContentPrefetchEvent` | `0x41C0` | 70 | UnwindData |  |
| 16 | `SebCreateDeviceServicingEvent` | `0x4210` | 83 | UnwindData |  |
| 17 | `SebCreateDeviceUseEvent` | `0x4270` | 83 | UnwindData |  |
| 19 | `SebCreateEmailNotificationEvent` | `0x42D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `SebCreateInfrastructureConditionEvent` | `0x42F0` | 83 | UnwindData |  |
| 21 | `SebCreateKnownFoldersChangedEvent` | `0x4350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `SebCreateLockScreenAppAddedEvent` | `0x4370` | 79 | UnwindData |  |
| 23 | `SebCreateLockScreenAppRemovedEvent` | `0x43D0` | 79 | UnwindData |  |
| 24 | `SebCreateMediaProcessingTriggerEvent` | `0x4430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `SebCreateMessageInterceptNotificationEvent` | `0x4450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `SebCreateMobileBroadbandEvent` | `0x4470` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `SebCreateNetOperatorHotSpotAuthEvent` | `0x44A0` | 83 | UnwindData |  |
| 28 | `SebCreateOEMPreInstallEvent` | `0x4500` | 83 | UnwindData |  |
| 29 | `SebCreatePowerStateChangeEvent` | `0x4560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `SebCreateRcsEndUserMessageNotificationEvent` | `0x4580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `SebCreateSessionConnectedEvent` | `0x45A0` | 119 | UnwindData |  |
| 32 | `SebCreateTelephonyEvent` | `0x4620` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `SebCreateUnconstrainedBackgroundDownloadEvent` | `0x4670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `SebCreateUserPresentEvent` | `0x4680` | 119 | UnwindData |  |
| 39 | `SebGetStatusStateName` | `0x4700` | 104 | UnwindData |  |
| 42 | `SebRegisterPrivateEvent` | `0x4770` | 109 | UnwindData |  |
| 44 | `SebRegisterWellKnownFilteredEvent` | `0x47F0` | 182 | UnwindData |  |
| 46 | `SebSignalBackgroundDownloadEvent` | `0x48B0` | 70 | UnwindData |  |
| 50 | `SebSignalLevelEvent` | `0x4900` | 69 | UnwindData |  |
