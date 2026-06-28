# Binary Specification: pla.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\pla.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f454ea072faba2277aa99b59c32bfb89c07228fe949b3f2bcc0f014626061472`
* **Total Exported Functions:** 15

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 12 | `PlaGetServerCapabilities` | `0x313A0` | 36 | UnwindData |  |
| 4 | `DllGetClassObject` | `0x33470` | 50 | UnwindData |  |
| 3 | `DllCanUnloadNow` | `0x43E80` | 91,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllRegisterServer` | `0x5A220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllUnregisterServer` | `0x5A220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `PlaServer` | `0x5A230` | 1,240 | UnwindData |  |
| 1 | `ServiceMain` | `0x5AB90` | 1,185 | UnwindData |  |
| 2 | `SvchostPushServiceGlobals` | `0x5B040` | 10,896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `PlaUpgrade` | `0x5DAD0` | 1,076 | UnwindData |  |
| 10 | `PlaGetLegacyAlertActionsFlagsFromString` | `0xFE430` | 1,371 | UnwindData |  |
| 11 | `PlaGetLegacyAlertActionsStringFromFlags` | `0xFE9A0` | 1,377 | UnwindData |  |
| 8 | `PlaExpandTaskArguments` | `0x121D20` | 515 | UnwindData |  |
| 13 | `PlaHost` | `0x122E70` | 638 | UnwindData |  |
| 7 | `PlaDeleteReport` | `0x140DE0` | 322 | UnwindData |  |
| 9 | `PlaExtractCabinet` | `0x140F30` | 35,436 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
