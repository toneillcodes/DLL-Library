# Binary Specification: wshqos.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wshqos.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c6b4847560629654394eb539b1e3e2e8941c7e5a305f9bb3093506a0be2b0aa0`
* **Total Exported Functions:** 15

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `WSHGetSocketInformation` | `0x1010` | 133 | UnwindData |  |
| 13 | `WSHOpenSocket2` | `0x1280` | 157 | UnwindData |  |
| 11 | `WSHNotify` | `0x1500` | 106 | UnwindData |  |
| 4 | `WSHGetSockaddrType` | `0x1670` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `WSHAddressToString` | `0x16E0` | 70 | UnwindData |  |
| 7 | `WSHGetWildcardSockaddr` | `0x1730` | 2,784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `WSHEnumProtocols` | `0x2210` | 489 | UnwindData |  |
| 3 | `WSHGetProviderGuid` | `0x2400` | 74 | UnwindData |  |
| 6 | `WSHGetWSAProtocolInfo` | `0x2450` | 98 | UnwindData |  |
| 8 | `WSHGetWinsockMapping` | `0x24C0` | 132 | UnwindData |  |
| 9 | `WSHIoctl` | `0x2550` | 467 | UnwindData |  |
| 10 | `WSHJoinLeaf` | `0x2730` | 301 | UnwindData |  |
| 12 | `WSHOpenSocket` | `0x2870` | 48 | UnwindData |  |
| 14 | `WSHSetSocketInformation` | `0x28B0` | 77 | UnwindData |  |
| 15 | `WSHStringToAddress` | `0x2910` | 62 | UnwindData |  |
