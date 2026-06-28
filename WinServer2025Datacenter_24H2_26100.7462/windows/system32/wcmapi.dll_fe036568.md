# Binary Specification: wcmapi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wcmapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fe0365682529cf01523e912908c53595c8656dabab56fa699d09654ecd13ad12`
* **Total Exported Functions:** 36

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 30 | `WcmQueryParameter` | `0x2860` | 1,138 | UnwindData |  |
| 31 | `WcmQueryProperty` | `0x2CE0` | 833 | UnwindData |  |
| 21 | `WcmGetInterfaceContextTable` | `0x34F0` | 544 | UnwindData |  |
| 34 | `WcmSetParameter` | `0x3720` | 984 | UnwindData |  |
| 25 | `WcmOpenHandle` | `0x4040` | 1,200 | UnwindData |  |
| 14 | `WcmCloseHandle` | `0x4580` | 646 | UnwindData |  |
| 24 | `WcmGetRoutingHint` | `0x4950` | 551 | UnwindData |  |
| 39 | `WcmUpdateCapabilityAccess` | `0x51B0` | 468 | UnwindData |  |
| 18 | `WcmDeprovisionCapability` | `0x53C0` | 431 | UnwindData |  |
| 20 | `WcmFreeMemory` | `0x59C0` | 57 | UnwindData |  |
| 22 | `WcmGetProfileList` | `0x62B0` | 426 | UnwindData |  |
| 6 | `DllCanUnloadNow` | `0x9270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `DllGetClassObject` | `0x9290` | 189 | UnwindData |  |
| 8 | `DllRegisterServer` | `0x9360` | 26,592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `DllUnregisterServer` | `0x9360` | 26,592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | *Ordinal Only* | `0xFB40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `WcmAddAppBasedRoutePolicy` | `0xFB50` | 395 | UnwindData |  |
| 11 | `WcmAddRoutePolicy` | `0xFCF0` | 508 | UnwindData |  |
| 12 | `WcmCancelOnDemandRequest` | `0xFF00` | 709 | UnwindData |  |
| 13 | `WcmCheckCapabilityStatus` | `0x101D0` | 401 | UnwindData |  |
| 15 | `WcmCloseOnDemandRequestHandle` | `0x10370` | 691 | UnwindData |  |
| 16 | `WcmDeleteAppBasedRoutePolicy` | `0x10630` | 395 | UnwindData |  |
| 17 | `WcmDeleteProxyInformation` | `0x107D0` | 412 | UnwindData |  |
| 19 | `WcmEnumInterfaces` | `0x10980` | 691 | UnwindData |  |
| 23 | `WcmGetProfileListByPurpose` | `0x10C40` | 604 | UnwindData |  |
| 26 | `WcmOpenOnDemandRequestHandle` | `0x10EB0` | 1,174 | UnwindData |  |
| 27 | `WcmOpenOnDemandRequestHandleByWwanProfileName` | `0x11350` | 964 | UnwindData |  |
| 28 | `WcmOrderConnection` | `0x11720` | 497 | UnwindData |  |
| 29 | `WcmQueryOnDemandRequestStateInfo` | `0x11920` | 712 | UnwindData |  |
| 5 | *Ordinal Only* | `0x11BF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `WcmRemoveMatchingRoutePolicy` | `0x11C00` | 419 | UnwindData |  |
| 33 | `WcmRemoveRoutePolicy` | `0x11DB0` | 318 | UnwindData |  |
| 35 | `WcmSetProfileList` | `0x11F00` | 698 | UnwindData |  |
| 36 | `WcmSetProperty` | `0x121C0` | 613 | UnwindData |  |
| 37 | `WcmSetProxyInformation` | `0x12430` | 432 | UnwindData |  |
| 38 | `WcmStartOnDemandRequest` | `0x125F0` | 1,088 | UnwindData |  |
