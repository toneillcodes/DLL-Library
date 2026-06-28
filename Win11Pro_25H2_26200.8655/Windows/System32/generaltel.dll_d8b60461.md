# Binary Specification: generaltel.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\generaltel.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d8b60461a6cf7cee1aa49777c606b85a2f08209b23b8ea4e973296132d9d1b0c`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `GetCITDataApr` | `0x163C0` | 25,776 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DoCensusRun` | `0x1C870` | 230 | UnwindData |  |
| 3 | `EnumerateOfficeAddins` | `0x1CD80` | 30,592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `EnumerateOfficeDocuments` | `0x1CD80` | 30,592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `RunInUserCxtW` | `0x24500` | 757 | UnwindData |  |
| 6 | `GetCITTelemetryPoints` | `0x2F050` | 1,095 | UnwindData |  |
| 1 | `CalculateCensusId` | `0x32E00` | 28,880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `RunGeneralTelemetry` | `0x39ED0` | 944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `RunGeneralTelemetryTCEx` | `0x3A280` | 61 | UnwindData |  |
| 10 | `SysprepCleanupEnableCustomTrigger` | `0x3B5F0` | 470 | UnwindData |  |
