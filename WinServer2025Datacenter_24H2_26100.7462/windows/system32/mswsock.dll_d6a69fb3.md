# Binary Specification: mswsock.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\mswsock.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d6a69fb3926d8d41217ce479d1d8d61256a11eea0d8ea63afe2e3dec125a5287`
* **Total Exported Functions:** 64

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 56 | `WSPStartup` | `0xCD50` | 899 | UnwindData |  |
| 17 | `NSPStartup` | `0xE830` | 70 | UnwindData |  |
| 43 | `Tcpip6_WSHGetSocketInformation` | `0x170A0` | 3,632 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `Tcpip4_WSHGetSockaddrType` | `0x17ED0` | 148 | UnwindData |  |
| 51 | `Tcpip6_WSHOpenSocket2` | `0x17F70` | 809 | UnwindData |  |
| 28 | `Tcpip4_WSHGetSocketInformation` | `0x18D40` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `Tcpip6_WSHGetSockaddrType` | `0x18EF0` | 231 | UnwindData |  |
| 36 | `Tcpip4_WSHOpenSocket2` | `0x192A0` | 828 | UnwindData |  |
| 23 | `Tcpip4_WSHAddressToString` | `0x19AD0` | 153 | UnwindData |  |
| 39 | `Tcpip6_WSHAddressToString` | `0x1A180` | 153 | UnwindData |  |
| 38 | `Tcpip4_WSHStringToAddress` | `0x1A400` | 126 | UnwindData |  |
| 53 | `Tcpip6_WSHStringToAddress` | `0x1D530` | 139 | UnwindData |  |
| 30 | `Tcpip4_WSHGetWildcardSockaddr` | `0x1D6B0` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `Tcpip6_WSHGetWildcardSockaddr` | `0x1D9A0` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `AcceptEx` | `0x1DE00` | 429 | UnwindData |  |
| 4 | `GetAcceptExSockaddrs` | `0x1E520` | 225 | UnwindData |  |
| 37 | `Tcpip4_WSHSetSocketInformation` | `0x1E610` | 24,176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `Tcpip6_WSHSetSocketInformation` | `0x1E610` | 24,176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `ProcessSocketNotifications` | `0x24480` | 446 | UnwindData |  |
| 21 | `StartWsdpService` | `0x249A0` | 814 | UnwindData |  |
| 22 | `StopWsdpService` | `0x24CE0` | 78 | UnwindData |  |
| 58 | `getnetbyname` | `0x24DC0` | 29 | UnwindData |  |
| 59 | `inet_network` | `0x24DF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `rcmd` | `0x24E00` | 31 | UnwindData |  |
| 61 | `rexec` | `0x24E00` | 31 | UnwindData |  |
| 62 | `rresvport` | `0x24E00` | 31 | UnwindData |  |
| 64 | `sethostname` | `0x24E30` | 30 | UnwindData |  |
| 57 | `dn_expand` | `0x2A410` | 315 | UnwindData |  |
| 54 | `TransmitFile` | `0x2AFE0` | 195 | UnwindData |  |
| 2 | `EnumProtocolsA` | `0x2B0B0` | 148 | UnwindData |  |
| 3 | `EnumProtocolsW` | `0x2B150` | 1,975 | UnwindData |  |
| 5 | `GetAddressByNameA` | `0x2C550` | 575 | UnwindData |  |
| 6 | `GetAddressByNameW` | `0x2C7A0` | 232 | UnwindData |  |
| 7 | `GetNameByTypeA` | `0x2C940` | 292 | UnwindData |  |
| 8 | `GetNameByTypeW` | `0x2CA70` | 783 | UnwindData |  |
| 12 | `GetTypeByNameA` | `0x2CD90` | 148 | UnwindData |  |
| 13 | `GetTypeByNameW` | `0x2CE30` | 696 | UnwindData |  |
| 9 | `GetServiceA` | `0x2D250` | 167 | UnwindData |  |
| 10 | `GetServiceW` | `0x2D300` | 56 | UnwindData |  |
| 19 | `SetServiceA` | `0x2DE30` | 545 | UnwindData |  |
| 20 | `SetServiceW` | `0x2E060` | 43 | UnwindData |  |
| 11 | `GetSocketErrorMessageW` | `0x2E340` | 1,733 | UnwindData |  |
| 63 | `s_perror` | `0x2EA10` | 78 | UnwindData |  |
| 16 | `NPLoadNameSpaces` | `0x2F150` | 353 | UnwindData |  |
| 55 | `WSARecvEx` | `0x2FEA0` | 123 | UnwindData |  |
| 14 | `MigrateWinsockConfiguration` | `0x32B00` | 44 | UnwindData |  |
| 15 | `MigrateWinsockConfigurationEx` | `0x32B40` | 3,120 | UnwindData |  |
| 24 | `Tcpip4_WSHEnumProtocols` | `0x365E0` | 373 | UnwindData |  |
| 25 | `Tcpip4_WSHGetBroadcastSockaddr` | `0x36760` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `Tcpip4_WSHGetProviderGuid` | `0x367A0` | 67 | UnwindData |  |
| 29 | `Tcpip4_WSHGetWSAProtocolInfo` | `0x367F0` | 91 | UnwindData |  |
| 31 | `Tcpip4_WSHGetWinsockMapping` | `0x36860` | 105 | UnwindData |  |
| 32 | `Tcpip4_WSHIoctl` | `0x368D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `Tcpip6_WSHIoctl` | `0x368D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `Tcpip4_WSHJoinLeaf` | `0x368E0` | 220 | UnwindData |  |
| 34 | `Tcpip4_WSHNotify` | `0x369D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `Tcpip4_WSHOpenSocket` | `0x36A10` | 48 | UnwindData |  |
| 40 | `Tcpip6_WSHEnumProtocols` | `0x36A50` | 380 | UnwindData |  |
| 41 | `Tcpip6_WSHGetProviderGuid` | `0x36BE0` | 67 | UnwindData |  |
| 44 | `Tcpip6_WSHGetWSAProtocolInfo` | `0x36C30` | 91 | UnwindData |  |
| 46 | `Tcpip6_WSHGetWinsockMapping` | `0x36CA0` | 105 | UnwindData |  |
| 48 | `Tcpip6_WSHJoinLeaf` | `0x36D10` | 281 | UnwindData |  |
| 49 | `Tcpip6_WSHNotify` | `0x36E30` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `Tcpip6_WSHOpenSocket` | `0x36E70` | 48 | UnwindData |  |
