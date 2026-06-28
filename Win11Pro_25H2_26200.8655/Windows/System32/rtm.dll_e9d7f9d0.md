# Binary Specification: rtm.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\rtm.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e9d7f9d0e0544b6e1c8e6835dfdfcd6c24dc02681b29f6e140468c1b08ec7942`
* **Total Exported Functions:** 116

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `BestMatchInTable` | `0x1AD0` | 240 | UnwindData |  |
| 2 | `CheckTable` | `0x1C80` | 40 | UnwindData |  |
| 3 | `CreateTable` | `0x1DF0` | 92 | UnwindData |  |
| 4 | `DeleteFromTable` | `0x1E60` | 307 | UnwindData |  |
| 5 | `DestroyTable` | `0x1FA0` | 63 | UnwindData |  |
| 6 | `DumpTable` | `0x2100` | 114 | UnwindData |  |
| 7 | `EnumOverTable` | `0x2240` | 441 | UnwindData |  |
| 8 | `InsertIntoTable` | `0x2400` | 468 | UnwindData |  |
| 27 | `NextMatchInTable` | `0x25E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `SearchInTable` | `0x2600` | 358 | UnwindData |  |
| 56 | `RtmDeregisterFromChangeNotification` | `0x3880` | 671 | UnwindData |  |
| 60 | `RtmGetChangeStatus` | `0x3B30` | 159 | UnwindData |  |
| 61 | `RtmGetChangedDests` | `0x3BE0` | 1,047 | UnwindData |  |
| 87 | `RtmIgnoreChangedDests` | `0x4000` | 170 | UnwindData |  |
| 91 | `RtmIsMarkedForChangeNotification` | `0x40B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `RtmMarkDestForChangeNotification` | `0x40F0` | 144 | UnwindData |  |
| 103 | `RtmRegisterForChangeNotification` | `0x4190` | 675 | UnwindData |  |
| 104 | `RtmReleaseChangedDests` | `0x4440` | 94 | UnwindData |  |
| 98 | `RtmReadAddressFamilyConfig` | `0x4540` | 1,606 | UnwindData |  |
| 99 | `RtmReadInstanceConfig` | `0x4B90` | 622 | UnwindData |  |
| 114 | `RtmWriteAddressFamilyConfig` | `0x4E10` | 2,046 | UnwindData |  |
| 115 | `RtmWriteInstanceConfig` | `0x58C0` | 635 | UnwindData |  |
| 39 | `RtmCreateBestRouteEnum` | `0x5C80` | 385 | UnwindData |  |
| 40 | `RtmCreateDestEnum` | `0x5E10` | 528 | UnwindData |  |
| 42 | `RtmCreateNextHopEnum` | `0x6030` | 471 | UnwindData |  |
| 43 | `RtmCreateRouteEnum` | `0x6210` | 851 | UnwindData |  |
| 46 | `RtmDeleteEnumHandle` | `0x6570` | 503 | UnwindData |  |
| 65 | `RtmGetEnumBestRoutes` | `0x6770` | 693 | UnwindData |  |
| 66 | `RtmGetEnumDests` | `0x6A30` | 658 | UnwindData |  |
| 67 | `RtmGetEnumNextHops` | `0x6CD0` | 542 | UnwindData |  |
| 68 | `RtmGetEnumRoutes` | `0x6F00` | 782 | UnwindData |  |
| 106 | `RtmReleaseDests` | `0x7220` | 95 | UnwindData |  |
| 110 | `RtmReleaseNextHops` | `0x7290` | 92 | UnwindData |  |
| 112 | `RtmReleaseRoutes` | `0x7300` | 92 | UnwindData |  |
| 53 | `RtmDereferenceHandles` | `0x7370` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `RtmReferenceHandles` | `0x73A0` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `RtmGetDestInfo` | `0x7600` | 140 | UnwindData |  |
| 63 | `RtmGetEntityInfo` | `0x76A0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `RtmGetNextHopInfo` | `0x76F0` | 174 | UnwindData |  |
| 84 | `RtmGetRouteInfo` | `0x77B0` | 141 | UnwindData |  |
| 105 | `RtmReleaseDestInfo` | `0x7850` | 195 | UnwindData |  |
| 108 | `RtmReleaseEntityInfo` | `0x7920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `RtmReleaseNextHopInfo` | `0x7930` | 81 | UnwindData |  |
| 111 | `RtmReleaseRouteInfo` | `0x7990` | 184 | UnwindData |  |
| 44 | `RtmCreateRouteList` | `0x7A50` | 125 | UnwindData |  |
| 45 | `RtmCreateRouteListEnum` | `0x7AE0` | 240 | UnwindData |  |
| 49 | `RtmDeleteRouteList` | `0x7BE0` | 318 | UnwindData |  |
| 75 | `RtmGetListEnumRoutes` | `0x7D30` | 278 | UnwindData |  |
| 88 | `RtmInsertInRouteList` | `0x7E50` | 273 | UnwindData |  |
| 35 | `RtmCleanupInstances` | `0x8350` | 517 | UnwindData |  |
| 33 | `RtmBlockMethods` | `0x8590` | 76 | UnwindData |  |
| 64 | `RtmGetEntityMethods` | `0x85F0` | 130 | UnwindData |  |
| 89 | `RtmInvokeMethod` | `0x8680` | 348 | UnwindData |  |
| 59 | `RtmGetAddressFamilyInfo` | `0x8960` | 697 | UnwindData |  |
| 72 | `RtmGetInstanceInfo` | `0x8C20` | 636 | UnwindData |  |
| 73 | `RtmGetInstances` | `0x8EB0` | 386 | UnwindData |  |
| 28 | `RtmAddNextHop` | `0x90D0` | 667 | UnwindData |  |
| 47 | `RtmDeleteNextHop` | `0x9380` | 449 | UnwindData |  |
| 58 | `RtmFindNextHop` | `0x9550` | 203 | UnwindData |  |
| 79 | `RtmGetNextHopPointer` | `0x9630` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `RtmLockNextHop` | `0x9660` | 136 | UnwindData |  |
| 69 | `RtmGetExactMatchDestination` | `0xAD80` | 233 | UnwindData |  |
| 70 | `RtmGetExactMatchRoute` | `0xAE70` | 364 | UnwindData |  |
| 74 | `RtmGetLessSpecificDestination` | `0xAFF0` | 215 | UnwindData |  |
| 76 | `RtmGetMostSpecificDestination` | `0xB0D0` | 249 | UnwindData |  |
| 90 | `RtmIsBestRoute` | `0xB1D0` | 196 | UnwindData |  |
| 55 | `RtmDeregisterEntity` | `0xB2A0` | 631 | UnwindData |  |
| 81 | `RtmGetOpaqueInformationPointer` | `0xB520` | 457 | UnwindData |  |
| 82 | `RtmGetRegisteredEntities` | `0xB6F0` | 628 | UnwindData |  |
| 93 | `RtmLockDestination` | `0xB970` | 80 | UnwindData |  |
| 102 | `RtmRegisterEntity` | `0xB9D0` | 744 | UnwindData |  |
| 107 | `RtmReleaseEntities` | `0xBCC0` | 70 | UnwindData |  |
| 30 | `RtmAddRouteToDest` | `0xBF50` | 4,602 | UnwindData |  |
| 51 | `RtmDeleteRouteToDest` | `0xD150` | 2,174 | UnwindData |  |
| 85 | `RtmGetRoutePointer` | `0xD9E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `RtmHoldDestination` | `0xDA20` | 238 | UnwindData |  |
| 95 | `RtmLockRoute` | `0xDB20` | 174 | UnwindData |  |
| 113 | `RtmUpdateAndUnlockRoute` | `0xDBE0` | 2,436 | UnwindData |  |
| 37 | `RtmConvertIpv6AddressAndLengthToNetAddress` | `0xE8C0` | 135 | UnwindData |  |
| 38 | `RtmConvertNetAddressToIpv6AddressAndLength` | `0xE950` | 166 | UnwindData |  |
| 29 | `RtmAddRoute` | `0xFC80` | 2,311 | UnwindData |  |
| 31 | `RtmBlockConvertRoutesToStatic` | `0x10590` | 725 | UnwindData |  |
| 32 | `RtmBlockDeleteRoutes` | `0x10870` | 701 | UnwindData |  |
| 34 | `RtmBlockSetRouteEnable` | `0x10B40` | 816 | UnwindData |  |
| 36 | `RtmCloseEnumerationHandle` | `0x10E80` | 284 | UnwindData |  |
| 41 | `RtmCreateEnumerationHandle` | `0x10FB0` | 623 | UnwindData |  |
| 48 | `RtmDeleteRoute` | `0x11230` | 669 | UnwindData |  |
| 50 | `RtmDeleteRouteTable` | `0x114E0` | 442 | UnwindData |  |
| 52 | `RtmDequeueRouteChangeMessage` | `0x116A0` | 586 | UnwindData |  |
| 54 | `RtmDeregisterClient` | `0x118F0` | 506 | UnwindData |  |
| 57 | `RtmEnumerateGetNextRoute` | `0x11AF0` | 481 | UnwindData |  |
| 71 | `RtmGetFirstRoute` | `0x11CE0` | 566 | UnwindData |  |
| 77 | `RtmGetNetworkCount` | `0x11F20` | 75 | UnwindData |  |
| 80 | `RtmGetNextRoute` | `0x11F80` | 748 | UnwindData |  |
| 83 | `RtmGetRouteAge` | `0x12280` | 107 | UnwindData |  |
| 92 | `RtmIsRoute` | `0x12300` | 328 | UnwindData |  |
| 96 | `RtmLookupIPDestination` | `0x12450` | 68 | UnwindData |  |
| 101 | `RtmRegisterClient` | `0x124A0` | 452 | UnwindData |  |
| 9 | `MgmAddGroupMembershipEntry` | `0x12A80` | 2,456 | UnwindData |  |
| 10 | `MgmDeInitialize` | `0x13420` | 1,022 | UnwindData |  |
| 11 | `MgmDeRegisterMProtocol` | `0x13830` | 477 | UnwindData |  |
| 12 | `MgmDeleteGroupMembershipEntry` | `0x13A20` | 1,352 | UnwindData |  |
| 13 | `MgmGetFirstMfe` | `0x140E0` | 331 | UnwindData |  |
| 14 | `MgmGetFirstMfeStats` | `0x14240` | 332 | UnwindData |  |
| 15 | `MgmGetMfe` | `0x143A0` | 277 | UnwindData |  |
| 16 | `MgmGetMfeStats` | `0x144C0` | 278 | UnwindData |  |
| 17 | `MgmGetNextMfe` | `0x145E0` | 288 | UnwindData |  |
| 18 | `MgmGetNextMfeStats` | `0x14710` | 294 | UnwindData |  |
| 19 | `MgmGetProtocolOnInterface` | `0x14840` | 512 | UnwindData |  |
| 20 | `MgmGroupEnumerationEnd` | `0x14A50` | 274 | UnwindData |  |
| 21 | `MgmGroupEnumerationGetNext` | `0x14B70` | 327 | UnwindData |  |
| 22 | `MgmGroupEnumerationStart` | `0x14CC0` | 461 | UnwindData |  |
| 23 | `MgmInitialize` | `0x14EA0` | 1,863 | UnwindData |  |
| 24 | `MgmRegisterMProtocol` | `0x155F0` | 888 | UnwindData |  |
| 25 | `MgmReleaseInterfaceOwnership` | `0x15970` | 995 | UnwindData |  |
| 26 | `MgmTakeInterfaceOwnership` | `0x15D60` | 679 | UnwindData |  |
