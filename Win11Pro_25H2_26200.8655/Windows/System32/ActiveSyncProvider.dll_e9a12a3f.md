# Binary Specification: ActiveSyncProvider.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ActiveSyncProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e9a12a3ff05f155771bafada9dffa8e09d88741a0593b10119337da65c54d5ce`
* **Total Exported Functions:** 37

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 44 | *Ordinal Only* | `0x9780` | 785 | UnwindData |  |
| 22 | `SyncGetMAPISession` | `0x11AC0` | 140 | UnwindData |  |
| 19 | *Ordinal Only* | `0x159D0` | 38 | UnwindData |  |
| 11 | `GetOutlookExtensionSupportForAccount` | `0x1AC30` | 235 | UnwindData |  |
| 2 | `IsEnabledForSync` | `0x220B0` | 611 | UnwindData |  |
| 23 | `SyncGetMessageStore` | `0x256F0` | 279 | UnwindData |  |
| 24 | `SyncGetSpecialFolder` | `0x32350` | 321 | UnwindData |  |
| 5 | `DllCanUnloadNow` | `0x35CA0` | 42 | UnwindData |  |
| 18 | *Ordinal Only* | `0x366B0` | 48 | UnwindData |  |
| 17 | `IsValidOutlookExtensionVersion` | `0x36D20` | 9,376 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `CreateSyncServiceLayer` | `0x391C0` | 399 | UnwindData |  |
| 3 | `CreateMassObject` | `0x3C7B0` | 1,086 | UnwindData |  |
| 62 | `InitializeSyncStatus` | `0x49360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `SyncSqmUpdateStats` | `0x49370` | 15,904 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllGetClassObject` | `0x4D190` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `OneStopFactory` | `0x4D1E0` | 57 | UnwindData |  |
| 45 | *Ordinal Only* | `0x7CEE0` | 543 | UnwindData |  |
| 7 | `DownloadEmailAttachment` | `0x90090` | 1,080 | UnwindData |  |
| 8 | `DownloadEmailBody` | `0x904D0` | 743 | UnwindData |  |
| 12 | `GetOutlookExtensionSupportFromAccessor` | `0x95B80` | 512 | UnwindData |  |
| 36 | *Ordinal Only* | `0x9C8A0` | 64 | UnwindData |  |
| 1 | *Ordinal Only* | `0x9C9C0` | 163 | UnwindData |  |
| 25 | `SyncMgrPurgeFolderProvider` | `0x9CA70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `SyncMgrPurgeProviderStore` | `0x9CA80` | 131 | UnwindData |  |
| 27 | `SyncMgrRemovePolicy` | `0x9CB10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | *Ordinal Only* | `0x9CB20` | 24 | UnwindData |  |
| 29 | `WriteStoreCapabilityProps` | `0x9DAB0` | 1,742 | UnwindData |  |
| 30 | `WriteStoreContentTypesProps` | `0x9E190` | 1,330 | UnwindData |  |
| 9 | `GetActiveSyncServerProbeInstance` | `0xC28F0` | 64 | UnwindData |  |
| 10 | `GetConversationSyncEnabled` | `0xC29A0` | 193 | UnwindData |  |
| 14 | `HandleEasMeetingResponseForAppointment` | `0xC33A0` | 686 | UnwindData |  |
| 15 | `HandleEasMeetingResponseForMeetingNotification` | `0xC3660` | 832 | UnwindData |  |
| 16 | `IsErrorCatastrophic` | `0xC4890` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | *Ordinal Only* | `0xC48D0` | 225 | UnwindData |  |
| 20 | `MarkPeopleFolderForResync` | `0xC4AD0` | 46 | UnwindData |  |
| 28 | `UpdateEasTrackingSchema` | `0xC4B10` | 383 | UnwindData |  |
| 13 | `GetUserInfoForUnconfiguredAccount` | `0xE3040` | 585 | UnwindData |  |
