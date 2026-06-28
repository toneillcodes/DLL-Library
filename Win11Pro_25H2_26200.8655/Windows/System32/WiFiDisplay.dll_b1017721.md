# Binary Specification: WiFiDisplay.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\WiFiDisplay.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b1017721e276f26ff32ff4e980073376700abb512f291ef783b2a1b20b2a3c38`
* **Total Exported Functions:** 22

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CreateInfraCastSourceConnector` | `0xB560` | 344 | UnwindData |  |
| 2 | `CloseMiracastSession` | `0xB6C0` | 257 | UnwindData |  |
| 3 | `CreateDAFProviderMiracastHelper` | `0xB7D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `CreateWiFiDisplayEtwProvider` | `0xB7E0` | 192 | UnwindData |  |
| 5 | `IsMiracastSupportedByWlan` | `0xB8B0` | 69 | UnwindData |  |
| 6 | `MiracastFreeMemory` | `0xB900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `MiracastIeDecode` | `0xB910` | 102 | UnwindData |  |
| 8 | `MiracastIeEncode` | `0xB980` | 109 | UnwindData |  |
| 9 | `MiracastQueryParameters` | `0xBA00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `MiracastRegisterDatarateCallback` | `0xBA10` | 769 | UnwindData |  |
| 11 | `MiracastUnregisterDatarateCallback` | `0xBD20` | 308 | UnwindData |  |
| 12 | `OpenMiracastSession` | `0xBE60` | 605 | UnwindData |  |
| 13 | `VsIeProviderGetFunctionTable` | `0xC0D0` | 296 | UnwindData |  |
| 14 | `WFDDisplaySinkCloseSession` | `0xC200` | 275 | UnwindData |  |
| 15 | `WFDDisplaySinkDeInit` | `0xC320` | 217 | UnwindData |  |
| 16 | `WFDDisplaySinkInit` | `0xC400` | 271 | UnwindData |  |
| 17 | `WFDDisplaySinkQueryCapabilities` | `0xC520` | 405 | UnwindData |  |
| 18 | `WFDDisplaySinkSetPersistedGroupIDList` | `0xC6C0` | 347 | UnwindData |  |
| 19 | `WFDDisplaySinkSetProperty` | `0xC830` | 358 | UnwindData |  |
| 20 | `WFDDisplaySinkStart` | `0xC9A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `WFDDisplaySinkStartEx` | `0xC9B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `WFDDisplaySinkStop` | `0xC9C0` | 261,388 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
