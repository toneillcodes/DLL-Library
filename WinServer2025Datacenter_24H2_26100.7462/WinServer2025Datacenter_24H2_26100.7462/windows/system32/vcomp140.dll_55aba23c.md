# Binary Specification: vcomp140.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\vcomp140.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `55aba23cdcd6484fbb06f4155b8ca75adfce7a881f10afd0c49457165e677164`
* **Total Exported Functions:** 113

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 63 | `_vcomp_for_static_end` | `0x1430` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `_vcomp_set_num_threads` | `0x1500` | 36 | UnwindData |  |
| 68 | `_vcomp_fork` | `0x1530` | 536 | UnwindData |  |
| 1 | `C2VectParallel` | `0x1810` | 266 | UnwindData |  |
| 66 | `_vcomp_for_static_simple_init` | `0x1B80` | 305 | UnwindData |  |
| 67 | `_vcomp_for_static_simple_init_i8` | `0x1CC0` | 329 | UnwindData |  |
| 64 | `_vcomp_for_static_init` | `0x1E10` | 471 | UnwindData |  |
| 65 | `_vcomp_for_static_init_i8` | `0x1FF0` | 77 | UnwindData |  |
| 59 | `_vcomp_for_dynamic_init` | `0x2040` | 183 | UnwindData |  |
| 60 | `_vcomp_for_dynamic_init_i8` | `0x2100` | 186 | UnwindData |  |
| 61 | `_vcomp_for_dynamic_next` | `0x21C0` | 210 | UnwindData |  |
| 62 | `_vcomp_for_dynamic_next_i8` | `0x22A0` | 213 | UnwindData |  |
| 74 | `_vcomp_ordered_begin` | `0x2380` | 154 | UnwindData |  |
| 75 | `_vcomp_ordered_end` | `0x2420` | 154 | UnwindData |  |
| 76 | `_vcomp_ordered_loop_end` | `0x24C0` | 169 | UnwindData |  |
| 87 | `_vcomp_sections_init` | `0x46D0` | 203 | UnwindData |  |
| 88 | `_vcomp_sections_next` | `0x47A0` | 72 | UnwindData |  |
| 90 | `_vcomp_single_begin` | `0x47F0` | 270 | UnwindData |  |
| 91 | `_vcomp_single_end` | `0x4900` | 44 | UnwindData |  |
| 55 | `_vcomp_copyprivate_broadcast` | `0x4930` | 140 | UnwindData |  |
| 56 | `_vcomp_copyprivate_receive` | `0x49C0` | 121 | UnwindData |  |
| 72 | `_vcomp_master_begin` | `0x4A40` | 61 | UnwindData |  |
| 73 | `_vcomp_master_end` | `0x4A80` | 39 | UnwindData |  |
| 69 | `_vcomp_get_thread_num` | `0x4AB0` | 33 | UnwindData |  |
| 109 | `omp_set_num_threads` | `0x4AE0` | 43 | UnwindData |  |
| 98 | `omp_get_num_threads` | `0x4B10` | 45 | UnwindData |  |
| 95 | `omp_get_max_threads` | `0x4B40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `omp_get_thread_num` | `0x4B60` | 40 | UnwindData |  |
| 97 | `omp_get_num_procs` | `0x4B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `omp_in_parallel` | `0x4BA0` | 45 | UnwindData |  |
| 105 | `omp_set_dynamic` | `0x4BD0` | 32 | UnwindData |  |
| 94 | `omp_get_dynamic` | `0x4BF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `omp_set_nested` | `0x4C00` | 32 | UnwindData |  |
| 96 | `omp_get_nested` | `0x4C20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `omp_init_lock` | `0x4C30` | 70 | UnwindData |  |
| 104 | `omp_init_nest_lock` | `0x4C30` | 70 | UnwindData |  |
| 92 | `omp_destroy_lock` | `0x4C80` | 68 | UnwindData |  |
| 93 | `omp_destroy_nest_lock` | `0x4C80` | 68 | UnwindData |  |
| 106 | `omp_set_lock` | `0x4CD0` | 49 | UnwindData |  |
| 112 | `omp_unset_lock` | `0x4D10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `omp_test_lock` | `0x4D30` | 71 | UnwindData |  |
| 107 | `omp_set_nest_lock` | `0x4D80` | 28 | UnwindData |  |
| 113 | `omp_unset_nest_lock` | `0x4DA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `omp_test_nest_lock` | `0x4DB0` | 44 | UnwindData |  |
| 101 | `omp_get_wtime` | `0x4DE0` | 105 | UnwindData |  |
| 100 | `omp_get_wtick` | `0x4E50` | 832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `_vcomp_reduction_i1` | `0x5190` | 294 | UnwindData |  |
| 78 | `_vcomp_reduction_i2` | `0x52C0` | 302 | UnwindData |  |
| 79 | `_vcomp_reduction_i4` | `0x53F0` | 298 | UnwindData |  |
| 85 | `_vcomp_reduction_u4` | `0x53F0` | 298 | UnwindData |  |
| 80 | `_vcomp_reduction_i8` | `0x5520` | 299 | UnwindData |  |
| 86 | `_vcomp_reduction_u8` | `0x5520` | 299 | UnwindData |  |
| 83 | `_vcomp_reduction_u1` | `0x5650` | 294 | UnwindData |  |
| 84 | `_vcomp_reduction_u2` | `0x5780` | 302 | UnwindData |  |
| 81 | `_vcomp_reduction_r4` | `0x58B0` | 297 | UnwindData |  |
| 82 | `_vcomp_reduction_r8` | `0x59E0` | 298 | UnwindData |  |
| 54 | `_vcomp_barrier` | `0x7540` | 249 | UnwindData |  |
| 71 | `_vcomp_master_barrier` | `0x7640` | 329 | UnwindData |  |
| 57 | `_vcomp_enter_critsect` | `0x7790` | 148 | UnwindData |  |
| 70 | `_vcomp_leave_critsect` | `0x7830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `_vcomp_flush` | `0x7840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `_vcomp_atomic_add_i1` | `0x7860` | 57 | UnwindData |  |
| 44 | `_vcomp_atomic_sub_i1` | `0x78A0` | 57 | UnwindData |  |
| 22 | `_vcomp_atomic_mul_i1` | `0x78E0` | 63 | UnwindData |  |
| 12 | `_vcomp_atomic_div_i1` | `0x7920` | 60 | UnwindData |  |
| 18 | `_vcomp_atomic_div_ui1` | `0x7960` | 61 | UnwindData |  |
| 8 | `_vcomp_atomic_and_i1` | `0x79A0` | 57 | UnwindData |  |
| 50 | `_vcomp_atomic_xor_i1` | `0x79E0` | 57 | UnwindData |  |
| 28 | `_vcomp_atomic_or_i1` | `0x7A20` | 57 | UnwindData |  |
| 32 | `_vcomp_atomic_shl_i1` | `0x7A60` | 59 | UnwindData |  |
| 36 | `_vcomp_atomic_shr_i1` | `0x7AA0` | 59 | UnwindData |  |
| 40 | `_vcomp_atomic_shr_ui1` | `0x7AE0` | 59 | UnwindData |  |
| 3 | `_vcomp_atomic_add_i2` | `0x7B20` | 61 | UnwindData |  |
| 45 | `_vcomp_atomic_sub_i2` | `0x7B60` | 61 | UnwindData |  |
| 23 | `_vcomp_atomic_mul_i2` | `0x7BA0` | 64 | UnwindData |  |
| 13 | `_vcomp_atomic_div_i2` | `0x7BE0` | 61 | UnwindData |  |
| 19 | `_vcomp_atomic_div_ui2` | `0x7C20` | 62 | UnwindData |  |
| 9 | `_vcomp_atomic_and_i2` | `0x7C60` | 61 | UnwindData |  |
| 51 | `_vcomp_atomic_xor_i2` | `0x7CA0` | 61 | UnwindData |  |
| 29 | `_vcomp_atomic_or_i2` | `0x7CE0` | 61 | UnwindData |  |
| 33 | `_vcomp_atomic_shl_i2` | `0x7D20` | 63 | UnwindData |  |
| 37 | `_vcomp_atomic_shr_i2` | `0x7D60` | 63 | UnwindData |  |
| 41 | `_vcomp_atomic_shr_ui2` | `0x7DA0` | 63 | UnwindData |  |
| 4 | `_vcomp_atomic_add_i4` | `0x7DE0` | 67 | UnwindData |  |
| 46 | `_vcomp_atomic_sub_i4` | `0x7E30` | 69 | UnwindData |  |
| 24 | `_vcomp_atomic_mul_i4` | `0x7E80` | 84 | UnwindData |  |
| 14 | `_vcomp_atomic_div_i4` | `0x7EE0` | 90 | UnwindData |  |
| 20 | `_vcomp_atomic_div_ui4` | `0x7F40` | 92 | UnwindData |  |
| 10 | `_vcomp_atomic_and_i4` | `0x7FA0` | 67 | UnwindData |  |
| 52 | `_vcomp_atomic_xor_i4` | `0x7FF0` | 67 | UnwindData |  |
| 30 | `_vcomp_atomic_or_i4` | `0x8040` | 67 | UnwindData |  |
| 34 | `_vcomp_atomic_shl_i4` | `0x8090` | 86 | UnwindData |  |
| 38 | `_vcomp_atomic_shr_i4` | `0x80F0` | 86 | UnwindData |  |
| 42 | `_vcomp_atomic_shr_ui4` | `0x8150` | 86 | UnwindData |  |
| 5 | `_vcomp_atomic_add_i8` | `0x81B0` | 72 | UnwindData |  |
| 47 | `_vcomp_atomic_sub_i8` | `0x8200` | 75 | UnwindData |  |
| 25 | `_vcomp_atomic_mul_i8` | `0x8250` | 89 | UnwindData |  |
| 15 | `_vcomp_atomic_div_i8` | `0x82B0` | 97 | UnwindData |  |
| 21 | `_vcomp_atomic_div_ui8` | `0x8320` | 97 | UnwindData |  |
| 11 | `_vcomp_atomic_and_i8` | `0x8390` | 72 | UnwindData |  |
| 53 | `_vcomp_atomic_xor_i8` | `0x83E0` | 72 | UnwindData |  |
| 31 | `_vcomp_atomic_or_i8` | `0x8430` | 72 | UnwindData |  |
| 35 | `_vcomp_atomic_shl_i8` | `0x8480` | 93 | UnwindData |  |
| 39 | `_vcomp_atomic_shr_i8` | `0x84E0` | 93 | UnwindData |  |
| 43 | `_vcomp_atomic_shr_ui8` | `0x8540` | 93 | UnwindData |  |
| 6 | `_vcomp_atomic_add_r4` | `0x85A0` | 95 | UnwindData |  |
| 48 | `_vcomp_atomic_sub_r4` | `0x8600` | 99 | UnwindData |  |
| 26 | `_vcomp_atomic_mul_r4` | `0x8670` | 95 | UnwindData |  |
| 16 | `_vcomp_atomic_div_r4` | `0x86D0` | 99 | UnwindData |  |
| 7 | `_vcomp_atomic_add_r8` | `0x8740` | 101 | UnwindData |  |
| 49 | `_vcomp_atomic_sub_r8` | `0x87B0` | 105 | UnwindData |  |
| 27 | `_vcomp_atomic_mul_r8` | `0x8820` | 101 | UnwindData |  |
| 17 | `_vcomp_atomic_div_r8` | `0x8890` | 105 | UnwindData |  |
