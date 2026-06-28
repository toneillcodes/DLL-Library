# Binary Specification: FXSTIFF.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\FXSTIFF.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b4fea5dcd8d48d2706e68471c74df43226524260916f329f0e5f27f937c41326`
* **Total Exported Functions:** 42

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `ConvertTiffFileToValidFaxFormat` | `0x4590` | 1,941 | UnwindData |  |
| 5 | `FXSTIFFInitialize` | `0x4F90` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `FreeMsTagInfo` | `0x4FF0` | 477 | UnwindData |  |
| 8 | `GetMsTagDwordLong` | `0x51E0` | 58 | UnwindData |  |
| 9 | `GetMsTagFileTime` | `0x51E0` | 58 | UnwindData |  |
| 10 | `GetMsTagString` | `0x5220` | 98 | UnwindData |  |
| 11 | `GetW2kMsTiffTags` | `0x5510` | 1,087 | UnwindData |  |
| 12 | `MemoryMapTiffFile` | `0x5A00` | 868 | UnwindData |  |
| 13 | `MergeTiffFiles` | `0x5D70` | 703 | UnwindData |  |
| 14 | `MmrAddBranding` | `0x6040` | 2,061 | UnwindData |  |
| 15 | `PrintTiffFile` | `0x6860` | 988 | UnwindData |  |
| 18 | `TiffAddMsTags` | `0x6D40` | 4,995 | UnwindData |  |
| 19 | `TiffClose` | `0x80D0` | 146 | UnwindData |  |
| 20 | `TiffCreate` | `0x8170` | 807 | UnwindData |  |
| 21 | `TiffEncodeLinesMmrCompression` | `0x84A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `TiffEndPage` | `0x84B0` | 458 | UnwindData |  |
| 23 | `TiffEndPageForInMemoryConversion` | `0x8680` | 127 | UnwindData |  |
| 24 | `TiffExtractFirstPage` | `0x8710` | 196 | UnwindData |  |
| 25 | `TiffGetCurrentPageData` | `0x87E0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `TiffGetIFDData` | `0x8830` | 54 | UnwindData |  |
| 27 | `TiffGetIFDSize` | `0x8870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `TiffLimitTagNumber` | `0x8890` | 1,005 | UnwindData |  |
| 29 | `TiffOpen` | `0x8C90` | 1,324 | UnwindData |  |
| 33 | `TiffRead` | `0x9500` | 236 | UnwindData |  |
| 34 | `TiffRecoverGoodPages` | `0x9600` | 303 | UnwindData |  |
| 35 | `TiffSeekToPage` | `0x9740` | 2,113 | UnwindData |  |
| 36 | `TiffSetCurrentPageParams` | `0x9F90` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `TiffSetNextIFDOffset` | `0x9FF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `TiffStartPage` | `0xA010` | 91 | UnwindData |  |
| 39 | `TiffStartPageForInMemoryConversion` | `0xA080` | 366 | UnwindData |  |
| 42 | `TiffWriteRaw` | `0xA200` | 87 | UnwindData |  |
| 1 | `ConvMmrPageHiResToMrLoRes` | `0xACF0` | 34 | UnwindData |  |
| 2 | `ConvMmrPageToMh` | `0xAD20` | 40 | UnwindData |  |
| 3 | `ConvMmrPageToMrSameRes` | `0xAD50` | 39 | UnwindData |  |
| 6 | `FindNextEol` | `0xAD80` | 336 | UnwindData |  |
| 16 | `ScanMhSegment` | `0xCFB0` | 1,104 | UnwindData |  |
| 17 | `ScanMrSegment` | `0xD410` | 2,174 | UnwindData |  |
| 30 | `TiffPostProcessFast` | `0xDCA0` | 178 | UnwindData |  |
| 40 | `TiffUncompressMmrPage` | `0xDD60` | 248 | UnwindData |  |
| 41 | `TiffUncompressMmrPageRaw` | `0xDE60` | 1,078 | UnwindData |  |
| 31 | `TiffPrint` | `0xEEA0` | 242 | UnwindData |  |
| 32 | `TiffPrintDC` | `0xEFA0` | 691 | UnwindData |  |
