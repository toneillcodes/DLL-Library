# Binary Specification: srmtrace.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\srmtrace.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9a2d9a9278522d4ea92d46163140676a221f8dac379ea6ebec31fc7718f093aa`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 10 | `SrmGetTracingContextPerThread` | `0x4D50` | 96 | UnwindData |  |
| 12 | `SrmGetTracingModuleInfo` | `0x4DC0` | 78 | UnwindData |  |
| 11 | `SrmGetTracingSequenceNumber` | `0x4E20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `SrmIsTracingEnabled` | `0x4E30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `SrmIsTracingEnabledOnFunction` | `0x4E50` | 152 | UnwindData |  |
| 7 | `SrmIsTracingEnabledOnModule` | `0x4EF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `SrmIsTracingEnabledPerThread` | `0x4F20` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `SrmSetTracingContextPerThread` | `0x4F50` | 86 | UnwindData |  |
| 1 | `SrmTraceInitialize` | `0x4FB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `SrmTraceMessage` | `0x4FD0` | 96 | UnwindData |  |
| 2 | `SrmTraceUninitialize` | `0x5040` | 27,130 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
