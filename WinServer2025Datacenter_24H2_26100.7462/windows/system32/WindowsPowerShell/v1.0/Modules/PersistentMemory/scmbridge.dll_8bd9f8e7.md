# Binary Specification: scmbridge.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\WindowsPowerShell\v1.0\Modules\PersistentMemory\scmbridge.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8bd9f8e7fa2b25fa2e8162c6b50e819499b3c53987085846bc367229093a9558`
* **Total Exported Functions:** 19

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `ScmDeleteAllSimulatedPmemDisks` | `0x25380` | 41 | UnwindData |  |
| 2 | `ScmDeletePmemDisk` | `0x253B0` | 41 | UnwindData |  |
| 3 | `ScmDeletePmemDm` | `0x253E0` | 41 | UnwindData |  |
| 4 | `ScmGetDiskNumberFromDiskGuid` | `0x25410` | 50 | UnwindData |  |
| 5 | `ScmGetLogicalPmemDiskByDiskNumber` | `0x25450` | 50 | UnwindData |  |
| 6 | `ScmGetLogicalPmemDisks` | `0x25490` | 50 | UnwindData |  |
| 7 | `ScmGetLogicalPmemDmByDeviceNumber` | `0x254D0` | 50 | UnwindData |  |
| 8 | `ScmGetLogicalPmemDms` | `0x25510` | 50 | UnwindData |  |
| 9 | `ScmGetPhysicalNvdimmByNfitHandle` | `0x25550` | 50 | UnwindData |  |
| 10 | `ScmGetPhysicalNvdimms` | `0x25590` | 50 | UnwindData |  |
| 11 | `ScmGetUnusedPmemRegionById` | `0x255D0` | 50 | UnwindData |  |
| 12 | `ScmGetUnusedPmemRegions` | `0x25610` | 50 | UnwindData |  |
| 13 | `ScmInitializePmemPhysicalDevice` | `0x25650` | 41 | UnwindData |  |
| 14 | `ScmNewPmemDiskFromUnusedRegion` | `0x25680` | 79 | UnwindData |  |
| 15 | `ScmNewPmemDmFromUnusedRegion` | `0x256E0` | 62 | UnwindData |  |
| 16 | `ScmNewSimulatedPmemDisk` | `0x25730` | 62 | UnwindData |  |
| 17 | `ScmRebuildStacks` | `0x25780` | 41 | UnwindData |  |
| 18 | `ScmRefreshNamespace` | `0x257B0` | 41 | UnwindData |  |
| 19 | `ScmSetPmemDmState` | `0x257E0` | 50 | UnwindData |  |
