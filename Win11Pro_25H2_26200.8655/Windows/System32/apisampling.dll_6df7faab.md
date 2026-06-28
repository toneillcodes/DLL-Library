# Binary Specification: apisampling.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\apisampling.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6df7faab5a611a7a08f8de2c1a646b62a3c7d4f2f6f28a2e25623a51f8304ad2`
* **Total Exported Functions:** 13

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `APISamplingClearSettings` | `0x4E80` | 40 | UnwindData |  |
| 2 | `APISamplingGetDwordSettings` | `0x4EB0` | 76 | UnwindData |  |
| 3 | `APISamplingGetStatus` | `0x4F10` | 67 | UnwindData |  |
| 4 | `APISamplingGetStringSettings` | `0x4F60` | 76 | UnwindData |  |
| 5 | `APISamplingInitialize` | `0x4FC0` | 163 | UnwindData |  |
| 6 | `APISamplingSetDwordSettings` | `0x5070` | 60 | UnwindData |  |
| 7 | `APISamplingSetFileCallback` | `0x50C0` | 50 | UnwindData |  |
| 8 | `APISamplingSetProcessFilter` | `0x5100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `APISamplingSetStringSettings` | `0x5110` | 60 | UnwindData |  |
| 10 | `APISamplingSetValue` | `0x5160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `APISamplingStart` | `0x5170` | 46 | UnwindData |  |
| 12 | `APISamplingStop` | `0x51B0` | 43 | UnwindData |  |
| 13 | `APISamplingUninitialize` | `0x51F0` | 25 | UnwindData |  |
