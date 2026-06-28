# Binary Specification: archiveint.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\archiveint.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0c0f9038b5b8cf84102bfa57789bc6fe69ae9c96293e19757013175736ad869d`
* **Total Exported Functions:** 455

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 293 | `archive_read_set_close_callback` | `0x42D0` | 67 | UnwindData |  |
| 203 | `archive_match_excluded` | `0x4320` | 164 | UnwindData |  |
| 349 | `archive_read_support_format_tar` | `0x5A60` | 382 | UnwindData |  |
| 244 | `archive_read_data_skip` | `0x5D40` | 142 | UnwindData |  |
| 28 | `archive_entry_clear` | `0x5F50` | 176 | UnwindData |  |
| 356 | `archive_set_error` | `0x7A50` | 69 | UnwindData |  |
| 93 | `archive_entry_pathname_w` | `0x8B90` | 79 | UnwindData |  |
| 143 | `archive_entry_sparse_clear` | `0x11320` | 77 | UnwindData |  |
| 170 | `archive_entry_xattr_clear` | `0x11380` | 123 | UnwindData |  |
| 40 | `archive_entry_copy_mac_metadata` | `0x11410` | 149 | UnwindData |  |
| 380 | `archive_write_data` | `0x114B0` | 656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `archive_entry_set_mtime` | `0x11740` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `archive_entry_set_ctime` | `0x117F0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `archive_entry_set_atime` | `0x11850` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `archive_entry_update_pathname_utf8` | `0x11A40` | 71 | UnwindData |  |
| 2 | `archive_clear_error` | `0x11B90` | 1,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `archive_entry_mtime_nsec` | `0x120A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 242 | `archive_read_data_block` | `0x120B0` | 23 | UnwindData |  |
| 84 | `archive_entry_mtime` | `0x120D0` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 276 | `archive_read_next_header` | `0x12250` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `archive_entry_size` | `0x12540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `archive_entry_atime_is_set` | `0x12550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `archive_entry_birthtime_is_set` | `0x12570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `archive_entry_filetype` | `0x12590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `archive_entry_set_mode` | `0x125B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `archive_entry_linkresolver_free` | `0x125F0` | 79 | UnwindData |  |
| 131 | `archive_entry_set_size` | `0x12840` | 19,648 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 351 | `archive_read_support_format_xar` | `0x17500` | 252 | UnwindData |  |
| 336 | `archive_read_support_format_all` | `0x186B0` | 171 | UnwindData |  |
| 339 | `archive_read_support_format_cab` | `0x18770` | 311 | UnwindData |  |
| 344 | `archive_read_support_format_lha` | `0x188B0` | 258 | UnwindData |  |
| 346 | `archive_read_support_format_rar` | `0x189C0` | 261 | UnwindData |  |
| 352 | `archive_read_support_format_zip` | `0x18AD0` | 33 | UnwindData |  |
| 354 | `archive_read_support_format_zip_streamable` | `0x18B00` | 271 | UnwindData |  |
| 337 | `archive_read_support_format_ar` | `0x18C20` | 239 | UnwindData |  |
| 335 | `archive_read_support_format_7zip` | `0x18D20` | 247 | UnwindData |  |
| 340 | `archive_read_support_format_cpio` | `0x18E20` | 240 | UnwindData |  |
| 347 | `archive_read_support_format_rar5` | `0x18F20` | 291 | UnwindData |  |
| 350 | `archive_read_support_format_warc` | `0x19050` | 234 | UnwindData |  |
| 341 | `archive_read_support_format_empty` | `0x19140` | 126 | UnwindData |  |
| 345 | `archive_read_support_format_mtree` | `0x191D0` | 267 | UnwindData |  |
| 343 | `archive_read_support_format_iso9660` | `0x192F0` | 293 | UnwindData |  |
| 108 | `archive_entry_set_filetype` | `0x1A0F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `archive_entry_set_rdevmajor` | `0x1A130` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | `archive_entry_set_rdevminor` | `0x1A160` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `archive_entry_set_dev` | `0x1A190` | 646,672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `archive_entry_acl` | `0xB7FA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `archive_entry_acl_add_entry` | `0xB7FB0` | 102 | UnwindData |  |
| 10 | `archive_entry_acl_add_entry_w` | `0xB8020` | 60 | UnwindData |  |
| 11 | `archive_entry_acl_clear` | `0xB8070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `archive_entry_acl_count` | `0xB8090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `archive_entry_acl_from_text` | `0xB80B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `archive_entry_acl_from_text_w` | `0xB80D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `archive_entry_acl_next` | `0xB80F0` | 112 | UnwindData |  |
| 16 | `archive_entry_acl_reset` | `0xB8170` | 64 | UnwindData |  |
| 17 | `archive_entry_acl_text` | `0xB81C0` | 94 | UnwindData |  |
| 18 | `archive_entry_acl_text_w` | `0xB8260` | 94 | UnwindData |  |
| 19 | `archive_entry_acl_to_text` | `0xB82D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `archive_entry_acl_to_text_w` | `0xB82F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `archive_entry_acl_types` | `0xB8310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `archive_entry_atime` | `0xB8320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 182 | `archive_format_name` | `0xB8320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `archive_entry_atime_nsec` | `0xB8330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `archive_file_count` | `0xB8330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `archive_entry_birthtime` | `0xB8340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `archive_entry_birthtime_nsec` | `0xB8350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `archive_entry_clone` | `0xB8360` | 619 | UnwindData |  |
| 31 | `archive_entry_copy_fflags_text` | `0xB85E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `archive_entry_copy_fflags_text_len` | `0xB8600` | 76 | UnwindData |  |
| 33 | `archive_entry_copy_fflags_text_w` | `0xB8660` | 60 | UnwindData |  |
| 34 | `archive_entry_copy_gname` | `0xB86B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `archive_entry_set_gname` | `0xB86B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `archive_entry_copy_gname_w` | `0xB86D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `archive_entry_copy_hardlink` | `0xB86F0` | 71 | UnwindData |  |
| 37 | `archive_entry_copy_hardlink_w` | `0xB8740` | 71 | UnwindData |  |
| 38 | `archive_entry_copy_link` | `0xB8790` | 47 | UnwindData |  |
| 118 | `archive_entry_set_link` | `0xB8790` | 47 | UnwindData |  |
| 39 | `archive_entry_copy_link_w` | `0xB87D0` | 47 | UnwindData |  |
| 41 | `archive_entry_copy_pathname` | `0xB8810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `archive_entry_set_pathname` | `0xB8810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `archive_entry_copy_pathname_w` | `0xB8830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `archive_entry_copy_sourcepath` | `0xB8850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `archive_entry_copy_sourcepath_w` | `0xB8870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `archive_entry_copy_symlink` | `0xB8890` | 76 | UnwindData |  |
| 132 | `archive_entry_set_symlink` | `0xB8890` | 76 | UnwindData |  |
| 47 | `archive_entry_copy_symlink_w` | `0xB88F0` | 76 | UnwindData |  |
| 48 | `archive_entry_copy_uname` | `0xB8950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `archive_entry_set_uname` | `0xB8950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `archive_entry_copy_uname_w` | `0xB8970` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `archive_entry_ctime` | `0xB8990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `archive_entry_ctime_is_set` | `0xB89A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `archive_entry_ctime_nsec` | `0xB89C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `archive_entry_dev` | `0xB89D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `archive_entry_dev_is_set` | `0xB8A10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `archive_entry_devmajor` | `0xB8A30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `archive_entry_devminor` | `0xB8A50` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `archive_entry_digest` | `0xB8A80` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `archive_entry_fflags` | `0xB8AE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `archive_entry_fflags_text` | `0xB8B00` | 237 | UnwindData |  |
| 61 | `archive_entry_filetype_is_set` | `0xB8C00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `archive_entry_free` | `0xB8C20` | 34 | UnwindData |  |
| 63 | `archive_entry_gid` | `0xB8C50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `archive_entry_gid_is_set` | `0xB8C60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `archive_entry_gname` | `0xB8C80` | 79 | UnwindData |  |
| 66 | `archive_entry_gname_utf8` | `0xB8CE0` | 79 | UnwindData |  |
| 67 | `archive_entry_gname_w` | `0xB8D40` | 79 | UnwindData |  |
| 68 | `archive_entry_hardlink` | `0xB8DA0` | 88 | UnwindData |  |
| 69 | `archive_entry_hardlink_is_set` | `0xB8E00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `archive_entry_hardlink_utf8` | `0xB8E20` | 88 | UnwindData |  |
| 71 | `archive_entry_hardlink_w` | `0xB8E80` | 88 | UnwindData |  |
| 72 | `archive_entry_ino` | `0xB8EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `archive_entry_ino64` | `0xB8EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `archive_entry_ino_is_set` | `0xB8EF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `archive_entry_is_data_encrypted` | `0xB8F10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `archive_entry_is_encrypted` | `0xB8F30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `archive_entry_is_metadata_encrypted` | `0xB8F50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `archive_entry_mac_metadata` | `0xB8F70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `archive_entry_mode` | `0xB8F90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `archive_entry_mtime_is_set` | `0xB8FA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `archive_entry_new` | `0xB8FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `archive_entry_new2` | `0xB8FD0` | 53 | UnwindData |  |
| 89 | `archive_entry_nlink` | `0xB9010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `archive_entry_pathname` | `0xB9020` | 134 | UnwindData |  |
| 92 | `archive_entry_pathname_utf8` | `0xB90B0` | 79 | UnwindData |  |
| 94 | `archive_entry_perm` | `0xB9110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `archive_entry_perm_is_set` | `0xB9130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `archive_entry_rdev` | `0xB9150` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `archive_entry_rdev_is_set` | `0xB91A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `archive_entry_rdevmajor` | `0xB91C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `archive_entry_rdevminor` | `0xB91F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `archive_entry_set_birthtime` | `0xB9230` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `archive_entry_set_devmajor` | `0xB9290` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `archive_entry_set_devminor` | `0xB92C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `archive_entry_set_digest` | `0xB92F0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `archive_entry_set_fflags` | `0xB9410` | 64 | UnwindData |  |
| 109 | `archive_entry_set_gid` | `0xB9460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `archive_entry_set_gname_utf8` | `0xB9480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `archive_entry_set_hardlink` | `0xB94A0` | 60 | UnwindData |  |
| 113 | `archive_entry_set_hardlink_utf8` | `0xB94F0` | 71 | UnwindData |  |
| 114 | `archive_entry_set_ino` | `0xB9540` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `archive_entry_set_ino64` | `0xB9540` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `archive_entry_set_is_data_encrypted` | `0xB9570` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `archive_entry_set_is_metadata_encrypted` | `0xB95A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `archive_entry_set_link_to_hardlink` | `0xB95D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `archive_entry_set_link_to_symlink` | `0xB95F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `archive_entry_set_link_utf8` | `0xB9610` | 47 | UnwindData |  |
| 124 | `archive_entry_set_nlink` | `0xB9650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `archive_entry_set_pathname_utf8` | `0xB9660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `archive_entry_set_perm` | `0xB9680` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `archive_entry_set_rdev` | `0xB96C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `archive_entry_set_symlink_type` | `0xB96F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `archive_entry_set_symlink_utf8` | `0xB9700` | 76 | UnwindData |  |
| 135 | `archive_entry_set_uid` | `0xB9760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `archive_entry_set_uname_utf8` | `0xB9780` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `archive_entry_size_is_set` | `0xB97A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `archive_entry_sourcepath` | `0xB97C0` | 79 | UnwindData |  |
| 141 | `archive_entry_sourcepath_w` | `0xB9820` | 51 | UnwindData |  |
| 149 | `archive_entry_symlink` | `0xB9860` | 88 | UnwindData |  |
| 150 | `archive_entry_symlink_type` | `0xB98C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | `archive_entry_symlink_utf8` | `0xB98D0` | 88 | UnwindData |  |
| 152 | `archive_entry_symlink_w` | `0xB9930` | 88 | UnwindData |  |
| 153 | `archive_entry_uid` | `0xB9990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `archive_entry_uid_is_set` | `0xB99A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `archive_entry_uname` | `0xB99C0` | 79 | UnwindData |  |
| 156 | `archive_entry_uname_utf8` | `0xB9A20` | 79 | UnwindData |  |
| 157 | `archive_entry_uname_w` | `0xB9A80` | 79 | UnwindData |  |
| 158 | `archive_entry_unset_atime` | `0xB9AE0` | 33 | UnwindData |  |
| 159 | `archive_entry_unset_birthtime` | `0xB9B10` | 33 | UnwindData |  |
| 160 | `archive_entry_unset_ctime` | `0xB9B40` | 33 | UnwindData |  |
| 161 | `archive_entry_unset_mtime` | `0xB9B70` | 33 | UnwindData |  |
| 162 | `archive_entry_unset_size` | `0xB9BA0` | 30 | UnwindData |  |
| 163 | `archive_entry_update_gname_utf8` | `0xB9BD0` | 71 | UnwindData |  |
| 164 | `archive_entry_update_hardlink_utf8` | `0xB9C20` | 109 | UnwindData |  |
| 165 | `archive_entry_update_link_utf8` | `0xB9CA0` | 97 | UnwindData |  |
| 167 | `archive_entry_update_symlink_utf8` | `0xB9D10` | 112 | UnwindData |  |
| 168 | `archive_entry_update_uname_utf8` | `0xB9D90` | 71 | UnwindData |  |
| 30 | `archive_entry_copy_bhfi` | `0xB9DE0` | 279 | UnwindData |  |
| 45 | `archive_entry_copy_stat` | `0xB9F00` | 251 | UnwindData |  |
| 78 | `archive_entry_linkify` | `0xBA010` | 422 | UnwindData |  |
| 80 | `archive_entry_linkresolver_new` | `0xBA1C0` | 99 | UnwindData |  |
| 81 | `archive_entry_linkresolver_set_strategy` | `0xBA230` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `archive_entry_partial_links` | `0xBA2B0` | 131 | UnwindData |  |
| 142 | `archive_entry_sparse_add_entry` | `0xBA6D0` | 215 | UnwindData |  |
| 144 | `archive_entry_sparse_count` | `0xBA7B0` | 70 | UnwindData |  |
| 145 | `archive_entry_sparse_next` | `0xBA800` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `archive_entry_sparse_reset` | `0xBA850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `archive_entry_stat` | `0xBA870` | 199 | UnwindData |  |
| 148 | `archive_entry_strmode` | `0xBA940` | 281 | UnwindData |  |
| 169 | `archive_entry_xattr_add_entry` | `0xBAA60` | 203 | UnwindData |  |
| 171 | `archive_entry_xattr_count` | `0xBAB40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 172 | `archive_entry_xattr_next` | `0xBAB60` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 173 | `archive_entry_xattr_reset` | `0xBABC0` | 2,416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 198 | `archive_match_exclude_entry` | `0xBB530` | 129 | UnwindData |  |
| 199 | `archive_match_exclude_pattern` | `0xBB5C0` | 113 | UnwindData |  |
| 200 | `archive_match_exclude_pattern_from_file` | `0xBB640` | 99 | UnwindData |  |
| 201 | `archive_match_exclude_pattern_from_file_w` | `0xBB6B0` | 96 | UnwindData |  |
| 202 | `archive_match_exclude_pattern_w` | `0xBB720` | 115 | UnwindData |  |
| 204 | `archive_match_free` | `0xBB7A0` | 225 | UnwindData |  |
| 205 | `archive_match_include_date` | `0xBB890` | 148 | UnwindData |  |
| 206 | `archive_match_include_date_w` | `0xBB930` | 69 | UnwindData |  |
| 207 | `archive_match_include_file_time` | `0xBB980` | 69 | UnwindData |  |
| 208 | `archive_match_include_file_time_w` | `0xBB9D0` | 69 | UnwindData |  |
| 209 | `archive_match_include_gid` | `0xBBA20` | 76 | UnwindData |  |
| 210 | `archive_match_include_gname` | `0xBBA80` | 82 | UnwindData |  |
| 211 | `archive_match_include_gname_w` | `0xBBAE0` | 79 | UnwindData |  |
| 212 | `archive_match_include_pattern` | `0xBBB40` | 113 | UnwindData |  |
| 213 | `archive_match_include_pattern_from_file` | `0xBBBC0` | 99 | UnwindData |  |
| 214 | `archive_match_include_pattern_from_file_w` | `0xBBC30` | 96 | UnwindData |  |
| 215 | `archive_match_include_pattern_w` | `0xBBCA0` | 115 | UnwindData |  |
| 216 | `archive_match_include_time` | `0xBBD20` | 94 | UnwindData |  |
| 217 | `archive_match_include_uid` | `0xBBD90` | 76 | UnwindData |  |
| 218 | `archive_match_include_uname` | `0xBBDF0` | 82 | UnwindData |  |
| 219 | `archive_match_include_uname_w` | `0xBBE50` | 79 | UnwindData |  |
| 220 | `archive_match_new` | `0xBBEB0` | 184 | UnwindData |  |
| 221 | `archive_match_owner_excluded` | `0xBBF70` | 110 | UnwindData |  |
| 222 | `archive_match_path_excluded` | `0xBBFF0` | 118 | UnwindData |  |
| 223 | `archive_match_path_unmatched_inclusions` | `0xBC070` | 66 | UnwindData |  |
| 224 | `archive_match_path_unmatched_inclusions_next` | `0xBC0C0` | 98 | UnwindData |  |
| 225 | `archive_match_path_unmatched_inclusions_next_w` | `0xBC130` | 95 | UnwindData |  |
| 226 | `archive_match_set_inclusion_recursion` | `0xBC1A0` | 65 | UnwindData |  |
| 227 | `archive_match_time_excluded` | `0xBC1F0` | 110 | UnwindData |  |
| 231 | `archive_parse_date` | `0xBDBD0` | 863 | UnwindData |  |
| 234 | `archive_read_add_callback_data` | `0xC2D80` | 294 | UnwindData |  |
| 236 | `archive_read_append_callback_data` | `0xC2EB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 241 | `archive_read_data` | `0xC2ED0` | 377 | UnwindData |  |
| 269 | `archive_read_extract_set_skip_file` | `0xC3050` | 92 | UnwindData |  |
| 271 | `archive_read_format_capabilities` | `0xC30C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 273 | `archive_read_has_encrypted_entries` | `0xC30F0` | 77 | UnwindData |  |
| 274 | `archive_read_header_position` | `0xC3150` | 58 | UnwindData |  |
| 275 | `archive_read_new` | `0xC3190` | 99 | UnwindData |  |
| 278 | `archive_read_open` | `0xC3200` | 93 | UnwindData |  |
| 279 | `archive_read_open1` | `0xC3270` | 426 | UnwindData |  |
| 280 | `archive_read_open2` | `0xC3420` | 103 | UnwindData |  |
| 290 | `archive_read_prepend_callback_data` | `0xC3490` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 291 | `archive_read_set_callback_data` | `0xC34A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 292 | `archive_read_set_callback_data2` | `0xC34B0` | 220 | UnwindData |  |
| 297 | `archive_read_set_open_callback` | `0xC35A0` | 67 | UnwindData |  |
| 301 | `archive_read_set_read_callback` | `0xC35F0` | 67 | UnwindData |  |
| 302 | `archive_read_set_seek_callback` | `0xC3640` | 67 | UnwindData |  |
| 303 | `archive_read_set_skip_callback` | `0xC3690` | 67 | UnwindData |  |
| 304 | `archive_read_set_switch_callback` | `0xC36E0` | 67 | UnwindData |  |
| 355 | `archive_seek_data` | `0xC3730` | 125 | UnwindData |  |
| 235 | `archive_read_add_passphrase` | `0xC3E40` | 141 | UnwindData |  |
| 300 | `archive_read_set_passphrase_callback` | `0xC3EE0` | 87 | UnwindData |  |
| 237 | `archive_read_append_filter` | `0xC3FF0` | 833 | UnwindData |  |
| 238 | `archive_read_append_filter_program` | `0xC4340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 239 | `archive_read_append_filter_program_signature` | `0xC4360` | 230 | UnwindData |  |
| 243 | `archive_read_data_into_fd` | `0xC4450` | 467 | UnwindData |  |
| 260 | `archive_read_disk_set_standard_lookup` | `0xC4700` | 30 | UnwindData |  |
| 245 | `archive_read_disk_can_descend` | `0xC4DB0` | 74 | UnwindData |  |
| 246 | `archive_read_disk_current_filesystem` | `0xC4E00` | 59 | UnwindData |  |
| 247 | `archive_read_disk_current_filesystem_is_remote` | `0xC4E50` | 63 | UnwindData |  |
| 248 | `archive_read_disk_current_filesystem_is_synthetic` | `0xC4EA0` | 63 | UnwindData |  |
| 249 | `archive_read_disk_descend` | `0xC4EF0` | 281 | UnwindData |  |
| 250 | `archive_read_disk_entry_from_file` | `0xC5010` | 1,188 | UnwindData |  |
| 251 | `archive_read_disk_gname` | `0xC54C0` | 86 | UnwindData |  |
| 252 | `archive_read_disk_new` | `0xC5520` | 123 | UnwindData |  |
| 253 | `archive_read_disk_open` | `0xC55B0` | 259 | UnwindData |  |
| 254 | `archive_read_disk_open_w` | `0xC56C0` | 82 | UnwindData |  |
| 255 | `archive_read_disk_set_atime_restored` | `0xC5720` | 75 | UnwindData |  |
| 256 | `archive_read_disk_set_behavior` | `0xC5780` | 115 | UnwindData |  |
| 257 | `archive_read_disk_set_gname_lookup` | `0xC5800` | 136 | UnwindData |  |
| 258 | `archive_read_disk_set_matching` | `0xC5890` | 107 | UnwindData |  |
| 259 | `archive_read_disk_set_metadata_filter_callback` | `0xC5910` | 87 | UnwindData |  |
| 261 | `archive_read_disk_set_symlink_hybrid` | `0xC5970` | 61 | UnwindData |  |
| 262 | `archive_read_disk_set_symlink_logical` | `0xC59C0` | 61 | UnwindData |  |
| 263 | `archive_read_disk_set_symlink_physical` | `0xC5A10` | 61 | UnwindData |  |
| 264 | `archive_read_disk_set_uname_lookup` | `0xC5A60` | 136 | UnwindData |  |
| 265 | `archive_read_disk_uname` | `0xC5AF0` | 86 | UnwindData |  |
| 4 | `archive_commoncrypto_version` | `0xC7FD0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | `archive_libacl_version` | `0xC7FD0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `archive_libattr_version` | `0xC7FD0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `archive_libbsdxml_version` | `0xC7FD0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 187 | `archive_libexpat_version` | `0xC7FD0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 188 | `archive_libiconv_version` | `0xC7FD0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 189 | `archive_liblz4_version` | `0xC7FD0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 191 | `archive_liblzo2_version` | `0xC7FD0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 192 | `archive_libmd_version` | `0xC7FD0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 193 | `archive_libpcre2_version` | `0xC7FD0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 194 | `archive_libpcre_version` | `0xC7FD0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 195 | `archive_librichacl_version` | `0xC7FD0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 196 | `archive_libxml2_version` | `0xC7FD0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 228 | `archive_mbedtls_version` | `0xC7FD0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 229 | `archive_nettle_version` | `0xC7FD0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 230 | `archive_openssl_version` | `0xC7FD0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 361 | `archive_wincrypt_version` | `0xC7FD0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 374 | `archive_write_add_filter_none` | `0xC7FD0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 413 | `archive_write_set_compression_none` | `0xC7FD0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 266 | `archive_read_extract` | `0xC8120` | 141 | UnwindData |  |
| 267 | `archive_read_extract2` | `0xC8220` | 203 | UnwindData |  |
| 268 | `archive_read_extract_set_progress_callback` | `0xC8360` | 46 | UnwindData |  |
| 282 | `archive_read_open_fd` | `0xC8460` | 420 | UnwindData |  |
| 281 | `archive_read_open_FILE` | `0xC8A70` | 408 | UnwindData |  |
| 283 | `archive_read_open_file` | `0xC8C10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 284 | `archive_read_open_filename` | `0xC8C20` | 31 | UnwindData |  |
| 285 | `archive_read_open_filename_w` | `0xC8C50` | 31 | UnwindData |  |
| 286 | `archive_read_open_filenames` | `0xC8C80` | 406 | UnwindData |  |
| 287 | `archive_read_open_filenames_w` | `0xC8E20` | 403 | UnwindData |  |
| 288 | `archive_read_open_memory` | `0xC93B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 289 | `archive_read_open_memory2` | `0xC93C0` | 229 | UnwindData |  |
| 295 | `archive_read_set_format` | `0xC95B0` | 562 | UnwindData |  |
| 294 | `archive_read_set_filter_option` | `0xC97F0` | 47 | UnwindData |  |
| 296 | `archive_read_set_format_option` | `0xC9830` | 47 | UnwindData |  |
| 298 | `archive_read_set_option` | `0xC9870` | 47 | UnwindData |  |
| 299 | `archive_read_set_options` | `0xC98B0` | 40 | UnwindData |  |
| 305 | `archive_read_support_compression_all` | `0xC9A10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 317 | `archive_read_support_filter_all` | `0xC9A20` | 214 | UnwindData |  |
| 318 | `archive_read_support_filter_by_code` | `0xC9B00` | 327 | UnwindData |  |
| 306 | `archive_read_support_compression_bzip2` | `0xC9C50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 319 | `archive_read_support_filter_bzip2` | `0xC9C60` | 38 | UnwindData |  |
| 307 | `archive_read_support_compression_compress` | `0xCA050` | 1,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 320 | `archive_read_support_filter_compress` | `0xCA050` | 1,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 321 | `archive_read_support_filter_grzip` | `0xCA600` | 67 | UnwindData |  |
| 308 | `archive_read_support_compression_gzip` | `0xCA6F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 322 | `archive_read_support_filter_gzip` | `0xCA700` | 38 | UnwindData |  |
| 323 | `archive_read_support_filter_lrzip` | `0xCAC60` | 71 | UnwindData |  |
| 324 | `archive_read_support_filter_lz4` | `0xCAD50` | 71 | UnwindData |  |
| 327 | `archive_read_support_filter_lzop` | `0xCAF70` | 67 | UnwindData |  |
| 311 | `archive_read_support_compression_none` | `0xCB070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 328 | `archive_read_support_filter_none` | `0xCB080` | 45 | UnwindData |  |
| 312 | `archive_read_support_compression_program` | `0xCB280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 329 | `archive_read_support_filter_program` | `0xCB280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 313 | `archive_read_support_compression_program_signature` | `0xCB2A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 330 | `archive_read_support_filter_program_signature` | `0xCB2B0` | 236 | UnwindData |  |
| 314 | `archive_read_support_compression_rpm` | `0xCB8B0` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 331 | `archive_read_support_filter_rpm` | `0xCB8B0` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 315 | `archive_read_support_compression_uu` | `0xCBC90` | 3,632 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 332 | `archive_read_support_filter_uu` | `0xCBC90` | 3,632 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 309 | `archive_read_support_compression_lzip` | `0xCCAC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 310 | `archive_read_support_compression_lzma` | `0xCCAD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 316 | `archive_read_support_compression_xz` | `0xCCAE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 325 | `archive_read_support_filter_lzip` | `0xCCAF0` | 38 | UnwindData |  |
| 326 | `archive_read_support_filter_lzma` | `0xCCB20` | 38 | UnwindData |  |
| 333 | `archive_read_support_filter_xz` | `0xCCB50` | 38 | UnwindData |  |
| 334 | `archive_read_support_filter_zstd` | `0xCD560` | 38 | UnwindData |  |
| 338 | `archive_read_support_format_by_code` | `0xD2640` | 411 | UnwindData |  |
| 348 | `archive_read_support_format_raw` | `0xE4E00` | 230 | UnwindData |  |
| 342 | `archive_read_support_format_gnutar` | `0xE54C0` | 57 | UnwindData |  |
| 353 | `archive_read_support_format_zip_seekable` | `0xEE300` | 264 | UnwindData |  |
| 5 | `archive_compression` | `0xF45E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `archive_compression_name` | `0xF45F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `archive_copy_error` | `0xF4600` | 57 | UnwindData |  |
| 174 | `archive_errno` | `0xF4640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 175 | `archive_error_string` | `0xF4650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `archive_format` | `0xF4670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 232 | `archive_position_compressed` | `0xF4680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 233 | `archive_position_uncompressed` | `0xF4690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 357 | `archive_utility_string_sort` | `0xF46A0` | 54 | UnwindData |  |
| 359 | `archive_version_number` | `0xF4710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 360 | `archive_version_string` | `0xF4720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `archive_bzlib_version` | `0xF4730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `archive_cng_version` | `0xF4740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `archive_liblzma_version` | `0xF4750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 197 | `archive_libzstd_version` | `0xF4760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 358 | `archive_version_details` | `0xF4770` | 418 | UnwindData |  |
| 455 | `archive_zlib_version` | `0xF4920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 177 | `archive_filter_bytes` | `0xF4930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 178 | `archive_filter_code` | `0xF4950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `archive_filter_count` | `0xF4970` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 180 | `archive_filter_name` | `0xF4990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `archive_free` | `0xF49B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 240 | `archive_read_close` | `0xF49D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 379 | `archive_write_close` | `0xF49D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 270 | `archive_read_finish` | `0xF49F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 272 | `archive_read_free` | `0xF49F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 391 | `archive_write_finish` | `0xF49F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 393 | `archive_write_free` | `0xF49F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 277 | `archive_read_next_header2` | `0xF4A00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 381 | `archive_write_data_block` | `0xF4A20` | 65 | UnwindData |  |
| 390 | `archive_write_fail` | `0xF4A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 392 | `archive_write_finish_entry` | `0xF4A80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 396 | `archive_write_header` | `0xF4AA0` | 5,872 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 394 | `archive_write_get_bytes_in_last_block` | `0xF6190` | 55 | UnwindData |  |
| 395 | `archive_write_get_bytes_per_block` | `0xF61D0` | 62 | UnwindData |  |
| 397 | `archive_write_new` | `0xF6220` | 149 | UnwindData |  |
| 398 | `archive_write_open` | `0xF62C0` | 31 | UnwindData |  |
| 399 | `archive_write_open2` | `0xF62F0` | 284 | UnwindData |  |
| 406 | `archive_write_set_bytes_in_last_block` | `0xF6420` | 65 | UnwindData |  |
| 407 | `archive_write_set_bytes_per_block` | `0xF6470` | 69 | UnwindData |  |
| 448 | `archive_write_set_skip_file` | `0xF64C0` | 97 | UnwindData |  |
| 362 | `archive_write_add_filter` | `0xF6560` | 83 | UnwindData |  |
| 363 | `archive_write_add_filter_b64encode` | `0xF69D0` | 237 | UnwindData |  |
| 364 | `archive_write_add_filter_by_name` | `0xF6C20` | 143 | UnwindData |  |
| 365 | `archive_write_add_filter_bzip2` | `0xF6FB0` | 190 | UnwindData |  |
| 408 | `archive_write_set_compression_bzip2` | `0xF7080` | 27 | UnwindData |  |
| 366 | `archive_write_add_filter_compress` | `0xF75F0` | 97 | UnwindData |  |
| 409 | `archive_write_set_compression_compress` | `0xF7660` | 27 | UnwindData |  |
| 367 | `archive_write_add_filter_grzip` | `0xF7860` | 281 | UnwindData |  |
| 368 | `archive_write_add_filter_gzip` | `0xF7F20` | 194 | UnwindData |  |
| 410 | `archive_write_set_compression_gzip` | `0xF7FF0` | 27 | UnwindData |  |
| 369 | `archive_write_add_filter_lrzip` | `0xF80D0` | 281 | UnwindData |  |
| 370 | `archive_write_add_filter_lz4` | `0xF8740` | 280 | UnwindData |  |
| 373 | `archive_write_add_filter_lzop` | `0xF8860` | 273 | UnwindData |  |
| 375 | `archive_write_add_filter_program` | `0xF8E80` | 357 | UnwindData |  |
| 414 | `archive_write_set_compression_program` | `0xF8FF0` | 42 | UnwindData |  |
| 376 | `archive_write_add_filter_uuencode` | `0xF9430` | 235 | UnwindData |  |
| 371 | `archive_write_add_filter_lzip` | `0xF9DD0` | 87 | UnwindData |  |
| 372 | `archive_write_add_filter_lzma` | `0xF9E30` | 87 | UnwindData |  |
| 377 | `archive_write_add_filter_xz` | `0xF9E90` | 87 | UnwindData |  |
| 411 | `archive_write_set_compression_lzip` | `0xF9EF0` | 27 | UnwindData |  |
| 412 | `archive_write_set_compression_lzma` | `0xF9F20` | 27 | UnwindData |  |
| 415 | `archive_write_set_compression_xz` | `0xF9F50` | 27 | UnwindData |  |
| 378 | `archive_write_add_filter_zstd` | `0xFA630` | 306 | UnwindData |  |
| 387 | `archive_write_disk_set_standard_lookup` | `0xFAAA0` | 179 | UnwindData |  |
| 382 | `archive_write_disk_gid` | `0xFB8E0` | 113 | UnwindData |  |
| 383 | `archive_write_disk_new` | `0xFB960` | 206 | UnwindData |  |
| 384 | `archive_write_disk_set_group_lookup` | `0xFBA40` | 136 | UnwindData |  |
| 385 | `archive_write_disk_set_options` | `0xFBAD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 386 | `archive_write_disk_set_skip_file` | `0xFBAE0` | 97 | UnwindData |  |
| 388 | `archive_write_disk_set_user_lookup` | `0xFBB50` | 136 | UnwindData |  |
| 389 | `archive_write_disk_uid` | `0xFBBE0` | 113 | UnwindData |  |
| 401 | `archive_write_open_fd` | `0xFE860` | 149 | UnwindData |  |
| 400 | `archive_write_open_FILE` | `0xFEAA0` | 121 | UnwindData |  |
| 402 | `archive_write_open_file` | `0xFEB90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 403 | `archive_write_open_filename` | `0xFEBA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 404 | `archive_write_open_filename_w` | `0xFEBD0` | 912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 405 | `archive_write_open_memory` | `0xFEF60` | 159 | UnwindData |  |
| 417 | `archive_write_set_format` | `0xFF1B0` | 83 | UnwindData |  |
| 418 | `archive_write_set_format_7zip` | `0xFFDE0` | 343 | UnwindData |  |
| 419 | `archive_write_set_format_ar_bsd` | `0x102570` | 76 | UnwindData |  |
| 420 | `archive_write_set_format_ar_svr4` | `0x1025D0` | 76 | UnwindData |  |
| 421 | `archive_write_set_format_by_name` | `0x1027A0` | 143 | UnwindData |  |
| 422 | `archive_write_set_format_cpio` | `0x102840` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 423 | `archive_write_set_format_cpio_bin` | `0x102B40` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 426 | `archive_write_set_format_cpio_pwb` | `0x102C80` | 1,808 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 425 | `archive_write_set_format_cpio_odc` | `0x103390` | 244 | UnwindData |  |
| 424 | `archive_write_set_format_cpio_newc` | `0x103B90` | 244 | UnwindData |  |
| 427 | `archive_write_set_format_filter_by_ext` | `0x104200` | 127 | UnwindData |  |
| 428 | `archive_write_set_format_filter_by_ext_def` | `0x104290` | 145 | UnwindData |  |
| 429 | `archive_write_set_format_gnutar` | `0x105080` | 191 | UnwindData |  |
| 430 | `archive_write_set_format_iso9660` | `0x1058E0` | 983 | UnwindData |  |
| 431 | `archive_write_set_format_mtree` | `0x10F0A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 432 | `archive_write_set_format_mtree_classic` | `0x10F0C0` | 54 | UnwindData |  |
| 434 | `archive_write_set_format_pax` | `0x113BC0` | 251 | UnwindData |  |
| 435 | `archive_write_set_format_pax_restricted` | `0x113CD0` | 72 | UnwindData |  |
| 436 | `archive_write_set_format_raw` | `0x114710` | 229 | UnwindData |  |
| 437 | `archive_write_set_format_shar` | `0x114930` | 261 | UnwindData |  |
| 438 | `archive_write_set_format_shar_dump` | `0x114A40` | 68 | UnwindData |  |
| 439 | `archive_write_set_format_ustar` | `0x115E10` | 244 | UnwindData |  |
| 440 | `archive_write_set_format_v7tar` | `0x116350` | 237 | UnwindData |  |
| 441 | `archive_write_set_format_warc` | `0x117160` | 286 | UnwindData |  |
| 442 | `archive_write_set_format_xar` | `0x117340` | 512 | UnwindData |  |
| 443 | `archive_write_set_format_zip` | `0x11B800` | 367 | UnwindData |  |
| 449 | `archive_write_zip_set_compression_bzip2` | `0x11DC50` | 107 | UnwindData |  |
| 450 | `archive_write_zip_set_compression_deflate` | `0x11DCD0` | 107 | UnwindData |  |
| 451 | `archive_write_zip_set_compression_lzma` | `0x11DD50` | 107 | UnwindData |  |
| 452 | `archive_write_zip_set_compression_store` | `0x11DDD0` | 113 | UnwindData |  |
| 453 | `archive_write_zip_set_compression_xz` | `0x11DE50` | 107 | UnwindData |  |
| 454 | `archive_write_zip_set_compression_zstd` | `0x11DED0` | 107 | UnwindData |  |
| 416 | `archive_write_set_filter_option` | `0x11E770` | 47 | UnwindData |  |
| 433 | `archive_write_set_format_option` | `0x11E7B0` | 47 | UnwindData |  |
| 444 | `archive_write_set_option` | `0x11E7F0` | 47 | UnwindData |  |
| 445 | `archive_write_set_options` | `0x11E830` | 40 | UnwindData |  |
| 446 | `archive_write_set_passphrase` | `0x11E8C0` | 69 | UnwindData |  |
| 447 | `archive_write_set_passphrase_callback` | `0x11E910` | 87 | UnwindData |  |
