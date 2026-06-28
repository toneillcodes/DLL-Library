# Binary Specification: comsetup.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\setup\comsetup.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `00d698bd1dbb767074ceebbe21f70d9e72490662a2146a57ce7c0d43d5e4b7a8`
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
