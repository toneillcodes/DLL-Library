# Binary Specification: NvTelemetry64.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\nvlt.inf_amd64_18cae871934f9f98\NvTelemetry64.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `180f95eba56f146b8707b1d518fe1cb68dfb52d826fa710d1c1f7808841ffe72`
* **Total Exported Functions:** 15

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `NvPluginGetInfo` | `0x5EBA0` | 25,424 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `InitializeTelemetryStandalone` | `0x64EF0` | 458 | UnwindData |  |
| 6 | `InitializeTelemetryStandaloneWithDeviceId` | `0x65140` | 661 | UnwindData |  |
| 15 | `UninitializeTelemetry` | `0x653E0` | 163 | UnwindData |  |
| 12 | `NvTelemetrySetAbContext` | `0x65490` | 533 | UnwindData |  |
| 9 | `NvTelemetrySendEvent` | `0x656B0` | 941 | UnwindData |  |
| 8 | `NvTelemetrySendAnonymousEvent` | `0x65A60` | 941 | UnwindData |  |
| 10 | `NvTelemetrySendFeedback` | `0x65E10` | 26 | UnwindData |  |
| 11 | `NvTelemetrySendFeedback_2` | `0x65E30` | 2,209 | UnwindData |  |
| 4 | `GetUserTelemetryConsent` | `0x66700` | 925 | UnwindData |  |
| 14 | `SetUserTelemetryConsent` | `0x66AA0` | 713 | UnwindData |  |
| 3 | `GetDeviceTelemetryConsent` | `0x66D70` | 925 | UnwindData |  |
| 13 | `SetDeviceTelemetryConsent` | `0x67110` | 713 | UnwindData |  |
| 1 | `DeviceId` | `0x673E0` | 257 | UnwindData |  |
| 2 | `DeviceIdFree` | `0x675B0` | 2,677,228 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
