# Binary Specification: udhisapi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\udhisapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9f06402bb952789a9cdd574cf2c749e1b05fa57e3614a3299e8cc991e1652eb9`
* **Total Exported Functions:** 3

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `GetExtensionVersion` | `0x2430` | 146 | UnwindData |  |
| 2 | `HttpExtensionProc` | `0x24D0` | 900 | UnwindData |  |
| 3 | `TerminateExtension` | `0x2860` | 36,624 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
