# Binary Specification: winsqlite3.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\winsqlite3.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2dbf56faf6abfe4e0b16d75e9392daa8a7139e4c228f4a131d842938e54bf13f`
* **Total Exported Functions:** 292

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 147 | `sqlite3_open16` | `0x1E00` | 221 | UnwindData |  |
| 143 | `sqlite3_mutex_leave` | `0xD240` | 3,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `sqlite3_mutex_enter` | `0xDF20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `sqlite3_exec` | `0xDF40` | 944 | UnwindData |  |
| 59 | `sqlite3_column_text` | `0xE300` | 190 | UnwindData |  |
| 164 | `sqlite3_reset` | `0xE400` | 190 | UnwindData |  |
| 111 | `sqlite3_finalize` | `0xE960` | 182 | UnwindData |  |
| 60 | `sqlite3_column_text16` | `0xECB0` | 190 | UnwindData |  |
| 51 | `sqlite3_column_int` | `0xEE10` | 134 | UnwindData |  |
| 42 | `sqlite3_column_blob` | `0xF3F0` | 135 | UnwindData |  |
| 243 | `sqlite3_value_blob` | `0xF480` | 122 | UnwindData |  |
| 43 | `sqlite3_column_bytes` | `0xF500` | 191 | UnwindData |  |
| 52 | `sqlite3_column_int64` | `0xF5D0` | 185 | UnwindData |  |
| 132 | `sqlite3_log` | `0x10CE0` | 47 | UnwindData |  |
| 112 | `sqlite3_free` | `0x11E80` | 133 | UnwindData |  |
| 29 | `sqlite3_blob_read` | `0x16A00` | 27 | UnwindData |  |
| 6 | `sqlite3_backup_init` | `0x16CB0` | 353 | UnwindData |  |
| 26 | `sqlite3_blob_bytes` | `0x16E20` | 704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `sqlite3_blob_reopen` | `0x170E0` | 201 | UnwindData |  |
| 278 | `sqlite3_wal_checkpoint` | `0x173C0` | 27 | UnwindData |  |
| 70 | `sqlite3_create_collation` | `0x174B0` | 31 | UnwindData |  |
| 72 | `sqlite3_create_collation_v2` | `0x174E0` | 183 | UnwindData |  |
| 279 | `sqlite3_wal_checkpoint_v2` | `0x17680` | 320 | UnwindData |  |
| 21 | `sqlite3_bind_text16` | `0x182B0` | 246 | UnwindData |  |
| 193 | `sqlite3_set_last_insert_rowid` | `0x186E0` | 83 | UnwindData |  |
| 27 | `sqlite3_blob_close` | `0x1A490` | 89 | UnwindData |  |
| 138 | `sqlite3_mprintf` | `0x1C160` | 57 | UnwindData |  |
| 266 | `sqlite3_vmprintf` | `0x1C1A0` | 243 | UnwindData |  |
| 160 | `sqlite3_randomness` | `0x1C2E0` | 408 | UnwindData |  |
| 162 | `sqlite3_realloc64` | `0x1C510` | 52 | UnwindData |  |
| 134 | `sqlite3_malloc64` | `0x1C5F0` | 40 | UnwindData |  |
| 133 | `sqlite3_malloc` | `0x1C7A0` | 49 | UnwindData |  |
| 121 | `sqlite3_initialize` | `0x1C7E0` | 522 | UnwindData |  |
| 151 | `sqlite3_overload_function` | `0x1CBA0` | 281 | UnwindData |  |
| 127 | `sqlite3_last_insert_rowid` | `0x1CCC0` | 75 | UnwindData |  |
| 74 | `sqlite3_create_function` | `0x1CD80` | 80 | UnwindData |  |
| 154 | `sqlite3_prepare16_v2` | `0x1D040` | 36 | UnwindData |  |
| 76 | `sqlite3_create_function_v2` | `0x1D250` | 380 | UnwindData |  |
| 116 | `sqlite3_get_autocommit` | `0x1D570` | 55 | UnwindData |  |
| 156 | `sqlite3_prepare_v2` | `0x1D5B0` | 42 | UnwindData |  |
| 210 | `sqlite3_str_appendall` | `0x26330` | 70 | UnwindData |  |
| 217 | `sqlite3_str_reset` | `0x28CE0` | 61 | UnwindData |  |
| 221 | `sqlite3_stricmp` | `0x29190` | 2,128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `sqlite3_db_filename` | `0x299E0` | 112 | UnwindData |  |
| 107 | `sqlite3_file_control` | `0x29A60` | 386 | UnwindData |  |
| 209 | `sqlite3_str_append` | `0x2AAC0` | 59 | UnwindData |  |
| 14 | `sqlite3_bind_int64` | `0x2AC90` | 540 | UnwindData |  |
| 61 | `sqlite3_column_type` | `0x2AEC0` | 58 | UnwindData |  |
| 10 | `sqlite3_bind_blob` | `0x2C360` | 64 | UnwindData |  |
| 15 | `sqlite3_bind_null` | `0x2C3B0` | 52 | UnwindData |  |
| 50 | `sqlite3_column_double` | `0x2C880` | 53 | UnwindData |  |
| 1 | `sqlite3_aggregate_context` | `0x2CB00` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `sqlite3_result_text` | `0x2CCF0` | 23 | UnwindData |  |
| 184 | `sqlite3_result_value` | `0x2CE10` | 112 | UnwindData |  |
| 23 | `sqlite3_bind_value` | `0x2D310` | 180 | UnwindData |  |
| 223 | `sqlite3_strnicmp` | `0x34F30` | 9,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `sqlite3_mutex_free` | `0x372D0` | 27 | UnwindData |  |
| 287 | `sqlite3_win32_sleep` | `0x37630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 277 | `sqlite3_wal_autocheckpoint` | `0x37650` | 93 | UnwindData |  |
| 280 | `sqlite3_wal_hook` | `0x376C0` | 128 | UnwindData |  |
| 238 | `sqlite3_uri_boolean` | `0x380C0` | 48 | UnwindData |  |
| 241 | `sqlite3_uri_parameter` | `0x38100` | 45 | UnwindData |  |
| 263 | `sqlite3_vfs_find` | `0x38CB0` | 141 | UnwindData |  |
| 113 | `sqlite3_free_filename` | `0x392F0` | 29 | UnwindData |  |
| 97 | `sqlite3_errcode` | `0x39320` | 97 | UnwindData |  |
| 98 | `sqlite3_errmsg` | `0x39390` | 258 | UnwindData |  |
| 196 | `sqlite3_snprintf` | `0x39C00` | 132 | UnwindData |  |
| 78 | `sqlite3_create_module_v2` | `0x3A7F0` | 143 | UnwindData |  |
| 77 | `sqlite3_create_module` | `0x3A890` | 115 | UnwindData |  |
| 219 | `sqlite3_str_vappendf` | `0x3E970` | 123 | UnwindData |  |
| 203 | `sqlite3_step` | `0x426B0` | 365 | UnwindData |  |
| 91 | `sqlite3_db_status` | `0x4E860` | 1,123 | UnwindData |  |
| 139 | `sqlite3_msize` | `0x4ED90` | 33 | UnwindData |  |
| 92 | `sqlite3_declare_vtab` | `0x4F1A0` | 594 | UnwindData |  |
| 145 | `sqlite3_next_stmt` | `0x52D70` | 167 | UnwindData |  |
| 17 | `sqlite3_bind_parameter_index` | `0x54880` | 48 | UnwindData |  |
| 244 | `sqlite3_value_bytes` | `0x58860` | 72 | UnwindData |  |
| 204 | `sqlite3_stmt_busy` | `0x59220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 261 | `sqlite3_value_type` | `0x59240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `sqlite3_clear_bindings` | `0x59260` | 189 | UnwindData |  |
| 257 | `sqlite3_value_text` | `0x59750` | 68 | UnwindData |  |
| 200 | `sqlite3_sql` | `0x59A30` | 19,936 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 174 | `sqlite3_result_int` | `0x5E810` | 2,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `sqlite3_db_handle` | `0x5EFE0` | 880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 175 | `sqlite3_result_int64` | `0x5F350` | 1,472 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 258 | `sqlite3_value_text16` | `0x5F910` | 68 | UnwindData |  |
| 260 | `sqlite3_value_text16le` | `0x5F910` | 68 | UnwindData |  |
| 144 | `sqlite3_mutex_try` | `0x5FAB0` | 6,880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `sqlite3_bind_text` | `0x61590` | 33 | UnwindData |  |
| 254 | `sqlite3_value_numeric_type` | `0x62C40` | 68 | UnwindData |  |
| 251 | `sqlite3_value_int` | `0x62DC0` | 3,904 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 252 | `sqlite3_value_int64` | `0x62DC0` | 3,904 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `sqlite3_global_recover` | `0x63D00` | 2,384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `sqlite3_memory_alarm` | `0x63D00` | 2,384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 163 | `sqlite3_release_memory` | `0x63D00` | 2,384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 267 | `sqlite3_vsnprintf` | `0x64650` | 130 | UnwindData |  |
| 69 | `sqlite3_context_db_handle` | `0x664E0` | 1,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `sqlite3_changes64` | `0x66A10` | 55 | UnwindData |  |
| 13 | `sqlite3_bind_int` | `0x66FE0` | 3,856 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 242 | `sqlite3_user_data` | `0x67EF0` | 1,392 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `sqlite3_os_init` | `0x68460` | 443 | UnwindData |  |
| 264 | `sqlite3_vfs_register` | `0x68630` | 177 | UnwindData |  |
| 53 | `sqlite3_column_name` | `0x68740` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `sqlite3_bind_parameter_count` | `0x687D0` | 2,368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 212 | `sqlite3_str_appendf` | `0x69110` | 34 | UnwindData |  |
| 12 | `sqlite3_bind_double` | `0x69F40` | 100 | UnwindData |  |
| 207 | `sqlite3_stmt_readonly` | `0x6A2B0` | 704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `sqlite3_data_count` | `0x6A570` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `sqlite3_column_value` | `0x6A5A0` | 77 | UnwindData |  |
| 176 | `sqlite3_result_null` | `0x6A7B0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 187 | `sqlite3_rollback_hook` | `0x6A8F0` | 128 | UnwindData |  |
| 84 | `sqlite3_db_config` | `0x6AFA0` | 233 | UnwindData |  |
| 33 | `sqlite3_busy_timeout` | `0x6B500` | 126 | UnwindData |  |
| 32 | `sqlite3_busy_handler` | `0x6B590` | 146 | UnwindData |  |
| 140 | `sqlite3_mutex_alloc` | `0x6B690` | 57 | UnwindData |  |
| 246 | `sqlite3_value_double` | `0x6B710` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 285 | `sqlite3_win32_set_directory16` | `0x6B8E0` | 79 | UnwindData |  |
| 286 | `sqlite3_win32_set_directory8` | `0x6B940` | 178 | UnwindData |  |
| 288 | `sqlite3_win32_unicode_to_utf8` | `0x6BA00` | 65 | UnwindData |  |
| 106 | `sqlite3_extended_result_codes` | `0x6BA50` | 121 | UnwindData |  |
| 68 | `sqlite3_config` | `0x6D2E0` | 987 | UnwindData |  |
| 48 | `sqlite3_column_decltype` | `0x6D9A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `sqlite3_close_v2` | `0x6D9C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `sqlite3_backup_finish` | `0x6D9D0` | 229 | UnwindData |  |
| 275 | `sqlite3_vtab_on_conflict` | `0x6DAF0` | 89 | UnwindData |  |
| 35 | `sqlite3_changes` | `0x6DCD0` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 228 | `sqlite3_thread_cleanup` | `0x6DEB0` | 5,616 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 148 | `sqlite3_open_v2` | `0x6F4A0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `sqlite3_close` | `0x6F560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `sqlite3_open` | `0x6F570` | 8,816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 211 | `sqlite3_str_appendchar` | `0x717E0` | 83 | UnwindData |  |
| 9 | `sqlite3_backup_step` | `0x80E00` | 1,242 | UnwindData |  |
| 22 | `sqlite3_bind_text64` | `0x812E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `sqlite3_column_count` | `0x81320` | 8,272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 173 | `sqlite3_result_error_toobig` | `0x83370` | 109 | UnwindData |  |
| 284 | `sqlite3_win32_set_directory` | `0x83520` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 171 | `sqlite3_result_error_code` | `0x83810` | 67 | UnwindData |  |
| 152 | `sqlite3_prepare` | `0x83B20` | 39 | UnwindData |  |
| 169 | `sqlite3_result_error` | `0x83B80` | 37 | UnwindData |  |
| 222 | `sqlite3_strlike` | `0x83BB0` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 229 | `sqlite3_threadsafe` | `0x83D30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 281 | `sqlite3_win32_is_nt` | `0x83D30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 199 | `sqlite3_sourceid` | `0x83D40` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `sqlite3_prepare_v3` | `0x83DA0` | 50 | UnwindData |  |
| 2 | `sqlite3_aggregate_count` | `0xC8440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `sqlite3_auto_extension` | `0xC8450` | 163 | UnwindData |  |
| 4 | `sqlite3_autovacuum_pages` | `0xC8500` | 178 | UnwindData |  |
| 7 | `sqlite3_backup_pagecount` | `0xC85C0` | 44 | UnwindData |  |
| 8 | `sqlite3_backup_remaining` | `0xC8600` | 44 | UnwindData |  |
| 11 | `sqlite3_bind_blob64` | `0xC8640` | 30 | UnwindData |  |
| 18 | `sqlite3_bind_parameter_name` | `0xC8670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `sqlite3_bind_pointer` | `0xC8690` | 142 | UnwindData |  |
| 24 | `sqlite3_bind_zeroblob` | `0xC8730` | 99 | UnwindData |  |
| 25 | `sqlite3_bind_zeroblob64` | `0xC87A0` | 113 | UnwindData |  |
| 28 | `sqlite3_blob_open` | `0xC8820` | 1,291 | UnwindData |  |
| 31 | `sqlite3_blob_write` | `0xC8D40` | 27 | UnwindData |  |
| 34 | `sqlite3_cancel_auto_extension` | `0xC8D70` | 134 | UnwindData |  |
| 40 | `sqlite3_collation_needed` | `0xC8E00` | 114 | UnwindData |  |
| 41 | `sqlite3_collation_needed16` | `0xC8E80` | 114 | UnwindData |  |
| 44 | `sqlite3_column_bytes16` | `0xC8F00` | 52 | UnwindData |  |
| 46 | `sqlite3_column_database_name` | `0xC8F40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `sqlite3_column_database_name16` | `0xC8F60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `sqlite3_column_decltype16` | `0xC8F80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `sqlite3_column_name16` | `0xC8FA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `sqlite3_column_origin_name` | `0xC8FC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `sqlite3_column_origin_name16` | `0xC8FE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `sqlite3_column_table_name` | `0xC9000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `sqlite3_column_table_name16` | `0xC9020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `sqlite3_commit_hook` | `0xC9040` | 126 | UnwindData |  |
| 64 | `sqlite3_compileoption_get` | `0xC90D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `sqlite3_compileoption_used` | `0xC90F0` | 192 | UnwindData |  |
| 66 | `sqlite3_complete` | `0xC91C0` | 694 | UnwindData |  |
| 67 | `sqlite3_complete16` | `0xC9480` | 107 | UnwindData |  |
| 71 | `sqlite3_create_collation16` | `0xC9500` | 205 | UnwindData |  |
| 73 | `sqlite3_create_filename` | `0xC95E0` | 354 | UnwindData |  |
| 75 | `sqlite3_create_function16` | `0xC9750` | 261 | UnwindData |  |
| 79 | `sqlite3_create_window_function` | `0xC9860` | 95 | UnwindData |  |
| 82 | `sqlite3_database_file_object` | `0xC98D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `sqlite3_db_cacheflush` | `0xC9900` | 274 | UnwindData |  |
| 87 | `sqlite3_db_mutex` | `0xC9A20` | 53 | UnwindData |  |
| 88 | `sqlite3_db_name` | `0xC9A60` | 85 | UnwindData |  |
| 89 | `sqlite3_db_readonly` | `0xC9AC0` | 89 | UnwindData |  |
| 90 | `sqlite3_db_release_memory` | `0xC9B20` | 166 | UnwindData |  |
| 93 | `sqlite3_deserialize` | `0xC9BD0` | 453 | UnwindData |  |
| 94 | `sqlite3_drop_modules` | `0xC9DA0` | 179 | UnwindData |  |
| 95 | `sqlite3_enable_load_extension` | `0xC9E60` | 77 | UnwindData |  |
| 96 | `sqlite3_enable_shared_cache` | `0xC9EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `sqlite3_errmsg16` | `0xC9ED0` | 162 | UnwindData |  |
| 100 | `sqlite3_error_offset` | `0xC9F80` | 71 | UnwindData |  |
| 101 | `sqlite3_errstr` | `0xC9FD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `sqlite3_expanded_sql` | `0xC9FE0` | 91 | UnwindData |  |
| 104 | `sqlite3_expired` | `0xCA050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `sqlite3_extended_errcode` | `0xCA070` | 71 | UnwindData |  |
| 108 | `sqlite3_filename_database` | `0xCA0C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `sqlite3_filename_journal` | `0xCA0E0` | 81 | UnwindData |  |
| 110 | `sqlite3_filename_wal` | `0xCA140` | 42 | UnwindData |  |
| 114 | `sqlite3_free_table` | `0xCA170` | 87 | UnwindData |  |
| 117 | `sqlite3_get_auxdata` | `0xCA1D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `sqlite3_get_table` | `0xCA210` | 458 | UnwindData |  |
| 120 | `sqlite3_hard_heap_limit64` | `0xCA540` | 110 | UnwindData |  |
| 122 | `sqlite3_interrupt` | `0xCA5C0` | 73 | UnwindData |  |
| 123 | `sqlite3_is_interrupted` | `0xCA610` | 77 | UnwindData |  |
| 124 | `sqlite3_keyword_check` | `0xCA670` | 25 | UnwindData |  |
| 125 | `sqlite3_keyword_count` | `0xCA690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `sqlite3_keyword_name` | `0xCA6A0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `sqlite3_libversion` | `0xCA6F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `sqlite3_libversion_number` | `0xCA700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | `sqlite3_limit` | `0xCA710` | 131 | UnwindData |  |
| 131 | `sqlite3_load_extension` | `0xCA7A0` | 103 | UnwindData |  |
| 136 | `sqlite3_memory_highwater` | `0xCA810` | 41 | UnwindData |  |
| 137 | `sqlite3_memory_used` | `0xCA840` | 41 | UnwindData |  |
| 149 | `sqlite3_os_end` | `0xCA870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `sqlite3_prepare16` | `0xCA890` | 33 | UnwindData |  |
| 155 | `sqlite3_prepare16_v3` | `0xCA8C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 158 | `sqlite3_profile` | `0xCA8E0` | 146 | UnwindData |  |
| 159 | `sqlite3_progress_handler` | `0xCA980` | 152 | UnwindData |  |
| 161 | `sqlite3_realloc` | `0xCAA20` | 60 | UnwindData |  |
| 165 | `sqlite3_reset_auto_extension` | `0xCAA70` | 76 | UnwindData |  |
| 166 | `sqlite3_result_blob` | `0xCAAD0` | 23 | UnwindData |  |
| 167 | `sqlite3_result_blob64` | `0xCAAF0` | 53 | UnwindData |  |
| 168 | `sqlite3_result_double` | `0xCAB30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 170 | `sqlite3_result_error16` | `0xCAB40` | 37 | UnwindData |  |
| 172 | `sqlite3_result_error_nomem` | `0xCAB70` | 41 | UnwindData |  |
| 177 | `sqlite3_result_pointer` | `0xCABA0` | 83 | UnwindData |  |
| 178 | `sqlite3_result_subtype` | `0xCAC00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 180 | `sqlite3_result_text16` | `0xCAC20` | 27 | UnwindData |  |
| 182 | `sqlite3_result_text16le` | `0xCAC20` | 27 | UnwindData |  |
| 181 | `sqlite3_result_text16be` | `0xCAC50` | 27 | UnwindData |  |
| 183 | `sqlite3_result_text64` | `0xCAC80` | 107 | UnwindData |  |
| 185 | `sqlite3_result_zeroblob` | `0xCAD00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `sqlite3_result_zeroblob64` | `0xCAD20` | 79 | UnwindData |  |
| 188 | `sqlite3_rtree_geometry_callback` | `0xCAD80` | 162 | UnwindData |  |
| 189 | `sqlite3_rtree_query_callback` | `0xCAE30` | 196 | UnwindData |  |
| 190 | `sqlite3_serialize` | `0xCAF00` | 545 | UnwindData |  |
| 191 | `sqlite3_set_authorizer` | `0xCB130` | 124 | UnwindData |  |
| 192 | `sqlite3_set_auxdata` | `0xCB1C0` | 219 | UnwindData |  |
| 194 | `sqlite3_shutdown` | `0xCB2B0` | 187 | UnwindData |  |
| 195 | `sqlite3_sleep` | `0xCB380` | 70 | UnwindData |  |
| 197 | `sqlite3_soft_heap_limit` | `0xCB3D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 198 | `sqlite3_soft_heap_limit64` | `0xCB3F0` | 181 | UnwindData |  |
| 201 | `sqlite3_status` | `0xCB4B0` | 103 | UnwindData |  |
| 202 | `sqlite3_status64` | `0xCB520` | 192 | UnwindData |  |
| 205 | `sqlite3_stmt_explain` | `0xCB5F0` | 292 | UnwindData |  |
| 206 | `sqlite3_stmt_isexplain` | `0xCB720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 208 | `sqlite3_stmt_status` | `0xCB740` | 179 | UnwindData |  |
| 213 | `sqlite3_str_errcode` | `0xCB800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 214 | `sqlite3_str_finish` | `0xCB820` | 63 | UnwindData |  |
| 215 | `sqlite3_str_length` | `0xCB870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 216 | `sqlite3_str_new` | `0xCB890` | 80 | UnwindData |  |
| 218 | `sqlite3_str_value` | `0xCB8F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 220 | `sqlite3_strglob` | `0xCB920` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 224 | `sqlite3_system_errno` | `0xCB960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 225 | `sqlite3_table_column_metadata` | `0xCB980` | 701 | UnwindData |  |
| 227 | `sqlite3_test_control` | `0xCBC50` | 998 | UnwindData |  |
| 230 | `sqlite3_total_changes` | `0xCC040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 231 | `sqlite3_total_changes64` | `0xCC050` | 56 | UnwindData |  |
| 232 | `sqlite3_trace` | `0xCC090` | 140 | UnwindData |  |
| 233 | `sqlite3_trace_v2` | `0xCC130` | 142 | UnwindData |  |
| 234 | `sqlite3_transfer_bindings` | `0xCC1D0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 235 | `sqlite3_txn_state` | `0xCC230` | 194 | UnwindData |  |
| 237 | `sqlite3_update_hook` | `0xCC300` | 126 | UnwindData |  |
| 239 | `sqlite3_uri_int64` | `0xCC390` | 56 | UnwindData |  |
| 240 | `sqlite3_uri_key` | `0xCC3D0` | 104 | UnwindData |  |
| 245 | `sqlite3_value_bytes16` | `0xCC440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 247 | `sqlite3_value_dup` | `0xCC450` | 180 | UnwindData |  |
| 248 | `sqlite3_value_encoding` | `0xCC510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 249 | `sqlite3_value_free` | `0xCC520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 250 | `sqlite3_value_frombind` | `0xCC530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 253 | `sqlite3_value_nochange` | `0xCC550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 255 | `sqlite3_value_pointer` | `0xCC570` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 256 | `sqlite3_value_subtype` | `0xCC5D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 259 | `sqlite3_value_text16be` | `0xCC5F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 265 | `sqlite3_vfs_unregister` | `0xCC600` | 71 | UnwindData |  |
| 268 | `sqlite3_vtab_collation` | `0xCC650` | 96 | UnwindData |  |
| 269 | `sqlite3_vtab_config` | `0xCC6C0` | 210 | UnwindData |  |
| 270 | `sqlite3_vtab_distinct` | `0xCC7A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 271 | `sqlite3_vtab_in` | `0xCC7B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 272 | `sqlite3_vtab_in_first` | `0xCC7F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 273 | `sqlite3_vtab_in_next` | `0xCC800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 274 | `sqlite3_vtab_nochange` | `0xCC820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 276 | `sqlite3_vtab_rhs_value` | `0xCC840` | 143 | UnwindData |  |
| 282 | `sqlite3_win32_mbcs_to_utf8` | `0xCC8E0` | 79 | UnwindData |  |
| 283 | `sqlite3_win32_mbcs_to_utf8_v2` | `0xCC940` | 75 | UnwindData |  |
| 289 | `sqlite3_win32_utf8_to_mbcs` | `0xCC9A0` | 79 | UnwindData |  |
| 290 | `sqlite3_win32_utf8_to_mbcs_v2` | `0xCCA00` | 75 | UnwindData |  |
| 291 | `sqlite3_win32_utf8_to_unicode` | `0xCCA60` | 65 | UnwindData |  |
| 292 | `sqlite3_win32_write_debug` | `0xCCAB0` | 176 | UnwindData |  |
| 262 | `sqlite3_version` | `0xE8164` | 67,584 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `sqlite3_fts3_may_be_corrupt` | `0xF8964` | 1,548 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `sqlite3_data_directory` | `0xF8F70` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 226 | `sqlite3_temp_directory` | `0xF8F78` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 236 | `sqlite3_unsupported_selecttrace` | `0xF90C8` | 0 | Indeterminate |  |
