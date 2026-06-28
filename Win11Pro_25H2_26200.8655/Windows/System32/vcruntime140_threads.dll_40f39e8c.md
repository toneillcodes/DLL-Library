# Binary Specification: vcruntime140_threads.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\vcruntime140_threads.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `40f39e8cee5f5a531b4010e18b807e8fe265b908dc58f959ecb7ebc6ea6cb11a`
* **Total Exported Functions:** 28

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 9 | `cnd_destroy` | `0x1420` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `mtx_destroy` | `0x1420` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `_cnd_timedwait32` | `0x15C0` | 271 | UnwindData |  |
| 2 | `_cnd_timedwait64` | `0x16D0` | 296 | UnwindData |  |
| 3 | `_mtx_timedlock32` | `0x1800` | 111 | UnwindData |  |
| 4 | `_mtx_timedlock64` | `0x1920` | 111 | UnwindData |  |
| 5 | `_thrd_sleep32` | `0x1A50` | 44 | UnwindData |  |
| 6 | `_thrd_sleep64` | `0x1A80` | 44 | UnwindData |  |
| 7 | `call_once` | `0x1AB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `cnd_broadcast` | `0x1AD0` | 17 | UnwindData |  |
| 10 | `cnd_init` | `0x1AF0` | 17 | UnwindData |  |
| 11 | `cnd_signal` | `0x1B10` | 17 | UnwindData |  |
| 12 | `cnd_wait` | `0x1B30` | 148 | UnwindData |  |
| 14 | `mtx_init` | `0x1BD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `mtx_lock` | `0x1BF0` | 58 | UnwindData |  |
| 16 | `mtx_trylock` | `0x1C30` | 108 | UnwindData |  |
| 17 | `mtx_unlock` | `0x1CA0` | 87 | UnwindData |  |
| 18 | `thrd_create` | `0x1D00` | 183 | UnwindData |  |
| 19 | `thrd_current` | `0x1DC0` | 34 | UnwindData |  |
| 20 | `thrd_detach` | `0x1DF0` | 32 | UnwindData |  |
| 21 | `thrd_equal` | `0x1E10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `thrd_exit` | `0x1E20` | 11 | UnwindData |  |
| 23 | `thrd_join` | `0x1E30` | 113 | UnwindData |  |
| 24 | `thrd_yield` | `0x1EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `tss_create` | `0x1EC0` | 252 | UnwindData |  |
| 26 | `tss_delete` | `0x1FC0` | 96 | UnwindData |  |
| 27 | `tss_get` | `0x2020` | 53 | UnwindData |  |
| 28 | `tss_set` | `0x20A0` | 275 | UnwindData |  |
