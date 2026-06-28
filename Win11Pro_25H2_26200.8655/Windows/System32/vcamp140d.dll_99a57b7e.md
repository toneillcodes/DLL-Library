# Binary Specification: vcamp140d.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\vcamp140d.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `99a57b7e7f9e8803c441b9e2fc0a21848ad68cc8509086cc288c66e4db2ba63d`
* **Total Exported Functions:** 166

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 126 | `?create_accelerator_view@direct3d@Concurrency@@YA?AVaccelerator_view@2@AEAVaccelerator@2@_NW4queuing_mode@2@@Z` | `0xB250` | 357 | UnwindData |  |
| 127 | `?create_accelerator_view@direct3d@Concurrency@@YA?AVaccelerator_view@2@PEAUIUnknown@@W4queuing_mode@2@@Z` | `0xB3C0` | 929 | UnwindData |  |
| 156 | `?is_timeout_disabled@direct3d@Concurrency@@YA_NAEBVaccelerator_view@2@@Z` | `0xB9C0` | 220 | UnwindData |  |
| 17 | `??0scoped_d3d_access_lock@direct3d@Concurrency@@QEAA@$$QEAV012@@Z` | `0x152A0` | 66 | UnwindData |  |
| 18 | `??0scoped_d3d_access_lock@direct3d@Concurrency@@QEAA@AEAVaccelerator_view@2@@Z` | `0x152F0` | 170 | UnwindData |  |
| 19 | `??0scoped_d3d_access_lock@direct3d@Concurrency@@QEAA@AEAVaccelerator_view@2@Uadopt_d3d_access_lock_t@12@@Z` | `0x153A0` | 153 | UnwindData |  |
| 27 | `??1scoped_d3d_access_lock@direct3d@Concurrency@@QEAA@XZ` | `0x16980` | 68 | UnwindData |  |
| 32 | `??4scoped_d3d_access_lock@direct3d@Concurrency@@QEAAAEAV012@$$QEAV012@@Z` | `0x16B90` | 138 | UnwindData |  |
| 64 | `?_Get_D3D_buffer@_D3D_interop@details@Concurrency@@SAPEAUIUnknown@@PEAV_Buffer@23@@Z` | `0x21090` | 431 | UnwindData |  |
| 65 | `?_Get_D3D_sampler@_D3D_interop@details@Concurrency@@SAPEAUIUnknown@@AEBVaccelerator_view@3@PEAV_Sampler@23@@Z` | `0x21260` | 856 | UnwindData |  |
| 66 | `?_Get_D3D_sampler_data_ptr@_D3D_interop@details@Concurrency@@SAPEAXPEAUIUnknown@@@Z` | `0x215C0` | 266 | UnwindData |  |
| 67 | `?_Get_D3D_texture@_D3D_interop@details@Concurrency@@SAPEAUIUnknown@@PEAV_Texture@23@@Z` | `0x216D0` | 375 | UnwindData |  |
| 155 | `?get_view_removed_reason@accelerator_view_removed@Concurrency@@QEBAJXZ` | `0x21980` | 2,800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `?_Get_preferred_copy_chunk_size@details@Concurrency@@YA_K_K@Z` | `0x22470` | 24 | UnwindData |  |
| 107 | `?_Release_D3D_sampler_data_ptr@_D3D_interop@details@Concurrency@@SAXPEAX@Z` | `0x27150` | 25 | UnwindData |  |
| 130 | `?d3d_access_lock@direct3d@Concurrency@@YAXAEAVaccelerator_view@2@@Z` | `0x29E90` | 130 | UnwindData |  |
| 131 | `?d3d_access_try_lock@direct3d@Concurrency@@YA_NAEAVaccelerator_view@2@@Z` | `0x29F20` | 129 | UnwindData |  |
| 132 | `?d3d_access_unlock@direct3d@Concurrency@@YAXAEAVaccelerator_view@2@@Z` | `0x29FB0` | 130 | UnwindData |  |
| 142 | `?get_device@direct3d@Concurrency@@YAPEAUIUnknown@@AEBVaccelerator_view@2@@Z` | `0x2A900` | 336 | UnwindData |  |
| 75 | `?_Get_devices@details@Concurrency@@YAPEAV?$_Reference_counted_obj_ptr@V_Accelerator_impl@details@Concurrency@@@12@XZ` | `0x31DC0` | 22 | UnwindData |  |
| 78 | `?_Get_num_devices@details@Concurrency@@YA_KXZ` | `0x31E10` | 22 | UnwindData |  |
| 87 | `?_Is_D3D_accelerator_view@details@Concurrency@@YA_NAEBVaccelerator_view@2@@Z` | `0x321D0` | 70 | UnwindData |  |
| 109 | `?_Select_default_accelerator@details@Concurrency@@YA?AVaccelerator@2@XZ` | `0x32520` | 105 | UnwindData |  |
| 110 | `?_Set_default_accelerator@details@Concurrency@@YA_NV?$_Reference_counted_obj_ptr@V_Accelerator_impl@details@Concurrency@@@12@@Z` | `0x325F0` | 73 | UnwindData |  |
| 3 | `??0accelerator@Concurrency@@AEAA@V?$_Reference_counted_obj_ptr@V_Accelerator_impl@details@Concurrency@@@details@1@@Z` | `0x44410` | 60 | UnwindData |  |
| 1 | `??0_Event@details@Concurrency@@QEAA@AEBV012@@Z` | `0x44450` | 53 | UnwindData |  |
| 4 | `??0accelerator@Concurrency@@QEAA@AEBV01@@Z` | `0x44450` | 53 | UnwindData |  |
| 5 | `??0accelerator@Concurrency@@QEAA@XZ` | `0x44490` | 196 | UnwindData |  |
| 6 | `??0accelerator_view@Concurrency@@AEAA@V?$_Reference_counted_obj_ptr@V_Accelerator_view_impl@details@Concurrency@@@details@1@_N@Z` | `0x44560` | 78 | UnwindData |  |
| 7 | `??0accelerator_view@Concurrency@@QEAA@AEBV01@@Z` | `0x445B0` | 70 | UnwindData |  |
| 8 | `??0accelerator_view_removed@Concurrency@@QEAA@J@Z` | `0x44600` | 66 | UnwindData |  |
| 9 | `??0accelerator_view_removed@Concurrency@@QEAA@PEBDJ@Z` | `0x44650` | 78 | UnwindData |  |
| 10 | `??0invalid_compute_domain@Concurrency@@QEAA@PEBD@Z` | `0x44990` | 61 | UnwindData |  |
| 11 | `??0invalid_compute_domain@Concurrency@@QEAA@XZ` | `0x449D0` | 58 | UnwindData |  |
| 12 | `??0out_of_memory@Concurrency@@QEAA@PEBD@Z` | `0x44B30` | 61 | UnwindData |  |
| 13 | `??0out_of_memory@Concurrency@@QEAA@XZ` | `0x44B70` | 58 | UnwindData |  |
| 14 | `??0runtime_exception@Concurrency@@QEAA@AEBV01@@Z` | `0x44C70` | 102 | UnwindData |  |
| 15 | `??0runtime_exception@Concurrency@@QEAA@J@Z` | `0x44CE0` | 68 | UnwindData |  |
| 16 | `??0runtime_exception@Concurrency@@QEAA@PEBDJ@Z` | `0x44D30` | 72 | UnwindData |  |
| 20 | `??0unsupported_feature@Concurrency@@QEAA@PEBD@Z` | `0x45040` | 61 | UnwindData |  |
| 21 | `??0unsupported_feature@Concurrency@@QEAA@XZ` | `0x45080` | 58 | UnwindData |  |
| 23 | `??1_Event@details@Concurrency@@QEAA@XZ` | `0x451B0` | 28 | UnwindData |  |
| 24 | `??1accelerator@Concurrency@@QEAA@XZ` | `0x451B0` | 28 | UnwindData |  |
| 25 | `??1accelerator_view@Concurrency@@QEAA@XZ` | `0x451B0` | 28 | UnwindData |  |
| 26 | `??1runtime_exception@Concurrency@@UEAA@XZ` | `0x47420` | 40 | UnwindData |  |
| 28 | `??4_Event@details@Concurrency@@QEAAAEAV012@AEBV012@@Z` | `0x47850` | 55 | UnwindData |  |
| 29 | `??4accelerator@Concurrency@@QEAAAEAV01@AEBV01@@Z` | `0x47850` | 55 | UnwindData |  |
| 30 | `??4accelerator_view@Concurrency@@QEAAAEAV01@AEBV01@@Z` | `0x47890` | 71 | UnwindData |  |
| 31 | `??4runtime_exception@Concurrency@@QEAAAEAV01@AEBV01@@Z` | `0x47970` | 67 | UnwindData |  |
| 33 | `??8_Event@details@Concurrency@@QEBA_NAEBV012@@Z` | `0x47A00` | 80 | UnwindData |  |
| 34 | `??8accelerator@Concurrency@@QEBA_NAEBV01@@Z` | `0x47A00` | 80 | UnwindData |  |
| 35 | `??8accelerator_view@Concurrency@@QEBA_NAEBV01@@Z` | `0x47A00` | 80 | UnwindData |  |
| 36 | `??9_Event@details@Concurrency@@QEBA_NAEBV012@@Z` | `0x47B70` | 64 | UnwindData |  |
| 37 | `??9accelerator@Concurrency@@QEBA_NAEBV01@@Z` | `0x47B70` | 64 | UnwindData |  |
| 38 | `??9accelerator_view@Concurrency@@QEBA_NAEBV01@@Z` | `0x47B70` | 64 | UnwindData |  |
| 41 | `?_Adopt_texture@_Texture@details@Concurrency@@SAPEAV123@IW4_Short_vector_base_type_id@23@PEAUIUnknown@@Vaccelerator_view@3@I@Z` | `0x4C5B0` | 1,230 | UnwindData |  |
| 42 | `?_Clone_texture@_Texture@details@Concurrency@@SAPEAV123@PEBV123@AEBVaccelerator_view@3@1@Z` | `0x4DD00` | 235 | UnwindData |  |
| 43 | `?_Copy_async_impl@details@Concurrency@@YA?AV_Event@12@PEAV_Texture@12@PEB_KI01I11@Z` | `0x4EB40` | 7,315 | UnwindData |  |
| 44 | `?_Copy_impl@details@Concurrency@@YA?AV_Event@12@PEAV_Buffer@12@V?$_Reference_counted_obj_ptr@V_View_shape@details@Concurrency@@@12@01@Z` | `0x507E0` | 4,872 | UnwindData |  |
| 45 | `?_Copy_impl@details@Concurrency@@YA?AV_Event@12@PEAV_Buffer@12@_K0111@Z` | `0x51AF0` | 3,493 | UnwindData |  |
| 46 | `?_Copy_to_async@_Buffer@details@Concurrency@@QEAA?AV_Event@23@PEAV123@V?$_Reference_counted_obj_ptr@V_View_shape@details@Concurrency@@@23@1@Z` | `0x528A0` | 766 | UnwindData |  |
| 47 | `?_Copy_to_async@_Buffer@details@Concurrency@@QEAA?AV_Event@23@PEAV123@_K11@Z` | `0x52BA0` | 477 | UnwindData |  |
| 48 | `?_Copy_to_async@_Texture@details@Concurrency@@QEAA?AV_Event@23@PEAV123@PEB_K11II@Z` | `0x52D80` | 399 | UnwindData |  |
| 49 | `?_Create@_Sampler@details@Concurrency@@SAPEAV123@IIMMMM@Z` | `0x52F90` | 156 | UnwindData |  |
| 50 | `?_Create@_Sampler@details@Concurrency@@SAPEAV123@PEAX@Z` | `0x53030` | 150 | UnwindData |  |
| 51 | `?_Create_buffer@_Buffer@details@Concurrency@@SAPEAV123@PEAXVaccelerator_view@3@_K2@Z` | `0x536D0` | 312 | UnwindData |  |
| 52 | `?_Create_buffer@_Buffer@details@Concurrency@@SAPEAV123@Vaccelerator_view@3@0_K1_NW4access_type@3@@Z` | `0x53810` | 360 | UnwindData |  |
| 53 | `?_Create_stage_buffer@_Buffer@details@Concurrency@@SAPEAV123@Vaccelerator_view@3@0_K1_N@Z` | `0x53980` | 492 | UnwindData |  |
| 54 | `?_Create_stage_texture@_Texture@details@Concurrency@@SAPEAV123@Vaccelerator_view@3@0I_K11II_N@Z` | `0x53B70` | 615 | UnwindData |  |
| 55 | `?_Create_stage_texture@_Texture@details@Concurrency@@SAPEAV123@Vaccelerator_view@3@0I_K11IW4_Short_vector_base_type_id@23@II@Z` | `0x53DE0` | 907 | UnwindData |  |
| 56 | `?_Create_texture@_Texture@details@Concurrency@@SAPEAV123@Vaccelerator_view@3@I_K11IW4_Short_vector_base_type_id@23@II_N@Z` | `0x54170` | 720 | UnwindData |  |
| 57 | `?_Create_ubiquitous_buffer@_Ubiquitous_buffer@details@Concurrency@@SAPEAV123@V?$_Reference_counted_obj_ptr@V_Buffer@details@Concurrency@@@23@@Z` | `0x54440` | 192 | UnwindData |  |
| 58 | `?_Create_ubiquitous_buffer@_Ubiquitous_buffer@details@Concurrency@@SAPEAV123@_K0@Z` | `0x54500` | 203 | UnwindData |  |
| 59 | `?_Create_view_shape@_View_shape@details@Concurrency@@SAPEAV123@IIPEBI00PEB_N@Z` | `0x545D0` | 246 | UnwindData |  |
| 60 | `?_Discard@_Ubiquitous_buffer@details@Concurrency@@QEAAXPEAU_Buffer_descriptor@23@@Z` | `0x55B50` | 769 | UnwindData |  |
| 61 | `?_Exclusively_owns_data@_Buffer@details@Concurrency@@QEAA_NXZ` | `0x569A0` | 84 | UnwindData |  |
| 145 | `?get_is_auto_selection@accelerator_view@Concurrency@@QEBA_NXZ` | `0x571C0` | 3,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `?_Get_CPU_access@_Buffer_descriptor@details@Concurrency@@QEBAXW4_Access_mode@@@Z` | `0x57F10` | 472 | UnwindData |  |
| 68 | `?_Get_accelerator_view@_Buffer@details@Concurrency@@QEBA?AVaccelerator_view@3@XZ` | `0x580F0` | 109 | UnwindData |  |
| 76 | `?_Get_master_accelerator_view@_Ubiquitous_buffer@details@Concurrency@@QEBA?AVaccelerator_view@3@XZ` | `0x580F0` | 109 | UnwindData |  |
| 69 | `?_Get_access_async@_Ubiquitous_buffer@details@Concurrency@@AEAA?AV_Event@23@PEAU_Buffer_descriptor@23@Vaccelerator_view@3@W4_Access_mode@@AEAV?$_Reference_counted_obj_ptr@V_Buffer@details@Concurrency@@@23@PEA_K@Z` | `0x58160` | 188 | UnwindData |  |
| 70 | `?_Get_access_async@_Ubiquitous_buffer@details@Concurrency@@QEAA?AV_Event@23@PEAU_Buffer_descriptor@23@V?$_Reference_counted_obj_ptr@V_Accelerator_view_impl@details@Concurrency@@@23@W4_Access_mode@@AEAV?$_Reference_counted_obj_ptr@V_Buffer@details@Concurrency@@@23@PEA_K@Z` | `0x58220` | 6,675 | UnwindData |  |
| 71 | `?_Get_access_on_accelerator_view@_Buffer@details@Concurrency@@QEBA?AVaccelerator_view@3@XZ` | `0x59C40` | 109 | UnwindData |  |
| 73 | `?_Get_description@accelerator@Concurrency@@AEBAPEB_WXZ` | `0x5AED0` | 65 | UnwindData |  |
| 74 | `?_Get_device_path@accelerator@Concurrency@@AEBAPEB_WXZ` | `0x5AF20` | 65 | UnwindData |  |
| 77 | `?_Get_master_buffer@_Ubiquitous_buffer@details@Concurrency@@QEBA?AV?$_Reference_counted_obj_ptr@V_Buffer@details@Concurrency@@@23@XZ` | `0x5AF70` | 64 | UnwindData |  |
| 143 | `?get_error_code@runtime_exception@Concurrency@@QEBAJXZ` | `0x5B1B0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `?_Get_recommended_buffer_host_access_mode@details@Concurrency@@YA?AW4_Access_mode@@AEBVaccelerator_view@2@@Z` | `0x5B270` | 117 | UnwindData |  |
| 81 | `?_Get_reduced_shape_for_copy@_View_shape@details@Concurrency@@QEAAPEAV123@XZ` | `0x5B2F0` | 762 | UnwindData |  |
| 82 | `?_Get_src_dest_accelerator_view@details@Concurrency@@YA?AU?$pair@Vaccelerator_view@Concurrency@@V12@@std@@PEBU_Buffer_descriptor@12@0@Z` | `0x5B5F0` | 928 | UnwindData |  |
| 83 | `?_Get_temp_staging_buffer@_Buffer@details@Concurrency@@SAPEAV123@Vaccelerator_view@3@_K1@Z` | `0x5B9F0` | 231 | UnwindData |  |
| 84 | `?_Get_temp_staging_texture@_Texture@details@Concurrency@@SAPEAV123@Vaccelerator_view@3@I_K11II@Z` | `0x5BAE0` | 694 | UnwindData |  |
| 85 | `?_Get_view_shape@_Ubiquitous_buffer@details@Concurrency@@QEAA?AV?$_Reference_counted_obj_ptr@V_View_shape@details@Concurrency@@@23@PEAU_Buffer_descriptor@23@@Z` | `0x5C060` | 426 | UnwindData |  |
| 86 | `?_Init@accelerator@Concurrency@@AEAAXPEB_W@Z` | `0x5C880` | 236 | UnwindData |  |
| 91 | `?_Is_mappable@_Buffer@details@Concurrency@@QEBA_NXZ` | `0x5CD80` | 101 | UnwindData |  |
| 99 | `?_Map_buffer@_Buffer@details@Concurrency@@QEAAXW4_Access_mode@@_N@Z` | `0x5D080` | 260 | UnwindData |  |
| 100 | `?_Map_buffer_async@_Buffer@details@Concurrency@@QEAA?AV_Event@23@W4_Access_mode@@@Z` | `0x5D190` | 285 | UnwindData |  |
| 101 | `?_Recursive_array_copy@details@Concurrency@@YAJAEBU_Array_copy_desc@12@IV?$function@$$A6AJAEBU_Array_copy_desc@details@Concurrency@@@Z@std@@@Z` | `0x5DB60` | 2,429 | UnwindData |  |
| 102 | `?_Register_async_event@details@Concurrency@@YAXAEBV_Event@12@AEBV?$shared_future@X@std@@@Z` | `0x5E8C0` | 50 | UnwindData |  |
| 103 | `?_Register_view@_Buffer@details@Concurrency@@QEAAXPEAU_Buffer_descriptor@23@@Z` | `0x5E900` | 465 | UnwindData |  |
| 104 | `?_Register_view@_Ubiquitous_buffer@details@Concurrency@@QEAAXPEAU_Buffer_descriptor@23@Vaccelerator_view@3@V?$_Reference_counted_obj_ptr@V_View_shape@details@Concurrency@@@23@QEAU423@@Z` | `0x5EAE0` | 770 | UnwindData |  |
| 105 | `?_Register_view_copy@_Ubiquitous_buffer@details@Concurrency@@QEAAXPEAU_Buffer_descriptor@23@0@Z` | `0x5EDF0` | 804 | UnwindData |  |
| 106 | `?_Release@_Reference_counter@details@Concurrency@@QEAAXXZ` | `0x5F340` | 132 | UnwindData |  |
| 108 | `?_Select_copy_src_accelerator_view@details@Concurrency@@YA?AVaccelerator_view@2@PEAU_Buffer_descriptor@12@AEBV32@@Z` | `0x60410` | 1,793 | UnwindData |  |
| 120 | `?_Unmap_buffer@_Buffer@details@Concurrency@@QEAAXXZ` | `0x62D90` | 161 | UnwindData |  |
| 121 | `?_Unregister_view@_Buffer@details@Concurrency@@QEAAXPEAU_Buffer_descriptor@23@@Z` | `0x62E70` | 340 | UnwindData |  |
| 122 | `?_Unregister_view@_Ubiquitous_buffer@details@Concurrency@@QEAAXPEAU_Buffer_descriptor@23@@Z` | `0x62FD0` | 710 | UnwindData |  |
| 124 | `?amp_uninitialize@Concurrency@@YAXXZ` | `0x63F10` | 15 | UnwindData |  |
| 128 | `?create_marker@accelerator_view@Concurrency@@QEAA?AVcompletion_future@2@XZ` | `0x64660` | 318 | UnwindData |  |
| 129 | `?create_view@accelerator@Concurrency@@QEAA?AVaccelerator_view@2@W4queuing_mode@2@@Z` | `0x647A0` | 309 | UnwindData |  |
| 136 | `?flush@accelerator_view@Concurrency@@QEAAXXZ` | `0x64EB0` | 143 | UnwindData |  |
| 137 | `?get_accelerator@accelerator_view@Concurrency@@QEBA?AVaccelerator@2@XZ` | `0x65000` | 118 | UnwindData |  |
| 138 | `?get_auto_selection_view@accelerator@Concurrency@@SA?AVaccelerator_view@2@XZ` | `0x65090` | 238 | UnwindData |  |
| 139 | `?get_dedicated_memory@accelerator@Concurrency@@QEBA_KXZ` | `0x65220` | 65 | UnwindData |  |
| 140 | `?get_default_cpu_access_type@accelerator@Concurrency@@QEBA?AW4access_type@2@XZ` | `0x65270` | 51 | UnwindData |  |
| 141 | `?get_default_view@accelerator@Concurrency@@QEBA?AVaccelerator_view@2@XZ` | `0x652B0` | 121 | UnwindData |  |
| 144 | `?get_has_display@accelerator@Concurrency@@QEBA_NXZ` | `0x65380` | 65 | UnwindData |  |
| 146 | `?get_is_debug@accelerator@Concurrency@@QEBA_NXZ` | `0x653D0` | 101 | UnwindData |  |
| 147 | `?get_is_debug@accelerator_view@Concurrency@@QEBA_NXZ` | `0x65440` | 35 | UnwindData |  |
| 148 | `?get_is_emulated@accelerator@Concurrency@@QEBA_NXZ` | `0x65470` | 35 | UnwindData |  |
| 149 | `?get_queuing_mode@accelerator_view@Concurrency@@QEBA?AW4queuing_mode@2@XZ` | `0x654A0` | 35 | UnwindData |  |
| 150 | `?get_supports_cpu_shared_memory@accelerator@Concurrency@@QEBA_NXZ` | `0x65510` | 35 | UnwindData |  |
| 151 | `?get_supports_double_precision@accelerator@Concurrency@@QEBA_NXZ` | `0x65540` | 35 | UnwindData |  |
| 152 | `?get_supports_limited_double_precision@accelerator@Concurrency@@QEBA_NXZ` | `0x65570` | 35 | UnwindData |  |
| 153 | `?get_version@accelerator@Concurrency@@QEBAIXZ` | `0x655A0` | 100 | UnwindData |  |
| 154 | `?get_version@accelerator_view@Concurrency@@QEBAIXZ` | `0x65610` | 35 | UnwindData |  |
| 157 | `?set_default_cpu_access_type@accelerator@Concurrency@@QEAA_NW4access_type@2@@Z` | `0x66300` | 177 | UnwindData |  |
| 158 | `?wait@accelerator_view@Concurrency@@QEAAXXZ` | `0x66710` | 171 | UnwindData |  |
| 159 | `__dpc_create_call_handle` | `0x6A6C0` | 86 | UnwindData |  |
| 160 | `__dpc_dispatch_kernel` | `0x6A720` | 205 | UnwindData |  |
| 161 | `__dpc_dispatch_kernel_test` | `0x6A7F0` | 102 | UnwindData |  |
| 162 | `__dpc_release_call_handle` | `0x6A860` | 63 | UnwindData |  |
| 163 | `__dpc_set_const_buffer_info` | `0x6A8A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 164 | `__dpc_set_device_resource_info` | `0x6A8D0` | 259 | UnwindData |  |
| 165 | `__dpc_set_kernel_dispatch_info` | `0x6A9E0` | 4,115 | UnwindData |  |
| 166 | `__dpc_set_kernel_shader_info` | `0x6BA00` | 323 | UnwindData |  |
| 2 | `??0_Event@details@Concurrency@@QEAA@XZ` | `0x7F8E0` | 42 | UnwindData |  |
| 39 | `?_Add_continuation@_Event@details@Concurrency@@QEAA?AV123@AEBV?$function@$$A6A?AV_Event@details@Concurrency@@XZ@std@@@Z` | `0x80330` | 266 | UnwindData |  |
| 40 | `?_Add_event@_Event@details@Concurrency@@QEAA?AV123@V123@@Z` | `0x80440` | 914 | UnwindData |  |
| 62 | `?_Get@_Event@details@Concurrency@@QEAAXXZ` | `0x80D40` | 56 | UnwindData |  |
| 88 | `?_Is_empty@_Event@details@Concurrency@@QEBA_NXZ` | `0x814E0` | 55 | UnwindData |  |
| 89 | `?_Is_finished@_Event@details@Concurrency@@QEAA_NXZ` | `0x81520` | 57 | UnwindData |  |
| 90 | `?_Is_finished_nothrow@_Event@details@Concurrency@@QEAA_NXZ` | `0x81AD0` | 57 | UnwindData |  |
| 22 | `??1_Amp_runtime_trace@details@Concurrency@@QEAA@XZ` | `0x84150` | 113 | UnwindData |  |
| 72 | `?_Get_amp_trace@details@Concurrency@@YAPEAV_Amp_runtime_trace@12@XZ` | `0x84840` | 126 | UnwindData |  |
| 92 | `?_Launch_array_view_synchronize_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Buffer_descriptor@23@@Z` | `0x84FC0` | 462 | UnwindData |  |
| 93 | `?_Launch_async_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAK$$TAEBU_Buffer_descriptor@23@_K@Z` | `0x85680` | 505 | UnwindData |  |
| 94 | `?_Launch_async_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAK$$TAEBU_Texture_descriptor@23@_K@Z` | `0x85880` | 356 | UnwindData |  |
| 95 | `?_Launch_async_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Buffer_descriptor@23@$$T_K@Z` | `0x859F0` | 506 | UnwindData |  |
| 96 | `?_Launch_async_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Buffer_descriptor@23@0_K@Z` | `0x85BF0` | 546 | UnwindData |  |
| 97 | `?_Launch_async_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Texture_descriptor@23@$$T_K@Z` | `0x85E20` | 357 | UnwindData |  |
| 98 | `?_Launch_async_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Texture_descriptor@23@0_K@Z` | `0x85F90` | 315 | UnwindData |  |
| 111 | `?_Start_array_view_synchronize_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Buffer_descriptor@23@@Z` | `0x86AF0` | 462 | UnwindData |  |
| 112 | `?_Start_async_op_wait_event@_Amp_runtime_trace@details@Concurrency@@AEAAKK@Z` | `0x86CC0` | 474 | UnwindData |  |
| 113 | `?_Start_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAK$$TAEBU_Buffer_descriptor@23@_K@Z` | `0x87390` | 505 | UnwindData |  |
| 114 | `?_Start_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAK$$TAEBU_Texture_descriptor@23@_K@Z` | `0x87590` | 356 | UnwindData |  |
| 115 | `?_Start_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Buffer_descriptor@23@$$T_K@Z` | `0x87700` | 506 | UnwindData |  |
| 116 | `?_Start_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Buffer_descriptor@23@0_K@Z` | `0x87900` | 546 | UnwindData |  |
| 117 | `?_Start_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Texture_descriptor@23@$$T_K@Z` | `0x87B30` | 357 | UnwindData |  |
| 118 | `?_Start_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Texture_descriptor@23@0_K@Z` | `0x87CA0` | 315 | UnwindData |  |
| 119 | `?_Start_parallel_for_each_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKPEAU_DPC_call_handle@23@@Z` | `0x88480` | 1,396 | UnwindData |  |
| 123 | `?_Write_end_event@_Amp_runtime_trace@details@Concurrency@@QEAAXK@Z` | `0x89050` | 347 | UnwindData |  |
| 133 | `?default_accelerator@accelerator@Concurrency@@2QB_WB` | `0xA7898` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `?cpu_accelerator@accelerator@Concurrency@@2QB_WB` | `0xA78A8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `?direct3d_warp@accelerator@Concurrency@@2QB_WB` | `0xA78B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `?direct3d_ref@accelerator@Concurrency@@2QB_WB` | `0xA78D0` | 0 | Indeterminate |  |
