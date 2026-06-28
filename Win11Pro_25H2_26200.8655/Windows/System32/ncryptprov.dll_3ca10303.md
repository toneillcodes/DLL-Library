# Binary Specification: ncryptprov.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ncryptprov.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3ca10303eebeb113b4a81596ec1c69cb8908d733bf7b9e14206781df36de15ee`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `GetKeyStorageInterface` | `0x169A0` | 151 | UnwindData |  |
| 3 | `SKCacheFlush` | `0x1B3C0` | 132 | UnwindData |  |
| 1 | `BCryptIsoDoStateChangeWork` | `0x473D0` | 194 | UnwindData |  |
| 4 | `SetAuditingInterface` | `0x4ED70` | 111,253 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
