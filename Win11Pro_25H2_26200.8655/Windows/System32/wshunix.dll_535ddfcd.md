# Binary Specification: wshunix.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wshunix.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `535ddfcd2f030413e164e675933464dd727bf5a69e39b4667c6db5dedcbc579c`
* **Total Exported Functions:** 16

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `WSHAddressToString` | `0x15F0` | 75 | UnwindData |  |
| 2 | `WSHEnumProtocols` | `0x1650` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `WSHGetBroadcastSockaddr` | `0x16F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `WSHIoctl` | `0x16F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `WSHGetProviderGuid` | `0x1700` | 74 | UnwindData |  |
| 5 | `WSHGetSockaddrType` | `0x1750` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `WSHGetSocketInformation` | `0x1780` | 479 | UnwindData |  |
| 7 | `WSHGetWSAProtocolInfo` | `0x1970` | 98 | UnwindData |  |
| 8 | `WSHGetWildcardSockaddr` | `0x19E0` | 49 | UnwindData |  |
| 9 | `WSHGetWinsockMapping` | `0x1A20` | 55 | UnwindData |  |
| 11 | `WSHJoinLeaf` | `0x1A60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `WSHNotify` | `0x1A80` | 265 | UnwindData |  |
| 13 | `WSHOpenSocket` | `0x1B90` | 48 | UnwindData |  |
| 14 | `WSHOpenSocket2` | `0x1BD0` | 176 | UnwindData |  |
| 15 | `WSHSetSocketInformation` | `0x1C90` | 991 | UnwindData |  |
| 16 | `WSHStringToAddress` | `0x2080` | 91 | UnwindData |  |
