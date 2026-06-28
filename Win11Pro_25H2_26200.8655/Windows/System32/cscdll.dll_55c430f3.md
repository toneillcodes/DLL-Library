# Binary Specification: cscdll.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\cscdll.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `55c430f38cea90403e8c53a0dc92ae93f2463ce290cb648bca02dd8608d1b3f5`
* **Total Exported Functions:** 18

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 45 | `CSCDeleteW` | `0x2260` | 114 | UnwindData |  |
| 73 | `CSCDisconnectPath` | `0x22E0` | 104 | UnwindData |  |
| 14 | `CSCDoEnableDisable` | `0x2350` | 111 | UnwindData |  |
| 55 | `CSCEnumForStatsExW` | `0x23D0` | 29 | UnwindData |  |
| 49 | `CSCEnumForStatsW` | `0x23D0` | 29 | UnwindData |  |
| 10 | `CSCFindClose` | `0x2970` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `CSCFindFirstFileForSidW` | `0x29E0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `CSCFindFirstFileW` | `0x2AC0` | 48 | UnwindData |  |
| 44 | `CSCFindNextFileW` | `0x2BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `CSCIsCSCEnabled` | `0x2BB0` | 131 | UnwindData |  |
| 75 | `CSCIsPathOffline` | `0x2C40` | 164 | UnwindData |  |
| 50 | `CSCIsServerOfflineW` | `0x2CF0` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `CSCPinFileW` | `0x2E70` | 30 | UnwindData |  |
| 42 | `CSCQueryFileStatusW` | `0x2F60` | 132 | UnwindData |  |
| 11 | `CSCSetMaxSpace` | `0x2FF0` | 151 | UnwindData |  |
| 76 | `CSCTransitionPathOnline` | `0x3090` | 103 | UnwindData |  |
| 52 | `CSCTransitionServerOnlineW` | `0x3100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `CSCUnpinFileW` | `0x3110` | 30 | UnwindData |  |
