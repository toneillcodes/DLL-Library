# Binary Specification: dfdts.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\dfdts.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `389d2736a967d51fe50ec033f23d7f14ff62b73d8a7c1b4fffd8f7db2f488a29`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DfdGetDefaultPolicyAndSMART` | `0x2470` | 431 | UnwindData |  |
| 2 | `WdiDiagnosticModuleMain` | `0x2630` | 419 | UnwindData |  |
| 3 | `WdiGetDiagnosticModuleInterfaceVersion` | `0x27E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `WdiHandleInstance` | `0x27F0` | 999 | UnwindData |  |
