# Binary Specification: aidd.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\aidd.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fb6dfd5aa7035ef48863f9b8e89516ccfed618ad6e6d56b1a72404d318f4e4fe`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `AiddInitialize` | `0xA6D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `AiddIsEnabled` | `0xA6E0` | 262 | UnwindData |  |
| 3 | `AiddRunTask` | `0xA7F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `AiddUninitialize` | `0xA800` | 736,924 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
