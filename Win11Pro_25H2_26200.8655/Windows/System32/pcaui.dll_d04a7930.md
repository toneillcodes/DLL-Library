# Binary Specification: pcaui.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\pcaui.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d04a7930c6e5fc7aca4c28f4d7b76423a1828ba5f931348d9e1542772728ba90`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `PcaShowDialog` | `0x202D0` | 97 | UnwindData |  |
| 1 | `DisplayApphelpDialog` | `0x22500` | 62 | UnwindData |  |
| 2 | `PcaLaunchApplicationWithConsent` | `0x22550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `PcaPersistSettingsAndLaunchApplication` | `0x22560` | 281 | UnwindData |  |
