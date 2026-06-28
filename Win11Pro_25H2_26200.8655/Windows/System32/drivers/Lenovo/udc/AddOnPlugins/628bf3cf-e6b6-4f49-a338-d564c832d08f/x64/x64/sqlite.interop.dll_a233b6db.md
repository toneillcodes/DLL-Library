# Binary Specification: sqlite.interop.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\drivers\Lenovo\udc\AddOnPlugins\628bf3cf-e6b6-4f49-a338-d564c832d08f\x64\x64\sqlite.interop.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a233b6dba1f845b37eaa35fb8a505dfa34eeafa94ea3331201148e944d170062`
* **Total Exported Functions:** 207

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 152 | `sqlite3_totype_init` | `0x14040` | 156 | UnwindData |  |
| 145 | `sqlite3_sha_init` | `0x14C20` | 156 | UnwindData |  |
| 123 | `sqlite3_regexp_init` | `0x17010` | 71 | UnwindData |  |
| 117 | `sqlite3_percentile_init` | `0x18BB0` | 78 | UnwindData |  |
| 94 | `sqlite3_json_init` | `0x18F90` | 55,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `sqlite3_fts5_init` | `0x26910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `sqlite3_fts_init` | `0x26920` | 123,632 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 167 | `sqlite3_vtshim_init` | `0x44C10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `sqlite3_dispose_module` | `0x44C20` | 15 | UnwindData |  |
| 65 | `sqlite3_create_disposable_module` | `0x44CB0` | 817 | UnwindData |  |
| 68 | `sqlite3_cursor_rowid_interop` | `0x46470` | 66 | UnwindData |  |
| 151 | `sqlite3_table_cursor_interop` | `0x465C0` | 172 | UnwindData |  |
| 92 | `sqlite3_index_column_info_interop` | `0x46680` | 393 | UnwindData |  |
| 150 | `sqlite3_table_column_metadata_interop` | `0x46810` | 203 | UnwindData |  |
| 51 | `sqlite3_column_origin_name16_interop` | `0x468F0` | 69 | UnwindData |  |
| 52 | `sqlite3_column_origin_name_interop` | `0x46940` | 64 | UnwindData |  |
| 53 | `sqlite3_column_table_name16_interop` | `0x46990` | 69 | UnwindData |  |
| 54 | `sqlite3_column_table_name_interop` | `0x469E0` | 64 | UnwindData |  |
| 40 | `sqlite3_column_database_name16_interop` | `0x46A30` | 69 | UnwindData |  |
| 41 | `sqlite3_column_database_name_interop` | `0x46A80` | 64 | UnwindData |  |
| 63 | `sqlite3_context_collseq_interop` | `0x46AD0` | 167 | UnwindData |  |
| 62 | `sqlite3_context_collcompare_interop` | `0x46B80` | 140 | UnwindData |  |
| 137 | `sqlite3_result_int64_interop` | `0x46C20` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `sqlite3_result_double_interop` | `0x46C60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 164 | `sqlite3_value_text16_interop` | `0x46C80` | 182 | UnwindData |  |
| 165 | `sqlite3_value_text_interop` | `0x46D40` | 182 | UnwindData |  |
| 163 | `sqlite3_value_int64_interop` | `0x46E00` | 91 | UnwindData |  |
| 160 | `sqlite3_value_double_interop` | `0x46E70` | 89 | UnwindData |  |
| 67 | `sqlite3_create_function_interop` | `0x46ED0` | 194 | UnwindData |  |
| 126 | `sqlite3_reset_interop` | `0x46FA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `sqlite3_blob_close_interop` | `0x46FB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `sqlite3_backup_finish_interop` | `0x46FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `sqlite3_finalize_interop` | `0x46FD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `sqlite3_column_text16_interop` | `0x46FE0` | 77 | UnwindData |  |
| 56 | `sqlite3_column_text_interop` | `0x47040` | 77 | UnwindData |  |
| 107 | `sqlite3_memory_highwater_interop` | `0x470A0` | 27 | UnwindData |  |
| 109 | `sqlite3_memory_used_interop` | `0x470D0` | 10 | UnwindData |  |
| 97 | `sqlite3_last_insert_rowid_interop` | `0x47130` | 27 | UnwindData |  |
| 48 | `sqlite3_column_int64_interop` | `0x47160` | 27 | UnwindData |  |
| 45 | `sqlite3_column_double_interop` | `0x47190` | 28 | UnwindData |  |
| 42 | `sqlite3_column_decltype16_interop` | `0x471C0` | 68 | UnwindData |  |
| 43 | `sqlite3_column_decltype_interop` | `0x47210` | 64 | UnwindData |  |
| 49 | `sqlite3_column_name16_interop` | `0x47260` | 66 | UnwindData |  |
| 50 | `sqlite3_column_name_interop` | `0x472B0` | 61 | UnwindData |  |
| 21 | `sqlite3_bind_parameter_name_interop` | `0x47300` | 129 | UnwindData |  |
| 17 | `sqlite3_bind_int64_interop` | `0x47390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `sqlite3_bind_double_interop` | `0x473B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `sqlite3_create_disposable_module_interop` | `0x473D0` | 391 | UnwindData |  |
| 118 | `sqlite3_prepare16_interop` | `0x47560` | 97 | UnwindData |  |
| 119 | `sqlite3_prepare_interop` | `0x475D0` | 92 | UnwindData |  |
| 33 | `sqlite3_changes_interop` | `0x47640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `sqlite3_errmsg_interop` | `0x47650` | 59 | UnwindData |  |
| 114 | `sqlite3_open16_interop` | `0x476A0` | 51 | UnwindData |  |
| 115 | `sqlite3_open_interop` | `0x47770` | 48 | UnwindData |  |
| 4 | `interop_sourceid` | `0x47820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `interop_libversion` | `0x47830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `sqlite3_close_interop` | `0x47840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `sqlite3_msize_interop` | `0x47850` | 48 | UnwindData |  |
| 105 | `sqlite3_malloc_size_interop` | `0x47890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `interop_compileoption_get` | `0x478A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `interop_compileoption_used` | `0x478C0` | 520 | UnwindData |  |
| 124 | `sqlite3_rekey` | `0x4BFD0` | 155 | UnwindData |  |
| 95 | `sqlite3_key` | `0x4C450` | 155 | UnwindData |  |
| 147 | `sqlite3_sourceid` | `0x4F8E0` | 1,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 180 | `sqlite3changeset_concat_strm` | `0x4FD30` | 195 | UnwindData |  |
| 179 | `sqlite3changeset_concat` | `0x4FE00` | 192 | UnwindData |  |
| 173 | `sqlite3changegroup_delete` | `0x4FED0` | 15 | UnwindData |  |
| 176 | `sqlite3changegroup_output_strm` | `0x50120` | 26 | UnwindData |  |
| 172 | `sqlite3changegroup_add_strm` | `0x50140` | 170 | UnwindData |  |
| 175 | `sqlite3changegroup_output` | `0x501F0` | 27 | UnwindData |  |
| 171 | `sqlite3changegroup_add` | `0x50220` | 165 | UnwindData |  |
| 174 | `sqlite3changegroup_new` | `0x502D0` | 83 | UnwindData |  |
| 178 | `sqlite3changeset_apply_strm` | `0x50E00` | 40 | UnwindData |  |
| 177 | `sqlite3changeset_apply` | `0x50EF0` | 40 | UnwindData |  |
| 185 | `sqlite3changeset_invert_strm` | `0x54B50` | 101 | UnwindData |  |
| 184 | `sqlite3changeset_invert` | `0x54BC0` | 81 | UnwindData |  |
| 182 | `sqlite3changeset_finalize` | `0x555E0` | 20 | UnwindData |  |
| 183 | `sqlite3changeset_fk_conflicts` | `0x55690` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `sqlite3changeset_conflict` | `0x556C0` | 68 | UnwindData |  |
| 186 | `sqlite3changeset_new` | `0x55710` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 188 | `sqlite3changeset_old` | `0x55760` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `sqlite3changeset_pk` | `0x557A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 189 | `sqlite3changeset_op` | `0x557C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 187 | `sqlite3changeset_next` | `0x557F0` | 70 | UnwindData |  |
| 194 | `sqlite3changeset_start_v2_strm` | `0x56790` | 40 | UnwindData |  |
| 192 | `sqlite3changeset_start_strm` | `0x567C0` | 32 | UnwindData |  |
| 193 | `sqlite3changeset_start_v2` | `0x567F0` | 158 | UnwindData |  |
| 191 | `sqlite3changeset_start` | `0x568A0` | 149 | UnwindData |  |
| 204 | `sqlite3session_memory_used` | `0x569F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 203 | `sqlite3session_isempty` | `0x56A00` | 227 | UnwindData |  |
| 202 | `sqlite3session_indirect` | `0x56AF0` | 82 | UnwindData |  |
| 201 | `sqlite3session_enable` | `0x56B50` | 82 | UnwindData |  |
| 205 | `sqlite3session_patchset` | `0x56BB0` | 34 | UnwindData |  |
| 206 | `sqlite3session_patchset_strm` | `0x56BE0` | 35 | UnwindData |  |
| 197 | `sqlite3session_changeset_strm` | `0x56C10` | 34 | UnwindData |  |
| 196 | `sqlite3session_changeset` | `0x56C40` | 32 | UnwindData |  |
| 195 | `sqlite3session_attach` | `0x59200` | 6 | UnwindData |  |
| 207 | `sqlite3session_table_filter` | `0x59420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 199 | `sqlite3session_delete` | `0x59440` | 457 | UnwindData |  |
| 198 | `sqlite3session_create` | `0x598A0` | 351 | UnwindData |  |
| 200 | `sqlite3session_diff` | `0x59A10` | 64 | UnwindData |  |
| 59 | `sqlite3_compileoption_get` | `0x864D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `sqlite3_compileoption_used` | `0x864F0` | 60 | UnwindData |  |
| 72 | `sqlite3_db_readonly` | `0x866B0` | 185 | UnwindData |  |
| 70 | `sqlite3_db_filename` | `0x86770` | 128 | UnwindData |  |
| 85 | `sqlite3_file_control` | `0x87170` | 401 | UnwindData |  |
| 84 | `sqlite3_extended_result_codes` | `0x87370` | 201 | UnwindData |  |
| 91 | `sqlite3_get_autocommit` | `0x879B0` | 131 | UnwindData |  |
| 64 | `sqlite3_create_collation` | `0x87E90` | 33 | UnwindData |  |
| 100 | `sqlite3_limit` | `0x88F00` | 178 | UnwindData |  |
| 81 | `sqlite3_errstr` | `0x89200` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `sqlite3_extended_errcode` | `0x89280` | 133 | UnwindData |  |
| 79 | `sqlite3_errcode` | `0x89310` | 136 | UnwindData |  |
| 143 | `sqlite3_rollback_hook` | `0x89BD0` | 233 | UnwindData |  |
| 155 | `sqlite3_update_hook` | `0x89CC0` | 233 | UnwindData |  |
| 58 | `sqlite3_commit_hook` | `0x89DB0` | 233 | UnwindData |  |
| 154 | `sqlite3_trace_v2` | `0x89FB0` | 235 | UnwindData |  |
| 153 | `sqlite3_trace` | `0x8A0B0` | 247 | UnwindData |  |
| 116 | `sqlite3_overload_function` | `0x8A1B0` | 174 | UnwindData |  |
| 93 | `sqlite3_interrupt` | `0x8AB40` | 166 | UnwindData |  |
| 31 | `sqlite3_busy_timeout` | `0x8ABF0` | 203 | UnwindData |  |
| 120 | `sqlite3_progress_handler` | `0x8ACD0` | 243 | UnwindData |  |
| 32 | `sqlite3_changes` | `0x8BDE0` | 130 | UnwindData |  |
| 96 | `sqlite3_last_insert_rowid` | `0x8BF30` | 131 | UnwindData |  |
| 69 | `sqlite3_db_config` | `0x8C100` | 50 | UnwindData |  |
| 73 | `sqlite3_db_release_memory` | `0x8C370` | 135 | UnwindData |  |
| 61 | `sqlite3_config` | `0x8C790` | 85 | UnwindData |  |
| 146 | `sqlite3_shutdown` | `0x8CC20` | 184 | UnwindData |  |
| 99 | `sqlite3_libversion_number` | `0x8CF10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `sqlite3_libversion` | `0x8CF20` | 123,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `sqlite3_declare_vtab` | `0xAB1D0` | 178 | UnwindData |  |
| 77 | `sqlite3_enable_load_extension` | `0xC9F20` | 80 | UnwindData |  |
| 101 | `sqlite3_load_extension` | `0xCA0C0` | 128 | UnwindData |  |
| 82 | `sqlite3_exec` | `0xCA830` | 165 | UnwindData |  |
| 144 | `sqlite3_set_authorizer` | `0xE6F30` | 264 | UnwindData |  |
| 29 | `sqlite3_blob_reopen` | `0x1038E0` | 80 | UnwindData |  |
| 24 | `sqlite3_blob_bytes` | `0x1039E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `sqlite3_blob_write` | `0x103A00` | 26 | UnwindData |  |
| 28 | `sqlite3_blob_read` | `0x103A20` | 26 | UnwindData |  |
| 25 | `sqlite3_blob_close` | `0x103C30` | 18 | UnwindData |  |
| 27 | `sqlite3_blob_open` | `0x103D00` | 152 | UnwindData |  |
| 113 | `sqlite3_next_stmt` | `0x10CCE0` | 199 | UnwindData |  |
| 149 | `sqlite3_stmt_readonly` | `0x10CE00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `sqlite3_db_handle` | `0x10CE20` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `sqlite3_bind_parameter_index` | `0x10CFA0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `sqlite3_bind_parameter_count` | `0x10D050` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `sqlite3_bind_text16` | `0x10D2A0` | 29 | UnwindData |  |
| 22 | `sqlite3_bind_text` | `0x10D330` | 29 | UnwindData |  |
| 18 | `sqlite3_bind_null` | `0x10D420` | 55 | UnwindData |  |
| 16 | `sqlite3_bind_int64` | `0x10D460` | 133 | UnwindData |  |
| 15 | `sqlite3_bind_int` | `0x10D4F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `sqlite3_bind_double` | `0x10D500` | 105 | UnwindData |  |
| 12 | `sqlite3_bind_blob` | `0x10D5C0` | 86 | UnwindData |  |
| 57 | `sqlite3_column_type` | `0x10DB40` | 100 | UnwindData |  |
| 47 | `sqlite3_column_int64` | `0x10DD90` | 153 | UnwindData |  |
| 46 | `sqlite3_column_int` | `0x10DE30` | 152 | UnwindData |  |
| 44 | `sqlite3_column_double` | `0x10DED0` | 135 | UnwindData |  |
| 38 | `sqlite3_column_bytes16` | `0x10DF60` | 155 | UnwindData |  |
| 37 | `sqlite3_column_bytes` | `0x10E010` | 155 | UnwindData |  |
| 36 | `sqlite3_column_blob` | `0x10E0C0` | 94 | UnwindData |  |
| 39 | `sqlite3_column_count` | `0x10E230` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `sqlite3_aggregate_count` | `0x10E250` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `sqlite3_aggregate_context` | `0x10E3B0` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 148 | `sqlite3_step` | `0x10E5A0` | 135 | UnwindData |  |
| 133 | `sqlite3_result_error_nomem` | `0x10EA50` | 136 | UnwindData |  |
| 134 | `sqlite3_result_error_toobig` | `0x10EAE0` | 86 | UnwindData |  |
| 132 | `sqlite3_result_error_code` | `0x10EB40` | 39 | UnwindData |  |
| 142 | `sqlite3_result_zeroblob` | `0x10ECD0` | 82 | UnwindData |  |
| 141 | `sqlite3_result_value` | `0x10ED30` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `sqlite3_result_text16` | `0x10EE20` | 106 | UnwindData |  |
| 139 | `sqlite3_result_text` | `0x10EED0` | 106 | UnwindData |  |
| 138 | `sqlite3_result_null` | `0x10EFF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `sqlite3_result_int64` | `0x10F020` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `sqlite3_result_int` | `0x10F050` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `sqlite3_result_error16` | `0x10F080` | 36 | UnwindData |  |
| 130 | `sqlite3_result_error` | `0x10F0B0` | 309 | UnwindData |  |
| 128 | `sqlite3_result_double` | `0x10F1F0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `sqlite3_result_blob` | `0x10F290` | 106 | UnwindData |  |
| 166 | `sqlite3_value_type` | `0x10F520` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 162 | `sqlite3_value_int64` | `0x10F6C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 161 | `sqlite3_value_int` | `0x10F700` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `sqlite3_value_double` | `0x10F730` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 158 | `sqlite3_value_bytes16` | `0x10F760` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `sqlite3_value_bytes` | `0x10F7A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `sqlite3_value_blob` | `0x10F7E0` | 121 | UnwindData |  |
| 34 | `sqlite3_clear_bindings` | `0x10F860` | 9 | UnwindData |  |
| 9 | `sqlite3_backup_pagecount` | `0x119DA0` | 66 | UnwindData |  |
| 10 | `sqlite3_backup_remaining` | `0x119DF0` | 66 | UnwindData |  |
| 11 | `sqlite3_backup_step` | `0x119F70` | 171 | UnwindData |  |
| 8 | `sqlite3_backup_init` | `0x11A9F0` | 468 | UnwindData |  |
| 78 | `sqlite3_enable_shared_cache` | `0x1292E0` | 73,872 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 170 | `sqlite3_win32_set_directory` | `0x13B370` | 2,384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `sqlite3_win32_reset_heap` | `0x13BCC0` | 13 | UnwindData |  |
| 168 | `sqlite3_win32_compact_heap` | `0x13BE20` | 144 | UnwindData |  |
| 102 | `sqlite3_log` | `0x13F180` | 44 | UnwindData |  |
| 110 | `sqlite3_mprintf` | `0x13F340` | 60 | UnwindData |  |
| 122 | `sqlite3_realloc64` | `0x141CB0` | 59 | UnwindData |  |
| 121 | `sqlite3_realloc` | `0x141D00` | 65 | UnwindData |  |
| 87 | `sqlite3_free` | `0x142040` | 111 | UnwindData |  |
| 111 | `sqlite3_msize` | `0x1420C0` | 31 | UnwindData |  |
| 104 | `sqlite3_malloc64` | `0x142190` | 39 | UnwindData |  |
| 103 | `sqlite3_malloc` | `0x1421C0` | 43 | UnwindData |  |
| 106 | `sqlite3_memory_highwater` | `0x142460` | 98 | UnwindData |  |
| 108 | `sqlite3_memory_used` | `0x1424D0` | 66 | UnwindData |  |
| 125 | `sqlite3_release_memory` | `0x142840` | 12,288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `sqlite3_db_status` | `0x145840` | 185 | UnwindData |  |
| 88 | `sqlite3_fts3_may_be_corrupt` | `0x187C5C` | 0 | Indeterminate |  |
