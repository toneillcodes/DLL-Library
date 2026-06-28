# Binary Specification: vcruntime140_threadsd.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\vcruntime140_threadsd.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `cef5fe7055e83b065dcfdad3a86a715abc27eb61eed591d1ad7389bd4a741f9c`
* **Total Exported Functions:** 28

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `_cnd_timedwait32` | `0x2C00` | 44 | UnwindData |  |
| 2 | `_cnd_timedwait64` | `0x2C30` | 44 | UnwindData |  |
| 3 | `_mtx_timedlock32` | `0x2C60` | 34 | UnwindData |  |
| 4 | `_mtx_timedlock64` | `0x2C90` | 34 | UnwindData |  |
| 5 | `_thrd_sleep32` | `0x2CC0` | 34 | UnwindData |  |
| 6 | `_thrd_sleep64` | `0x2CF0` | 34 | UnwindData |  |
| 7 | `call_once` | `0x2D20` | 59 | UnwindData |  |
| 8 | `cnd_broadcast` | `0x2D60` | 30 | UnwindData |  |
| 9 | `cnd_destroy` | `0x2D80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `cnd_init` | `0x2D90` | 30 | UnwindData |  |
| 11 | `cnd_signal` | `0x2DB0` | 30 | UnwindData |  |
| 12 | `cnd_wait` | `0x2DD0` | 200 | UnwindData |  |
| 13 | `mtx_destroy` | `0x2EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `mtx_init` | `0x2EB0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `mtx_lock` | `0x2F00` | 65 | UnwindData |  |
| 16 | `mtx_trylock` | `0x2F50` | 225 | UnwindData |  |
| 17 | `mtx_unlock` | `0x3040` | 65 | UnwindData |  |
| 18 | `thrd_create` | `0x3090` | 252 | UnwindData |  |
| 19 | `thrd_current` | `0x3190` | 45 | UnwindData |  |
| 20 | `thrd_detach` | `0x31C0` | 41 | UnwindData |  |
| 21 | `thrd_equal` | `0x31F0` | 56 | UnwindData |  |
| 22 | `thrd_exit` | `0x3230` | 24 | UnwindData |  |
| 23 | `thrd_join` | `0x3250` | 136 | UnwindData |  |
| 24 | `thrd_yield` | `0x32E0` | 16 | UnwindData |  |
| 25 | `tss_create` | `0x32F0` | 41 | UnwindData |  |
| 26 | `tss_delete` | `0x3320` | 30 | UnwindData |  |
| 27 | `tss_get` | `0x3340` | 29 | UnwindData |  |
| 28 | `tss_set` | `0x3360` | 39 | UnwindData |  |
