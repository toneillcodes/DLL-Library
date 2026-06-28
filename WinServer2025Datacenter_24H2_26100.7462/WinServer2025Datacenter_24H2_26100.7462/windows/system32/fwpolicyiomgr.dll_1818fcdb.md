# Binary Specification: fwpolicyiomgr.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\fwpolicyiomgr.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1818fcdbb39e07f9660bf6201ac7dcceaeae818a1c626939492e8e7e448325d4`
* **Total Exported Functions:** 178

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `CreateDefaultAuthAppRule` | `0x18E0` | 151 | UnwindData |  |
| 49 | `FwConvertFwRuleToHyperVRule` | `0x1980` | 1,160 | UnwindData |  |
| 5 | `CreateDefaultIcmpRule` | `0x1E10` | 263 | UnwindData |  |
| 57 | `FwCopyHyperVRule` | `0x1F20` | 812 | UnwindData |  |
| 100 | `FwFreeRules` | `0x2260` | 27 | UnwindData |  |
| 97 | `FwFreeHyperVRulesBySchemaVersion` | `0x27D0` | 80 | UnwindData |  |
| 152 | `FwUniteWFAddressesContents` | `0x28F0` | 482 | UnwindData |  |
| 10 | `CreateDefaultRule` | `0x2AE0` | 540 | UnwindData |  |
| 67 | `FwCopyRule` | `0x2D10` | 3,442 | UnwindData |  |
| 102 | `FwFreeWFRule` | `0x3A90` | 18 | UnwindData |  |
| 130 | `FwPolioCopyWFAddressesContents` | `0x3E00` | 422 | UnwindData |  |
| 131 | `FwPolioEmptyWFAddresses` | `0x3FB0` | 13 | UnwindData |  |
| 41 | `FwCSRuleEmptyByBinaryVersion` | `0x4040` | 416 | UnwindData |  |
| 54 | `FwCopyCSRule` | `0x41F0` | 1,854 | UnwindData |  |
| 98 | `FwFreeHyperVVMCreatorsBySchemaVersion` | `0x4940` | 100 | UnwindData |  |
| 89 | `FwEnumHyperVVMCreatorsFromRegistry` | `0x49B0` | 188 | UnwindData |  |
| 110 | `FwGetRule` | `0x5630` | 261 | UnwindData |  |
| 103 | `FwGetConfig` | `0x6850` | 629 | UnwindData |  |
| 46 | `FwClosePolicyStore` | `0x6AD0` | 102 | UnwindData |  |
| 105 | `FwGetGlobalConfig` | `0x6EA0` | 987 | UnwindData |  |
| 37 | `FwAreAllContainedInAddresses` | `0x83A0` | 81 | UnwindData |  |
| 31 | `FwAddRule` | `0x86E0` | 445 | UnwindData |  |
| 77 | `FwDeleteRule` | `0x88B0` | 310 | UnwindData |  |
| 144 | `FwSetRule` | `0x8DD0` | 583 | UnwindData |  |
| 86 | `FwEncodeSyntacticallyImportantFields` | `0x9200` | 116 | UnwindData |  |
| 138 | `FwSetConfig` | `0x9AC0` | 448 | UnwindData |  |
| 140 | `FwSetGlobalConfigInLocalTempStore` | `0x9C90` | 220 | UnwindData |  |
| 11 | `FwParseAllPortVersions` | `0xA240` | 172 | UnwindData |  |
| 84 | `FwEmptyWFRule` | `0xA7B0` | 14 | UnwindData |  |
| 39 | `FwBinariesFree` | `0xAB10` | 85 | UnwindData |  |
| 159 | `GetOpenPortorAuthAppAsBSTR` | `0xBA80` | 182 | UnwindData |  |
| 158 | `GetOpenPortorAuthAppAddrAsString` | `0xBB40` | 464 | UnwindData |  |
| 172 | `OpenPortOrAuthAppAddrToStringInt2` | `0xBD20` | 43 | UnwindData |  |
| 173 | `OpenPortOrAuthAppAddrToStringInt3` | `0xBD60` | 3,373 | UnwindData |  |
| 59 | `FwCopyICMPTypeCode` | `0x126F0` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `FwCopyPlatform` | `0x126F0` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `FwCopyPortRange` | `0x126F0` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `FwVerifyWFRuleSemantics` | `0x128E0` | 51 | UnwindData |  |
| 150 | `FwStringToSids` | `0x12930` | 552 | UnwindData |  |
| 148 | `FwSidCopy` | `0x133B0` | 167 | UnwindData |  |
| 23 | `FWInitExtensionDllCriticalSection` | `0x14280` | 98 | UnwindData |  |
| 18 | `FWDestroyExtensionDllCriticalSection` | `0x144D0` | 80 | UnwindData |  |
| 13 | `FwParseInterfaceType` | `0x14A80` | 140 | UnwindData |  |
| 17 | `CalculateOpenPortOrAuthAppAddrStringSize2` | `0x14B20` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | `FwSubtractAddresses` | `0x14C40` | 311 | UnwindData |  |
| 16 | `CalculateOpenPortOrAuthAppAddrStringSize` | `0x153B0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `FwPolioMergeAddresses` | `0x15480` | 77 | UnwindData |  |
| 147 | `FwSidAndAttributesFree` | `0x15590` | 86 | UnwindData |  |
| 12 | `FwParseICMPTypeCodes` | `0x15610` | 379 | UnwindData |  |
| 167 | `IsUnicastExplicitAddressesEmpty` | `0x158E0` | 99 | UnwindData |  |
| 19 | `FWGPLock` | `0x15A20` | 81 | UnwindData |  |
| 22 | `FWGPUnlockEx` | `0x15A80` | 104 | UnwindData |  |
| 62 | `FwCopyLUID` | `0x16CB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `FwNegateAddresses` | `0x16CD0` | 48 | UnwindData |  |
| 55 | `FwCopyCryptoSet` | `0x16F70` | 935 | UnwindData |  |
| 101 | `FwFreeSets` | `0x17380` | 106 | UnwindData |  |
| 71 | `FwCryptoSetFree` | `0x173F0` | 34 | UnwindData |  |
| 135 | `FwRemoveDuplicateAddresses` | `0x17770` | 32 | UnwindData |  |
| 160 | `IsEqualAddresses` | `0x179F0` | 204 | UnwindData |  |
| 1 | `CopyIcmpSettings` | `0x17B70` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `FwPolioCopyAuthSet` | `0x17C70` | 715 | UnwindData |  |
| 91 | `FwEnumSets` | `0x181F0` | 919 | UnwindData |  |
| 2 | `CopyIcmpV4Rules` | `0x189F0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `FwOpenAppCDbPolicyStore` | `0x18AE0` | 449 | UnwindData |  |
| 177 | `StringToOpenPortOrAuthAppAddress2` | `0x18EC0` | 465 | UnwindData |  |
| 3 | `CopyIcmpV6Rules` | `0x190D0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `Isv4Orv6AddressesEmpty` | `0x191A0` | 3,984 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `FwConvertIPv6SubNetToRange` | `0x1A130` | 168 | UnwindData |  |
| 128 | `FwPolioConvertIPv6SubNetToRange` | `0x1A130` | 168 | UnwindData |  |
| 87 | `FwEncodeSyntacticallyImportantFieldsInt` | `0x1A1E0` | 1,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `FwAdvPolicyEncodeRule` | `0x1A720` | 1,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `FwIsV6AddrLoopback` | `0x1ACA0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 162 | `IsFwRuleHyperVApplicable` | `0x1ACF0` | 432 | UnwindData |  |
| 80 | `FwDoNothingOnObject` | `0x1AF40` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `FwSidsToString` | `0x1B180` | 627 | UnwindData |  |
| 174 | `SanitizeForPrivacy` | `0x1B790` | 112 | UnwindData |  |
| 88 | `FwEnumAllDynamicKeywordAddressesInRegistry` | `0x1B880` | 280 | UnwindData |  |
| 27 | `FWSetGPHelperFnPtrs` | `0x1B9E0` | 223 | UnwindData |  |
| 90 | `FwEnumRules` | `0x1BAF0` | 635 | UnwindData |  |
| 176 | `StringToOpenPortOrAuthAppAddress` | `0x1BE20` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `FwIPV4RangeContainsMulticast` | `0x1BE90` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `FwHyperVRuleVerify` | `0x1BFA0` | 111 | UnwindData |  |
| 82 | `FwDownlevelFirewallRuleEmpty` | `0x1C340` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `FwFindMatchingOpenPortRule` | `0x1C590` | 162 | UnwindData |  |
| 126 | `FwOpenPolicyStore` | `0x1DA40` | 1,658 | UnwindData |  |
| 136 | `FwRuleResolveFlags` | `0x1E0C0` | 1,749 | UnwindData |  |
| 119 | `FwMMRuleFree` | `0x1F680` | 141 | UnwindData |  |
| 38 | `FwAuthSetFree` | `0x1F800` | 34 | UnwindData |  |
| 42 | `FwCSRuleFree` | `0x1FC50` | 146 | UnwindData |  |
| 114 | `FwICFProtocolToWfProtocol` | `0x20050` | 52 | UnwindData |  |
| 116 | `FwIPV6RangeContainsMulticast` | `0x20220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `FwFreeDynamicKeywordAddressesInternal` | `0x20240` | 91 | UnwindData |  |
| 25 | `FWPrimitivesSetGPHelperFnPtrs` | `0x20340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `FwCSRuleEmpty` | `0x20360` | 6,592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `GetRemoteAdminSettings` | `0x21D20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `CreateDefaultOpenPortRule` | `0x21D40` | 241 | UnwindData |  |
| 7 | `CreateDefaultPerInterfaceIcmpRule` | `0x21E40` | 486 | UnwindData |  |
| 8 | `CreateDefaultPerInterfaceOpenPortRule` | `0x22030` | 220 | UnwindData |  |
| 9 | `CreateDefaultRemoteAdminRule` | `0x22120` | 872 | UnwindData |  |
| 28 | `FreeAbsoluteInterfaces` | `0x22820` | 50 | UnwindData |  |
| 36 | `FwAppContainerChangeFree` | `0x22860` | 146 | UnwindData |  |
| 43 | `FwCSRuleVerify` | `0x22900` | 49 | UnwindData |  |
| 44 | `FwChkBuildSidAndAttributesFree` | `0x22940` | 149 | UnwindData |  |
| 45 | `FwCleanupPhase1Sa` | `0x229E0` | 70 | UnwindData |  |
| 47 | `FwCompareCSRule` | `0x22A30` | 1,023 | UnwindData |  |
| 48 | `FwCompareFWRule` | `0x22E40` | 1,340 | UnwindData |  |
| 51 | `FwCopyAuthSetListToLowerVersion` | `0x23390` | 265 | UnwindData |  |
| 52 | `FwCopyAuthSetToLowerVersion` | `0x234A0` | 850 | UnwindData |  |
| 53 | `FwCopyAuthsetToHigherVersion` | `0x23800` | 710 | UnwindData |  |
| 56 | `FwCopyHyperVPort` | `0x23AD0` | 449 | UnwindData |  |
| 58 | `FwCopyHyperVVMCreator` | `0x23CA0` | 255 | UnwindData |  |
| 60 | `FwCopyInterfaceIndexes` | `0x23DB0` | 214 | UnwindData |  |
| 61 | `FwCopyInterfaceLuids` | `0x23E90` | 214 | UnwindData |  |
| 63 | `FwCopyMMRule` | `0x23F70` | 979 | UnwindData |  |
| 66 | `FwCopyPortsContents` | `0x24350` | 120 | UnwindData |  |
| 68 | `FwCountAuthAppRules` | `0x243D0` | 97 | UnwindData |  |
| 69 | `FwCountGlobalOpenPortRules` | `0x24440` | 97 | UnwindData |  |
| 81 | `FwDownlevelAuthSetFree` | `0x244B0` | 40 | UnwindData |  |
| 83 | `FwDynamicKeywordAddressIsStringValid` | `0x244E0` | 63 | UnwindData |  |
| 94 | `FwFreeDynamicKeywordAddressDataBySchemaVersion` | `0x24540` | 109 | UnwindData |  |
| 96 | `FwFreeHyperVPortsBySchemaVersion` | `0x245C0` | 141 | UnwindData |  |
| 99 | `FwFreeObjects` | `0x24660` | 68 | UnwindData |  |
| 113 | `FwICFProfileToWfProfile` | `0x246B0` | 57 | UnwindData |  |
| 117 | `FwInvertAddresses` | `0x246F0` | 139 | UnwindData |  |
| 120 | `FwMMRuleVerify` | `0x24790` | 49 | UnwindData |  |
| 121 | `FwMigrateLegacyAuthenticatedBypassSddl` | `0x247D0` | 39 | UnwindData |  |
| 127 | `FwParseAddressToken` | `0x24800` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `FwReduceHyperVRulesToVersion` | `0x24860` | 187 | UnwindData |  |
| 134 | `FwReduceObjectsToVersion` | `0x24930` | 1,610 | UnwindData |  |
| 137 | `FwSddlStringVerify` | `0x24F80` | 36 | UnwindData |  |
| 146 | `FwSidAndAttributesCopy` | `0x24FB0` | 346 | UnwindData |  |
| 156 | `FwWfProtocolToICFProtocol` | `0x25110` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `GetOpenPortOrAuthAppAddrScope` | `0x25140` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 161 | `IsEqualFwPorts` | `0x25180` | 81 | UnwindData |  |
| 163 | `IsPortsEmpty` | `0x25250` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 165 | `IsRulePerInterfaceIcmp` | `0x25270` | 59 | UnwindData |  |
| 166 | `IsRulePerInterfaceOpenPort` | `0x252C0` | 75 | UnwindData |  |
| 170 | `MakeAbsoluteInterfaces` | `0x253F0` | 261 | UnwindData |  |
| 171 | `OpenPortOrAuthAppAddrToString` | `0x25500` | 45 | UnwindData |  |
| 175 | `StringArrayToOpenPortOrAuthAppAddress` | `0x255A0` | 419 | UnwindData |  |
| 178 | `ValidatePortOrAppAddressString` | `0x25750` | 194 | UnwindData |  |
| 14 | `FwParseInterfaceTypeCsp` | `0x28720` | 98 | UnwindData |  |
| 26 | `FWResolveGPONames` | `0x2CC40` | 83 | UnwindData |  |
| 169 | `LoadGPExtensionDll` | `0x2CCA0` | 397 | UnwindData |  |
| 20 | `FWGPOCleanup` | `0x2CE40` | 22 | UnwindData |  |
| 21 | `FWGPOSave` | `0x2CE60` | 32 | UnwindData |  |
| 24 | `FWOpenGPOAndGetRegKey` | `0x2CE90` | 55 | UnwindData |  |
| 29 | `FwAddDynamicKeywordAddressInRegistry` | `0x35020` | 479 | UnwindData |  |
| 30 | `FwAddHyperVVMCreatorToRegistry` | `0x35210` | 518 | UnwindData |  |
| 32 | `FwAddSet` | `0x35420` | 321 | UnwindData |  |
| 70 | `FwCreateLocalTempStore` | `0x355A0` | 525 | UnwindData |  |
| 73 | `FwDeleteAllRules` | `0x357C0` | 228 | UnwindData |  |
| 74 | `FwDeleteAllSets` | `0x358B0` | 260 | UnwindData |  |
| 75 | `FwDeleteDynamicKeywordAddressInRegistry` | `0x359C0` | 412 | UnwindData |  |
| 76 | `FwDeleteHyperVVMCreatorFromRegistry` | `0x35B70` | 424 | UnwindData |  |
| 78 | `FwDeleteSet` | `0x35D20` | 285 | UnwindData |  |
| 79 | `FwDestroyLocalTempStore` | `0x35E50` | 146 | UnwindData |  |
| 92 | `FwEraseGPOStoreBaseKey` | `0x35EF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `FwGetDynamicKeywordOriginFromStoreType` | `0x35F10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `FwGetGlobalConfigFromLocalTempStore` | `0x35F30` | 220 | UnwindData |  |
| 107 | `FwGetHyperVProfileConfigFromRegistry` | `0x36020` | 396 | UnwindData |  |
| 108 | `FwGetHyperVVMConfigFromRegistry` | `0x361C0` | 381 | UnwindData |  |
| 109 | `FwGetHyperVVMCreatorIdsFromRegistry` | `0x36350` | 775 | UnwindData |  |
| 111 | `FwGetStoreTypeFromDynamicKeywordOriginType` | `0x36660` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `FwMigrateLegacySettings` | `0x36690` | 148 | UnwindData |  |
| 125 | `FwOpenOfflinePolicyStore` | `0x36730` | 946 | UnwindData |  |
| 139 | `FwSetGlobalConfig` | `0x36C00` | 504 | UnwindData |  |
| 141 | `FwSetHyperVProfileConfigInRegistry` | `0x36E00` | 759 | UnwindData |  |
| 142 | `FwSetHyperVVMConfigInRegistry` | `0x37100` | 708 | UnwindData |  |
| 143 | `FwSetResolveFlags` | `0x373D0` | 400 | UnwindData |  |
| 145 | `FwSetSet` | `0x37570` | 321 | UnwindData |  |
| 153 | `FwUpdateDynamicKeywordAddressInRegistry` | `0x376C0` | 466 | UnwindData |  |
| 154 | `FwUpgradeHyperVVMConfigToProfileConfig` | `0x378A0` | 435 | UnwindData |  |
| 33 | `FwAdvPolicyDecodeFirewallRule` | `0x37BE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `FwAdvPolicyVerifyFirewallRule` | `0x37C00` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `FwDecodeDynamicKeywordAddress` | `0x37E00` | 509 | UnwindData |  |
| 85 | `FwEncodeDynamicKeywordAddress` | `0x38010` | 663 | UnwindData |  |
| 164 | `IsRuleLegacyICMPSettings` | `0x39A10` | 28,812 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
