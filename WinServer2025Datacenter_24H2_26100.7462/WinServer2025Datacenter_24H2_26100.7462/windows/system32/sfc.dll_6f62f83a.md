# Binary Specification: sfc.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\sfc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6f62f83a3f3affe40ab4d9bc2ed3b888a90866e7639700c77415f8f44778fbb4`
* **Total Exported Functions:** 16

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 10 | `SRSetRestorePoint` | `0x0` | - | Forwarded | Forwarded to: `sfc_os.SRSetRestorePointA` |
| 11 | `SRSetRestorePointA` | `0x0` | - | Forwarded | Forwarded to: `sfc_os.SRSetRestorePointA` |
| 12 | `SRSetRestorePointW` | `0x0` | - | Forwarded | Forwarded to: `sfc_os.SRSetRestorePointW` |
| 13 | `SfcGetNextProtectedFile` | `0x0` | - | Forwarded | Forwarded to: `sfc_os.SfcGetNextProtectedFile` |
| 14 | `SfcIsFileProtected` | `0x0` | - | Forwarded | Forwarded to: `sfc_os.SfcIsFileProtected` |
| 15 | `SfcIsKeyProtected` | `0x0` | - | Forwarded | Forwarded to: `sfc_os.SfcIsKeyProtected` |
| 16 | `SfpVerifyFile` | `0x0` | - | Forwarded | Forwarded to: `sfc_os.SfpVerifyFile` |
| 1 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `sfc_os.SfcInitProt` |
| 2 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `sfc_os.SfcTerminateWatcherThread` |
| 3 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `sfc_os.SfcConnectToServer` |
| 4 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `sfc_os.SfcClose` |
| 5 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `sfc_os.SfcFileException` |
| 6 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `sfc_os.SfcInitiateScan` |
| 7 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `sfc_os.SfcInstallProtectedFiles` |
| 8 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `sfc_os.SfpInstallCatalog` |
| 9 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `sfc_os.SfpDeleteCatalog` |
