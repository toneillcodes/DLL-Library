# Binary Specification: diagnosticdataquery.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\diagnosticdataquery.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `51d1dea3c84d59cab9e6176e140d3eb48f838e432d1f28708077c2e684521692`
* **Total Exported Functions:** 37

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DdqCancelDiagnosticRecordOperation` | `0x9060` | 221 | UnwindData |  |
| 2 | `DdqCloseSession` | `0x9150` | 222 | UnwindData |  |
| 3 | `DdqCreateSession` | `0x9240` | 219 | UnwindData |  |
| 4 | `DdqExtractDiagnosticReport` | `0x9330` | 259 | UnwindData |  |
| 5 | `DdqFreeDiagnosticRecordLocaleTags` | `0x9440` | 146 | UnwindData |  |
| 6 | `DdqFreeDiagnosticRecordPage` | `0x94E0` | 214 | UnwindData |  |
| 7 | `DdqFreeDiagnosticRecordProducerCategories` | `0x95C0` | 117 | UnwindData |  |
| 8 | `DdqFreeDiagnosticRecordProducers` | `0x9640` | 116 | UnwindData |  |
| 9 | `DdqFreeDiagnosticReport` | `0x96C0` | 333 | UnwindData |  |
| 10 | `DdqGetDiagnosticDataAccessLevelAllowed` | `0x9820` | 192 | UnwindData |  |
| 11 | `DdqGetDiagnosticRecordAtIndex` | `0x98F0` | 135 | UnwindData |  |
| 12 | `DdqGetDiagnosticRecordBinaryDistribution` | `0x9980` | 280 | UnwindData |  |
| 13 | `DdqGetDiagnosticRecordCategoryAtIndex` | `0x9AA0` | 73 | UnwindData |  |
| 14 | `DdqGetDiagnosticRecordCategoryCount` | `0x9AF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `DdqGetDiagnosticRecordCount` | `0x9AF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `DdqGetDiagnosticRecordLocaleTagCount` | `0x9AF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `DdqGetDiagnosticRecordProducerCount` | `0x9AF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `DdqGetDiagnosticReportCount` | `0x9AF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `DdqGetDiagnosticRecordLocaleTagAtIndex` | `0x9B00` | 85 | UnwindData |  |
| 18 | `DdqGetDiagnosticRecordLocaleTags` | `0x9B60` | 299 | UnwindData |  |
| 19 | `DdqGetDiagnosticRecordPage` | `0x9CA0` | 340 | UnwindData |  |
| 20 | `DdqGetDiagnosticRecordPayload` | `0x9E00` | 252 | UnwindData |  |
| 21 | `DdqGetDiagnosticRecordProducerAtIndex` | `0x9F10` | 68 | UnwindData |  |
| 22 | `DdqGetDiagnosticRecordProducerCategories` | `0x9F60` | 299 | UnwindData |  |
| 24 | `DdqGetDiagnosticRecordProducers` | `0xA0A0` | 276 | UnwindData |  |
| 25 | `DdqGetDiagnosticRecordStats` | `0xA1C0` | 271 | UnwindData |  |
| 26 | `DdqGetDiagnosticRecordSummary` | `0xA2E0` | 259 | UnwindData |  |
| 27 | `DdqGetDiagnosticRecordTagDistribution` | `0xA3F0` | 271 | UnwindData |  |
| 28 | `DdqGetDiagnosticReport` | `0xA510` | 298 | UnwindData |  |
| 29 | `DdqGetDiagnosticReportAtIndex` | `0xA640` | 82 | UnwindData |  |
| 31 | `DdqGetDiagnosticReportStoreReportCount` | `0xA6A0` | 251 | UnwindData |  |
| 32 | `DdqGetSessionAccessLevel` | `0xA7B0` | 241 | UnwindData |  |
| 33 | `DdqGetTranscriptConfiguration` | `0xA8B0` | 237 | UnwindData |  |
| 34 | `DdqIsDiagnosticRecordSampledIn` | `0xA9B0` | 311 | UnwindData |  |
| 35 | `DdqSetTranscriptConfiguration` | `0xAAF0` | 237 | UnwindData |  |
| 36 | `UtcSendTraceLogging` | `0xAC30` | 286 | UnwindData |  |
| 37 | `UtcSendTraceLogging2` | `0xAD60` | 290 | UnwindData |  |
