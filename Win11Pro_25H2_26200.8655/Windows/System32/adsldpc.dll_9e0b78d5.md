# Binary Specification: adsldpc.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\adsldpc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9e0b78d5f9b5f6236deb3c67828638cfc4f19b4e1c617a7ce4cb461812ec18a3`
* **Total Exported Functions:** 175

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 37 | `BuildADsParentPathFromObjectInfo2` | `0x1010` | 146 | UnwindData |  |
| 38 | `BuildADsParentPathFromObjectInfo` | `0x10B0` | 899 | UnwindData |  |
| 17 | `ADsGetColumn` | `0x1680` | 1,648 | UnwindData |  |
| 173 | `MapLDAPTypeToADSType` | `0x2280` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `ADsExecuteSearch` | `0x22B0` | 1,827 | UnwindData |  |
| 40 | `BuildADsPathFromLDAPPath` | `0x2A10` | 1,367 | UnwindData |  |
| 41 | `BuildADsPathFromParent` | `0x2FF0` | 229 | UnwindData |  |
| 42 | `BuildLDAPPathFromADsPath2` | `0x30E0` | 696 | UnwindData |  |
| 24 | `ADsObject` | `0x33A0` | 156 | UnwindData |  |
| 51 | `FreeObjectInfo` | `0x3450` | 58 | UnwindData |  |
| 59 | `InitObjectInfo` | `0x3800` | 172 | UnwindData |  |
| 123 | `PathName` | `0x3BA0` | 274 | UnwindData |  |
| 45 | `Component` | `0x4230` | 541 | UnwindData |  |
| 53 | `GetDisplayName` | `0x4AB0` | 394 | UnwindData |  |
| 66 | `LdapCloseObject` | `0x4D00` | 65 | UnwindData |  |
| 16 | `ADsFreeColumn` | `0x50B0` | 488 | UnwindData |  |
| 114 | `LdapTypeFreeLdapObjects` | `0x52A0` | 116 | UnwindData |  |
| 2 | `??1CLexer@@QEAA@XZ` | `0x5500` | 24 | UnwindData |  |
| 169 | `FreeADsMem` | `0x5520` | 32 | UnwindData |  |
| 111 | `LdapTypeCopyConstruct` | `0x6830` | 76 | UnwindData |  |
| 168 | `AllocADsStr` | `0x7D30` | 165 | UnwindData |  |
| 170 | `FreeADsStr` | `0x8640` | 39 | UnwindData |  |
| 3 | `ADSIPrint` | `0x8BA0` | 174 | UnwindData |  |
| 135 | `SchemaGetStringsFromStringTable` | `0x8C60` | 326 | UnwindData |  |
| 81 | `LdapGetSyntaxIdOfAttribute` | `0xA2C0` | 156 | UnwindData |  |
| 127 | `ReadServerSupportsIsADControl` | `0xAE40` | 154 | UnwindData |  |
| 95 | `LdapOpenObject2` | `0xBB10` | 937 | UnwindData |  |
| 96 | `LdapOpenObject` | `0xBEC0` | 36 | UnwindData |  |
| 57 | `GetServerAndPort` | `0xC940` | 272 | UnwindData |  |
| 125 | `ReadSecurityDescriptorControlType` | `0xCBD0` | 174 | UnwindData |  |
| 94 | `LdapNextEntry` | `0xD7D0` | 103 | UnwindData |  |
| 20 | `ADsGetNextRow` | `0xD840` | 1,064 | UnwindData |  |
| 13 | `ADsEnumAttributes` | `0xE060` | 1,108 | UnwindData |  |
| 133 | `SchemaGetPropertyInfo` | `0xE4C0` | 158 | UnwindData |  |
| 171 | `LdapTypeToAdsTypeCopyConstruct` | `0xE570` | 235 | UnwindData |  |
| 21 | `ADsGetObjectAttributes` | `0xE670` | 2,589 | UnwindData |  |
| 106 | `LdapSearchExtS` | `0xF600` | 128 | UnwindData |  |
| 101 | `LdapReadAttributeFast` | `0xF690` | 329 | UnwindData |  |
| 108 | `LdapSearchS` | `0xF7E0` | 81 | UnwindData |  |
| 76 | `LdapFirstEntry` | `0xFA80` | 105 | UnwindData |  |
| 82 | `LdapGetSyntaxOfAttributeOnServer` | `0xFBF0` | 170 | UnwindData |  |
| 143 | `UnMarshallLDAPToLDAPSynID` | `0xFCA0` | 367 | UnwindData |  |
| 49 | `FindEntryInSearchTable` | `0xFE20` | 71 | UnwindData |  |
| 166 | `AdsTypeFreeAdsObjects` | `0xFEF0` | 221 | UnwindData |  |
| 18 | `ADsGetFirstRow` | `0xFFE0` | 666 | UnwindData |  |
| 83 | `LdapGetValues` | `0x10280` | 142 | UnwindData |  |
| 19 | `ADsGetNextColumnName` | `0x10320` | 240 | UnwindData |  |
| 93 | `LdapNextAttribute` | `0x10420` | 54 | UnwindData |  |
| 75 | `LdapFirstAttribute` | `0x10460` | 102 | UnwindData |  |
| 165 | `ADsSetLastError` | `0x10F20` | 89 | UnwindData |  |
| 103 | `LdapResult` | `0x11170` | 300 | UnwindData |  |
| 136 | `SchemaGetSyntaxOfAttribute` | `0x112B0` | 271 | UnwindData |  |
| 84 | `LdapGetValuesLen` | `0x113D0` | 142 | UnwindData |  |
| 130 | `SchemaGetClassInfo` | `0x11470` | 98 | UnwindData |  |
| 78 | `LdapGetNextPageS` | `0x114E0` | 160 | UnwindData |  |
| 144 | `intcmp` | `0x11680` | 8,304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `SortAndRemoveDuplicateOIDs` | `0x136F0` | 160 | UnwindData |  |
| 50 | `FindSearchTableIndex` | `0x146D0` | 87 | UnwindData |  |
| 167 | `AllocADsMem` | `0x14940` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 174 | `ReallocADsMem` | `0x14DA0` | 120 | UnwindData |  |
| 112 | `LdapTypeFreeLdapModList` | `0x15210` | 62 | UnwindData |  |
| 113 | `LdapTypeFreeLdapModObject` | `0x15260` | 89 | UnwindData |  |
| 52 | `GetDefaultServer` | `0x152C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `?InitializePath@CLexer@@QEAAJPEAG@Z` | `0x15300` | 75 | UnwindData |  |
| 26 | `ADsSetSearchPreference` | `0x15360` | 2,274 | UnwindData |  |
| 124 | `ReadPagingSupportedAttr` | `0x15CD0` | 150 | UnwindData |  |
| 5 | `ADsCloseSearchHandle` | `0x15F40` | 735 | UnwindData |  |
| 85 | `LdapInitializeSearchPreferences` | `0x16B30` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `LdapValueFree` | `0x16C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `??0CLexer@@QEAA@XZ` | `0x16C70` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `LdapAttributeFree` | `0x16D00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `SchemaOpen` | `0x16D10` | 50 | UnwindData |  |
| 70 | `LdapCountEntries` | `0x16D50` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `BuildADsPathFromLDAPPath2` | `0x16DE0` | 555 | UnwindData |  |
| 36 | `BuildADsParentPath` | `0x17980` | 330 | UnwindData |  |
| 99 | `LdapReadAttribute2` | `0x17C20` | 266 | UnwindData |  |
| 163 | `ADsEncodeBinaryData` | `0x18180` | 196 | UnwindData |  |
| 92 | `LdapMsgFree` | `0x18250` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `LdapValueFreeLen` | `0x18270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `LdapMemFree` | `0x18290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `IsGCNamespace` | `0x182B0` | 104 | UnwindData |  |
| 77 | `LdapGetDn` | `0x18570` | 94 | UnwindData |  |
| 139 | `?SetAtDisabler@CLexer@@QEAAXH@Z` | `0x18780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `LdapControlFree` | `0x18790` | 4,720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 162 | `ADsDecodeBinaryData` | `0x19A00` | 320 | UnwindData |  |
| 175 | `ReallocADsStr` | `0x19B50` | 91 | UnwindData |  |
| 164 | `ADsGetLastError` | `0x19BC0` | 321 | UnwindData |  |
| 145 | `ADSIAbandonSearch` | `0x19E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `ADSICloseDSObject` | `0x19E70` | 36 | UnwindData |  |
| 147 | `ADSICloseSearchHandle` | `0x19EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 148 | `ADSICreateDSObject` | `0x19EB0` | 43 | UnwindData |  |
| 149 | `ADSIDeleteDSObject` | `0x19EF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `ADSIExecuteSearch` | `0x19F10` | 143 | UnwindData |  |
| 151 | `ADSIFreeColumn` | `0x19FB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `ADSIGetColumn` | `0x19FC0` | 43 | UnwindData |  |
| 153 | `ADSIGetFirstRow` | `0x1A000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `ADSIGetNextColumnName` | `0x1A020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `ADSIGetNextRow` | `0x1A040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `ADSIGetObjectAttributes` | `0x1A060` | 142 | UnwindData |  |
| 157 | `ADSIGetPreviousRow` | `0x1A100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 158 | `ADSIModifyRdn` | `0x1A120` | 287 | UnwindData |  |
| 159 | `ADSIOpenDSObject` | `0x1A250` | 575 | UnwindData |  |
| 160 | `ADSISetObjectAttributes` | `0x1A4A0` | 129 | UnwindData |  |
| 161 | `ADSISetSearchPreference` | `0x1A530` | 63 | UnwindData |  |
| 8 | `ADsCreateDSObject` | `0x1A7B0` | 33 | UnwindData |  |
| 9 | `ADsCreateDSObjectExt` | `0x1A7E0` | 851 | UnwindData |  |
| 12 | `ADsDeleteDSObject` | `0x1AB40` | 183 | UnwindData |  |
| 25 | `ADsSetObjectAttributes` | `0x1AC00` | 1,419 | UnwindData |  |
| 172 | `MapADSTypeToLDAPType` | `0x1B1A0` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `LdapTypeToAdsTypeDNWithBinary` | `0x1B3B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `LdapTypeToAdsTypeDNWithString` | `0x1B3C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `LdapTypeToAdsTypeGeneralizedTime` | `0x1B3D0` | 57 | UnwindData |  |
| 118 | `LdapTypeToAdsTypeUTCTime` | `0x1B5C0` | 57 | UnwindData |  |
| 126 | `ReadServerSupportsIsADAMControl` | `0x1CA80` | 150 | UnwindData |  |
| 110 | `LdapTypeBinaryToString` | `0x1D070` | 311 | UnwindData |  |
| 34 | `BerBvFree` | `0x1D1B0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `LdapAddExtS` | `0x1D200` | 83 | UnwindData |  |
| 63 | `LdapAddS` | `0x1D260` | 73 | UnwindData |  |
| 65 | `LdapCacheAddRef` | `0x1D2B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `LdapCompareExt` | `0x1D2C0` | 106 | UnwindData |  |
| 69 | `LdapControlsFree` | `0x1D330` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `LdapCrackUserDNtoNTLMUser2` | `0x1D350` | 331 | UnwindData |  |
| 72 | `LdapCreatePageControl` | `0x1D4B0` | 68 | UnwindData |  |
| 73 | `LdapDeleteExtS` | `0x1D500` | 73 | UnwindData |  |
| 74 | `LdapDeleteS` | `0x1D550` | 73 | UnwindData |  |
| 89 | `LdapModDnS` | `0x1D5F0` | 73 | UnwindData |  |
| 90 | `LdapModifyExtS` | `0x1D640` | 83 | UnwindData |  |
| 91 | `LdapModifyS` | `0x1D6A0` | 73 | UnwindData |  |
| 97 | `LdapParsePageControl` | `0x1DA40` | 58 | UnwindData |  |
| 98 | `LdapParseResult` | `0x1DA80` | 102 | UnwindData |  |
| 100 | `LdapReadAttribute` | `0x1DAF0` | 70 | UnwindData |  |
| 102 | `LdapRenameExtS` | `0x1DB40` | 104 | UnwindData |  |
| 104 | `LdapSearch` | `0x1DBB0` | 129 | UnwindData |  |
| 105 | `LdapSearchAbandonPage` | `0x1DC40` | 73 | UnwindData |  |
| 107 | `LdapSearchInitPage` | `0x1DC90` | 200 | UnwindData |  |
| 109 | `LdapSearchST` | `0x1DD60` | 86 | UnwindData |  |
| 122 | `LdapcSetStickyServer` | `0x1DDC0` | 202 | UnwindData |  |
| 121 | `LdapcKeepHandleAround` | `0x1E080` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `AdsTypeToLdapTypeCopyConstruct` | `0x1E270` | 198 | UnwindData |  |
| 30 | `AdsTypeToLdapTypeCopyDNWithBinary` | `0x1E340` | 388 | UnwindData |  |
| 31 | `AdsTypeToLdapTypeCopyDNWithString` | `0x1E4D0` | 317 | UnwindData |  |
| 32 | `AdsTypeToLdapTypeCopyGeneralizedTime` | `0x1E620` | 201 | UnwindData |  |
| 33 | `AdsTypeToLdapTypeCopyTime` | `0x1EA30` | 233 | UnwindData |  |
| 55 | `GetLDAPTypeName` | `0x1F0C0` | 252 | UnwindData |  |
| 56 | `?GetNextToken@CLexer@@QEAAJPEAGPEAK@Z` | `0x1F1D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `?SetExclaimnationDisabler@CLexer@@QEAAXH@Z` | `0x1F1F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `?SetFSlashDisabler@CLexer@@QEAAXH@Z` | `0x1F200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `BuildLDAPPathFromADsPath` | `0x1F210` | 436 | UnwindData |  |
| 44 | `ChangeSeparator` | `0x1F3D0` | 55 | UnwindData |  |
| 6 | `ADsCreateAttributeDefinition` | `0x1F410` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `ADsCreateClassDefinition` | `0x1F410` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `ADsDeleteAttributeDefinition` | `0x1F410` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `ADsDeleteClassDefinition` | `0x1F410` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `ADsEnumClasses` | `0x1F410` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `ADsWriteAttributeDefinition` | `0x1F410` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `ADsWriteClassDefinition` | `0x1F410` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `LdapGetSchemaObjectCount` | `0x1F5D0` | 97 | UnwindData |  |
| 80 | `LdapGetSubSchemaSubEntryPath` | `0x1F640` | 108 | UnwindData |  |
| 86 | `LdapIsClassNameValidOnServer` | `0x1F6C0` | 133 | UnwindData |  |
| 87 | `LdapMakeSchemaCacheObsolete` | `0x1F750` | 76 | UnwindData |  |
| 128 | `SchemaAddRef` | `0x1F7B0` | 81 | UnwindData |  |
| 129 | `SchemaClose` | `0x1F810` | 46 | UnwindData |  |
| 131 | `SchemaGetClassInfoByIndex` | `0x1F850` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `SchemaGetObjectCount` | `0x1F880` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `SchemaGetPropertyInfoByIndex` | `0x1F8B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `SchemaIsClassAContainer` | `0x1F8E0` | 329 | UnwindData |  |
| 46 | `ConvertSidToString` | `0x1FB30` | 479 | UnwindData |  |
| 47 | `ConvertSidToU2Trustee` | `0x1FD20` | 659 | UnwindData |  |
| 48 | `ConvertU2TrusteeToSid` | `0x1FFC0` | 457 | UnwindData |  |
| 4 | `ADsAbandonSearch` | `0x20190` | 120 | UnwindData |  |
| 22 | `ADsGetPreviousRow` | `0x204B0` | 249 | UnwindData |  |
| 23 | `ADsHelperGetCurrentRowMessage` | `0x205B0` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `BerEncodingQuotaControl` | `0x20850` | 173 | UnwindData |  |
| 54 | `GetDomainDNSNameForDomain` | `0x21060` | 80 | UnwindData |  |
| 58 | `GetSyntaxOfAttribute` | `0x210C0` | 168 | UnwindData |  |
