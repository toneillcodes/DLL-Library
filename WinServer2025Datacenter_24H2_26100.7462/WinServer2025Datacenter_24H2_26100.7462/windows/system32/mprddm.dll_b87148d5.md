# Binary Specification: mprddm.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\mprddm.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b87148d5dbd365426511e00b57ac3cc05a56ec6e251a507bc6ccad9ba2219f05`
* **Total Exported Functions:** 62

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DDMAdminConnectionClearStats` | `0x3030` | 699 | UnwindData |  |
| 2 | `DDMAdminConnectionEnum` | `0x3300` | 115 | UnwindData |  |
| 3 | `DDMAdminConnectionEnumEx` | `0x3380` | 168 | UnwindData |  |
| 4 | `DDMAdminConnectionGetInfo` | `0x3430` | 807 | UnwindData |  |
| 5 | `DDMAdminConnectionGetInfoEx` | `0x3760` | 677 | UnwindData |  |
| 6 | `DDMAdminInterfaceConnect` | `0x3A10` | 1,803 | UnwindData |  |
| 7 | `DDMAdminInterfaceDisconnect` | `0x4130` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `DDMAdminPortClearStats` | `0x4140` | 175 | UnwindData |  |
| 9 | `DDMAdminPortDisconnect` | `0x4200` | 177 | UnwindData |  |
| 10 | `DDMAdminPortEnum` | `0x42C0` | 915 | UnwindData |  |
| 11 | `DDMAdminPortGetInfo` | `0x4660` | 298 | UnwindData |  |
| 12 | `DDMAdminPortReset` | `0x4790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `DDMAdminRemoveQuarantine` | `0x47A0` | 247 | UnwindData |  |
| 14 | `DDMAdminRoutingDomainConnectionEnumEx` | `0x48A0` | 113 | UnwindData |  |
| 15 | `DDMAdminServerGetInfo` | `0x4920` | 565 | UnwindData |  |
| 16 | `DDMAdminServerGetInfoEx` | `0x4B60` | 3,203 | UnwindData |  |
| 17 | `DDMAdminServerSetInfo` | `0x57F0` | 958 | UnwindData |  |
| 18 | `DDMAdminServerSetInfoEx` | `0x5BC0` | 4,616 | UnwindData |  |
| 19 | `DDMAdminUpdateConnection` | `0x6DD0` | 1,563 | UnwindData |  |
| 20 | `DDMAdminUpdateQoSPolicies` | `0x7400` | 363 | UnwindData |  |
| 25 | `DDMPlumbRDIkev2TunnelPolicy` | `0x7580` | 382 | UnwindData |  |
| 27 | `DDMRegisterConnectionNotification` | `0x7710` | 312 | UnwindData |  |
| 28 | `DDMSendUserMessage` | `0x7850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `IfObjectGetStatistics` | `0x7860` | 934 | UnwindData |  |
| 30 | `DDMServicePostListens` | `0x85E0` | 97 | UnwindData |  |
| 36 | `DdmUpdateGlobalPhoneBookContext` | `0x9A80` | 77 | UnwindData |  |
| 37 | `IfObjectConnectionChangeNotification` | `0x9BE0` | 98 | UnwindData |  |
| 38 | `IfObjectFreePhonebookContext` | `0x9C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `IfObjectLoadDestinationInfo` | `0x9C70` | 434 | UnwindData |  |
| 41 | `IfObjectLoadPhonebookInfo` | `0x9E30` | 755 | UnwindData |  |
| 42 | `IfObjectSetDialoutHoursRestriction` | `0xA130` | 34 | UnwindData |  |
| 43 | `IfObjectUpdatePbkExtraInfo` | `0xA160` | 576 | UnwindData |  |
| 44 | `IfObjectUpdatePbkInfo` | `0xA3B0` | 882 | UnwindData |  |
| 31 | `DDMTransportCreate` | `0xBCC0` | 1,000 | UnwindData |  |
| 58 | `RasConnectionInitiate` | `0xFEF0` | 1,147 | UnwindData |  |
| 32 | `DdmDeleteIkev2PskPolicy` | `0x11040` | 408 | UnwindData |  |
| 33 | `DdmGetKey` | `0x11F10` | 784 | UnwindData |  |
| 34 | `DdmPlumbIkev2PskPolicy` | `0x12990` | 1,356 | UnwindData |  |
| 35 | `DdmSetKey` | `0x14860` | 484 | UnwindData |  |
| 21 | `DDMConnectInterface` | `0x19DD0` | 1,051 | UnwindData |  |
| 22 | `DDMDisconnectInterface` | `0x1A200` | 3,033 | UnwindData |  |
| 24 | `DDMHandleRoutingDomainConfigChange` | `0x1B520` | 1,022 | UnwindData |  |
| 29 | `DDMServiceInitialize` | `0x1BF40` | 9,649 | UnwindData |  |
| 45 | `MarkInterfaceAsReachable` | `0x1F960` | 185 | UnwindData |  |
| 59 | `ReConnectInterface` | `0x1FA20` | 1,090 | UnwindData |  |
| 60 | `ReConnectPersistentInterface` | `0x1FE70` | 693 | UnwindData |  |
| 61 | `TimerQInsert` | `0x20130` | 288 | UnwindData |  |
| 62 | `TimerQRemove` | `0x20260` | 369 | UnwindData |  |
| 23 | `DDMGetIdentityAttributes` | `0x279B0` | 433 | UnwindData |  |
| 26 | `DDMPostCleanup` | `0x27B70` | 279 | UnwindData |  |
| 46 | `RasAcctConfigChangeNotification` | `0x4DF10` | 61 | UnwindData |  |
| 47 | `RasAcctProviderFreeAttributes` | `0x4DF60` | 17 | UnwindData |  |
| 55 | `RasAuthProviderFreeAttributes` | `0x4DF60` | 17 | UnwindData |  |
| 48 | `RasAcctProviderInitialize` | `0x4DF80` | 148 | UnwindData |  |
| 49 | `RasAcctProviderInterimAccounting` | `0x4E020` | 92 | UnwindData |  |
| 50 | `RasAcctProviderStartAccounting` | `0x4E090` | 89 | UnwindData |  |
| 51 | `RasAcctProviderStopAccounting` | `0x4E0F0` | 92 | UnwindData |  |
| 52 | `RasAcctProviderTerminate` | `0x4E160` | 94 | UnwindData |  |
| 53 | `RasAuthConfigChangeNotification` | `0x4E1D0` | 61 | UnwindData |  |
| 54 | `RasAuthProviderAuthenticateUser` | `0x4E220` | 104 | UnwindData |  |
| 56 | `RasAuthProviderInitialize` | `0x4E290` | 399 | UnwindData |  |
| 57 | `RasAuthProviderTerminate` | `0x4E430` | 263 | UnwindData |  |
