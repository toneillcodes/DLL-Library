# Binary Specification: cryptcatsvc.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\cryptcatsvc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `857e12c2031ec5c2650921812cb6aa5a8662c700122d4c7d0069df924cf59f11`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `CryptsvcDllCtrl` | `0xA130` | 87 | UnwindData |  |
| 1 | `CatDbOfflineRebuildDatabasesRundll32W` | `0x14620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CryptCATAdminCatalogDatabase` | `0x14630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `CatDbOfflineRebuildDatabasesW` | `0x14640` | 58,462 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
