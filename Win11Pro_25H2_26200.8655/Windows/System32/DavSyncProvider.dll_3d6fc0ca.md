# Binary Specification: DavSyncProvider.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DavSyncProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3d6fc0cae0fd04dd33f474ddfba3c02160a30b78763da227d0af6f0473b0fa53`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x87E0` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x8810` | 4,784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `ForceCalDavCollectionsListRefreshDuringNextSync` | `0x9AC0` | 407 | UnwindData |  |
| 6 | `UpdateCalDavTrackingSchema` | `0x9C60` | 339 | UnwindData |  |
| 7 | `UpdateGMailContactSyncPartner` | `0xA2F0` | 747 | UnwindData |  |
| 4 | `HandleWebDavMeetingResponseForAppointment` | `0x43E40` | 537 | UnwindData |  |
| 5 | `HandleWebDavMeetingResponseForMeetingNotification` | `0x44060` | 622 | UnwindData |  |
