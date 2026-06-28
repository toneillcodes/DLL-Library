# Binary Specification: energy.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\energy.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d38508dd44e36d38b94afaa19acdb6f8b844abed51193b9ccec439c38a829baa`
* **Total Exported Functions:** 18

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 16 | `SendScreenOnTelemetry` | `0x23CB0` | 509 | UnwindData |  |
| 14 | `SaveSleepStudyReport` | `0x3E180` | 1,533 | UnwindData |  |
| 2 | `SaveBatteryReport` | `0x4BFE0` | 473 | UnwindData |  |
| 17 | `TransformBatteryReport` | `0x4C1C0` | 92 | UnwindData |  |
| 4 | `EnergyWizard_Analyze` | `0x5C700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `EnergyWizard_CancelTrace` | `0x5C720` | 114 | UnwindData |  |
| 6 | `EnergyWizard_CollectTrace` | `0x5C7A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `EnergyWizard_CreateEnergyWizard` | `0x5C7C0` | 35 | UnwindData |  |
| 8 | `EnergyWizard_DefaultTraceDuration` | `0x5C7F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `EnergyWizard_DestroyEnergyWizard` | `0x5C820` | 38 | UnwindData |  |
| 10 | `EnergyWizard_GetLogEntryCounts` | `0x5C850` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `EnergyWizard_SaveReport` | `0x5C8B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `EnergyWizard_SqmAnalysis` | `0x5C8D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `EnergyWizard_TransformReport` | `0x5C8F0` | 104 | UnwindData |  |
| 18 | `TransformSleepStudyReport` | `0x79D70` | 116 | UnwindData |  |
| 3 | `TransformSystemSleepDiagnosticsReport` | `0x93250` | 92 | UnwindData |  |
| 15 | `SaveSystemSleepDiagnosticsReport` | `0x936A0` | 650 | UnwindData |  |
| 1 | `CreateProvisioningXml` | `0x98EF0` | 122 | UnwindData |  |
