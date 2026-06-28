# Binary Specification: vcomp140.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\vcomp140.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `95d4ce4a6802d1e18b5e0e1722cc30ea72ca7e033f83828f05c0b7b993fe7cbf`
* **Total Exported Functions:** 113

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 63 | `_vcomp_for_static_end` | `0x1500` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `_vcomp_set_num_threads` | `0x15D0` | 36 | UnwindData |  |
| 68 | `_vcomp_fork` | `0x1600` | 2,407 | UnwindData |  |
| 1 | `C2VectParallel` | `0x2030` | 266 | UnwindData |  |
| 66 | `_vcomp_for_static_simple_init` | `0x2390` | 234 | UnwindData |  |
| 67 | `_vcomp_for_static_simple_init_i8` | `0x2480` | 274 | UnwindData |  |
| 64 | `_vcomp_for_static_init` | `0x25A0` | 456 | UnwindData |  |
| 65 | `_vcomp_for_static_init_i8` | `0x2770` | 498 | UnwindData |  |
| 59 | `_vcomp_for_dynamic_init` | `0x2970` | 1,199 | UnwindData |  |
| 60 | `_vcomp_for_dynamic_init_i8` | `0x2E20` | 1,251 | UnwindData |  |
| 61 | `_vcomp_for_dynamic_next` | `0x3310` | 174 | UnwindData |  |
| 62 | `_vcomp_for_dynamic_next_i8` | `0x33C0` | 179 | UnwindData |  |
| 74 | `_vcomp_ordered_begin` | `0x3480` | 458 | UnwindData |  |
| 75 | `_vcomp_ordered_end` | `0x3650` | 513 | UnwindData |  |
| 76 | `_vcomp_ordered_loop_end` | `0x3860` | 151 | UnwindData |  |
| 87 | `_vcomp_sections_init` | `0x48D0` | 160 | UnwindData |  |
| 88 | `_vcomp_sections_next` | `0x4970` | 72 | UnwindData |  |
| 90 | `_vcomp_single_begin` | `0x49C0` | 261 | UnwindData |  |
| 91 | `_vcomp_single_end` | `0x4AD0` | 44 | UnwindData |  |
| 55 | `_vcomp_copyprivate_broadcast` | `0x4B00` | 140 | UnwindData |  |
| 56 | `_vcomp_copyprivate_receive` | `0x4B90` | 121 | UnwindData |  |
| 72 | `_vcomp_master_begin` | `0x4C10` | 61 | UnwindData |  |
| 73 | `_vcomp_master_end` | `0x4C50` | 39 | UnwindData |  |
| 69 | `_vcomp_get_thread_num` | `0x4C80` | 28 | UnwindData |  |
| 109 | `omp_set_num_threads` | `0x4CA0` | 43 | UnwindData |  |
| 98 | `omp_get_num_threads` | `0x4CD0` | 45 | UnwindData |  |
| 95 | `omp_get_max_threads` | `0x4D00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `omp_get_thread_num` | `0x4D20` | 37 | UnwindData |  |
| 97 | `omp_get_num_procs` | `0x4D50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `omp_in_parallel` | `0x4D60` | 42 | UnwindData |  |
| 105 | `omp_set_dynamic` | `0x4D90` | 32 | UnwindData |  |
| 94 | `omp_get_dynamic` | `0x4DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `omp_set_nested` | `0x4DC0` | 32 | UnwindData |  |
| 96 | `omp_get_nested` | `0x4DE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `omp_init_lock` | `0x4DF0` | 73 | UnwindData |  |
| 104 | `omp_init_nest_lock` | `0x4DF0` | 73 | UnwindData |  |
| 92 | `omp_destroy_lock` | `0x4E40` | 68 | UnwindData |  |
| 93 | `omp_destroy_nest_lock` | `0x4E40` | 68 | UnwindData |  |
| 106 | `omp_set_lock` | `0x4E90` | 49 | UnwindData |  |
| 112 | `omp_unset_lock` | `0x4ED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `omp_test_lock` | `0x4EF0` | 62 | UnwindData |  |
| 107 | `omp_set_nest_lock` | `0x4F30` | 28 | UnwindData |  |
| 113 | `omp_unset_nest_lock` | `0x4F50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `omp_test_nest_lock` | `0x4F60` | 40 | UnwindData |  |
| 101 | `omp_get_wtime` | `0x4F90` | 106 | UnwindData |  |
| 100 | `omp_get_wtick` | `0x5000` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `_vcomp_reduction_i1` | `0x5210` | 253 | UnwindData |  |
| 78 | `_vcomp_reduction_i2` | `0x5310` | 260 | UnwindData |  |
| 79 | `_vcomp_reduction_i4` | `0x5420` | 256 | UnwindData |  |
| 85 | `_vcomp_reduction_u4` | `0x5420` | 256 | UnwindData |  |
| 80 | `_vcomp_reduction_i8` | `0x5520` | 258 | UnwindData |  |
| 86 | `_vcomp_reduction_u8` | `0x5520` | 258 | UnwindData |  |
| 83 | `_vcomp_reduction_u1` | `0x5630` | 253 | UnwindData |  |
| 84 | `_vcomp_reduction_u2` | `0x5730` | 260 | UnwindData |  |
| 81 | `_vcomp_reduction_r4` | `0x5840` | 264 | UnwindData |  |
| 82 | `_vcomp_reduction_r8` | `0x5950` | 265 | UnwindData |  |
| 54 | `_vcomp_barrier` | `0x7200` | 234 | UnwindData |  |
| 71 | `_vcomp_master_barrier` | `0x72F0` | 304 | UnwindData |  |
| 57 | `_vcomp_enter_critsect` | `0x7420` | 151 | UnwindData |  |
| 70 | `_vcomp_leave_critsect` | `0x74C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `_vcomp_flush` | `0x74D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `_vcomp_atomic_add_i1` | `0x74F0` | 57 | UnwindData |  |
| 44 | `_vcomp_atomic_sub_i1` | `0x7530` | 57 | UnwindData |  |
| 22 | `_vcomp_atomic_mul_i1` | `0x7570` | 63 | UnwindData |  |
| 12 | `_vcomp_atomic_div_i1` | `0x75B0` | 60 | UnwindData |  |
| 18 | `_vcomp_atomic_div_ui1` | `0x75F0` | 61 | UnwindData |  |
| 8 | `_vcomp_atomic_and_i1` | `0x7630` | 57 | UnwindData |  |
| 50 | `_vcomp_atomic_xor_i1` | `0x7670` | 57 | UnwindData |  |
| 28 | `_vcomp_atomic_or_i1` | `0x76B0` | 57 | UnwindData |  |
| 32 | `_vcomp_atomic_shl_i1` | `0x76F0` | 59 | UnwindData |  |
| 36 | `_vcomp_atomic_shr_i1` | `0x7730` | 59 | UnwindData |  |
| 40 | `_vcomp_atomic_shr_ui1` | `0x7770` | 59 | UnwindData |  |
| 3 | `_vcomp_atomic_add_i2` | `0x77B0` | 61 | UnwindData |  |
| 45 | `_vcomp_atomic_sub_i2` | `0x77F0` | 61 | UnwindData |  |
| 23 | `_vcomp_atomic_mul_i2` | `0x7830` | 64 | UnwindData |  |
| 13 | `_vcomp_atomic_div_i2` | `0x7870` | 61 | UnwindData |  |
| 19 | `_vcomp_atomic_div_ui2` | `0x78B0` | 62 | UnwindData |  |
| 9 | `_vcomp_atomic_and_i2` | `0x78F0` | 61 | UnwindData |  |
| 51 | `_vcomp_atomic_xor_i2` | `0x7930` | 61 | UnwindData |  |
| 29 | `_vcomp_atomic_or_i2` | `0x7970` | 61 | UnwindData |  |
| 33 | `_vcomp_atomic_shl_i2` | `0x79B0` | 63 | UnwindData |  |
| 37 | `_vcomp_atomic_shr_i2` | `0x79F0` | 63 | UnwindData |  |
| 41 | `_vcomp_atomic_shr_ui2` | `0x7A30` | 63 | UnwindData |  |
| 4 | `_vcomp_atomic_add_i4` | `0x7A70` | 67 | UnwindData |  |
| 46 | `_vcomp_atomic_sub_i4` | `0x7AC0` | 69 | UnwindData |  |
| 24 | `_vcomp_atomic_mul_i4` | `0x7B10` | 84 | UnwindData |  |
| 14 | `_vcomp_atomic_div_i4` | `0x7B70` | 90 | UnwindData |  |
| 20 | `_vcomp_atomic_div_ui4` | `0x7BD0` | 92 | UnwindData |  |
| 10 | `_vcomp_atomic_and_i4` | `0x7C30` | 67 | UnwindData |  |
| 52 | `_vcomp_atomic_xor_i4` | `0x7C80` | 67 | UnwindData |  |
| 30 | `_vcomp_atomic_or_i4` | `0x7CD0` | 67 | UnwindData |  |
| 34 | `_vcomp_atomic_shl_i4` | `0x7D20` | 86 | UnwindData |  |
| 38 | `_vcomp_atomic_shr_i4` | `0x7D80` | 86 | UnwindData |  |
| 42 | `_vcomp_atomic_shr_ui4` | `0x7DE0` | 86 | UnwindData |  |
| 5 | `_vcomp_atomic_add_i8` | `0x7E40` | 72 | UnwindData |  |
| 47 | `_vcomp_atomic_sub_i8` | `0x7E90` | 75 | UnwindData |  |
| 25 | `_vcomp_atomic_mul_i8` | `0x7EE0` | 89 | UnwindData |  |
| 15 | `_vcomp_atomic_div_i8` | `0x7F40` | 97 | UnwindData |  |
| 21 | `_vcomp_atomic_div_ui8` | `0x7FB0` | 97 | UnwindData |  |
| 11 | `_vcomp_atomic_and_i8` | `0x8020` | 72 | UnwindData |  |
| 53 | `_vcomp_atomic_xor_i8` | `0x8070` | 72 | UnwindData |  |
| 31 | `_vcomp_atomic_or_i8` | `0x80C0` | 72 | UnwindData |  |
| 35 | `_vcomp_atomic_shl_i8` | `0x8110` | 93 | UnwindData |  |
| 39 | `_vcomp_atomic_shr_i8` | `0x8170` | 93 | UnwindData |  |
| 43 | `_vcomp_atomic_shr_ui8` | `0x81D0` | 93 | UnwindData |  |
| 6 | `_vcomp_atomic_add_r4` | `0x8230` | 95 | UnwindData |  |
| 48 | `_vcomp_atomic_sub_r4` | `0x8290` | 99 | UnwindData |  |
| 26 | `_vcomp_atomic_mul_r4` | `0x8300` | 95 | UnwindData |  |
| 16 | `_vcomp_atomic_div_r4` | `0x8360` | 99 | UnwindData |  |
| 7 | `_vcomp_atomic_add_r8` | `0x83D0` | 101 | UnwindData |  |
| 49 | `_vcomp_atomic_sub_r8` | `0x8440` | 105 | UnwindData |  |
| 27 | `_vcomp_atomic_mul_r8` | `0x84B0` | 101 | UnwindData |  |
| 17 | `_vcomp_atomic_div_r8` | `0x8520` | 105 | UnwindData |  |
