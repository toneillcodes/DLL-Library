# Binary Specification: wsock32.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wsock32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7c6658e8ddb19e10679c13050bc7febc33d190b162b653ebafb0da6e7d292519`
* **Total Exported Functions:** 75

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1141 | `AcceptEx` | `0x0` | - | Forwarded | Forwarded to: `MSWSOCK.AcceptEx` |
| 1111 | `EnumProtocolsA` | `0x0` | - | Forwarded | Forwarded to: `MSWSOCK.EnumProtocolsA` |
| 1112 | `EnumProtocolsW` | `0x0` | - | Forwarded | Forwarded to: `MSWSOCK.EnumProtocolsW` |
| 1142 | `GetAcceptExSockaddrs` | `0x0` | - | Forwarded | Forwarded to: `MSWSOCK.GetAcceptExSockaddrs` |
| 1109 | `GetAddressByNameA` | `0x0` | - | Forwarded | Forwarded to: `MSWSOCK.GetAddressByNameA` |
| 1110 | `GetAddressByNameW` | `0x0` | - | Forwarded | Forwarded to: `MSWSOCK.GetAddressByNameW` |
| 1115 | `GetNameByTypeA` | `0x0` | - | Forwarded | Forwarded to: `MSWSOCK.GetNameByTypeA` |
| 1116 | `GetNameByTypeW` | `0x0` | - | Forwarded | Forwarded to: `MSWSOCK.GetNameByTypeW` |
| 1119 | `GetServiceA` | `0x0` | - | Forwarded | Forwarded to: `MSWSOCK.GetServiceA` |
| 1120 | `GetServiceW` | `0x0` | - | Forwarded | Forwarded to: `MSWSOCK.GetServiceW` |
| 1113 | `GetTypeByNameA` | `0x0` | - | Forwarded | Forwarded to: `MSWSOCK.GetTypeByNameA` |
| 1114 | `GetTypeByNameW` | `0x0` | - | Forwarded | Forwarded to: `MSWSOCK.GetTypeByNameW` |
| 24 | `MigrateWinsockConfiguration` | `0x0` | - | Forwarded | Forwarded to: `MSWSOCK.MigrateWinsockConfiguration` |
| 1130 | `NPLoadNameSpaces` | `0x0` | - | Forwarded | Forwarded to: `MSWSOCK.NPLoadNameSpaces` |
| 1117 | `SetServiceA` | `0x0` | - | Forwarded | Forwarded to: `MSWSOCK.SetServiceA` |
| 1118 | `SetServiceW` | `0x0` | - | Forwarded | Forwarded to: `MSWSOCK.SetServiceW` |
| 1140 | `TransmitFile` | `0x0` | - | Forwarded | Forwarded to: `MSWSOCK.TransmitFile` |
| 500 | `WEP` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.WEP` |
| 102 | `WSAAsyncGetHostByAddr` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.WSAAsyncGetHostByAddr` |
| 103 | `WSAAsyncGetHostByName` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.WSAAsyncGetHostByName` |
| 105 | `WSAAsyncGetProtoByName` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.WSAAsyncGetProtoByName` |
| 104 | `WSAAsyncGetProtoByNumber` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.WSAAsyncGetProtoByNumber` |
| 107 | `WSAAsyncGetServByName` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.WSAAsyncGetServByName` |
| 106 | `WSAAsyncGetServByPort` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.WSAAsyncGetServByPort` |
| 101 | `WSAAsyncSelect` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.WSAAsyncSelect` |
| 108 | `WSACancelAsyncRequest` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.WSACancelAsyncRequest` |
| 113 | `WSACancelBlockingCall` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.WSACancelBlockingCall` |
| 116 | `WSACleanup` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.WSACleanup` |
| 111 | `WSAGetLastError` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.WSAGetLastError` |
| 114 | `WSAIsBlocking` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.WSAIsBlocking` |
| 1107 | `WSARecvEx` | `0x0` | - | Forwarded | Forwarded to: `MSWSOCK.WSARecvEx` |
| 109 | `WSASetBlockingHook` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.WSASetBlockingHook` |
| 112 | `WSASetLastError` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.WSASetLastError` |
| 115 | `WSAStartup` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.WSAStartup` |
| 110 | `WSAUnhookBlockingHook` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.WSAUnhookBlockingHook` |
| 1000 | `WSApSetPostRoutine` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.WSApSetPostRoutine` |
| 151 | `__WSAFDIsSet` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.__WSAFDIsSet` |
| 1 | `accept` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.accept` |
| 2 | `bind` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.bind` |
| 3 | `closesocket` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.closesocket` |
| 4 | `connect` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.connect` |
| 1106 | `dn_expand` | `0x0` | - | Forwarded | Forwarded to: `MSWSOCK.dn_expand` |
| 51 | `gethostbyaddr` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.gethostbyaddr` |
| 52 | `gethostbyname` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.gethostbyname` |
| 57 | `gethostname` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.gethostname` |
| 1101 | `getnetbyname` | `0x0` | - | Forwarded | Forwarded to: `MSWSOCK.getnetbyname` |
| 5 | `getpeername` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.getpeername` |
| 53 | `getprotobyname` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.getprotobyname` |
| 54 | `getprotobynumber` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.getprotobynumber` |
| 55 | `getservbyname` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.getservbyname` |
| 56 | `getservbyport` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.getservbyport` |
| 6 | `getsockname` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.getsockname` |
| 8 | `htonl` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.htonl` |
| 9 | `htons` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.htons` |
| 10 | `inet_addr` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.inet_addr` |
| 1100 | `inet_network` | `0x0` | - | Forwarded | Forwarded to: `MSWSOCK.inet_network` |
| 11 | `inet_ntoa` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.inet_ntoa` |
| 12 | `ioctlsocket` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.ioctlsocket` |
| 13 | `listen` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.listen` |
| 14 | `ntohl` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.ntohl` |
| 15 | `ntohs` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.ntohs` |
| 1102 | `rcmd` | `0x0` | - | Forwarded | Forwarded to: `MSWSOCK.rcmd` |
| 1103 | `rexec` | `0x0` | - | Forwarded | Forwarded to: `MSWSOCK.rexec` |
| 1104 | `rresvport` | `0x0` | - | Forwarded | Forwarded to: `MSWSOCK.rresvport` |
| 1108 | `s_perror` | `0x0` | - | Forwarded | Forwarded to: `MSWSOCK.s_perror` |
| 18 | `select` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.select` |
| 19 | `send` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.send` |
| 20 | `sendto` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.sendto` |
| 1105 | `sethostname` | `0x0` | - | Forwarded | Forwarded to: `MSWSOCK.sethostname` |
| 22 | `shutdown` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.shutdown` |
| 23 | `socket` | `0x0` | - | Forwarded | Forwarded to: `ws2_32.socket` |
| 16 | `recv` | `0x1010` | 120 | UnwindData |  |
| 17 | `recvfrom` | `0x1090` | 153 | UnwindData |  |
| 21 | `setsockopt` | `0x1130` | 119 | UnwindData |  |
| 7 | `getsockopt` | `0x1240` | 147 | UnwindData |  |
