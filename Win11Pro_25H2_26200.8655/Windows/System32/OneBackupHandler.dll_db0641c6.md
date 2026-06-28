# Binary Specification: OneBackupHandler.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\OneBackupHandler.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `db0641c646425cffdff8c136dd88f9c6c6db09eaf7d81c2a8fa2aaff65006a39`
* **Total Exported Functions:** 3

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xBA60` | 42 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0xBA90` | 45 | UnwindData |  |
| 3 | `GetSetting` | `0xBB40` | 205,676 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
