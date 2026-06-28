# Binary Specification: ufat.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ufat.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3bc42c4e022d6d42026bee6086ae39e175572de7b0bcafe926936916fb741a67`
* **Total Exported Functions:** 57

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `??0CLUSTER_CHAIN@@QEAA@XZ` | `0x24B0` | 111 | UnwindData |  |
| 9 | `??1CLUSTER_CHAIN@@UEAA@XZ` | `0x2530` | 60 | UnwindData |  |
| 23 | `?Initialize@CLUSTER_CHAIN@@QEAAEPEAVMEM@@PEAVLOG_IO_DP_DRIVE@@PEAVFAT_SA@@PEBVFAT@@KK@Z` | `0x26D0` | 718 | UnwindData |  |
| 46 | `?Read@CLUSTER_CHAIN@@UEAAEXZ` | `0x29B0` | 120 | UnwindData |  |
| 51 | `?Write@CLUSTER_CHAIN@@UEAAEXZ` | `0x2A30` | 154 | UnwindData |  |
| 2 | `??0EA_HEADER@@QEAA@XZ` | `0x2AD0` | 71 | UnwindData |  |
| 10 | `??1EA_HEADER@@UEAA@XZ` | `0x2B20` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `?Initialize@EA_HEADER@@QEAAEPEAVMEM@@PEAVLOG_IO_DP_DRIVE@@PEAVFAT_SA@@PEBVFAT@@KK@Z` | `0x2BF0` | 508 | UnwindData |  |
| 37 | `?QueryEaSetClusterNumber@EA_HEADER@@QEBAGG@Z` | `0x2E00` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0EA_SET@@QEAA@XZ` | `0x2E50` | 100 | UnwindData |  |
| 11 | `??1EA_SET@@UEAA@XZ` | `0x2EC0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `?GetEa@EA_SET@@QEAAPEAU_EA@@KPEAJPEAE@Z` | `0x2F80` | 399 | UnwindData |  |
| 25 | `?Initialize@EA_SET@@QEAAEPEAVMEM@@PEAVLOG_IO_DP_DRIVE@@PEAVFAT_SA@@PEBVFAT@@KK@Z` | `0x3120` | 508 | UnwindData |  |
| 47 | `?Read@EA_SET@@UEAAEXZ` | `0x3330` | 152 | UnwindData |  |
| 20 | `GetFsFormatOptions` | `0x3690` | 79 | UnwindData |  |
| 52 | `Chkdsk` | `0x39F0` | 2,342 | UnwindData |  |
| 53 | `ChkdskEx` | `0x4320` | 3,450 | UnwindData |  |
| 54 | `Format` | `0x50A0` | 984 | UnwindData |  |
| 55 | `FormatEx` | `0x5480` | 1,565 | UnwindData |  |
| 56 | `GetFilesystemInformation` | `0x5AB0` | 1,092 | UnwindData |  |
| 57 | `Recover` | `0x5F00` | 537 | UnwindData |  |
| 17 | `?AllocChain@FAT@@QEAAKKPEAK@Z` | `0x6200` | 190 | UnwindData |  |
| 18 | `?FreeChain@FAT@@QEAAXK@Z` | `0x62D0` | 87 | UnwindData |  |
| 21 | `?Index12@FAT@@AEBAKK@Z` | `0x6330` | 1,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `?QueryAllocatedClusters@FAT@@QEBAKXZ` | `0x6760` | 101 | UnwindData |  |
| 42 | `?QueryLengthOfChain@FAT@@QEBAKKPEAK@Z` | `0x68A0` | 121 | UnwindData |  |
| 45 | `?QueryNthCluster@FAT@@QEBAKKK@Z` | `0x6920` | 62 | UnwindData |  |
| 50 | `?Set12@FAT@@AEAAXKK@Z` | `0x6C00` | 98 | UnwindData |  |
| 4 | `??0FAT_DIRENT@@QEAA@XZ` | `0x6CB0` | 68 | UnwindData |  |
| 12 | `??1FAT_DIRENT@@UEAA@XZ` | `0x6D00` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `?Initialize@FAT_DIRENT@@QEAAEPEAX@Z` | `0x6DA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `?Initialize@FAT_DIRENT@@QEAAEPEAXE@Z` | `0x6DC0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `?IsValidCreationTime@FAT_DIRENT@@QEBAEXZ` | `0x6E00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `?IsValidLastAccessTime@FAT_DIRENT@@QEBAEXZ` | `0x6E20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `?IsValidLastWriteTime@FAT_DIRENT@@QEBAEXZ` | `0x6E40` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `?QueryCreationTime@FAT_DIRENT@@QEBAEPEAT_LARGE_INTEGER@@@Z` | `0x7010` | 230 | UnwindData |  |
| 40 | `?QueryLastAccessTime@FAT_DIRENT@@QEBAEPEAT_LARGE_INTEGER@@@Z` | `0x7100` | 124 | UnwindData |  |
| 41 | `?QueryLastWriteTime@FAT_DIRENT@@QEBAEPEAT_LARGE_INTEGER@@@Z` | `0x7190` | 174 | UnwindData |  |
| 44 | `?QueryName@FAT_DIRENT@@QEBAEPEAVWSTRING@@@Z` | `0x72F0` | 819 | UnwindData |  |
| 43 | `?QueryLongName@FATDIR@@QEAAEJPEAVWSTRING@@@Z` | `0x7DC0` | 426 | UnwindData |  |
| 49 | `?SearchForDirEntry@FATDIR@@QEAAPEAXPEBVWSTRING@@@Z` | `0x7F70` | 261 | UnwindData |  |
| 5 | `??0FAT_SA@@QEAA@XZ` | `0x8080` | 81 | UnwindData |  |
| 13 | `??1FAT_SA@@UEAA@XZ` | `0x80E0` | 129 | UnwindData |  |
| 38 | `?QueryFileStartingCluster@FAT_SA@@QEAAKPEBVWSTRING@@PEAVHMEM@@PEAPEAVFATDIR@@PEAEPEAVFAT_DIRENT@@@Z` | `0x8480` | 958 | UnwindData |  |
| 35 | `?QueryCensusAndRelocate@FAT_SA@@QEAAEPEAU_CENSUS_REPORT@@PEAVINTSTACK@@PEAE@Z` | `0x14BD0` | 299 | UnwindData |  |
| 6 | `??0FILEDIR@@QEAA@XZ` | `0x15A80` | 72 | UnwindData |  |
| 14 | `??1FILEDIR@@UEAA@XZ` | `0x15AD0` | 55 | UnwindData |  |
| 28 | `?Initialize@FILEDIR@@QEAAEPEAVMEM@@PEAVLOG_IO_DP_DRIVE@@PEAVFAT_SA@@PEBVFAT@@K@Z` | `0x15B80` | 177 | UnwindData |  |
| 7 | `??0REAL_FAT_SA@@QEAA@XZ` | `0x15D90` | 161 | UnwindData |  |
| 15 | `??1REAL_FAT_SA@@UEAA@XZ` | `0x15E40` | 91 | UnwindData |  |
| 22 | `?InitFATChkDirty@REAL_FAT_SA@@QEAAEPEAVLOG_IO_DP_DRIVE@@PEAVMESSAGE@@@Z` | `0x16DA0` | 807 | UnwindData |  |
| 29 | `?Initialize@REAL_FAT_SA@@UEAAEPEAVLOG_IO_DP_DRIVE@@PEAVMESSAGE@@E@Z` | `0x170D0` | 1,278 | UnwindData |  |
| 39 | `?QueryFreeSectors@REAL_FAT_SA@@QEBAKXZ` | `0x180A0` | 69 | UnwindData |  |
| 48 | `?Read@REAL_FAT_SA@@UEAAEPEAVMESSAGE@@@Z` | `0x182F0` | 2,292 | UnwindData |  |
| 8 | `??0ROOTDIR@@QEAA@XZ` | `0x1B910` | 76 | UnwindData |  |
| 16 | `??1ROOTDIR@@UEAA@XZ` | `0x1B970` | 59 | UnwindData |  |
| 30 | `?Initialize@ROOTDIR@@QEAAEPEAVMEM@@PEAVLOG_IO_DP_DRIVE@@KJ@Z` | `0x1BA50` | 149 | UnwindData |  |
