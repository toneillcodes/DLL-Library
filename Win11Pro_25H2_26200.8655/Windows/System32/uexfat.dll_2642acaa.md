# Binary Specification: uexfat.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\uexfat.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2642acaa8d86a207517d5354c47b4f7164f4a90827f6f160639813b686dd63ee`
* **Total Exported Functions:** 36

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 12 | `Chkdsk` | `0x22E0` | 553 | UnwindData |  |
| 13 | `ChkdskEx` | `0x2510` | 1,849 | UnwindData |  |
| 14 | `Format` | `0x2C50` | 667 | UnwindData |  |
| 15 | `FormatEx` | `0x2F00` | 1,046 | UnwindData |  |
| 17 | `GetFilesystemInformation` | `0x3320` | 761 | UnwindData |  |
| 18 | `GetFsFormatOptions` | `0x3620` | 79 | UnwindData |  |
| 31 | `Recover` | `0x3680` | 736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `??0EXFAT_VOL@@QEAA@XZ` | `0x3960` | 64 | UnwindData |  |
| 10 | `??1EXFAT_VOL@@UEAA@XZ` | `0x39B0` | 51 | UnwindData |  |
| 23 | `?Initialize@EXFAT_VOL@@QEAA?AW4FORMAT_ERROR_CODE@@PEBVWSTRING@@PEAVMESSAGE@@EEW4_MEDIA_TYPE@@EEE@Z` | `0x3AC0` | 478 | UnwindData |  |
| 4 | `??0EXFAT_SA@@QEAA@XZ` | `0x4350` | 238 | UnwindData |  |
| 9 | `??1EXFAT_SA@@UEAA@XZ` | `0x4450` | 213 | UnwindData |  |
| 22 | `?Initialize@EXFAT_SA@@QEAAEPEAVLOG_IO_DP_DRIVE@@PEAVMESSAGE@@@Z` | `0x68B0` | 215 | UnwindData |  |
| 2 | `??0EXFATDIR@@QEAA@XZ` | `0x17890` | 80 | UnwindData |  |
| 7 | `??1EXFATDIR@@UEAA@XZ` | `0x178F0` | 53 | UnwindData |  |
| 20 | `?Initialize@EXFATDIR@@QEAAEPEAVHMEM@@PEAVLOG_IO_DP_DRIVE@@PEAVEXFAT_SA@@PEBVFAT@@K_KE@Z` | `0x182B0` | 771 | UnwindData |  |
| 3 | `??0EXFAT_DIRENT@@QEAA@XZ` | `0x186C0` | 57 | UnwindData |  |
| 8 | `??1EXFAT_DIRENT@@UEAA@XZ` | `0x18700` | 736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `?Initialize@EXFAT_DIRENT@@QEAAEPEAVEXFAT_SA@@PEAXPEAVEXFATDIR@@K@Z` | `0x189E0` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `?QueryFileSize@EXFAT_DIRENT@@QEAA_JXZ` | `0x18C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `?QueryStartingCluster@EXFAT_DIRENT@@QEAAKXZ` | `0x18C40` | 1,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `?SetFileSize@EXFAT_DIRENT@@QEAAE_J@Z` | `0x19160` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `?SetStartingCluster@EXFAT_DIRENT@@QEAAEK@Z` | `0x19190` | 3,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `?VerifyAndFixPhase2@EXFAT_DIRENT@@QEAAEPEAVEXFATBITMAP@@0PEAVWSTRING@@EEEW4FIX_LEVEL@@PEAEPEAVMESSAGE@@@Z` | `0x19DB0` | 2,157 | UnwindData |  |
| 1 | `??0CLUSTER_CHAIN@@QEAA@XZ` | `0x1ADD0` | 80 | UnwindData |  |
| 6 | `??1CLUSTER_CHAIN@@UEAA@XZ` | `0x1AE30` | 44 | UnwindData |  |
| 19 | `?Initialize@CLUSTER_CHAIN@@QEAAEPEAVMEM@@PEAVLOG_IO_DP_DRIVE@@PEAVEXFAT_SA@@PEBVFAT@@KKE@Z` | `0x1AFE0` | 766 | UnwindData |  |
| 29 | `?Read@CLUSTER_CHAIN@@UEAAEXZ` | `0x1B2F0` | 114 | UnwindData |  |
| 30 | `?ReadAndRecordBadSectors@CLUSTER_CHAIN@@QEAAEPEAVEXFATSECRUNBITMAP@@@Z` | `0x1B370` | 512 | UnwindData |  |
| 35 | `?Write@CLUSTER_CHAIN@@UEAAEXZ` | `0x1B580` | 114 | UnwindData |  |
| 36 | `?WriteAndSkipBadSectors@CLUSTER_CHAIN@@QEAAEXZ` | `0x1B600` | 474 | UnwindData |  |
| 11 | `?AllocChain@FAT@@QEAAKPEAVEXFATBITMAP@@KPEAK@Z` | `0x1B870` | 366 | UnwindData |  |
| 16 | `?FreeChain@FAT@@QEAAXPEAVEXFATBITMAP@@K@Z` | `0x1B9F0` | 166 | UnwindData |  |
| 24 | `?QueryAllocatedClusters@FAT@@QEBAKXZ` | `0x1BBA0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `?QueryLengthOfChain@FAT@@QEBAKKPEAK@Z` | `0x1BBE0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `?QueryNthCluster@FAT@@QEBAKKK@Z` | `0x1BC30` | 1,500 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
