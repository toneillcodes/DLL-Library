# Binary Specification: zip.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\drivers\Lenovo\udc\Service\zip.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `071566da8d078228d7ac0f234d6c2963d22edafe1d4916f2c6f495223ac3f99c`
* **Total Exported Functions:** 128

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `zip_add` | `0x1000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `zip_add_dir` | `0x1010` | 5,760 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `zip_close` | `0x2690` | 1,644 | UnwindData |  |
| 5 | `zip_delete` | `0x2D00` | 164 | UnwindData |  |
| 6 | `zip_dir_add` | `0x2DB0` | 95 | UnwindData |  |
| 7 | `zip_discard` | `0x50D0` | 17 | UnwindData |  |
| 10 | `zip_error_code_system` | `0x5270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `zip_error_code_zip` | `0x5280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `zip_error_fini` | `0x5290` | 33 | UnwindData |  |
| 15 | `zip_error_init` | `0x52C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `zip_error_init_with_code` | `0x52D0` | 87 | UnwindData |  |
| 17 | `zip_error_set` | `0x5330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `zip_error_set_from_source` | `0x5340` | 61 | UnwindData |  |
| 20 | `zip_error_system_type` | `0x5380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `zip_error_to_data` | `0x53A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `zip_error_clear` | `0x53C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `zip_error_get` | `0x53D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `zip_file_get_error` | `0x53E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `zip_get_error` | `0x53F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `zip_error_get_sys_type` | `0x5400` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `zip_error_strerror` | `0x5490` | 673 | UnwindData |  |
| 22 | `zip_error_to_str` | `0x5740` | 148 | UnwindData |  |
| 29 | `zip_file_extra_field_delete` | `0x6580` | 205 | UnwindData |  |
| 30 | `zip_file_extra_field_delete_by_id` | `0x6650` | 215 | UnwindData |  |
| 31 | `zip_file_extra_field_get` | `0x6730` | 75 | UnwindData |  |
| 32 | `zip_file_extra_field_get_by_id` | `0x6840` | 77 | UnwindData |  |
| 33 | `zip_file_extra_field_set` | `0x6900` | 574 | UnwindData |  |
| 34 | `zip_file_extra_fields_count` | `0x6B40` | 191 | UnwindData |  |
| 35 | `zip_file_extra_fields_count_by_id` | `0x6C00` | 72 | UnwindData |  |
| 23 | `zip_fclose` | `0x6CC0` | 59 | UnwindData |  |
| 24 | `zip_fdopen` | `0x6D00` | 37 | UnwindData |  |
| 25 | `zip_file_add` | `0x6E50` | 71 | UnwindData |  |
| 27 | `zip_file_error_clear` | `0x6EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `zip_file_error_get` | `0x6EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `zip_file_get_comment` | `0x6EC0` | 111 | UnwindData |  |
| 38 | `zip_file_get_external_attributes` | `0x6F30` | 70 | UnwindData |  |
| 40 | `zip_file_rename` | `0x7180` | 248 | UnwindData |  |
| 41 | `zip_file_replace` | `0x7430` | 75 | UnwindData |  |
| 42 | `zip_file_set_comment` | `0x7480` | 413 | UnwindData |  |
| 44 | `zip_file_set_encryption` | `0x7620` | 252 | UnwindData |  |
| 45 | `zip_file_set_external_attributes` | `0x78D0` | 383 | UnwindData |  |
| 43 | `zip_file_set_dostime` | `0x7A50` | 31 | UnwindData |  |
| 46 | `zip_file_set_mtime` | `0x7A70` | 127 | UnwindData |  |
| 47 | `zip_file_strerror` | `0x7C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `zip_fopen` | `0x7C40` | 67 | UnwindData |  |
| 49 | `zip_fopen_encrypted` | `0x7C90` | 84 | UnwindData |  |
| 50 | `zip_fopen_index` | `0x7CF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `zip_fopen_index_encrypted` | `0x7D00` | 112 | UnwindData |  |
| 52 | `zip_fread` | `0x7DD0` | 112 | UnwindData |  |
| 39 | `zip_file_is_seekable` | `0x7E40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `zip_fseek` | `0x7E60` | 60 | UnwindData |  |
| 54 | `zip_ftell` | `0x7EA0` | 58 | UnwindData |  |
| 55 | `zip_get_archive_comment` | `0x7EE0` | 79 | UnwindData |  |
| 56 | `zip_get_archive_flag` | `0x7F30` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `zip_encryption_method_supported` | `0x7FB0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `zip_get_file_comment` | `0x8030` | 41 | UnwindData |  |
| 59 | `zip_get_name` | `0x80A0` | 68 | UnwindData |  |
| 60 | `zip_get_num_entries` | `0x80F0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `zip_get_num_files` | `0x8140` | 48 | UnwindData |  |
| 62 | `zip_libzip_version` | `0x8E60` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `zip_name_locate` | `0x9100` | 5,392 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `zip_open` | `0xA610` | 206 | UnwindData |  |
| 65 | `zip_open_from_source` | `0xA6E0` | 101 | UnwindData |  |
| 66 | `zip_register_cancel_callback_with_state` | `0xAD30` | 257 | UnwindData |  |
| 67 | `zip_register_progress_callback` | `0xAE40` | 287 | UnwindData |  |
| 68 | `zip_register_progress_callback_with_state` | `0xAF60` | 261 | UnwindData |  |
| 69 | `zip_rename` | `0xB070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `zip_replace` | `0xB080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `zip_set_archive_comment` | `0xB090` | 83 | UnwindData |  |
| 73 | `zip_set_archive_flag` | `0xB1E0` | 45 | UnwindData |  |
| 74 | `zip_set_default_password` | `0xB2A0` | 113 | UnwindData |  |
| 75 | `zip_set_file_comment` | `0xB320` | 58 | UnwindData |  |
| 76 | `zip_set_file_compression` | `0xB360` | 330 | UnwindData |  |
| 77 | `zip_source_begin_write` | `0xB7D0` | 113 | UnwindData |  |
| 78 | `zip_source_begin_write_cloning` | `0xB850` | 113 | UnwindData |  |
| 79 | `zip_source_buffer` | `0xC6F0` | 60 | UnwindData |  |
| 80 | `zip_source_buffer_create` | `0xC730` | 22 | UnwindData |  |
| 81 | `zip_source_buffer_fragment` | `0xC750` | 60 | UnwindData |  |
| 82 | `zip_source_buffer_fragment_create` | `0xC790` | 22 | UnwindData |  |
| 83 | `zip_source_close` | `0xCB10` | 110 | UnwindData |  |
| 84 | `zip_source_commit_write` | `0xCB80` | 183 | UnwindData |  |
| 4 | `zip_compression_method_supported` | `0xD370` | 1,264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `zip_source_error` | `0xD860` | 2,960 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `zip_source_filep` | `0xE3F0` | 85 | UnwindData |  |
| 89 | `zip_source_filep_create` | `0xE450` | 89 | UnwindData |  |
| 90 | `zip_source_free` | `0xE4B0` | 131 | UnwindData |  |
| 91 | `zip_source_function` | `0xE5C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `zip_source_function_create` | `0xE5E0` | 201 | UnwindData |  |
| 96 | `zip_source_keep` | `0xE6B0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `zip_file_attributes_init` | `0xE790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `zip_source_get_file_attributes` | `0xE7A0` | 397 | UnwindData |  |
| 94 | `zip_source_is_deleted` | `0xE930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `zip_source_layered` | `0xE940` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `zip_source_layered_create` | `0xE970` | 173 | UnwindData |  |
| 100 | `zip_source_open` | `0xEA20` | 211 | UnwindData |  |
| 101 | `zip_source_pass_to_lower_layer` | `0xEB00` | 166 | UnwindData |  |
| 102 | `zip_source_read` | `0xF570` | 106 | UnwindData |  |
| 103 | `zip_source_rollback_write` | `0xF760` | 54 | UnwindData |  |
| 104 | `zip_source_seek` | `0xF7A0` | 145 | UnwindData |  |
| 105 | `zip_source_seek_compute_offset` | `0xF840` | 95 | UnwindData |  |
| 106 | `zip_source_seek_write` | `0xF8A0` | 145 | UnwindData |  |
| 107 | `zip_source_stat` | `0xF940` | 26 | UnwindData |  |
| 95 | `zip_source_is_seekable` | `0xFA10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `zip_source_make_command_bitmap` | `0xFA20` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `zip_source_tell` | `0xFA80` | 127 | UnwindData |  |
| 109 | `zip_source_tell_write` | `0xFB00` | 94 | UnwindData |  |
| 116 | `zip_source_window_create` | `0x10330` | 44 | UnwindData |  |
| 117 | `zip_source_write` | `0x104C0` | 69 | UnwindData |  |
| 118 | `zip_source_zip` | `0x10510` | 131 | UnwindData |  |
| 119 | `zip_source_zip_create` | `0x105A0` | 115 | UnwindData |  |
| 120 | `zip_source_zip_file` | `0x10620` | 72 | UnwindData |  |
| 121 | `zip_source_zip_file_create` | `0x10670` | 1,418 | UnwindData |  |
| 122 | `zip_stat` | `0x10C00` | 87 | UnwindData |  |
| 123 | `zip_stat_index` | `0x10C60` | 75 | UnwindData |  |
| 124 | `zip_stat_init` | `0x10F60` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `zip_strerror` | `0x10F90` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `zip_unchange` | `0x114E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `zip_unchange_all` | `0x114F0` | 118 | UnwindData |  |
| 128 | `zip_unchange_archive` | `0x11570` | 50 | UnwindData |  |
| 112 | `zip_source_win32handle` | `0x11C90` | 86 | UnwindData |  |
| 113 | `zip_source_win32handle_create` | `0x11CF0` | 90 | UnwindData |  |
| 114 | `zip_source_win32w` | `0x12430` | 98 | UnwindData |  |
| 115 | `zip_source_win32w_create` | `0x124A0` | 94 | UnwindData |  |
| 86 | `zip_source_file` | `0x12500` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `zip_source_file_create` | `0x12530` | 99 | UnwindData |  |
| 110 | `zip_source_win32a` | `0x12700` | 98 | UnwindData |  |
| 111 | `zip_source_win32a_create` | `0x12770` | 94 | UnwindData |  |
| 71 | `zip_secure_random` | `0x130E0` | 34 | UnwindData |  |
