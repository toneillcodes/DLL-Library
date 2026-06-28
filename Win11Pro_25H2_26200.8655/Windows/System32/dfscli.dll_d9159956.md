# Binary Specification: dfscli.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\dfscli.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d91599565f3c6685903b53b72739cffb15ec1503df8010c0a7e2d755c1f9a8a8`
* **Total Exported Functions:** 29

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `I_NetDfsIsThisADomainName` | `0x64F0` | 55 | UnwindData |  |
| 2 | `NetDfsAdd` | `0x66E0` | 212 | UnwindData |  |
| 3 | `NetDfsAddFtRoot` | `0x67C0` | 484 | UnwindData |  |
| 4 | `NetDfsAddRootTarget` | `0x69B0` | 1,191 | UnwindData |  |
| 5 | `NetDfsAddStdRoot` | `0x6E60` | 119 | UnwindData |  |
| 6 | `NetDfsAddStdRootForced` | `0x6EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `NetDfsGetDcAddress` | `0x6EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `NetDfsManagerGetConfigInfo` | `0x6EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `NetDfsManagerInitialize` | `0x6EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `NetDfsManagerSendSiteInfo` | `0x6EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `NetDfsRename` | `0x6EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `NetDfsEnum` | `0x6EF0` | 661 | UnwindData |  |
| 8 | `NetDfsGetClientInfo` | `0x7190` | 1,324 | UnwindData |  |
| 10 | `NetDfsGetFtContainerSecurity` | `0x76D0` | 135 | UnwindData |  |
| 11 | `NetDfsGetInfo` | `0x7760` | 279 | UnwindData |  |
| 12 | `NetDfsGetSecurity` | `0x7880` | 312 | UnwindData |  |
| 13 | `NetDfsGetStdContainerSecurity` | `0x79C0` | 140 | UnwindData |  |
| 14 | `NetDfsGetSupportedNamespaceVersion` | `0x7A60` | 598 | UnwindData |  |
| 18 | `NetDfsMove` | `0x7CC0` | 665 | UnwindData |  |
| 19 | `NetDfsRemove` | `0x7F60` | 209 | UnwindData |  |
| 20 | `NetDfsRemoveFtRoot` | `0x8040` | 490 | UnwindData |  |
| 21 | `NetDfsRemoveFtRootForced` | `0x8230` | 556 | UnwindData |  |
| 22 | `NetDfsRemoveRootTarget` | `0x8470` | 1,243 | UnwindData |  |
| 23 | `NetDfsRemoveStdRoot` | `0x8960` | 97 | UnwindData |  |
| 25 | `NetDfsSetClientInfo` | `0x89D0` | 823 | UnwindData |  |
| 26 | `NetDfsSetFtContainerSecurity` | `0x8D10` | 117 | UnwindData |  |
| 27 | `NetDfsSetInfo` | `0x8D90` | 1,116 | UnwindData |  |
| 28 | `NetDfsSetSecurity` | `0x9200` | 299 | UnwindData |  |
| 29 | `NetDfsSetStdContainerSecurity` | `0x9340` | 122 | UnwindData |  |
