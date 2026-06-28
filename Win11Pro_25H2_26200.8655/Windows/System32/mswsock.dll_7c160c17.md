# Binary Specification: mswsock.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\mswsock.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7c160c171225c0d69ead13816aeefdc4245be116bc23eda7f604fb940702b525`
* **Total Exported Functions:** 64

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 56 | `WSPStartup` | `0xCEB0` | 901 | UnwindData |  |
| 17 | `NSPStartup` | `0xE9C0` | 70 | UnwindData |  |
| 43 | `Tcpip6_WSHGetSocketInformation` | `0x155B0` | 3,632 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `Tcpip4_WSHGetSockaddrType` | `0x163E0` | 148 | UnwindData |  |
| 51 | `Tcpip6_WSHOpenSocket2` | `0x16480` | 809 | UnwindData |  |
| 28 | `Tcpip4_WSHGetSocketInformation` | `0x172C0` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `Tcpip6_WSHGetSockaddrType` | `0x174E0` | 231 | UnwindData |  |
| 36 | `Tcpip4_WSHOpenSocket2` | `0x178A0` | 828 | UnwindData |  |
| 23 | `Tcpip4_WSHAddressToString` | `0x18A90` | 153 | UnwindData |  |
| 39 | `Tcpip6_WSHAddressToString` | `0x19300` | 153 | UnwindData |  |
| 38 | `Tcpip4_WSHStringToAddress` | `0x19510` | 126 | UnwindData |  |
| 53 | `Tcpip6_WSHStringToAddress` | `0x1C400` | 139 | UnwindData |  |
| 30 | `Tcpip4_WSHGetWildcardSockaddr` | `0x1C7E0` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `Tcpip6_WSHGetWildcardSockaddr` | `0x1CC40` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `AcceptEx` | `0x1D0A0` | 429 | UnwindData |  |
| 4 | `GetAcceptExSockaddrs` | `0x1D740` | 225 | UnwindData |  |
| 37 | `Tcpip4_WSHSetSocketInformation` | `0x1D830` | 29,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `Tcpip6_WSHSetSocketInformation` | `0x1D830` | 29,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `ProcessSocketNotifications` | `0x24BB0` | 446 | UnwindData |  |
| 21 | `StartWsdpService` | `0x25100` | 819 | UnwindData |  |
| 22 | `StopWsdpService` | `0x25440` | 78 | UnwindData |  |
| 58 | `getnetbyname` | `0x25520` | 29 | UnwindData |  |
| 59 | `inet_network` | `0x25550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `rcmd` | `0x25560` | 31 | UnwindData |  |
| 61 | `rexec` | `0x25560` | 31 | UnwindData |  |
| 62 | `rresvport` | `0x25560` | 31 | UnwindData |  |
| 64 | `sethostname` | `0x25590` | 30 | UnwindData |  |
| 57 | `dn_expand` | `0x2A9F0` | 320 | UnwindData |  |
| 54 | `TransmitFile` | `0x2B6A0` | 195 | UnwindData |  |
| 2 | `EnumProtocolsA` | `0x2B770` | 148 | UnwindData |  |
| 3 | `EnumProtocolsW` | `0x2B810` | 1,975 | UnwindData |  |
| 5 | `GetAddressByNameA` | `0x2CC10` | 575 | UnwindData |  |
| 6 | `GetAddressByNameW` | `0x2CE60` | 232 | UnwindData |  |
| 7 | `GetNameByTypeA` | `0x2D000` | 292 | UnwindData |  |
| 8 | `GetNameByTypeW` | `0x2D130` | 783 | UnwindData |  |
| 12 | `GetTypeByNameA` | `0x2D450` | 148 | UnwindData |  |
| 13 | `GetTypeByNameW` | `0x2D4F0` | 696 | UnwindData |  |
| 9 | `GetServiceA` | `0x2D910` | 167 | UnwindData |  |
| 10 | `GetServiceW` | `0x2D9C0` | 56 | UnwindData |  |
| 19 | `SetServiceA` | `0x2E4F0` | 545 | UnwindData |  |
| 20 | `SetServiceW` | `0x2E720` | 43 | UnwindData |  |
| 11 | `GetSocketErrorMessageW` | `0x2EA00` | 1,733 | UnwindData |  |
| 63 | `s_perror` | `0x2F0D0` | 78 | UnwindData |  |
| 16 | `NPLoadNameSpaces` | `0x2F810` | 353 | UnwindData |  |
| 55 | `WSARecvEx` | `0x30560` | 123 | UnwindData |  |
| 14 | `MigrateWinsockConfiguration` | `0x33620` | 44 | UnwindData |  |
| 15 | `MigrateWinsockConfigurationEx` | `0x33660` | 3,165 | UnwindData |  |
| 24 | `Tcpip4_WSHEnumProtocols` | `0x37200` | 373 | UnwindData |  |
| 25 | `Tcpip4_WSHGetBroadcastSockaddr` | `0x37380` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `Tcpip4_WSHGetProviderGuid` | `0x373C0` | 67 | UnwindData |  |
| 29 | `Tcpip4_WSHGetWSAProtocolInfo` | `0x37410` | 91 | UnwindData |  |
| 31 | `Tcpip4_WSHGetWinsockMapping` | `0x37480` | 105 | UnwindData |  |
| 32 | `Tcpip4_WSHIoctl` | `0x374F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `Tcpip6_WSHIoctl` | `0x374F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `Tcpip4_WSHJoinLeaf` | `0x37500` | 220 | UnwindData |  |
| 34 | `Tcpip4_WSHNotify` | `0x375F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `Tcpip4_WSHOpenSocket` | `0x37630` | 48 | UnwindData |  |
| 40 | `Tcpip6_WSHEnumProtocols` | `0x37670` | 380 | UnwindData |  |
| 41 | `Tcpip6_WSHGetProviderGuid` | `0x37800` | 67 | UnwindData |  |
| 44 | `Tcpip6_WSHGetWSAProtocolInfo` | `0x37850` | 91 | UnwindData |  |
| 46 | `Tcpip6_WSHGetWinsockMapping` | `0x378C0` | 105 | UnwindData |  |
| 48 | `Tcpip6_WSHJoinLeaf` | `0x37930` | 281 | UnwindData |  |
| 49 | `Tcpip6_WSHNotify` | `0x37A50` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `Tcpip6_WSHOpenSocket` | `0x37A90` | 48 | UnwindData |  |
