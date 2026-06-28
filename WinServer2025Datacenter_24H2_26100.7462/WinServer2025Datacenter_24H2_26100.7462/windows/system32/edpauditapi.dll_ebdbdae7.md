# Binary Specification: edpauditapi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\edpauditapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ebdbdae76b737eb17ce24c5b75ddfc48fbbcde2c909e2d88bff682d7e78f2623`
* **Total Exported Functions:** 13

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `EdpFlushTraces` | `0x42F0` | 9,808 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `EdpAuditHarden` | `0x6940` | 145 | UnwindData |  |
| 10 | `EdpAuditRead` | `0x6A20` | 100 | UnwindData |  |
| 11 | `EdpGetLogFullPathFromRelativePath` | `0x6A90` | 366 | UnwindData |  |
| 12 | `ReadAuditLogByCount` | `0x7A60` | 327 | UnwindData |  |
| 13 | `ReadAuditLogByTimeRange` | `0x7BB0` | 330 | UnwindData |  |
| 3 | `EdpAuditLogApplicationGenerated` | `0x13A90` | 235 | UnwindData |  |
| 4 | `EdpAuditLogApplicationLearning` | `0x13B90` | 341 | UnwindData |  |
| 5 | `EdpAuditLogDataCopied` | `0x13CF0` | 275 | UnwindData |  |
| 6 | `EdpAuditLogProtectionRemoved` | `0x13E10` | 227 | UnwindData |  |
| 7 | `EdpAuditLogSiteLearning` | `0x13F00` | 317 | UnwindData |  |
| 8 | `EdpAuditLoggerRegister` | `0x14050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `EdpAuditLoggerUnregister` | `0x14070` | 4,540 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
