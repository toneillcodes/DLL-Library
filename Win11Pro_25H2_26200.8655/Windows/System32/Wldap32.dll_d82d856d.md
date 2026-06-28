# Binary Specification: Wldap32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Wldap32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d82d856dc9346c92eff99b2a9051068077421df681e7a0bb3b15c9fe7d8a499a`
* **Total Exported Functions:** 245

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 41 | `ldap_msgfree` | `0xBEB0` | 18 | UnwindData |  |
| 37 | `ldap_count_values` | `0x15A40` | 2,224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `ldap_count_valuesA` | `0x15A40` | 2,224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `ldap_get_values_lenW` | `0x162F0` | 305 | UnwindData |  |
| 26 | `ldap_first_entry` | `0x174C0` | 212 | UnwindData |  |
| 203 | `ldap_search_ext_sW` | `0x17B30` | 16 | UnwindData |  |
| 88 | `ldap_connect` | `0x17DA0` | 199 | UnwindData |  |
| 140 | `ldap_get_valuesW` | `0x17E70` | 299 | UnwindData |  |
| 13 | `ldap_unbind` | `0x17FB0` | 30 | UnwindData |  |
| 14 | `ldap_set_optionW` | `0x18130` | 229 | UnwindData |  |
| 40 | `ldap_result` | `0x18220` | 874 | UnwindData |  |
| 22 | `ldap_err2string` | `0x19E40` | 1,159 | UnwindData |  |
| 117 | `ldap_err2stringA` | `0x19E40` | 1,159 | UnwindData |  |
| 38 | `ldap_value_free` | `0x1B460` | 18 | UnwindData |  |
| 223 | `ldap_value_freeA` | `0x1B460` | 18 | UnwindData |  |
| 310 | `ber_printf` | `0x221E0` | 606 | UnwindData |  |
| 91 | `ldap_control_freeW` | `0x22670` | 63 | UnwindData |  |
| 197 | `ldap_escape_filter_element` | `0x24400` | 297 | UnwindData |  |
| 119 | `ldap_escape_filter_elementA` | `0x24400` | 297 | UnwindData |  |
| 17 | `cldap_open` | `0x24F30` | 272 | UnwindData |  |
| 55 | `cldap_openA` | `0x24F30` | 272 | UnwindData |  |
| 219 | `ldap_sslinitW` | `0x25310` | 380 | UnwindData |  |
| 145 | `ldap_initW` | `0x254A0` | 371 | UnwindData |  |
| 73 | `ldap_bind_sW` | `0x26BA0` | 232 | UnwindData |  |
| 16 | `LdapGetLastError` | `0x27F00` | 47 | UnwindData |  |
| 210 | `ldap_search_stW` | `0x29730` | 774 | UnwindData |  |
| 21 | `ldap_result2error` | `0x29C50` | 346 | UnwindData |  |
| 135 | `ldap_get_next_page_s` | `0x29DB0` | 752 | UnwindData |  |
| 191 | `ldap_search_abandon_page` | `0x2AEC0` | 836 | UnwindData |  |
| 18 | `LdapMapErrorToWin32` | `0x2C9D0` | 754 | UnwindData |  |
| 200 | `ldap_memfree` | `0x2CCD0` | 452 | UnwindData |  |
| 146 | `ldap_memfreeA` | `0x2CCD0` | 452 | UnwindData |  |
| 29 | `LdapUTF8ToUnicode` | `0x2CED0` | 45 | UnwindData |  |
| 53 | `LdapUnicodeToUTF8` | `0x2D6B0` | 56 | UnwindData |  |
| 192 | `ldap_search_ext` | `0x2D9B0` | 860 | UnwindData |  |
| 193 | `ldap_search_extA` | `0x2D9B0` | 860 | UnwindData |  |
| 35 | `ldap_get_values_len` | `0x2E560` | 524 | UnwindData |  |
| 141 | `ldap_get_values_lenA` | `0x2E560` | 524 | UnwindData |  |
| 94 | `ldap_controls_freeW` | `0x2EBA0` | 95 | UnwindData |  |
| 97 | `ldap_count_valuesW` | `0x2EDA0` | 912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `ldap_count_values_len` | `0x2EDA0` | 912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 167 | `ldap_next_attributeW` | `0x2F130` | 202 | UnwindData |  |
| 27 | `ldap_next_entry` | `0x2F2D0` | 209 | UnwindData |  |
| 136 | `ldap_get_option` | `0x2F3B0` | 215 | UnwindData |  |
| 137 | `ldap_get_optionA` | `0x2F3B0` | 215 | UnwindData |  |
| 12 | `ldap_get_optionW` | `0x2F490` | 215 | UnwindData |  |
| 36 | `ldap_count_entries` | `0x2FDC0` | 222 | UnwindData |  |
| 224 | `ldap_value_freeW` | `0x30350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `ldap_value_free_len` | `0x30350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `ldap_first_attributeW` | `0x30360` | 202 | UnwindData |  |
| 309 | `ber_flatten` | `0x30E20` | 221 | UnwindData |  |
| 46 | `ldap_unbind_s` | `0x30F90` | 1,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 194 | `ldap_search_extW` | `0x31430` | 313 | UnwindData |  |
| 54 | `ber_bvfree` | `0x316B0` | 62 | UnwindData |  |
| 133 | `ldap_get_dnW` | `0x31700` | 307 | UnwindData |  |
| 301 | `ber_free` | `0x31840` | 25 | UnwindData |  |
| 33 | `ldap_next_attribute` | `0x31860` | 202 | UnwindData |  |
| 166 | `ldap_next_attributeA` | `0x31860` | 202 | UnwindData |  |
| 32 | `ldap_first_attribute` | `0x31930` | 202 | UnwindData |  |
| 126 | `ldap_first_attributeA` | `0x31930` | 202 | UnwindData |  |
| 211 | `ldap_set_option` | `0x31EB0` | 202 | UnwindData |  |
| 212 | `ldap_set_optionA` | `0x31EB0` | 202 | UnwindData |  |
| 206 | `ldap_search_init_pageW` | `0x322D0` | 306 | UnwindData |  |
| 147 | `ldap_memfreeW` | `0x373C0` | 7,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `ldap_abandon` | `0x39150` | 259 | UnwindData |  |
| 11 | `ldap_add` | `0x3A140` | 43 | UnwindData |  |
| 56 | `ldap_addA` | `0x3A140` | 43 | UnwindData |  |
| 42 | `ldap_addW` | `0x3A180` | 246 | UnwindData |  |
| 57 | `ldap_add_ext` | `0x3A280` | 368 | UnwindData |  |
| 58 | `ldap_add_extA` | `0x3A280` | 368 | UnwindData |  |
| 62 | `ldap_add_extW` | `0x3A400` | 258 | UnwindData |  |
| 63 | `ldap_add_ext_s` | `0x3A510` | 509 | UnwindData |  |
| 64 | `ldap_add_ext_sA` | `0x3A510` | 509 | UnwindData |  |
| 65 | `ldap_add_ext_sW` | `0x3A720` | 433 | UnwindData |  |
| 44 | `ldap_add_s` | `0x3A8E0` | 24 | UnwindData |  |
| 66 | `ldap_add_sA` | `0x3A8E0` | 24 | UnwindData |  |
| 69 | `ldap_add_sW` | `0x3A900` | 24 | UnwindData |  |
| 82 | `ldap_perror` | `0x401A0` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 199 | `ldap_set_dbg_routine` | `0x401A0` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `ldap_bind` | `0x406F0` | 20 | UnwindData |  |
| 70 | `ldap_bindA` | `0x406F0` | 20 | UnwindData |  |
| 71 | `ldap_bindW` | `0x40710` | 232 | UnwindData |  |
| 45 | `ldap_bind_s` | `0x40800` | 20 | UnwindData |  |
| 72 | `ldap_bind_sA` | `0x40800` | 20 | UnwindData |  |
| 59 | `ldap_simple_bind` | `0x40820` | 26 | UnwindData |  |
| 213 | `ldap_simple_bindA` | `0x40820` | 26 | UnwindData |  |
| 214 | `ldap_simple_bindW` | `0x40840` | 222 | UnwindData |  |
| 60 | `ldap_simple_bind_s` | `0x40930` | 26 | UnwindData |  |
| 215 | `ldap_simple_bind_sA` | `0x40930` | 26 | UnwindData |  |
| 216 | `ldap_simple_bind_sW` | `0x40950` | 223 | UnwindData |  |
| 19 | `ldap_compare` | `0x416B0` | 49 | UnwindData |  |
| 75 | `ldap_compareA` | `0x416B0` | 49 | UnwindData |  |
| 76 | `ldap_compareW` | `0x416F0` | 270 | UnwindData |  |
| 78 | `ldap_compare_ext` | `0x41810` | 573 | UnwindData |  |
| 80 | `ldap_compare_extA` | `0x41810` | 573 | UnwindData |  |
| 81 | `ldap_compare_extW` | `0x41A60` | 290 | UnwindData |  |
| 83 | `ldap_compare_ext_s` | `0x41B90` | 660 | UnwindData |  |
| 84 | `ldap_compare_ext_sA` | `0x41B90` | 660 | UnwindData |  |
| 85 | `ldap_compare_ext_sW` | `0x41E30` | 405 | UnwindData |  |
| 52 | `ldap_compare_s` | `0x41FD0` | 32 | UnwindData |  |
| 86 | `ldap_compare_sA` | `0x41FD0` | 32 | UnwindData |  |
| 87 | `ldap_compare_sW` | `0x42000` | 32 | UnwindData |  |
| 89 | `ldap_control_free` | `0x42050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `ldap_control_freeA` | `0x42050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `ldap_controls_free` | `0x42060` | 5,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `ldap_controls_freeA` | `0x42060` | 5,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `ldap_free_controls` | `0x42060` | 5,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | `ldap_free_controlsA` | `0x42060` | 5,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `ldap_free_controlsW` | `0x42060` | 5,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `ldap_delete` | `0x43440` | 40 | UnwindData |  |
| 104 | `ldap_deleteA` | `0x43440` | 40 | UnwindData |  |
| 105 | `ldap_deleteW` | `0x43470` | 40 | UnwindData |  |
| 106 | `ldap_delete_ext` | `0x434A0` | 355 | UnwindData |  |
| 107 | `ldap_delete_extA` | `0x434A0` | 355 | UnwindData |  |
| 108 | `ldap_delete_extW` | `0x43610` | 248 | UnwindData |  |
| 109 | `ldap_delete_ext_s` | `0x43710` | 496 | UnwindData |  |
| 110 | `ldap_delete_ext_sA` | `0x43710` | 496 | UnwindData |  |
| 111 | `ldap_delete_ext_sW` | `0x43910` | 409 | UnwindData |  |
| 47 | `ldap_delete_s` | `0x43AB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `ldap_delete_sA` | `0x43AB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `ldap_delete_sW` | `0x43AD0` | 1,648 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `ldap_close_extended_op` | `0x44140` | 207 | UnwindData |  |
| 123 | `ldap_extended_operation` | `0x44220` | 368 | UnwindData |  |
| 124 | `ldap_extended_operationA` | `0x44220` | 368 | UnwindData |  |
| 125 | `ldap_extended_operationW` | `0x443A0` | 258 | UnwindData |  |
| 333 | `ldap_extended_operation_sA` | `0x444B0` | 539 | UnwindData |  |
| 332 | `ldap_extended_operation_sW` | `0x446E0` | 452 | UnwindData |  |
| 202 | `ldap_cleanup` | `0x45960` | 50 | UnwindData |  |
| 201 | `ldap_startup` | `0x459A0` | 63 | UnwindData |  |
| 23 | `ldap_modify` | `0x46530` | 43 | UnwindData |  |
| 148 | `ldap_modifyA` | `0x46530` | 43 | UnwindData |  |
| 149 | `ldap_modifyW` | `0x46570` | 246 | UnwindData |  |
| 150 | `ldap_modify_ext` | `0x46670` | 364 | UnwindData |  |
| 151 | `ldap_modify_extA` | `0x46670` | 364 | UnwindData |  |
| 152 | `ldap_modify_extW` | `0x467F0` | 258 | UnwindData |  |
| 153 | `ldap_modify_ext_s` | `0x46900` | 515 | UnwindData |  |
| 154 | `ldap_modify_ext_sA` | `0x46900` | 515 | UnwindData |  |
| 155 | `ldap_modify_ext_sW` | `0x46B10` | 433 | UnwindData |  |
| 48 | `ldap_modify_s` | `0x46CD0` | 24 | UnwindData |  |
| 156 | `ldap_modify_sA` | `0x46CD0` | 24 | UnwindData |  |
| 157 | `ldap_modify_sW` | `0x46CF0` | 24 | UnwindData |  |
| 31 | `ldap_dn2ufn` | `0x46DA0` | 139 | UnwindData |  |
| 232 | `ldap_dn2ufnA` | `0x46DA0` | 139 | UnwindData |  |
| 114 | `ldap_dn2ufnW` | `0x46E40` | 711 | UnwindData |  |
| 39 | `ldap_explode_dn` | `0x47110` | 175 | UnwindData |  |
| 121 | `ldap_explode_dnA` | `0x47110` | 175 | UnwindData |  |
| 122 | `ldap_explode_dnW` | `0x471D0` | 665 | UnwindData |  |
| 220 | `ldap_ufn2dn` | `0x47470` | 160 | UnwindData |  |
| 221 | `ldap_ufn2dnA` | `0x47470` | 160 | UnwindData |  |
| 222 | `ldap_ufn2dnW` | `0x47520` | 955 | UnwindData |  |
| 304 | `ber_alloc_t` | `0x478F0` | 120 | UnwindData |  |
| 303 | `ber_bvdup` | `0x47970` | 213 | UnwindData |  |
| 302 | `ber_bvecfree` | `0x47A50` | 73 | UnwindData |  |
| 307 | `ber_first_element` | `0x47AA0` | 110 | UnwindData |  |
| 300 | `ber_init` | `0x47B20` | 222 | UnwindData |  |
| 308 | `ber_next_element` | `0x47C10` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 306 | `ber_peek_tag` | `0x47C50` | 53 | UnwindData |  |
| 311 | `ber_scanf` | `0x47C90` | 1,458 | UnwindData |  |
| 305 | `ber_skip_tag` | `0x48250` | 57 | UnwindData |  |
| 28 | `cldap_openW` | `0x484B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `ldap_init` | `0x484C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `ldap_initA` | `0x484C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `ldap_open` | `0x484D0` | 97 | UnwindData |  |
| 169 | `ldap_openA` | `0x484D0` | 97 | UnwindData |  |
| 170 | `ldap_openW` | `0x48540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 217 | `ldap_sslinit` | `0x48550` | 109 | UnwindData |  |
| 218 | `ldap_sslinitA` | `0x48550` | 109 | UnwindData |  |
| 98 | `ldap_create_page_control` | `0x49040` | 244 | UnwindData |  |
| 99 | `ldap_create_page_controlA` | `0x49040` | 244 | UnwindData |  |
| 100 | `ldap_create_page_controlW` | `0x49140` | 230 | UnwindData |  |
| 320 | `ldap_create_vlv_controlA` | `0x49230` | 32 | UnwindData |  |
| 319 | `ldap_create_vlv_controlW` | `0x49260` | 29 | UnwindData |  |
| 134 | `ldap_get_next_page` | `0x49290` | 510 | UnwindData |  |
| 138 | `ldap_get_paged_count` | `0x494A0` | 363 | UnwindData |  |
| 171 | `ldap_parse_page_control` | `0x49620` | 225 | UnwindData |  |
| 172 | `ldap_parse_page_controlA` | `0x49620` | 225 | UnwindData |  |
| 173 | `ldap_parse_page_controlW` | `0x49710` | 222 | UnwindData |  |
| 322 | `ldap_parse_vlv_controlA` | `0x49800` | 245 | UnwindData |  |
| 321 | `ldap_parse_vlv_controlW` | `0x49900` | 242 | UnwindData |  |
| 204 | `ldap_search_init_page` | `0x49A00` | 470 | UnwindData |  |
| 205 | `ldap_search_init_pageA` | `0x49A00` | 470 | UnwindData |  |
| 318 | `ldap_parse_extended_resultA` | `0x49F60` | 233 | UnwindData |  |
| 317 | `ldap_parse_extended_resultW` | `0x4A050` | 230 | UnwindData |  |
| 177 | `ldap_parse_result` | `0x4A140` | 275 | UnwindData |  |
| 178 | `ldap_parse_resultA` | `0x4A140` | 275 | UnwindData |  |
| 179 | `ldap_parse_resultW` | `0x4A260` | 272 | UnwindData |  |
| 24 | `ldap_modrdn` | `0x4C540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 162 | `ldap_modrdnA` | `0x4C540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `ldap_modrdn2` | `0x4C560` | 392 | UnwindData |  |
| 158 | `ldap_modrdn2A` | `0x4C560` | 392 | UnwindData |  |
| 159 | `ldap_modrdn2W` | `0x4C6F0` | 461 | UnwindData |  |
| 68 | `ldap_modrdn2_s` | `0x4C8D0` | 338 | UnwindData |  |
| 160 | `ldap_modrdn2_sA` | `0x4C8D0` | 338 | UnwindData |  |
| 161 | `ldap_modrdn2_sW` | `0x4CA30` | 338 | UnwindData |  |
| 163 | `ldap_modrdnW` | `0x4CB90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `ldap_modrdn_s` | `0x4CBB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 164 | `ldap_modrdn_sA` | `0x4CBB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 165 | `ldap_modrdn_sW` | `0x4CBD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `ldap_rename_ext` | `0x4CBF0` | 592 | UnwindData |  |
| 184 | `ldap_rename_extA` | `0x4CBF0` | 592 | UnwindData |  |
| 185 | `ldap_rename_extW` | `0x4CE50` | 288 | UnwindData |  |
| 186 | `ldap_rename_ext_s` | `0x4CF80` | 659 | UnwindData |  |
| 187 | `ldap_rename_ext_sA` | `0x4CF80` | 659 | UnwindData |  |
| 188 | `ldap_rename_ext_sW` | `0x4D220` | 394 | UnwindData |  |
| 30 | `ldap_get_dn` | `0x4D660` | 64 | UnwindData |  |
| 132 | `ldap_get_dnA` | `0x4D660` | 64 | UnwindData |  |
| 34 | `ldap_get_values` | `0x4D6B0` | 347 | UnwindData |  |
| 139 | `ldap_get_valuesA` | `0x4D820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `ldap_search` | `0x4D830` | 470 | UnwindData |  |
| 189 | `ldap_searchA` | `0x4D830` | 470 | UnwindData |  |
| 190 | `ldap_searchW` | `0x4DA10` | 304 | UnwindData |  |
| 195 | `ldap_search_ext_s` | `0x4DB50` | 751 | UnwindData |  |
| 196 | `ldap_search_ext_sA` | `0x4DB50` | 751 | UnwindData |  |
| 50 | `ldap_search_s` | `0x4DE50` | 52 | UnwindData |  |
| 207 | `ldap_search_sA` | `0x4DE50` | 52 | UnwindData |  |
| 208 | `ldap_search_sW` | `0x4DE90` | 52 | UnwindData |  |
| 51 | `ldap_search_st` | `0x4DED0` | 326 | UnwindData |  |
| 209 | `ldap_search_stA` | `0x4DED0` | 326 | UnwindData |  |
| 315 | `ldap_sasl_bindA` | `0x4EE90` | 550 | UnwindData |  |
| 313 | `ldap_sasl_bindW` | `0x4F0C0` | 342 | UnwindData |  |
| 316 | `ldap_sasl_bind_sA` | `0x4F220` | 529 | UnwindData |  |
| 314 | `ldap_sasl_bind_sW` | `0x4F440` | 337 | UnwindData |  |
| 101 | `ldap_create_sort_control` | `0x4FBA0` | 23 | UnwindData |  |
| 102 | `ldap_create_sort_controlA` | `0x4FBA0` | 23 | UnwindData |  |
| 103 | `ldap_create_sort_controlW` | `0x4FBC0` | 20 | UnwindData |  |
| 115 | `ldap_encode_sort_controlA` | `0x4FBE0` | 225 | UnwindData |  |
| 116 | `ldap_encode_sort_controlW` | `0x4FCD0` | 222 | UnwindData |  |
| 180 | `ldap_parse_sort_control` | `0x4FDC0` | 225 | UnwindData |  |
| 181 | `ldap_parse_sort_controlA` | `0x4FDC0` | 225 | UnwindData |  |
| 182 | `ldap_parse_sort_controlW` | `0x4FEB0` | 222 | UnwindData |  |
| 230 | `ldap_check_filterA` | `0x4FFA0` | 102 | UnwindData |  |
| 231 | `ldap_check_filterW` | `0x50010` | 465 | UnwindData |  |
| 120 | `ldap_escape_filter_elementW` | `0x501F0` | 301 | UnwindData |  |
| 330 | `ldap_start_tls_sA` | `0x509A0` | 25 | UnwindData |  |
| 329 | `ldap_start_tls_sW` | `0x509A0` | 25 | UnwindData |  |
| 331 | `ldap_stop_tls_s` | `0x509C0` | 1,104 | UnwindData |  |
| 95 | `ldap_count_references` | `0x50F90` | 193 | UnwindData |  |
| 128 | `ldap_first_reference` | `0x51060` | 195 | UnwindData |  |
| 168 | `ldap_next_reference` | `0x51130` | 195 | UnwindData |  |
| 174 | `ldap_parse_reference` | `0x51200` | 204 | UnwindData |  |
| 175 | `ldap_parse_referenceA` | `0x51200` | 204 | UnwindData |  |
| 176 | `ldap_parse_referenceW` | `0x512E0` | 204 | UnwindData |  |
| 312 | `ldap_conn_from_msg` | `0x51680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `ldap_err2stringW` | `0x516A0` | 65 | UnwindData |  |
| 198 | `ldap_set_dbg_flags` | `0x516F0` | 0 | Indeterminate |  |
