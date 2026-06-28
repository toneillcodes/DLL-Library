# Binary Specification: sxsstore.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\sxsstore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2bf199c4e632c1b7df53894c1ff21bf9aa1f074bf0921633076f5b90fd8fa4d1`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `SxsStoreFinalize` | `0x4AF0` | 82 | UnwindData |  |
| 4 | `SxsStoreInitialize` | `0x4B50` | 306 | UnwindData |  |
| 1 | `DllGetClassObject` | `0x4C90` | 101 | UnwindData |  |
| 2 | `DllMain` | `0x4D00` | 3,948 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
