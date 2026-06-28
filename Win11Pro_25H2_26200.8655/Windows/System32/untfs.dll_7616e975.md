# Binary Specification: untfs.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\untfs.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7616e975b507a1ac29ac213e63dda27e0aa10d5094b73ee06f0b039e9d36581c`
* **Total Exported Functions:** 168

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 48 | `?CompareDupInfo@NTFS_MFT_INFO@@SAEPEAXPEAU_FILE_NAME@@@Z` | `0x21F0` | 40 | UnwindData |  |
| 120 | `?QueryFlags@NTFS_MFT_INFO@@SAEPEAXG@Z` | `0x2220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `?QuerySegmentReference@NTFS_MFT_INFO@@SA?AU_MFT_SEGMENT_REFERENCE@@PEAX@Z` | `0x2230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `CreateFormatCorruptionRecordContext` | `0x2240` | 79 | UnwindData |  |
| 160 | `DeleteFormatCorruptionRecordContext` | `0x22A0` | 37 | UnwindData |  |
| 163 | `FormatCorruptionRecordA` | `0x22D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 164 | `FormatCorruptionRecordW` | `0x22E0` | 341 | UnwindData |  |
| 2 | `??0NTFS_ATTRIBUTE_DEFINITION_TABLE@@QEAA@XZ` | `0x54F0` | 45 | UnwindData |  |
| 23 | `??1NTFS_ATTRIBUTE_DEFINITION_TABLE@@UEAA@XZ` | `0x5530` | 736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `?Initialize@NTFS_ATTRIBUTE_DEFINITION_TABLE@@QEAAEW4FIX_LEVEL@@PEAVNTFS_MASTER_FILE_TABLE@@E@Z` | `0x5810` | 1,936 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `??0NTFS_ATTRIBUTE@@QEAA@XZ` | `0x5FA0` | 115 | UnwindData |  |
| 22 | `??1NTFS_ATTRIBUTE@@UEAA@XZ` | `0x6020` | 60 | UnwindData |  |
| 64 | `?GrowSparse@NTFS_ATTRIBUTE@@UEAAEVBIG_INT@@PEAVNTFS_BITMAP@@E@Z` | `0x6990` | 170 | UnwindData |  |
| 65 | `?Initialize@NTFS_ATTRIBUTE@@QEAAEPEAVLOG_IO_DP_DRIVE@@KPEBVNTFS_EXTENT_LIST@@VBIG_INT@@2KPEBVWSTRING@@G@Z` | `0x71D0` | 464 | UnwindData |  |
| 66 | `?Initialize@NTFS_ATTRIBUTE@@QEAAEPEAVLOG_IO_DP_DRIVE@@KPEBXKKPEBVWSTRING@@G@Z` | `0x73B0` | 367 | UnwindData |  |
| 98 | `?InsertIntoFile@NTFS_ATTRIBUTE@@UEAAEPEAVNTFS_FILE_RECORD_SEGMENT@@PEAVNTFS_BITMAP@@@Z` | `0x7530` | 1,040 | UnwindData |  |
| 104 | `?MakeNonresident@NTFS_ATTRIBUTE@@UEAAEPEAVNTFS_BITMAP@@@Z` | `0x8090` | 777 | UnwindData |  |
| 105 | `?Prefetch@NTFS_ATTRIBUTE@@QEAAEVBIG_INT@@K@Z` | `0x8720` | 377 | UnwindData |  |
| 112 | `?QueryClustersAllocated@NTFS_ATTRIBUTE@@QEBA?AVBIG_INT@@XZ` | `0x89B0` | 50 | UnwindData |  |
| 129 | `?Read@NTFS_ATTRIBUTE@@QEAAEPEAXVBIG_INT@@KPEAK@Z` | `0x89F0` | 31 | UnwindData |  |
| 139 | `?ReadWithAltExtents@NTFS_ATTRIBUTE@@QEAAEPEAXVBIG_INT@@KPEAKPEAVNTFS_EXTENT_LIST@@@Z` | `0x8A20` | 875 | UnwindData |  |
| 143 | `?Resize@NTFS_ATTRIBUTE@@UEAAEVBIG_INT@@PEAVNTFS_BITMAP@@@Z` | `0x95E0` | 519 | UnwindData |  |
| 147 | `?SetSparse@NTFS_ATTRIBUTE@@UEAAEVBIG_INT@@PEAVNTFS_BITMAP@@E@Z` | `0x9950` | 243 | UnwindData |  |
| 151 | `?Write@NTFS_ATTRIBUTE@@UEAAEPEBXVBIG_INT@@KPEAKPEAVNTFS_BITMAP@@@Z` | `0x9E40` | 1,266 | UnwindData |  |
| 3 | `??0NTFS_ATTRIBUTE_LIST@@QEAA@XZ` | `0xA360` | 79 | UnwindData |  |
| 24 | `??1NTFS_ATTRIBUTE_LIST@@UEAA@XZ` | `0xA3C0` | 66 | UnwindData |  |
| 61 | `?GetNextAttributeListEntry@NTFS_ATTRIBUTE_LIST@@QEBAPEBU_ATTRIBUTE_LIST_ENTRY@@PEBU2@@Z` | `0xAA90` | 912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `?QueryNextEntry@NTFS_ATTRIBUTE_LIST@@QEBAEPEAU_ATTR_LIST_CURR_ENTRY@@PEAKPEAVBIG_INT@@PEAU_MFT_SEGMENT_REFERENCE@@PEAGPEAVWSTRING@@@Z` | `0xAE20` | 234 | UnwindData |  |
| 137 | `?ReadList@NTFS_ATTRIBUTE_LIST@@QEAAEXZ` | `0xAF10` | 181 | UnwindData |  |
| 4 | `??0NTFS_ATTRIBUTE_RECORD@@QEAA@XZ` | `0xB870` | 69 | UnwindData |  |
| 25 | `??1NTFS_ATTRIBUTE_RECORD@@UEAA@XZ` | `0xB8C0` | 44 | UnwindData |  |
| 68 | `?Initialize@NTFS_ATTRIBUTE_RECORD@@QEAAEPEAVIO_DP_DRIVE@@PEAX@Z` | `0xC2E0` | 66 | UnwindData |  |
| 117 | `?QueryExtentList@NTFS_ATTRIBUTE_RECORD@@QEBAEPEAVNTFS_EXTENT_LIST@@@Z` | `0xC4A0` | 93 | UnwindData |  |
| 123 | `?QueryName@NTFS_ATTRIBUTE_RECORD@@QEBAEPEAVWSTRING@@@Z` | `0xC510` | 121 | UnwindData |  |
| 5 | `??0NTFS_BAD_CLUSTER_FILE@@QEAA@XZ` | `0xE1A0` | 53 | UnwindData |  |
| 26 | `??1NTFS_BAD_CLUSTER_FILE@@UEAA@XZ` | `0xE1E0` | 68 | UnwindData |  |
| 69 | `?Initialize@NTFS_BAD_CLUSTER_FILE@@QEAAEW4FIX_LEVEL@@PEAVNTFS_MASTER_FILE_TABLE@@@Z` | `0xE9A0` | 93 | UnwindData |  |
| 7 | `??0NTFS_BITMAP_FILE@@QEAA@XZ` | `0xF040` | 45 | UnwindData |  |
| 28 | `??1NTFS_BITMAP_FILE@@UEAA@XZ` | `0xF080` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `??1NTFS_BOOT_FILE@@UEAA@XZ` | `0xF080` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `??1NTFS_LOG_FILE@@UEAA@XZ` | `0xF080` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `??1NTFS_REFLECTED_MASTER_FILE_TABLE@@UEAA@XZ` | `0xF080` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `??1NTFS_UPCASE_FILE@@UEAA@XZ` | `0xF080` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `?Initialize@NTFS_BITMAP_FILE@@QEAAEW4FIX_LEVEL@@PEAVNTFS_MASTER_FILE_TABLE@@@Z` | `0xF2E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `??0NTFS_BOOT_FILE@@QEAA@XZ` | `0xF300` | 45 | UnwindData |  |
| 72 | `?Initialize@NTFS_BOOT_FILE@@QEAAEW4FIX_LEVEL@@PEAVNTFS_MASTER_FILE_TABLE@@@Z` | `0xF460` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `??0NTFS_CLUSTER_RUN@@QEAA@XZ` | `0xF620` | 68 | UnwindData |  |
| 30 | `??1NTFS_CLUSTER_RUN@@UEAA@XZ` | `0xF670` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `?Initialize@NTFS_CLUSTER_RUN@@QEAAEPEAVMEM@@PEAVLOG_IO_DP_DRIVE@@VBIG_INT@@KK@Z` | `0xF770` | 121 | UnwindData |  |
| 140 | `?Relocate@NTFS_CLUSTER_RUN@@QEAAXVBIG_INT@@@Z` | `0xF7F0` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `GetFsFormatOptions` | `0xFAA0` | 243 | UnwindData |  |
| 146 | `SetOriginalVolumeName` | `0xFD00` | 162 | UnwindData |  |
| 149 | `SetWriteViewCacheVolumeName` | `0xFDB0` | 162 | UnwindData |  |
| 157 | `Chkdsk` | `0xFE60` | 1,671 | UnwindData |  |
| 158 | `ChkdskEx` | `0x104F0` | 5,341 | UnwindData |  |
| 161 | `Extend` | `0x119E0` | 675 | UnwindData |  |
| 162 | `Format` | `0x11C90` | 1,203 | UnwindData |  |
| 165 | `FormatEx` | `0x12150` | 1,805 | UnwindData |  |
| 166 | `GetFilesystemInformation` | `0x12870` | 554 | UnwindData |  |
| 168 | `Recover` | `0x12AA0` | 589 | UnwindData |  |
| 10 | `??0NTFS_EXTENT_LIST@@QEAA@XZ` | `0x12D00` | 69 | UnwindData |  |
| 31 | `??1NTFS_EXTENT_LIST@@UEAA@XZ` | `0x12D50` | 44 | UnwindData |  |
| 43 | `?AddExtent@NTFS_EXTENT_LIST@@QEAAEVBIG_INT@@00@Z` | `0x12E60` | 199 | UnwindData |  |
| 74 | `?Initialize@NTFS_EXTENT_LIST@@QEAAEVBIG_INT@@0@Z` | `0x13430` | 181 | UnwindData |  |
| 116 | `?QueryExtent@NTFS_EXTENT_LIST@@QEBAEKPEAVBIG_INT@@00@Z` | `0x139D0` | 105 | UnwindData |  |
| 122 | `?QueryLcnFromVcn@NTFS_EXTENT_LIST@@QEBAEVBIG_INT@@PEAV2@1@Z` | `0x13A40` | 277 | UnwindData |  |
| 125 | `?QueryNumberOfExtents@NTFS_EXTENT_LIST@@QEBAKXZ` | `0x13B60` | 3,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `?CreateElementaryStructures@NTFS_SA@@QEAAEPEAVNTFS_BITMAP@@KKKKPEBVNUMBER_SET@@EEEEEKPEAVMESSAGE@@PEAUBIOS_PARAMETER_BLOCK@@PEBVWSTRING@@E@Z` | `0x148B0` | 8,743 | UnwindData |  |
| 126 | `?QuerySectorsInElementaryStructures@NTFS_SA@@SAKPEAVDP_DRIVE@@KKKKE@Z` | `0x16DF0` | 535 | UnwindData |  |
| 156 | `?WriteRemainingBootCode@NTFS_SA@@QEAAEXZ` | `0x17090` | 345 | UnwindData |  |
| 11 | `??0NTFS_FILE_RECORD_SEGMENT@@QEAA@XZ` | `0x171F0` | 109 | UnwindData |  |
| 32 | `??1NTFS_FILE_RECORD_SEGMENT@@UEAA@XZ` | `0x17270` | 72 | UnwindData |  |
| 44 | `?AddFileNameAttribute@NTFS_FILE_RECORD_SEGMENT@@QEAAEPEAU_FILE_NAME@@@Z` | `0x17570` | 169 | UnwindData |  |
| 45 | `?AddSecurityDescriptor@NTFS_FILE_RECORD_SEGMENT@@QEAAEW4_CANNED_SECURITY_TYPE@@PEAVNTFS_BITMAP@@@Z` | `0x17620` | 139 | UnwindData |  |
| 46 | `?AddSecurityDescriptorData@NTFS_FILE_RECORD_SEGMENT@@QEAAEPEAVNTFS_ATTRIBUTE@@PEAXPEAPEAU_SECURITY_ENTRY@@KW4_CANNED_SECURITY_TYPE@@PEAVNTFS_BITMAP@@W4FIX_LEVEL@@@Z` | `0x176C0` | 841 | UnwindData |  |
| 53 | `?Create@NTFS_FILE_RECORD_SEGMENT@@QEAAEPEBU_STANDARD_INFORMATION@@G@Z` | `0x17E70` | 162 | UnwindData |  |
| 57 | `?Flush@NTFS_FILE_RECORD_SEGMENT@@QEAAEPEAVNTFS_BITMAP@@PEAVNTFS_INDEX_TREE@@E@Z` | `0x19ED0` | 553 | UnwindData |  |
| 75 | `?Initialize@NTFS_FILE_RECORD_SEGMENT@@QEAAEW4FIX_LEVEL@@@Z` | `0x1A280` | 191 | UnwindData |  |
| 76 | `?Initialize@NTFS_FILE_RECORD_SEGMENT@@QEAAEW4FIX_LEVEL@@PEAVNTFS_FRS_STRUCTURE@@PEAVNTFS_MASTER_FILE_TABLE@@@Z` | `0x1A350` | 202 | UnwindData |  |
| 77 | `?Initialize@NTFS_FILE_RECORD_SEGMENT@@QEAAEW4FIX_LEVEL@@VBIG_INT@@KPEAVNTFS_MASTER_FILE_TABLE@@@Z` | `0x1A420` | 273 | UnwindData |  |
| 78 | `?Initialize@NTFS_FILE_RECORD_SEGMENT@@QEAAEW4FIX_LEVEL@@VBIG_INT@@PEAVNTFS_MASTER_FILE_TABLE@@@Z` | `0x1A540` | 279 | UnwindData |  |
| 79 | `?Initialize@NTFS_FILE_RECORD_SEGMENT@@QEAAEW4FIX_LEVEL@@VBIG_INT@@PEAVNTFS_MFT_FILE@@@Z` | `0x1A660` | 2,800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `?IsAttributePresent@NTFS_FILE_RECORD_SEGMENT@@QEAAEKPEBVWSTRING@@E@Z` | `0x1B150` | 469 | UnwindData |  |
| 107 | `?QueryAttribute@NTFS_FILE_RECORD_SEGMENT@@QEAAEPEAVNTFS_ATTRIBUTE@@PEAEKPEBVWSTRING@@@Z` | `0x1B9F0` | 1,212 | UnwindData |  |
| 108 | `?QueryAttributeByOrdinal@NTFS_FILE_RECORD_SEGMENT@@QEAAEPEAVNTFS_ATTRIBUTE@@PEAEKK@Z` | `0x1BEC0` | 983 | UnwindData |  |
| 110 | `?QueryAttributeListAttribute@NTFS_FILE_RECORD_SEGMENT@@QEAAEPEAVNTFS_ATTRIBUTE@@PEAE@Z` | `0x1C370` | 283 | UnwindData |  |
| 114 | `?QueryDuplicatedInformation@NTFS_FILE_RECORD_SEGMENT@@QEAAEPEAU_DUPLICATED_INFORMATION@@@Z` | `0x1C560` | 634 | UnwindData |  |
| 119 | `?QueryFileSizes@NTFS_FILE_RECORD_SEGMENT@@QEAAEPEAVBIG_INT@@0PEAE@Z` | `0x1C7E0` | 615 | UnwindData |  |
| 153 | `?Write@NTFS_FILE_RECORD_SEGMENT@@UEAAEXZ` | `0x218A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `??0NTFS_FRS_STRUCTURE@@QEAA@XZ` | `0x218B0` | 94 | UnwindData |  |
| 33 | `??1NTFS_FRS_STRUCTURE@@UEAA@XZ` | `0x21920` | 44 | UnwindData |  |
| 62 | `?GetNextAttributeRecord@NTFS_FRS_STRUCTURE@@QEAAPEAXPEBXPEAVMESSAGE@@PEAE@Z` | `0x21D40` | 941 | UnwindData |  |
| 80 | `?Initialize@NTFS_FRS_STRUCTURE@@QEAAEPEAU_FILE_RECORD_SEGMENT_HEADER@@PEAVNTFS_ATTRIBUTE@@VBIG_INT@@KK2KPEAVNTFS_UPCASE_TABLE@@@Z` | `0x22100` | 121 | UnwindData |  |
| 81 | `?Initialize@NTFS_FRS_STRUCTURE@@QEAAEPEAVMEM@@PEAVLOG_IO_DP_DRIVE@@VBIG_INT@@K2KPEAVNTFS_UPCASE_TABLE@@K@Z` | `0x22180` | 406 | UnwindData |  |
| 82 | `?Initialize@NTFS_FRS_STRUCTURE@@QEAAEPEAVMEM@@PEAVNTFS_ATTRIBUTE@@VBIG_INT@@K2KPEAVNTFS_UPCASE_TABLE@@@Z` | `0x22320` | 156 | UnwindData |  |
| 83 | `?Initialize@NTFS_FRS_STRUCTURE@@QEAAEPEAVMEM@@PEAVNTFS_ATTRIBUTE@@VBIG_INT@@KK2KPEAVNTFS_UPCASE_TABLE@@@Z` | `0x223D0` | 160 | UnwindData |  |
| 106 | `?Prefetch@NTFS_FRS_STRUCTURE@@QEAAEVBIG_INT@@0@Z` | `0x22E20` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `?QueryAttributeList@NTFS_FRS_STRUCTURE@@QEAAEPEAVNTFS_ATTRIBUTE_LIST@@@Z` | `0x22E60` | 205 | UnwindData |  |
| 130 | `?Read@NTFS_FRS_STRUCTURE@@QEAAEVBIG_INT@@@Z` | `0x22F40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `?ReadAt@NTFS_FRS_STRUCTURE@@QEAAEVBIG_INT@@@Z` | `0x22F40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `?Read@NTFS_FRS_STRUCTURE@@UEAAEXZ` | `0x22F60` | 191 | UnwindData |  |
| 135 | `?ReadAgain@NTFS_FRS_STRUCTURE@@QEAAEVBIG_INT@@@Z` | `0x23030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `?ReadNext@NTFS_FRS_STRUCTURE@@QEAAEVBIG_INT@@@Z` | `0x23040` | 170 | UnwindData |  |
| 144 | `?SafeQueryAttribute@NTFS_FRS_STRUCTURE@@QEAAEKPEAVNTFS_ATTRIBUTE@@0PEAVWSTRING@@@Z` | `0x230F0` | 1,719 | UnwindData |  |
| 154 | `?Write@NTFS_FRS_STRUCTURE@@QEAAEXZ` | `0x24BD0` | 449 | UnwindData |  |
| 13 | `??0NTFS_INDEX_TREE@@QEAA@XZ` | `0x38780` | 149 | UnwindData |  |
| 34 | `??1NTFS_INDEX_TREE@@UEAA@XZ` | `0x38960` | 63 | UnwindData |  |
| 52 | `?CopyIterator@NTFS_INDEX_TREE@@QEAAEPEAV1@@Z` | `0x38B80` | 446 | UnwindData |  |
| 60 | `?GetNext@NTFS_INDEX_TREE@@QEAAPEBU_INDEX_ENTRY@@PEAKPEAEE@Z` | `0x39DD0` | 90 | UnwindData |  |
| 84 | `?Initialize@NTFS_INDEX_TREE@@QEAAEKPEAVLOG_IO_DP_DRIVE@@KPEAVNTFS_BITMAP@@PEAVNTFS_UPCASE_TABLE@@KKKPEBVWSTRING@@@Z` | `0x3A6E0` | 578 | UnwindData |  |
| 85 | `?Initialize@NTFS_INDEX_TREE@@QEAAEPEAVLOG_IO_DP_DRIVE@@KPEAVNTFS_BITMAP@@PEAVNTFS_UPCASE_TABLE@@KPEAVNTFS_FILE_RECORD_SEGMENT@@PEBVWSTRING@@@Z` | `0x3A930` | 1,005 | UnwindData |  |
| 97 | `?InsertEntry@NTFS_INDEX_TREE@@QEAAEKPEAXU_MFT_SEGMENT_REFERENCE@@E@Z` | `0x3AD30` | 243 | UnwindData |  |
| 115 | `?QueryEntry@NTFS_INDEX_TREE@@QEAAEKPEAXKPEAPEAU_INDEX_ENTRY@@PEAPEAVNTFS_INDEX_BUFFER@@PEAE@Z` | `0x3C6A0` | 204 | UnwindData |  |
| 118 | `?QueryFileReference@NTFS_INDEX_TREE@@QEAAEKPEAXKPEAU_MFT_SEGMENT_REFERENCE@@PEAE@Z` | `0x3C780` | 249 | UnwindData |  |
| 141 | `?ResetIterator@NTFS_INDEX_TREE@@QEAAEE@Z` | `0x3D030` | 252 | UnwindData |  |
| 142 | `?ResetIterator@NTFS_INDEX_TREE@@QEAAEPEBU_INDEX_ENTRY@@E@Z` | `0x3D140` | 178 | UnwindData |  |
| 145 | `?Save@NTFS_INDEX_TREE@@QEAAEPEAVNTFS_FILE_RECORD_SEGMENT@@@Z` | `0x3D3A0` | 912 | UnwindData |  |
| 14 | `??0NTFS_LOG_FILE@@QEAA@XZ` | `0x3DC50` | 45 | UnwindData |  |
| 54 | `?CreateDataAttribute@NTFS_LOG_FILE@@QEAAEVBIG_INT@@KPEAVNTFS_BITMAP@@@Z` | `0x3DC90` | 375 | UnwindData |  |
| 86 | `?Initialize@NTFS_LOG_FILE@@QEAAEW4FIX_LEVEL@@PEAVNTFS_MASTER_FILE_TABLE@@@Z` | `0x3DFA0` | 3,664 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `?AllocateFileRecordSegment@NTFS_MASTER_FILE_TABLE@@QEAAEPEAVBIG_INT@@E@Z` | `0x3EDF0` | 677 | UnwindData |  |
| 56 | `?Extend@NTFS_MASTER_FILE_TABLE@@QEAAEK@Z` | `0x3F0A0` | 369 | UnwindData |  |
| 15 | `??0NTFS_MFT_FILE@@QEAA@XZ` | `0x3F220` | 128 | UnwindData |  |
| 36 | `??1NTFS_MFT_FILE@@UEAA@XZ` | `0x3F2B0` | 115 | UnwindData |  |
| 58 | `?Flush@NTFS_MFT_FILE@@QEAAEXZ` | `0x3F7D0` | 1,544 | UnwindData |  |
| 87 | `?Initialize@NTFS_MFT_FILE@@QEAAEW4FIX_LEVEL@@PEAVLOG_IO_DP_DRIVE@@VBIG_INT@@KK2PEAVNTFS_BITMAP@@PEAVNTFS_UPCASE_TABLE@@PEAVNTFS_ATTRIBUTE@@@Z` | `0x3FDE0` | 409 | UnwindData |  |
| 132 | `?Read@NTFS_MFT_FILE@@UEAAEXZ` | `0x3FF80` | 399 | UnwindData |  |
| 16 | `??0NTFS_MFT_INFO@@QEAA@XZ` | `0x40120` | 121 | UnwindData |  |
| 37 | `??1NTFS_MFT_INFO@@UEAA@XZ` | `0x401A0` | 60 | UnwindData |  |
| 49 | `?CompareFileName@NTFS_MFT_INFO@@SAEPEAXKPEAU_FILE_NAME@@PEAG@Z` | `0x402C0` | 98 | UnwindData |  |
| 50 | `?ComputeDupInfoSignature@NTFS_MFT_INFO@@CAXPEAU_DUPLICATED_INFORMATION@@QEAE@Z` | `0x40330` | 109 | UnwindData |  |
| 51 | `?ComputeFileNameSignature@NTFS_MFT_INFO@@CAXKPEAU_FILE_NAME@@QEAE@Z` | `0x403B0` | 166 | UnwindData |  |
| 88 | `?Initialize@NTFS_MFT_INFO@@QEAAEVBIG_INT@@PEAVNTFS_UPCASE_TABLE@@EE_K@Z` | `0x40820` | 239 | UnwindData |  |
| 89 | `?Initialize@NTFS_MFT_INFO@@QEAAEXZ` | `0x40920` | 123 | UnwindData |  |
| 17 | `??0NTFS_REFLECTED_MASTER_FILE_TABLE@@QEAA@XZ` | `0x409B0` | 45 | UnwindData |  |
| 90 | `?Initialize@NTFS_REFLECTED_MASTER_FILE_TABLE@@QEAAEW4FIX_LEVEL@@PEAVNTFS_MASTER_FILE_TABLE@@@Z` | `0x40B40` | 1,936 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `??0NTFS_BITMAP@@QEAA@XZ` | `0x412D0` | 138 | UnwindData |  |
| 27 | `??1NTFS_BITMAP@@UEAA@XZ` | `0x41360` | 95 | UnwindData |  |
| 70 | `?Initialize@NTFS_BITMAP@@QEAAEVBIG_INT@@EPEAVLOG_IO_DP_DRIVE@@KE@Z` | `0x419B0` | 349 | UnwindData |  |
| 99 | `?IsAllocated@NTFS_BITMAP@@QEBAEVBIG_INT@@0@Z` | `0x41B20` | 116 | UnwindData |  |
| 102 | `?IsFree@NTFS_BITMAP@@QEBAEVBIG_INT@@0@Z` | `0x41BA0` | 116 | UnwindData |  |
| 152 | `?Write@NTFS_BITMAP@@QEAAEPEAVNTFS_ATTRIBUTE@@PEAV1@@Z` | `0x41DB0` | 188 | UnwindData |  |
| 155 | `?WriteModified@NTFS_BITMAP@@QEAAEPEAVNTFS_ATTRIBUTE@@PEAV1@@Z` | `0x41E80` | 929 | UnwindData |  |
| 63 | `?GetRootFrsIndex@NTFS_SA@@SAEW4FIX_LEVEL@@PEAVNTFS_MFT_FILE@@PEAVNTFS_FILE_RECORD_SEGMENT@@PEAVNTFS_INDEX_TREE@@@Z` | `0x4A640` | 296 | UnwindData |  |
| 18 | `??0NTFS_SA@@QEAA@XZ` | `0x5CA60` | 201 | UnwindData |  |
| 39 | `??1NTFS_SA@@UEAA@XZ` | `0x5CD50` | 167 | UnwindData |  |
| 91 | `?Initialize@NTFS_SA@@QEAAEPEAVLOG_IO_DP_DRIVE@@PEAVMESSAGE@@VBIG_INT@@2KE@Z` | `0x5D330` | 391 | UnwindData |  |
| 101 | `?IsDosName@NTFS_SA@@SAEPEBU_FILE_NAME@@@Z` | `0x5D570` | 311 | UnwindData |  |
| 103 | `?IsNtfsName@NTFS_SA@@SAEPEBU_FILE_NAME@@@Z` | `0x5D6B0` | 1,136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `?QueryClusterFactor@NTFS_SA@@QEBAKXZ` | `0x5DB20` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `?QueryDefaultClustersPerIndexBuffer@NTFS_SA@@SAKPEBVDP_DRIVE@@K@Z` | `0x5DC40` | 79 | UnwindData |  |
| 121 | `?QueryFrsFromPath@NTFS_SA@@QEAAEW4FIX_LEVEL@@PEBVWSTRING@@PEAVNTFS_MASTER_FILE_TABLE@@PEAVNTFS_BITMAP@@PEAVNTFS_FILE_RECORD_SEGMENT@@PEAE5@Z` | `0x5DCA0` | 1,154 | UnwindData |  |
| 128 | `?QueryVolumeFlagsAndLabel@NTFS_SA@@QEAAGPEAE00PEAVWSTRING@@@Z` | `0x5E230` | 1,303 | UnwindData |  |
| 133 | `?Read@NTFS_SA@@QEAAEPEAVMESSAGE@@@Z` | `0x5E750` | 533 | UnwindData |  |
| 134 | `?Read@NTFS_SA@@UEAAEXZ` | `0x5E970` | 73 | UnwindData |  |
| 148 | `?SetVolumeFlag@NTFS_SA@@QEAAEGPEAE@Z` | `0x5F0E0` | 566 | UnwindData |  |
| 150 | `?TakeCensus@NTFS_SA@@QEAAEPEAVNTFS_MASTER_FILE_TABLE@@KPEAUNTFS_CENSUS_INFO@@@Z` | `0x5F320` | 464 | UnwindData |  |
| 20 | `??0NTFS_UPCASE_TABLE@@QEAA@XZ` | `0x818D0` | 61 | UnwindData |  |
| 41 | `??1NTFS_UPCASE_TABLE@@UEAA@XZ` | `0x81920` | 44 | UnwindData |  |
| 93 | `?Initialize@NTFS_UPCASE_TABLE@@QEAAEPEAGK@Z` | `0x81A80` | 148 | UnwindData |  |
| 94 | `?Initialize@NTFS_UPCASE_TABLE@@QEAAEPEAVNTFS_ATTRIBUTE@@PEA_K@Z` | `0x81B20` | 260 | UnwindData |  |
| 95 | `?Initialize@NTFS_UPCASE_TABLE@@QEAAEXZ` | `0x81C30` | 249 | UnwindData |  |
| 167 | `NtfsUpcaseCompare` | `0x81E00` | 249 | UnwindData |  |
| 19 | `??0NTFS_UPCASE_FILE@@QEAA@XZ` | `0x81F00` | 45 | UnwindData |  |
| 92 | `?Initialize@NTFS_UPCASE_FILE@@QEAAEW4FIX_LEVEL@@PEAVNTFS_MASTER_FILE_TABLE@@@Z` | `0x820F0` | 9,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `??0NTFS_VOLUME_FILE@@QEAA@XZ` | `0x84730` | 64 | UnwindData |  |
| 42 | `??1NTFS_VOLUME_FILE@@UEAA@XZ` | `0x84780` | 51 | UnwindData |  |
| 96 | `?Initialize@NTFS_VOLUME_FILE@@QEAAEPEAVLOG_IO_DP_DRIVE@@PEAVNTFS_MASTER_FILE_TABLE@@PEAVNTFS_FILE_RECORD_SEGMENT@@PEAVNTFS_INDEX_TREE@@PEAU_VOLUME_INFORMATION@@PEAVWSTRING@@W4FIX_LEVEL@@@Z` | `0x85080` | 161 | UnwindData |  |
