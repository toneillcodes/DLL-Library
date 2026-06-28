# Binary Specification: fwbase.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\fwbase.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f302585a08c5f599764143536605bf05fb228679c0cc5c123e735192179aa223`
* **Total Exported Functions:** 205

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 53 | `FwGetIcmpSettings` | `0x1270` | 200 | UnwindData |  |
| 63 | `FwGetServices` | `0x13F0` | 194 | UnwindData |  |
| 61 | `FwGetService` | `0x15E0` | 41 | UnwindData |  |
| 29 | `FwChangeSourceShutdown` | `0x1610` | 37 | UnwindData |  |
| 125 | `FwRegOpenKey` | `0x1640` | 244 | UnwindData |  |
| 79 | `FwIOWritePortUseIndications` | `0x1740` | 490 | UnwindData |  |
| 59 | `FwGetRpcCallersProcessImageName` | `0x1D10` | 256 | UnwindData |  |
| 104 | `FwLoadString` | `0x1E20` | 470 | UnwindData |  |
| 30 | `FwChangeSourceSignal` | `0x2000` | 102 | UnwindData |  |
| 7 | `FwAddrChangeSourceSignal` | `0x2070` | 92 | UnwindData |  |
| 121 | `FwRegDeleteValue` | `0x20E0` | 300 | UnwindData |  |
| 130 | `FwRegSetDWord` | `0x2220` | 318 | UnwindData |  |
| 44 | `FwExpandEnvironmentStrings` | `0x2460` | 385 | UnwindData |  |
| 52 | `FwGetExpandedCanonicalLongPathName` | `0x25F0` | 222 | UnwindData |  |
| 68 | `FwGetTokenInformation` | `0x26E0` | 315 | UnwindData |  |
| 126 | `FwRegQueryDWord` | `0x2830` | 389 | UnwindData |  |
| 131 | `FwRegSetString` | `0x29C0` | 350 | UnwindData |  |
| 117 | `FwRegCloseKey` | `0x2B30` | 40 | UnwindData |  |
| 129 | `FwRegQueryString` | `0x2B60` | 534 | UnwindData |  |
| 103 | `FwLoadIndirectString` | `0x2D80` | 593 | UnwindData |  |
| 85 | `FwIcfDynamicFwPortDestroy` | `0x30E0` | 56 | UnwindData |  |
| 118 | `FwRegCreateKey` | `0x3120` | 240 | UnwindData |  |
| 98 | `FwIsMachineLocalHost` | `0x3220` | 285 | UnwindData |  |
| 138 | `FwResolveIndirectString` | `0x3350` | 152 | UnwindData |  |
| 122 | `FwRegEnumValueNameAndValueData` | `0x33F0` | 1,141 | UnwindData |  |
| 54 | `FwGetLongPathName` | `0x3870` | 557 | UnwindData |  |
| 60 | `FwGetRpcCallersProcessInfo` | `0x3AB0` | 21 | UnwindData |  |
| 49 | `FwFreeRpcCallersProcessInfo` | `0x43D0` | 14 | UnwindData |  |
| 22 | `FwBaseFree` | `0x44C0` | 52 | UnwindData |  |
| 47 | `FwFree` | `0x44C0` | 52 | UnwindData |  |
| 8 | `FwAlloc` | `0x4500` | 82 | UnwindData |  |
| 20 | `FwBaseAlloc` | `0x4500` | 82 | UnwindData |  |
| 163 | `FwSubstituteDeviceName` | `0x4820` | 802 | UnwindData |  |
| 137 | `FwReportReturnError` | `0x4B50` | 91 | UnwindData |  |
| 156 | `FwStringCopy` | `0x4BC0` | 61 | UnwindData |  |
| 136 | `FwReportErrorAsWinError` | `0x4D40` | 128 | UnwindData |  |
| 152 | `FwStringBuild` | `0x4DD0` | 622 | UnwindData |  |
| 89 | `FwIcfSubNetsDestroy` | `0x5050` | 37 | UnwindData |  |
| 109 | `FwMetaDataCopy` | `0x50B0` | 340 | UnwindData |  |
| 10 | `FwAllocCheckSize` | `0x5210` | 85 | UnwindData |  |
| 21 | `FwBaseAllocCheckSize` | `0x5210` | 85 | UnwindData |  |
| 11 | `FwArrayAppend` | `0x5270` | 315 | UnwindData |  |
| 26 | `FwChangeSinkCreate` | `0x53C0` | 679 | UnwindData |  |
| 110 | `FwMetaDataFree` | `0x5670` | 55 | UnwindData |  |
| 37 | `FwCriticalSectionCreate` | `0x56B0` | 118 | UnwindData |  |
| 123 | `FwRegNotifyCreate` | `0x5730` | 458 | UnwindData |  |
| 9 | `FwAllocArray` | `0x5900` | 55 | UnwindData |  |
| 3 | `FwPortsToString` | `0x5940` | 1,820 | UnwindData |  |
| 2 | `FwIsValidPorts` | `0x6070` | 181 | UnwindData |  |
| 27 | `FwChangeSinkDestroy` | `0x61D0` | 37 | UnwindData |  |
| 124 | `FwRegNotifyDestroy` | `0x6200` | 89 | UnwindData |  |
| 116 | `FwProfileTypesToString` | `0x6260` | 967 | UnwindData |  |
| 78 | `FwIOReadPortUseIndications` | `0x69E0` | 698 | UnwindData |  |
| 81 | `FwIcfAuthBypassSubNetsDestroy` | `0x6CA0` | 62 | UnwindData |  |
| 15 | `FwArrayDestroy` | `0x6CF0` | 136 | UnwindData |  |
| 12 | `FwArrayCat` | `0x6D80` | 35 | UnwindData |  |
| 154 | `FwStringCanonicalizeCopy` | `0x6FA0` | 499 | UnwindData |  |
| 114 | `FwNtStatusToHResult` | `0x71A0` | 131 | UnwindData |  |
| 32 | `FwCloseHandle` | `0x7230` | 45 | UnwindData |  |
| 140 | `FwServiceSidCreateInPlace` | `0x7270` | 245 | UnwindData |  |
| 67 | `FwGetSysPathName` | `0x75D0` | 330 | UnwindData |  |
| 100 | `FwLicensingIsNetIsolationOnly` | `0x7720` | 41 | UnwindData |  |
| 45 | `FwFieldNameMatchStringBegining` | `0xD650` | 160 | UnwindData |  |
| 146 | `FwSizeTMultiply` | `0xD700` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `FwVerifyFirewallRuleQuery` | `0xD8B0` | 480 | UnwindData |  |
| 175 | `FwVerifyFirewallRule` | `0xDF50` | 356 | UnwindData |  |
| 198 | `IsAddressesEmpty` | `0xE380` | 55 | UnwindData |  |
| 204 | `Isv4AddressesEmpty` | `0xE3C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 205 | `Isv6AddressesEmpty` | `0xE3E0` | 3,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | `Int_FWVerifyFirewallRule` | `0xF010` | 58 | UnwindData |  |
| 194 | `Int_FwValidateComplianceAndReduceFirewallRuleToVersion` | `0x11190` | 51 | UnwindData |  |
| 106 | `FwMarshalledMetaDataCopy` | `0x12310` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `FwUpdateHash` | `0x12440` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `FwRestructureHashtable` | `0x12470` | 152 | UnwindData |  |
| 57 | `FwGetProfileTypeFromProfileIndex` | `0x12510` | 37 | UnwindData |  |
| 197 | `Int_FwValidateSecurityDescriptor` | `0x12540` | 186 | UnwindData |  |
| 190 | `Int_FwValidateAndMigrateSecurityDescriptor` | `0x12600` | 1,329 | UnwindData |  |
| 107 | `FwMarshalledMetaDataInitialize` | `0x12B40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `FwGetProfileIndexFromProfileType` | `0x12B60` | 97 | UnwindData |  |
| 69 | `FwHResultToWindowsError` | `0x12C30` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `FwIpV4SubNetDecode` | `0x12D80` | 364 | UnwindData |  |
| 41 | `FwDWordMultiply` | `0x12F30` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `FwMetaDataIsEnforcementStatePresent` | `0x12F70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 200 | `IsRuleOldAuthApp` | `0x12FA0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `FwSizeTAdd` | `0x12FE0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `FwMetaDataAddEnforcementState` | `0x13060` | 59 | UnwindData |  |
| 25 | `FwCanonizeAuthorizedApps` | `0x130B0` | 198 | UnwindData |  |
| 65 | `FwGetStringId` | `0x13180` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | `IsRuleOldGlobalOpenPort` | `0x131B0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 203 | `IsRuleOpenPortOrAuthApp` | `0x13350` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `FwIcfSubNetsIsEqual` | `0x13480` | 58 | UnwindData |  |
| 102 | `FwLicensingIsXbox` | `0x134C0` | 24 | UnwindData |  |
| 40 | `FwCriticalSectionLeave` | `0x135B0` | 42 | UnwindData |  |
| 39 | `FwCriticalSectionEnter` | `0x135E0` | 42 | UnwindData |  |
| 147 | `FwSortAddresses` | `0x13610` | 108 | UnwindData |  |
| 23 | `FwBoolIsEqual` | `0x136B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `FwIcfIpV4SubNetsCanonize` | `0x136D0` | 133 | UnwindData |  |
| 148 | `FwSortInterfaceLUIDs` | `0x13760` | 57 | UnwindData |  |
| 87 | `FwIcfIpV6SubNetsCanonize` | `0x137A0` | 130 | UnwindData |  |
| 1 | `FwExtractPortNumber` | `0x14070` | 148 | UnwindData |  |
| 38 | `FwCriticalSectionDestroy` | `0x14110` | 38 | UnwindData |  |
| 66 | `FwGetStringIdForStatusCode` | `0x14140` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 189 | `Int_FwIsV6AddrLoopback` | `0x14170` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `FwHashtableInsert` | `0x141F0` | 104 | UnwindData |  |
| 95 | `FwInitializeHashContext` | `0x14260` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `FwRegQueryNumValues` | `0x14270` | 203 | UnwindData |  |
| 73 | `FwHashtableFind` | `0x14350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 187 | `Int_FwIPV4RangeContainsMulticast` | `0x14370` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `FwSidCreate` | `0x143B0` | 177 | UnwindData |  |
| 55 | `FwGetPolicyAppIdFromSDDLString` | `0x14470` | 169 | UnwindData |  |
| 46 | `FwFinalHash` | `0x14520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `FwIcfAuthBypassServicesDestroy` | `0x14530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `FwTriggerRegisterWait` | `0x14550` | 469 | UnwindData |  |
| 70 | `FwHashtableCreate` | `0x14730` | 61 | UnwindData |  |
| 165 | `FwTriggerRearm` | `0x14800` | 305 | UnwindData |  |
| 72 | `FwHashtableEmpty` | `0x14940` | 199 | UnwindData |  |
| 77 | `FwHashtableRemove` | `0x14A10` | 34 | UnwindData |  |
| 35 | `FwCreateSDDLStringFromPackageFamilyName` | `0x14A40` | 142 | UnwindData |  |
| 93 | `FwImageListHasImage` | `0x14B90` | 87 | UnwindData |  |
| 180 | `FwWcsICmp` | `0x14BF0` | 800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `FwAuthSuiteEmptyByVersion` | `0x14F10` | 154 | UnwindData |  |
| 99 | `FwLicensingIsIoT` | `0x150C0` | 81 | UnwindData |  |
| 50 | `FwGetAppBlockList` | `0x15120` | 59 | UnwindData |  |
| 191 | `Int_FwValidateComplianceAndReduceAuthSetToVersion` | `0x15290` | 575 | UnwindData |  |
| 144 | `FwSidDestroy` | `0x154E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `FwRegDeleteKey` | `0x15500` | 155 | UnwindData |  |
| 28 | `FwChangeSourceInitialize` | `0x15660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 192 | `Int_FwValidateComplianceAndReduceConnSecRuleToVersion` | `0x15670` | 1,239 | UnwindData |  |
| 164 | `FwTriggerGetEventForSource` | `0x15B50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `FwEnableMemTracing` | `0x15B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `FwInitMemoryMgr` | `0x15B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `FwSetMemLeakPolicy` | `0x15B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `FwShutdownMemoryMgr` | `0x15B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `FwVerifyNoHeapLeaks` | `0x15B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `FwAddrChangeSourceInitialize` | `0x15B70` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `FwHashtableDestroy` | `0x15CF0` | 222 | UnwindData |  |
| 84 | `FwIcfAuthorizedAppsDestroy` | `0x15EA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `FwImageListDestroy` | `0x15EC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `FwChangeSourceSignalStart` | `0x15EE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 193 | `Int_FwValidateComplianceAndReduceCryptoSetToVersion` | `0x15F00` | 1,116 | UnwindData |  |
| 13 | `FwArrayCopy` | `0x16470` | 824 | UnwindData |  |
| 181 | `Int_FWVerifyAuthenticationSet` | `0x16910` | 1,058 | UnwindData |  |
| 182 | `Int_FWVerifyConnectionSecurityRule` | `0x16D40` | 5,085 | UnwindData |  |
| 183 | `Int_FWVerifyCryptoSet` | `0x18130` | 928 | UnwindData |  |
| 202 | `IsRuleOldv1Compliant` | `0x19700` | 58 | UnwindData |  |
| 135 | `FwReportErrorAsNtStatus` | `0x19740` | 114 | UnwindData |  |
| 199 | `IsCSRuleTunnelMode` | `0x197C0` | 6,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `FWIndicatePortInUse_Helper` | `0x1AF30` | 260 | UnwindData |  |
| 119 | `FwRegDeleteAllValues` | `0x1B040` | 316 | UnwindData |  |
| 127 | `FwRegQueryNumKeys` | `0x1B310` | 197 | UnwindData |  |
| 24 | `FwBuildIndirectString` | `0x1B7A0` | 126 | UnwindData |  |
| 33 | `FwConstructRemoteMachineSPN` | `0x1B830` | 366 | UnwindData |  |
| 34 | `FwCreateDirectory` | `0x1B9B0` | 357 | UnwindData |  |
| 36 | `FwCreateSDDLStringFromPolicyAppId` | `0x1BB20` | 140 | UnwindData |  |
| 43 | `FwEnablePrivilege` | `0x1BBC0` | 479 | UnwindData |  |
| 105 | `FwLookupAccountSid` | `0x1BE30` | 571 | UnwindData |  |
| 112 | `FwModifySDDLStringWithPolicyAppId` | `0x1C080` | 754 | UnwindData |  |
| 113 | `FwMultiByteToWideChar` | `0x1C380` | 351 | UnwindData |  |
| 132 | `FwReleasePrivilege` | `0x1C670` | 195 | UnwindData |  |
| 133 | `FwRemovePolicyAppIdFromSDDLString` | `0x1C740` | 514 | UnwindData |  |
| 134 | `FwReplacePolicyAppIdInSDDLString` | `0x1C950` | 297 | UnwindData |  |
| 151 | `FwStringArrayCopy` | `0x1CA80` | 298 | UnwindData |  |
| 153 | `FwStringBuildWithPrefix` | `0x1CBB0` | 409 | UnwindData |  |
| 155 | `FwStringConcat` | `0x1CD50` | 133 | UnwindData |  |
| 157 | `FwStringCopyA` | `0x1CDE0` | 234 | UnwindData |  |
| 158 | `FwStringCopyAtoWAlloc` | `0x1CED0` | 325 | UnwindData |  |
| 159 | `FwStringCopyWtoAAlloc` | `0x1D020` | 342 | UnwindData |  |
| 160 | `FwStringPrefixConcat` | `0x1D180` | 136 | UnwindData |  |
| 161 | `FwStringPrefixCopy` | `0x1D210` | 317 | UnwindData |  |
| 14 | `FwArrayCreateFromRegistry` | `0x26350` | 526 | UnwindData |  |
| 16 | `FwArrayErase` | `0x26570` | 172 | UnwindData |  |
| 82 | `FwIcfAuthorizedAppCopy` | `0x26E60` | 313 | UnwindData |  |
| 83 | `FwIcfAuthorizedAppsCopy` | `0x26FF0` | 147 | UnwindData |  |
| 88 | `FwIcfSubNetsCopy` | `0x272E0` | 139 | UnwindData |  |
| 90 | `FwIcfSubNetsGetScope` | `0x27380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `FwHashtableGetNext` | `0x273A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `FwHashtableIsEmpty` | `0x273C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `FwParseEdpCloudResourceStringToNrptRuleList` | `0x273D0` | 1,219 | UnwindData |  |
| 101 | `FwLicensingIsVAILContainer` | `0x278A0` | 25,673 | UnwindData |  |
| 167 | `FwTriggerUnregisterWait` | `0x2DD70` | 258 | UnwindData |  |
| 6 | `FwAddrChangeSourceShutdown` | `0x2DE80` | 37 | UnwindData |  |
| 19 | `FwAuthorizedAppEncode` | `0x2E710` | 289 | UnwindData |  |
| 51 | `FwGetAuthorizedApp` | `0x2E840` | 231 | UnwindData |  |
| 58 | `FwGetRemoteAdminSettings` | `0x2E930` | 70 | UnwindData |  |
| 64 | `FwGetStaticFwPort` | `0x2E980` | 282 | UnwindData |  |
| 149 | `FwStaticFwPortEncode` | `0x2EBC0` | 321 | UnwindData |  |
| 150 | `FwStaticFwPortEncodeValueName` | `0x2ED10` | 160 | UnwindData |  |
| 162 | `FwSubNetsEncode` | `0x2EDC0` | 352 | UnwindData |  |
| 17 | `FwAuthSuiteEmpty` | `0x2EF30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `FwFreeCertCriteria` | `0x2EF40` | 100 | UnwindData |  |
| 62 | `FwGetServiceTypes` | `0x2F000` | 252 | UnwindData |  |
| 97 | `FwIsBuiltInPort` | `0x2F110` | 25 | UnwindData |  |
| 169 | `FwVerifyAuthenticationSet` | `0x2F130` | 331 | UnwindData |  |
| 170 | `FwVerifyAuthenticationSetQuery` | `0x2F290` | 329 | UnwindData |  |
| 171 | `FwVerifyConnectionSecurityRule` | `0x2F3E0` | 399 | UnwindData |  |
| 172 | `FwVerifyConnectionSecurityRuleQuery` | `0x2F580` | 329 | UnwindData |  |
| 173 | `FwVerifyCryptoSet` | `0x2F6D0` | 331 | UnwindData |  |
| 174 | `FwVerifyCryptoSetQuery` | `0x2F830` | 329 | UnwindData |  |
| 177 | `FwVerifyMainModeRule` | `0x2F980` | 295 | UnwindData |  |
| 178 | `FwVerifyMainModeRuleQuery` | `0x2FAB0` | 331 | UnwindData |  |
| 185 | `Int_FWVerifyHyperVRule` | `0x30E80` | 946 | UnwindData |  |
| 186 | `Int_FWVerifyMainModeRule` | `0x31240` | 1,409 | UnwindData |  |
| 188 | `Int_FwIPV6RangeContainsMulticast` | `0x31890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 195 | `Int_FwValidateComplianceAndReduceHyperVRuleToVersion` | `0x318B0` | 252 | UnwindData |  |
| 196 | `Int_FwValidateComplianceAndReduceMainModeRuleToVersion` | `0x319C0` | 301 | UnwindData |  |
