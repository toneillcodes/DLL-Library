# Binary Specification: telclient.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Microsoft-Edge-WebView\telclient.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8889bc6bb70a9c13aec1cab6a209e69ba7d0af44f501c27304e11bc82d12293e`
* **Total Exported Functions:** 23

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 23 | `GetHandleVerifier` | `0x89D00` | 33 | UnwindData |  |
| 7 | `??4MetricsLogSplitter@telemetry_client@@QEAAAEAV01@AEBV01@@Z` | `0x140460` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `??4TelemetryClientDecoder@telemetry_client@@QEAAAEAV01@AEBV01@@Z` | `0x140460` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `??1MetricsLogSplitter@telemetry_client@@UEAA@XZ` | `0x140670` | 7,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `??1TelemetryClientDecoder@telemetry_client@@UEAA@XZ` | `0x140670` | 7,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `??0MetricsLogSplitter@telemetry_client@@QEAA@AEBV01@@Z` | `0x1422C0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0MetricsLogSplitter@telemetry_client@@QEAA@XZ` | `0x1422C0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0TelemetryClientDecoder@telemetry_client@@QEAA@AEBV01@@Z` | `0x1422C0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `??0TelemetryClientDecoder@telemetry_client@@QEAA@XZ` | `0x1422C0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `?AllocLogsContainer@MetricsLogSplitter@telemetry_client@@KA?AV?$unique_ptr@V?$vector@ULogInfo@telemetry_client@@V?$allocator@ULogInfo@telemetry_client@@@__Cr@std@@@__Cr@std@@P6AXPEBV123@@Z@__Cr@std@@XZ` | `0x1423E0` | 55 | UnwindData |  |
| 18 | `FreeLogs` | `0x142420` | 96 | UnwindData |  |
| 20 | `FreeSplitter` | `0x142480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `FreeTelemetryClientDecoder` | `0x142480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `CreateSplitter` | `0x1424A0` | 59 | UnwindData |  |
| 22 | `FreeTelemetryClientDecoderPayload` | `0x142540` | 65 | UnwindData |  |
| 14 | `CreateTelemetryClientDecoder` | `0x142590` | 53 | UnwindData |  |
| 11 | `?AllocDecodedPayload@TelemetryClientDecoder@telemetry_client@@KA?AV?$unique_ptr@UDecodedPayload@telemetry_client@@P6AXPEBU12@@Z@__Cr@std@@XZ` | `0x1425D0` | 51 | UnwindData |  |
| 15 | `DecodePayload` | `0x14E990` | 34 | UnwindData |  |
| 17 | `DecodeUmaPayload` | `0x14E990` | 34 | UnwindData |  |
| 16 | `DecodeUkmPayload` | `0x14ED00` | 37 | UnwindData |  |
| 19 | `FreePayload` | `0x14ED30` | 76 | UnwindData |  |
| 9 | `??_7MetricsLogSplitter@telemetry_client@@6B@` | `0x2EEBF0` | 0 | Indeterminate |  |
| 10 | `??_7TelemetryClientDecoder@telemetry_client@@6B@` | `0x2EEBF0` | 0 | Indeterminate |  |
