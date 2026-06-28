# Binary Specification: ddptrace.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ddptrace.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5b59d68ed17634a908606fad64b67f27a7f95223bcc86a4b461956e2584f4e48`
* **Total Exported Functions:** 14

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 10 | `SrmGetTracingContextPerThread` | `0x5370` | 136 | UnwindData |  |
| 15 | `SrmGetTracingModuleInfo` | `0x5400` | 75 | UnwindData |  |
| 11 | `SrmGetTracingSequenceNumber` | `0x5460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `SrmIsDebugFlagSet` | `0x5470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `SrmIsTracingEnabled` | `0x5490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `SrmIsTracingEnabledOnFunction` | `0x54B0` | 178 | UnwindData |  |
| 7 | `SrmIsTracingEnabledOnModule` | `0x5570` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `SrmIsTracingEnabledPerThread` | `0x55A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `SrmSetTracingContextPerThread` | `0x55D0` | 124 | UnwindData |  |
| 4 | `SrmTraceBinary` | `0x5660` | 107 | UnwindData |  |
| 1 | `SrmTraceInitialize` | `0x56E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `SrmTraceMessage` | `0x5700` | 96 | UnwindData |  |
| 2 | `SrmTraceUninitialize` | `0x5770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `SrmIsKernelDebuggerAttached` | `0x5790` | 67 | UnwindData |  |
