# Binary Specification: dnsapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\dnsapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `55f028f320563f04d456682850d47d0e67d4dba89cc62711fbf3653a648bba43`
* **Total Exported Functions:** 352

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 48 | `DnsConnectionFreeProxyInfoEx` | `0x3120` | 63 | UnwindData |  |
| 54 | `DnsConnectionGetProxyInfoForHostUrlEx` | `0x43D0` | 154 | UnwindData |  |
| 89 | `DnsFree` | `0x7420` | 577 | UnwindData |  |
| 59 | `DnsConnectionUpdateIfIndexTable` | `0x8A40` | 82 | UnwindData |  |
| 94 | `DnsFreeNrptRule` | `0x9710` | 257 | UnwindData |  |
| 124 | `DnsGetNrptRuleNamesList` | `0xA370` | 589 | UnwindData |  |
| 120 | `DnsGetInterfaceSettingsInProc` | `0x113F0` | 35 | UnwindData |  |
| 29 | `DnsApiFree` | `0x12680` | 73 | UnwindData |  |
| 313 | `NetInfo_Clean` | `0x1B4E0` | 478 | UnwindData |  |
| 13 | `AddRefQueryBlobEx` | `0x1BA10` | 497 | UnwindData |  |
| 18 | `DeRefQueryBlobEx` | `0x1BC10` | 1,099 | UnwindData |  |
| 244 | `DnsValidateName_W` | `0x22010` | 210 | UnwindData |  |
| 107 | `DnsGetAdaptersInfo` | `0x22CE0` | 558 | UnwindData |  |
| 182 | `DnsQuery_W` | `0x23590` | 452 | UnwindData |  |
| 180 | `DnsQuery_A` | `0x24C60` | 87 | UnwindData |  |
| 181 | `DnsQuery_UTF8` | `0x24F50` | 87 | UnwindData |  |
| 204 | `DnsResolverQueryHvsi` | `0x25080` | 452 | UnwindData |  |
| 314 | `NetInfo_Copy` | `0x25DF0` | 302 | UnwindData |  |
| 316 | `NetInfo_CreatePerNetworkNetinfo` | `0x268B0` | 1,083 | UnwindData |  |
| 312 | `NetInfo_BuildEx` | `0x26F10` | 1,658 | UnwindData |  |
| 334 | `Reg_ReadGlobalsEx` | `0x27B30` | 428 | UnwindData |  |
| 317 | `NetInfo_Free` | `0x29280` | 462 | UnwindData |  |
| 208 | `DnsServiceConstructInstance` | `0x2A9E0` | 875 | UnwindData |  |
| 321 | `NetInfo_IsAddrConfig` | `0x30000` | 341 | UnwindData |  |
| 162 | `DnsNameCompare_W` | `0x32130` | 161 | UnwindData |  |
| 209 | `DnsServiceCopyInstance` | `0x339F0` | 91 | UnwindData |  |
| 210 | `DnsServiceDeRegister` | `0x33A60` | 298 | UnwindData |  |
| 212 | `DnsServiceRegister` | `0x33DD0` | 485 | UnwindData |  |
| 214 | `DnsServiceResolve` | `0x34860` | 235 | UnwindData |  |
| 206 | `DnsServiceBrowse` | `0x34AF0` | 672 | UnwindData |  |
| 229 | `DnsStopMulticastQuery` | `0x34F20` | 456 | UnwindData |  |
| 98 | `DnsFreeWellKnownServerProperty` | `0x3CED0` | 103 | UnwindData |  |
| 344 | `Socket_ClearMessageSockets` | `0x43450` | 306 | UnwindData |  |
| 90 | `DnsFreeAdaptersInfo` | `0x46090` | 11 | UnwindData |  |
| 50 | `DnsConnectionGetHandleForHostUrlPrivate` | `0x49BE0` | 423 | UnwindData |  |
| 27 | `DnsApiAlloc` | `0x49DB0` | 1,008 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `DnsApiAllocZero` | `0x49DB0` | 1,008 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 339 | `Send_MessagePrivateEx` | `0x4A1A0` | 899 | UnwindData |  |
| 92 | `DnsFreeCustomServers` | `0x4A530` | 174 | UnwindData |  |
| 173 | `DnsQueryConfigDword` | `0x4DF40` | 200 | UnwindData |  |
| 168 | `DnsNotifyResolver` | `0x562A0` | 142 | UnwindData |  |
| 319 | `NetInfo_GetAdapterByInterfaceIndex` | `0x57330` | 419 | UnwindData |  |
| 67 | `DnsDhcpRegisterAddrs` | `0x57560` | 195 | UnwindData |  |
| 203 | `DnsResolverOp` | `0x576E0` | 451 | UnwindData |  |
| 132 | `DnsGetSettings` | `0x58530` | 323 | UnwindData |  |
| 211 | `DnsServiceFreeInstance` | `0x58AB0` | 155 | UnwindData |  |
| 207 | `DnsServiceBrowseCancel` | `0x59FB0` | 186 | UnwindData |  |
| 119 | `DnsGetInterfaceSettings` | `0x5B780` | 373 | UnwindData |  |
| 219 | `DnsSetInterfaceSettings` | `0x5D010` | 373 | UnwindData |  |
| 52 | `DnsConnectionGetProxyInfo` | `0x5DEC0` | 1,968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `DnsFlushResolverCacheEntry_W` | `0x5E670` | 467 | UnwindData |  |
| 96 | `DnsFreePolicyConfig` | `0x5ECF0` | 221 | UnwindData |  |
| 170 | `DnsNotifyResolverEx` | `0x5EDE0` | 69 | UnwindData |  |
| 133 | `DnsGetWellKnownServerProperty` | `0x5EEA0` | 382 | UnwindData |  |
| 47 | `DnsConnectionFreeProxyInfo` | `0x5F2C0` | 880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 215 | `DnsServiceResolveCancel` | `0x5F630` | 184 | UnwindData |  |
| 187 | `DnsRecordListFree` | `0x60100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 261 | `Dns_BuildPacket` | `0x60120` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 197 | `DnsRemoveNrptRule` | `0x60280` | 303 | UnwindData |  |
| 161 | `DnsNameCompare_UTF8` | `0x60400` | 2,160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `DnsRecordCopyEx` | `0x60C70` | 2,768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `AdaptiveTimeout_ClearInterfaceSpecificConfiguration` | `0x61740` | 379 | UnwindData |  |
| 213 | `DnsServiceRegisterCancel` | `0x61B30` | 175 | UnwindData |  |
| 86 | `DnsFlushResolverCacheEntry_A` | `0x61BF0` | 1,008 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 227 | `DnsStartMulticastQuery` | `0x61FE0` | 4,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 188 | `DnsRecordListUnmapV4MappedAAAAInPlace` | `0x63260` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 243 | `DnsValidateName_UTF8` | `0x632C0` | 160 | UnwindData |  |
| 95 | `DnsFreeNrptRuleNamesList` | `0x638B0` | 82 | UnwindData |  |
| 217 | `DnsSetConfigDword` | `0x63990` | 64 | UnwindData |  |
| 129 | `DnsGetProxyInformation` | `0x63DD0` | 38 | UnwindData |  |
| 130 | `DnsGetProxyInformationEx` | `0x63E00` | 500 | UnwindData |  |
| 171 | `DnsQueryConfig` | `0x642C0` | 1,120 | UnwindData |  |
| 172 | `DnsQueryConfigAllocEx` | `0x64730` | 354 | UnwindData |  |
| 69 | `DnsDhcpRegisterInit` | `0x648A0` | 69 | UnwindData |  |
| 125 | `DnsGetPolicyTableInfo` | `0x65180` | 295 | UnwindData |  |
| 274 | `Dns_FreeMsgBuf` | `0x652B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 280 | `Dns_ParseMessage` | `0x652C0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `DnsCancelQuery` | `0x65320` | 625 | UnwindData |  |
| 109 | `DnsGetApplicationSettings` | `0x655A0` | 363 | UnwindData |  |
| 174 | `DnsQueryEx` | `0x65720` | 889 | UnwindData |  |
| 330 | `Query_InProcSetCompletion` | `0x65C20` | 446 | UnwindData |  |
| 235 | `DnsUpdateCaptivePortalPresence` | `0x664B0` | 365 | UnwindData |  |
| 221 | `DnsSetNrptRules` | `0x66C80` | 812 | UnwindData |  |
| 17 | `CreateSendBlob` | `0x66FC0` | 239 | UnwindData |  |
| 22 | `DnsAddrArrayAddAddr` | `0x670C0` | 239 | UnwindData |  |
| 24 | `DnsAddrArrayCreate` | `0x671C0` | 236 | UnwindData |  |
| 25 | `DnsAddrBuildFromDnsRecord` | `0x672C0` | 236 | UnwindData |  |
| 40 | `DnsCheckNrptRuleIntegrity` | `0x673C0` | 239 | UnwindData |  |
| 41 | `DnsCheckNrptRules` | `0x674C0` | 239 | UnwindData |  |
| 64 | `DnsDeRegisterLocal` | `0x675C0` | 239 | UnwindData |  |
| 91 | `DnsFreeConfigStructure` | `0x676C0` | 399 | UnwindData |  |
| 108 | `DnsGetApplicationIdentifier` | `0x67860` | 396 | UnwindData |  |
| 111 | `DnsGetCacheDataTable` | `0x67A00` | 47 | UnwindData |  |
| 112 | `DnsGetCacheDataTableEx` | `0x67A40` | 481 | UnwindData |  |
| 131 | `DnsGetQueryRetryTimeouts` | `0x67C30` | 599 | UnwindData |  |
| 163 | `DnsNameCopy` | `0x68040` | 256 | UnwindData |  |
| 230 | `DnsStringCopyAllocateEx` | `0x68150` | 259 | UnwindData |  |
| 259 | `Dns_AddRecordsToMessage` | `0x68260` | 239 | UnwindData |  |
| 260 | `Dns_AllocateMsgBuf` | `0x68360` | 236 | UnwindData |  |
| 272 | `Dns_ExtractRecordsFromMessage` | `0x68460` | 245 | UnwindData |  |
| 275 | `Dns_GetRandomXid` | `0x68560` | 249 | UnwindData |  |
| 276 | `Dns_InitializeMsgBuf` | `0x68660` | 391 | UnwindData |  |
| 283 | `Dns_ReadPacketName` | `0x687F0` | 278 | UnwindData |  |
| 284 | `Dns_ReadPacketNameAllocate` | `0x68910` | 273 | UnwindData |  |
| 285 | `Dns_ReadRecordStructureFromPacket` | `0x68A30` | 393 | UnwindData |  |
| 291 | `Dns_SetRecordsScopeId` | `0x68BC0` | 234 | UnwindData |  |
| 292 | `Dns_SetRecordsSection` | `0x68CB0` | 262 | UnwindData |  |
| 293 | `Dns_SetRecordsTtl` | `0x68DC0` | 240 | UnwindData |  |
| 294 | `Dns_SkipPacketName` | `0x68EC0` | 236 | UnwindData |  |
| 298 | `Dns_WriteDottedNameToPacket` | `0x68FC0` | 417 | UnwindData |  |
| 299 | `Dns_WriteQuestionToMessage` | `0x69170` | 239 | UnwindData |  |
| 300 | `Dns_WriteRecordStructureToPacketEx` | `0x69270` | 248 | UnwindData |  |
| 301 | `ExtraInfo_Init` | `0x69370` | 286 | UnwindData |  |
| 304 | `GetCurrentTimeInSeconds` | `0x694A0` | 273 | UnwindData |  |
| 305 | `HostsFile_Close` | `0x695C0` | 234 | UnwindData |  |
| 306 | `HostsFile_Open` | `0x696B0` | 236 | UnwindData |  |
| 307 | `HostsFile_ReadLine` | `0x697B0` | 236 | UnwindData |  |
| 308 | `IpHelp_IsAddrOnLink` | `0x698B0` | 236 | UnwindData |  |
| 309 | `Local_GetRecordsForLocalName` | `0x699B0` | 247 | UnwindData |  |
| 333 | `Reg_GetValueEx` | `0x69AB0` | 437 | UnwindData |  |
| 337 | `Send_AndRecvUdpWithParam` | `0x69C70` | 239 | UnwindData |  |
| 338 | `Send_MessagePrivate` | `0x69D70` | 239 | UnwindData |  |
| 346 | `Socket_CloseMessageSockets` | `0x69E70` | 227 | UnwindData |  |
| 356 | `ThreadPool_QueueWork` | `0x69F60` | 239 | UnwindData |  |
| 357 | `Trace_Reset` | `0x6A060` | 235 | UnwindData |  |
| 360 | `Util_IsRunningOnXboxOne` | `0x6A160` | 236 | UnwindData |  |
| 361 | `WriteDnsNrptRulesToRegistry` | `0x6A260` | 242 | UnwindData |  |
| 302 | `Faz_AreServerListsInSameNameSpace` | `0x6A360` | 558 | UnwindData |  |
| 310 | `Local_GetRecordsForLocalNameEx` | `0x6ABF0` | 410 | UnwindData |  |
| 315 | `NetInfo_CopyNetworkIndex` | `0x6BE40` | 339 | UnwindData |  |
| 318 | `NetInfo_GetAdapterByAddress` | `0x6C4D0` | 447 | UnwindData |  |
| 320 | `NetInfo_GetAdapterByName` | `0x6C6A0` | 436 | UnwindData |  |
| 323 | `NetInfo_IsTcpipConfigChange` | `0x6C860` | 499 | UnwindData |  |
| 324 | `NetInfo_ResetServerPriorities` | `0x6CA60` | 546 | UnwindData |  |
| 325 | `NetInfo_UpdateDnsInterfaceConfigChange` | `0x6CC90` | 352 | UnwindData |  |
| 326 | `NetInfo_UpdateNetworkProperties` | `0x6CE00` | 758 | UnwindData |  |
| 327 | `NetInfo_UpdateServerReachability` | `0x6D100` | 426 | UnwindData |  |
| 329 | `Query_Cancel` | `0x6F690` | 747 | UnwindData |  |
| 331 | `Query_Main` | `0x70140` | 1,203 | UnwindData |  |
| 332 | `Reg_FreeUpdateInfo` | `0x71D20` | 377 | UnwindData |  |
| 335 | `Reg_ReadUpdateInfo` | `0x721A0` | 770 | UnwindData |  |
| 31 | `DnsApiOnNetworkChange` | `0x724B0` | 428 | UnwindData |  |
| 152 | `DnsLogEvent` | `0x72B80` | 538 | UnwindData |  |
| 232 | `DnsTraceServerConfig` | `0x72DA0` | 762 | UnwindData |  |
| 345 | `Socket_CloseEx` | `0x76C20` | 423 | UnwindData |  |
| 347 | `Socket_Create` | `0x76EF0` | 320 | UnwindData |  |
| 350 | `Socket_JoinMulticast` | `0x77660` | 534 | UnwindData |  |
| 351 | `Socket_RecvFrom` | `0x77880` | 865 | UnwindData |  |
| 352 | `Socket_SetMulticastInterface` | `0x77BF0` | 651 | UnwindData |  |
| 353 | `Socket_SetMulticastLoopBack` | `0x77E90` | 429 | UnwindData |  |
| 354 | `Socket_SetTtl` | `0x78050` | 560 | UnwindData |  |
| 358 | `Update_ReplaceAddressRecordsW` | `0x79020` | 337 | UnwindData |  |
| 19 | `DelaySortDAServerlist` | `0x79CD0` | 283 | UnwindData |  |
| 126 | `DnsGetPolicyTableInfoPrivate` | `0x79E00` | 563 | UnwindData |  |
| 128 | `DnsGetProxyInfoPrivate` | `0x7A040` | 945 | UnwindData |  |
| 167 | `DnsNotifyProxyConfigChangePrivate` | `0x7A400` | 512 | UnwindData |  |
| 236 | `DnsUpdateMachinePresence` | `0x7A610` | 1,357 | UnwindData |  |
| 303 | `FlushDnsPolicyUnreachableStatus` | `0x7AB70` | 347 | UnwindData |  |
| 15 | `Coalesce_UpdateNetVersion` | `0x7AF00` | 284 | UnwindData |  |
| 12 | `AdaptiveTimeout_ResetAdaptiveTimeout` | `0x7B2A0` | 376 | UnwindData |  |
| 44 | `DnsConnectionDeletePolicyEntriesPrivate` | `0x7E380` | 208 | UnwindData |  |
| 57 | `DnsConnectionSetPolicyEntriesPrivate` | `0x7E460` | 226 | UnwindData |  |
| 85 | `DnsFlushResolverCache` | `0x84E80` | 318 | UnwindData |  |
| 144 | `DnsIp6ReverseNameToAddressW` | `0x85B20` | 3,600 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 231 | `DnsStringToAddress` | `0x86930` | 704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `DnsFreeProxyName` | `0x86BF0` | 20 | UnwindData |  |
| 218 | `DnsSetConfigValue` | `0x896E0` | 238 | UnwindData |  |
| 70 | `DnsDhcpRegisterTerm` | `0x897E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `DnsDhcpRemoveRegistrations` | `0x897F0` | 95 | UnwindData |  |
| 73 | `DnsDhcpSrvRegisterHostAddrEx` | `0x8A3F0` | 104 | UnwindData |  |
| 75 | `DnsDhcpSrvRegisterHostNameEx` | `0x8A460` | 359 | UnwindData |  |
| 77 | `DnsDhcpSrvRegisterInitEx` | `0x8A5D0` | 860 | UnwindData |  |
| 79 | `DnsDhcpSrvRegisterTerm` | `0x8A940` | 270 | UnwindData |  |
| 65 | `DnsDeleteSettings` | `0x8BFC0` | 314 | UnwindData |  |
| 66 | `DnsDeleteWellKnownServerProperty` | `0x8C100` | 340 | UnwindData |  |
| 93 | `DnsFreeNetworkServers` | `0x8C290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `DnsFreeWellKnownServerPropertyEx` | `0x8C2A0` | 158 | UnwindData |  |
| 100 | `DnsFreeWellKnownServers` | `0x8C350` | 104 | UnwindData |  |
| 113 | `DnsGetCacheRecords` | `0x8C3C0` | 476 | UnwindData |  |
| 122 | `DnsGetNetworkServers` | `0x8C7C0` | 513 | UnwindData |  |
| 134 | `DnsGetWellKnownServers` | `0x8C9D0` | 406 | UnwindData |  |
| 10 | `DnsIsZtEnabled` | `0x8CB70` | 302 | UnwindData |  |
| 223 | `DnsSetSettings` | `0x8CCB0` | 314 | UnwindData |  |
| 224 | `DnsSetWellKnownServerProperty` | `0x8CDF0` | 365 | UnwindData |  |
| 258 | `DnsZtNotifyDnscache` | `0x8CF70` | 438 | UnwindData |  |
| 82 | `DnsExtractRecordsFromMessage_UTF8` | `0x8D130` | 26 | UnwindData |  |
| 83 | `DnsExtractRecordsFromMessage_W` | `0x8D150` | 27 | UnwindData |  |
| 143 | `DnsIp6AddressToReverseNameW` | `0x8D180` | 29 | UnwindData |  |
| 148 | `DnsIsFlatRecord` | `0x8D1B0` | 131 | UnwindData |  |
| 157 | `DnsNameCompareEx_A` | `0x8D240` | 271 | UnwindData |  |
| 158 | `DnsNameCompareEx_UTF8` | `0x8D360` | 271 | UnwindData |  |
| 159 | `DnsNameCompareEx_W` | `0x8D480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 160 | `DnsNameCompare_A` | `0x8D4A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | `DnsRecordBuild_W` | `0x8D4B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `DnsRecordCompare` | `0x8D4C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 189 | `DnsRecordSetCompare` | `0x8D4D0` | 24 | UnwindData |  |
| 190 | `DnsRecordSetCopyEx` | `0x8D4F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 191 | `DnsRecordSetDetach` | `0x8D510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 192 | `DnsRecordStringForType` | `0x8D520` | 32 | UnwindData |  |
| 228 | `DnsStatusString` | `0x8D550` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 242 | `DnsValidateName_A` | `0x8D590` | 227 | UnwindData |  |
| 251 | `DnsWriteQuestionToBuffer_UTF8` | `0x8D720` | 228 | UnwindData |  |
| 252 | `DnsWriteQuestionToBuffer_W` | `0x8D810` | 228 | UnwindData |  |
| 254 | `DnsWriteReverseNameStringForIpAddressW` | `0x8D900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `DnsApiRealloc` | `0x8D910` | 317 | UnwindData |  |
| 216 | `DnsSetApplicationSettings` | `0x8E200` | 511 | UnwindData |  |
| 87 | `DnsFlushResolverCacheEntry_UTF8` | `0x8F580` | 255 | UnwindData |  |
| 20 | `DnsAcquireContextHandle_A` | `0x8F850` | 366 | UnwindData |  |
| 21 | `DnsAcquireContextHandle_W` | `0x8F9D0` | 212 | UnwindData |  |
| 154 | `DnsModifyRecordsInSet_A` | `0x8FAB0` | 60 | UnwindData |  |
| 155 | `DnsModifyRecordsInSet_UTF8` | `0x8FB00` | 60 | UnwindData |  |
| 156 | `DnsModifyRecordsInSet_W` | `0x8FB50` | 60 | UnwindData |  |
| 196 | `DnsReleaseContextHandle` | `0x8FBA0` | 166 | UnwindData |  |
| 199 | `DnsReplaceRecordSetA` | `0x8FC50` | 33 | UnwindData |  |
| 200 | `DnsReplaceRecordSetUTF8` | `0x8FC80` | 33 | UnwindData |  |
| 201 | `DnsReplaceRecordSetW` | `0x8FCB0` | 33 | UnwindData |  |
| 237 | `DnsUpdateTest_A` | `0x8FDD0` | 367 | UnwindData |  |
| 238 | `DnsUpdateTest_UTF8` | `0x8FF50` | 367 | UnwindData |  |
| 239 | `DnsUpdateTest_W` | `0x900D0` | 362 | UnwindData |  |
| 245 | `DnsValidateServerArray_A` | `0x902F0` | 405 | UnwindData |  |
| 246 | `DnsValidateServerArray_W` | `0x90490` | 99 | UnwindData |  |
| 247 | `DnsValidateServerStatus` | `0x90500` | 157 | UnwindData |  |
| 248 | `DnsValidateServer_A` | `0x905B0` | 405 | UnwindData |  |
| 249 | `DnsValidateServer_W` | `0x90750` | 735 | UnwindData |  |
| 80 | `DnsDisableIdnEncoding` | `0x90A40` | 1,376 | UnwindData |  |
| 123 | `DnsGetNrptRule` | `0x90FB0` | 528 | UnwindData |  |
| 14 | `BreakRecordsIntoBlob` | `0x91490` | 508 | UnwindData |  |
| 16 | `CombineRecordsInBlob` | `0x916A0` | 331 | UnwindData |  |
| 23 | `DnsAddrArrayAddIp4` | `0x91800` | 236 | UnwindData |  |
| 26 | `DnsAllocateRecord` | `0x91900` | 236 | UnwindData |  |
| 30 | `DnsApiHeapReset` | `0x91A00` | 227 | UnwindData |  |
| 33 | `DnsApiSetDebugGlobals` | `0x91AF0` | 234 | UnwindData |  |
| 34 | `DnsAsyncRegisterHostAddrs` | `0x91BE0` | 297 | UnwindData |  |
| 35 | `DnsAsyncRegisterInit` | `0x91D10` | 239 | UnwindData |  |
| 36 | `DnsAsyncRegisterTerm` | `0x91E10` | 236 | UnwindData |  |
| 37 | `DnsBuildDotHost` | `0x91F10` | 239 | UnwindData |  |
| 42 | `DnsCleanupTcpConnections` | `0x92010` | 227 | UnwindData |  |
| 60 | `DnsCopyStringEx` | `0x92100` | 294 | UnwindData |  |
| 61 | `DnsCreateReverseNameStringForIpAddress` | `0x92230` | 236 | UnwindData |  |
| 62 | `DnsCreateStandardDnsNameCopy` | `0x92330` | 236 | UnwindData |  |
| 63 | `DnsCreateStringCopy` | `0x92430` | 236 | UnwindData |  |
| 68 | `DnsDhcpRegisterHostAddrs` | `0x92530` | 381 | UnwindData |  |
| 72 | `DnsDhcpSrvRegisterHostAddr` | `0x926C0` | 379 | UnwindData |  |
| 74 | `DnsDhcpSrvRegisterHostName` | `0x92850` | 322 | UnwindData |  |
| 76 | `DnsDhcpSrvRegisterInit` | `0x929A0` | 239 | UnwindData |  |
| 78 | `DnsDhcpSrvRegisterInitialize` | `0x92AA0` | 239 | UnwindData |  |
| 81 | `DnsDowncaseDnsNameLabel` | `0x92BA0` | 239 | UnwindData |  |
| 110 | `DnsGetBufferLengthForStringCopy` | `0x92CA0` | 262 | UnwindData |  |
| 117 | `DnsGetDnsServerList` | `0x92DB0` | 279 | UnwindData |  |
| 118 | `DnsGetDomainName` | `0x92ED0` | 281 | UnwindData |  |
| 121 | `DnsGetLastFailedUpdateInfo` | `0x92FF0` | 239 | UnwindData |  |
| 127 | `DnsGetPrimaryDomainName_A` | `0x930F0` | 246 | UnwindData |  |
| 145 | `DnsIpv6AddressToString` | `0x931F0` | 250 | UnwindData |  |
| 146 | `DnsIpv6StringToAddress` | `0x932F0` | 236 | UnwindData |  |
| 147 | `DnsIsAMailboxType` | `0x933F0` | 244 | UnwindData |  |
| 149 | `DnsIsNSECType` | `0x934F0` | 253 | UnwindData |  |
| 150 | `DnsIsStatusRcode` | `0x93600` | 236 | UnwindData |  |
| 151 | `DnsIsStringCountValidForTextType` | `0x93700` | 236 | UnwindData |  |
| 153 | `DnsMapRcodeToStatus` | `0x93800` | 242 | UnwindData |  |
| 164 | `DnsNameCopyAllocate` | `0x93900` | 239 | UnwindData |  |
| 169 | `DnsNotifyResolverClusterIp` | `0x93A00` | 227 | UnwindData |  |
| 175 | `DnsQueryExA` | `0x93AF0` | 302 | UnwindData |  |
| 176 | `DnsQueryExUTF8` | `0x93C30` | 302 | UnwindData |  |
| 177 | `DnsQueryExW` | `0x93D70` | 351 | UnwindData |  |
| 183 | `DnsRecordBuild_UTF8` | `0x93EE0` | 262 | UnwindData |  |
| 193 | `DnsRecordStringForWritableType` | `0x93FF0` | 283 | UnwindData |  |
| 194 | `DnsRecordTypeForName` | `0x94120` | 249 | UnwindData |  |
| 195 | `DnsRegisterLocal` | `0x94220` | 252 | UnwindData |  |
| 198 | `DnsRemoveRegistrations` | `0x94330` | 239 | UnwindData |  |
| 202 | `DnsResetQueryRetryTimeouts` | `0x94430` | 340 | UnwindData |  |
| 205 | `DnsScreenLocalAddrsForRegistration` | `0x94590` | 477 | UnwindData |  |
| 220 | `DnsSetNrptRule` | `0x94780` | 259 | UnwindData |  |
| 222 | `DnsSetQueryRetryTimeouts` | `0x94890` | 543 | UnwindData |  |
| 226 | `DnsSplitDotHost` | `0x94AC0` | 239 | UnwindData |  |
| 233 | `DnsUnicodeToUtf8` | `0x94BC0` | 239 | UnwindData |  |
| 234 | `DnsUpdate` | `0x94CC0` | 239 | UnwindData |  |
| 240 | `DnsUtf8ToUnicode` | `0x94DC0` | 272 | UnwindData |  |
| 241 | `DnsValidateNameOrIp_TempW` | `0x94EE0` | 475 | UnwindData |  |
| 250 | `DnsValidateUtf8Byte` | `0x950D0` | 236 | UnwindData |  |
| 253 | `DnsWriteReverseNameStringForIpAddress` | `0x951D0` | 236 | UnwindData |  |
| 263 | `Dns_CacheServiceInit` | `0x952D0` | 236 | UnwindData |  |
| 266 | `Dns_CleanupWinsock` | `0x953D0` | 227 | UnwindData |  |
| 267 | `Dns_CloseConnection` | `0x954C0` | 255 | UnwindData |  |
| 268 | `Dns_CloseSocket` | `0x955D0` | 252 | UnwindData |  |
| 269 | `Dns_CreateMulticastSocket` | `0x956E0` | 231 | UnwindData |  |
| 270 | `Dns_CreateSocket` | `0x957D0` | 257 | UnwindData |  |
| 271 | `Dns_CreateSocketEx` | `0x958E0` | 344 | UnwindData |  |
| 273 | `Dns_FindAuthoritativeZoneLib` | `0x95A40` | 232 | UnwindData |  |
| 277 | `Dns_InitializeMsgRemoteSockaddr` | `0x95B30` | 300 | UnwindData |  |
| 278 | `Dns_InitializeWinsock` | `0x95C70` | 232 | UnwindData |  |
| 279 | `Dns_OpenTcpConnectionAndSend` | `0x95D60` | 302 | UnwindData |  |
| 281 | `Dns_ParsePacketRecord` | `0x95EA0` | 236 | UnwindData |  |
| 282 | `Dns_PingAdapterServers` | `0x95FA0` | 239 | UnwindData |  |
| 287 | `Dns_ResetNetworkInfo` | `0x960A0` | 339 | UnwindData |  |
| 288 | `Dns_SendAndRecvUdp` | `0x96200` | 418 | UnwindData |  |
| 289 | `Dns_SendEx` | `0x963B0` | 317 | UnwindData |  |
| 290 | `Dns_SetRecordDatalength` | `0x96500` | 237 | UnwindData |  |
| 295 | `Dns_SkipToRecord` | `0x96600` | 236 | UnwindData |  |
| 296 | `Dns_UpdateLib` | `0x96700` | 239 | UnwindData |  |
| 297 | `Dns_UpdateLibEx` | `0x96800` | 239 | UnwindData |  |
| 311 | `NetInfo_Build` | `0x96900` | 277 | UnwindData |  |
| 328 | `QueryDirectEx` | `0x96A20` | 777 | UnwindData |  |
| 340 | `Send_OpenTcpConnectionAndSend` | `0x96D30` | 255 | UnwindData |  |
| 341 | `Socket_CacheCleanup` | `0x96E40` | 227 | UnwindData |  |
| 342 | `Socket_CacheInit` | `0x96F30` | 236 | UnwindData |  |
| 343 | `Socket_CleanupWinsock` | `0x97030` | 227 | UnwindData |  |
| 348 | `Socket_CreateMulticast` | `0x97120` | 246 | UnwindData |  |
| 349 | `Socket_InitWinsock` | `0x97220` | 232 | UnwindData |  |
| 359 | `Util_IsIp6Running` | `0x97370` | 276 | UnwindData |  |
| 101 | `DnsFreeZtClientCertConfig` | `0x97490` | 262 | UnwindData |  |
| 102 | `DnsFreeZtConfig` | `0x975A0` | 234 | UnwindData |  |
| 103 | `DnsFreeZtRules` | `0x97690` | 311 | UnwindData |  |
| 104 | `DnsFreeZtSettings` | `0x977D0` | 256 | UnwindData |  |
| 105 | `DnsFreeZtTrustedCa` | `0x978E0` | 289 | UnwindData |  |
| 106 | `DnsFreeZtTrustedServers` | `0x97A10` | 311 | UnwindData |  |
| 135 | `DnsGetZtClientCertConfig` | `0x97B50` | 688 | UnwindData |  |
| 136 | `DnsGetZtConfig` | `0x97E10` | 749 | UnwindData |  |
| 137 | `DnsGetZtFilterIds` | `0x98110` | 344 | UnwindData |  |
| 138 | `DnsGetZtRules` | `0x98270` | 718 | UnwindData |  |
| 139 | `DnsGetZtSettings` | `0x98550` | 475 | UnwindData |  |
| 140 | `DnsGetZtTrustedCa` | `0x98740` | 687 | UnwindData |  |
| 141 | `DnsGetZtTrustedServers` | `0x98A00` | 718 | UnwindData |  |
| 225 | `DnsSetZtSettings` | `0x98CE0` | 342 | UnwindData |  |
| 255 | `DnsZtHelperGetSettings` | `0x98E40` | 414 | UnwindData |  |
| 256 | `DnsZtHelperProcessClientCerts` | `0x98FF0` | 360 | UnwindData |  |
| 257 | `DnsZtHelperPromoteConfig` | `0x99160` | 407 | UnwindData |  |
| 84 | `DnsFindAuthoritativeZone` | `0x9BD90` | 513 | UnwindData |  |
| 165 | `DnsNetworkInfo_CreateFromFAZ` | `0x9BFA0` | 506 | UnwindData |  |
| 166 | `DnsNetworkInformation_CreateFromFAZ` | `0x9C650` | 534 | UnwindData |  |
| 322 | `NetInfo_IsForUpdate` | `0x9CB00` | 331 | UnwindData |  |
| 262 | `Dns_CacheServiceCleanup` | `0x9E200` | 578 | UnwindData |  |
| 264 | `Dns_CacheServiceInitEx` | `0x9E450` | 1,268 | UnwindData |  |
| 265 | `Dns_CacheServiceStopIssued` | `0x9E950` | 283 | UnwindData |  |
| 286 | `Dns_RecvTcp` | `0x9F960` | 953 | UnwindData |  |
| 355 | `Socket_TcpListen` | `0xA3C00` | 393 | UnwindData |  |
| 336 | `Security_ContextListTimeout` | `0xA9130` | 364 | UnwindData |  |
| 43 | `DnsConnectionDeletePolicyEntries` | `0xAEBD0` | 362 | UnwindData |  |
| 45 | `DnsConnectionDeleteProxyInfo` | `0xAED40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `DnsConnectionFreeNameList` | `0xAED50` | 112 | UnwindData |  |
| 49 | `DnsConnectionFreeProxyList` | `0xAEDD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `DnsConnectionGetNameList` | `0xAEDE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `DnsConnectionGetProxyInfoForHostUrl` | `0xAEDF0` | 68 | UnwindData |  |
| 55 | `DnsConnectionGetProxyList` | `0xAEE40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `DnsConnectionSetPolicyEntries` | `0xAEE50` | 404 | UnwindData |  |
| 58 | `DnsConnectionSetProxyInfo` | `0xAEFF0` | 10,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `DnsGetDdrInfo` | `0xB18B0` | 391 | UnwindData |  |
| 115 | `DnsGetDdrInfoCancel` | `0xB1A40` | 96 | UnwindData |  |
| 39 | `DnsCancelQueryRaw` | `0xB8FD0` | 96 | UnwindData |  |
| 178 | `DnsQueryRaw` | `0xB9040` | 975 | UnwindData |  |
| 179 | `DnsQueryRawResultFree` | `0xB9420` | 33 | UnwindData |  |
| 116 | `DnsGetDdrInfoInternal` | `0xBD390` | 690 | UnwindData |  |
| 142 | `DnsGlobals` | `0x1296C0` | 0 | Indeterminate |  |
