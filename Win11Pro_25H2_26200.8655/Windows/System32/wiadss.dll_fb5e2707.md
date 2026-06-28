# Binary Specification: wiadss.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wiadss.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fb5e27071390a5a9452fc8a4a6aa96f53af7d8cab1df12014b38cb573ae21072`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `CloseFindContext` | `0x3700` | 214 | UnwindData |  |
| 1 | `FindFirstImportDS` | `0x3A40` | 469 | UnwindData |  |
| 7 | `FindImportDSByDeviceName` | `0x3C20` | 169 | UnwindData |  |
| 2 | `FindNextImportDS` | `0x3CD0` | 665 | UnwindData |  |
| 6 | `GetLoaderStatus` | `0x4510` | 2,032 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `LoadImportDS` | `0x4D00` | 601 | UnwindData |  |
| 5 | `UnloadImportDS` | `0x5FF0` | 177 | UnwindData |  |
