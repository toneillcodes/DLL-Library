# Binary Specification: wshrm.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wshrm.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5cd4bcbf79bcfc7ed0261101a4aed7732b8d465257566d0e3e3d69209d5be0c4`
* **Total Exported Functions:** 16

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `WSHAddressToString` | `0x1D80` | 317 | UnwindData |  |
| 2 | `WSHEnumProtocols` | `0x1ED0` | 226 | UnwindData |  |
| 3 | `WSHGetBroadcastSockaddr` | `0x1FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `WSHGetProviderGuid` | `0x1FD0` | 85 | UnwindData |  |
| 5 | `WSHGetSockaddrType` | `0x2030` | 170 | UnwindData |  |
| 6 | `WSHGetSocketInformation` | `0x20E0` | 947 | UnwindData |  |
| 7 | `WSHGetWSAProtocolInfo` | `0x24A0` | 108 | UnwindData |  |
| 8 | `WSHGetWildcardSockaddr` | `0x2520` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `WSHGetWinsockMapping` | `0x2550` | 55 | UnwindData |  |
| 10 | `WSHIoctl` | `0x2590` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `WSHJoinLeaf` | `0x25C0` | 575 | UnwindData |  |
| 12 | `WSHNotify` | `0x2810` | 246 | UnwindData |  |
| 13 | `WSHOpenSocket` | `0x2910` | 48 | UnwindData |  |
| 14 | `WSHOpenSocket2` | `0x2950` | 305 | UnwindData |  |
| 15 | `WSHSetSocketInformation` | `0x2A90` | 925 | UnwindData |  |
| 16 | `WSHStringToAddress` | `0x2E40` | 460 | UnwindData |  |
