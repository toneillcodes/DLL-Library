# Binary Specification: Wldap32.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Wldap32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a109d036fcc5c0b09c6b8213b74e30a9361b1bcb7cb4c5e62c441a5433005662`
* **Total Exported Functions:** 245

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 41 | `ldap_msgfree` | `0xBFC0` | 18 | UnwindData |  |
| 37 | `ldap_count_values` | `0x15B50` | 2,224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `ldap_count_valuesA` | `0x15B50` | 2,224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `ldap_get_values_lenW` | `0x16400` | 305 | UnwindData |  |
| 26 | `ldap_first_entry` | `0x175B0` | 212 | UnwindData |  |
| 203 | `ldap_search_ext_sW` | `0x17C20` | 16 | UnwindData |  |
| 88 | `ldap_connect` | `0x17E90` | 199 | UnwindData |  |
| 140 | `ldap_get_valuesW` | `0x17F60` | 299 | UnwindData |  |
| 13 | `ldap_unbind` | `0x180A0` | 30 | UnwindData |  |
| 14 | `ldap_set_optionW` | `0x18220` | 229 | UnwindData |  |
| 40 | `ldap_result` | `0x18310` | 874 | UnwindData |  |
| 22 | `ldap_err2string` | `0x19F30` | 1,159 | UnwindData |  |
| 117 | `ldap_err2stringA` | `0x19F30` | 1,159 | UnwindData |  |
| 38 | `ldap_value_free` | `0x1B550` | 18 | UnwindData |  |
| 223 | `ldap_value_freeA` | `0x1B550` | 18 | UnwindData |  |
| 310 | `ber_printf` | `0x222D0` | 606 | UnwindData |  |
| 91 | `ldap_control_freeW` | `0x22760` | 63 | UnwindData |  |
| 197 | `ldap_escape_filter_element` | `0x24550` | 297 | UnwindData |  |
| 119 | `ldap_escape_filter_elementA` | `0x24550` | 297 | UnwindData |  |
| 17 | `cldap_open` | `0x24F00` | 272 | UnwindData |  |
| 55 | `cldap_openA` | `0x24F00` | 272 | UnwindData |  |
| 219 | `ldap_sslinitW` | `0x252E0` | 380 | UnwindData |  |
| 145 | `ldap_initW` | `0x25470` | 371 | UnwindData |  |
| 73 | `ldap_bind_sW` | `0x26870` | 232 | UnwindData |  |
| 16 | `LdapGetLastError` | `0x27BD0` | 47 | UnwindData |  |
| 210 | `ldap_search_stW` | `0x29400` | 774 | UnwindData |  |
| 21 | `ldap_result2error` | `0x29920` | 346 | UnwindData |  |
| 135 | `ldap_get_next_page_s` | `0x29A80` | 752 | UnwindData |  |
| 191 | `ldap_search_abandon_page` | `0x2ADF0` | 836 | UnwindData |  |
| 18 | `LdapMapErrorToWin32` | `0x2C900` | 754 | UnwindData |  |
| 200 | `ldap_memfree` | `0x2CC00` | 452 | UnwindData |  |
| 146 | `ldap_memfreeA` | `0x2CC00` | 452 | UnwindData |  |
| 29 | `LdapUTF8ToUnicode` | `0x2CE00` | 45 | UnwindData |  |
| 53 | `LdapUnicodeToUTF8` | `0x2D5F0` | 56 | UnwindData |  |
| 192 | `ldap_search_ext` | `0x2D860` | 860 | UnwindData |  |
| 193 | `ldap_search_extA` | `0x2D860` | 860 | UnwindData |  |
| 35 | `ldap_get_values_len` | `0x2E390` | 524 | UnwindData |  |
| 141 | `ldap_get_values_lenA` | `0x2E390` | 524 | UnwindData |  |
| 94 | `ldap_controls_freeW` | `0x2E9D0` | 95 | UnwindData |  |
| 97 | `ldap_count_valuesW` | `0x2EBD0` | 912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `ldap_count_values_len` | `0x2EBD0` | 912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 167 | `ldap_next_attributeW` | `0x2EF60` | 202 | UnwindData |  |
| 27 | `ldap_next_entry` | `0x2F100` | 209 | UnwindData |  |
| 136 | `ldap_get_option` | `0x2F1E0` | 215 | UnwindData |  |
| 137 | `ldap_get_optionA` | `0x2F1E0` | 215 | UnwindData |  |
| 12 | `ldap_get_optionW` | `0x2F2C0` | 215 | UnwindData |  |
| 36 | `ldap_count_entries` | `0x2FBF0` | 222 | UnwindData |  |
| 224 | `ldap_value_freeW` | `0x30070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `ldap_value_free_len` | `0x30070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `ldap_first_attributeW` | `0x30080` | 202 | UnwindData |  |
| 309 | `ber_flatten` | `0x30BF0` | 221 | UnwindData |  |
| 46 | `ldap_unbind_s` | `0x30D60` | 1,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 194 | `ldap_search_extW` | `0x31200` | 313 | UnwindData |  |
| 54 | `ber_bvfree` | `0x31440` | 62 | UnwindData |  |
| 133 | `ldap_get_dnW` | `0x31490` | 307 | UnwindData |  |
| 301 | `ber_free` | `0x315D0` | 25 | UnwindData |  |
| 33 | `ldap_next_attribute` | `0x315F0` | 202 | UnwindData |  |
| 166 | `ldap_next_attributeA` | `0x315F0` | 202 | UnwindData |  |
| 32 | `ldap_first_attribute` | `0x316C0` | 202 | UnwindData |  |
| 126 | `ldap_first_attributeA` | `0x316C0` | 202 | UnwindData |  |
| 211 | `ldap_set_option` | `0x31C00` | 202 | UnwindData |  |
| 212 | `ldap_set_optionA` | `0x31C00` | 202 | UnwindData |  |
| 206 | `ldap_search_init_pageW` | `0x32020` | 306 | UnwindData |  |
| 147 | `ldap_memfreeW` | `0x37240` | 27,424 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `ldap_perror` | `0x3DD60` | 1,616 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 199 | `ldap_set_dbg_routine` | `0x3DD60` | 1,616 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `ldap_abandon` | `0x3E3B0` | 259 | UnwindData |  |
| 11 | `ldap_add` | `0x3F900` | 43 | UnwindData |  |
| 56 | `ldap_addA` | `0x3F900` | 43 | UnwindData |  |
| 42 | `ldap_addW` | `0x3F940` | 246 | UnwindData |  |
| 57 | `ldap_add_ext` | `0x3FA40` | 368 | UnwindData |  |
| 58 | `ldap_add_extA` | `0x3FA40` | 368 | UnwindData |  |
| 62 | `ldap_add_extW` | `0x3FBC0` | 258 | UnwindData |  |
| 63 | `ldap_add_ext_s` | `0x3FCD0` | 509 | UnwindData |  |
| 64 | `ldap_add_ext_sA` | `0x3FCD0` | 509 | UnwindData |  |
| 65 | `ldap_add_ext_sW` | `0x3FEE0` | 433 | UnwindData |  |
| 44 | `ldap_add_s` | `0x400A0` | 24 | UnwindData |  |
| 66 | `ldap_add_sA` | `0x400A0` | 24 | UnwindData |  |
| 69 | `ldap_add_sW` | `0x400C0` | 24 | UnwindData |  |
| 61 | `ldap_bind` | `0x40A20` | 20 | UnwindData |  |
| 70 | `ldap_bindA` | `0x40A20` | 20 | UnwindData |  |
| 71 | `ldap_bindW` | `0x40A40` | 232 | UnwindData |  |
| 45 | `ldap_bind_s` | `0x40B30` | 20 | UnwindData |  |
| 72 | `ldap_bind_sA` | `0x40B30` | 20 | UnwindData |  |
| 59 | `ldap_simple_bind` | `0x40B50` | 26 | UnwindData |  |
| 213 | `ldap_simple_bindA` | `0x40B50` | 26 | UnwindData |  |
| 214 | `ldap_simple_bindW` | `0x40B70` | 222 | UnwindData |  |
| 60 | `ldap_simple_bind_s` | `0x40C60` | 26 | UnwindData |  |
| 215 | `ldap_simple_bind_sA` | `0x40C60` | 26 | UnwindData |  |
| 216 | `ldap_simple_bind_sW` | `0x40C80` | 223 | UnwindData |  |
| 19 | `ldap_compare` | `0x414D0` | 49 | UnwindData |  |
| 75 | `ldap_compareA` | `0x414D0` | 49 | UnwindData |  |
| 76 | `ldap_compareW` | `0x41510` | 270 | UnwindData |  |
| 78 | `ldap_compare_ext` | `0x41630` | 573 | UnwindData |  |
| 80 | `ldap_compare_extA` | `0x41630` | 573 | UnwindData |  |
| 81 | `ldap_compare_extW` | `0x41880` | 290 | UnwindData |  |
| 83 | `ldap_compare_ext_s` | `0x419B0` | 660 | UnwindData |  |
| 84 | `ldap_compare_ext_sA` | `0x419B0` | 660 | UnwindData |  |
| 85 | `ldap_compare_ext_sW` | `0x41C50` | 405 | UnwindData |  |
| 52 | `ldap_compare_s` | `0x41DF0` | 32 | UnwindData |  |
| 86 | `ldap_compare_sA` | `0x41DF0` | 32 | UnwindData |  |
| 87 | `ldap_compare_sW` | `0x41E20` | 32 | UnwindData |  |
| 89 | `ldap_control_free` | `0x41E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `ldap_control_freeA` | `0x41E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `ldap_controls_free` | `0x41E80` | 5,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `ldap_controls_freeA` | `0x41E80` | 5,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `ldap_free_controls` | `0x41E80` | 5,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | `ldap_free_controlsA` | `0x41E80` | 5,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `ldap_free_controlsW` | `0x41E80` | 5,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `ldap_delete` | `0x43260` | 40 | UnwindData |  |
| 104 | `ldap_deleteA` | `0x43260` | 40 | UnwindData |  |
| 105 | `ldap_deleteW` | `0x43290` | 40 | UnwindData |  |
| 106 | `ldap_delete_ext` | `0x432C0` | 355 | UnwindData |  |
| 107 | `ldap_delete_extA` | `0x432C0` | 355 | UnwindData |  |
| 108 | `ldap_delete_extW` | `0x43430` | 248 | UnwindData |  |
| 109 | `ldap_delete_ext_s` | `0x43530` | 496 | UnwindData |  |
| 110 | `ldap_delete_ext_sA` | `0x43530` | 496 | UnwindData |  |
| 111 | `ldap_delete_ext_sW` | `0x43730` | 409 | UnwindData |  |
| 47 | `ldap_delete_s` | `0x438D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `ldap_delete_sA` | `0x438D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `ldap_delete_sW` | `0x438F0` | 1,648 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `ldap_close_extended_op` | `0x43F60` | 207 | UnwindData |  |
| 123 | `ldap_extended_operation` | `0x44040` | 368 | UnwindData |  |
| 124 | `ldap_extended_operationA` | `0x44040` | 368 | UnwindData |  |
| 125 | `ldap_extended_operationW` | `0x441C0` | 258 | UnwindData |  |
| 333 | `ldap_extended_operation_sA` | `0x442D0` | 539 | UnwindData |  |
| 332 | `ldap_extended_operation_sW` | `0x44500` | 452 | UnwindData |  |
| 202 | `ldap_cleanup` | `0x46BC0` | 50 | UnwindData |  |
| 201 | `ldap_startup` | `0x46C00` | 63 | UnwindData |  |
| 23 | `ldap_modify` | `0x47790` | 43 | UnwindData |  |
| 148 | `ldap_modifyA` | `0x47790` | 43 | UnwindData |  |
| 149 | `ldap_modifyW` | `0x477D0` | 246 | UnwindData |  |
| 150 | `ldap_modify_ext` | `0x478D0` | 364 | UnwindData |  |
| 151 | `ldap_modify_extA` | `0x478D0` | 364 | UnwindData |  |
| 152 | `ldap_modify_extW` | `0x47A50` | 258 | UnwindData |  |
| 153 | `ldap_modify_ext_s` | `0x47B60` | 515 | UnwindData |  |
| 154 | `ldap_modify_ext_sA` | `0x47B60` | 515 | UnwindData |  |
| 155 | `ldap_modify_ext_sW` | `0x47D70` | 433 | UnwindData |  |
| 48 | `ldap_modify_s` | `0x47F30` | 24 | UnwindData |  |
| 156 | `ldap_modify_sA` | `0x47F30` | 24 | UnwindData |  |
| 157 | `ldap_modify_sW` | `0x47F50` | 24 | UnwindData |  |
| 31 | `ldap_dn2ufn` | `0x48000` | 139 | UnwindData |  |
| 232 | `ldap_dn2ufnA` | `0x48000` | 139 | UnwindData |  |
| 114 | `ldap_dn2ufnW` | `0x480A0` | 711 | UnwindData |  |
| 39 | `ldap_explode_dn` | `0x48370` | 175 | UnwindData |  |
| 121 | `ldap_explode_dnA` | `0x48370` | 175 | UnwindData |  |
| 122 | `ldap_explode_dnW` | `0x48430` | 665 | UnwindData |  |
| 220 | `ldap_ufn2dn` | `0x486D0` | 160 | UnwindData |  |
| 221 | `ldap_ufn2dnA` | `0x486D0` | 160 | UnwindData |  |
| 222 | `ldap_ufn2dnW` | `0x48780` | 955 | UnwindData |  |
| 304 | `ber_alloc_t` | `0x48B50` | 120 | UnwindData |  |
| 303 | `ber_bvdup` | `0x48BD0` | 213 | UnwindData |  |
| 302 | `ber_bvecfree` | `0x48CB0` | 73 | UnwindData |  |
| 307 | `ber_first_element` | `0x48D00` | 110 | UnwindData |  |
| 300 | `ber_init` | `0x48D80` | 222 | UnwindData |  |
| 308 | `ber_next_element` | `0x48E70` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 306 | `ber_peek_tag` | `0x48EB0` | 53 | UnwindData |  |
| 311 | `ber_scanf` | `0x48EF0` | 1,458 | UnwindData |  |
| 305 | `ber_skip_tag` | `0x494B0` | 57 | UnwindData |  |
| 28 | `cldap_openW` | `0x49710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `ldap_init` | `0x49720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `ldap_initA` | `0x49720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `ldap_open` | `0x49730` | 97 | UnwindData |  |
| 169 | `ldap_openA` | `0x49730` | 97 | UnwindData |  |
| 170 | `ldap_openW` | `0x497A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 217 | `ldap_sslinit` | `0x497B0` | 109 | UnwindData |  |
| 218 | `ldap_sslinitA` | `0x497B0` | 109 | UnwindData |  |
| 98 | `ldap_create_page_control` | `0x4A2A0` | 244 | UnwindData |  |
| 99 | `ldap_create_page_controlA` | `0x4A2A0` | 244 | UnwindData |  |
| 100 | `ldap_create_page_controlW` | `0x4A3A0` | 230 | UnwindData |  |
| 320 | `ldap_create_vlv_controlA` | `0x4A490` | 32 | UnwindData |  |
| 319 | `ldap_create_vlv_controlW` | `0x4A4C0` | 29 | UnwindData |  |
| 134 | `ldap_get_next_page` | `0x4A4F0` | 510 | UnwindData |  |
| 138 | `ldap_get_paged_count` | `0x4A700` | 363 | UnwindData |  |
| 171 | `ldap_parse_page_control` | `0x4A880` | 225 | UnwindData |  |
| 172 | `ldap_parse_page_controlA` | `0x4A880` | 225 | UnwindData |  |
| 173 | `ldap_parse_page_controlW` | `0x4A970` | 222 | UnwindData |  |
| 322 | `ldap_parse_vlv_controlA` | `0x4AA60` | 245 | UnwindData |  |
| 321 | `ldap_parse_vlv_controlW` | `0x4AB60` | 242 | UnwindData |  |
| 204 | `ldap_search_init_page` | `0x4AC60` | 470 | UnwindData |  |
| 205 | `ldap_search_init_pageA` | `0x4AC60` | 470 | UnwindData |  |
| 318 | `ldap_parse_extended_resultA` | `0x4B1C0` | 233 | UnwindData |  |
| 317 | `ldap_parse_extended_resultW` | `0x4B2B0` | 230 | UnwindData |  |
| 177 | `ldap_parse_result` | `0x4B3A0` | 275 | UnwindData |  |
| 178 | `ldap_parse_resultA` | `0x4B3A0` | 275 | UnwindData |  |
| 179 | `ldap_parse_resultW` | `0x4B4C0` | 272 | UnwindData |  |
| 24 | `ldap_modrdn` | `0x4D7A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 162 | `ldap_modrdnA` | `0x4D7A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `ldap_modrdn2` | `0x4D7C0` | 392 | UnwindData |  |
| 158 | `ldap_modrdn2A` | `0x4D7C0` | 392 | UnwindData |  |
| 159 | `ldap_modrdn2W` | `0x4D950` | 461 | UnwindData |  |
| 68 | `ldap_modrdn2_s` | `0x4DB30` | 338 | UnwindData |  |
| 160 | `ldap_modrdn2_sA` | `0x4DB30` | 338 | UnwindData |  |
| 161 | `ldap_modrdn2_sW` | `0x4DC90` | 338 | UnwindData |  |
| 163 | `ldap_modrdnW` | `0x4DDF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `ldap_modrdn_s` | `0x4DE10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 164 | `ldap_modrdn_sA` | `0x4DE10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 165 | `ldap_modrdn_sW` | `0x4DE30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `ldap_rename_ext` | `0x4DE50` | 592 | UnwindData |  |
| 184 | `ldap_rename_extA` | `0x4DE50` | 592 | UnwindData |  |
| 185 | `ldap_rename_extW` | `0x4E0B0` | 288 | UnwindData |  |
| 186 | `ldap_rename_ext_s` | `0x4E1E0` | 659 | UnwindData |  |
| 187 | `ldap_rename_ext_sA` | `0x4E1E0` | 659 | UnwindData |  |
| 188 | `ldap_rename_ext_sW` | `0x4E480` | 394 | UnwindData |  |
| 30 | `ldap_get_dn` | `0x4E8C0` | 64 | UnwindData |  |
| 132 | `ldap_get_dnA` | `0x4E8C0` | 64 | UnwindData |  |
| 34 | `ldap_get_values` | `0x4E910` | 347 | UnwindData |  |
| 139 | `ldap_get_valuesA` | `0x4EA80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `ldap_search` | `0x4EA90` | 470 | UnwindData |  |
| 189 | `ldap_searchA` | `0x4EA90` | 470 | UnwindData |  |
| 190 | `ldap_searchW` | `0x4EC70` | 304 | UnwindData |  |
| 195 | `ldap_search_ext_s` | `0x4EDB0` | 751 | UnwindData |  |
| 196 | `ldap_search_ext_sA` | `0x4EDB0` | 751 | UnwindData |  |
| 50 | `ldap_search_s` | `0x4F0B0` | 52 | UnwindData |  |
| 207 | `ldap_search_sA` | `0x4F0B0` | 52 | UnwindData |  |
| 208 | `ldap_search_sW` | `0x4F0F0` | 52 | UnwindData |  |
| 51 | `ldap_search_st` | `0x4F130` | 326 | UnwindData |  |
| 209 | `ldap_search_stA` | `0x4F130` | 326 | UnwindData |  |
| 315 | `ldap_sasl_bindA` | `0x500F0` | 550 | UnwindData |  |
| 313 | `ldap_sasl_bindW` | `0x50320` | 342 | UnwindData |  |
| 316 | `ldap_sasl_bind_sA` | `0x50480` | 529 | UnwindData |  |
| 314 | `ldap_sasl_bind_sW` | `0x506A0` | 337 | UnwindData |  |
| 101 | `ldap_create_sort_control` | `0x50E00` | 23 | UnwindData |  |
| 102 | `ldap_create_sort_controlA` | `0x50E00` | 23 | UnwindData |  |
| 103 | `ldap_create_sort_controlW` | `0x50E20` | 20 | UnwindData |  |
| 115 | `ldap_encode_sort_controlA` | `0x50E40` | 225 | UnwindData |  |
| 116 | `ldap_encode_sort_controlW` | `0x50F30` | 222 | UnwindData |  |
| 180 | `ldap_parse_sort_control` | `0x51020` | 225 | UnwindData |  |
| 181 | `ldap_parse_sort_controlA` | `0x51020` | 225 | UnwindData |  |
| 182 | `ldap_parse_sort_controlW` | `0x51110` | 222 | UnwindData |  |
| 230 | `ldap_check_filterA` | `0x51200` | 102 | UnwindData |  |
| 231 | `ldap_check_filterW` | `0x51270` | 465 | UnwindData |  |
| 120 | `ldap_escape_filter_elementW` | `0x51450` | 301 | UnwindData |  |
| 330 | `ldap_start_tls_sA` | `0x51C00` | 25 | UnwindData |  |
| 329 | `ldap_start_tls_sW` | `0x51C00` | 25 | UnwindData |  |
| 331 | `ldap_stop_tls_s` | `0x51C20` | 1,104 | UnwindData |  |
| 95 | `ldap_count_references` | `0x521F0` | 193 | UnwindData |  |
| 128 | `ldap_first_reference` | `0x522C0` | 195 | UnwindData |  |
| 168 | `ldap_next_reference` | `0x52390` | 195 | UnwindData |  |
| 174 | `ldap_parse_reference` | `0x52460` | 204 | UnwindData |  |
| 175 | `ldap_parse_referenceA` | `0x52460` | 204 | UnwindData |  |
| 176 | `ldap_parse_referenceW` | `0x52540` | 204 | UnwindData |  |
| 312 | `ldap_conn_from_msg` | `0x528E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `ldap_err2stringW` | `0x52900` | 65 | UnwindData |  |
| 198 | `ldap_set_dbg_flags` | `0x52950` | 0 | Indeterminate |  |
