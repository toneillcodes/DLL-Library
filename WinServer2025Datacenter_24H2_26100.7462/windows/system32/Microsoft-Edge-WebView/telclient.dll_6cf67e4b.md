# Binary Specification: telclient.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Microsoft-Edge-WebView\telclient.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6cf67e4b0172324eacb8019048171803978e8eea5371c157c9fae96f40566c3c`
* **Total Exported Functions:** 23

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 23 | `GetHandleVerifier` | `0x4D240` | 33 | UnwindData |  |
| 7 | `??4MetricsLogSplitter@telemetry_client@@QEAAAEAV01@AEBV01@@Z` | `0x939D0` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `??4TelemetryClientDecoder@telemetry_client@@QEAAAEAV01@AEBV01@@Z` | `0x939D0` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `??1MetricsLogSplitter@telemetry_client@@UEAA@XZ` | `0x93BE0` | 7,376 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `??1TelemetryClientDecoder@telemetry_client@@UEAA@XZ` | `0x93BE0` | 7,376 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `??0MetricsLogSplitter@telemetry_client@@QEAA@AEBV01@@Z` | `0x958B0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0MetricsLogSplitter@telemetry_client@@QEAA@XZ` | `0x958B0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0TelemetryClientDecoder@telemetry_client@@QEAA@AEBV01@@Z` | `0x958B0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `??0TelemetryClientDecoder@telemetry_client@@QEAA@XZ` | `0x958B0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `?AllocLogsContainer@MetricsLogSplitter@telemetry_client@@KA?AV?$unique_ptr@V?$vector@ULogInfo@telemetry_client@@V?$allocator@ULogInfo@telemetry_client@@@__Cr@std@@@__Cr@std@@P6AXPEBV123@@Z@__Cr@std@@XZ` | `0x959D0` | 55 | UnwindData |  |
| 18 | `FreeLogs` | `0x95A10` | 91 | UnwindData |  |
| 20 | `FreeSplitter` | `0x95A70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `FreeTelemetryClientDecoder` | `0x95A70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `CreateSplitter` | `0x95A90` | 59 | UnwindData |  |
| 22 | `FreeTelemetryClientDecoderPayload` | `0x95B30` | 46 | UnwindData |  |
| 14 | `CreateTelemetryClientDecoder` | `0x95B60` | 53 | UnwindData |  |
| 11 | `?AllocDecodedPayload@TelemetryClientDecoder@telemetry_client@@KA?AV?$unique_ptr@UDecodedPayload@telemetry_client@@P6AXPEBU12@@Z@__Cr@std@@XZ` | `0x95BA0` | 51 | UnwindData |  |
| 15 | `DecodePayload` | `0xA1BB0` | 34 | UnwindData |  |
| 17 | `DecodeUmaPayload` | `0xA1BB0` | 34 | UnwindData |  |
| 16 | `DecodeUkmPayload` | `0xA1F00` | 37 | UnwindData |  |
| 19 | `FreePayload` | `0xA1F30` | 76 | UnwindData |  |
| 9 | `??_7MetricsLogSplitter@telemetry_client@@6B@` | `0x1F1BD0` | 0 | Indeterminate |  |
| 10 | `??_7TelemetryClientDecoder@telemetry_client@@6B@` | `0x1F1BD0` | 0 | Indeterminate |  |
