# Binary Specification: WMASF.DLL

## Binary Metadata
* **Original Path:** `C:\Windows\System32\WMASF.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d45de875ff827f00e5dedc9d47b0794758888697e9b9de2cae26c1cdc667be34`
* **Total Exported Functions:** 35

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 12 | `CreateAsfCellPoolAllocator` | `0x3770` | 116 | UnwindData |  |
| 21 | `ASFCreateBitrateTracker` | `0x3EF0` | 177,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `ASFCreateIOMonitor` | `0x3EF0` | 177,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `ASFGetDataUnitInfo` | `0x3EF0` | 177,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `ASFReadHeaderFromFile` | `0x3EF0` | 177,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `ASFSetDataUnitInfo` | `0x3EF0` | 177,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `ASFWriteHeaderToFile` | `0x3EF0` | 177,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `ASFAddPresDelta` | `0x2F5A0` | 68 | UnwindData |  |
| 16 | `ASFAddSendDelta` | `0x2F5F0` | 68 | UnwindData |  |
| 20 | `ASFCalculatePresDelta` | `0x2F640` | 220 | UnwindData |  |
| 27 | `ASFGetTimeBase` | `0x2F730` | 133 | UnwindData |  |
| 28 | `ASFPresDeltaTimeToTime` | `0x2F7C0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `ASFPresDeltaToFull` | `0x2F820` | 72 | UnwindData |  |
| 30 | `ASFPresFullToDelta` | `0x2F870` | 296 | UnwindData |  |
| 31 | `ASFPresTimeToSendTime` | `0x2F9A0` | 68 | UnwindData |  |
| 32 | `ASFPresTimeToTime` | `0x2F9F0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `ASFSendTimeToPresTime` | `0x2FA50` | 57 | UnwindData |  |
| 35 | `ASFSendTimeToTime` | `0x2FA90` | 107 | UnwindData |  |
| 37 | `ASFTimeToPresDeltaTime` | `0x2FB10` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `ASFTimeToPresTime` | `0x2FBE0` | 236 | UnwindData |  |
| 39 | `ASFTimeToSendTime` | `0x2FDA0` | 263 | UnwindData |  |
| 13 | `ASFCreateIndexMaker` | `0x31170` | 242 | UnwindData |  |
| 14 | `ASFCreateIndexMakerFileSink` | `0x317E0` | 122 | UnwindData |  |
| 5 | `ASFCreateLibrary` | `0x31860` | 141 | UnwindData |  |
| 9 | `ASFFindHeaderObject` | `0x31900` | 533 | UnwindData |  |
| 10 | `ASFFindRootObject` | `0x31B20` | 399 | UnwindData |  |
| 11 | `ASFFindStreamPropertiesObject` | `0x31CC0` | 740 | UnwindData |  |
| 6 | `ASFGetHeaderObject` | `0x31FB0` | 656 | UnwindData |  |
| 7 | `ASFGetRootObject` | `0x32250` | 490 | UnwindData |  |
| 8 | `ASFGetStreamPropertiesObject` | `0x32440` | 825 | UnwindData |  |
| 33 | `ASFReadHeaderFromFileHandle` | `0x32780` | 1,019 | UnwindData |  |
| 25 | `ASFCreateMediaObjectIndexMaker` | `0x33A60` | 232 | UnwindData |  |
| 26 | `ASFCreateStreamSelector` | `0x3C790` | 71 | UnwindData |  |
| 17 | `ASFGUIDFromCodecID` | `0x3CDC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `ASFGUIDToCodecID` | `0x3CDE0` | 7,500 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
