# Binary Specification: syssetup.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\syssetup.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `93e6df0bcdc4d46509bd0991f55319ac1df0e7eb4e2da7c9aa870f98c6287e26`
* **Total Exported Functions:** 13

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 9 | `SetupInfObjectInstallActionW` | `0x0` | - | Forwarded | Forwarded to: `SETUPAPI.InstallHinfSectionW` |
| 1 | `AsrAddSifEntryA` | `0x1BC0` | 29 | UnwindData |  |
| 2 | `AsrAddSifEntryW` | `0x1BC0` | 29 | UnwindData |  |
| 3 | `AsrCreateStateFileA` | `0x1BC0` | 29 | UnwindData |  |
| 4 | `AsrCreateStateFileW` | `0x1BC0` | 29 | UnwindData |  |
| 5 | `AsrFreeContext` | `0x1BC0` | 29 | UnwindData |  |
| 6 | `AsrRestorePlugPlayRegistryData` | `0x1BC0` | 29 | UnwindData |  |
| 7 | `GetAnswerFileSetting` | `0x1BC0` | 29 | UnwindData |  |
| 8 | `SetupChangeFontSize` | `0x2810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `SetupSetDisplay` | `0x2820` | 1,385 | UnwindData |  |
| 11 | `Sysprep_Specialize_Offline_Pnp_Compat` | `0x2DC0` | 228 | UnwindData |  |
| 12 | `Sysprep_Specialize_Pnp_Compat` | `0x2EB0` | 873 | UnwindData |  |
| 13 | `WaitForSamService` | `0x3220` | 258 | UnwindData |  |
