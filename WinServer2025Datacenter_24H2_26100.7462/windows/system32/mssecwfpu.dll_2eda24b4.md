# Binary Specification: mssecwfpu.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\mssecwfpu.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2eda24b49527f124210b2acc6087fdf121ab68a5a3a80e8b75687af009f671cc`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `SecSetWfpGuardConfiguration` | `0x4D00` | 432 | UnwindData |  |
| 2 | `SecWfpAllowDriverUnload` | `0x4EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `SecWfpClose` | `0x4EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `SecWfpOpen` | `0x4ED0` | 100 | UnwindData |  |
