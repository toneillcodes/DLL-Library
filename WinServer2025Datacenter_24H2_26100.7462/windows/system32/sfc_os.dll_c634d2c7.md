# Binary Specification: sfc_os.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\sfc_os.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c634d2c7647566808bc7a5796ac9389925e75664e8d31eab2813c7d128043fbb`
* **Total Exported Functions:** 18

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 9 | `SfcGetNextProtectedFile` | `0x1010` | 141 | UnwindData |  |
| 13 | `SfcIsFileProtected` | `0x10B0` | 144 | UnwindData |  |
| 14 | `SfcIsKeyProtected` | `0x1150` | 63 | UnwindData |  |
| 1 | `BeginFileMapEnumeration` | `0x11A0` | 99 | UnwindData |  |
| 3 | `GetNextFileMapContent` | `0x1210` | 203 | UnwindData |  |
| 2 | `CloseFileMapEnumeration` | `0x12F0` | 53 | UnwindData |  |
| 10 | `SfcInitProt` | `0x1370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `SfpDeleteCatalog` | `0x1370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `SfpInstallCatalog` | `0x1370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `SfpVerifyFile` | `0x1380` | 29 | UnwindData |  |
| 4 | `SRSetRestorePointA` | `0x13B0` | 168 | UnwindData |  |
| 5 | `SRSetRestorePointW` | `0x1460` | 168 | UnwindData |  |
| 6 | `SfcClose` | `0x1510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `SfcTerminateWatcherThread` | `0x1510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `SfcConnectToServer` | `0x1520` | 0 | Indeterminate |  |
| 8 | `SfcFileException` | `0x1520` | 0 | Indeterminate |  |
| 11 | `SfcInitiateScan` | `0x1520` | 0 | Indeterminate |  |
| 12 | `SfcInstallProtectedFiles` | `0x1520` | 0 | Indeterminate |  |
