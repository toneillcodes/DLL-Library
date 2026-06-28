# Binary Specification: dtrace.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\dtrace.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fe07054a1768b79a60e53c568db833ba184bea60c6b9b62a90be372ea31f4e51`
* **Total Exported Functions:** 90

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 89 | `proc_gethandle` | `0x2A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `proc_getpid` | `0x2A90` | 10,704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x5460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllRegisterServer` | `0x5470` | 280 | UnwindData |  |
| 3 | `DllUnregisterServer` | `0x5590` | 31 | UnwindData |  |
| 4 | `DtSipCreateHash` | `0x55C0` | 922 | UnwindData |  |
| 5 | `DtSipDelSignature` | `0x5960` | 280 | UnwindData |  |
| 6 | `DtSipGetCaps` | `0x5A80` | 75 | UnwindData |  |
| 7 | `DtSipGetSignature` | `0x5AE0` | 225 | UnwindData |  |
| 8 | `DtSipIsMyFileType` | `0x5BD0` | 131 | UnwindData |  |
| 9 | `DtSipPutSignature` | `0x5C60` | 461 | UnwindData |  |
| 10 | `DtSipVerifyHash` | `0x5E40` | 542 | UnwindData |  |
| 34 | `dtrace_dof_destroy` | `0xDEF0` | 1,648 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `dtrace_addr2str` | `0xE560` | 366 | UnwindData |  |
| 27 | `dtrace_attr2str` | `0xE6E0` | 144 | UnwindData |  |
| 28 | `dtrace_class_name` | `0xE780` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `dtrace_desc2str` | `0xE7E0` | 111 | UnwindData |  |
| 50 | `dtrace_id2desc` | `0xE860` | 125 | UnwindData |  |
| 72 | `dtrace_stability_name` | `0xE8F0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `dtrace_str2attr` | `0xE970` | 436 | UnwindData |  |
| 81 | `dtrace_str2desc` | `0xEB30` | 29 | UnwindData |  |
| 84 | `dtrace_uaddr2str` | `0xEB60` | 453 | UnwindData |  |
| 88 | `dtrace_xstr2desc` | `0xED30` | 1,038 | UnwindData |  |
| 13 | `dtrace_aggregate_clear` | `0x10D90` | 153 | UnwindData |  |
| 14 | `dtrace_aggregate_print` | `0x10E30` | 115 | UnwindData |  |
| 15 | `dtrace_aggregate_snap` | `0x10EB0` | 209 | UnwindData |  |
| 16 | `dtrace_aggregate_walk` | `0x10F90` | 127 | UnwindData |  |
| 17 | `dtrace_aggregate_walk_joined` | `0x11020` | 2,252 | UnwindData |  |
| 18 | `dtrace_aggregate_walk_keyrevsorted` | `0x11900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `dtrace_aggregate_walk_keysorted` | `0x11920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `dtrace_aggregate_walk_keyvarrevsorted` | `0x11940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `dtrace_aggregate_walk_keyvarsorted` | `0x11960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `dtrace_aggregate_walk_sorted` | `0x11980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `dtrace_aggregate_walk_valrevsorted` | `0x11990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `dtrace_aggregate_walk_valsorted` | `0x119B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `dtrace_aggregate_walk_valvarrevsorted` | `0x119D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `dtrace_aggregate_walk_valvarsorted` | `0x119F0` | 3,968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `dtrace_close` | `0x12970` | 1,776 | UnwindData |  |
| 31 | `dtrace_ctlfd` | `0x13070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `dtrace_open` | `0x13080` | 24 | UnwindData |  |
| 69 | `dtrace_provider_modules` | `0x130A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `dtrace_version` | `0x130E0` | 18,368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `dtrace_consume` | `0x178A0` | 1,492 | UnwindData |  |
| 33 | `dtrace_dof_create` | `0x19330` | 1,994 | UnwindData |  |
| 41 | `dtrace_geterr_dof` | `0x19B00` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `dtrace_getopt_dof` | `0x19B40` | 260 | UnwindData |  |
| 35 | `dtrace_errmsg` | `0x19DA0` | 160 | UnwindData |  |
| 36 | `dtrace_errno` | `0x19E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `dtrace_faultstr` | `0x19E60` | 5,664 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `dtrace_fprinta` | `0x1B480` | 383 | UnwindData |  |
| 39 | `dtrace_fprintf` | `0x1B610` | 71 | UnwindData |  |
| 40 | `dtrace_freopen` | `0x1B660` | 460 | UnwindData |  |
| 54 | `dtrace_printa_create` | `0x1B840` | 24 | UnwindData |  |
| 55 | `dtrace_printf_create` | `0x1B860` | 145 | UnwindData |  |
| 56 | `dtrace_printf_format` | `0x1B900` | 527 | UnwindData |  |
| 83 | `dtrace_system` | `0x1BC40` | 180 | UnwindData |  |
| 42 | `dtrace_getopt` | `0x1EF70` | 226 | UnwindData |  |
| 70 | `dtrace_setopt` | `0x1F060` | 307 | UnwindData |  |
| 44 | `dtrace_go` | `0x1F1A0` | 718 | UnwindData |  |
| 71 | `dtrace_sleep` | `0x1F480` | 372 | UnwindData |  |
| 73 | `dtrace_status` | `0x1F600` | 396 | UnwindData |  |
| 79 | `dtrace_stop` | `0x1F7A0` | 255 | UnwindData |  |
| 87 | `dtrace_work` | `0x1F8B0` | 186 | UnwindData |  |
| 45 | `dtrace_handle_buffered` | `0x20220` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `dtrace_handle_drop` | `0x20290` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `dtrace_handle_err` | `0x202E0` | 243 | UnwindData |  |
| 48 | `dtrace_handle_proc` | `0x203E0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `dtrace_handle_setopt` | `0x20430` | 12,688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `dtrace_object_info` | `0x235C0` | 130 | UnwindData |  |
| 52 | `dtrace_object_iter` | `0x23650` | 124 | UnwindData |  |
| 85 | `dtrace_update` | `0x23830` | 692 | UnwindData |  |
| 57 | `dtrace_probe_info` | `0x24FF0` | 24 | UnwindData |  |
| 58 | `dtrace_probe_iter` | `0x25010` | 711 | UnwindData |  |
| 59 | `dtrace_proc_continue` | `0x25CF0` | 31 | UnwindData |  |
| 60 | `dtrace_proc_create` | `0x25D20` | 390 | UnwindData |  |
| 61 | `dtrace_proc_grab` | `0x25EB0` | 107 | UnwindData |  |
| 62 | `dtrace_proc_release` | `0x25F30` | 2,608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `dtrace_program_exec` | `0x26960` | 292 | UnwindData |  |
| 65 | `dtrace_program_header` | `0x26A90` | 499 | UnwindData |  |
| 66 | `dtrace_program_info` | `0x26C90` | 435 | UnwindData |  |
| 74 | `dtrace_stmt_action` | `0x26E50` | 113 | UnwindData |  |
| 75 | `dtrace_stmt_add` | `0x26ED0` | 85 | UnwindData |  |
| 76 | `dtrace_stmt_create` | `0x26F30` | 76 | UnwindData |  |
| 77 | `dtrace_stmt_destroy` | `0x26F90` | 252 | UnwindData |  |
| 78 | `dtrace_stmt_iter` | `0x270A0` | 113 | UnwindData |  |
| 64 | `dtrace_program_fcompile` | `0x2B470` | 67 | UnwindData |  |
| 68 | `dtrace_program_strcompile` | `0x2B4C0` | 73 | UnwindData |  |
| 67 | `dtrace_program_link` | `0x2B510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `dtrace_subrstr` | `0x2B520` | 120,880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `ctf_type_name` | `0x48D50` | 54 | UnwindData |  |
