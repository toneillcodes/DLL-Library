# Binary Specification: ActiveSyncProvider.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ActiveSyncProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0814ddd7aeae0db57c4ca1933fa511f3eef6e07fcb3d2375e929a701799c73ba`
* **Total Exported Functions:** 37

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 44 | *Ordinal Only* | `0x9780` | 785 | UnwindData |  |
| 22 | `SyncGetMAPISession` | `0x11AC0` | 140 | UnwindData |  |
| 19 | *Ordinal Only* | `0x159D0` | 38 | UnwindData |  |
| 11 | `GetOutlookExtensionSupportForAccount` | `0x1AC30` | 235 | UnwindData |  |
| 2 | `IsEnabledForSync` | `0x22320` | 611 | UnwindData |  |
| 23 | `SyncGetMessageStore` | `0x25960` | 279 | UnwindData |  |
| 24 | `SyncGetSpecialFolder` | `0x32200` | 321 | UnwindData |  |
| 5 | `DllCanUnloadNow` | `0x35CB0` | 42 | UnwindData |  |
| 18 | *Ordinal Only* | `0x366C0` | 48 | UnwindData |  |
| 17 | `IsValidOutlookExtensionVersion` | `0x36D30` | 9,376 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `CreateSyncServiceLayer` | `0x391D0` | 399 | UnwindData |  |
| 3 | `CreateMassObject` | `0x3C7C0` | 1,086 | UnwindData |  |
| 62 | `InitializeSyncStatus` | `0x49360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `SyncSqmUpdateStats` | `0x49370` | 15,888 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllGetClassObject` | `0x4D180` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `OneStopFactory` | `0x4D1D0` | 57 | UnwindData |  |
| 45 | *Ordinal Only* | `0x7CED0` | 543 | UnwindData |  |
| 7 | `DownloadEmailAttachment` | `0x90080` | 1,080 | UnwindData |  |
| 8 | `DownloadEmailBody` | `0x904C0` | 743 | UnwindData |  |
| 12 | `GetOutlookExtensionSupportFromAccessor` | `0x95B70` | 512 | UnwindData |  |
| 36 | *Ordinal Only* | `0x9C890` | 64 | UnwindData |  |
| 1 | *Ordinal Only* | `0x9C9B0` | 163 | UnwindData |  |
| 25 | `SyncMgrPurgeFolderProvider` | `0x9CA60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `SyncMgrPurgeProviderStore` | `0x9CA70` | 131 | UnwindData |  |
| 27 | `SyncMgrRemovePolicy` | `0x9CB00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | *Ordinal Only* | `0x9CB10` | 24 | UnwindData |  |
| 29 | `WriteStoreCapabilityProps` | `0x9DAA0` | 1,742 | UnwindData |  |
| 30 | `WriteStoreContentTypesProps` | `0x9E180` | 1,330 | UnwindData |  |
| 9 | `GetActiveSyncServerProbeInstance` | `0xC28E0` | 64 | UnwindData |  |
| 10 | `GetConversationSyncEnabled` | `0xC2990` | 193 | UnwindData |  |
| 14 | `HandleEasMeetingResponseForAppointment` | `0xC3390` | 686 | UnwindData |  |
| 15 | `HandleEasMeetingResponseForMeetingNotification` | `0xC3650` | 832 | UnwindData |  |
| 16 | `IsErrorCatastrophic` | `0xC4880` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | *Ordinal Only* | `0xC48C0` | 225 | UnwindData |  |
| 20 | `MarkPeopleFolderForResync` | `0xC4AC0` | 46 | UnwindData |  |
| 28 | `UpdateEasTrackingSchema` | `0xC4B00` | 383 | UnwindData |  |
| 13 | `GetUserInfoForUnconfiguredAccount` | `0xE3030` | 585 | UnwindData |  |
