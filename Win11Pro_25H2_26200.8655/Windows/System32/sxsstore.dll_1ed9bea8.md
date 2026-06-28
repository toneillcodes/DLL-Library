# Binary Specification: sxsstore.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\sxsstore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1ed9bea871b57258c581826a47bdf41e26e0df9b3a34a0952d3efbcefd3cacb0`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `SxsStoreFinalize` | `0x4B00` | 82 | UnwindData |  |
| 4 | `SxsStoreInitialize` | `0x4B60` | 306 | UnwindData |  |
| 1 | `DllGetClassObject` | `0x4CA0` | 101 | UnwindData |  |
| 2 | `DllMain` | `0x4D10` | 3,948 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
