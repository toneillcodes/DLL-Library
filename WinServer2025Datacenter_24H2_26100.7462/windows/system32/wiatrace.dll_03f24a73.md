# Binary Specification: wiatrace.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wiatrace.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `03f24a73f0163070ee9ace60ecbd1bb3963a598a9413ebf90c03ffdde09ef875`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `WIATRACE_OutputString` | `0x1320` | 147 | UnwindData |  |
| 3 | `WIATRACE_GetTraceSettings` | `0x22D0` | 116 | UnwindData |  |
| 7 | `WIATRACE_SetTraceSettings` | `0x2350` | 86 | UnwindData |  |
| 2 | `WIATRACE_GetIndentLevel` | `0x23B0` | 896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `WIATRACE_Init` | `0x2730` | 3,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `WIATRACE_Term` | `0x2730` | 3,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `WIATRACE_DecrementIndentLevel` | `0x36A0` | 62 | UnwindData |  |
| 4 | `WIATRACE_IncrementIndentLevel` | `0x36F0` | 56 | UnwindData |  |
