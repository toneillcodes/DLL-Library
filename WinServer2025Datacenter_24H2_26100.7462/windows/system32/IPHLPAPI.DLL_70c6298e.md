# Binary Specification: IPHLPAPI.DLL

## Binary Metadata
* **Original Path:** `c:\windows\system32\IPHLPAPI.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `70c6298e4836c05d1a4b27529f1a97ac991aeca5ceaaca40f3f712402e0a09c9`
* **Total Exported Functions:** 313

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 76 | `GetBestRoute` | `0x13A0` | 482 | UnwindData |  |
| 214 | `InternalGetTunnelPhysicalAdapter` | `0x16A0` | 363 | UnwindData |  |
| 26 | `ConvertLengthToIpv4Mask` | `0x1820` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `GetIpAddrTable` | `0x1850` | 495 | UnwindData |  |
| 70 | `GetAdaptersAddresses` | `0x1DC0` | 8 | UnwindData |  |
| 12 | `ConvertGuidToStringA` | `0x2890` | 59 | UnwindData |  |
| 13 | `ConvertGuidToStringW` | `0x3F60` | 59 | UnwindData |  |
| 21 | `ConvertInterfaceLuidToNameW` | `0x4590` | 50 | UnwindData |  |
| 67 | `FreeMibTable` | `0x6A20` | 58 | UnwindData |  |
| 189 | `InternalGetForwardIpTable2` | `0x7530` | 96 | UnwindData |  |
| 71 | `GetAdaptersInfo` | `0x8170` | 505 | UnwindData |  |
| 132 | `GetPerAdapterInfo` | `0x89A0` | 263 | UnwindData |  |
| 198 | `InternalGetIpInterfaceTable` | `0x9140` | 722 | UnwindData |  |
| 92 | `GetIfStackTable` | `0x9630` | 289 | UnwindData |  |
| 253 | `NotifyIpInterfaceChange` | `0x98B0` | 260 | UnwindData |  |
| 197 | `InternalGetIpInterfaceEntry` | `0x99C0` | 461 | UnwindData |  |
| 149 | `GetUdpStatisticsEx` | `0x9E90` | 247 | UnwindData |  |
| 142 | `GetTcpStatisticsEx` | `0xA2B0` | 326 | UnwindData |  |
| 78 | `GetCurrentThreadCompartmentId` | `0xB300` | 91 | UnwindData |  |
| 16 | `ConvertInterfaceIndexToLuid` | `0xBE70` | 103 | UnwindData |  |
| 77 | `GetBestRoute2` | `0xBFF0` | 1,227 | UnwindData |  |
| 259 | `NotifyUnicastIpAddressChange` | `0xC4D0` | 36 | UnwindData |  |
| 145 | `GetTcpTable2` | `0xC7B0` | 29 | UnwindData |  |
| 201 | `InternalGetIpNetTable2` | `0xC7E0` | 93 | UnwindData |  |
| 199 | `InternalGetIpNetEntry2` | `0xCEA0` | 941 | UnwindData |  |
| 80 | `GetDefaultCompartmentId` | `0xD260` | 222 | UnwindData |  |
| 279 | `ResolveIpNetEntry2` | `0xD350` | 571 | UnwindData |  |
| 195 | `InternalGetIpForwardEntry2` | `0xD5A0` | 631 | UnwindData |  |
| 282 | `SendARP` | `0xD820` | 204 | UnwindData |  |
| 114 | `GetIpNetworkConnectionBandwidthEstimates` | `0xDB50` | 317 | UnwindData |  |
| 74 | `GetBestInterface` | `0xDCA0` | 82 | UnwindData |  |
| 184 | `InternalFindInterfaceByAddress` | `0xDE30` | 223 | UnwindData |  |
| 46 | `CreateSortedAddressPairs` | `0xDF20` | 592 | UnwindData |  |
| 312 | `if_nametoindex` | `0xE180` | 127 | UnwindData |  |
| 22 | `ConvertInterfaceNameToLuidA` | `0xE210` | 206 | UnwindData |  |
| 23 | `ConvertInterfaceNameToLuidW` | `0xE2F0` | 78 | UnwindData |  |
| 101 | `GetInterfaceInfo` | `0xE570` | 605 | UnwindData |  |
| 131 | `GetOwnerModuleFromUdpEntry` | `0xE940` | 54 | UnwindData |  |
| 128 | `GetOwnerModuleFromTcp6Entry` | `0xE980` | 54 | UnwindData |  |
| 129 | `GetOwnerModuleFromTcpEntry` | `0xE9C0` | 54 | UnwindData |  |
| 127 | `GetOwnerModuleFromPidAndInfo` | `0xEA00` | 173 | UnwindData |  |
| 75 | `GetBestInterfaceEx` | `0xF480` | 289 | UnwindData |  |
| 18 | `ConvertInterfaceLuidToGuid` | `0xF720` | 126 | UnwindData |  |
| 112 | `GetIpNetTable` | `0xF7B0` | 540 | UnwindData |  |
| 19 | `ConvertInterfaceLuidToIndex` | `0xF9E0` | 27 | UnwindData |  |
| 247 | `NhGetInterfaceNameFromDeviceGuid` | `0xFA70` | 80 | UnwindData |  |
| 248 | `NhGetInterfaceNameFromGuid` | `0xFA70` | 80 | UnwindData |  |
| 15 | `ConvertInterfaceGuidToLuid` | `0xFAD0` | 323 | UnwindData |  |
| 17 | `ConvertInterfaceLuidToAlias` | `0xFC20` | 251 | UnwindData |  |
| 82 | `GetExtendedTcpTable` | `0x10250` | 341 | UnwindData |  |
| 68 | `GetAdapterIndex` | `0x103B0` | 501 | UnwindData |  |
| 138 | `GetSessionCompartmentId` | `0x105B0` | 94 | UnwindData |  |
| 79 | `GetCurrentThreadCompartmentScope` | `0x10650` | 146 | UnwindData |  |
| 83 | `GetExtendedUdpTable` | `0x106F0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `GetIpForwardTable` | `0x10770` | 946 | UnwindData |  |
| 91 | `GetIfEntry2Ex` | `0x10C70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `GetIfTable` | `0x10CA0` | 419 | UnwindData |  |
| 125 | `GetNetworkParams` | `0x10E50` | 392 | UnwindData |  |
| 118 | `GetIpStatisticsEx` | `0x11260` | 538 | UnwindData |  |
| 162 | `IcmpSendEcho` | `0x11570` | 90 | UnwindData |  |
| 163 | `IcmpSendEcho2` | `0x115D0` | 105 | UnwindData |  |
| 164 | `IcmpSendEcho2Ex` | `0x11640` | 1,012 | UnwindData |  |
| 161 | `IcmpParseReplies` | `0x11A40` | 74 | UnwindData |  |
| 89 | `GetIfEntry` | `0x11AD0` | 359 | UnwindData |  |
| 135 | `GetPerTcpConnectionEStats` | `0x120B0` | 608 | UnwindData |  |
| 285 | `SetCurrentThreadCompartmentScope` | `0x12320` | 80 | UnwindData |  |
| 90 | `GetIfEntry2` | `0x12380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `GetIpInterfaceEntry` | `0x123A0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 261 | `ParseNetworkString` | `0x12410` | 1,734 | UnwindData |  |
| 87 | `GetIcmpStatistics` | `0x12AE0` | 292 | UnwindData |  |
| 88 | `GetIcmpStatisticsEx` | `0x12C10` | 230 | UnwindData |  |
| 34 | `ConvertStringToGuidW` | `0x12D00` | 87 | UnwindData |  |
| 191 | `InternalGetIfEntry2` | `0x12D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `GetNumberOfInterfaces` | `0x12D70` | 142 | UnwindData |  |
| 140 | `GetTcp6Table2` | `0x12E10` | 702 | UnwindData |  |
| 94 | `GetIfTable2` | `0x130E0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `GetNetworkConnectivityHint` | `0x131F0` | 182 | UnwindData |  |
| 154 | `GetUnicastIpAddressTable` | `0x13370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `GetJobCompartmentId` | `0x13390` | 101 | UnwindData |  |
| 311 | `if_indextoname` | `0x134B0` | 135 | UnwindData |  |
| 20 | `ConvertInterfaceLuidToNameA` | `0x13540` | 166 | UnwindData |  |
| 95 | `GetIfTable2Ex` | `0x135F0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `GetIpInterfaceTable` | `0x13650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 250 | `NotifyAddrChange` | `0x13670` | 45 | UnwindData |  |
| 225 | `InternalGetUnicastIpAddressTable` | `0x136B0` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `ConvertRemoteInterfaceLuidToAlias` | `0x13A10` | 293 | UnwindData |  |
| 25 | `ConvertIpv4MaskToLength` | `0x13B40` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `InitializeIpInterfaceEntry` | `0x13B80` | 55 | UnwindData |  |
| 111 | `GetIpNetEntry2` | `0x13BE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 230 | `InternalSetIpInterfaceEntry` | `0x13C00` | 957 | UnwindData |  |
| 212 | `InternalGetTcpTableWithOwnerModule` | `0x13FF0` | 46 | UnwindData |  |
| 206 | `InternalGetTcp6TableWithOwnerModule` | `0x14030` | 46 | UnwindData |  |
| 205 | `InternalGetTcp6Table2` | `0x14070` | 46 | UnwindData |  |
| 210 | `InternalGetTcpTable2` | `0x140B0` | 46 | UnwindData |  |
| 215 | `InternalGetUdp6Table2` | `0x140F0` | 46 | UnwindData |  |
| 220 | `InternalGetUdpTable2` | `0x14130` | 46 | UnwindData |  |
| 192 | `InternalGetIfTable` | `0x14170` | 46 | UnwindData |  |
| 108 | `GetIpForwardTable2` | `0x142B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `GetPerTcp6ConnectionEStats` | `0x142D0` | 658 | UnwindData |  |
| 113 | `GetIpNetTable2` | `0x14570` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `CancelIPChangeNotify` | `0x14820` | 31 | UnwindData |  |
| 158 | `Icmp6SendEcho2` | `0x14850` | 1,060 | UnwindData |  |
| 167 | `InitializeIpForwardEntry` | `0x14D30` | 50 | UnwindData |  |
| 32 | `ConvertRemoteInterfaceLuidToIndex` | `0x15260` | 118 | UnwindData |  |
| 204 | `InternalGetRtcSlotInformation` | `0x152E0` | 499 | UnwindData |  |
| 153 | `GetUnicastIpAddressEntry` | `0x15850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `DeleteIpForwardEntry` | `0x15870` | 285 | UnwindData |  |
| 190 | `InternalGetIPPhysicalInterfaceForDestination` | `0x159A0` | 1,701 | UnwindData |  |
| 224 | `InternalGetUnicastIpAddressEntry` | `0x160A0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 160 | `IcmpCreateFile` | `0x16150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `InitializeUnicastIpAddressEntry` | `0x16170` | 53 | UnwindData |  |
| 86 | `GetFriendlyIfIndex` | `0x161B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `GetIpForwardEntry2` | `0x161C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 170 | `InternalCleanupPersistentStore` | `0x161E0` | 161 | UnwindData |  |
| 256 | `NotifyRouteChange2` | `0x16860` | 205 | UnwindData |  |
| 117 | `GetIpStatistics` | `0x16940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 284 | `SetCurrentThreadCompartmentId` | `0x16950` | 78 | UnwindData |  |
| 255 | `NotifyRouteChange` | `0x169E0` | 45 | UnwindData |  |
| 66 | `FreeInterfaceDnsSettings` | `0x16A20` | 211 | UnwindData |  |
| 236 | `InternalSetTeredoPort` | `0x16B00` | 74 | UnwindData |  |
| 99 | `GetInterfaceDnsSettings` | `0x16B50` | 311 | UnwindData |  |
| 39 | `CreateIpForwardEntry` | `0x16D40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `ConvertCompartmentGuidToId` | `0x16D50` | 145 | UnwindData |  |
| 144 | `GetTcpTable` | `0x16DF0` | 26 | UnwindData |  |
| 157 | `Icmp6ParseReplies` | `0x16F90` | 62 | UnwindData |  |
| 156 | `Icmp6CreateFile` | `0x16FE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `ConvertCompartmentIdToGuid` | `0x17000` | 253 | UnwindData |  |
| 141 | `GetTcpStatistics` | `0x17160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 254 | `NotifyNetworkConnectivityHintChange` | `0x17170` | 350 | UnwindData |  |
| 286 | `SetDnsSettings` | `0x172E0` | 152 | UnwindData |  |
| 65 | `FreeDnsSettings` | `0x17380` | 107 | UnwindData |  |
| 130 | `GetOwnerModuleFromUdp6Entry` | `0x17400` | 54 | UnwindData |  |
| 139 | `GetTcp6Table` | `0x17440` | 604 | UnwindData |  |
| 180 | `InternalDeleteIpForwardEntry2` | `0x17860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `FlushIpNetTable2` | `0x17880` | 192 | UnwindData |  |
| 9 | `CloseGetIPPhysicalInterfaceForDestination` | `0x17950` | 353 | UnwindData |  |
| 290 | `SetIpForwardEntry` | `0x17BF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `ConvertRemoteInterfaceIndexToLuid` | `0x17C00` | 109 | UnwindData |  |
| 292 | `SetIpInterfaceEntry` | `0x17C80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `ConvertRemoteInterfaceAliasToLuid` | `0x17CA0` | 427 | UnwindData |  |
| 81 | `GetDnsSettings` | `0x17E60` | 134 | UnwindData |  |
| 300 | `SetPerTcp6ConnectionEStats` | `0x18000` | 253 | UnwindData |  |
| 54 | `DeleteIpNetEntry` | `0x18110` | 163 | UnwindData |  |
| 53 | `DeleteIpForwardEntry2` | `0x181C0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `GetNetworkInformation` | `0x18320` | 232 | UnwindData |  |
| 173 | `InternalCreateIpForwardEntry2` | `0x18410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 175 | `InternalCreateIpNetEntry2` | `0x18430` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 177 | `InternalCreateUnicastIpAddressEntry` | `0x18470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `IcmpCloseHandle` | `0x18490` | 301 | UnwindData |  |
| 6 | `CancelMibChangeNotify2` | `0x187C0` | 268 | UnwindData |  |
| 28 | `ConvertRemoteInterfaceGuidToLuid` | `0x18950` | 336 | UnwindData |  |
| 148 | `GetUdpStatistics` | `0x18B30` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `CreateUnicastIpAddressEntry` | `0x18C00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `DeleteUnicastIpAddressEntry` | `0x18C20` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `InternalDeleteUnicastIpAddressEntry` | `0x18CC0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `CreateIpForwardEntry2` | `0x18DA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `CreateIpNetEntry2` | `0x18DC0` | 6,704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `GetIpErrorString` | `0x1A7F0` | 198 | UnwindData |  |
| 2 | `AllocateAndGetInterfaceInfoFromStack` | `0x1A8C0` | 571 | UnwindData |  |
| 249 | `NhpAllocateAndGetInterfaceInfoFromStack` | `0x1A8C0` | 571 | UnwindData |  |
| 31 | `ConvertRemoteInterfaceLuidToGuid` | `0x1AB20` | 122 | UnwindData |  |
| 33 | `ConvertStringToGuidA` | `0x1ABA0` | 116 | UnwindData |  |
| 69 | `GetAdapterOrderMap` | `0x1AC20` | 310 | UnwindData |  |
| 245 | `NhGetGuidFromInterfaceName` | `0x1AD60` | 49 | UnwindData |  |
| 246 | `NhGetInterfaceDescriptionFromGuid` | `0x1ADA0` | 285 | UnwindData |  |
| 288 | `SetIfEntry` | `0x1AED0` | 130 | UnwindData |  |
| 3 | `AllocateAndGetIpAddrTableFromStack` | `0x1AFB0` | 35 | UnwindData |  |
| 60 | `DisableMediaSense` | `0x1AFE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `GetWPAOACSupportLevel` | `0x1AFE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 281 | `RestoreMediaSense` | `0x1AFE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 172 | `InternalCreateIpForwardEntry` | `0x1AFF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 174 | `InternalCreateIpNetEntry` | `0x1B010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `InternalDeleteIpForwardEntry` | `0x1B030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `InternalDeleteIpNetEntry` | `0x1B040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 187 | `InternalGetBoundTcp6EndpointTable` | `0x1B050` | 46 | UnwindData |  |
| 188 | `InternalGetBoundTcpEndpointTable` | `0x1B090` | 46 | UnwindData |  |
| 194 | `InternalGetIpAddrTable` | `0x1B240` | 46 | UnwindData |  |
| 196 | `InternalGetIpForwardTable` | `0x1B280` | 46 | UnwindData |  |
| 200 | `InternalGetIpNetTable` | `0x1B2C0` | 46 | UnwindData |  |
| 207 | `InternalGetTcp6TableWithOwnerPid` | `0x1B300` | 46 | UnwindData |  |
| 209 | `InternalGetTcpTable` | `0x1B340` | 46 | UnwindData |  |
| 211 | `InternalGetTcpTableEx` | `0x1B380` | 46 | UnwindData |  |
| 213 | `InternalGetTcpTableWithOwnerPid` | `0x1B3C0` | 46 | UnwindData |  |
| 216 | `InternalGetUdp6TableWithOwnerModule` | `0x1B400` | 46 | UnwindData |  |
| 217 | `InternalGetUdp6TableWithOwnerPid` | `0x1B440` | 46 | UnwindData |  |
| 219 | `InternalGetUdpTable` | `0x1B480` | 46 | UnwindData |  |
| 221 | `InternalGetUdpTableEx` | `0x1B4C0` | 46 | UnwindData |  |
| 222 | `InternalGetUdpTableWithOwnerModule` | `0x1B500` | 46 | UnwindData |  |
| 223 | `InternalGetUdpTableWithOwnerPid` | `0x1B540` | 46 | UnwindData |  |
| 226 | `InternalIcmpCreateFileEx` | `0x1B580` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 227 | `InternalSetIfEntry` | `0x1B5B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 228 | `InternalSetIpForwardEntry` | `0x1B5C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 231 | `InternalSetIpNetEntry` | `0x1B5E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 233 | `InternalSetIpStats` | `0x1B600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 235 | `InternalSetTcpEntry` | `0x1B620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 283 | `SetAdapterIpAddress` | `0x1B630` | 351 | UnwindData |  |
| 1 | `AddIPAddress` | `0x1B7B0` | 278 | UnwindData |  |
| 41 | `CreateIpNetEntry` | `0x1B8D0` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `CreateProxyArpEntry` | `0x1BA40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `DeleteIPAddress` | `0x1BA60` | 254 | UnwindData |  |
| 58 | `DeleteProxyArpEntry` | `0x1BB70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `EnableRouter` | `0x1BB90` | 94 | UnwindData |  |
| 62 | `FlushIpNetTable` | `0x1BC00` | 127 | UnwindData |  |
| 152 | `GetUniDirectionalAdapterInfo` | `0x1BC90` | 285 | UnwindData |  |
| 239 | `IpReleaseAddress` | `0x1BDC0` | 75 | UnwindData |  |
| 240 | `IpRenewAddress` | `0x1BE20` | 75 | UnwindData |  |
| 98 | `GetInterfaceCurrentTimestampCapabilities` | `0x1BE80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `GetInterfaceHardwareTimestampCapabilities` | `0x1BE80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 252 | `NotifyIfTimestampConfigChange` | `0x1BE80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 280 | `ResolveNeighbor` | `0x1BE80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 293 | `SetIpNetEntry` | `0x1BE90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 295 | `SetIpStatistics` | `0x1BEA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 296 | `SetIpStatisticsEx` | `0x1BEB0` | 218 | UnwindData |  |
| 297 | `SetIpTTL` | `0x1BF90` | 125 | UnwindData |  |
| 307 | `UnenableRouter` | `0x1C0C0` | 124 | UnwindData |  |
| 243 | `NTPTimeToNTFileTime` | `0x1C150` | 146 | UnwindData |  |
| 244 | `NTTimeToNTPTime` | `0x1C1F0` | 231 | UnwindData |  |
| 262 | `PfAddFiltersToInterface` | `0x1C480` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 263 | `PfAddGlobalFilterToInterface` | `0x1C480` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 264 | `PfBindInterfaceToIPAddress` | `0x1C480` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 265 | `PfBindInterfaceToIndex` | `0x1C480` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 266 | `PfCreateInterface` | `0x1C480` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 267 | `PfDeleteInterface` | `0x1C480` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 268 | `PfDeleteLog` | `0x1C480` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 269 | `PfGetInterfaceStatistics` | `0x1C480` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 270 | `PfMakeLog` | `0x1C480` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 271 | `PfRebindFilters` | `0x1C480` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 272 | `PfRemoveFilterHandles` | `0x1C480` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 273 | `PfRemoveFiltersFromInterface` | `0x1C480` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 274 | `PfRemoveGlobalFilterFromInterface` | `0x1C480` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 275 | `PfSetLogBuffer` | `0x1C480` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 276 | `PfTestPacket` | `0x1C480` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 277 | `PfUnBindInterface` | `0x1C480` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `GetRTTAndHopCount` | `0x1C4E0` | 633 | UnwindData |  |
| 309 | `do_echo_rep` | `0x1CA40` | 471 | UnwindData |  |
| 310 | `do_echo_req` | `0x1CC20` | 380 | UnwindData |  |
| 313 | `register_icmp` | `0x1CDB0` | 52 | UnwindData |  |
| 208 | `InternalGetTcpDynamicPortRange` | `0x1D860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 218 | `InternalGetUdpDynamicPortRange` | `0x1D880` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 234 | `InternalSetTcpDynamicPortRange` | `0x1D910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 237 | `InternalSetUdpDynamicPortRange` | `0x1D930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `CreatePersistentTcpPortReservation` | `0x1D950` | 46 | UnwindData |  |
| 44 | `CreatePersistentUdpPortReservation` | `0x1D990` | 46 | UnwindData |  |
| 56 | `DeletePersistentTcpPortReservation` | `0x1D9D0` | 47 | UnwindData |  |
| 57 | `DeletePersistentUdpPortReservation` | `0x1DA10` | 45 | UnwindData |  |
| 241 | `LookupPersistentTcpPortReservation` | `0x1DB60` | 44 | UnwindData |  |
| 242 | `LookupPersistentUdpPortReservation` | `0x1DBA0` | 44 | UnwindData |  |
| 134 | `GetPerTcp6ConnectionStats` | `0x1E0D0` | 182 | UnwindData |  |
| 136 | `GetPerTcpConnectionStats` | `0x1E190` | 183 | UnwindData |  |
| 143 | `GetTcpStatisticsEx2` | `0x1E290` | 322 | UnwindData |  |
| 301 | `SetPerTcp6ConnectionStats` | `0x1E6E0` | 171 | UnwindData |  |
| 302 | `SetPerTcpConnectionEStats` | `0x1E7A0` | 244 | UnwindData |  |
| 303 | `SetPerTcpConnectionStats` | `0x1E8A0` | 158 | UnwindData |  |
| 305 | `SetTcpEntry` | `0x1E950` | 169 | UnwindData |  |
| 147 | `GetUdp6Table` | `0x1EA20` | 528 | UnwindData |  |
| 150 | `GetUdpStatisticsEx2` | `0x1EC40` | 238 | UnwindData |  |
| 151 | `GetUdpTable` | `0x1ED40` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `CancelIfTimestampConfigChange` | `0x1EF80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `CaptureInterfaceHardwareCrossTimestamp` | `0x1EF90` | 310 | UnwindData |  |
| 96 | `GetInterfaceActiveTimestampCapabilities` | `0x1F110` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `GetInterfaceSupportedTimestampCapabilities` | `0x1F2D0` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 278 | `RegisterInterfaceTimestampConfigChange` | `0x1F510` | 248 | UnwindData |  |
| 308 | `UnregisterInterfaceTimestampConfigChange` | `0x1F740` | 113 | UnwindData |  |
| 8 | `CloseCompartment` | `0x1FCD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `CreateCompartment` | `0x1FCF0` | 397 | UnwindData |  |
| 49 | `DeleteCompartment` | `0x1FE90` | 73 | UnwindData |  |
| 97 | `GetInterfaceCompartmentId` | `0x1FEE0` | 95 | UnwindData |  |
| 165 | `InitializeCompartmentEntry` | `0x1FF50` | 41 | UnwindData |  |
| 251 | `NotifyCompartmentChange` | `0x20010` | 142 | UnwindData |  |
| 260 | `OpenCompartment` | `0x200B0` | 376 | UnwindData |  |
| 298 | `SetJobCompartmentId` | `0x20230` | 93 | UnwindData |  |
| 299 | `SetNetworkInformation` | `0x202A0` | 233 | UnwindData |  |
| 304 | `SetSessionCompartmentId` | `0x20390` | 87 | UnwindData |  |
| 14 | `ConvertInterfaceAliasToLuid` | `0x203F0` | 416 | UnwindData |  |
| 24 | `ConvertInterfacePhysicalAddressToLuid` | `0x205A0` | 376 | UnwindData |  |
| 35 | `ConvertStringToInterfacePhysicalAddress` | `0x20720` | 179 | UnwindData |  |
| 36 | `CreateAnycastIpAddressEntry` | `0x207E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `DeleteAnycastIpAddressEntry` | `0x20800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `GetAnycastIpAddressEntry` | `0x20820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `GetAnycastIpAddressTable` | `0x20840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `GetMulticastIpAddressEntry` | `0x20860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `GetMulticastIpAddressTable` | `0x20880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 171 | `InternalCreateAnycastIpAddressEntry` | `0x208A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 178 | `InternalDeleteAnycastIpAddressEntry` | `0x208C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `InternalGetAnycastIpAddressEntry` | `0x208E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `InternalGetAnycastIpAddressTable` | `0x20900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | `InternalGetMulticastIpAddressEntry` | `0x20920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 203 | `InternalGetMulticastIpAddressTable` | `0x20940` | 704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 238 | `InternalSetUnicastIpAddressEntry` | `0x20C00` | 1,552 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 257 | `NotifyStableUnicastIpAddressTable` | `0x21210` | 36 | UnwindData |  |
| 306 | `SetUnicastIpAddressEntry` | `0x21670` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `CreateFlVirtualInterface` | `0x217D0` | 161 | UnwindData |  |
| 50 | `DeleteFlVirtualInterface` | `0x21880` | 148 | UnwindData |  |
| 84 | `GetFlVirtualInterface` | `0x21A50` | 286 | UnwindData |  |
| 85 | `GetFlVirtualInterfaceTable` | `0x21B80` | 647 | UnwindData |  |
| 166 | `InitializeFlVirtualInterfaceEntry` | `0x21E10` | 42 | UnwindData |  |
| 287 | `SetFlVirtualInterface` | `0x21E40` | 158 | UnwindData |  |
| 176 | `InternalCreateOrRefIpForwardEntry2` | `0x21EF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 229 | `InternalSetIpForwardEntry2` | `0x21F10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 291 | `SetIpForwardEntry2` | `0x21F30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `DeleteIpNetEntry2` | `0x21F50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 182 | `InternalDeleteIpNetEntry2` | `0x21F70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 232 | `InternalSetIpNetEntry2` | `0x21F90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 294 | `SetIpNetEntry2` | `0x21FB0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `FlushIpPathTable` | `0x220A0` | 225 | UnwindData |  |
| 115 | `GetIpPathEntry` | `0x22190` | 529 | UnwindData |  |
| 116 | `GetIpPathTable` | `0x223B0` | 675 | UnwindData |  |
| 289 | `SetInterfaceDnsSettings` | `0x22660` | 436 | UnwindData |  |
| 103 | `GetInvertedIfStackTable` | `0x22820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 193 | `InternalGetIfTable2` | `0x22830` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `GetNetworkConnectivityHintForInterface` | `0x22960` | 630 | UnwindData |  |
| 146 | `GetTeredoPort` | `0x22C50` | 124 | UnwindData |  |
| 258 | `NotifyTeredoPortChange` | `0x22D10` | 165 | UnwindData |  |
