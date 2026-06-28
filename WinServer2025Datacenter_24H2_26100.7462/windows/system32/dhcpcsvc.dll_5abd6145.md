# Binary Specification: dhcpcsvc.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\dhcpcsvc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5abd6145947f915926f9f954b800346dc3d2723d897cacc66e514d4cecd3c663`
* **Total Exported Functions:** 71

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 32 | `DhcpIsEnabled` | `0x1220` | 36 | UnwindData |  |
| 19 | `DhcpFreeLeaseInfoArray` | `0x1810` | 81 | UnwindData |  |
| 16 | `DhcpFreeCachedParamsData` | `0x1AD0` | 96 | UnwindData |  |
| 18 | `DhcpFreeLeaseInfo` | `0x1C30` | 87 | UnwindData |  |
| 17 | `DhcpFreeEnumeratedInterfaces` | `0x1EE0` | 118 | UnwindData |  |
| 4 | `DhcpCApiInitialize` | `0x2200` | 72 | UnwindData |  |
| 8 | `DhcpDeRegisterParamChange` | `0x2250` | 65 | UnwindData |  |
| 14 | `DhcpEnumInterfaces` | `0x23A0` | 400 | UnwindData |  |
| 23 | `DhcpGetDhcpServicedConnections` | `0x2540` | 836 | UnwindData |  |
| 33 | `DhcpIsMeteredDetected` | `0x2890` | 639 | UnwindData |  |
| 41 | `DhcpQueryLeaseInfo` | `0x2B20` | 949 | UnwindData |  |
| 42 | `DhcpQueryLeaseInfoArray` | `0x2EE0` | 1,539 | UnwindData |  |
| 43 | `DhcpQueryLeaseInfoEx` | `0x34F0` | 979 | UnwindData |  |
| 55 | `DhcpRequestParams` | `0x38D0` | 2,130 | UnwindData |  |
| 20 | `DhcpFreeMem` | `0x4670` | 63 | UnwindData |  |
| 1 | `DhcpAcquireParameters` | `0x6190` | 319 | UnwindData |  |
| 2 | `DhcpAcquireParametersByBroadcast` | `0x62E0` | 319 | UnwindData |  |
| 3 | `DhcpCApiCleanup` | `0x6430` | 51 | UnwindData |  |
| 5 | `DhcpClient_Generalize` | `0x6470` | 313 | UnwindData |  |
| 6 | `DhcpDeRegisterConnectionStateNotification` | `0x6730` | 287 | UnwindData |  |
| 7 | `DhcpDeRegisterOptions` | `0x6860` | 63 | UnwindData |  |
| 9 | `DhcpDelPersistentRequestParams` | `0x69F0` | 1,205 | UnwindData |  |
| 10 | `DhcpEnableDhcp` | `0x6EB0` | 248 | UnwindData |  |
| 11 | `DhcpEnableDhcpAdvanced` | `0x6FB0` | 373 | UnwindData |  |
| 12 | `DhcpEnableTracing` | `0x73B0` | 208 | UnwindData |  |
| 15 | `DhcpFallbackRefreshParams` | `0x7490` | 368 | UnwindData |  |
| 21 | `DhcpGetClassId` | `0x7610` | 506 | UnwindData |  |
| 22 | `DhcpGetClientId` | `0x7810` | 491 | UnwindData |  |
| 24 | `DhcpGetFallbackParams` | `0x7A10` | 330 | UnwindData |  |
| 25 | `DhcpGetNotificationStatus` | `0x7B60` | 951 | UnwindData |  |
| 26 | `DhcpGetOriginalSubnetMask` | `0x7F20` | 326 | UnwindData |  |
| 27 | `DhcpGetTraceArray` | `0x8070` | 349 | UnwindData |  |
| 34 | `DhcpLeaseIpAddress` | `0x81E0` | 55 | UnwindData |  |
| 35 | `DhcpLeaseIpAddressEx` | `0x8220` | 1,091 | UnwindData |  |
| 38 | `DhcpNotifyMediaReconnected` | `0x8670` | 368 | UnwindData |  |
| 40 | `DhcpPersistentRequestParams` | `0x87F0` | 246 | UnwindData |  |
| 44 | `DhcpRegisterConnectionStateNotification` | `0x8B90` | 461 | UnwindData |  |
| 45 | `DhcpRegisterOptions` | `0x8D70` | 449 | UnwindData |  |
| 46 | `DhcpRegisterParamChange` | `0x8F40` | 432 | UnwindData |  |
| 47 | `DhcpReleaseIpAddressLease` | `0xA440` | 151 | UnwindData |  |
| 48 | `DhcpReleaseIpAddressLeaseEx` | `0xA4E0` | 1,072 | UnwindData |  |
| 49 | `DhcpReleaseParameters` | `0xA920` | 319 | UnwindData |  |
| 50 | `DhcpRemoveDNSRegistrations` | `0xAA70` | 283 | UnwindData |  |
| 51 | `DhcpRenewIpAddressLease` | `0xABA0` | 192 | UnwindData |  |
| 52 | `DhcpRenewIpAddressLeaseEx` | `0xAC70` | 1,133 | UnwindData |  |
| 53 | `DhcpRequestCachedParams` | `0xB0F0` | 770 | UnwindData |  |
| 54 | `DhcpRequestOptions` | `0xB400` | 1,366 | UnwindData |  |
| 56 | `DhcpRetrieveOptionsViaInform` | `0xB960` | 477 | UnwindData |  |
| 57 | `DhcpSetClassId` | `0xBB50` | 532 | UnwindData |  |
| 58 | `DhcpSetClientId` | `0xBD70` | 519 | UnwindData |  |
| 59 | `DhcpSetFallbackParams` | `0xBF80` | 509 | UnwindData |  |
| 60 | `DhcpSetMSFTVendorSpecificOptions` | `0xC190` | 677 | UnwindData |  |
| 61 | `DhcpStaticRefreshParams` | `0xC440` | 141 | UnwindData |  |
| 62 | `DhcpUndoRequestParams` | `0xC600` | 208 | UnwindData |  |
| 63 | `Dhcpv4CheckServerAvailability` | `0xC6E0` | 379 | UnwindData |  |
| 64 | `Dhcpv4EnableDhcpEx` | `0xC870` | 422 | UnwindData |  |
| 65 | `McastApiCleanup` | `0xCA50` | 258 | UnwindData |  |
| 66 | `McastApiStartup` | `0xCB60` | 303 | UnwindData |  |
| 67 | `McastEnumerateScopes` | `0xCCA0` | 607 | UnwindData |  |
| 68 | `McastGenUID` | `0xCF10` | 429 | UnwindData |  |
| 69 | `McastReleaseAddress` | `0xD0D0` | 630 | UnwindData |  |
| 70 | `McastRenewAddress` | `0xD350` | 960 | UnwindData |  |
| 71 | `McastRequestAddress` | `0xD720` | 904 | UnwindData |  |
| 13 | `DhcpEnumClasses` | `0xDD30` | 612 | UnwindData |  |
| 31 | `DhcpHandlePnPEvent` | `0xDFA0` | 219 | UnwindData |  |
| 36 | `DhcpNotifyConfigChange` | `0xE090` | 230 | UnwindData |  |
| 37 | `DhcpNotifyConfigChangeEx` | `0xE180` | 317 | UnwindData |  |
| 39 | `DhcpOpenGlobalEvent` | `0xE2D0` | 641 | UnwindData |  |
| 28 | `DhcpGlobalIsShuttingDown` | `0x1E75C` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `DhcpGlobalServiceSyncEvent` | `0x1E760` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `DhcpGlobalTerminateEvent` | `0x1E768` | 0 | Indeterminate |  |
