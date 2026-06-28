# Binary Specification: vcomp140d.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\vcomp140d.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f460d27e37583e5f1b2af43333d86749f7bd1983b4e0d22ed2bdb60004ebff49`
* **Total Exported Functions:** 113

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `C2VectParallel` | `0x2180` | 165 | UnwindData |  |
| 68 | `_vcomp_fork` | `0x2230` | 839 | UnwindData |  |
| 89 | `_vcomp_set_num_threads` | `0x2580` | 79 | UnwindData |  |
| 59 | `_vcomp_for_dynamic_init` | `0x97F0` | 59 | UnwindData |  |
| 60 | `_vcomp_for_dynamic_init_i8` | `0x9830` | 63 | UnwindData |  |
| 61 | `_vcomp_for_dynamic_next` | `0x9870` | 42 | UnwindData |  |
| 62 | `_vcomp_for_dynamic_next_i8` | `0x98A0` | 42 | UnwindData |  |
| 63 | `_vcomp_for_static_end` | `0x98D0` | 60 | UnwindData |  |
| 64 | `_vcomp_for_static_init` | `0x9910` | 116 | UnwindData |  |
| 65 | `_vcomp_for_static_init_i8` | `0x9990` | 120 | UnwindData |  |
| 66 | `_vcomp_for_static_simple_init` | `0x9A10` | 71 | UnwindData |  |
| 67 | `_vcomp_for_static_simple_init_i8` | `0x9A60` | 75 | UnwindData |  |
| 74 | `_vcomp_ordered_begin` | `0x9AB0` | 346 | UnwindData |  |
| 75 | `_vcomp_ordered_end` | `0x9C10` | 263 | UnwindData |  |
| 76 | `_vcomp_ordered_loop_end` | `0x9D20` | 250 | UnwindData |  |
| 55 | `_vcomp_copyprivate_broadcast` | `0xA560` | 99 | UnwindData |  |
| 56 | `_vcomp_copyprivate_receive` | `0xA5D0` | 169 | UnwindData |  |
| 69 | `_vcomp_get_thread_num` | `0xA680` | 63 | UnwindData |  |
| 72 | `_vcomp_master_begin` | `0xA6C0` | 117 | UnwindData |  |
| 73 | `_vcomp_master_end` | `0xA740` | 45 | UnwindData |  |
| 87 | `_vcomp_sections_init` | `0xA770` | 575 | UnwindData |  |
| 88 | `_vcomp_sections_next` | `0xA9B0` | 70 | UnwindData |  |
| 90 | `_vcomp_single_begin` | `0xAA00` | 522 | UnwindData |  |
| 91 | `_vcomp_single_end` | `0xAC10` | 45 | UnwindData |  |
| 92 | `omp_destroy_lock` | `0xB290` | 78 | UnwindData |  |
| 93 | `omp_destroy_nest_lock` | `0xB2E0` | 78 | UnwindData |  |
| 94 | `omp_get_dynamic` | `0xB330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `omp_get_max_threads` | `0xB340` | 43 | UnwindData |  |
| 96 | `omp_get_nested` | `0xB370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `omp_get_num_procs` | `0xB380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `omp_get_num_threads` | `0xB390` | 70 | UnwindData |  |
| 99 | `omp_get_thread_num` | `0xB3E0` | 63 | UnwindData |  |
| 100 | `omp_get_wtick` | `0xB420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `omp_get_wtime` | `0xB430` | 181 | UnwindData |  |
| 102 | `omp_in_parallel` | `0xB4F0` | 73 | UnwindData |  |
| 103 | `omp_init_lock` | `0xB540` | 76 | UnwindData |  |
| 104 | `omp_init_nest_lock` | `0xB590` | 76 | UnwindData |  |
| 105 | `omp_set_dynamic` | `0xB5E0` | 78 | UnwindData |  |
| 106 | `omp_set_lock` | `0xB630` | 28 | UnwindData |  |
| 107 | `omp_set_nest_lock` | `0xB650` | 28 | UnwindData |  |
| 108 | `omp_set_nested` | `0xB670` | 78 | UnwindData |  |
| 109 | `omp_set_num_threads` | `0xB6C0` | 100 | UnwindData |  |
| 110 | `omp_test_lock` | `0xB730` | 35 | UnwindData |  |
| 111 | `omp_test_nest_lock` | `0xB760` | 35 | UnwindData |  |
| 112 | `omp_unset_lock` | `0xB790` | 28 | UnwindData |  |
| 113 | `omp_unset_nest_lock` | `0xB7B0` | 28 | UnwindData |  |
| 77 | `_vcomp_reduction_i1` | `0x11C80` | 44 | UnwindData |  |
| 78 | `_vcomp_reduction_i2` | `0x11CB0` | 45 | UnwindData |  |
| 79 | `_vcomp_reduction_i4` | `0x11CE0` | 43 | UnwindData |  |
| 80 | `_vcomp_reduction_i8` | `0x11D10` | 43 | UnwindData |  |
| 81 | `_vcomp_reduction_r4` | `0x11D40` | 45 | UnwindData |  |
| 82 | `_vcomp_reduction_r8` | `0x11D70` | 45 | UnwindData |  |
| 83 | `_vcomp_reduction_u1` | `0x11DA0` | 44 | UnwindData |  |
| 84 | `_vcomp_reduction_u2` | `0x11DD0` | 45 | UnwindData |  |
| 85 | `_vcomp_reduction_u4` | `0x11E00` | 43 | UnwindData |  |
| 86 | `_vcomp_reduction_u8` | `0x11E30` | 43 | UnwindData |  |
| 2 | `_vcomp_atomic_add_i1` | `0x13210` | 70 | UnwindData |  |
| 3 | `_vcomp_atomic_add_i2` | `0x13260` | 72 | UnwindData |  |
| 4 | `_vcomp_atomic_add_i4` | `0x132B0` | 86 | UnwindData |  |
| 5 | `_vcomp_atomic_add_i8` | `0x13310` | 92 | UnwindData |  |
| 6 | `_vcomp_atomic_add_r4` | `0x13370` | 162 | UnwindData |  |
| 7 | `_vcomp_atomic_add_r8` | `0x13420` | 172 | UnwindData |  |
| 8 | `_vcomp_atomic_and_i1` | `0x134D0` | 70 | UnwindData |  |
| 9 | `_vcomp_atomic_and_i2` | `0x13520` | 72 | UnwindData |  |
| 10 | `_vcomp_atomic_and_i4` | `0x13570` | 86 | UnwindData |  |
| 11 | `_vcomp_atomic_and_i8` | `0x135D0` | 92 | UnwindData |  |
| 12 | `_vcomp_atomic_div_i1` | `0x13630` | 79 | UnwindData |  |
| 13 | `_vcomp_atomic_div_i2` | `0x13680` | 81 | UnwindData |  |
| 14 | `_vcomp_atomic_div_i4` | `0x136E0` | 130 | UnwindData |  |
| 15 | `_vcomp_atomic_div_i8` | `0x13770` | 147 | UnwindData |  |
| 16 | `_vcomp_atomic_div_r4` | `0x13810` | 162 | UnwindData |  |
| 17 | `_vcomp_atomic_div_r8` | `0x138C0` | 172 | UnwindData |  |
| 18 | `_vcomp_atomic_div_ui1` | `0x13970` | 79 | UnwindData |  |
| 19 | `_vcomp_atomic_div_ui2` | `0x139C0` | 81 | UnwindData |  |
| 20 | `_vcomp_atomic_div_ui4` | `0x13A20` | 132 | UnwindData |  |
| 21 | `_vcomp_atomic_div_ui8` | `0x13AB0` | 147 | UnwindData |  |
| 22 | `_vcomp_atomic_mul_i1` | `0x13B50` | 71 | UnwindData |  |
| 23 | `_vcomp_atomic_mul_i2` | `0x13BA0` | 73 | UnwindData |  |
| 24 | `_vcomp_atomic_mul_i4` | `0x13BF0` | 130 | UnwindData |  |
| 25 | `_vcomp_atomic_mul_i8` | `0x13C80` | 145 | UnwindData |  |
| 26 | `_vcomp_atomic_mul_r4` | `0x13D20` | 162 | UnwindData |  |
| 27 | `_vcomp_atomic_mul_r8` | `0x13DD0` | 172 | UnwindData |  |
| 28 | `_vcomp_atomic_or_i1` | `0x13E80` | 70 | UnwindData |  |
| 29 | `_vcomp_atomic_or_i2` | `0x13ED0` | 72 | UnwindData |  |
| 30 | `_vcomp_atomic_or_i4` | `0x13F20` | 86 | UnwindData |  |
| 31 | `_vcomp_atomic_or_i8` | `0x13F80` | 92 | UnwindData |  |
| 32 | `_vcomp_atomic_shl_i1` | `0x13FE0` | 77 | UnwindData |  |
| 33 | `_vcomp_atomic_shl_i2` | `0x14030` | 81 | UnwindData |  |
| 34 | `_vcomp_atomic_shl_i4` | `0x14090` | 135 | UnwindData |  |
| 35 | `_vcomp_atomic_shl_i8` | `0x14120` | 152 | UnwindData |  |
| 36 | `_vcomp_atomic_shr_i1` | `0x141C0` | 77 | UnwindData |  |
| 37 | `_vcomp_atomic_shr_i2` | `0x14210` | 81 | UnwindData |  |
| 38 | `_vcomp_atomic_shr_i4` | `0x14270` | 135 | UnwindData |  |
| 39 | `_vcomp_atomic_shr_i8` | `0x14300` | 152 | UnwindData |  |
| 40 | `_vcomp_atomic_shr_ui1` | `0x143A0` | 77 | UnwindData |  |
| 41 | `_vcomp_atomic_shr_ui2` | `0x143F0` | 81 | UnwindData |  |
| 42 | `_vcomp_atomic_shr_ui4` | `0x14450` | 135 | UnwindData |  |
| 43 | `_vcomp_atomic_shr_ui8` | `0x144E0` | 152 | UnwindData |  |
| 44 | `_vcomp_atomic_sub_i1` | `0x14580` | 70 | UnwindData |  |
| 45 | `_vcomp_atomic_sub_i2` | `0x145D0` | 72 | UnwindData |  |
| 46 | `_vcomp_atomic_sub_i4` | `0x14620` | 88 | UnwindData |  |
| 47 | `_vcomp_atomic_sub_i8` | `0x14680` | 95 | UnwindData |  |
| 48 | `_vcomp_atomic_sub_r4` | `0x146E0` | 162 | UnwindData |  |
| 49 | `_vcomp_atomic_sub_r8` | `0x14790` | 172 | UnwindData |  |
| 50 | `_vcomp_atomic_xor_i1` | `0x14840` | 70 | UnwindData |  |
| 51 | `_vcomp_atomic_xor_i2` | `0x14890` | 72 | UnwindData |  |
| 52 | `_vcomp_atomic_xor_i4` | `0x148E0` | 86 | UnwindData |  |
| 53 | `_vcomp_atomic_xor_i8` | `0x14940` | 92 | UnwindData |  |
| 54 | `_vcomp_barrier` | `0x149A0` | 507 | UnwindData |  |
| 57 | `_vcomp_enter_critsect` | `0x14BA0` | 183 | UnwindData |  |
| 58 | `_vcomp_flush` | `0x14C60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `_vcomp_leave_critsect` | `0x14C80` | 25 | UnwindData |  |
| 71 | `_vcomp_master_barrier` | `0x14CA0` | 368 | UnwindData |  |
