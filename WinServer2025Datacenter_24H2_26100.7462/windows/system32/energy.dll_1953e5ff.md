# Binary Specification: energy.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\energy.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1953e5ff8b25c7aa0a536aaef8a0a67a931ba0e1d98559083922fb895bd123a6`
* **Total Exported Functions:** 18

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 16 | `SendScreenOnTelemetry` | `0x260C0` | 509 | UnwindData |  |
| 14 | `SaveSleepStudyReport` | `0x3EB90` | 1,533 | UnwindData |  |
| 2 | `SaveBatteryReport` | `0x4BD70` | 473 | UnwindData |  |
| 17 | `TransformBatteryReport` | `0x4BF50` | 92 | UnwindData |  |
| 4 | `EnergyWizard_Analyze` | `0x5B510` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `EnergyWizard_CancelTrace` | `0x5B530` | 114 | UnwindData |  |
| 6 | `EnergyWizard_CollectTrace` | `0x5B5B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `EnergyWizard_CreateEnergyWizard` | `0x5B5D0` | 35 | UnwindData |  |
| 8 | `EnergyWizard_DefaultTraceDuration` | `0x5B600` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `EnergyWizard_DestroyEnergyWizard` | `0x5B630` | 38 | UnwindData |  |
| 10 | `EnergyWizard_GetLogEntryCounts` | `0x5B660` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `EnergyWizard_SaveReport` | `0x5B6C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `EnergyWizard_SqmAnalysis` | `0x5B6E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `EnergyWizard_TransformReport` | `0x5B700` | 104 | UnwindData |  |
| 18 | `TransformSleepStudyReport` | `0x72DE0` | 116 | UnwindData |  |
| 3 | `TransformSystemSleepDiagnosticsReport` | `0x88470` | 92 | UnwindData |  |
| 15 | `SaveSystemSleepDiagnosticsReport` | `0x888C0` | 650 | UnwindData |  |
| 1 | `CreateProvisioningXml` | `0x8E110` | 122 | UnwindData |  |
