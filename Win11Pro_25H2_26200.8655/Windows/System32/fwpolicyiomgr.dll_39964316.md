# Binary Specification: fwpolicyiomgr.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\fwpolicyiomgr.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `39964316ac42e7392a1f0a439e19b3a7ec277f487c3e843c862d18392f5c8fc3`
* **Total Exported Functions:** 178

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `CreateDefaultAuthAppRule` | `0x18F0` | 151 | UnwindData |  |
| 49 | `FwConvertFwRuleToHyperVRule` | `0x1990` | 1,160 | UnwindData |  |
| 5 | `CreateDefaultIcmpRule` | `0x1E20` | 263 | UnwindData |  |
| 57 | `FwCopyHyperVRule` | `0x1F30` | 812 | UnwindData |  |
| 100 | `FwFreeRules` | `0x2270` | 27 | UnwindData |  |
| 97 | `FwFreeHyperVRulesBySchemaVersion` | `0x27E0` | 80 | UnwindData |  |
| 152 | `FwUniteWFAddressesContents` | `0x2900` | 482 | UnwindData |  |
| 10 | `CreateDefaultRule` | `0x2AF0` | 540 | UnwindData |  |
| 67 | `FwCopyRule` | `0x2D20` | 3,442 | UnwindData |  |
| 102 | `FwFreeWFRule` | `0x3AA0` | 18 | UnwindData |  |
| 130 | `FwPolioCopyWFAddressesContents` | `0x3E10` | 422 | UnwindData |  |
| 131 | `FwPolioEmptyWFAddresses` | `0x3FC0` | 13 | UnwindData |  |
| 41 | `FwCSRuleEmptyByBinaryVersion` | `0x4050` | 416 | UnwindData |  |
| 54 | `FwCopyCSRule` | `0x4200` | 1,854 | UnwindData |  |
| 98 | `FwFreeHyperVVMCreatorsBySchemaVersion` | `0x4950` | 100 | UnwindData |  |
| 89 | `FwEnumHyperVVMCreatorsFromRegistry` | `0x49C0` | 188 | UnwindData |  |
| 110 | `FwGetRule` | `0x5640` | 261 | UnwindData |  |
| 103 | `FwGetConfig` | `0x6860` | 629 | UnwindData |  |
| 46 | `FwClosePolicyStore` | `0x6AE0` | 102 | UnwindData |  |
| 105 | `FwGetGlobalConfig` | `0x6EB0` | 987 | UnwindData |  |
| 37 | `FwAreAllContainedInAddresses` | `0x83B0` | 81 | UnwindData |  |
| 31 | `FwAddRule` | `0x86F0` | 445 | UnwindData |  |
| 77 | `FwDeleteRule` | `0x88C0` | 310 | UnwindData |  |
| 144 | `FwSetRule` | `0x8DE0` | 583 | UnwindData |  |
| 86 | `FwEncodeSyntacticallyImportantFields` | `0x9210` | 116 | UnwindData |  |
| 138 | `FwSetConfig` | `0x9AD0` | 448 | UnwindData |  |
| 140 | `FwSetGlobalConfigInLocalTempStore` | `0x9CA0` | 220 | UnwindData |  |
| 11 | `FwParseAllPortVersions` | `0xA250` | 172 | UnwindData |  |
| 84 | `FwEmptyWFRule` | `0xA7C0` | 14 | UnwindData |  |
| 39 | `FwBinariesFree` | `0xAB20` | 85 | UnwindData |  |
| 159 | `GetOpenPortorAuthAppAsBSTR` | `0xBA90` | 182 | UnwindData |  |
| 158 | `GetOpenPortorAuthAppAddrAsString` | `0xBB50` | 464 | UnwindData |  |
| 172 | `OpenPortOrAuthAppAddrToStringInt2` | `0xBD30` | 43 | UnwindData |  |
| 173 | `OpenPortOrAuthAppAddrToStringInt3` | `0xBD70` | 3,373 | UnwindData |  |
| 59 | `FwCopyICMPTypeCode` | `0x125D0` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `FwCopyPlatform` | `0x125D0` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `FwCopyPortRange` | `0x125D0` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `FwVerifyWFRuleSemantics` | `0x127C0` | 51 | UnwindData |  |
| 150 | `FwStringToSids` | `0x12810` | 552 | UnwindData |  |
| 148 | `FwSidCopy` | `0x13290` | 167 | UnwindData |  |
| 23 | `FWInitExtensionDllCriticalSection` | `0x14160` | 98 | UnwindData |  |
| 18 | `FWDestroyExtensionDllCriticalSection` | `0x143B0` | 80 | UnwindData |  |
| 13 | `FwParseInterfaceType` | `0x14960` | 140 | UnwindData |  |
| 17 | `CalculateOpenPortOrAuthAppAddrStringSize2` | `0x14A00` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | `FwSubtractAddresses` | `0x14B20` | 311 | UnwindData |  |
| 16 | `CalculateOpenPortOrAuthAppAddrStringSize` | `0x15290` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `FwPolioMergeAddresses` | `0x15360` | 77 | UnwindData |  |
| 147 | `FwSidAndAttributesFree` | `0x15470` | 86 | UnwindData |  |
| 12 | `FwParseICMPTypeCodes` | `0x154F0` | 379 | UnwindData |  |
| 167 | `IsUnicastExplicitAddressesEmpty` | `0x157C0` | 99 | UnwindData |  |
| 19 | `FWGPLock` | `0x15900` | 81 | UnwindData |  |
| 22 | `FWGPUnlockEx` | `0x15960` | 104 | UnwindData |  |
| 62 | `FwCopyLUID` | `0x168B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `FwNegateAddresses` | `0x168D0` | 48 | UnwindData |  |
| 55 | `FwCopyCryptoSet` | `0x16B70` | 935 | UnwindData |  |
| 101 | `FwFreeSets` | `0x16F80` | 106 | UnwindData |  |
| 71 | `FwCryptoSetFree` | `0x16FF0` | 34 | UnwindData |  |
| 135 | `FwRemoveDuplicateAddresses` | `0x17370` | 32 | UnwindData |  |
| 160 | `IsEqualAddresses` | `0x175F0` | 204 | UnwindData |  |
| 1 | `CopyIcmpSettings` | `0x17770` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `FwPolioCopyAuthSet` | `0x17870` | 715 | UnwindData |  |
| 91 | `FwEnumSets` | `0x18010` | 919 | UnwindData |  |
| 2 | `CopyIcmpV4Rules` | `0x18810` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `FwOpenAppCDbPolicyStore` | `0x18900` | 449 | UnwindData |  |
| 177 | `StringToOpenPortOrAuthAppAddress2` | `0x18CE0` | 465 | UnwindData |  |
| 3 | `CopyIcmpV6Rules` | `0x18EF0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `Isv4Orv6AddressesEmpty` | `0x18FC0` | 3,984 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `FwConvertIPv6SubNetToRange` | `0x19F50` | 168 | UnwindData |  |
| 128 | `FwPolioConvertIPv6SubNetToRange` | `0x19F50` | 168 | UnwindData |  |
| 87 | `FwEncodeSyntacticallyImportantFieldsInt` | `0x1A000` | 1,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `FwAdvPolicyEncodeRule` | `0x1A540` | 1,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `FwIsV6AddrLoopback` | `0x1AA50` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 162 | `IsFwRuleHyperVApplicable` | `0x1AAA0` | 432 | UnwindData |  |
| 80 | `FwDoNothingOnObject` | `0x1ACF0` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `FwSidsToString` | `0x1AF30` | 627 | UnwindData |  |
| 174 | `SanitizeForPrivacy` | `0x1B540` | 112 | UnwindData |  |
| 88 | `FwEnumAllDynamicKeywordAddressesInRegistry` | `0x1B630` | 280 | UnwindData |  |
| 27 | `FWSetGPHelperFnPtrs` | `0x1B790` | 223 | UnwindData |  |
| 90 | `FwEnumRules` | `0x1B8A0` | 635 | UnwindData |  |
| 176 | `StringToOpenPortOrAuthAppAddress` | `0x1BBD0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `FwIPV4RangeContainsMulticast` | `0x1BC40` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `FwHyperVRuleVerify` | `0x1BD50` | 111 | UnwindData |  |
| 82 | `FwDownlevelFirewallRuleEmpty` | `0x1C0F0` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `FwFindMatchingOpenPortRule` | `0x1C370` | 162 | UnwindData |  |
| 126 | `FwOpenPolicyStore` | `0x1D9A0` | 1,658 | UnwindData |  |
| 136 | `FwRuleResolveFlags` | `0x1E020` | 1,749 | UnwindData |  |
| 119 | `FwMMRuleFree` | `0x1F5E0` | 141 | UnwindData |  |
| 38 | `FwAuthSetFree` | `0x1F760` | 34 | UnwindData |  |
| 42 | `FwCSRuleFree` | `0x1FBB0` | 146 | UnwindData |  |
| 114 | `FwICFProtocolToWfProtocol` | `0x1FFB0` | 52 | UnwindData |  |
| 116 | `FwIPV6RangeContainsMulticast` | `0x20180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `FwFreeDynamicKeywordAddressesInternal` | `0x201A0` | 91 | UnwindData |  |
| 25 | `FWPrimitivesSetGPHelperFnPtrs` | `0x202A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `FwCSRuleEmpty` | `0x202C0` | 6,592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `GetRemoteAdminSettings` | `0x21C80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `CreateDefaultOpenPortRule` | `0x21CA0` | 241 | UnwindData |  |
| 7 | `CreateDefaultPerInterfaceIcmpRule` | `0x21DA0` | 486 | UnwindData |  |
| 8 | `CreateDefaultPerInterfaceOpenPortRule` | `0x21F90` | 220 | UnwindData |  |
| 9 | `CreateDefaultRemoteAdminRule` | `0x22080` | 872 | UnwindData |  |
| 28 | `FreeAbsoluteInterfaces` | `0x22780` | 50 | UnwindData |  |
| 36 | `FwAppContainerChangeFree` | `0x227C0` | 146 | UnwindData |  |
| 43 | `FwCSRuleVerify` | `0x22860` | 49 | UnwindData |  |
| 44 | `FwChkBuildSidAndAttributesFree` | `0x228A0` | 149 | UnwindData |  |
| 45 | `FwCleanupPhase1Sa` | `0x22940` | 70 | UnwindData |  |
| 47 | `FwCompareCSRule` | `0x22990` | 1,023 | UnwindData |  |
| 48 | `FwCompareFWRule` | `0x22DA0` | 1,340 | UnwindData |  |
| 51 | `FwCopyAuthSetListToLowerVersion` | `0x232F0` | 265 | UnwindData |  |
| 52 | `FwCopyAuthSetToLowerVersion` | `0x23400` | 850 | UnwindData |  |
| 53 | `FwCopyAuthsetToHigherVersion` | `0x23760` | 710 | UnwindData |  |
| 56 | `FwCopyHyperVPort` | `0x23A30` | 449 | UnwindData |  |
| 58 | `FwCopyHyperVVMCreator` | `0x23C00` | 255 | UnwindData |  |
| 60 | `FwCopyInterfaceIndexes` | `0x23D10` | 214 | UnwindData |  |
| 61 | `FwCopyInterfaceLuids` | `0x23DF0` | 214 | UnwindData |  |
| 63 | `FwCopyMMRule` | `0x23ED0` | 979 | UnwindData |  |
| 66 | `FwCopyPortsContents` | `0x242B0` | 120 | UnwindData |  |
| 68 | `FwCountAuthAppRules` | `0x24330` | 97 | UnwindData |  |
| 69 | `FwCountGlobalOpenPortRules` | `0x243A0` | 97 | UnwindData |  |
| 81 | `FwDownlevelAuthSetFree` | `0x24410` | 40 | UnwindData |  |
| 83 | `FwDynamicKeywordAddressIsStringValid` | `0x24440` | 63 | UnwindData |  |
| 94 | `FwFreeDynamicKeywordAddressDataBySchemaVersion` | `0x244A0` | 109 | UnwindData |  |
| 96 | `FwFreeHyperVPortsBySchemaVersion` | `0x24520` | 141 | UnwindData |  |
| 99 | `FwFreeObjects` | `0x245C0` | 68 | UnwindData |  |
| 113 | `FwICFProfileToWfProfile` | `0x24610` | 57 | UnwindData |  |
| 117 | `FwInvertAddresses` | `0x24650` | 139 | UnwindData |  |
| 120 | `FwMMRuleVerify` | `0x246F0` | 49 | UnwindData |  |
| 121 | `FwMigrateLegacyAuthenticatedBypassSddl` | `0x24730` | 39 | UnwindData |  |
| 127 | `FwParseAddressToken` | `0x24760` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `FwReduceHyperVRulesToVersion` | `0x247C0` | 187 | UnwindData |  |
| 134 | `FwReduceObjectsToVersion` | `0x24890` | 1,610 | UnwindData |  |
| 137 | `FwSddlStringVerify` | `0x24EE0` | 36 | UnwindData |  |
| 146 | `FwSidAndAttributesCopy` | `0x24F10` | 346 | UnwindData |  |
| 156 | `FwWfProtocolToICFProtocol` | `0x25070` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `GetOpenPortOrAuthAppAddrScope` | `0x250A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 161 | `IsEqualFwPorts` | `0x250E0` | 81 | UnwindData |  |
| 163 | `IsPortsEmpty` | `0x251B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 165 | `IsRulePerInterfaceIcmp` | `0x251D0` | 59 | UnwindData |  |
| 166 | `IsRulePerInterfaceOpenPort` | `0x25220` | 75 | UnwindData |  |
| 170 | `MakeAbsoluteInterfaces` | `0x25350` | 261 | UnwindData |  |
| 171 | `OpenPortOrAuthAppAddrToString` | `0x25460` | 45 | UnwindData |  |
| 175 | `StringArrayToOpenPortOrAuthAppAddress` | `0x25500` | 419 | UnwindData |  |
| 178 | `ValidatePortOrAppAddressString` | `0x256B0` | 194 | UnwindData |  |
| 14 | `FwParseInterfaceTypeCsp` | `0x28680` | 98 | UnwindData |  |
| 26 | `FWResolveGPONames` | `0x2C340` | 83 | UnwindData |  |
| 169 | `LoadGPExtensionDll` | `0x2C3A0` | 397 | UnwindData |  |
| 20 | `FWGPOCleanup` | `0x2C540` | 22 | UnwindData |  |
| 21 | `FWGPOSave` | `0x2C560` | 32 | UnwindData |  |
| 24 | `FWOpenGPOAndGetRegKey` | `0x2C590` | 55 | UnwindData |  |
| 29 | `FwAddDynamicKeywordAddressInRegistry` | `0x31480` | 479 | UnwindData |  |
| 30 | `FwAddHyperVVMCreatorToRegistry` | `0x31670` | 518 | UnwindData |  |
| 32 | `FwAddSet` | `0x31880` | 321 | UnwindData |  |
| 70 | `FwCreateLocalTempStore` | `0x31A00` | 525 | UnwindData |  |
| 73 | `FwDeleteAllRules` | `0x31C20` | 228 | UnwindData |  |
| 74 | `FwDeleteAllSets` | `0x31D10` | 260 | UnwindData |  |
| 75 | `FwDeleteDynamicKeywordAddressInRegistry` | `0x31E20` | 412 | UnwindData |  |
| 76 | `FwDeleteHyperVVMCreatorFromRegistry` | `0x31FD0` | 424 | UnwindData |  |
| 78 | `FwDeleteSet` | `0x32180` | 285 | UnwindData |  |
| 79 | `FwDestroyLocalTempStore` | `0x322B0` | 146 | UnwindData |  |
| 92 | `FwEraseGPOStoreBaseKey` | `0x32350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `FwGetDynamicKeywordOriginFromStoreType` | `0x32370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `FwGetGlobalConfigFromLocalTempStore` | `0x32390` | 220 | UnwindData |  |
| 107 | `FwGetHyperVProfileConfigFromRegistry` | `0x32480` | 396 | UnwindData |  |
| 108 | `FwGetHyperVVMConfigFromRegistry` | `0x32620` | 381 | UnwindData |  |
| 109 | `FwGetHyperVVMCreatorIdsFromRegistry` | `0x327B0` | 775 | UnwindData |  |
| 111 | `FwGetStoreTypeFromDynamicKeywordOriginType` | `0x32AC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `FwMigrateLegacySettings` | `0x32AF0` | 148 | UnwindData |  |
| 125 | `FwOpenOfflinePolicyStore` | `0x32B90` | 946 | UnwindData |  |
| 139 | `FwSetGlobalConfig` | `0x33060` | 550 | UnwindData |  |
| 141 | `FwSetHyperVProfileConfigInRegistry` | `0x33290` | 759 | UnwindData |  |
| 142 | `FwSetHyperVVMConfigInRegistry` | `0x33590` | 708 | UnwindData |  |
| 143 | `FwSetResolveFlags` | `0x33860` | 400 | UnwindData |  |
| 145 | `FwSetSet` | `0x33A00` | 321 | UnwindData |  |
| 153 | `FwUpdateDynamicKeywordAddressInRegistry` | `0x33B50` | 466 | UnwindData |  |
| 154 | `FwUpgradeHyperVVMConfigToProfileConfig` | `0x33D30` | 435 | UnwindData |  |
| 33 | `FwAdvPolicyDecodeFirewallRule` | `0x34070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `FwAdvPolicyVerifyFirewallRule` | `0x34090` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `FwDecodeDynamicKeywordAddress` | `0x34290` | 509 | UnwindData |  |
| 85 | `FwEncodeDynamicKeywordAddress` | `0x344A0` | 663 | UnwindData |  |
| 164 | `IsRuleLegacyICMPSettings` | `0x35EA0` | 28,796 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
