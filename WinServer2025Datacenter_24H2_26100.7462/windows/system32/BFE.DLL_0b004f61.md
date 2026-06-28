# Binary Specification: BFE.DLL

## Binary Metadata
* **Original Path:** `c:\windows\system32\BFE.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0b004f612e55ad36a8b7827f9434c50185b323f5cb8a78e50b7c442e4df14130`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `BfeGetDirectDispatchTable` | `0x45B40` | 8,272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `BfeServiceMain` | `0x47B90` | 147 | UnwindData |  |
| 4 | `SvchostPushServiceGlobals` | `0x655D0` | 23,776 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `BfeOnServiceStartTypeChange` | `0x6B2B0` | 241 | UnwindData |  |
