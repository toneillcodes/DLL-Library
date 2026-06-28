# Binary Specification: uexfat.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\uexfat.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8c8aad56715be695405ddf9db116024211668cec87837f6c5182f999955d4be2`
* **Total Exported Functions:** 36

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 12 | `Chkdsk` | `0x1FB0` | 553 | UnwindData |  |
| 13 | `ChkdskEx` | `0x21E0` | 1,849 | UnwindData |  |
| 14 | `Format` | `0x2920` | 667 | UnwindData |  |
| 15 | `FormatEx` | `0x2BD0` | 1,046 | UnwindData |  |
| 17 | `GetFilesystemInformation` | `0x2FF0` | 761 | UnwindData |  |
| 18 | `GetFsFormatOptions` | `0x32F0` | 79 | UnwindData |  |
| 31 | `Recover` | `0x3350` | 736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `??0EXFAT_VOL@@QEAA@XZ` | `0x3630` | 64 | UnwindData |  |
| 10 | `??1EXFAT_VOL@@UEAA@XZ` | `0x3680` | 51 | UnwindData |  |
| 23 | `?Initialize@EXFAT_VOL@@QEAA?AW4FORMAT_ERROR_CODE@@PEBVWSTRING@@PEAVMESSAGE@@EEW4_MEDIA_TYPE@@EEE@Z` | `0x3790` | 478 | UnwindData |  |
| 4 | `??0EXFAT_SA@@QEAA@XZ` | `0x4020` | 238 | UnwindData |  |
| 9 | `??1EXFAT_SA@@UEAA@XZ` | `0x4120` | 213 | UnwindData |  |
| 22 | `?Initialize@EXFAT_SA@@QEAAEPEAVLOG_IO_DP_DRIVE@@PEAVMESSAGE@@@Z` | `0x6580` | 215 | UnwindData |  |
| 2 | `??0EXFATDIR@@QEAA@XZ` | `0xFE10` | 80 | UnwindData |  |
| 7 | `??1EXFATDIR@@UEAA@XZ` | `0xFE70` | 53 | UnwindData |  |
| 20 | `?Initialize@EXFATDIR@@QEAAEPEAVHMEM@@PEAVLOG_IO_DP_DRIVE@@PEAVEXFAT_SA@@PEBVFAT@@K_KE@Z` | `0x10830` | 771 | UnwindData |  |
| 3 | `??0EXFAT_DIRENT@@QEAA@XZ` | `0x10C40` | 57 | UnwindData |  |
| 8 | `??1EXFAT_DIRENT@@UEAA@XZ` | `0x10C80` | 736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `?Initialize@EXFAT_DIRENT@@QEAAEPEAVEXFAT_SA@@PEAXPEAVEXFATDIR@@K@Z` | `0x10F60` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `?QueryFileSize@EXFAT_DIRENT@@QEAA_JXZ` | `0x111B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `?QueryStartingCluster@EXFAT_DIRENT@@QEAAKXZ` | `0x111C0` | 1,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `?SetFileSize@EXFAT_DIRENT@@QEAAE_J@Z` | `0x116E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `?SetStartingCluster@EXFAT_DIRENT@@QEAAEK@Z` | `0x11710` | 3,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `?VerifyAndFixPhase2@EXFAT_DIRENT@@QEAAEPEAVEXFATBITMAP@@0PEAVWSTRING@@EEEW4FIX_LEVEL@@PEAEPEAVMESSAGE@@@Z` | `0x12330` | 2,157 | UnwindData |  |
| 1 | `??0CLUSTER_CHAIN@@QEAA@XZ` | `0x13350` | 80 | UnwindData |  |
| 6 | `??1CLUSTER_CHAIN@@UEAA@XZ` | `0x133B0` | 44 | UnwindData |  |
| 19 | `?Initialize@CLUSTER_CHAIN@@QEAAEPEAVMEM@@PEAVLOG_IO_DP_DRIVE@@PEAVEXFAT_SA@@PEBVFAT@@KKE@Z` | `0x13560` | 766 | UnwindData |  |
| 29 | `?Read@CLUSTER_CHAIN@@UEAAEXZ` | `0x13870` | 114 | UnwindData |  |
| 30 | `?ReadAndRecordBadSectors@CLUSTER_CHAIN@@QEAAEPEAVEXFATSECRUNBITMAP@@@Z` | `0x138F0` | 512 | UnwindData |  |
| 35 | `?Write@CLUSTER_CHAIN@@UEAAEXZ` | `0x13B00` | 114 | UnwindData |  |
| 36 | `?WriteAndSkipBadSectors@CLUSTER_CHAIN@@QEAAEXZ` | `0x13B80` | 474 | UnwindData |  |
| 11 | `?AllocChain@FAT@@QEAAKPEAVEXFATBITMAP@@KPEAK@Z` | `0x13DF0` | 366 | UnwindData |  |
| 16 | `?FreeChain@FAT@@QEAAXPEAVEXFATBITMAP@@K@Z` | `0x13F70` | 166 | UnwindData |  |
| 24 | `?QueryAllocatedClusters@FAT@@QEBAKXZ` | `0x14120` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `?QueryLengthOfChain@FAT@@QEBAKKPEAK@Z` | `0x14160` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `?QueryNthCluster@FAT@@QEBAKKK@Z` | `0x141B0` | 1,104 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
