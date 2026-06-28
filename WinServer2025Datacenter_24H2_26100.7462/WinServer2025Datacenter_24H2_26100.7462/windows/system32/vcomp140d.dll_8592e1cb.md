# Binary Specification: vcomp140d.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\vcomp140d.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8592e1cbe71a512c1108736cb4a829f836abc29659ffb9195634ad73b1d5e812`
* **Total Exported Functions:** 113

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 89 | `_vcomp_set_num_threads` | `0x1540` | 51 | UnwindData |  |
| 68 | `_vcomp_fork` | `0x1580` | 536 | UnwindData |  |
| 1 | `C2VectParallel` | `0x1870` | 266 | UnwindData |  |
| 66 | `_vcomp_for_static_simple_init` | `0x1C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `_vcomp_for_static_simple_init_i8` | `0x1C40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `_vcomp_for_static_init` | `0x1C50` | 77 | UnwindData |  |
| 65 | `_vcomp_for_static_init_i8` | `0x1CA0` | 77 | UnwindData |  |
| 63 | `_vcomp_for_static_end` | `0x1CF0` | 28 | UnwindData |  |
| 91 | `_vcomp_single_end` | `0x1CF0` | 28 | UnwindData |  |
| 59 | `_vcomp_for_dynamic_init` | `0x1D10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `_vcomp_for_dynamic_init_i8` | `0x1D20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `_vcomp_for_dynamic_next` | `0x1D30` | 210 | UnwindData |  |
| 62 | `_vcomp_for_dynamic_next_i8` | `0x1E10` | 213 | UnwindData |  |
| 74 | `_vcomp_ordered_begin` | `0x1EF0` | 208 | UnwindData |  |
| 75 | `_vcomp_ordered_end` | `0x1FC0` | 144 | UnwindData |  |
| 76 | `_vcomp_ordered_loop_end` | `0x2050` | 177 | UnwindData |  |
| 87 | `_vcomp_sections_init` | `0x5330` | 383 | UnwindData |  |
| 88 | `_vcomp_sections_next` | `0x54B0` | 72 | UnwindData |  |
| 90 | `_vcomp_single_begin` | `0x5500` | 401 | UnwindData |  |
| 55 | `_vcomp_copyprivate_broadcast` | `0x56A0` | 125 | UnwindData |  |
| 56 | `_vcomp_copyprivate_receive` | `0x5720` | 121 | UnwindData |  |
| 72 | `_vcomp_master_begin` | `0x57A0` | 73 | UnwindData |  |
| 73 | `_vcomp_master_end` | `0x57F0` | 28 | UnwindData |  |
| 69 | `_vcomp_get_thread_num` | `0x5810` | 33 | UnwindData |  |
| 109 | `omp_set_num_threads` | `0x5840` | 79 | UnwindData |  |
| 98 | `omp_get_num_threads` | `0x5890` | 45 | UnwindData |  |
| 95 | `omp_get_max_threads` | `0x58C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `omp_get_thread_num` | `0x58E0` | 40 | UnwindData |  |
| 97 | `omp_get_num_procs` | `0x5910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `omp_in_parallel` | `0x5920` | 45 | UnwindData |  |
| 105 | `omp_set_dynamic` | `0x5950` | 54 | UnwindData |  |
| 94 | `omp_get_dynamic` | `0x5990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `omp_set_nested` | `0x59A0` | 54 | UnwindData |  |
| 96 | `omp_get_nested` | `0x59E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `omp_init_lock` | `0x59F0` | 77 | UnwindData |  |
| 92 | `omp_destroy_lock` | `0x5A40` | 109 | UnwindData |  |
| 106 | `omp_set_lock` | `0x5AB0` | 90 | UnwindData |  |
| 112 | `omp_unset_lock` | `0x5B10` | 105 | UnwindData |  |
| 110 | `omp_test_lock` | `0x5B80` | 123 | UnwindData |  |
| 104 | `omp_init_nest_lock` | `0x5C00` | 77 | UnwindData |  |
| 93 | `omp_destroy_nest_lock` | `0x5C50` | 109 | UnwindData |  |
| 107 | `omp_set_nest_lock` | `0x5CC0` | 69 | UnwindData |  |
| 113 | `omp_unset_nest_lock` | `0x5D10` | 99 | UnwindData |  |
| 111 | `omp_test_nest_lock` | `0x5D80` | 85 | UnwindData |  |
| 101 | `omp_get_wtime` | `0x5DE0` | 105 | UnwindData |  |
| 100 | `omp_get_wtick` | `0x5E50` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `_vcomp_reduction_i1` | `0x61A0` | 294 | UnwindData |  |
| 78 | `_vcomp_reduction_i2` | `0x62D0` | 302 | UnwindData |  |
| 79 | `_vcomp_reduction_i4` | `0x6400` | 298 | UnwindData |  |
| 85 | `_vcomp_reduction_u4` | `0x6400` | 298 | UnwindData |  |
| 80 | `_vcomp_reduction_i8` | `0x6530` | 299 | UnwindData |  |
| 86 | `_vcomp_reduction_u8` | `0x6530` | 299 | UnwindData |  |
| 83 | `_vcomp_reduction_u1` | `0x6660` | 294 | UnwindData |  |
| 84 | `_vcomp_reduction_u2` | `0x6790` | 302 | UnwindData |  |
| 81 | `_vcomp_reduction_r4` | `0x68C0` | 297 | UnwindData |  |
| 82 | `_vcomp_reduction_r8` | `0x69F0` | 298 | UnwindData |  |
| 54 | `_vcomp_barrier` | `0x85B0` | 361 | UnwindData |  |
| 71 | `_vcomp_master_barrier` | `0x8720` | 295 | UnwindData |  |
| 57 | `_vcomp_enter_critsect` | `0x8850` | 239 | UnwindData |  |
| 70 | `_vcomp_leave_critsect` | `0x8940` | 48 | UnwindData |  |
| 58 | `_vcomp_flush` | `0x8970` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `_vcomp_atomic_add_i1` | `0x8990` | 55 | UnwindData |  |
| 44 | `_vcomp_atomic_sub_i1` | `0x89D0` | 55 | UnwindData |  |
| 22 | `_vcomp_atomic_mul_i1` | `0x8A10` | 61 | UnwindData |  |
| 12 | `_vcomp_atomic_div_i1` | `0x8A50` | 58 | UnwindData |  |
| 18 | `_vcomp_atomic_div_ui1` | `0x8A90` | 59 | UnwindData |  |
| 8 | `_vcomp_atomic_and_i1` | `0x8AD0` | 55 | UnwindData |  |
| 50 | `_vcomp_atomic_xor_i1` | `0x8B10` | 55 | UnwindData |  |
| 28 | `_vcomp_atomic_or_i1` | `0x8B50` | 55 | UnwindData |  |
| 32 | `_vcomp_atomic_shl_i1` | `0x8B90` | 57 | UnwindData |  |
| 36 | `_vcomp_atomic_shr_i1` | `0x8BD0` | 57 | UnwindData |  |
| 40 | `_vcomp_atomic_shr_ui1` | `0x8C10` | 57 | UnwindData |  |
| 3 | `_vcomp_atomic_add_i2` | `0x8C50` | 59 | UnwindData |  |
| 45 | `_vcomp_atomic_sub_i2` | `0x8C90` | 59 | UnwindData |  |
| 23 | `_vcomp_atomic_mul_i2` | `0x8CD0` | 62 | UnwindData |  |
| 13 | `_vcomp_atomic_div_i2` | `0x8D10` | 59 | UnwindData |  |
| 19 | `_vcomp_atomic_div_ui2` | `0x8D50` | 60 | UnwindData |  |
| 9 | `_vcomp_atomic_and_i2` | `0x8D90` | 59 | UnwindData |  |
| 51 | `_vcomp_atomic_xor_i2` | `0x8DD0` | 59 | UnwindData |  |
| 29 | `_vcomp_atomic_or_i2` | `0x8E10` | 59 | UnwindData |  |
| 33 | `_vcomp_atomic_shl_i2` | `0x8E50` | 61 | UnwindData |  |
| 37 | `_vcomp_atomic_shr_i2` | `0x8E90` | 61 | UnwindData |  |
| 41 | `_vcomp_atomic_shr_ui2` | `0x8ED0` | 61 | UnwindData |  |
| 4 | `_vcomp_atomic_add_i4` | `0x8F10` | 66 | UnwindData |  |
| 46 | `_vcomp_atomic_sub_i4` | `0x8F60` | 68 | UnwindData |  |
| 24 | `_vcomp_atomic_mul_i4` | `0x8FB0` | 83 | UnwindData |  |
| 14 | `_vcomp_atomic_div_i4` | `0x9010` | 89 | UnwindData |  |
| 20 | `_vcomp_atomic_div_ui4` | `0x9070` | 91 | UnwindData |  |
| 10 | `_vcomp_atomic_and_i4` | `0x90D0` | 66 | UnwindData |  |
| 52 | `_vcomp_atomic_xor_i4` | `0x9120` | 66 | UnwindData |  |
| 30 | `_vcomp_atomic_or_i4` | `0x9170` | 66 | UnwindData |  |
| 34 | `_vcomp_atomic_shl_i4` | `0x91C0` | 85 | UnwindData |  |
| 38 | `_vcomp_atomic_shr_i4` | `0x9220` | 85 | UnwindData |  |
| 42 | `_vcomp_atomic_shr_ui4` | `0x9280` | 85 | UnwindData |  |
| 5 | `_vcomp_atomic_add_i8` | `0x92E0` | 71 | UnwindData |  |
| 47 | `_vcomp_atomic_sub_i8` | `0x9330` | 74 | UnwindData |  |
| 25 | `_vcomp_atomic_mul_i8` | `0x9380` | 88 | UnwindData |  |
| 15 | `_vcomp_atomic_div_i8` | `0x93E0` | 96 | UnwindData |  |
| 21 | `_vcomp_atomic_div_ui8` | `0x9440` | 96 | UnwindData |  |
| 11 | `_vcomp_atomic_and_i8` | `0x94A0` | 71 | UnwindData |  |
| 53 | `_vcomp_atomic_xor_i8` | `0x94F0` | 71 | UnwindData |  |
| 31 | `_vcomp_atomic_or_i8` | `0x9540` | 71 | UnwindData |  |
| 35 | `_vcomp_atomic_shl_i8` | `0x9590` | 92 | UnwindData |  |
| 39 | `_vcomp_atomic_shr_i8` | `0x95F0` | 92 | UnwindData |  |
| 43 | `_vcomp_atomic_shr_ui8` | `0x9650` | 92 | UnwindData |  |
| 6 | `_vcomp_atomic_add_r4` | `0x96B0` | 94 | UnwindData |  |
| 48 | `_vcomp_atomic_sub_r4` | `0x9710` | 98 | UnwindData |  |
| 26 | `_vcomp_atomic_mul_r4` | `0x9780` | 94 | UnwindData |  |
| 16 | `_vcomp_atomic_div_r4` | `0x97E0` | 98 | UnwindData |  |
| 7 | `_vcomp_atomic_add_r8` | `0x9850` | 100 | UnwindData |  |
| 49 | `_vcomp_atomic_sub_r8` | `0x98C0` | 104 | UnwindData |  |
| 27 | `_vcomp_atomic_mul_r8` | `0x9930` | 100 | UnwindData |  |
| 17 | `_vcomp_atomic_div_r8` | `0x99A0` | 104 | UnwindData |  |
