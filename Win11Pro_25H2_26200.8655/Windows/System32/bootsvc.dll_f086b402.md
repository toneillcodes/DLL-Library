# Binary Specification: bootsvc.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\bootsvc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f086b402f5bd800b126aa6e3262ed5aac784d3cd470d2bdf66861148b03147fc`
* **Total Exported Functions:** 20

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `BfsCheckSystemPartition` | `0x1CD0` | 124 | UnwindData |  |
| 13 | `BfsRepairSystemPartition` | `0x1D60` | 1,013 | UnwindData |  |
| 2 | `BfsCleanupBcdStore` | `0x2F00` | 834 | UnwindData |  |
| 5 | `BfsInitializeBcdStore` | `0x3250` | 15 | UnwindData |  |
| 9 | `BfsMigrateLoaderSettings` | `0x36C0` | 731 | UnwindData |  |
| 19 | `BfsValidateBcdStore` | `0x39B0` | 460 | UnwindData |  |
| 3 | `BfsCreateOfflineBootstat` | `0x8CE0` | 530 | UnwindData |  |
| 10 | `BfsRedirectLogging` | `0x8F00` | 900 | UnwindData |  |
| 11 | `BfsReflectCurrentHypervisorLaunchType` | `0x9290` | 422 | UnwindData |  |
| 16 | `BfsServiceBootFiles` | `0x9440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `BfsServiceBootFilesEx` | `0x9460` | 23,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `BfsGetVolumeName` | `0xF000` | 336 | UnwindData |  |
| 6 | `BfsInitializeSystemVolume` | `0xF160` | 103 | UnwindData |  |
| 7 | `BfsIsBitLockerDisabled` | `0x10790` | 233 | UnwindData |  |
| 8 | `BfsIsBitLockerResealNeeded` | `0x10880` | 835 | UnwindData |  |
| 14 | `BfsResealAndResumeBitLocker` | `0x11430` | 668 | UnwindData |  |
| 15 | `BfsResealBitLockerWithRetry` | `0x116E0` | 1,203 | UnwindData |  |
| 12 | `BfsRegisterLogCallback` | `0x12520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `BfsUnregisterLogCallback` | `0x12530` | 90,352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `BsdSummarize` | `0x28620` | 784 | UnwindData |  |
