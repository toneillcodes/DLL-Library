# Binary Specification: mprapi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\mprapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `538e6708e2af504747a54db86a1bda7597fcea6df6dc910ef524a41deec09d00`
* **Total Exported Functions:** 161

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `MprAdminAddRoutingDomain` | `0x4360` | 96 | UnwindData |  |
| 3 | `MprAdminBufferFree` | `0x43D0` | 34 | UnwindData |  |
| 54 | `MprAdminMIBBufferFree` | `0x43D0` | 34 | UnwindData |  |
| 4 | `MprAdminConnectionClearStats` | `0x4400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `MprAdminConnectionEnum` | `0x4410` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `MprAdminConnectionEnumEx` | `0x4470` | 511 | UnwindData |  |
| 7 | `MprAdminConnectionGetInfo` | `0x4680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `MprAdminConnectionGetInfoEx` | `0x4690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `MprAdminConnectionRemoveQuarantine` | `0x46A0` | 48 | UnwindData |  |
| 10 | `MprAdminDeleteRoutingDomain` | `0x46E0` | 96 | UnwindData |  |
| 11 | `MprAdminDeregisterConnectionNotification` | `0x4750` | 90 | UnwindData |  |
| 12 | `MprAdminDeviceEnum` | `0x47B0` | 148 | UnwindData |  |
| 14 | `MprAdminFreeRoutingDomainConfigEx` | `0x4850` | 85 | UnwindData |  |
| 15 | `MprAdminGetErrorString` | `0x48B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `MprAdminGetProtocolStatistics` | `0x48D0` | 288 | UnwindData |  |
| 18 | `MprAdminGetRoutingDomainId` | `0x4A00` | 139 | UnwindData |  |
| 19 | `MprAdminInterfaceAddIkev2Policy` | `0x4AA0` | 64 | UnwindData |  |
| 20 | `MprAdminInterfaceClearStatisticsEx` | `0x4AF0` | 75 | UnwindData |  |
| 21 | `MprAdminInterfaceConnect` | `0x4B50` | 136 | UnwindData |  |
| 22 | `MprAdminInterfaceCreate` | `0x4BE0` | 243 | UnwindData |  |
| 23 | `MprAdminInterfaceCreateEx` | `0x4CE0` | 361 | UnwindData |  |
| 24 | `MprAdminInterfaceDelete` | `0x4E50` | 64 | UnwindData |  |
| 25 | `MprAdminInterfaceDeviceGetInfo` | `0x4EA0` | 289 | UnwindData |  |
| 26 | `MprAdminInterfaceDeviceSetInfo` | `0x4FD0` | 559 | UnwindData |  |
| 27 | `MprAdminInterfaceDisconnect` | `0x5210` | 64 | UnwindData |  |
| 28 | `MprAdminInterfaceEnum` | `0x5260` | 315 | UnwindData |  |
| 29 | `MprAdminInterfaceEnumEx` | `0x53B0` | 439 | UnwindData |  |
| 30 | `MprAdminInterfaceGetCredentials` | `0x5570` | 455 | UnwindData |  |
| 31 | `MprAdminInterfaceGetCredentialsEx` | `0x5740` | 286 | UnwindData |  |
| 32 | `MprAdminInterfaceGetCustomInfoEx` | `0x5870` | 329 | UnwindData |  |
| 33 | `MprAdminInterfaceGetHandle` | `0x59C0` | 119 | UnwindData |  |
| 34 | `MprAdminInterfaceGetInfo` | `0x5A40` | 177 | UnwindData |  |
| 35 | `MprAdminInterfaceGetInfoEx` | `0x5B00` | 249 | UnwindData |  |
| 36 | `MprAdminInterfaceGetStatisticsEx` | `0x5C00` | 322 | UnwindData |  |
| 37 | `MprAdminInterfaceQueryUpdateResult` | `0x5D50` | 88 | UnwindData |  |
| 38 | `MprAdminInterfaceSetCredentials` | `0x5DB0` | 385 | UnwindData |  |
| 39 | `MprAdminInterfaceSetCredentialsEx` | `0x5F40` | 382 | UnwindData |  |
| 40 | `MprAdminInterfaceSetCustomInfoEx` | `0x60D0` | 338 | UnwindData |  |
| 41 | `MprAdminInterfaceSetInfo` | `0x6230` | 189 | UnwindData |  |
| 42 | `MprAdminInterfaceSetInfoEx` | `0x6300` | 348 | UnwindData |  |
| 43 | `MprAdminInterfaceTransportAdd` | `0x6470` | 132 | UnwindData |  |
| 44 | `MprAdminInterfaceTransportGetInfo` | `0x6500` | 177 | UnwindData |  |
| 45 | `MprAdminInterfaceTransportRemove` | `0x65C0` | 69 | UnwindData |  |
| 46 | `MprAdminInterfaceTransportSetInfo` | `0x6610` | 132 | UnwindData |  |
| 47 | `MprAdminInterfaceUpdatePhonebookInfo` | `0x66A0` | 64 | UnwindData |  |
| 48 | `MprAdminInterfaceUpdateRoutes` | `0x66F0` | 136 | UnwindData |  |
| 50 | `MprAdminIsModernStackEnabled` | `0x6780` | 88 | UnwindData |  |
| 51 | `MprAdminIsMultiTenancyEnabled` | `0x67E0` | 88 | UnwindData |  |
| 52 | `MprAdminIsServiceInitialized` | `0x6840` | 127 | UnwindData |  |
| 53 | `MprAdminIsServiceRunning` | `0x68D0` | 29 | UnwindData |  |
| 55 | `MprAdminMIBEntryCreate` | `0x6900` | 150 | UnwindData |  |
| 56 | `MprAdminMIBEntryDelete` | `0x69A0` | 150 | UnwindData |  |
| 57 | `MprAdminMIBEntryGet` | `0x6A40` | 221 | UnwindData |  |
| 58 | `MprAdminMIBEntryGetFirst` | `0x6B30` | 236 | UnwindData |  |
| 59 | `MprAdminMIBEntryGetNext` | `0x6C30` | 221 | UnwindData |  |
| 60 | `MprAdminMIBEntrySet` | `0x6D20` | 150 | UnwindData |  |
| 61 | `MprAdminMIBServerConnect` | `0x6DC0` | 20 | UnwindData |  |
| 62 | `MprAdminMIBServerDisconnect` | `0x6DE0` | 30 | UnwindData |  |
| 77 | `MprAdminServerDisconnect` | `0x6DE0` | 30 | UnwindData |  |
| 63 | `MprAdminMarkServerOffline` | `0x6E10` | 74 | UnwindData |  |
| 64 | `MprAdminPortClearStats` | `0x6E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `MprAdminPortDisconnect` | `0x6E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `MprAdminPortEnum` | `0x6E80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `MprAdminPortGetInfo` | `0x6EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `MprAdminPortReset` | `0x6EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `MprAdminProtocolAction` | `0x6EC0` | 150 | UnwindData |  |
| 70 | `MprAdminRegisterConnectionNotification` | `0x6F60` | 124 | UnwindData |  |
| 71 | `MprAdminRoutingDomainConnectionEnumEx` | `0x6FF0` | 293 | UnwindData |  |
| 72 | `MprAdminRoutingDomainGetConfigEx` | `0x7120` | 308 | UnwindData |  |
| 73 | `MprAdminRoutingDomainSetConfigEx` | `0x7260` | 204 | UnwindData |  |
| 74 | `MprAdminRoutingDomainsEnumEx` | `0x7340` | 378 | UnwindData |  |
| 75 | `MprAdminSendUserMessage` | `0x74C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `MprAdminServerConnect` | `0x74D0` | 140 | UnwindData |  |
| 78 | `MprAdminServerGetCredentials` | `0x7570` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `MprAdminServerGetInfo` | `0x75A0` | 138 | UnwindData |  |
| 80 | `MprAdminServerGetInfoEx` | `0x7630` | 1,297 | UnwindData |  |
| 81 | `MprAdminServerSetCredentials` | `0x7B50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `MprAdminServerSetInfo` | `0x7B70` | 164 | UnwindData |  |
| 83 | `MprAdminServerSetInfoEx` | `0x7C20` | 1,167 | UnwindData |  |
| 84 | `MprAdminTransportCreate` | `0x80C0` | 195 | UnwindData |  |
| 85 | `MprAdminTransportGetInfo` | `0x8190` | 283 | UnwindData |  |
| 86 | `MprAdminTransportSetInfo` | `0x82C0` | 168 | UnwindData |  |
| 87 | `MprAdminUpdateConnection` | `0x8370` | 329 | UnwindData |  |
| 148 | `MprFreeInterfaceInfoEx` | `0x84C0` | 68 | UnwindData |  |
| 1 | `CompressPhoneNumber` | `0x8BF0` | 693 | UnwindData |  |
| 13 | `MprAdminEstablishDomainRasServer` | `0x9910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `MprAdminIsDomainRasServer` | `0x9920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `MprDomainQueryRasServer` | `0x9930` | 185 | UnwindData |  |
| 147 | `MprDomainRegisterRasServer` | `0x99F0` | 186 | UnwindData |  |
| 159 | `MprPortSetUsage` | `0x18AE0` | 115 | UnwindData |  |
| 99 | `MprConfigAddRoutingDomain` | `0x18EC0` | 174 | UnwindData |  |
| 101 | `MprConfigDeleteRoutingDomain` | `0x18F80` | 222 | UnwindData |  |
| 104 | `MprConfigFreeRoutingDomainConfigEx` | `0x19070` | 106 | UnwindData |  |
| 107 | `MprConfigGetRoutingDomainId` | `0x190E0` | 166 | UnwindData |  |
| 126 | `MprConfigIsMultiTenancyEnabled` | `0x19190` | 112 | UnwindData |  |
| 127 | `MprConfigRoutingDomainEnumEx` | `0x19210` | 389 | UnwindData |  |
| 128 | `MprConfigRoutingDomainGetConfigEx` | `0x193A0` | 380 | UnwindData |  |
| 129 | `MprConfigRoutingDomainSetConfigEx` | `0x19530` | 258 | UnwindData |  |
| 100 | `MprConfigBufferFree` | `0x267B0` | 55 | UnwindData |  |
| 102 | `MprConfigFilterGetInfo` | `0x267F0` | 81 | UnwindData |  |
| 103 | `MprConfigFilterSetInfo` | `0x26850` | 81 | UnwindData |  |
| 105 | `MprConfigGetFriendlyName` | `0x268B0` | 139 | UnwindData |  |
| 106 | `MprConfigGetGuidName` | `0x26950` | 139 | UnwindData |  |
| 108 | `MprConfigInterfaceCreate` | `0x269F0` | 1,283 | UnwindData |  |
| 109 | `MprConfigInterfaceCreateEx` | `0x26F00` | 1,985 | UnwindData |  |
| 110 | `MprConfigInterfaceDelete` | `0x276D0` | 335 | UnwindData |  |
| 111 | `MprConfigInterfaceEnum` | `0x27830` | 596 | UnwindData |  |
| 112 | `MprConfigInterfaceEnumEx` | `0x27A90` | 818 | UnwindData |  |
| 113 | `MprConfigInterfaceGetCustomInfoEx` | `0x27DD0` | 407 | UnwindData |  |
| 114 | `MprConfigInterfaceGetHandle` | `0x27F70` | 250 | UnwindData |  |
| 115 | `MprConfigInterfaceGetInfo` | `0x28070` | 505 | UnwindData |  |
| 116 | `MprConfigInterfaceGetInfoEx` | `0x28270` | 550 | UnwindData |  |
| 117 | `MprConfigInterfaceSetCustomInfoEx` | `0x284A0` | 969 | UnwindData |  |
| 118 | `MprConfigInterfaceSetInfo` | `0x28870` | 582 | UnwindData |  |
| 119 | `MprConfigInterfaceSetInfoEx` | `0x28AC0` | 1,115 | UnwindData |  |
| 120 | `MprConfigInterfaceTransportAdd` | `0x28F30` | 756 | UnwindData |  |
| 121 | `MprConfigInterfaceTransportEnum` | `0x29230` | 593 | UnwindData |  |
| 122 | `MprConfigInterfaceTransportGetHandle` | `0x29490` | 259 | UnwindData |  |
| 123 | `MprConfigInterfaceTransportGetInfo` | `0x295A0` | 287 | UnwindData |  |
| 124 | `MprConfigInterfaceTransportRemove` | `0x296D0` | 189 | UnwindData |  |
| 125 | `MprConfigInterfaceTransportSetInfo` | `0x297A0` | 216 | UnwindData |  |
| 130 | `MprConfigServerBackup` | `0x29880` | 2,318 | UnwindData |  |
| 131 | `MprConfigServerConnect` | `0x2A1A0` | 579 | UnwindData |  |
| 132 | `MprConfigServerDisconnect` | `0x2A3F0` | 529 | UnwindData |  |
| 133 | `MprConfigServerGetInfo` | `0x2A610` | 387 | UnwindData |  |
| 134 | `MprConfigServerGetInfoEx` | `0x2A7A0` | 105 | UnwindData |  |
| 135 | `MprConfigServerInstall` | `0x2A810` | 2,470 | UnwindData |  |
| 136 | `MprConfigServerRefresh` | `0x2B1C0` | 557 | UnwindData |  |
| 137 | `MprConfigServerRestore` | `0x2B400` | 1,399 | UnwindData |  |
| 138 | `MprConfigServerSetInfo` | `0x2B980` | 286 | UnwindData |  |
| 139 | `MprConfigServerSetInfoEx` | `0x2BAB0` | 207 | UnwindData |  |
| 140 | `MprConfigTransportCreate` | `0x2BBC0` | 885 | UnwindData |  |
| 141 | `MprConfigTransportDelete` | `0x2BF40` | 218 | UnwindData |  |
| 142 | `MprConfigTransportEnum` | `0x2C020` | 586 | UnwindData |  |
| 143 | `MprConfigTransportGetHandle` | `0x2C270` | 215 | UnwindData |  |
| 144 | `MprConfigTransportGetInfo` | `0x2C350` | 573 | UnwindData |  |
| 145 | `MprConfigTransportSetInfo` | `0x2C5A0` | 365 | UnwindData |  |
| 160 | `MprUpgradeRouterConfigHelper` | `0x2C720` | 6,976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `MprAdminGetPDCServer` | `0x2E260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `MprAdminUpgradeUsers` | `0x2E280` | 147 | UnwindData |  |
| 89 | `MprAdminUserClose` | `0x2E320` | 58 | UnwindData |  |
| 90 | `MprAdminUserGetInfo` | `0x2E360` | 341 | UnwindData |  |
| 91 | `MprAdminUserOpen` | `0x2E4C0` | 134 | UnwindData |  |
| 92 | `MprAdminUserRead` | `0x2E550` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `MprAdminUserReadProfFlags` | `0x2E580` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `MprAdminUserServerConnect` | `0x2E640` | 312 | UnwindData |  |
| 95 | `MprAdminUserServerDisconnect` | `0x2E780` | 226 | UnwindData |  |
| 96 | `MprAdminUserSetInfo` | `0x2E870` | 314 | UnwindData |  |
| 97 | `MprAdminUserWrite` | `0x2E9B0` | 79 | UnwindData |  |
| 98 | `MprAdminUserWriteProfFlags` | `0x2EA10` | 26 | UnwindData |  |
| 161 | `RasPrivilegeAndCallBackNumber` | `0x2EE30` | 211 | UnwindData |  |
| 149 | `MprGetUsrParams` | `0x2F3C0` | 500 | UnwindData |  |
| 150 | `MprInfoBlockAdd` | `0x372D0` | 683 | UnwindData |  |
| 151 | `MprInfoBlockFind` | `0x37590` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `MprInfoBlockQuerySize` | `0x37620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `MprInfoBlockRemove` | `0x37640` | 643 | UnwindData |  |
| 154 | `MprInfoBlockSet` | `0x378D0` | 893 | UnwindData |  |
| 155 | `MprInfoCreate` | `0x37C60` | 120 | UnwindData |  |
| 156 | `MprInfoDelete` | `0x37CE0` | 60 | UnwindData |  |
| 157 | `MprInfoDuplicate` | `0x37D30` | 126 | UnwindData |  |
| 158 | `MprInfoRemoveAll` | `0x37DC0` | 127,308 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
