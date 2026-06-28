# Binary Specification: ifsutil.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ifsutil.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `16f123a2b7afa44a19af3a115166468ae2f253d8bc18edf50db16529e5e9e052`
* **Total Exported Functions:** 329

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 314 | `?Verify@IO_DP_DRIVE@@QEAAEVBIG_INT@@0PEAVNUMBER_SET@@@Z` | `0x1010` | 751 | UnwindData |  |
| 313 | `?Verify@IO_DP_DRIVE@@QEAAEVBIG_INT@@0@Z` | `0x1310` | 332 | UnwindData |  |
| 149 | `?Initialize@VOL_LIODPDRV@@IEAA?AW4FORMAT_ERROR_CODE@@PEBVWSTRING@@PEAVSUPERAREA@@PEAVMESSAGE@@EEW4_MEDIA_TYPE@@GEIEE@Z` | `0x14E0` | 1,472 | UnwindData |  |
| 203 | `?QueryFileSystemName@IFS_SYSTEM@@SAEPEBVWSTRING@@PEAV2@PEAJ1@Z` | `0x1C10` | 305 | UnwindData |  |
| 48 | `?AddDriveName@MOUNT_POINT_MAP@@QEAAEPEAVWSTRING@@0@Z` | `0x1D50` | 369 | UnwindData |  |
| 130 | `?Initialize@INTSTACK@@QEAAEXZ` | `0x27B0` | 64 | UnwindData |  |
| 30 | `??1DP_DRIVE@@UEAA@XZ` | `0x2890` | 56 | UnwindData |  |
| 31 | `??1INTSTACK@@UEAA@XZ` | `0x28D0` | 87 | UnwindData |  |
| 7 | `??0LOG_IO_DP_DRIVE@@QEAA@XZ` | `0x2B00` | 56 | UnwindData |  |
| 5 | `??0DP_DRIVE@@QEAA@XZ` | `0x2BF0` | 207 | UnwindData |  |
| 136 | `?Initialize@MOUNT_POINT_MAP@@QEAAEXZ` | `0x2F10` | 104 | UnwindData |  |
| 51 | `?AddVolumeName@MOUNT_POINT_MAP@@QEAAEPEAVWSTRING@@0@Z` | `0x30D0` | 366 | UnwindData |  |
| 10 | `??0MOUNT_POINT_TUPLE@@QEAA@XZ` | `0x3280` | 118 | UnwindData |  |
| 33 | `??1MOUNT_POINT_MAP@@UEAA@XZ` | `0x5020` | 44 | UnwindData |  |
| 225 | `?QueryNtfsSupportInfo@DP_DRIVE@@SAJPEAXPEAE@Z` | `0x5240` | 382 | UnwindData |  |
| 82 | `?EliminateCycles@DIGRAPH@@QEAAEPEAVCONTAINER@@PEAE@Z` | `0x58A0` | 312 | UnwindData |  |
| 137 | `?Initialize@NUMBER_SET@@QEAAEXZ` | `0x5DD0` | 158 | UnwindData |  |
| 56 | `?CheckAndAdd@NUMBER_SET@@QEAAEVBIG_INT@@PEAE@Z` | `0x5E80` | 429 | UnwindData |  |
| 11 | `??0NUMBER_SET@@QEAA@XZ` | `0x6040` | 71 | UnwindData |  |
| 321 | `?WriteEntireDrive@VOL_LIODPDRV@@UEAA?AW4FORMAT_ERROR_CODE@@PEAVMESSAGE@@PEAXKII@Z` | `0x64A0` | 794 | UnwindData |  |
| 122 | `?HardRead@IO_DP_DRIVE@@QEAAEVBIG_INT@@KPEAX@Z` | `0x67E0` | 30 | UnwindData |  |
| 123 | `?HardWrite@IO_DP_DRIVE@@QEAAEVBIG_INT@@KPEAXE@Z` | `0x69D0` | 94 | UnwindData |  |
| 315 | `?VerifyRead@IO_DP_DRIVE@@QEAAEVBIG_INT@@KPEAX@Z` | `0x7EF0` | 47 | UnwindData |  |
| 316 | `?VerifyRead@SECRUN@@UEAAEPEAE@Z` | `0x7F30` | 184 | UnwindData |  |
| 238 | `?QueryProcessPrivateMemory@IFS_SYSTEM@@SAEPEAXPEA_K@Z` | `0x8B40` | 192 | UnwindData |  |
| 45 | `?Add@NUMBER_SET@@QEAAEVBIG_INT@@@Z` | `0x9DA0` | 415 | UnwindData |  |
| 79 | `?DoesIntersectSet@NUMBER_SET@@QEBAEVBIG_INT@@0@Z` | `0x9F80` | 199 | UnwindData |  |
| 193 | `?QueryContainingRange@NUMBER_SET@@QEBAEVBIG_INT@@PEAV2@1@Z` | `0xA1B0` | 153 | UnwindData |  |
| 300 | `?SetPhaseSubPhase@DRIVE_CACHE@@SAXPEAG0@Z` | `0xA2B0` | 164 | UnwindData |  |
| 114 | `?GetPhaseSubPhase@DRIVE_CACHE@@SAXPEAPEAG0@Z` | `0xA360` | 117 | UnwindData |  |
| 227 | `?QueryNtfsVersion@IFS_SYSTEM@@SAEPEAE0PEAVLOG_IO_DP_DRIVE@@PEAX@Z` | `0xA3E0` | 698 | UnwindData |  |
| 21 | `??0SUPERAREA@@IEAA@XZ` | `0xA6A0` | 61 | UnwindData |  |
| 18 | `??0SECRUN@@QEAA@XZ` | `0xA6F0` | 80 | UnwindData |  |
| 240 | `?QueryReadAndVerifiedUsage@IO_DP_DRIVE@@QEAAXPEA_K0@Z` | `0xA750` | 73 | UnwindData |  |
| 49 | `?AddEdge@DIGRAPH@@QEAAEKK@Z` | `0xA7A0` | 331 | UnwindData |  |
| 44 | `?Add@NUMBER_SET@@QEAAEVBIG_INT@@0@Z` | `0xA900` | 467 | UnwindData |  |
| 280 | `?RemoveAll@NUMBER_SET@@QEAAEXZ` | `0xAAE0` | 110 | UnwindData |  |
| 58 | `?CheckAndRemove@NUMBER_SET@@QEAAEVBIG_INT@@PEAE@Z` | `0xAF10` | 368 | UnwindData |  |
| 291 | `?Set@BIG_INT@@QEAAXEPEBE@Z` | `0xB090` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `?Push@INTSTACK@@QEAAEVBIG_INT@@@Z` | `0xB0D0` | 114 | UnwindData |  |
| 177 | `?Pop@INTSTACK@@QEAAXK@Z` | `0xB150` | 16 | UnwindData |  |
| 34 | `??1NUMBER_SET@@UEAA@XZ` | `0xB1C0` | 131 | UnwindData |  |
| 269 | `?Read@IO_DP_DRIVE@@QEAAEVBIG_INT@@KPEAX@Z` | `0xB670` | 46 | UnwindData |  |
| 35 | `??1SECRUN@@UEAA@XZ` | `0xB7D0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 278 | `?Remove@NUMBER_SET@@QEAAEVBIG_INT@@@Z` | `0xB820` | 359 | UnwindData |  |
| 277 | `?Remove@NUMBER_SET@@QEAAEVBIG_INT@@0@Z` | `0xB990` | 420 | UnwindData |  |
| 6 | `??0INTSTACK@@QEAA@XZ` | `0xBB40` | 72 | UnwindData |  |
| 245 | `?QuerySectorSize@DP_DRIVE@@UEBAKXZ` | `0xBB90` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 253 | `?QuerySystemMemory@IFS_SYSTEM@@SAEPEAKPEA_K11@Z` | `0xBDC0` | 325 | UnwindData |  |
| 46 | `?Add@SPARSE_SET@@QEAAEPEBV1@@Z` | `0xBF40` | 120 | UnwindData |  |
| 47 | `?Add@SPARSE_SET@@QEAAEVBIG_INT@@@Z` | `0xBFC0` | 277 | UnwindData |  |
| 194 | `?QueryCorruptionState@IFS_SYSTEM@@SAEPEAVWSTRING@@PEAKPEAEPEAJ@Z` | `0xC0E0` | 565 | UnwindData |  |
| 144 | `?Initialize@SECRUN@@QEAAEPEAVMEM@@PEAVIO_DP_DRIVE@@VBIG_INT@@K@Z` | `0xC320` | 128 | UnwindData |  |
| 230 | `?QueryNumber@NUMBER_SET@@QEBA?AVBIG_INT@@V2@@Z` | `0xC3B0` | 145 | UnwindData |  |
| 59 | `?CheckAndRemove@SPARSE_SET@@QEAAEVBIG_INT@@PEAE@Z` | `0xC450` | 238 | UnwindData |  |
| 143 | `?Initialize@READ_WRITE_CACHE@@QEAAEPEAVIO_DP_DRIVE@@KE@Z` | `0xC7B0` | 554 | UnwindData |  |
| 176 | `?NtDriveNameToDosDriveName@IFS_SYSTEM@@SAEPEBVWSTRING@@PEAV2@@Z` | `0xCA50` | 705 | UnwindData |  |
| 326 | `QueryPersistRegistryKeyValueWithFallback` | `0xCD20` | 330 | UnwindData |  |
| 96 | `?GetAt@MOUNT_POINT_MAP@@QEAAEKPEAVWSTRING@@0@Z` | `0xCE70` | 127 | UnwindData |  |
| 241 | `?QueryReadCacheSize@DP_DRIVE@@UEAAJPEA_K@Z` | `0xCF00` | 539 | UnwindData |  |
| 64 | `?CleanupBackingStore@WRITEVIEW_BACKINGSTORE@@SAEPEAVWSTRING@@@Z` | `0xD130` | 1,076 | UnwindData |  |
| 287 | `?SendSonyMSInquiryCmd@DP_DRIVE@@QEAAEPEAUSONY_MS_INQUIRY_DATA@@@Z` | `0xD570` | 136 | UnwindData |  |
| 164 | `?IsMember@INTSTACK@@QEBAEVBIG_INT@@@Z` | `0xD9C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 270 | `?Read@SECRUN@@UEAAEXZ` | `0xD9E0` | 59 | UnwindData |  |
| 9 | `??0MOUNT_POINT_MAP@@QEAA@XZ` | `0xDAB0` | 68 | UnwindData |  |
| 174 | `?Look@INTSTACK@@QEBA?AVBIG_INT@@K@Z` | `0xDB00` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 233 | `?QueryParents@DIGRAPH@@QEBAEKPEAVNUMBER_SET@@@Z` | `0xDB40` | 244 | UnwindData |  |
| 147 | `?Initialize@SUPERAREA@@IEAAEPEAVMEM@@PEAVLOG_IO_DP_DRIVE@@KPEAVMESSAGE@@@Z` | `0xDC40` | 221 | UnwindData |  |
| 247 | `?QuerySectors@DP_DRIVE@@UEBA?AVBIG_INT@@XZ` | `0xDD30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 165 | `?IsThinlyProvisioned@DP_DRIVE@@QEAAEXZ` | `0xDD50` | 313 | UnwindData |  |
| 80 | `?DosDriveNameToNtDriveName@IFS_SYSTEM@@SAEPEBVWSTRING@@PEAV2@@Z` | `0xDFD0` | 334 | UnwindData |  |
| 319 | `?Write@IO_DP_DRIVE@@QEAAEVBIG_INT@@KPEAX@Z` | `0xE180` | 46 | UnwindData |  |
| 226 | `?QueryNtfsTime@IFS_SYSTEM@@SAXPEAT_LARGE_INTEGER@@@Z` | `0xE1C0` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 320 | `?Write@SECRUN@@UEAAEXZ` | `0xE470` | 59 | UnwindData |  |
| 62 | `?CheckValidSecurityDescriptor@IFS_SYSTEM@@SAEKPEAU_SECURITY_DESCRIPTOR@@@Z` | `0xE9E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `??1LOG_IO_DP_DRIVE@@UEAA@XZ` | `0xEA00` | 1,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `?Prefetch@IO_DP_DRIVE@@QEAAEVBIG_INT@@K@Z` | `0xEE00` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `??1SUPERAREA@@UEAA@XZ` | `0xEE90` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `?CheckLinkList@TLINK@@QEAAXXZ` | `0xF0F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `?DumpHashTable@SPARSE_SET@@QEAAXXZ` | `0xF0F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 180 | `?Purge@WRITEVIEW_CACHE@@QEAAXVBIG_INT@@K@Z` | `0xF0F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 312 | `?TraverseLinkList@TLINK@@QEAAXXZ` | `0xF0F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | `?QueryDriveType@DP_DRIVE@@QEBA?AW4DRIVE_TYPE@@XZ` | `0xF100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `?IsDax@IO_DP_DRIVE@@QEAAEXZ` | `0xF110` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `??1WRITEVIEW_CACHE_ENTRY@@QEAA@XZ` | `0xF1B0` | 216 | UnwindData |  |
| 169 | `?IsUdfMediaWritable@DP_DRIVE@@QEAAEXZ` | `0xF290` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `?Initialize@LOG_IO_DP_DRIVE@@QEAAEPEAXE@Z` | `0xF4C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 195 | `?QueryDataRedundancyCount@DP_DRIVE@@UEAAJPEAK0@Z` | `0xF4D0` | 288 | UnwindData |  |
| 95 | `?GenerateLabelNotification@SUPERAREA@@SAJPEBVWSTRING@@PEAV2@PEAU_FILE_FS_SIZE_INFORMATION@@PEAU_FILE_FS_VOLUME_INFORMATION@@@Z` | `0xF600` | 837 | UnwindData |  |
| 237 | `?QueryPhysicalSectorSize@DP_DRIVE@@QEAAKXZ` | `0xF950` | 1,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 279 | `?Remove@WRITEVIEW_CACHE@@QEAAXPEAVWRITEVIEW_CACHE_ENTRY@@@Z` | `0xFE00` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 235 | `?QueryPartitionInfo@DP_DRIVE@@UEAAEPEAU_PARTITION_INFORMATION_EX@@@Z` | `0xFE70` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 192 | `?QueryCompressedInteger@BIG_INT@@QEBAXPEAE0@Z` | `0x10000` | 1,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 282 | `?RemoveEdge@DIGRAPH@@QEAAEKK@Z` | `0x10540` | 227 | UnwindData |  |
| 25 | `??0WRITEVIEW_CACHE_ENTRY@@QEAA@PEAVWRITEVIEW_CACHE@@G@Z` | `0x10630` | 193 | UnwindData |  |
| 187 | `?QueryCacheSize@WRITEVIEW_CACHE@@UEAAXPEA_K0@Z` | `0x10700` | 1,776 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `??0DIGRAPH_EDGE@@QEAA@XZ` | `0x10DF0` | 78 | UnwindData |  |
| 128 | `?Initialize@DP_DRIVE@@QEAAEPEBVWSTRING@@PEAVMESSAGE@@EE@Z` | `0x11020` | 34 | UnwindData |  |
| 199 | `?QueryDriveHandle@DP_DRIVE@@QEBAPEAXXZ` | `0x11080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `?GetPerfFreq@BLOCK_CACHE@@QEAA_KXZ` | `0x11090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 259 | `?QueryUdfMediaNeedsVat@DP_DRIVE@@QEAAEXZ` | `0x110A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 262 | `?QueryUdfMediaType@DP_DRIVE@@QEAAKXZ` | `0x110C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 211 | `?QueryHotPlugInfo@DP_DRIVE@@QEBAEXZ` | `0x110D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `?Initialize@LOG_IO_DP_DRIVE@@QEAAEPEBVWSTRING@@PEAVMESSAGE@@E@Z` | `0x110E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 220 | `?QueryMemoryLimit@IO_DP_DRIVE@@QEAAEPEA_KPEAE@Z` | `0x110F0` | 3,504 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `?CreateTrack@MEDIA_TRACK_INFORMATION@@QEAAPEAV1@KE@Z` | `0x11EA0` | 211 | UnwindData |  |
| 98 | `?GetBuffer@TLINK@@QEAAPEAXPEAX@Z` | `0x11F80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `?GetData@TLINK@@QEAAAEAVBIG_INT@@G@Z` | `0x11F90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `?GetData@TLINK@@QEAAAEAVBIG_INT@@PEAX@Z` | `0x11FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `?GetDrive@SECRUN@@QEAAPEAVIO_DP_DRIVE@@XZ` | `0x11FD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `?GetDrive@SUPERAREA@@QEAAPEAVIO_DP_DRIVE@@XZ` | `0x11FE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `?GetFirst@TLINK@@QEAAPEAXXZ` | `0x11FF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `?GetIoErrorDisplayFlags@IO_DP_DRIVE@@QEBAKXZ` | `0x12010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `?GetMessageW@IO_DP_DRIVE@@QEAAPEAVMESSAGE@@XZ` | `0x12020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `?GetMessageW@SUPERAREA@@QEAAPEAVMESSAGE@@XZ` | `0x12030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `?GetNext@TLINK@@QEAAPEAXPEAX@Z` | `0x12050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `?GetSortedFirst@TLINK@@QEAAPEAXXZ` | `0x12060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `?GetSortedNext@TLINK@@QEAAPEAXPEAX@Z` | `0x12080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `?Initialize@MEDIA_TRACK_INFORMATION_SORTED_BY_SIZE@@QEAAXPEAVMEDIA_TRACK_INFORMATION@@@Z` | `0x12090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 163 | `?IsLocked@IO_DP_DRIVE@@QEAAEXZ` | `0x120A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 219 | `?QueryMemberCount@TLINK@@QEBAGXZ` | `0x120B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 242 | `?QueryReadUsage@IO_DP_DRIVE@@QEAAXPEA_K0@Z` | `0x120C0` | 63 | UnwindData |  |
| 249 | `?QuerySize@TLINK@@QEBAGXZ` | `0x12110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 268 | `?QueryWriteUsage@IO_DP_DRIVE@@QEAAXPEA_K0@Z` | `0x12120` | 63 | UnwindData |  |
| 296 | `?SetIoErrorDisplayFlags@IO_DP_DRIVE@@QEAAXK@Z` | `0x12170` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 298 | `?SetLastStatus@DP_DRIVE@@QEAAXJ@Z` | `0x12180` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 307 | `?Sort@TLINK@@QEAAXXZ` | `0x12190` | 57 | UnwindData |  |
| 329 | `WritePersistRegistryKeyValue` | `0x122D0` | 226 | UnwindData |  |
| 50 | `?AddEntry@AUTOREG@@SAEPEBVWSTRING@@@Z` | `0x123C0` | 244 | UnwindData |  |
| 72 | `?DeleteEntry@AUTOREG@@SAEPEBVWSTRING@@00@Z` | `0x124C0` | 701 | UnwindData |  |
| 73 | `?DeleteEntry@AUTOREG@@SAEPEBVWSTRING@@0@Z` | `0x12790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `?DeleteEntry@AUTOREG@@SAEPEBVWSTRING@@E@Z` | `0x127A0` | 459 | UnwindData |  |
| 158 | `?IsEntryPresent@AUTOREG@@SAEPEBVWSTRING@@0@Z` | `0x12980` | 400 | UnwindData |  |
| 159 | `?IsEntryPresent@AUTOREG@@SAEPEBVWSTRING@@@Z` | `0x12B20` | 218 | UnwindData |  |
| 162 | `?IsFrontEndPresent@AUTOREG@@SAEPEBVWSTRING@@0@Z` | `0x12C00` | 559 | UnwindData |  |
| 182 | `?PushEntry@AUTOREG@@SAEPEBVWSTRING@@@Z` | `0x12E40` | 260 | UnwindData |  |
| 2 | `??0CANNED_SECURITY@@QEAA@XZ` | `0x13210` | 141 | UnwindData |  |
| 28 | `??1CANNED_SECURITY@@UEAA@XZ` | `0x132B0` | 44 | UnwindData |  |
| 100 | `?GetCannedSecurityDescriptor@CANNED_SECURITY@@QEAAPEAXW4_CANNED_SECURITY_TYPE@@PEAK@Z` | `0x14CA0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `?Initialize@CANNED_SECURITY@@QEAAEXZ` | `0x14D80` | 1,016 | UnwindData |  |
| 1 | `??0BLOCK_CACHE@@QEAA@XZ` | `0x156A0` | 100 | UnwindData |  |
| 27 | `??1BLOCK_CACHE@@UEAA@XZ` | `0x15830` | 84 | UnwindData |  |
| 52 | `?AdjustCacheSize@BLOCK_CACHE@@UEAAXPEA_K0@Z` | `0x15AB0` | 291 | UnwindData |  |
| 83 | `?EnableFileSystem@IFS_SYSTEM@@SAEPEBVWSTRING@@@Z` | `0x15C80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `?Initialize@BLOCK_CACHE@@QEAAEPEAVIO_DP_DRIVE@@@Z` | `0x15C90` | 630 | UnwindData |  |
| 185 | `?QueryCacheSize@BLOCK_CACHE@@UEAAXPEA_K0@Z` | `0x15F10` | 131 | UnwindData |  |
| 308 | `?SqmExport@BLOCK_CACHE@@UEAAEP6AEPEAXKEPEADZZ0@Z` | `0x15FE0` | 1,466 | UnwindData |  |
| 323 | `GetDefaultFileSystemIfs` | `0x16840` | 1,899 | UnwindData |  |
| 3 | `??0DIGRAPH@@QEAA@XZ` | `0x16FC0` | 107 | UnwindData |  |
| 29 | `??1DIGRAPH@@UEAA@XZ` | `0x17040` | 92 | UnwindData |  |
| 126 | `?Initialize@DIGRAPH@@QEAAEK@Z` | `0x17380` | 147 | UnwindData |  |
| 189 | `?QueryChildren@DIGRAPH@@QEBAEKPEAVNUMBER_SET@@@Z` | `0x17420` | 209 | UnwindData |  |
| 228 | `?QueryNumChildren@DIGRAPH@@QEBAKK@Z` | `0x17500` | 126 | UnwindData |  |
| 229 | `?QueryNumParents@DIGRAPH@@QEBAKK@Z` | `0x17590` | 211 | UnwindData |  |
| 234 | `?QueryParentsWithChildren@DIGRAPH@@QEBAEPEAVNUMBER_SET@@K@Z` | `0x17670` | 265 | UnwindData |  |
| 284 | `?SearchForMatch@DIGRAPH@@QEAAEKPEAVBITVECTOR@@PEAVNUMBER_SET@@PEAEPEAVBIG_INT@@@Z` | `0x17780` | 242 | UnwindData |  |
| 53 | `?AdjustCacheSize@IO_DP_DRIVE@@QEAAXPEA_K0@Z` | `0x17940` | 34 | UnwindData |  |
| 65 | `?ClearMachineSpecificFileSystemState@DP_DRIVE@@QEAAKXZ` | `0x17970` | 325 | UnwindData |  |
| 66 | `?CloseDriveHandle@DP_DRIVE@@QEAAXXZ` | `0x17AC0` | 74 | UnwindData |  |
| 68 | `?CreateFileSystemRegistryKey@DP_DRIVE@@QEAAKKW4_FMIFS_CREATE_PMFSS_FLAGS@@PEAU_GUID@@PEAPEAUHKEY__@@@Z` | `0x17E30` | 156 | UnwindData |  |
| 77 | `?DismountAndLock@IO_DP_DRIVE@@QEAAEXZ` | `0x17F60` | 121 | UnwindData |  |
| 90 | `?FlushCache@IO_DP_DRIVE@@QEAAEXZ` | `0x18060` | 1,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `?Initialize@DP_DRIVE@@QEAAEPEBVWSTRING@@0PEAVMESSAGE@@EE@Z` | `0x18490` | 796 | UnwindData |  |
| 132 | `?Initialize@LOG_IO_DP_DRIVE@@QEAAEPEBVWSTRING@@0PEAVMESSAGE@@E@Z` | `0x18880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `?InvalidateVolume@IO_DP_DRIVE@@QEAAEXZ` | `0x18890` | 342 | UnwindData |  |
| 156 | `?IsBootCriticalVolume@DP_DRIVE@@QEAAEXZ` | `0x189F0` | 264 | UnwindData |  |
| 172 | `?IssueDeleteNotification@IO_DP_DRIVE@@QEAAE_KK@Z` | `0x18B40` | 364 | UnwindData |  |
| 173 | `?Lock@IO_DP_DRIVE@@QEAAEXZ` | `0x18CC0` | 212 | UnwindData |  |
| 184 | `?QueryBusType@DP_DRIVE@@UEAAEPEAW4_STORAGE_BUS_TYPE@@@Z` | `0x18F80` | 237 | UnwindData |  |
| 186 | `?QueryCacheSize@IO_DP_DRIVE@@QEAAXPEA_K0@Z` | `0x19080` | 52 | UnwindData |  |
| 212 | `?QueryID@DP_DRIVE@@QEAAEPEAU_GUID@@PEBVWSTRING@@E@Z` | `0x19170` | 991 | UnwindData |  |
| 213 | `?QueryID@DP_DRIVE@@QEAAEPEAVWSTRING@@PEBV2@E@Z` | `0x19560` | 200 | UnwindData |  |
| 218 | `?QueryMediaByte@DP_DRIVE@@QEBAEXZ` | `0x19630` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `?QueryMrwSupport@DP_DRIVE@@SAEPEAX@Z` | `0x196B0` | 267 | UnwindData |  |
| 223 | `?QueryNativeNVMe@DP_DRIVE@@UEAAEPEAE@Z` | `0x197D0` | 241 | UnwindData |  |
| 243 | `?QueryRecommendedMediaType@DP_DRIVE@@QEBA?AW4_MEDIA_TYPE@@XZ` | `0x198D0` | 100 | UnwindData |  |
| 244 | `?QueryRewritableMOSupport@DP_DRIVE@@QEAAEXZ` | `0x19940` | 293 | UnwindData |  |
| 255 | `?QueryTierCount@DP_DRIVE@@UEAAJPEAK@Z` | `0x19A70` | 376 | UnwindData |  |
| 263 | `?QueryVerifyHandle@IO_DP_DRIVE@@QEAAPEAXXZ` | `0x19BF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 267 | `?QueryWriteBlockSize@DP_DRIVE@@UEBAKXZ` | `0x19C00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 273 | `?ReinitializeDriveParameters@DP_DRIVE@@QEAAEPEAVMESSAGE@@@Z` | `0x19C10` | 77 | UnwindData |  |
| 293 | `?SetCache@IO_DP_DRIVE@@QEAAXPEAVDRIVE_CACHE@@@Z` | `0x19C70` | 63 | UnwindData |  |
| 294 | `?SetDaxAttribute@IO_DP_DRIVE@@QEAA?AW4FORMAT_ERROR_CODE@@E@Z` | `0x19CC0` | 1,324 | UnwindData |  |
| 302 | `?SetSectors@DP_DRIVE@@QEAAXVBIG_INT@@@Z` | `0x1A2E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 303 | `?SetSystemId@LOG_IO_DP_DRIVE@@QEAAEE@Z` | `0x1A2F0` | 209 | UnwindData |  |
| 304 | `?SetVerifyHandle@IO_DP_DRIVE@@QEAAPEAXPEAX@Z` | `0x1A3D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 309 | `?SqmExport@IO_DP_DRIVE@@QEAAEPEBVWSTRING@@P6AEPEAXKEPEADZZ1@Z` | `0x1A3E0` | 1,148 | UnwindData |  |
| 327 | `RegisterExtensionCallbacks` | `0x1B1D0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 324 | `InvalidateFve` | `0x1B2D0` | 75 | UnwindData |  |
| 325 | `NotifyFveAfterFormat` | `0x1B330` | 592 | UnwindData |  |
| 78 | `?DismountVolume@IFS_SYSTEM@@SAEPEBVWSTRING@@@Z` | `0x1B5C0` | 357 | UnwindData |  |
| 84 | `?EnableVolumeCompression@IFS_SYSTEM@@SAEPEBVWSTRING@@@Z` | `0x1B730` | 510 | UnwindData |  |
| 85 | `?EnableVolumeIntegrity@IFS_SYSTEM@@SAEPEBVWSTRING@@G@Z` | `0x1B940` | 508 | UnwindData |  |
| 86 | `?EnableVolumeUpgrade@IFS_SYSTEM@@SAEPEBVWSTRING@@@Z` | `0x1BB50` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `?FileSetAttributes@IFS_SYSTEM@@SAEPEBVWSTRING@@KPEAK@Z` | `0x1BC20` | 251 | UnwindData |  |
| 93 | `?FormatScaleQuickFormatVerify@IFS_SYSTEM@@SAE_KPEAK11PEA_K@Z` | `0x1BD30` | 70 | UnwindData |  |
| 94 | `?FormatScaleTotalFreeClusters@IFS_SYSTEM@@SAE_K0PEAK1PEA_K2@Z` | `0x1BD80` | 110 | UnwindData |  |
| 99 | `?GetCannedSecurity@IFS_SYSTEM@@SAPEAVCANNED_SECURITY@@XZ` | `0x1BE00` | 224 | UnwindData |  |
| 120 | `?GetSystemTime@IFS_SYSTEM@@SAXPEAU_TIME_FIELDS@@@Z` | `0x1BEF0` | 59 | UnwindData |  |
| 155 | `?IsArcSystemPartition@IFS_SYSTEM@@SAEPEBVWSTRING@@PEAE@Z` | `0x1BF40` | 856 | UnwindData |  |
| 161 | `?IsFileSystemEnabled@IFS_SYSTEM@@SAEPEBVWSTRING@@PEAE@Z` | `0x1C2A0` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `?IsThisNtfs@IFS_SYSTEM@@SAEVBIG_INT@@KPEAX@Z` | `0x1C4B0` | 20 | UnwindData |  |
| 167 | `?IsThisReFS@IFS_SYSTEM@@SAEVBIG_INT@@KPEAX@Z` | `0x1C4D0` | 20 | UnwindData |  |
| 168 | `?IsTotalDeviceFailure@IFS_SYSTEM@@SAEJ@Z` | `0x1C4F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 170 | `?IsVolumeDirty@IFS_SYSTEM@@SAEPEAVWSTRING@@PEAE1PEAJ@Z` | `0x1C520` | 371 | UnwindData |  |
| 171 | `?IsVolumeWriteable@IFS_SYSTEM@@SAEPEAVWSTRING@@PEAEPEAJ@Z` | `0x1C6A0` | 135 | UnwindData |  |
| 175 | `?NtDeviceNameToDosDriveName@IFS_SYSTEM@@SAEPEBVWSTRING@@PEAV2@@Z` | `0x1C730` | 643 | UnwindData |  |
| 188 | `?QueryCanonicalNtDriveName@IFS_SYSTEM@@SAEPEBVWSTRING@@PEAV2@@Z` | `0x1C9C0` | 333 | UnwindData |  |
| 190 | `?QueryCluster@IFS_SYSTEM@@SAEPEAE@Z` | `0x1CB20` | 114 | UnwindData |  |
| 191 | `?QueryClusterFunctionalLevel@IFS_SYSTEM@@SAEPEAK0@Z` | `0x1CBA0` | 296 | UnwindData |  |
| 204 | `?QueryFileSystemNameByHandle@IFS_SYSTEM@@SAEPEAXPEAVWSTRING@@PEAJ1@Z` | `0x1CCD0` | 158 | UnwindData |  |
| 209 | `?QueryFreeDiskSpace@IFS_SYSTEM@@SAEPEBVWSTRING@@PEAVBIG_INT@@@Z` | `0x1CD80` | 215 | UnwindData |  |
| 215 | `?QueryIsSystemUEFI@IFS_SYSTEM@@SAEXZ` | `0x1CE60` | 115 | UnwindData |  |
| 232 | `?QueryPageSize@IFS_SYSTEM@@SAKXZ` | `0x1D010` | 93 | UnwindData |  |
| 236 | `?QueryPersistentVolumeFlags@IFS_SYSTEM@@SAEPEAVWSTRING@@KPEAKPEAEPEAJ@Z` | `0x1D080` | 403 | UnwindData |  |
| 239 | `?QueryProcessorInformation@IFS_SYSTEM@@SAEPEAVDSTRING@@PEAKPEA_K@Z` | `0x1D220` | 406 | UnwindData |  |
| 248 | `?QueryServer@IFS_SYSTEM@@SAEPEAE@Z` | `0x1D3C0` | 193 | UnwindData |  |
| 251 | `?QueryStorageAdapterProperty@IFS_SYSTEM@@SAEPEAXPEAVDSTRING@@1@Z` | `0x1D490` | 407 | UnwindData |  |
| 252 | `?QueryStorageDeviceProperty@IFS_SYSTEM@@SAEPEAXPEAVDSTRING@@11PEAE2@Z` | `0x1D630` | 705 | UnwindData |  |
| 254 | `?QuerySystemVersion@IFS_SYSTEM@@SAEPEAVDSTRING@@@Z` | `0x1DA10` | 160 | UnwindData |  |
| 266 | `?QueryVolumeSize@IFS_SYSTEM@@SAEPEBVWSTRING@@PEA_K@Z` | `0x1DAC0` | 157 | UnwindData |  |
| 299 | `?SetPersistentVolumeFlags@IFS_SYSTEM@@SAEPEAVWSTRING@@KKPEAEPEAJ@Z` | `0x1DBB0` | 388 | UnwindData |  |
| 322 | `?WriteToFile@IFS_SYSTEM@@SAEPEBVWSTRING@@PEAXKE@Z` | `0x1DD40` | 495 | UnwindData |  |
| 283 | `?ReverseCopy@INTSTACK@@QEAAEPEAV1@@Z` | `0x1E290` | 57 | UnwindData |  |
| 97 | `?GetAt@MOUNT_POINT_MAP@@QEAAEKPEAVWSTRING@@0PEAE@Z` | `0x1E340` | 143 | UnwindData |  |
| 200 | `?QueryDriveName@MOUNT_POINT_MAP@@QEAAEPEAVWSTRING@@0@Z` | `0x1E3E0` | 186 | UnwindData |  |
| 214 | `?QueryIsSystemPartition@MOUNT_POINT_MAP@@QEAAEPEAVWSTRING@@PEAE@Z` | `0x1E4A0` | 177 | UnwindData |  |
| 265 | `?QueryVolumeName@MOUNT_POINT_MAP@@QEAAEPEAVWSTRING@@0@Z` | `0x1E560` | 186 | UnwindData |  |
| 297 | `?SetIsSystemPartition@MOUNT_POINT_MAP@@QEAAEPEAVWSTRING@@E@Z` | `0x1E620` | 188 | UnwindData |  |
| 43 | `?Add@NUMBER_SET@@QEAAEPEBV1@@Z` | `0x1E760` | 87 | UnwindData |  |
| 87 | `?Enumerate@NUMBER_SET@@QEBAEEPEAVBIG_INT@@0@Z` | `0x1E7C0` | 72 | UnwindData |  |
| 197 | `?QueryDisjointRange@NUMBER_SET@@QEBAXKPEAVBIG_INT@@0@Z` | `0x1E810` | 135 | UnwindData |  |
| 276 | `?Remove@NUMBER_SET@@QEAAEPEBV1@@Z` | `0x1E8A0` | 87 | UnwindData |  |
| 311 | `?Subtract@NUMBER_SET@@QEAAEPEAV1@0@Z` | `0x1E900` | 176 | UnwindData |  |
| 15 | `??0READ_CACHE@@QEAA@XZ` | `0x1E9C0` | 142 | UnwindData |  |
| 141 | `?Initialize@READ_CACHE@@QEAAEPEAVIO_DP_DRIVE@@K@Z` | `0x1EAD0` | 70 | UnwindData |  |
| 14 | `??0READ_AHEAD_CACHE@@QEAA@XZ` | `0x1ECA0` | 65 | UnwindData |  |
| 140 | `?Initialize@READ_AHEAD_CACHE@@QEAAEPEAVIO_DP_DRIVE@@KK@Z` | `0x1EDA0` | 152 | UnwindData |  |
| 26 | `??0WRITE_ONCE_CACHE@@QEAA@XZ` | `0x1EFA0` | 70 | UnwindData |  |
| 152 | `?Initialize@WRITE_ONCE_CACHE@@QEAAEPEAVIO_DP_DRIVE@@KKK@Z` | `0x1F0E0` | 150 | UnwindData |  |
| 17 | `??0READ_WRITE_CACHE@@QEAA@XZ` | `0x1F240` | 117 | UnwindData |  |
| 16 | `??0READ_MODIFY_WRITE_CACHE@@QEAA@XZ` | `0x1F350` | 148 | UnwindData |  |
| 142 | `?Initialize@READ_MODIFY_WRITE_CACHE@@QEAAEPEAVIO_DP_DRIVE@@KKEE@Z` | `0x1F860` | 562 | UnwindData |  |
| 12 | `??0POW_CACHE@@QEAA@XZ` | `0x1FD50` | 67 | UnwindData |  |
| 13 | `??0POW_TRACK@@QEAA@XZ` | `0x1FDA0` | 63 | UnwindData |  |
| 138 | `?Initialize@POW_CACHE@@QEAAEKKKKK@Z` | `0x20250` | 214 | UnwindData |  |
| 139 | `?Initialize@POW_CACHE@@QEAAEPEAVIO_DP_DRIVE@@@Z` | `0x20330` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 246 | `?QuerySectorSize@POW_CACHE@@QEAAKXZ` | `0x203F0` | 1,392 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 286 | `?SendSonyMSFormatCmd@DP_DRIVE@@QEAAEE@Z` | `0x20960` | 151 | UnwindData |  |
| 288 | `?SendSonyMSModeSenseCmd@DP_DRIVE@@QEAAEPEAUSONY_MS_MODE_SENSE_DATA@@@Z` | `0x20A00` | 143 | UnwindData |  |
| 289 | `?SendSonyMSRequestSenseCmd@DP_DRIVE@@QEAAEPEAU_SENSE_DATA@@@Z` | `0x20AA0` | 140 | UnwindData |  |
| 290 | `?SendSonyMSTestUnitReadyCmd@DP_DRIVE@@QEAAEPEAU_SENSE_DATA@@@Z` | `0x20B40` | 128 | UnwindData |  |
| 19 | `??0SNAPSHOT@@AEAA@XZ` | `0x20C20` | 68 | UnwindData |  |
| 36 | `??1SNAPSHOT@@EEAA@XZ` | `0x20C70` | 60 | UnwindData |  |
| 61 | `?CheckSnapshotPresence@SNAPSHOT@@QEAAEXZ` | `0x20D30` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `?GetCurrentSnapshot@SNAPSHOT@@SAPEAV1@XZ` | `0x20DA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `?GetSnapshotErrorMessage@SNAPSHOT@@SAEJPEAVWSTRING@@@Z` | `0x20DB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `?GetSnapshotGlobalDeviceName@SNAPSHOT@@QEAAPEAGXZ` | `0x20DD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `?GetSnapshotNtDeviceName@SNAPSHOT@@QEAAPEAGXZ` | `0x20DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `?GetVolumeSnapshot@SNAPSHOT@@SAJPEAVWSTRING@@PEAPEAV1@@Z` | `0x20E10` | 1,037 | UnwindData |  |
| 145 | `?Initialize@SNAPSHOT@@AEAAJPEAG@Z` | `0x21230` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 160 | `?IsFatalError@SNAPSHOT@@SAEJ@Z` | `0x21250` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 250 | `?QuerySnapshotDiffAreaVolume@SNAPSHOT@@QEAAEPEAVWSTRING@@@Z` | `0x21290` | 273 | UnwindData |  |
| 275 | `?ReleaseVolumeSnapshot@SNAPSHOT@@SAEPEAV1@@Z` | `0x213B0` | 343 | UnwindData |  |
| 20 | `??0SPARSE_SET@@QEAA@XZ` | `0x21630` | 73 | UnwindData |  |
| 37 | `??1SPARSE_SET@@UEAA@XZ` | `0x21680` | 44 | UnwindData |  |
| 55 | `?Check@SPARSE_SET@@QEAAEVBIG_INT@@@Z` | `0x21730` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `?CheckAndAdd@SPARSE_SET@@QEAAEVBIG_INT@@PEAE@Z` | `0x217A0` | 290 | UnwindData |  |
| 146 | `?Initialize@SPARSE_SET@@QEAAEXZ` | `0x218D0` | 93 | UnwindData |  |
| 281 | `?RemoveAll@SPARSE_SET@@QEAAEXZ` | `0x21940` | 105 | UnwindData |  |
| 67 | `?ComputeVolId@SUPERAREA@@SAKK@Z` | `0x21A20` | 117 | UnwindData |  |
| 22 | `??0TLINK@@QEAA@XZ` | `0x21B10` | 72 | UnwindData |  |
| 39 | `??1TLINK@@UEAA@XZ` | `0x21B60` | 44 | UnwindData |  |
| 112 | `?GetNextDataSlot@TLINK@@QEAAAEAVBIG_INT@@XZ` | `0x21C60` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 148 | `?Initialize@TLINK@@QEAAEG@Z` | `0x21C90` | 108 | UnwindData |  |
| 198 | `?QueryDisjointRangeAndAssignBuffer@TLINK@@QEAAPEAXPEAVBIG_INT@@PEAG1PEAXK2@Z` | `0x21D10` | 105 | UnwindData |  |
| 306 | `?ShellSort@TLINK@@QEAAXXZ` | `0x21D80` | 297 | UnwindData |  |
| 8 | `??0MEDIA_TRACK_INFORMATION@@QEAA@XZ` | `0x21EB0` | 78 | UnwindData |  |
| 69 | `?CreateTrack@DP_DRIVE@@QEAAEKEW4NwaType@1@@Z` | `0x224A0` | 239 | UnwindData |  |
| 134 | `?Initialize@MEDIA_TRACK_INFORMATION@@QEAAXPEAU_TRACK_INFORMATION2@@@Z` | `0x229E0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `?InitializePowTrackConfiguration@DP_DRIVE@@QEAAEEPEAE@Z` | `0x22B00` | 274 | UnwindData |  |
| 178 | `?PowForceAllocation@IO_DP_DRIVE@@QEAAEKKPEAKW4NwaType@DP_DRIVE@@@Z` | `0x23160` | 482 | UnwindData |  |
| 196 | `?QueryDiscStatus@DP_DRIVE@@QEAAEPEAK0@Z` | `0x23600` | 257 | UnwindData |  |
| 202 | `?QueryEccBlockSizeInSectors@DP_DRIVE@@QEAAGXZ` | `0x23710` | 928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 205 | `?QueryFirstBlockInLastNonEmptySession@DP_DRIVE@@QEAAEPEAK@Z` | `0x23AB0` | 314 | UnwindData |  |
| 206 | `?QueryFirstBlockInLastSession@DP_DRIVE@@QEAAEPEAK@Z` | `0x23BF0` | 327 | UnwindData |  |
| 207 | `?QueryFreeBlocksInLastTrack@DP_DRIVE@@QEAAEPEAK@Z` | `0x23D40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 208 | `?QueryFreeBlocksInLastTrack@DP_DRIVE@@SAEPEAXPEAK@Z` | `0x23D50` | 358 | UnwindData |  |
| 210 | `?QueryHighestTrackAddress@DP_DRIVE@@QEAAEPEAK@Z` | `0x23EC0` | 122 | UnwindData |  |
| 216 | `?QueryLastRecordedAddress@DP_DRIVE@@QEAAEPEAK@Z` | `0x23F40` | 359 | UnwindData |  |
| 217 | `?QueryLastWritableAddress@DP_DRIVE@@QEAAEPEAKW4NwaType@1@@Z` | `0x240B0` | 153 | UnwindData |  |
| 224 | `?QueryNextWritableAddress@DP_DRIVE@@QEAAEPEAKW4NwaType@1@@Z` | `0x24150` | 400 | UnwindData |  |
| 231 | `?QueryOpenSessionBounds@DP_DRIVE@@QEAAEPEAK0@Z` | `0x242F0` | 689 | UnwindData |  |
| 256 | `?QueryUdfMediaHasPow@DP_DRIVE@@QEAAEXZ` | `0x246C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 257 | `?QueryUdfMediaNeedsLowLevelFormat@DP_DRIVE@@QEAAEXZ` | `0x246E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 258 | `?QueryUdfMediaNeedsSparing@DP_DRIVE@@QEAAEXZ` | `0x246F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 260 | `?QueryUdfMediaSupportsBackgroundFormat@DP_DRIVE@@QEAAEXZ` | `0x24710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 261 | `?QueryUdfMediaSupportsQuickGrow@DP_DRIVE@@QEAAEXZ` | `0x24720` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 264 | `?QueryVolumeBounds@DP_DRIVE@@QEAAEPEAK0@Z` | `0x24750` | 518 | UnwindData |  |
| 271 | `?ReadFormattableCapacity@DP_DRIVE@@QEAAEEPEAKPEAE0@Z` | `0x24B00` | 988 | UnwindData |  |
| 274 | `?ReinitiateBackgroundFormat@DP_DRIVE@@QEAAEXZ` | `0x25010` | 117 | UnwindData |  |
| 285 | `?SendPowLowLevelFormat@DP_DRIVE@@QEAAEPEAVMESSAGE@@@Z` | `0x25550` | 324 | UnwindData |  |
| 301 | `?SetPowTrackConfiguration@DP_DRIVE@@QEAAEE@Z` | `0x256A0` | 1,132 | UnwindData |  |
| 317 | `?WaitForUnit@DP_DRIVE@@QEAAEPEAVMESSAGE@@@Z` | `0x25CD0` | 24 | UnwindData |  |
| 318 | `?WaitForWriteCompletion@DP_DRIVE@@QEAAEPEAVMESSAGE@@@Z` | `0x25D60` | 214 | UnwindData |  |
| 23 | `??0VOL_LIODPDRV@@IEAA@XZ` | `0x25EC0` | 95 | UnwindData |  |
| 40 | `??1VOL_LIODPDRV@@UEAA@XZ` | `0x25F70` | 81 | UnwindData |  |
| 63 | `?ChkDsk@VOL_LIODPDRV@@QEAAEW4FIX_LEVEL@@PEAVMESSAGE@@KKGPEAKPEBVWSTRING@@@Z` | `0x26040` | 751 | UnwindData |  |
| 88 | `?Export@FORMAT_SQM@@QEAAEH@Z` | `0x26340` | 451 | UnwindData |  |
| 91 | `?ForceAutochk@VOL_LIODPDRV@@QEAAEEKKGPEBVWSTRING@@@Z` | `0x26510` | 2,029 | UnwindData |  |
| 92 | `?Format@VOL_LIODPDRV@@QEAA?AW4FORMAT_ERROR_CODE@@PEBVWSTRING@@PEAVMESSAGE@@KKK@Z` | `0x26D10` | 1,251 | UnwindData |  |
| 106 | `?GetFileSystemName@VOL_LIODPDRV@@QEAAPEBGXZ` | `0x276E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `?Initialize@FORMAT_SQM@@QEAAEPEAVDP_DRIVE@@PEBGKK@Z` | `0x27700` | 346 | UnwindData |  |
| 150 | `?Initialize@VOL_LIODPDRV@@IEAAEPEBVWSTRING@@0PEAVSUPERAREA@@PEAVMESSAGE@@E@Z` | `0x27860` | 87 | UnwindData |  |
| 183 | `?QueryAutochkTimeOut@VOL_LIODPDRV@@SAEPEAK@Z` | `0x278C0` | 115 | UnwindData |  |
| 272 | `?Recover@VOL_LIODPDRV@@QEAAEPEBVWSTRING@@PEAVMESSAGE@@@Z` | `0x279F0` | 128 | UnwindData |  |
| 292 | `?SetAutochkTimeOut@VOL_LIODPDRV@@SAEK@Z` | `0x27A80` | 66 | UnwindData |  |
| 295 | `?SetFileSystemName@VOL_LIODPDRV@@QEAAEPEBG@Z` | `0x27AD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 305 | `?SetVolumeLabelAndPrintFormatReport@VOL_LIODPDRV@@QEAAEPEBVWSTRING@@PEAVMESSAGE@@@Z` | `0x27AF0` | 668 | UnwindData |  |
| 328 | `RestoreThreadExecutionState` | `0x27E10` | 87 | UnwindData |  |
| 24 | `??0WRITEVIEW_CACHE@@QEAA@XZ` | `0x27E70` | 293 | UnwindData |  |
| 41 | `??1WRITEVIEW_CACHE@@UEAA@XZ` | `0x280F0` | 118 | UnwindData |  |
| 54 | `?AdjustCacheSize@WRITEVIEW_CACHE@@UEAAXPEA_K0@Z` | `0x28280` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `?Delete@WRITEVIEW_CACHE@@QEAAXPEAVWRITEVIEW_CACHE_ENTRY@@@Z` | `0x28480` | 34 | UnwindData |  |
| 75 | `?Destroy@WRITEVIEW_CACHE@@QEAAXXZ` | `0x284B0` | 313 | UnwindData |  |
| 76 | `?DestroyWrites@WRITEVIEW_CACHE@@QEAAXXZ` | `0x285F0` | 277 | UnwindData |  |
| 151 | `?Initialize@WRITEVIEW_CACHE@@QEAAEPEAVIO_DP_DRIVE@@PEAVDRIVE_CACHE@@PEBVWSTRING@@GEE@Z` | `0x28C90` | 1,041 | UnwindData |  |
| 221 | `?QueryMemoryLimit@WRITEVIEW_CACHE@@UEAAEPEA_KPEAE@Z` | `0x29130` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 310 | `?SqmExport@WRITEVIEW_CACHE@@UEAAEP6AEPEAXKEPEADZZ0@Z` | `0x29270` | 1,346 | UnwindData |  |
