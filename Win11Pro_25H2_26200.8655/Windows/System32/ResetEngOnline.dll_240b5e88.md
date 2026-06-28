# Binary Specification: ResetEngOnline.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ResetEngOnline.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `240b5e88c5b30ea4caabe74b4c56bc9f59c623d8a7240aba9834f2c2d7a7f968`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `IsEsimPresent` | `0x4D90` | 726 | UnwindData |  |
| 3 | `ResetEsim` | `0x5270` | 265 | UnwindData |  |
| 4 | `ResetGetEngineInterface` | `0x5380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `ResetInitializeEngine` | `0x53A0` | 18 | UnwindData |  |
| 6 | `ResetRebootSystem` | `0x53C0` | 200 | UnwindData |  |
| 7 | `ResetReleaseEngine` | `0x5490` | 96 | UnwindData |  |
| 8 | `UninstallFinalize` | `0x5500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `UninstallGetInterface` | `0x5510` | 7,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `GetNetworkCost` | `0x7190` | 188 | UnwindData |  |
