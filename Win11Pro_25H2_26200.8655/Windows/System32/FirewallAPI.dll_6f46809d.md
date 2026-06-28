# Binary Specification: FirewallAPI.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\FirewallAPI.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6f46809d88a59336e8ad5b0aae64943919641a4ee99911e8fb449c32cec89c7a`
* **Total Exported Functions:** 247

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `FwBstrToPorts` | `0x1BB0` | 511 | UnwindData |  |
| 158 | `FWVerifyFirewallRule` | `0x20E0` | 84 | UnwindData |  |
| 20 | `FWAddFirewallRule` | `0x45B0` | 706 | UnwindData |  |
| 137 | `FWSetFirewallRule` | `0x4BB0` | 715 | UnwindData |  |
| 61 | `FWEnumFirewallRules` | `0x6DB0` | 759 | UnwindData |  |
| 46 | `FWDeleteFirewallRule` | `0x7C20` | 268 | UnwindData |  |
| 183 | `FwIsRemoteManagementEnabled` | `0x9CA0` | 1,280 | UnwindData |  |
| 120 | `FWQueryFirewallRules` | `0xAEE0` | 326 | UnwindData |  |
| 86 | `FWFreeFirewallRules` | `0xBA00` | 230 | UnwindData |  |
| 71 | `FWEnumProducts` | `0xCC40` | 272 | UnwindData |  |
| 217 | `IsFirewallInCoExistanceMode` | `0xCF30` | 657 | UnwindData |  |
| 29 | `FWClosePolicyStore` | `0xD1D0` | 1,072 | UnwindData |  |
| 116 | `FWOpenPolicyStore` | `0xD610` | 2,156 | UnwindData |  |
| 103 | `FWGetGlobalConfig` | `0xF390` | 390 | UnwindData |  |
| 104 | `FWGetGlobalConfig2` | `0xF520` | 404 | UnwindData |  |
| 10 | `GetDisabledInterfaces` | `0x119C0` | 695 | UnwindData |  |
| 101 | `FWGetConfig` | `0x11FF0` | 330 | UnwindData |  |
| 102 | `FWGetConfig2` | `0x12140` | 301 | UnwindData |  |
| 218 | `IsPortOrICMPAllowed` | `0x12E50` | 2,413 | UnwindData |  |
| 167 | `FwAnalyzeFirewallPolicy` | `0x16470` | 30 | UnwindData |  |
| 168 | `FwAnalyzeFirewallPolicyOnProfile` | `0x16790` | 585 | UnwindData |  |
| 147 | `FWStatusMessageFromStatusCode` | `0x16E30` | 626 | UnwindData |  |
| 12 | `DllGetClassObject` | `0x17200` | 378 | UnwindData |  |
| 163 | `FwAlloc` | `0x17380` | 2,864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `FwInterfaceTypesToBstr` | `0x17EB0` | 744 | UnwindData |  |
| 11 | `DllCanUnloadNow` | `0x183B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `FWVerifyFirewallRuleQuery` | `0x183E0` | 84 | UnwindData |  |
| 241 | `NetworkIsolationGetEnterpriseId` | `0x18440` | 119 | UnwindData |  |
| 242 | `NetworkIsolationGetEnterpriseIdAsync` | `0x184C0` | 1,187 | UnwindData |  |
| 243 | `NetworkIsolationGetEnterpriseIdClose` | `0x18970` | 734 | UnwindData |  |
| 26 | `FWChangeNotificationCreate` | `0x1A480` | 200 | UnwindData |  |
| 202 | `IcfChangeNotificationCreate` | `0x1A480` | 200 | UnwindData |  |
| 232 | `NetworkIsolationDiagnoseConnectFailure` | `0x1A590` | 942 | UnwindData |  |
| 73 | `FWFreeAdapters` | `0x1AB00` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `FWFreeDiagAppList` | `0x1AB00` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `FWFreeNetworks` | `0x1AB00` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `FWFreeProducts` | `0x1AB00` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `FwFree` | `0x1AB00` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `FWChangeNotificationDestroy` | `0x1ACF0` | 138 | UnwindData |  |
| 203 | `IcfChangeNotificationDestroy` | `0x1ACF0` | 138 | UnwindData |  |
| 246 | `NetworkIsolationSetupAppContainerBinaries` | `0x1BAD0` | 960 | UnwindData |  |
| 126 | `FWResetIndicatedPortInUse` | `0x1C420` | 309 | UnwindData |  |
| 108 | `FWGetIndicatedPortInUse` | `0x1C560` | 1,085 | UnwindData |  |
| 110 | `FWIndicatePortInUse` | `0x1C9B0` | 1,222 | UnwindData |  |
| 221 | `NetworkIsolationCreateAppContainer` | `0x1CF30` | 1,191 | UnwindData |  |
| 105 | `FWGetGlobalConfig3` | `0x1D600` | 323 | UnwindData |  |
| 1 | `FwBstrToIcmp` | `0x1DB60` | 344 | UnwindData |  |
| 59 | `FWEnumDynamicKeywordAddressesByType0` | `0x1E690` | 245 | UnwindData |  |
| 60 | `FWEnumDynamicKeywordAddresses_Int` | `0x1E790` | 375 | UnwindData |  |
| 7 | `FwIcmpToBstr` | `0x1F060` | 571 | UnwindData |  |
| 201 | `IcfAddrChangeNotificationCreate` | `0x1F2B0` | 206 | UnwindData |  |
| 227 | `NetworkIsolationDeleteAppContainer` | `0x202A0` | 794 | UnwindData |  |
| 175 | `FwEmptyWFAddresses` | `0x20630` | 1,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 177 | `FwFreeAddresses` | `0x20630` | 1,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `FWFreeFirewallRulesByHandle` | `0x20B40` | 249 | UnwindData |  |
| 199 | `FwStringToAddresses` | `0x21040` | 213 | UnwindData |  |
| 182 | `FwIsGroupPolicyEnforced` | `0x21940` | 1,355 | UnwindData |  |
| 56 | `FWEnumConnectionSecurityRules` | `0x230A0` | 467 | UnwindData |  |
| 118 | `FWQueryConnectionSecurityRules` | `0x234D0` | 315 | UnwindData |  |
| 198 | `FwServicesSet` | `0x23750` | 427 | UnwindData |  |
| 127 | `FWResetIndicatedTupleInUse` | `0x23910` | 303 | UnwindData |  |
| 179 | `FwGetAddressesAsString` | `0x23B10` | 82 | UnwindData |  |
| 6 | `FwGetVersionField` | `0x23CC0` | 627 | UnwindData |  |
| 21 | `FWAddHyperVRule0` | `0x247E0` | 267 | UnwindData |  |
| 85 | `FWFreeFirewallRule` | `0x26A50` | 22,896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 205 | `IcfDisconnect` | `0x2C3C0` | 9,392 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 215 | `IcfOpenDynamicFwPortWithoutSocket` | `0x2C3C0` | 9,392 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `DllRegisterServer` | `0x2E870` | 173 | UnwindData |  |
| 14 | `DllUnregisterServer` | `0x2E930` | 133 | UnwindData |  |
| 2 | `FwBstrToInterfaceTypes` | `0x2FD00` | 334 | UnwindData |  |
| 3 | `FwBstrToInterfaceTypesCsp` | `0x2FE60` | 410 | UnwindData |  |
| 9 | `FwInterfaceTypesToBstrCsp` | `0x302F0` | 870 | UnwindData |  |
| 5 | `FwGetCurrentProfile` | `0x31AC0` | 223 | UnwindData |  |
| 204 | `IcfConnect` | `0x331C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | `IcfFreeDynamicFwPorts` | `0x331E0` | 197 | UnwindData |  |
| 207 | `IcfFreeProfile` | `0x332B0` | 784 | UnwindData |  |
| 208 | `IcfFreeTickets` | `0x335D0` | 148 | UnwindData |  |
| 209 | `IcfGetCurrentProfileType` | `0x33670` | 160 | UnwindData |  |
| 210 | `IcfGetDynamicFwPorts` | `0x33720` | 855 | UnwindData |  |
| 211 | `IcfGetOperationalMode` | `0x33A80` | 424 | UnwindData |  |
| 212 | `IcfGetProfile` | `0x33C30` | 865 | UnwindData |  |
| 213 | `IcfGetTickets` | `0x33FA0` | 788 | UnwindData |  |
| 216 | `IcfSubNetsGetScope` | `0x342C0` | 151 | UnwindData |  |
| 162 | `FwActivate` | `0x346A0` | 227 | UnwindData |  |
| 165 | `FwAllowedProgramsAdd` | `0x36830` | 465 | UnwindData |  |
| 166 | `FwAllowedProgramsDelete` | `0x36A10` | 381 | UnwindData |  |
| 169 | `FwApiHelperFree` | `0x36BA0` | 119 | UnwindData |  |
| 170 | `FwApiHelperInit` | `0x36C20` | 207 | UnwindData |  |
| 180 | `FwIcmpSettingsEnum` | `0x36D00` | 397 | UnwindData |  |
| 181 | `FwIcmpSettingsSet` | `0x36EA0` | 383 | UnwindData |  |
| 184 | `FwLogSettingsSet` | `0x37030` | 574 | UnwindData |  |
| 186 | `FwMulticastBroadcastResponsesEnum` | `0x37280` | 387 | UnwindData |  |
| 187 | `FwMulticastBroadcastResponsesSet` | `0x37410` | 377 | UnwindData |  |
| 188 | `FwNotificationsEnum` | `0x37590` | 387 | UnwindData |  |
| 189 | `FwNotificationsSet` | `0x37720` | 377 | UnwindData |  |
| 190 | `FwOpModesEnum` | `0x378A0` | 387 | UnwindData |  |
| 191 | `FwOpModesSet` | `0x37A30` | 339 | UnwindData |  |
| 192 | `FwPortOpeningsAdd` | `0x37B90` | 502 | UnwindData |  |
| 193 | `FwPortOpeningsDelete` | `0x37D90` | 383 | UnwindData |  |
| 194 | `FwProfileTypeCurrentGet` | `0x37F20` | 188 | UnwindData |  |
| 195 | `FwProfileTypeGet` | `0x37FF0` | 188 | UnwindData |  |
| 196 | `FwRestoreDefaults` | `0x380C0` | 130 | UnwindData |  |
| 197 | `FwServicesEnum` | `0x38150` | 477 | UnwindData |  |
| 214 | `IcfIsPortAllowed` | `0x38940` | 278 | UnwindData |  |
| 15 | `FWAddAuthenticationSet` | `0x4D0E0` | 394 | UnwindData |  |
| 16 | `FWAddConnectionSecurityRule` | `0x4D270` | 399 | UnwindData |  |
| 17 | `FWAddCryptoSet` | `0x4D410` | 364 | UnwindData |  |
| 18 | `FWAddDynamicKeywordAddress0` | `0x4D590` | 212 | UnwindData |  |
| 19 | `FWAddDynamicKeywordAddress_Int` | `0x4D670` | 296 | UnwindData |  |
| 22 | `FWAddHyperVRule1` | `0x4D7A0` | 267 | UnwindData |  |
| 23 | `FWAddMainModeRule` | `0x4D8C0` | 327 | UnwindData |  |
| 24 | `FWAddSecurityRealm` | `0x4DA10` | 531 | UnwindData |  |
| 25 | `FWAuditLogPolicyImported` | `0x4DC30` | 502 | UnwindData |  |
| 28 | `FWChangeTransactionalState` | `0x4DE30` | 391 | UnwindData |  |
| 30 | `FWCopyAuthenticationSet` | `0x4DFC0` | 75 | UnwindData |  |
| 31 | `FWCopyConnectionSecurityRule` | `0x4E020` | 82 | UnwindData |  |
| 32 | `FWCopyCryptoSet` | `0x4E080` | 82 | UnwindData |  |
| 33 | `FWCopyFirewallRule` | `0x4E0E0` | 82 | UnwindData |  |
| 34 | `FWCreateHyperVPort0` | `0x4E140` | 365 | UnwindData |  |
| 35 | `FWCreateHyperVPort1` | `0x4E2C0` | 365 | UnwindData |  |
| 36 | `FWDeleteAllAuthenticationSets` | `0x4E440` | 254 | UnwindData |  |
| 37 | `FWDeleteAllConnectionSecurityRules` | `0x4E550` | 243 | UnwindData |  |
| 38 | `FWDeleteAllCryptoSets` | `0x4E650` | 254 | UnwindData |  |
| 39 | `FWDeleteAllFirewallRules` | `0x4E760` | 243 | UnwindData |  |
| 40 | `FWDeleteAllMainModeRules` | `0x4E860` | 244 | UnwindData |  |
| 41 | `FWDeleteAuthenticationSet` | `0x4E960` | 251 | UnwindData |  |
| 42 | `FWDeleteConnectionSecurityRule` | `0x4EA70` | 252 | UnwindData |  |
| 43 | `FWDeleteCryptoSet` | `0x4EB80` | 251 | UnwindData |  |
| 44 | `FWDeleteDynamicKeywordAddress0` | `0x4EC90` | 222 | UnwindData |  |
| 45 | `FWDeleteDynamicKeywordAddress_Int` | `0x4ED80` | 229 | UnwindData |  |
| 47 | `FWDeleteHyperVPort0` | `0x4EE70` | 375 | UnwindData |  |
| 48 | `FWDeleteHyperVRule0` | `0x4EFF0` | 267 | UnwindData |  |
| 49 | `FWDeleteMainModeRule` | `0x4F110` | 252 | UnwindData |  |
| 50 | `FWDeletePhase1SAs` | `0x4F220` | 229 | UnwindData |  |
| 51 | `FWDeletePhase2SAs` | `0x4F310` | 229 | UnwindData |  |
| 52 | `FWDeleteSecurityRealm` | `0x4F400` | 42 | UnwindData |  |
| 53 | `FWDiagGetAppList` | `0x4F430` | 253 | UnwindData |  |
| 54 | `FWEnumAdapters` | `0x4F540` | 262 | UnwindData |  |
| 55 | `FWEnumAuthenticationSets` | `0x4F650` | 426 | UnwindData |  |
| 57 | `FWEnumCryptoSets` | `0x4F800` | 394 | UnwindData |  |
| 58 | `FWEnumDynamicKeywordAddressById0` | `0x4F990` | 241 | UnwindData |  |
| 62 | `FWEnumHyperVPorts0` | `0x4FA90` | 365 | UnwindData |  |
| 63 | `FWEnumHyperVPorts1` | `0x4FC10` | 365 | UnwindData |  |
| 64 | `FWEnumHyperVRules0` | `0x4FD90` | 298 | UnwindData |  |
| 65 | `FWEnumHyperVRules1` | `0x4FEC0` | 298 | UnwindData |  |
| 66 | `FWEnumHyperVVMCreators0` | `0x4FFF0` | 365 | UnwindData |  |
| 67 | `FWEnumMainModeRules` | `0x50170` | 357 | UnwindData |  |
| 68 | `FWEnumNetworks` | `0x502E0` | 262 | UnwindData |  |
| 69 | `FWEnumPhase1SAs` | `0x503F0` | 235 | UnwindData |  |
| 70 | `FWEnumPhase2SAs` | `0x504F0` | 235 | UnwindData |  |
| 72 | `FWExportPolicy` | `0x505F0` | 345 | UnwindData |  |
| 74 | `FWFreeAuthenticationSet` | `0x50750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `FWFreeAuthenticationSets` | `0x50770` | 220 | UnwindData |  |
| 76 | `FWFreeAuthenticationSetsByHandle` | `0x50860` | 247 | UnwindData |  |
| 77 | `FWFreeConnectionSecurityRule` | `0x50960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `FWFreeConnectionSecurityRules` | `0x50980` | 223 | UnwindData |  |
| 79 | `FWFreeConnectionSecurityRulesByHandle` | `0x50A70` | 243 | UnwindData |  |
| 80 | `FWFreeCryptoSet` | `0x50B70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `FWFreeCryptoSets` | `0x50B90` | 223 | UnwindData |  |
| 82 | `FWFreeCryptoSetsByHandle` | `0x50C80` | 300 | UnwindData |  |
| 84 | `FWFreeDynamicKeywordAddressData0` | `0x50DC0` | 84 | UnwindData |  |
| 88 | `FWFreeFirewallRulesOld` | `0x50E20` | 211 | UnwindData |  |
| 89 | `FWFreeHyperVPorts0` | `0x50F00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `FWFreeHyperVPorts1` | `0x50F20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `FWFreeHyperVRules0` | `0x50F40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `FWFreeHyperVRules1` | `0x50F60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `FWFreeHyperVVMCreators0` | `0x50F80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `FWFreeMainModeRule` | `0x50FA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `FWFreeMainModeRules` | `0x50FC0` | 223 | UnwindData |  |
| 96 | `FWFreeMainModeRulesByHandle` | `0x510B0` | 247 | UnwindData |  |
| 98 | `FWFreePhase1SAs` | `0x511B0` | 275 | UnwindData |  |
| 99 | `FWFreePhase2SAs` | `0x512D0` | 223 | UnwindData |  |
| 106 | `FWGetHyperVProfileConfig0` | `0x513C0` | 522 | UnwindData |  |
| 107 | `FWGetHyperVVMConfig0` | `0x515D0` | 495 | UnwindData |  |
| 109 | `FWImportPolicy` | `0x517D0` | 345 | UnwindData |  |
| 111 | `FWIndicateProxyForUrl` | `0x51930` | 305 | UnwindData |  |
| 112 | `FWIndicateProxyResolverRefresh` | `0x51A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `FWIndicateTupleInUse` | `0x51A80` | 395 | UnwindData |  |
| 114 | `FWIndicateTupleInUse2` | `0x51C20` | 395 | UnwindData |  |
| 115 | `FWIsTargetAProxy` | `0x51DC0` | 294 | UnwindData |  |
| 117 | `FWQueryAuthenticationSets` | `0x52020` | 319 | UnwindData |  |
| 119 | `FWQueryCryptoSets` | `0x52170` | 319 | UnwindData |  |
| 121 | `FWQueryIsolationType` | `0x522C0` | 325 | UnwindData |  |
| 122 | `FWQueryMainModeRules` | `0x52410` | 297 | UnwindData |  |
| 123 | `FWRefreshHyperVPorts0` | `0x52540` | 339 | UnwindData |  |
| 124 | `FWRegisterHyperVVMCreator0` | `0x526A0` | 347 | UnwindData |  |
| 125 | `FWRegisterProduct` | `0x52810` | 426 | UnwindData |  |
| 128 | `FWRestoreDefaults` | `0x529C0` | 767 | UnwindData |  |
| 129 | `FWRestoreGPODefaults` | `0x52CD0` | 382 | UnwindData |  |
| 130 | `FWRevertTransaction` | `0x52E60` | 279 | UnwindData |  |
| 131 | `FWRuleDuplicateStatusByRuleID` | `0x52F80` | 333 | UnwindData |  |
| 132 | `FWSelectConSecRule` | `0x530E0` | 505 | UnwindData |  |
| 133 | `FWSetAuthenticationSet` | `0x532E0` | 392 | UnwindData |  |
| 134 | `FWSetConfig` | `0x53470` | 255 | UnwindData |  |
| 135 | `FWSetConnectionSecurityRule` | `0x53580` | 397 | UnwindData |  |
| 136 | `FWSetCryptoSet` | `0x53720` | 361 | UnwindData |  |
| 138 | `FWSetGlobalConfig` | `0x53890` | 344 | UnwindData |  |
| 139 | `FWSetGlobalConfig2` | `0x539F0` | 341 | UnwindData |  |
| 140 | `FWSetHyperVPort0` | `0x53B50` | 365 | UnwindData |  |
| 141 | `FWSetHyperVPort1` | `0x53CD0` | 365 | UnwindData |  |
| 142 | `FWSetHyperVProfileConfig0` | `0x53E50` | 332 | UnwindData |  |
| 143 | `FWSetHyperVRule0` | `0x53FB0` | 267 | UnwindData |  |
| 144 | `FWSetHyperVRule1` | `0x540D0` | 267 | UnwindData |  |
| 145 | `FWSetHyperVVMConfig0` | `0x541F0` | 311 | UnwindData |  |
| 146 | `FWSetMainModeRule` | `0x54330` | 324 | UnwindData |  |
| 148 | `FWUnregisterHyperVVMCreator0` | `0x54480` | 364 | UnwindData |  |
| 149 | `FWUnregisterProduct` | `0x54600` | 205 | UnwindData |  |
| 150 | `FWUpdateDynamicKeywordAddress0` | `0x546E0` | 237 | UnwindData |  |
| 151 | `FWUpdateDynamicKeywordAddress_Int` | `0x547E0` | 271 | UnwindData |  |
| 152 | `FWVerifyAuthenticationSet` | `0x54900` | 82 | UnwindData |  |
| 153 | `FWVerifyAuthenticationSetQuery` | `0x54960` | 82 | UnwindData |  |
| 154 | `FWVerifyConnectionSecurityRule` | `0x549C0` | 82 | UnwindData |  |
| 155 | `FWVerifyConnectionSecurityRuleQuery` | `0x54A20` | 82 | UnwindData |  |
| 156 | `FWVerifyCryptoSet` | `0x54A80` | 82 | UnwindData |  |
| 157 | `FWVerifyCryptoSetQuery` | `0x54AE0` | 82 | UnwindData |  |
| 160 | `FWVerifyMainModeRule` | `0x54B40` | 82 | UnwindData |  |
| 161 | `FWVerifyMainModeRuleQuery` | `0x54BA0` | 82 | UnwindData |  |
| 164 | `FwAllocCheckSize` | `0x54C00` | 82 | UnwindData |  |
| 171 | `FwConvertIPv6SubNetToRange` | `0x54C60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 172 | `FwCopyAuthSet` | `0x54C80` | 82 | UnwindData |  |
| 173 | `FwCopyMainModeRule` | `0x54CE0` | 82 | UnwindData |  |
| 174 | `FwCopyWFAddressesContents` | `0x54D40` | 82 | UnwindData |  |
| 178 | `FwFreePorts` | `0x54DA0` | 45 | UnwindData |  |
| 185 | `FwMergeAddresses` | `0x54DE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 200 | `FwStringToPorts` | `0x54E00` | 208 | UnwindData |  |
| 219 | `NetworkIsolationAddAllowEnterpriseIdRule` | `0x55C00` | 366 | UnwindData |  |
| 220 | `NetworkIsolationCreateAllInterfacesContainer` | `0x55D80` | 750 | UnwindData |  |
| 222 | `NetworkIsolationCreateAppContainerLoopbackRules` | `0x56080` | 940 | UnwindData |  |
| 223 | `NetworkIsolationCreateContainer` | `0x56440` | 1,051 | UnwindData |  |
| 224 | `NetworkIsolationCreateInterfaceContainer` | `0x56870` | 791 | UnwindData |  |
| 225 | `NetworkIsolationDeleteAllInterfacesContainer` | `0x56B90` | 365 | UnwindData |  |
| 226 | `NetworkIsolationDeleteAllowEnterpriseIdRule` | `0x56D10` | 246 | UnwindData |  |
| 228 | `NetworkIsolationDeleteAppContainerLoopbackRules` | `0x56E10` | 862 | UnwindData |  |
| 229 | `NetworkIsolationDeleteContainer` | `0x57180` | 886 | UnwindData |  |
| 230 | `NetworkIsolationDeleteInterfaceContainer` | `0x57500` | 276 | UnwindData |  |
| 231 | `NetworkIsolationDeleteUserAppContainers` | `0x57620` | 403 | UnwindData |  |
| 233 | `NetworkIsolationDiagnoseConnectFailureAndGetInfo` | `0x577C0` | 288 | UnwindData |  |
| 234 | `NetworkIsolationDiagnoseListen` | `0x578F0` | 367 | UnwindData |  |
| 235 | `NetworkIsolationDiagnoseSocketCreation` | `0x57A70` | 359 | UnwindData |  |
| 236 | `NetworkIsolationEnumAppContainers` | `0x57BE0` | 425 | UnwindData |  |
| 237 | `NetworkIsolationEnumerateAppContainerRules` | `0x57D90` | 120 | UnwindData |  |
| 238 | `NetworkIsolationFreeAppContainers` | `0x57E10` | 191 | UnwindData |  |
| 239 | `NetworkIsolationGetAppContainer` | `0x57EE0` | 360 | UnwindData |  |
| 240 | `NetworkIsolationGetAppContainerConfig` | `0x58050` | 414 | UnwindData |  |
| 244 | `NetworkIsolationRegisterForAppContainerChanges` | `0x58200` | 1,214 | UnwindData |  |
| 245 | `NetworkIsolationSetAppContainerConfig` | `0x586D0` | 292 | UnwindData |  |
| 247 | `NetworkIsolationUnregisterForAppContainerChanges` | `0x58800` | 737 | UnwindData |  |
