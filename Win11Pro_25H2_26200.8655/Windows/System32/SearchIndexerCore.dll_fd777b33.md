# Binary Specification: SearchIndexerCore.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\SearchIndexerCore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fd777b331498fb1863cc3c9076d5591a00dbd75ebde11a3e00d34f3ac50be74b`
* **Total Exported Functions:** 271

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 108 | `sqlite3_finalize` | `0xA210` | 221 | UnwindData |  |
| 15 | `sqlite3_bind_blob` | `0xBAE0` | 87 | UnwindData |  |
| 16 | `sqlite3_bind_blob64` | `0xC020` | 617 | UnwindData |  |
| 47 | `sqlite3_column_blob` | `0xC290` | 135 | UnwindData |  |
| 235 | `sqlite3_value_blob` | `0xC320` | 124 | UnwindData |  |
| 196 | `sqlite3_step` | `0xC3B0` | 43 | UnwindData |  |
| 249 | `sqlite3_value_text` | `0xC730` | 68 | UnwindData |  |
| 58 | `sqlite3_column_text` | `0xC780` | 254 | UnwindData |  |
| 48 | `sqlite3_column_bytes` | `0xD800` | 234 | UnwindData |  |
| 54 | `sqlite3_column_int` | `0xDC10` | 233 | UnwindData |  |
| 160 | `sqlite3_reset` | `0xDD00` | 22 | UnwindData |  |
| 55 | `sqlite3_column_int64` | `0xDE70` | 256 | UnwindData |  |
| 60 | `sqlite3_column_type` | `0xDFD0` | 219 | UnwindData |  |
| 19 | `sqlite3_bind_int64` | `0xE170` | 139 | UnwindData |  |
| 109 | `sqlite3_free` | `0xEB30` | 117 | UnwindData |  |
| 99 | `sqlite3_exec` | `0xFD90` | 1,020 | UnwindData |  |
| 151 | `sqlite3_prepare_v2` | `0x11500` | 42 | UnwindData |  |
| 216 | `sqlite3_strnicmp` | `0x21E50` | 5,152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 254 | `sqlite3_vfs_find` | `0x23270` | 139 | UnwindData |  |
| 17 | `sqlite3_bind_double` | `0x23310` | 100 | UnwindData |  |
| 218 | `sqlite3_table_column_metadata` | `0x23730` | 800 | UnwindData |  |
| 112 | `sqlite3_get_autocommit` | `0x23A60` | 75 | UnwindData |  |
| 41 | `sqlite3_changes64` | `0x23AC0` | 55 | UnwindData |  |
| 138 | `sqlite3_mutex_enter` | `0x23B50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `sqlite3_bind_null` | `0x23B70` | 52 | UnwindData |  |
| 140 | `sqlite3_mutex_leave` | `0x23BB0` | 912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 270 | `sqlite3_wal_checkpoint_v2` | `0x23F40` | 288 | UnwindData |  |
| 129 | `sqlite3_log` | `0x2E370` | 47 | UnwindData |  |
| 155 | `sqlite3_randomness` | `0x32AB0` | 406 | UnwindData |  |
| 130 | `sqlite3_malloc` | `0x33520` | 49 | UnwindData |  |
| 157 | `sqlite3_realloc64` | `0x33560` | 52 | UnwindData |  |
| 77 | `sqlite3_create_module_v2` | `0x33A10` | 143 | UnwindData |  |
| 75 | `sqlite3_create_function_v2` | `0x33EA0` | 88 | UnwindData |  |
| 136 | `sqlite3_multi_value_extension_init` | `0x34050` | 371 | UnwindData |  |
| 257 | `sqlite3_vmprintf` | `0x341D0` | 220 | UnwindData |  |
| 134 | `sqlite3_mprintf` | `0x342C0` | 57 | UnwindData |  |
| 73 | `sqlite3_create_function` | `0x34550` | 80 | UnwindData |  |
| 131 | `sqlite3_malloc64` | `0x345B0` | 40 | UnwindData |  |
| 189 | `sqlite3_snprintf` | `0x34CD0` | 132 | UnwindData |  |
| 258 | `sqlite3_vsnprintf` | `0x35310` | 130 | UnwindData |  |
| 203 | `sqlite3_str_appendall` | `0x35C80` | 30 | UnwindData |  |
| 212 | `sqlite3_str_vappendf` | `0x35DA0` | 4,741 | UnwindData |  |
| 146 | `sqlite3_overload_function` | `0x37670` | 285 | UnwindData |  |
| 95 | `sqlite3_errmsg` | `0x38810` | 164 | UnwindData |  |
| 94 | `sqlite3_errcode` | `0x38AA0` | 76 | UnwindData |  |
| 53 | `sqlite3_column_double` | `0x3A690` | 53 | UnwindData |  |
| 22 | `sqlite3_bind_parameter_index` | `0x3DBD0` | 185 | UnwindData |  |
| 104 | `sqlite3_file_control` | `0x3E8B0` | 349 | UnwindData |  |
| 214 | `sqlite3_stricmp` | `0x3EBF0` | 14,944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `sqlite3_global_recover` | `0x42650` | 2,592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `sqlite3_release_memory` | `0x42650` | 2,592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `sqlite3_aggregate_context` | `0x43070` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 244 | `sqlite3_value_int64` | `0x432F0` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 236 | `sqlite3_value_bytes` | `0x436D0` | 74 | UnwindData |  |
| 18 | `sqlite3_bind_int` | `0x45290` | 139 | UnwindData |  |
| 202 | `sqlite3_str_append` | `0x457F0` | 59 | UnwindData |  |
| 3 | `sqlite3GetVarint` | `0x47330` | 441 | UnwindData |  |
| 253 | `sqlite3_value_type` | `0x48030` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `sqlite3_backup_step` | `0x481A0` | 1,355 | UnwindData |  |
| 27 | `sqlite3_bind_text64` | `0x492B0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 228 | `sqlite3_unicode_collations_extension_init` | `0x493E0` | 141 | UnwindData |  |
| 71 | `sqlite3_create_collation_v2` | `0x49480` | 183 | UnwindData |  |
| 110 | `sqlite3_free_filename` | `0x49700` | 33 | UnwindData |  |
| 230 | `sqlite3_uri_boolean` | `0x49730` | 48 | UnwindData |  |
| 233 | `sqlite3_uri_parameter` | `0x49770` | 45 | UnwindData |  |
| 243 | `sqlite3_value_int` | `0x49990` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `sqlite3_mutex_try` | `0x49A30` | 3,664 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `sqlite3_db_handle` | `0x4A880` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `sqlite3_changes` | `0x4AB80` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `sqlite3_busy_timeout` | `0x4B0D0` | 126 | UnwindData |  |
| 37 | `sqlite3_busy_handler` | `0x4B160` | 122 | UnwindData |  |
| 256 | `sqlite3_vfs_unregister` | `0x4B8E0` | 71 | UnwindData |  |
| 255 | `sqlite3_vfs_register` | `0x4BAF0` | 177 | UnwindData |  |
| 268 | `sqlite3_wal_autocheckpoint` | `0x4BE40` | 117 | UnwindData |  |
| 271 | `sqlite3_wal_hook` | `0x4BEC0` | 128 | UnwindData |  |
| 139 | `sqlite3_mutex_free` | `0x4C450` | 27 | UnwindData |  |
| 56 | `sqlite3_column_name` | `0x4C580` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 238 | `sqlite3_value_double` | `0x4C8E0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 193 | `sqlite3_sql` | `0x4C9C0` | 1,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `sqlite3_create_module` | `0x4CFE0` | 139 | UnwindData |  |
| 195 | `sqlite3_status64` | `0x4D0C0` | 246 | UnwindData |  |
| 43 | `sqlite3_close` | `0x4D6E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `sqlite3_mutex_alloc` | `0x4D6F0` | 57 | UnwindData |  |
| 269 | `sqlite3_wal_checkpoint` | `0x4D750` | 27 | UnwindData |  |
| 145 | `sqlite3_open_v2` | `0x4D900` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `sqlite3_column_count` | `0x4D990` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `sqlite3_last_insert_rowid` | `0x4DBD0` | 75 | UnwindData |  |
| 199 | `sqlite3_stmt_isexplain` | `0x4DC80` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `sqlite3_context_db_handle` | `0x4DD50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `sqlite3_memory_used` | `0x4DD70` | 55 | UnwindData |  |
| 132 | `sqlite3_memory_highwater` | `0x4DE10` | 85 | UnwindData |  |
| 171 | `sqlite3_result_int64` | `0x4E500` | 23 | UnwindData |  |
| 2 | `delete_sqlite3_impersonation_vfs` | `0x4E520` | 73 | UnwindData |  |
| 25 | `sqlite3_bind_text` | `0x4E570` | 33 | UnwindData |  |
| 220 | `sqlite3_thread_cleanup` | `0x4EA70` | 3,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 217 | `sqlite3_system_errno` | `0x4F670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `sqlite3_extended_errcode` | `0x4F690` | 71 | UnwindData |  |
| 4 | `sqlite3PutVarint` | `0x4F6E0` | 98,240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `sqlite3_clear_bindings` | `0x676A0` | 67 | UnwindData |  |
| 163 | `sqlite3_result_blob64` | `0x677C0` | 63 | UnwindData |  |
| 175 | `sqlite3_result_text` | `0x67810` | 49 | UnwindData |  |
| 1 | `create_sqlite3_impersonation_vfs` | `0x6BED0` | 377 | UnwindData |  |
| 117 | `sqlite3_indexer_extensions_init` | `0x6CD50` | 92 | UnwindData |  |
| 169 | `sqlite3_result_error_toobig` | `0x715B0` | 50 | UnwindData |  |
| 204 | `sqlite3_str_appendchar` | `0x728B0` | 83 | UnwindData |  |
| 239 | `sqlite3_value_dup` | `0x73BD0` | 180 | UnwindData |  |
| 241 | `sqlite3_value_free` | `0x74050` | 8,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `sqlite3_db_release_memory` | `0x76140` | 192 | UnwindData |  |
| 250 | `sqlite3_value_text16` | `0x77CF0` | 2,720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 252 | `sqlite3_value_text16le` | `0x77CF0` | 2,720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `sqlite3_backup_finish` | `0x78790` | 221 | UnwindData |  |
| 210 | `sqlite3_str_reset` | `0x7AF40` | 59 | UnwindData |  |
| 205 | `sqlite3_str_appendf` | `0x7B2B0` | 34 | UnwindData |  |
| 192 | `sqlite3_sourceid` | `0x7B3B0` | 130,768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `sqlite3_aggregate_count` | `0x9B280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `sqlite3_auto_extension` | `0x9B290` | 193 | UnwindData |  |
| 9 | `sqlite3_autovacuum_pages` | `0x9B360` | 178 | UnwindData |  |
| 11 | `sqlite3_backup_init` | `0x9B420` | 337 | UnwindData |  |
| 12 | `sqlite3_backup_pagecount` | `0x9B580` | 44 | UnwindData |  |
| 13 | `sqlite3_backup_remaining` | `0x9B5C0` | 44 | UnwindData |  |
| 21 | `sqlite3_bind_parameter_count` | `0x9B600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `sqlite3_bind_parameter_name` | `0x9B620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `sqlite3_bind_pointer` | `0x9B640` | 142 | UnwindData |  |
| 26 | `sqlite3_bind_text16` | `0x9B6E0` | 37 | UnwindData |  |
| 28 | `sqlite3_bind_value` | `0x9B710` | 184 | UnwindData |  |
| 29 | `sqlite3_bind_zeroblob` | `0x9B7D0` | 99 | UnwindData |  |
| 30 | `sqlite3_bind_zeroblob64` | `0x9B840` | 140 | UnwindData |  |
| 31 | `sqlite3_blob_bytes` | `0x9B8E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `sqlite3_blob_close` | `0x9B900` | 87 | UnwindData |  |
| 33 | `sqlite3_blob_open` | `0x9B960` | 1,328 | UnwindData |  |
| 34 | `sqlite3_blob_read` | `0x9BEA0` | 27 | UnwindData |  |
| 35 | `sqlite3_blob_reopen` | `0x9BED0` | 198 | UnwindData |  |
| 36 | `sqlite3_blob_write` | `0x9BFA0` | 27 | UnwindData |  |
| 39 | `sqlite3_cancel_auto_extension` | `0x9BFD0` | 140 | UnwindData |  |
| 44 | `sqlite3_close_v2` | `0x9C070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `sqlite3_collation_needed` | `0x9C080` | 114 | UnwindData |  |
| 46 | `sqlite3_collation_needed16` | `0x9C100` | 114 | UnwindData |  |
| 49 | `sqlite3_column_bytes16` | `0x9C180` | 52 | UnwindData |  |
| 51 | `sqlite3_column_decltype` | `0x9C1C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `sqlite3_column_decltype16` | `0x9C1E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `sqlite3_column_name16` | `0x9C200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `sqlite3_column_text16` | `0x9C220` | 54 | UnwindData |  |
| 61 | `sqlite3_column_value` | `0x9C260` | 75 | UnwindData |  |
| 62 | `sqlite3_commit_hook` | `0x9C2C0` | 126 | UnwindData |  |
| 63 | `sqlite3_compileoption_get` | `0x9C350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `sqlite3_compileoption_used` | `0x9C370` | 192 | UnwindData |  |
| 65 | `sqlite3_complete` | `0x9C440` | 694 | UnwindData |  |
| 66 | `sqlite3_complete16` | `0x9C700` | 107 | UnwindData |  |
| 69 | `sqlite3_create_collation` | `0x9CB60` | 31 | UnwindData |  |
| 70 | `sqlite3_create_collation16` | `0x9CB90` | 205 | UnwindData |  |
| 72 | `sqlite3_create_filename` | `0x9CC70` | 354 | UnwindData |  |
| 74 | `sqlite3_create_function16` | `0x9CDE0` | 261 | UnwindData |  |
| 78 | `sqlite3_create_window_function` | `0x9CEF0` | 95 | UnwindData |  |
| 79 | `sqlite3_data_count` | `0x9CF60` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `sqlite3_database_file_object` | `0x9CF90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `sqlite3_db_cacheflush` | `0x9CFC0` | 274 | UnwindData |  |
| 82 | `sqlite3_db_config` | `0x9D0E0` | 270 | UnwindData |  |
| 83 | `sqlite3_db_filename` | `0x9D200` | 112 | UnwindData |  |
| 85 | `sqlite3_db_mutex` | `0x9D280` | 53 | UnwindData |  |
| 86 | `sqlite3_db_name` | `0x9D2C0` | 85 | UnwindData |  |
| 87 | `sqlite3_db_readonly` | `0x9D320` | 89 | UnwindData |  |
| 89 | `sqlite3_db_status` | `0x9D380` | 1,165 | UnwindData |  |
| 90 | `sqlite3_declare_vtab` | `0x9D820` | 687 | UnwindData |  |
| 91 | `sqlite3_deserialize` | `0x9DAE0` | 453 | UnwindData |  |
| 92 | `sqlite3_drop_modules` | `0x9DCB0` | 179 | UnwindData |  |
| 93 | `sqlite3_enable_shared_cache` | `0x9DD70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `sqlite3_errmsg16` | `0x9DD80` | 162 | UnwindData |  |
| 97 | `sqlite3_error_offset` | `0x9DE30` | 71 | UnwindData |  |
| 98 | `sqlite3_errstr` | `0x9DE80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `sqlite3_expanded_sql` | `0x9DE90` | 91 | UnwindData |  |
| 101 | `sqlite3_expired` | `0x9DF00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `sqlite3_extended_result_codes` | `0x9DF20` | 95 | UnwindData |  |
| 105 | `sqlite3_filename_database` | `0x9DF90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `sqlite3_filename_journal` | `0x9DFB0` | 81 | UnwindData |  |
| 107 | `sqlite3_filename_wal` | `0x9E010` | 42 | UnwindData |  |
| 111 | `sqlite3_free_table` | `0x9E040` | 87 | UnwindData |  |
| 113 | `sqlite3_get_auxdata` | `0x9E0A0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `sqlite3_get_table` | `0x9E160` | 458 | UnwindData |  |
| 116 | `sqlite3_hard_heap_limit64` | `0x9E490` | 110 | UnwindData |  |
| 118 | `sqlite3_interrupt` | `0x9E510` | 73 | UnwindData |  |
| 119 | `sqlite3_is_interrupted` | `0x9E560` | 77 | UnwindData |  |
| 120 | `sqlite3_key_v2` | `0x9E5C0` | 146 | UnwindData |  |
| 121 | `sqlite3_keyword_check` | `0x9E660` | 25 | UnwindData |  |
| 122 | `sqlite3_keyword_count` | `0x9E680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `sqlite3_keyword_name` | `0x9E690` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `sqlite3_libversion` | `0x9E6E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `sqlite3_libversion_number` | `0x9E6F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `sqlite3_limit` | `0x9E700` | 131 | UnwindData |  |
| 128 | `sqlite3_load_extension` | `0x9E790` | 103 | UnwindData |  |
| 135 | `sqlite3_msize` | `0x9E800` | 31 | UnwindData |  |
| 142 | `sqlite3_next_stmt` | `0x9E830` | 97 | UnwindData |  |
| 143 | `sqlite3_open` | `0x9E8A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `sqlite3_open16` | `0x9E8C0` | 220 | UnwindData |  |
| 147 | `sqlite3_prepare` | `0x9E9B0` | 39 | UnwindData |  |
| 148 | `sqlite3_prepare16` | `0x9E9E0` | 33 | UnwindData |  |
| 149 | `sqlite3_prepare16_v2` | `0x9EA10` | 36 | UnwindData |  |
| 150 | `sqlite3_prepare16_v3` | `0x9EA40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `sqlite3_prepare_v3` | `0x9EA60` | 50 | UnwindData |  |
| 153 | `sqlite3_profile` | `0x9EAA0` | 146 | UnwindData |  |
| 154 | `sqlite3_progress_handler` | `0x9EB40` | 152 | UnwindData |  |
| 156 | `sqlite3_realloc` | `0x9EBE0` | 60 | UnwindData |  |
| 158 | `sqlite3_rekey_v2` | `0x9EC30` | 620 | UnwindData |  |
| 161 | `sqlite3_reset_auto_extension` | `0x9EEB0` | 76 | UnwindData |  |
| 162 | `sqlite3_result_blob` | `0x9EF10` | 54 | UnwindData |  |
| 164 | `sqlite3_result_double` | `0x9EF50` | 23 | UnwindData |  |
| 165 | `sqlite3_result_error` | `0x9EF70` | 42 | UnwindData |  |
| 166 | `sqlite3_result_error16` | `0x9EFA0` | 42 | UnwindData |  |
| 167 | `sqlite3_result_error_code` | `0x9EFD0` | 72 | UnwindData |  |
| 168 | `sqlite3_result_error_nomem` | `0x9F020` | 47 | UnwindData |  |
| 170 | `sqlite3_result_int` | `0x9F060` | 26 | UnwindData |  |
| 172 | `sqlite3_result_null` | `0x9F080` | 23 | UnwindData |  |
| 173 | `sqlite3_result_pointer` | `0x9F0A0` | 106 | UnwindData |  |
| 174 | `sqlite3_result_subtype` | `0x9F110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `sqlite3_result_text16` | `0x9F130` | 27 | UnwindData |  |
| 178 | `sqlite3_result_text16le` | `0x9F130` | 27 | UnwindData |  |
| 177 | `sqlite3_result_text16be` | `0x9F160` | 27 | UnwindData |  |
| 179 | `sqlite3_result_text64` | `0x9F190` | 111 | UnwindData |  |
| 180 | `sqlite3_result_value` | `0x9F210` | 85 | UnwindData |  |
| 181 | `sqlite3_result_zeroblob` | `0x9F270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 182 | `sqlite3_result_zeroblob64` | `0x9F290` | 88 | UnwindData |  |
| 183 | `sqlite3_rollback_hook` | `0x9F2F0` | 126 | UnwindData |  |
| 184 | `sqlite3_serialize` | `0x9F380` | 639 | UnwindData |  |
| 185 | `sqlite3_set_authorizer` | `0x9F610` | 124 | UnwindData |  |
| 186 | `sqlite3_set_auxdata` | `0x9F6A0` | 230 | UnwindData |  |
| 187 | `sqlite3_set_last_insert_rowid` | `0x9F8D0` | 81 | UnwindData |  |
| 188 | `sqlite3_sleep` | `0x9F930` | 70 | UnwindData |  |
| 190 | `sqlite3_soft_heap_limit` | `0x9F980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 191 | `sqlite3_soft_heap_limit64` | `0x9F9A0` | 181 | UnwindData |  |
| 194 | `sqlite3_status` | `0x9FA60` | 103 | UnwindData |  |
| 197 | `sqlite3_stmt_busy` | `0x9FAD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 198 | `sqlite3_stmt_explain` | `0x9FAF0` | 310 | UnwindData |  |
| 200 | `sqlite3_stmt_readonly` | `0x9FC30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | `sqlite3_stmt_status` | `0x9FC50` | 179 | UnwindData |  |
| 206 | `sqlite3_str_errcode` | `0x9FD10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 207 | `sqlite3_str_finish` | `0x9FD30` | 63 | UnwindData |  |
| 208 | `sqlite3_str_length` | `0x9FD80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 209 | `sqlite3_str_new` | `0x9FDA0` | 80 | UnwindData |  |
| 211 | `sqlite3_str_value` | `0x9FE00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 213 | `sqlite3_strglob` | `0x9FE30` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 215 | `sqlite3_strlike` | `0x9FE70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 219 | `sqlite3_test_control` | `0x9FEA0` | 1,071 | UnwindData |  |
| 221 | `sqlite3_threadsafe` | `0xA02E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `sqlite3_total_changes` | `0xA02F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 223 | `sqlite3_total_changes64` | `0xA0300` | 56 | UnwindData |  |
| 224 | `sqlite3_trace` | `0xA0340` | 140 | UnwindData |  |
| 225 | `sqlite3_trace_v2` | `0xA03E0` | 142 | UnwindData |  |
| 226 | `sqlite3_transfer_bindings` | `0xA0480` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 227 | `sqlite3_txn_state` | `0xA04E0` | 194 | UnwindData |  |
| 229 | `sqlite3_update_hook` | `0xA05B0` | 126 | UnwindData |  |
| 231 | `sqlite3_uri_int64` | `0xA0640` | 56 | UnwindData |  |
| 232 | `sqlite3_uri_key` | `0xA0680` | 104 | UnwindData |  |
| 234 | `sqlite3_user_data` | `0xA06F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 237 | `sqlite3_value_bytes16` | `0xA0710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 240 | `sqlite3_value_encoding` | `0xA0720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 242 | `sqlite3_value_frombind` | `0xA0730` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 245 | `sqlite3_value_nochange` | `0xA0750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 246 | `sqlite3_value_numeric_type` | `0xA0770` | 66 | UnwindData |  |
| 247 | `sqlite3_value_pointer` | `0xA07C0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 248 | `sqlite3_value_subtype` | `0xA0820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 251 | `sqlite3_value_text16be` | `0xA0840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 259 | `sqlite3_vtab_collation` | `0xA0850` | 96 | UnwindData |  |
| 260 | `sqlite3_vtab_config` | `0xA08C0` | 210 | UnwindData |  |
| 261 | `sqlite3_vtab_distinct` | `0xA09A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 262 | `sqlite3_vtab_in` | `0xA09B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 263 | `sqlite3_vtab_in_first` | `0xA09F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 264 | `sqlite3_vtab_in_next` | `0xA0A00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 265 | `sqlite3_vtab_nochange` | `0xA0A20` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 266 | `sqlite3_vtab_on_conflict` | `0xA0A50` | 66 | UnwindData |  |
| 267 | `sqlite3_vtab_rhs_value` | `0xA0AA0` | 158 | UnwindData |  |
| 5 | `sqlite3VarintLen` | `0xAA630` | 31,472 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `sqlite3_cosine_similarity_extension_init` | `0xB2120` | 121 | UnwindData |  |
