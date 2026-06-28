# Binary Specification: archiveint.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\archiveint.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6654eec3789010fa86fd0eecc5a5f2b4ae187de6c687d55a54577c3c17e74a35`
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
| 103 | `archive_entry_set_dev` | `0x1A190` | 637,216 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `archive_entry_acl` | `0xB5AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `archive_entry_acl_add_entry` | `0xB5AC0` | 102 | UnwindData |  |
| 10 | `archive_entry_acl_add_entry_w` | `0xB5B30` | 60 | UnwindData |  |
| 11 | `archive_entry_acl_clear` | `0xB5B80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `archive_entry_acl_count` | `0xB5BA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `archive_entry_acl_from_text` | `0xB5BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `archive_entry_acl_from_text_w` | `0xB5BE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `archive_entry_acl_next` | `0xB5C00` | 112 | UnwindData |  |
| 16 | `archive_entry_acl_reset` | `0xB5C80` | 64 | UnwindData |  |
| 17 | `archive_entry_acl_text` | `0xB5CD0` | 94 | UnwindData |  |
| 18 | `archive_entry_acl_text_w` | `0xB5D70` | 94 | UnwindData |  |
| 19 | `archive_entry_acl_to_text` | `0xB5DE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `archive_entry_acl_to_text_w` | `0xB5E00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `archive_entry_acl_types` | `0xB5E20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `archive_entry_atime` | `0xB5E30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 182 | `archive_format_name` | `0xB5E30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `archive_entry_atime_nsec` | `0xB5E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `archive_file_count` | `0xB5E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `archive_entry_birthtime` | `0xB5E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `archive_entry_birthtime_nsec` | `0xB5E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `archive_entry_clone` | `0xB5E70` | 619 | UnwindData |  |
| 31 | `archive_entry_copy_fflags_text` | `0xB60F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `archive_entry_copy_fflags_text_len` | `0xB6110` | 76 | UnwindData |  |
| 33 | `archive_entry_copy_fflags_text_w` | `0xB6170` | 60 | UnwindData |  |
| 34 | `archive_entry_copy_gname` | `0xB61C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `archive_entry_set_gname` | `0xB61C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `archive_entry_copy_gname_w` | `0xB61E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `archive_entry_copy_hardlink` | `0xB6200` | 71 | UnwindData |  |
| 37 | `archive_entry_copy_hardlink_w` | `0xB6250` | 71 | UnwindData |  |
| 38 | `archive_entry_copy_link` | `0xB62A0` | 47 | UnwindData |  |
| 118 | `archive_entry_set_link` | `0xB62A0` | 47 | UnwindData |  |
| 39 | `archive_entry_copy_link_w` | `0xB62E0` | 47 | UnwindData |  |
| 41 | `archive_entry_copy_pathname` | `0xB6320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `archive_entry_set_pathname` | `0xB6320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `archive_entry_copy_pathname_w` | `0xB6340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `archive_entry_copy_sourcepath` | `0xB6360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `archive_entry_copy_sourcepath_w` | `0xB6380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `archive_entry_copy_symlink` | `0xB63A0` | 76 | UnwindData |  |
| 132 | `archive_entry_set_symlink` | `0xB63A0` | 76 | UnwindData |  |
| 47 | `archive_entry_copy_symlink_w` | `0xB6400` | 76 | UnwindData |  |
| 48 | `archive_entry_copy_uname` | `0xB6460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `archive_entry_set_uname` | `0xB6460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `archive_entry_copy_uname_w` | `0xB6480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `archive_entry_ctime` | `0xB64A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `archive_entry_ctime_is_set` | `0xB64B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `archive_entry_ctime_nsec` | `0xB64D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `archive_entry_dev` | `0xB64E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `archive_entry_dev_is_set` | `0xB6520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `archive_entry_devmajor` | `0xB6540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `archive_entry_devminor` | `0xB6560` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `archive_entry_digest` | `0xB6590` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `archive_entry_fflags` | `0xB65F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `archive_entry_fflags_text` | `0xB6610` | 237 | UnwindData |  |
| 61 | `archive_entry_filetype_is_set` | `0xB6710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `archive_entry_free` | `0xB6730` | 34 | UnwindData |  |
| 63 | `archive_entry_gid` | `0xB6760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `archive_entry_gid_is_set` | `0xB6770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `archive_entry_gname` | `0xB6790` | 79 | UnwindData |  |
| 66 | `archive_entry_gname_utf8` | `0xB67F0` | 79 | UnwindData |  |
| 67 | `archive_entry_gname_w` | `0xB6850` | 79 | UnwindData |  |
| 68 | `archive_entry_hardlink` | `0xB68B0` | 88 | UnwindData |  |
| 69 | `archive_entry_hardlink_is_set` | `0xB6910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `archive_entry_hardlink_utf8` | `0xB6930` | 88 | UnwindData |  |
| 71 | `archive_entry_hardlink_w` | `0xB6990` | 88 | UnwindData |  |
| 72 | `archive_entry_ino` | `0xB69F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `archive_entry_ino64` | `0xB69F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `archive_entry_ino_is_set` | `0xB6A00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `archive_entry_is_data_encrypted` | `0xB6A20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `archive_entry_is_encrypted` | `0xB6A40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `archive_entry_is_metadata_encrypted` | `0xB6A60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `archive_entry_mac_metadata` | `0xB6A80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `archive_entry_mode` | `0xB6AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `archive_entry_mtime_is_set` | `0xB6AB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `archive_entry_new` | `0xB6AD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `archive_entry_new2` | `0xB6AE0` | 53 | UnwindData |  |
| 89 | `archive_entry_nlink` | `0xB6B20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `archive_entry_pathname` | `0xB6B30` | 134 | UnwindData |  |
| 92 | `archive_entry_pathname_utf8` | `0xB6BC0` | 79 | UnwindData |  |
| 94 | `archive_entry_perm` | `0xB6C20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `archive_entry_perm_is_set` | `0xB6C40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `archive_entry_rdev` | `0xB6C60` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `archive_entry_rdev_is_set` | `0xB6CB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `archive_entry_rdevmajor` | `0xB6CD0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `archive_entry_rdevminor` | `0xB6D00` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `archive_entry_set_birthtime` | `0xB6D40` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `archive_entry_set_devmajor` | `0xB6DA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `archive_entry_set_devminor` | `0xB6DD0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `archive_entry_set_digest` | `0xB6E00` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `archive_entry_set_fflags` | `0xB6F20` | 64 | UnwindData |  |
| 109 | `archive_entry_set_gid` | `0xB6F70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `archive_entry_set_gname_utf8` | `0xB6F90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `archive_entry_set_hardlink` | `0xB6FB0` | 60 | UnwindData |  |
| 113 | `archive_entry_set_hardlink_utf8` | `0xB7000` | 71 | UnwindData |  |
| 114 | `archive_entry_set_ino` | `0xB7050` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `archive_entry_set_ino64` | `0xB7050` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `archive_entry_set_is_data_encrypted` | `0xB7080` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `archive_entry_set_is_metadata_encrypted` | `0xB70B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `archive_entry_set_link_to_hardlink` | `0xB70E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `archive_entry_set_link_to_symlink` | `0xB7100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `archive_entry_set_link_utf8` | `0xB7120` | 47 | UnwindData |  |
| 124 | `archive_entry_set_nlink` | `0xB7160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `archive_entry_set_pathname_utf8` | `0xB7170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `archive_entry_set_perm` | `0xB7190` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `archive_entry_set_rdev` | `0xB71D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `archive_entry_set_symlink_type` | `0xB7200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `archive_entry_set_symlink_utf8` | `0xB7210` | 76 | UnwindData |  |
| 135 | `archive_entry_set_uid` | `0xB7270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `archive_entry_set_uname_utf8` | `0xB7290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `archive_entry_size_is_set` | `0xB72B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `archive_entry_sourcepath` | `0xB72D0` | 79 | UnwindData |  |
| 141 | `archive_entry_sourcepath_w` | `0xB7330` | 51 | UnwindData |  |
| 149 | `archive_entry_symlink` | `0xB7370` | 88 | UnwindData |  |
| 150 | `archive_entry_symlink_type` | `0xB73D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | `archive_entry_symlink_utf8` | `0xB73E0` | 88 | UnwindData |  |
| 152 | `archive_entry_symlink_w` | `0xB7440` | 88 | UnwindData |  |
| 153 | `archive_entry_uid` | `0xB74A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `archive_entry_uid_is_set` | `0xB74B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `archive_entry_uname` | `0xB74D0` | 79 | UnwindData |  |
| 156 | `archive_entry_uname_utf8` | `0xB7530` | 79 | UnwindData |  |
| 157 | `archive_entry_uname_w` | `0xB7590` | 79 | UnwindData |  |
| 158 | `archive_entry_unset_atime` | `0xB75F0` | 33 | UnwindData |  |
| 159 | `archive_entry_unset_birthtime` | `0xB7620` | 33 | UnwindData |  |
| 160 | `archive_entry_unset_ctime` | `0xB7650` | 33 | UnwindData |  |
| 161 | `archive_entry_unset_mtime` | `0xB7680` | 33 | UnwindData |  |
| 162 | `archive_entry_unset_size` | `0xB76B0` | 30 | UnwindData |  |
| 163 | `archive_entry_update_gname_utf8` | `0xB76E0` | 71 | UnwindData |  |
| 164 | `archive_entry_update_hardlink_utf8` | `0xB7730` | 109 | UnwindData |  |
| 165 | `archive_entry_update_link_utf8` | `0xB77B0` | 97 | UnwindData |  |
| 167 | `archive_entry_update_symlink_utf8` | `0xB7820` | 112 | UnwindData |  |
| 168 | `archive_entry_update_uname_utf8` | `0xB78A0` | 71 | UnwindData |  |
| 30 | `archive_entry_copy_bhfi` | `0xB78F0` | 279 | UnwindData |  |
| 45 | `archive_entry_copy_stat` | `0xB7A10` | 251 | UnwindData |  |
| 78 | `archive_entry_linkify` | `0xB7B20` | 422 | UnwindData |  |
| 80 | `archive_entry_linkresolver_new` | `0xB7CD0` | 99 | UnwindData |  |
| 81 | `archive_entry_linkresolver_set_strategy` | `0xB7D40` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `archive_entry_partial_links` | `0xB7DC0` | 131 | UnwindData |  |
| 142 | `archive_entry_sparse_add_entry` | `0xB81E0` | 215 | UnwindData |  |
| 144 | `archive_entry_sparse_count` | `0xB82C0` | 70 | UnwindData |  |
| 145 | `archive_entry_sparse_next` | `0xB8310` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `archive_entry_sparse_reset` | `0xB8360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `archive_entry_stat` | `0xB8380` | 199 | UnwindData |  |
| 148 | `archive_entry_strmode` | `0xB8450` | 281 | UnwindData |  |
| 169 | `archive_entry_xattr_add_entry` | `0xB8570` | 203 | UnwindData |  |
| 171 | `archive_entry_xattr_count` | `0xB8650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 172 | `archive_entry_xattr_next` | `0xB8670` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 173 | `archive_entry_xattr_reset` | `0xB86D0` | 2,416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 198 | `archive_match_exclude_entry` | `0xB9040` | 129 | UnwindData |  |
| 199 | `archive_match_exclude_pattern` | `0xB90D0` | 113 | UnwindData |  |
| 200 | `archive_match_exclude_pattern_from_file` | `0xB9150` | 99 | UnwindData |  |
| 201 | `archive_match_exclude_pattern_from_file_w` | `0xB91C0` | 96 | UnwindData |  |
| 202 | `archive_match_exclude_pattern_w` | `0xB9230` | 115 | UnwindData |  |
| 204 | `archive_match_free` | `0xB92B0` | 225 | UnwindData |  |
| 205 | `archive_match_include_date` | `0xB93A0` | 148 | UnwindData |  |
| 206 | `archive_match_include_date_w` | `0xB9440` | 69 | UnwindData |  |
| 207 | `archive_match_include_file_time` | `0xB9490` | 69 | UnwindData |  |
| 208 | `archive_match_include_file_time_w` | `0xB94E0` | 69 | UnwindData |  |
| 209 | `archive_match_include_gid` | `0xB9530` | 76 | UnwindData |  |
| 210 | `archive_match_include_gname` | `0xB9590` | 82 | UnwindData |  |
| 211 | `archive_match_include_gname_w` | `0xB95F0` | 79 | UnwindData |  |
| 212 | `archive_match_include_pattern` | `0xB9650` | 113 | UnwindData |  |
| 213 | `archive_match_include_pattern_from_file` | `0xB96D0` | 99 | UnwindData |  |
| 214 | `archive_match_include_pattern_from_file_w` | `0xB9740` | 96 | UnwindData |  |
| 215 | `archive_match_include_pattern_w` | `0xB97B0` | 115 | UnwindData |  |
| 216 | `archive_match_include_time` | `0xB9830` | 94 | UnwindData |  |
| 217 | `archive_match_include_uid` | `0xB98A0` | 76 | UnwindData |  |
| 218 | `archive_match_include_uname` | `0xB9900` | 82 | UnwindData |  |
| 219 | `archive_match_include_uname_w` | `0xB9960` | 79 | UnwindData |  |
| 220 | `archive_match_new` | `0xB99C0` | 184 | UnwindData |  |
| 221 | `archive_match_owner_excluded` | `0xB9A80` | 110 | UnwindData |  |
| 222 | `archive_match_path_excluded` | `0xB9B00` | 118 | UnwindData |  |
| 223 | `archive_match_path_unmatched_inclusions` | `0xB9B80` | 66 | UnwindData |  |
| 224 | `archive_match_path_unmatched_inclusions_next` | `0xB9BD0` | 98 | UnwindData |  |
| 225 | `archive_match_path_unmatched_inclusions_next_w` | `0xB9C40` | 95 | UnwindData |  |
| 226 | `archive_match_set_inclusion_recursion` | `0xB9CB0` | 65 | UnwindData |  |
| 227 | `archive_match_time_excluded` | `0xB9D00` | 110 | UnwindData |  |
| 231 | `archive_parse_date` | `0xBB6E0` | 863 | UnwindData |  |
| 234 | `archive_read_add_callback_data` | `0xC0890` | 294 | UnwindData |  |
| 236 | `archive_read_append_callback_data` | `0xC09C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 241 | `archive_read_data` | `0xC09E0` | 377 | UnwindData |  |
| 269 | `archive_read_extract_set_skip_file` | `0xC0B60` | 92 | UnwindData |  |
| 271 | `archive_read_format_capabilities` | `0xC0BD0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 273 | `archive_read_has_encrypted_entries` | `0xC0C00` | 77 | UnwindData |  |
| 274 | `archive_read_header_position` | `0xC0C60` | 58 | UnwindData |  |
| 275 | `archive_read_new` | `0xC0CA0` | 99 | UnwindData |  |
| 278 | `archive_read_open` | `0xC0D10` | 93 | UnwindData |  |
| 279 | `archive_read_open1` | `0xC0D80` | 426 | UnwindData |  |
| 280 | `archive_read_open2` | `0xC0F30` | 103 | UnwindData |  |
| 290 | `archive_read_prepend_callback_data` | `0xC0FA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 291 | `archive_read_set_callback_data` | `0xC0FB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 292 | `archive_read_set_callback_data2` | `0xC0FC0` | 220 | UnwindData |  |
| 297 | `archive_read_set_open_callback` | `0xC10B0` | 67 | UnwindData |  |
| 301 | `archive_read_set_read_callback` | `0xC1100` | 67 | UnwindData |  |
| 302 | `archive_read_set_seek_callback` | `0xC1150` | 67 | UnwindData |  |
| 303 | `archive_read_set_skip_callback` | `0xC11A0` | 67 | UnwindData |  |
| 304 | `archive_read_set_switch_callback` | `0xC11F0` | 67 | UnwindData |  |
| 355 | `archive_seek_data` | `0xC1240` | 125 | UnwindData |  |
| 235 | `archive_read_add_passphrase` | `0xC1950` | 141 | UnwindData |  |
| 300 | `archive_read_set_passphrase_callback` | `0xC19F0` | 87 | UnwindData |  |
| 237 | `archive_read_append_filter` | `0xC1B00` | 833 | UnwindData |  |
| 238 | `archive_read_append_filter_program` | `0xC1E50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 239 | `archive_read_append_filter_program_signature` | `0xC1E70` | 230 | UnwindData |  |
| 243 | `archive_read_data_into_fd` | `0xC1F60` | 467 | UnwindData |  |
| 260 | `archive_read_disk_set_standard_lookup` | `0xC2210` | 30 | UnwindData |  |
| 245 | `archive_read_disk_can_descend` | `0xC28C0` | 74 | UnwindData |  |
| 246 | `archive_read_disk_current_filesystem` | `0xC2910` | 59 | UnwindData |  |
| 247 | `archive_read_disk_current_filesystem_is_remote` | `0xC2960` | 63 | UnwindData |  |
| 248 | `archive_read_disk_current_filesystem_is_synthetic` | `0xC29B0` | 63 | UnwindData |  |
| 249 | `archive_read_disk_descend` | `0xC2A00` | 281 | UnwindData |  |
| 250 | `archive_read_disk_entry_from_file` | `0xC2B20` | 1,188 | UnwindData |  |
| 251 | `archive_read_disk_gname` | `0xC2FD0` | 86 | UnwindData |  |
| 252 | `archive_read_disk_new` | `0xC3030` | 123 | UnwindData |  |
| 253 | `archive_read_disk_open` | `0xC30C0` | 259 | UnwindData |  |
| 254 | `archive_read_disk_open_w` | `0xC31D0` | 82 | UnwindData |  |
| 255 | `archive_read_disk_set_atime_restored` | `0xC3230` | 75 | UnwindData |  |
| 256 | `archive_read_disk_set_behavior` | `0xC3290` | 115 | UnwindData |  |
| 257 | `archive_read_disk_set_gname_lookup` | `0xC3310` | 136 | UnwindData |  |
| 258 | `archive_read_disk_set_matching` | `0xC33A0` | 107 | UnwindData |  |
| 259 | `archive_read_disk_set_metadata_filter_callback` | `0xC3420` | 87 | UnwindData |  |
| 261 | `archive_read_disk_set_symlink_hybrid` | `0xC3480` | 61 | UnwindData |  |
| 262 | `archive_read_disk_set_symlink_logical` | `0xC34D0` | 61 | UnwindData |  |
| 263 | `archive_read_disk_set_symlink_physical` | `0xC3520` | 61 | UnwindData |  |
| 264 | `archive_read_disk_set_uname_lookup` | `0xC3570` | 136 | UnwindData |  |
| 265 | `archive_read_disk_uname` | `0xC3600` | 86 | UnwindData |  |
| 4 | `archive_commoncrypto_version` | `0xC5AE0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | `archive_libacl_version` | `0xC5AE0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `archive_libattr_version` | `0xC5AE0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `archive_libbsdxml_version` | `0xC5AE0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 187 | `archive_libexpat_version` | `0xC5AE0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 188 | `archive_libiconv_version` | `0xC5AE0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 189 | `archive_liblz4_version` | `0xC5AE0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 191 | `archive_liblzo2_version` | `0xC5AE0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 192 | `archive_libmd_version` | `0xC5AE0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 193 | `archive_libpcre2_version` | `0xC5AE0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 194 | `archive_libpcre_version` | `0xC5AE0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 195 | `archive_librichacl_version` | `0xC5AE0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 196 | `archive_libxml2_version` | `0xC5AE0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 228 | `archive_mbedtls_version` | `0xC5AE0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 229 | `archive_nettle_version` | `0xC5AE0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 230 | `archive_openssl_version` | `0xC5AE0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 361 | `archive_wincrypt_version` | `0xC5AE0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 374 | `archive_write_add_filter_none` | `0xC5AE0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 413 | `archive_write_set_compression_none` | `0xC5AE0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 266 | `archive_read_extract` | `0xC5C20` | 141 | UnwindData |  |
| 267 | `archive_read_extract2` | `0xC5D20` | 203 | UnwindData |  |
| 268 | `archive_read_extract_set_progress_callback` | `0xC5E60` | 46 | UnwindData |  |
| 282 | `archive_read_open_fd` | `0xC5F60` | 420 | UnwindData |  |
| 281 | `archive_read_open_FILE` | `0xC6570` | 408 | UnwindData |  |
| 283 | `archive_read_open_file` | `0xC6710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 284 | `archive_read_open_filename` | `0xC6720` | 31 | UnwindData |  |
| 285 | `archive_read_open_filename_w` | `0xC6750` | 31 | UnwindData |  |
| 286 | `archive_read_open_filenames` | `0xC6780` | 406 | UnwindData |  |
| 287 | `archive_read_open_filenames_w` | `0xC6920` | 403 | UnwindData |  |
| 288 | `archive_read_open_memory` | `0xC6EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 289 | `archive_read_open_memory2` | `0xC6EC0` | 229 | UnwindData |  |
| 295 | `archive_read_set_format` | `0xC70B0` | 562 | UnwindData |  |
| 294 | `archive_read_set_filter_option` | `0xC72F0` | 47 | UnwindData |  |
| 296 | `archive_read_set_format_option` | `0xC7330` | 47 | UnwindData |  |
| 298 | `archive_read_set_option` | `0xC7370` | 47 | UnwindData |  |
| 299 | `archive_read_set_options` | `0xC73B0` | 40 | UnwindData |  |
| 305 | `archive_read_support_compression_all` | `0xC7510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 317 | `archive_read_support_filter_all` | `0xC7520` | 214 | UnwindData |  |
| 318 | `archive_read_support_filter_by_code` | `0xC7600` | 327 | UnwindData |  |
| 306 | `archive_read_support_compression_bzip2` | `0xC7750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 319 | `archive_read_support_filter_bzip2` | `0xC7760` | 38 | UnwindData |  |
| 307 | `archive_read_support_compression_compress` | `0xC7B50` | 1,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 320 | `archive_read_support_filter_compress` | `0xC7B50` | 1,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 321 | `archive_read_support_filter_grzip` | `0xC8100` | 67 | UnwindData |  |
| 308 | `archive_read_support_compression_gzip` | `0xC81F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 322 | `archive_read_support_filter_gzip` | `0xC8200` | 38 | UnwindData |  |
| 323 | `archive_read_support_filter_lrzip` | `0xC8760` | 71 | UnwindData |  |
| 324 | `archive_read_support_filter_lz4` | `0xC8850` | 71 | UnwindData |  |
| 327 | `archive_read_support_filter_lzop` | `0xC8980` | 67 | UnwindData |  |
| 311 | `archive_read_support_compression_none` | `0xC8A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 328 | `archive_read_support_filter_none` | `0xC8A90` | 45 | UnwindData |  |
| 312 | `archive_read_support_compression_program` | `0xC8C90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 329 | `archive_read_support_filter_program` | `0xC8C90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 313 | `archive_read_support_compression_program_signature` | `0xC8CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 330 | `archive_read_support_filter_program_signature` | `0xC8CC0` | 236 | UnwindData |  |
| 314 | `archive_read_support_compression_rpm` | `0xC92C0` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 331 | `archive_read_support_filter_rpm` | `0xC92C0` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 315 | `archive_read_support_compression_uu` | `0xC96A0` | 3,632 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 332 | `archive_read_support_filter_uu` | `0xC96A0` | 3,632 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 309 | `archive_read_support_compression_lzip` | `0xCA4D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 310 | `archive_read_support_compression_lzma` | `0xCA4E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 316 | `archive_read_support_compression_xz` | `0xCA4F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 325 | `archive_read_support_filter_lzip` | `0xCA500` | 38 | UnwindData |  |
| 326 | `archive_read_support_filter_lzma` | `0xCA530` | 38 | UnwindData |  |
| 333 | `archive_read_support_filter_xz` | `0xCA560` | 38 | UnwindData |  |
| 334 | `archive_read_support_filter_zstd` | `0xCAF70` | 38 | UnwindData |  |
| 338 | `archive_read_support_format_by_code` | `0xCFF30` | 411 | UnwindData |  |
| 348 | `archive_read_support_format_raw` | `0xE26F0` | 230 | UnwindData |  |
| 342 | `archive_read_support_format_gnutar` | `0xE2DB0` | 57 | UnwindData |  |
| 353 | `archive_read_support_format_zip_seekable` | `0xEBBE0` | 264 | UnwindData |  |
| 5 | `archive_compression` | `0xF1EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `archive_compression_name` | `0xF1EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `archive_copy_error` | `0xF1ED0` | 57 | UnwindData |  |
| 174 | `archive_errno` | `0xF1F10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 175 | `archive_error_string` | `0xF1F20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `archive_format` | `0xF1F40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 232 | `archive_position_compressed` | `0xF1F50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 233 | `archive_position_uncompressed` | `0xF1F60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 357 | `archive_utility_string_sort` | `0xF1F70` | 54 | UnwindData |  |
| 359 | `archive_version_number` | `0xF1FE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 360 | `archive_version_string` | `0xF1FF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `archive_bzlib_version` | `0xF2000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `archive_cng_version` | `0xF2010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `archive_liblzma_version` | `0xF2020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 197 | `archive_libzstd_version` | `0xF2030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 358 | `archive_version_details` | `0xF2040` | 418 | UnwindData |  |
| 455 | `archive_zlib_version` | `0xF21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 177 | `archive_filter_bytes` | `0xF2200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 178 | `archive_filter_code` | `0xF2220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `archive_filter_count` | `0xF2240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 180 | `archive_filter_name` | `0xF2260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `archive_free` | `0xF2280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 240 | `archive_read_close` | `0xF22A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 379 | `archive_write_close` | `0xF22A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 270 | `archive_read_finish` | `0xF22C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 272 | `archive_read_free` | `0xF22C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 391 | `archive_write_finish` | `0xF22C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 393 | `archive_write_free` | `0xF22C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 277 | `archive_read_next_header2` | `0xF22D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 381 | `archive_write_data_block` | `0xF22F0` | 65 | UnwindData |  |
| 390 | `archive_write_fail` | `0xF2340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 392 | `archive_write_finish_entry` | `0xF2350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 396 | `archive_write_header` | `0xF2370` | 5,872 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 394 | `archive_write_get_bytes_in_last_block` | `0xF3A60` | 55 | UnwindData |  |
| 395 | `archive_write_get_bytes_per_block` | `0xF3AA0` | 62 | UnwindData |  |
| 397 | `archive_write_new` | `0xF3AF0` | 149 | UnwindData |  |
| 398 | `archive_write_open` | `0xF3B90` | 31 | UnwindData |  |
| 399 | `archive_write_open2` | `0xF3BC0` | 284 | UnwindData |  |
| 406 | `archive_write_set_bytes_in_last_block` | `0xF3CF0` | 65 | UnwindData |  |
| 407 | `archive_write_set_bytes_per_block` | `0xF3D40` | 69 | UnwindData |  |
| 448 | `archive_write_set_skip_file` | `0xF3D90` | 97 | UnwindData |  |
| 362 | `archive_write_add_filter` | `0xF3E30` | 83 | UnwindData |  |
| 363 | `archive_write_add_filter_b64encode` | `0xF42A0` | 237 | UnwindData |  |
| 364 | `archive_write_add_filter_by_name` | `0xF44F0` | 143 | UnwindData |  |
| 365 | `archive_write_add_filter_bzip2` | `0xF4880` | 190 | UnwindData |  |
| 408 | `archive_write_set_compression_bzip2` | `0xF4950` | 27 | UnwindData |  |
| 366 | `archive_write_add_filter_compress` | `0xF4EC0` | 97 | UnwindData |  |
| 409 | `archive_write_set_compression_compress` | `0xF4F30` | 27 | UnwindData |  |
| 367 | `archive_write_add_filter_grzip` | `0xF5130` | 281 | UnwindData |  |
| 368 | `archive_write_add_filter_gzip` | `0xF57F0` | 194 | UnwindData |  |
| 410 | `archive_write_set_compression_gzip` | `0xF58C0` | 27 | UnwindData |  |
| 369 | `archive_write_add_filter_lrzip` | `0xF59A0` | 281 | UnwindData |  |
| 370 | `archive_write_add_filter_lz4` | `0xF6010` | 280 | UnwindData |  |
| 373 | `archive_write_add_filter_lzop` | `0xF6130` | 273 | UnwindData |  |
| 375 | `archive_write_add_filter_program` | `0xF6750` | 357 | UnwindData |  |
| 414 | `archive_write_set_compression_program` | `0xF68C0` | 42 | UnwindData |  |
| 376 | `archive_write_add_filter_uuencode` | `0xF6D00` | 235 | UnwindData |  |
| 371 | `archive_write_add_filter_lzip` | `0xF76A0` | 87 | UnwindData |  |
| 372 | `archive_write_add_filter_lzma` | `0xF7700` | 87 | UnwindData |  |
| 377 | `archive_write_add_filter_xz` | `0xF7760` | 87 | UnwindData |  |
| 411 | `archive_write_set_compression_lzip` | `0xF77C0` | 27 | UnwindData |  |
| 412 | `archive_write_set_compression_lzma` | `0xF77F0` | 27 | UnwindData |  |
| 415 | `archive_write_set_compression_xz` | `0xF7820` | 27 | UnwindData |  |
| 378 | `archive_write_add_filter_zstd` | `0xF7F00` | 306 | UnwindData |  |
| 387 | `archive_write_disk_set_standard_lookup` | `0xF8370` | 179 | UnwindData |  |
| 382 | `archive_write_disk_gid` | `0xF91B0` | 113 | UnwindData |  |
| 383 | `archive_write_disk_new` | `0xF9230` | 206 | UnwindData |  |
| 384 | `archive_write_disk_set_group_lookup` | `0xF9310` | 136 | UnwindData |  |
| 385 | `archive_write_disk_set_options` | `0xF93A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 386 | `archive_write_disk_set_skip_file` | `0xF93B0` | 97 | UnwindData |  |
| 388 | `archive_write_disk_set_user_lookup` | `0xF9420` | 136 | UnwindData |  |
| 389 | `archive_write_disk_uid` | `0xF94B0` | 113 | UnwindData |  |
| 401 | `archive_write_open_fd` | `0xFC130` | 149 | UnwindData |  |
| 400 | `archive_write_open_FILE` | `0xFC370` | 121 | UnwindData |  |
| 402 | `archive_write_open_file` | `0xFC460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 403 | `archive_write_open_filename` | `0xFC470` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 404 | `archive_write_open_filename_w` | `0xFC4A0` | 880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 405 | `archive_write_open_memory` | `0xFC810` | 159 | UnwindData |  |
| 417 | `archive_write_set_format` | `0xFCA60` | 83 | UnwindData |  |
| 418 | `archive_write_set_format_7zip` | `0xFD690` | 343 | UnwindData |  |
| 419 | `archive_write_set_format_ar_bsd` | `0xFFE20` | 76 | UnwindData |  |
| 420 | `archive_write_set_format_ar_svr4` | `0xFFE80` | 76 | UnwindData |  |
| 421 | `archive_write_set_format_by_name` | `0x100050` | 143 | UnwindData |  |
| 422 | `archive_write_set_format_cpio` | `0x1000F0` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 423 | `archive_write_set_format_cpio_bin` | `0x1003F0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 426 | `archive_write_set_format_cpio_pwb` | `0x100530` | 1,808 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 425 | `archive_write_set_format_cpio_odc` | `0x100C40` | 244 | UnwindData |  |
| 424 | `archive_write_set_format_cpio_newc` | `0x101440` | 244 | UnwindData |  |
| 427 | `archive_write_set_format_filter_by_ext` | `0x101AB0` | 127 | UnwindData |  |
| 428 | `archive_write_set_format_filter_by_ext_def` | `0x101B40` | 145 | UnwindData |  |
| 429 | `archive_write_set_format_gnutar` | `0x102930` | 191 | UnwindData |  |
| 430 | `archive_write_set_format_iso9660` | `0x103190` | 983 | UnwindData |  |
| 431 | `archive_write_set_format_mtree` | `0x10C950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 432 | `archive_write_set_format_mtree_classic` | `0x10C970` | 54 | UnwindData |  |
| 434 | `archive_write_set_format_pax` | `0x111470` | 251 | UnwindData |  |
| 435 | `archive_write_set_format_pax_restricted` | `0x111580` | 72 | UnwindData |  |
| 436 | `archive_write_set_format_raw` | `0x111FC0` | 229 | UnwindData |  |
| 437 | `archive_write_set_format_shar` | `0x1121E0` | 261 | UnwindData |  |
| 438 | `archive_write_set_format_shar_dump` | `0x1122F0` | 68 | UnwindData |  |
| 439 | `archive_write_set_format_ustar` | `0x1136C0` | 244 | UnwindData |  |
| 440 | `archive_write_set_format_v7tar` | `0x113C00` | 237 | UnwindData |  |
| 441 | `archive_write_set_format_warc` | `0x114A10` | 286 | UnwindData |  |
| 442 | `archive_write_set_format_xar` | `0x114BF0` | 512 | UnwindData |  |
| 443 | `archive_write_set_format_zip` | `0x1190B0` | 367 | UnwindData |  |
| 449 | `archive_write_zip_set_compression_bzip2` | `0x11B500` | 107 | UnwindData |  |
| 450 | `archive_write_zip_set_compression_deflate` | `0x11B580` | 107 | UnwindData |  |
| 451 | `archive_write_zip_set_compression_lzma` | `0x11B600` | 107 | UnwindData |  |
| 452 | `archive_write_zip_set_compression_store` | `0x11B680` | 113 | UnwindData |  |
| 453 | `archive_write_zip_set_compression_xz` | `0x11B700` | 107 | UnwindData |  |
| 454 | `archive_write_zip_set_compression_zstd` | `0x11B780` | 107 | UnwindData |  |
| 416 | `archive_write_set_filter_option` | `0x11C020` | 47 | UnwindData |  |
| 433 | `archive_write_set_format_option` | `0x11C060` | 47 | UnwindData |  |
| 444 | `archive_write_set_option` | `0x11C0A0` | 47 | UnwindData |  |
| 445 | `archive_write_set_options` | `0x11C0E0` | 40 | UnwindData |  |
| 446 | `archive_write_set_passphrase` | `0x11C170` | 69 | UnwindData |  |
| 447 | `archive_write_set_passphrase_callback` | `0x11C1C0` | 87 | UnwindData |  |
