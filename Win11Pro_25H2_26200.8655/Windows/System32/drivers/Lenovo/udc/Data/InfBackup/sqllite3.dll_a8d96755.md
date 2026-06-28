# Binary Specification: sqllite3.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\drivers\Lenovo\udc\Data\InfBackup\sqllite3.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a8d96755d9d2d66bb9925fdd59190795b41cdd7f5d55531d305ded6e5f2d2831`
* **Total Exported Functions:** 287

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 225 | `sqlite3_threadsafe` | `0x1000` | 8,816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 276 | `sqlite3_win32_is_nt` | `0x1000` | 8,816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 198 | `sqlite3_status64` | `0x3270` | 28 | UnwindData |  |
| 197 | `sqlite3_status` | `0x3350` | 28 | UnwindData |  |
| 86 | `sqlite3_db_status64` | `0x3450` | 26 | UnwindData |  |
| 85 | `sqlite3_db_status` | `0x3A60` | 86 | UnwindData |  |
| 258 | `sqlite3_vfs_find` | `0x71F0` | 177 | UnwindData |  |
| 259 | `sqlite3_vfs_register` | `0x72B0` | 34 | UnwindData |  |
| 260 | `sqlite3_vfs_unregister` | `0x7390` | 28 | UnwindData |  |
| 114 | `sqlite3_global_recover` | `0x7510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | `sqlite3_memory_alarm` | `0x7510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 158 | `sqlite3_release_memory` | `0x7510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 224 | `sqlite3_thread_cleanup` | `0x7520` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `sqlite3_mutex_alloc` | `0x75C0` | 51 | UnwindData |  |
| 137 | `sqlite3_mutex_free` | `0x7600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `sqlite3_mutex_enter` | `0x7610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `sqlite3_mutex_try` | `0x7620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `sqlite3_mutex_leave` | `0x7630` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 194 | `sqlite3_soft_heap_limit64` | `0x7830` | 217 | UnwindData |  |
| 193 | `sqlite3_soft_heap_limit` | `0x7910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `sqlite3_hard_heap_limit64` | `0x7920` | 129 | UnwindData |  |
| 132 | `sqlite3_memory_used` | `0x79B0` | 66 | UnwindData |  |
| 131 | `sqlite3_memory_highwater` | `0x7A00` | 98 | UnwindData |  |
| 128 | `sqlite3_malloc` | `0x7BE0` | 43 | UnwindData |  |
| 129 | `sqlite3_malloc64` | `0x7C10` | 39 | UnwindData |  |
| 134 | `sqlite3_msize` | `0x7C40` | 31 | UnwindData |  |
| 107 | `sqlite3_free` | `0x7C60` | 111 | UnwindData |  |
| 156 | `sqlite3_realloc` | `0x7FD0` | 65 | UnwindData |  |
| 157 | `sqlite3_realloc64` | `0x8020` | 59 | UnwindData |  |
| 215 | `sqlite3_str_vappendf` | `0x8870` | 116 | UnwindData |  |
| 207 | `sqlite3_str_appendchar` | `0xA6F0` | 95 | UnwindData |  |
| 205 | `sqlite3_str_append` | `0xA7A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | `sqlite3_str_appendall` | `0xA7D0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 210 | `sqlite3_str_finish` | `0xA930` | 30 | UnwindData |  |
| 209 | `sqlite3_str_errcode` | `0xA9A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 211 | `sqlite3_str_length` | `0xA9B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 214 | `sqlite3_str_value` | `0xA9C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 213 | `sqlite3_str_reset` | `0xA9E0` | 144 | UnwindData |  |
| 212 | `sqlite3_str_new` | `0xAA70` | 90 | UnwindData |  |
| 261 | `sqlite3_vmprintf` | `0xABD0` | 193 | UnwindData |  |
| 133 | `sqlite3_mprintf` | `0xACA0` | 60 | UnwindData |  |
| 262 | `sqlite3_vsnprintf` | `0xACE0` | 103 | UnwindData |  |
| 192 | `sqlite3_snprintf` | `0xAD50` | 110 | UnwindData |  |
| 127 | `sqlite3_log` | `0xADC0` | 195 | UnwindData |  |
| 208 | `sqlite3_str_appendf` | `0xAE90` | 34 | UnwindData |  |
| 155 | `sqlite3_randomness` | `0xB1E0` | 34 | UnwindData |  |
| 217 | `sqlite3_stricmp` | `0xC020` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 219 | `sqlite3_strnicmp` | `0xC0B0` | 11,008 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 287 | `sqlite3_win32_write_debug` | `0xEBB0` | 133 | UnwindData |  |
| 282 | `sqlite3_win32_sleep` | `0xEC40` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 286 | `sqlite3_win32_utf8_to_unicode` | `0xEF90` | 39 | UnwindData |  |
| 283 | `sqlite3_win32_unicode_to_utf8` | `0xEFC0` | 39 | UnwindData |  |
| 277 | `sqlite3_win32_mbcs_to_utf8` | `0xEFF0` | 47 | UnwindData |  |
| 278 | `sqlite3_win32_mbcs_to_utf8_v2` | `0xF020` | 57 | UnwindData |  |
| 284 | `sqlite3_win32_utf8_to_mbcs` | `0xF060` | 47 | UnwindData |  |
| 285 | `sqlite3_win32_utf8_to_mbcs_v2` | `0xF090` | 57 | UnwindData |  |
| 281 | `sqlite3_win32_set_directory8` | `0xF0D0` | 59 | UnwindData |  |
| 280 | `sqlite3_win32_set_directory16` | `0xF1B0` | 116 | UnwindData |  |
| 279 | `sqlite3_win32_set_directory` | `0xF230` | 15,136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `sqlite3_os_init` | `0x12D50` | 7 | UnwindData |  |
| 144 | `sqlite3_os_end` | `0x13090` | 2,896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `sqlite3_serialize` | `0x13BE0` | 319 | UnwindData |  |
| 88 | `sqlite3_deserialize` | `0x13ED0` | 8 | UnwindData |  |
| 7 | `sqlite3_backup_pagecount` | `0x15BD0` | 17,264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `sqlite3_database_file_object` | `0x19F40` | 25,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `sqlite3_enable_shared_cache` | `0x204A0` | 62,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `sqlite3_backup_init` | `0x2F9B0` | 6 | UnwindData |  |
| 9 | `sqlite3_backup_step` | `0x2FD00` | 25 | UnwindData |  |
| 5 | `sqlite3_backup_finish` | `0x30480` | 298 | UnwindData |  |
| 8 | `sqlite3_backup_remaining` | `0x305B0` | 3,136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 246 | `sqlite3_value_int` | `0x311F0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 247 | `sqlite3_value_int64` | `0x311F0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 241 | `sqlite3_value_double` | `0x31280` | 31,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `sqlite3_expired` | `0x38CD0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `sqlite3_finalize` | `0x38DD0` | 219 | UnwindData |  |
| 159 | `sqlite3_reset` | `0x38EB0` | 33 | UnwindData |  |
| 37 | `sqlite3_clear_bindings` | `0x38F70` | 9 | UnwindData |  |
| 238 | `sqlite3_value_blob` | `0x39040` | 191 | UnwindData |  |
| 239 | `sqlite3_value_bytes` | `0x39100` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 240 | `sqlite3_value_bytes16` | `0x39140` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 251 | `sqlite3_value_subtype` | `0x39180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 250 | `sqlite3_value_pointer` | `0x391A0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 252 | `sqlite3_value_text` | `0x391F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 253 | `sqlite3_value_text16` | `0x39230` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 255 | `sqlite3_value_text16le` | `0x39230` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 254 | `sqlite3_value_text16be` | `0x39270` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 256 | `sqlite3_value_type` | `0x392B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 243 | `sqlite3_value_encoding` | `0x392D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 248 | `sqlite3_value_nochange` | `0x392E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 245 | `sqlite3_value_frombind` | `0x39300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 242 | `sqlite3_value_dup` | `0x39310` | 217 | UnwindData |  |
| 244 | `sqlite3_value_free` | `0x393F0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 161 | `sqlite3_result_blob` | `0x394E0` | 22 | UnwindData |  |
| 162 | `sqlite3_result_blob64` | `0x39500` | 100 | UnwindData |  |
| 163 | `sqlite3_result_double` | `0x39570` | 121 | UnwindData |  |
| 164 | `sqlite3_result_error` | `0x395F0` | 39 | UnwindData |  |
| 165 | `sqlite3_result_error16` | `0x39620` | 39 | UnwindData |  |
| 169 | `sqlite3_result_int` | `0x39650` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 170 | `sqlite3_result_int64` | `0x39680` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 171 | `sqlite3_result_null` | `0x396B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 172 | `sqlite3_result_pointer` | `0x396D0` | 147 | UnwindData |  |
| 173 | `sqlite3_result_subtype` | `0x39770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 174 | `sqlite3_result_text` | `0x39780` | 22 | UnwindData |  |
| 178 | `sqlite3_result_text64` | `0x397A0` | 140 | UnwindData |  |
| 175 | `sqlite3_result_text16` | `0x39830` | 26 | UnwindData |  |
| 177 | `sqlite3_result_text16le` | `0x39830` | 26 | UnwindData |  |
| 176 | `sqlite3_result_text16be` | `0x39850` | 26 | UnwindData |  |
| 179 | `sqlite3_result_value` | `0x39870` | 138 | UnwindData |  |
| 180 | `sqlite3_result_zeroblob` | `0x39900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `sqlite3_result_zeroblob64` | `0x39910` | 153 | UnwindData |  |
| 166 | `sqlite3_result_error_code` | `0x399B0` | 146 | UnwindData |  |
| 168 | `sqlite3_result_error_toobig` | `0x39A50` | 50 | UnwindData |  |
| 167 | `sqlite3_result_error_nomem` | `0x39A90` | 66 | UnwindData |  |
| 199 | `sqlite3_step` | `0x39D70` | 109 | UnwindData |  |
| 237 | `sqlite3_user_data` | `0x39F70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `sqlite3_context_db_handle` | `0x39F80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 269 | `sqlite3_vtab_nochange` | `0x39F90` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 267 | `sqlite3_vtab_in_first` | `0x3A290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 268 | `sqlite3_vtab_in_next` | `0x3A2A0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `sqlite3_aggregate_context` | `0x3A390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `sqlite3_get_auxdata` | `0x3A3B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `sqlite3_set_auxdata` | `0x3A3F0` | 233 | UnwindData |  |
| 2 | `sqlite3_aggregate_count` | `0x3A4E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `sqlite3_column_count` | `0x3A4F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `sqlite3_data_count` | `0x3A500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `sqlite3_column_blob` | `0x3A520` | 192 | UnwindData |  |
| 43 | `sqlite3_column_bytes` | `0x3A5E0` | 230 | UnwindData |  |
| 44 | `sqlite3_column_bytes16` | `0x3A6D0` | 243 | UnwindData |  |
| 48 | `sqlite3_column_double` | `0x3A7D0` | 6 | UnwindData |  |
| 49 | `sqlite3_column_int` | `0x3A8C0` | 275 | UnwindData |  |
| 50 | `sqlite3_column_int64` | `0x3A9E0` | 276 | UnwindData |  |
| 53 | `sqlite3_column_text` | `0x3AB00` | 238 | UnwindData |  |
| 56 | `sqlite3_column_value` | `0x3ABF0` | 203 | UnwindData |  |
| 54 | `sqlite3_column_text16` | `0x3ACC0` | 238 | UnwindData |  |
| 55 | `sqlite3_column_type` | `0x3ADB0` | 211 | UnwindData |  |
| 51 | `sqlite3_column_name` | `0x3B060` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `sqlite3_column_name16` | `0x3B070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `sqlite3_column_decltype` | `0x3B080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `sqlite3_column_decltype16` | `0x3B090` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `sqlite3_bind_blob` | `0x3B380` | 205 | UnwindData |  |
| 11 | `sqlite3_bind_blob64` | `0x3B450` | 205 | UnwindData |  |
| 12 | `sqlite3_bind_double` | `0x3B520` | 190 | UnwindData |  |
| 13 | `sqlite3_bind_int` | `0x3B5E0` | 133 | UnwindData |  |
| 14 | `sqlite3_bind_int64` | `0x3B670` | 133 | UnwindData |  |
| 15 | `sqlite3_bind_null` | `0x3B700` | 57 | UnwindData |  |
| 19 | `sqlite3_bind_pointer` | `0x3B740` | 194 | UnwindData |  |
| 20 | `sqlite3_bind_text` | `0x3B810` | 32 | UnwindData |  |
| 22 | `sqlite3_bind_text64` | `0x3B830` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `sqlite3_bind_text16` | `0x3B860` | 36 | UnwindData |  |
| 23 | `sqlite3_bind_value` | `0x3B890` | 286 | UnwindData |  |
| 24 | `sqlite3_bind_zeroblob` | `0x3BA30` | 152 | UnwindData |  |
| 25 | `sqlite3_bind_zeroblob64` | `0x3BAD0` | 141 | UnwindData |  |
| 16 | `sqlite3_bind_parameter_count` | `0x3BB60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `sqlite3_bind_parameter_name` | `0x3BB70` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `sqlite3_bind_parameter_index` | `0x3BBB0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 230 | `sqlite3_transfer_bindings` | `0x3BD00` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `sqlite3_db_handle` | `0x3BD50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 203 | `sqlite3_stmt_readonly` | `0x3BD60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | `sqlite3_stmt_isexplain` | `0x3BD80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | `sqlite3_stmt_explain` | `0x3BDA0` | 7 | UnwindData |  |
| 200 | `sqlite3_stmt_busy` | `0x3BEE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `sqlite3_next_stmt` | `0x3BF00` | 75 | UnwindData |  |
| 204 | `sqlite3_stmt_status` | `0x3BF50` | 33 | UnwindData |  |
| 196 | `sqlite3_sql` | `0x3C030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `sqlite3_expanded_sql` | `0x3C040` | 14 | UnwindData |  |
| 249 | `sqlite3_value_numeric_type` | `0x3CA10` | 272 | UnwindData |  |
| 28 | `sqlite3_blob_open` | `0x441F0` | 2,116 | UnwindData |  |
| 27 | `sqlite3_blob_close` | `0x44A40` | 18 | UnwindData |  |
| 29 | `sqlite3_blob_read` | `0x44CB0` | 26 | UnwindData |  |
| 31 | `sqlite3_blob_write` | `0x44CD0` | 26 | UnwindData |  |
| 26 | `sqlite3_blob_bytes` | `0x44CF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `sqlite3_blob_reopen` | `0x44D10` | 75 | UnwindData |  |
| 184 | `sqlite3_set_authorizer` | `0x63250` | 136 | UnwindData |  |
| 216 | `sqlite3_strglob` | `0x74EC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 218 | `sqlite3_strlike` | `0x74EF0` | 60,624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `sqlite3_exec` | `0x83BC0` | 152 | UnwindData |  |
| 126 | `sqlite3_load_extension` | `0x846D0` | 128 | UnwindData |  |
| 90 | `sqlite3_enable_load_extension` | `0x84750` | 88 | UnwindData |  |
| 3 | `sqlite3_auto_extension` | `0x847B0` | 28 | UnwindData |  |
| 34 | `sqlite3_cancel_auto_extension` | `0x848A0` | 159 | UnwindData |  |
| 160 | `sqlite3_reset_auto_extension` | `0x84940` | 62 | UnwindData |  |
| 147 | `sqlite3_prepare` | `0x8DFE0` | 41 | UnwindData |  |
| 151 | `sqlite3_prepare_v2` | `0x8E010` | 44 | UnwindData |  |
| 152 | `sqlite3_prepare_v3` | `0x8E040` | 52 | UnwindData |  |
| 148 | `sqlite3_prepare16` | `0x8E360` | 32 | UnwindData |  |
| 149 | `sqlite3_prepare16_v2` | `0x8E380` | 35 | UnwindData |  |
| 150 | `sqlite3_prepare16_v3` | `0x8E3B0` | 74,208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `sqlite3_get_table` | `0xA0590` | 408 | UnwindData |  |
| 109 | `sqlite3_free_table` | `0xA0730` | 17 | UnwindData |  |
| 71 | `sqlite3_create_module` | `0xA91C0` | 138 | UnwindData |  |
| 72 | `sqlite3_create_module_v2` | `0xA9250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `sqlite3_drop_modules` | `0xA9260` | 37 | UnwindData |  |
| 87 | `sqlite3_declare_vtab` | `0xAA4F0` | 143 | UnwindData |  |
| 270 | `sqlite3_vtab_on_conflict` | `0xAB210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 264 | `sqlite3_vtab_config` | `0xAB230` | 208 | UnwindData |  |
| 263 | `sqlite3_vtab_collation` | `0xBAC70` | 31 | UnwindData |  |
| 266 | `sqlite3_vtab_in` | `0xBAD90` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 271 | `sqlite3_vtab_rhs_value` | `0xBADD0` | 34 | UnwindData |  |
| 265 | `sqlite3_vtab_distinct` | `0xBAEE0` | 67,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `sqlite3_keyword_name` | `0xCB5D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `sqlite3_keyword_count` | `0xCB610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `sqlite3_keyword_check` | `0xCB620` | 49 | UnwindData |  |
| 60 | `sqlite3_complete` | `0xCC390` | 1,398 | UnwindData |  |
| 61 | `sqlite3_complete16` | `0xCC910` | 25 | UnwindData |  |
| 123 | `sqlite3_libversion` | `0xCC9F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `sqlite3_libversion_number` | `0xCCA00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `sqlite3_initialize` | `0xCCA10` | 40 | UnwindData |  |
| 190 | `sqlite3_shutdown` | `0xCCF50` | 171 | UnwindData |  |
| 62 | `sqlite3_config` | `0xCD000` | 110 | UnwindData |  |
| 81 | `sqlite3_db_mutex` | `0xCD7D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `sqlite3_db_release_memory` | `0xCD7E0` | 4 | UnwindData |  |
| 77 | `sqlite3_db_cacheflush` | `0xCD890` | 328 | UnwindData |  |
| 78 | `sqlite3_db_config` | `0xCD9E0` | 18 | UnwindData |  |
| 122 | `sqlite3_last_insert_rowid` | `0xCDCA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 188 | `sqlite3_set_last_insert_rowid` | `0xCDCB0` | 61 | UnwindData |  |
| 36 | `sqlite3_changes64` | `0xCDCF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `sqlite3_changes` | `0xCDD00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 227 | `sqlite3_total_changes64` | `0xCDD10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 226 | `sqlite3_total_changes` | `0xCDD20` | 1,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 231 | `sqlite3_txn_state` | `0xCE1C0` | 174 | UnwindData |  |
| 38 | `sqlite3_close` | `0xCE270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `sqlite3_close_v2` | `0xCE280` | 1,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `sqlite3_errstr` | `0xCE910` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `sqlite3_busy_handler` | `0xCE9E0` | 100 | UnwindData |  |
| 154 | `sqlite3_progress_handler` | `0xCEA50` | 119 | UnwindData |  |
| 33 | `sqlite3_busy_timeout` | `0xCEAD0` | 170 | UnwindData |  |
| 189 | `sqlite3_setlk_timeout` | `0xCEB80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `sqlite3_interrupt` | `0xCEB90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `sqlite3_is_interrupted` | `0xCEBA0` | 1,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `sqlite3_create_function` | `0xCF040` | 79 | UnwindData |  |
| 70 | `sqlite3_create_function_v2` | `0xCF090` | 87 | UnwindData |  |
| 73 | `sqlite3_create_window_function` | `0xCF0F0` | 97 | UnwindData |  |
| 69 | `sqlite3_create_function16` | `0xCF160` | 327 | UnwindData |  |
| 146 | `sqlite3_overload_function` | `0xCF310` | 231 | UnwindData |  |
| 228 | `sqlite3_trace` | `0xCF400` | 121 | UnwindData |  |
| 229 | `sqlite3_trace_v2` | `0xCF480` | 122 | UnwindData |  |
| 153 | `sqlite3_profile` | `0xCF500` | 125 | UnwindData |  |
| 57 | `sqlite3_commit_hook` | `0xCF580` | 104 | UnwindData |  |
| 232 | `sqlite3_update_hook` | `0xCF5F0` | 104 | UnwindData |  |
| 182 | `sqlite3_rollback_hook` | `0xCF660` | 104 | UnwindData |  |
| 4 | `sqlite3_autovacuum_pages` | `0xCF6D0` | 127 | UnwindData |  |
| 272 | `sqlite3_wal_autocheckpoint` | `0xCF7B0` | 139 | UnwindData |  |
| 275 | `sqlite3_wal_hook` | `0xCF840` | 104 | UnwindData |  |
| 274 | `sqlite3_wal_checkpoint_v2` | `0xCF8B0` | 350 | UnwindData |  |
| 273 | `sqlite3_wal_checkpoint` | `0xCFA10` | 29 | UnwindData |  |
| 93 | `sqlite3_errmsg` | `0xCFC00` | 411 | UnwindData |  |
| 187 | `sqlite3_set_errmsg` | `0xCFDA0` | 280 | UnwindData |  |
| 95 | `sqlite3_error_offset` | `0xCFEC0` | 115 | UnwindData |  |
| 94 | `sqlite3_errmsg16` | `0xCFF40` | 134 | UnwindData |  |
| 92 | `sqlite3_errcode` | `0xD0110` | 128 | UnwindData |  |
| 100 | `sqlite3_extended_errcode` | `0xD0190` | 125 | UnwindData |  |
| 220 | `sqlite3_system_errno` | `0xD0210` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `sqlite3_limit` | `0xD0440` | 3,552 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `sqlite3_open` | `0xD1220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `sqlite3_open_v2` | `0xD1230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `sqlite3_open16` | `0xD1240` | 36 | UnwindData |  |
| 64 | `sqlite3_create_collation` | `0xD1360` | 33 | UnwindData |  |
| 66 | `sqlite3_create_collation_v2` | `0xD1390` | 149 | UnwindData |  |
| 65 | `sqlite3_create_collation16` | `0xD1430` | 278 | UnwindData |  |
| 40 | `sqlite3_collation_needed` | `0xD1550` | 97 | UnwindData |  |
| 41 | `sqlite3_collation_needed16` | `0xD15C0` | 97 | UnwindData |  |
| 112 | `sqlite3_get_clientdata` | `0xD1630` | 156 | UnwindData |  |
| 186 | `sqlite3_set_clientdata` | `0xD16D0` | 441 | UnwindData |  |
| 110 | `sqlite3_get_autocommit` | `0xD1890` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 221 | `sqlite3_table_column_metadata` | `0xD1910` | 1,206 | UnwindData |  |
| 191 | `sqlite3_sleep` | `0xD1DD0` | 47 | UnwindData |  |
| 101 | `sqlite3_extended_result_codes` | `0xD1E80` | 76 | UnwindData |  |
| 102 | `sqlite3_file_control` | `0xD1ED0` | 6 | UnwindData |  |
| 223 | `sqlite3_test_control` | `0xD2100` | 801 | UnwindData |  |
| 67 | `sqlite3_create_filename` | `0xD2670` | 409 | UnwindData |  |
| 108 | `sqlite3_free_filename` | `0xD2810` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 236 | `sqlite3_uri_parameter` | `0xD2840` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 235 | `sqlite3_uri_key` | `0xD2920` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 233 | `sqlite3_uri_boolean` | `0xD29F0` | 66 | UnwindData |  |
| 234 | `sqlite3_uri_int64` | `0xD2A40` | 49 | UnwindData |  |
| 103 | `sqlite3_filename_database` | `0xD2A80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `sqlite3_filename_journal` | `0xD2AB0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `sqlite3_filename_wal` | `0xD2B50` | 57 | UnwindData |  |
| 82 | `sqlite3_db_name` | `0xD2B90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `sqlite3_db_filename` | `0xD2BB0` | 104 | UnwindData |  |
| 83 | `sqlite3_db_readonly` | `0xD2C20` | 73 | UnwindData |  |
| 59 | `sqlite3_compileoption_used` | `0xD2C70` | 382 | UnwindData |  |
| 58 | `sqlite3_compileoption_get` | `0xD2DF0` | 40,848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 195 | `sqlite3_sourceid` | `0xDCD80` | 44,584 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 257 | `sqlite3_version` | `0xE7BA8` | 131,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `sqlite3_data_directory` | `0x107EF8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `sqlite3_temp_directory` | `0x107F00` | 0 | Indeterminate |  |
