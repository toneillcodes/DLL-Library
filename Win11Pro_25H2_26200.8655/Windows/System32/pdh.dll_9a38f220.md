# Binary Specification: pdh.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\pdh.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9a38f22048c3e1a81880ca899b4e9f1623a120eb3f4613df7f26c1f2859b8f23`
* **Total Exported Functions:** 119

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 38 | `PdhExpandCounterPathW` | `0x1300` | 31 | UnwindData |  |
| 42 | `PdhExpandWildCardPathW` | `0x1330` | 337 | UnwindData |  |
| 57 | `PdhGetDefaultPerfObjectW` | `0x16A0` | 186 | UnwindData |  |
| 36 | `PdhEnumObjectsW` | `0x1760` | 327 | UnwindData |  |
| 79 | `PdhOpenQueryA` | `0x18B0` | 176 | UnwindData |  |
| 32 | `PdhEnumObjectItemsW` | `0x1970` | 451 | UnwindData |  |
| 31 | `PdhEnumObjectItemsHW` | `0x1B40` | 546 | UnwindData |  |
| 53 | `PdhGetDefaultPerfCounterW` | `0x2C20` | 112 | UnwindData |  |
| 78 | `PdhOpenQuery` | `0x2D90` | 503 | UnwindData |  |
| 81 | `PdhOpenQueryW` | `0x2D90` | 503 | UnwindData |  |
| 35 | `PdhEnumObjectsHW` | `0x3520` | 230 | UnwindData |  |
| 75 | `PdhMakeCounterPathW` | `0x36E0` | 55 | UnwindData |  |
| 20 | `PdhConnectMachineW` | `0x6EA0` | 132 | UnwindData |  |
| 66 | `PdhGetRawCounterArrayA` | `0x6F30` | 159 | UnwindData |  |
| 72 | `PdhLookupPerfNameByIndexA` | `0x7060` | 429 | UnwindData |  |
| 60 | `PdhGetFormattedCounterArrayA` | `0x87E0` | 167 | UnwindData |  |
| 73 | `PdhLookupPerfNameByIndexW` | `0x8890` | 392 | UnwindData |  |
| 67 | `PdhGetRawCounterArrayW` | `0x8A40` | 157 | UnwindData |  |
| 61 | `PdhGetFormattedCounterArrayW` | `0x92B0` | 169 | UnwindData |  |
| 45 | `PdhGetCounterInfoW` | `0x9490` | 60 | UnwindData |  |
| 62 | `PdhGetFormattedCounterValue` | `0xAD40` | 122 | UnwindData |  |
| 68 | `PdhGetRawCounterValue` | `0xCD80` | 266 | UnwindData |  |
| 15 | `PdhCollectQueryData` | `0xCE90` | 78 | UnwindData |  |
| 43 | `PdhFormatFromRawValue` | `0xD7E0` | 196 | UnwindData |  |
| 12 | `PdhCalculateCounterFromRawValue` | `0xEBF0` | 286 | UnwindData |  |
| 101 | `PdhUpdateLogW` | `0xF910` | 389 | UnwindData |  |
| 98 | `PdhTranslateLocaleCounterW` | `0x10790` | 91 | UnwindData |  |
| 97 | `PdhTranslate009CounterW` | `0x10800` | 97 | UnwindData |  |
| 41 | `PdhExpandWildCardPathHW` | `0x112C0` | 121 | UnwindData |  |
| 29 | `PdhEnumObjectItemsA` | `0x11340` | 440 | UnwindData |  |
| 30 | `PdhEnumObjectItemsHA` | `0x11500` | 675 | UnwindData |  |
| 39 | `PdhExpandWildCardPathA` | `0x117B0` | 308 | UnwindData |  |
| 40 | `PdhExpandWildCardPathHA` | `0x11960` | 223 | UnwindData |  |
| 1 | `PdhAddCounterA` | `0x11A50` | 231 | UnwindData |  |
| 88 | `PdhRemoveCounter` | `0x16830` | 235 | UnwindData |  |
| 13 | `PdhCloseLog` | `0x16B50` | 308 | UnwindData |  |
| 14 | `PdhCloseQuery` | `0x174C0` | 165 | UnwindData |  |
| 46 | `PdhGetCounterTimeBase` | `0x17950` | 180 | UnwindData |  |
| 16 | `PdhCollectQueryDataEx` | `0x17AC0` | 485 | UnwindData |  |
| 74 | `PdhMakeCounterPathA` | `0x17FF0` | 1,021 | UnwindData |  |
| 105 | `PdhValidatePathW` | `0x18C70` | 1,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `PdhComputeCounterStatistics` | `0x19190` | 292 | UnwindData |  |
| 103 | `PdhValidatePathExA` | `0x199B0` | 146 | UnwindData |  |
| 17 | `PdhCollectQueryDataWithTime` | `0x19C90` | 89 | UnwindData |  |
| 7 | `PdhBindInputDataSourceW` | `0x1A470` | 410 | UnwindData |  |
| 102 | `PdhValidatePathA` | `0x1ABF0` | 12,304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `PdhAddCounterW` | `0x1DC00` | 75 | UnwindData |  |
| 3 | `PdhAddEnglishCounterA` | `0x1DD30` | 236 | UnwindData |  |
| 4 | `PdhAddEnglishCounterW` | `0x1DE30` | 242 | UnwindData |  |
| 83 | `PdhParseCounterPathW` | `0x203E0` | 51 | UnwindData |  |
| 84 | `PdhParseInstanceNameA` | `0x207F0` | 486 | UnwindData |  |
| 104 | `PdhValidatePathExW` | `0x209E0` | 2,660 | UnwindData |  |
| 44 | `PdhGetCounterInfoA` | `0x23B90` | 61 | UnwindData |  |
| 92 | `PdhSetCounterScaleFactor` | `0x23BE0` | 80 | UnwindData |  |
| 70 | `PdhLookupPerfIndexByNameA` | `0x2BCB0` | 345 | UnwindData |  |
| 71 | `PdhLookupPerfIndexByNameW` | `0x2BE10` | 277 | UnwindData |  |
| 58 | `PdhGetDllVersion` | `0x2C090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `PdhIsRealTimeQuery` | `0x2C0B0` | 79 | UnwindData |  |
| 80 | `PdhOpenQueryH` | `0x2C110` | 358 | UnwindData |  |
| 94 | `PdhSetDefaultRealTimeDataSource` | `0x2C280` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `PdhSetQueryTimeRange` | `0x2C2C0` | 141 | UnwindData |  |
| 106 | `PdhVbAddCounter` | `0x2E400` | 81 | UnwindData |  |
| 107 | `PdhVbCreateCounterPathList` | `0x2E460` | 497 | UnwindData |  |
| 108 | `PdhVbGetCounterPathElements` | `0x2E660` | 492 | UnwindData |  |
| 109 | `PdhVbGetCounterPathFromList` | `0x2E860` | 413 | UnwindData |  |
| 110 | `PdhVbGetDoubleCounterValue` | `0x2EA10` | 73 | UnwindData |  |
| 111 | `PdhVbGetLogFileSize` | `0x2EA60` | 79 | UnwindData |  |
| 112 | `PdhVbGetOneCounterPath` | `0x2EAC0` | 231 | UnwindData |  |
| 113 | `PdhVbIsGoodStatus` | `0x2EBB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `PdhVbOpenLog` | `0x2EBE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `PdhVbOpenQuery` | `0x2EBF0` | 69 | UnwindData |  |
| 116 | `PdhVbUpdateLog` | `0x2EC40` | 6,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `PdhBindInputDataSourceA` | `0x305B0` | 325 | UnwindData |  |
| 47 | `PdhGetDataSourceTimeRangeA` | `0x30700` | 250 | UnwindData |  |
| 48 | `PdhGetDataSourceTimeRangeH` | `0x30800` | 317 | UnwindData |  |
| 49 | `PdhGetDataSourceTimeRangeW` | `0x30950` | 214 | UnwindData |  |
| 63 | `PdhGetLogFileSize` | `0x30A30` | 95 | UnwindData |  |
| 64 | `PdhGetLogFileTypeW` | `0x30AA0` | 258 | UnwindData |  |
| 65 | `PdhGetLogSetGUID` | `0x30BB0` | 150 | UnwindData |  |
| 76 | `PdhOpenLogA` | `0x30C50` | 331 | UnwindData |  |
| 77 | `PdhOpenLogW` | `0x30DB0` | 766 | UnwindData |  |
| 86 | `PdhReadRawLogRecord` | `0x310C0` | 166 | UnwindData |  |
| 95 | `PdhSetLogSetRunID` | `0x31170` | 79 | UnwindData |  |
| 99 | `PdhUpdateLogA` | `0x311D0` | 139 | UnwindData |  |
| 100 | `PdhUpdateLogFileCatalog` | `0x31270` | 85 | UnwindData |  |
| 21 | `PdhCreateSQLTablesA` | `0x3A6B0` | 98 | UnwindData |  |
| 22 | `PdhCreateSQLTablesW` | `0x3A720` | 60 | UnwindData |  |
| 23 | `PdhEnumLogSetNamesA` | `0x3A770` | 150 | UnwindData |  |
| 24 | `PdhEnumLogSetNamesW` | `0x3A810` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `PdhVerifySQLDBA` | `0x3A870` | 98 | UnwindData |  |
| 118 | `PdhVerifySQLDBW` | `0x3A8E0` | 60 | UnwindData |  |
| 5 | `PdhAddRelogCounter` | `0x42040` | 343 | UnwindData |  |
| 87 | `PdhRelogW` | `0x421A0` | 975 | UnwindData |  |
| 89 | `PdhResetRelogCounterValues` | `0x42580` | 219 | UnwindData |  |
| 93 | `PdhSetCounterValue` | `0x42670` | 568 | UnwindData |  |
| 119 | `PdhWriteRelogSample` | `0x428B0` | 305 | UnwindData |  |
| 19 | `PdhConnectMachineA` | `0x42E80` | 178 | UnwindData |  |
| 25 | `PdhEnumMachinesA` | `0x42F40` | 231 | UnwindData |  |
| 26 | `PdhEnumMachinesHA` | `0x43030` | 143 | UnwindData |  |
| 27 | `PdhEnumMachinesHW` | `0x430D0` | 154 | UnwindData |  |
| 28 | `PdhEnumMachinesW` | `0x43170` | 250 | UnwindData |  |
| 33 | `PdhEnumObjectsA` | `0x43270` | 277 | UnwindData |  |
| 34 | `PdhEnumObjectsHA` | `0x43390` | 329 | UnwindData |  |
| 50 | `PdhGetDefaultPerfCounterA` | `0x434E0` | 110 | UnwindData |  |
| 51 | `PdhGetDefaultPerfCounterHA` | `0x43560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `PdhGetDefaultPerfCounterHW` | `0x43580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `PdhGetDefaultPerfObjectA` | `0x435A0` | 100 | UnwindData |  |
| 55 | `PdhGetDefaultPerfObjectHA` | `0x43610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `PdhGetDefaultPerfObjectHW` | `0x43630` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `PdhGetExplainText` | `0x43670` | 110 | UnwindData |  |
| 82 | `PdhParseCounterPathA` | `0x436F0` | 876 | UnwindData |  |
| 85 | `PdhParseInstanceNameW` | `0x43A70` | 517 | UnwindData |  |
| 8 | `PdhBrowseCountersA` | `0x43D20` | 70 | UnwindData |  |
| 9 | `PdhBrowseCountersHA` | `0x43D70` | 70 | UnwindData |  |
| 10 | `PdhBrowseCountersHW` | `0x43DC0` | 70 | UnwindData |  |
| 11 | `PdhBrowseCountersW` | `0x43E10` | 70 | UnwindData |  |
| 90 | `PdhSelectDataSourceA` | `0x43E60` | 112 | UnwindData |  |
| 91 | `PdhSelectDataSourceW` | `0x43EE0` | 112 | UnwindData |  |
| 37 | `PdhExpandCounterPathA` | `0x43F60` | 31 | UnwindData |  |
