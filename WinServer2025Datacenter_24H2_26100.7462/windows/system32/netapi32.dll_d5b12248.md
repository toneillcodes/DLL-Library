# Binary Specification: netapi32.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\netapi32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d5b12248b116177329bf72cb517d515637cf2476dff1c159a0e1e7d28420be09`
* **Total Exported Functions:** 298

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DavAddConnection` | `0x0` | - | Forwarded | Forwarded to: `ext-ms-win-rdr-davhlpr-l1-1-0.DavAddConnection` |
| 2 | `DavDeleteConnection` | `0x0` | - | Forwarded | Forwarded to: `ext-ms-win-rdr-davhlpr-l1-1-0.DavDeleteConnection` |
| 3 | `DavFlushFile` | `0x0` | - | Forwarded | Forwarded to: `ext-ms-win-rdr-davhlpr-l1-1-0.DavFlushFile` |
| 4 | `DavGetExtendedError` | `0x0` | - | Forwarded | Forwarded to: `ext-ms-win-rdr-davhlpr-l1-1-0.DavGetExtendedError` |
| 5 | `DavGetHTTPFromUNCPath` | `0x0` | - | Forwarded | Forwarded to: `ext-ms-win-rdr-davhlpr-l1-1-0.DavGetHTTPFromUNCPath` |
| 6 | `DavGetUNCFromHTTPPath` | `0x0` | - | Forwarded | Forwarded to: `ext-ms-win-rdr-davhlpr-l1-1-0.DavGetUNCFromHTTPPath` |
| 7 | `DsAddressToSiteNamesA` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.DsAddressToSiteNamesA` |
| 8 | `DsAddressToSiteNamesExA` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.DsAddressToSiteNamesExA` |
| 9 | `DsAddressToSiteNamesExW` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.DsAddressToSiteNamesExW` |
| 10 | `DsAddressToSiteNamesW` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.DsAddressToSiteNamesW` |
| 11 | `DsDeregisterDnsHostRecordsA` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.DsDeregisterDnsHostRecordsA` |
| 12 | `DsDeregisterDnsHostRecordsW` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.DsDeregisterDnsHostRecordsW` |
| 13 | `DsEnumerateDomainTrustsA` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.DsEnumerateDomainTrustsA` |
| 14 | `DsEnumerateDomainTrustsW` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.DsEnumerateDomainTrustsW` |
| 15 | `DsGetDcCloseW` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.DsGetDcCloseW` |
| 16 | `DsGetDcNameA` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.DsGetDcNameA` |
| 17 | `DsGetDcNameW` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.DsGetDcNameW` |
| 18 | `DsGetDcNameWithAccountA` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.DsGetDcNameWithAccountA` |
| 19 | `DsGetDcNameWithAccountW` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.DsGetDcNameWithAccountW` |
| 20 | `DsGetDcNextA` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.DsGetDcNextA` |
| 21 | `DsGetDcNextW` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.DsGetDcNextW` |
| 22 | `DsGetDcOpenA` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.DsGetDcOpenA` |
| 23 | `DsGetDcOpenW` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.DsGetDcOpenW` |
| 24 | `DsGetDcSiteCoverageA` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.DsGetDcSiteCoverageA` |
| 25 | `DsGetDcSiteCoverageW` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.DsGetDcSiteCoverageW` |
| 26 | `DsGetForestTrustInformationW` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.DsGetForestTrustInformationW` |
| 27 | `DsGetSiteNameA` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.DsGetSiteNameA` |
| 28 | `DsGetSiteNameW` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.DsGetSiteNameW` |
| 29 | `DsMergeForestTrustInformationW` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.DsMergeForestTrustInformationW` |
| 30 | `DsRoleFreeMemory` | `0x0` | - | Forwarded | Forwarded to: `DSROLE.DsRoleFreeMemory` |
| 31 | `DsRoleGetPrimaryDomainInformation` | `0x0` | - | Forwarded | Forwarded to: `DSROLE.DsRoleGetPrimaryDomainInformation` |
| 32 | `DsValidateSubnetNameA` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.DsValidateSubnetNameA` |
| 33 | `DsValidateSubnetNameW` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.DsValidateSubnetNameW` |
| 35 | `I_DsUpdateReadOnlyServerDnsRecords` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.I_DsUpdateReadOnlyServerDnsRecords` |
| 36 | `I_NetAccountDeltas` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.I_NetAccountDeltas` |
| 37 | `I_NetAccountSync` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.I_NetAccountSync` |
| 38 | `I_NetChainSetClientAttributes` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.I_NetChainSetClientAttributes` |
| 39 | `I_NetChainSetClientAttributes2` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.I_NetChainSetClientAttributes2` |
| 40 | `I_NetDatabaseDeltas` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.I_NetDatabaseDeltas` |
| 41 | `I_NetDatabaseRedo` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.I_NetDatabaseRedo` |
| 42 | `I_NetDatabaseSync` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.I_NetDatabaseSync` |
| 43 | `I_NetDatabaseSync2` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.I_NetDatabaseSync2` |
| 44 | `I_NetDfsGetVersion` | `0x0` | - | Forwarded | Forwarded to: `SRVCLI.I_NetDfsGetVersion` |
| 45 | `I_NetDfsIsThisADomainName` | `0x0` | - | Forwarded | Forwarded to: `DFSCLI.I_NetDfsIsThisADomainName` |
| 46 | `I_NetGetDCList` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.I_NetGetDCList` |
| 47 | `I_NetGetForestTrustInformation` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.I_NetGetForestTrustInformation` |
| 48 | `I_NetLogonControl` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.I_NetLogonControl` |
| 49 | `I_NetLogonControl2` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.I_NetLogonControl2` |
| 50 | `I_NetLogonGetDomainInfo` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.I_NetLogonGetDomainInfo` |
| 51 | `I_NetLogonSamLogoff` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.I_NetLogonSamLogoff` |
| 52 | `I_NetLogonSamLogon` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.I_NetLogonSamLogon` |
| 53 | `I_NetLogonSamLogonEx` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.I_NetLogonSamLogonEx` |
| 54 | `I_NetLogonSamLogonWithFlags` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.I_NetLogonSamLogonWithFlags` |
| 55 | `I_NetLogonSendToSam` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.I_NetLogonSendToSam` |
| 56 | `I_NetLogonUasLogoff` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.I_NetLogonUasLogoff` |
| 57 | `I_NetLogonUasLogon` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.I_NetLogonUasLogon` |
| 58 | `I_NetServerAuthenticate` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.I_NetServerAuthenticate` |
| 59 | `I_NetServerAuthenticate2` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.I_NetServerAuthenticate2` |
| 60 | `I_NetServerAuthenticate3` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.I_NetServerAuthenticate3` |
| 61 | `I_NetServerAuthenticateKerberos` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.I_NetServerAuthenticateKerberos` |
| 62 | `I_NetServerGetTrustInfo` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.I_NetServerGetTrustInfo` |
| 63 | `I_NetServerPasswordGet` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.I_NetServerPasswordGet` |
| 64 | `I_NetServerPasswordSet` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.I_NetServerPasswordSet` |
| 65 | `I_NetServerPasswordSet2` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.I_NetServerPasswordSet2` |
| 66 | `I_NetServerReqChallenge` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.I_NetServerReqChallenge` |
| 67 | `I_NetServerSetServiceBits` | `0x0` | - | Forwarded | Forwarded to: `SRVCLI.I_NetServerSetServiceBits` |
| 68 | `I_NetServerSetServiceBitsEx` | `0x0` | - | Forwarded | Forwarded to: `SRVCLI.I_NetServerSetServiceBitsEx` |
| 69 | `I_NetServerTrustPasswordsGet` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.I_NetServerTrustPasswordsGet` |
| 70 | `I_NetlogonComputeClientDigest` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.I_NetlogonComputeClientDigest` |
| 71 | `I_NetlogonComputeServerDigest` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.I_NetlogonComputeServerDigest` |
| 78 | `NetAddAlternateComputerName` | `0x0` | - | Forwarded | Forwarded to: `WKSCLI.NetAddAlternateComputerName` |
| 79 | `NetAddServiceAccount` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.NetAddServiceAccount` |
| 82 | `NetApiBufferAllocate` | `0x0` | - | Forwarded | Forwarded to: `NETUTILS.NetApiBufferAllocate` |
| 83 | `NetApiBufferFree` | `0x0` | - | Forwarded | Forwarded to: `NETUTILS.NetApiBufferFree` |
| 84 | `NetApiBufferReallocate` | `0x0` | - | Forwarded | Forwarded to: `NETUTILS.NetApiBufferReallocate` |
| 85 | `NetApiBufferSize` | `0x0` | - | Forwarded | Forwarded to: `NETUTILS.NetApiBufferSize` |
| 92 | `NetConnectionEnum` | `0x0` | - | Forwarded | Forwarded to: `SRVCLI.NetConnectionEnum` |
| 93 | `NetCreateProvisioningPackage` | `0x0` | - | Forwarded | Forwarded to: `NETJOIN.NetCreateProvisioningPackage` |
| 94 | `NetDfsAdd` | `0x0` | - | Forwarded | Forwarded to: `DFSCLI.NetDfsAdd` |
| 95 | `NetDfsAddFtRoot` | `0x0` | - | Forwarded | Forwarded to: `DFSCLI.NetDfsAddFtRoot` |
| 96 | `NetDfsAddRootTarget` | `0x0` | - | Forwarded | Forwarded to: `DFSCLI.NetDfsAddRootTarget` |
| 97 | `NetDfsAddStdRoot` | `0x0` | - | Forwarded | Forwarded to: `DFSCLI.NetDfsAddStdRoot` |
| 98 | `NetDfsAddStdRootForced` | `0x0` | - | Forwarded | Forwarded to: `DFSCLI.NetDfsAddStdRootForced` |
| 99 | `NetDfsEnum` | `0x0` | - | Forwarded | Forwarded to: `DFSCLI.NetDfsEnum` |
| 100 | `NetDfsGetClientInfo` | `0x0` | - | Forwarded | Forwarded to: `DFSCLI.NetDfsGetClientInfo` |
| 101 | `NetDfsGetDcAddress` | `0x0` | - | Forwarded | Forwarded to: `DFSCLI.NetDfsGetDcAddress` |
| 102 | `NetDfsGetFtContainerSecurity` | `0x0` | - | Forwarded | Forwarded to: `DFSCLI.NetDfsGetFtContainerSecurity` |
| 103 | `NetDfsGetInfo` | `0x0` | - | Forwarded | Forwarded to: `DFSCLI.NetDfsGetInfo` |
| 104 | `NetDfsGetSecurity` | `0x0` | - | Forwarded | Forwarded to: `DFSCLI.NetDfsGetSecurity` |
| 105 | `NetDfsGetStdContainerSecurity` | `0x0` | - | Forwarded | Forwarded to: `DFSCLI.NetDfsGetStdContainerSecurity` |
| 106 | `NetDfsGetSupportedNamespaceVersion` | `0x0` | - | Forwarded | Forwarded to: `DFSCLI.NetDfsGetSupportedNamespaceVersion` |
| 107 | `NetDfsManagerGetConfigInfo` | `0x0` | - | Forwarded | Forwarded to: `DFSCLI.NetDfsManagerGetConfigInfo` |
| 108 | `NetDfsManagerInitialize` | `0x0` | - | Forwarded | Forwarded to: `DFSCLI.NetDfsManagerInitialize` |
| 109 | `NetDfsManagerSendSiteInfo` | `0x0` | - | Forwarded | Forwarded to: `DFSCLI.NetDfsManagerSendSiteInfo` |
| 110 | `NetDfsMove` | `0x0` | - | Forwarded | Forwarded to: `DFSCLI.NetDfsMove` |
| 111 | `NetDfsRemove` | `0x0` | - | Forwarded | Forwarded to: `DFSCLI.NetDfsRemove` |
| 112 | `NetDfsRemoveFtRoot` | `0x0` | - | Forwarded | Forwarded to: `DFSCLI.NetDfsRemoveFtRoot` |
| 113 | `NetDfsRemoveFtRootForced` | `0x0` | - | Forwarded | Forwarded to: `DFSCLI.NetDfsRemoveFtRootForced` |
| 114 | `NetDfsRemoveRootTarget` | `0x0` | - | Forwarded | Forwarded to: `DFSCLI.NetDfsRemoveRootTarget` |
| 115 | `NetDfsRemoveStdRoot` | `0x0` | - | Forwarded | Forwarded to: `DFSCLI.NetDfsRemoveStdRoot` |
| 116 | `NetDfsRename` | `0x0` | - | Forwarded | Forwarded to: `DFSCLI.NetDfsRename` |
| 117 | `NetDfsSetClientInfo` | `0x0` | - | Forwarded | Forwarded to: `DFSCLI.NetDfsSetClientInfo` |
| 118 | `NetDfsSetFtContainerSecurity` | `0x0` | - | Forwarded | Forwarded to: `DFSCLI.NetDfsSetFtContainerSecurity` |
| 119 | `NetDfsSetInfo` | `0x0` | - | Forwarded | Forwarded to: `DFSCLI.NetDfsSetInfo` |
| 120 | `NetDfsSetSecurity` | `0x0` | - | Forwarded | Forwarded to: `DFSCLI.NetDfsSetSecurity` |
| 121 | `NetDfsSetStdContainerSecurity` | `0x0` | - | Forwarded | Forwarded to: `DFSCLI.NetDfsSetStdContainerSecurity` |
| 122 | `NetEnumerateComputerNames` | `0x0` | - | Forwarded | Forwarded to: `WKSCLI.NetEnumerateComputerNames` |
| 123 | `NetEnumerateServiceAccounts` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.NetEnumerateServiceAccounts` |
| 124 | `NetEnumerateTrustedDomains` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.NetEnumerateTrustedDomains` |
| 128 | `NetFileClose` | `0x0` | - | Forwarded | Forwarded to: `SRVCLI.NetFileClose` |
| 129 | `NetFileEnum` | `0x0` | - | Forwarded | Forwarded to: `SRVCLI.NetFileEnum` |
| 130 | `NetFileGetInfo` | `0x0` | - | Forwarded | Forwarded to: `SRVCLI.NetFileGetInfo` |
| 131 | `NetFreeAadJoinInformation` | `0x0` | - | Forwarded | Forwarded to: `DSREG.DsrFreeJoinInfo` |
| 132 | `NetGetAadJoinInformation` | `0x0` | - | Forwarded | Forwarded to: `DSREG.DsrGetJoinInfo` |
| 133 | `NetGetAnyDCName` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.NetGetAnyDCName` |
| 134 | `NetGetDCName` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.NetGetDCName` |
| 135 | `NetGetDisplayInformationIndex` | `0x0` | - | Forwarded | Forwarded to: `SAMCLI.NetGetDisplayInformationIndex` |
| 136 | `NetGetJoinInformation` | `0x0` | - | Forwarded | Forwarded to: `WKSCLI.NetGetJoinInformation` |
| 137 | `NetGetJoinableOUs` | `0x0` | - | Forwarded | Forwarded to: `WKSCLI.NetGetJoinableOUs` |
| 138 | `NetGroupAdd` | `0x0` | - | Forwarded | Forwarded to: `SAMCLI.NetGroupAdd` |
| 139 | `NetGroupAddUser` | `0x0` | - | Forwarded | Forwarded to: `SAMCLI.NetGroupAddUser` |
| 140 | `NetGroupDel` | `0x0` | - | Forwarded | Forwarded to: `SAMCLI.NetGroupDel` |
| 141 | `NetGroupDelUser` | `0x0` | - | Forwarded | Forwarded to: `SAMCLI.NetGroupDelUser` |
| 142 | `NetGroupEnum` | `0x0` | - | Forwarded | Forwarded to: `SAMCLI.NetGroupEnum` |
| 143 | `NetGroupGetInfo` | `0x0` | - | Forwarded | Forwarded to: `SAMCLI.NetGroupGetInfo` |
| 144 | `NetGroupGetUsers` | `0x0` | - | Forwarded | Forwarded to: `SAMCLI.NetGroupGetUsers` |
| 145 | `NetGroupSetInfo` | `0x0` | - | Forwarded | Forwarded to: `SAMCLI.NetGroupSetInfo` |
| 146 | `NetGroupSetUsers` | `0x0` | - | Forwarded | Forwarded to: `SAMCLI.NetGroupSetUsers` |
| 147 | `NetIsServiceAccount` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.NetIsServiceAccount` |
| 148 | `NetIsServiceAccount2` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.NetIsServiceAccount2` |
| 149 | `NetJoinDomain` | `0x0` | - | Forwarded | Forwarded to: `WKSCLI.NetJoinDomain` |
| 150 | `NetLocalGroupAdd` | `0x0` | - | Forwarded | Forwarded to: `SAMCLI.NetLocalGroupAdd` |
| 151 | `NetLocalGroupAddMember` | `0x0` | - | Forwarded | Forwarded to: `SAMCLI.NetLocalGroupAddMember` |
| 152 | `NetLocalGroupAddMembers` | `0x0` | - | Forwarded | Forwarded to: `SAMCLI.NetLocalGroupAddMembers` |
| 153 | `NetLocalGroupDel` | `0x0` | - | Forwarded | Forwarded to: `SAMCLI.NetLocalGroupDel` |
| 154 | `NetLocalGroupDelMember` | `0x0` | - | Forwarded | Forwarded to: `SAMCLI.NetLocalGroupDelMember` |
| 155 | `NetLocalGroupDelMembers` | `0x0` | - | Forwarded | Forwarded to: `SAMCLI.NetLocalGroupDelMembers` |
| 156 | `NetLocalGroupEnum` | `0x0` | - | Forwarded | Forwarded to: `SAMCLI.NetLocalGroupEnum` |
| 157 | `NetLocalGroupGetInfo` | `0x0` | - | Forwarded | Forwarded to: `SAMCLI.NetLocalGroupGetInfo` |
| 158 | `NetLocalGroupGetMembers` | `0x0` | - | Forwarded | Forwarded to: `SAMCLI.NetLocalGroupGetMembers` |
| 159 | `NetLocalGroupSetInfo` | `0x0` | - | Forwarded | Forwarded to: `SAMCLI.NetLocalGroupSetInfo` |
| 160 | `NetLocalGroupSetMembers` | `0x0` | - | Forwarded | Forwarded to: `SAMCLI.NetLocalGroupSetMembers` |
| 161 | `NetLogonGetTimeServiceParentDomain` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.NetLogonGetTimeServiceParentDomain` |
| 162 | `NetLogonSetServiceBits` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.NetLogonSetServiceBits` |
| 168 | `NetProvisionComputerAccount` | `0x0` | - | Forwarded | Forwarded to: `NETJOIN.NetProvisionComputerAccount` |
| 169 | `NetQueryDisplayInformation` | `0x0` | - | Forwarded | Forwarded to: `SAMCLI.NetQueryDisplayInformation` |
| 170 | `NetQueryServiceAccount` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.NetQueryServiceAccount` |
| 172 | `NetRemoteComputerSupports` | `0x0` | - | Forwarded | Forwarded to: `NETUTILS.NetRemoteComputerSupports` |
| 173 | `NetRemoteTOD` | `0x0` | - | Forwarded | Forwarded to: `SRVCLI.NetRemoteTOD` |
| 174 | `NetRemoveAlternateComputerName` | `0x0` | - | Forwarded | Forwarded to: `WKSCLI.NetRemoveAlternateComputerName` |
| 175 | `NetRemoveServiceAccount` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.NetRemoveServiceAccount` |
| 176 | `NetRenameMachineInDomain` | `0x0` | - | Forwarded | Forwarded to: `WKSCLI.NetRenameMachineInDomain` |
| 192 | `NetRequestOfflineDomainJoin` | `0x0` | - | Forwarded | Forwarded to: `NETJOIN.NetRequestOfflineDomainJoin` |
| 193 | `NetRequestProvisioningPackageInstall` | `0x0` | - | Forwarded | Forwarded to: `NETJOIN.NetRequestProvisioningPackageInstall` |
| 194 | `NetScheduleJobAdd` | `0x0` | - | Forwarded | Forwarded to: `SCHEDCLI.NetScheduleJobAdd` |
| 195 | `NetScheduleJobDel` | `0x0` | - | Forwarded | Forwarded to: `SCHEDCLI.NetScheduleJobDel` |
| 196 | `NetScheduleJobEnum` | `0x0` | - | Forwarded | Forwarded to: `SCHEDCLI.NetScheduleJobEnum` |
| 197 | `NetScheduleJobGetInfo` | `0x0` | - | Forwarded | Forwarded to: `SCHEDCLI.NetScheduleJobGetInfo` |
| 198 | `NetServerAliasAdd` | `0x0` | - | Forwarded | Forwarded to: `SRVCLI.NetServerAliasAdd` |
| 199 | `NetServerAliasDel` | `0x0` | - | Forwarded | Forwarded to: `SRVCLI.NetServerAliasDel` |
| 200 | `NetServerAliasEnum` | `0x0` | - | Forwarded | Forwarded to: `SRVCLI.NetServerAliasEnum` |
| 201 | `NetServerComputerNameAdd` | `0x0` | - | Forwarded | Forwarded to: `SRVCLI.NetServerComputerNameAdd` |
| 202 | `NetServerComputerNameDel` | `0x0` | - | Forwarded | Forwarded to: `SRVCLI.NetServerComputerNameDel` |
| 203 | `NetServerDiskEnum` | `0x0` | - | Forwarded | Forwarded to: `SRVCLI.NetServerDiskEnum` |
| 206 | `NetServerGetInfo` | `0x0` | - | Forwarded | Forwarded to: `SRVCLI.NetServerGetInfo` |
| 207 | `NetServerSetInfo` | `0x0` | - | Forwarded | Forwarded to: `SRVCLI.NetServerSetInfo` |
| 208 | `NetServerTransportAdd` | `0x0` | - | Forwarded | Forwarded to: `SRVCLI.NetServerTransportAdd` |
| 209 | `NetServerTransportAddEx` | `0x0` | - | Forwarded | Forwarded to: `SRVCLI.NetServerTransportAddEx` |
| 210 | `NetServerTransportDel` | `0x0` | - | Forwarded | Forwarded to: `SRVCLI.NetServerTransportDel` |
| 211 | `NetServerTransportEnum` | `0x0` | - | Forwarded | Forwarded to: `SRVCLI.NetServerTransportEnum` |
| 216 | `NetSessionDel` | `0x0` | - | Forwarded | Forwarded to: `SRVCLI.NetSessionDel` |
| 217 | `NetSessionEnum` | `0x0` | - | Forwarded | Forwarded to: `SRVCLI.NetSessionEnum` |
| 218 | `NetSessionGetInfo` | `0x0` | - | Forwarded | Forwarded to: `SRVCLI.NetSessionGetInfo` |
| 219 | `NetSetPrimaryComputerName` | `0x0` | - | Forwarded | Forwarded to: `WKSCLI.NetSetPrimaryComputerName` |
| 220 | `NetShareAdd` | `0x0` | - | Forwarded | Forwarded to: `SRVCLI.NetShareAdd` |
| 221 | `NetShareCheck` | `0x0` | - | Forwarded | Forwarded to: `SRVCLI.NetShareCheck` |
| 222 | `NetShareDel` | `0x0` | - | Forwarded | Forwarded to: `SRVCLI.NetShareDel` |
| 223 | `NetShareDelEx` | `0x0` | - | Forwarded | Forwarded to: `SRVCLI.NetShareDelEx` |
| 224 | `NetShareDelSticky` | `0x0` | - | Forwarded | Forwarded to: `SRVCLI.NetShareDelSticky` |
| 225 | `NetShareEnum` | `0x0` | - | Forwarded | Forwarded to: `SRVCLI.NetShareEnum` |
| 226 | `NetShareEnumSticky` | `0x0` | - | Forwarded | Forwarded to: `SRVCLI.NetShareEnumSticky` |
| 227 | `NetShareGetInfo` | `0x0` | - | Forwarded | Forwarded to: `SRVCLI.NetShareGetInfo` |
| 228 | `NetShareSetInfo` | `0x0` | - | Forwarded | Forwarded to: `SRVCLI.NetShareSetInfo` |
| 230 | `NetUnjoinDomain` | `0x0` | - | Forwarded | Forwarded to: `WKSCLI.NetUnjoinDomain` |
| 232 | `NetUseAdd` | `0x0` | - | Forwarded | Forwarded to: `WKSCLI.NetUseAdd` |
| 233 | `NetUseDel` | `0x0` | - | Forwarded | Forwarded to: `WKSCLI.NetUseDel` |
| 234 | `NetUseEnum` | `0x0` | - | Forwarded | Forwarded to: `WKSCLI.NetUseEnum` |
| 235 | `NetUseGetInfo` | `0x0` | - | Forwarded | Forwarded to: `WKSCLI.NetUseGetInfo` |
| 236 | `NetUserAdd` | `0x0` | - | Forwarded | Forwarded to: `SAMCLI.NetUserAdd` |
| 237 | `NetUserChangePassword` | `0x0` | - | Forwarded | Forwarded to: `SAMCLI.NetUserChangePassword` |
| 238 | `NetUserDel` | `0x0` | - | Forwarded | Forwarded to: `SAMCLI.NetUserDel` |
| 239 | `NetUserEnum` | `0x0` | - | Forwarded | Forwarded to: `SAMCLI.NetUserEnum` |
| 240 | `NetUserGetGroups` | `0x0` | - | Forwarded | Forwarded to: `SAMCLI.NetUserGetGroups` |
| 241 | `NetUserGetInfo` | `0x0` | - | Forwarded | Forwarded to: `SAMCLI.NetUserGetInfo` |
| 242 | `NetUserGetLocalGroups` | `0x0` | - | Forwarded | Forwarded to: `SAMCLI.NetUserGetLocalGroups` |
| 243 | `NetUserModalsGet` | `0x0` | - | Forwarded | Forwarded to: `SAMCLI.NetUserModalsGet` |
| 244 | `NetUserModalsSet` | `0x0` | - | Forwarded | Forwarded to: `SAMCLI.NetUserModalsSet` |
| 245 | `NetUserSetGroups` | `0x0` | - | Forwarded | Forwarded to: `SAMCLI.NetUserSetGroups` |
| 246 | `NetUserSetInfo` | `0x0` | - | Forwarded | Forwarded to: `SAMCLI.NetUserSetInfo` |
| 247 | `NetValidateName` | `0x0` | - | Forwarded | Forwarded to: `WKSCLI.NetValidateName` |
| 248 | `NetValidatePasswordPolicy` | `0x0` | - | Forwarded | Forwarded to: `SAMCLI.NetValidatePasswordPolicy` |
| 249 | `NetValidatePasswordPolicyFree` | `0x0` | - | Forwarded | Forwarded to: `SAMCLI.NetValidatePasswordPolicyFree` |
| 252 | `NetWkstaTransportAdd` | `0x0` | - | Forwarded | Forwarded to: `WKSCLI.NetWkstaTransportAdd` |
| 253 | `NetWkstaTransportDel` | `0x0` | - | Forwarded | Forwarded to: `WKSCLI.NetWkstaTransportDel` |
| 254 | `NetWkstaTransportEnum` | `0x0` | - | Forwarded | Forwarded to: `WKSCLI.NetWkstaTransportEnum` |
| 255 | `NetWkstaUserEnum` | `0x0` | - | Forwarded | Forwarded to: `WKSCLI.NetWkstaUserEnum` |
| 256 | `NetWkstaUserGetInfo` | `0x0` | - | Forwarded | Forwarded to: `WKSCLI.NetWkstaUserGetInfo` |
| 257 | `NetWkstaUserSetInfo` | `0x0` | - | Forwarded | Forwarded to: `WKSCLI.NetWkstaUserSetInfo` |
| 258 | `NetapipBufferAllocate` | `0x0` | - | Forwarded | Forwarded to: `NETUTILS.NetapipBufferAllocate` |
| 274 | `NetpIsRemote` | `0x0` | - | Forwarded | Forwarded to: `NETUTILS.NetpIsRemote` |
| 281 | `NetpwNameCanonicalize` | `0x0` | - | Forwarded | Forwarded to: `NETUTILS.NetpwNameCanonicalize` |
| 282 | `NetpwNameCompare` | `0x0` | - | Forwarded | Forwarded to: `NETUTILS.NetpwNameCompare` |
| 283 | `NetpwNameValidate` | `0x0` | - | Forwarded | Forwarded to: `NETUTILS.NetpwNameValidate` |
| 284 | `NetpwPathCanonicalize` | `0x0` | - | Forwarded | Forwarded to: `NETUTILS.NetpwPathCanonicalize` |
| 285 | `NetpwPathCompare` | `0x0` | - | Forwarded | Forwarded to: `NETUTILS.NetpwPathCompare` |
| 286 | `NetpwPathType` | `0x0` | - | Forwarded | Forwarded to: `NETUTILS.NetpwPathType` |
| 287 | `NlBindingAddServerToCache` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.NlBindingAddServerToCache` |
| 288 | `NlBindingRemoveServerFromCache` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.NlBindingRemoveServerFromCache` |
| 289 | `NlBindingSetAuthInfo` | `0x0` | - | Forwarded | Forwarded to: `LOGONCLI.NlBindingSetAuthInfo` |
| 250 | `NetWkstaGetInfo` | `0x1010` | 216 | UnwindData |  |
| 259 | `Netbios` | `0x1160` | 156 | UnwindData |  |
| 229 | `NetStatisticsGet` | `0x1210` | 185 | UnwindData |  |
| 275 | `NetpIsUncComputerNameValid` | `0x21A0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `NetAccessAdd` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `NetAccessDel` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `NetAccessEnum` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `NetAccessGetInfo` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `NetAccessGetUserPerms` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `NetAccessSetInfo` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `NetAlertRaise` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `NetAlertRaiseEx` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `NetAuditClear` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `NetAuditRead` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `NetAuditWrite` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `NetConfigGet` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `NetConfigGetAll` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `NetConfigSet` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `NetErrorLogClear` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `NetErrorLogRead` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `NetErrorLogWrite` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 163 | `NetMessageBufferSend` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 164 | `NetMessageNameAdd` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 165 | `NetMessageNameDel` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `NetMessageNameEnum` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 167 | `NetMessageNameGetInfo` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 177 | `NetReplExportDirAdd` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 178 | `NetReplExportDirDel` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `NetReplExportDirEnum` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 180 | `NetReplExportDirGetInfo` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `NetReplExportDirLock` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 182 | `NetReplExportDirSetInfo` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `NetReplExportDirUnlock` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | `NetReplGetInfo` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `NetReplImportDirAdd` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `NetReplImportDirDel` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 187 | `NetReplImportDirEnum` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 188 | `NetReplImportDirGetInfo` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 189 | `NetReplImportDirLock` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `NetReplImportDirUnlock` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 191 | `NetReplSetInfo` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 271 | `NetpGetFileSecurity` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 280 | `NetpSetFileSecurity` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 290 | `RxNetAccessAdd` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 291 | `RxNetAccessDel` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 292 | `RxNetAccessEnum` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 293 | `RxNetAccessGetInfo` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 294 | `RxNetAccessGetUserPerms` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 295 | `RxNetAccessSetInfo` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 297 | `RxNetUserPasswordSet` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `I_BrowserSetNetlogonState` | `0x2200` | 94 | UnwindData |  |
| 204 | `NetServerEnum` | `0x2270` | 155 | UnwindData |  |
| 205 | `NetServerEnumEx` | `0x2320` | 155 | UnwindData |  |
| 262 | `NetpAssertFailed` | `0x23D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 272 | `NetpHexDump` | `0x23D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 266 | `NetpDbgPrint` | `0x23E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 277 | `NetpNetBiosReset` | `0x2400` | 111 | UnwindData |  |
| 278 | `NetpNetBiosStatusToApiStatus` | `0x2480` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 171 | `NetRegisterDomainNameChangeNotification` | `0x2510` | 158 | UnwindData |  |
| 231 | `NetUnregisterDomainNameChangeNotification` | `0x25C0` | 85 | UnwindData |  |
| 251 | `NetWkstaSetInfo` | `0x2620` | 145 | UnwindData |  |
| 212 | `NetServiceControl` | `0x26C0` | 148 | UnwindData |  |
| 213 | `NetServiceEnum` | `0x2760` | 172 | UnwindData |  |
| 214 | `NetServiceGetInfo` | `0x2820` | 149 | UnwindData |  |
| 215 | `NetServiceInstall` | `0x28C0` | 163 | UnwindData |  |
| 296 | `RxNetServerEnum` | `0x3C70` | 772 | UnwindData |  |
| 298 | `RxRemoteApi` | `0x4570` | 819 | UnwindData |  |
| 260 | `NetpAddTlnFtinfoEntry` | `0x6EA0` | 240 | UnwindData |  |
| 261 | `NetpAllocFtinfoEntry` | `0x6FA0` | 131 | UnwindData |  |
| 263 | `NetpCleanFtinfoContext` | `0x7590` | 92 | UnwindData |  |
| 265 | `NetpCopyFtinfoContext` | `0x7A40` | 485 | UnwindData |  |
| 273 | `NetpInitFtinfoContext` | `0x7EC0` | 1,856 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 276 | `NetpMergeFtinfo` | `0x8600` | 253 | UnwindData |  |
| 264 | `NetpCloseConfigData` | `0x9450` | 51 | UnwindData |  |
| 267 | `NetpGetConfigBool` | `0x9490` | 412 | UnwindData |  |
| 268 | `NetpGetConfigDword` | `0x9640` | 488 | UnwindData |  |
| 269 | `NetpGetConfigTStrArray` | `0x9830` | 216 | UnwindData |  |
| 270 | `NetpGetConfigValue` | `0x9910` | 276 | UnwindData |  |
| 279 | `NetpOpenConfigData` | `0x9A30` | 8,800 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
