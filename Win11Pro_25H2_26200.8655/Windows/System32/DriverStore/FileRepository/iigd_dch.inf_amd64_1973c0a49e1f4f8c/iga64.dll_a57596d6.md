# Binary Specification: iga64.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_1973c0a49e1f4f8c\iga64.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a57596d692b416739b4ef90fda680f93fd66fbb4ef64ef47951f30e8d81f66ab`
* **Total Exported Functions:** 84

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `iga_assemble` | `0x115E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `iga_context_assemble` | `0x115F0` | 225 | UnwindData |  |
| 3 | `iga_context_create` | `0x116E0` | 310 | UnwindData |  |
| 4 | `iga_context_disassemble` | `0x11820` | 230 | UnwindData |  |
| 5 | `iga_context_disassemble_instruction` | `0x11910` | 208 | UnwindData |  |
| 6 | `iga_context_get_errors` | `0x119E0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `iga_context_get_warnings` | `0x11A60` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `iga_context_release` | `0x11AE0` | 183 | UnwindData |  |
| 9 | `iga_create_context` | `0x11BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `iga_diagnostic_get_message` | `0x11BB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `iga_diagnostic_get_offset` | `0x11BD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `iga_diagnostic_get_text_column` | `0x11BF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `iga_diagnostic_get_text_extent` | `0x11C10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `iga_diagnostic_get_text_line` | `0x11C40` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `iga_diagnostic_get_type` | `0x11C70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `iga_disassemble` | `0x11CA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `iga_disassemble_instruction` | `0x11CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `iga_get_errors` | `0x11CC0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `iga_get_interface` | `0x11D40` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `iga_get_warnings` | `0x11E40` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `iga_opspec_description` | `0x11EC0` | 31 | UnwindData |  |
| 22 | `iga_opspec_enumerate` | `0x11F40` | 33 | UnwindData |  |
| 23 | `iga_opspec_from_op` | `0x12150` | 107 | UnwindData |  |
| 24 | `iga_opspec_mnemonic` | `0x121C0` | 49 | UnwindData |  |
| 25 | `iga_opspec_name` | `0x12370` | 49 | UnwindData |  |
| 26 | `iga_opspec_op` | `0x12520` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `iga_opspec_op_encoding` | `0x12550` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `iga_platform_names` | `0x12580` | 344 | UnwindData |  |
| 29 | `iga_platform_symbol_suffix` | `0x126E0` | 219 | UnwindData |  |
| 30 | `iga_platforms_list` | `0x127C0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `iga_release_context` | `0x12830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `iga_status_to_string` | `0x12840` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `iga_version_string` | `0x12900` | 14,832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `kv_create` | `0x162F0` | 870 | UnwindData |  |
| 35 | `kv_delete` | `0x16660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `kv_get_channel_offset` | `0x16670` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `kv_get_default_label_name` | `0x166D0` | 120 | UnwindData |  |
| 38 | `kv_get_destination_data_type` | `0x16750` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `kv_get_destination_indirect_imm_off` | `0x167B0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `kv_get_destination_mme_number` | `0x16820` | 135 | UnwindData |  |
| 41 | `kv_get_destination_modifier` | `0x168B0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `kv_get_destination_region` | `0x16910` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `kv_get_destination_register` | `0x16980` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `kv_get_destination_register_kind` | `0x169F0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `kv_get_destination_register_type` | `0x16A50` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `kv_get_destination_sub_register` | `0x16AB0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `kv_get_execution_size` | `0x16B20` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `kv_get_flag_modifier` | `0x16B70` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `kv_get_flag_register` | `0x16BD0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `kv_get_flag_sub_register` | `0x16C30` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `kv_get_has_destination` | `0x16C90` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `kv_get_inst_size` | `0x16CF0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `kv_get_inst_syntax` | `0x16D50` | 145 | UnwindData |  |
| 54 | `kv_get_inst_targets` | `0x16F10` | 121 | UnwindData |  |
| 55 | `kv_get_is_inverse_predicate` | `0x17010` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `kv_get_mask_control` | `0x17070` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `kv_get_message_len` | `0x170D0` | 246 | UnwindData |  |
| 58 | `kv_get_message_len_ext` | `0x171D0` | 184 | UnwindData |  |
| 59 | `kv_get_message_sfid` | `0x17290` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `kv_get_message_type` | `0x17340` | 209 | UnwindData |  |
| 61 | `kv_get_message_type_ext` | `0x17420` | 206 | UnwindData |  |
| 62 | `kv_get_number_sources` | `0x174F0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `kv_get_opcode` | `0x17540` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `kv_get_opgroup` | `0x17590` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `kv_get_predicate` | `0x17640` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `kv_get_send_descs` | `0x176A0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `kv_get_send_exbso` | `0x17770` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `kv_get_send_exdesc_immoff` | `0x17820` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `kv_get_send_indirect_descs` | `0x178E0` | 44 | UnwindData |  |
| 70 | `kv_get_source_data_type` | `0x179D0` | 143 | UnwindData |  |
| 71 | `kv_get_source_immediate` | `0x17A60` | 173 | UnwindData |  |
| 72 | `kv_get_source_indirect_imm_off` | `0x17B10` | 172 | UnwindData |  |
| 73 | `kv_get_source_mme_number` | `0x17BC0` | 175 | UnwindData |  |
| 74 | `kv_get_source_modifier` | `0x17C70` | 148 | UnwindData |  |
| 75 | `kv_get_source_region` | `0x17D10` | 253 | UnwindData |  |
| 76 | `kv_get_source_register` | `0x17E10` | 154 | UnwindData |  |
| 77 | `kv_get_source_register_kind` | `0x17EB0` | 134 | UnwindData |  |
| 78 | `kv_get_source_register_type` | `0x17F40` | 156 | UnwindData |  |
| 79 | `kv_get_source_sub_register` | `0x17FE0` | 159 | UnwindData |  |
| 80 | `kv_get_subfunction` | `0x18080` | 397 | UnwindData |  |
| 81 | `kv_get_swsb_info` | `0x18210` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `kv_has_inst_opt` | `0x18280` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `kv_is_inst_target` | `0x182E0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `kv_is_source_vector` | `0x18340` | 193 | UnwindData |  |
