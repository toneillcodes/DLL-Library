# Binary Specification: vcamp140d.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\vcamp140d.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2512ad06046e96e262efd71619d8d4be8ad341be3591f0f508249a35eb0ab001`
* **Total Exported Functions:** 166

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 126 | `?create_accelerator_view@direct3d@Concurrency@@YA?AVaccelerator_view@2@AEAVaccelerator@2@_NW4queuing_mode@2@@Z` | `0xB0A0` | 357 | UnwindData |  |
| 127 | `?create_accelerator_view@direct3d@Concurrency@@YA?AVaccelerator_view@2@PEAUIUnknown@@W4queuing_mode@2@@Z` | `0xB210` | 929 | UnwindData |  |
| 156 | `?is_timeout_disabled@direct3d@Concurrency@@YA_NAEBVaccelerator_view@2@@Z` | `0xB830` | 220 | UnwindData |  |
| 17 | `??0scoped_d3d_access_lock@direct3d@Concurrency@@QEAA@$$QEAV012@@Z` | `0x14D60` | 66 | UnwindData |  |
| 18 | `??0scoped_d3d_access_lock@direct3d@Concurrency@@QEAA@AEAVaccelerator_view@2@@Z` | `0x14DB0` | 170 | UnwindData |  |
| 19 | `??0scoped_d3d_access_lock@direct3d@Concurrency@@QEAA@AEAVaccelerator_view@2@Uadopt_d3d_access_lock_t@12@@Z` | `0x14E60` | 153 | UnwindData |  |
| 27 | `??1scoped_d3d_access_lock@direct3d@Concurrency@@QEAA@XZ` | `0x16470` | 68 | UnwindData |  |
| 32 | `??4scoped_d3d_access_lock@direct3d@Concurrency@@QEAAAEAV012@$$QEAV012@@Z` | `0x16680` | 138 | UnwindData |  |
| 64 | `?_Get_D3D_buffer@_D3D_interop@details@Concurrency@@SAPEAUIUnknown@@PEAV_Buffer@23@@Z` | `0x20C60` | 431 | UnwindData |  |
| 65 | `?_Get_D3D_sampler@_D3D_interop@details@Concurrency@@SAPEAUIUnknown@@AEBVaccelerator_view@3@PEAV_Sampler@23@@Z` | `0x20E30` | 856 | UnwindData |  |
| 66 | `?_Get_D3D_sampler_data_ptr@_D3D_interop@details@Concurrency@@SAPEAXPEAUIUnknown@@@Z` | `0x21190` | 266 | UnwindData |  |
| 67 | `?_Get_D3D_texture@_D3D_interop@details@Concurrency@@SAPEAUIUnknown@@PEAV_Texture@23@@Z` | `0x212A0` | 375 | UnwindData |  |
| 155 | `?get_view_removed_reason@accelerator_view_removed@Concurrency@@QEBAJXZ` | `0x21550` | 2,800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `?_Get_preferred_copy_chunk_size@details@Concurrency@@YA_K_K@Z` | `0x22040` | 24 | UnwindData |  |
| 107 | `?_Release_D3D_sampler_data_ptr@_D3D_interop@details@Concurrency@@SAXPEAX@Z` | `0x26D50` | 25 | UnwindData |  |
| 130 | `?d3d_access_lock@direct3d@Concurrency@@YAXAEAVaccelerator_view@2@@Z` | `0x29B40` | 130 | UnwindData |  |
| 131 | `?d3d_access_try_lock@direct3d@Concurrency@@YA_NAEAVaccelerator_view@2@@Z` | `0x29BD0` | 129 | UnwindData |  |
| 132 | `?d3d_access_unlock@direct3d@Concurrency@@YAXAEAVaccelerator_view@2@@Z` | `0x29C60` | 130 | UnwindData |  |
| 142 | `?get_device@direct3d@Concurrency@@YAPEAUIUnknown@@AEBVaccelerator_view@2@@Z` | `0x2A650` | 336 | UnwindData |  |
| 75 | `?_Get_devices@details@Concurrency@@YAPEAV?$_Reference_counted_obj_ptr@V_Accelerator_impl@details@Concurrency@@@12@XZ` | `0x31E40` | 22 | UnwindData |  |
| 78 | `?_Get_num_devices@details@Concurrency@@YA_KXZ` | `0x31E90` | 22 | UnwindData |  |
| 87 | `?_Is_D3D_accelerator_view@details@Concurrency@@YA_NAEBVaccelerator_view@2@@Z` | `0x32250` | 70 | UnwindData |  |
| 109 | `?_Select_default_accelerator@details@Concurrency@@YA?AVaccelerator@2@XZ` | `0x325A0` | 105 | UnwindData |  |
| 110 | `?_Set_default_accelerator@details@Concurrency@@YA_NV?$_Reference_counted_obj_ptr@V_Accelerator_impl@details@Concurrency@@@12@@Z` | `0x32670` | 73 | UnwindData |  |
| 3 | `??0accelerator@Concurrency@@AEAA@V?$_Reference_counted_obj_ptr@V_Accelerator_impl@details@Concurrency@@@details@1@@Z` | `0x44230` | 60 | UnwindData |  |
| 1 | `??0_Event@details@Concurrency@@QEAA@AEBV012@@Z` | `0x44270` | 53 | UnwindData |  |
| 4 | `??0accelerator@Concurrency@@QEAA@AEBV01@@Z` | `0x44270` | 53 | UnwindData |  |
| 5 | `??0accelerator@Concurrency@@QEAA@XZ` | `0x442B0` | 196 | UnwindData |  |
| 6 | `??0accelerator_view@Concurrency@@AEAA@V?$_Reference_counted_obj_ptr@V_Accelerator_view_impl@details@Concurrency@@@details@1@_N@Z` | `0x44380` | 78 | UnwindData |  |
| 7 | `??0accelerator_view@Concurrency@@QEAA@AEBV01@@Z` | `0x443D0` | 70 | UnwindData |  |
| 8 | `??0accelerator_view_removed@Concurrency@@QEAA@J@Z` | `0x44420` | 66 | UnwindData |  |
| 9 | `??0accelerator_view_removed@Concurrency@@QEAA@PEBDJ@Z` | `0x44470` | 78 | UnwindData |  |
| 10 | `??0invalid_compute_domain@Concurrency@@QEAA@PEBD@Z` | `0x447B0` | 61 | UnwindData |  |
| 11 | `??0invalid_compute_domain@Concurrency@@QEAA@XZ` | `0x447F0` | 58 | UnwindData |  |
| 12 | `??0out_of_memory@Concurrency@@QEAA@PEBD@Z` | `0x44950` | 61 | UnwindData |  |
| 13 | `??0out_of_memory@Concurrency@@QEAA@XZ` | `0x44990` | 58 | UnwindData |  |
| 14 | `??0runtime_exception@Concurrency@@QEAA@AEBV01@@Z` | `0x44A90` | 102 | UnwindData |  |
| 15 | `??0runtime_exception@Concurrency@@QEAA@J@Z` | `0x44B00` | 68 | UnwindData |  |
| 16 | `??0runtime_exception@Concurrency@@QEAA@PEBDJ@Z` | `0x44B50` | 72 | UnwindData |  |
| 20 | `??0unsupported_feature@Concurrency@@QEAA@PEBD@Z` | `0x44E60` | 61 | UnwindData |  |
| 21 | `??0unsupported_feature@Concurrency@@QEAA@XZ` | `0x44EA0` | 58 | UnwindData |  |
| 23 | `??1_Event@details@Concurrency@@QEAA@XZ` | `0x44FD0` | 28 | UnwindData |  |
| 24 | `??1accelerator@Concurrency@@QEAA@XZ` | `0x44FD0` | 28 | UnwindData |  |
| 25 | `??1accelerator_view@Concurrency@@QEAA@XZ` | `0x44FD0` | 28 | UnwindData |  |
| 26 | `??1runtime_exception@Concurrency@@UEAA@XZ` | `0x47290` | 40 | UnwindData |  |
| 28 | `??4_Event@details@Concurrency@@QEAAAEAV012@AEBV012@@Z` | `0x476C0` | 55 | UnwindData |  |
| 29 | `??4accelerator@Concurrency@@QEAAAEAV01@AEBV01@@Z` | `0x476C0` | 55 | UnwindData |  |
| 30 | `??4accelerator_view@Concurrency@@QEAAAEAV01@AEBV01@@Z` | `0x47700` | 71 | UnwindData |  |
| 31 | `??4runtime_exception@Concurrency@@QEAAAEAV01@AEBV01@@Z` | `0x477E0` | 67 | UnwindData |  |
| 33 | `??8_Event@details@Concurrency@@QEBA_NAEBV012@@Z` | `0x47870` | 80 | UnwindData |  |
| 34 | `??8accelerator@Concurrency@@QEBA_NAEBV01@@Z` | `0x47870` | 80 | UnwindData |  |
| 35 | `??8accelerator_view@Concurrency@@QEBA_NAEBV01@@Z` | `0x47870` | 80 | UnwindData |  |
| 36 | `??9_Event@details@Concurrency@@QEBA_NAEBV012@@Z` | `0x479E0` | 64 | UnwindData |  |
| 37 | `??9accelerator@Concurrency@@QEBA_NAEBV01@@Z` | `0x479E0` | 64 | UnwindData |  |
| 38 | `??9accelerator_view@Concurrency@@QEBA_NAEBV01@@Z` | `0x479E0` | 64 | UnwindData |  |
| 41 | `?_Adopt_texture@_Texture@details@Concurrency@@SAPEAV123@IW4_Short_vector_base_type_id@23@PEAUIUnknown@@Vaccelerator_view@3@I@Z` | `0x4C4D0` | 1,230 | UnwindData |  |
| 42 | `?_Clone_texture@_Texture@details@Concurrency@@SAPEAV123@PEBV123@AEBVaccelerator_view@3@1@Z` | `0x4DC10` | 235 | UnwindData |  |
| 43 | `?_Copy_async_impl@details@Concurrency@@YA?AV_Event@12@PEAV_Texture@12@PEB_KI01I11@Z` | `0x4EA50` | 7,315 | UnwindData |  |
| 44 | `?_Copy_impl@details@Concurrency@@YA?AV_Event@12@PEAV_Buffer@12@V?$_Reference_counted_obj_ptr@V_View_shape@details@Concurrency@@@12@01@Z` | `0x506F0` | 4,872 | UnwindData |  |
| 45 | `?_Copy_impl@details@Concurrency@@YA?AV_Event@12@PEAV_Buffer@12@_K0111@Z` | `0x51A00` | 3,493 | UnwindData |  |
| 46 | `?_Copy_to_async@_Buffer@details@Concurrency@@QEAA?AV_Event@23@PEAV123@V?$_Reference_counted_obj_ptr@V_View_shape@details@Concurrency@@@23@1@Z` | `0x527B0` | 766 | UnwindData |  |
| 47 | `?_Copy_to_async@_Buffer@details@Concurrency@@QEAA?AV_Event@23@PEAV123@_K11@Z` | `0x52AB0` | 477 | UnwindData |  |
| 48 | `?_Copy_to_async@_Texture@details@Concurrency@@QEAA?AV_Event@23@PEAV123@PEB_K11II@Z` | `0x52C90` | 399 | UnwindData |  |
| 49 | `?_Create@_Sampler@details@Concurrency@@SAPEAV123@IIMMMM@Z` | `0x52EA0` | 156 | UnwindData |  |
| 50 | `?_Create@_Sampler@details@Concurrency@@SAPEAV123@PEAX@Z` | `0x52F40` | 150 | UnwindData |  |
| 51 | `?_Create_buffer@_Buffer@details@Concurrency@@SAPEAV123@PEAXVaccelerator_view@3@_K2@Z` | `0x535E0` | 312 | UnwindData |  |
| 52 | `?_Create_buffer@_Buffer@details@Concurrency@@SAPEAV123@Vaccelerator_view@3@0_K1_NW4access_type@3@@Z` | `0x53720` | 360 | UnwindData |  |
| 53 | `?_Create_stage_buffer@_Buffer@details@Concurrency@@SAPEAV123@Vaccelerator_view@3@0_K1_N@Z` | `0x53890` | 492 | UnwindData |  |
| 54 | `?_Create_stage_texture@_Texture@details@Concurrency@@SAPEAV123@Vaccelerator_view@3@0I_K11II_N@Z` | `0x53A80` | 615 | UnwindData |  |
| 55 | `?_Create_stage_texture@_Texture@details@Concurrency@@SAPEAV123@Vaccelerator_view@3@0I_K11IW4_Short_vector_base_type_id@23@II@Z` | `0x53CF0` | 907 | UnwindData |  |
| 56 | `?_Create_texture@_Texture@details@Concurrency@@SAPEAV123@Vaccelerator_view@3@I_K11IW4_Short_vector_base_type_id@23@II_N@Z` | `0x54080` | 720 | UnwindData |  |
| 57 | `?_Create_ubiquitous_buffer@_Ubiquitous_buffer@details@Concurrency@@SAPEAV123@V?$_Reference_counted_obj_ptr@V_Buffer@details@Concurrency@@@23@@Z` | `0x54350` | 192 | UnwindData |  |
| 58 | `?_Create_ubiquitous_buffer@_Ubiquitous_buffer@details@Concurrency@@SAPEAV123@_K0@Z` | `0x54410` | 203 | UnwindData |  |
| 59 | `?_Create_view_shape@_View_shape@details@Concurrency@@SAPEAV123@IIPEBI00PEB_N@Z` | `0x544E0` | 246 | UnwindData |  |
| 60 | `?_Discard@_Ubiquitous_buffer@details@Concurrency@@QEAAXPEAU_Buffer_descriptor@23@@Z` | `0x55A60` | 769 | UnwindData |  |
| 61 | `?_Exclusively_owns_data@_Buffer@details@Concurrency@@QEAA_NXZ` | `0x568B0` | 84 | UnwindData |  |
| 145 | `?get_is_auto_selection@accelerator_view@Concurrency@@QEBA_NXZ` | `0x570D0` | 3,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `?_Get_CPU_access@_Buffer_descriptor@details@Concurrency@@QEBAXW4_Access_mode@@@Z` | `0x57E50` | 472 | UnwindData |  |
| 68 | `?_Get_accelerator_view@_Buffer@details@Concurrency@@QEBA?AVaccelerator_view@3@XZ` | `0x58030` | 109 | UnwindData |  |
| 76 | `?_Get_master_accelerator_view@_Ubiquitous_buffer@details@Concurrency@@QEBA?AVaccelerator_view@3@XZ` | `0x58030` | 109 | UnwindData |  |
| 69 | `?_Get_access_async@_Ubiquitous_buffer@details@Concurrency@@AEAA?AV_Event@23@PEAU_Buffer_descriptor@23@Vaccelerator_view@3@W4_Access_mode@@AEAV?$_Reference_counted_obj_ptr@V_Buffer@details@Concurrency@@@23@PEA_K@Z` | `0x580A0` | 188 | UnwindData |  |
| 70 | `?_Get_access_async@_Ubiquitous_buffer@details@Concurrency@@QEAA?AV_Event@23@PEAU_Buffer_descriptor@23@V?$_Reference_counted_obj_ptr@V_Accelerator_view_impl@details@Concurrency@@@23@W4_Access_mode@@AEAV?$_Reference_counted_obj_ptr@V_Buffer@details@Concurrency@@@23@PEA_K@Z` | `0x58160` | 6,675 | UnwindData |  |
| 71 | `?_Get_access_on_accelerator_view@_Buffer@details@Concurrency@@QEBA?AVaccelerator_view@3@XZ` | `0x59B80` | 109 | UnwindData |  |
| 73 | `?_Get_description@accelerator@Concurrency@@AEBAPEB_WXZ` | `0x5AE10` | 65 | UnwindData |  |
| 74 | `?_Get_device_path@accelerator@Concurrency@@AEBAPEB_WXZ` | `0x5AE60` | 65 | UnwindData |  |
| 77 | `?_Get_master_buffer@_Ubiquitous_buffer@details@Concurrency@@QEBA?AV?$_Reference_counted_obj_ptr@V_Buffer@details@Concurrency@@@23@XZ` | `0x5AEB0` | 64 | UnwindData |  |
| 143 | `?get_error_code@runtime_exception@Concurrency@@QEBAJXZ` | `0x5B0F0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `?_Get_recommended_buffer_host_access_mode@details@Concurrency@@YA?AW4_Access_mode@@AEBVaccelerator_view@2@@Z` | `0x5B1B0` | 117 | UnwindData |  |
| 81 | `?_Get_reduced_shape_for_copy@_View_shape@details@Concurrency@@QEAAPEAV123@XZ` | `0x5B230` | 762 | UnwindData |  |
| 82 | `?_Get_src_dest_accelerator_view@details@Concurrency@@YA?AU?$pair@Vaccelerator_view@Concurrency@@V12@@std@@PEBU_Buffer_descriptor@12@0@Z` | `0x5B530` | 928 | UnwindData |  |
| 83 | `?_Get_temp_staging_buffer@_Buffer@details@Concurrency@@SAPEAV123@Vaccelerator_view@3@_K1@Z` | `0x5B930` | 231 | UnwindData |  |
| 84 | `?_Get_temp_staging_texture@_Texture@details@Concurrency@@SAPEAV123@Vaccelerator_view@3@I_K11II@Z` | `0x5BA20` | 694 | UnwindData |  |
| 85 | `?_Get_view_shape@_Ubiquitous_buffer@details@Concurrency@@QEAA?AV?$_Reference_counted_obj_ptr@V_View_shape@details@Concurrency@@@23@PEAU_Buffer_descriptor@23@@Z` | `0x5BFA0` | 426 | UnwindData |  |
| 86 | `?_Init@accelerator@Concurrency@@AEAAXPEB_W@Z` | `0x5C7C0` | 236 | UnwindData |  |
| 91 | `?_Is_mappable@_Buffer@details@Concurrency@@QEBA_NXZ` | `0x5CCC0` | 101 | UnwindData |  |
| 99 | `?_Map_buffer@_Buffer@details@Concurrency@@QEAAXW4_Access_mode@@_N@Z` | `0x5CFC0` | 260 | UnwindData |  |
| 100 | `?_Map_buffer_async@_Buffer@details@Concurrency@@QEAA?AV_Event@23@W4_Access_mode@@@Z` | `0x5D0D0` | 285 | UnwindData |  |
| 101 | `?_Recursive_array_copy@details@Concurrency@@YAJAEBU_Array_copy_desc@12@IV?$function@$$A6AJAEBU_Array_copy_desc@details@Concurrency@@@Z@std@@@Z` | `0x5DAA0` | 2,429 | UnwindData |  |
| 102 | `?_Register_async_event@details@Concurrency@@YAXAEBV_Event@12@AEBV?$shared_future@X@std@@@Z` | `0x5E800` | 50 | UnwindData |  |
| 103 | `?_Register_view@_Buffer@details@Concurrency@@QEAAXPEAU_Buffer_descriptor@23@@Z` | `0x5E840` | 465 | UnwindData |  |
| 104 | `?_Register_view@_Ubiquitous_buffer@details@Concurrency@@QEAAXPEAU_Buffer_descriptor@23@Vaccelerator_view@3@V?$_Reference_counted_obj_ptr@V_View_shape@details@Concurrency@@@23@QEAU423@@Z` | `0x5EA20` | 770 | UnwindData |  |
| 105 | `?_Register_view_copy@_Ubiquitous_buffer@details@Concurrency@@QEAAXPEAU_Buffer_descriptor@23@0@Z` | `0x5ED30` | 804 | UnwindData |  |
| 106 | `?_Release@_Reference_counter@details@Concurrency@@QEAAXXZ` | `0x5F280` | 132 | UnwindData |  |
| 108 | `?_Select_copy_src_accelerator_view@details@Concurrency@@YA?AVaccelerator_view@2@PEAU_Buffer_descriptor@12@AEBV32@@Z` | `0x60350` | 1,793 | UnwindData |  |
| 120 | `?_Unmap_buffer@_Buffer@details@Concurrency@@QEAAXXZ` | `0x62CE0` | 161 | UnwindData |  |
| 121 | `?_Unregister_view@_Buffer@details@Concurrency@@QEAAXPEAU_Buffer_descriptor@23@@Z` | `0x62DC0` | 340 | UnwindData |  |
| 122 | `?_Unregister_view@_Ubiquitous_buffer@details@Concurrency@@QEAAXPEAU_Buffer_descriptor@23@@Z` | `0x62F20` | 710 | UnwindData |  |
| 124 | `?amp_uninitialize@Concurrency@@YAXXZ` | `0x63F00` | 15 | UnwindData |  |
| 128 | `?create_marker@accelerator_view@Concurrency@@QEAA?AVcompletion_future@2@XZ` | `0x64650` | 318 | UnwindData |  |
| 129 | `?create_view@accelerator@Concurrency@@QEAA?AVaccelerator_view@2@W4queuing_mode@2@@Z` | `0x64790` | 309 | UnwindData |  |
| 136 | `?flush@accelerator_view@Concurrency@@QEAAXXZ` | `0x64ED0` | 143 | UnwindData |  |
| 137 | `?get_accelerator@accelerator_view@Concurrency@@QEBA?AVaccelerator@2@XZ` | `0x65020` | 118 | UnwindData |  |
| 138 | `?get_auto_selection_view@accelerator@Concurrency@@SA?AVaccelerator_view@2@XZ` | `0x650B0` | 238 | UnwindData |  |
| 139 | `?get_dedicated_memory@accelerator@Concurrency@@QEBA_KXZ` | `0x65240` | 65 | UnwindData |  |
| 140 | `?get_default_cpu_access_type@accelerator@Concurrency@@QEBA?AW4access_type@2@XZ` | `0x65290` | 51 | UnwindData |  |
| 141 | `?get_default_view@accelerator@Concurrency@@QEBA?AVaccelerator_view@2@XZ` | `0x652D0` | 121 | UnwindData |  |
| 144 | `?get_has_display@accelerator@Concurrency@@QEBA_NXZ` | `0x653A0` | 65 | UnwindData |  |
| 146 | `?get_is_debug@accelerator@Concurrency@@QEBA_NXZ` | `0x653F0` | 101 | UnwindData |  |
| 147 | `?get_is_debug@accelerator_view@Concurrency@@QEBA_NXZ` | `0x65460` | 35 | UnwindData |  |
| 148 | `?get_is_emulated@accelerator@Concurrency@@QEBA_NXZ` | `0x65490` | 35 | UnwindData |  |
| 149 | `?get_queuing_mode@accelerator_view@Concurrency@@QEBA?AW4queuing_mode@2@XZ` | `0x654C0` | 35 | UnwindData |  |
| 150 | `?get_supports_cpu_shared_memory@accelerator@Concurrency@@QEBA_NXZ` | `0x65530` | 35 | UnwindData |  |
| 151 | `?get_supports_double_precision@accelerator@Concurrency@@QEBA_NXZ` | `0x65560` | 35 | UnwindData |  |
| 152 | `?get_supports_limited_double_precision@accelerator@Concurrency@@QEBA_NXZ` | `0x65590` | 35 | UnwindData |  |
| 153 | `?get_version@accelerator@Concurrency@@QEBAIXZ` | `0x655C0` | 100 | UnwindData |  |
| 154 | `?get_version@accelerator_view@Concurrency@@QEBAIXZ` | `0x65630` | 35 | UnwindData |  |
| 157 | `?set_default_cpu_access_type@accelerator@Concurrency@@QEAA_NW4access_type@2@@Z` | `0x66320` | 177 | UnwindData |  |
| 158 | `?wait@accelerator_view@Concurrency@@QEAAXXZ` | `0x66760` | 171 | UnwindData |  |
| 159 | `__dpc_create_call_handle` | `0x6A740` | 86 | UnwindData |  |
| 160 | `__dpc_dispatch_kernel` | `0x6A7A0` | 205 | UnwindData |  |
| 161 | `__dpc_dispatch_kernel_test` | `0x6A870` | 102 | UnwindData |  |
| 162 | `__dpc_release_call_handle` | `0x6A8E0` | 63 | UnwindData |  |
| 163 | `__dpc_set_const_buffer_info` | `0x6A920` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 164 | `__dpc_set_device_resource_info` | `0x6A950` | 259 | UnwindData |  |
| 165 | `__dpc_set_kernel_dispatch_info` | `0x6AA60` | 4,115 | UnwindData |  |
| 166 | `__dpc_set_kernel_shader_info` | `0x6BA80` | 323 | UnwindData |  |
| 2 | `??0_Event@details@Concurrency@@QEAA@XZ` | `0x7F7D0` | 42 | UnwindData |  |
| 39 | `?_Add_continuation@_Event@details@Concurrency@@QEAA?AV123@AEBV?$function@$$A6A?AV_Event@details@Concurrency@@XZ@std@@@Z` | `0x80220` | 266 | UnwindData |  |
| 40 | `?_Add_event@_Event@details@Concurrency@@QEAA?AV123@V123@@Z` | `0x80330` | 914 | UnwindData |  |
| 62 | `?_Get@_Event@details@Concurrency@@QEAAXXZ` | `0x80C30` | 56 | UnwindData |  |
| 88 | `?_Is_empty@_Event@details@Concurrency@@QEBA_NXZ` | `0x813D0` | 55 | UnwindData |  |
| 89 | `?_Is_finished@_Event@details@Concurrency@@QEAA_NXZ` | `0x81410` | 57 | UnwindData |  |
| 90 | `?_Is_finished_nothrow@_Event@details@Concurrency@@QEAA_NXZ` | `0x819C0` | 57 | UnwindData |  |
| 22 | `??1_Amp_runtime_trace@details@Concurrency@@QEAA@XZ` | `0x84040` | 113 | UnwindData |  |
| 72 | `?_Get_amp_trace@details@Concurrency@@YAPEAV_Amp_runtime_trace@12@XZ` | `0x84730` | 126 | UnwindData |  |
| 92 | `?_Launch_array_view_synchronize_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Buffer_descriptor@23@@Z` | `0x84EB0` | 462 | UnwindData |  |
| 93 | `?_Launch_async_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAK$$TAEBU_Buffer_descriptor@23@_K@Z` | `0x85570` | 505 | UnwindData |  |
| 94 | `?_Launch_async_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAK$$TAEBU_Texture_descriptor@23@_K@Z` | `0x85770` | 356 | UnwindData |  |
| 95 | `?_Launch_async_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Buffer_descriptor@23@$$T_K@Z` | `0x858E0` | 506 | UnwindData |  |
| 96 | `?_Launch_async_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Buffer_descriptor@23@0_K@Z` | `0x85AE0` | 546 | UnwindData |  |
| 97 | `?_Launch_async_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Texture_descriptor@23@$$T_K@Z` | `0x85D10` | 357 | UnwindData |  |
| 98 | `?_Launch_async_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Texture_descriptor@23@0_K@Z` | `0x85E80` | 315 | UnwindData |  |
| 111 | `?_Start_array_view_synchronize_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Buffer_descriptor@23@@Z` | `0x869E0` | 462 | UnwindData |  |
| 112 | `?_Start_async_op_wait_event@_Amp_runtime_trace@details@Concurrency@@AEAAKK@Z` | `0x86BB0` | 474 | UnwindData |  |
| 113 | `?_Start_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAK$$TAEBU_Buffer_descriptor@23@_K@Z` | `0x87280` | 505 | UnwindData |  |
| 114 | `?_Start_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAK$$TAEBU_Texture_descriptor@23@_K@Z` | `0x87480` | 356 | UnwindData |  |
| 115 | `?_Start_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Buffer_descriptor@23@$$T_K@Z` | `0x875F0` | 506 | UnwindData |  |
| 116 | `?_Start_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Buffer_descriptor@23@0_K@Z` | `0x877F0` | 546 | UnwindData |  |
| 117 | `?_Start_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Texture_descriptor@23@$$T_K@Z` | `0x87A20` | 357 | UnwindData |  |
| 118 | `?_Start_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Texture_descriptor@23@0_K@Z` | `0x87B90` | 315 | UnwindData |  |
| 119 | `?_Start_parallel_for_each_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKPEAU_DPC_call_handle@23@@Z` | `0x88370` | 1,396 | UnwindData |  |
| 123 | `?_Write_end_event@_Amp_runtime_trace@details@Concurrency@@QEAAXK@Z` | `0x88F40` | 347 | UnwindData |  |
| 133 | `?default_accelerator@accelerator@Concurrency@@2QB_WB` | `0xA3AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `?cpu_accelerator@accelerator@Concurrency@@2QB_WB` | `0xA3AB0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `?direct3d_warp@accelerator@Concurrency@@2QB_WB` | `0xA3AB8` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `?direct3d_ref@accelerator@Concurrency@@2QB_WB` | `0xA3AD8` | 0 | Indeterminate |  |
