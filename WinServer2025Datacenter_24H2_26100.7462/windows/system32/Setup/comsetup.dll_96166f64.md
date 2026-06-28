# Binary Specification: comsetup.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Setup\comsetup.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `96166f641e5bbe0be6188e68c04240bb85896efd9416ccf3a22fc8488fc20b38`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `InstallOnReboot` | `0x3850` | 837 | UnwindData |  |
| 2 | `RunComPlusSetWebApplicationServerRoleW` | `0x3C60` | 68 | UnwindData |  |
| 4 | `UpgradeDSSchema` | `0x3ED0` | 96 | UnwindData |  |
| 6 | `ComPlusGetWebApplicationServerRole` | `0x40D0` | 140 | UnwindData |  |
| 7 | `ComPlusSetWebApplicationServerRole` | `0x4170` | 50,864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `SetupPrintLog` | `0x10820` | 464 | UnwindData |  |
| 5 | `ComPlusCompleteCbbSetup` | `0x1CAF0` | 215 | UnwindData |  |
