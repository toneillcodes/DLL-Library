# Binary Specification: appraiser.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\appraiser.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9be8a843d3c6c79ba1e62a6940155cd36992447b73845cf7b93686832f4a1ba6`
* **Total Exported Functions:** 13

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 10 | `Sgd` | `0x178B0` | 5,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `UpdateCacheCompatStatuses` | `0x178B0` | 5,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DoProcessRestoreApps` | `0x18F50` | 61 | UnwindData |  |
| 2 | `DoScheduledTelemetryRun` | `0x18FA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DoScheduledTelemetryRunTC` | `0x18FB0` | 177 | UnwindData |  |
| 4 | `GetCtacProvider` | `0x1A2A0` | 238 | UnwindData |  |
| 5 | `GetProvider` | `0x1AFE0` | 47 | UnwindData |  |
| 6 | `GetTargetVersionList` | `0x1B020` | 481 | UnwindData |  |
| 7 | `ProcessRestoreApps` | `0x1BD60` | 549 | UnwindData |  |
| 8 | `RunTest` | `0x1BF90` | 287 | UnwindData |  |
| 9 | `RunXml` | `0x1C0C0` | 58 | UnwindData |  |
| 11 | `UpdateAvStatus` | `0x1C440` | 763 | UnwindData |  |
| 13 | `UpdateExperienceIndicators` | `0x1C750` | 2,419,171 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
