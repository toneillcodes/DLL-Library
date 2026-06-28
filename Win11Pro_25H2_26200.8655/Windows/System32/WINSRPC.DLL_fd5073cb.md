# Binary Specification: WINSRPC.DLL

## Binary Metadata
* **Original Path:** `C:\Windows\System32\WINSRPC.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fd5073cbe1588ceeb399c0bce3a3a31e07c97e69e24bc541d031ad1b58189d21`
* **Total Exported Functions:** 31

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `WinsAllocMem` | `0x1920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `WinsFreeMem` | `0x1940` | 27 | UnwindData |  |
| 29 | `WinsUBind` | `0x1970` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `WinsABind` | `0x19B0` | 244 | UnwindData |  |
| 11 | `WinsGetBrowserNames` | `0x1BD0` | 65 | UnwindData |  |
| 30 | `WinsUnbind` | `0x1C20` | 32 | UnwindData |  |
| 3 | `WinsBackup` | `0x1C50` | 73 | UnwindData |  |
| 4 | `WinsCheckAccess` | `0x1CA0` | 65 | UnwindData |  |
| 5 | `WinsDelDbRecs` | `0x1CF0` | 74 | UnwindData |  |
| 6 | `WinsDeleteWins` | `0x1EF0` | 65 | UnwindData |  |
| 7 | `WinsDoScavenging` | `0x1F40` | 60 | UnwindData |  |
| 8 | `WinsDoScavengingNew` | `0x1F90` | 65 | UnwindData |  |
| 9 | `WinsDoStaticInit` | `0x1FE0` | 70 | UnwindData |  |
| 12 | `WinsGetDbRecs` | `0x2030` | 86 | UnwindData |  |
| 13 | `WinsGetDbRecsByName` | `0x2090` | 119 | UnwindData |  |
| 14 | `WinsGetNameAndAdd` | `0x2110` | 70 | UnwindData |  |
| 15 | `WinsPullRange` | `0x2160` | 82 | UnwindData |  |
| 16 | `WinsRecordAction` | `0x2310` | 63 | UnwindData |  |
| 17 | `WinsResetCounters` | `0x2360` | 60 | UnwindData |  |
| 18 | `WinsRestore` | `0x23B0` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `WinsRestoreEx` | `0x2790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `WinsSetFlags` | `0x27A0` | 64 | UnwindData |  |
| 21 | `WinsSetPriorityClass` | `0x27F0` | 64 | UnwindData |  |
| 22 | `WinsStatus` | `0x2840` | 69 | UnwindData |  |
| 23 | `WinsStatusNew` | `0x2890` | 69 | UnwindData |  |
| 24 | `WinsStatusWHdl` | `0x28E0` | 69 | UnwindData |  |
| 25 | `WinsSyncUp` | `0x2930` | 88 | UnwindData |  |
| 26 | `WinsTerm` | `0x2990` | 67 | UnwindData |  |
| 27 | `WinsTombstoneDbRecs` | `0x29E0` | 72 | UnwindData |  |
| 28 | `WinsTrigger` | `0x2A30` | 70 | UnwindData |  |
| 31 | `WinsWorkerThdUpd` | `0x2A80` | 64 | UnwindData |  |
