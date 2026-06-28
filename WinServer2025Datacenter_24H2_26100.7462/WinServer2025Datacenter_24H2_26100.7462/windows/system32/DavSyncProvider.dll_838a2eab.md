# Binary Specification: DavSyncProvider.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\DavSyncProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `838a2eab1e5c94556796cbb1ff9bbfd107d1214e06728e35f73b91233c045953`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x87D0` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x8800` | 4,784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `ForceCalDavCollectionsListRefreshDuringNextSync` | `0x9AB0` | 407 | UnwindData |  |
| 6 | `UpdateCalDavTrackingSchema` | `0x9C50` | 339 | UnwindData |  |
| 7 | `UpdateGMailContactSyncPartner` | `0xA2E0` | 747 | UnwindData |  |
| 4 | `HandleWebDavMeetingResponseForAppointment` | `0x43E30` | 537 | UnwindData |  |
| 5 | `HandleWebDavMeetingResponseForMeetingNotification` | `0x44050` | 622 | UnwindData |  |
