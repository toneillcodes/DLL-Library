# Binary Specification: fveskybackup.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\fveskybackup.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `af7359c54be0316306c217b1ffba49275626abfd34b64739c200608b255ea393`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `FveBackupRecoveryPasswordToSkyDrive` | `0xB2E0` | 3,958 | UnwindData |  |
| 5 | `FveGetSkyDriveRecoveryPasswordBackupAccount` | `0xC260` | 790 | UnwindData |  |
| 6 | `FveRecoveryPasswordAccountStrToBufObfuscate` | `0xC580` | 2,857 | UnwindData |  |
| 7 | `FveUploadRecoveryPasswordToPDRWrapper` | `0xD0B0` | 360 | UnwindData |  |
| 1 | `FveBackupRecoveryPasswordToCloudDomain` | `0x115A0` | 3,979 | UnwindData |  |
| 3 | `FveDeleteRecoveryPasswordsFromCloudDomain` | `0x13C50` | 2,946 | UnwindData |  |
| 4 | `FveGetAllRecoveryPasswordsFromCloudDomain` | `0x147E0` | 3,563 | UnwindData |  |
