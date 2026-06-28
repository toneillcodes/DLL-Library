# Binary Specification: MsiCofire.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\MsiCofire.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c133e57d196311c42fcdef33b793a4b07f2fb27319e4619c46939726a0edc86b`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `WdiDiagnosticModuleMain` | `0x2700` | 106 | UnwindData |  |
| 2 | `WdiGetDiagnosticModuleInterfaceVersion` | `0x2770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `WdiHandleInstance` | `0x2780` | 385 | UnwindData |  |
| 4 | `DllMain` | `0x2AC0` | 16,847 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
