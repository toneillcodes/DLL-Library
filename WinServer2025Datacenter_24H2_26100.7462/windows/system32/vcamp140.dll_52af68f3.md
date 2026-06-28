# Binary Specification: vcamp140.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\vcamp140.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `52af68f35476bd03d7b97752b01bef358ffdda568d150057d6ce809f77c4f704`
* **Total Exported Functions:** 165

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 127 | `?create_accelerator_view@direct3d@Concurrency@@YA?AVaccelerator_view@2@PEAUIUnknown@@W4queuing_mode@2@@Z` | `0x38F0` | 648 | UnwindData |  |
| 126 | `?create_accelerator_view@direct3d@Concurrency@@YA?AVaccelerator_view@2@AEAVaccelerator@2@_NW4queuing_mode@2@@Z` | `0x3B80` | 233 | UnwindData |  |
| 156 | `?is_timeout_disabled@direct3d@Concurrency@@YA_NAEBVaccelerator_view@2@@Z` | `0x3C70` | 118 | UnwindData |  |
| 79 | `?_Get_preferred_copy_chunk_size@details@Concurrency@@YA_K_K@Z` | `0x50F0` | 25,664 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `?_Get_D3D_buffer@_D3D_interop@details@Concurrency@@SAPEAUIUnknown@@PEAV_Buffer@23@@Z` | `0xB530` | 168 | UnwindData |  |
| 67 | `?_Get_D3D_texture@_D3D_interop@details@Concurrency@@SAPEAUIUnknown@@PEAV_Texture@23@@Z` | `0xB5E0` | 47 | UnwindData |  |
| 66 | `?_Get_D3D_sampler_data_ptr@_D3D_interop@details@Concurrency@@SAPEAXPEAUIUnknown@@@Z` | `0xB610` | 143 | UnwindData |  |
| 107 | `?_Release_D3D_sampler_data_ptr@_D3D_interop@details@Concurrency@@SAXPEAX@Z` | `0xB6A0` | 29 | UnwindData |  |
| 65 | `?_Get_D3D_sampler@_D3D_interop@details@Concurrency@@SAPEAUIUnknown@@AEBVaccelerator_view@3@PEAV_Sampler@23@@Z` | `0xB6C0` | 253 | UnwindData |  |
| 142 | `?get_device@direct3d@Concurrency@@YAPEAUIUnknown@@AEBVaccelerator_view@2@@Z` | `0xB8B0` | 140 | UnwindData |  |
| 130 | `?d3d_access_lock@direct3d@Concurrency@@YAXAEAVaccelerator_view@2@@Z` | `0xB940` | 124 | UnwindData |  |
| 131 | `?d3d_access_try_lock@direct3d@Concurrency@@YA_NAEAVaccelerator_view@2@@Z` | `0xB9C0` | 124 | UnwindData |  |
| 132 | `?d3d_access_unlock@direct3d@Concurrency@@YAXAEAVaccelerator_view@2@@Z` | `0xBA40` | 124 | UnwindData |  |
| 18 | `??0scoped_d3d_access_lock@direct3d@Concurrency@@QEAA@AEAVaccelerator_view@2@@Z` | `0xBAC0` | 148 | UnwindData |  |
| 19 | `??0scoped_d3d_access_lock@direct3d@Concurrency@@QEAA@AEAVaccelerator_view@2@Uadopt_d3d_access_lock_t@12@@Z` | `0xBB60` | 124 | UnwindData |  |
| 27 | `??1scoped_d3d_access_lock@direct3d@Concurrency@@QEAA@XZ` | `0xBBE0` | 75 | UnwindData |  |
| 17 | `??0scoped_d3d_access_lock@direct3d@Concurrency@@QEAA@$$QEAV012@@Z` | `0xBC30` | 140 | UnwindData |  |
| 32 | `??4scoped_d3d_access_lock@direct3d@Concurrency@@QEAAAEAV012@$$QEAV012@@Z` | `0xBCC0` | 229 | UnwindData |  |
| 78 | `?_Get_num_devices@details@Concurrency@@YA_KXZ` | `0xEF30` | 28 | UnwindData |  |
| 75 | `?_Get_devices@details@Concurrency@@YAPEAV?$_Reference_counted_obj_ptr@V_Accelerator_impl@details@Concurrency@@@12@XZ` | `0xEF50` | 17 | UnwindData |  |
| 109 | `?_Select_default_accelerator@details@Concurrency@@YA?AVaccelerator@2@XZ` | `0xEF70` | 131 | UnwindData |  |
| 110 | `?_Set_default_accelerator@details@Concurrency@@YA_NV?$_Reference_counted_obj_ptr@V_Accelerator_impl@details@Concurrency@@@12@@Z` | `0xF000` | 211 | UnwindData |  |
| 87 | `?_Is_D3D_accelerator_view@details@Concurrency@@YA_NAEBVaccelerator_view@2@@Z` | `0xF0E0` | 27,760 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `?get_auto_selection_view@accelerator@Concurrency@@SA?AVaccelerator_view@2@XZ` | `0x15D50` | 155 | UnwindData |  |
| 5 | `??0accelerator@Concurrency@@QEAA@XZ` | `0x15DF0` | 193 | UnwindData |  |
| 86 | `?_Init@accelerator@Concurrency@@AEAAXPEB_W@Z` | `0x15EC0` | 261 | UnwindData |  |
| 23 | `??1_Event@details@Concurrency@@QEAA@XZ` | `0x15FD0` | 41 | UnwindData |  |
| 24 | `??1accelerator@Concurrency@@QEAA@XZ` | `0x15FD0` | 41 | UnwindData |  |
| 25 | `??1accelerator_view@Concurrency@@QEAA@XZ` | `0x15FD0` | 41 | UnwindData |  |
| 1 | `??0_Event@details@Concurrency@@QEAA@AEBV012@@Z` | `0x16000` | 24 | UnwindData |  |
| 4 | `??0accelerator@Concurrency@@QEAA@AEBV01@@Z` | `0x16000` | 24 | UnwindData |  |
| 28 | `??4_Event@details@Concurrency@@QEAAAEAV012@AEBV012@@Z` | `0x16020` | 69 | UnwindData |  |
| 29 | `??4accelerator@Concurrency@@QEAAAEAV01@AEBV01@@Z` | `0x16020` | 69 | UnwindData |  |
| 3 | `??0accelerator@Concurrency@@AEAA@V?$_Reference_counted_obj_ptr@V_Accelerator_impl@details@Concurrency@@@details@1@@Z` | `0x16070` | 68 | UnwindData |  |
| 74 | `?_Get_device_path@accelerator@Concurrency@@AEBAPEB_WXZ` | `0x160C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `?_Get_description@accelerator@Concurrency@@AEBAPEB_WXZ` | `0x160E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `?get_version@accelerator@Concurrency@@QEBAIXZ` | `0x16100` | 69 | UnwindData |  |
| 146 | `?get_is_debug@accelerator@Concurrency@@QEBA_NXZ` | `0x16150` | 69 | UnwindData |  |
| 148 | `?get_is_emulated@accelerator@Concurrency@@QEBA_NXZ` | `0x161A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `?get_has_display@accelerator@Concurrency@@QEBA_NXZ` | `0x161B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | `?get_supports_double_precision@accelerator@Concurrency@@QEBA_NXZ` | `0x161D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `?get_supports_limited_double_precision@accelerator@Concurrency@@QEBA_NXZ` | `0x161E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `?get_supports_cpu_shared_memory@accelerator@Concurrency@@QEBA_NXZ` | `0x161F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `?get_default_view@accelerator@Concurrency@@QEBA?AVaccelerator_view@2@XZ` | `0x16200` | 85 | UnwindData |  |
| 139 | `?get_dedicated_memory@accelerator@Concurrency@@QEBA_KXZ` | `0x16260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `?get_default_cpu_access_type@accelerator@Concurrency@@QEBA?AW4access_type@2@XZ` | `0x16280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `?set_default_cpu_access_type@accelerator@Concurrency@@QEAA_NW4access_type@2@@Z` | `0x162A0` | 192 | UnwindData |  |
| 129 | `?create_view@accelerator@Concurrency@@QEAA?AVaccelerator_view@2@W4queuing_mode@2@@Z` | `0x16360` | 210 | UnwindData |  |
| 33 | `??8_Event@details@Concurrency@@QEBA_NAEBV012@@Z` | `0x16440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `??8accelerator@Concurrency@@QEBA_NAEBV01@@Z` | `0x16440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `??8accelerator_view@Concurrency@@QEBA_NAEBV01@@Z` | `0x16440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `??9_Event@details@Concurrency@@QEBA_NAEBV012@@Z` | `0x16450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `??9accelerator@Concurrency@@QEBA_NAEBV01@@Z` | `0x16450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `??9accelerator_view@Concurrency@@QEBA_NAEBV01@@Z` | `0x16450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `??0accelerator_view@Concurrency@@QEAA@AEBV01@@Z` | `0x16460` | 30 | UnwindData |  |
| 30 | `??4accelerator_view@Concurrency@@QEAAAEAV01@AEBV01@@Z` | `0x16480` | 87 | UnwindData |  |
| 154 | `?get_version@accelerator_view@Concurrency@@QEBAIXZ` | `0x164E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `?get_is_debug@accelerator_view@Concurrency@@QEBA_NXZ` | `0x164F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `?get_queuing_mode@accelerator_view@Concurrency@@QEBA?AW4queuing_mode@2@XZ` | `0x16500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `?get_is_auto_selection@accelerator_view@Concurrency@@QEBA_NXZ` | `0x16510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `?get_accelerator@accelerator_view@Concurrency@@QEBA?AVaccelerator@2@XZ` | `0x16520` | 82 | UnwindData |  |
| 128 | `?create_marker@accelerator_view@Concurrency@@QEAA?AVcompletion_future@2@XZ` | `0x16580` | 306 | UnwindData |  |
| 158 | `?wait@accelerator_view@Concurrency@@QEAAXXZ` | `0x166C0` | 229 | UnwindData |  |
| 136 | `?flush@accelerator_view@Concurrency@@QEAAXXZ` | `0x167B0` | 167 | UnwindData |  |
| 6 | `??0accelerator_view@Concurrency@@AEAA@V?$_Reference_counted_obj_ptr@V_Accelerator_view_impl@details@Concurrency@@@details@1@_N@Z` | `0x16860` | 72 | UnwindData |  |
| 16 | `??0runtime_exception@Concurrency@@QEAA@PEBDJ@Z` | `0x168B0` | 92 | UnwindData |  |
| 15 | `??0runtime_exception@Concurrency@@QEAA@J@Z` | `0x16910` | 95 | UnwindData |  |
| 14 | `??0runtime_exception@Concurrency@@QEAA@AEBV01@@Z` | `0x16970` | 109 | UnwindData |  |
| 31 | `??4runtime_exception@Concurrency@@QEAAAEAV01@AEBV01@@Z` | `0x169E0` | 75 | UnwindData |  |
| 26 | `??1runtime_exception@Concurrency@@UEAA@XZ` | `0x16A30` | 45 | UnwindData |  |
| 143 | `?get_error_code@runtime_exception@Concurrency@@QEBAJXZ` | `0x16A60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `??0out_of_memory@Concurrency@@QEAA@PEBD@Z` | `0x16A70` | 44 | UnwindData |  |
| 13 | `??0out_of_memory@Concurrency@@QEAA@XZ` | `0x16AA0` | 51 | UnwindData |  |
| 9 | `??0accelerator_view_removed@Concurrency@@QEAA@PEBDJ@Z` | `0x16AE0` | 60 | UnwindData |  |
| 8 | `??0accelerator_view_removed@Concurrency@@QEAA@J@Z` | `0x16B20` | 58 | UnwindData |  |
| 155 | `?get_view_removed_reason@accelerator_view_removed@Concurrency@@QEBAJXZ` | `0x16B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `??0invalid_compute_domain@Concurrency@@QEAA@PEBD@Z` | `0x16B70` | 44 | UnwindData |  |
| 11 | `??0invalid_compute_domain@Concurrency@@QEAA@XZ` | `0x16BA0` | 51 | UnwindData |  |
| 20 | `??0unsupported_feature@Concurrency@@QEAA@PEBD@Z` | `0x16BE0` | 44 | UnwindData |  |
| 21 | `??0unsupported_feature@Concurrency@@QEAA@XZ` | `0x16C10` | 51 | UnwindData |  |
| 106 | `?_Release@_Reference_counter@details@Concurrency@@QEAAXXZ` | `0x16C50` | 122 | UnwindData |  |
| 101 | `?_Recursive_array_copy@details@Concurrency@@YAJAEBU_Array_copy_desc@12@IV?$function@$$A6AJAEBU_Array_copy_desc@details@Concurrency@@@Z@std@@@Z` | `0x16CD0` | 1,082 | UnwindData |  |
| 59 | `?_Create_view_shape@_View_shape@details@Concurrency@@SAPEAV123@IIPEBI00PEB_N@Z` | `0x17110` | 114 | UnwindData |  |
| 81 | `?_Get_reduced_shape_for_copy@_View_shape@details@Concurrency@@QEAAPEAV123@XZ` | `0x17190` | 296 | UnwindData |  |
| 52 | `?_Create_buffer@_Buffer@details@Concurrency@@SAPEAV123@Vaccelerator_view@3@0_K1_NW4access_type@3@@Z` | `0x17540` | 357 | UnwindData |  |
| 51 | `?_Create_buffer@_Buffer@details@Concurrency@@SAPEAV123@PEAXVaccelerator_view@3@_K2@Z` | `0x176B0` | 229 | UnwindData |  |
| 53 | `?_Create_stage_buffer@_Buffer@details@Concurrency@@SAPEAV123@Vaccelerator_view@3@0_K1_N@Z` | `0x177A0` | 256 | UnwindData |  |
| 83 | `?_Get_temp_staging_buffer@_Buffer@details@Concurrency@@SAPEAV123@Vaccelerator_view@3@_K1@Z` | `0x178A0` | 151 | UnwindData |  |
| 99 | `?_Map_buffer@_Buffer@details@Concurrency@@QEAAXW4_Access_mode@@_N@Z` | `0x17940` | 38 | UnwindData |  |
| 100 | `?_Map_buffer_async@_Buffer@details@Concurrency@@QEAA?AV_Event@23@W4_Access_mode@@@Z` | `0x17970` | 63 | UnwindData |  |
| 120 | `?_Unmap_buffer@_Buffer@details@Concurrency@@QEAAXXZ` | `0x179B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `?_Copy_to_async@_Buffer@details@Concurrency@@QEAA?AV_Event@23@PEAV123@_K11@Z` | `0x179D0` | 216 | UnwindData |  |
| 46 | `?_Copy_to_async@_Buffer@details@Concurrency@@QEAA?AV_Event@23@PEAV123@V?$_Reference_counted_obj_ptr@V_View_shape@details@Concurrency@@@23@1@Z` | `0x17AB0` | 437 | UnwindData |  |
| 68 | `?_Get_accelerator_view@_Buffer@details@Concurrency@@QEBA?AVaccelerator_view@3@XZ` | `0x17C70` | 82 | UnwindData |  |
| 76 | `?_Get_master_accelerator_view@_Ubiquitous_buffer@details@Concurrency@@QEBA?AVaccelerator_view@3@XZ` | `0x17C70` | 82 | UnwindData |  |
| 71 | `?_Get_access_on_accelerator_view@_Buffer@details@Concurrency@@QEBA?AVaccelerator_view@3@XZ` | `0x17CD0` | 82 | UnwindData |  |
| 103 | `?_Register_view@_Buffer@details@Concurrency@@QEAAXPEAU_Buffer_descriptor@23@@Z` | `0x17D30` | 362 | UnwindData |  |
| 121 | `?_Unregister_view@_Buffer@details@Concurrency@@QEAAXPEAU_Buffer_descriptor@23@@Z` | `0x17EA0` | 61 | UnwindData |  |
| 61 | `?_Exclusively_owns_data@_Buffer@details@Concurrency@@QEAA_NXZ` | `0x17EE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `?_Is_mappable@_Buffer@details@Concurrency@@QEBA_NXZ` | `0x17F00` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `?_Create_texture@_Texture@details@Concurrency@@SAPEAV123@Vaccelerator_view@3@I_K11IW4_Short_vector_base_type_id@23@II_N@Z` | `0x180C0` | 436 | UnwindData |  |
| 41 | `?_Adopt_texture@_Texture@details@Concurrency@@SAPEAV123@IW4_Short_vector_base_type_id@23@PEAUIUnknown@@Vaccelerator_view@3@I@Z` | `0x18280` | 703 | UnwindData |  |
| 54 | `?_Create_stage_texture@_Texture@details@Concurrency@@SAPEAV123@Vaccelerator_view@3@0I_K11II_N@Z` | `0x18540` | 372 | UnwindData |  |
| 84 | `?_Get_temp_staging_texture@_Texture@details@Concurrency@@SAPEAV123@Vaccelerator_view@3@I_K11II@Z` | `0x186C0` | 356 | UnwindData |  |
| 55 | `?_Create_stage_texture@_Texture@details@Concurrency@@SAPEAV123@Vaccelerator_view@3@0I_K11IW4_Short_vector_base_type_id@23@II@Z` | `0x18830` | 466 | UnwindData |  |
| 48 | `?_Copy_to_async@_Texture@details@Concurrency@@QEAA?AV_Event@23@PEAV123@PEB_K11II@Z` | `0x18A10` | 205 | UnwindData |  |
| 42 | `?_Clone_texture@_Texture@details@Concurrency@@SAPEAV123@PEBV123@AEBVaccelerator_view@3@1@Z` | `0x18AE0` | 135 | UnwindData |  |
| 58 | `?_Create_ubiquitous_buffer@_Ubiquitous_buffer@details@Concurrency@@SAPEAV123@_K0@Z` | `0x18D40` | 148 | UnwindData |  |
| 57 | `?_Create_ubiquitous_buffer@_Ubiquitous_buffer@details@Concurrency@@SAPEAV123@V?$_Reference_counted_obj_ptr@V_Buffer@details@Concurrency@@@23@@Z` | `0x18DE0` | 87 | UnwindData |  |
| 104 | `?_Register_view@_Ubiquitous_buffer@details@Concurrency@@QEAAXPEAU_Buffer_descriptor@23@Vaccelerator_view@3@V?$_Reference_counted_obj_ptr@V_View_shape@details@Concurrency@@@23@QEAU423@@Z` | `0x18E40` | 458 | UnwindData |  |
| 105 | `?_Register_view_copy@_Ubiquitous_buffer@details@Concurrency@@QEAAXPEAU_Buffer_descriptor@23@0@Z` | `0x19010` | 201 | UnwindData |  |
| 122 | `?_Unregister_view@_Ubiquitous_buffer@details@Concurrency@@QEAAXPEAU_Buffer_descriptor@23@@Z` | `0x190E0` | 410 | UnwindData |  |
| 69 | `?_Get_access_async@_Ubiquitous_buffer@details@Concurrency@@AEAA?AV_Event@23@PEAU_Buffer_descriptor@23@Vaccelerator_view@3@W4_Access_mode@@AEAV?$_Reference_counted_obj_ptr@V_Buffer@details@Concurrency@@@23@PEA_K@Z` | `0x193C0` | 136 | UnwindData |  |
| 70 | `?_Get_access_async@_Ubiquitous_buffer@details@Concurrency@@QEAA?AV_Event@23@PEAU_Buffer_descriptor@23@V?$_Reference_counted_obj_ptr@V_Accelerator_view_impl@details@Concurrency@@@23@W4_Access_mode@@AEAV?$_Reference_counted_obj_ptr@V_Buffer@details@Concurrency@@@23@PEA_K@Z` | `0x19450` | 4,873 | UnwindData |  |
| 60 | `?_Discard@_Ubiquitous_buffer@details@Concurrency@@QEAAXPEAU_Buffer_descriptor@23@@Z` | `0x1AB80` | 186 | UnwindData |  |
| 77 | `?_Get_master_buffer@_Ubiquitous_buffer@details@Concurrency@@QEBA?AV?$_Reference_counted_obj_ptr@V_Buffer@details@Concurrency@@@23@XZ` | `0x1AC40` | 48 | UnwindData |  |
| 85 | `?_Get_view_shape@_Ubiquitous_buffer@details@Concurrency@@QEAA?AV?$_Reference_counted_obj_ptr@V_View_shape@details@Concurrency@@@23@PEAU_Buffer_descriptor@23@@Z` | `0x1AC70` | 135 | UnwindData |  |
| 63 | `?_Get_CPU_access@_Buffer_descriptor@details@Concurrency@@QEBAXW4_Access_mode@@@Z` | `0x1C170` | 322 | UnwindData |  |
| 49 | `?_Create@_Sampler@details@Concurrency@@SAPEAV123@IIMMMM@Z` | `0x1C2C0` | 150 | UnwindData |  |
| 50 | `?_Create@_Sampler@details@Concurrency@@SAPEAV123@PEAX@Z` | `0x1C360` | 75 | UnwindData |  |
| 102 | `?_Register_async_event@details@Concurrency@@YAXAEBV_Event@12@AEBV?$shared_future@X@std@@@Z` | `0x1C430` | 368 | UnwindData |  |
| 45 | `?_Copy_impl@details@Concurrency@@YA?AV_Event@12@PEAV_Buffer@12@_K0111@Z` | `0x1C5A0` | 2,249 | UnwindData |  |
| 44 | `?_Copy_impl@details@Concurrency@@YA?AV_Event@12@PEAV_Buffer@12@V?$_Reference_counted_obj_ptr@V_View_shape@details@Concurrency@@@12@01@Z` | `0x1CF70` | 3,541 | UnwindData |  |
| 43 | `?_Copy_async_impl@details@Concurrency@@YA?AV_Event@12@PEAV_Texture@12@PEB_KI01I11@Z` | `0x1DFD0` | 2,962 | UnwindData |  |
| 108 | `?_Select_copy_src_accelerator_view@details@Concurrency@@YA?AVaccelerator_view@2@PEAU_Buffer_descriptor@12@AEBV32@@Z` | `0x1EC20` | 778 | UnwindData |  |
| 80 | `?_Get_recommended_buffer_host_access_mode@details@Concurrency@@YA?AW4_Access_mode@@AEBVaccelerator_view@2@@Z` | `0x1EF30` | 70 | UnwindData |  |
| 82 | `?_Get_src_dest_accelerator_view@details@Concurrency@@YA?AU?$pair@Vaccelerator_view@Concurrency@@V12@@std@@PEBU_Buffer_descriptor@12@0@Z` | `0x1EF80` | 574 | UnwindData |  |
| 124 | `?amp_uninitialize@Concurrency@@YAXXZ` | `0x1F1F0` | 36,624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `__dpc_create_call_handle` | `0x28100` | 132 | UnwindData |  |
| 161 | `__dpc_release_call_handle` | `0x28190` | 37 | UnwindData |  |
| 163 | `__dpc_set_device_resource_info` | `0x281C0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 165 | `__dpc_set_kernel_shader_info` | `0x28210` | 128 | UnwindData |  |
| 162 | `__dpc_set_const_buffer_info` | `0x28290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 164 | `__dpc_set_kernel_dispatch_info` | `0x282A0` | 1,236 | UnwindData |  |
| 160 | `__dpc_dispatch_kernel` | `0x28780` | 78 | UnwindData |  |
| 2 | `??0_Event@details@Concurrency@@QEAA@XZ` | `0x2F690` | 16 | UnwindData |  |
| 90 | `?_Is_finished_nothrow@_Event@details@Concurrency@@QEAA_NXZ` | `0x2F6A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `?_Is_finished@_Event@details@Concurrency@@QEAA_NXZ` | `0x2F6B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `?_Is_empty@_Event@details@Concurrency@@QEBA_NXZ` | `0x2F6C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `?_Get@_Event@details@Concurrency@@QEAAXXZ` | `0x2F6D0` | 22 | UnwindData |  |
| 40 | `?_Add_event@_Event@details@Concurrency@@QEAA?AV123@V123@@Z` | `0x2F6F0` | 404 | UnwindData |  |
| 39 | `?_Add_continuation@_Event@details@Concurrency@@QEAA?AV123@AEBV?$function@$$A6A?AV_Event@details@Concurrency@@XZ@std@@@Z` | `0x2F890` | 263 | UnwindData |  |
| 22 | `??1_Amp_runtime_trace@details@Concurrency@@QEAA@XZ` | `0x30FD0` | 99 | UnwindData |  |
| 72 | `?_Get_amp_trace@details@Concurrency@@YAPEAV_Amp_runtime_trace@12@XZ` | `0x31100` | 108 | UnwindData |  |
| 123 | `?_Write_end_event@_Amp_runtime_trace@details@Concurrency@@QEAAXK@Z` | `0x31220` | 94 | UnwindData |  |
| 112 | `?_Start_async_op_wait_event@_Amp_runtime_trace@details@Concurrency@@AEAAKK@Z` | `0x31460` | 132 | UnwindData |  |
| 119 | `?_Start_parallel_for_each_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKPEAU_DPC_call_handle@23@@Z` | `0x314F0` | 894 | UnwindData |  |
| 111 | `?_Start_array_view_synchronize_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Buffer_descriptor@23@@Z` | `0x31870` | 366 | UnwindData |  |
| 92 | `?_Launch_array_view_synchronize_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Buffer_descriptor@23@@Z` | `0x319E0` | 366 | UnwindData |  |
| 116 | `?_Start_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Buffer_descriptor@23@0_K@Z` | `0x31C70` | 258 | UnwindData |  |
| 113 | `?_Start_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAK$$TAEBU_Buffer_descriptor@23@_K@Z` | `0x31D80` | 208 | UnwindData |  |
| 115 | `?_Start_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Buffer_descriptor@23@$$T_K@Z` | `0x31E50` | 213 | UnwindData |  |
| 96 | `?_Launch_async_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Buffer_descriptor@23@0_K@Z` | `0x31F30` | 258 | UnwindData |  |
| 93 | `?_Launch_async_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAK$$TAEBU_Buffer_descriptor@23@_K@Z` | `0x32040` | 208 | UnwindData |  |
| 95 | `?_Launch_async_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Buffer_descriptor@23@$$T_K@Z` | `0x32110` | 213 | UnwindData |  |
| 117 | `?_Start_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Texture_descriptor@23@$$T_K@Z` | `0x321F0` | 86 | UnwindData |  |
| 114 | `?_Start_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAK$$TAEBU_Texture_descriptor@23@_K@Z` | `0x32250` | 76 | UnwindData |  |
| 118 | `?_Start_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Texture_descriptor@23@0_K@Z` | `0x322A0` | 101 | UnwindData |  |
| 97 | `?_Launch_async_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Texture_descriptor@23@$$T_K@Z` | `0x32310` | 86 | UnwindData |  |
| 94 | `?_Launch_async_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAK$$TAEBU_Texture_descriptor@23@_K@Z` | `0x32370` | 76 | UnwindData |  |
| 98 | `?_Launch_async_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Texture_descriptor@23@0_K@Z` | `0x323C0` | 101 | UnwindData |  |
| 133 | `?default_accelerator@accelerator@Concurrency@@2QB_WB` | `0x40790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `?cpu_accelerator@accelerator@Concurrency@@2QB_WB` | `0x407A0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `?direct3d_warp@accelerator@Concurrency@@2QB_WB` | `0x407A8` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `?direct3d_ref@accelerator@Concurrency@@2QB_WB` | `0x407C8` | 0 | Indeterminate |  |
