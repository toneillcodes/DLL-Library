# Binary Specification: msdart.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\msdart.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `143d26c867626a7f987377a30b1a674f13a290604816ff8cef9875127607996a`
* **Total Exported Functions:** 625

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 609 | `MPInitializeCriticalSection` | `0x11F0` | 92 | UnwindData |  |
| 610 | `MPInitializeCriticalSectionAndSpinCount` | `0x1520` | 35 | UnwindData |  |
| 612 | `MpHeapAlloc` | `0x17E0` | 64 | UnwindData |  |
| 608 | `MPDeleteCriticalSection` | `0x1A00` | 42 | UnwindData |  |
| 621 | `UMSEnterCSWraper` | `0x1C20` | 95 | UnwindData |  |
| 615 | `MpHeapFree` | `0x1CD0` | 84 | UnwindData |  |
| 623 | `mpFree` | `0x1E30` | 20 | UnwindData |  |
| 565 | `?_TryWriteLock@CReaderWriterLock3AR@@AEAA_NJ@Z` | `0x1F50` | 118 | UnwindData |  |
| 348 | `?ReadOrWriteLock@CReaderWriterLock3AR@@QEAA_NXZ` | `0x1FD0` | 93 | UnwindData |  |
| 353 | `?ReadOrWriteUnlock@CReaderWriterLock3AR@@QEAAX_N@Z` | `0x2040` | 38 | UnwindData |  |
| 464 | `?WriteUnlock@CReaderWriterLock3AR@@QEAAXXZ` | `0x2070` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 454 | `?WriteLock@CReaderWriterLock3AR@@QEAAXXZ` | `0x20B0` | 96 | UnwindData |  |
| 562 | `?_TryWriteLock2@CReaderWriterLock3AR@@AEAA_NXZ` | `0x2120` | 49 | UnwindData |  |
| 560 | `?_TryReadLockRecursive@CReaderWriterLock3AR@@AEAA_NXZ` | `0x2670` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 559 | `?_TryReadLockRecursive@CReaderWriterLock3@@AEAA_NXZ` | `0x26A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 611 | `MpGetHeapHandle` | `0x26D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 270 | `?IsWriteLocked@CReaderWriterLock3AR@@QEBA_NXZ` | `0x26E0` | 48 | UnwindData |  |
| 488 | `?_CmpExch@CReaderWriterLock2@@AEAA_NJJ@Z` | `0x2720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 489 | `?_CmpExch@CReaderWriterLock3@@AEAA_NJJ@Z` | `0x2720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 490 | `?_CmpExch@CReaderWriterLock3AR@@AEAA_NJJ@Z` | `0x2720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 491 | `?_CmpExch@CReaderWriterLock@@AEAA_NJJ@Z` | `0x2720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 624 | `mpMalloc` | `0x2740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 256 | `?IsWin2korLater@CMdVersionInfo@@SAHXZ` | `0x2760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 262 | `?IsWinNT@CMdVersionInfo@@SAHXZ` | `0x2760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 263 | `?IsWinNt4orLater@CMdVersionInfo@@SAHXZ` | `0x2760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 290 | `?LockType@?$CLockBase@$00$00$02$00$02$01@@SA?AW4LOCK_LOCKTYPE@@XZ` | `0x2760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 303 | `?MutexType@?$CLockBase@$00$00$02$00$02$01@@SA?AW4LOCK_RW_MUTEX@@XZ` | `0x2760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 304 | `?MutexType@?$CLockBase@$01$00$00$00$02$01@@SA?AW4LOCK_RW_MUTEX@@XZ` | `0x2760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 305 | `?MutexType@?$CLockBase@$02$00$00$00$00$00@@SA?AW4LOCK_RW_MUTEX@@XZ` | `0x2760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 306 | `?MutexType@?$CLockBase@$03$00$00$01$02$02@@SA?AW4LOCK_RW_MUTEX@@XZ` | `0x2760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 313 | `?NumSubTables@CLKRLinearHashTable@@QEBAHXZ` | `0x2760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 317 | `?PerLockSpin@?$CLockBase@$02$00$00$00$00$00@@SA?AW4LOCK_PERLOCK_SPIN@@XZ` | `0x2760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 329 | `?QueueType@?$CLockBase@$02$00$00$00$00$00@@SA?AW4LOCK_QUEUE_TYPE@@XZ` | `0x2760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 368 | `?Recursion@?$CLockBase@$01$00$00$00$02$01@@SA?AW4LOCK_RECURSION@@XZ` | `0x2760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 369 | `?Recursion@?$CLockBase@$02$00$00$00$00$00@@SA?AW4LOCK_RECURSION@@XZ` | `0x2760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 370 | `?Recursion@?$CLockBase@$03$00$00$01$02$02@@SA?AW4LOCK_RECURSION@@XZ` | `0x2760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 373 | `?Recursion@?$CLockBase@$06$01$00$00$02$01@@SA?AW4LOCK_RECURSION@@XZ` | `0x2760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 374 | `?Recursion@?$CLockBase@$07$01$00$00$02$01@@SA?AW4LOCK_RECURSION@@XZ` | `0x2760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 440 | `?WaitType@?$CLockBase@$00$00$02$00$02$01@@SA?AW4LOCK_WAIT_TYPE@@XZ` | `0x2760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 441 | `?WaitType@?$CLockBase@$01$00$00$00$02$01@@SA?AW4LOCK_WAIT_TYPE@@XZ` | `0x2760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 442 | `?WaitType@?$CLockBase@$02$00$00$00$00$00@@SA?AW4LOCK_WAIT_TYPE@@XZ` | `0x2760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 444 | `?WaitType@?$CLockBase@$04$01$01$00$02$01@@SA?AW4LOCK_WAIT_TYPE@@XZ` | `0x2760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 445 | `?WaitType@?$CLockBase@$05$01$01$00$02$01@@SA?AW4LOCK_WAIT_TYPE@@XZ` | `0x2760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 446 | `?WaitType@?$CLockBase@$06$01$00$00$02$01@@SA?AW4LOCK_WAIT_TYPE@@XZ` | `0x2760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 447 | `?WaitType@?$CLockBase@$07$01$00$00$02$01@@SA?AW4LOCK_WAIT_TYPE@@XZ` | `0x2760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 606 | `MPCSInitialize` | `0x2760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 361 | `?ReadUnlock@CReaderWriterLock3AR@@QEAAXXZ` | `0x2770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 616 | `MpHeapReAlloc` | `0x2790` | 61 | UnwindData |  |
| 419 | `?TryReadLock@CReaderWriterLock2@@QEAA_NXZ` | `0x2A20` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 420 | `?TryReadLock@CReaderWriterLock3@@QEAA_NXZ` | `0x2A20` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 421 | `?TryReadLock@CReaderWriterLock3AR@@QEAA_NXZ` | `0x2A20` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 555 | `?_TryReadLock@CReaderWriterLock2@@AEAA_NXZ` | `0x2AD0` | 1,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 556 | `?_TryReadLock@CReaderWriterLock3@@AEAA_NXZ` | `0x2AD0` | 1,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 557 | `?_TryReadLock@CReaderWriterLock3AR@@AEAA_NXZ` | `0x2AD0` | 1,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 341 | `?ReadLock@CReaderWriterLock3AR@@QEAAXXZ` | `0x2F20` | 48 | UnwindData |  |
| 30 | `??0CReaderWriterLock3AR@@QEAA@XZ` | `0x2F60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 350 | `?ReadOrWriteUnlock@CCritSec@@QEAAX_N@Z` | `0x2F80` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 355 | `?ReadUnlock@CCritSec@@QEAAXXZ` | `0x2F80` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 458 | `?WriteUnlock@CCritSec@@QEAAXXZ` | `0x2F80` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 622 | `mpCalloc` | `0x30E0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 600 | `FXMemAttach` | `0x3200` | 94 | UnwindData |  |
| 359 | `?ReadUnlock@CReaderWriterLock2@@QEAAXXZ` | `0x35E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 360 | `?ReadUnlock@CReaderWriterLock3@@QEAAXXZ` | `0x35E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 531 | `?_LockSpin@CReaderWriterLock3AR@@AEAAXW4SPIN_TYPE@1@@Z` | `0x3600` | 367 | UnwindData |  |
| 494 | `?_CurrentThreadId@CReaderWriterLock3AR@@CAJXZ` | `0x3780` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 495 | `?_CurrentThreadId@CSmallSpinLock@@CAJXZ` | `0x3780` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `??1CDoubleList@@QEAA@XZ` | `0x37A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `??1CFakeLock@@QEAA@XZ` | `0x37A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `??1CLockedDoubleList@@QEAA@XZ` | `0x37A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `??1CLockedSingleList@@QEAA@XZ` | `0x37A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `??1CReaderWriterLock2@@QEAA@XZ` | `0x37A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `??1CReaderWriterLock3@@QEAA@XZ` | `0x37A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `??1CReaderWriterLock3AR@@QEAA@XZ` | `0x37A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `??1CReaderWriterLock@@QEAA@XZ` | `0x37A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `??1CSingleList@@QEAA@XZ` | `0x37A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `??1CSmallSpinLock@@QEAA@XZ` | `0x37A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `??1CSpinLock@@QEAA@XZ` | `0x37A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `?ConvertExclusiveToShared@CCritSec@@QEAAXXZ` | `0x37A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `?ConvertExclusiveToShared@CFakeLock@@QEAAXXZ` | `0x37A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `?ConvertExclusiveToShared@CSmallSpinLock@@QEAAXXZ` | `0x37A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `?ConvertExclusiveToShared@CSpinLock@@QEAAXXZ` | `0x37A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `?ConvertSharedToExclusive@CCritSec@@QEAAXXZ` | `0x37A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `?ConvertSharedToExclusive@CFakeLock@@QEAAXXZ` | `0x37A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `?ConvertSharedToExclusive@CSmallSpinLock@@QEAAXXZ` | `0x37A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `?ConvertSharedToExclusive@CSpinLock@@QEAAXXZ` | `0x37A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 336 | `?ReadLock@CFakeLock@@QEAAXXZ` | `0x37A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 351 | `?ReadOrWriteUnlock@CFakeLock@@QEAAX_N@Z` | `0x37A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 356 | `?ReadUnlock@CFakeLock@@QEAAXXZ` | `0x37A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 410 | `?SetTableLockSpinCount@CLKRHashTable@@QEAAXG@Z` | `0x37A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 411 | `?SetTableLockSpinCount@CLKRLinearHashTable@@QEAAXG@Z` | `0x37A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 449 | `?WriteLock@CFakeLock@@QEAAXXZ` | `0x37A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 459 | `?WriteUnlock@CFakeLock@@QEAAXXZ` | `0x37A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 607 | `MPCSUninitialize` | `0x37A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 625 | `mpRealloc` | `0x37B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `??0CLockedDoubleList@@QEAA@XZ` | `0x37D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0CDoubleList@@QEAA@XZ` | `0x37F0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `??0CReaderWriterLock2@@QEAA@XZ` | `0x3850` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `??0CSmallSpinLock@@QEAA@XZ` | `0x3850` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `??0CSpinLock@@QEAA@XZ` | `0x3850` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 570 | `?_WriteLockSpin@CReaderWriterLock3AR@@AEAAXXZ` | `0x38B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 301 | `?MultiKeys@CLKRHashTable@@QEBA_NXZ` | `0x38F0` | 4,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 302 | `?MultiKeys@CLKRLinearHashTable@@QEBA_NXZ` | `0x38F0` | 4,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 403 | `?SetSpinCount@CFakeLock@@QEAA_NG@Z` | `0x38F0` | 4,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 404 | `?SetSpinCount@CReaderWriterLock2@@QEAA_NG@Z` | `0x38F0` | 4,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 405 | `?SetSpinCount@CReaderWriterLock3@@QEAA_NG@Z` | `0x38F0` | 4,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 406 | `?SetSpinCount@CReaderWriterLock3AR@@QEAA_NG@Z` | `0x38F0` | 4,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 407 | `?SetSpinCount@CReaderWriterLock@@QEAA_NG@Z` | `0x38F0` | 4,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 408 | `?SetSpinCount@CSmallSpinLock@@QEAA_NG@Z` | `0x38F0` | 4,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 409 | `?SetSpinCount@CSpinLock@@QEAA_NG@Z` | `0x38F0` | 4,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `??0CCritSec@@QEAA@XZ` | `0x48C0` | 50 | UnwindData |  |
| 6 | `??0CFakeLock@@QEAA@XZ` | `0x4900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `??4?$CLockBase@$00$00$02$00$02$01@@QEAAAEAV0@$$QEAV0@@Z` | `0x4900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `??4?$CLockBase@$00$00$02$00$02$01@@QEAAAEAV0@AEBV0@@Z` | `0x4900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `??4?$CLockBase@$01$00$00$00$02$01@@QEAAAEAV0@$$QEAV0@@Z` | `0x4900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `??4?$CLockBase@$01$00$00$00$02$01@@QEAAAEAV0@AEBV0@@Z` | `0x4900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `??4?$CLockBase@$02$00$00$00$00$00@@QEAAAEAV0@$$QEAV0@@Z` | `0x4900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `??4?$CLockBase@$02$00$00$00$00$00@@QEAAAEAV0@AEBV0@@Z` | `0x4900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `??4?$CLockBase@$03$00$00$01$02$02@@QEAAAEAV0@$$QEAV0@@Z` | `0x4900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `??4?$CLockBase@$03$00$00$01$02$02@@QEAAAEAV0@AEBV0@@Z` | `0x4900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `??4?$CLockBase@$04$01$01$00$02$01@@QEAAAEAV0@$$QEAV0@@Z` | `0x4900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `??4?$CLockBase@$04$01$01$00$02$01@@QEAAAEAV0@AEBV0@@Z` | `0x4900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `??4?$CLockBase@$05$01$01$00$02$01@@QEAAAEAV0@$$QEAV0@@Z` | `0x4900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `??4?$CLockBase@$05$01$01$00$02$01@@QEAAAEAV0@AEBV0@@Z` | `0x4900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `??4?$CLockBase@$06$01$00$00$02$01@@QEAAAEAV0@$$QEAV0@@Z` | `0x4900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `??4?$CLockBase@$06$01$00$00$02$01@@QEAAAEAV0@AEBV0@@Z` | `0x4900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `??4?$CLockBase@$07$01$00$00$02$01@@QEAAAEAV0@$$QEAV0@@Z` | `0x4900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `??4?$CLockBase@$07$01$00$00$02$01@@QEAAAEAV0@AEBV0@@Z` | `0x4900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `??4CFakeLock@@QEAAAEAV0@AEBV0@@Z` | `0x4900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `??4CMdVersionInfo@@QEAAAEAV0@$$QEAV0@@Z` | `0x4900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `??4CMdVersionInfo@@QEAAAEAV0@AEBV0@@Z` | `0x4900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 207 | `?HeadNode@CDoubleList@@QEBAQEBVCListEntry@@XZ` | `0x4900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `??0CLKRHashTableStats@@QEAA@XZ` | `0x4910` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `??0CLKRHashTable_Iterator@@IEAA@PEAVCLKRHashTable@@F@Z` | `0x4960` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `??0CLKRHashTable_Iterator@@QEAA@$$QEAV0@@Z` | `0x4990` | 58 | UnwindData |  |
| 11 | `??0CLKRHashTable_Iterator@@QEAA@AEBV0@@Z` | `0x4990` | 58 | UnwindData |  |
| 12 | `??0CLKRHashTable_Iterator@@QEAA@XZ` | `0x49D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `??0CLKRLinearHashTable_Iterator@@IEAA@PEAVCLKRLinearHashTable@@PEAVCNodeClump@@KF@Z` | `0x4A00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `??0CLKRLinearHashTable_Iterator@@QEAA@AEBV0@@Z` | `0x4A20` | 57 | UnwindData |  |
| 17 | `??0CLKRLinearHashTable_Iterator@@QEAA@XZ` | `0x4A60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `??0CLKRhashDefaultAllocator@@QEAA@XZ` | `0x4A80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `??0CLockedDoubleList@@QEAA@$$QEAV0@@Z` | `0x4AA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `??0CLockedDoubleList@@QEAA@AEBV0@@Z` | `0x4AA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `??4CLockedDoubleList@@QEAAAEAV0@$$QEAV0@@Z` | `0x4AA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `??4CLockedDoubleList@@QEAAAEAV0@AEBV0@@Z` | `0x4AA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `??0CLockedSingleList@@QEAA@$$QEAV0@@Z` | `0x4AC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `??0CLockedSingleList@@QEAA@AEBV0@@Z` | `0x4AC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `??4CLockedSingleList@@QEAAAEAV0@$$QEAV0@@Z` | `0x4AC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `??4CLockedSingleList@@QEAAAEAV0@AEBV0@@Z` | `0x4AC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `??0CLockedSingleList@@QEAA@XZ` | `0x4AE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `??0CReaderWriterLock2@@QEAA@AEBV0@@Z` | `0x4B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `??0CSmallSpinLock@@QEAA@AEBV0@@Z` | `0x4B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `??0CSpinLock@@QEAA@AEBV0@@Z` | `0x4B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `??4CReaderWriterLock2@@QEAAAEAV0@AEBV0@@Z` | `0x4B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `??4CSmallSpinLock@@QEAAAEAV0@AEBV0@@Z` | `0x4B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `??4CSpinLock@@QEAAAEAV0@AEBV0@@Z` | `0x4B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `??0CReaderWriterLock3@@QEAA@AEBV0@@Z` | `0x4B10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `??0CReaderWriterLock@@QEAA@AEBV0@@Z` | `0x4B10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `??4CReaderWriterLock3@@QEAAAEAV0@AEBV0@@Z` | `0x4B10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `??4CReaderWriterLock@@QEAAAEAV0@AEBV0@@Z` | `0x4B10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `??0CReaderWriterLock3@@QEAA@XZ` | `0x4B30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `??0CReaderWriterLock@@QEAA@XZ` | `0x4B30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `??0CReaderWriterLock3AR@@QEAA@AEBV0@@Z` | `0x4B50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `??4CReaderWriterLock3AR@@QEAAAEAV0@AEBV0@@Z` | `0x4B50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `??0CExFileOperation@@QEAA@XZ` | `0x4B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `??0CSingleList@@QEAA@XZ` | `0x4B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `??1CCritSec@@QEAA@XZ` | `0x4B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `??1CLKRHashTable_Iterator@@QEAA@XZ` | `0x4B90` | 23 | UnwindData |  |
| 46 | `??1CLKRLinearHashTable_Iterator@@QEAA@XZ` | `0x4BB0` | 19 | UnwindData |  |
| 72 | `??4CCritSec@@QEAAAEAV0@AEBV0@@Z` | `0x4BD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `??4CExFileOperation@@QEAAAEAV0@AEBV0@@Z` | `0x4BD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `??4CSingleList@@QEAAAEAV0@AEBV0@@Z` | `0x4BD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `??4CDoubleList@@QEAAAEAV0@AEBV0@@Z` | `0x4BF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `??4CEXAutoBackupFile@@QEAAAEAV0@AEBV0@@Z` | `0x4C10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `??4CLKRHashTableStats@@QEAAAEAV0@$$QEAV0@@Z` | `0x4C30` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `??4CLKRHashTableStats@@QEAAAEAV0@AEBV0@@Z` | `0x4CB0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `??4CLKRHashTable_Iterator@@QEAAAEAV0@$$QEAV0@@Z` | `0x4D50` | 58 | UnwindData |  |
| 80 | `??4CLKRHashTable_Iterator@@QEAAAEAV0@AEBV0@@Z` | `0x4D50` | 58 | UnwindData |  |
| 81 | `??4CLKRLinearHashTable_Iterator@@QEAAAEAV0@AEBV0@@Z` | `0x4D90` | 83 | UnwindData |  |
| 95 | `??8CLKRHashTable_Iterator@@QEBA_NAEBV0@@Z` | `0x4DF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `??8CLKRLinearHashTable_Iterator@@QEBA_NAEBV0@@Z` | `0x4E20` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `??9CLKRHashTable_Iterator@@QEBA_NAEBV0@@Z` | `0x4E50` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `??9CLKRLinearHashTable_Iterator@@QEBA_NAEBV0@@Z` | `0x4E80` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `?Alloc@CLKRhashDefaultAllocator@@UEAAPEAX_KW4Type@CLKRhashAllocator@@@Z` | `0x4EE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `?BucketIndex@CLKRHashTableStats@@SAJJ@Z` | `0x4F00` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `?BucketSize@CLKRHashTableStats@@SAJJ@Z` | `0x4F40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `?BucketSizes@CLKRHashTableStats@@SAPEBJXZ` | `0x4F60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `?ClassName@CCritSec@@SAPEBGXZ` | `0x4F70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `?ClassName@CFakeLock@@SAPEBGXZ` | `0x4F80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `?ClassName@CLKRHashTable@@SAPEBGXZ` | `0x4F90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `?ClassName@CLKRLinearHashTable@@SAPEBGXZ` | `0x4FA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `?ClassName@CLKRhashDefaultAllocator@@UEAAPEBGXZ` | `0x4FB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `?ClassName@CReaderWriterLock2@@SAPEBGXZ` | `0x4FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `?ClassName@CReaderWriterLock3@@SAPEBGXZ` | `0x4FD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `?ClassName@CReaderWriterLock3AR@@SAPEBGXZ` | `0x4FE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `?ClassName@CReaderWriterLock@@SAPEBGXZ` | `0x4FF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `?ClassName@CSmallSpinLock@@SAPEBGXZ` | `0x5000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `?ClassName@CSpinLock@@SAPEBGXZ` | `0x5010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `?Clear@CLKRLinearHashTable@@QEAAXXZ` | `0x5020` | 37 | UnwindData |  |
| 129 | `?ConvertExclusiveToShared@CLKRLinearHashTable@@QEBAXXZ` | `0x5050` | 28 | UnwindData |  |
| 130 | `?ConvertExclusiveToShared@CReaderWriterLock2@@QEAAXXZ` | `0x5080` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `?ConvertExclusiveToShared@CReaderWriterLock3@@QEAAXXZ` | `0x50B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `?ConvertExclusiveToShared@CReaderWriterLock3AR@@QEAAXXZ` | `0x50E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `?ConvertExclusiveToShared@CReaderWriterLock@@QEAAXXZ` | `0x5110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `?ConvertSharedToExclusive@CLKRLinearHashTable@@QEBAXXZ` | `0x5130` | 28 | UnwindData |  |
| 140 | `?ConvertSharedToExclusive@CReaderWriterLock2@@QEAAXXZ` | `0x5160` | 54 | UnwindData |  |
| 141 | `?ConvertSharedToExclusive@CReaderWriterLock3@@QEAAXXZ` | `0x51A0` | 76 | UnwindData |  |
| 142 | `?ConvertSharedToExclusive@CReaderWriterLock3AR@@QEAAXXZ` | `0x5200` | 77 | UnwindData |  |
| 143 | `?ConvertSharedToExclusive@CReaderWriterLock@@QEAAXXZ` | `0x5260` | 47 | UnwindData |  |
| 150 | `?DeleteKey@CLKRLinearHashTable@@QEAA?AW4LK_RETCODE@@_K@Z` | `0x52A0` | 54 | UnwindData |  |
| 152 | `?DeleteRecord@CLKRLinearHashTable@@QEAA?AW4LK_RETCODE@@PEBX@Z` | `0x52E0` | 82 | UnwindData |  |
| 153 | `?End@CLKRHashTable@@QEAA?AVCLKRHashTable_Iterator@@XZ` | `0x5340` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `?End@CLKRLinearHashTable@@QEAA?AVCLKRLinearHashTable_Iterator@@XZ` | `0x5370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `?FindKey@CLKRLinearHashTable@@QEBA?AW4LK_RETCODE@@_KPEAPEBX@Z` | `0x5390` | 87 | UnwindData |  |
| 171 | `?FindRecord@CLKRLinearHashTable@@QEBA?AW4LK_RETCODE@@PEBX@Z` | `0x53F0` | 82 | UnwindData |  |
| 172 | `?First@CDoubleList@@QEBAQEAVCListEntry@@XZ` | `0x5450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 173 | `?First@CLockedDoubleList@@QEAAQEAVCListEntry@@XZ` | `0x5460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 286 | `?Last@CDoubleList@@QEBAQEAVCListEntry@@XZ` | `0x5460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 174 | `?Free@CLKRhashDefaultAllocator@@UEAA_NPEAXW4Type@CLKRhashAllocator@@@Z` | `0x5470` | 27 | UnwindData |  |
| 175 | `?GetBackupFile@CEXAutoBackupFile@@QEAAHPEAPEAG@Z` | `0x54A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 178 | `?GetDefaultSpinAdjustmentFactor@CCritSec@@SANXZ` | `0x54C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `?GetDefaultSpinAdjustmentFactor@CFakeLock@@SANXZ` | `0x54D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 180 | `?GetDefaultSpinAdjustmentFactor@CReaderWriterLock2@@SANXZ` | `0x54E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `?GetDefaultSpinAdjustmentFactor@CReaderWriterLock3@@SANXZ` | `0x54F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 182 | `?GetDefaultSpinAdjustmentFactor@CReaderWriterLock3AR@@SANXZ` | `0x5500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `?GetDefaultSpinAdjustmentFactor@CReaderWriterLock@@SANXZ` | `0x5510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | `?GetDefaultSpinAdjustmentFactor@CSmallSpinLock@@SANXZ` | `0x5520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `?GetDefaultSpinAdjustmentFactor@CSpinLock@@SANXZ` | `0x5530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `?GetDefaultSpinCount@CCritSec@@SAGXZ` | `0x5540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 194 | `?GetSpinCount@CCritSec@@QEBAGXZ` | `0x5540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 187 | `?GetDefaultSpinCount@CFakeLock@@SAGXZ` | `0x5550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 188 | `?GetDefaultSpinCount@CReaderWriterLock2@@SAGXZ` | `0x5560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 196 | `?GetSpinCount@CReaderWriterLock2@@QEBAGXZ` | `0x5560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 189 | `?GetDefaultSpinCount@CReaderWriterLock3@@SAGXZ` | `0x5570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 197 | `?GetSpinCount@CReaderWriterLock3@@QEBAGXZ` | `0x5570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 205 | `?GetTableLockSpinCount@CLKRLinearHashTable@@QEBAGXZ` | `0x5570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `?GetDefaultSpinCount@CReaderWriterLock3AR@@SAGXZ` | `0x5580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 198 | `?GetSpinCount@CReaderWriterLock3AR@@QEBAGXZ` | `0x5580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 191 | `?GetDefaultSpinCount@CReaderWriterLock@@SAGXZ` | `0x5590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 199 | `?GetSpinCount@CReaderWriterLock@@QEBAGXZ` | `0x5590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 192 | `?GetDefaultSpinCount@CSmallSpinLock@@SAGXZ` | `0x55A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 200 | `?GetSpinCount@CSmallSpinLock@@QEBAGXZ` | `0x55A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 193 | `?GetDefaultSpinCount@CSpinLock@@SAGXZ` | `0x55B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | `?GetSpinCount@CSpinLock@@QEBAGXZ` | `0x55B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 195 | `?GetSpinCount@CFakeLock@@QEBAGXZ` | `0x55C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 226 | `?IsMillnm@CMdVersionInfo@@SAHXZ` | `0x55C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 255 | `?IsWin2k@CMdVersionInfo@@SAHXZ` | `0x55C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 257 | `?IsWin95@CMdVersionInfo@@SAHXZ` | `0x55C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 258 | `?IsWin98@CMdVersionInfo@@SAHXZ` | `0x55C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 259 | `?IsWin98orLater@CMdVersionInfo@@SAHXZ` | `0x55C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 260 | `?IsWin9x@CMdVersionInfo@@SAHXZ` | `0x55C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 261 | `?IsWinNT4@CMdVersionInfo@@SAHXZ` | `0x55C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 208 | `?HeadNode@CLockedDoubleList@@QEBAQEBVCListEntry@@XZ` | `0x55D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 209 | `?Increment@CLKRHashTable_Iterator@@QEAA_NXZ` | `0x55E0` | 41 | UnwindData |  |
| 210 | `?Increment@CLKRLinearHashTable_Iterator@@QEAA_NXZ` | `0x5610` | 41 | UnwindData |  |
| 214 | `?InsertHead@CDoubleList@@QEAAXQEAVCListEntry@@@Z` | `0x5640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 215 | `?InsertHead@CLockedDoubleList@@QEAAXQEAVCListEntry@@@Z` | `0x5660` | 70 | UnwindData |  |
| 217 | `?InsertRecord@CLKRLinearHashTable@@QEAA?AW4LK_RETCODE@@PEBX_NPEAPEBX@Z` | `0x56B0` | 131 | UnwindData |  |
| 218 | `?InsertTail@CDoubleList@@QEAAXQEAVCListEntry@@@Z` | `0x5740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 219 | `?InsertTail@CLockedDoubleList@@QEAAXQEAVCListEntry@@@Z` | `0x5760` | 71 | UnwindData |  |
| 220 | `?IsEmpty@CDoubleList@@QEBA_NXZ` | `0x57B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 221 | `?IsEmpty@CLockedDoubleList@@QEBA_NXZ` | `0x57C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `?IsEmpty@CLockedSingleList@@QEBA_NXZ` | `0x57E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 223 | `?IsEmpty@CSingleList@@QEBA_NXZ` | `0x57F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 224 | `?IsLocked@CLockedDoubleList@@QEBA_NXZ` | `0x5800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 225 | `?IsLocked@CLockedSingleList@@QEBA_NXZ` | `0x5800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 236 | `?IsReadLocked@CSpinLock@@QEBA_NXZ` | `0x5800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 273 | `?IsWriteLocked@CSpinLock@@QEBA_NXZ` | `0x5800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 227 | `?IsReadLocked@CCritSec@@QEBA_NXZ` | `0x5810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 228 | `?IsReadLocked@CFakeLock@@QEBA_NXZ` | `0x5810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 237 | `?IsReadUnlocked@CCritSec@@QEBA_NXZ` | `0x5810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 238 | `?IsReadUnlocked@CFakeLock@@QEBA_NXZ` | `0x5810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 264 | `?IsWriteLocked@CCritSec@@QEBA_NXZ` | `0x5810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 265 | `?IsWriteLocked@CFakeLock@@QEBA_NXZ` | `0x5810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 274 | `?IsWriteUnlocked@CCritSec@@QEBA_NXZ` | `0x5810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 275 | `?IsWriteUnlocked@CFakeLock@@QEBA_NXZ` | `0x5810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 346 | `?ReadOrWriteLock@CFakeLock@@QEAA_NXZ` | `0x5810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 418 | `?TryReadLock@CFakeLock@@QEAA_NXZ` | `0x5810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 428 | `?TryWriteLock@CFakeLock@@QEAA_NXZ` | `0x5810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 602 | `GetAllocCounters` | `0x5810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 230 | `?IsReadLocked@CLKRLinearHashTable@@QEBA_NXZ` | `0x5820` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 231 | `?IsReadLocked@CReaderWriterLock2@@QEBA_NXZ` | `0x5850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 232 | `?IsReadLocked@CReaderWriterLock3@@QEBA_NXZ` | `0x5850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 233 | `?IsReadLocked@CReaderWriterLock3AR@@QEBA_NXZ` | `0x5850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 234 | `?IsReadLocked@CReaderWriterLock@@QEBA_NXZ` | `0x5870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 235 | `?IsReadLocked@CSmallSpinLock@@QEBA_NXZ` | `0x5880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 240 | `?IsReadUnlocked@CLKRLinearHashTable@@QEBA_NXZ` | `0x5890` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 241 | `?IsReadUnlocked@CReaderWriterLock2@@QEBA_NXZ` | `0x58C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 242 | `?IsReadUnlocked@CReaderWriterLock3@@QEBA_NXZ` | `0x58C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 243 | `?IsReadUnlocked@CReaderWriterLock3AR@@QEBA_NXZ` | `0x58C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 244 | `?IsReadUnlocked@CReaderWriterLock@@QEBA_NXZ` | `0x58E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 245 | `?IsReadUnlocked@CSmallSpinLock@@QEBA_NXZ` | `0x58F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 282 | `?IsWriteUnlocked@CSmallSpinLock@@QEBA_NXZ` | `0x58F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 246 | `?IsReadUnlocked@CSpinLock@@QEBA_NXZ` | `0x5900` | 17 | UnwindData |  |
| 247 | `?IsUnlocked@CLockedDoubleList@@QEBA_NXZ` | `0x5900` | 17 | UnwindData |  |
| 248 | `?IsUnlocked@CLockedSingleList@@QEBA_NXZ` | `0x5900` | 17 | UnwindData |  |
| 283 | `?IsWriteUnlocked@CSpinLock@@QEBA_NXZ` | `0x5900` | 17 | UnwindData |  |
| 249 | `?IsUsable@CLKRHashTable@@QEBA_NXZ` | `0x5920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 250 | `?IsUsable@CLKRLinearHashTable@@QEBA_NXZ` | `0x5930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 252 | `?IsValid@CLKRHashTable_Iterator@@QEBA_NXZ` | `0x5940` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 254 | `?IsValid@CLKRLinearHashTable_Iterator@@QEBA_NXZ` | `0x5980` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 267 | `?IsWriteLocked@CLKRLinearHashTable@@QEBA_NXZ` | `0x59B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 268 | `?IsWriteLocked@CReaderWriterLock2@@QEBA_NXZ` | `0x59D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 269 | `?IsWriteLocked@CReaderWriterLock3@@QEBA_NXZ` | `0x59F0` | 41 | UnwindData |  |
| 271 | `?IsWriteLocked@CReaderWriterLock@@QEBA_NXZ` | `0x5A20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 272 | `?IsWriteLocked@CSmallSpinLock@@QEBA_NXZ` | `0x5A30` | 35 | UnwindData |  |
| 277 | `?IsWriteUnlocked@CLKRLinearHashTable@@QEBA_NXZ` | `0x5A60` | 34 | UnwindData |  |
| 278 | `?IsWriteUnlocked@CReaderWriterLock2@@QEBA_NXZ` | `0x5A90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 279 | `?IsWriteUnlocked@CReaderWriterLock3@@QEBA_NXZ` | `0x5AB0` | 17 | UnwindData |  |
| 280 | `?IsWriteUnlocked@CReaderWriterLock3AR@@QEBA_NXZ` | `0x5AD0` | 17 | UnwindData |  |
| 281 | `?IsWriteUnlocked@CReaderWriterLock@@QEBA_NXZ` | `0x5AF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 284 | `?Key@CLKRHashTable_Iterator@@QEBA?B_KXZ` | `0x5B00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 285 | `?Key@CLKRLinearHashTable_Iterator@@QEBA?B_KXZ` | `0x5B30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 287 | `?Last@CLockedDoubleList@@QEAAQEAVCListEntry@@XZ` | `0x5B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 288 | `?Lock@CLockedDoubleList@@QEAAXXZ` | `0x5B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 289 | `?Lock@CLockedSingleList@@QEAAXXZ` | `0x5B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 291 | `?LockType@?$CLockBase@$01$00$00$00$02$01@@SA?AW4LOCK_LOCKTYPE@@XZ` | `0x5B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 307 | `?MutexType@?$CLockBase@$04$01$01$00$02$01@@SA?AW4LOCK_RW_MUTEX@@XZ` | `0x5B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 308 | `?MutexType@?$CLockBase@$05$01$01$00$02$01@@SA?AW4LOCK_RW_MUTEX@@XZ` | `0x5B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 309 | `?MutexType@?$CLockBase@$06$01$00$00$02$01@@SA?AW4LOCK_RW_MUTEX@@XZ` | `0x5B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 310 | `?MutexType@?$CLockBase@$07$01$00$00$02$01@@SA?AW4LOCK_RW_MUTEX@@XZ` | `0x5B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 314 | `?NumSubTables@CLKRLinearHashTable@@SA?AW4LK_TABLESIZE@@AEAK0_N@Z` | `0x5B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 315 | `?PerLockSpin@?$CLockBase@$00$00$02$00$02$01@@SA?AW4LOCK_PERLOCK_SPIN@@XZ` | `0x5B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 316 | `?PerLockSpin@?$CLockBase@$01$00$00$00$02$01@@SA?AW4LOCK_PERLOCK_SPIN@@XZ` | `0x5B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 319 | `?PerLockSpin@?$CLockBase@$04$01$01$00$02$01@@SA?AW4LOCK_PERLOCK_SPIN@@XZ` | `0x5B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 320 | `?PerLockSpin@?$CLockBase@$05$01$01$00$02$01@@SA?AW4LOCK_PERLOCK_SPIN@@XZ` | `0x5B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 321 | `?PerLockSpin@?$CLockBase@$06$01$00$00$02$01@@SA?AW4LOCK_PERLOCK_SPIN@@XZ` | `0x5B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 322 | `?PerLockSpin@?$CLockBase@$07$01$00$00$02$01@@SA?AW4LOCK_PERLOCK_SPIN@@XZ` | `0x5B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 371 | `?Recursion@?$CLockBase@$04$01$01$00$02$01@@SA?AW4LOCK_RECURSION@@XZ` | `0x5B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 372 | `?Recursion@?$CLockBase@$05$01$01$00$02$01@@SA?AW4LOCK_RECURSION@@XZ` | `0x5B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 443 | `?WaitType@?$CLockBase@$03$00$00$01$02$02@@SA?AW4LOCK_WAIT_TYPE@@XZ` | `0x5B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 292 | `?LockType@?$CLockBase@$02$00$00$00$00$00@@SA?AW4LOCK_LOCKTYPE@@XZ` | `0x5B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 318 | `?PerLockSpin@?$CLockBase@$03$00$00$01$02$02@@SA?AW4LOCK_PERLOCK_SPIN@@XZ` | `0x5B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 327 | `?QueueType@?$CLockBase@$00$00$02$00$02$01@@SA?AW4LOCK_QUEUE_TYPE@@XZ` | `0x5B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 328 | `?QueueType@?$CLockBase@$01$00$00$00$02$01@@SA?AW4LOCK_QUEUE_TYPE@@XZ` | `0x5B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 330 | `?QueueType@?$CLockBase@$03$00$00$01$02$02@@SA?AW4LOCK_QUEUE_TYPE@@XZ` | `0x5B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 331 | `?QueueType@?$CLockBase@$04$01$01$00$02$01@@SA?AW4LOCK_QUEUE_TYPE@@XZ` | `0x5B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 332 | `?QueueType@?$CLockBase@$05$01$01$00$02$01@@SA?AW4LOCK_QUEUE_TYPE@@XZ` | `0x5B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 333 | `?QueueType@?$CLockBase@$06$01$00$00$02$01@@SA?AW4LOCK_QUEUE_TYPE@@XZ` | `0x5B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 334 | `?QueueType@?$CLockBase@$07$01$00$00$02$01@@SA?AW4LOCK_QUEUE_TYPE@@XZ` | `0x5B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 367 | `?Recursion@?$CLockBase@$00$00$02$00$02$01@@SA?AW4LOCK_RECURSION@@XZ` | `0x5B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 536 | `?_PredTrue@CLKRLinearHashTable@@CA?AW4LK_PREDICATE@@PEBXPEAX@Z` | `0x5B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 293 | `?LockType@?$CLockBase@$03$00$00$01$02$02@@SA?AW4LOCK_LOCKTYPE@@XZ` | `0x5BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 294 | `?LockType@?$CLockBase@$04$01$01$00$02$01@@SA?AW4LOCK_LOCKTYPE@@XZ` | `0x5BB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 295 | `?LockType@?$CLockBase@$05$01$01$00$02$01@@SA?AW4LOCK_LOCKTYPE@@XZ` | `0x5BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 296 | `?LockType@?$CLockBase@$06$01$00$00$02$01@@SA?AW4LOCK_LOCKTYPE@@XZ` | `0x5BD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 297 | `?LockType@?$CLockBase@$07$01$00$00$02$01@@SA?AW4LOCK_LOCKTYPE@@XZ` | `0x5BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 299 | `?MaxSize@CLKRLinearHashTable@@QEBAKXZ` | `0x5BF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 311 | `?NumSubTables@CLKRHashTable@@QEBAHXZ` | `0x5C20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 323 | `?Pop@CLockedSingleList@@QEAAQEAVCSingleListEntry@@XZ` | `0x5C30` | 58 | UnwindData |  |
| 324 | `?Pop@CSingleList@@QEAAQEAVCSingleListEntry@@XZ` | `0x5C70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 325 | `?Push@CLockedSingleList@@QEAAXQEAVCSingleListEntry@@@Z` | `0x5C90` | 64 | UnwindData |  |
| 326 | `?Push@CSingleList@@QEAAXQEAVCSingleListEntry@@@Z` | `0x5CE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 335 | `?ReadLock@CCritSec@@QEAAXXZ` | `0x5D00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 448 | `?WriteLock@CCritSec@@QEAAXXZ` | `0x5D00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 338 | `?ReadLock@CLKRLinearHashTable@@QEBAXXZ` | `0x5D10` | 28 | UnwindData |  |
| 339 | `?ReadLock@CReaderWriterLock2@@QEAAXXZ` | `0x5D40` | 45 | UnwindData |  |
| 340 | `?ReadLock@CReaderWriterLock3@@QEAAXXZ` | `0x5D80` | 48 | UnwindData |  |
| 342 | `?ReadLock@CReaderWriterLock@@QEAAXXZ` | `0x5DC0` | 49 | UnwindData |  |
| 343 | `?ReadLock@CSmallSpinLock@@QEAAXXZ` | `0x5E00` | 52 | UnwindData |  |
| 456 | `?WriteLock@CSmallSpinLock@@QEAAXXZ` | `0x5E00` | 52 | UnwindData |  |
| 344 | `?ReadLock@CSpinLock@@QEAAXXZ` | `0x5E40` | 58 | UnwindData |  |
| 457 | `?WriteLock@CSpinLock@@QEAAXXZ` | `0x5E40` | 58 | UnwindData |  |
| 345 | `?ReadOrWriteLock@CCritSec@@QEAA_NXZ` | `0x5E80` | 17 | UnwindData |  |
| 347 | `?ReadOrWriteLock@CReaderWriterLock3@@QEAA_NXZ` | `0x5EA0` | 74 | UnwindData |  |
| 349 | `?ReadOrWriteLock@CSpinLock@@QEAA_NXZ` | `0x5EF0` | 17 | UnwindData |  |
| 352 | `?ReadOrWriteUnlock@CReaderWriterLock3@@QEAAX_N@Z` | `0x5F10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 354 | `?ReadOrWriteUnlock@CSpinLock@@QEAAX_N@Z` | `0x5F30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 364 | `?ReadUnlock@CSpinLock@@QEAAXXZ` | `0x5F30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 436 | `?Unlock@CLockedDoubleList@@QEAAXXZ` | `0x5F30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 437 | `?Unlock@CLockedSingleList@@QEAAXXZ` | `0x5F30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 467 | `?WriteUnlock@CSpinLock@@QEAAXXZ` | `0x5F30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 567 | `?_Unlock@CSpinLock@@AEAAXXZ` | `0x5F30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 358 | `?ReadUnlock@CLKRLinearHashTable@@QEBAXXZ` | `0x5F50` | 28 | UnwindData |  |
| 362 | `?ReadUnlock@CReaderWriterLock@@QEAAXXZ` | `0x5F80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 363 | `?ReadUnlock@CSmallSpinLock@@QEAAXXZ` | `0x5F90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 466 | `?WriteUnlock@CSmallSpinLock@@QEAAXXZ` | `0x5F90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 365 | `?Record@CLKRHashTable_Iterator@@QEBAPEBXXZ` | `0x5FA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 366 | `?Record@CLKRLinearHashTable_Iterator@@QEBAPEBXXZ` | `0x5FC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 376 | `?RemoveEntry@CDoubleList@@SAXQEAVCListEntry@@@Z` | `0x5FE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 377 | `?RemoveEntry@CLockedDoubleList@@QEAAXQEAVCListEntry@@@Z` | `0x6000` | 61 | UnwindData |  |
| 378 | `?RemoveHead@CDoubleList@@QEAAQEAVCListEntry@@XZ` | `0x6050` | 27 | UnwindData |  |
| 379 | `?RemoveHead@CLockedDoubleList@@QEAAQEAVCListEntry@@XZ` | `0x6080` | 53 | UnwindData |  |
| 380 | `?RemoveTail@CDoubleList@@QEAAQEAVCListEntry@@XZ` | `0x60C0` | 28 | UnwindData |  |
| 381 | `?RemoveTail@CLockedDoubleList@@QEAAQEAVCListEntry@@XZ` | `0x60F0` | 53 | UnwindData |  |
| 385 | `?SetDefaultSpinAdjustmentFactor@CCritSec@@SAXN@Z` | `0x6130` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 386 | `?SetDefaultSpinAdjustmentFactor@CFakeLock@@SAXN@Z` | `0x6160` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 387 | `?SetDefaultSpinAdjustmentFactor@CReaderWriterLock2@@SAXN@Z` | `0x6190` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 388 | `?SetDefaultSpinAdjustmentFactor@CReaderWriterLock3@@SAXN@Z` | `0x61C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 389 | `?SetDefaultSpinAdjustmentFactor@CReaderWriterLock3AR@@SAXN@Z` | `0x61F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 390 | `?SetDefaultSpinAdjustmentFactor@CReaderWriterLock@@SAXN@Z` | `0x6220` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 391 | `?SetDefaultSpinAdjustmentFactor@CSmallSpinLock@@SAXN@Z` | `0x6250` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 392 | `?SetDefaultSpinAdjustmentFactor@CSpinLock@@SAXN@Z` | `0x6280` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 393 | `?SetDefaultSpinCount@CCritSec@@SAXG@Z` | `0x62B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 394 | `?SetDefaultSpinCount@CFakeLock@@SAXG@Z` | `0x62F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 395 | `?SetDefaultSpinCount@CReaderWriterLock2@@SAXG@Z` | `0x6330` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 396 | `?SetDefaultSpinCount@CReaderWriterLock3@@SAXG@Z` | `0x6370` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 397 | `?SetDefaultSpinCount@CReaderWriterLock3AR@@SAXG@Z` | `0x63B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 398 | `?SetDefaultSpinCount@CReaderWriterLock@@SAXG@Z` | `0x63F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 399 | `?SetDefaultSpinCount@CSmallSpinLock@@SAXG@Z` | `0x6430` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 400 | `?SetDefaultSpinCount@CSpinLock@@SAXG@Z` | `0x6470` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 401 | `?SetSpinCount@CCritSec@@QEAA_NG@Z` | `0x64B0` | 34 | UnwindData |  |
| 413 | `?Size@CLKRLinearHashTable@@QEBAKXZ` | `0x64E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 414 | `?Swap@CSingleList@@QEAAXAEAV1@@Z` | `0x64F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 415 | `?TryConvertSharedToExclusive@CReaderWriterLock3@@QEAA_NXZ` | `0x6510` | 61 | UnwindData |  |
| 416 | `?TryConvertSharedToExclusive@CReaderWriterLock3AR@@QEAA_NXZ` | `0x6560` | 62 | UnwindData |  |
| 417 | `?TryReadLock@CCritSec@@QEAA_NXZ` | `0x65B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 422 | `?TryReadLock@CReaderWriterLock@@QEAA_NXZ` | `0x65C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 423 | `?TryReadLock@CSmallSpinLock@@QEAA_NXZ` | `0x65F0` | 49 | UnwindData |  |
| 433 | `?TryWriteLock@CSmallSpinLock@@QEAA_NXZ` | `0x65F0` | 49 | UnwindData |  |
| 424 | `?TryReadLock@CSpinLock@@QEAA_NXZ` | `0x6630` | 55 | UnwindData |  |
| 434 | `?TryWriteLock@CSpinLock@@QEAA_NXZ` | `0x6630` | 55 | UnwindData |  |
| 425 | `?TryReadOrWriteLock@CReaderWriterLock3@@QEAA_NAEA_N@Z` | `0x6670` | 81 | UnwindData |  |
| 426 | `?TryReadOrWriteLock@CReaderWriterLock3AR@@QEAA_NAEA_N@Z` | `0x66D0` | 81 | UnwindData |  |
| 429 | `?TryWriteLock@CReaderWriterLock2@@QEAA_NXZ` | `0x6730` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 430 | `?TryWriteLock@CReaderWriterLock3@@QEAA_NXZ` | `0x6760` | 90 | UnwindData |  |
| 431 | `?TryWriteLock@CReaderWriterLock3AR@@QEAA_NXZ` | `0x67C0` | 91 | UnwindData |  |
| 432 | `?TryWriteLock@CReaderWriterLock@@QEAA_NXZ` | `0x6830` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 438 | `?ValidSignature@CLKRHashTable@@QEBA_NXZ` | `0x6860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 439 | `?ValidSignature@CLKRLinearHashTable@@QEBA_NXZ` | `0x6880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 451 | `?WriteLock@CLKRLinearHashTable@@QEAAXXZ` | `0x68A0` | 28 | UnwindData |  |
| 452 | `?WriteLock@CReaderWriterLock2@@QEAAXXZ` | `0x68D0` | 49 | UnwindData |  |
| 453 | `?WriteLock@CReaderWriterLock3@@QEAAXXZ` | `0x6910` | 100 | UnwindData |  |
| 455 | `?WriteLock@CReaderWriterLock@@QEAAXXZ` | `0x6980` | 38 | UnwindData |  |
| 461 | `?WriteUnlock@CLKRLinearHashTable@@QEBAXXZ` | `0x69B0` | 28 | UnwindData |  |
| 462 | `?WriteUnlock@CReaderWriterLock2@@QEAAXXZ` | `0x69E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 463 | `?WriteUnlock@CReaderWriterLock3@@QEAAXXZ` | `0x6A10` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 465 | `?WriteUnlock@CReaderWriterLock@@QEAAXXZ` | `0x6A50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 468 | `?_AddRef@CLKRLinearHashTable_Iterator@@IEBAXH@Z` | `0x6A60` | 48 | UnwindData |  |
| 469 | `?_AddRefRecord@CLKRLinearHashTable@@AEBAXPEBXH@Z` | `0x6AA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 477 | `?_Bucket@CLKRLinearHashTable@@AEBAQEAVCBucket@@K@Z` | `0x6AC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 478 | `?_BucketAddress@CLKRLinearHashTable@@AEBAKK@Z` | `0x6AF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 479 | `?_BucketLock@CLKRLinearHashTable@@AEBAXQEAVCBucket@@W4LK_LOCKTYPE@@@Z` | `0x6B10` | 42 | UnwindData |  |
| 480 | `?_BucketReadLock@CLKRLinearHashTable@@AEBAXQEAVCBucket@@@Z` | `0x6B40` | 27 | UnwindData |  |
| 481 | `?_BucketReadUnlock@CLKRLinearHashTable@@AEBAXQEAVCBucket@@@Z` | `0x6B70` | 27 | UnwindData |  |
| 482 | `?_BucketUnlock@CLKRLinearHashTable@@AEBAXQEAVCBucket@@W4LK_LOCKTYPE@@@Z` | `0x6BA0` | 42 | UnwindData |  |
| 483 | `?_BucketWriteLock@CLKRLinearHashTable@@AEBAXQEAVCBucket@@@Z` | `0x6BD0` | 27 | UnwindData |  |
| 484 | `?_BucketWriteUnlock@CLKRLinearHashTable@@AEBAXQEAVCBucket@@@Z` | `0x6C00` | 27 | UnwindData |  |
| 485 | `?_CalcKeyHash@CLKRHashTable@@AEBAK_K@Z` | `0x6C30` | 52 | UnwindData |  |
| 486 | `?_CalcKeyHash@CLKRLinearHashTable@@AEBAK_K@Z` | `0x6C30` | 52 | UnwindData |  |
| 493 | `?_CurrentThreadId@CReaderWriterLock3@@CAJXZ` | `0x6D50` | 25 | UnwindData |  |
| 496 | `?_CurrentThreadId@CSpinLock@@CAJXZ` | `0x6D50` | 25 | UnwindData |  |
| 501 | `?_EqualKeys@CLKRLinearHashTable@@AEBA_N_K0@Z` | `0x6D70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 504 | `?_ExtractKey@CLKRHashTable@@AEBA?B_KPEBX@Z` | `0x6D90` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 505 | `?_ExtractKey@CLKRLinearHashTable@@AEBA?B_KPEBX@Z` | `0x6D90` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 514 | `?_H0@CLKRLinearHashTable@@AEBAKK@Z` | `0x6E20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 515 | `?_H0@CLKRLinearHashTable@@CAKKK@Z` | `0x6E30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 516 | `?_H1@CLKRLinearHashTable@@AEBAKK@Z` | `0x6E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 517 | `?_H1@CLKRLinearHashTable@@CAKKK@Z` | `0x6E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 522 | `?_InsertThisIntoGlobalList@CLKRHashTable@@AEAAXXZ` | `0x6E60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 523 | `?_InsertThisIntoGlobalList@CLKRLinearHashTable@@AEAAXXZ` | `0x6E80` | 39 | UnwindData |  |
| 524 | `?_IsLocked@CSpinLock@@AEBA_NXZ` | `0x6F00` | 41 | UnwindData |  |
| 526 | `?_IsValidIterator@CLKRHashTable@@AEBA_NAEBVCLKRHashTable_Iterator@@@Z` | `0x6F30` | 51 | UnwindData |  |
| 527 | `?_IsValidIterator@CLKRLinearHashTable@@AEBA_NAEBVCLKRLinearHashTable_Iterator@@@Z` | `0x6F70` | 44 | UnwindData |  |
| 528 | `?_Lock@CSpinLock@@AEAAXXZ` | `0x6FB0` | 59 | UnwindData |  |
| 537 | `?_ReadLockSpin@CReaderWriterLock2@@AEAAXXZ` | `0x7000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 538 | `?_ReadLockSpin@CReaderWriterLock3@@AEAAXW4SPIN_TYPE@1@@Z` | `0x7010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 539 | `?_ReadLockSpin@CReaderWriterLock3AR@@AEAAXW4SPIN_TYPE@1@@Z` | `0x7020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 540 | `?_ReadLockSpin@CReaderWriterLock@@AEAAXXZ` | `0x7030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 541 | `?_ReadOrWriteLock@CLKRLinearHashTable@@AEBA_NXZ` | `0x7040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 542 | `?_ReadOrWriteUnlock@CLKRLinearHashTable@@AEBAX_N@Z` | `0x7060` | 41 | UnwindData |  |
| 543 | `?_RemoveThisFromGlobalList@CLKRHashTable@@AEAAXXZ` | `0x7090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 544 | `?_RemoveThisFromGlobalList@CLKRLinearHashTable@@AEAAXXZ` | `0x70B0` | 39 | UnwindData |  |
| 545 | `?_SegIndex@CLKRLinearHashTable@@AEBAKK@Z` | `0x70E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 546 | `?_Segment@CLKRLinearHashTable@@AEBAAEAPEAVCSegment@@K@Z` | `0x70F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 551 | `?_TableLock@CLKRLinearHashTable@@AEAAXW4LK_LOCKTYPE@@@Z` | `0x7110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 552 | `?_TableUnlock@CLKRLinearHashTable@@AEAAXW4LK_LOCKTYPE@@@Z` | `0x7130` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 553 | `?_TryLock@CSmallSpinLock@@AEAA_NXZ` | `0x71B0` | 49 | UnwindData |  |
| 554 | `?_TryLock@CSpinLock@@AEAA_NXZ` | `0x71F0` | 55 | UnwindData |  |
| 558 | `?_TryReadLock@CReaderWriterLock@@AEAA_NXZ` | `0x7230` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 561 | `?_TryWriteLock2@CReaderWriterLock3@@AEAA_NXZ` | `0x7270` | 55 | UnwindData |  |
| 563 | `?_TryWriteLock@CReaderWriterLock2@@AEAA_NJ@Z` | `0x72B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 564 | `?_TryWriteLock@CReaderWriterLock3@@AEAA_NJ@Z` | `0x72E0` | 84 | UnwindData |  |
| 566 | `?_TryWriteLock@CReaderWriterLock@@AEAA_NXZ` | `0x7340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 571 | `?_WriteLockSpin@CReaderWriterLock@@AEAAXXZ` | `0x7360` | 896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 574 | `?fHaveBackup@CEXAutoBackupFile@@QEAAHXZ` | `0x76E0` | 3,648 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 598 | `DllBidEntryPoint` | `0x8520` | 239 | UnwindData |  |
| 599 | `DllMain` | `0x8620` | 459 | UnwindData |  |
| 300 | `?MpHeapCompact@@YA_KPEAX@Z` | `0x8B90` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 613 | `MpHeapCreate` | `0x8C30` | 252 | UnwindData |  |
| 614 | `MpHeapDestroy` | `0x8D40` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `??0CEXAutoBackupFile@@QEAA@XZ` | `0x8DB0` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 603 | `GetIUMS` | `0x8FE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 619 | `SetIUMS` | `0x9000` | 1,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 601 | `FXMemDetach` | `0x94A0` | 97 | UnwindData |  |
| 617 | `MpHeapSize` | `0x9510` | 260 | UnwindData |  |
| 618 | `MpHeapValidate` | `0x9620` | 247 | UnwindData |  |
| 620 | `SetMemHook` | `0x9720` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | `?GetVersionExW@CMdVersionInfo@@SAHPEAU_OSVERSIONINFOW@@@Z` | `0x9C70` | 131 | UnwindData |  |
| 211 | `?InitializeVersionInfo@CMdVersionInfo@@CAHXZ` | `0x9D00` | 136 | UnwindData |  |
| 375 | `?ReleaseVersionInfo@CMdVersionInfo@@SAXXZ` | `0x9D90` | 36 | UnwindData |  |
| 146 | `?CreateHolder@@YAJPEAUIGPDispenser@@HIPEAPEAUIGPHolder@@@Z` | `0x9DC0` | 98 | UnwindData |  |
| 7 | `??0CLKRHashTable@@QEAA@PEBDP6A?B_KPEBX@ZP6AK_K@ZP6A_N33@ZP6AX1H@ZNKK_N7PEAVCLKRhashAllocator@@@Z` | `0xC450` | 555 | UnwindData |  |
| 13 | `??0CLKRLinearHashTable@@AEAA@PEBDP6A?B_KPEBX@ZP6AK_K@ZP6A_N33@ZP6AX1H@ZNKPEAVCLKRHashTable@@_N8PEAVCLKRhashAllocator@@@Z` | `0xC690` | 188 | UnwindData |  |
| 14 | `??0CLKRLinearHashTable@@QEAA@PEBDP6A?B_KPEBX@ZP6AK_K@ZP6A_N33@ZP6AX1H@ZNKK_N7PEAVCLKRhashAllocator@@@Z` | `0xC760` | 177 | UnwindData |  |
| 43 | `??1CLKRHashTable@@QEAA@XZ` | `0xC860` | 106 | UnwindData |  |
| 45 | `??1CLKRLinearHashTable@@QEAA@XZ` | `0xC8D0` | 60 | UnwindData |  |
| 101 | `?Apply@CLKRHashTable@@QEAAKP6A?AW4LK_ACTION@@PEBXPEAX@Z1W4LK_LOCKTYPE@@@Z` | `0xCA40` | 262 | UnwindData |  |
| 102 | `?Apply@CLKRLinearHashTable@@QEAAKP6A?AW4LK_ACTION@@PEBXPEAX@Z1W4LK_LOCKTYPE@@@Z` | `0xCB50` | 157 | UnwindData |  |
| 103 | `?ApplyIf@CLKRHashTable@@QEAAKP6A?AW4LK_PREDICATE@@PEBXPEAX@ZP6A?AW4LK_ACTION@@01@Z1W4LK_LOCKTYPE@@@Z` | `0xCC00` | 263 | UnwindData |  |
| 104 | `?ApplyIf@CLKRLinearHashTable@@QEAAKP6A?AW4LK_PREDICATE@@PEBXPEAX@ZP6A?AW4LK_ACTION@@01@Z1W4LK_LOCKTYPE@@@Z` | `0xCD10` | 167 | UnwindData |  |
| 106 | `?Begin@CLKRHashTable@@QEAA?AVCLKRHashTable_Iterator@@XZ` | `0xCDC0` | 129 | UnwindData |  |
| 107 | `?Begin@CLKRLinearHashTable@@QEAA?AVCLKRLinearHashTable_Iterator@@XZ` | `0xCE50` | 240 | UnwindData |  |
| 111 | `?CheckTable@CLKRHashTable@@QEBAHXZ` | `0xCF50` | 80 | UnwindData |  |
| 112 | `?CheckTable@CLKRLinearHashTable@@QEBAHXZ` | `0xCFB0` | 552 | UnwindData |  |
| 124 | `?Clear@CLKRHashTable@@QEAAXXZ` | `0xD1E0` | 65 | UnwindData |  |
| 128 | `?ConvertExclusiveToShared@CLKRHashTable@@QEBAXXZ` | `0xD260` | 52 | UnwindData |  |
| 138 | `?ConvertSharedToExclusive@CLKRHashTable@@QEBAXXZ` | `0xD2A0` | 52 | UnwindData |  |
| 147 | `?DeleteIf@CLKRHashTable@@QEAAKP6A?AW4LK_PREDICATE@@PEBXPEAX@Z1@Z` | `0xD2E0` | 196 | UnwindData |  |
| 148 | `?DeleteIf@CLKRLinearHashTable@@QEAAKP6A?AW4LK_PREDICATE@@PEBXPEAX@Z1@Z` | `0xD3B0` | 104 | UnwindData |  |
| 149 | `?DeleteKey@CLKRHashTable@@QEAA?AW4LK_RETCODE@@_K@Z` | `0xD420` | 110 | UnwindData |  |
| 151 | `?DeleteRecord@CLKRHashTable@@QEAA?AW4LK_RETCODE@@PEBX@Z` | `0xD4A0` | 138 | UnwindData |  |
| 155 | `?EqualRange@CLKRHashTable@@QEAA_N_KAEAVCLKRHashTable_Iterator@@1@Z` | `0xD530` | 337 | UnwindData |  |
| 156 | `?EqualRange@CLKRLinearHashTable@@QEAA_N_KAEAVCLKRLinearHashTable_Iterator@@1@Z` | `0xD690` | 273 | UnwindData |  |
| 157 | `?Erase@CLKRHashTable@@QEAA_NAEAVCLKRHashTable_Iterator@@0@Z` | `0xD7B0` | 307 | UnwindData |  |
| 158 | `?Erase@CLKRHashTable@@QEAA_NAEAVCLKRHashTable_Iterator@@@Z` | `0xD8F0` | 194 | UnwindData |  |
| 159 | `?Erase@CLKRLinearHashTable@@QEAA_NAEAVCLKRLinearHashTable_Iterator@@0@Z` | `0xD9C0` | 177 | UnwindData |  |
| 160 | `?Erase@CLKRLinearHashTable@@QEAA_NAEAVCLKRLinearHashTable_Iterator@@@Z` | `0xDA80` | 115 | UnwindData |  |
| 166 | `?Find@CLKRHashTable@@QEAA_N_KAEAVCLKRHashTable_Iterator@@@Z` | `0xDB00` | 282 | UnwindData |  |
| 167 | `?Find@CLKRLinearHashTable@@QEAA_N_KAEAVCLKRLinearHashTable_Iterator@@@Z` | `0xDC20` | 149 | UnwindData |  |
| 168 | `?FindKey@CLKRHashTable@@QEBA?AW4LK_RETCODE@@_KPEAPEBX@Z` | `0xDCC0` | 143 | UnwindData |  |
| 170 | `?FindRecord@CLKRHashTable@@QEBA?AW4LK_RETCODE@@PEBX@Z` | `0xDD60` | 138 | UnwindData |  |
| 176 | `?GetBucketLockSpinCount@CLKRHashTable@@QEBAGXZ` | `0xDDF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 177 | `?GetBucketLockSpinCount@CLKRLinearHashTable@@QEBAGXZ` | `0xDE20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | `?GetStatistics@CLKRHashTable@@QEBA?AVCLKRHashTableStats@@XZ` | `0xDE30` | 445 | UnwindData |  |
| 203 | `?GetStatistics@CLKRLinearHashTable@@QEBA?AVCLKRHashTableStats@@XZ` | `0xE000` | 761 | UnwindData |  |
| 204 | `?GetTableLockSpinCount@CLKRHashTable@@QEBAGXZ` | `0xE300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 212 | `?Insert@CLKRHashTable@@QEAA_NPEBXAEAVCLKRHashTable_Iterator@@_N@Z` | `0xE320` | 308 | UnwindData |  |
| 213 | `?Insert@CLKRLinearHashTable@@QEAA_NPEBXAEAVCLKRLinearHashTable_Iterator@@_N@Z` | `0xE460` | 182 | UnwindData |  |
| 216 | `?InsertRecord@CLKRHashTable@@QEAA?AW4LK_RETCODE@@PEBX_NPEAPEBX@Z` | `0xE520` | 187 | UnwindData |  |
| 229 | `?IsReadLocked@CLKRHashTable@@QEBA_NXZ` | `0xE5F0` | 75 | UnwindData |  |
| 239 | `?IsReadUnlocked@CLKRHashTable@@QEBA_NXZ` | `0xE650` | 75 | UnwindData |  |
| 251 | `?IsValid@CLKRHashTable@@QEBA_NXZ` | `0xE6B0` | 101 | UnwindData |  |
| 253 | `?IsValid@CLKRLinearHashTable@@QEBA_NXZ` | `0xE720` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 266 | `?IsWriteLocked@CLKRHashTable@@QEBA_NXZ` | `0xE7A0` | 75 | UnwindData |  |
| 276 | `?IsWriteUnlocked@CLKRHashTable@@QEBA_NXZ` | `0xE800` | 75 | UnwindData |  |
| 298 | `?MaxSize@CLKRHashTable@@QEBAKXZ` | `0xE860` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 312 | `?NumSubTables@CLKRHashTable@@SA?AW4LK_TABLESIZE@@AEAK0_N@Z` | `0xE8A0` | 167 | UnwindData |  |
| 337 | `?ReadLock@CLKRHashTable@@QEBAXXZ` | `0xE950` | 52 | UnwindData |  |
| 357 | `?ReadUnlock@CLKRHashTable@@QEBAXXZ` | `0xE990` | 70 | UnwindData |  |
| 383 | `?SetBucketLockSpinCount@CLKRHashTable@@QEAAXG@Z` | `0xE9E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 384 | `?SetBucketLockSpinCount@CLKRLinearHashTable@@QEAAXG@Z` | `0xEA10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 412 | `?Size@CLKRHashTable@@QEBAKXZ` | `0xEA20` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 450 | `?WriteLock@CLKRHashTable@@QEAAXXZ` | `0xEAA0` | 52 | UnwindData |  |
| 460 | `?WriteUnlock@CLKRHashTable@@QEBAXXZ` | `0xEAE0` | 70 | UnwindData |  |
| 470 | `?_AllocateNodeClump@CLKRLinearHashTable@@AEAAQEAVCNodeClump@@XZ` | `0xEB30` | 52 | UnwindData |  |
| 471 | `?_AllocateSegment@CLKRLinearHashTable@@AEBAQEAVCSegment@@XZ` | `0xEB70` | 303 | UnwindData |  |
| 472 | `?_AllocateSegmentDirectory@CLKRLinearHashTable@@AEAAQEAVCDirEntry@@_K@Z` | `0xECB0` | 106 | UnwindData |  |
| 473 | `?_AllocateSubTable@CLKRHashTable@@AEAAQEAVCLKRLinearHashTable@@PEBDP6A?B_KPEBX@ZP6AK_K@ZP6A_N33@ZP6AX1H@ZNKPEAV1@_N8@Z` | `0xED20` | 198 | UnwindData |  |
| 474 | `?_AllocateSubTableArray@CLKRHashTable@@AEAAQEAPEAVCLKRLinearHashTable@@_K@Z` | `0xEDF0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 475 | `?_Apply@CLKRLinearHashTable@@AEAAKP6A?AW4LK_ACTION@@PEBXPEAX@Z1W4LK_LOCKTYPE@@AEAW4LK_PREDICATE@@@Z` | `0xEE30` | 43 | UnwindData |  |
| 476 | `?_ApplyIf@CLKRLinearHashTable@@AEAAKP6A?AW4LK_PREDICATE@@PEBXPEAX@ZP6A?AW4LK_ACTION@@01@Z1W4LK_LOCKTYPE@@AEAW42@@Z` | `0xEE70` | 553 | UnwindData |  |
| 487 | `?_Clear@CLKRLinearHashTable@@AEAAX_N@Z` | `0xF0A0` | 515 | UnwindData |  |
| 492 | `?_Contract@CLKRLinearHashTable@@AEAA?AW4LK_RETCODE@@XZ` | `0xF2B0` | 761 | UnwindData |  |
| 497 | `?_DeleteIf@CLKRLinearHashTable@@AEAAKP6A?AW4LK_PREDICATE@@PEBXPEAX@Z1AEAW42@@Z` | `0xF5B0` | 423 | UnwindData |  |
| 498 | `?_DeleteKey@CLKRLinearHashTable@@AEAA?AW4LK_RETCODE@@_KK@Z` | `0xF760` | 430 | UnwindData |  |
| 499 | `?_DeleteNode@CLKRLinearHashTable@@AEAA_NQEAVCBucket@@AEAPEAVCNodeClump@@1AEAH@Z` | `0xF920` | 350 | UnwindData |  |
| 500 | `?_DeleteRecord@CLKRLinearHashTable@@AEAA?AW4LK_RETCODE@@PEBXK@Z` | `0xFA90` | 378 | UnwindData |  |
| 502 | `?_Erase@CLKRLinearHashTable@@AEAA_NAEAVCLKRLinearHashTable_Iterator@@K@Z` | `0xFC10` | 218 | UnwindData |  |
| 503 | `?_Expand@CLKRLinearHashTable@@AEAA?AW4LK_RETCODE@@XZ` | `0xFCF0` | 663 | UnwindData |  |
| 506 | `?_FindBucket@CLKRLinearHashTable@@AEBAQEAVCBucket@@K_N@Z` | `0xFF90` | 91 | UnwindData |  |
| 507 | `?_FindKey@CLKRLinearHashTable@@AEBA?AW4LK_RETCODE@@_KKPEAPEBXPEAVCLKRLinearHashTable_Iterator@@@Z` | `0x10000` | 355 | UnwindData |  |
| 508 | `?_FindRecord@CLKRLinearHashTable@@AEBA?AW4LK_RETCODE@@PEBXK@Z` | `0x10170` | 251 | UnwindData |  |
| 509 | `?_FreeNodeClump@CLKRLinearHashTable@@AEAA_NPEAVCNodeClump@@@Z` | `0x10280` | 37 | UnwindData |  |
| 510 | `?_FreeSegment@CLKRLinearHashTable@@AEBA_NPEAVCSegment@@@Z` | `0x102B0` | 131 | UnwindData |  |
| 511 | `?_FreeSegmentDirectory@CLKRLinearHashTable@@AEAA_NXZ` | `0x10340` | 56 | UnwindData |  |
| 512 | `?_FreeSubTable@CLKRHashTable@@AEAA_NPEAVCLKRLinearHashTable@@@Z` | `0x10380` | 63 | UnwindData |  |
| 513 | `?_FreeSubTableArray@CLKRHashTable@@AEAA_NPEAPEAVCLKRLinearHashTable@@@Z` | `0x103D0` | 34 | UnwindData |  |
| 518 | `?_Increment@CLKRHashTable_Iterator@@IEAA_N_N@Z` | `0x10400` | 190 | UnwindData |  |
| 519 | `?_Increment@CLKRLinearHashTable_Iterator@@IEAA_N_N@Z` | `0x104D0` | 377 | UnwindData |  |
| 520 | `?_Initialize@CLKRLinearHashTable@@AEAA?AW4LK_RETCODE@@P6A?B_KPEBX@ZP6AK_K@ZP6A_N22@ZP6AX0H@ZPEBDNK@Z` | `0x10650` | 352 | UnwindData |  |
| 521 | `?_InsertRecord@CLKRLinearHashTable@@AEAA?AW4LK_RETCODE@@PEBXK_NPEAPEBXPEAVCLKRLinearHashTable_Iterator@@@Z` | `0x107C0` | 646 | UnwindData |  |
| 525 | `?_IsNodeCompact@CLKRLinearHashTable@@AEBAHQEAVCBucket@@@Z` | `0x10A50` | 177 | UnwindData |  |
| 535 | `?_MergeRecordSets@CLKRLinearHashTable@@AEAA?AW4LK_RETCODE@@PEAVCBucket@@PEAVCNodeClump@@1@Z` | `0x10B10` | 339 | UnwindData |  |
| 547 | `?_SetSegVars@CLKRLinearHashTable@@AEAA?AW4LK_RETCODE@@W4LK_TABLESIZE@@K@Z` | `0x10C70` | 403 | UnwindData |  |
| 548 | `?_SplitRecordSet@CLKRLinearHashTable@@AEAA?AW4LK_RETCODE@@PEAVCNodeClump@@0KKK0@Z` | `0x10E10` | 399 | UnwindData |  |
| 549 | `?_SubTable@CLKRHashTable@@AEBAPEAVCLKRLinearHashTable@@K@Z` | `0x10FB0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 550 | `?_SubTableIndex@CLKRHashTable@@AEBAHPEAVCLKRLinearHashTable@@@Z` | `0x11000` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 402 | `?SetSpinCount@CCritSec@@SAKPEAPEAVCCriticalSection@@K@Z` | `0x11090` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 427 | `?TryWriteLock@CCritSec@@QEAA_NXZ` | `0x11110` | 23 | UnwindData |  |
| 529 | `?_LockSpin@CReaderWriterLock2@@AEAAX_N@Z` | `0x11130` | 289 | UnwindData |  |
| 530 | `?_LockSpin@CReaderWriterLock3@@AEAAXW4SPIN_TYPE@1@@Z` | `0x11260` | 366 | UnwindData |  |
| 532 | `?_LockSpin@CReaderWriterLock@@AEAAX_N@Z` | `0x113E0` | 279 | UnwindData |  |
| 533 | `?_LockSpin@CSmallSpinLock@@AEAAXXZ` | `0x11500` | 300 | UnwindData |  |
| 534 | `?_LockSpin@CSpinLock@@AEAAXXZ` | `0x11640` | 284 | UnwindData |  |
| 568 | `?_WriteLockSpin@CReaderWriterLock2@@AEAAXXZ` | `0x11770` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 569 | `?_WriteLockSpin@CReaderWriterLock3@@AEAAXXZ` | `0x117A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 604 | `IrtlAssert` | `0x117D0` | 49 | UnwindData |  |
| 605 | `IrtlTrace` | `0x11810` | 138 | UnwindData |  |
| 3 | `??0CEXAutoBackupFile@@QEAA@PEBG@Z` | `0x12060` | 100 | UnwindData |  |
| 40 | `??1CEXAutoBackupFile@@QEAA@XZ` | `0x120D0` | 45 | UnwindData |  |
| 41 | `??1CExFileOperation@@QEAA@XZ` | `0x12110` | 33 | UnwindData |  |
| 105 | `?BackupFile@CEXAutoBackupFile@@QEAAJPEBG@Z` | `0x12140` | 439 | UnwindData |  |
| 161 | `?FOCopyFile@CExFileOperation@@QEAAJPEBG0H@Z` | `0x12300` | 166 | UnwindData |  |
| 162 | `?FOCopyFileDACLS@CExFileOperation@@QEAAJPEBG0@Z` | `0x123B0` | 48 | UnwindData |  |
| 163 | `?FODeleteFile@CExFileOperation@@QEAAJPEBG@Z` | `0x123F0` | 85 | UnwindData |  |
| 164 | `?FOMoveFile@CExFileOperation@@QEAAJPEBG0@Z` | `0x12450` | 88 | UnwindData |  |
| 165 | `?FOReplaceFile@CExFileOperation@@QEAAJPEBG0@Z` | `0x124B0` | 103 | UnwindData |  |
| 382 | `?RestoreFile@CEXAutoBackupFile@@QEAAJXZ` | `0x12520` | 107 | UnwindData |  |
| 435 | `?UndoBackup@CEXAutoBackupFile@@QEAAJXZ` | `0x12640` | 85 | UnwindData |  |
| 572 | `?_getFileSecurity@CExFileOperation@@AEAAJPEBG@Z` | `0x126A0` | 234 | UnwindData |  |
| 573 | `?_setFileSecurity@CExFileOperation@@AEAAJPEBG@Z` | `0x12790` | 108 | UnwindData |  |
| 99 | `??_7CLKRhashDefaultAllocator@@6B@` | `0x15ED8` | 9,496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 575 | `?s_aBucketSizes@?1??BucketSizes@CLKRHashTableStats@@SAPEBJXZ@4QBJB` | `0x183F0` | 52,704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 576 | `?sm_DefaultAllocator@CLKRHashTable@@0VCLKRhashDefaultAllocator@@A` | `0x251D0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 586 | `?sm_llGlobalList@CLKRLinearHashTable@@0VCLockedDoubleList@@A` | `0x251D8` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 585 | `?sm_llGlobalList@CLKRHashTable@@0VCLockedDoubleList@@A` | `0x251F0` | 440 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 582 | `?sm_dblDfltSpinAdjFctr@CReaderWriterLock@@1NA` | `0x253A8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 597 | `?sm_wDefaultSpinCount@CSpinLock@@1GA` | `0x253B0` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 596 | `?sm_wDefaultSpinCount@CSmallSpinLock@@1GA` | `0x253B4` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 592 | `?sm_wDefaultSpinCount@CReaderWriterLock2@@1GA` | `0x253B8` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 594 | `?sm_wDefaultSpinCount@CReaderWriterLock3AR@@1GA` | `0x253BC` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 595 | `?sm_wDefaultSpinCount@CReaderWriterLock@@1GA` | `0x253C0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 581 | `?sm_dblDfltSpinAdjFctr@CReaderWriterLock3AR@@1NA` | `0x253C8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 590 | `?sm_wDefaultSpinCount@CCritSec@@1GA` | `0x253D0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 580 | `?sm_dblDfltSpinAdjFctr@CReaderWriterLock3@@1NA` | `0x253D8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 578 | `?sm_dblDfltSpinAdjFctr@CFakeLock@@1NA` | `0x253E0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 593 | `?sm_wDefaultSpinCount@CReaderWriterLock3@@1GA` | `0x253E8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 584 | `?sm_dblDfltSpinAdjFctr@CSpinLock@@1NA` | `0x253F0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 579 | `?sm_dblDfltSpinAdjFctr@CReaderWriterLock2@@1NA` | `0x253F8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 591 | `?sm_wDefaultSpinCount@CFakeLock@@1GA` | `0x25400` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 583 | `?sm_dblDfltSpinAdjFctr@CSmallSpinLock@@1NA` | `0x25408` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 577 | `?sm_dblDfltSpinAdjFctr@CCritSec@@1NA` | `0x25410` | 1,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 589 | `?sm_pfnTryEnterCriticalSection@CCriticalSection@@0P6AHPEAU_RTL_CRITICAL_SECTION@@@ZEA` | `0x25B10` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 588 | `?sm_pfnSetCriticalSectionSpinCount@CCriticalSection@@0P6AKPEAU_RTL_CRITICAL_SECTION@@K@ZEA` | `0x25B18` | 216 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 587 | `?sm_lpOSVERSIONINFO@CMdVersionInfo@@0PEAU_OSVERSIONINFOW@@EA` | `0x25BF0` | 0 | Indeterminate |  |
