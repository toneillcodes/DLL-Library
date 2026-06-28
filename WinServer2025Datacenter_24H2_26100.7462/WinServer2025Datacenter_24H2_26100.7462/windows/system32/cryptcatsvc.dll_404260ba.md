# Binary Specification: cryptcatsvc.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\cryptcatsvc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `404260ba57509a0f921c9e20f63ec456ad4548b82fa07f6d2eecea2f2e3e041a`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `CryptsvcDllCtrl` | `0xA110` | 87 | UnwindData |  |
| 1 | `CatDbOfflineRebuildDatabasesRundll32W` | `0x14530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CryptCATAdminCatalogDatabase` | `0x14540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `CatDbOfflineRebuildDatabasesW` | `0x14550` | 60,190 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
