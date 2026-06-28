# Binary Specification: ntlanman.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ntlanman.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `88c47e29cfc525a7f539cdd32c56a7c9e54f636802c83302bfd40580052e8078`
* **Total Exported Functions:** 27

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 38 | `NPAddConnection3` | `0x1770` | 737 | UnwindData |  |
| 49 | `NPGetConnectionPerformance` | `0x1AC0` | 55 | UnwindData |  |
| 55 | `NPAddConnection4` | `0x1B00` | 93 | UnwindData |  |
| 52 | `NPGetResourceInformation` | `0x1D60` | 91 | UnwindData |  |
| 34 | `NPEnumResource` | `0x54A0` | 59 | UnwindData |  |
| 33 | `NPOpenEnum` | `0x5A90` | 38 | UnwindData |  |
| 12 | `NPGetConnection` | `0x75F0` | 1,480 | UnwindData |  |
| 54 | `NPGetConnection3` | `0x8010` | 57 | UnwindData |  |
| 36 | `NPFormatNetworkName` | `0x8840` | 190 | UnwindData |  |
| 13 | `NPGetCaps` | `0x8E30` | 1,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `DllMain` | `0x9240` | 170 | UnwindData |  |
| 35 | `NPCloseEnum` | `0x9850` | 129 | UnwindData |  |
| 57 | `NPCancelConnection2` | `0xA820` | 69 | UnwindData |  |
| 40 | `NPGetUniversalName` | `0xB1A0` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `RegisterAppInstanceVersion` | `0xB330` | 181 | UnwindData |  |
| 41 | `NPGetResourceParent` | `0xB580` | 10,960 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `NPAddConnection` | `0xE050` | 31 | UnwindData |  |
| 18 | `NPCancelConnection` | `0xE080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `NPGetPersistentUseOptionsForConnection` | `0xE090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `NPGetPersistentUseOptionsForConnection2` | `0xE0A0` | 127 | UnwindData |  |
| 53 | `NPGetReconnectFlags` | `0xE130` | 30 | UnwindData |  |
| 16 | `NPGetUser` | `0xE160` | 96 | UnwindData |  |
| 15 | `I_SystemFocusDialog` | `0xE1D0` | 301 | UnwindData |  |
| 19 | `QueryAppInstanceVersion` | `0xE360` | 228 | UnwindData |  |
| 20 | `RegisterAppInstance` | `0xE450` | 186 | UnwindData |  |
| 22 | `ResetAllAppInstanceVersions` | `0xE510` | 98 | UnwindData |  |
| 23 | `SetAppInstanceCsvFlags` | `0xE580` | 123 | UnwindData |  |
