# Binary Specification: ntlanman.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ntlanman.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `312c4ebc47427b307d7b28bf19151736e774a96714abf33e3475a09ba6f93f85`
* **Total Exported Functions:** 27

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 57 | `NPCancelConnection2` | `0x1190` | 69 | UnwindData |  |
| 34 | `NPEnumResource` | `0x20E0` | 59 | UnwindData |  |
| 33 | `NPOpenEnum` | `0x26D0` | 38 | UnwindData |  |
| 12 | `NPGetConnection` | `0x4230` | 1,480 | UnwindData |  |
| 54 | `NPGetConnection3` | `0x4C90` | 57 | UnwindData |  |
| 38 | `NPAddConnection3` | `0x5840` | 737 | UnwindData |  |
| 49 | `NPGetConnectionPerformance` | `0x5B90` | 55 | UnwindData |  |
| 55 | `NPAddConnection4` | `0x5BD0` | 93 | UnwindData |  |
| 52 | `NPGetResourceInformation` | `0x5E30` | 91 | UnwindData |  |
| 36 | `NPFormatNetworkName` | `0x7D20` | 190 | UnwindData |  |
| 13 | `NPGetCaps` | `0x8380` | 1,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `DllMain` | `0x8790` | 170 | UnwindData |  |
| 35 | `NPCloseEnum` | `0x92B0` | 129 | UnwindData |  |
| 40 | `NPGetUniversalName` | `0xAA80` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `RegisterAppInstanceVersion` | `0xAC10` | 181 | UnwindData |  |
| 41 | `NPGetResourceParent` | `0xAE60` | 12,688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `NPAddConnection` | `0xDFF0` | 31 | UnwindData |  |
| 18 | `NPCancelConnection` | `0xE020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `NPGetPersistentUseOptionsForConnection` | `0xE030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `NPGetPersistentUseOptionsForConnection2` | `0xE040` | 127 | UnwindData |  |
| 53 | `NPGetReconnectFlags` | `0xE0D0` | 30 | UnwindData |  |
| 16 | `NPGetUser` | `0xE100` | 96 | UnwindData |  |
| 15 | `I_SystemFocusDialog` | `0xE170` | 301 | UnwindData |  |
| 19 | `QueryAppInstanceVersion` | `0xE300` | 228 | UnwindData |  |
| 20 | `RegisterAppInstance` | `0xE3F0` | 186 | UnwindData |  |
| 22 | `ResetAllAppInstanceVersions` | `0xE4B0` | 98 | UnwindData |  |
| 23 | `SetAppInstanceCsvFlags` | `0xE520` | 123 | UnwindData |  |
