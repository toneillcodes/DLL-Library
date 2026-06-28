# Binary Specification: ssdpapi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ssdpapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d6c0745fffa083ee5519bcd00eaed888777730e4e3dd3c68c2922ee1c1d6f8d0`
* **Total Exported Functions:** 29

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 12 | `FindServicesCallbackEx` | `0x1060` | 92 | UnwindData |  |
| 14 | `FindServicesClose` | `0x12B0` | 44 | UnwindData |  |
| 16 | `FindServicesOnNetworkCallbackEx` | `0x1690` | 86 | UnwindData |  |
| 10 | `FindServices` | `0x2530` | 199 | UnwindData |  |
| 5 | `DeregisterNotification` | `0x2BB0` | 782 | UnwindData |  |
| 28 | `SsdpCleanup` | `0x52B0` | 272 | UnwindData |  |
| 1 | `BeginRegisterPropChangeNotificationEx` | `0x5800` | 1,336 | UnwindData |  |
| 9 | `EndRegisterPropChangeNotificationEx` | `0x6020` | 572 | UnwindData |  |
| 29 | `SsdpStartup` | `0x6820` | 227 | UnwindData |  |
| 24 | `RegisterNotification` | `0x70E0` | 162 | UnwindData |  |
| 25 | `RegisterNotificationEx` | `0x7190` | 171 | UnwindData |  |
| 23 | `RegisterAliveNotificationOnNetworkEx` | `0x7250` | 160 | UnwindData |  |
| 19 | `GetFirstService` | `0x77F0` | 164 | UnwindData |  |
| 22 | `GetNextServiceEx` | `0x78A0` | 186 | UnwindData |  |
| 20 | `GetFirstServiceEx` | `0x7B10` | 49 | UnwindData |  |
| 27 | `RegisterServiceEx` | `0x7DD0` | 683 | UnwindData |  |
| 13 | `FindServicesCancel` | `0x8110` | 44 | UnwindData |  |
| 6 | `DeregisterService` | `0x82C0` | 223 | UnwindData |  |
| 21 | `GetNextService` | `0x8D80` | 164 | UnwindData |  |
| 18 | `FreeSsdpMessageEx` | `0x9930` | 40 | UnwindData |  |
| 2 | `CleanupCache` | `0xABB0` | 190 | UnwindData |  |
| 17 | `FreeSsdpMessage` | `0xAC80` | 130 | UnwindData |  |
| 26 | `RegisterService` | `0xAF70` | 148 | UnwindData |  |
| 11 | `FindServicesCallback` | `0xB060` | 68 | UnwindData |  |
| 15 | `FindServicesEx` | `0xB0B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DHSetICSInterfaces` | `0xB0C0` | 44 | UnwindData |  |
| 4 | `DHSetICSOff` | `0xB100` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `DisableFirewallRule` | `0xB130` | 291 | UnwindData |  |
| 8 | `EnableFirewallRule` | `0xB260` | 350 | UnwindData |  |
