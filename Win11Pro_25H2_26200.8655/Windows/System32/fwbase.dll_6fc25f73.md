# Binary Specification: fwbase.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\fwbase.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6fc25f73f1e642c530afe861abe547415b1f6679b4243445ffd6c5b9722b5b00`
* **Total Exported Functions:** 205

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 53 | `FwGetIcmpSettings` | `0x1280` | 200 | UnwindData |  |
| 63 | `FwGetServices` | `0x1400` | 194 | UnwindData |  |
| 61 | `FwGetService` | `0x15F0` | 41 | UnwindData |  |
| 29 | `FwChangeSourceShutdown` | `0x1620` | 37 | UnwindData |  |
| 125 | `FwRegOpenKey` | `0x1650` | 244 | UnwindData |  |
| 79 | `FwIOWritePortUseIndications` | `0x1750` | 490 | UnwindData |  |
| 59 | `FwGetRpcCallersProcessImageName` | `0x1D20` | 256 | UnwindData |  |
| 104 | `FwLoadString` | `0x1E30` | 470 | UnwindData |  |
| 30 | `FwChangeSourceSignal` | `0x2010` | 102 | UnwindData |  |
| 7 | `FwAddrChangeSourceSignal` | `0x2080` | 92 | UnwindData |  |
| 121 | `FwRegDeleteValue` | `0x20F0` | 300 | UnwindData |  |
| 130 | `FwRegSetDWord` | `0x2230` | 318 | UnwindData |  |
| 44 | `FwExpandEnvironmentStrings` | `0x2470` | 385 | UnwindData |  |
| 52 | `FwGetExpandedCanonicalLongPathName` | `0x2600` | 222 | UnwindData |  |
| 68 | `FwGetTokenInformation` | `0x26F0` | 315 | UnwindData |  |
| 126 | `FwRegQueryDWord` | `0x2840` | 389 | UnwindData |  |
| 131 | `FwRegSetString` | `0x29D0` | 350 | UnwindData |  |
| 117 | `FwRegCloseKey` | `0x2B40` | 40 | UnwindData |  |
| 129 | `FwRegQueryString` | `0x2B70` | 534 | UnwindData |  |
| 103 | `FwLoadIndirectString` | `0x2D90` | 593 | UnwindData |  |
| 85 | `FwIcfDynamicFwPortDestroy` | `0x30F0` | 56 | UnwindData |  |
| 118 | `FwRegCreateKey` | `0x3130` | 240 | UnwindData |  |
| 98 | `FwIsMachineLocalHost` | `0x3230` | 285 | UnwindData |  |
| 138 | `FwResolveIndirectString` | `0x3360` | 152 | UnwindData |  |
| 122 | `FwRegEnumValueNameAndValueData` | `0x3400` | 1,141 | UnwindData |  |
| 54 | `FwGetLongPathName` | `0x3880` | 557 | UnwindData |  |
| 60 | `FwGetRpcCallersProcessInfo` | `0x3AC0` | 21 | UnwindData |  |
| 49 | `FwFreeRpcCallersProcessInfo` | `0x43E0` | 14 | UnwindData |  |
| 22 | `FwBaseFree` | `0x44D0` | 52 | UnwindData |  |
| 47 | `FwFree` | `0x44D0` | 52 | UnwindData |  |
| 8 | `FwAlloc` | `0x4510` | 82 | UnwindData |  |
| 20 | `FwBaseAlloc` | `0x4510` | 82 | UnwindData |  |
| 163 | `FwSubstituteDeviceName` | `0x4830` | 802 | UnwindData |  |
| 137 | `FwReportReturnError` | `0x4B60` | 91 | UnwindData |  |
| 156 | `FwStringCopy` | `0x4BD0` | 61 | UnwindData |  |
| 136 | `FwReportErrorAsWinError` | `0x4D50` | 128 | UnwindData |  |
| 152 | `FwStringBuild` | `0x4DE0` | 622 | UnwindData |  |
| 89 | `FwIcfSubNetsDestroy` | `0x5060` | 37 | UnwindData |  |
| 109 | `FwMetaDataCopy` | `0x50C0` | 340 | UnwindData |  |
| 10 | `FwAllocCheckSize` | `0x5220` | 85 | UnwindData |  |
| 21 | `FwBaseAllocCheckSize` | `0x5220` | 85 | UnwindData |  |
| 11 | `FwArrayAppend` | `0x5280` | 315 | UnwindData |  |
| 26 | `FwChangeSinkCreate` | `0x53D0` | 679 | UnwindData |  |
| 110 | `FwMetaDataFree` | `0x5680` | 55 | UnwindData |  |
| 37 | `FwCriticalSectionCreate` | `0x56C0` | 118 | UnwindData |  |
| 123 | `FwRegNotifyCreate` | `0x5740` | 458 | UnwindData |  |
| 9 | `FwAllocArray` | `0x5910` | 55 | UnwindData |  |
| 3 | `FwPortsToString` | `0x5950` | 1,820 | UnwindData |  |
| 2 | `FwIsValidPorts` | `0x6080` | 181 | UnwindData |  |
| 27 | `FwChangeSinkDestroy` | `0x61E0` | 37 | UnwindData |  |
| 124 | `FwRegNotifyDestroy` | `0x6210` | 89 | UnwindData |  |
| 116 | `FwProfileTypesToString` | `0x6270` | 967 | UnwindData |  |
| 78 | `FwIOReadPortUseIndications` | `0x69F0` | 698 | UnwindData |  |
| 81 | `FwIcfAuthBypassSubNetsDestroy` | `0x6CB0` | 62 | UnwindData |  |
| 15 | `FwArrayDestroy` | `0x6D00` | 136 | UnwindData |  |
| 12 | `FwArrayCat` | `0x6D90` | 35 | UnwindData |  |
| 154 | `FwStringCanonicalizeCopy` | `0x6FB0` | 499 | UnwindData |  |
| 114 | `FwNtStatusToHResult` | `0x71B0` | 131 | UnwindData |  |
| 32 | `FwCloseHandle` | `0x7240` | 45 | UnwindData |  |
| 140 | `FwServiceSidCreateInPlace` | `0x7280` | 245 | UnwindData |  |
| 67 | `FwGetSysPathName` | `0x75E0` | 330 | UnwindData |  |
| 100 | `FwLicensingIsNetIsolationOnly` | `0x7730` | 41 | UnwindData |  |
| 45 | `FwFieldNameMatchStringBegining` | `0xD660` | 160 | UnwindData |  |
| 146 | `FwSizeTMultiply` | `0xD710` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `FwVerifyFirewallRuleQuery` | `0xD8C0` | 480 | UnwindData |  |
| 175 | `FwVerifyFirewallRule` | `0xDF60` | 356 | UnwindData |  |
| 198 | `IsAddressesEmpty` | `0xE390` | 55 | UnwindData |  |
| 204 | `Isv4AddressesEmpty` | `0xE3D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 205 | `Isv6AddressesEmpty` | `0xE3F0` | 3,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | `Int_FWVerifyFirewallRule` | `0xF020` | 58 | UnwindData |  |
| 194 | `Int_FwValidateComplianceAndReduceFirewallRuleToVersion` | `0x111A0` | 51 | UnwindData |  |
| 106 | `FwMarshalledMetaDataCopy` | `0x12320` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `FwUpdateHash` | `0x12450` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `FwRestructureHashtable` | `0x12480` | 152 | UnwindData |  |
| 57 | `FwGetProfileTypeFromProfileIndex` | `0x12520` | 37 | UnwindData |  |
| 197 | `Int_FwValidateSecurityDescriptor` | `0x12550` | 186 | UnwindData |  |
| 190 | `Int_FwValidateAndMigrateSecurityDescriptor` | `0x12610` | 1,329 | UnwindData |  |
| 107 | `FwMarshalledMetaDataInitialize` | `0x12B50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `FwGetProfileIndexFromProfileType` | `0x12B70` | 97 | UnwindData |  |
| 69 | `FwHResultToWindowsError` | `0x12C40` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `FwIpV4SubNetDecode` | `0x12D90` | 364 | UnwindData |  |
| 41 | `FwDWordMultiply` | `0x12F40` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `FwMetaDataIsEnforcementStatePresent` | `0x12F80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 200 | `IsRuleOldAuthApp` | `0x12FB0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `FwSizeTAdd` | `0x12FF0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `FwMetaDataAddEnforcementState` | `0x13070` | 59 | UnwindData |  |
| 25 | `FwCanonizeAuthorizedApps` | `0x130C0` | 198 | UnwindData |  |
| 65 | `FwGetStringId` | `0x13190` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | `IsRuleOldGlobalOpenPort` | `0x131C0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 203 | `IsRuleOpenPortOrAuthApp` | `0x13360` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `FwIcfSubNetsIsEqual` | `0x13490` | 58 | UnwindData |  |
| 102 | `FwLicensingIsXbox` | `0x134D0` | 24 | UnwindData |  |
| 40 | `FwCriticalSectionLeave` | `0x135C0` | 42 | UnwindData |  |
| 39 | `FwCriticalSectionEnter` | `0x135F0` | 42 | UnwindData |  |
| 147 | `FwSortAddresses` | `0x13620` | 108 | UnwindData |  |
| 23 | `FwBoolIsEqual` | `0x136C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `FwIcfIpV4SubNetsCanonize` | `0x136E0` | 133 | UnwindData |  |
| 148 | `FwSortInterfaceLUIDs` | `0x13770` | 57 | UnwindData |  |
| 87 | `FwIcfIpV6SubNetsCanonize` | `0x137B0` | 130 | UnwindData |  |
| 1 | `FwExtractPortNumber` | `0x14080` | 148 | UnwindData |  |
| 38 | `FwCriticalSectionDestroy` | `0x14120` | 38 | UnwindData |  |
| 66 | `FwGetStringIdForStatusCode` | `0x14150` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 189 | `Int_FwIsV6AddrLoopback` | `0x14180` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `FwHashtableInsert` | `0x14200` | 104 | UnwindData |  |
| 95 | `FwInitializeHashContext` | `0x14270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `FwRegQueryNumValues` | `0x14280` | 203 | UnwindData |  |
| 73 | `FwHashtableFind` | `0x14360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 187 | `Int_FwIPV4RangeContainsMulticast` | `0x14380` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `FwSidCreate` | `0x143C0` | 177 | UnwindData |  |
| 55 | `FwGetPolicyAppIdFromSDDLString` | `0x14480` | 169 | UnwindData |  |
| 46 | `FwFinalHash` | `0x14530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `FwIcfAuthBypassServicesDestroy` | `0x14540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `FwTriggerRegisterWait` | `0x14560` | 469 | UnwindData |  |
| 70 | `FwHashtableCreate` | `0x14740` | 61 | UnwindData |  |
| 165 | `FwTriggerRearm` | `0x14810` | 305 | UnwindData |  |
| 72 | `FwHashtableEmpty` | `0x14950` | 199 | UnwindData |  |
| 77 | `FwHashtableRemove` | `0x14A20` | 34 | UnwindData |  |
| 35 | `FwCreateSDDLStringFromPackageFamilyName` | `0x14A50` | 142 | UnwindData |  |
| 93 | `FwImageListHasImage` | `0x14BA0` | 87 | UnwindData |  |
| 180 | `FwWcsICmp` | `0x14C00` | 800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `FwAuthSuiteEmptyByVersion` | `0x14F20` | 154 | UnwindData |  |
| 99 | `FwLicensingIsIoT` | `0x150D0` | 81 | UnwindData |  |
| 50 | `FwGetAppBlockList` | `0x15130` | 59 | UnwindData |  |
| 191 | `Int_FwValidateComplianceAndReduceAuthSetToVersion` | `0x152A0` | 575 | UnwindData |  |
| 144 | `FwSidDestroy` | `0x154F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `FwRegDeleteKey` | `0x15510` | 155 | UnwindData |  |
| 28 | `FwChangeSourceInitialize` | `0x15670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 192 | `Int_FwValidateComplianceAndReduceConnSecRuleToVersion` | `0x15680` | 1,239 | UnwindData |  |
| 164 | `FwTriggerGetEventForSource` | `0x15B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `FwEnableMemTracing` | `0x15B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `FwInitMemoryMgr` | `0x15B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `FwSetMemLeakPolicy` | `0x15B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `FwShutdownMemoryMgr` | `0x15B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `FwVerifyNoHeapLeaks` | `0x15B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `FwAddrChangeSourceInitialize` | `0x15B80` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `FwHashtableDestroy` | `0x15D00` | 222 | UnwindData |  |
| 84 | `FwIcfAuthorizedAppsDestroy` | `0x15EB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `FwImageListDestroy` | `0x15ED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `FwChangeSourceSignalStart` | `0x15EF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 193 | `Int_FwValidateComplianceAndReduceCryptoSetToVersion` | `0x15F10` | 1,116 | UnwindData |  |
| 13 | `FwArrayCopy` | `0x16480` | 824 | UnwindData |  |
| 181 | `Int_FWVerifyAuthenticationSet` | `0x16920` | 1,058 | UnwindData |  |
| 182 | `Int_FWVerifyConnectionSecurityRule` | `0x16D50` | 5,320 | UnwindData |  |
| 183 | `Int_FWVerifyCryptoSet` | `0x18220` | 928 | UnwindData |  |
| 202 | `IsRuleOldv1Compliant` | `0x197F0` | 58 | UnwindData |  |
| 135 | `FwReportErrorAsNtStatus` | `0x19830` | 114 | UnwindData |  |
| 199 | `IsCSRuleTunnelMode` | `0x198B0` | 6,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `FWIndicatePortInUse_Helper` | `0x1B020` | 260 | UnwindData |  |
| 119 | `FwRegDeleteAllValues` | `0x1B130` | 316 | UnwindData |  |
| 127 | `FwRegQueryNumKeys` | `0x1B400` | 197 | UnwindData |  |
| 24 | `FwBuildIndirectString` | `0x1B890` | 126 | UnwindData |  |
| 33 | `FwConstructRemoteMachineSPN` | `0x1B920` | 366 | UnwindData |  |
| 34 | `FwCreateDirectory` | `0x1BAA0` | 357 | UnwindData |  |
| 36 | `FwCreateSDDLStringFromPolicyAppId` | `0x1BC10` | 140 | UnwindData |  |
| 43 | `FwEnablePrivilege` | `0x1BCB0` | 479 | UnwindData |  |
| 105 | `FwLookupAccountSid` | `0x1BF20` | 571 | UnwindData |  |
| 112 | `FwModifySDDLStringWithPolicyAppId` | `0x1C170` | 754 | UnwindData |  |
| 113 | `FwMultiByteToWideChar` | `0x1C470` | 351 | UnwindData |  |
| 132 | `FwReleasePrivilege` | `0x1C760` | 195 | UnwindData |  |
| 133 | `FwRemovePolicyAppIdFromSDDLString` | `0x1C830` | 514 | UnwindData |  |
| 134 | `FwReplacePolicyAppIdInSDDLString` | `0x1CA40` | 297 | UnwindData |  |
| 151 | `FwStringArrayCopy` | `0x1CB70` | 298 | UnwindData |  |
| 153 | `FwStringBuildWithPrefix` | `0x1CCA0` | 409 | UnwindData |  |
| 155 | `FwStringConcat` | `0x1CE40` | 133 | UnwindData |  |
| 157 | `FwStringCopyA` | `0x1CED0` | 234 | UnwindData |  |
| 158 | `FwStringCopyAtoWAlloc` | `0x1CFC0` | 325 | UnwindData |  |
| 159 | `FwStringCopyWtoAAlloc` | `0x1D110` | 342 | UnwindData |  |
| 160 | `FwStringPrefixConcat` | `0x1D270` | 136 | UnwindData |  |
| 161 | `FwStringPrefixCopy` | `0x1D300` | 317 | UnwindData |  |
| 14 | `FwArrayCreateFromRegistry` | `0x265D0` | 526 | UnwindData |  |
| 16 | `FwArrayErase` | `0x267F0` | 172 | UnwindData |  |
| 82 | `FwIcfAuthorizedAppCopy` | `0x270E0` | 313 | UnwindData |  |
| 83 | `FwIcfAuthorizedAppsCopy` | `0x27270` | 147 | UnwindData |  |
| 88 | `FwIcfSubNetsCopy` | `0x27560` | 139 | UnwindData |  |
| 90 | `FwIcfSubNetsGetScope` | `0x27600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `FwHashtableGetNext` | `0x27620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `FwHashtableIsEmpty` | `0x27640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `FwParseEdpCloudResourceStringToNrptRuleList` | `0x27650` | 1,219 | UnwindData |  |
| 101 | `FwLicensingIsVAILContainer` | `0x27B20` | 25,673 | UnwindData |  |
| 167 | `FwTriggerUnregisterWait` | `0x2DFF0` | 258 | UnwindData |  |
| 6 | `FwAddrChangeSourceShutdown` | `0x2E100` | 37 | UnwindData |  |
| 19 | `FwAuthorizedAppEncode` | `0x2E990` | 289 | UnwindData |  |
| 51 | `FwGetAuthorizedApp` | `0x2EAC0` | 231 | UnwindData |  |
| 58 | `FwGetRemoteAdminSettings` | `0x2EBB0` | 70 | UnwindData |  |
| 64 | `FwGetStaticFwPort` | `0x2EC00` | 282 | UnwindData |  |
| 149 | `FwStaticFwPortEncode` | `0x2EE40` | 321 | UnwindData |  |
| 150 | `FwStaticFwPortEncodeValueName` | `0x2EF90` | 160 | UnwindData |  |
| 162 | `FwSubNetsEncode` | `0x2F040` | 352 | UnwindData |  |
| 17 | `FwAuthSuiteEmpty` | `0x2F1B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `FwFreeCertCriteria` | `0x2F1C0` | 100 | UnwindData |  |
| 62 | `FwGetServiceTypes` | `0x2F280` | 252 | UnwindData |  |
| 97 | `FwIsBuiltInPort` | `0x2F390` | 25 | UnwindData |  |
| 169 | `FwVerifyAuthenticationSet` | `0x2F3B0` | 331 | UnwindData |  |
| 170 | `FwVerifyAuthenticationSetQuery` | `0x2F510` | 329 | UnwindData |  |
| 171 | `FwVerifyConnectionSecurityRule` | `0x2F660` | 399 | UnwindData |  |
| 172 | `FwVerifyConnectionSecurityRuleQuery` | `0x2F800` | 329 | UnwindData |  |
| 173 | `FwVerifyCryptoSet` | `0x2F950` | 331 | UnwindData |  |
| 174 | `FwVerifyCryptoSetQuery` | `0x2FAB0` | 329 | UnwindData |  |
| 177 | `FwVerifyMainModeRule` | `0x2FC00` | 295 | UnwindData |  |
| 178 | `FwVerifyMainModeRuleQuery` | `0x2FD30` | 331 | UnwindData |  |
| 185 | `Int_FWVerifyHyperVRule` | `0x31540` | 946 | UnwindData |  |
| 186 | `Int_FWVerifyMainModeRule` | `0x31900` | 1,409 | UnwindData |  |
| 188 | `Int_FwIPV6RangeContainsMulticast` | `0x31F50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 195 | `Int_FwValidateComplianceAndReduceHyperVRuleToVersion` | `0x31F70` | 252 | UnwindData |  |
| 196 | `Int_FwValidateComplianceAndReduceMainModeRuleToVersion` | `0x32080` | 301 | UnwindData |  |
