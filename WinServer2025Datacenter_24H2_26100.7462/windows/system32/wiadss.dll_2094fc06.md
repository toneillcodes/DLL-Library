# Binary Specification: wiadss.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wiadss.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2094fc06f715105f4a0aba4f55f58736786bf7972c573fa2514d76d1f3efe600`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `CloseFindContext` | `0x3700` | 214 | UnwindData |  |
| 1 | `FindFirstImportDS` | `0x3A40` | 469 | UnwindData |  |
| 7 | `FindImportDSByDeviceName` | `0x3C20` | 169 | UnwindData |  |
| 2 | `FindNextImportDS` | `0x3CD0` | 665 | UnwindData |  |
| 6 | `GetLoaderStatus` | `0x4540` | 1,936 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `LoadImportDS` | `0x4CD0` | 601 | UnwindData |  |
| 5 | `UnloadImportDS` | `0x5FC0` | 177 | UnwindData |  |
