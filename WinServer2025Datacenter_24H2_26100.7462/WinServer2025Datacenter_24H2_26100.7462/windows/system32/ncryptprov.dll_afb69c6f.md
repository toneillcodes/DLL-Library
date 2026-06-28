# Binary Specification: ncryptprov.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ncryptprov.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `afb69c6f8a06a9109fecc2103927096f9f330d70f61392efc57af17fa44380da`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `GetKeyStorageInterface` | `0x169C0` | 151 | UnwindData |  |
| 3 | `SKCacheFlush` | `0x1B1C0` | 132 | UnwindData |  |
| 1 | `BCryptIsoDoStateChangeWork` | `0x475C0` | 194 | UnwindData |  |
| 4 | `SetAuditingInterface` | `0x4F870` | 111,813 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
