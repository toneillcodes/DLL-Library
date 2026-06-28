# Binary Specification: mtxclu.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\mtxclu.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `eb30f11baad820d4c0d140a0ad896162d373a16e3d280bcf34b8bc018643c07b`
* **Total Exported Functions:** 38

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 13 | `MtxCluCreateClusterProxyTmInstance` | `0x5A70` | 386 | UnwindData |  |
| 14 | `MtxCluCreateClusterTmInstance` | `0x5C00` | 325 | UnwindData |  |
| 15 | `MtxCluCreateTmInstanceForVirtualServer` | `0x5D50` | 698 | UnwindData |  |
| 10 | `FailedClusterAPIToEventLog` | `0xAEB0` | 191 | UnwindData |  |
| 12 | `MtxCluClearClusterTmMappings` | `0xC590` | 1,412 | UnwindData |  |
| 16 | `MtxCluEnumerateClusterTmMappings` | `0xCB20` | 1,565 | UnwindData |  |
| 17 | `MtxCluEnumerateDtcResources` | `0xD150` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `MtxCluEnumerateDtcResourcesEx` | `0xD160` | 1,201 | UnwindData |  |
| 19 | `MtxCluGetActiveClusterNode` | `0xD620` | 704 | UnwindData |  |
| 20 | `MtxCluGetClusterResourceIdFromName` | `0xDA80` | 586 | UnwindData |  |
| 21 | `MtxCluGetDTCResourceForResource` | `0xE6C0` | 372 | UnwindData |  |
| 22 | `MtxCluGetDTCVirtualServerNameW` | `0xEEE0` | 506 | UnwindData |  |
| 23 | `MtxCluGetDefaultClusterResource` | `0xF0E0` | 897 | UnwindData |  |
| 24 | `MtxCluGetDefaultClusterResourceNonAdmin` | `0xF470` | 629 | UnwindData |  |
| 25 | `MtxCluGetDtcDiskResourceDrive` | `0xF6F0` | 2,325 | UnwindData |  |
| 26 | `MtxCluGetNameFromResourceIdString` | `0x10010` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `MtxCluGetNameFromResourceIdStringNonAdmin` | `0x101A0` | 791 | UnwindData |  |
| 28 | `MtxCluGetResourceId` | `0x104C0` | 542 | UnwindData |  |
| 29 | `MtxCluGetResourceIdStringFromName` | `0x106F0` | 384 | UnwindData |  |
| 30 | `MtxCluGetTmResource` | `0x10F90` | 1,025 | UnwindData |  |
| 31 | `MtxCluGetVirtualServerToken` | `0x113A0` | 924 | UnwindData |  |
| 32 | `MtxCluIsClusterPresentExW` | `0x11750` | 61 | UnwindData |  |
| 33 | `MtxCluRemoveClusterTmMappingByName` | `0x119D0` | 432 | UnwindData |  |
| 34 | `MtxCluSetClusterTmMapping` | `0x11C90` | 1,155 | UnwindData |  |
| 35 | `MtxCluSetDefaultClusterResource` | `0x12120` | 625 | UnwindData |  |
| 37 | `MtxCluVerifyLogPathInDependantDiskResource` | `0x131C0` | 1,087 | UnwindData |  |
| 38 | `MtxCluVerifyLogPathIsValidCSV` | `0x13610` | 564 | UnwindData |  |
| 9 | `Startup` | `0x192D0` | 103 | UnwindData |  |
| 1 | `MtxCluGetComputerNameW` | `0x19F70` | 460 | UnwindData |  |
| 2 | `MtxCluGetDTCStatusW` | `0x1A150` | 296 | UnwindData |  |
| 3 | `MtxCluGetSecurityRegValue` | `0x1A280` | 243 | UnwindData |  |
| 8 | `MtxCluSetSecurityRegValue` | `0x1A380` | 241 | UnwindData |  |
| 11 | `MtxCluBringOnlineDTCW` | `0x1A480` | 278 | UnwindData |  |
| 36 | `MtxCluTakeOfflineDTCW` | `0x1A5A0` | 278 | UnwindData |  |
| 4 | `MtxCluIsClusterPresent` | `0x1C390` | 29 | UnwindData |  |
| 5 | `MtxCluIsNetworkNameInLocalClusterW` | `0x1C520` | 345 | UnwindData |  |
| 6 | `MtxCluIsSameClusterW` | `0x1C7F0` | 185 | UnwindData |  |
| 7 | `MtxCluIsSameNodeW` | `0x1C8B0` | 517 | UnwindData |  |
