# Binary Specification: appraiser.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\appraiser.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2552b094a8815fdf9725416c2e00f2451f49a996d9c4d440a5fe57ab678a11b4`
* **Total Exported Functions:** 13

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 10 | `Sgd` | `0x13420` | 4,704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `UpdateCacheCompatStatuses` | `0x13420` | 4,704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DoProcessRestoreApps` | `0x14680` | 61 | UnwindData |  |
| 2 | `DoScheduledTelemetryRun` | `0x146D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DoScheduledTelemetryRunTC` | `0x146E0` | 177 | UnwindData |  |
| 4 | `GetCtacProvider` | `0x147A0` | 238 | UnwindData |  |
| 5 | `GetProvider` | `0x148A0` | 47 | UnwindData |  |
| 6 | `GetTargetVersionList` | `0x148E0` | 481 | UnwindData |  |
| 7 | `ProcessRestoreApps` | `0x15450` | 287 | UnwindData |  |
| 8 | `RunTest` | `0x15580` | 287 | UnwindData |  |
| 9 | `RunXml` | `0x156B0` | 58 | UnwindData |  |
| 11 | `UpdateAvStatus` | `0x15A30` | 630 | UnwindData |  |
| 13 | `UpdateExperienceIndicators` | `0x15CB0` | 2,204,371 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
