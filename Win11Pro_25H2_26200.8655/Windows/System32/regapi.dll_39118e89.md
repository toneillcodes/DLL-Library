# Binary Specification: regapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\regapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `39118e89a5e9a6a3edd1fb94d4e447041250341a0eb1af98fe5a26a4d079b223`
* **Total Exported Functions:** 100

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 29 | `RegGetUserPolicy` | `0x1010` | 449 | UnwindData |  |
| 45 | `RegPdEnumerateW` | `0x1C30` | 122 | UnwindData |  |
| 68 | `RegWdQueryW` | `0x1FB0` | 285 | UnwindData |  |
| 50 | `RegQueryMonitorSettings` | `0x25A0` | 752 | UnwindData |  |
| 26 | `RegGetMachinePolicyNew` | `0x28A0` | 126 | UnwindData |  |
| 86 | `RegWinStationQueryW` | `0x3F10` | 104 | UnwindData |  |
| 35 | `RegMergeMachineAndProtocolPolicy` | `0x47B0` | 465 | UnwindData |  |
| 36 | `RegMergeOnlyMachinePolicy` | `0x4990` | 636 | UnwindData |  |
| 80 | `RegWinStationQueryExW` | `0x5BF0` | 91 | UnwindData |  |
| 3 | `QueryUserConfig` | `0x6DD0` | 5,079 | UnwindData |  |
| 20 | `RegDefaultUserConfigQueryW` | `0x8980` | 242 | UnwindData |  |
| 92 | `RegWinstationQuerySecurityConfig_Machine` | `0x8D50` | 98 | UnwindData |  |
| 93 | `RegWinstationQuerySecurityConfig_Merged` | `0x9160` | 106 | UnwindData |  |
| 47 | `RegPdQueryW` | `0x96E0` | 771 | UnwindData |  |
| 85 | `RegWinStationQueryValueW` | `0x9BF0` | 140 | UnwindData |  |
| 51 | `RegQueryOEMId` | `0x9D30` | 320 | UnwindData |  |
| 75 | `RegWinStationEnumerateW` | `0x9FF0` | 134 | UnwindData |  |
| 66 | `RegWdEnumerateW` | `0xA220` | 141 | UnwindData |  |
| 23 | `RegGetLicensePolicyID` | `0xA7D0` | 48,747 | UnwindData |  |
| 49 | `RegQueryListenerStart` | `0x16710` | 645 | UnwindData |  |
| 53 | `RegQueryUtilityCommandList` | `0x16F10` | 1,003 | UnwindData |  |
| 34 | `RegIsTimeZoneRedirectionEnabled` | `0x17310` | 617 | UnwindData |  |
| 15 | `RegConsoleShadowQueryA` | `0x18860` | 351 | UnwindData |  |
| 16 | `RegConsoleShadowQueryW` | `0x189D0` | 350 | UnwindData |  |
| 17 | `RegCreateMonitorConfigW` | `0x18B40` | 262 | UnwindData |  |
| 18 | `RegCreateUserConfigW` | `0x18C50` | 208 | UnwindData |  |
| 48 | `RegQueryConnectionSettings` | `0x18D30` | 234 | UnwindData |  |
| 52 | `RegQuerySessionSettings` | `0x18E20` | 196 | UnwindData |  |
| 69 | `RegWinStationAccessCheck` | `0x18EF0` | 86 | UnwindData |  |
| 70 | `RegWinStationCreateA` | `0x18F50` | 399 | UnwindData |  |
| 71 | `RegWinStationCreateW` | `0x190F0` | 704 | UnwindData |  |
| 72 | `RegWinStationDeleteA` | `0x193C0` | 112 | UnwindData |  |
| 73 | `RegWinStationDeleteW` | `0x19440` | 230 | UnwindData |  |
| 74 | `RegWinStationEnumerateA` | `0x19530` | 246 | UnwindData |  |
| 76 | `RegWinStationQueryA` | `0x19630` | 410 | UnwindData |  |
| 77 | `RegWinStationQueryDefaultSecurity` | `0x197D0` | 143 | UnwindData |  |
| 78 | `RegWinStationQueryEx` | `0x19870` | 170 | UnwindData |  |
| 79 | `RegWinStationQueryExNew` | `0x19920` | 296 | UnwindData |  |
| 81 | `RegWinStationQueryExtendedSettingsW` | `0x19A50` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `RegWinStationQueryNumValueW` | `0x19A90` | 131 | UnwindData |  |
| 83 | `RegWinStationQuerySecurityA` | `0x19B20` | 158 | UnwindData |  |
| 84 | `RegWinStationQuerySecurityW` | `0x19BD0` | 110 | UnwindData |  |
| 87 | `RegWinStationSetDefaultSecurity` | `0x19C50` | 327 | UnwindData |  |
| 88 | `RegWinStationSetExtendedSettingsW` | `0x19DA0` | 166 | UnwindData |  |
| 89 | `RegWinStationSetNumValueW` | `0x19E50` | 111 | UnwindData |  |
| 90 | `RegWinStationSetSecurityA` | `0x19ED0` | 128 | UnwindData |  |
| 91 | `RegWinStationSetSecurityW` | `0x19F60` | 316 | UnwindData |  |
| 94 | `RegWinstationSetSecurityConfig` | `0x1A0B0` | 352 | UnwindData |  |
| 14 | `RegCloseServer` | `0x1AB20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `RegOpenServerA` | `0x1AB40` | 153 | UnwindData |  |
| 39 | `RegOpenServerW` | `0x1ABE0` | 72 | UnwindData |  |
| 40 | `RegPdCreateA` | `0x1AC30` | 319 | UnwindData |  |
| 41 | `RegPdCreateW` | `0x1AD80` | 583 | UnwindData |  |
| 42 | `RegPdDeleteA` | `0x1AFD0` | 164 | UnwindData |  |
| 43 | `RegPdDeleteW` | `0x1B080` | 377 | UnwindData |  |
| 44 | `RegPdEnumerateA` | `0x1B200` | 351 | UnwindData |  |
| 46 | `RegPdQueryA` | `0x1B370` | 363 | UnwindData |  |
| 61 | `RegWdCreateA` | `0x1B4F0` | 242 | UnwindData |  |
| 62 | `RegWdCreateW` | `0x1B5F0` | 381 | UnwindData |  |
| 63 | `RegWdDeleteA` | `0x1B780` | 112 | UnwindData |  |
| 64 | `RegWdDeleteW` | `0x1B800` | 196 | UnwindData |  |
| 65 | `RegWdEnumerateA` | `0x1B8D0` | 246 | UnwindData |  |
| 67 | `RegWdQueryA` | `0x1B9D0` | 274 | UnwindData |  |
| 6 | `RegCdCreateA` | `0x1BAF0` | 267 | UnwindData |  |
| 7 | `RegCdCreateW` | `0x1BC10` | 485 | UnwindData |  |
| 8 | `RegCdDeleteA` | `0x1BE00` | 161 | UnwindData |  |
| 9 | `RegCdDeleteW` | `0x1BEB0` | 352 | UnwindData |  |
| 10 | `RegCdEnumerateA` | `0x1C020` | 324 | UnwindData |  |
| 11 | `RegCdEnumerateW` | `0x1C170` | 497 | UnwindData |  |
| 12 | `RegCdQueryA` | `0x1C370` | 270 | UnwindData |  |
| 13 | `RegCdQueryW` | `0x1C490` | 398 | UnwindData |  |
| 19 | `RegDefaultUserConfigQueryA` | `0x1C630` | 205 | UnwindData |  |
| 33 | `RegIsTServer` | `0x1C710` | 142 | UnwindData |  |
| 57 | `RegUserConfigDelete` | `0x1C7B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `RegUserConfigRename` | `0x1C7B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `RegUserConfigQuery` | `0x1C7C0` | 166 | UnwindData |  |
| 60 | `RegUserConfigSet` | `0x1C870` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `CheckStringForAsciiConversion` | `0x1C8A0` | 118 | UnwindData |  |
| 28 | `RegGetUserConfigFromUserParameters` | `0x1CCE0` | 169 | UnwindData |  |
| 37 | `RegMergeUserConfigWithUserParameters` | `0x1CD90` | 203 | UnwindData |  |
| 54 | `RegSAMUserConfig` | `0x1CE70` | 1,457 | UnwindData |  |
| 96 | `UsrPropGetString` | `0x1D430` | 516 | UnwindData |  |
| 97 | `UsrPropGetValue` | `0x1D640` | 308 | UnwindData |  |
| 98 | `UsrPropSetString` | `0x1E0F0` | 738 | UnwindData |  |
| 99 | `UsrPropSetValue` | `0x1E3E0` | 359 | UnwindData |  |
| 4 | `QueryUserProperty` | `0x1E650` | 510 | UnwindData |  |
| 95 | `SetUserProperty` | `0x1E8F0` | 1,045 | UnwindData |  |
| 2 | `GetDomainName` | `0x1EE90` | 324 | UnwindData |  |
| 5 | `RegBuildNumberQuery` | `0x207A0` | 230 | UnwindData |  |
| 22 | `RegFreeUtilityCommandList` | `0x20890` | 127 | UnwindData |  |
| 27 | `RegGetTServerVersion` | `0x20920` | 194 | UnwindData |  |
| 55 | `RegSetLicensePolicyID` | `0x209F0` | 48,328 | UnwindData |  |
| 32 | `RegIsSrcAcceptingConnections` | `0x2C6C0` | 848 | UnwindData |  |
| 56 | `RegSetSrcAcceptConnections` | `0x2CA20` | 353 | UnwindData |  |
| 21 | `RegDenyTSConnectionsPolicy` | `0x2D2D0` | 345 | UnwindData |  |
| 24 | `RegGetLicensingModePolicy` | `0x2D430` | 352 | UnwindData |  |
| 25 | `RegGetMachinePolicyEx` | `0x2D5A0` | 620 | UnwindData |  |
| 100 | `WaitForTSConnectionsPolicyChanges` | `0x2D820` | 1,188 | UnwindData |  |
| 30 | `RegIsMachineInHelpMode` | `0x2DDD0` | 57 | UnwindData |  |
| 31 | `RegIsMachinePolicyAllowHelp` | `0x2DE10` | 85 | UnwindData |  |
