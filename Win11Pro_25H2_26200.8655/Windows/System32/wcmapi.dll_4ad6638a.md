# Binary Specification: wcmapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wcmapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4ad6638a7ee3d32e6a5d61713366f6b9e0af524dcd602e319c97c581b6de4483`
* **Total Exported Functions:** 36

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 30 | `WcmQueryParameter` | `0x2810` | 1,138 | UnwindData |  |
| 31 | `WcmQueryProperty` | `0x2C90` | 833 | UnwindData |  |
| 21 | `WcmGetInterfaceContextTable` | `0x34A0` | 544 | UnwindData |  |
| 34 | `WcmSetParameter` | `0x36D0` | 984 | UnwindData |  |
| 25 | `WcmOpenHandle` | `0x3FF0` | 1,200 | UnwindData |  |
| 14 | `WcmCloseHandle` | `0x4530` | 646 | UnwindData |  |
| 24 | `WcmGetRoutingHint` | `0x4900` | 551 | UnwindData |  |
| 39 | `WcmUpdateCapabilityAccess` | `0x5160` | 468 | UnwindData |  |
| 18 | `WcmDeprovisionCapability` | `0x5370` | 431 | UnwindData |  |
| 20 | `WcmFreeMemory` | `0x5970` | 57 | UnwindData |  |
| 22 | `WcmGetProfileList` | `0x6260` | 426 | UnwindData |  |
| 6 | `DllCanUnloadNow` | `0x9220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `DllGetClassObject` | `0x9240` | 189 | UnwindData |  |
| 8 | `DllRegisterServer` | `0x9310` | 25,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `DllUnregisterServer` | `0x9310` | 25,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | *Ordinal Only* | `0xF5D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `WcmAddAppBasedRoutePolicy` | `0xF5E0` | 395 | UnwindData |  |
| 11 | `WcmAddRoutePolicy` | `0xF780` | 508 | UnwindData |  |
| 12 | `WcmCancelOnDemandRequest` | `0xF990` | 709 | UnwindData |  |
| 13 | `WcmCheckCapabilityStatus` | `0xFC60` | 401 | UnwindData |  |
| 15 | `WcmCloseOnDemandRequestHandle` | `0xFE00` | 691 | UnwindData |  |
| 16 | `WcmDeleteAppBasedRoutePolicy` | `0x100C0` | 395 | UnwindData |  |
| 17 | `WcmDeleteProxyInformation` | `0x10260` | 412 | UnwindData |  |
| 19 | `WcmEnumInterfaces` | `0x10410` | 691 | UnwindData |  |
| 23 | `WcmGetProfileListByPurpose` | `0x106D0` | 604 | UnwindData |  |
| 26 | `WcmOpenOnDemandRequestHandle` | `0x10940` | 1,174 | UnwindData |  |
| 27 | `WcmOpenOnDemandRequestHandleByWwanProfileName` | `0x10DE0` | 964 | UnwindData |  |
| 28 | `WcmOrderConnection` | `0x111B0` | 497 | UnwindData |  |
| 29 | `WcmQueryOnDemandRequestStateInfo` | `0x113B0` | 712 | UnwindData |  |
| 5 | *Ordinal Only* | `0x11680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `WcmRemoveMatchingRoutePolicy` | `0x11690` | 419 | UnwindData |  |
| 33 | `WcmRemoveRoutePolicy` | `0x11840` | 318 | UnwindData |  |
| 35 | `WcmSetProfileList` | `0x11990` | 698 | UnwindData |  |
| 36 | `WcmSetProperty` | `0x11C50` | 613 | UnwindData |  |
| 37 | `WcmSetProxyInformation` | `0x11EC0` | 432 | UnwindData |  |
| 38 | `WcmStartOnDemandRequest` | `0x12080` | 1,088 | UnwindData |  |
