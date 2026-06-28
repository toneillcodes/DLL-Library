# Binary Specification: edpauditapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\edpauditapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `28a0fd93d9786a5ceb1cca9aac9a9ff0f86ac80e1a2e1c0b24b9b6a256ad7b99`
* **Total Exported Functions:** 13

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `EdpFlushTraces` | `0x42F0` | 9,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `EdpAuditHarden` | `0x6960` | 145 | UnwindData |  |
| 10 | `EdpAuditRead` | `0x6A40` | 100 | UnwindData |  |
| 11 | `EdpGetLogFullPathFromRelativePath` | `0x6AB0` | 366 | UnwindData |  |
| 12 | `ReadAuditLogByCount` | `0x7A80` | 327 | UnwindData |  |
| 13 | `ReadAuditLogByTimeRange` | `0x7BD0` | 330 | UnwindData |  |
| 3 | `EdpAuditLogApplicationGenerated` | `0x13AB0` | 235 | UnwindData |  |
| 4 | `EdpAuditLogApplicationLearning` | `0x13BB0` | 341 | UnwindData |  |
| 5 | `EdpAuditLogDataCopied` | `0x13D10` | 275 | UnwindData |  |
| 6 | `EdpAuditLogProtectionRemoved` | `0x13E30` | 227 | UnwindData |  |
| 7 | `EdpAuditLogSiteLearning` | `0x13F20` | 317 | UnwindData |  |
| 8 | `EdpAuditLoggerRegister` | `0x14070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `EdpAuditLoggerUnregister` | `0x14090` | 4,540 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
