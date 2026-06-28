# Binary Specification: netdiagfx.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\netdiagfx.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e7299a8a9eb13cfaba20f3cd2f5f3691800938c03224b6b795db026fcdefd892`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `WdiDiagnosticModuleMain` | `0x4A00` | 221 | UnwindData |  |
| 2 | `WdiGetDiagnosticModuleInterfaceVersion` | `0x4AF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `WdiHandleInstance` | `0x4B00` | 1,956 | UnwindData |  |
| 4 | `HelperTraceEvent` | `0x53C0` | 123 | UnwindData |  |
| 5 | `HelperTraceInitialize` | `0x5450` | 17 | UnwindData |  |
| 6 | `HelperTraceUninitialize` | `0x5470` | 17 | UnwindData |  |
