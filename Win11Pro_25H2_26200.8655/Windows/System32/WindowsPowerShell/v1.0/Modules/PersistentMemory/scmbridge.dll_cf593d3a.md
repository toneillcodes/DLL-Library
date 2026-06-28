# Binary Specification: scmbridge.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\WindowsPowerShell\v1.0\Modules\PersistentMemory\scmbridge.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `cf593d3aa245433650e4ccff355c53746897a7b841afd9b682c5b4f866c9cfd2`
* **Total Exported Functions:** 19

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `ScmDeleteAllSimulatedPmemDisks` | `0x25390` | 41 | UnwindData |  |
| 2 | `ScmDeletePmemDisk` | `0x253C0` | 41 | UnwindData |  |
| 3 | `ScmDeletePmemDm` | `0x253F0` | 41 | UnwindData |  |
| 4 | `ScmGetDiskNumberFromDiskGuid` | `0x25420` | 50 | UnwindData |  |
| 5 | `ScmGetLogicalPmemDiskByDiskNumber` | `0x25460` | 50 | UnwindData |  |
| 6 | `ScmGetLogicalPmemDisks` | `0x254A0` | 50 | UnwindData |  |
| 7 | `ScmGetLogicalPmemDmByDeviceNumber` | `0x254E0` | 50 | UnwindData |  |
| 8 | `ScmGetLogicalPmemDms` | `0x25520` | 50 | UnwindData |  |
| 9 | `ScmGetPhysicalNvdimmByNfitHandle` | `0x25560` | 50 | UnwindData |  |
| 10 | `ScmGetPhysicalNvdimms` | `0x255A0` | 50 | UnwindData |  |
| 11 | `ScmGetUnusedPmemRegionById` | `0x255E0` | 50 | UnwindData |  |
| 12 | `ScmGetUnusedPmemRegions` | `0x25620` | 50 | UnwindData |  |
| 13 | `ScmInitializePmemPhysicalDevice` | `0x25660` | 41 | UnwindData |  |
| 14 | `ScmNewPmemDiskFromUnusedRegion` | `0x25690` | 79 | UnwindData |  |
| 15 | `ScmNewPmemDmFromUnusedRegion` | `0x256F0` | 62 | UnwindData |  |
| 16 | `ScmNewSimulatedPmemDisk` | `0x25740` | 62 | UnwindData |  |
| 17 | `ScmRebuildStacks` | `0x25790` | 41 | UnwindData |  |
| 18 | `ScmRefreshNamespace` | `0x257C0` | 41 | UnwindData |  |
| 19 | `ScmSetPmemDmState` | `0x257F0` | 50 | UnwindData |  |
