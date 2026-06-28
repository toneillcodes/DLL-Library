# Binary Specification: ufat.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ufat.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `35c47bb965336b799d7a661b1eb2f1c805602afe69b01920ca5cc2e52279ea4d`
* **Total Exported Functions:** 57

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `??0CLUSTER_CHAIN@@QEAA@XZ` | `0x8900` | 111 | UnwindData |  |
| 9 | `??1CLUSTER_CHAIN@@UEAA@XZ` | `0x8980` | 60 | UnwindData |  |
| 23 | `?Initialize@CLUSTER_CHAIN@@QEAAEPEAVMEM@@PEAVLOG_IO_DP_DRIVE@@PEAVFAT_SA@@PEBVFAT@@KK@Z` | `0x8B20` | 718 | UnwindData |  |
| 46 | `?Read@CLUSTER_CHAIN@@UEAAEXZ` | `0x8E00` | 120 | UnwindData |  |
| 51 | `?Write@CLUSTER_CHAIN@@UEAAEXZ` | `0x8E80` | 154 | UnwindData |  |
| 2 | `??0EA_HEADER@@QEAA@XZ` | `0x8F20` | 71 | UnwindData |  |
| 10 | `??1EA_HEADER@@UEAA@XZ` | `0x8F70` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `?Initialize@EA_HEADER@@QEAAEPEAVMEM@@PEAVLOG_IO_DP_DRIVE@@PEAVFAT_SA@@PEBVFAT@@KK@Z` | `0x9040` | 508 | UnwindData |  |
| 37 | `?QueryEaSetClusterNumber@EA_HEADER@@QEBAGG@Z` | `0x9250` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0EA_SET@@QEAA@XZ` | `0x92A0` | 100 | UnwindData |  |
| 11 | `??1EA_SET@@UEAA@XZ` | `0x9310` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `?GetEa@EA_SET@@QEAAPEAU_EA@@KPEAJPEAE@Z` | `0x93D0` | 399 | UnwindData |  |
| 25 | `?Initialize@EA_SET@@QEAAEPEAVMEM@@PEAVLOG_IO_DP_DRIVE@@PEAVFAT_SA@@PEBVFAT@@KK@Z` | `0x9570` | 508 | UnwindData |  |
| 47 | `?Read@EA_SET@@UEAAEXZ` | `0x9780` | 152 | UnwindData |  |
| 20 | `GetFsFormatOptions` | `0x9AE0` | 79 | UnwindData |  |
| 52 | `Chkdsk` | `0x9DD0` | 2,342 | UnwindData |  |
| 53 | `ChkdskEx` | `0xA700` | 3,450 | UnwindData |  |
| 54 | `Format` | `0xB480` | 984 | UnwindData |  |
| 55 | `FormatEx` | `0xB860` | 1,565 | UnwindData |  |
| 56 | `GetFilesystemInformation` | `0xBE90` | 1,092 | UnwindData |  |
| 57 | `Recover` | `0xC2E0` | 537 | UnwindData |  |
| 17 | `?AllocChain@FAT@@QEAAKKPEAK@Z` | `0xC5E0` | 190 | UnwindData |  |
| 18 | `?FreeChain@FAT@@QEAAXK@Z` | `0xC6B0` | 87 | UnwindData |  |
| 21 | `?Index12@FAT@@AEBAKK@Z` | `0xC710` | 1,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `?QueryAllocatedClusters@FAT@@QEBAKXZ` | `0xCB40` | 101 | UnwindData |  |
| 42 | `?QueryLengthOfChain@FAT@@QEBAKKPEAK@Z` | `0xCC80` | 121 | UnwindData |  |
| 45 | `?QueryNthCluster@FAT@@QEBAKKK@Z` | `0xCD00` | 62 | UnwindData |  |
| 50 | `?Set12@FAT@@AEAAXKK@Z` | `0xCFE0` | 98 | UnwindData |  |
| 4 | `??0FAT_DIRENT@@QEAA@XZ` | `0xD090` | 68 | UnwindData |  |
| 12 | `??1FAT_DIRENT@@UEAA@XZ` | `0xD0E0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `?Initialize@FAT_DIRENT@@QEAAEPEAX@Z` | `0xD180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `?Initialize@FAT_DIRENT@@QEAAEPEAXE@Z` | `0xD1A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `?IsValidCreationTime@FAT_DIRENT@@QEBAEXZ` | `0xD1E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `?IsValidLastAccessTime@FAT_DIRENT@@QEBAEXZ` | `0xD200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `?IsValidLastWriteTime@FAT_DIRENT@@QEBAEXZ` | `0xD220` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `?QueryCreationTime@FAT_DIRENT@@QEBAEPEAT_LARGE_INTEGER@@@Z` | `0xD3F0` | 230 | UnwindData |  |
| 40 | `?QueryLastAccessTime@FAT_DIRENT@@QEBAEPEAT_LARGE_INTEGER@@@Z` | `0xD4E0` | 124 | UnwindData |  |
| 41 | `?QueryLastWriteTime@FAT_DIRENT@@QEBAEPEAT_LARGE_INTEGER@@@Z` | `0xD570` | 174 | UnwindData |  |
| 44 | `?QueryName@FAT_DIRENT@@QEBAEPEAVWSTRING@@@Z` | `0xD6D0` | 819 | UnwindData |  |
| 43 | `?QueryLongName@FATDIR@@QEAAEJPEAVWSTRING@@@Z` | `0xE1A0` | 426 | UnwindData |  |
| 49 | `?SearchForDirEntry@FATDIR@@QEAAPEAXPEBVWSTRING@@@Z` | `0xE350` | 261 | UnwindData |  |
| 5 | `??0FAT_SA@@QEAA@XZ` | `0xE460` | 81 | UnwindData |  |
| 13 | `??1FAT_SA@@UEAA@XZ` | `0xE4C0` | 129 | UnwindData |  |
| 38 | `?QueryFileStartingCluster@FAT_SA@@QEAAKPEBVWSTRING@@PEAVHMEM@@PEAPEAVFATDIR@@PEAEPEAVFAT_DIRENT@@@Z` | `0xE860` | 958 | UnwindData |  |
| 35 | `?QueryCensusAndRelocate@FAT_SA@@QEAAEPEAU_CENSUS_REPORT@@PEAVINTSTACK@@PEAE@Z` | `0x1AF90` | 299 | UnwindData |  |
| 6 | `??0FILEDIR@@QEAA@XZ` | `0x1BE40` | 72 | UnwindData |  |
| 14 | `??1FILEDIR@@UEAA@XZ` | `0x1BE90` | 55 | UnwindData |  |
| 28 | `?Initialize@FILEDIR@@QEAAEPEAVMEM@@PEAVLOG_IO_DP_DRIVE@@PEAVFAT_SA@@PEBVFAT@@K@Z` | `0x1BF40` | 177 | UnwindData |  |
| 7 | `??0REAL_FAT_SA@@QEAA@XZ` | `0x1C180` | 161 | UnwindData |  |
| 15 | `??1REAL_FAT_SA@@UEAA@XZ` | `0x1C230` | 91 | UnwindData |  |
| 22 | `?InitFATChkDirty@REAL_FAT_SA@@QEAAEPEAVLOG_IO_DP_DRIVE@@PEAVMESSAGE@@@Z` | `0x1D650` | 807 | UnwindData |  |
| 29 | `?Initialize@REAL_FAT_SA@@UEAAEPEAVLOG_IO_DP_DRIVE@@PEAVMESSAGE@@E@Z` | `0x1D980` | 1,278 | UnwindData |  |
| 39 | `?QueryFreeSectors@REAL_FAT_SA@@QEBAKXZ` | `0x1E9B0` | 69 | UnwindData |  |
| 48 | `?Read@REAL_FAT_SA@@UEAAEPEAVMESSAGE@@@Z` | `0x1ECF0` | 2,292 | UnwindData |  |
| 8 | `??0ROOTDIR@@QEAA@XZ` | `0x22AB0` | 76 | UnwindData |  |
| 16 | `??1ROOTDIR@@UEAA@XZ` | `0x22B10` | 59 | UnwindData |  |
| 30 | `?Initialize@ROOTDIR@@QEAAEPEAVMEM@@PEAVLOG_IO_DP_DRIVE@@KJ@Z` | `0x22BF0` | 149 | UnwindData |  |
