# Binary Specification: camext.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\camext.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a2851855d1fadbf294c4bc79b72ede049592797f4145215c82e37b2dad8c44a3`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CamCleanupDisardedCandidateAccounts` | `0x1DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CamConnectCandidateUser` | `0x1DC0` | 52 | UnwindData |  |
| 3 | `CamFreeAuthBuffer` | `0x1E00` | 60 | UnwindData |  |
| 4 | `CamFreeBuffer` | `0x1E50` | 36 | UnwindData |  |
| 5 | `CamGetCandidateAccountCredz` | `0x1E80` | 30 | UnwindData |  |
| 6 | `CamGetCandidateUserSessionIds` | `0x1EB0` | 30 | UnwindData |  |
| 7 | `CamGetNonCandidateUserSessionIds` | `0x1EE0` | 30 | UnwindData |  |
| 8 | `CamIsCandidateUser` | `0x1F10` | 30 | UnwindData |  |
| 9 | `CamIsEphemeralCandidateUser` | `0x1F40` | 30 | UnwindData |  |
| 10 | `CamRefreshCandidateUser` | `0x1F70` | 0 | Indeterminate |  |
