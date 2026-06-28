# Binary Specification: resutils.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\resutils.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e043620ac59de22e030ce4c62f4d21d250d9fc21b0138e6b38c985f30bee46b2`
* **Total Exported Functions:** 146

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 49 | `ResUtilAddUnknownProperties` | `0xA150` | 46 | UnwindData |  |
| 52 | `ResUtilDupParameterBlock` | `0xA190` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `ResUtilEnumPrivateProperties` | `0xA1A0` | 36 | UnwindData |  |
| 58 | `ResUtilEnumProperties` | `0xA1D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `ResUtilEnumResources` | `0xA1E0` | 647 | UnwindData |  |
| 60 | `ResUtilEnumResourcesEx` | `0xA470` | 33 | UnwindData |  |
| 61 | `ResUtilEnumResourcesEx2` | `0xA4A0` | 626 | UnwindData |  |
| 63 | `ResUtilFindBinaryProperty` | `0xAA30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `ResUtilFindDwordProperty` | `0xAA40` | 50 | UnwindData |  |
| 66 | `ResUtilFindExpandSzProperty` | `0xAA80` | 20 | UnwindData |  |
| 71 | `ResUtilFindSzProperty` | `0xAA80` | 20 | UnwindData |  |
| 67 | `ResUtilFindExpandedSzProperty` | `0xAAA0` | 23 | UnwindData |  |
| 68 | `ResUtilFindFileTimeProperty` | `0xAAC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `ResUtilFindLongProperty` | `0xAAD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `ResUtilFindMultiSzProperty` | `0xAAE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `ResUtilFindULargeIntegerProperty` | `0xAAF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `ResUtilFreeParameterBlock` | `0xAB00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `ResUtilGetAllProperties` | `0xAB10` | 46 | UnwindData |  |
| 90 | `ResUtilGetPrivateProperties` | `0xAB50` | 36 | UnwindData |  |
| 91 | `ResUtilGetProperties` | `0xAB80` | 111 | UnwindData |  |
| 92 | `ResUtilGetPropertiesToParameterBlock` | `0xAC00` | 36 | UnwindData |  |
| 93 | `ResUtilGetProperty` | `0xAC30` | 26 | UnwindData |  |
| 94 | `ResUtilGetPropertyFormats` | `0xAC50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `ResUtilGetPropertySize` | `0xAC60` | 26 | UnwindData |  |
| 97 | `ResUtilGetResourceDependency` | `0xAC80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `ResUtilGetResourceDependencyByClass` | `0xACA0` | 34 | UnwindData |  |
| 99 | `ResUtilGetResourceDependencyByClassEx` | `0xACD0` | 34 | UnwindData |  |
| 100 | `ResUtilGetResourceDependencyByName` | `0xAD00` | 31 | UnwindData |  |
| 101 | `ResUtilGetResourceDependencyByNameAndClass` | `0xAD30` | 1,106 | UnwindData |  |
| 102 | `ResUtilGetResourceDependencyByNameEx` | `0xB190` | 31 | UnwindData |  |
| 103 | `ResUtilGetResourceDependencyEx` | `0xB1C0` | 157 | UnwindData |  |
| 106 | `ResUtilGetResourceNameDependency` | `0xB270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `ResUtilGetResourceNameDependencyEx` | `0xB290` | 222 | UnwindData |  |
| 110 | `ResUtilGroupsEqual` | `0xB380` | 288 | UnwindData |  |
| 112 | `ResUtilIsResourceClassEqual` | `0xB4B0` | 112 | UnwindData |  |
| 116 | `ResUtilPropertyListFromParameterBlock` | `0xB530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `ResUtilResourceTypesEqual` | `0xB540` | 301 | UnwindData |  |
| 120 | `ResUtilResourcesEqual` | `0xB680` | 429 | UnwindData |  |
| 125 | `ResUtilSetPrivatePropertyList` | `0xB840` | 146 | UnwindData |  |
| 126 | `ResUtilSetPropertyParameterBlock` | `0xB8E0` | 190 | UnwindData |  |
| 127 | `ResUtilSetPropertyParameterBlockEx` | `0xB9B0` | 200 | UnwindData |  |
| 128 | `ResUtilSetPropertyTable` | `0xBA80` | 207 | UnwindData |  |
| 129 | `ResUtilSetPropertyTableEx` | `0xBB60` | 213 | UnwindData |  |
| 135 | `ResUtilSetUnknownProperties` | `0xBC40` | 153 | UnwindData |  |
| 141 | `ResUtilVerifyPrivatePropertyList` | `0xBCE0` | 29 | UnwindData |  |
| 142 | `ResUtilVerifyPropertyTable` | `0xBD10` | 66 | UnwindData |  |
| 80 | `ResUtilGetClusterRoleState` | `0xBF80` | 659 | UnwindData |  |
| 11 | `ClusterClearBackupStateForSharedVolume` | `0xC220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `ClusterGetVolumeNameForVolumeMountPoint` | `0xC240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `ClusterGetVolumePathName` | `0xC250` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `ClusterIsPathOnSharedVolume` | `0xC270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `ClusterPrepareSharedVolumeForBackup` | `0xC280` | 40 | UnwindData |  |
| 1 | `ClusWorkerStart` | `0xF150` | 204 | UnwindData |  |
| 3 | `ClusAddClusterHealthFault` | `0x10480` | 1,488 | UnwindData |  |
| 4 | `ClusGetClusterHealthFaults` | `0x10A60` | 141 | UnwindData |  |
| 5 | `ClusRemoveClusterHealthFault` | `0x10B00` | 1,615 | UnwindData |  |
| 6 | `ClusWorkerCheckTerminate` | `0x11160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `ClusWorkerCreate` | `0x11170` | 384 | UnwindData |  |
| 8 | `ClusWorkerTerminate` | `0x11300` | 238 | UnwindData |  |
| 9 | `ClusWorkerTerminateEx` | `0x11400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `ClusWorkersTerminate` | `0x11410` | 795 | UnwindData |  |
| 43 | `FreeClusterHealthFault` | `0x11740` | 99 | UnwindData |  |
| 44 | `FreeClusterHealthFaultArray` | `0x117B0` | 100 | UnwindData |  |
| 45 | `InitializeClusterHealthFault` | `0x11820` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `InitializeClusterHealthFaultArray` | `0x11850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `ResUtilCreateDirectoryTree` | `0x11870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `ResUtilDupGroup` | `0x11880` | 269 | UnwindData |  |
| 53 | `ResUtilDupResource` | `0x119A0` | 269 | UnwindData |  |
| 54 | `ResUtilDupString` | `0x11AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `ResUtilEnumGroups` | `0x11AD0` | 23 | UnwindData |  |
| 56 | `ResUtilEnumGroupsEx` | `0x11AF0` | 35 | UnwindData |  |
| 62 | `ResUtilExpandEnvironmentStrings` | `0x11B20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `ResUtilFindDependentDiskResourceDriveLetter` | `0x11B30` | 946 | UnwindData |  |
| 73 | `ResUtilFreeEnvironment` | `0x11EF0` | 34 | UnwindData |  |
| 76 | `ResUtilGetBinaryProperty` | `0x11F20` | 147 | UnwindData |  |
| 77 | `ResUtilGetBinaryValue` | `0x11FC0` | 208 | UnwindData |  |
| 78 | `ResUtilGetClusterGroupType` | `0x120A0` | 212 | UnwindData |  |
| 79 | `ResUtilGetClusterId` | `0x12180` | 245 | UnwindData |  |
| 81 | `ResUtilGetCoreClusterResources` | `0x12280` | 23 | UnwindData |  |
| 82 | `ResUtilGetCoreClusterResourcesEx` | `0x122A0` | 26 | UnwindData |  |
| 83 | `ResUtilGetCoreGroup` | `0x122C0` | 230 | UnwindData |  |
| 84 | `ResUtilGetDwordProperty` | `0x123B0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `ResUtilGetDwordValue` | `0x12410` | 117 | UnwindData |  |
| 86 | `ResUtilGetEnvironmentWithNetName` | `0x12490` | 317 | UnwindData |  |
| 87 | `ResUtilGetFileTimeProperty` | `0x125E0` | 180 | UnwindData |  |
| 88 | `ResUtilGetLongProperty` | `0x126A0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `ResUtilGetMultiSzProperty` | `0x12700` | 161 | UnwindData |  |
| 96 | `ResUtilGetQwordValue` | `0x127B0` | 120 | UnwindData |  |
| 104 | `ResUtilGetResourceDependentIPAddressProps` | `0x12830` | 1,424 | UnwindData |  |
| 105 | `ResUtilGetResourceName` | `0x12DD0` | 235 | UnwindData |  |
| 108 | `ResUtilGetSzProperty` | `0x12ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `ResUtilGetSzValue` | `0x12EE0` | 246 | UnwindData |  |
| 111 | `ResUtilIsPathValid` | `0x12FE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `ResUtilLeftPaxosIsLessThanRight` | `0x12FF0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `ResUtilNodeEnum` | `0x13040` | 656 | UnwindData |  |
| 115 | `ResUtilPaxosComparer` | `0x132E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `ResUtilRemoveResourceServiceEnvironment` | `0x13320` | 300 | UnwindData |  |
| 118 | `ResUtilResourceDepEnum` | `0x13460` | 23 | UnwindData |  |
| 121 | `ResUtilSetBinaryValue` | `0x13480` | 221 | UnwindData |  |
| 122 | `ResUtilSetDwordValue` | `0x13570` | 65 | UnwindData |  |
| 123 | `ResUtilSetExpandSzValue` | `0x135C0` | 246 | UnwindData |  |
| 124 | `ResUtilSetMultiSzValue` | `0x136C0` | 221 | UnwindData |  |
| 130 | `ResUtilSetQwordValue` | `0x137B0` | 70 | UnwindData |  |
| 131 | `ResUtilSetResourceServiceEnvironment` | `0x13800` | 507 | UnwindData |  |
| 132 | `ResUtilSetResourceServiceStartParameters` | `0x13A10` | 36 | UnwindData |  |
| 133 | `ResUtilSetResourceServiceStartParametersEx` | `0x13A40` | 723 | UnwindData |  |
| 134 | `ResUtilSetSzValue` | `0x13D20` | 247 | UnwindData |  |
| 136 | `ResUtilSetValueEx` | `0x13E20` | 162 | UnwindData |  |
| 137 | `ResUtilStartResourceService` | `0x13ED0` | 334 | UnwindData |  |
| 138 | `ResUtilStopResourceService` | `0x14030` | 330 | UnwindData |  |
| 139 | `ResUtilStopService` | `0x14180` | 234 | UnwindData |  |
| 140 | `ResUtilTerminateServiceProcessFromResDll` | `0x14270` | 550 | UnwindData |  |
| 143 | `ResUtilVerifyResourceService` | `0x144A0` | 227 | UnwindData |  |
| 144 | `ResUtilVerifyService` | `0x14590` | 117 | UnwindData |  |
| 146 | `ResUtilsDeleteKeyTree` | `0x14610` | 282 | UnwindData |  |
| 26 | `ClusterSharedVolumeCheckSnapshotPresence` | `0x17180` | 192 | UnwindData |  |
| 27 | `ClusterSharedVolumeCreateSnapshot` | `0x17250` | 633 | UnwindData |  |
| 28 | `ClusterSharedVolumeReleaseSnapshot` | `0x174D0` | 70 | UnwindData |  |
| 2 | `CloseClusterCryptProvider` | `0x180B0` | 84 | UnwindData |  |
| 12 | `ClusterDecrypt` | `0x18110` | 627 | UnwindData |  |
| 13 | `ClusterEncrypt` | `0x18390` | 444 | UnwindData |  |
| 42 | `FreeClusterCrypt` | `0x18560` | 75 | UnwindData |  |
| 47 | `OpenClusterCryptProvider` | `0x185C0` | 389 | UnwindData |  |
| 48 | `OpenClusterCryptProviderEx` | `0x18750` | 505 | UnwindData |  |
| 145 | `ResUtilVerifyShutdownSafe` | `0x19350` | 782 | UnwindData |  |
| 15 | `ClusterFileShareCreate` | `0x2FC40` | 5,610 | UnwindData |  |
| 16 | `ClusterFileShareDelete` | `0x31230` | 641 | UnwindData |  |
| 17 | `ClusterFileShareUpdate` | `0x314C0` | 1,216 | UnwindData |  |
| 23 | `ClusterIsClusterDisk` | `0x31990` | 649 | UnwindData |  |
| 14 | `ClusterEnumTasks` | `0x32FE0` | 1,630 | UnwindData |  |
| 18 | `ClusterFreeTaskInfo` | `0x33650` | 190 | UnwindData |  |
| 19 | `ClusterFreeTaskList` | `0x33720` | 70 | UnwindData |  |
| 20 | `ClusterGetTaskNode` | `0x33770` | 307 | UnwindData |  |
| 29 | `ClusterTaskChangeFromXML` | `0x338B0` | 887 | UnwindData |  |
| 30 | `ClusterTaskChangeFromXMLFile` | `0x33C30` | 342 | UnwindData |  |
| 31 | `ClusterTaskChange_TS_V1` | `0x33D90` | 1,002 | UnwindData |  |
| 32 | `ClusterTaskCreateFromXML` | `0x34180` | 1,268 | UnwindData |  |
| 33 | `ClusterTaskCreateFromXMLFile` | `0x34680` | 393 | UnwindData |  |
| 34 | `ClusterTaskCreate_TS_V1` | `0x34810` | 1,508 | UnwindData |  |
| 35 | `ClusterTaskDelete` | `0x34E00` | 698 | UnwindData |  |
| 36 | `ClusterTaskDelete_TS_V1` | `0x350C0` | 790 | UnwindData |  |
| 37 | `ClusterTaskExists_TS_V1` | `0x353E0` | 964 | UnwindData |  |
| 38 | `ClusterTaskQuery` | `0x357B0` | 947 | UnwindData |  |
| 39 | `CreateClusterStorageSpacesClustering` | `0x38DD0` | 121 | UnwindData |  |
| 40 | `CreateClusterStorageSpacesResourceLocator` | `0x38E50` | 46 | UnwindData |  |
| 41 | `CreateClusterStorageSpacesSubProvider` | `0x38E90` | 121 | UnwindData |  |
