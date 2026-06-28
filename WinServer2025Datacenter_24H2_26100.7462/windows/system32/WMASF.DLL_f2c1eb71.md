# Binary Specification: WMASF.DLL

## Binary Metadata
* **Original Path:** `c:\windows\system32\WMASF.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f2c1eb71da8ba4e19780782cf8283d94697719427d3152a9a0c5d8df68952a75`
* **Total Exported Functions:** 35

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 12 | `CreateAsfCellPoolAllocator` | `0x2F10` | 116 | UnwindData |  |
| 21 | `ASFCreateBitrateTracker` | `0x3690` | 177,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `ASFCreateIOMonitor` | `0x3690` | 177,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `ASFGetDataUnitInfo` | `0x3690` | 177,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `ASFReadHeaderFromFile` | `0x3690` | 177,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `ASFSetDataUnitInfo` | `0x3690` | 177,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `ASFWriteHeaderToFile` | `0x3690` | 177,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `ASFAddPresDelta` | `0x2EA20` | 68 | UnwindData |  |
| 16 | `ASFAddSendDelta` | `0x2EA70` | 68 | UnwindData |  |
| 20 | `ASFCalculatePresDelta` | `0x2EAC0` | 220 | UnwindData |  |
| 27 | `ASFGetTimeBase` | `0x2EBB0` | 133 | UnwindData |  |
| 28 | `ASFPresDeltaTimeToTime` | `0x2EC40` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `ASFPresDeltaToFull` | `0x2ECA0` | 72 | UnwindData |  |
| 30 | `ASFPresFullToDelta` | `0x2ECF0` | 296 | UnwindData |  |
| 31 | `ASFPresTimeToSendTime` | `0x2EE20` | 68 | UnwindData |  |
| 32 | `ASFPresTimeToTime` | `0x2EE70` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `ASFSendTimeToPresTime` | `0x2EED0` | 57 | UnwindData |  |
| 35 | `ASFSendTimeToTime` | `0x2EF10` | 107 | UnwindData |  |
| 37 | `ASFTimeToPresDeltaTime` | `0x2EF90` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `ASFTimeToPresTime` | `0x2F060` | 236 | UnwindData |  |
| 39 | `ASFTimeToSendTime` | `0x2F220` | 263 | UnwindData |  |
| 13 | `ASFCreateIndexMaker` | `0x305F0` | 242 | UnwindData |  |
| 14 | `ASFCreateIndexMakerFileSink` | `0x30C60` | 122 | UnwindData |  |
| 5 | `ASFCreateLibrary` | `0x30CE0` | 141 | UnwindData |  |
| 9 | `ASFFindHeaderObject` | `0x30D80` | 533 | UnwindData |  |
| 10 | `ASFFindRootObject` | `0x30FA0` | 399 | UnwindData |  |
| 11 | `ASFFindStreamPropertiesObject` | `0x31140` | 740 | UnwindData |  |
| 6 | `ASFGetHeaderObject` | `0x31430` | 656 | UnwindData |  |
| 7 | `ASFGetRootObject` | `0x316D0` | 490 | UnwindData |  |
| 8 | `ASFGetStreamPropertiesObject` | `0x318C0` | 825 | UnwindData |  |
| 33 | `ASFReadHeaderFromFileHandle` | `0x31C00` | 1,019 | UnwindData |  |
| 25 | `ASFCreateMediaObjectIndexMaker` | `0x32EE0` | 232 | UnwindData |  |
| 26 | `ASFCreateStreamSelector` | `0x37F40` | 71 | UnwindData |  |
| 17 | `ASFGUIDFromCodecID` | `0x37F90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `ASFGUIDToCodecID` | `0x37FB0` | 8,016 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
