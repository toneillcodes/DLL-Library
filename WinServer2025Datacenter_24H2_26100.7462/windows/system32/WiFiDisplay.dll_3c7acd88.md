# Binary Specification: WiFiDisplay.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\WiFiDisplay.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3c7acd8813fbf1475fca26eda379a4bbee4845b171c2c4d0ceca065afc8a0e39`
* **Total Exported Functions:** 22

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CreateInfraCastSourceConnector` | `0xB490` | 344 | UnwindData |  |
| 2 | `CloseMiracastSession` | `0xB5F0` | 257 | UnwindData |  |
| 3 | `CreateDAFProviderMiracastHelper` | `0xB700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `CreateWiFiDisplayEtwProvider` | `0xB710` | 192 | UnwindData |  |
| 5 | `IsMiracastSupportedByWlan` | `0xB7E0` | 69 | UnwindData |  |
| 6 | `MiracastFreeMemory` | `0xB830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `MiracastIeDecode` | `0xB840` | 102 | UnwindData |  |
| 8 | `MiracastIeEncode` | `0xB8B0` | 109 | UnwindData |  |
| 9 | `MiracastQueryParameters` | `0xB930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `MiracastRegisterDatarateCallback` | `0xB940` | 769 | UnwindData |  |
| 11 | `MiracastUnregisterDatarateCallback` | `0xBC50` | 308 | UnwindData |  |
| 12 | `OpenMiracastSession` | `0xBD90` | 605 | UnwindData |  |
| 13 | `VsIeProviderGetFunctionTable` | `0xC000` | 296 | UnwindData |  |
| 14 | `WFDDisplaySinkCloseSession` | `0xC130` | 275 | UnwindData |  |
| 15 | `WFDDisplaySinkDeInit` | `0xC250` | 217 | UnwindData |  |
| 16 | `WFDDisplaySinkInit` | `0xC330` | 271 | UnwindData |  |
| 17 | `WFDDisplaySinkQueryCapabilities` | `0xC450` | 405 | UnwindData |  |
| 18 | `WFDDisplaySinkSetPersistedGroupIDList` | `0xC5F0` | 347 | UnwindData |  |
| 19 | `WFDDisplaySinkSetProperty` | `0xC760` | 358 | UnwindData |  |
| 20 | `WFDDisplaySinkStart` | `0xC8D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `WFDDisplaySinkStartEx` | `0xC8E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `WFDDisplaySinkStop` | `0xC8F0` | 259,820 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
