# Binary Specification: udhisapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\udhisapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `89a2f27a404029523c77fa333283126d015f5f5a55cc0b9d78f64a91aad072a1`
* **Total Exported Functions:** 3

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `GetExtensionVersion` | `0x2430` | 146 | UnwindData |  |
| 2 | `HttpExtensionProc` | `0x24D0` | 900 | UnwindData |  |
| 3 | `TerminateExtension` | `0x2860` | 36,624 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
