# Binary Specification: ttdloader.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ttdloader.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `56bddbadbc4a9012e6c1f2caa26ab4d08d9ce5575accabbc8de5925fa03f6e66`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `GetCfgPointers` | `0x1040` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `InjectThread` | `0x1200` | 102 | UnwindData |  |
| 4 | `StubDllEntry` | `0x3EB0` | 16,552 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `ntdllLdrInitializeThunk` | `0x7F58` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `ParametersBlock` | `0x7F68` | 0 | Indeterminate |  |
