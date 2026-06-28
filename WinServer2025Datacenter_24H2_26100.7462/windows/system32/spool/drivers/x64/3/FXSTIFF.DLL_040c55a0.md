# Binary Specification: FXSTIFF.DLL

## Binary Metadata
* **Original Path:** `c:\windows\system32\spool\drivers\x64\3\FXSTIFF.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `040c55a0134acccae24093b06759350dba2acc6a17c5e3ace315a6c4627cf603`
* **Total Exported Functions:** 42

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `ConvertTiffFileToValidFaxFormat` | `0x4530` | 1,941 | UnwindData |  |
| 5 | `FXSTIFFInitialize` | `0x4F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `FreeMsTagInfo` | `0x4F40` | 477 | UnwindData |  |
| 8 | `GetMsTagDwordLong` | `0x5130` | 58 | UnwindData |  |
| 9 | `GetMsTagFileTime` | `0x5130` | 58 | UnwindData |  |
| 10 | `GetMsTagString` | `0x5170` | 98 | UnwindData |  |
| 11 | `GetW2kMsTiffTags` | `0x5460` | 1,087 | UnwindData |  |
| 12 | `MemoryMapTiffFile` | `0x5950` | 868 | UnwindData |  |
| 13 | `MergeTiffFiles` | `0x5CC0` | 703 | UnwindData |  |
| 14 | `MmrAddBranding` | `0x5F90` | 2,061 | UnwindData |  |
| 15 | `PrintTiffFile` | `0x67B0` | 988 | UnwindData |  |
| 18 | `TiffAddMsTags` | `0x6C90` | 4,995 | UnwindData |  |
| 19 | `TiffClose` | `0x8020` | 146 | UnwindData |  |
| 20 | `TiffCreate` | `0x80C0` | 807 | UnwindData |  |
| 21 | `TiffEncodeLinesMmrCompression` | `0x83F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `TiffEndPage` | `0x8400` | 458 | UnwindData |  |
| 23 | `TiffEndPageForInMemoryConversion` | `0x85D0` | 127 | UnwindData |  |
| 24 | `TiffExtractFirstPage` | `0x8660` | 196 | UnwindData |  |
| 25 | `TiffGetCurrentPageData` | `0x8730` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `TiffGetIFDData` | `0x8780` | 54 | UnwindData |  |
| 27 | `TiffGetIFDSize` | `0x87C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `TiffLimitTagNumber` | `0x87E0` | 1,005 | UnwindData |  |
| 29 | `TiffOpen` | `0x8BE0` | 1,324 | UnwindData |  |
| 33 | `TiffRead` | `0x9450` | 236 | UnwindData |  |
| 34 | `TiffRecoverGoodPages` | `0x9550` | 303 | UnwindData |  |
| 35 | `TiffSeekToPage` | `0x9690` | 1,811 | UnwindData |  |
| 36 | `TiffSetCurrentPageParams` | `0x9DB0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `TiffSetNextIFDOffset` | `0x9E10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `TiffStartPage` | `0x9E30` | 91 | UnwindData |  |
| 39 | `TiffStartPageForInMemoryConversion` | `0x9EA0` | 366 | UnwindData |  |
| 42 | `TiffWriteRaw` | `0xA020` | 87 | UnwindData |  |
| 1 | `ConvMmrPageHiResToMrLoRes` | `0xAB10` | 34 | UnwindData |  |
| 2 | `ConvMmrPageToMh` | `0xAB40` | 40 | UnwindData |  |
| 3 | `ConvMmrPageToMrSameRes` | `0xAB70` | 39 | UnwindData |  |
| 6 | `FindNextEol` | `0xABA0` | 336 | UnwindData |  |
| 16 | `ScanMhSegment` | `0xCDD0` | 1,104 | UnwindData |  |
| 17 | `ScanMrSegment` | `0xD230` | 2,174 | UnwindData |  |
| 30 | `TiffPostProcessFast` | `0xDAC0` | 178 | UnwindData |  |
| 40 | `TiffUncompressMmrPage` | `0xDB80` | 248 | UnwindData |  |
| 41 | `TiffUncompressMmrPageRaw` | `0xDC80` | 1,078 | UnwindData |  |
| 31 | `TiffPrint` | `0xECC0` | 242 | UnwindData |  |
| 32 | `TiffPrintDC` | `0xEDC0` | 691 | UnwindData |  |
