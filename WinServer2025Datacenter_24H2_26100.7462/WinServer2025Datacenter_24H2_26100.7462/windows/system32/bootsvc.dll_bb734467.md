# Binary Specification: bootsvc.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\bootsvc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `bb734467e628d9191fa734974f696e3467c5a31c825466507a47e7abc6d21aa3`
* **Total Exported Functions:** 20

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `BfsCheckSystemPartition` | `0x1CD0` | 124 | UnwindData |  |
| 13 | `BfsRepairSystemPartition` | `0x1D60` | 1,013 | UnwindData |  |
| 2 | `BfsCleanupBcdStore` | `0x25D0` | 834 | UnwindData |  |
| 5 | `BfsInitializeBcdStore` | `0x2920` | 15 | UnwindData |  |
| 9 | `BfsMigrateLoaderSettings` | `0x2D90` | 731 | UnwindData |  |
| 19 | `BfsValidateBcdStore` | `0x3080` | 460 | UnwindData |  |
| 3 | `BfsCreateOfflineBootstat` | `0x83B0` | 530 | UnwindData |  |
| 10 | `BfsRedirectLogging` | `0x85D0` | 900 | UnwindData |  |
| 11 | `BfsReflectCurrentHypervisorLaunchType` | `0x8960` | 422 | UnwindData |  |
| 16 | `BfsServiceBootFiles` | `0x8B10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `BfsServiceBootFilesEx` | `0x8B30` | 18,752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `BfsGetVolumeName` | `0xD470` | 336 | UnwindData |  |
| 6 | `BfsInitializeSystemVolume` | `0xD5D0` | 103 | UnwindData |  |
| 7 | `BfsIsBitLockerDisabled` | `0xEB10` | 240 | UnwindData |  |
| 8 | `BfsIsBitLockerResealNeeded` | `0xEC10` | 649 | UnwindData |  |
| 14 | `BfsResealAndResumeBitLocker` | `0xF6A0` | 678 | UnwindData |  |
| 15 | `BfsResealBitLockerWithRetry` | `0xF950` | 1,095 | UnwindData |  |
| 12 | `BfsRegisterLogCallback` | `0x104E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `BfsUnregisterLogCallback` | `0x104F0` | 89,936 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `BsdSummarize` | `0x26440` | 784 | UnwindData |  |
