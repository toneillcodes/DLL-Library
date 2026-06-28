# Binary Specification: FirewallAPI.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\FirewallAPI.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3b6f659956656bf8408d7e4cd7a03da122b67c724badc9f3b3e84ab8af08b921`
* **Total Exported Functions:** 247

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `FwBstrToPorts` | `0x1BA0` | 511 | UnwindData |  |
| 158 | `FWVerifyFirewallRule` | `0x20D0` | 84 | UnwindData |  |
| 20 | `FWAddFirewallRule` | `0x45A0` | 706 | UnwindData |  |
| 137 | `FWSetFirewallRule` | `0x4BA0` | 715 | UnwindData |  |
| 61 | `FWEnumFirewallRules` | `0x6DA0` | 759 | UnwindData |  |
| 46 | `FWDeleteFirewallRule` | `0x7C10` | 268 | UnwindData |  |
| 183 | `FwIsRemoteManagementEnabled` | `0x9C90` | 1,280 | UnwindData |  |
| 120 | `FWQueryFirewallRules` | `0xAED0` | 326 | UnwindData |  |
| 86 | `FWFreeFirewallRules` | `0xB9F0` | 230 | UnwindData |  |
| 71 | `FWEnumProducts` | `0xCC30` | 272 | UnwindData |  |
| 217 | `IsFirewallInCoExistanceMode` | `0xCF20` | 657 | UnwindData |  |
| 29 | `FWClosePolicyStore` | `0xD1C0` | 1,072 | UnwindData |  |
| 116 | `FWOpenPolicyStore` | `0xD600` | 2,156 | UnwindData |  |
| 103 | `FWGetGlobalConfig` | `0xF380` | 390 | UnwindData |  |
| 104 | `FWGetGlobalConfig2` | `0xF510` | 404 | UnwindData |  |
| 10 | `GetDisabledInterfaces` | `0x119B0` | 695 | UnwindData |  |
| 101 | `FWGetConfig` | `0x11FE0` | 330 | UnwindData |  |
| 102 | `FWGetConfig2` | `0x12130` | 301 | UnwindData |  |
| 218 | `IsPortOrICMPAllowed` | `0x12E40` | 2,413 | UnwindData |  |
| 167 | `FwAnalyzeFirewallPolicy` | `0x16460` | 30 | UnwindData |  |
| 168 | `FwAnalyzeFirewallPolicyOnProfile` | `0x16780` | 585 | UnwindData |  |
| 147 | `FWStatusMessageFromStatusCode` | `0x16E20` | 626 | UnwindData |  |
| 12 | `DllGetClassObject` | `0x171F0` | 378 | UnwindData |  |
| 163 | `FwAlloc` | `0x17370` | 2,864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `FwInterfaceTypesToBstr` | `0x17EA0` | 744 | UnwindData |  |
| 11 | `DllCanUnloadNow` | `0x183A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `FWVerifyFirewallRuleQuery` | `0x183D0` | 84 | UnwindData |  |
| 241 | `NetworkIsolationGetEnterpriseId` | `0x18430` | 119 | UnwindData |  |
| 242 | `NetworkIsolationGetEnterpriseIdAsync` | `0x184B0` | 1,187 | UnwindData |  |
| 243 | `NetworkIsolationGetEnterpriseIdClose` | `0x18960` | 734 | UnwindData |  |
| 26 | `FWChangeNotificationCreate` | `0x1A5C0` | 200 | UnwindData |  |
| 202 | `IcfChangeNotificationCreate` | `0x1A5C0` | 200 | UnwindData |  |
| 232 | `NetworkIsolationDiagnoseConnectFailure` | `0x1A6D0` | 942 | UnwindData |  |
| 73 | `FWFreeAdapters` | `0x1ABF0` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `FWFreeDiagAppList` | `0x1ABF0` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `FWFreeNetworks` | `0x1ABF0` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `FWFreeProducts` | `0x1ABF0` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `FwFree` | `0x1ABF0` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `FWChangeNotificationDestroy` | `0x1ADE0` | 138 | UnwindData |  |
| 203 | `IcfChangeNotificationDestroy` | `0x1ADE0` | 138 | UnwindData |  |
| 246 | `NetworkIsolationSetupAppContainerBinaries` | `0x1BBC0` | 960 | UnwindData |  |
| 126 | `FWResetIndicatedPortInUse` | `0x1C510` | 309 | UnwindData |  |
| 108 | `FWGetIndicatedPortInUse` | `0x1C650` | 1,085 | UnwindData |  |
| 110 | `FWIndicatePortInUse` | `0x1CAA0` | 1,222 | UnwindData |  |
| 221 | `NetworkIsolationCreateAppContainer` | `0x1D020` | 1,191 | UnwindData |  |
| 105 | `FWGetGlobalConfig3` | `0x1D6F0` | 323 | UnwindData |  |
| 1 | `FwBstrToIcmp` | `0x1DC50` | 344 | UnwindData |  |
| 59 | `FWEnumDynamicKeywordAddressesByType0` | `0x1E780` | 245 | UnwindData |  |
| 60 | `FWEnumDynamicKeywordAddresses_Int` | `0x1E880` | 375 | UnwindData |  |
| 7 | `FwIcmpToBstr` | `0x1F150` | 571 | UnwindData |  |
| 201 | `IcfAddrChangeNotificationCreate` | `0x1F3A0` | 206 | UnwindData |  |
| 227 | `NetworkIsolationDeleteAppContainer` | `0x20390` | 794 | UnwindData |  |
| 175 | `FwEmptyWFAddresses` | `0x20720` | 1,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 177 | `FwFreeAddresses` | `0x20720` | 1,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `FWFreeFirewallRulesByHandle` | `0x20CA0` | 249 | UnwindData |  |
| 199 | `FwStringToAddresses` | `0x21170` | 213 | UnwindData |  |
| 182 | `FwIsGroupPolicyEnforced` | `0x21A70` | 1,355 | UnwindData |  |
| 56 | `FWEnumConnectionSecurityRules` | `0x231D0` | 467 | UnwindData |  |
| 118 | `FWQueryConnectionSecurityRules` | `0x23600` | 315 | UnwindData |  |
| 198 | `FwServicesSet` | `0x23880` | 427 | UnwindData |  |
| 127 | `FWResetIndicatedTupleInUse` | `0x23A40` | 303 | UnwindData |  |
| 179 | `FwGetAddressesAsString` | `0x23D00` | 82 | UnwindData |  |
| 6 | `FwGetVersionField` | `0x23EB0` | 627 | UnwindData |  |
| 21 | `FWAddHyperVRule0` | `0x24780` | 267 | UnwindData |  |
| 85 | `FWFreeFirewallRule` | `0x26B00` | 22,896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 205 | `IcfDisconnect` | `0x2C470` | 9,392 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 215 | `IcfOpenDynamicFwPortWithoutSocket` | `0x2C470` | 9,392 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `DllRegisterServer` | `0x2E920` | 173 | UnwindData |  |
| 14 | `DllUnregisterServer` | `0x2E9E0` | 133 | UnwindData |  |
| 2 | `FwBstrToInterfaceTypes` | `0x2FDB0` | 334 | UnwindData |  |
| 3 | `FwBstrToInterfaceTypesCsp` | `0x2FF10` | 410 | UnwindData |  |
| 9 | `FwInterfaceTypesToBstrCsp` | `0x303A0` | 870 | UnwindData |  |
| 5 | `FwGetCurrentProfile` | `0x31B70` | 223 | UnwindData |  |
| 204 | `IcfConnect` | `0x33270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | `IcfFreeDynamicFwPorts` | `0x33290` | 197 | UnwindData |  |
| 207 | `IcfFreeProfile` | `0x33360` | 784 | UnwindData |  |
| 208 | `IcfFreeTickets` | `0x33680` | 148 | UnwindData |  |
| 209 | `IcfGetCurrentProfileType` | `0x33720` | 160 | UnwindData |  |
| 210 | `IcfGetDynamicFwPorts` | `0x337D0` | 855 | UnwindData |  |
| 211 | `IcfGetOperationalMode` | `0x33B30` | 424 | UnwindData |  |
| 212 | `IcfGetProfile` | `0x33CE0` | 865 | UnwindData |  |
| 213 | `IcfGetTickets` | `0x34050` | 788 | UnwindData |  |
| 216 | `IcfSubNetsGetScope` | `0x34370` | 151 | UnwindData |  |
| 162 | `FwActivate` | `0x34750` | 227 | UnwindData |  |
| 165 | `FwAllowedProgramsAdd` | `0x368E0` | 465 | UnwindData |  |
| 166 | `FwAllowedProgramsDelete` | `0x36AC0` | 381 | UnwindData |  |
| 169 | `FwApiHelperFree` | `0x36C50` | 119 | UnwindData |  |
| 170 | `FwApiHelperInit` | `0x36CD0` | 207 | UnwindData |  |
| 180 | `FwIcmpSettingsEnum` | `0x36DB0` | 397 | UnwindData |  |
| 181 | `FwIcmpSettingsSet` | `0x36F50` | 383 | UnwindData |  |
| 184 | `FwLogSettingsSet` | `0x370E0` | 574 | UnwindData |  |
| 186 | `FwMulticastBroadcastResponsesEnum` | `0x37330` | 387 | UnwindData |  |
| 187 | `FwMulticastBroadcastResponsesSet` | `0x374C0` | 377 | UnwindData |  |
| 188 | `FwNotificationsEnum` | `0x37640` | 387 | UnwindData |  |
| 189 | `FwNotificationsSet` | `0x377D0` | 377 | UnwindData |  |
| 190 | `FwOpModesEnum` | `0x37950` | 387 | UnwindData |  |
| 191 | `FwOpModesSet` | `0x37AE0` | 339 | UnwindData |  |
| 192 | `FwPortOpeningsAdd` | `0x37C40` | 502 | UnwindData |  |
| 193 | `FwPortOpeningsDelete` | `0x37E40` | 383 | UnwindData |  |
| 194 | `FwProfileTypeCurrentGet` | `0x37FD0` | 188 | UnwindData |  |
| 195 | `FwProfileTypeGet` | `0x380A0` | 188 | UnwindData |  |
| 196 | `FwRestoreDefaults` | `0x38170` | 130 | UnwindData |  |
| 197 | `FwServicesEnum` | `0x38200` | 477 | UnwindData |  |
| 214 | `IcfIsPortAllowed` | `0x389F0` | 278 | UnwindData |  |
| 15 | `FWAddAuthenticationSet` | `0x50E80` | 394 | UnwindData |  |
| 16 | `FWAddConnectionSecurityRule` | `0x51010` | 399 | UnwindData |  |
| 17 | `FWAddCryptoSet` | `0x511B0` | 364 | UnwindData |  |
| 18 | `FWAddDynamicKeywordAddress0` | `0x51330` | 212 | UnwindData |  |
| 19 | `FWAddDynamicKeywordAddress_Int` | `0x51410` | 296 | UnwindData |  |
| 22 | `FWAddHyperVRule1` | `0x51540` | 267 | UnwindData |  |
| 23 | `FWAddMainModeRule` | `0x51660` | 327 | UnwindData |  |
| 24 | `FWAddSecurityRealm` | `0x517B0` | 531 | UnwindData |  |
| 25 | `FWAuditLogPolicyImported` | `0x519D0` | 502 | UnwindData |  |
| 28 | `FWChangeTransactionalState` | `0x51BD0` | 391 | UnwindData |  |
| 30 | `FWCopyAuthenticationSet` | `0x51D60` | 75 | UnwindData |  |
| 31 | `FWCopyConnectionSecurityRule` | `0x51DC0` | 82 | UnwindData |  |
| 32 | `FWCopyCryptoSet` | `0x51E20` | 82 | UnwindData |  |
| 33 | `FWCopyFirewallRule` | `0x51E80` | 82 | UnwindData |  |
| 34 | `FWCreateHyperVPort0` | `0x51EE0` | 365 | UnwindData |  |
| 35 | `FWCreateHyperVPort1` | `0x52060` | 365 | UnwindData |  |
| 36 | `FWDeleteAllAuthenticationSets` | `0x521E0` | 254 | UnwindData |  |
| 37 | `FWDeleteAllConnectionSecurityRules` | `0x522F0` | 243 | UnwindData |  |
| 38 | `FWDeleteAllCryptoSets` | `0x523F0` | 254 | UnwindData |  |
| 39 | `FWDeleteAllFirewallRules` | `0x52500` | 243 | UnwindData |  |
| 40 | `FWDeleteAllMainModeRules` | `0x52600` | 244 | UnwindData |  |
| 41 | `FWDeleteAuthenticationSet` | `0x52700` | 251 | UnwindData |  |
| 42 | `FWDeleteConnectionSecurityRule` | `0x52810` | 252 | UnwindData |  |
| 43 | `FWDeleteCryptoSet` | `0x52920` | 251 | UnwindData |  |
| 44 | `FWDeleteDynamicKeywordAddress0` | `0x52A30` | 222 | UnwindData |  |
| 45 | `FWDeleteDynamicKeywordAddress_Int` | `0x52B20` | 229 | UnwindData |  |
| 47 | `FWDeleteHyperVPort0` | `0x52C10` | 375 | UnwindData |  |
| 48 | `FWDeleteHyperVRule0` | `0x52D90` | 267 | UnwindData |  |
| 49 | `FWDeleteMainModeRule` | `0x52EB0` | 252 | UnwindData |  |
| 50 | `FWDeletePhase1SAs` | `0x52FC0` | 229 | UnwindData |  |
| 51 | `FWDeletePhase2SAs` | `0x530B0` | 229 | UnwindData |  |
| 52 | `FWDeleteSecurityRealm` | `0x531A0` | 42 | UnwindData |  |
| 53 | `FWDiagGetAppList` | `0x531D0` | 253 | UnwindData |  |
| 54 | `FWEnumAdapters` | `0x532E0` | 262 | UnwindData |  |
| 55 | `FWEnumAuthenticationSets` | `0x533F0` | 426 | UnwindData |  |
| 57 | `FWEnumCryptoSets` | `0x535A0` | 394 | UnwindData |  |
| 58 | `FWEnumDynamicKeywordAddressById0` | `0x53730` | 241 | UnwindData |  |
| 62 | `FWEnumHyperVPorts0` | `0x53830` | 365 | UnwindData |  |
| 63 | `FWEnumHyperVPorts1` | `0x539B0` | 365 | UnwindData |  |
| 64 | `FWEnumHyperVRules0` | `0x53B30` | 298 | UnwindData |  |
| 65 | `FWEnumHyperVRules1` | `0x53C60` | 298 | UnwindData |  |
| 66 | `FWEnumHyperVVMCreators0` | `0x53D90` | 365 | UnwindData |  |
| 67 | `FWEnumMainModeRules` | `0x53F10` | 357 | UnwindData |  |
| 68 | `FWEnumNetworks` | `0x54080` | 262 | UnwindData |  |
| 69 | `FWEnumPhase1SAs` | `0x54190` | 235 | UnwindData |  |
| 70 | `FWEnumPhase2SAs` | `0x54290` | 235 | UnwindData |  |
| 72 | `FWExportPolicy` | `0x54390` | 345 | UnwindData |  |
| 74 | `FWFreeAuthenticationSet` | `0x544F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `FWFreeAuthenticationSets` | `0x54510` | 220 | UnwindData |  |
| 76 | `FWFreeAuthenticationSetsByHandle` | `0x54600` | 247 | UnwindData |  |
| 77 | `FWFreeConnectionSecurityRule` | `0x54700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `FWFreeConnectionSecurityRules` | `0x54720` | 223 | UnwindData |  |
| 79 | `FWFreeConnectionSecurityRulesByHandle` | `0x54810` | 243 | UnwindData |  |
| 80 | `FWFreeCryptoSet` | `0x54910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `FWFreeCryptoSets` | `0x54930` | 223 | UnwindData |  |
| 82 | `FWFreeCryptoSetsByHandle` | `0x54A20` | 300 | UnwindData |  |
| 84 | `FWFreeDynamicKeywordAddressData0` | `0x54B60` | 84 | UnwindData |  |
| 88 | `FWFreeFirewallRulesOld` | `0x54BC0` | 211 | UnwindData |  |
| 89 | `FWFreeHyperVPorts0` | `0x54CA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `FWFreeHyperVPorts1` | `0x54CC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `FWFreeHyperVRules0` | `0x54CE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `FWFreeHyperVRules1` | `0x54D00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `FWFreeHyperVVMCreators0` | `0x54D20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `FWFreeMainModeRule` | `0x54D40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `FWFreeMainModeRules` | `0x54D60` | 223 | UnwindData |  |
| 96 | `FWFreeMainModeRulesByHandle` | `0x54E50` | 247 | UnwindData |  |
| 98 | `FWFreePhase1SAs` | `0x54F50` | 275 | UnwindData |  |
| 99 | `FWFreePhase2SAs` | `0x55070` | 223 | UnwindData |  |
| 106 | `FWGetHyperVProfileConfig0` | `0x55160` | 522 | UnwindData |  |
| 107 | `FWGetHyperVVMConfig0` | `0x55370` | 495 | UnwindData |  |
| 109 | `FWImportPolicy` | `0x55570` | 345 | UnwindData |  |
| 111 | `FWIndicateProxyForUrl` | `0x556D0` | 305 | UnwindData |  |
| 112 | `FWIndicateProxyResolverRefresh` | `0x55810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `FWIndicateTupleInUse` | `0x55820` | 395 | UnwindData |  |
| 114 | `FWIndicateTupleInUse2` | `0x559C0` | 395 | UnwindData |  |
| 115 | `FWIsTargetAProxy` | `0x55B60` | 294 | UnwindData |  |
| 117 | `FWQueryAuthenticationSets` | `0x55DC0` | 319 | UnwindData |  |
| 119 | `FWQueryCryptoSets` | `0x55F10` | 319 | UnwindData |  |
| 121 | `FWQueryIsolationType` | `0x56060` | 325 | UnwindData |  |
| 122 | `FWQueryMainModeRules` | `0x561B0` | 297 | UnwindData |  |
| 123 | `FWRefreshHyperVPorts0` | `0x562E0` | 339 | UnwindData |  |
| 124 | `FWRegisterHyperVVMCreator0` | `0x56440` | 347 | UnwindData |  |
| 125 | `FWRegisterProduct` | `0x565B0` | 426 | UnwindData |  |
| 128 | `FWRestoreDefaults` | `0x56760` | 767 | UnwindData |  |
| 129 | `FWRestoreGPODefaults` | `0x56A70` | 382 | UnwindData |  |
| 130 | `FWRevertTransaction` | `0x56C00` | 279 | UnwindData |  |
| 131 | `FWRuleDuplicateStatusByRuleID` | `0x56D20` | 333 | UnwindData |  |
| 132 | `FWSelectConSecRule` | `0x56E80` | 505 | UnwindData |  |
| 133 | `FWSetAuthenticationSet` | `0x57080` | 392 | UnwindData |  |
| 134 | `FWSetConfig` | `0x57210` | 255 | UnwindData |  |
| 135 | `FWSetConnectionSecurityRule` | `0x57320` | 397 | UnwindData |  |
| 136 | `FWSetCryptoSet` | `0x574C0` | 361 | UnwindData |  |
| 138 | `FWSetGlobalConfig` | `0x57630` | 344 | UnwindData |  |
| 139 | `FWSetGlobalConfig2` | `0x57790` | 341 | UnwindData |  |
| 140 | `FWSetHyperVPort0` | `0x578F0` | 365 | UnwindData |  |
| 141 | `FWSetHyperVPort1` | `0x57A70` | 365 | UnwindData |  |
| 142 | `FWSetHyperVProfileConfig0` | `0x57BF0` | 332 | UnwindData |  |
| 143 | `FWSetHyperVRule0` | `0x57D50` | 267 | UnwindData |  |
| 144 | `FWSetHyperVRule1` | `0x57E70` | 267 | UnwindData |  |
| 145 | `FWSetHyperVVMConfig0` | `0x57F90` | 311 | UnwindData |  |
| 146 | `FWSetMainModeRule` | `0x580D0` | 324 | UnwindData |  |
| 148 | `FWUnregisterHyperVVMCreator0` | `0x58220` | 364 | UnwindData |  |
| 149 | `FWUnregisterProduct` | `0x583A0` | 205 | UnwindData |  |
| 150 | `FWUpdateDynamicKeywordAddress0` | `0x58480` | 237 | UnwindData |  |
| 151 | `FWUpdateDynamicKeywordAddress_Int` | `0x58580` | 271 | UnwindData |  |
| 152 | `FWVerifyAuthenticationSet` | `0x586A0` | 82 | UnwindData |  |
| 153 | `FWVerifyAuthenticationSetQuery` | `0x58700` | 82 | UnwindData |  |
| 154 | `FWVerifyConnectionSecurityRule` | `0x58760` | 82 | UnwindData |  |
| 155 | `FWVerifyConnectionSecurityRuleQuery` | `0x587C0` | 82 | UnwindData |  |
| 156 | `FWVerifyCryptoSet` | `0x58820` | 82 | UnwindData |  |
| 157 | `FWVerifyCryptoSetQuery` | `0x58880` | 82 | UnwindData |  |
| 160 | `FWVerifyMainModeRule` | `0x588E0` | 82 | UnwindData |  |
| 161 | `FWVerifyMainModeRuleQuery` | `0x58940` | 82 | UnwindData |  |
| 164 | `FwAllocCheckSize` | `0x589A0` | 82 | UnwindData |  |
| 171 | `FwConvertIPv6SubNetToRange` | `0x58A00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 172 | `FwCopyAuthSet` | `0x58A20` | 82 | UnwindData |  |
| 173 | `FwCopyMainModeRule` | `0x58A80` | 82 | UnwindData |  |
| 174 | `FwCopyWFAddressesContents` | `0x58AE0` | 82 | UnwindData |  |
| 178 | `FwFreePorts` | `0x58B40` | 45 | UnwindData |  |
| 185 | `FwMergeAddresses` | `0x58B80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 200 | `FwStringToPorts` | `0x58BA0` | 208 | UnwindData |  |
| 219 | `NetworkIsolationAddAllowEnterpriseIdRule` | `0x599A0` | 366 | UnwindData |  |
| 220 | `NetworkIsolationCreateAllInterfacesContainer` | `0x59B20` | 750 | UnwindData |  |
| 222 | `NetworkIsolationCreateAppContainerLoopbackRules` | `0x59E20` | 940 | UnwindData |  |
| 223 | `NetworkIsolationCreateContainer` | `0x5A1E0` | 1,051 | UnwindData |  |
| 224 | `NetworkIsolationCreateInterfaceContainer` | `0x5A610` | 791 | UnwindData |  |
| 225 | `NetworkIsolationDeleteAllInterfacesContainer` | `0x5A930` | 365 | UnwindData |  |
| 226 | `NetworkIsolationDeleteAllowEnterpriseIdRule` | `0x5AAB0` | 246 | UnwindData |  |
| 228 | `NetworkIsolationDeleteAppContainerLoopbackRules` | `0x5ABB0` | 862 | UnwindData |  |
| 229 | `NetworkIsolationDeleteContainer` | `0x5AF20` | 886 | UnwindData |  |
| 230 | `NetworkIsolationDeleteInterfaceContainer` | `0x5B2A0` | 276 | UnwindData |  |
| 231 | `NetworkIsolationDeleteUserAppContainers` | `0x5B3C0` | 403 | UnwindData |  |
| 233 | `NetworkIsolationDiagnoseConnectFailureAndGetInfo` | `0x5B560` | 288 | UnwindData |  |
| 234 | `NetworkIsolationDiagnoseListen` | `0x5B690` | 367 | UnwindData |  |
| 235 | `NetworkIsolationDiagnoseSocketCreation` | `0x5B810` | 359 | UnwindData |  |
| 236 | `NetworkIsolationEnumAppContainers` | `0x5B980` | 425 | UnwindData |  |
| 237 | `NetworkIsolationEnumerateAppContainerRules` | `0x5BB30` | 120 | UnwindData |  |
| 238 | `NetworkIsolationFreeAppContainers` | `0x5BBB0` | 191 | UnwindData |  |
| 239 | `NetworkIsolationGetAppContainer` | `0x5BC80` | 360 | UnwindData |  |
| 240 | `NetworkIsolationGetAppContainerConfig` | `0x5BDF0` | 414 | UnwindData |  |
| 244 | `NetworkIsolationRegisterForAppContainerChanges` | `0x5BFA0` | 1,214 | UnwindData |  |
| 245 | `NetworkIsolationSetAppContainerConfig` | `0x5C470` | 292 | UnwindData |  |
| 247 | `NetworkIsolationUnregisterForAppContainerChanges` | `0x5C5A0` | 737 | UnwindData |  |
