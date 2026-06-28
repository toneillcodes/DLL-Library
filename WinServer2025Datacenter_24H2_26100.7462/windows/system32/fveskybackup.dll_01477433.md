# Binary Specification: fveskybackup.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\fveskybackup.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `01477433c43b129cdc7c5cb8c364569489eef65d067e46a43b302cb1cb18eafa`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `FveBackupRecoveryPasswordToSkyDrive` | `0xB200` | 4,165 | UnwindData |  |
| 5 | `FveGetSkyDriveRecoveryPasswordBackupAccount` | `0xC250` | 790 | UnwindData |  |
| 6 | `FveRecoveryPasswordAccountStrToBufObfuscate` | `0xC570` | 2,857 | UnwindData |  |
| 7 | `FveUploadRecoveryPasswordToPDRWrapper` | `0xD0A0` | 360 | UnwindData |  |
| 1 | `FveBackupRecoveryPasswordToCloudDomain` | `0x11BE0` | 3,979 | UnwindData |  |
| 3 | `FveDeleteRecoveryPasswordsFromCloudDomain` | `0x14290` | 2,946 | UnwindData |  |
| 4 | `FveGetAllRecoveryPasswordsFromCloudDomain` | `0x14E20` | 3,563 | UnwindData |  |
