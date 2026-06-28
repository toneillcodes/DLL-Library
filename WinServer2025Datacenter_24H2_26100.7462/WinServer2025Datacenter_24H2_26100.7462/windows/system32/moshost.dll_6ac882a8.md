# Binary Specification: moshost.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\moshost.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6ac882a82c8f453c6fa6defb3ab57cb6f0cf04dd6592c7c1876762b870f5f0e8`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `MosHostCacheStateGetSizes` | `0x7870` | 19,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `MosHostCacheStateGetSlotToCleanup` | `0x7870` | 19,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `MosHostCacheStateSetMaxSize` | `0x7870` | 19,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `MosHostCacheStateSetSlotSize` | `0x7870` | 19,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `MosHostCacheStateSnapshot` | `0x7870` | 19,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `MosHostCacheStateUnuseSlot` | `0x7870` | 19,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `MosHostCacheStateUseSlot` | `0x7870` | 19,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `MosHostRequestResourceLock` | `0x7870` | 19,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `MosHostRequestResourceUnlock` | `0x7870` | 19,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `ServiceMain` | `0xC640` | 521 | UnwindData |  |
| 2 | `SvchostPushServiceGlobals` | `0xCA60` | 755 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
