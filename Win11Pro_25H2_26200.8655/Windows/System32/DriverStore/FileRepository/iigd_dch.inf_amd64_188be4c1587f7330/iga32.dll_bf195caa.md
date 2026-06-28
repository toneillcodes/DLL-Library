# Binary Specification: iga32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_188be4c1587f7330\iga32.dll`
* **Architecture:** x86
* **SHA256 Fingerprint:** `bf195caaa317fefd8a76b813e0749aa5253a28d54ceee6e5c4fb39b29648e7a5`
* **Total Exported Functions:** 84

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `iga_assemble` | `0x11150` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `iga_context_assemble` | `0x11160` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `iga_context_create` | `0x11270` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `iga_context_disassemble` | `0x11410` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `iga_context_disassemble_instruction` | `0x11510` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `iga_context_get_errors` | `0x11600` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `iga_context_get_warnings` | `0x11690` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `iga_context_release` | `0x11720` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `iga_create_context` | `0x117C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `iga_diagnostic_get_message` | `0x117D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `iga_diagnostic_get_offset` | `0x11800` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `iga_diagnostic_get_text_column` | `0x11830` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `iga_diagnostic_get_text_extent` | `0x11860` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `iga_diagnostic_get_text_line` | `0x11890` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `iga_diagnostic_get_type` | `0x118C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `iga_disassemble` | `0x11900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `iga_disassemble_instruction` | `0x11910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `iga_get_errors` | `0x11920` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `iga_get_interface` | `0x119C0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `iga_get_warnings` | `0x11A60` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `iga_opspec_description` | `0x11B00` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `iga_opspec_enumerate` | `0x11B60` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `iga_opspec_from_op` | `0x11CF0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `iga_opspec_mnemonic` | `0x11D40` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `iga_opspec_name` | `0x11EA0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `iga_opspec_op` | `0x12000` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `iga_opspec_op_encoding` | `0x12030` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `iga_platform_names` | `0x12060` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `iga_platform_symbol_suffix` | `0x12170` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `iga_platforms_list` | `0x12220` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `iga_release_context` | `0x12280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `iga_status_to_string` | `0x12290` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `iga_version_string` | `0x12330` | 11,728 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `kv_create` | `0x15100` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `kv_delete` | `0x15460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `kv_get_channel_offset` | `0x15480` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `kv_get_default_label_name` | `0x154E0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `kv_get_destination_data_type` | `0x15550` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `kv_get_destination_indirect_imm_off` | `0x155B0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `kv_get_destination_mme_number` | `0x15620` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `kv_get_destination_modifier` | `0x156B0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `kv_get_destination_region` | `0x15710` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `kv_get_destination_register` | `0x15790` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `kv_get_destination_register_kind` | `0x15810` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `kv_get_destination_register_type` | `0x15870` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `kv_get_destination_sub_register` | `0x158D0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `kv_get_execution_size` | `0x15950` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `kv_get_flag_modifier` | `0x159B0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `kv_get_flag_register` | `0x15A10` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `kv_get_flag_sub_register` | `0x15A70` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `kv_get_has_destination` | `0x15AD0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `kv_get_inst_size` | `0x15B30` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `kv_get_inst_syntax` | `0x15BA0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `kv_get_inst_targets` | `0x15CF0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `kv_get_is_inverse_predicate` | `0x15DB0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `kv_get_mask_control` | `0x15E10` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `kv_get_message_len` | `0x15E70` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `kv_get_message_len_ext` | `0x15F50` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `kv_get_message_sfid` | `0x15FD0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `kv_get_message_type` | `0x16090` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `kv_get_message_type_ext` | `0x16160` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `kv_get_number_sources` | `0x16210` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `kv_get_opcode` | `0x16270` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `kv_get_opgroup` | `0x162D0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `kv_get_predicate` | `0x16400` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `kv_get_send_descs` | `0x16460` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `kv_get_send_exbso` | `0x16500` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `kv_get_send_exdesc_immoff` | `0x165B0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `kv_get_send_indirect_descs` | `0x16680` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `kv_get_source_data_type` | `0x16770` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `kv_get_source_immediate` | `0x167F0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `kv_get_source_indirect_imm_off` | `0x16880` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `kv_get_source_mme_number` | `0x16900` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `kv_get_source_modifier` | `0x16990` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `kv_get_source_region` | `0x16A10` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `kv_get_source_register` | `0x16AE0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `kv_get_source_register_kind` | `0x16B70` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `kv_get_source_register_type` | `0x16BE0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `kv_get_source_sub_register` | `0x16C60` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `kv_get_subfunction` | `0x16CF0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `kv_get_swsb_info` | `0x16DA0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `kv_has_inst_opt` | `0x16E10` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `kv_is_inst_target` | `0x16E70` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `kv_is_source_vector` | `0x16ED0` | 740,298 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
