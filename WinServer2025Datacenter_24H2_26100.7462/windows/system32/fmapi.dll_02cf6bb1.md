# Binary Specification: fmapi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\fmapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `02cf6bb117203601b771488c1bd554008d06d31891cf5f159542e6bec45ac6f0`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CloseFileRestoreContext` | `0xF590` | 276 | UnwindData |  |
| 2 | `CreateFileRestoreContext` | `0xF6B0` | 1,048 | UnwindData |  |
| 3 | `DetectBootSector` | `0xFAD0` | 272 | UnwindData |  |
| 4 | `DetectEncryptedVolume` | `0xFBF0` | 29 | UnwindData |  |
| 5 | `DetectEncryptedVolumeEx` | `0xFBF0` | 29 | UnwindData |  |
| 8 | `SupplyDecryptionInfo` | `0xFBF0` | 29 | UnwindData |  |
| 6 | `RestoreFile` | `0xFD30` | 469 | UnwindData |  |
| 7 | `ScanRestorableFiles` | `0xFF10` | 378 | UnwindData |  |
