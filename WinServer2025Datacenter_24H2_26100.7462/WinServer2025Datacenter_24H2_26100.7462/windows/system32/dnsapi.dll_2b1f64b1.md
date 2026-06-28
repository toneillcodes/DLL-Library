# Binary Specification: dnsapi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\dnsapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2b1f64b134fb835d92ddca88e2d1d2e30f105866df062eb632d4fba052c4c591`
* **Total Exported Functions:** 351

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 44 | `DnsConnectionDeletePolicyEntriesPrivate` | `0x22A0` | 168 | UnwindData |  |
| 59 | `DnsConnectionUpdateIfIndexTable` | `0x27A0` | 82 | UnwindData |  |
| 48 | `DnsConnectionFreeProxyInfoEx` | `0x37A0` | 63 | UnwindData |  |
| 54 | `DnsConnectionGetProxyInfoForHostUrlEx` | `0x37F0` | 154 | UnwindData |  |
| 351 | `Socket_SetMulticastInterface` | `0xA160` | 416 | UnwindData |  |
| 31 | `DnsApiOnNetworkChange` | `0xA340` | 140 | UnwindData |  |
| 346 | `Socket_Create` | `0xAFA0` | 28 | UnwindData |  |
| 344 | `Socket_CloseEx` | `0xBB70` | 133 | UnwindData |  |
| 17 | `CreateSendBlob` | `0xE0A0` | 214 | UnwindData |  |
| 88 | `DnsFlushResolverCacheEntry_W` | `0xE970` | 438 | UnwindData |  |
| 13 | `AddRefQueryBlobEx` | `0x138F0` | 84 | UnwindData |  |
| 290 | `Dns_SetRecordsScopeId` | `0x15080` | 252 | UnwindData |  |
| 258 | `Dns_AddRecordsToMessage` | `0x192E0` | 917 | UnwindData |  |
| 338 | `Send_MessagePrivateEx` | `0x1A810` | 754 | UnwindData |  |
| 41 | `DnsCheckNrptRules` | `0x25390` | 424 | UnwindData |  |
| 128 | `DnsGetProxyInfoPrivate` | `0x27550` | 857 | UnwindData |  |
| 306 | `HostsFile_ReadLine` | `0x29180` | 239 | UnwindData |  |
| 323 | `NetInfo_ResetServerPriorities` | `0x2C600` | 280 | UnwindData |  |
| 311 | `NetInfo_BuildEx` | `0x2C720` | 1,627 | UnwindData |  |
| 313 | `NetInfo_Copy` | `0x2D8E0` | 193 | UnwindData |  |
| 316 | `NetInfo_Free` | `0x2E830` | 72 | UnwindData |  |
| 315 | `NetInfo_CreatePerNetworkNetinfo` | `0x300F0` | 1,057 | UnwindData |  |
| 231 | `DnsTraceServerConfig` | `0x305A0` | 313 | UnwindData |  |
| 319 | `NetInfo_GetAdapterByName` | `0x30ED0` | 213 | UnwindData |  |
| 170 | `DnsQueryConfig` | `0x33BF0` | 1,029 | UnwindData |  |
| 29 | `DnsApiFree` | `0x353C0` | 73 | UnwindData |  |
| 120 | `DnsGetInterfaceSettingsInProc` | `0x35EB0` | 28 | UnwindData |  |
| 108 | `DnsGetApplicationIdentifier` | `0x37DE0` | 1,004 | UnwindData |  |
| 50 | `DnsConnectionGetHandleForHostUrlPrivate` | `0x38D30` | 392 | UnwindData |  |
| 309 | `Local_GetRecordsForLocalNameEx` | `0x3A7A0` | 163 | UnwindData |  |
| 332 | `Reg_GetValueEx` | `0x3A850` | 30 | UnwindData |  |
| 243 | `DnsValidateName_W` | `0x3C2C0` | 495 | UnwindData |  |
| 333 | `Reg_ReadGlobalsEx` | `0x3C930` | 174 | UnwindData |  |
| 282 | `Dns_ReadPacketName` | `0x3CEB0` | 53 | UnwindData |  |
| 297 | `Dns_WriteDottedNameToPacket` | `0x3D770` | 718 | UnwindData |  |
| 259 | `Dns_AllocateMsgBuf` | `0x3FCB0` | 234 | UnwindData |  |
| 274 | `Dns_GetRandomXid` | `0x3FE20` | 130 | UnwindData |  |
| 260 | `Dns_BuildPacket` | `0x403B0` | 53 | UnwindData |  |
| 304 | `HostsFile_Close` | `0x428E0` | 68 | UnwindData |  |
| 305 | `HostsFile_Open` | `0x42930` | 660 | UnwindData |  |
| 359 | `Util_IsRunningOnXboxOne` | `0x42E30` | 61 | UnwindData |  |
| 171 | `DnsQueryConfigAllocEx` | `0x43220` | 500 | UnwindData |  |
| 161 | `DnsNameCompare_W` | `0x446C0` | 161 | UnwindData |  |
| 129 | `DnsGetProxyInformation` | `0x448D0` | 38 | UnwindData |  |
| 92 | `DnsFreeCustomServers` | `0x44DB0` | 174 | UnwindData |  |
| 119 | `DnsGetInterfaceSettings` | `0x44E70` | 363 | UnwindData |  |
| 67 | `DnsDhcpRegisterAddrs` | `0x451C0` | 190 | UnwindData |  |
| 111 | `DnsGetCacheDataTable` | `0x454B0` | 29 | UnwindData |  |
| 112 | `DnsGetCacheDataTableEx` | `0x454E0` | 460 | UnwindData |  |
| 202 | `DnsResolverOp` | `0x456C0` | 435 | UnwindData |  |
| 130 | `DnsGetProxyInformationEx` | `0x45880` | 497 | UnwindData |  |
| 132 | `DnsGetSettings` | `0x45CA0` | 313 | UnwindData |  |
| 180 | `DnsQuery_UTF8` | `0x45DE0` | 87 | UnwindData |  |
| 179 | `DnsQuery_A` | `0x45E40` | 87 | UnwindData |  |
| 107 | `DnsGetAdaptersInfo` | `0x46D60` | 541 | UnwindData |  |
| 173 | `DnsQueryEx` | `0x47240` | 1,140 | UnwindData |  |
| 181 | `DnsQuery_W` | `0x47E50` | 452 | UnwindData |  |
| 357 | `Update_ReplaceAddressRecordsW` | `0x49810` | 40 | UnwindData |  |
| 317 | `NetInfo_GetAdapterByAddress` | `0x4AE70` | 188 | UnwindData |  |
| 22 | `DnsAddrArrayAddAddr` | `0x4B2F0` | 140 | UnwindData |  |
| 320 | `NetInfo_IsAddrConfig` | `0x4B760` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `DnsAddrBuildFromDnsRecord` | `0x4B8C0` | 414 | UnwindData |  |
| 307 | `IpHelp_IsAddrOnLink` | `0x4BB40` | 253 | UnwindData |  |
| 271 | `Dns_ExtractRecordsFromMessage` | `0x4F0A0` | 475 | UnwindData |  |
| 279 | `Dns_ParseMessage` | `0x4FB70` | 2,619 | UnwindData |  |
| 328 | `Query_Cancel` | `0x50600` | 574 | UnwindData |  |
| 18 | `DeRefQueryBlobEx` | `0x50850` | 25 | UnwindData |  |
| 273 | `Dns_FreeMsgBuf` | `0x50D30` | 131 | UnwindData |  |
| 89 | `DnsFree` | `0x50E20` | 394 | UnwindData |  |
| 312 | `NetInfo_Clean` | `0x53A00` | 203 | UnwindData |  |
| 308 | `Local_GetRecordsForLocalName` | `0x53C00` | 130 | UnwindData |  |
| 131 | `DnsGetQueryRetryTimeouts` | `0x55470` | 429 | UnwindData |  |
| 213 | `DnsServiceResolve` | `0x586D0` | 214 | UnwindData |  |
| 205 | `DnsServiceBrowse` | `0x58D10` | 650 | UnwindData |  |
| 228 | `DnsStopMulticastQuery` | `0x593C0` | 446 | UnwindData |  |
| 211 | `DnsServiceRegister` | `0x5A5F0` | 462 | UnwindData |  |
| 209 | `DnsServiceDeRegister` | `0x5A7D0` | 273 | UnwindData |  |
| 355 | `ThreadPool_QueueWork` | `0x5AC30` | 148 | UnwindData |  |
| 208 | `DnsServiceCopyInstance` | `0x5BBD0` | 91 | UnwindData |  |
| 207 | `DnsServiceConstructInstance` | `0x5C680` | 859 | UnwindData |  |
| 64 | `DnsDeRegisterLocal` | `0x5D350` | 114 | UnwindData |  |
| 98 | `DnsFreeWellKnownServerProperty` | `0x5DAF0` | 93 | UnwindData |  |
| 90 | `DnsFreeAdaptersInfo` | `0x5ED00` | 11 | UnwindData |  |
| 350 | `Socket_RecvFrom` | `0x5EFB0` | 513 | UnwindData |  |
| 284 | `Dns_ReadRecordStructureFromPacket` | `0x614D0` | 293 | UnwindData |  |
| 28 | `DnsApiAllocZero` | `0x62E60` | 3,008 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 318 | `NetInfo_GetAdapterByInterfaceIndex` | `0x63A20` | 148 | UnwindData |  |
| 109 | `DnsGetApplicationSettings` | `0x64400` | 386 | UnwindData |  |
| 293 | `Dns_SkipPacketName` | `0x64DE0` | 173 | UnwindData |  |
| 353 | `Socket_SetTtl` | `0x64F00` | 339 | UnwindData |  |
| 172 | `DnsQueryConfigDword` | `0x65150` | 192 | UnwindData |  |
| 336 | `Send_AndRecvUdpWithParam` | `0x67320` | 1,887 | UnwindData |  |
| 167 | `DnsNotifyResolver` | `0x69370` | 135 | UnwindData |  |
| 298 | `Dns_WriteQuestionToMessage` | `0x699F0` | 245 | UnwindData |  |
| 229 | `DnsStringCopyAllocateEx` | `0x6A1B0` | 2,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 326 | `NetInfo_UpdateServerReachability` | `0x6AD20` | 166 | UnwindData |  |
| 334 | `Reg_ReadUpdateInfo` | `0x6ADD0` | 634 | UnwindData |  |
| 343 | `Socket_ClearMessageSockets` | `0x6B490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 349 | `Socket_JoinMulticast` | `0x6B4B0` | 308 | UnwindData |  |
| 322 | `NetInfo_IsTcpipConfigChange` | `0x6BAF0` | 229 | UnwindData |  |
| 352 | `Socket_SetMulticastLoopBack` | `0x6C180` | 204 | UnwindData |  |
| 210 | `DnsServiceFreeInstance` | `0x6C610` | 155 | UnwindData |  |
| 19 | `DelaySortDAServerlist` | `0x6D720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 329 | `Query_InProcSetCompletion` | `0x6D740` | 136 | UnwindData |  |
| 40 | `DnsCheckNrptRuleIntegrity` | `0x6D7D0` | 1,146 | UnwindData |  |
| 325 | `NetInfo_UpdateNetworkProperties` | `0x6DE10` | 526 | UnwindData |  |
| 166 | `DnsNotifyProxyConfigChangePrivate` | `0x6E110` | 243 | UnwindData |  |
| 126 | `DnsGetPolicyTableInfoPrivate` | `0x6E360` | 283 | UnwindData |  |
| 331 | `Reg_FreeUpdateInfo` | `0x6EFF0` | 108 | UnwindData |  |
| 206 | `DnsServiceBrowseCancel` | `0x6F110` | 168 | UnwindData |  |
| 24 | `DnsAddrArrayCreate` | `0x71670` | 4,480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 299 | `Dns_WriteRecordStructureToPacketEx` | `0x727F0` | 121 | UnwindData |  |
| 314 | `NetInfo_CopyNetworkIndex` | `0x73760` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 303 | `GetCurrentTimeInSeconds` | `0x73800` | 52 | UnwindData |  |
| 94 | `DnsFreeNrptRule` | `0x73A90` | 229 | UnwindData |  |
| 124 | `DnsGetNrptRuleNamesList` | `0x73BD0` | 1,076 | UnwindData |  |
| 15 | `Coalesce_UpdateNetVersion` | `0x741A0` | 3,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 356 | `Trace_Reset` | `0x750F0` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 218 | `DnsSetInterfaceSettings` | `0x752F0` | 363 | UnwindData |  |
| 162 | `DnsNameCopy` | `0x757E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `AdaptiveTimeout_ResetAdaptiveTimeout` | `0x757F0` | 111 | UnwindData |  |
| 291 | `Dns_SetRecordsSection` | `0x75870` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `DnsFreeConfigStructure` | `0x759D0` | 131 | UnwindData |  |
| 11 | `AdaptiveTimeout_ClearInterfaceSpecificConfiguration` | `0x762E0` | 107 | UnwindData |  |
| 292 | `Dns_SetRecordsTtl` | `0x76390` | 896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `DnsConnectionGetProxyInfo` | `0x76710` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 196 | `DnsRemoveNrptRule` | `0x76830` | 785 | UnwindData |  |
| 96 | `DnsFreePolicyConfig` | `0x76FB0` | 208 | UnwindData |  |
| 169 | `DnsNotifyResolverEx` | `0x77090` | 68 | UnwindData |  |
| 133 | `DnsGetWellKnownServerProperty` | `0x771F0` | 372 | UnwindData |  |
| 47 | `DnsConnectionFreeProxyInfo` | `0x77980` | 1,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 214 | `DnsServiceResolveCancel` | `0x77DC0` | 166 | UnwindData |  |
| 186 | `DnsRecordListFree` | `0x78370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 324 | `NetInfo_UpdateDnsInterfaceConfigChange` | `0x78390` | 96 | UnwindData |  |
| 160 | `DnsNameCompare_UTF8` | `0x78440` | 2,832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `DnsRecordCopyEx` | `0x78F50` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `DnsGetPolicyTableInfo` | `0x78FD0` | 265 | UnwindData |  |
| 212 | `DnsServiceRegisterCancel` | `0x79DA0` | 160 | UnwindData |  |
| 86 | `DnsFlushResolverCacheEntry_A` | `0x79E50` | 1,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | `DnsLogEvent` | `0x7A270` | 299 | UnwindData |  |
| 226 | `DnsStartMulticastQuery` | `0x7A3B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 337 | `Send_MessagePrivate` | `0x7A3C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 301 | `Faz_AreServerListsInSameNameSpace` | `0x7A3D0` | 336 | UnwindData |  |
| 203 | `DnsResolverQueryHvsi` | `0x7A5A0` | 433 | UnwindData |  |
| 283 | `Dns_ReadPacketNameAllocate` | `0x7B3A0` | 240 | UnwindData |  |
| 300 | `ExtraInfo_Init` | `0x7B4A0` | 54 | UnwindData |  |
| 234 | `DnsUpdateCaptivePortalPresence` | `0x7B770` | 86 | UnwindData |  |
| 187 | `DnsRecordListUnmapV4MappedAAAAInPlace` | `0x7B830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `DnsCancelQuery` | `0x7B840` | 474 | UnwindData |  |
| 242 | `DnsValidateName_UTF8` | `0x7BA70` | 160 | UnwindData |  |
| 69 | `DnsDhcpRegisterInit` | `0x7C3C0` | 36 | UnwindData |  |
| 95 | `DnsFreeNrptRuleNamesList` | `0x7C540` | 82 | UnwindData |  |
| 216 | `DnsSetConfigDword` | `0x7C620` | 64 | UnwindData |  |
| 57 | `DnsConnectionSetPolicyEntriesPrivate` | `0x7C920` | 177 | UnwindData |  |
| 27 | `DnsApiAlloc` | `0x7D580` | 6,080 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 330 | `Query_Main` | `0x7ED40` | 1,096 | UnwindData |  |
| 275 | `Dns_InitializeMsgBuf` | `0x7F380` | 188 | UnwindData |  |
| 220 | `DnsSetNrptRules` | `0x7FF60` | 645 | UnwindData |  |
| 360 | `WriteDnsNrptRulesToRegistry` | `0x80860` | 169 | UnwindData |  |
| 235 | `DnsUpdateMachinePresence` | `0x80960` | 1,116 | UnwindData |  |
| 302 | `FlushDnsPolicyUnreachableStatus` | `0x80DD0` | 77 | UnwindData |  |
| 345 | `Socket_CloseMessageSockets` | `0x81050` | 26 | UnwindData |  |
| 85 | `DnsFlushResolverCache` | `0x87520` | 303 | UnwindData |  |
| 294 | `Dns_SkipToRecord` | `0x877E0` | 224 | UnwindData |  |
| 217 | `DnsSetConfigValue` | `0x885C0` | 203 | UnwindData |  |
| 143 | `DnsIp6ReverseNameToAddressW` | `0x889F0` | 1,552 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `DnsFreeZtTrustedServers` | `0x89000` | 102 | UnwindData |  |
| 127 | `DnsGetPrimaryDomainName_A` | `0x890E0` | 1,808 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 230 | `DnsStringToAddress` | `0x897F0` | 1,232 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `DnsFreeProxyName` | `0x89CC0` | 20 | UnwindData |  |
| 163 | `DnsNameCopyAllocate` | `0x89D50` | 9,136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `DnsDhcpRegisterHostAddrs` | `0x8C100` | 145 | UnwindData |  |
| 36 | `DnsAsyncRegisterTerm` | `0x8C1A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `DnsDhcpRegisterTerm` | `0x8C1A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 262 | `Dns_CacheServiceInit` | `0x8C1A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 341 | `Socket_CacheInit` | `0x8C1A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `DnsDhcpRemoveRegistrations` | `0x8C1B0` | 85 | UnwindData |  |
| 72 | `DnsDhcpSrvRegisterHostAddr` | `0x8CD70` | 156 | UnwindData |  |
| 73 | `DnsDhcpSrvRegisterHostAddrEx` | `0x8CE20` | 104 | UnwindData |  |
| 74 | `DnsDhcpSrvRegisterHostName` | `0x8CE90` | 108 | UnwindData |  |
| 75 | `DnsDhcpSrvRegisterHostNameEx` | `0x8CF10` | 359 | UnwindData |  |
| 76 | `DnsDhcpSrvRegisterInit` | `0x8D080` | 533 | UnwindData |  |
| 77 | `DnsDhcpSrvRegisterInitEx` | `0x8D2A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `DnsDhcpSrvRegisterTerm` | `0x8D2C0` | 251 | UnwindData |  |
| 261 | `Dns_CacheServiceCleanup` | `0x8E750` | 269 | UnwindData |  |
| 263 | `Dns_CacheServiceInitEx` | `0x8E870` | 862 | UnwindData |  |
| 264 | `Dns_CacheServiceStopIssued` | `0x8EBE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `DnsBuildDotHost` | `0x8EC00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `DnsDeleteSettings` | `0x8EC10` | 304 | UnwindData |  |
| 66 | `DnsDeleteWellKnownServerProperty` | `0x8ED50` | 330 | UnwindData |  |
| 93 | `DnsFreeNetworkServers` | `0x8EEA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `DnsFreeWellKnownServerPropertyEx` | `0x8EEB0` | 143 | UnwindData |  |
| 100 | `DnsFreeWellKnownServers` | `0x8EF50` | 104 | UnwindData |  |
| 113 | `DnsGetCacheRecords` | `0x8EFC0` | 426 | UnwindData |  |
| 122 | `DnsGetNetworkServers` | `0x8F170` | 491 | UnwindData |  |
| 134 | `DnsGetWellKnownServers` | `0x8F370` | 392 | UnwindData |  |
| 10 | `DnsIsZtEnabled` | `0x8F500` | 216 | UnwindData |  |
| 201 | `DnsResetQueryRetryTimeouts` | `0x8F5E0` | 153 | UnwindData |  |
| 221 | `DnsSetQueryRetryTimeouts` | `0x8F680` | 329 | UnwindData |  |
| 222 | `DnsSetSettings` | `0x8F7D0` | 304 | UnwindData |  |
| 223 | `DnsSetWellKnownServerProperty` | `0x8F910` | 351 | UnwindData |  |
| 225 | `DnsSplitDotHost` | `0x8FA80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 257 | `DnsZtNotifyDnscache` | `0x8FA90` | 460 | UnwindData |  |
| 23 | `DnsAddrArrayAddIp4` | `0x8FD30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `DnsAllocateRecord` | `0x8FD40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `DnsAsyncRegisterHostAddrs` | `0x8FD50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `DnsAsyncRegisterInit` | `0x8FD60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `DnsCopyStringEx` | `0x8FD70` | 62 | UnwindData |  |
| 61 | `DnsCreateReverseNameStringForIpAddress` | `0x8FDC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `DnsCreateStandardDnsNameCopy` | `0x8FDD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `DnsCreateStringCopy` | `0x8FDE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `DnsDhcpSrvRegisterInitialize` | `0x8FDF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `DnsDowncaseDnsNameLabel` | `0x8FE00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `DnsGetBufferLengthForStringCopy` | `0x8FE10` | 38 | UnwindData |  |
| 117 | `DnsGetDnsServerList` | `0x8FE40` | 33 | UnwindData |  |
| 118 | `DnsGetDomainName` | `0x8FE70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `DnsIp6AddressToReverseNameW` | `0x8FEA0` | 29 | UnwindData |  |
| 144 | `DnsIpv6AddressToString` | `0x8FED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `DnsIpv6StringToAddress` | `0x8FEF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `DnsIsAMailboxType` | `0x8FF00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `DnsIsFlatRecord` | `0x8FF20` | 122 | UnwindData |  |
| 148 | `DnsIsNSECType` | `0x8FFA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `DnsIsStatusRcode` | `0x8FFC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `DnsIsStringCountValidForTextType` | `0x8FFD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `DnsMapRcodeToStatus` | `0x8FFE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `DnsNameCompareEx_A` | `0x8FFF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `DnsNameCompareEx_UTF8` | `0x90010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 158 | `DnsNameCompareEx_W` | `0x90030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `DnsNameCompare_A` | `0x90050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 182 | `DnsRecordBuild_UTF8` | `0x90060` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `DnsRecordBuild_W` | `0x90070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | `DnsRecordCompare` | `0x90080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 188 | `DnsRecordSetCompare` | `0x90090` | 24 | UnwindData |  |
| 189 | `DnsRecordSetCopyEx` | `0x900B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `DnsRecordSetDetach` | `0x900D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 191 | `DnsRecordStringForType` | `0x900E0` | 32 | UnwindData |  |
| 192 | `DnsRecordStringForWritableType` | `0x90110` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 193 | `DnsRecordTypeForName` | `0x90150` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 197 | `DnsRemoveRegistrations` | `0x90160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 227 | `DnsStatusString` | `0x90170` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 232 | `DnsUnicodeToUtf8` | `0x901B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 239 | `DnsUtf8ToUnicode` | `0x901C0` | 48 | UnwindData |  |
| 241 | `DnsValidateName_A` | `0x90200` | 227 | UnwindData |  |
| 249 | `DnsValidateUtf8Byte` | `0x902F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 252 | `DnsWriteReverseNameStringForIpAddress` | `0x90300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 253 | `DnsWriteReverseNameStringForIpAddressW` | `0x90310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 266 | `Dns_CloseConnection` | `0x90320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 267 | `Dns_CloseSocket` | `0x90330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 269 | `Dns_CreateSocket` | `0x90340` | 34 | UnwindData |  |
| 270 | `Dns_CreateSocketEx` | `0x90370` | 153 | UnwindData |  |
| 335 | `Security_ContextListTimeout` | `0x90410` | 1,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 204 | `DnsScreenLocalAddrsForRegistration` | `0x90B90` | 257 | UnwindData |  |
| 32 | `DnsApiRealloc` | `0x90E30` | 79 | UnwindData |  |
| 240 | `DnsValidateNameOrIp_TempW` | `0x90E90` | 269 | UnwindData |  |
| 286 | `Dns_ResetNetworkInfo` | `0x91250` | 88 | UnwindData |  |
| 310 | `NetInfo_Build` | `0x91430` | 49 | UnwindData |  |
| 84 | `DnsFindAuthoritativeZone` | `0x91E20` | 303 | UnwindData |  |
| 164 | `DnsNetworkInfo_CreateFromFAZ` | `0x91F60` | 299 | UnwindData |  |
| 165 | `DnsNetworkInformation_CreateFromFAZ` | `0x92250` | 318 | UnwindData |  |
| 321 | `NetInfo_IsForUpdate` | `0x923F0` | 81 | UnwindData |  |
| 327 | `QueryDirectEx` | `0x93170` | 550 | UnwindData |  |
| 14 | `BreakRecordsIntoBlob` | `0x93590` | 295 | UnwindData |  |
| 16 | `CombineRecordsInBlob` | `0x936C0` | 94 | UnwindData |  |
| 174 | `DnsQueryExA` | `0x93E80` | 64 | UnwindData |  |
| 175 | `DnsQueryExUTF8` | `0x93ED0` | 64 | UnwindData |  |
| 176 | `DnsQueryExW` | `0x93F20` | 105 | UnwindData |  |
| 215 | `DnsSetApplicationSettings` | `0x93F90` | 485 | UnwindData |  |
| 82 | `DnsExtractRecordsFromMessage_UTF8` | `0x94DC0` | 26 | UnwindData |  |
| 83 | `DnsExtractRecordsFromMessage_W` | `0x94DE0` | 27 | UnwindData |  |
| 250 | `DnsWriteQuestionToBuffer_UTF8` | `0x94E10` | 228 | UnwindData |  |
| 251 | `DnsWriteQuestionToBuffer_W` | `0x94F00` | 228 | UnwindData |  |
| 280 | `Dns_ParsePacketRecord` | `0x95220` | 106 | UnwindData |  |
| 289 | `Dns_SetRecordDatalength` | `0x95290` | 1,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `DnsFlushResolverCacheEntry_UTF8` | `0x95730` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 276 | `Dns_InitializeMsgRemoteSockaddr` | `0x95A30` | 102 | UnwindData |  |
| 278 | `Dns_OpenTcpConnectionAndSend` | `0x95AA0` | 135 | UnwindData |  |
| 285 | `Dns_RecvTcp` | `0x95B30` | 656 | UnwindData |  |
| 287 | `Dns_SendAndRecvUdp` | `0x95DD0` | 184 | UnwindData |  |
| 288 | `Dns_SendEx` | `0x95E90` | 132 | UnwindData |  |
| 339 | `Send_OpenTcpConnectionAndSend` | `0x97AF0` | 36 | UnwindData |  |
| 354 | `Socket_TcpListen` | `0x98420` | 124 | UnwindData |  |
| 20 | `DnsAcquireContextHandle_A` | `0x98CD0` | 48 | UnwindData |  |
| 21 | `DnsAcquireContextHandle_W` | `0x98D10` | 51 | UnwindData |  |
| 153 | `DnsModifyRecordsInSet_A` | `0x98D50` | 60 | UnwindData |  |
| 154 | `DnsModifyRecordsInSet_UTF8` | `0x98DA0` | 60 | UnwindData |  |
| 155 | `DnsModifyRecordsInSet_W` | `0x98DF0` | 60 | UnwindData |  |
| 195 | `DnsReleaseContextHandle` | `0x98E40` | 71 | UnwindData |  |
| 198 | `DnsReplaceRecordSetA` | `0x98E90` | 33 | UnwindData |  |
| 199 | `DnsReplaceRecordSetUTF8` | `0x98EC0` | 33 | UnwindData |  |
| 200 | `DnsReplaceRecordSetW` | `0x98EF0` | 33 | UnwindData |  |
| 236 | `DnsUpdateTest_A` | `0x98F20` | 164 | UnwindData |  |
| 237 | `DnsUpdateTest_UTF8` | `0x98FD0` | 164 | UnwindData |  |
| 238 | `DnsUpdateTest_W` | `0x99080` | 283 | UnwindData |  |
| 358 | `Util_IsIp6Running` | `0x993B0` | 45 | UnwindData |  |
| 244 | `DnsValidateServerArray_A` | `0x99430` | 216 | UnwindData |  |
| 245 | `DnsValidateServerArray_W` | `0x99510` | 99 | UnwindData |  |
| 246 | `DnsValidateServerStatus` | `0x99580` | 157 | UnwindData |  |
| 247 | `DnsValidateServer_A` | `0x99630` | 216 | UnwindData |  |
| 248 | `DnsValidateServer_W` | `0x99710` | 744 | UnwindData |  |
| 80 | `DnsDisableIdnEncoding` | `0x99C20` | 1,354 | UnwindData |  |
| 123 | `DnsGetNrptRule` | `0x9A170` | 506 | UnwindData |  |
| 219 | `DnsSetNrptRule` | `0x9A370` | 61 | UnwindData |  |
| 30 | `DnsApiHeapReset` | `0x9C0E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `DnsCleanupTcpConnections` | `0x9C0E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `DnsNotifyResolverClusterIp` | `0x9C0E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 265 | `Dns_CleanupWinsock` | `0x9C0E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 340 | `Socket_CacheCleanup` | `0x9C0E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 342 | `Socket_CleanupWinsock` | `0x9C0E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `DnsApiSetDebugGlobals` | `0x9C0F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `DnsGetLastFailedUpdateInfo` | `0x9C100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 233 | `DnsUpdate` | `0x9C120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 295 | `Dns_UpdateLib` | `0x9C120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 296 | `Dns_UpdateLibEx` | `0x9C120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 268 | `Dns_CreateMulticastSocket` | `0x9C130` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 272 | `Dns_FindAuthoritativeZoneLib` | `0x9C140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 277 | `Dns_InitializeWinsock` | `0x9C140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 348 | `Socket_InitWinsock` | `0x9C140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 281 | `Dns_PingAdapterServers` | `0x9C150` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 347 | `Socket_CreateMulticast` | `0x9C160` | 29 | UnwindData |  |
| 101 | `DnsFreeZtClientCertConfig` | `0xA00B0` | 67 | UnwindData |  |
| 102 | `DnsFreeZtConfig` | `0xA0100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `DnsFreeZtRules` | `0xA0110` | 117 | UnwindData |  |
| 104 | `DnsFreeZtSettings` | `0xA0190` | 104 | UnwindData |  |
| 105 | `DnsFreeZtTrustedCa` | `0xA0200` | 46 | UnwindData |  |
| 135 | `DnsGetZtClientCertConfig` | `0xA0240` | 440 | UnwindData |  |
| 136 | `DnsGetZtConfig` | `0xA0400` | 504 | UnwindData |  |
| 137 | `DnsGetZtFilterIds` | `0xA0600` | 374 | UnwindData |  |
| 138 | `DnsGetZtRules` | `0xA0780` | 479 | UnwindData |  |
| 139 | `DnsGetZtTrustedCa` | `0xA0970` | 442 | UnwindData |  |
| 140 | `DnsGetZtTrustedServers` | `0xA0B30` | 479 | UnwindData |  |
| 224 | `DnsSetZtSettings` | `0xA0D20` | 373 | UnwindData |  |
| 254 | `DnsZtHelperGetSettings` | `0xA0EA0` | 441 | UnwindData |  |
| 255 | `DnsZtHelperProcessClientCerts` | `0xA1060` | 391 | UnwindData |  |
| 256 | `DnsZtHelperPromoteConfig` | `0xA11F0` | 345 | UnwindData |  |
| 194 | `DnsRegisterLocal` | `0xA1CC0` | 27 | UnwindData |  |
| 43 | `DnsConnectionDeletePolicyEntries` | `0xA2FF0` | 352 | UnwindData |  |
| 45 | `DnsConnectionDeleteProxyInfo` | `0xA3160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `DnsConnectionFreeNameList` | `0xA3170` | 102 | UnwindData |  |
| 49 | `DnsConnectionFreeProxyList` | `0xA31E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `DnsConnectionGetNameList` | `0xA31F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `DnsConnectionGetProxyInfoForHostUrl` | `0xA3200` | 68 | UnwindData |  |
| 55 | `DnsConnectionGetProxyList` | `0xA3250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `DnsConnectionSetPolicyEntries` | `0xA3260` | 392 | UnwindData |  |
| 58 | `DnsConnectionSetProxyInfo` | `0xA33F0` | 25,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `DnsGetDdrInfo` | `0xA9640` | 373 | UnwindData |  |
| 115 | `DnsGetDdrInfoCancel` | `0xA97C0` | 86 | UnwindData |  |
| 116 | `DnsGetDdrInfoInternal` | `0xA9820` | 506 | UnwindData |  |
| 39 | `DnsCancelQueryRaw` | `0xABD10` | 86 | UnwindData |  |
| 177 | `DnsQueryRaw` | `0xABD70` | 938 | UnwindData |  |
| 178 | `DnsQueryRawResultFree` | `0xAC120` | 33 | UnwindData |  |
| 141 | `DnsGlobals` | `0x10B6C0` | 0 | Indeterminate |  |
