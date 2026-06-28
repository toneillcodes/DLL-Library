# Binary Specification: wiarpc.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wiarpc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `edcd133304726d0dc2088a9e4fee99b9d7b708668d535d7e627f3fea58d686b6`
* **Total Exported Functions:** 13

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `??0BUFFER@@QEAA@I@Z` | `0x3B80` | 36 | UnwindData |  |
| 2 | `??0BUFFER_CHAIN@@QEAA@XZ` | `0x3BB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0BUFFER_CHAIN_ITEM@@QEAA@I@Z` | `0x3BD0` | 45 | UnwindData |  |
| 4 | `??1BUFFER@@QEAA@XZ` | `0x3D50` | 30 | UnwindData |  |
| 5 | `??1BUFFER_CHAIN@@QEAA@XZ` | `0x3D80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `??1BUFFER_CHAIN_ITEM@@QEAA@XZ` | `0x3D90` | 50 | UnwindData |  |
| 7 | `??_FBUFFER@@QEAAXXZ` | `0x3EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `??_FBUFFER_CHAIN_ITEM@@QEAAXXZ` | `0x3F00` | 8,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `?QueryPtr@BUFFER@@QEBAPEAXXZ` | `0x5E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `?QuerySize@BUFFER@@QEBAIXZ` | `0x5E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `?QueryUsed@BUFFER_CHAIN_ITEM@@QEBAKXZ` | `0x5E60` | 1,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `ServiceMain` | `0x6300` | 1,223 | UnwindData |  |
| 13 | `?SetUsed@BUFFER_CHAIN_ITEM@@QEAAXK@Z` | `0x6B30` | 36,256 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
