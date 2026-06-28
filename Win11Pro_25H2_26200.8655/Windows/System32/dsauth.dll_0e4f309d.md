# Binary Specification: dsauth.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\dsauth.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0e4f309d9f9ff24199426da02f82031c915b3761292aaf9154b2933ac3d58691`
* **Total Exported Functions:** 24

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 14 | `StoreBeginSearch` | `0x36D0` | 111 | UnwindData |  |
| 15 | `StoreCleanupHandle` | `0x3750` | 127 | UnwindData |  |
| 16 | `StoreCollectAttributes` | `0x37E0` | 479 | UnwindData |  |
| 17 | `StoreCreateObjectVA` | `0x3BB0` | 616 | UnwindData |  |
| 18 | `StoreDeleteObject` | `0x3E20` | 64 | UnwindData |  |
| 19 | `StoreEndSearch` | `0x40B0` | 86 | UnwindData |  |
| 20 | `StoreGetHandle` | `0x4110` | 390 | UnwindData |  |
| 21 | `StoreInitHandle` | `0x42A0` | 789 | UnwindData |  |
| 22 | `StoreSearchGetNext` | `0x45C0` | 327 | UnwindData |  |
| 23 | `StoreSetSearchOneLevel` | `0x4710` | 175 | UnwindData |  |
| 24 | `StoreSetSearchSubTree` | `0x47D0` | 180 | UnwindData |  |
| 7 | `DhcpDsGetAttribs` | `0x4C40` | 912 | UnwindData |  |
| 8 | `DhcpDsGetLists` | `0x4FE0` | 487 | UnwindData |  |
| 9 | `DhcpDsGetRoot` | `0x51D0` | 602 | UnwindData |  |
| 11 | `DhcpDsSetLists` | `0x5430` | 4,819 | UnwindData |  |
| 3 | `DhcpDsAddServer` | `0x6850` | 1,713 | UnwindData |  |
| 5 | `DhcpDsDelServer` | `0x6F10` | 1,965 | UnwindData |  |
| 6 | `DhcpDsEnumServers` | `0x76D0` | 815 | UnwindData |  |
| 1 | `DhcpAddServerDS` | `0x8070` | 1,751 | UnwindData |  |
| 2 | `DhcpDeleteServerDS` | `0x8750` | 137 | UnwindData |  |
| 4 | `DhcpDsCleanupDS` | `0x87E0` | 101 | UnwindData |  |
| 10 | `DhcpDsInitDS` | `0x8850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `DhcpEnumServersDS` | `0x8860` | 933 | UnwindData |  |
| 12 | `DhcpDsValidateService` | `0x8D90` | 895 | UnwindData |  |
