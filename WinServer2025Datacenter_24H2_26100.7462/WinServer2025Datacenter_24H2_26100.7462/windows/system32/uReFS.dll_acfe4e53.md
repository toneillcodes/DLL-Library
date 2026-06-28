# Binary Specification: uReFS.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\uReFS.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `acfe4e53d6e82ecf922cd3d2a69f37c0746e1121444406ba10a53e6115bf74b0`
* **Total Exported Functions:** 15

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `Chkdsk` | `0xA140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `Extend` | `0xA140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `Recover` | `0xA140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `ChkdskEx` | `0xA150` | 166 | UnwindData |  |
| 8 | `Format` | `0xA200` | 659 | UnwindData |  |
| 9 | `FormatEx` | `0xA4A0` | 1,649 | UnwindData |  |
| 10 | `GetFilesystemInformation` | `0xAB20` | 23 | UnwindData |  |
| 11 | `GetFilesystemInformationWithFlags` | `0xAB40` | 431 | UnwindData |  |
| 12 | `GetFsFormatOptions` | `0xAD00` | 79 | UnwindData |  |
| 15 | `SetOriginalVolumeName` | `0x169A0` | 147 | UnwindData |  |
| 1 | `??0REFS_SA@@QEAA@XZ` | `0x1B900` | 146 | UnwindData |  |
| 3 | `??1REFS_SA@@UEAA@XZ` | `0x1B9E0` | 91 | UnwindData |  |
| 13 | `?Initialize@REFS_SA@@QEAAEPEAVLOG_IO_DP_DRIVE@@PEAVMESSAGE@@K@Z` | `0x1BD50` | 242 | UnwindData |  |
| 2 | `??0REFS_UPCASE_TABLE@@QEAA@XZ` | `0x1C630` | 77 | UnwindData |  |
| 4 | `??1REFS_UPCASE_TABLE@@UEAA@XZ` | `0x1C690` | 44 | UnwindData |  |
