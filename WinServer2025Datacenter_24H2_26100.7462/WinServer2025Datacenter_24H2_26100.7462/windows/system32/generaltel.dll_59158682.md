# Binary Specification: generaltel.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\generaltel.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `59158682f6048bc694abdc212cfc794ae162d4c12f5ed956b05e4e2fbf6632c5`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `GetCITDataApr` | `0x1FCB0` | 22,448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DoCensusRun` | `0x25460` | 230 | UnwindData |  |
| 3 | `EnumerateOfficeAddins` | `0x258C0` | 26,368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `EnumerateOfficeDocuments` | `0x258C0` | 26,368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `RunInUserCxtW` | `0x2BFC0` | 986 | UnwindData |  |
| 6 | `GetCITTelemetryPoints` | `0x37530` | 1,095 | UnwindData |  |
| 1 | `CalculateCensusId` | `0x3C2F0` | 37,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `RunGeneralTelemetry` | `0x45690` | 1,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `RunGeneralTelemetryTCEx` | `0x45B40` | 61 | UnwindData |  |
| 10 | `SysprepCleanupEnableCustomTrigger` | `0x478F0` | 470 | UnwindData |  |
