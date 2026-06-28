# Binary Specification: hotplug.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\hotplug.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3ed4a2b8ff3ea7efb9a15814b63a44c94f745361144ee0545d76869986211d7a`
* **Total Exported Functions:** 13

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 13 | `DllGetClassObject` | `0x2790` | 179 | UnwindData |  |
| 1 | `CPlApplet` | `0x4CB0` | 183 | UnwindData |  |
| 2 | `HotPlugChildWithInvalidIdW` | `0x4EC0` | 661 | UnwindData |  |
| 3 | `HotPlugDriverBlockedW` | `0x5160` | 676 | UnwindData |  |
| 6 | `HotPlugEjectVetoedW` | `0x5410` | 39 | UnwindData |  |
| 7 | `HotPlugHibernateVetoedW` | `0x5440` | 39 | UnwindData |  |
| 8 | `HotPlugRemovalVetoedW` | `0x5470` | 39 | UnwindData |  |
| 9 | `HotPlugSafeRemovalDriveNotificationW` | `0x54A0` | 277 | UnwindData |  |
| 10 | `HotPlugSafeRemovalNotificationW` | `0x5800` | 172 | UnwindData |  |
| 11 | `HotPlugStandbyVetoedW` | `0x58C0` | 39 | UnwindData |  |
| 12 | `HotPlugWarmEjectVetoedW` | `0x58F0` | 39 | UnwindData |  |
| 4 | `HotPlugEjectDevice` | `0x77A0` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `HotPlugEjectDeviceEx` | `0x7B80` | 384 | UnwindData |  |
