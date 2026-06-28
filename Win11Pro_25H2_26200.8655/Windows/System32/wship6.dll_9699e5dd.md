# Binary Specification: wship6.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wship6.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9699e5dd5edabcbf24269b2462c56ae00c40afa89e397cb47dd1f35583b7fa39`
* **Total Exported Functions:** 15

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `WSHAddressToString` | `0x12C0` | 151 | UnwindData |  |
| 2 | `WSHEnumProtocols` | `0x1360` | 478 | UnwindData |  |
| 3 | `WSHGetProviderGuid` | `0x1550` | 74 | UnwindData |  |
| 4 | `WSHGetSockaddrType` | `0x15A0` | 208 | UnwindData |  |
| 5 | `WSHGetSocketInformation` | `0x1680` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `WSHGetWSAProtocolInfo` | `0x16D0` | 98 | UnwindData |  |
| 7 | `WSHGetWildcardSockaddr` | `0x1740` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `WSHGetWinsockMapping` | `0x1790` | 105 | UnwindData |  |
| 9 | `WSHIoctl` | `0x1800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `WSHJoinLeaf` | `0x1810` | 281 | UnwindData |  |
| 11 | `WSHNotify` | `0x1930` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `WSHOpenSocket` | `0x1970` | 48 | UnwindData |  |
| 13 | `WSHOpenSocket2` | `0x19B0` | 771 | UnwindData |  |
| 14 | `WSHSetSocketInformation` | `0x1CC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `WSHStringToAddress` | `0x1CF0` | 139 | UnwindData |  |
