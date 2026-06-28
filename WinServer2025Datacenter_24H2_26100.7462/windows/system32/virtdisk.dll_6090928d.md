# Binary Specification: virtdisk.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\virtdisk.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6090928d934688e18284cbd8fa74439a88f94791594859f07fa0d7e8b5552649`
* **Total Exported Functions:** 29

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 15 | `GetStorageDependencyInformation` | `0x1010` | 11 | UnwindData |  |
| 10 | `DetachVirtualDisk` | `0x25F0` | 368 | UnwindData |  |
| 7 | `CreateVirtualDisk` | `0x2770` | 35 | UnwindData |  |
| 23 | `OpenVirtualDisk` | `0x4230` | 8 | UnwindData |  |
| 18 | `GetVirtualDiskOperationProgress` | `0x44B0` | 29 | UnwindData |  |
| 27 | `SetVirtualDiskInformation` | `0x4830` | 10 | UnwindData |  |
| 19 | `GetVirtualDiskPhysicalPath` | `0x4D70` | 10 | UnwindData |  |
| 1 | `AddVirtualDiskParent` | `0x64D0` | 468 | UnwindData |  |
| 14 | `GetAllAttachedVirtualDiskPhysicalPaths` | `0x76C0` | 733 | UnwindData |  |
| 16 | `GetVirtualDiskInformation` | `0x7D10` | 301 | UnwindData |  |
| 24 | `QueryChangesVirtualDisk` | `0x86C0` | 466 | UnwindData |  |
| 2 | `ApplySnapshotVhdSet` | `0x8BA0` | 189 | UnwindData |  |
| 4 | `BreakMirrorVirtualDisk` | `0x8C70` | 101 | UnwindData |  |
| 5 | `CompactVirtualDisk` | `0x8CE0` | 344 | UnwindData |  |
| 6 | `CompleteForkVirtualDisk` | `0x8E40` | 101 | UnwindData |  |
| 8 | `DeleteSnapshotVhdSet` | `0x8EB0` | 173 | UnwindData |  |
| 12 | `ExpandVirtualDisk` | `0x8F70` | 233 | UnwindData |  |
| 13 | `ForkVirtualDisk` | `0x9060` | 500 | UnwindData |  |
| 20 | `MergeVirtualDisk` | `0x9260` | 351 | UnwindData |  |
| 21 | `MirrorVirtualDisk` | `0x93D0` | 520 | UnwindData |  |
| 22 | `ModifyVhdSet` | `0x95E0` | 409 | UnwindData |  |
| 26 | `ResizeVirtualDisk` | `0x9780` | 361 | UnwindData |  |
| 29 | `TakeSnapshotVhdSet` | `0x99A0` | 257 | UnwindData |  |
| 3 | `AttachVirtualDisk` | `0x9E90` | 959 | UnwindData |  |
| 25 | `RawSCSIVirtualDisk` | `0xABF0` | 757 | UnwindData |  |
| 9 | `DeleteVirtualDiskMetadata` | `0xB980` | 121 | UnwindData |  |
| 11 | `EnumerateVirtualDiskMetadata` | `0xBA00` | 233 | UnwindData |  |
| 17 | `GetVirtualDiskMetadata` | `0xBAF0` | 282 | UnwindData |  |
| 28 | `SetVirtualDiskMetadata` | `0xBC10` | 134 | UnwindData |  |
