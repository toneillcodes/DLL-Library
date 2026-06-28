# Binary Specification: SearchIndexerCore.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\SearchIndexerCore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `49bb86eae9bd92d229a7aac205328540aa7c5d38f73161f491bfe6d58fedb04a`
* **Total Exported Functions:** 271

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 108 | `sqlite3_finalize` | `0x116B0` | 221 | UnwindData |  |
| 15 | `sqlite3_bind_blob` | `0x12E50` | 87 | UnwindData |  |
| 16 | `sqlite3_bind_blob64` | `0x13390` | 617 | UnwindData |  |
| 47 | `sqlite3_column_blob` | `0x13600` | 135 | UnwindData |  |
| 235 | `sqlite3_value_blob` | `0x13690` | 124 | UnwindData |  |
| 196 | `sqlite3_step` | `0x13720` | 43 | UnwindData |  |
| 249 | `sqlite3_value_text` | `0x13AA0` | 68 | UnwindData |  |
| 58 | `sqlite3_column_text` | `0x13AF0` | 254 | UnwindData |  |
| 48 | `sqlite3_column_bytes` | `0x14B70` | 234 | UnwindData |  |
| 54 | `sqlite3_column_int` | `0x14F80` | 233 | UnwindData |  |
| 160 | `sqlite3_reset` | `0x15070` | 22 | UnwindData |  |
| 55 | `sqlite3_column_int64` | `0x151E0` | 256 | UnwindData |  |
| 60 | `sqlite3_column_type` | `0x15340` | 219 | UnwindData |  |
| 19 | `sqlite3_bind_int64` | `0x154E0` | 139 | UnwindData |  |
| 109 | `sqlite3_free` | `0x15EA0` | 117 | UnwindData |  |
| 99 | `sqlite3_exec` | `0x17100` | 1,020 | UnwindData |  |
| 151 | `sqlite3_prepare_v2` | `0x18870` | 42 | UnwindData |  |
| 95 | `sqlite3_errmsg` | `0x1F7D0` | 164 | UnwindData |  |
| 94 | `sqlite3_errcode` | `0x1FA60` | 76 | UnwindData |  |
| 256 | `sqlite3_vfs_unregister` | `0x200A0` | 71 | UnwindData |  |
| 255 | `sqlite3_vfs_register` | `0x204D0` | 177 | UnwindData |  |
| 137 | `sqlite3_mutex_alloc` | `0x20C40` | 57 | UnwindData |  |
| 76 | `sqlite3_create_module` | `0x20C80` | 139 | UnwindData |  |
| 130 | `sqlite3_malloc` | `0x20D20` | 49 | UnwindData |  |
| 157 | `sqlite3_realloc64` | `0x20D60` | 52 | UnwindData |  |
| 77 | `sqlite3_create_module_v2` | `0x20DA0` | 143 | UnwindData |  |
| 75 | `sqlite3_create_function_v2` | `0x20E60` | 88 | UnwindData |  |
| 214 | `sqlite3_stricmp` | `0x21070` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `sqlite3_overload_function` | `0x210D0` | 285 | UnwindData |  |
| 136 | `sqlite3_multi_value_extension_init` | `0x21200` | 371 | UnwindData |  |
| 228 | `sqlite3_unicode_collations_extension_init` | `0x215D0` | 141 | UnwindData |  |
| 257 | `sqlite3_vmprintf` | `0x21670` | 220 | UnwindData |  |
| 134 | `sqlite3_mprintf` | `0x21760` | 57 | UnwindData |  |
| 37 | `sqlite3_busy_handler` | `0x21840` | 122 | UnwindData |  |
| 73 | `sqlite3_create_function` | `0x218C0` | 80 | UnwindData |  |
| 131 | `sqlite3_malloc64` | `0x21E80` | 40 | UnwindData |  |
| 104 | `sqlite3_file_control` | `0x22160` | 349 | UnwindData |  |
| 38 | `sqlite3_busy_timeout` | `0x22590` | 126 | UnwindData |  |
| 71 | `sqlite3_create_collation_v2` | `0x227A0` | 183 | UnwindData |  |
| 254 | `sqlite3_vfs_find` | `0x23790` | 139 | UnwindData |  |
| 17 | `sqlite3_bind_double` | `0x23830` | 100 | UnwindData |  |
| 218 | `sqlite3_table_column_metadata` | `0x23C50` | 800 | UnwindData |  |
| 112 | `sqlite3_get_autocommit` | `0x23F80` | 75 | UnwindData |  |
| 41 | `sqlite3_changes64` | `0x23FE0` | 55 | UnwindData |  |
| 138 | `sqlite3_mutex_enter` | `0x24070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `sqlite3_bind_null` | `0x24090` | 52 | UnwindData |  |
| 140 | `sqlite3_mutex_leave` | `0x240D0` | 912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 270 | `sqlite3_wal_checkpoint_v2` | `0x24460` | 288 | UnwindData |  |
| 216 | `sqlite3_strnicmp` | `0x27460` | 8,464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 203 | `sqlite3_str_appendall` | `0x29570` | 30 | UnwindData |  |
| 212 | `sqlite3_str_vappendf` | `0x29690` | 4,741 | UnwindData |  |
| 258 | `sqlite3_vsnprintf` | `0x2AD10` | 130 | UnwindData |  |
| 129 | `sqlite3_log` | `0x33850` | 47 | UnwindData |  |
| 155 | `sqlite3_randomness` | `0x37F90` | 406 | UnwindData |  |
| 189 | `sqlite3_snprintf` | `0x3D2C0` | 132 | UnwindData |  |
| 53 | `sqlite3_column_double` | `0x3E500` | 53 | UnwindData |  |
| 22 | `sqlite3_bind_parameter_index` | `0x40250` | 185 | UnwindData |  |
| 1 | `create_sqlite3_impersonation_vfs` | `0x43C60` | 362 | UnwindData |  |
| 115 | `sqlite3_global_recover` | `0x44BB0` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `sqlite3_release_memory` | `0x44BB0` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `sqlite3_aggregate_context` | `0x44D30` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 244 | `sqlite3_value_int64` | `0x44FB0` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 236 | `sqlite3_value_bytes` | `0x45390` | 74 | UnwindData |  |
| 18 | `sqlite3_bind_int` | `0x46CE0` | 139 | UnwindData |  |
| 202 | `sqlite3_str_append` | `0x47220` | 59 | UnwindData |  |
| 3 | `sqlite3GetVarint` | `0x485D0` | 441 | UnwindData |  |
| 253 | `sqlite3_value_type` | `0x492D0` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `sqlite3_backup_step` | `0x494B0` | 1,355 | UnwindData |  |
| 27 | `sqlite3_bind_text64` | `0x4A5C0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `sqlite3_free_filename` | `0x4A6F0` | 33 | UnwindData |  |
| 230 | `sqlite3_uri_boolean` | `0x4A720` | 48 | UnwindData |  |
| 233 | `sqlite3_uri_parameter` | `0x4A760` | 45 | UnwindData |  |
| 243 | `sqlite3_value_int` | `0x4A960` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `sqlite3_mutex_try` | `0x4AA00` | 1,904 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `sqlite3_db_handle` | `0x4B170` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `sqlite3_changes` | `0x4B470` | 3,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 268 | `sqlite3_wal_autocheckpoint` | `0x4C150` | 117 | UnwindData |  |
| 271 | `sqlite3_wal_hook` | `0x4C1D0` | 128 | UnwindData |  |
| 139 | `sqlite3_mutex_free` | `0x4C790` | 27 | UnwindData |  |
| 56 | `sqlite3_column_name` | `0x4C8C0` | 896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 238 | `sqlite3_value_double` | `0x4CC40` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 193 | `sqlite3_sql` | `0x4CD20` | 1,632 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 195 | `sqlite3_status64` | `0x4D380` | 246 | UnwindData |  |
| 43 | `sqlite3_close` | `0x4D750` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 269 | `sqlite3_wal_checkpoint` | `0x4D780` | 27 | UnwindData |  |
| 145 | `sqlite3_open_v2` | `0x4D930` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `sqlite3_column_count` | `0x4D9C0` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `sqlite3_last_insert_rowid` | `0x4DC00` | 75 | UnwindData |  |
| 199 | `sqlite3_stmt_isexplain` | `0x4DCB0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `sqlite3_context_db_handle` | `0x4DD80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `sqlite3_memory_used` | `0x4DDA0` | 55 | UnwindData |  |
| 132 | `sqlite3_memory_highwater` | `0x4DDE0` | 85 | UnwindData |  |
| 171 | `sqlite3_result_int64` | `0x4E520` | 23 | UnwindData |  |
| 2 | `delete_sqlite3_impersonation_vfs` | `0x4E540` | 73 | UnwindData |  |
| 25 | `sqlite3_bind_text` | `0x4E590` | 33 | UnwindData |  |
| 220 | `sqlite3_thread_cleanup` | `0x4EA90` | 3,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 217 | `sqlite3_system_errno` | `0x4F690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `sqlite3_extended_errcode` | `0x4F6B0` | 71 | UnwindData |  |
| 4 | `sqlite3PutVarint` | `0x4F700` | 100,992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `sqlite3_clear_bindings` | `0x68180` | 67 | UnwindData |  |
| 163 | `sqlite3_result_blob64` | `0x682A0` | 63 | UnwindData |  |
| 175 | `sqlite3_result_text` | `0x682F0` | 49 | UnwindData |  |
| 117 | `sqlite3_indexer_extensions_init` | `0x6C9B0` | 92 | UnwindData |  |
| 169 | `sqlite3_result_error_toobig` | `0x71230` | 50 | UnwindData |  |
| 204 | `sqlite3_str_appendchar` | `0x72530` | 83 | UnwindData |  |
| 239 | `sqlite3_value_dup` | `0x73850` | 180 | UnwindData |  |
| 241 | `sqlite3_value_free` | `0x73CD0` | 8,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `sqlite3_db_release_memory` | `0x75DC0` | 192 | UnwindData |  |
| 250 | `sqlite3_value_text16` | `0x77970` | 2,720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 252 | `sqlite3_value_text16le` | `0x77970` | 2,720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `sqlite3_backup_finish` | `0x78410` | 221 | UnwindData |  |
| 210 | `sqlite3_str_reset` | `0x7ABC0` | 59 | UnwindData |  |
| 205 | `sqlite3_str_appendf` | `0x7AF30` | 34 | UnwindData |  |
| 192 | `sqlite3_sourceid` | `0x7B030` | 130,768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `sqlite3_aggregate_count` | `0x9AF00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `sqlite3_auto_extension` | `0x9AF10` | 193 | UnwindData |  |
| 9 | `sqlite3_autovacuum_pages` | `0x9AFE0` | 178 | UnwindData |  |
| 11 | `sqlite3_backup_init` | `0x9B0A0` | 337 | UnwindData |  |
| 12 | `sqlite3_backup_pagecount` | `0x9B200` | 44 | UnwindData |  |
| 13 | `sqlite3_backup_remaining` | `0x9B240` | 44 | UnwindData |  |
| 21 | `sqlite3_bind_parameter_count` | `0x9B280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `sqlite3_bind_parameter_name` | `0x9B2A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `sqlite3_bind_pointer` | `0x9B2C0` | 142 | UnwindData |  |
| 26 | `sqlite3_bind_text16` | `0x9B360` | 37 | UnwindData |  |
| 28 | `sqlite3_bind_value` | `0x9B390` | 184 | UnwindData |  |
| 29 | `sqlite3_bind_zeroblob` | `0x9B450` | 99 | UnwindData |  |
| 30 | `sqlite3_bind_zeroblob64` | `0x9B4C0` | 140 | UnwindData |  |
| 31 | `sqlite3_blob_bytes` | `0x9B560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `sqlite3_blob_close` | `0x9B580` | 87 | UnwindData |  |
| 33 | `sqlite3_blob_open` | `0x9B5E0` | 1,328 | UnwindData |  |
| 34 | `sqlite3_blob_read` | `0x9BB20` | 27 | UnwindData |  |
| 35 | `sqlite3_blob_reopen` | `0x9BB50` | 198 | UnwindData |  |
| 36 | `sqlite3_blob_write` | `0x9BC20` | 27 | UnwindData |  |
| 39 | `sqlite3_cancel_auto_extension` | `0x9BC50` | 140 | UnwindData |  |
| 44 | `sqlite3_close_v2` | `0x9BCF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `sqlite3_collation_needed` | `0x9BD00` | 114 | UnwindData |  |
| 46 | `sqlite3_collation_needed16` | `0x9BD80` | 114 | UnwindData |  |
| 49 | `sqlite3_column_bytes16` | `0x9BE00` | 52 | UnwindData |  |
| 51 | `sqlite3_column_decltype` | `0x9BE40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `sqlite3_column_decltype16` | `0x9BE60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `sqlite3_column_name16` | `0x9BE80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `sqlite3_column_text16` | `0x9BEA0` | 54 | UnwindData |  |
| 61 | `sqlite3_column_value` | `0x9BEE0` | 75 | UnwindData |  |
| 62 | `sqlite3_commit_hook` | `0x9BF40` | 126 | UnwindData |  |
| 63 | `sqlite3_compileoption_get` | `0x9BFD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `sqlite3_compileoption_used` | `0x9BFF0` | 192 | UnwindData |  |
| 65 | `sqlite3_complete` | `0x9C0C0` | 694 | UnwindData |  |
| 66 | `sqlite3_complete16` | `0x9C380` | 107 | UnwindData |  |
| 69 | `sqlite3_create_collation` | `0x9C7E0` | 31 | UnwindData |  |
| 70 | `sqlite3_create_collation16` | `0x9C810` | 205 | UnwindData |  |
| 72 | `sqlite3_create_filename` | `0x9C8F0` | 354 | UnwindData |  |
| 74 | `sqlite3_create_function16` | `0x9CA60` | 261 | UnwindData |  |
| 78 | `sqlite3_create_window_function` | `0x9CB70` | 95 | UnwindData |  |
| 79 | `sqlite3_data_count` | `0x9CBE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `sqlite3_database_file_object` | `0x9CC10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `sqlite3_db_cacheflush` | `0x9CC40` | 274 | UnwindData |  |
| 82 | `sqlite3_db_config` | `0x9CD60` | 270 | UnwindData |  |
| 83 | `sqlite3_db_filename` | `0x9CE80` | 112 | UnwindData |  |
| 85 | `sqlite3_db_mutex` | `0x9CF00` | 53 | UnwindData |  |
| 86 | `sqlite3_db_name` | `0x9CF40` | 85 | UnwindData |  |
| 87 | `sqlite3_db_readonly` | `0x9CFA0` | 89 | UnwindData |  |
| 89 | `sqlite3_db_status` | `0x9D000` | 1,165 | UnwindData |  |
| 90 | `sqlite3_declare_vtab` | `0x9D4A0` | 687 | UnwindData |  |
| 91 | `sqlite3_deserialize` | `0x9D760` | 453 | UnwindData |  |
| 92 | `sqlite3_drop_modules` | `0x9D930` | 179 | UnwindData |  |
| 93 | `sqlite3_enable_shared_cache` | `0x9D9F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `sqlite3_errmsg16` | `0x9DA00` | 162 | UnwindData |  |
| 97 | `sqlite3_error_offset` | `0x9DAB0` | 71 | UnwindData |  |
| 98 | `sqlite3_errstr` | `0x9DB00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `sqlite3_expanded_sql` | `0x9DB10` | 91 | UnwindData |  |
| 101 | `sqlite3_expired` | `0x9DB80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `sqlite3_extended_result_codes` | `0x9DBA0` | 95 | UnwindData |  |
| 105 | `sqlite3_filename_database` | `0x9DC10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `sqlite3_filename_journal` | `0x9DC30` | 81 | UnwindData |  |
| 107 | `sqlite3_filename_wal` | `0x9DC90` | 42 | UnwindData |  |
| 111 | `sqlite3_free_table` | `0x9DCC0` | 87 | UnwindData |  |
| 113 | `sqlite3_get_auxdata` | `0x9DD20` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `sqlite3_get_table` | `0x9DDE0` | 458 | UnwindData |  |
| 116 | `sqlite3_hard_heap_limit64` | `0x9E110` | 110 | UnwindData |  |
| 118 | `sqlite3_interrupt` | `0x9E190` | 73 | UnwindData |  |
| 119 | `sqlite3_is_interrupted` | `0x9E1E0` | 77 | UnwindData |  |
| 120 | `sqlite3_key_v2` | `0x9E240` | 146 | UnwindData |  |
| 121 | `sqlite3_keyword_check` | `0x9E2E0` | 25 | UnwindData |  |
| 122 | `sqlite3_keyword_count` | `0x9E300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `sqlite3_keyword_name` | `0x9E310` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `sqlite3_libversion` | `0x9E360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `sqlite3_libversion_number` | `0x9E370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `sqlite3_limit` | `0x9E380` | 131 | UnwindData |  |
| 128 | `sqlite3_load_extension` | `0x9E410` | 103 | UnwindData |  |
| 135 | `sqlite3_msize` | `0x9E480` | 31 | UnwindData |  |
| 142 | `sqlite3_next_stmt` | `0x9E4B0` | 97 | UnwindData |  |
| 143 | `sqlite3_open` | `0x9E520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `sqlite3_open16` | `0x9E540` | 220 | UnwindData |  |
| 147 | `sqlite3_prepare` | `0x9E630` | 39 | UnwindData |  |
| 148 | `sqlite3_prepare16` | `0x9E660` | 33 | UnwindData |  |
| 149 | `sqlite3_prepare16_v2` | `0x9E690` | 36 | UnwindData |  |
| 150 | `sqlite3_prepare16_v3` | `0x9E6C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `sqlite3_prepare_v3` | `0x9E6E0` | 50 | UnwindData |  |
| 153 | `sqlite3_profile` | `0x9E720` | 146 | UnwindData |  |
| 154 | `sqlite3_progress_handler` | `0x9E7C0` | 152 | UnwindData |  |
| 156 | `sqlite3_realloc` | `0x9E860` | 60 | UnwindData |  |
| 158 | `sqlite3_rekey_v2` | `0x9E8B0` | 620 | UnwindData |  |
| 161 | `sqlite3_reset_auto_extension` | `0x9EB30` | 76 | UnwindData |  |
| 162 | `sqlite3_result_blob` | `0x9EB90` | 54 | UnwindData |  |
| 164 | `sqlite3_result_double` | `0x9EBD0` | 23 | UnwindData |  |
| 165 | `sqlite3_result_error` | `0x9EBF0` | 42 | UnwindData |  |
| 166 | `sqlite3_result_error16` | `0x9EC20` | 42 | UnwindData |  |
| 167 | `sqlite3_result_error_code` | `0x9EC50` | 72 | UnwindData |  |
| 168 | `sqlite3_result_error_nomem` | `0x9ECA0` | 47 | UnwindData |  |
| 170 | `sqlite3_result_int` | `0x9ECE0` | 26 | UnwindData |  |
| 172 | `sqlite3_result_null` | `0x9ED00` | 23 | UnwindData |  |
| 173 | `sqlite3_result_pointer` | `0x9ED20` | 106 | UnwindData |  |
| 174 | `sqlite3_result_subtype` | `0x9ED90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `sqlite3_result_text16` | `0x9EDB0` | 27 | UnwindData |  |
| 178 | `sqlite3_result_text16le` | `0x9EDB0` | 27 | UnwindData |  |
| 177 | `sqlite3_result_text16be` | `0x9EDE0` | 27 | UnwindData |  |
| 179 | `sqlite3_result_text64` | `0x9EE10` | 111 | UnwindData |  |
| 180 | `sqlite3_result_value` | `0x9EE90` | 85 | UnwindData |  |
| 181 | `sqlite3_result_zeroblob` | `0x9EEF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 182 | `sqlite3_result_zeroblob64` | `0x9EF10` | 88 | UnwindData |  |
| 183 | `sqlite3_rollback_hook` | `0x9EF70` | 126 | UnwindData |  |
| 184 | `sqlite3_serialize` | `0x9F000` | 639 | UnwindData |  |
| 185 | `sqlite3_set_authorizer` | `0x9F290` | 124 | UnwindData |  |
| 186 | `sqlite3_set_auxdata` | `0x9F320` | 230 | UnwindData |  |
| 187 | `sqlite3_set_last_insert_rowid` | `0x9F550` | 81 | UnwindData |  |
| 188 | `sqlite3_sleep` | `0x9F5B0` | 70 | UnwindData |  |
| 190 | `sqlite3_soft_heap_limit` | `0x9F600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 191 | `sqlite3_soft_heap_limit64` | `0x9F620` | 181 | UnwindData |  |
| 194 | `sqlite3_status` | `0x9F6E0` | 103 | UnwindData |  |
| 197 | `sqlite3_stmt_busy` | `0x9F750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 198 | `sqlite3_stmt_explain` | `0x9F770` | 310 | UnwindData |  |
| 200 | `sqlite3_stmt_readonly` | `0x9F8B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | `sqlite3_stmt_status` | `0x9F8D0` | 179 | UnwindData |  |
| 206 | `sqlite3_str_errcode` | `0x9F990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 207 | `sqlite3_str_finish` | `0x9F9B0` | 63 | UnwindData |  |
| 208 | `sqlite3_str_length` | `0x9FA00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 209 | `sqlite3_str_new` | `0x9FA20` | 80 | UnwindData |  |
| 211 | `sqlite3_str_value` | `0x9FA80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 213 | `sqlite3_strglob` | `0x9FAB0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 215 | `sqlite3_strlike` | `0x9FAF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 219 | `sqlite3_test_control` | `0x9FB20` | 1,071 | UnwindData |  |
| 221 | `sqlite3_threadsafe` | `0x9FF60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `sqlite3_total_changes` | `0x9FF70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 223 | `sqlite3_total_changes64` | `0x9FF80` | 56 | UnwindData |  |
| 224 | `sqlite3_trace` | `0x9FFC0` | 140 | UnwindData |  |
| 225 | `sqlite3_trace_v2` | `0xA0060` | 142 | UnwindData |  |
| 226 | `sqlite3_transfer_bindings` | `0xA0100` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 227 | `sqlite3_txn_state` | `0xA0160` | 194 | UnwindData |  |
| 229 | `sqlite3_update_hook` | `0xA0230` | 126 | UnwindData |  |
| 231 | `sqlite3_uri_int64` | `0xA02C0` | 56 | UnwindData |  |
| 232 | `sqlite3_uri_key` | `0xA0300` | 104 | UnwindData |  |
| 234 | `sqlite3_user_data` | `0xA0370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 237 | `sqlite3_value_bytes16` | `0xA0390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 240 | `sqlite3_value_encoding` | `0xA03A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 242 | `sqlite3_value_frombind` | `0xA03B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 245 | `sqlite3_value_nochange` | `0xA03D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 246 | `sqlite3_value_numeric_type` | `0xA03F0` | 66 | UnwindData |  |
| 247 | `sqlite3_value_pointer` | `0xA0440` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 248 | `sqlite3_value_subtype` | `0xA04A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 251 | `sqlite3_value_text16be` | `0xA04C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 259 | `sqlite3_vtab_collation` | `0xA04D0` | 96 | UnwindData |  |
| 260 | `sqlite3_vtab_config` | `0xA0540` | 210 | UnwindData |  |
| 261 | `sqlite3_vtab_distinct` | `0xA0620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 262 | `sqlite3_vtab_in` | `0xA0630` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 263 | `sqlite3_vtab_in_first` | `0xA0670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 264 | `sqlite3_vtab_in_next` | `0xA0680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 265 | `sqlite3_vtab_nochange` | `0xA06A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 266 | `sqlite3_vtab_on_conflict` | `0xA06D0` | 66 | UnwindData |  |
| 267 | `sqlite3_vtab_rhs_value` | `0xA0720` | 158 | UnwindData |  |
| 5 | `sqlite3VarintLen` | `0xA9430` | 31,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `sqlite3_cosine_similarity_extension_init` | `0xB0E10` | 121 | UnwindData |  |
