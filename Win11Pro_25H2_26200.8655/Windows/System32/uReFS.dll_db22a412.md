# Binary Specification: uReFS.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\uReFS.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `db22a4125f44610c019885c7836a1822df52b22fd6f24d507ea7960de4ee5bde`
* **Total Exported Functions:** 15

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `Chkdsk` | `0x9930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `Extend` | `0x9930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `Recover` | `0x9930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `ChkdskEx` | `0x9940` | 166 | UnwindData |  |
| 8 | `Format` | `0x99F0` | 659 | UnwindData |  |
| 9 | `FormatEx` | `0x9C90` | 1,649 | UnwindData |  |
| 10 | `GetFilesystemInformation` | `0xA310` | 23 | UnwindData |  |
| 11 | `GetFilesystemInformationWithFlags` | `0xA330` | 431 | UnwindData |  |
| 12 | `GetFsFormatOptions` | `0xA4F0` | 79 | UnwindData |  |
| 15 | `SetOriginalVolumeName` | `0x16190` | 147 | UnwindData |  |
| 1 | `??0REFS_SA@@QEAA@XZ` | `0x1B0F0` | 146 | UnwindData |  |
| 3 | `??1REFS_SA@@UEAA@XZ` | `0x1B1D0` | 91 | UnwindData |  |
| 13 | `?Initialize@REFS_SA@@QEAAEPEAVLOG_IO_DP_DRIVE@@PEAVMESSAGE@@K@Z` | `0x1B540` | 242 | UnwindData |  |
| 2 | `??0REFS_UPCASE_TABLE@@QEAA@XZ` | `0x1BE20` | 77 | UnwindData |  |
| 4 | `??1REFS_UPCASE_TABLE@@UEAA@XZ` | `0x1BE80` | 44 | UnwindData |  |
