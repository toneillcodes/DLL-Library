# Binary Specification: iga64.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_188be4c1587f7330\iga64.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a62335a6a267993509cc75334174c227a6c1b5b358d5c40d90c3cd06596c9800`
* **Total Exported Functions:** 84

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `iga_assemble` | `0x12140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `iga_context_assemble` | `0x12150` | 225 | UnwindData |  |
| 3 | `iga_context_create` | `0x12240` | 310 | UnwindData |  |
| 4 | `iga_context_disassemble` | `0x12380` | 230 | UnwindData |  |
| 5 | `iga_context_disassemble_instruction` | `0x12470` | 218 | UnwindData |  |
| 6 | `iga_context_get_errors` | `0x12550` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `iga_context_get_warnings` | `0x125D0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `iga_context_release` | `0x12650` | 183 | UnwindData |  |
| 9 | `iga_create_context` | `0x12710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `iga_diagnostic_get_message` | `0x12720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `iga_diagnostic_get_offset` | `0x12740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `iga_diagnostic_get_text_column` | `0x12760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `iga_diagnostic_get_text_extent` | `0x12780` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `iga_diagnostic_get_text_line` | `0x127B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `iga_diagnostic_get_type` | `0x127E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `iga_disassemble` | `0x12810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `iga_disassemble_instruction` | `0x12820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `iga_get_errors` | `0x12830` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `iga_get_interface` | `0x128B0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `iga_get_warnings` | `0x129B0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `iga_opspec_description` | `0x12A30` | 31 | UnwindData |  |
| 22 | `iga_opspec_enumerate` | `0x12AB0` | 33 | UnwindData |  |
| 23 | `iga_opspec_from_op` | `0x12CB0` | 107 | UnwindData |  |
| 24 | `iga_opspec_mnemonic` | `0x12D20` | 49 | UnwindData |  |
| 25 | `iga_opspec_name` | `0x12ED0` | 49 | UnwindData |  |
| 26 | `iga_opspec_op` | `0x13080` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `iga_opspec_op_encoding` | `0x130B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `iga_platform_names` | `0x130E0` | 339 | UnwindData |  |
| 29 | `iga_platform_symbol_suffix` | `0x13240` | 221 | UnwindData |  |
| 30 | `iga_platforms_list` | `0x13320` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `iga_release_context` | `0x13390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `iga_status_to_string` | `0x133A0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `iga_version_string` | `0x13460` | 14,768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `kv_create` | `0x16E10` | 870 | UnwindData |  |
| 35 | `kv_delete` | `0x17180` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `kv_get_channel_offset` | `0x17190` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `kv_get_default_label_name` | `0x171F0` | 120 | UnwindData |  |
| 38 | `kv_get_destination_data_type` | `0x17270` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `kv_get_destination_indirect_imm_off` | `0x172D0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `kv_get_destination_mme_number` | `0x17340` | 139 | UnwindData |  |
| 41 | `kv_get_destination_modifier` | `0x173D0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `kv_get_destination_region` | `0x17430` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `kv_get_destination_register` | `0x174A0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `kv_get_destination_register_kind` | `0x17510` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `kv_get_destination_register_type` | `0x17570` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `kv_get_destination_sub_register` | `0x175D0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `kv_get_execution_size` | `0x17640` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `kv_get_flag_modifier` | `0x17690` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `kv_get_flag_register` | `0x176F0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `kv_get_flag_sub_register` | `0x17750` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `kv_get_has_destination` | `0x177B0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `kv_get_inst_size` | `0x17810` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `kv_get_inst_syntax` | `0x17870` | 145 | UnwindData |  |
| 54 | `kv_get_inst_targets` | `0x17A40` | 121 | UnwindData |  |
| 55 | `kv_get_is_inverse_predicate` | `0x17B40` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `kv_get_mask_control` | `0x17BA0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `kv_get_message_len` | `0x17C00` | 246 | UnwindData |  |
| 58 | `kv_get_message_len_ext` | `0x17D00` | 184 | UnwindData |  |
| 59 | `kv_get_message_sfid` | `0x17DC0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `kv_get_message_type` | `0x17E70` | 209 | UnwindData |  |
| 61 | `kv_get_message_type_ext` | `0x17F50` | 208 | UnwindData |  |
| 62 | `kv_get_number_sources` | `0x18020` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `kv_get_opcode` | `0x18070` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `kv_get_opgroup` | `0x180C0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `kv_get_predicate` | `0x18170` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `kv_get_send_descs` | `0x181D0` | 184 | UnwindData |  |
| 67 | `kv_get_send_exbso` | `0x18290` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `kv_get_send_exdesc_immoff` | `0x18340` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `kv_get_send_indirect_descs` | `0x18400` | 44 | UnwindData |  |
| 70 | `kv_get_source_data_type` | `0x184F0` | 143 | UnwindData |  |
| 71 | `kv_get_source_immediate` | `0x18580` | 173 | UnwindData |  |
| 72 | `kv_get_source_indirect_imm_off` | `0x18630` | 172 | UnwindData |  |
| 73 | `kv_get_source_mme_number` | `0x186E0` | 175 | UnwindData |  |
| 74 | `kv_get_source_modifier` | `0x18790` | 148 | UnwindData |  |
| 75 | `kv_get_source_region` | `0x18830` | 253 | UnwindData |  |
| 76 | `kv_get_source_register` | `0x18930` | 154 | UnwindData |  |
| 77 | `kv_get_source_register_kind` | `0x189D0` | 134 | UnwindData |  |
| 78 | `kv_get_source_register_type` | `0x18A60` | 156 | UnwindData |  |
| 79 | `kv_get_source_sub_register` | `0x18B00` | 159 | UnwindData |  |
| 80 | `kv_get_subfunction` | `0x18BA0` | 388 | UnwindData |  |
| 81 | `kv_get_swsb_info` | `0x18D30` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `kv_has_inst_opt` | `0x18DA0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `kv_is_inst_target` | `0x18E00` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `kv_is_source_vector` | `0x18E60` | 191 | UnwindData |  |
