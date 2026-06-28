# Binary Specification: StateRepository.Core.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\StateRepository.Core.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `824f3c5796e11d34d827764fa514913b9beea1799777a994e427aa5b747b5ace`
* **Total Exported Functions:** 280

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 269 | `sqlite3_wal_hook` | `0x7370` | 148 | UnwindData |  |
| 266 | `sqlite3_wal_autocheckpoint` | `0x7410` | 117 | UnwindData |  |
| 120 | `sqlite3_last_insert_rowid` | `0x7490` | 55 | UnwindData |  |
| 33 | `sqlite3_busy_timeout` | `0x7AE0` | 126 | UnwindData |  |
| 99 | `sqlite3_extended_result_codes` | `0x7B70` | 121 | UnwindData |  |
| 145 | `sqlite3_prepare` | `0x7C40` | 39 | UnwindData |  |
| 247 | `sqlite3_value_text` | `0x7C70` | 70 | UnwindData |  |
| 248 | `sqlite3_value_text16` | `0x7D40` | 70 | UnwindData |  |
| 250 | `sqlite3_value_text16le` | `0x7D40` | 70 | UnwindData |  |
| 53 | `sqlite3_column_text` | `0x7D90` | 173 | UnwindData |  |
| 43 | `sqlite3_column_bytes` | `0x7E50` | 132 | UnwindData |  |
| 55 | `sqlite3_column_type` | `0x7EE0` | 141 | UnwindData |  |
| 95 | `sqlite3_exec` | `0x8060` | 980 | UnwindData |  |
| 195 | `sqlite3_step` | `0x8440` | 384 | UnwindData |  |
| 157 | `sqlite3_reset` | `0x8910` | 190 | UnwindData |  |
| 42 | `sqlite3_column_blob` | `0x8A60` | 132 | UnwindData |  |
| 233 | `sqlite3_value_blob` | `0x8AF0` | 122 | UnwindData |  |
| 49 | `sqlite3_column_int` | `0x8BC0` | 180 | UnwindData |  |
| 50 | `sqlite3_column_int64` | `0x8C80` | 181 | UnwindData |  |
| 54 | `sqlite3_column_text16` | `0x8D70` | 228 | UnwindData |  |
| 13 | `sqlite3_bind_int` | `0x8FD0` | 141 | UnwindData |  |
| 14 | `sqlite3_bind_int64` | `0x9070` | 141 | UnwindData |  |
| 21 | `sqlite3_bind_text16` | `0x9110` | 218 | UnwindData |  |
| 10 | `sqlite3_bind_blob` | `0x91F0` | 247 | UnwindData |  |
| 136 | `sqlite3_mutex_leave` | `0x94F0` | 1,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `sqlite3_prepare_v2` | `0x9BF0` | 42 | UnwindData |  |
| 134 | `sqlite3_mutex_enter` | `0x9E40` | 1,424 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `sqlite3_create_function_v2` | `0xA3D0` | 431 | UnwindData |  |
| 105 | `sqlite3_free` | `0xB460` | 133 | UnwindData |  |
| 78 | `sqlite3_db_filename` | `0xD4C0` | 20 | UnwindData |  |
| 90 | `sqlite3_errcode` | `0xE620` | 97 | UnwindData |  |
| 125 | `sqlite3_log` | `0xE690` | 44 | UnwindData |  |
| 204 | `sqlite3_str_appendf` | `0xE710` | 34 | UnwindData |  |
| 211 | `sqlite3_str_vappendf` | `0xE740` | 4,802 | UnwindData |  |
| 213 | `sqlite3_stricmp` | `0xFBB0` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 256 | `sqlite3_vsnprintf` | `0xFE00` | 130 | UnwindData |  |
| 192 | `sqlite3_sql` | `0x13F00` | 2,592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `sqlite3_aggregate_context` | `0x14920` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 177 | `sqlite3_result_value` | `0x14D00` | 85 | UnwindData |  |
| 275 | `sqlite3_win32_sleep` | `0x15B10` | 1,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `sqlite3_randomness` | `0x15F20` | 406 | UnwindData |  |
| 186 | `sqlite3_shutdown` | `0x16C80` | 207 | UnwindData |  |
| 143 | `sqlite3_os_init` | `0x16D60` | 429 | UnwindData |  |
| 158 | `sqlite3_reset_auto_extension` | `0x175E0` | 76 | UnwindData |  |
| 144 | `sqlite3_overload_function` | `0x17640` | 274 | UnwindData |  |
| 131 | `sqlite3_mprintf` | `0x17760` | 57 | UnwindData |  |
| 253 | `sqlite3_vfs_register` | `0x177A0` | 153 | UnwindData |  |
| 255 | `sqlite3_vmprintf` | `0x178A0` | 243 | UnwindData |  |
| 254 | `sqlite3_vfs_unregister` | `0x179A0` | 75 | UnwindData |  |
| 133 | `sqlite3_mutex_alloc` | `0x18050` | 57 | UnwindData |  |
| 127 | `sqlite3_malloc64` | `0x18090` | 40 | UnwindData |  |
| 126 | `sqlite3_malloc` | `0x180C0` | 49 | UnwindData |  |
| 155 | `sqlite3_realloc64` | `0x18100` | 52 | UnwindData |  |
| 114 | `sqlite3_initialize` | `0x18290` | 472 | UnwindData |  |
| 252 | `sqlite3_vfs_find` | `0x18470` | 141 | UnwindData |  |
| 62 | `sqlite3_config` | `0x185C0` | 988 | UnwindData |  |
| 188 | `sqlite3_snprintf` | `0x1BD10` | 132 | UnwindData |  |
| 108 | `sqlite3_get_autocommit` | `0x1CB10` | 93 | UnwindData |  |
| 91 | `sqlite3_errmsg` | `0x1D6B0` | 166 | UnwindData |  |
| 79 | `sqlite3_db_handle` | `0x1D8C0` | 1,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 215 | `sqlite3_strnicmp` | `0x1E040` | 12,160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | `sqlite3_str_append` | `0x20FC0` | 59 | UnwindData |  |
| 241 | `sqlite3_value_int` | `0x25420` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 242 | `sqlite3_value_int64` | `0x25420` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 234 | `sqlite3_value_bytes` | `0x256C0` | 2,336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 194 | `sqlite3_status64` | `0x25FE0` | 198 | UnwindData |  |
| 193 | `sqlite3_status` | `0x26520` | 253 | UnwindData |  |
| 132 | `sqlite3_msize` | `0x26890` | 33 | UnwindData |  |
| 141 | `sqlite3_open_v2` | `0x268C0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | `sqlite3_str_appendall` | `0x26990` | 30 | UnwindData |  |
| 38 | `sqlite3_close` | `0x26AE0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 268 | `sqlite3_wal_checkpoint_v2` | `0x26B40` | 288 | UnwindData |  |
| 228 | `sqlite3_uri_boolean` | `0x26CC0` | 48 | UnwindData |  |
| 231 | `sqlite3_uri_parameter` | `0x26D00` | 45 | UnwindData |  |
| 51 | `sqlite3_column_name` | `0x276C0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `sqlite3_busy_handler` | `0x27740` | 146 | UnwindData |  |
| 82 | `sqlite3_db_readonly` | `0x279D0` | 111 | UnwindData |  |
| 112 | `sqlite3_global_recover` | `0x28030` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `sqlite3_memory_alarm` | `0x28030` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `sqlite3_release_memory` | `0x28030` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `sqlite3_mutex_free` | `0x282D0` | 27 | UnwindData |  |
| 251 | `sqlite3_value_type` | `0x28300` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `sqlite3_result_text64` | `0x285F0` | 111 | UnwindData |  |
| 9 | `sqlite3_backup_step` | `0x60F00` | 1,242 | UnwindData |  |
| 35 | `sqlite3_changes` | `0x613E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `sqlite3_clear_bindings` | `0x613F0` | 201 | UnwindData |  |
| 77 | `sqlite3_db_config` | `0x614C0` | 270 | UnwindData |  |
| 84 | `sqlite3_db_status` | `0x615E0` | 1,078 | UnwindData |  |
| 100 | `sqlite3_file_control` | `0x61A20` | 333 | UnwindData |  |
| 104 | `sqlite3_finalize` | `0x61B80` | 145 | UnwindData |  |
| 159 | `sqlite3_result_blob` | `0x61C20` | 54 | UnwindData |  |
| 167 | `sqlite3_result_int` | `0x61C60` | 26 | UnwindData |  |
| 168 | `sqlite3_result_int64` | `0x61C80` | 23 | UnwindData |  |
| 172 | `sqlite3_result_text` | `0x61CA0` | 49 | UnwindData |  |
| 214 | `sqlite3_strlike` | `0x61CE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 221 | `sqlite3_total_changes` | `0x61D10` | 41,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `sqlite3_db_release_memory` | `0x6BDA0` | 192 | UnwindData |  |
| 166 | `sqlite3_result_error_toobig` | `0x6C010` | 50 | UnwindData |  |
| 63 | `sqlite3_context_db_handle` | `0x6C050` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 209 | `sqlite3_str_reset` | `0x6C230` | 65 | UnwindData |  |
| 267 | `sqlite3_wal_checkpoint` | `0x6C4D0` | 27 | UnwindData |  |
| 142 | `sqlite3_os_end` | `0x6C540` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 191 | `sqlite3_sourceid` | `0x6C570` | 75,152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 219 | `sqlite3_thread_cleanup` | `0x7EB00` | 82,384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `sqlite3_aggregate_count` | `0x92CD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `sqlite3_auto_extension` | `0x92CE0` | 193 | UnwindData |  |
| 4 | `sqlite3_autovacuum_pages` | `0x92DB0` | 178 | UnwindData |  |
| 5 | `sqlite3_backup_finish` | `0x92E70` | 221 | UnwindData |  |
| 6 | `sqlite3_backup_init` | `0x92F60` | 337 | UnwindData |  |
| 7 | `sqlite3_backup_pagecount` | `0x930C0` | 44 | UnwindData |  |
| 8 | `sqlite3_backup_remaining` | `0x93100` | 44 | UnwindData |  |
| 11 | `sqlite3_bind_blob64` | `0x93140` | 30 | UnwindData |  |
| 12 | `sqlite3_bind_double` | `0x93170` | 100 | UnwindData |  |
| 15 | `sqlite3_bind_null` | `0x931E0` | 52 | UnwindData |  |
| 16 | `sqlite3_bind_parameter_count` | `0x93220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `sqlite3_bind_parameter_index` | `0x93240` | 30 | UnwindData |  |
| 18 | `sqlite3_bind_parameter_name` | `0x93270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `sqlite3_bind_pointer` | `0x93290` | 142 | UnwindData |  |
| 20 | `sqlite3_bind_text` | `0x93330` | 33 | UnwindData |  |
| 22 | `sqlite3_bind_text64` | `0x93360` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `sqlite3_bind_value` | `0x933A0` | 184 | UnwindData |  |
| 24 | `sqlite3_bind_zeroblob` | `0x93460` | 99 | UnwindData |  |
| 25 | `sqlite3_bind_zeroblob64` | `0x934D0` | 140 | UnwindData |  |
| 26 | `sqlite3_blob_bytes` | `0x93570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `sqlite3_blob_close` | `0x93590` | 87 | UnwindData |  |
| 28 | `sqlite3_blob_open` | `0x935F0` | 1,314 | UnwindData |  |
| 29 | `sqlite3_blob_read` | `0x93B20` | 27 | UnwindData |  |
| 30 | `sqlite3_blob_reopen` | `0x93B50` | 203 | UnwindData |  |
| 31 | `sqlite3_blob_write` | `0x93C30` | 27 | UnwindData |  |
| 34 | `sqlite3_cancel_auto_extension` | `0x93C60` | 140 | UnwindData |  |
| 36 | `sqlite3_changes64` | `0x93D00` | 53 | UnwindData |  |
| 39 | `sqlite3_close_v2` | `0x93D40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `sqlite3_collation_needed` | `0x93D50` | 114 | UnwindData |  |
| 41 | `sqlite3_collation_needed16` | `0x93DD0` | 114 | UnwindData |  |
| 44 | `sqlite3_column_bytes16` | `0x93E50` | 52 | UnwindData |  |
| 45 | `sqlite3_column_count` | `0x93E90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `sqlite3_column_decltype` | `0x93EB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `sqlite3_column_decltype16` | `0x93ED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `sqlite3_column_double` | `0x93EF0` | 53 | UnwindData |  |
| 52 | `sqlite3_column_name16` | `0x93F30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `sqlite3_column_value` | `0x93F50` | 75 | UnwindData |  |
| 57 | `sqlite3_commit_hook` | `0x93FB0` | 126 | UnwindData |  |
| 58 | `sqlite3_compileoption_get` | `0x94040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `sqlite3_compileoption_used` | `0x94060` | 192 | UnwindData |  |
| 60 | `sqlite3_complete` | `0x94130` | 694 | UnwindData |  |
| 61 | `sqlite3_complete16` | `0x943F0` | 107 | UnwindData |  |
| 64 | `sqlite3_create_collation` | `0x94470` | 31 | UnwindData |  |
| 65 | `sqlite3_create_collation16` | `0x944A0` | 205 | UnwindData |  |
| 66 | `sqlite3_create_collation_v2` | `0x94580` | 161 | UnwindData |  |
| 67 | `sqlite3_create_filename` | `0x94630` | 354 | UnwindData |  |
| 68 | `sqlite3_create_function` | `0x947A0` | 80 | UnwindData |  |
| 69 | `sqlite3_create_function16` | `0x94800` | 256 | UnwindData |  |
| 71 | `sqlite3_create_module` | `0x94910` | 115 | UnwindData |  |
| 72 | `sqlite3_create_module_v2` | `0x94990` | 119 | UnwindData |  |
| 73 | `sqlite3_create_window_function` | `0x94A10` | 95 | UnwindData |  |
| 74 | `sqlite3_data_count` | `0x94A80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `sqlite3_database_file_object` | `0x94AB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `sqlite3_db_cacheflush` | `0x94AE0` | 274 | UnwindData |  |
| 80 | `sqlite3_db_mutex` | `0x94C00` | 53 | UnwindData |  |
| 81 | `sqlite3_db_name` | `0x94C40` | 85 | UnwindData |  |
| 85 | `sqlite3_declare_vtab` | `0x94CA0` | 693 | UnwindData |  |
| 86 | `sqlite3_deserialize` | `0x94F60` | 453 | UnwindData |  |
| 87 | `sqlite3_drop_modules` | `0x95130` | 179 | UnwindData |  |
| 88 | `sqlite3_enable_load_extension` | `0x951F0` | 108 | UnwindData |  |
| 89 | `sqlite3_enable_shared_cache` | `0x95270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `sqlite3_errmsg16` | `0x95280` | 162 | UnwindData |  |
| 93 | `sqlite3_error_offset` | `0x95330` | 71 | UnwindData |  |
| 94 | `sqlite3_errstr` | `0x95380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `sqlite3_expanded_sql` | `0x95390` | 91 | UnwindData |  |
| 97 | `sqlite3_expired` | `0x95400` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `sqlite3_extended_errcode` | `0x95420` | 71 | UnwindData |  |
| 101 | `sqlite3_filename_database` | `0x95470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `sqlite3_filename_journal` | `0x95490` | 81 | UnwindData |  |
| 103 | `sqlite3_filename_wal` | `0x954F0` | 42 | UnwindData |  |
| 106 | `sqlite3_free_filename` | `0x95520` | 29 | UnwindData |  |
| 107 | `sqlite3_free_table` | `0x95550` | 87 | UnwindData |  |
| 109 | `sqlite3_get_auxdata` | `0x955B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `sqlite3_get_clientdata` | `0x955F0` | 110 | UnwindData |  |
| 111 | `sqlite3_get_table` | `0x95670` | 458 | UnwindData |  |
| 113 | `sqlite3_hard_heap_limit64` | `0x959A0` | 110 | UnwindData |  |
| 115 | `sqlite3_interrupt` | `0x95A20` | 73 | UnwindData |  |
| 116 | `sqlite3_is_interrupted` | `0x95A70` | 77 | UnwindData |  |
| 117 | `sqlite3_keyword_check` | `0x95AD0` | 25 | UnwindData |  |
| 118 | `sqlite3_keyword_count` | `0x95AF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `sqlite3_keyword_name` | `0x95B00` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `sqlite3_libversion` | `0x95B50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `sqlite3_libversion_number` | `0x95B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `sqlite3_limit` | `0x95B70` | 131 | UnwindData |  |
| 124 | `sqlite3_load_extension` | `0x95C00` | 103 | UnwindData |  |
| 129 | `sqlite3_memory_highwater` | `0x95C70` | 41 | UnwindData |  |
| 130 | `sqlite3_memory_used` | `0x95CA0` | 41 | UnwindData |  |
| 137 | `sqlite3_mutex_try` | `0x95CD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `sqlite3_next_stmt` | `0x95CF0` | 97 | UnwindData |  |
| 139 | `sqlite3_open` | `0x95D60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `sqlite3_open16` | `0x95D80` | 220 | UnwindData |  |
| 146 | `sqlite3_prepare16` | `0x95E70` | 33 | UnwindData |  |
| 147 | `sqlite3_prepare16_v2` | `0x95EA0` | 36 | UnwindData |  |
| 148 | `sqlite3_prepare16_v3` | `0x95ED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `sqlite3_prepare_v3` | `0x95EF0` | 50 | UnwindData |  |
| 151 | `sqlite3_profile` | `0x95F30` | 146 | UnwindData |  |
| 152 | `sqlite3_progress_handler` | `0x95FD0` | 152 | UnwindData |  |
| 154 | `sqlite3_realloc` | `0x96070` | 60 | UnwindData |  |
| 160 | `sqlite3_result_blob64` | `0x960C0` | 63 | UnwindData |  |
| 161 | `sqlite3_result_double` | `0x96110` | 23 | UnwindData |  |
| 162 | `sqlite3_result_error` | `0x96130` | 42 | UnwindData |  |
| 163 | `sqlite3_result_error16` | `0x96160` | 42 | UnwindData |  |
| 164 | `sqlite3_result_error_code` | `0x96190` | 72 | UnwindData |  |
| 165 | `sqlite3_result_error_nomem` | `0x961E0` | 47 | UnwindData |  |
| 169 | `sqlite3_result_null` | `0x96220` | 23 | UnwindData |  |
| 170 | `sqlite3_result_pointer` | `0x96240` | 106 | UnwindData |  |
| 171 | `sqlite3_result_subtype` | `0x962B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 173 | `sqlite3_result_text16` | `0x962D0` | 27 | UnwindData |  |
| 175 | `sqlite3_result_text16le` | `0x962D0` | 27 | UnwindData |  |
| 174 | `sqlite3_result_text16be` | `0x96300` | 27 | UnwindData |  |
| 178 | `sqlite3_result_zeroblob` | `0x96330` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `sqlite3_result_zeroblob64` | `0x96350` | 88 | UnwindData |  |
| 180 | `sqlite3_rollback_hook` | `0x963B0` | 126 | UnwindData |  |
| 181 | `sqlite3_serialize` | `0x96440` | 639 | UnwindData |  |
| 182 | `sqlite3_set_authorizer` | `0x966D0` | 124 | UnwindData |  |
| 183 | `sqlite3_set_auxdata` | `0x96760` | 230 | UnwindData |  |
| 184 | `sqlite3_set_clientdata` | `0x96850` | 310 | UnwindData |  |
| 185 | `sqlite3_set_last_insert_rowid` | `0x96990` | 81 | UnwindData |  |
| 187 | `sqlite3_sleep` | `0x969F0` | 70 | UnwindData |  |
| 189 | `sqlite3_soft_heap_limit` | `0x96A40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `sqlite3_soft_heap_limit64` | `0x96A60` | 181 | UnwindData |  |
| 196 | `sqlite3_stmt_busy` | `0x96B20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 197 | `sqlite3_stmt_explain` | `0x96B40` | 310 | UnwindData |  |
| 198 | `sqlite3_stmt_isexplain` | `0x96C80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 199 | `sqlite3_stmt_readonly` | `0x96CA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 200 | `sqlite3_stmt_status` | `0x96CC0` | 179 | UnwindData |  |
| 203 | `sqlite3_str_appendchar` | `0x96D80` | 83 | UnwindData |  |
| 205 | `sqlite3_str_errcode` | `0x96DE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | `sqlite3_str_finish` | `0x96E00` | 63 | UnwindData |  |
| 207 | `sqlite3_str_length` | `0x96E50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 208 | `sqlite3_str_new` | `0x96E70` | 80 | UnwindData |  |
| 210 | `sqlite3_str_value` | `0x96ED0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 212 | `sqlite3_strglob` | `0x96F00` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 216 | `sqlite3_system_errno` | `0x96F40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 217 | `sqlite3_table_column_metadata` | `0x96F60` | 765 | UnwindData |  |
| 218 | `sqlite3_test_control` | `0x97270` | 1,030 | UnwindData |  |
| 220 | `sqlite3_threadsafe` | `0x97680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `sqlite3_total_changes64` | `0x97690` | 56 | UnwindData |  |
| 223 | `sqlite3_trace` | `0x976D0` | 140 | UnwindData |  |
| 224 | `sqlite3_trace_v2` | `0x97770` | 142 | UnwindData |  |
| 225 | `sqlite3_transfer_bindings` | `0x97810` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 226 | `sqlite3_txn_state` | `0x97870` | 194 | UnwindData |  |
| 227 | `sqlite3_update_hook` | `0x97940` | 126 | UnwindData |  |
| 229 | `sqlite3_uri_int64` | `0x979D0` | 56 | UnwindData |  |
| 230 | `sqlite3_uri_key` | `0x97A10` | 104 | UnwindData |  |
| 232 | `sqlite3_user_data` | `0x97A80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 235 | `sqlite3_value_bytes16` | `0x97AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 236 | `sqlite3_value_double` | `0x97AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 237 | `sqlite3_value_dup` | `0x97AC0` | 180 | UnwindData |  |
| 238 | `sqlite3_value_encoding` | `0x97B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 239 | `sqlite3_value_free` | `0x97B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 240 | `sqlite3_value_frombind` | `0x97BA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 243 | `sqlite3_value_nochange` | `0x97BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 244 | `sqlite3_value_numeric_type` | `0x97BE0` | 66 | UnwindData |  |
| 245 | `sqlite3_value_pointer` | `0x97C30` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 246 | `sqlite3_value_subtype` | `0x97C90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 249 | `sqlite3_value_text16be` | `0x97CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 257 | `sqlite3_vtab_collation` | `0x97CC0` | 92 | UnwindData |  |
| 258 | `sqlite3_vtab_config` | `0x97D30` | 210 | UnwindData |  |
| 259 | `sqlite3_vtab_distinct` | `0x97E10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 260 | `sqlite3_vtab_in` | `0x97E20` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 261 | `sqlite3_vtab_in_first` | `0x97E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 262 | `sqlite3_vtab_in_next` | `0x97E70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 263 | `sqlite3_vtab_nochange` | `0x97E90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 264 | `sqlite3_vtab_on_conflict` | `0x97EC0` | 66 | UnwindData |  |
| 265 | `sqlite3_vtab_rhs_value` | `0x97F10` | 154 | UnwindData |  |
| 270 | `sqlite3_win32_mbcs_to_utf8` | `0x97FB0` | 79 | UnwindData |  |
| 271 | `sqlite3_win32_mbcs_to_utf8_v2` | `0x98010` | 75 | UnwindData |  |
| 272 | `sqlite3_win32_set_directory` | `0x98070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 273 | `sqlite3_win32_set_directory16` | `0x98080` | 79 | UnwindData |  |
| 274 | `sqlite3_win32_set_directory8` | `0x980E0` | 178 | UnwindData |  |
| 276 | `sqlite3_win32_unicode_to_utf8` | `0x981A0` | 65 | UnwindData |  |
| 277 | `sqlite3_win32_utf8_to_mbcs` | `0x981F0` | 79 | UnwindData |  |
| 278 | `sqlite3_win32_utf8_to_mbcs_v2` | `0x98250` | 75 | UnwindData |  |
| 279 | `sqlite3_win32_utf8_to_unicode` | `0x982B0` | 65 | UnwindData |  |
| 280 | `sqlite3_win32_write_debug` | `0x98300` | 176 | UnwindData |  |
