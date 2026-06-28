# Binary Specification: iga32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_1973c0a49e1f4f8c\iga32.dll`
* **Architecture:** x86
* **SHA256 Fingerprint:** `a67158750554645804071f83514706132fa3a2fa67426006bf73299d7f14bdae`
* **Total Exported Functions:** 84

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `iga_assemble` | `0x104D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `iga_context_assemble` | `0x104E0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `iga_context_create` | `0x105F0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `iga_context_disassemble` | `0x10790` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `iga_context_disassemble_instruction` | `0x10890` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `iga_context_get_errors` | `0x10980` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `iga_context_get_warnings` | `0x10A10` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `iga_context_release` | `0x10AA0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `iga_create_context` | `0x10B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `iga_diagnostic_get_message` | `0x10B50` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `iga_diagnostic_get_offset` | `0x10B80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `iga_diagnostic_get_text_column` | `0x10BB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `iga_diagnostic_get_text_extent` | `0x10BE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `iga_diagnostic_get_text_line` | `0x10C10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `iga_diagnostic_get_type` | `0x10C40` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `iga_disassemble` | `0x10C80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `iga_disassemble_instruction` | `0x10C90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `iga_get_errors` | `0x10CA0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `iga_get_interface` | `0x10D40` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `iga_get_warnings` | `0x10DE0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `iga_opspec_description` | `0x10E80` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `iga_opspec_enumerate` | `0x10EE0` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `iga_opspec_from_op` | `0x11060` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `iga_opspec_mnemonic` | `0x110B0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `iga_opspec_name` | `0x11210` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `iga_opspec_op` | `0x11370` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `iga_opspec_op_encoding` | `0x113A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `iga_platform_names` | `0x113D0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `iga_platform_symbol_suffix` | `0x114E0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `iga_platforms_list` | `0x11590` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `iga_release_context` | `0x115F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `iga_status_to_string` | `0x11600` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `iga_version_string` | `0x116A0` | 11,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `kv_create` | `0x14360` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `kv_delete` | `0x146C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `kv_get_channel_offset` | `0x146E0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `kv_get_default_label_name` | `0x14740` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `kv_get_destination_data_type` | `0x147B0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `kv_get_destination_indirect_imm_off` | `0x14810` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `kv_get_destination_mme_number` | `0x14880` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `kv_get_destination_modifier` | `0x14900` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `kv_get_destination_region` | `0x14960` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `kv_get_destination_register` | `0x149E0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `kv_get_destination_register_kind` | `0x14A60` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `kv_get_destination_register_type` | `0x14AC0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `kv_get_destination_sub_register` | `0x14B20` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `kv_get_execution_size` | `0x14BA0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `kv_get_flag_modifier` | `0x14C00` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `kv_get_flag_register` | `0x14C60` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `kv_get_flag_sub_register` | `0x14CC0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `kv_get_has_destination` | `0x14D20` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `kv_get_inst_size` | `0x14D80` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `kv_get_inst_syntax` | `0x14DF0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `kv_get_inst_targets` | `0x14F30` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `kv_get_is_inverse_predicate` | `0x14FF0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `kv_get_mask_control` | `0x15050` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `kv_get_message_len` | `0x150B0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `kv_get_message_len_ext` | `0x15190` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `kv_get_message_sfid` | `0x15210` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `kv_get_message_type` | `0x152D0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `kv_get_message_type_ext` | `0x153A0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `kv_get_number_sources` | `0x15450` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `kv_get_opcode` | `0x154B0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `kv_get_opgroup` | `0x15510` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `kv_get_predicate` | `0x15630` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `kv_get_send_descs` | `0x15690` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `kv_get_send_exbso` | `0x15730` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `kv_get_send_exdesc_immoff` | `0x157E0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `kv_get_send_indirect_descs` | `0x158B0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `kv_get_source_data_type` | `0x159A0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `kv_get_source_immediate` | `0x15A20` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `kv_get_source_indirect_imm_off` | `0x15AB0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `kv_get_source_mme_number` | `0x15B30` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `kv_get_source_modifier` | `0x15BC0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `kv_get_source_region` | `0x15C40` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `kv_get_source_register` | `0x15D10` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `kv_get_source_register_kind` | `0x15DA0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `kv_get_source_register_type` | `0x15E10` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `kv_get_source_sub_register` | `0x15E90` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `kv_get_subfunction` | `0x15F20` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `kv_get_swsb_info` | `0x15FD0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `kv_has_inst_opt` | `0x16040` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `kv_is_inst_target` | `0x160A0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `kv_is_source_vector` | `0x16100` | 747,194 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
