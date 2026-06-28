# Binary Specification: diagnosticdataquery.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\diagnosticdataquery.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fbd56541fb14596b812609dd260025d6f9ea521b6315ebba5115f738bca9749f`
* **Total Exported Functions:** 37

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DdqCancelDiagnosticRecordOperation` | `0x9070` | 221 | UnwindData |  |
| 2 | `DdqCloseSession` | `0x9160` | 222 | UnwindData |  |
| 3 | `DdqCreateSession` | `0x9250` | 219 | UnwindData |  |
| 4 | `DdqExtractDiagnosticReport` | `0x9340` | 259 | UnwindData |  |
| 5 | `DdqFreeDiagnosticRecordLocaleTags` | `0x9450` | 146 | UnwindData |  |
| 6 | `DdqFreeDiagnosticRecordPage` | `0x94F0` | 214 | UnwindData |  |
| 7 | `DdqFreeDiagnosticRecordProducerCategories` | `0x95D0` | 117 | UnwindData |  |
| 8 | `DdqFreeDiagnosticRecordProducers` | `0x9650` | 116 | UnwindData |  |
| 9 | `DdqFreeDiagnosticReport` | `0x96D0` | 333 | UnwindData |  |
| 10 | `DdqGetDiagnosticDataAccessLevelAllowed` | `0x9830` | 192 | UnwindData |  |
| 11 | `DdqGetDiagnosticRecordAtIndex` | `0x9900` | 135 | UnwindData |  |
| 12 | `DdqGetDiagnosticRecordBinaryDistribution` | `0x9990` | 280 | UnwindData |  |
| 13 | `DdqGetDiagnosticRecordCategoryAtIndex` | `0x9AB0` | 73 | UnwindData |  |
| 14 | `DdqGetDiagnosticRecordCategoryCount` | `0x9B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `DdqGetDiagnosticRecordCount` | `0x9B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `DdqGetDiagnosticRecordLocaleTagCount` | `0x9B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `DdqGetDiagnosticRecordProducerCount` | `0x9B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `DdqGetDiagnosticReportCount` | `0x9B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `DdqGetDiagnosticRecordLocaleTagAtIndex` | `0x9B10` | 85 | UnwindData |  |
| 18 | `DdqGetDiagnosticRecordLocaleTags` | `0x9B70` | 299 | UnwindData |  |
| 19 | `DdqGetDiagnosticRecordPage` | `0x9CB0` | 340 | UnwindData |  |
| 20 | `DdqGetDiagnosticRecordPayload` | `0x9E10` | 252 | UnwindData |  |
| 21 | `DdqGetDiagnosticRecordProducerAtIndex` | `0x9F20` | 68 | UnwindData |  |
| 22 | `DdqGetDiagnosticRecordProducerCategories` | `0x9F70` | 299 | UnwindData |  |
| 24 | `DdqGetDiagnosticRecordProducers` | `0xA0B0` | 276 | UnwindData |  |
| 25 | `DdqGetDiagnosticRecordStats` | `0xA1D0` | 271 | UnwindData |  |
| 26 | `DdqGetDiagnosticRecordSummary` | `0xA2F0` | 259 | UnwindData |  |
| 27 | `DdqGetDiagnosticRecordTagDistribution` | `0xA400` | 271 | UnwindData |  |
| 28 | `DdqGetDiagnosticReport` | `0xA520` | 298 | UnwindData |  |
| 29 | `DdqGetDiagnosticReportAtIndex` | `0xA650` | 82 | UnwindData |  |
| 31 | `DdqGetDiagnosticReportStoreReportCount` | `0xA6B0` | 251 | UnwindData |  |
| 32 | `DdqGetSessionAccessLevel` | `0xA7C0` | 241 | UnwindData |  |
| 33 | `DdqGetTranscriptConfiguration` | `0xA8C0` | 237 | UnwindData |  |
| 34 | `DdqIsDiagnosticRecordSampledIn` | `0xA9C0` | 311 | UnwindData |  |
| 35 | `DdqSetTranscriptConfiguration` | `0xAB00` | 237 | UnwindData |  |
| 36 | `UtcSendTraceLogging` | `0xAC40` | 286 | UnwindData |  |
| 37 | `UtcSendTraceLogging2` | `0xAD70` | 290 | UnwindData |  |
