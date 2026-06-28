# Binary Specification: vcruntime140_threads.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\vcruntime140_threads.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `219915cf20822f34d5e7c1fdd4e21ae7f3396881096c51036225fb8f84b47afa`
* **Total Exported Functions:** 28

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 9 | `cnd_destroy` | `0x1470` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `mtx_destroy` | `0x1470` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `_cnd_timedwait32` | `0x14C0` | 246 | UnwindData |  |
| 2 | `_cnd_timedwait64` | `0x15C0` | 270 | UnwindData |  |
| 3 | `_mtx_timedlock32` | `0x16D0` | 236 | UnwindData |  |
| 4 | `_mtx_timedlock64` | `0x17C0` | 248 | UnwindData |  |
| 5 | `_thrd_sleep32` | `0x18C0` | 41 | UnwindData |  |
| 6 | `_thrd_sleep64` | `0x18F0` | 41 | UnwindData |  |
| 7 | `call_once` | `0x1920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `cnd_broadcast` | `0x1940` | 17 | UnwindData |  |
| 10 | `cnd_init` | `0x1960` | 17 | UnwindData |  |
| 11 | `cnd_signal` | `0x1980` | 17 | UnwindData |  |
| 12 | `cnd_wait` | `0x19A0` | 125 | UnwindData |  |
| 14 | `mtx_init` | `0x1A20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `mtx_lock` | `0x1A40` | 58 | UnwindData |  |
| 16 | `mtx_trylock` | `0x1A80` | 115 | UnwindData |  |
| 17 | `mtx_unlock` | `0x1B00` | 58 | UnwindData |  |
| 18 | `thrd_create` | `0x1B40` | 198 | UnwindData |  |
| 19 | `thrd_current` | `0x1C10` | 34 | UnwindData |  |
| 20 | `thrd_detach` | `0x1C40` | 27 | UnwindData |  |
| 21 | `thrd_equal` | `0x1C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `thrd_exit` | `0x1C70` | 11 | UnwindData |  |
| 23 | `thrd_join` | `0x1C80` | 97 | UnwindData |  |
| 24 | `thrd_yield` | `0x1CF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `tss_create` | `0x1D00` | 239 | UnwindData |  |
| 26 | `tss_delete` | `0x1DF0` | 81 | UnwindData |  |
| 27 | `tss_get` | `0x1E50` | 98 | UnwindData |  |
| 28 | `tss_set` | `0x1EC0` | 255 | UnwindData |  |
