# Binary Specification: vsstrace.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\vsstrace.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e0db5ee54e4985f8de5f1784efe803a69f74f7dd6dea8916d6efbe9b296fc04a`
* **Total Exported Functions:** 15

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 9 | `VssSetTracingContextPerThread` | `0x1AA0` | 88 | UnwindData |  |
| 10 | `VssGetTracingContextPerThread` | `0x1B00` | 20 | UnwindData |  |
| 5 | `VssIsTracingEnabled` | `0x1B90` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `VssTraceInitialize` | `0x1D70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `VssTraceUninitialize` | `0x1DA0` | 7,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `AssertFail` | `0x3A60` | 467 | UnwindData |  |
| 12 | `VssGetTracingModuleInfo` | `0x55F0` | 147 | UnwindData |  |
| 11 | `VssGetTracingSequenceNumber` | `0x5690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `VssIsKernelDebuggerAttached` | `0x56B0` | 67 | UnwindData |  |
| 8 | `VssIsTracingEnabledOnFunction` | `0x5700` | 63 | UnwindData |  |
| 7 | `VssIsTracingEnabledOnModule` | `0x5750` | 62 | UnwindData |  |
| 6 | `VssIsTracingEnabledPerThread` | `0x57A0` | 55 | UnwindData |  |
| 14 | `VssSetDebugReport` | `0x57E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `VssTraceBinary` | `0x57F0` | 124 | UnwindData |  |
| 3 | `VssTraceMessage` | `0x5880` | 113 | UnwindData |  |
