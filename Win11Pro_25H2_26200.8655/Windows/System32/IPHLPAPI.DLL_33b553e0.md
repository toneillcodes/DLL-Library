# Binary Specification: IPHLPAPI.DLL

## Binary Metadata
* **Original Path:** `C:\Windows\System32\IPHLPAPI.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `33b553e04e2b4a062173d2cdda9fec59f4664f486d0831be6e1ad09a5dc59e71`
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
| 253 | `NotifyIpInterfaceChange` | `0x9880` | 260 | UnwindData |  |
| 197 | `InternalGetIpInterfaceEntry` | `0x9990` | 461 | UnwindData |  |
| 149 | `GetUdpStatisticsEx` | `0x9E60` | 247 | UnwindData |  |
| 142 | `GetTcpStatisticsEx` | `0xA280` | 326 | UnwindData |  |
| 78 | `GetCurrentThreadCompartmentId` | `0xB2D0` | 91 | UnwindData |  |
| 16 | `ConvertInterfaceIndexToLuid` | `0xBE40` | 103 | UnwindData |  |
| 77 | `GetBestRoute2` | `0xBFC0` | 1,227 | UnwindData |  |
| 259 | `NotifyUnicastIpAddressChange` | `0xC4A0` | 36 | UnwindData |  |
| 145 | `GetTcpTable2` | `0xC780` | 29 | UnwindData |  |
| 201 | `InternalGetIpNetTable2` | `0xC7B0` | 93 | UnwindData |  |
| 199 | `InternalGetIpNetEntry2` | `0xCE70` | 941 | UnwindData |  |
| 80 | `GetDefaultCompartmentId` | `0xD230` | 222 | UnwindData |  |
| 279 | `ResolveIpNetEntry2` | `0xD320` | 571 | UnwindData |  |
| 195 | `InternalGetIpForwardEntry2` | `0xD570` | 631 | UnwindData |  |
| 282 | `SendARP` | `0xD7F0` | 204 | UnwindData |  |
| 114 | `GetIpNetworkConnectionBandwidthEstimates` | `0xDB20` | 317 | UnwindData |  |
| 74 | `GetBestInterface` | `0xDC70` | 82 | UnwindData |  |
| 184 | `InternalFindInterfaceByAddress` | `0xDE00` | 223 | UnwindData |  |
| 46 | `CreateSortedAddressPairs` | `0xDEF0` | 592 | UnwindData |  |
| 312 | `if_nametoindex` | `0xE150` | 127 | UnwindData |  |
| 22 | `ConvertInterfaceNameToLuidA` | `0xE1E0` | 206 | UnwindData |  |
| 23 | `ConvertInterfaceNameToLuidW` | `0xE2C0` | 78 | UnwindData |  |
| 101 | `GetInterfaceInfo` | `0xE540` | 605 | UnwindData |  |
| 75 | `GetBestInterfaceEx` | `0xEBD0` | 289 | UnwindData |  |
| 18 | `ConvertInterfaceLuidToGuid` | `0xEE70` | 126 | UnwindData |  |
| 112 | `GetIpNetTable` | `0xEF00` | 540 | UnwindData |  |
| 19 | `ConvertInterfaceLuidToIndex` | `0xF130` | 27 | UnwindData |  |
| 247 | `NhGetInterfaceNameFromDeviceGuid` | `0xF1C0` | 80 | UnwindData |  |
| 248 | `NhGetInterfaceNameFromGuid` | `0xF1C0` | 80 | UnwindData |  |
| 15 | `ConvertInterfaceGuidToLuid` | `0xF220` | 323 | UnwindData |  |
| 17 | `ConvertInterfaceLuidToAlias` | `0xF370` | 251 | UnwindData |  |
| 131 | `GetOwnerModuleFromUdpEntry` | `0xF4A0` | 54 | UnwindData |  |
| 128 | `GetOwnerModuleFromTcp6Entry` | `0xF4E0` | 54 | UnwindData |  |
| 129 | `GetOwnerModuleFromTcpEntry` | `0xF520` | 54 | UnwindData |  |
| 127 | `GetOwnerModuleFromPidAndInfo` | `0xF560` | 143 | UnwindData |  |
| 82 | `GetExtendedTcpTable` | `0x100A0` | 341 | UnwindData |  |
| 68 | `GetAdapterIndex` | `0x10200` | 501 | UnwindData |  |
| 138 | `GetSessionCompartmentId` | `0x10400` | 94 | UnwindData |  |
| 79 | `GetCurrentThreadCompartmentScope` | `0x104A0` | 146 | UnwindData |  |
| 83 | `GetExtendedUdpTable` | `0x10540` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `GetIpForwardTable` | `0x105C0` | 946 | UnwindData |  |
| 91 | `GetIfEntry2Ex` | `0x10AC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `GetIfTable` | `0x10AF0` | 419 | UnwindData |  |
| 125 | `GetNetworkParams` | `0x10CA0` | 392 | UnwindData |  |
| 118 | `GetIpStatisticsEx` | `0x110B0` | 538 | UnwindData |  |
| 162 | `IcmpSendEcho` | `0x113C0` | 90 | UnwindData |  |
| 163 | `IcmpSendEcho2` | `0x11420` | 105 | UnwindData |  |
| 164 | `IcmpSendEcho2Ex` | `0x11490` | 1,012 | UnwindData |  |
| 161 | `IcmpParseReplies` | `0x11890` | 74 | UnwindData |  |
| 89 | `GetIfEntry` | `0x11920` | 359 | UnwindData |  |
| 135 | `GetPerTcpConnectionEStats` | `0x11F00` | 608 | UnwindData |  |
| 285 | `SetCurrentThreadCompartmentScope` | `0x12170` | 80 | UnwindData |  |
| 90 | `GetIfEntry2` | `0x121D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `GetIpInterfaceEntry` | `0x121F0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 261 | `ParseNetworkString` | `0x12260` | 1,734 | UnwindData |  |
| 87 | `GetIcmpStatistics` | `0x12930` | 292 | UnwindData |  |
| 88 | `GetIcmpStatisticsEx` | `0x12A60` | 230 | UnwindData |  |
| 34 | `ConvertStringToGuidW` | `0x12B50` | 87 | UnwindData |  |
| 191 | `InternalGetIfEntry2` | `0x12BB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `GetNumberOfInterfaces` | `0x12BC0` | 142 | UnwindData |  |
| 140 | `GetTcp6Table2` | `0x12C60` | 702 | UnwindData |  |
| 94 | `GetIfTable2` | `0x12F30` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `GetNetworkConnectivityHint` | `0x13040` | 182 | UnwindData |  |
| 154 | `GetUnicastIpAddressTable` | `0x131C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `GetJobCompartmentId` | `0x131E0` | 101 | UnwindData |  |
| 311 | `if_indextoname` | `0x13300` | 135 | UnwindData |  |
| 20 | `ConvertInterfaceLuidToNameA` | `0x13390` | 166 | UnwindData |  |
| 95 | `GetIfTable2Ex` | `0x13440` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `GetIpInterfaceTable` | `0x134A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 250 | `NotifyAddrChange` | `0x134C0` | 45 | UnwindData |  |
| 225 | `InternalGetUnicastIpAddressTable` | `0x13500` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `ConvertRemoteInterfaceLuidToAlias` | `0x13860` | 293 | UnwindData |  |
| 25 | `ConvertIpv4MaskToLength` | `0x13990` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `InitializeIpInterfaceEntry` | `0x139D0` | 55 | UnwindData |  |
| 111 | `GetIpNetEntry2` | `0x13A30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 230 | `InternalSetIpInterfaceEntry` | `0x13A50` | 957 | UnwindData |  |
| 212 | `InternalGetTcpTableWithOwnerModule` | `0x13E40` | 46 | UnwindData |  |
| 206 | `InternalGetTcp6TableWithOwnerModule` | `0x13E80` | 46 | UnwindData |  |
| 205 | `InternalGetTcp6Table2` | `0x13EC0` | 46 | UnwindData |  |
| 210 | `InternalGetTcpTable2` | `0x13F00` | 46 | UnwindData |  |
| 215 | `InternalGetUdp6Table2` | `0x13F40` | 46 | UnwindData |  |
| 220 | `InternalGetUdpTable2` | `0x13F80` | 46 | UnwindData |  |
| 192 | `InternalGetIfTable` | `0x13FC0` | 46 | UnwindData |  |
| 108 | `GetIpForwardTable2` | `0x14100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `GetPerTcp6ConnectionEStats` | `0x14120` | 658 | UnwindData |  |
| 113 | `GetIpNetTable2` | `0x143C0` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `CancelIPChangeNotify` | `0x14670` | 31 | UnwindData |  |
| 158 | `Icmp6SendEcho2` | `0x146A0` | 1,060 | UnwindData |  |
| 167 | `InitializeIpForwardEntry` | `0x14B80` | 50 | UnwindData |  |
| 32 | `ConvertRemoteInterfaceLuidToIndex` | `0x150B0` | 118 | UnwindData |  |
| 204 | `InternalGetRtcSlotInformation` | `0x15130` | 499 | UnwindData |  |
| 153 | `GetUnicastIpAddressEntry` | `0x156A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `DeleteIpForwardEntry` | `0x156C0` | 285 | UnwindData |  |
| 190 | `InternalGetIPPhysicalInterfaceForDestination` | `0x157F0` | 1,701 | UnwindData |  |
| 224 | `InternalGetUnicastIpAddressEntry` | `0x15EF0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 160 | `IcmpCreateFile` | `0x15FA0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `InitializeUnicastIpAddressEntry` | `0x16060` | 53 | UnwindData |  |
| 86 | `GetFriendlyIfIndex` | `0x160A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `GetIpForwardEntry2` | `0x160B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 170 | `InternalCleanupPersistentStore` | `0x160D0` | 161 | UnwindData |  |
| 256 | `NotifyRouteChange2` | `0x16750` | 205 | UnwindData |  |
| 117 | `GetIpStatistics` | `0x16830` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 284 | `SetCurrentThreadCompartmentId` | `0x169C0` | 78 | UnwindData |  |
| 255 | `NotifyRouteChange` | `0x16A50` | 45 | UnwindData |  |
| 66 | `FreeInterfaceDnsSettings` | `0x16A90` | 211 | UnwindData |  |
| 236 | `InternalSetTeredoPort` | `0x16B70` | 74 | UnwindData |  |
| 99 | `GetInterfaceDnsSettings` | `0x16BC0` | 311 | UnwindData |  |
| 39 | `CreateIpForwardEntry` | `0x16DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `ConvertCompartmentGuidToId` | `0x16DC0` | 145 | UnwindData |  |
| 144 | `GetTcpTable` | `0x16E60` | 26 | UnwindData |  |
| 157 | `Icmp6ParseReplies` | `0x17000` | 62 | UnwindData |  |
| 156 | `Icmp6CreateFile` | `0x17050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `ConvertCompartmentIdToGuid` | `0x17070` | 253 | UnwindData |  |
| 141 | `GetTcpStatistics` | `0x171D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 254 | `NotifyNetworkConnectivityHintChange` | `0x171E0` | 350 | UnwindData |  |
| 286 | `SetDnsSettings` | `0x17350` | 152 | UnwindData |  |
| 65 | `FreeDnsSettings` | `0x173F0` | 107 | UnwindData |  |
| 130 | `GetOwnerModuleFromUdp6Entry` | `0x17470` | 54 | UnwindData |  |
| 139 | `GetTcp6Table` | `0x174B0` | 604 | UnwindData |  |
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
| 159 | `IcmpCloseHandle` | `0x18490` | 264 | UnwindData |  |
| 6 | `CancelMibChangeNotify2` | `0x18780` | 241 | UnwindData |  |
| 28 | `ConvertRemoteInterfaceGuidToLuid` | `0x18900` | 336 | UnwindData |  |
| 148 | `GetUdpStatistics` | `0x18AE0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `CreateUnicastIpAddressEntry` | `0x18BB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `DeleteUnicastIpAddressEntry` | `0x18BD0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `InternalDeleteUnicastIpAddressEntry` | `0x18C70` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `CreateIpForwardEntry2` | `0x18D50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `CreateIpNetEntry2` | `0x18D70` | 9,376 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `GetIpErrorString` | `0x1B210` | 198 | UnwindData |  |
| 2 | `AllocateAndGetInterfaceInfoFromStack` | `0x1B2E0` | 571 | UnwindData |  |
| 249 | `NhpAllocateAndGetInterfaceInfoFromStack` | `0x1B2E0` | 571 | UnwindData |  |
| 31 | `ConvertRemoteInterfaceLuidToGuid` | `0x1B540` | 122 | UnwindData |  |
| 33 | `ConvertStringToGuidA` | `0x1B5C0` | 116 | UnwindData |  |
| 69 | `GetAdapterOrderMap` | `0x1B640` | 310 | UnwindData |  |
| 245 | `NhGetGuidFromInterfaceName` | `0x1B780` | 49 | UnwindData |  |
| 246 | `NhGetInterfaceDescriptionFromGuid` | `0x1B7C0` | 285 | UnwindData |  |
| 288 | `SetIfEntry` | `0x1B8F0` | 130 | UnwindData |  |
| 3 | `AllocateAndGetIpAddrTableFromStack` | `0x1B9D0` | 35 | UnwindData |  |
| 60 | `DisableMediaSense` | `0x1BA00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `GetWPAOACSupportLevel` | `0x1BA00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 281 | `RestoreMediaSense` | `0x1BA00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 172 | `InternalCreateIpForwardEntry` | `0x1BA10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 174 | `InternalCreateIpNetEntry` | `0x1BA30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `InternalDeleteIpForwardEntry` | `0x1BA50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `InternalDeleteIpNetEntry` | `0x1BA60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 187 | `InternalGetBoundTcp6EndpointTable` | `0x1BA70` | 46 | UnwindData |  |
| 188 | `InternalGetBoundTcpEndpointTable` | `0x1BAB0` | 46 | UnwindData |  |
| 194 | `InternalGetIpAddrTable` | `0x1BC60` | 46 | UnwindData |  |
| 196 | `InternalGetIpForwardTable` | `0x1BCA0` | 46 | UnwindData |  |
| 200 | `InternalGetIpNetTable` | `0x1BCE0` | 46 | UnwindData |  |
| 207 | `InternalGetTcp6TableWithOwnerPid` | `0x1BD20` | 46 | UnwindData |  |
| 209 | `InternalGetTcpTable` | `0x1BD60` | 46 | UnwindData |  |
| 211 | `InternalGetTcpTableEx` | `0x1BDA0` | 46 | UnwindData |  |
| 213 | `InternalGetTcpTableWithOwnerPid` | `0x1BDE0` | 46 | UnwindData |  |
| 216 | `InternalGetUdp6TableWithOwnerModule` | `0x1BE20` | 46 | UnwindData |  |
| 217 | `InternalGetUdp6TableWithOwnerPid` | `0x1BE60` | 46 | UnwindData |  |
| 219 | `InternalGetUdpTable` | `0x1BEA0` | 46 | UnwindData |  |
| 221 | `InternalGetUdpTableEx` | `0x1BEE0` | 46 | UnwindData |  |
| 222 | `InternalGetUdpTableWithOwnerModule` | `0x1BF20` | 46 | UnwindData |  |
| 223 | `InternalGetUdpTableWithOwnerPid` | `0x1BF60` | 46 | UnwindData |  |
| 226 | `InternalIcmpCreateFileEx` | `0x1BFA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 227 | `InternalSetIfEntry` | `0x1BFD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 228 | `InternalSetIpForwardEntry` | `0x1BFE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 231 | `InternalSetIpNetEntry` | `0x1C000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 233 | `InternalSetIpStats` | `0x1C020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 235 | `InternalSetTcpEntry` | `0x1C040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 283 | `SetAdapterIpAddress` | `0x1C050` | 351 | UnwindData |  |
| 1 | `AddIPAddress` | `0x1C1D0` | 278 | UnwindData |  |
| 41 | `CreateIpNetEntry` | `0x1C2F0` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `CreateProxyArpEntry` | `0x1C460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `DeleteIPAddress` | `0x1C480` | 254 | UnwindData |  |
| 58 | `DeleteProxyArpEntry` | `0x1C590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `EnableRouter` | `0x1C5B0` | 94 | UnwindData |  |
| 62 | `FlushIpNetTable` | `0x1C620` | 127 | UnwindData |  |
| 152 | `GetUniDirectionalAdapterInfo` | `0x1C6B0` | 285 | UnwindData |  |
| 239 | `IpReleaseAddress` | `0x1C7E0` | 75 | UnwindData |  |
| 240 | `IpRenewAddress` | `0x1C840` | 75 | UnwindData |  |
| 98 | `GetInterfaceCurrentTimestampCapabilities` | `0x1C8A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `GetInterfaceHardwareTimestampCapabilities` | `0x1C8A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 252 | `NotifyIfTimestampConfigChange` | `0x1C8A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 280 | `ResolveNeighbor` | `0x1C8A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 293 | `SetIpNetEntry` | `0x1C8B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 295 | `SetIpStatistics` | `0x1C8C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 296 | `SetIpStatisticsEx` | `0x1C8D0` | 218 | UnwindData |  |
| 297 | `SetIpTTL` | `0x1C9B0` | 125 | UnwindData |  |
| 307 | `UnenableRouter` | `0x1CAE0` | 124 | UnwindData |  |
| 243 | `NTPTimeToNTFileTime` | `0x1CB70` | 146 | UnwindData |  |
| 244 | `NTTimeToNTPTime` | `0x1CC10` | 231 | UnwindData |  |
| 262 | `PfAddFiltersToInterface` | `0x1CEA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 263 | `PfAddGlobalFilterToInterface` | `0x1CEA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 264 | `PfBindInterfaceToIPAddress` | `0x1CEA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 265 | `PfBindInterfaceToIndex` | `0x1CEA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 266 | `PfCreateInterface` | `0x1CEA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 267 | `PfDeleteInterface` | `0x1CEA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 268 | `PfDeleteLog` | `0x1CEA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 269 | `PfGetInterfaceStatistics` | `0x1CEA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 270 | `PfMakeLog` | `0x1CEA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 271 | `PfRebindFilters` | `0x1CEA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 272 | `PfRemoveFilterHandles` | `0x1CEA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 273 | `PfRemoveFiltersFromInterface` | `0x1CEA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 274 | `PfRemoveGlobalFilterFromInterface` | `0x1CEA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 275 | `PfSetLogBuffer` | `0x1CEA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 276 | `PfTestPacket` | `0x1CEA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 277 | `PfUnBindInterface` | `0x1CEA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `GetRTTAndHopCount` | `0x1CEB0` | 633 | UnwindData |  |
| 309 | `do_echo_rep` | `0x1D130` | 471 | UnwindData |  |
| 310 | `do_echo_req` | `0x1D310` | 380 | UnwindData |  |
| 313 | `register_icmp` | `0x1D4A0` | 52 | UnwindData |  |
| 208 | `InternalGetTcpDynamicPortRange` | `0x1D560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 218 | `InternalGetUdpDynamicPortRange` | `0x1D580` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 234 | `InternalSetTcpDynamicPortRange` | `0x1D610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 237 | `InternalSetUdpDynamicPortRange` | `0x1D630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `CreatePersistentTcpPortReservation` | `0x1D650` | 46 | UnwindData |  |
| 44 | `CreatePersistentUdpPortReservation` | `0x1D690` | 46 | UnwindData |  |
| 56 | `DeletePersistentTcpPortReservation` | `0x1D6D0` | 47 | UnwindData |  |
| 57 | `DeletePersistentUdpPortReservation` | `0x1D710` | 45 | UnwindData |  |
| 241 | `LookupPersistentTcpPortReservation` | `0x1D860` | 44 | UnwindData |  |
| 242 | `LookupPersistentUdpPortReservation` | `0x1D8A0` | 44 | UnwindData |  |
| 134 | `GetPerTcp6ConnectionStats` | `0x1DDD0` | 182 | UnwindData |  |
| 136 | `GetPerTcpConnectionStats` | `0x1DE90` | 183 | UnwindData |  |
| 143 | `GetTcpStatisticsEx2` | `0x1DF90` | 322 | UnwindData |  |
| 301 | `SetPerTcp6ConnectionStats` | `0x1E3E0` | 171 | UnwindData |  |
| 302 | `SetPerTcpConnectionEStats` | `0x1E4A0` | 244 | UnwindData |  |
| 303 | `SetPerTcpConnectionStats` | `0x1E5A0` | 158 | UnwindData |  |
| 305 | `SetTcpEntry` | `0x1E650` | 169 | UnwindData |  |
| 147 | `GetUdp6Table` | `0x1E720` | 528 | UnwindData |  |
| 150 | `GetUdpStatisticsEx2` | `0x1E940` | 238 | UnwindData |  |
| 151 | `GetUdpTable` | `0x1EA40` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `CancelIfTimestampConfigChange` | `0x1EC80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `CaptureInterfaceHardwareCrossTimestamp` | `0x1EC90` | 310 | UnwindData |  |
| 96 | `GetInterfaceActiveTimestampCapabilities` | `0x1EE10` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `GetInterfaceSupportedTimestampCapabilities` | `0x1EFD0` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 278 | `RegisterInterfaceTimestampConfigChange` | `0x1F210` | 208 | UnwindData |  |
| 308 | `UnregisterInterfaceTimestampConfigChange` | `0x1F2F0` | 76 | UnwindData |  |
| 8 | `CloseCompartment` | `0x1F450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `CreateCompartment` | `0x1F470` | 397 | UnwindData |  |
| 49 | `DeleteCompartment` | `0x1F610` | 73 | UnwindData |  |
| 97 | `GetInterfaceCompartmentId` | `0x1F660` | 95 | UnwindData |  |
| 165 | `InitializeCompartmentEntry` | `0x1F6D0` | 41 | UnwindData |  |
| 251 | `NotifyCompartmentChange` | `0x1F790` | 142 | UnwindData |  |
| 260 | `OpenCompartment` | `0x1F830` | 376 | UnwindData |  |
| 298 | `SetJobCompartmentId` | `0x1F9B0` | 93 | UnwindData |  |
| 299 | `SetNetworkInformation` | `0x1FA20` | 233 | UnwindData |  |
| 304 | `SetSessionCompartmentId` | `0x1FB10` | 87 | UnwindData |  |
| 14 | `ConvertInterfaceAliasToLuid` | `0x1FB70` | 416 | UnwindData |  |
| 24 | `ConvertInterfacePhysicalAddressToLuid` | `0x1FD20` | 376 | UnwindData |  |
| 35 | `ConvertStringToInterfacePhysicalAddress` | `0x1FEA0` | 179 | UnwindData |  |
| 36 | `CreateAnycastIpAddressEntry` | `0x1FF60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `DeleteAnycastIpAddressEntry` | `0x1FF80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `GetAnycastIpAddressEntry` | `0x1FFA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `GetAnycastIpAddressTable` | `0x1FFC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `GetMulticastIpAddressEntry` | `0x1FFE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `GetMulticastIpAddressTable` | `0x20000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 171 | `InternalCreateAnycastIpAddressEntry` | `0x20020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 178 | `InternalDeleteAnycastIpAddressEntry` | `0x20040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `InternalGetAnycastIpAddressEntry` | `0x20060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `InternalGetAnycastIpAddressTable` | `0x20080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | `InternalGetMulticastIpAddressEntry` | `0x200A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 203 | `InternalGetMulticastIpAddressTable` | `0x200C0` | 704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 238 | `InternalSetUnicastIpAddressEntry` | `0x20380` | 1,552 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 257 | `NotifyStableUnicastIpAddressTable` | `0x20990` | 36 | UnwindData |  |
| 306 | `SetUnicastIpAddressEntry` | `0x20BB0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `CreateFlVirtualInterface` | `0x20D10` | 161 | UnwindData |  |
| 50 | `DeleteFlVirtualInterface` | `0x20DC0` | 148 | UnwindData |  |
| 84 | `GetFlVirtualInterface` | `0x20F90` | 286 | UnwindData |  |
| 85 | `GetFlVirtualInterfaceTable` | `0x210C0` | 647 | UnwindData |  |
| 166 | `InitializeFlVirtualInterfaceEntry` | `0x21350` | 42 | UnwindData |  |
| 287 | `SetFlVirtualInterface` | `0x21380` | 158 | UnwindData |  |
| 176 | `InternalCreateOrRefIpForwardEntry2` | `0x21430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 229 | `InternalSetIpForwardEntry2` | `0x21450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 291 | `SetIpForwardEntry2` | `0x21470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `DeleteIpNetEntry2` | `0x21490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 182 | `InternalDeleteIpNetEntry2` | `0x214B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 232 | `InternalSetIpNetEntry2` | `0x214D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 294 | `SetIpNetEntry2` | `0x214F0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `FlushIpPathTable` | `0x215E0` | 225 | UnwindData |  |
| 115 | `GetIpPathEntry` | `0x216D0` | 529 | UnwindData |  |
| 116 | `GetIpPathTable` | `0x218F0` | 675 | UnwindData |  |
| 289 | `SetInterfaceDnsSettings` | `0x21BA0` | 436 | UnwindData |  |
| 103 | `GetInvertedIfStackTable` | `0x21D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 193 | `InternalGetIfTable2` | `0x21D70` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `GetNetworkConnectivityHintForInterface` | `0x21E60` | 697 | UnwindData |  |
| 146 | `GetTeredoPort` | `0x22120` | 124 | UnwindData |  |
| 258 | `NotifyTeredoPortChange` | `0x221E0` | 165 | UnwindData |  |
