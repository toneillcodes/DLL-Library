# Binary Specification: vcamp120.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\vcamp120.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `88a5ed51a7be4ff7ebded0c107fafda6ace3801877216c0bb6cbb458ae054a7b`
* **Total Exported Functions:** 165

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 127 | `?create_accelerator_view@direct3d@Concurrency@@YA?AVaccelerator_view@2@PEAUIUnknown@@W4queuing_mode@2@@Z` | `0x6E7C` | 940 | UnwindData |  |
| 126 | `?create_accelerator_view@direct3d@Concurrency@@YA?AVaccelerator_view@2@AEAVaccelerator@2@_NW4queuing_mode@2@@Z` | `0x7228` | 309 | UnwindData |  |
| 156 | `?is_timeout_disabled@direct3d@Concurrency@@YA_NAEBVaccelerator_view@2@@Z` | `0x7360` | 160 | UnwindData |  |
| 79 | `?_Get_preferred_copy_chunk_size@details@Concurrency@@YA_K_K@Z` | `0x853C` | 25,988 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `?_Get_D3D_buffer@_D3D_interop@details@Concurrency@@SAPEAUIUnknown@@PEAV_Buffer@23@@Z` | `0xEAC0` | 266 | UnwindData |  |
| 67 | `?_Get_D3D_texture@_D3D_interop@details@Concurrency@@SAPEAUIUnknown@@PEAV_Texture@23@@Z` | `0xEBCC` | 43 | UnwindData |  |
| 66 | `?_Get_D3D_sampler_data_ptr@_D3D_interop@details@Concurrency@@SAPEAXPEAUIUnknown@@@Z` | `0xEBF8` | 93 | UnwindData |  |
| 107 | `?_Release_D3D_sampler_data_ptr@_D3D_interop@details@Concurrency@@SAXPEAX@Z` | `0xEC58` | 29 | UnwindData |  |
| 65 | `?_Get_D3D_sampler@_D3D_interop@details@Concurrency@@SAPEAUIUnknown@@AEBVaccelerator_view@3@PEAV_Sampler@23@@Z` | `0xEC78` | 273 | UnwindData |  |
| 142 | `?get_device@direct3d@Concurrency@@YAPEAUIUnknown@@AEBVaccelerator_view@2@@Z` | `0xEE64` | 175 | UnwindData |  |
| 130 | `?d3d_access_lock@direct3d@Concurrency@@YAXAEAVaccelerator_view@2@@Z` | `0xEF14` | 166 | UnwindData |  |
| 131 | `?d3d_access_try_lock@direct3d@Concurrency@@YA_NAEAVaccelerator_view@2@@Z` | `0xEFBC` | 166 | UnwindData |  |
| 132 | `?d3d_access_unlock@direct3d@Concurrency@@YAXAEAVaccelerator_view@2@@Z` | `0xF064` | 166 | UnwindData |  |
| 18 | `??0scoped_d3d_access_lock@direct3d@Concurrency@@QEAA@AEAVaccelerator_view@2@@Z` | `0xF10C` | 195 | UnwindData |  |
| 19 | `??0scoped_d3d_access_lock@direct3d@Concurrency@@QEAA@AEAVaccelerator_view@2@Uadopt_d3d_access_lock_t@12@@Z` | `0xF1D0` | 178 | UnwindData |  |
| 27 | `??1scoped_d3d_access_lock@direct3d@Concurrency@@QEAA@XZ` | `0xF284` | 69 | UnwindData |  |
| 17 | `??0scoped_d3d_access_lock@direct3d@Concurrency@@QEAA@$$QEAV012@@Z` | `0xF2CC` | 160 | UnwindData |  |
| 32 | `??4scoped_d3d_access_lock@direct3d@Concurrency@@QEAAAEAV012@$$QEAV012@@Z` | `0xF36C` | 255 | UnwindData |  |
| 78 | `?_Get_num_devices@details@Concurrency@@YA_KXZ` | `0x12FA8` | 28 | UnwindData |  |
| 75 | `?_Get_devices@details@Concurrency@@YAPEAV?$_Reference_counted_obj_ptr@V_Accelerator_impl@details@Concurrency@@@12@XZ` | `0x12FC4` | 17 | UnwindData |  |
| 109 | `?_Select_default_accelerator@details@Concurrency@@YA?AVaccelerator@2@XZ` | `0x12FD8` | 136 | UnwindData |  |
| 110 | `?_Set_default_accelerator@details@Concurrency@@YA_NV?$_Reference_counted_obj_ptr@V_Accelerator_impl@details@Concurrency@@@12@@Z` | `0x13060` | 217 | UnwindData |  |
| 87 | `?_Is_D3D_accelerator_view@details@Concurrency@@YA_NAEBVaccelerator_view@2@@Z` | `0x1313C` | 21,468 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `?get_auto_selection_view@accelerator@Concurrency@@SA?AVaccelerator_view@2@XZ` | `0x18518` | 195 | UnwindData |  |
| 5 | `??0accelerator@Concurrency@@QEAA@XZ` | `0x185DC` | 230 | UnwindData |  |
| 86 | `?_Init@accelerator@Concurrency@@AEAAXPEB_W@Z` | `0x186C4` | 306 | UnwindData |  |
| 23 | `??1_Event@details@Concurrency@@QEAA@XZ` | `0x187F8` | 42 | UnwindData |  |
| 24 | `??1accelerator@Concurrency@@QEAA@XZ` | `0x187F8` | 42 | UnwindData |  |
| 25 | `??1accelerator_view@Concurrency@@QEAA@XZ` | `0x187F8` | 42 | UnwindData |  |
| 1 | `??0_Event@details@Concurrency@@QEAA@AEBV012@@Z` | `0x18824` | 40 | UnwindData |  |
| 4 | `??0accelerator@Concurrency@@QEAA@AEBV01@@Z` | `0x18824` | 40 | UnwindData |  |
| 28 | `??4_Event@details@Concurrency@@QEAAAEAV012@AEBV012@@Z` | `0x1884C` | 62 | UnwindData |  |
| 29 | `??4accelerator@Concurrency@@QEAAAEAV01@AEBV01@@Z` | `0x1884C` | 62 | UnwindData |  |
| 3 | `??0accelerator@Concurrency@@AEAA@V?$_Reference_counted_obj_ptr@V_Accelerator_impl@details@Concurrency@@@details@1@@Z` | `0x1888C` | 70 | UnwindData |  |
| 74 | `?_Get_device_path@accelerator@Concurrency@@AEBAPEB_WXZ` | `0x188D4` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `?_Get_description@accelerator@Concurrency@@AEBAPEB_WXZ` | `0x188E0` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `?get_version@accelerator@Concurrency@@QEBAIXZ` | `0x188EC` | 50 | UnwindData |  |
| 146 | `?get_is_debug@accelerator@Concurrency@@QEBA_NXZ` | `0x18920` | 50 | UnwindData |  |
| 148 | `?get_is_emulated@accelerator@Concurrency@@QEBA_NXZ` | `0x18954` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `?get_has_display@accelerator@Concurrency@@QEBA_NXZ` | `0x1895C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | `?get_supports_double_precision@accelerator@Concurrency@@QEBA_NXZ` | `0x18968` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `?get_supports_limited_double_precision@accelerator@Concurrency@@QEBA_NXZ` | `0x18974` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `?get_supports_cpu_shared_memory@accelerator@Concurrency@@QEBA_NXZ` | `0x18980` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `?get_default_view@accelerator@Concurrency@@QEBA?AVaccelerator_view@2@XZ` | `0x18988` | 115 | UnwindData |  |
| 139 | `?get_dedicated_memory@accelerator@Concurrency@@QEBA_KXZ` | `0x189FC` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `?get_default_cpu_access_type@accelerator@Concurrency@@QEBA?AW4access_type@2@XZ` | `0x18A08` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `?set_default_cpu_access_type@accelerator@Concurrency@@QEAA_NW4access_type@2@@Z` | `0x18A24` | 252 | UnwindData |  |
| 129 | `?create_view@accelerator@Concurrency@@QEAA?AVaccelerator_view@2@W4queuing_mode@2@@Z` | `0x18B20` | 186 | UnwindData |  |
| 33 | `??8_Event@details@Concurrency@@QEBA_NAEBV012@@Z` | `0x18BDC` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `??8accelerator@Concurrency@@QEBA_NAEBV01@@Z` | `0x18BDC` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `??8accelerator_view@Concurrency@@QEBA_NAEBV01@@Z` | `0x18BDC` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `??9_Event@details@Concurrency@@QEBA_NAEBV012@@Z` | `0x18BE8` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `??9accelerator@Concurrency@@QEBA_NAEBV01@@Z` | `0x18BE8` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `??9accelerator_view@Concurrency@@QEBA_NAEBV01@@Z` | `0x18BE8` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `??0accelerator_view@Concurrency@@QEAA@AEBV01@@Z` | `0x18BF4` | 46 | UnwindData |  |
| 30 | `??4accelerator_view@Concurrency@@QEAAAEAV01@AEBV01@@Z` | `0x18C24` | 80 | UnwindData |  |
| 154 | `?get_version@accelerator_view@Concurrency@@QEBAIXZ` | `0x18C74` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `?get_is_debug@accelerator_view@Concurrency@@QEBA_NXZ` | `0x18C7C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `?get_queuing_mode@accelerator_view@Concurrency@@QEBA?AW4queuing_mode@2@XZ` | `0x18C84` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `?get_is_auto_selection@accelerator_view@Concurrency@@QEBA_NXZ` | `0x18C8C` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `?get_accelerator@accelerator_view@Concurrency@@QEBA?AVaccelerator@2@XZ` | `0x18C90` | 116 | UnwindData |  |
| 128 | `?create_marker@accelerator_view@Concurrency@@QEAA?AVcompletion_future@2@XZ` | `0x18D04` | 311 | UnwindData |  |
| 158 | `?wait@accelerator_view@Concurrency@@QEAAXXZ` | `0x18E3C` | 221 | UnwindData |  |
| 136 | `?flush@accelerator_view@Concurrency@@QEAAXXZ` | `0x18F1C` | 165 | UnwindData |  |
| 6 | `??0accelerator_view@Concurrency@@AEAA@V?$_Reference_counted_obj_ptr@V_Accelerator_view_impl@details@Concurrency@@@details@1@_N@Z` | `0x18FC4` | 74 | UnwindData |  |
| 16 | `??0runtime_exception@Concurrency@@QEAA@PEBDJ@Z` | `0x19010` | 72 | UnwindData |  |
| 15 | `??0runtime_exception@Concurrency@@QEAA@J@Z` | `0x19058` | 78 | UnwindData |  |
| 14 | `??0runtime_exception@Concurrency@@QEAA@AEBV01@@Z` | `0x190A8` | 89 | UnwindData |  |
| 31 | `??4runtime_exception@Concurrency@@QEAAAEAV01@AEBV01@@Z` | `0x19104` | 47 | UnwindData |  |
| 26 | `??1runtime_exception@Concurrency@@UEAA@XZ` | `0x19134` | 39 | UnwindData |  |
| 143 | `?get_error_code@runtime_exception@Concurrency@@QEBAJXZ` | `0x1915C` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `??0out_of_memory@Concurrency@@QEAA@PEBD@Z` | `0x19160` | 53 | UnwindData |  |
| 13 | `??0out_of_memory@Concurrency@@QEAA@XZ` | `0x19198` | 60 | UnwindData |  |
| 9 | `??0accelerator_view_removed@Concurrency@@QEAA@PEBDJ@Z` | `0x191D4` | 69 | UnwindData |  |
| 8 | `??0accelerator_view_removed@Concurrency@@QEAA@J@Z` | `0x1921C` | 67 | UnwindData |  |
| 155 | `?get_view_removed_reason@accelerator_view_removed@Concurrency@@QEBAJXZ` | `0x19260` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `??0invalid_compute_domain@Concurrency@@QEAA@PEBD@Z` | `0x19264` | 53 | UnwindData |  |
| 11 | `??0invalid_compute_domain@Concurrency@@QEAA@XZ` | `0x1929C` | 60 | UnwindData |  |
| 20 | `??0unsupported_feature@Concurrency@@QEAA@PEBD@Z` | `0x192D8` | 53 | UnwindData |  |
| 21 | `??0unsupported_feature@Concurrency@@QEAA@XZ` | `0x19310` | 60 | UnwindData |  |
| 106 | `?_Release@_Reference_counter@details@Concurrency@@QEAAXXZ` | `0x1934C` | 82 | UnwindData |  |
| 101 | `?_Recursive_array_copy@details@Concurrency@@YAJAEBU_Array_copy_desc@12@IV?$function@$$A6AJAEBU_Array_copy_desc@details@Concurrency@@@Z@std@@@Z` | `0x193A0` | 1,034 | UnwindData |  |
| 59 | `?_Create_view_shape@_View_shape@details@Concurrency@@SAPEAV123@IIPEBI00PEB_N@Z` | `0x197AC` | 130 | UnwindData |  |
| 81 | `?_Get_reduced_shape_for_copy@_View_shape@details@Concurrency@@QEAAPEAV123@XZ` | `0x19830` | 362 | UnwindData |  |
| 52 | `?_Create_buffer@_Buffer@details@Concurrency@@SAPEAV123@Vaccelerator_view@3@0_K1_NW4access_type@3@@Z` | `0x19B80` | 386 | UnwindData |  |
| 51 | `?_Create_buffer@_Buffer@details@Concurrency@@SAPEAV123@PEAXVaccelerator_view@3@_K2@Z` | `0x19D04` | 255 | UnwindData |  |
| 53 | `?_Create_stage_buffer@_Buffer@details@Concurrency@@SAPEAV123@Vaccelerator_view@3@0_K1_N@Z` | `0x19E04` | 204 | UnwindData |  |
| 83 | `?_Get_temp_staging_buffer@_Buffer@details@Concurrency@@SAPEAV123@Vaccelerator_view@3@_K1@Z` | `0x19ED0` | 117 | UnwindData |  |
| 99 | `?_Map_buffer@_Buffer@details@Concurrency@@QEAAXW4_Access_mode@@_N@Z` | `0x19F48` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `?_Map_buffer_async@_Buffer@details@Concurrency@@QEAA?AV_Event@23@W4_Access_mode@@@Z` | `0x19F60` | 62 | UnwindData |  |
| 120 | `?_Unmap_buffer@_Buffer@details@Concurrency@@QEAAXXZ` | `0x19FA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `?_Copy_to_async@_Buffer@details@Concurrency@@QEAA?AV_Event@23@PEAV123@_K11@Z` | `0x19FB0` | 171 | UnwindData |  |
| 46 | `?_Copy_to_async@_Buffer@details@Concurrency@@QEAA?AV_Event@23@PEAV123@V?$_Reference_counted_obj_ptr@V_View_shape@details@Concurrency@@@23@1@Z` | `0x1A05C` | 464 | UnwindData |  |
| 68 | `?_Get_accelerator_view@_Buffer@details@Concurrency@@QEBA?AVaccelerator_view@3@XZ` | `0x1A22C` | 88 | UnwindData |  |
| 76 | `?_Get_master_accelerator_view@_Ubiquitous_buffer@details@Concurrency@@QEBA?AVaccelerator_view@3@XZ` | `0x1A22C` | 88 | UnwindData |  |
| 71 | `?_Get_access_on_accelerator_view@_Buffer@details@Concurrency@@QEBA?AVaccelerator_view@3@XZ` | `0x1A284` | 88 | UnwindData |  |
| 103 | `?_Register_view@_Buffer@details@Concurrency@@QEAAXPEAU_Buffer_descriptor@23@@Z` | `0x1A2DC` | 232 | UnwindData |  |
| 121 | `?_Unregister_view@_Buffer@details@Concurrency@@QEAAXPEAU_Buffer_descriptor@23@@Z` | `0x1A3C4` | 70 | UnwindData |  |
| 61 | `?_Exclusively_owns_data@_Buffer@details@Concurrency@@QEAA_NXZ` | `0x1A40C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `?_Is_mappable@_Buffer@details@Concurrency@@QEBA_NXZ` | `0x1A41C` | 476 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `?_Create_texture@_Texture@details@Concurrency@@SAPEAV123@Vaccelerator_view@3@I_K11IW4_Short_vector_base_type_id@23@II_N@Z` | `0x1A5F8` | 461 | UnwindData |  |
| 41 | `?_Adopt_texture@_Texture@details@Concurrency@@SAPEAV123@IW4_Short_vector_base_type_id@23@PEAUIUnknown@@Vaccelerator_view@3@I@Z` | `0x1A7C8` | 886 | UnwindData |  |
| 54 | `?_Create_stage_texture@_Texture@details@Concurrency@@SAPEAV123@Vaccelerator_view@3@0I_K11II_N@Z` | `0x1AB40` | 302 | UnwindData |  |
| 84 | `?_Get_temp_staging_texture@_Texture@details@Concurrency@@SAPEAV123@Vaccelerator_view@3@I_K11II@Z` | `0x1AC70` | 350 | UnwindData |  |
| 55 | `?_Create_stage_texture@_Texture@details@Concurrency@@SAPEAV123@Vaccelerator_view@3@0I_K11IW4_Short_vector_base_type_id@23@II@Z` | `0x1ADD0` | 485 | UnwindData |  |
| 48 | `?_Copy_to_async@_Texture@details@Concurrency@@QEAA?AV_Event@23@PEAV123@PEB_K11II@Z` | `0x1AFB8` | 148 | UnwindData |  |
| 42 | `?_Clone_texture@_Texture@details@Concurrency@@SAPEAV123@PEBV123@AEBVaccelerator_view@3@1@Z` | `0x1B04C` | 114 | UnwindData |  |
| 58 | `?_Create_ubiquitous_buffer@_Ubiquitous_buffer@details@Concurrency@@SAPEAV123@_K0@Z` | `0x1B280` | 327 | UnwindData |  |
| 57 | `?_Create_ubiquitous_buffer@_Ubiquitous_buffer@details@Concurrency@@SAPEAV123@V?$_Reference_counted_obj_ptr@V_Buffer@details@Concurrency@@@23@@Z` | `0x1B3C8` | 99 | UnwindData |  |
| 104 | `?_Register_view@_Ubiquitous_buffer@details@Concurrency@@QEAAXPEAU_Buffer_descriptor@23@Vaccelerator_view@3@V?$_Reference_counted_obj_ptr@V_View_shape@details@Concurrency@@@23@@Z` | `0x1B42C` | 776 | UnwindData |  |
| 105 | `?_Register_view_copy@_Ubiquitous_buffer@details@Concurrency@@QEAAXPEAU_Buffer_descriptor@23@0@Z` | `0x1B734` | 303 | UnwindData |  |
| 122 | `?_Unregister_view@_Ubiquitous_buffer@details@Concurrency@@QEAAXPEAU_Buffer_descriptor@23@@Z` | `0x1B864` | 430 | UnwindData |  |
| 69 | `?_Get_access_async@_Ubiquitous_buffer@details@Concurrency@@AEAA?AV_Event@23@PEAU_Buffer_descriptor@23@Vaccelerator_view@3@W4_Access_mode@@AEAV?$_Reference_counted_obj_ptr@V_Buffer@details@Concurrency@@@23@PEA_K@Z` | `0x1BB04` | 142 | UnwindData |  |
| 70 | `?_Get_access_async@_Ubiquitous_buffer@details@Concurrency@@QEAA?AV_Event@23@PEAU_Buffer_descriptor@23@V?$_Reference_counted_obj_ptr@V_Accelerator_view_impl@details@Concurrency@@@23@W4_Access_mode@@AEAV?$_Reference_counted_obj_ptr@V_Buffer@details@Concurrency@@@23@PEA_K@Z` | `0x1BB94` | 4,857 | UnwindData |  |
| 60 | `?_Discard@_Ubiquitous_buffer@details@Concurrency@@QEAAXPEAU_Buffer_descriptor@23@@Z` | `0x1D608` | 203 | UnwindData |  |
| 77 | `?_Get_master_buffer@_Ubiquitous_buffer@details@Concurrency@@QEBA?AV?$_Reference_counted_obj_ptr@V_Buffer@details@Concurrency@@@23@XZ` | `0x1D6D4` | 54 | UnwindData |  |
| 85 | `?_Get_view_shape@_Ubiquitous_buffer@details@Concurrency@@QEAA?AV?$_Reference_counted_obj_ptr@V_View_shape@details@Concurrency@@@23@PEAU_Buffer_descriptor@23@@Z` | `0x1D70C` | 140 | UnwindData |  |
| 63 | `?_Get_CPU_access@_Buffer_descriptor@details@Concurrency@@QEBAXW4_Access_mode@@@Z` | `0x1E788` | 332 | UnwindData |  |
| 49 | `?_Create@_Sampler@details@Concurrency@@SAPEAV123@IIMMMM@Z` | `0x1E8D4` | 162 | UnwindData |  |
| 50 | `?_Create@_Sampler@details@Concurrency@@SAPEAV123@PEAX@Z` | `0x1E978` | 78 | UnwindData |  |
| 102 | `?_Register_async_event@details@Concurrency@@YAXAEBV_Event@12@AEBV?$shared_future@X@std@@@Z` | `0x1EA34` | 443 | UnwindData |  |
| 45 | `?_Copy_impl@details@Concurrency@@YA?AV_Event@12@PEAV_Buffer@12@_K0111@Z` | `0x1EBF0` | 2,742 | UnwindData |  |
| 44 | `?_Copy_impl@details@Concurrency@@YA?AV_Event@12@PEAV_Buffer@12@V?$_Reference_counted_obj_ptr@V_View_shape@details@Concurrency@@@12@01@Z` | `0x1FB64` | 3,358 | UnwindData |  |
| 43 | `?_Copy_async_impl@details@Concurrency@@YA?AV_Event@12@PEAV_Texture@12@PEB_KI01I11@Z` | `0x20C84` | 3,017 | UnwindData |  |
| 108 | `?_Select_copy_src_accelerator_view@details@Concurrency@@YA?AVaccelerator_view@2@PEAU_Buffer_descriptor@12@AEBV32@@Z` | `0x21BD4` | 711 | UnwindData |  |
| 80 | `?_Get_recommended_buffer_host_access_mode@details@Concurrency@@YA?AW4_Access_mode@@AEBVaccelerator_view@2@@Z` | `0x21E9C` | 50 | UnwindData |  |
| 82 | `?_Get_src_dest_accelerator_view@details@Concurrency@@YA?AU?$pair@Vaccelerator_view@Concurrency@@V12@@std@@PEBU_Buffer_descriptor@12@0@Z` | `0x21ED0` | 556 | UnwindData |  |
| 124 | `?amp_uninitialize@Concurrency@@YAXXZ` | `0x2212C` | 38,956 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `__dpc_create_call_handle` | `0x2B958` | 175 | UnwindData |  |
| 161 | `__dpc_release_call_handle` | `0x2BA08` | 199 | UnwindData |  |
| 163 | `__dpc_set_device_resource_info` | `0x2BAD0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 165 | `__dpc_set_kernel_shader_info` | `0x2BB10` | 552 | UnwindData |  |
| 162 | `__dpc_set_const_buffer_info` | `0x2BD38` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 164 | `__dpc_set_kernel_dispatch_info` | `0x2BD44` | 1,377 | UnwindData |  |
| 160 | `__dpc_dispatch_kernel` | `0x2C2A8` | 72 | UnwindData |  |
| 2 | `??0_Event@details@Concurrency@@QEAA@XZ` | `0x30EB4` | 29 | UnwindData |  |
| 90 | `?_Is_finished_nothrow@_Event@details@Concurrency@@QEAA_NXZ` | `0x30ED4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `?_Is_finished@_Event@details@Concurrency@@QEAA_NXZ` | `0x30EE4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `?_Is_empty@_Event@details@Concurrency@@QEBA_NXZ` | `0x30EF4` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `?_Get@_Event@details@Concurrency@@QEAAXXZ` | `0x30F00` | 22 | UnwindData |  |
| 40 | `?_Add_event@_Event@details@Concurrency@@QEAA?AV123@V123@@Z` | `0x30F18` | 449 | UnwindData |  |
| 39 | `?_Add_continuation@_Event@details@Concurrency@@QEAA?AV123@AEBV?$function@$$A6A?AV_Event@details@Concurrency@@XZ@std@@@Z` | `0x310DC` | 239 | UnwindData |  |
| 22 | `??1_Amp_runtime_trace@details@Concurrency@@QEAA@XZ` | `0x324B4` | 118 | UnwindData |  |
| 72 | `?_Get_amp_trace@details@Concurrency@@YAPEAV_Amp_runtime_trace@12@XZ` | `0x3261C` | 70 | UnwindData |  |
| 123 | `?_Write_end_event@_Amp_runtime_trace@details@Concurrency@@QEAAXK@Z` | `0x32840` | 99 | UnwindData |  |
| 112 | `?_Start_async_op_wait_event@_Amp_runtime_trace@details@Concurrency@@AEAAKK@Z` | `0x32A84` | 133 | UnwindData |  |
| 119 | `?_Start_parallel_for_each_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKPEAU_DPC_call_handle@23@@Z` | `0x32B0C` | 890 | UnwindData |  |
| 111 | `?_Start_array_view_synchronize_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Buffer_descriptor@23@@Z` | `0x32E88` | 372 | UnwindData |  |
| 92 | `?_Launch_array_view_synchronize_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Buffer_descriptor@23@@Z` | `0x32FFC` | 372 | UnwindData |  |
| 116 | `?_Start_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Buffer_descriptor@23@0_K@Z` | `0x3328C` | 245 | UnwindData |  |
| 113 | `?_Start_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAK$$TAEBU_Buffer_descriptor@23@_K@Z` | `0x33384` | 210 | UnwindData |  |
| 115 | `?_Start_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Buffer_descriptor@23@$$T_K@Z` | `0x33458` | 209 | UnwindData |  |
| 96 | `?_Launch_async_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Buffer_descriptor@23@0_K@Z` | `0x3352C` | 245 | UnwindData |  |
| 93 | `?_Launch_async_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAK$$TAEBU_Buffer_descriptor@23@_K@Z` | `0x33624` | 210 | UnwindData |  |
| 95 | `?_Launch_async_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Buffer_descriptor@23@$$T_K@Z` | `0x336F8` | 209 | UnwindData |  |
| 117 | `?_Start_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Texture_descriptor@23@$$T_K@Z` | `0x337CC` | 79 | UnwindData |  |
| 114 | `?_Start_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAK$$TAEBU_Texture_descriptor@23@_K@Z` | `0x3381C` | 78 | UnwindData |  |
| 118 | `?_Start_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Texture_descriptor@23@0_K@Z` | `0x3386C` | 96 | UnwindData |  |
| 97 | `?_Launch_async_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Texture_descriptor@23@$$T_K@Z` | `0x338CC` | 79 | UnwindData |  |
| 94 | `?_Launch_async_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAK$$TAEBU_Texture_descriptor@23@_K@Z` | `0x3391C` | 78 | UnwindData |  |
| 98 | `?_Launch_async_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Texture_descriptor@23@0_K@Z` | `0x3396C` | 96 | UnwindData |  |
| 125 | `?cpu_accelerator@accelerator@Concurrency@@2QB_WB` | `0x429F0` | 904 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `?default_accelerator@accelerator@Concurrency@@2QB_WB` | `0x42D78` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `?direct3d_warp@accelerator@Concurrency@@2QB_WB` | `0x42E08` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `?direct3d_ref@accelerator@Concurrency@@2QB_WB` | `0x42F48` | 0 | Indeterminate |  |
