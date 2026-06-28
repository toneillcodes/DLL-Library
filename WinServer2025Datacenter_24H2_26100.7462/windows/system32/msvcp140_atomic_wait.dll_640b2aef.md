# Binary Specification: msvcp140_atomic_wait.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\msvcp140_atomic_wait.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `640b2aefced484d0368eea5bdd06addd0658a3a70a49256e560d6923b404a479`
* **Total Exported Functions:** 32

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `__std_atomic_compare_exchange_128` | `0x1190` | 42 | UnwindData |  |
| 3 | `__std_atomic_get_mutex` | `0x11C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `__std_atomic_has_cmpxchg16b` | `0x11F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `__std_atomic_notify_all_direct` | `0x1200` | 66 | UnwindData |  |
| 6 | `__std_atomic_notify_all_indirect` | `0x1250` | 138 | UnwindData |  |
| 7 | `__std_atomic_notify_one_direct` | `0x12E0` | 66 | UnwindData |  |
| 8 | `__std_atomic_notify_one_indirect` | `0x1330` | 120 | UnwindData |  |
| 9 | `__std_atomic_set_api_level` | `0x13B0` | 78 | UnwindData |  |
| 10 | `__std_atomic_wait_direct` | `0x1400` | 129 | UnwindData |  |
| 11 | `__std_atomic_wait_get_deadline` | `0x1490` | 33 | UnwindData |  |
| 12 | `__std_atomic_wait_get_remaining_timeout` | `0x14C0` | 57 | UnwindData |  |
| 13 | `__std_atomic_wait_indirect` | `0x1500` | 319 | UnwindData |  |
| 14 | `__std_bulk_submit_threadpool_work` | `0x1640` | 47 | UnwindData |  |
| 16 | `__std_close_threadpool_work` | `0x1670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `__std_create_threadpool_work` | `0x1680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `__std_execution_wait_on_uchar` | `0x1690` | 33 | UnwindData |  |
| 19 | `__std_execution_wake_by_address_all` | `0x16C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `__std_parallel_algorithms_hw_threads` | `0x16D0` | 31 | UnwindData |  |
| 23 | `__std_submit_threadpool_work` | `0x16F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `__std_wait_for_threadpool_work_callbacks` | `0x1700` | 1,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `__std_acquire_shared_mutex_for_instance` | `0x1E30` | 318 | UnwindData |  |
| 22 | `__std_release_shared_mutex_for_instance` | `0x1F70` | 120 | UnwindData |  |
| 15 | `__std_calloc_crt` | `0x2860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `__std_free_crt` | `0x2870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `__std_tzdb_delete_current_zone` | `0x2880` | 41 | UnwindData |  |
| 25 | `__std_tzdb_delete_leap_seconds` | `0x28B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `__std_tzdb_delete_sys_info` | `0x28C0` | 41 | UnwindData |  |
| 27 | `__std_tzdb_delete_time_zones` | `0x28F0` | 156 | UnwindData |  |
| 28 | `__std_tzdb_get_current_zone` | `0x2990` | 276 | UnwindData |  |
| 29 | `__std_tzdb_get_leap_seconds` | `0x2AB0` | 326 | UnwindData |  |
| 30 | `__std_tzdb_get_sys_info` | `0x2C00` | 958 | UnwindData |  |
| 31 | `__std_tzdb_get_time_zones` | `0x2FC0` | 1,465 | UnwindData |  |
