# Binary Specification: netdiagfx.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\netdiagfx.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `655f677de371fd04d35b08dee97670bf2dec8fc0942b219049966e8aa102117d`
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
