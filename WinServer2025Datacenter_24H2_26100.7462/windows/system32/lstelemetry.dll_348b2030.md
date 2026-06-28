# Binary Specification: lstelemetry.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\lstelemetry.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `348b2030c1161e6e7f90e3e20e6f359d76a00c1107ad505b6b7d3fb35c882f6c`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `GetLicensingTelemetryCommonData` | `0x2B20` | 68 | UnwindData |  |
| 2 | `InitRDLSTelemetryCommonData` | `0x2B70` | 836 | UnwindData |  |
| 3 | `LogRDLSSettingsTelemetryData` | `0x2EC0` | 376 | UnwindData |  |
| 4 | `LogTSLSTelemetryEvent` | `0x3590` | 235 | UnwindData |  |
| 5 | `LogTSLSTelemetryRDSEvent` | `0x3BD0` | 34 | UnwindData |  |
| 6 | `RegisterAndEnableLicensingTelemetry` | `0x3EB0` | 183 | UnwindData |  |
| 7 | `UnregisterLicensingTelemetry` | `0x3F70` | 53 | UnwindData |  |
| 8 | `UpdateRDLSTelemetryCommonData` | `0x3FB0` | 0 | Indeterminate |  |
