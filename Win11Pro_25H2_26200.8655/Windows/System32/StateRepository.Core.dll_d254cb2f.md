# Binary Specification: StateRepository.Core.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\StateRepository.Core.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d254cb2ff077f9a641e469b79bedc0e51845e08a5262844e92eae6ba84dd8c16`
* **Total Exported Functions:** 273

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 77 | `sqlite3_db_filename` | `0x1310` | 20 | UnwindData |  |
| 208 | `sqlite3_stricmp` | `0x1550` | 23,728 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `sqlite3_errcode` | `0x7200` | 97 | UnwindData |  |
| 122 | `sqlite3_log` | `0x7270` | 44 | UnwindData |  |
| 141 | `sqlite3_prepare` | `0x78C0` | 39 | UnwindData |  |
| 240 | `sqlite3_value_text` | `0x78F0` | 70 | UnwindData |  |
| 241 | `sqlite3_value_text16` | `0x7980` | 70 | UnwindData |  |
| 243 | `sqlite3_value_text16le` | `0x7980` | 70 | UnwindData |  |
| 52 | `sqlite3_column_text` | `0x7F80` | 173 | UnwindData |  |
| 42 | `sqlite3_column_bytes` | `0x8040` | 132 | UnwindData |  |
| 54 | `sqlite3_column_type` | `0x80D0` | 141 | UnwindData |  |
| 94 | `sqlite3_exec` | `0x8170` | 980 | UnwindData |  |
| 190 | `sqlite3_step` | `0x8550` | 384 | UnwindData |  |
| 153 | `sqlite3_reset` | `0x89D0` | 190 | UnwindData |  |
| 41 | `sqlite3_column_blob` | `0x8B20` | 132 | UnwindData |  |
| 226 | `sqlite3_value_blob` | `0x8BB0` | 122 | UnwindData |  |
| 48 | `sqlite3_column_int` | `0x8C80` | 180 | UnwindData |  |
| 49 | `sqlite3_column_int64` | `0x8D40` | 181 | UnwindData |  |
| 53 | `sqlite3_column_text16` | `0x8E30` | 228 | UnwindData |  |
| 145 | `sqlite3_prepare_v2` | `0x9330` | 42 | UnwindData |  |
| 130 | `sqlite3_mutex_enter` | `0x9570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `sqlite3_mutex_leave` | `0x9590` | 1,440 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `sqlite3_create_function_v2` | `0x9B30` | 431 | UnwindData |  |
| 103 | `sqlite3_free` | `0xAAC0` | 133 | UnwindData |  |
| 173 | `sqlite3_result_value` | `0xC6D0` | 85 | UnwindData |  |
| 1 | `sqlite3_aggregate_context` | `0xC900` | 2,272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `sqlite3_randomness` | `0xD1E0` | 393 | UnwindData |  |
| 123 | `sqlite3_malloc` | `0xE160` | 24 | UnwindData |  |
| 187 | `sqlite3_sql` | `0x11600` | 2,672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 249 | `sqlite3_vsnprintf` | `0x12070` | 130 | UnwindData |  |
| 199 | `sqlite3_str_appendf` | `0x12200` | 34 | UnwindData |  |
| 206 | `sqlite3_str_vappendf` | `0x12230` | 5,111 | UnwindData |  |
| 12 | `sqlite3_bind_int` | `0x15F00` | 141 | UnwindData |  |
| 13 | `sqlite3_bind_int64` | `0x15FA0` | 141 | UnwindData |  |
| 151 | `sqlite3_realloc64` | `0x16B00` | 896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `sqlite3_snprintf` | `0x16E80` | 132 | UnwindData |  |
| 20 | `sqlite3_bind_text16` | `0x17180` | 37 | UnwindData |  |
| 9 | `sqlite3_bind_blob` | `0x171B0` | 87 | UnwindData |  |
| 106 | `sqlite3_get_autocommit` | `0x17ED0` | 93 | UnwindData |  |
| 90 | `sqlite3_errmsg` | `0x18A50` | 166 | UnwindData |  |
| 78 | `sqlite3_db_handle` | `0x18C60` | 1,376 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 210 | `sqlite3_strnicmp` | `0x191C0` | 14,128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 196 | `sqlite3_str_append` | `0x1C8F0` | 59 | UnwindData |  |
| 268 | `sqlite3_win32_sleep` | `0x1F400` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `sqlite3_extended_result_codes` | `0x1F460` | 121 | UnwindData |  |
| 32 | `sqlite3_busy_timeout` | `0x1F770` | 126 | UnwindData |  |
| 31 | `sqlite3_busy_handler` | `0x1F800` | 146 | UnwindData |  |
| 139 | `sqlite3_os_init` | `0x1F9F0` | 131 | UnwindData |  |
| 246 | `sqlite3_vfs_register` | `0x1FA80` | 144 | UnwindData |  |
| 259 | `sqlite3_wal_autocheckpoint` | `0x1FBE0` | 117 | UnwindData |  |
| 262 | `sqlite3_wal_hook` | `0x1FC60` | 148 | UnwindData |  |
| 124 | `sqlite3_malloc64` | `0x20740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 245 | `sqlite3_vfs_find` | `0x20750` | 128 | UnwindData |  |
| 234 | `sqlite3_value_int` | `0x20950` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 235 | `sqlite3_value_int64` | `0x20950` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 227 | `sqlite3_value_bytes` | `0x20BD0` | 784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `sqlite3_overload_function` | `0x20EE0` | 274 | UnwindData |  |
| 127 | `sqlite3_mprintf` | `0x21000` | 38 | UnwindData |  |
| 117 | `sqlite3_last_insert_rowid` | `0x21140` | 55 | UnwindData |  |
| 189 | `sqlite3_status64` | `0x214C0` | 198 | UnwindData |  |
| 188 | `sqlite3_status` | `0x218C0` | 253 | UnwindData |  |
| 128 | `sqlite3_msize` | `0x21C80` | 33 | UnwindData |  |
| 137 | `sqlite3_open_v2` | `0x21CB0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 197 | `sqlite3_str_appendall` | `0x21D20` | 30 | UnwindData |  |
| 37 | `sqlite3_close` | `0x21E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `sqlite3_shutdown` | `0x21E60` | 207 | UnwindData |  |
| 154 | `sqlite3_reset_auto_extension` | `0x21F40` | 67 | UnwindData |  |
| 261 | `sqlite3_wal_checkpoint_v2` | `0x22140` | 288 | UnwindData |  |
| 221 | `sqlite3_uri_boolean` | `0x22270` | 48 | UnwindData |  |
| 224 | `sqlite3_uri_parameter` | `0x222B0` | 45 | UnwindData |  |
| 50 | `sqlite3_column_name` | `0x229C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `sqlite3_config` | `0x229E0` | 1,005 | UnwindData |  |
| 81 | `sqlite3_db_readonly` | `0x22FD0` | 111 | UnwindData |  |
| 152 | `sqlite3_release_memory` | `0x23430` | 1,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `sqlite3_mutex_free` | `0x23840` | 27 | UnwindData |  |
| 244 | `sqlite3_value_type` | `0x23870` | 237,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `sqlite3_backup_step` | `0x5D980` | 1,207 | UnwindData |  |
| 34 | `sqlite3_changes` | `0x5DE40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `sqlite3_clear_bindings` | `0x5DE50` | 201 | UnwindData |  |
| 76 | `sqlite3_db_config` | `0x5DF20` | 295 | UnwindData |  |
| 83 | `sqlite3_db_status` | `0x5E050` | 159 | UnwindData |  |
| 98 | `sqlite3_file_control` | `0x5E100` | 326 | UnwindData |  |
| 102 | `sqlite3_finalize` | `0x5E250` | 145 | UnwindData |  |
| 111 | `sqlite3_initialize` | `0x5E2F0` | 472 | UnwindData |  |
| 129 | `sqlite3_mutex_alloc` | `0x5E4D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `sqlite3_result_blob` | `0x5E4F0` | 54 | UnwindData |  |
| 163 | `sqlite3_result_int` | `0x5E530` | 26 | UnwindData |  |
| 164 | `sqlite3_result_int64` | `0x5E550` | 23 | UnwindData |  |
| 168 | `sqlite3_result_text` | `0x5E570` | 49 | UnwindData |  |
| 172 | `sqlite3_result_text64` | `0x5E5B0` | 111 | UnwindData |  |
| 209 | `sqlite3_strlike` | `0x5E630` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 215 | `sqlite3_total_changes` | `0x5E660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 247 | `sqlite3_vfs_unregister` | `0x5E670` | 64 | UnwindData |  |
| 248 | `sqlite3_vmprintf` | `0x5E6C0` | 154 | UnwindData |  |
| 162 | `sqlite3_result_error_toobig` | `0x69F30` | 50 | UnwindData |  |
| 62 | `sqlite3_context_db_handle` | `0x69F70` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 204 | `sqlite3_str_reset` | `0x6A150` | 65 | UnwindData |  |
| 260 | `sqlite3_wal_checkpoint` | `0x6A3F0` | 27 | UnwindData |  |
| 138 | `sqlite3_os_end` | `0x6A460` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `sqlite3_sourceid` | `0x6A490` | 158,752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `sqlite3_auto_extension` | `0x910B0` | 183 | UnwindData |  |
| 3 | `sqlite3_autovacuum_pages` | `0x91170` | 178 | UnwindData |  |
| 4 | `sqlite3_backup_finish` | `0x91230` | 203 | UnwindData |  |
| 5 | `sqlite3_backup_init` | `0x91310` | 337 | UnwindData |  |
| 6 | `sqlite3_backup_pagecount` | `0x91470` | 44 | UnwindData |  |
| 7 | `sqlite3_backup_remaining` | `0x914B0` | 44 | UnwindData |  |
| 10 | `sqlite3_bind_blob64` | `0x914F0` | 30 | UnwindData |  |
| 11 | `sqlite3_bind_double` | `0x91520` | 100 | UnwindData |  |
| 14 | `sqlite3_bind_null` | `0x91590` | 52 | UnwindData |  |
| 15 | `sqlite3_bind_parameter_count` | `0x915D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `sqlite3_bind_parameter_index` | `0x915F0` | 30 | UnwindData |  |
| 17 | `sqlite3_bind_parameter_name` | `0x91620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `sqlite3_bind_pointer` | `0x91640` | 142 | UnwindData |  |
| 19 | `sqlite3_bind_text` | `0x916E0` | 33 | UnwindData |  |
| 21 | `sqlite3_bind_text64` | `0x91710` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `sqlite3_bind_value` | `0x91750` | 184 | UnwindData |  |
| 23 | `sqlite3_bind_zeroblob` | `0x91810` | 99 | UnwindData |  |
| 24 | `sqlite3_bind_zeroblob64` | `0x91880` | 140 | UnwindData |  |
| 25 | `sqlite3_blob_bytes` | `0x91920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `sqlite3_blob_close` | `0x91940` | 87 | UnwindData |  |
| 27 | `sqlite3_blob_open` | `0x919A0` | 1,202 | UnwindData |  |
| 28 | `sqlite3_blob_read` | `0x91E60` | 27 | UnwindData |  |
| 29 | `sqlite3_blob_reopen` | `0x91E90` | 203 | UnwindData |  |
| 30 | `sqlite3_blob_write` | `0x91F70` | 27 | UnwindData |  |
| 33 | `sqlite3_cancel_auto_extension` | `0x91FA0` | 140 | UnwindData |  |
| 35 | `sqlite3_changes64` | `0x92040` | 53 | UnwindData |  |
| 38 | `sqlite3_close_v2` | `0x92080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `sqlite3_collation_needed` | `0x92090` | 114 | UnwindData |  |
| 40 | `sqlite3_collation_needed16` | `0x92110` | 114 | UnwindData |  |
| 43 | `sqlite3_column_bytes16` | `0x92190` | 52 | UnwindData |  |
| 44 | `sqlite3_column_count` | `0x921D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `sqlite3_column_decltype` | `0x921F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `sqlite3_column_decltype16` | `0x92210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `sqlite3_column_double` | `0x92230` | 53 | UnwindData |  |
| 51 | `sqlite3_column_name16` | `0x92270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `sqlite3_column_value` | `0x92290` | 75 | UnwindData |  |
| 56 | `sqlite3_commit_hook` | `0x922F0` | 126 | UnwindData |  |
| 57 | `sqlite3_compileoption_get` | `0x92380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `sqlite3_compileoption_used` | `0x923A0` | 192 | UnwindData |  |
| 59 | `sqlite3_complete` | `0x92470` | 694 | UnwindData |  |
| 60 | `sqlite3_complete16` | `0x92730` | 98 | UnwindData |  |
| 63 | `sqlite3_create_collation` | `0x927A0` | 31 | UnwindData |  |
| 64 | `sqlite3_create_collation16` | `0x927D0` | 205 | UnwindData |  |
| 65 | `sqlite3_create_collation_v2` | `0x928B0` | 161 | UnwindData |  |
| 66 | `sqlite3_create_filename` | `0x92960` | 354 | UnwindData |  |
| 67 | `sqlite3_create_function` | `0x92AD0` | 80 | UnwindData |  |
| 68 | `sqlite3_create_function16` | `0x92B30` | 256 | UnwindData |  |
| 70 | `sqlite3_create_module` | `0x92C40` | 115 | UnwindData |  |
| 71 | `sqlite3_create_module_v2` | `0x92CC0` | 119 | UnwindData |  |
| 72 | `sqlite3_create_window_function` | `0x92D40` | 95 | UnwindData |  |
| 73 | `sqlite3_data_count` | `0x92DB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `sqlite3_database_file_object` | `0x92DE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `sqlite3_db_cacheflush` | `0x92E10` | 191 | UnwindData |  |
| 79 | `sqlite3_db_mutex` | `0x92EE0` | 53 | UnwindData |  |
| 80 | `sqlite3_db_name` | `0x92F20` | 85 | UnwindData |  |
| 82 | `sqlite3_db_release_memory` | `0x92F80` | 150 | UnwindData |  |
| 84 | `sqlite3_db_status64` | `0x93020` | 1,149 | UnwindData |  |
| 85 | `sqlite3_declare_vtab` | `0x934B0` | 700 | UnwindData |  |
| 86 | `sqlite3_deserialize` | `0x93780` | 453 | UnwindData |  |
| 87 | `sqlite3_drop_modules` | `0x93950` | 179 | UnwindData |  |
| 88 | `sqlite3_enable_load_extension` | `0x93A10` | 108 | UnwindData |  |
| 91 | `sqlite3_errmsg16` | `0x93A90` | 162 | UnwindData |  |
| 92 | `sqlite3_error_offset` | `0x93B40` | 71 | UnwindData |  |
| 93 | `sqlite3_errstr` | `0x93B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `sqlite3_expanded_sql` | `0x93BA0` | 91 | UnwindData |  |
| 96 | `sqlite3_extended_errcode` | `0x93C30` | 71 | UnwindData |  |
| 99 | `sqlite3_filename_database` | `0x93C80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `sqlite3_filename_journal` | `0x93CA0` | 81 | UnwindData |  |
| 101 | `sqlite3_filename_wal` | `0x93D00` | 42 | UnwindData |  |
| 104 | `sqlite3_free_filename` | `0x93D30` | 29 | UnwindData |  |
| 105 | `sqlite3_free_table` | `0x93D60` | 87 | UnwindData |  |
| 107 | `sqlite3_get_auxdata` | `0x93DC0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `sqlite3_get_clientdata` | `0x93E00` | 110 | UnwindData |  |
| 109 | `sqlite3_get_table` | `0x93E80` | 458 | UnwindData |  |
| 110 | `sqlite3_hard_heap_limit64` | `0x941B0` | 95 | UnwindData |  |
| 112 | `sqlite3_interrupt` | `0x94220` | 73 | UnwindData |  |
| 113 | `sqlite3_is_interrupted` | `0x94270` | 77 | UnwindData |  |
| 114 | `sqlite3_keyword_check` | `0x942D0` | 25 | UnwindData |  |
| 115 | `sqlite3_keyword_count` | `0x942F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `sqlite3_keyword_name` | `0x94300` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `sqlite3_libversion` | `0x94350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `sqlite3_libversion_number` | `0x94360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `sqlite3_limit` | `0x94370` | 131 | UnwindData |  |
| 121 | `sqlite3_load_extension` | `0x94400` | 103 | UnwindData |  |
| 125 | `sqlite3_memory_highwater` | `0x94470` | 41 | UnwindData |  |
| 126 | `sqlite3_memory_used` | `0x944A0` | 41 | UnwindData |  |
| 133 | `sqlite3_mutex_try` | `0x944D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `sqlite3_next_stmt` | `0x944F0` | 97 | UnwindData |  |
| 135 | `sqlite3_open` | `0x94560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `sqlite3_open16` | `0x94580` | 207 | UnwindData |  |
| 142 | `sqlite3_prepare16` | `0x94660` | 33 | UnwindData |  |
| 143 | `sqlite3_prepare16_v2` | `0x94690` | 36 | UnwindData |  |
| 144 | `sqlite3_prepare16_v3` | `0x946C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `sqlite3_prepare_v3` | `0x946E0` | 50 | UnwindData |  |
| 147 | `sqlite3_profile` | `0x94720` | 146 | UnwindData |  |
| 148 | `sqlite3_progress_handler` | `0x947C0` | 152 | UnwindData |  |
| 150 | `sqlite3_realloc` | `0x94860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `sqlite3_result_blob64` | `0x94880` | 63 | UnwindData |  |
| 157 | `sqlite3_result_double` | `0x948D0` | 23 | UnwindData |  |
| 158 | `sqlite3_result_error` | `0x948F0` | 42 | UnwindData |  |
| 159 | `sqlite3_result_error16` | `0x94920` | 42 | UnwindData |  |
| 160 | `sqlite3_result_error_code` | `0x94950` | 72 | UnwindData |  |
| 161 | `sqlite3_result_error_nomem` | `0x949A0` | 47 | UnwindData |  |
| 165 | `sqlite3_result_null` | `0x949E0` | 23 | UnwindData |  |
| 166 | `sqlite3_result_pointer` | `0x94A00` | 106 | UnwindData |  |
| 167 | `sqlite3_result_subtype` | `0x94A70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `sqlite3_result_text16` | `0x94A90` | 27 | UnwindData |  |
| 171 | `sqlite3_result_text16le` | `0x94A90` | 27 | UnwindData |  |
| 170 | `sqlite3_result_text16be` | `0x94AC0` | 27 | UnwindData |  |
| 174 | `sqlite3_result_zeroblob` | `0x94AF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 175 | `sqlite3_result_zeroblob64` | `0x94B10` | 88 | UnwindData |  |
| 176 | `sqlite3_rollback_hook` | `0x94B70` | 126 | UnwindData |  |
| 177 | `sqlite3_serialize` | `0x94C00` | 639 | UnwindData |  |
| 178 | `sqlite3_set_auxdata` | `0x94E90` | 230 | UnwindData |  |
| 179 | `sqlite3_set_clientdata` | `0x94F80` | 310 | UnwindData |  |
| 180 | `sqlite3_set_last_insert_rowid` | `0x95150` | 81 | UnwindData |  |
| 182 | `sqlite3_sleep` | `0x95200` | 70 | UnwindData |  |
| 184 | `sqlite3_soft_heap_limit` | `0x95250` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `sqlite3_soft_heap_limit64` | `0x95270` | 163 | UnwindData |  |
| 191 | `sqlite3_stmt_busy` | `0x95320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 192 | `sqlite3_stmt_explain` | `0x95340` | 310 | UnwindData |  |
| 193 | `sqlite3_stmt_isexplain` | `0x95480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 194 | `sqlite3_stmt_readonly` | `0x954A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 195 | `sqlite3_stmt_status` | `0x954C0` | 179 | UnwindData |  |
| 198 | `sqlite3_str_appendchar` | `0x95580` | 83 | UnwindData |  |
| 200 | `sqlite3_str_errcode` | `0x955E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | `sqlite3_str_finish` | `0x95600` | 63 | UnwindData |  |
| 202 | `sqlite3_str_length` | `0x95650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 203 | `sqlite3_str_new` | `0x95670` | 80 | UnwindData |  |
| 205 | `sqlite3_str_value` | `0x956D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 207 | `sqlite3_strglob` | `0x95700` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 211 | `sqlite3_system_errno` | `0x95740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 212 | `sqlite3_table_column_metadata` | `0x95760` | 633 | UnwindData |  |
| 213 | `sqlite3_test_control` | `0x959E0` | 1,030 | UnwindData |  |
| 214 | `sqlite3_threadsafe` | `0x95DF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 216 | `sqlite3_total_changes64` | `0x95E00` | 56 | UnwindData |  |
| 217 | `sqlite3_trace` | `0x95E40` | 140 | UnwindData |  |
| 218 | `sqlite3_trace_v2` | `0x95EE0` | 142 | UnwindData |  |
| 219 | `sqlite3_txn_state` | `0x95FE0` | 194 | UnwindData |  |
| 220 | `sqlite3_update_hook` | `0x960B0` | 126 | UnwindData |  |
| 222 | `sqlite3_uri_int64` | `0x96140` | 56 | UnwindData |  |
| 223 | `sqlite3_uri_key` | `0x96180` | 104 | UnwindData |  |
| 225 | `sqlite3_user_data` | `0x961F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 228 | `sqlite3_value_bytes16` | `0x96210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 229 | `sqlite3_value_double` | `0x96220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 230 | `sqlite3_value_dup` | `0x96230` | 180 | UnwindData |  |
| 231 | `sqlite3_value_encoding` | `0x962F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 232 | `sqlite3_value_free` | `0x96300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 233 | `sqlite3_value_frombind` | `0x96310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 236 | `sqlite3_value_nochange` | `0x96330` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 237 | `sqlite3_value_numeric_type` | `0x96350` | 66 | UnwindData |  |
| 238 | `sqlite3_value_pointer` | `0x963A0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 239 | `sqlite3_value_subtype` | `0x96400` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 242 | `sqlite3_value_text16be` | `0x96420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 250 | `sqlite3_vtab_collation` | `0x96430` | 92 | UnwindData |  |
| 251 | `sqlite3_vtab_config` | `0x964A0` | 210 | UnwindData |  |
| 252 | `sqlite3_vtab_distinct` | `0x96580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 253 | `sqlite3_vtab_in` | `0x96590` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 254 | `sqlite3_vtab_in_first` | `0x965D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 255 | `sqlite3_vtab_in_next` | `0x965E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 256 | `sqlite3_vtab_nochange` | `0x96600` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 257 | `sqlite3_vtab_on_conflict` | `0x96630` | 66 | UnwindData |  |
| 258 | `sqlite3_vtab_rhs_value` | `0x96680` | 154 | UnwindData |  |
| 263 | `sqlite3_win32_mbcs_to_utf8` | `0x96720` | 70 | UnwindData |  |
| 264 | `sqlite3_win32_mbcs_to_utf8_v2` | `0x96770` | 48 | UnwindData |  |
| 265 | `sqlite3_win32_set_directory` | `0x967B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 266 | `sqlite3_win32_set_directory16` | `0x967C0` | 79 | UnwindData |  |
| 267 | `sqlite3_win32_set_directory8` | `0x96820` | 171 | UnwindData |  |
| 269 | `sqlite3_win32_unicode_to_utf8` | `0x968E0` | 48 | UnwindData |  |
| 270 | `sqlite3_win32_utf8_to_mbcs` | `0x96920` | 70 | UnwindData |  |
| 271 | `sqlite3_win32_utf8_to_mbcs_v2` | `0x96970` | 48 | UnwindData |  |
| 272 | `sqlite3_win32_utf8_to_unicode` | `0x969B0` | 48 | UnwindData |  |
| 273 | `sqlite3_win32_write_debug` | `0x969F0` | 176 | UnwindData |  |
