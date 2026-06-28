# Binary Specification: pdh.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\pdh.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `00633dad3b3cbb0e0c032455b490a0200ed18bfd9225b6c8ef9e1bc552a63678`
* **Total Exported Functions:** 119

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 38 | `PdhExpandCounterPathW` | `0x12A0` | 31 | UnwindData |  |
| 42 | `PdhExpandWildCardPathW` | `0x12D0` | 337 | UnwindData |  |
| 57 | `PdhGetDefaultPerfObjectW` | `0x1640` | 186 | UnwindData |  |
| 36 | `PdhEnumObjectsW` | `0x1700` | 327 | UnwindData |  |
| 79 | `PdhOpenQueryA` | `0x1850` | 176 | UnwindData |  |
| 32 | `PdhEnumObjectItemsW` | `0x1910` | 451 | UnwindData |  |
| 31 | `PdhEnumObjectItemsHW` | `0x1AE0` | 546 | UnwindData |  |
| 53 | `PdhGetDefaultPerfCounterW` | `0x2BC0` | 112 | UnwindData |  |
| 78 | `PdhOpenQuery` | `0x2D30` | 503 | UnwindData |  |
| 81 | `PdhOpenQueryW` | `0x2D30` | 503 | UnwindData |  |
| 35 | `PdhEnumObjectsHW` | `0x34C0` | 230 | UnwindData |  |
| 75 | `PdhMakeCounterPathW` | `0x3680` | 196 | UnwindData |  |
| 20 | `PdhConnectMachineW` | `0x6FB0` | 132 | UnwindData |  |
| 66 | `PdhGetRawCounterArrayA` | `0x7040` | 159 | UnwindData |  |
| 72 | `PdhLookupPerfNameByIndexA` | `0x7170` | 429 | UnwindData |  |
| 60 | `PdhGetFormattedCounterArrayA` | `0x88F0` | 167 | UnwindData |  |
| 73 | `PdhLookupPerfNameByIndexW` | `0x89A0` | 392 | UnwindData |  |
| 67 | `PdhGetRawCounterArrayW` | `0x8B50` | 157 | UnwindData |  |
| 61 | `PdhGetFormattedCounterArrayW` | `0x93C0` | 169 | UnwindData |  |
| 45 | `PdhGetCounterInfoW` | `0x95A0` | 60 | UnwindData |  |
| 62 | `PdhGetFormattedCounterValue` | `0xAE50` | 122 | UnwindData |  |
| 68 | `PdhGetRawCounterValue` | `0xCE90` | 266 | UnwindData |  |
| 15 | `PdhCollectQueryData` | `0xCFA0` | 78 | UnwindData |  |
| 43 | `PdhFormatFromRawValue` | `0xD8F0` | 196 | UnwindData |  |
| 12 | `PdhCalculateCounterFromRawValue` | `0xED00` | 286 | UnwindData |  |
| 101 | `PdhUpdateLogW` | `0xFA20` | 389 | UnwindData |  |
| 98 | `PdhTranslateLocaleCounterW` | `0x108A0` | 91 | UnwindData |  |
| 97 | `PdhTranslate009CounterW` | `0x10910` | 97 | UnwindData |  |
| 41 | `PdhExpandWildCardPathHW` | `0x113D0` | 121 | UnwindData |  |
| 29 | `PdhEnumObjectItemsA` | `0x11450` | 440 | UnwindData |  |
| 30 | `PdhEnumObjectItemsHA` | `0x11610` | 675 | UnwindData |  |
| 39 | `PdhExpandWildCardPathA` | `0x118C0` | 308 | UnwindData |  |
| 40 | `PdhExpandWildCardPathHA` | `0x11A70` | 223 | UnwindData |  |
| 1 | `PdhAddCounterA` | `0x11B60` | 231 | UnwindData |  |
| 88 | `PdhRemoveCounter` | `0x16A00` | 235 | UnwindData |  |
| 13 | `PdhCloseLog` | `0x16D20` | 308 | UnwindData |  |
| 14 | `PdhCloseQuery` | `0x17690` | 165 | UnwindData |  |
| 46 | `PdhGetCounterTimeBase` | `0x17B20` | 180 | UnwindData |  |
| 16 | `PdhCollectQueryDataEx` | `0x17C90` | 485 | UnwindData |  |
| 74 | `PdhMakeCounterPathA` | `0x181C0` | 1,021 | UnwindData |  |
| 105 | `PdhValidatePathW` | `0x18E40` | 1,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `PdhComputeCounterStatistics` | `0x19360` | 292 | UnwindData |  |
| 103 | `PdhValidatePathExA` | `0x19B80` | 146 | UnwindData |  |
| 17 | `PdhCollectQueryDataWithTime` | `0x19E60` | 89 | UnwindData |  |
| 7 | `PdhBindInputDataSourceW` | `0x1A640` | 410 | UnwindData |  |
| 102 | `PdhValidatePathA` | `0x1ADC0` | 7,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `PdhAddCounterW` | `0x1CCB0` | 75 | UnwindData |  |
| 3 | `PdhAddEnglishCounterA` | `0x1CDE0` | 236 | UnwindData |  |
| 4 | `PdhAddEnglishCounterW` | `0x1CEE0` | 242 | UnwindData |  |
| 83 | `PdhParseCounterPathW` | `0x1F490` | 51 | UnwindData |  |
| 84 | `PdhParseInstanceNameA` | `0x1F8A0` | 486 | UnwindData |  |
| 104 | `PdhValidatePathExW` | `0x1FA90` | 2,660 | UnwindData |  |
| 44 | `PdhGetCounterInfoA` | `0x22C40` | 61 | UnwindData |  |
| 92 | `PdhSetCounterScaleFactor` | `0x22C90` | 80 | UnwindData |  |
| 70 | `PdhLookupPerfIndexByNameA` | `0x23E30` | 345 | UnwindData |  |
| 71 | `PdhLookupPerfIndexByNameW` | `0x23F90` | 277 | UnwindData |  |
| 58 | `PdhGetDllVersion` | `0x24210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `PdhIsRealTimeQuery` | `0x24230` | 79 | UnwindData |  |
| 80 | `PdhOpenQueryH` | `0x24290` | 358 | UnwindData |  |
| 94 | `PdhSetDefaultRealTimeDataSource` | `0x24400` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `PdhSetQueryTimeRange` | `0x24440` | 141 | UnwindData |  |
| 106 | `PdhVbAddCounter` | `0x2BE30` | 81 | UnwindData |  |
| 107 | `PdhVbCreateCounterPathList` | `0x2BE90` | 497 | UnwindData |  |
| 108 | `PdhVbGetCounterPathElements` | `0x2C090` | 492 | UnwindData |  |
| 109 | `PdhVbGetCounterPathFromList` | `0x2C290` | 413 | UnwindData |  |
| 110 | `PdhVbGetDoubleCounterValue` | `0x2C440` | 73 | UnwindData |  |
| 111 | `PdhVbGetLogFileSize` | `0x2C490` | 79 | UnwindData |  |
| 112 | `PdhVbGetOneCounterPath` | `0x2C4F0` | 231 | UnwindData |  |
| 113 | `PdhVbIsGoodStatus` | `0x2C5E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `PdhVbOpenLog` | `0x2C610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `PdhVbOpenQuery` | `0x2C620` | 69 | UnwindData |  |
| 116 | `PdhVbUpdateLog` | `0x2C670` | 6,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `PdhBindInputDataSourceA` | `0x2DFE0` | 325 | UnwindData |  |
| 47 | `PdhGetDataSourceTimeRangeA` | `0x2E130` | 250 | UnwindData |  |
| 48 | `PdhGetDataSourceTimeRangeH` | `0x2E230` | 317 | UnwindData |  |
| 49 | `PdhGetDataSourceTimeRangeW` | `0x2E380` | 214 | UnwindData |  |
| 63 | `PdhGetLogFileSize` | `0x2E460` | 95 | UnwindData |  |
| 64 | `PdhGetLogFileTypeW` | `0x2E4D0` | 258 | UnwindData |  |
| 65 | `PdhGetLogSetGUID` | `0x2E5E0` | 150 | UnwindData |  |
| 76 | `PdhOpenLogA` | `0x2E680` | 331 | UnwindData |  |
| 77 | `PdhOpenLogW` | `0x2E7E0` | 766 | UnwindData |  |
| 86 | `PdhReadRawLogRecord` | `0x2EAF0` | 166 | UnwindData |  |
| 95 | `PdhSetLogSetRunID` | `0x2EBA0` | 79 | UnwindData |  |
| 99 | `PdhUpdateLogA` | `0x2EC00` | 139 | UnwindData |  |
| 100 | `PdhUpdateLogFileCatalog` | `0x2ECA0` | 85 | UnwindData |  |
| 21 | `PdhCreateSQLTablesA` | `0x380E0` | 98 | UnwindData |  |
| 22 | `PdhCreateSQLTablesW` | `0x38150` | 60 | UnwindData |  |
| 23 | `PdhEnumLogSetNamesA` | `0x381A0` | 150 | UnwindData |  |
| 24 | `PdhEnumLogSetNamesW` | `0x38240` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `PdhVerifySQLDBA` | `0x382A0` | 98 | UnwindData |  |
| 118 | `PdhVerifySQLDBW` | `0x38310` | 60 | UnwindData |  |
| 5 | `PdhAddRelogCounter` | `0x3FA70` | 343 | UnwindData |  |
| 87 | `PdhRelogW` | `0x3FBD0` | 975 | UnwindData |  |
| 89 | `PdhResetRelogCounterValues` | `0x3FFB0` | 219 | UnwindData |  |
| 93 | `PdhSetCounterValue` | `0x400A0` | 568 | UnwindData |  |
| 119 | `PdhWriteRelogSample` | `0x402E0` | 305 | UnwindData |  |
| 19 | `PdhConnectMachineA` | `0x408B0` | 178 | UnwindData |  |
| 25 | `PdhEnumMachinesA` | `0x40970` | 231 | UnwindData |  |
| 26 | `PdhEnumMachinesHA` | `0x40A60` | 143 | UnwindData |  |
| 27 | `PdhEnumMachinesHW` | `0x40B00` | 154 | UnwindData |  |
| 28 | `PdhEnumMachinesW` | `0x40BA0` | 250 | UnwindData |  |
| 33 | `PdhEnumObjectsA` | `0x40CA0` | 277 | UnwindData |  |
| 34 | `PdhEnumObjectsHA` | `0x40DC0` | 329 | UnwindData |  |
| 50 | `PdhGetDefaultPerfCounterA` | `0x40F10` | 110 | UnwindData |  |
| 51 | `PdhGetDefaultPerfCounterHA` | `0x40F90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `PdhGetDefaultPerfCounterHW` | `0x40FB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `PdhGetDefaultPerfObjectA` | `0x40FD0` | 100 | UnwindData |  |
| 55 | `PdhGetDefaultPerfObjectHA` | `0x41040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `PdhGetDefaultPerfObjectHW` | `0x41060` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `PdhGetExplainText` | `0x410A0` | 110 | UnwindData |  |
| 82 | `PdhParseCounterPathA` | `0x41120` | 876 | UnwindData |  |
| 85 | `PdhParseInstanceNameW` | `0x414A0` | 517 | UnwindData |  |
| 8 | `PdhBrowseCountersA` | `0x41750` | 70 | UnwindData |  |
| 9 | `PdhBrowseCountersHA` | `0x417A0` | 70 | UnwindData |  |
| 10 | `PdhBrowseCountersHW` | `0x417F0` | 70 | UnwindData |  |
| 11 | `PdhBrowseCountersW` | `0x41840` | 70 | UnwindData |  |
| 90 | `PdhSelectDataSourceA` | `0x41890` | 112 | UnwindData |  |
| 91 | `PdhSelectDataSourceW` | `0x41910` | 112 | UnwindData |  |
| 37 | `PdhExpandCounterPathA` | `0x41990` | 31 | UnwindData |  |
