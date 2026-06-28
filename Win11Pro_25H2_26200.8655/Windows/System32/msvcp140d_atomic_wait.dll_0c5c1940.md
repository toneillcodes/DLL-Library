# Binary Specification: msvcp140d_atomic_wait.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\msvcp140d_atomic_wait.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0c5c194078138548fea061c560c41f3008c285f7b79873f34fc461c7446a06de`
* **Total Exported Functions:** 32

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `__std_atomic_compare_exchange_128` | `0x1210` | 108 | UnwindData |  |
| 3 | `__std_atomic_get_mutex` | `0x1280` | 121 | UnwindData |  |
| 4 | `__std_atomic_has_cmpxchg16b` | `0x1300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `__std_atomic_notify_all_direct` | `0x1310` | 25 | UnwindData |  |
| 6 | `__std_atomic_notify_all_indirect` | `0x1330` | 161 | UnwindData |  |
| 7 | `__std_atomic_notify_one_direct` | `0x13E0` | 25 | UnwindData |  |
| 8 | `__std_atomic_notify_one_indirect` | `0x1400` | 163 | UnwindData |  |
| 9 | `__std_atomic_set_api_level` | `0x14B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `__std_atomic_wait_direct` | `0x14C0` | 75 | UnwindData |  |
| 11 | `__std_atomic_wait_get_deadline` | `0x1510` | 44 | UnwindData |  |
| 12 | `__std_atomic_wait_get_remaining_timeout` | `0x1540` | 107 | UnwindData |  |
| 13 | `__std_atomic_wait_indirect` | `0x15B0` | 405 | UnwindData |  |
| 14 | `__std_bulk_submit_threadpool_work` | `0x1760` | 69 | UnwindData |  |
| 16 | `__std_close_threadpool_work` | `0x17B0` | 26 | UnwindData |  |
| 17 | `__std_create_threadpool_work` | `0x17D0` | 45 | UnwindData |  |
| 18 | `__std_execution_wait_on_uchar` | `0x1800` | 46 | UnwindData |  |
| 19 | `__std_execution_wake_by_address_all` | `0x1830` | 25 | UnwindData |  |
| 21 | `__std_parallel_algorithms_hw_threads` | `0x1850` | 55 | UnwindData |  |
| 23 | `__std_submit_threadpool_work` | `0x1890` | 26 | UnwindData |  |
| 32 | `__std_wait_for_threadpool_work_callbacks` | `0x18B0` | 34 | UnwindData |  |
| 1 | `__std_acquire_shared_mutex_for_instance` | `0x4BB0` | 155 | UnwindData |  |
| 22 | `__std_release_shared_mutex_for_instance` | `0x4C50` | 334 | UnwindData |  |
| 15 | `__std_calloc_crt` | `0x9350` | 56 | UnwindData |  |
| 20 | `__std_free_crt` | `0x9390` | 31 | UnwindData |  |
| 24 | `__std_tzdb_delete_current_zone` | `0x93B0` | 73 | UnwindData |  |
| 25 | `__std_tzdb_delete_leap_seconds` | `0x9400` | 35 | UnwindData |  |
| 26 | `__std_tzdb_delete_sys_info` | `0x9430` | 73 | UnwindData |  |
| 27 | `__std_tzdb_delete_time_zones` | `0x9480` | 278 | UnwindData |  |
| 28 | `__std_tzdb_get_current_zone` | `0x95A0` | 495 | UnwindData |  |
| 29 | `__std_tzdb_get_leap_seconds` | `0x9790` | 432 | UnwindData |  |
| 30 | `__std_tzdb_get_sys_info` | `0x9940` | 2,233 | UnwindData |  |
| 31 | `__std_tzdb_get_time_zones` | `0xA200` | 2,009 | UnwindData |  |
