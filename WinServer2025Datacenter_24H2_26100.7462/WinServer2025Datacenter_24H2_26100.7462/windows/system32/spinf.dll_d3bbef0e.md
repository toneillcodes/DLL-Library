# Binary Specification: spinf.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\spinf.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d3bbef0e043bad3b4b6db84adcba79663cdf3365be181154a17333236dbf857c`
* **Total Exported Functions:** 48

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 20 | `SpInfGetLineByIndex` | `0x1AC0` | 379 | UnwindData |  |
| 45 | `SpInfSetDirectoryId` | `0x1C50` | 966 | UnwindData |  |
| 30 | `SpInfGetStringField` | `0x2170` | 202 | UnwindData |  |
| 7 | `SpInfFindNextMatchLine` | `0x2370` | 476 | UnwindData |  |
| 36 | `SpInfLineFromContext` | `0x2560` | 107 | UnwindData |  |
| 21 | `SpInfGetLineCount` | `0x2770` | 300 | UnwindData |  |
| 9 | `SpInfFreeInfFile` | `0x2960` | 153 | UnwindData |  |
| 6 | `SpInfFindFirstLine` | `0x2A00` | 387 | UnwindData |  |
| 40 | `SpInfLocateSection` | `0x2EA0` | 421 | UnwindData |  |
| 39 | `SpInfLocateLine` | `0x3260` | 485 | UnwindData |  |
| 2 | `SpInfDoesInfContainString` | `0x6260` | 314 | UnwindData |  |
| 8 | `SpInfFindValueInSectionList` | `0x65C0` | 558 | UnwindData |  |
| 38 | `SpInfLoadInfFile` | `0x7130` | 2,717 | UnwindData |  |
| 14 | `SpInfGetIndirectString` | `0x7D50` | 143 | UnwindData |  |
| 35 | `SpInfIsIndirectString` | `0x8750` | 32 | UnwindData |  |
| 1 | `SpInfDetermineInfStyle` | `0x8E80` | 258 | UnwindData |  |
| 31 | `SpInfGetStringsSection` | `0xC560` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `SpInfLockInf` | `0xC720` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `SpInfGetInfStyle` | `0xC7D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `SpInfGetLineFieldCount` | `0xC7E0` | 100 | UnwindData |  |
| 47 | `SpInfUnlockInf` | `0xC850` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `SpInfGetOriginalInfName` | `0xC990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `SpInfGetInfLineNumber` | `0xC9A0` | 5,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `SpInfGetNextInf` | `0xDE90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `SpInfGetField` | `0xDEA0` | 656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `SpInfGetPrevInf` | `0xE130` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `SpInfGetLanguageId` | `0xE250` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `SpInfGetVersionNode` | `0xE460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `SpInfGetVersionDatum` | `0xE470` | 149 | UnwindData |  |
| 3 | `SpInfEnumInfSections` | `0x10350` | 341 | UnwindData |  |
| 17 | `SpInfGetInfSections` | `0x104B0` | 546 | UnwindData |  |
| 24 | `SpInfGetLineTextWithKey` | `0x106E0` | 589 | UnwindData |  |
| 4 | `SpInfFileFullPathFromLineContext` | `0x10940` | 245 | UnwindData |  |
| 5 | `SpInfFilenameFromHandle` | `0x10A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `SpInfSectionNameFromLineContext` | `0x10A50` | 284 | UnwindData |  |
| 46 | `SpInfSourcePathFromHandle` | `0x10B80` | 271 | UnwindData |  |
| 22 | `SpInfGetLineCountFromSection` | `0x10CA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `SpInfLineIsSearchable` | `0x10CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `SpInfGetBestInstallSection` | `0x10CC0` | 696 | UnwindData |  |
| 11 | `SpInfGetBestModelsSection` | `0x10F80` | 1,904 | UnwindData |  |
| 12 | `SpInfGetDriverVer` | `0x117C0` | 393 | UnwindData |  |
| 15 | `SpInfGetInfInformation` | `0x119A0` | 594 | UnwindData |  |
| 25 | `SpInfGetLogToken` | `0x11C00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `SpInfQueryInfFileInformation` | `0x11C10` | 324 | UnwindData |  |
| 43 | `SpInfQueryInfVersionInformation` | `0x11D60` | 347 | UnwindData |  |
| 48 | `SpInfVersionNodeFromInfInformation` | `0x11ED0` | 342 | UnwindData |  |
| 28 | `SpInfGetPathFromDirId` | `0x12680` | 329 | UnwindData |  |
| 32 | `SpInfGetTargetPath` | `0x127D0` | 1,372 | UnwindData |  |
