# Binary Specification: wshhyperv.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wshhyperv.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0e01bd8386df69fda8774fe09aab974fa7c295a3cc3f57f6744dda3a44a6e152`
* **Total Exported Functions:** 16

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `WSHAddressToString` | `0x12C0` | 129 | UnwindData |  |
| 2 | `WSHEnumProtocols` | `0x1350` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `WSHGetBroadcastSockaddr` | `0x13F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `WSHGetProviderGuid` | `0x1430` | 74 | UnwindData |  |
| 5 | `WSHGetSockaddrType` | `0x1480` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `WSHGetSocketInformation` | `0x1510` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `WSHGetWSAProtocolInfo` | `0x1560` | 98 | UnwindData |  |
| 8 | `WSHGetWildcardSockaddr` | `0x15D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `WSHGetWinsockMapping` | `0x1610` | 50 | UnwindData |  |
| 10 | `WSHIoctl` | `0x1650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `WSHJoinLeaf` | `0x1660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `WSHNotify` | `0x1680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `WSHOpenSocket` | `0x1690` | 48 | UnwindData |  |
| 14 | `WSHOpenSocket2` | `0x16D0` | 105 | UnwindData |  |
| 15 | `WSHSetSocketInformation` | `0x1740` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `WSHStringToAddress` | `0x1770` | 162 | UnwindData |  |
