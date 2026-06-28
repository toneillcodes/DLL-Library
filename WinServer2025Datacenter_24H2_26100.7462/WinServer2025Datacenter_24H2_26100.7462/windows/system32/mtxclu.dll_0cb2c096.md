# Binary Specification: mtxclu.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\mtxclu.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0cb2c09680cc693be69755c2a96a051128a9b8beb20acbf7ea39eb1f4ba2d1fb`
* **Total Exported Functions:** 38

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 13 | `MtxCluCreateClusterProxyTmInstance` | `0x5C70` | 386 | UnwindData |  |
| 14 | `MtxCluCreateClusterTmInstance` | `0x5E00` | 325 | UnwindData |  |
| 15 | `MtxCluCreateTmInstanceForVirtualServer` | `0x5F50` | 698 | UnwindData |  |
| 10 | `FailedClusterAPIToEventLog` | `0x124D0` | 191 | UnwindData |  |
| 12 | `MtxCluClearClusterTmMappings` | `0x13BB0` | 1,412 | UnwindData |  |
| 16 | `MtxCluEnumerateClusterTmMappings` | `0x14140` | 1,565 | UnwindData |  |
| 17 | `MtxCluEnumerateDtcResources` | `0x14770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `MtxCluEnumerateDtcResourcesEx` | `0x14780` | 1,201 | UnwindData |  |
| 19 | `MtxCluGetActiveClusterNode` | `0x14C40` | 704 | UnwindData |  |
| 20 | `MtxCluGetClusterResourceIdFromName` | `0x150A0` | 586 | UnwindData |  |
| 21 | `MtxCluGetDTCResourceForResource` | `0x15CE0` | 372 | UnwindData |  |
| 22 | `MtxCluGetDTCVirtualServerNameW` | `0x16500` | 506 | UnwindData |  |
| 23 | `MtxCluGetDefaultClusterResource` | `0x16700` | 897 | UnwindData |  |
| 24 | `MtxCluGetDefaultClusterResourceNonAdmin` | `0x16A90` | 673 | UnwindData |  |
| 25 | `MtxCluGetDtcDiskResourceDrive` | `0x16D40` | 2,325 | UnwindData |  |
| 26 | `MtxCluGetNameFromResourceIdString` | `0x17660` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `MtxCluGetNameFromResourceIdStringNonAdmin` | `0x177F0` | 831 | UnwindData |  |
| 28 | `MtxCluGetResourceId` | `0x17B40` | 542 | UnwindData |  |
| 29 | `MtxCluGetResourceIdStringFromName` | `0x17D70` | 384 | UnwindData |  |
| 30 | `MtxCluGetTmResource` | `0x18610` | 1,025 | UnwindData |  |
| 31 | `MtxCluGetVirtualServerToken` | `0x18A20` | 924 | UnwindData |  |
| 32 | `MtxCluIsClusterPresentExW` | `0x18DD0` | 61 | UnwindData |  |
| 33 | `MtxCluRemoveClusterTmMappingByName` | `0x19050` | 432 | UnwindData |  |
| 34 | `MtxCluSetClusterTmMapping` | `0x19310` | 1,155 | UnwindData |  |
| 35 | `MtxCluSetDefaultClusterResource` | `0x197A0` | 625 | UnwindData |  |
| 37 | `MtxCluVerifyLogPathInDependantDiskResource` | `0x1A840` | 1,087 | UnwindData |  |
| 38 | `MtxCluVerifyLogPathIsValidCSV` | `0x1AC90` | 564 | UnwindData |  |
| 9 | `Startup` | `0x20950` | 103 | UnwindData |  |
| 1 | `MtxCluGetComputerNameW` | `0x215F0` | 460 | UnwindData |  |
| 2 | `MtxCluGetDTCStatusW` | `0x217D0` | 296 | UnwindData |  |
| 3 | `MtxCluGetSecurityRegValue` | `0x21900` | 243 | UnwindData |  |
| 8 | `MtxCluSetSecurityRegValue` | `0x21A00` | 241 | UnwindData |  |
| 11 | `MtxCluBringOnlineDTCW` | `0x21B00` | 278 | UnwindData |  |
| 36 | `MtxCluTakeOfflineDTCW` | `0x21C20` | 278 | UnwindData |  |
| 4 | `MtxCluIsClusterPresent` | `0x23A10` | 29 | UnwindData |  |
| 5 | `MtxCluIsNetworkNameInLocalClusterW` | `0x23BA0` | 345 | UnwindData |  |
| 6 | `MtxCluIsSameClusterW` | `0x23E70` | 185 | UnwindData |  |
| 7 | `MtxCluIsSameNodeW` | `0x23F30` | 517 | UnwindData |  |
