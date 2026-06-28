# Binary Specification: dhcpcsvc.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\dhcpcsvc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2a9970e685b623060bd18f30a953670f1374c63b3ef46a31d80de11102102075`
* **Total Exported Functions:** 71

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 32 | `DhcpIsEnabled` | `0x11D0` | 36 | UnwindData |  |
| 19 | `DhcpFreeLeaseInfoArray` | `0x17F0` | 86 | UnwindData |  |
| 16 | `DhcpFreeCachedParamsData` | `0x1990` | 96 | UnwindData |  |
| 18 | `DhcpFreeLeaseInfo` | `0x1AF0` | 92 | UnwindData |  |
| 17 | `DhcpFreeEnumeratedInterfaces` | `0x1C90` | 123 | UnwindData |  |
| 4 | `DhcpCApiInitialize` | `0x1FC0` | 77 | UnwindData |  |
| 8 | `DhcpDeRegisterParamChange` | `0x2020` | 70 | UnwindData |  |
| 14 | `DhcpEnumInterfaces` | `0x2170` | 427 | UnwindData |  |
| 23 | `DhcpGetDhcpServicedConnections` | `0x2330` | 853 | UnwindData |  |
| 33 | `DhcpIsMeteredDetected` | `0x2690` | 673 | UnwindData |  |
| 41 | `DhcpQueryLeaseInfo` | `0x2940` | 983 | UnwindData |  |
| 42 | `DhcpQueryLeaseInfoArray` | `0x2D20` | 1,587 | UnwindData |  |
| 43 | `DhcpQueryLeaseInfoEx` | `0x3360` | 1,013 | UnwindData |  |
| 55 | `DhcpRequestParams` | `0x3760` | 2,141 | UnwindData |  |
| 20 | `DhcpFreeMem` | `0x48A0` | 68 | UnwindData |  |
| 1 | `DhcpAcquireParameters` | `0x63C0` | 334 | UnwindData |  |
| 2 | `DhcpAcquireParametersByBroadcast` | `0x6520` | 334 | UnwindData |  |
| 3 | `DhcpCApiCleanup` | `0x6680` | 56 | UnwindData |  |
| 5 | `DhcpClient_Generalize` | `0x66C0` | 339 | UnwindData |  |
| 6 | `DhcpDeRegisterConnectionStateNotification` | `0x69A0` | 303 | UnwindData |  |
| 7 | `DhcpDeRegisterOptions` | `0x6AE0` | 68 | UnwindData |  |
| 9 | `DhcpDelPersistentRequestParams` | `0x6C70` | 1,218 | UnwindData |  |
| 10 | `DhcpEnableDhcp` | `0x7140` | 266 | UnwindData |  |
| 11 | `DhcpEnableDhcpAdvanced` | `0x7250` | 389 | UnwindData |  |
| 15 | `DhcpFallbackRefreshParams` | `0x7680` | 388 | UnwindData |  |
| 21 | `DhcpGetClassId` | `0x7810` | 521 | UnwindData |  |
| 22 | `DhcpGetClientId` | `0x7A20` | 506 | UnwindData |  |
| 24 | `DhcpGetFallbackParams` | `0x7C20` | 345 | UnwindData |  |
| 25 | `DhcpGetNotificationStatus` | `0x7D80` | 961 | UnwindData |  |
| 26 | `DhcpGetOriginalSubnetMask` | `0x8150` | 339 | UnwindData |  |
| 27 | `DhcpGetTraceArray` | `0x82B0` | 362 | UnwindData |  |
| 34 | `DhcpLeaseIpAddress` | `0x8420` | 55 | UnwindData |  |
| 35 | `DhcpLeaseIpAddressEx` | `0x8460` | 1,159 | UnwindData |  |
| 38 | `DhcpNotifyMediaReconnected` | `0x88F0` | 388 | UnwindData |  |
| 40 | `DhcpPersistentRequestParams` | `0x8A80` | 253 | UnwindData |  |
| 44 | `DhcpRegisterConnectionStateNotification` | `0x8E30` | 483 | UnwindData |  |
| 45 | `DhcpRegisterOptions` | `0x9020` | 457 | UnwindData |  |
| 46 | `DhcpRegisterParamChange` | `0x91F0` | 440 | UnwindData |  |
| 47 | `DhcpReleaseIpAddressLease` | `0xA740` | 162 | UnwindData |  |
| 48 | `DhcpReleaseIpAddressLeaseEx` | `0xA7F0` | 1,098 | UnwindData |  |
| 49 | `DhcpReleaseParameters` | `0xAC40` | 334 | UnwindData |  |
| 50 | `DhcpRemoveDNSRegistrations` | `0xADA0` | 310 | UnwindData |  |
| 51 | `DhcpRenewIpAddressLease` | `0xAEE0` | 203 | UnwindData |  |
| 52 | `DhcpRenewIpAddressLeaseEx` | `0xAFC0` | 1,210 | UnwindData |  |
| 53 | `DhcpRequestCachedParams` | `0xB480` | 785 | UnwindData |  |
| 54 | `DhcpRequestOptions` | `0xB7A0` | 1,359 | UnwindData |  |
| 56 | `DhcpRetrieveOptionsViaInform` | `0xBD00` | 491 | UnwindData |  |
| 57 | `DhcpSetClassId` | `0xBF00` | 583 | UnwindData |  |
| 58 | `DhcpSetClientId` | `0xC150` | 579 | UnwindData |  |
| 59 | `DhcpSetFallbackParams` | `0xC3A0` | 537 | UnwindData |  |
| 60 | `DhcpSetMSFTVendorSpecificOptions` | `0xC5C0` | 696 | UnwindData |  |
| 61 | `DhcpStaticRefreshParams` | `0xC880` | 157 | UnwindData |  |
| 62 | `DhcpUndoRequestParams` | `0xCA50` | 221 | UnwindData |  |
| 63 | `Dhcpv4CheckServerAvailability` | `0xCB40` | 399 | UnwindData |  |
| 64 | `Dhcpv4EnableDhcpEx` | `0xCCE0` | 442 | UnwindData |  |
| 65 | `McastApiCleanup` | `0xCED0` | 283 | UnwindData |  |
| 66 | `McastApiStartup` | `0xD000` | 325 | UnwindData |  |
| 67 | `McastEnumerateScopes` | `0xD150` | 630 | UnwindData |  |
| 68 | `McastGenUID` | `0xD3D0` | 456 | UnwindData |  |
| 69 | `McastReleaseAddress` | `0xD5A0` | 657 | UnwindData |  |
| 70 | `McastRenewAddress` | `0xD840` | 979 | UnwindData |  |
| 71 | `McastRequestAddress` | `0xDC20` | 931 | UnwindData |  |
| 13 | `DhcpEnumClasses` | `0xE250` | 647 | UnwindData |  |
| 31 | `DhcpHandlePnPEvent` | `0xE4E0` | 224 | UnwindData |  |
| 36 | `DhcpNotifyConfigChange` | `0xF100` | 237 | UnwindData |  |
| 37 | `DhcpNotifyConfigChangeEx` | `0xF200` | 324 | UnwindData |  |
| 39 | `DhcpOpenGlobalEvent` | `0xF350` | 647 | UnwindData |  |
| 12 | `DhcpEnableTracing` | `0xF5E0` | 70,112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `DhcpGlobalIsShuttingDown` | `0x207C0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `DhcpGlobalServiceSyncEvent` | `0x207C8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `DhcpGlobalTerminateEvent` | `0x207D0` | 0 | Indeterminate |  |
