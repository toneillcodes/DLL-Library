# Binary Specification: resutils.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\resutils.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4515f020baba54774f91c437b321963a01850f7ff29f9d7922116c4d07161cb3`
* **Total Exported Functions:** 146

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 49 | `ResUtilAddUnknownProperties` | `0xA230` | 46 | UnwindData |  |
| 52 | `ResUtilDupParameterBlock` | `0xA270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `ResUtilEnumPrivateProperties` | `0xA280` | 36 | UnwindData |  |
| 58 | `ResUtilEnumProperties` | `0xA2B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `ResUtilEnumResources` | `0xA2C0` | 647 | UnwindData |  |
| 60 | `ResUtilEnumResourcesEx` | `0xA550` | 33 | UnwindData |  |
| 61 | `ResUtilEnumResourcesEx2` | `0xA580` | 626 | UnwindData |  |
| 63 | `ResUtilFindBinaryProperty` | `0xAB10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `ResUtilFindDwordProperty` | `0xAB20` | 50 | UnwindData |  |
| 66 | `ResUtilFindExpandSzProperty` | `0xAB60` | 20 | UnwindData |  |
| 71 | `ResUtilFindSzProperty` | `0xAB60` | 20 | UnwindData |  |
| 67 | `ResUtilFindExpandedSzProperty` | `0xAB80` | 23 | UnwindData |  |
| 68 | `ResUtilFindFileTimeProperty` | `0xABA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `ResUtilFindLongProperty` | `0xABB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `ResUtilFindMultiSzProperty` | `0xABC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `ResUtilFindULargeIntegerProperty` | `0xABD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `ResUtilFreeParameterBlock` | `0xABE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `ResUtilGetAllProperties` | `0xABF0` | 46 | UnwindData |  |
| 90 | `ResUtilGetPrivateProperties` | `0xAC30` | 36 | UnwindData |  |
| 91 | `ResUtilGetProperties` | `0xAC60` | 111 | UnwindData |  |
| 92 | `ResUtilGetPropertiesToParameterBlock` | `0xACE0` | 36 | UnwindData |  |
| 93 | `ResUtilGetProperty` | `0xAD10` | 26 | UnwindData |  |
| 94 | `ResUtilGetPropertyFormats` | `0xAD30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `ResUtilGetPropertySize` | `0xAD40` | 26 | UnwindData |  |
| 97 | `ResUtilGetResourceDependency` | `0xAD60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `ResUtilGetResourceDependencyByClass` | `0xAD80` | 34 | UnwindData |  |
| 99 | `ResUtilGetResourceDependencyByClassEx` | `0xADB0` | 34 | UnwindData |  |
| 100 | `ResUtilGetResourceDependencyByName` | `0xADE0` | 31 | UnwindData |  |
| 101 | `ResUtilGetResourceDependencyByNameAndClass` | `0xAE10` | 1,106 | UnwindData |  |
| 102 | `ResUtilGetResourceDependencyByNameEx` | `0xB270` | 31 | UnwindData |  |
| 103 | `ResUtilGetResourceDependencyEx` | `0xB2A0` | 157 | UnwindData |  |
| 106 | `ResUtilGetResourceNameDependency` | `0xB350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `ResUtilGetResourceNameDependencyEx` | `0xB370` | 222 | UnwindData |  |
| 110 | `ResUtilGroupsEqual` | `0xB460` | 288 | UnwindData |  |
| 112 | `ResUtilIsResourceClassEqual` | `0xB590` | 112 | UnwindData |  |
| 116 | `ResUtilPropertyListFromParameterBlock` | `0xB610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `ResUtilResourceTypesEqual` | `0xB620` | 301 | UnwindData |  |
| 120 | `ResUtilResourcesEqual` | `0xB760` | 429 | UnwindData |  |
| 125 | `ResUtilSetPrivatePropertyList` | `0xB920` | 146 | UnwindData |  |
| 126 | `ResUtilSetPropertyParameterBlock` | `0xB9C0` | 190 | UnwindData |  |
| 127 | `ResUtilSetPropertyParameterBlockEx` | `0xBA90` | 200 | UnwindData |  |
| 128 | `ResUtilSetPropertyTable` | `0xBB60` | 207 | UnwindData |  |
| 129 | `ResUtilSetPropertyTableEx` | `0xBC40` | 213 | UnwindData |  |
| 135 | `ResUtilSetUnknownProperties` | `0xBD20` | 153 | UnwindData |  |
| 141 | `ResUtilVerifyPrivatePropertyList` | `0xBDC0` | 29 | UnwindData |  |
| 142 | `ResUtilVerifyPropertyTable` | `0xBDF0` | 66 | UnwindData |  |
| 80 | `ResUtilGetClusterRoleState` | `0xC060` | 659 | UnwindData |  |
| 11 | `ClusterClearBackupStateForSharedVolume` | `0xC300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `ClusterGetVolumeNameForVolumeMountPoint` | `0xC320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `ClusterGetVolumePathName` | `0xC330` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `ClusterIsPathOnSharedVolume` | `0xC350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `ClusterPrepareSharedVolumeForBackup` | `0xC360` | 40 | UnwindData |  |
| 1 | `ClusWorkerStart` | `0xF230` | 204 | UnwindData |  |
| 3 | `ClusAddClusterHealthFault` | `0x10560` | 1,488 | UnwindData |  |
| 4 | `ClusGetClusterHealthFaults` | `0x10B40` | 141 | UnwindData |  |
| 5 | `ClusRemoveClusterHealthFault` | `0x10BE0` | 1,615 | UnwindData |  |
| 6 | `ClusWorkerCheckTerminate` | `0x11240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `ClusWorkerCreate` | `0x11250` | 384 | UnwindData |  |
| 8 | `ClusWorkerTerminate` | `0x113E0` | 238 | UnwindData |  |
| 9 | `ClusWorkerTerminateEx` | `0x114E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `ClusWorkersTerminate` | `0x114F0` | 795 | UnwindData |  |
| 43 | `FreeClusterHealthFault` | `0x11820` | 99 | UnwindData |  |
| 44 | `FreeClusterHealthFaultArray` | `0x11890` | 100 | UnwindData |  |
| 45 | `InitializeClusterHealthFault` | `0x11900` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `InitializeClusterHealthFaultArray` | `0x11930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `ResUtilCreateDirectoryTree` | `0x11950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `ResUtilDupGroup` | `0x11960` | 269 | UnwindData |  |
| 53 | `ResUtilDupResource` | `0x11A80` | 269 | UnwindData |  |
| 54 | `ResUtilDupString` | `0x11BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `ResUtilEnumGroups` | `0x11BB0` | 23 | UnwindData |  |
| 56 | `ResUtilEnumGroupsEx` | `0x11BD0` | 35 | UnwindData |  |
| 62 | `ResUtilExpandEnvironmentStrings` | `0x11C00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `ResUtilFindDependentDiskResourceDriveLetter` | `0x11C10` | 946 | UnwindData |  |
| 73 | `ResUtilFreeEnvironment` | `0x11FD0` | 34 | UnwindData |  |
| 76 | `ResUtilGetBinaryProperty` | `0x12000` | 147 | UnwindData |  |
| 77 | `ResUtilGetBinaryValue` | `0x120A0` | 208 | UnwindData |  |
| 78 | `ResUtilGetClusterGroupType` | `0x12180` | 212 | UnwindData |  |
| 79 | `ResUtilGetClusterId` | `0x12260` | 245 | UnwindData |  |
| 81 | `ResUtilGetCoreClusterResources` | `0x12360` | 23 | UnwindData |  |
| 82 | `ResUtilGetCoreClusterResourcesEx` | `0x12380` | 26 | UnwindData |  |
| 83 | `ResUtilGetCoreGroup` | `0x123A0` | 230 | UnwindData |  |
| 84 | `ResUtilGetDwordProperty` | `0x12490` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `ResUtilGetDwordValue` | `0x124F0` | 117 | UnwindData |  |
| 86 | `ResUtilGetEnvironmentWithNetName` | `0x12570` | 317 | UnwindData |  |
| 87 | `ResUtilGetFileTimeProperty` | `0x126C0` | 180 | UnwindData |  |
| 88 | `ResUtilGetLongProperty` | `0x12780` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `ResUtilGetMultiSzProperty` | `0x127E0` | 161 | UnwindData |  |
| 96 | `ResUtilGetQwordValue` | `0x12890` | 120 | UnwindData |  |
| 104 | `ResUtilGetResourceDependentIPAddressProps` | `0x12910` | 1,424 | UnwindData |  |
| 105 | `ResUtilGetResourceName` | `0x12EB0` | 235 | UnwindData |  |
| 108 | `ResUtilGetSzProperty` | `0x12FB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `ResUtilGetSzValue` | `0x12FC0` | 246 | UnwindData |  |
| 111 | `ResUtilIsPathValid` | `0x130C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `ResUtilLeftPaxosIsLessThanRight` | `0x130D0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `ResUtilNodeEnum` | `0x13120` | 656 | UnwindData |  |
| 115 | `ResUtilPaxosComparer` | `0x133C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `ResUtilRemoveResourceServiceEnvironment` | `0x13400` | 300 | UnwindData |  |
| 118 | `ResUtilResourceDepEnum` | `0x13540` | 23 | UnwindData |  |
| 121 | `ResUtilSetBinaryValue` | `0x13560` | 221 | UnwindData |  |
| 122 | `ResUtilSetDwordValue` | `0x13650` | 65 | UnwindData |  |
| 123 | `ResUtilSetExpandSzValue` | `0x136A0` | 246 | UnwindData |  |
| 124 | `ResUtilSetMultiSzValue` | `0x137A0` | 221 | UnwindData |  |
| 130 | `ResUtilSetQwordValue` | `0x13890` | 70 | UnwindData |  |
| 131 | `ResUtilSetResourceServiceEnvironment` | `0x138E0` | 507 | UnwindData |  |
| 132 | `ResUtilSetResourceServiceStartParameters` | `0x13AF0` | 36 | UnwindData |  |
| 133 | `ResUtilSetResourceServiceStartParametersEx` | `0x13B20` | 723 | UnwindData |  |
| 134 | `ResUtilSetSzValue` | `0x13E00` | 247 | UnwindData |  |
| 136 | `ResUtilSetValueEx` | `0x13F00` | 162 | UnwindData |  |
| 137 | `ResUtilStartResourceService` | `0x13FB0` | 334 | UnwindData |  |
| 138 | `ResUtilStopResourceService` | `0x14110` | 330 | UnwindData |  |
| 139 | `ResUtilStopService` | `0x14260` | 234 | UnwindData |  |
| 140 | `ResUtilTerminateServiceProcessFromResDll` | `0x14350` | 550 | UnwindData |  |
| 143 | `ResUtilVerifyResourceService` | `0x14580` | 227 | UnwindData |  |
| 144 | `ResUtilVerifyService` | `0x14670` | 117 | UnwindData |  |
| 146 | `ResUtilsDeleteKeyTree` | `0x146F0` | 282 | UnwindData |  |
| 26 | `ClusterSharedVolumeCheckSnapshotPresence` | `0x17260` | 192 | UnwindData |  |
| 27 | `ClusterSharedVolumeCreateSnapshot` | `0x17330` | 633 | UnwindData |  |
| 28 | `ClusterSharedVolumeReleaseSnapshot` | `0x175B0` | 70 | UnwindData |  |
| 2 | `CloseClusterCryptProvider` | `0x18190` | 84 | UnwindData |  |
| 12 | `ClusterDecrypt` | `0x181F0` | 627 | UnwindData |  |
| 13 | `ClusterEncrypt` | `0x18470` | 444 | UnwindData |  |
| 42 | `FreeClusterCrypt` | `0x18640` | 75 | UnwindData |  |
| 47 | `OpenClusterCryptProvider` | `0x186A0` | 389 | UnwindData |  |
| 48 | `OpenClusterCryptProviderEx` | `0x18830` | 505 | UnwindData |  |
| 145 | `ResUtilVerifyShutdownSafe` | `0x19430` | 782 | UnwindData |  |
| 15 | `ClusterFileShareCreate` | `0x2FD60` | 5,610 | UnwindData |  |
| 16 | `ClusterFileShareDelete` | `0x31350` | 641 | UnwindData |  |
| 17 | `ClusterFileShareUpdate` | `0x315E0` | 1,216 | UnwindData |  |
| 23 | `ClusterIsClusterDisk` | `0x31AB0` | 649 | UnwindData |  |
| 14 | `ClusterEnumTasks` | `0x33100` | 1,630 | UnwindData |  |
| 18 | `ClusterFreeTaskInfo` | `0x33770` | 190 | UnwindData |  |
| 19 | `ClusterFreeTaskList` | `0x33840` | 70 | UnwindData |  |
| 20 | `ClusterGetTaskNode` | `0x33890` | 307 | UnwindData |  |
| 29 | `ClusterTaskChangeFromXML` | `0x339D0` | 887 | UnwindData |  |
| 30 | `ClusterTaskChangeFromXMLFile` | `0x33D50` | 342 | UnwindData |  |
| 31 | `ClusterTaskChange_TS_V1` | `0x33EB0` | 1,002 | UnwindData |  |
| 32 | `ClusterTaskCreateFromXML` | `0x342A0` | 1,268 | UnwindData |  |
| 33 | `ClusterTaskCreateFromXMLFile` | `0x347A0` | 393 | UnwindData |  |
| 34 | `ClusterTaskCreate_TS_V1` | `0x34930` | 1,508 | UnwindData |  |
| 35 | `ClusterTaskDelete` | `0x34F20` | 698 | UnwindData |  |
| 36 | `ClusterTaskDelete_TS_V1` | `0x351E0` | 790 | UnwindData |  |
| 37 | `ClusterTaskExists_TS_V1` | `0x35500` | 964 | UnwindData |  |
| 38 | `ClusterTaskQuery` | `0x358D0` | 947 | UnwindData |  |
| 39 | `CreateClusterStorageSpacesClustering` | `0x38EF0` | 121 | UnwindData |  |
| 40 | `CreateClusterStorageSpacesResourceLocator` | `0x38F70` | 46 | UnwindData |  |
| 41 | `CreateClusterStorageSpacesSubProvider` | `0x38FB0` | 121 | UnwindData |  |
