# Binary Specification: ssdpapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ssdpapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c177e2e751f3e1c65ea185f8d8f94b559ee1621f06b0c284c8ba7590f58f931e`
* **Total Exported Functions:** 29

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 12 | `FindServicesCallbackEx` | `0x1250` | 92 | UnwindData |  |
| 16 | `FindServicesOnNetworkCallbackEx` | `0x1580` | 86 | UnwindData |  |
| 10 | `FindServices` | `0x1DC0` | 199 | UnwindData |  |
| 14 | `FindServicesClose` | `0x3D30` | 44 | UnwindData |  |
| 9 | `EndRegisterPropChangeNotificationEx` | `0x53A0` | 572 | UnwindData |  |
| 5 | `DeregisterNotification` | `0x5A30` | 782 | UnwindData |  |
| 1 | `BeginRegisterPropChangeNotificationEx` | `0x5F80` | 1,336 | UnwindData |  |
| 24 | `RegisterNotification` | `0x6880` | 162 | UnwindData |  |
| 25 | `RegisterNotificationEx` | `0x6930` | 171 | UnwindData |  |
| 23 | `RegisterAliveNotificationOnNetworkEx` | `0x69F0` | 160 | UnwindData |  |
| 19 | `GetFirstService` | `0x6F90` | 164 | UnwindData |  |
| 22 | `GetNextServiceEx` | `0x7040` | 186 | UnwindData |  |
| 20 | `GetFirstServiceEx` | `0x72B0` | 49 | UnwindData |  |
| 28 | `SsdpCleanup` | `0x7570` | 272 | UnwindData |  |
| 27 | `RegisterServiceEx` | `0x7970` | 683 | UnwindData |  |
| 13 | `FindServicesCancel` | `0x7CB0` | 44 | UnwindData |  |
| 6 | `DeregisterService` | `0x8310` | 223 | UnwindData |  |
| 21 | `GetNextService` | `0x8E90` | 164 | UnwindData |  |
| 29 | `SsdpStartup` | `0x94E0` | 111 | UnwindData |  |
| 18 | `FreeSsdpMessageEx` | `0x9C60` | 40 | UnwindData |  |
| 2 | `CleanupCache` | `0xAF70` | 190 | UnwindData |  |
| 17 | `FreeSsdpMessage` | `0xB040` | 130 | UnwindData |  |
| 26 | `RegisterService` | `0xB380` | 148 | UnwindData |  |
| 11 | `FindServicesCallback` | `0xB470` | 68 | UnwindData |  |
| 15 | `FindServicesEx` | `0xB4C0` | 25,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DHSetICSInterfaces` | `0x11780` | 44 | UnwindData |  |
| 4 | `DHSetICSOff` | `0x117C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `DisableFirewallRule` | `0x117F0` | 291 | UnwindData |  |
| 8 | `EnableFirewallRule` | `0x11920` | 350 | UnwindData |  |
