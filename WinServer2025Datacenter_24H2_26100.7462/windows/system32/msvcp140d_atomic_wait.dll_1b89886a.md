# Binary Specification: msvcp140d_atomic_wait.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\msvcp140d_atomic_wait.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1b89886a5fff261c79efd8e668771738390621b576789d322f2ed638ed1ec488`
* **Total Exported Functions:** 32

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `__std_atomic_compare_exchange_128` | `0x1D30` | 108 | UnwindData |  |
| 3 | `__std_atomic_get_mutex` | `0x1DA0` | 121 | UnwindData |  |
| 4 | `__std_atomic_has_cmpxchg16b` | `0x1E20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `__std_atomic_notify_all_direct` | `0x1E30` | 48 | UnwindData |  |
| 6 | `__std_atomic_notify_all_indirect` | `0x1E60` | 161 | UnwindData |  |
| 7 | `__std_atomic_notify_one_direct` | `0x1F10` | 48 | UnwindData |  |
| 8 | `__std_atomic_notify_one_indirect` | `0x1F40` | 163 | UnwindData |  |
| 9 | `__std_atomic_set_api_level` | `0x1FF0` | 62 | UnwindData |  |
| 10 | `__std_atomic_wait_direct` | `0x2030` | 130 | UnwindData |  |
| 11 | `__std_atomic_wait_get_deadline` | `0x20C0` | 44 | UnwindData |  |
| 12 | `__std_atomic_wait_get_remaining_timeout` | `0x20F0` | 107 | UnwindData |  |
| 13 | `__std_atomic_wait_indirect` | `0x2160` | 405 | UnwindData |  |
| 14 | `__std_bulk_submit_threadpool_work` | `0x2310` | 69 | UnwindData |  |
| 16 | `__std_close_threadpool_work` | `0x2360` | 26 | UnwindData |  |
| 17 | `__std_create_threadpool_work` | `0x2380` | 45 | UnwindData |  |
| 18 | `__std_execution_wait_on_uchar` | `0x23B0` | 46 | UnwindData |  |
| 19 | `__std_execution_wake_by_address_all` | `0x23E0` | 25 | UnwindData |  |
| 21 | `__std_parallel_algorithms_hw_threads` | `0x2400` | 55 | UnwindData |  |
| 23 | `__std_submit_threadpool_work` | `0x2440` | 26 | UnwindData |  |
| 32 | `__std_wait_for_threadpool_work_callbacks` | `0x2460` | 34 | UnwindData |  |
| 1 | `__std_acquire_shared_mutex_for_instance` | `0x57C0` | 155 | UnwindData |  |
| 22 | `__std_release_shared_mutex_for_instance` | `0x5860` | 334 | UnwindData |  |
| 15 | `__std_calloc_crt` | `0x9F10` | 56 | UnwindData |  |
| 20 | `__std_free_crt` | `0x9F50` | 31 | UnwindData |  |
| 24 | `__std_tzdb_delete_current_zone` | `0x9F70` | 73 | UnwindData |  |
| 25 | `__std_tzdb_delete_leap_seconds` | `0x9FC0` | 35 | UnwindData |  |
| 26 | `__std_tzdb_delete_sys_info` | `0x9FF0` | 73 | UnwindData |  |
| 27 | `__std_tzdb_delete_time_zones` | `0xA040` | 278 | UnwindData |  |
| 28 | `__std_tzdb_get_current_zone` | `0xA160` | 495 | UnwindData |  |
| 29 | `__std_tzdb_get_leap_seconds` | `0xA350` | 432 | UnwindData |  |
| 30 | `__std_tzdb_get_sys_info` | `0xA500` | 1,742 | UnwindData |  |
| 31 | `__std_tzdb_get_time_zones` | `0xABD0` | 2,009 | UnwindData |  |
