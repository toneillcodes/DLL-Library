# Binary Specification: vcomp100.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\vcomp100.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `34abd773c85ce0cac56bd93c12b00b03a3a695d19f477ce275a64f09984c5492`
* **Total Exported Functions:** 112

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 62 | `_vcomp_for_static_end` | `0x1410` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `_vcomp_set_num_threads` | `0x1428` | 56 | UnwindData |  |
| 67 | `_vcomp_fork` | `0x1468` | 572 | UnwindData |  |
| 65 | `_vcomp_for_static_simple_init` | `0x1978` | 282 | UnwindData |  |
| 66 | `_vcomp_for_static_simple_init_i8` | `0x1A98` | 288 | UnwindData |  |
| 63 | `_vcomp_for_static_init` | `0x1BC0` | 452 | UnwindData |  |
| 64 | `_vcomp_for_static_init_i8` | `0x1D8C` | 77 | UnwindData |  |
| 58 | `_vcomp_for_dynamic_init` | `0x1DE0` | 177 | UnwindData |  |
| 59 | `_vcomp_for_dynamic_init_i8` | `0x1E98` | 180 | UnwindData |  |
| 60 | `_vcomp_for_dynamic_next` | `0x1F54` | 200 | UnwindData |  |
| 61 | `_vcomp_for_dynamic_next_i8` | `0x2024` | 205 | UnwindData |  |
| 73 | `_vcomp_ordered_begin` | `0x20F8` | 122 | UnwindData |  |
| 74 | `_vcomp_ordered_end` | `0x2178` | 122 | UnwindData |  |
| 75 | `_vcomp_ordered_loop_end` | `0x21F8` | 139 | UnwindData |  |
| 86 | `_vcomp_sections_init` | `0x3FA8` | 181 | UnwindData |  |
| 87 | `_vcomp_sections_next` | `0x4064` | 73 | UnwindData |  |
| 89 | `_vcomp_single_begin` | `0x40B4` | 243 | UnwindData |  |
| 90 | `_vcomp_single_end` | `0x41B0` | 44 | UnwindData |  |
| 54 | `_vcomp_copyprivate_broadcast` | `0x41E4` | 147 | UnwindData |  |
| 55 | `_vcomp_copyprivate_receive` | `0x4280` | 116 | UnwindData |  |
| 71 | `_vcomp_master_begin` | `0x42FC` | 68 | UnwindData |  |
| 72 | `_vcomp_master_end` | `0x4348` | 39 | UnwindData |  |
| 68 | `_vcomp_get_thread_num` | `0x4378` | 34 | UnwindData |  |
| 108 | `omp_set_num_threads` | `0x43A0` | 63 | UnwindData |  |
| 97 | `omp_get_num_threads` | `0x43E8` | 45 | UnwindData |  |
| 94 | `omp_get_max_threads` | `0x441C` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `omp_get_thread_num` | `0x4434` | 40 | UnwindData |  |
| 96 | `omp_get_num_procs` | `0x4464` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `omp_in_parallel` | `0x4474` | 45 | UnwindData |  |
| 104 | `omp_set_dynamic` | `0x44A8` | 32 | UnwindData |  |
| 93 | `omp_get_dynamic` | `0x44D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `omp_set_nested` | `0x44E0` | 32 | UnwindData |  |
| 95 | `omp_get_nested` | `0x4508` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `omp_set_lock` | `0x4518` | 49 | UnwindData |  |
| 111 | `omp_unset_lock` | `0x4550` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `omp_test_lock` | `0x4564` | 71 | UnwindData |  |
| 102 | `omp_init_lock` | `0x45B4` | 67 | UnwindData |  |
| 103 | `omp_init_nest_lock` | `0x45B4` | 67 | UnwindData |  |
| 91 | `omp_destroy_lock` | `0x4600` | 65 | UnwindData |  |
| 92 | `omp_destroy_nest_lock` | `0x4600` | 65 | UnwindData |  |
| 106 | `omp_set_nest_lock` | `0x4648` | 28 | UnwindData |  |
| 112 | `omp_unset_nest_lock` | `0x466C` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `omp_test_nest_lock` | `0x4680` | 44 | UnwindData |  |
| 100 | `omp_get_wtime` | `0x46B4` | 79 | UnwindData |  |
| 99 | `omp_get_wtick` | `0x470C` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `_vcomp_reduction_i1` | `0x483C` | 277 | UnwindData |  |
| 82 | `_vcomp_reduction_u1` | `0x483C` | 277 | UnwindData |  |
| 77 | `_vcomp_reduction_i2` | `0x4958` | 280 | UnwindData |  |
| 83 | `_vcomp_reduction_u2` | `0x4958` | 280 | UnwindData |  |
| 78 | `_vcomp_reduction_i4` | `0x4A78` | 280 | UnwindData |  |
| 84 | `_vcomp_reduction_u4` | `0x4A78` | 280 | UnwindData |  |
| 79 | `_vcomp_reduction_i8` | `0x4B98` | 281 | UnwindData |  |
| 85 | `_vcomp_reduction_u8` | `0x4B98` | 281 | UnwindData |  |
| 80 | `_vcomp_reduction_r4` | `0x4CB8` | 292 | UnwindData |  |
| 81 | `_vcomp_reduction_r8` | `0x4DE4` | 294 | UnwindData |  |
| 53 | `_vcomp_barrier` | `0x61D4` | 229 | UnwindData |  |
| 70 | `_vcomp_master_barrier` | `0x62C0` | 302 | UnwindData |  |
| 56 | `_vcomp_enter_critsect` | `0x63F4` | 148 | UnwindData |  |
| 69 | `_vcomp_leave_critsect` | `0x6490` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `_vcomp_flush` | `0x64A0` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `_vcomp_atomic_add_i1` | `0x64BC` | 61 | UnwindData |  |
| 43 | `_vcomp_atomic_sub_i1` | `0x6500` | 61 | UnwindData |  |
| 21 | `_vcomp_atomic_mul_i1` | `0x6544` | 62 | UnwindData |  |
| 11 | `_vcomp_atomic_div_i1` | `0x6588` | 60 | UnwindData |  |
| 17 | `_vcomp_atomic_div_ui1` | `0x65CC` | 60 | UnwindData |  |
| 7 | `_vcomp_atomic_and_i1` | `0x6610` | 61 | UnwindData |  |
| 49 | `_vcomp_atomic_xor_i1` | `0x6654` | 61 | UnwindData |  |
| 27 | `_vcomp_atomic_or_i1` | `0x6698` | 61 | UnwindData |  |
| 31 | `_vcomp_atomic_shl_i1` | `0x66DC` | 62 | UnwindData |  |
| 35 | `_vcomp_atomic_shr_i1` | `0x6720` | 62 | UnwindData |  |
| 39 | `_vcomp_atomic_shr_ui1` | `0x6764` | 62 | UnwindData |  |
| 2 | `_vcomp_atomic_add_i2` | `0x67A8` | 63 | UnwindData |  |
| 44 | `_vcomp_atomic_sub_i2` | `0x67F0` | 63 | UnwindData |  |
| 22 | `_vcomp_atomic_mul_i2` | `0x6838` | 64 | UnwindData |  |
| 12 | `_vcomp_atomic_div_i2` | `0x6880` | 61 | UnwindData |  |
| 18 | `_vcomp_atomic_div_ui2` | `0x68C4` | 61 | UnwindData |  |
| 8 | `_vcomp_atomic_and_i2` | `0x6908` | 63 | UnwindData |  |
| 50 | `_vcomp_atomic_xor_i2` | `0x6950` | 63 | UnwindData |  |
| 28 | `_vcomp_atomic_or_i2` | `0x6998` | 63 | UnwindData |  |
| 32 | `_vcomp_atomic_shl_i2` | `0x69E0` | 66 | UnwindData |  |
| 36 | `_vcomp_atomic_shr_i2` | `0x6A28` | 66 | UnwindData |  |
| 40 | `_vcomp_atomic_shr_ui2` | `0x6A70` | 66 | UnwindData |  |
| 3 | `_vcomp_atomic_add_i4` | `0x6AB8` | 64 | UnwindData |  |
| 45 | `_vcomp_atomic_sub_i4` | `0x6B00` | 66 | UnwindData |  |
| 23 | `_vcomp_atomic_mul_i4` | `0x6B48` | 87 | UnwindData |  |
| 13 | `_vcomp_atomic_div_i4` | `0x6BA8` | 90 | UnwindData |  |
| 19 | `_vcomp_atomic_div_ui4` | `0x6C08` | 92 | UnwindData |  |
| 9 | `_vcomp_atomic_and_i4` | `0x6C6C` | 63 | UnwindData |  |
| 51 | `_vcomp_atomic_xor_i4` | `0x6CB4` | 63 | UnwindData |  |
| 29 | `_vcomp_atomic_or_i4` | `0x6CFC` | 63 | UnwindData |  |
| 33 | `_vcomp_atomic_shl_i4` | `0x6D44` | 82 | UnwindData |  |
| 37 | `_vcomp_atomic_shr_i4` | `0x6D9C` | 82 | UnwindData |  |
| 41 | `_vcomp_atomic_shr_ui4` | `0x6DF4` | 82 | UnwindData |  |
| 4 | `_vcomp_atomic_add_i8` | `0x6E4C` | 67 | UnwindData |  |
| 46 | `_vcomp_atomic_sub_i8` | `0x6E98` | 70 | UnwindData |  |
| 24 | `_vcomp_atomic_mul_i8` | `0x6EE4` | 89 | UnwindData |  |
| 14 | `_vcomp_atomic_div_i8` | `0x6F44` | 97 | UnwindData |  |
| 20 | `_vcomp_atomic_div_ui8` | `0x6FAC` | 97 | UnwindData |  |
| 10 | `_vcomp_atomic_and_i8` | `0x7014` | 66 | UnwindData |  |
| 52 | `_vcomp_atomic_xor_i8` | `0x705C` | 66 | UnwindData |  |
| 30 | `_vcomp_atomic_or_i8` | `0x70A4` | 66 | UnwindData |  |
| 34 | `_vcomp_atomic_shl_i8` | `0x70EC` | 87 | UnwindData |  |
| 38 | `_vcomp_atomic_shr_i8` | `0x714C` | 87 | UnwindData |  |
| 42 | `_vcomp_atomic_shr_ui8` | `0x71AC` | 87 | UnwindData |  |
| 5 | `_vcomp_atomic_add_r4` | `0x720C` | 103 | UnwindData |  |
| 47 | `_vcomp_atomic_sub_r4` | `0x727C` | 107 | UnwindData |  |
| 25 | `_vcomp_atomic_mul_r4` | `0x72F0` | 103 | UnwindData |  |
| 15 | `_vcomp_atomic_div_r4` | `0x7360` | 107 | UnwindData |  |
| 6 | `_vcomp_atomic_add_r8` | `0x73D4` | 108 | UnwindData |  |
| 48 | `_vcomp_atomic_sub_r8` | `0x7448` | 112 | UnwindData |  |
| 26 | `_vcomp_atomic_mul_r8` | `0x74C0` | 108 | UnwindData |  |
| 16 | `_vcomp_atomic_div_r8` | `0x7534` | 112 | UnwindData |  |
