# Binary Specification: vcomp110.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\vcomp110.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `30dbc138c12eca9cd0721c2208fd8c657090ac39b1cb7d20f1aa19935cdd946d`
* **Total Exported Functions:** 113

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 63 | `_vcomp_for_static_end` | `0x13E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `_vcomp_set_num_threads` | `0x1420` | 56 | UnwindData |  |
| 68 | `_vcomp_fork` | `0x1458` | 572 | UnwindData |  |
| 1 | `C2VectParallel` | `0x1818` | 231 | UnwindData |  |
| 66 | `_vcomp_for_static_simple_init` | `0x1BFC` | 324 | UnwindData |  |
| 67 | `_vcomp_for_static_simple_init_i8` | `0x1D40` | 370 | UnwindData |  |
| 64 | `_vcomp_for_static_init` | `0x1EB4` | 447 | UnwindData |  |
| 65 | `_vcomp_for_static_init_i8` | `0x2074` | 77 | UnwindData |  |
| 59 | `_vcomp_for_dynamic_init` | `0x20C4` | 177 | UnwindData |  |
| 60 | `_vcomp_for_dynamic_init_i8` | `0x2178` | 180 | UnwindData |  |
| 61 | `_vcomp_for_dynamic_next` | `0x222C` | 199 | UnwindData |  |
| 62 | `_vcomp_for_dynamic_next_i8` | `0x22F4` | 204 | UnwindData |  |
| 74 | `_vcomp_ordered_begin` | `0x23C0` | 122 | UnwindData |  |
| 75 | `_vcomp_ordered_end` | `0x243C` | 122 | UnwindData |  |
| 76 | `_vcomp_ordered_loop_end` | `0x24B8` | 145 | UnwindData |  |
| 87 | `_vcomp_sections_init` | `0x41F0` | 181 | UnwindData |  |
| 88 | `_vcomp_sections_next` | `0x42A8` | 73 | UnwindData |  |
| 90 | `_vcomp_single_begin` | `0x42F4` | 243 | UnwindData |  |
| 91 | `_vcomp_single_end` | `0x43E8` | 44 | UnwindData |  |
| 55 | `_vcomp_copyprivate_broadcast` | `0x4414` | 147 | UnwindData |  |
| 56 | `_vcomp_copyprivate_receive` | `0x44A8` | 114 | UnwindData |  |
| 72 | `_vcomp_master_begin` | `0x451C` | 67 | UnwindData |  |
| 73 | `_vcomp_master_end` | `0x4560` | 39 | UnwindData |  |
| 69 | `_vcomp_get_thread_num` | `0x4588` | 33 | UnwindData |  |
| 109 | `omp_set_num_threads` | `0x45AC` | 63 | UnwindData |  |
| 98 | `omp_get_num_threads` | `0x45EC` | 45 | UnwindData |  |
| 95 | `omp_get_max_threads` | `0x461C` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `omp_get_thread_num` | `0x4630` | 40 | UnwindData |  |
| 97 | `omp_get_num_procs` | `0x4658` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `omp_in_parallel` | `0x4660` | 45 | UnwindData |  |
| 105 | `omp_set_dynamic` | `0x4690` | 32 | UnwindData |  |
| 94 | `omp_get_dynamic` | `0x46B0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `omp_set_nested` | `0x46B8` | 32 | UnwindData |  |
| 96 | `omp_get_nested` | `0x46D8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `omp_init_lock` | `0x46E0` | 67 | UnwindData |  |
| 104 | `omp_init_nest_lock` | `0x46E0` | 67 | UnwindData |  |
| 92 | `omp_destroy_lock` | `0x4724` | 65 | UnwindData |  |
| 93 | `omp_destroy_nest_lock` | `0x4724` | 65 | UnwindData |  |
| 106 | `omp_set_lock` | `0x4768` | 49 | UnwindData |  |
| 112 | `omp_unset_lock` | `0x479C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `omp_test_lock` | `0x47AC` | 71 | UnwindData |  |
| 107 | `omp_set_nest_lock` | `0x47F4` | 28 | UnwindData |  |
| 113 | `omp_unset_nest_lock` | `0x4810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `omp_test_nest_lock` | `0x4820` | 44 | UnwindData |  |
| 101 | `omp_get_wtime` | `0x484C` | 77 | UnwindData |  |
| 100 | `omp_get_wtick` | `0x489C` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `_vcomp_reduction_i1` | `0x49BC` | 272 | UnwindData |  |
| 83 | `_vcomp_reduction_u1` | `0x49BC` | 272 | UnwindData |  |
| 78 | `_vcomp_reduction_i2` | `0x4ACC` | 279 | UnwindData |  |
| 84 | `_vcomp_reduction_u2` | `0x4ACC` | 279 | UnwindData |  |
| 79 | `_vcomp_reduction_i4` | `0x4BE4` | 276 | UnwindData |  |
| 85 | `_vcomp_reduction_u4` | `0x4BE4` | 276 | UnwindData |  |
| 80 | `_vcomp_reduction_i8` | `0x4CF8` | 276 | UnwindData |  |
| 86 | `_vcomp_reduction_u8` | `0x4CF8` | 276 | UnwindData |  |
| 81 | `_vcomp_reduction_r4` | `0x4E0C` | 289 | UnwindData |  |
| 82 | `_vcomp_reduction_r8` | `0x4F30` | 289 | UnwindData |  |
| 54 | `_vcomp_barrier` | `0x624C` | 229 | UnwindData |  |
| 71 | `_vcomp_master_barrier` | `0x6334` | 296 | UnwindData |  |
| 57 | `_vcomp_enter_critsect` | `0x645C` | 148 | UnwindData |  |
| 70 | `_vcomp_leave_critsect` | `0x64F0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `_vcomp_flush` | `0x64F8` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `_vcomp_atomic_add_i1` | `0x650C` | 61 | UnwindData |  |
| 44 | `_vcomp_atomic_sub_i1` | `0x654C` | 61 | UnwindData |  |
| 22 | `_vcomp_atomic_mul_i1` | `0x658C` | 62 | UnwindData |  |
| 12 | `_vcomp_atomic_div_i1` | `0x65CC` | 60 | UnwindData |  |
| 18 | `_vcomp_atomic_div_ui1` | `0x6608` | 60 | UnwindData |  |
| 8 | `_vcomp_atomic_and_i1` | `0x6644` | 61 | UnwindData |  |
| 50 | `_vcomp_atomic_xor_i1` | `0x6684` | 61 | UnwindData |  |
| 28 | `_vcomp_atomic_or_i1` | `0x66C4` | 61 | UnwindData |  |
| 32 | `_vcomp_atomic_shl_i1` | `0x6704` | 59 | UnwindData |  |
| 36 | `_vcomp_atomic_shr_i1` | `0x6740` | 59 | UnwindData |  |
| 40 | `_vcomp_atomic_shr_ui1` | `0x677C` | 59 | UnwindData |  |
| 3 | `_vcomp_atomic_add_i2` | `0x67B8` | 63 | UnwindData |  |
| 45 | `_vcomp_atomic_sub_i2` | `0x67F8` | 63 | UnwindData |  |
| 23 | `_vcomp_atomic_mul_i2` | `0x6838` | 64 | UnwindData |  |
| 13 | `_vcomp_atomic_div_i2` | `0x6878` | 61 | UnwindData |  |
| 19 | `_vcomp_atomic_div_ui2` | `0x68B8` | 61 | UnwindData |  |
| 9 | `_vcomp_atomic_and_i2` | `0x68F8` | 63 | UnwindData |  |
| 51 | `_vcomp_atomic_xor_i2` | `0x6938` | 63 | UnwindData |  |
| 29 | `_vcomp_atomic_or_i2` | `0x6978` | 63 | UnwindData |  |
| 33 | `_vcomp_atomic_shl_i2` | `0x69B8` | 63 | UnwindData |  |
| 37 | `_vcomp_atomic_shr_i2` | `0x69F8` | 63 | UnwindData |  |
| 41 | `_vcomp_atomic_shr_ui2` | `0x6A38` | 63 | UnwindData |  |
| 4 | `_vcomp_atomic_add_i4` | `0x6A78` | 64 | UnwindData |  |
| 46 | `_vcomp_atomic_sub_i4` | `0x6AB8` | 66 | UnwindData |  |
| 24 | `_vcomp_atomic_mul_i4` | `0x6AFC` | 84 | UnwindData |  |
| 14 | `_vcomp_atomic_div_i4` | `0x6B50` | 90 | UnwindData |  |
| 20 | `_vcomp_atomic_div_ui4` | `0x6BAC` | 92 | UnwindData |  |
| 10 | `_vcomp_atomic_and_i4` | `0x6C08` | 63 | UnwindData |  |
| 52 | `_vcomp_atomic_xor_i4` | `0x6C48` | 63 | UnwindData |  |
| 30 | `_vcomp_atomic_or_i4` | `0x6C88` | 63 | UnwindData |  |
| 34 | `_vcomp_atomic_shl_i4` | `0x6CC8` | 82 | UnwindData |  |
| 38 | `_vcomp_atomic_shr_i4` | `0x6D1C` | 82 | UnwindData |  |
| 42 | `_vcomp_atomic_shr_ui4` | `0x6D70` | 82 | UnwindData |  |
| 5 | `_vcomp_atomic_add_i8` | `0x6DC4` | 67 | UnwindData |  |
| 47 | `_vcomp_atomic_sub_i8` | `0x6E08` | 70 | UnwindData |  |
| 25 | `_vcomp_atomic_mul_i8` | `0x6E50` | 89 | UnwindData |  |
| 15 | `_vcomp_atomic_div_i8` | `0x6EAC` | 97 | UnwindData |  |
| 21 | `_vcomp_atomic_div_ui8` | `0x6F10` | 97 | UnwindData |  |
| 11 | `_vcomp_atomic_and_i8` | `0x6F74` | 66 | UnwindData |  |
| 53 | `_vcomp_atomic_xor_i8` | `0x6FB8` | 66 | UnwindData |  |
| 31 | `_vcomp_atomic_or_i8` | `0x6FFC` | 66 | UnwindData |  |
| 35 | `_vcomp_atomic_shl_i8` | `0x7040` | 87 | UnwindData |  |
| 39 | `_vcomp_atomic_shr_i8` | `0x7098` | 87 | UnwindData |  |
| 43 | `_vcomp_atomic_shr_ui8` | `0x70F0` | 87 | UnwindData |  |
| 6 | `_vcomp_atomic_add_r4` | `0x7148` | 103 | UnwindData |  |
| 48 | `_vcomp_atomic_sub_r4` | `0x71B0` | 107 | UnwindData |  |
| 26 | `_vcomp_atomic_mul_r4` | `0x721C` | 103 | UnwindData |  |
| 16 | `_vcomp_atomic_div_r4` | `0x7284` | 107 | UnwindData |  |
| 7 | `_vcomp_atomic_add_r8` | `0x72F0` | 107 | UnwindData |  |
| 49 | `_vcomp_atomic_sub_r8` | `0x735C` | 111 | UnwindData |  |
| 27 | `_vcomp_atomic_mul_r8` | `0x73CC` | 107 | UnwindData |  |
| 17 | `_vcomp_atomic_div_r8` | `0x7438` | 111 | UnwindData |  |
