# Binary Specification: msvcp140_atomic_wait.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\msvcp140_atomic_wait.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3d0cbfaa1bf3eecf5a3f4491d2960ee803cb994f30292c6adc4a07c498f60e2b`
* **Total Exported Functions:** 32

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `__std_atomic_compare_exchange_128` | `0x1080` | 42 | UnwindData |  |
| 3 | `__std_atomic_get_mutex` | `0x10B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `__std_atomic_has_cmpxchg16b` | `0x10E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `__std_atomic_notify_all_direct` | `0x10F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `__std_atomic_notify_all_indirect` | `0x1100` | 166 | UnwindData |  |
| 7 | `__std_atomic_notify_one_direct` | `0x11B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `__std_atomic_notify_one_indirect` | `0x11C0` | 126 | UnwindData |  |
| 9 | `__std_atomic_set_api_level` | `0x1240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `__std_atomic_wait_direct` | `0x1250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `__std_atomic_wait_get_deadline` | `0x1260` | 39 | UnwindData |  |
| 12 | `__std_atomic_wait_get_remaining_timeout` | `0x1290` | 67 | UnwindData |  |
| 13 | `__std_atomic_wait_indirect` | `0x12E0` | 372 | UnwindData |  |
| 14 | `__std_bulk_submit_threadpool_work` | `0x1460` | 65 | UnwindData |  |
| 16 | `__std_close_threadpool_work` | `0x14B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `__std_create_threadpool_work` | `0x14C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `__std_execution_wait_on_uchar` | `0x14D0` | 35 | UnwindData |  |
| 19 | `__std_execution_wake_by_address_all` | `0x1500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `__std_parallel_algorithms_hw_threads` | `0x1510` | 31 | UnwindData |  |
| 23 | `__std_submit_threadpool_work` | `0x1530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `__std_wait_for_threadpool_work_callbacks` | `0x1540` | 1,888 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `__std_acquire_shared_mutex_for_instance` | `0x1CA0` | 314 | UnwindData |  |
| 22 | `__std_release_shared_mutex_for_instance` | `0x1DE0` | 131 | UnwindData |  |
| 15 | `__std_calloc_crt` | `0x21D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `__std_free_crt` | `0x21E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `__std_tzdb_delete_current_zone` | `0x21F0` | 41 | UnwindData |  |
| 25 | `__std_tzdb_delete_leap_seconds` | `0x2220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `__std_tzdb_delete_sys_info` | `0x2230` | 41 | UnwindData |  |
| 27 | `__std_tzdb_delete_time_zones` | `0x2260` | 22 | UnwindData |  |
| 28 | `__std_tzdb_get_current_zone` | `0x2300` | 469 | UnwindData |  |
| 29 | `__std_tzdb_get_leap_seconds` | `0x24E0` | 331 | UnwindData |  |
| 30 | `__std_tzdb_get_sys_info` | `0x2630` | 1,549 | UnwindData |  |
| 31 | `__std_tzdb_get_time_zones` | `0x2C40` | 1,775 | UnwindData |  |
