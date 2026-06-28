# Binary Specification: e_sqlite3.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\udcdriver.inf_amd64_b155208a41961e18\EmbeddedPlugins\46C44A27-EAAD-4593-9AA0-8FA0F87BF955\Release\x64\e_sqlite3.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a6f505b285d9f5147d1797f1096b7750d0567b72bd193a6b61d800a719364e99`
* **Total Exported Functions:** 357

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 84 | `sqlite3_db_config` | `0x1300` | 18 | UnwindData |  |
| 106 | `sqlite3_extended_result_codes` | `0x1440` | 90 | UnwindData |  |
| 129 | `sqlite3_last_insert_rowid` | `0x14A0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 353 | `sqlite3session_memory_used` | `0x14A0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 204 | `sqlite3_set_last_insert_rowid` | `0x15F0` | 75 | UnwindData |  |
| 35 | `sqlite3_changes` | `0x1640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `sqlite3_changes64` | `0x1650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 247 | `sqlite3_total_changes` | `0x1660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 248 | `sqlite3_total_changes64` | `0x1670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `sqlite3_interrupt` | `0x1680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `sqlite3_is_interrupted` | `0x1690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `sqlite3_complete` | `0x16A0` | 1,410 | UnwindData |  |
| 67 | `sqlite3_complete16` | `0x1C30` | 22 | UnwindData |  |
| 32 | `sqlite3_busy_handler` | `0x1DD0` | 114 | UnwindData |  |
| 33 | `sqlite3_busy_timeout` | `0x1E50` | 140 | UnwindData |  |
| 205 | `sqlite3_setlk_timeout` | `0x1FD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `sqlite3_get_table` | `0x1FE0` | 800 | UnwindData |  |
| 114 | `sqlite3_free_table` | `0x2300` | 17 | UnwindData |  |
| 140 | `sqlite3_mprintf` | `0x2460` | 60 | UnwindData |  |
| 282 | `sqlite3_vmprintf` | `0x24A0` | 193 | UnwindData |  |
| 213 | `sqlite3_snprintf` | `0x2570` | 82 | UnwindData |  |
| 283 | `sqlite3_vsnprintf` | `0x25D0` | 75 | UnwindData |  |
| 135 | `sqlite3_malloc` | `0x2620` | 43 | UnwindData |  |
| 136 | `sqlite3_malloc64` | `0x2650` | 39 | UnwindData |  |
| 169 | `sqlite3_realloc` | `0x2680` | 65 | UnwindData |  |
| 170 | `sqlite3_realloc64` | `0x26D0` | 59 | UnwindData |  |
| 112 | `sqlite3_free` | `0x2710` | 150 | UnwindData |  |
| 141 | `sqlite3_msize` | `0x27B0` | 38 | UnwindData |  |
| 139 | `sqlite3_memory_used` | `0x27E0` | 80 | UnwindData |  |
| 138 | `sqlite3_memory_highwater` | `0x2830` | 110 | UnwindData |  |
| 168 | `sqlite3_randomness` | `0x28A0` | 28 | UnwindData |  |
| 201 | `sqlite3_set_authorizer` | `0x2A70` | 143 | UnwindData |  |
| 249 | `sqlite3_trace` | `0x2B00` | 132 | UnwindData |  |
| 166 | `sqlite3_profile` | `0x2CF0` | 139 | UnwindData |  |
| 250 | `sqlite3_trace_v2` | `0x2D90` | 136 | UnwindData |  |
| 167 | `sqlite3_progress_handler` | `0x2E30` | 133 | UnwindData |  |
| 148 | `sqlite3_open` | `0x3000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `sqlite3_open16` | `0x3010` | 34 | UnwindData |  |
| 150 | `sqlite3_open_v2` | `0x31C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 257 | `sqlite3_uri_parameter` | `0x31D0` | 34 | UnwindData |  |
| 254 | `sqlite3_uri_boolean` | `0x32A0` | 68 | UnwindData |  |
| 255 | `sqlite3_uri_int64` | `0x32F0` | 49 | UnwindData |  |
| 256 | `sqlite3_uri_key` | `0x3330` | 174 | UnwindData |  |
| 108 | `sqlite3_filename_database` | `0x33E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `sqlite3_filename_journal` | `0x3410` | 134 | UnwindData |  |
| 110 | `sqlite3_filename_wal` | `0x34A0` | 164 | UnwindData |  |
| 82 | `sqlite3_database_file_object` | `0x3560` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `sqlite3_create_filename` | `0x35A0` | 154 | UnwindData |  |
| 113 | `sqlite3_free_filename` | `0x37C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `sqlite3_errcode` | `0x3800` | 128 | UnwindData |  |
| 105 | `sqlite3_extended_errcode` | `0x3880` | 125 | UnwindData |  |
| 98 | `sqlite3_errmsg` | `0x3900` | 311 | UnwindData |  |
| 99 | `sqlite3_errmsg16` | `0x3A40` | 141 | UnwindData |  |
| 101 | `sqlite3_errstr` | `0x3BD0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `sqlite3_error_offset` | `0x3C20` | 139 | UnwindData |  |
| 132 | `sqlite3_limit` | `0x3DE0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `sqlite3_prepare` | `0x3E40` | 41 | UnwindData |  |
| 158 | `sqlite3_prepare_v2` | `0x3E70` | 44 | UnwindData |  |
| 159 | `sqlite3_prepare_v3` | `0x3EB0` | 52 | UnwindData |  |
| 155 | `sqlite3_prepare16` | `0x3FC0` | 32 | UnwindData |  |
| 156 | `sqlite3_prepare16_v2` | `0x3FE0` | 35 | UnwindData |  |
| 157 | `sqlite3_prepare16_v3` | `0x4010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 217 | `sqlite3_sql` | `0x4020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `sqlite3_expanded_sql` | `0x4030` | 14 | UnwindData |  |
| 224 | `sqlite3_stmt_readonly` | `0x40C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 223 | `sqlite3_stmt_isexplain` | `0x40E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `sqlite3_stmt_explain` | `0x4100` | 7 | UnwindData |  |
| 221 | `sqlite3_stmt_busy` | `0x4250` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `sqlite3_bind_blob` | `0x4270` | 204 | UnwindData |  |
| 11 | `sqlite3_bind_blob64` | `0x4340` | 204 | UnwindData |  |
| 12 | `sqlite3_bind_double` | `0x4410` | 112 | UnwindData |  |
| 13 | `sqlite3_bind_int` | `0x4480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `sqlite3_bind_int64` | `0x4490` | 137 | UnwindData |  |
| 15 | `sqlite3_bind_null` | `0x4520` | 64 | UnwindData |  |
| 20 | `sqlite3_bind_text` | `0x4560` | 32 | UnwindData |  |
| 21 | `sqlite3_bind_text16` | `0x4580` | 36 | UnwindData |  |
| 22 | `sqlite3_bind_text64` | `0x45B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `sqlite3_bind_value` | `0x45E0` | 65 | UnwindData |  |
| 19 | `sqlite3_bind_pointer` | `0x4700` | 196 | UnwindData |  |
| 24 | `sqlite3_bind_zeroblob` | `0x47D0` | 156 | UnwindData |  |
| 25 | `sqlite3_bind_zeroblob64` | `0x4870` | 152 | UnwindData |  |
| 16 | `sqlite3_bind_parameter_count` | `0x4910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `sqlite3_bind_parameter_name` | `0x4920` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `sqlite3_bind_parameter_index` | `0x4960` | 89 | UnwindData |  |
| 37 | `sqlite3_clear_bindings` | `0x49C0` | 9 | UnwindData |  |
| 45 | `sqlite3_column_count` | `0x4AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `sqlite3_column_name` | `0x4AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `sqlite3_column_name16` | `0x4AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `sqlite3_column_database_name` | `0x4AD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `sqlite3_column_database_name16` | `0x4AE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `sqlite3_column_table_name` | `0x4B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `sqlite3_column_table_name16` | `0x4B10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `sqlite3_column_origin_name` | `0x4B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `sqlite3_column_origin_name16` | `0x4B40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `sqlite3_column_decltype` | `0x4B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `sqlite3_column_decltype16` | `0x4B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 220 | `sqlite3_step` | `0x4B80` | 110 | UnwindData |  |
| 80 | `sqlite3_data_count` | `0x4DC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `sqlite3_column_blob` | `0x4DE0` | 206 | UnwindData |  |
| 50 | `sqlite3_column_double` | `0x4EB0` | 6 | UnwindData |  |
| 51 | `sqlite3_column_int` | `0x4FA0` | 289 | UnwindData |  |
| 52 | `sqlite3_column_int64` | `0x50D0` | 290 | UnwindData |  |
| 59 | `sqlite3_column_text` | `0x5200` | 252 | UnwindData |  |
| 60 | `sqlite3_column_text16` | `0x5300` | 252 | UnwindData |  |
| 62 | `sqlite3_column_value` | `0x5400` | 208 | UnwindData |  |
| 43 | `sqlite3_column_bytes` | `0x54D0` | 244 | UnwindData |  |
| 44 | `sqlite3_column_bytes16` | `0x55D0` | 257 | UnwindData |  |
| 61 | `sqlite3_column_type` | `0x56E0` | 225 | UnwindData |  |
| 111 | `sqlite3_finalize` | `0x57D0` | 232 | UnwindData |  |
| 174 | `sqlite3_reset` | `0x58C0` | 33 | UnwindData |  |
| 74 | `sqlite3_create_function` | `0x5990` | 79 | UnwindData |  |
| 75 | `sqlite3_create_function16` | `0x5A70` | 344 | UnwindData |  |
| 76 | `sqlite3_create_function_v2` | `0x5CB0` | 87 | UnwindData |  |
| 79 | `sqlite3_create_window_function` | `0x5D90` | 97 | UnwindData |  |
| 2 | `sqlite3_aggregate_count` | `0x5E00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `sqlite3_expired` | `0x5E10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 251 | `sqlite3_transfer_bindings` | `0x5E30` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 245 | `sqlite3_thread_cleanup` | `0x5E90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 259 | `sqlite3_value_blob` | `0x5EA0` | 118 | UnwindData |  |
| 262 | `sqlite3_value_double` | `0x5F20` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 267 | `sqlite3_value_int` | `0x5F50` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 268 | `sqlite3_value_int64` | `0x5F50` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 271 | `sqlite3_value_pointer` | `0x5FB0` | 72 | UnwindData |  |
| 273 | `sqlite3_value_text` | `0x6000` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 274 | `sqlite3_value_text16` | `0x6040` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 276 | `sqlite3_value_text16le` | `0x6040` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 275 | `sqlite3_value_text16be` | `0x6080` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 260 | `sqlite3_value_bytes` | `0x60C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 261 | `sqlite3_value_bytes16` | `0x6100` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 277 | `sqlite3_value_type` | `0x6140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 270 | `sqlite3_value_numeric_type` | `0x6160` | 65 | UnwindData |  |
| 269 | `sqlite3_value_nochange` | `0x61B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 266 | `sqlite3_value_frombind` | `0x61D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 264 | `sqlite3_value_encoding` | `0x61E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 272 | `sqlite3_value_subtype` | `0x61F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 263 | `sqlite3_value_dup` | `0x6210` | 386 | UnwindData |  |
| 265 | `sqlite3_value_free` | `0x63A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `sqlite3_aggregate_context` | `0x63B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 258 | `sqlite3_user_data` | `0x63D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `sqlite3_context_db_handle` | `0x63E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `sqlite3_get_auxdata` | `0x63F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | `sqlite3_set_auxdata` | `0x6430` | 269 | UnwindData |  |
| 117 | `sqlite3_get_clientdata` | `0x6540` | 173 | UnwindData |  |
| 203 | `sqlite3_set_clientdata` | `0x65F0` | 477 | UnwindData |  |
| 176 | `sqlite3_result_blob` | `0x67D0` | 22 | UnwindData |  |
| 177 | `sqlite3_result_blob64` | `0x67F0` | 106 | UnwindData |  |
| 178 | `sqlite3_result_double` | `0x6860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `sqlite3_result_error` | `0x6870` | 39 | UnwindData |  |
| 180 | `sqlite3_result_error16` | `0x68A0` | 39 | UnwindData |  |
| 183 | `sqlite3_result_error_toobig` | `0x68D0` | 50 | UnwindData |  |
| 182 | `sqlite3_result_error_nomem` | `0x6910` | 63 | UnwindData |  |
| 181 | `sqlite3_result_error_code` | `0x6950` | 146 | UnwindData |  |
| 184 | `sqlite3_result_int` | `0x69F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `sqlite3_result_int64` | `0x6A20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `sqlite3_result_null` | `0x6A40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 189 | `sqlite3_result_text` | `0x6A60` | 22 | UnwindData |  |
| 193 | `sqlite3_result_text64` | `0x6A80` | 146 | UnwindData |  |
| 190 | `sqlite3_result_text16` | `0x6B20` | 26 | UnwindData |  |
| 192 | `sqlite3_result_text16le` | `0x6B20` | 26 | UnwindData |  |
| 191 | `sqlite3_result_text16be` | `0x6B40` | 26 | UnwindData |  |
| 194 | `sqlite3_result_value` | `0x6B60` | 136 | UnwindData |  |
| 187 | `sqlite3_result_pointer` | `0x6BF0` | 141 | UnwindData |  |
| 195 | `sqlite3_result_zeroblob` | `0x6C80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 196 | `sqlite3_result_zeroblob64` | `0x6C90` | 153 | UnwindData |  |
| 188 | `sqlite3_result_subtype` | `0x6D30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `sqlite3_create_collation` | `0x6D40` | 33 | UnwindData |  |
| 72 | `sqlite3_create_collation_v2` | `0x6D70` | 163 | UnwindData |  |
| 71 | `sqlite3_create_collation16` | `0x6E20` | 295 | UnwindData |  |
| 40 | `sqlite3_collation_needed` | `0x6F50` | 111 | UnwindData |  |
| 41 | `sqlite3_collation_needed16` | `0x6FC0` | 111 | UnwindData |  |
| 207 | `sqlite3_sleep` | `0x7030` | 54 | UnwindData |  |
| 115 | `sqlite3_get_autocommit` | `0x7100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `sqlite3_db_handle` | `0x7110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `sqlite3_db_name` | `0x7120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `sqlite3_db_filename` | `0x7140` | 104 | UnwindData |  |
| 89 | `sqlite3_db_readonly` | `0x71B0` | 73 | UnwindData |  |
| 252 | `sqlite3_txn_state` | `0x7200` | 185 | UnwindData |  |
| 147 | `sqlite3_next_stmt` | `0x72C0` | 89 | UnwindData |  |
| 63 | `sqlite3_commit_hook` | `0x7320` | 118 | UnwindData |  |
| 197 | `sqlite3_rollback_hook` | `0x73A0` | 118 | UnwindData |  |
| 4 | `sqlite3_autovacuum_pages` | `0x7420` | 145 | UnwindData |  |
| 253 | `sqlite3_update_hook` | `0x74C0` | 118 | UnwindData |  |
| 96 | `sqlite3_enable_shared_cache` | `0x7540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `sqlite3_global_recover` | `0x7550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `sqlite3_memory_alarm` | `0x7550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 173 | `sqlite3_release_memory` | `0x7550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `sqlite3_db_release_memory` | `0x7560` | 4 | UnwindData |  |
| 215 | `sqlite3_soft_heap_limit64` | `0x7630` | 38 | UnwindData |  |
| 120 | `sqlite3_hard_heap_limit64` | `0x7710` | 143 | UnwindData |  |
| 214 | `sqlite3_soft_heap_limit` | `0x77A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 242 | `sqlite3_table_column_metadata` | `0x77B0` | 994 | UnwindData |  |
| 133 | `sqlite3_load_extension` | `0x7BA0` | 142 | UnwindData |  |
| 3 | `sqlite3_auto_extension` | `0x7C30` | 28 | UnwindData |  |
| 34 | `sqlite3_cancel_auto_extension` | `0x7D30` | 17 | UnwindData |  |
| 175 | `sqlite3_reset_auto_extension` | `0x7DF0` | 69 | UnwindData |  |
| 77 | `sqlite3_create_module` | `0x7EC0` | 152 | UnwindData |  |
| 78 | `sqlite3_create_module_v2` | `0x7F60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `sqlite3_drop_modules` | `0x7F70` | 30 | UnwindData |  |
| 92 | `sqlite3_declare_vtab` | `0x8070` | 142 | UnwindData |  |
| 153 | `sqlite3_overload_function` | `0x8490` | 229 | UnwindData |  |
| 28 | `sqlite3_blob_open` | `0x8580` | 2,192 | UnwindData |  |
| 30 | `sqlite3_blob_reopen` | `0x8E10` | 79 | UnwindData |  |
| 27 | `sqlite3_blob_close` | `0x8F80` | 18 | UnwindData |  |
| 26 | `sqlite3_blob_bytes` | `0x9060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `sqlite3_blob_read` | `0x9080` | 26 | UnwindData |  |
| 31 | `sqlite3_blob_write` | `0x90A0` | 26 | UnwindData |  |
| 279 | `sqlite3_vfs_find` | `0x90C0` | 177 | UnwindData |  |
| 280 | `sqlite3_vfs_register` | `0x9180` | 34 | UnwindData |  |
| 281 | `sqlite3_vfs_unregister` | `0x9270` | 28 | UnwindData |  |
| 142 | `sqlite3_mutex_alloc` | `0x9340` | 60 | UnwindData |  |
| 144 | `sqlite3_mutex_free` | `0x9380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `sqlite3_mutex_enter` | `0x93A0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `sqlite3_mutex_try` | `0x9410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `sqlite3_mutex_leave` | `0x9430` | 1,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `sqlite3_db_mutex` | `0x9950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `sqlite3_file_control` | `0x9960` | 6 | UnwindData |  |
| 244 | `sqlite3_test_control` | `0x9B50` | 796 | UnwindData |  |
| 127 | `sqlite3_keyword_count` | `0xA050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `sqlite3_keyword_name` | `0xA060` | 736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `sqlite3_keyword_check` | `0xA340` | 49 | UnwindData |  |
| 233 | `sqlite3_str_new` | `0xA380` | 92 | UnwindData |  |
| 231 | `sqlite3_str_finish` | `0xA3E0` | 30 | UnwindData |  |
| 229 | `sqlite3_str_appendf` | `0xA450` | 34 | UnwindData |  |
| 236 | `sqlite3_str_vappendf` | `0xA480` | 108 | UnwindData |  |
| 226 | `sqlite3_str_append` | `0xC040` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 227 | `sqlite3_str_appendall` | `0xC070` | 106 | UnwindData |  |
| 228 | `sqlite3_str_appendchar` | `0xC0E0` | 95 | UnwindData |  |
| 234 | `sqlite3_str_reset` | `0xC140` | 153 | UnwindData |  |
| 230 | `sqlite3_str_errcode` | `0xC1E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 232 | `sqlite3_str_length` | `0xC1F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 235 | `sqlite3_str_value` | `0xC200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 218 | `sqlite3_status` | `0xC220` | 28 | UnwindData |  |
| 219 | `sqlite3_status64` | `0xC330` | 28 | UnwindData |  |
| 91 | `sqlite3_db_status` | `0xDAA0` | 23 | UnwindData |  |
| 225 | `sqlite3_stmt_status` | `0xF450` | 18 | UnwindData |  |
| 6 | `sqlite3_backup_init` | `0xF510` | 6 | UnwindData |  |
| 9 | `sqlite3_backup_step` | `0xF680` | 10 | UnwindData |  |
| 5 | `sqlite3_backup_finish` | `0xFE80` | 314 | UnwindData |  |
| 8 | `sqlite3_backup_remaining` | `0xFFD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `sqlite3_backup_pagecount` | `0xFFE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 238 | `sqlite3_stricmp` | `0x10000` | 1,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 240 | `sqlite3_strnicmp` | `0x105B0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 237 | `sqlite3_strglob` | `0x10620` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 239 | `sqlite3_strlike` | `0x10650` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `sqlite3_log` | `0x10680` | 202 | UnwindData |  |
| 296 | `sqlite3_wal_hook` | `0x10750` | 118 | UnwindData |  |
| 293 | `sqlite3_wal_autocheckpoint` | `0x107D0` | 121 | UnwindData |  |
| 294 | `sqlite3_wal_checkpoint` | `0x10850` | 29 | UnwindData |  |
| 295 | `sqlite3_wal_checkpoint_v2` | `0x10870` | 364 | UnwindData |  |
| 285 | `sqlite3_vtab_config` | `0x109E0` | 222 | UnwindData |  |
| 291 | `sqlite3_vtab_on_conflict` | `0x10AD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 290 | `sqlite3_vtab_nochange` | `0x10AF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 284 | `sqlite3_vtab_collation` | `0x10B10` | 133 | UnwindData |  |
| 286 | `sqlite3_vtab_distinct` | `0x10BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 287 | `sqlite3_vtab_in` | `0x10BB0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 288 | `sqlite3_vtab_in_first` | `0x10BF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 289 | `sqlite3_vtab_in_next` | `0x10C00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 292 | `sqlite3_vtab_rhs_value` | `0x10C10` | 34 | UnwindData |  |
| 83 | `sqlite3_db_cacheflush` | `0x10D20` | 299 | UnwindData |  |
| 241 | `sqlite3_system_errno` | `0x10E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 200 | `sqlite3_serialize` | `0x10E60` | 1,025 | UnwindData |  |
| 93 | `sqlite3_deserialize` | `0x11A40` | 15 | UnwindData |  |
| 130 | `sqlite3_libversion` | `0x2C750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 216 | `sqlite3_sourceid` | `0x2C760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `sqlite3_libversion_number` | `0x2C770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `sqlite3_compileoption_used` | `0x2C780` | 370 | UnwindData |  |
| 64 | `sqlite3_compileoption_get` | `0x2C900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `sqlite3_key` | `0x2C920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `sqlite3_key_v2` | `0x2C920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 171 | `sqlite3_rekey` | `0x2C920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 172 | `sqlite3_rekey_v2` | `0x2C920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 246 | `sqlite3_threadsafe` | `0x2C920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 297 | `sqlite3_win32_is_nt` | `0x2C920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `sqlite3_close` | `0x2C930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `sqlite3_close_v2` | `0x2C940` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `sqlite3_exec` | `0x2CAD0` | 162 | UnwindData |  |
| 209 | `sqlite3_snapshot_free` | `0x67FC0` | 376,208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 161 | `sqlite3_preupdate_count` | `0xC3D50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 162 | `sqlite3_preupdate_depth` | `0xC3D70` | 508,896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `sqlite3_config` | `0x140150` | 110 | UnwindData |  |
| 95 | `sqlite3_enable_load_extension` | `0x140620` | 102 | UnwindData |  |
| 121 | `sqlite3_initialize` | `0x140A70` | 41 | UnwindData |  |
| 151 | `sqlite3_os_end` | `0x140ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `sqlite3_os_init` | `0x140EE0` | 21 | UnwindData |  |
| 160 | `sqlite3_preupdate_blobwrite` | `0x141290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 163 | `sqlite3_preupdate_hook` | `0x1412B0` | 118 | UnwindData |  |
| 164 | `sqlite3_preupdate_new` | `0x141330` | 7 | UnwindData |  |
| 165 | `sqlite3_preupdate_old` | `0x1415C0` | 12 | UnwindData |  |
| 198 | `sqlite3_rtree_geometry_callback` | `0x1419D0` | 176 | UnwindData |  |
| 199 | `sqlite3_rtree_query_callback` | `0x141A80` | 206 | UnwindData |  |
| 206 | `sqlite3_shutdown` | `0x141B50` | 183 | UnwindData |  |
| 208 | `sqlite3_snapshot_cmp` | `0x141C10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 210 | `sqlite3_snapshot_get` | `0x141C40` | 6 | UnwindData |  |
| 211 | `sqlite3_snapshot_open` | `0x141DD0` | 6 | UnwindData |  |
| 212 | `sqlite3_snapshot_recover` | `0x141FA0` | 206 | UnwindData |  |
| 298 | `sqlite3_win32_mbcs_to_utf8` | `0x142070` | 54 | UnwindData |  |
| 299 | `sqlite3_win32_mbcs_to_utf8_v2` | `0x1420B0` | 57 | UnwindData |  |
| 300 | `sqlite3_win32_set_directory` | `0x1420F0` | 116 | UnwindData |  |
| 301 | `sqlite3_win32_set_directory16` | `0x1420F0` | 116 | UnwindData |  |
| 302 | `sqlite3_win32_set_directory8` | `0x142170` | 75 | UnwindData |  |
| 303 | `sqlite3_win32_sleep` | `0x142270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 304 | `sqlite3_win32_unicode_to_utf8` | `0x142280` | 39 | UnwindData |  |
| 305 | `sqlite3_win32_utf8_to_mbcs` | `0x1422B0` | 54 | UnwindData |  |
| 306 | `sqlite3_win32_utf8_to_mbcs_v2` | `0x1422F0` | 57 | UnwindData |  |
| 307 | `sqlite3_win32_utf8_to_unicode` | `0x142330` | 39 | UnwindData |  |
| 308 | `sqlite3_win32_write_debug` | `0x142360` | 144 | UnwindData |  |
| 309 | `sqlite3changegroup_add` | `0x1423F0` | 175 | UnwindData |  |
| 310 | `sqlite3changegroup_add_change` | `0x1424A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 311 | `sqlite3changegroup_add_strm` | `0x1424D0` | 180 | UnwindData |  |
| 312 | `sqlite3changegroup_delete` | `0x142590` | 18 | UnwindData |  |
| 313 | `sqlite3changegroup_new` | `0x142680` | 88 | UnwindData |  |
| 338 | `sqlite3rebaser_create` | `0x142680` | 88 | UnwindData |  |
| 314 | `sqlite3changegroup_output` | `0x1426E0` | 27 | UnwindData |  |
| 315 | `sqlite3changegroup_output_strm` | `0x142700` | 26 | UnwindData |  |
| 316 | `sqlite3changegroup_schema` | `0x142720` | 103 | UnwindData |  |
| 317 | `sqlite3changeset_apply` | `0x142790` | 56 | UnwindData |  |
| 318 | `sqlite3changeset_apply_strm` | `0x1427D0` | 56 | UnwindData |  |
| 319 | `sqlite3changeset_apply_v2` | `0x142810` | 254 | UnwindData |  |
| 320 | `sqlite3changeset_apply_v2_strm` | `0x142910` | 256 | UnwindData |  |
| 321 | `sqlite3changeset_concat` | `0x142A10` | 210 | UnwindData |  |
| 322 | `sqlite3changeset_concat_strm` | `0x142AF0` | 211 | UnwindData |  |
| 323 | `sqlite3changeset_conflict` | `0x142BD0` | 68 | UnwindData |  |
| 324 | `sqlite3changeset_finalize` | `0x142C20` | 24 | UnwindData |  |
| 325 | `sqlite3changeset_fk_conflicts` | `0x142E20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 326 | `sqlite3changeset_invert` | `0x142E40` | 81 | UnwindData |  |
| 327 | `sqlite3changeset_invert_strm` | `0x142EA0` | 103 | UnwindData |  |
| 328 | `sqlite3changeset_new` | `0x142F10` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 329 | `sqlite3changeset_next` | `0x142F50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 330 | `sqlite3changeset_old` | `0x142F60` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 331 | `sqlite3changeset_op` | `0x142FA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 332 | `sqlite3changeset_pk` | `0x142FD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 333 | `sqlite3changeset_start` | `0x142FF0` | 160 | UnwindData |  |
| 334 | `sqlite3changeset_start_strm` | `0x143090` | 164 | UnwindData |  |
| 335 | `sqlite3changeset_start_v2` | `0x143140` | 47 | UnwindData |  |
| 336 | `sqlite3changeset_start_v2_strm` | `0x143170` | 40 | UnwindData |  |
| 337 | `sqlite3rebaser_configure` | `0x1431A0` | 178 | UnwindData |  |
| 339 | `sqlite3rebaser_delete` | `0x143260` | 15 | UnwindData |  |
| 340 | `sqlite3rebaser_rebase` | `0x143340` | 210 | UnwindData |  |
| 341 | `sqlite3rebaser_rebase_strm` | `0x143420` | 213 | UnwindData |  |
| 342 | `sqlite3session_attach` | `0x143500` | 12 | UnwindData |  |
| 343 | `sqlite3session_changeset` | `0x1436A0` | 52 | UnwindData |  |
| 344 | `sqlite3session_changeset_size` | `0x1436E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 345 | `sqlite3session_changeset_strm` | `0x1436F0` | 49 | UnwindData |  |
| 346 | `sqlite3session_config` | `0x143730` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 347 | `sqlite3session_create` | `0x143760` | 396 | UnwindData |  |
| 348 | `sqlite3session_delete` | `0x1438F0` | 6 | UnwindData |  |
| 349 | `sqlite3session_diff` | `0x143C40` | 69 | UnwindData |  |
| 350 | `sqlite3session_enable` | `0x1443C0` | 91 | UnwindData |  |
| 351 | `sqlite3session_indirect` | `0x144420` | 91 | UnwindData |  |
| 352 | `sqlite3session_isempty` | `0x144480` | 108 | UnwindData |  |
| 354 | `sqlite3session_object_config` | `0x1444F0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 355 | `sqlite3session_patchset` | `0x144570` | 55 | UnwindData |  |
| 356 | `sqlite3session_patchset_strm` | `0x1445B0` | 52 | UnwindData |  |
| 357 | `sqlite3session_table_filter` | `0x1445F0` | 253,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 278 | `sqlite3_version` | `0x1825F0` | 264,160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 243 | `sqlite3_temp_directory` | `0x1C2DD0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `sqlite3_data_directory` | `0x1C2DD8` | 0 | Indeterminate |  |
