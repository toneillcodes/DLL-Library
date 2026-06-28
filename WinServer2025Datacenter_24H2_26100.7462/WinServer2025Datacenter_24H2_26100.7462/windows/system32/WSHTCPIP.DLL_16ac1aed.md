# Binary Specification: WSHTCPIP.DLL

## Binary Metadata
* **Original Path:** `c:\windows\system32\WSHTCPIP.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `16ac1aed18660dc229644e5c11e2d5190c61a7b6cf250f2d09d7118bcd76ba83`
* **Total Exported Functions:** 16

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `WSHGetSockaddrType` | `0x1010` | 148 | UnwindData |  |
| 14 | `WSHOpenSocket2` | `0x10B0` | 779 | UnwindData |  |
| 6 | `WSHGetSocketInformation` | `0x13D0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `WSHNotify` | `0x1420` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `WSHGetWildcardSockaddr` | `0x1460` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `WSHAddressToString` | `0x17B0` | 151 | UnwindData |  |
| 2 | `WSHEnumProtocols` | `0x1850` | 375 | UnwindData |  |
| 3 | `WSHGetBroadcastSockaddr` | `0x19D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `WSHGetProviderGuid` | `0x1A10` | 74 | UnwindData |  |
| 7 | `WSHGetWSAProtocolInfo` | `0x1A60` | 98 | UnwindData |  |
| 9 | `WSHGetWinsockMapping` | `0x1AD0` | 105 | UnwindData |  |
| 10 | `WSHIoctl` | `0x1B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `WSHJoinLeaf` | `0x1B50` | 220 | UnwindData |  |
| 13 | `WSHOpenSocket` | `0x1C40` | 48 | UnwindData |  |
| 15 | `WSHSetSocketInformation` | `0x1C80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `WSHStringToAddress` | `0x1CB0` | 126 | UnwindData |  |
