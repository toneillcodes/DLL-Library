# Binary Specification: BFE.DLL

## Binary Metadata
* **Original Path:** `C:\Windows\System32\BFE.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `88cc4b201dfe226156edc3da982e30c6e043ca920be1ef5deca8e3fda038d565`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `BfeGetDirectDispatchTable` | `0x45640` | 9,264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `BfeServiceMain` | `0x47A70` | 147 | UnwindData |  |
| 4 | `SvchostPushServiceGlobals` | `0x62DE0` | 24,416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `BfeOnServiceStartTypeChange` | `0x68D40` | 241 | UnwindData |  |
