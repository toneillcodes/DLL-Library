# Binary Specification: iri.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\iri.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f393e922e30845ab33dbc31d3b4e3637bc96c06fe5c861c639b82b73d684bbd5`
* **Total Exported Functions:** 19

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 18 | `IriAppendRelativeIri` | `0x2820` | 173 | UnwindData |  |
| 17 | `IriAppendSegment` | `0x28E0` | 517 | UnwindData |  |
| 2 | `IriClose` | `0x2AF0` | 51 | UnwindData |  |
| 13 | `IriCompare` | `0x2B30` | 340 | UnwindData |  |
| 5 | `IriCopy` | `0x2C90` | 264 | UnwindData |  |
| 1 | `IriCreateFromString` | `0x2DA0` | 211 | UnwindData |  |
| 14 | `IriFindLastCommonSegment` | `0x2E80` | 369 | UnwindData |  |
| 7 | `IriGetAsString` | `0x3000` | 477 | UnwindData |  |
| 10 | `IriGetAttributeFlags` | `0x31F0` | 85 | UnwindData |  |
| 11 | `IriGetComponent` | `0x3250` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `IriGetRelative` | `0x32A0` | 261 | UnwindData |  |
| 12 | `IriGetSegment` | `0x33B0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `IriGetSegmentCount` | `0x3400` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `IriMakeConstantEx` | `0x3450` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `IriMutableClose` | `0x3490` | 51 | UnwindData |  |
| 16 | `IriSetComponent` | `0x34D0` | 524 | UnwindData |  |
| 19 | `IriSetMetadata` | `0x36F0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `IriSplit` | `0x3760` | 386 | UnwindData |  |
| 6 | `IriSplitIntoMutableIris` | `0x38F0` | 394 | UnwindData |  |
