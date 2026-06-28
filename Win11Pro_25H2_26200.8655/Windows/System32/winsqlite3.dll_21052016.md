# Binary Specification: winsqlite3.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\winsqlite3.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `21052016067029f33a10f441e9f7d612368a8efcd548bf2e82092e3aa3c49b3c`
* **Total Exported Functions:** 297

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 108 | `sqlite3_file_control` | `0x42A0` | 386 | UnwindData |  |
| 222 | `sqlite3_str_reset` | `0xA740` | 61 | UnwindData |  |
| 17 | `sqlite3_bind_parameter_index` | `0xAA90` | 48 | UnwindData |  |
| 215 | `sqlite3_str_appendall` | `0xAD10` | 70 | UnwindData |  |
| 224 | `sqlite3_str_vappendf` | `0xEF20` | 123 | UnwindData |  |
| 271 | `sqlite3_vmprintf` | `0x10E60` | 243 | UnwindData |  |
| 140 | `sqlite3_mprintf` | `0x10F60` | 57 | UnwindData |  |
| 153 | `sqlite3_overload_function` | `0x11050` | 281 | UnwindData |  |
| 226 | `sqlite3_stricmp` | `0x11740` | 3,008 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 205 | `sqlite3_sql` | `0x12300` | 3,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `sqlite3_column_type` | `0x12EE0` | 58 | UnwindData |  |
| 59 | `sqlite3_column_text` | `0x14890` | 190 | UnwindData |  |
| 166 | `sqlite3_reset` | `0x14990` | 190 | UnwindData |  |
| 112 | `sqlite3_finalize` | `0x14EF0` | 182 | UnwindData |  |
| 60 | `sqlite3_column_text16` | `0x15210` | 190 | UnwindData |  |
| 51 | `sqlite3_column_int` | `0x153B0` | 134 | UnwindData |  |
| 42 | `sqlite3_column_blob` | `0x15BF0` | 135 | UnwindData |  |
| 248 | `sqlite3_value_blob` | `0x15C80` | 122 | UnwindData |  |
| 43 | `sqlite3_column_bytes` | `0x15D00` | 191 | UnwindData |  |
| 52 | `sqlite3_column_int64` | `0x15DD0` | 185 | UnwindData |  |
| 134 | `sqlite3_log` | `0x16770` | 47 | UnwindData |  |
| 135 | `sqlite3_malloc` | `0x16CD0` | 49 | UnwindData |  |
| 123 | `sqlite3_initialize` | `0x16D10` | 472 | UnwindData |  |
| 113 | `sqlite3_free` | `0x188F0` | 133 | UnwindData |  |
| 145 | `sqlite3_mutex_leave` | `0x1C610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `sqlite3_exec` | `0x1C630` | 986 | UnwindData |  |
| 143 | `sqlite3_mutex_enter` | `0x1CBB0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `sqlite3_get_autocommit` | `0x1CC80` | 55 | UnwindData |  |
| 158 | `sqlite3_prepare_v2` | `0x1CCC0` | 42 | UnwindData |  |
| 208 | `sqlite3_step` | `0x1D410` | 365 | UnwindData |  |
| 228 | `sqlite3_strnicmp` | `0x24FD0` | 34,352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | `sqlite3_snprintf` | `0x2D600` | 132 | UnwindData |  |
| 162 | `sqlite3_randomness` | `0x2D690` | 408 | UnwindData |  |
| 268 | `sqlite3_vfs_find` | `0x2DBB0` | 141 | UnwindData |  |
| 247 | `sqlite3_user_data` | `0x2E050` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `sqlite3_result_value` | `0x2E180` | 85 | UnwindData |  |
| 69 | `sqlite3_context_db_handle` | `0x2E5B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 214 | `sqlite3_str_append` | `0x2E5D0` | 59 | UnwindData |  |
| 176 | `sqlite3_result_int` | `0x2ECD0` | 26 | UnwindData |  |
| 136 | `sqlite3_malloc64` | `0x31330` | 40 | UnwindData |  |
| 27 | `sqlite3_blob_close` | `0x313B0` | 89 | UnwindData |  |
| 164 | `sqlite3_realloc64` | `0x31500` | 52 | UnwindData |  |
| 15 | `sqlite3_bind_null` | `0x31B30` | 52 | UnwindData |  |
| 14 | `sqlite3_bind_int64` | `0x31B70` | 139 | UnwindData |  |
| 10 | `sqlite3_bind_blob` | `0x32260` | 64 | UnwindData |  |
| 20 | `sqlite3_bind_text` | `0x322B0` | 33 | UnwindData |  |
| 21 | `sqlite3_bind_text16` | `0x322E0` | 37 | UnwindData |  |
| 23 | `sqlite3_bind_value` | `0x33450` | 180 | UnwindData |  |
| 16 | `sqlite3_bind_parameter_count` | `0x33D10` | 1,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `sqlite3_last_insert_rowid` | `0x343B0` | 75 | UnwindData |  |
| 197 | `sqlite3_set_last_insert_rowid` | `0x34500` | 83 | UnwindData |  |
| 280 | `sqlite3_vtab_on_conflict` | `0x346F0` | 89 | UnwindData |  |
| 76 | `sqlite3_create_function_v2` | `0x36160` | 380 | UnwindData |  |
| 147 | `sqlite3_next_stmt` | `0x3C2A0` | 167 | UnwindData |  |
| 292 | `sqlite3_win32_sleep` | `0x3C840` | 16,656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 249 | `sqlite3_value_bytes` | `0x40950` | 72 | UnwindData |  |
| 98 | `sqlite3_errcode` | `0x45380` | 97 | UnwindData |  |
| 99 | `sqlite3_errmsg` | `0x453F0` | 258 | UnwindData |  |
| 209 | `sqlite3_stmt_busy` | `0x45610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 266 | `sqlite3_value_type` | `0x45630` | 800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 262 | `sqlite3_value_text` | `0x45950` | 68 | UnwindData |  |
| 1 | `sqlite3_aggregate_context` | `0x46EB0` | 10,240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `sqlite3_db_handle` | `0x496B0` | 2,768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 263 | `sqlite3_value_text16` | `0x4A180` | 68 | UnwindData |  |
| 265 | `sqlite3_value_text16le` | `0x4A180` | 68 | UnwindData |  |
| 146 | `sqlite3_mutex_try` | `0x4A320` | 2,656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `sqlite3_free_filename` | `0x4AD80` | 29 | UnwindData |  |
| 243 | `sqlite3_uri_boolean` | `0x4ADB0` | 48 | UnwindData |  |
| 246 | `sqlite3_uri_parameter` | `0x4ADF0` | 45 | UnwindData |  |
| 6 | `sqlite3_backup_init` | `0x4BAB0` | 353 | UnwindData |  |
| 29 | `sqlite3_blob_read` | `0x4BDC0` | 27 | UnwindData |  |
| 30 | `sqlite3_blob_reopen` | `0x4BF60` | 201 | UnwindData |  |
| 26 | `sqlite3_blob_bytes` | `0x4C1B0` | 4,352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `sqlite3_create_collation` | `0x4D2B0` | 31 | UnwindData |  |
| 72 | `sqlite3_create_collation_v2` | `0x4D2E0` | 183 | UnwindData |  |
| 156 | `sqlite3_prepare16_v2` | `0x4D570` | 36 | UnwindData |  |
| 74 | `sqlite3_create_function` | `0x4E8F0` | 80 | UnwindData |  |
| 259 | `sqlite3_value_numeric_type` | `0x4E9D0` | 68 | UnwindData |  |
| 149 | `sqlite3_open16` | `0x4EB10` | 221 | UnwindData |  |
| 256 | `sqlite3_value_int` | `0x4F180` | 1,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 257 | `sqlite3_value_int64` | `0x4F180` | 1,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `sqlite3_create_module` | `0x4F660` | 115 | UnwindData |  |
| 85 | `sqlite3_db_filename` | `0x4F800` | 112 | UnwindData |  |
| 78 | `sqlite3_create_module_v2` | `0x4FA50` | 143 | UnwindData |  |
| 121 | `sqlite3_global_recover` | `0x50130` | 2,272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `sqlite3_memory_alarm` | `0x50130` | 2,272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 165 | `sqlite3_release_memory` | `0x50130` | 2,272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 283 | `sqlite3_wal_checkpoint` | `0x50A10` | 27 | UnwindData |  |
| 284 | `sqlite3_wal_checkpoint_v2` | `0x50A90` | 288 | UnwindData |  |
| 272 | `sqlite3_vsnprintf` | `0x50BC0` | 130 | UnwindData |  |
| 50 | `sqlite3_column_double` | `0x50E50` | 53 | UnwindData |  |
| 36 | `sqlite3_changes64` | `0x52220` | 55 | UnwindData |  |
| 13 | `sqlite3_bind_int` | `0x522E0` | 1,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 282 | `sqlite3_wal_autocheckpoint` | `0x52A80` | 93 | UnwindData |  |
| 285 | `sqlite3_wal_hook` | `0x52AF0` | 128 | UnwindData |  |
| 152 | `sqlite3_os_init` | `0x53C90` | 443 | UnwindData |  |
| 269 | `sqlite3_vfs_register` | `0x53E60` | 177 | UnwindData |  |
| 53 | `sqlite3_column_name` | `0x53F70` | 944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `sqlite3_mutex_free` | `0x54320` | 27 | UnwindData |  |
| 12 | `sqlite3_bind_double` | `0x554C0` | 100 | UnwindData |  |
| 212 | `sqlite3_stmt_readonly` | `0x55830` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `sqlite3_data_count` | `0x55B60` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `sqlite3_column_value` | `0x55B90` | 77 | UnwindData |  |
| 189 | `sqlite3_rollback_hook` | `0x56270` | 128 | UnwindData |  |
| 181 | `sqlite3_result_text` | `0x56910` | 49 | UnwindData |  |
| 217 | `sqlite3_str_appendf` | `0x56950` | 34 | UnwindData |  |
| 33 | `sqlite3_busy_timeout` | `0x56CB0` | 126 | UnwindData |  |
| 32 | `sqlite3_busy_handler` | `0x56D40` | 146 | UnwindData |  |
| 141 | `sqlite3_msize` | `0x56E20` | 33 | UnwindData |  |
| 142 | `sqlite3_mutex_alloc` | `0x56E50` | 57 | UnwindData |  |
| 251 | `sqlite3_value_double` | `0x56ED0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 290 | `sqlite3_win32_set_directory16` | `0x56FB0` | 79 | UnwindData |  |
| 291 | `sqlite3_win32_set_directory8` | `0x57010` | 178 | UnwindData |  |
| 293 | `sqlite3_win32_unicode_to_utf8` | `0x570D0` | 65 | UnwindData |  |
| 107 | `sqlite3_extended_result_codes` | `0x57120` | 121 | UnwindData |  |
| 68 | `sqlite3_config` | `0x58780` | 988 | UnwindData |  |
| 48 | `sqlite3_column_decltype` | `0x58BA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `sqlite3_close_v2` | `0x58BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `sqlite3_backup_finish` | `0x58BD0` | 229 | UnwindData |  |
| 35 | `sqlite3_changes` | `0x58E90` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 233 | `sqlite3_thread_cleanup` | `0x59070` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `sqlite3_open_v2` | `0x59150` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `sqlite3_close` | `0x59210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 148 | `sqlite3_open` | `0x59220` | 7,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 216 | `sqlite3_str_appendchar` | `0x5B040` | 83 | UnwindData |  |
| 9 | `sqlite3_backup_step` | `0x79380` | 1,242 | UnwindData |  |
| 22 | `sqlite3_bind_text64` | `0x79860` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `sqlite3_clear_bindings` | `0x798A0` | 201 | UnwindData |  |
| 45 | `sqlite3_column_count` | `0x79970` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `sqlite3_db_config` | `0x79990` | 295 | UnwindData |  |
| 91 | `sqlite3_db_status` | `0x79AC0` | 159 | UnwindData |  |
| 93 | `sqlite3_declare_vtab` | `0x79B70` | 694 | UnwindData |  |
| 177 | `sqlite3_result_int64` | `0x79E30` | 23 | UnwindData |  |
| 178 | `sqlite3_result_null` | `0x79E50` | 23 | UnwindData |  |
| 289 | `sqlite3_win32_set_directory` | `0x83100` | 1,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `sqlite3_prepare` | `0x836B0` | 39 | UnwindData |  |
| 227 | `sqlite3_strlike` | `0x83710` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 234 | `sqlite3_threadsafe` | `0x83890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 286 | `sqlite3_win32_is_nt` | `0x83890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 204 | `sqlite3_sourceid` | `0x838A0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `sqlite3_prepare_v3` | `0x83900` | 50 | UnwindData |  |
| 2 | `sqlite3_aggregate_count` | `0xCFE20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `sqlite3_auto_extension` | `0xCFE30` | 193 | UnwindData |  |
| 4 | `sqlite3_autovacuum_pages` | `0xCFF00` | 178 | UnwindData |  |
| 7 | `sqlite3_backup_pagecount` | `0xCFFC0` | 44 | UnwindData |  |
| 8 | `sqlite3_backup_remaining` | `0xD0000` | 44 | UnwindData |  |
| 11 | `sqlite3_bind_blob64` | `0xD0040` | 30 | UnwindData |  |
| 18 | `sqlite3_bind_parameter_name` | `0xD0070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `sqlite3_bind_pointer` | `0xD0090` | 142 | UnwindData |  |
| 24 | `sqlite3_bind_zeroblob` | `0xD0130` | 99 | UnwindData |  |
| 25 | `sqlite3_bind_zeroblob64` | `0xD01A0` | 140 | UnwindData |  |
| 28 | `sqlite3_blob_open` | `0xD0240` | 1,282 | UnwindData |  |
| 31 | `sqlite3_blob_write` | `0xD0750` | 27 | UnwindData |  |
| 34 | `sqlite3_cancel_auto_extension` | `0xD0780` | 140 | UnwindData |  |
| 40 | `sqlite3_collation_needed` | `0xD0820` | 114 | UnwindData |  |
| 41 | `sqlite3_collation_needed16` | `0xD08A0` | 114 | UnwindData |  |
| 44 | `sqlite3_column_bytes16` | `0xD0920` | 52 | UnwindData |  |
| 46 | `sqlite3_column_database_name` | `0xD0960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `sqlite3_column_database_name16` | `0xD0980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `sqlite3_column_decltype16` | `0xD09A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `sqlite3_column_name16` | `0xD09C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `sqlite3_column_origin_name` | `0xD09E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `sqlite3_column_origin_name16` | `0xD0A00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `sqlite3_column_table_name` | `0xD0A20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `sqlite3_column_table_name16` | `0xD0A40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `sqlite3_commit_hook` | `0xD0A60` | 126 | UnwindData |  |
| 64 | `sqlite3_compileoption_get` | `0xD0AF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `sqlite3_compileoption_used` | `0xD0B10` | 192 | UnwindData |  |
| 66 | `sqlite3_complete` | `0xD0BE0` | 694 | UnwindData |  |
| 67 | `sqlite3_complete16` | `0xD0EA0` | 107 | UnwindData |  |
| 71 | `sqlite3_create_collation16` | `0xD0F20` | 205 | UnwindData |  |
| 73 | `sqlite3_create_filename` | `0xD1000` | 354 | UnwindData |  |
| 75 | `sqlite3_create_function16` | `0xD1170` | 261 | UnwindData |  |
| 79 | `sqlite3_create_window_function` | `0xD1280` | 95 | UnwindData |  |
| 82 | `sqlite3_database_file_object` | `0xD12F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `sqlite3_db_cacheflush` | `0xD1320` | 274 | UnwindData |  |
| 87 | `sqlite3_db_mutex` | `0xD1440` | 53 | UnwindData |  |
| 88 | `sqlite3_db_name` | `0xD1480` | 85 | UnwindData |  |
| 89 | `sqlite3_db_readonly` | `0xD14E0` | 89 | UnwindData |  |
| 90 | `sqlite3_db_release_memory` | `0xD1540` | 166 | UnwindData |  |
| 92 | `sqlite3_db_status64` | `0xD15F0` | 1,214 | UnwindData |  |
| 94 | `sqlite3_deserialize` | `0xD1AC0` | 453 | UnwindData |  |
| 95 | `sqlite3_drop_modules` | `0xD1C90` | 179 | UnwindData |  |
| 96 | `sqlite3_enable_load_extension` | `0xD1D50` | 108 | UnwindData |  |
| 97 | `sqlite3_enable_shared_cache` | `0xD1DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `sqlite3_errmsg16` | `0xD1DE0` | 162 | UnwindData |  |
| 101 | `sqlite3_error_offset` | `0xD1E90` | 71 | UnwindData |  |
| 102 | `sqlite3_errstr` | `0xD1EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `sqlite3_expanded_sql` | `0xD1EF0` | 91 | UnwindData |  |
| 105 | `sqlite3_expired` | `0xD1F60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `sqlite3_extended_errcode` | `0xD1F80` | 71 | UnwindData |  |
| 109 | `sqlite3_filename_database` | `0xD1FD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `sqlite3_filename_journal` | `0xD1FF0` | 81 | UnwindData |  |
| 111 | `sqlite3_filename_wal` | `0xD2050` | 42 | UnwindData |  |
| 115 | `sqlite3_free_table` | `0xD2080` | 87 | UnwindData |  |
| 118 | `sqlite3_get_auxdata` | `0xD20E0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `sqlite3_get_clientdata` | `0xD2130` | 110 | UnwindData |  |
| 120 | `sqlite3_get_table` | `0xD21B0` | 458 | UnwindData |  |
| 122 | `sqlite3_hard_heap_limit64` | `0xD24E0` | 110 | UnwindData |  |
| 124 | `sqlite3_interrupt` | `0xD2560` | 73 | UnwindData |  |
| 125 | `sqlite3_is_interrupted` | `0xD25B0` | 77 | UnwindData |  |
| 126 | `sqlite3_keyword_check` | `0xD2610` | 25 | UnwindData |  |
| 127 | `sqlite3_keyword_count` | `0xD2630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `sqlite3_keyword_name` | `0xD2640` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | `sqlite3_libversion` | `0xD2690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `sqlite3_libversion_number` | `0xD26A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `sqlite3_limit` | `0xD26B0` | 131 | UnwindData |  |
| 133 | `sqlite3_load_extension` | `0xD2740` | 103 | UnwindData |  |
| 138 | `sqlite3_memory_highwater` | `0xD27B0` | 41 | UnwindData |  |
| 139 | `sqlite3_memory_used` | `0xD27E0` | 41 | UnwindData |  |
| 151 | `sqlite3_os_end` | `0xD2810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `sqlite3_prepare16` | `0xD2830` | 33 | UnwindData |  |
| 157 | `sqlite3_prepare16_v3` | `0xD2860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 160 | `sqlite3_profile` | `0xD2880` | 146 | UnwindData |  |
| 161 | `sqlite3_progress_handler` | `0xD2920` | 152 | UnwindData |  |
| 163 | `sqlite3_realloc` | `0xD29C0` | 60 | UnwindData |  |
| 167 | `sqlite3_reset_auto_extension` | `0xD2A10` | 76 | UnwindData |  |
| 168 | `sqlite3_result_blob` | `0xD2A70` | 54 | UnwindData |  |
| 169 | `sqlite3_result_blob64` | `0xD2AB0` | 63 | UnwindData |  |
| 170 | `sqlite3_result_double` | `0xD2B00` | 23 | UnwindData |  |
| 171 | `sqlite3_result_error` | `0xD2B20` | 42 | UnwindData |  |
| 172 | `sqlite3_result_error16` | `0xD2B50` | 42 | UnwindData |  |
| 173 | `sqlite3_result_error_code` | `0xD2B80` | 72 | UnwindData |  |
| 174 | `sqlite3_result_error_nomem` | `0xD2BD0` | 47 | UnwindData |  |
| 175 | `sqlite3_result_error_toobig` | `0xD2C10` | 50 | UnwindData |  |
| 179 | `sqlite3_result_pointer` | `0xD2C50` | 106 | UnwindData |  |
| 180 | `sqlite3_result_subtype` | `0xD2CC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 182 | `sqlite3_result_text16` | `0xD2CE0` | 27 | UnwindData |  |
| 184 | `sqlite3_result_text16le` | `0xD2CE0` | 27 | UnwindData |  |
| 183 | `sqlite3_result_text16be` | `0xD2D10` | 27 | UnwindData |  |
| 185 | `sqlite3_result_text64` | `0xD2D40` | 111 | UnwindData |  |
| 187 | `sqlite3_result_zeroblob` | `0xD2DC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 188 | `sqlite3_result_zeroblob64` | `0xD2DE0` | 88 | UnwindData |  |
| 190 | `sqlite3_rtree_geometry_callback` | `0xD2E40` | 162 | UnwindData |  |
| 191 | `sqlite3_rtree_query_callback` | `0xD2EF0` | 196 | UnwindData |  |
| 192 | `sqlite3_serialize` | `0xD2FC0` | 639 | UnwindData |  |
| 193 | `sqlite3_set_authorizer` | `0xD3250` | 124 | UnwindData |  |
| 194 | `sqlite3_set_auxdata` | `0xD32E0` | 232 | UnwindData |  |
| 195 | `sqlite3_set_clientdata` | `0xD33D0` | 310 | UnwindData |  |
| 196 | `sqlite3_set_errmsg` | `0xD3510` | 135 | UnwindData |  |
| 198 | `sqlite3_setlk_timeout` | `0xD35A0` | 64 | UnwindData |  |
| 199 | `sqlite3_shutdown` | `0xD35F0` | 187 | UnwindData |  |
| 200 | `sqlite3_sleep` | `0xD36C0` | 70 | UnwindData |  |
| 202 | `sqlite3_soft_heap_limit` | `0xD3710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 203 | `sqlite3_soft_heap_limit64` | `0xD3730` | 181 | UnwindData |  |
| 206 | `sqlite3_status` | `0xD37F0` | 103 | UnwindData |  |
| 207 | `sqlite3_status64` | `0xD3860` | 192 | UnwindData |  |
| 210 | `sqlite3_stmt_explain` | `0xD3930` | 310 | UnwindData |  |
| 211 | `sqlite3_stmt_isexplain` | `0xD3A70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 213 | `sqlite3_stmt_status` | `0xD3A90` | 179 | UnwindData |  |
| 218 | `sqlite3_str_errcode` | `0xD3B50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 219 | `sqlite3_str_finish` | `0xD3B70` | 63 | UnwindData |  |
| 220 | `sqlite3_str_length` | `0xD3BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 221 | `sqlite3_str_new` | `0xD3BE0` | 80 | UnwindData |  |
| 223 | `sqlite3_str_value` | `0xD3C40` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 225 | `sqlite3_strglob` | `0xD3C70` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 229 | `sqlite3_system_errno` | `0xD3CB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 230 | `sqlite3_table_column_metadata` | `0xD3CD0` | 639 | UnwindData |  |
| 232 | `sqlite3_test_control` | `0xD3F60` | 1,030 | UnwindData |  |
| 235 | `sqlite3_total_changes` | `0xD4370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 236 | `sqlite3_total_changes64` | `0xD4380` | 56 | UnwindData |  |
| 237 | `sqlite3_trace` | `0xD43C0` | 140 | UnwindData |  |
| 238 | `sqlite3_trace_v2` | `0xD4460` | 142 | UnwindData |  |
| 239 | `sqlite3_transfer_bindings` | `0xD4500` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 240 | `sqlite3_txn_state` | `0xD4560` | 194 | UnwindData |  |
| 242 | `sqlite3_update_hook` | `0xD4630` | 126 | UnwindData |  |
| 244 | `sqlite3_uri_int64` | `0xD46C0` | 56 | UnwindData |  |
| 245 | `sqlite3_uri_key` | `0xD4700` | 104 | UnwindData |  |
| 250 | `sqlite3_value_bytes16` | `0xD4770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 252 | `sqlite3_value_dup` | `0xD4780` | 180 | UnwindData |  |
| 253 | `sqlite3_value_encoding` | `0xD4840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 254 | `sqlite3_value_free` | `0xD4850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 255 | `sqlite3_value_frombind` | `0xD4860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 258 | `sqlite3_value_nochange` | `0xD4880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 260 | `sqlite3_value_pointer` | `0xD48A0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 261 | `sqlite3_value_subtype` | `0xD4900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 264 | `sqlite3_value_text16be` | `0xD4920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 270 | `sqlite3_vfs_unregister` | `0xD4930` | 71 | UnwindData |  |
| 273 | `sqlite3_vtab_collation` | `0xD4980` | 92 | UnwindData |  |
| 274 | `sqlite3_vtab_config` | `0xD49F0` | 210 | UnwindData |  |
| 275 | `sqlite3_vtab_distinct` | `0xD4AD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 276 | `sqlite3_vtab_in` | `0xD4AE0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 277 | `sqlite3_vtab_in_first` | `0xD4B20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 278 | `sqlite3_vtab_in_next` | `0xD4B30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 279 | `sqlite3_vtab_nochange` | `0xD4B50` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 281 | `sqlite3_vtab_rhs_value` | `0xD4B80` | 154 | UnwindData |  |
| 287 | `sqlite3_win32_mbcs_to_utf8` | `0xD4C20` | 79 | UnwindData |  |
| 288 | `sqlite3_win32_mbcs_to_utf8_v2` | `0xD4C80` | 75 | UnwindData |  |
| 294 | `sqlite3_win32_utf8_to_mbcs` | `0xD4CE0` | 79 | UnwindData |  |
| 295 | `sqlite3_win32_utf8_to_mbcs_v2` | `0xD4D40` | 75 | UnwindData |  |
| 296 | `sqlite3_win32_utf8_to_unicode` | `0xD4DA0` | 65 | UnwindData |  |
| 297 | `sqlite3_win32_write_debug` | `0xD4DF0` | 176 | UnwindData |  |
| 267 | `sqlite3_version` | `0xF1E58` | 69,644 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `sqlite3_fts3_may_be_corrupt` | `0x102E64` | 1,548 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `sqlite3_data_directory` | `0x103470` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 231 | `sqlite3_temp_directory` | `0x103478` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 241 | `sqlite3_unsupported_selecttrace` | `0x1035D8` | 0 | Indeterminate |  |
