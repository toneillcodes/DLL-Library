# Binary Specification: vcamp110.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\vcamp110.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b26ddd1aeaf3f81edcc5a55a1938357a466ea2b0652560c4999faa92960f6190`
* **Total Exported Functions:** 130

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 82 | `?_Release@_Buffer@details@Concurrency@@UEAAXXZ` | `0x1B50` | 34 | UnwindData |  |
| 83 | `?_Release@_Ubiquitous_buffer@details@Concurrency@@UEAAXXZ` | `0x1B50` | 34 | UnwindData |  |
| 84 | `?_Release@_View_shape@details@Concurrency@@UEAAXXZ` | `0x1B50` | 34 | UnwindData |  |
| 101 | `?create_accelerator_view@direct3d@Concurrency@@YA?AVaccelerator_view@2@PEAUIUnknown@@W4queuing_mode@2@@Z` | `0x8458` | 423 | UnwindData |  |
| 61 | `?_Get_master_buffer@_Ubiquitous_buffer@details@Concurrency@@QEBA?AV?$_Reference_counted_obj_ptr@V_Buffer@details@Concurrency@@@23@XZ` | `0x87EC` | 54 | UnwindData |  |
| 50 | `?_Get_D3D_buffer@_D3D_interop@details@Concurrency@@SAPEAUIUnknown@@PEAV_Buffer@23@@Z` | `0xDAB4` | 206 | UnwindData |  |
| 51 | `?_Get_D3D_texture@_D3D_interop@details@Concurrency@@SAPEAUIUnknown@@PEAV_Texture@23@@Z` | `0xDB84` | 31 | UnwindData |  |
| 111 | `?get_device@direct3d@Concurrency@@YAPEAUIUnknown@@AEBVaccelerator_view@2@@Z` | `0xDBA4` | 98 | UnwindData |  |
| 62 | `?_Get_num_devices@details@Concurrency@@YA_KXZ` | `0xFA3C` | 28 | UnwindData |  |
| 59 | `?_Get_devices@details@Concurrency@@YAPEAV?$_Reference_counted_obj_ptr@V_Accelerator_impl@details@Concurrency@@@12@XZ` | `0xFA58` | 17 | UnwindData |  |
| 85 | `?_Select_default_accelerator@details@Concurrency@@YA?AVaccelerator@2@XZ` | `0xFA6C` | 84 | UnwindData |  |
| 86 | `?_Set_default_accelerator@details@Concurrency@@YA_NV?$_Reference_counted_obj_ptr@V_Accelerator_impl@details@Concurrency@@@12@@Z` | `0xFAC0` | 168 | UnwindData |  |
| 66 | `?_Is_D3D_accelerator_view@details@Concurrency@@YA_NAEBVaccelerator_view@2@@Z` | `0xFB68` | 74 | UnwindData |  |
| 5 | `??0accelerator@Concurrency@@QEAA@XZ` | `0x154FC` | 161 | UnwindData |  |
| 65 | `?_Init@accelerator@Concurrency@@AEAAXPEB_W@Z` | `0x155A0` | 287 | UnwindData |  |
| 20 | `??1_Event@details@Concurrency@@QEAA@XZ` | `0x156C0` | 43 | UnwindData |  |
| 21 | `??1accelerator@Concurrency@@QEAA@XZ` | `0x156C0` | 43 | UnwindData |  |
| 22 | `??1accelerator_view@Concurrency@@QEAA@XZ` | `0x156C0` | 43 | UnwindData |  |
| 1 | `??0_Event@details@Concurrency@@QEAA@AEBV012@@Z` | `0x156EC` | 40 | UnwindData |  |
| 4 | `??0accelerator@Concurrency@@QEAA@AEBV01@@Z` | `0x156EC` | 40 | UnwindData |  |
| 7 | `??0accelerator_view@Concurrency@@QEAA@AEBV01@@Z` | `0x156EC` | 40 | UnwindData |  |
| 24 | `??4_Event@details@Concurrency@@QEAAAEAV012@AEBV012@@Z` | `0x15714` | 63 | UnwindData |  |
| 25 | `??4accelerator@Concurrency@@QEAAAEAV01@AEBV01@@Z` | `0x15714` | 63 | UnwindData |  |
| 26 | `??4accelerator_view@Concurrency@@QEAAAEAV01@AEBV01@@Z` | `0x15714` | 63 | UnwindData |  |
| 3 | `??0accelerator@Concurrency@@AEAA@V?$_Reference_counted_obj_ptr@V_Accelerator_impl@details@Concurrency@@@details@1@@Z` | `0x15754` | 71 | UnwindData |  |
| 6 | `??0accelerator_view@Concurrency@@AEAA@V?$_Reference_counted_obj_ptr@V_Accelerator_view_impl@details@Concurrency@@@details@1@@Z` | `0x15754` | 71 | UnwindData |  |
| 58 | `?_Get_device_path@accelerator@Concurrency@@AEBAPEB_WXZ` | `0x1579C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `?_Get_description@accelerator@Concurrency@@AEBAPEB_WXZ` | `0x157A8` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `?get_version@accelerator@Concurrency@@QEBAIXZ` | `0x157B4` | 50 | UnwindData |  |
| 114 | `?get_is_debug@accelerator@Concurrency@@QEBA_NXZ` | `0x157E8` | 50 | UnwindData |  |
| 116 | `?get_is_emulated@accelerator@Concurrency@@QEBA_NXZ` | `0x1581C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `?get_has_display@accelerator@Concurrency@@QEBA_NXZ` | `0x15824` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `?get_supports_double_precision@accelerator@Concurrency@@QEBA_NXZ` | `0x15830` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `?get_supports_limited_double_precision@accelerator@Concurrency@@QEBA_NXZ` | `0x1583C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `?get_default_view@accelerator@Concurrency@@QEBA?AVaccelerator_view@2@XZ` | `0x15848` | 106 | UnwindData |  |
| 109 | `?get_dedicated_memory@accelerator@Concurrency@@QEBA_KXZ` | `0x158B4` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `?create_view@accelerator@Concurrency@@QEAA?AVaccelerator_view@2@W4queuing_mode@2@@Z` | `0x158C0` | 197 | UnwindData |  |
| 28 | `??8_Event@details@Concurrency@@QEBA_NAEBV012@@Z` | `0x15988` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `??8accelerator@Concurrency@@QEBA_NAEBV01@@Z` | `0x15988` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `??8accelerator_view@Concurrency@@QEBA_NAEBV01@@Z` | `0x15988` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `??9_Event@details@Concurrency@@QEBA_NAEBV012@@Z` | `0x15994` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `??9accelerator@Concurrency@@QEBA_NAEBV01@@Z` | `0x15994` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `??9accelerator_view@Concurrency@@QEBA_NAEBV01@@Z` | `0x15994` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `?get_version@accelerator_view@Concurrency@@QEBAIXZ` | `0x159A0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `?get_is_debug@accelerator_view@Concurrency@@QEBA_NXZ` | `0x159A8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `?get_queuing_mode@accelerator_view@Concurrency@@QEBA?AW4queuing_mode@2@XZ` | `0x159B0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `?get_accelerator@accelerator_view@Concurrency@@QEBA?AVaccelerator@2@XZ` | `0x159B8` | 116 | UnwindData |  |
| 102 | `?create_marker@accelerator_view@Concurrency@@QEAA?AVcompletion_future@2@XZ` | `0x15A2C` | 318 | UnwindData |  |
| 123 | `?wait@accelerator_view@Concurrency@@QEAAXXZ` | `0x15B6C` | 325 | UnwindData |  |
| 107 | `?flush@accelerator_view@Concurrency@@QEAAXXZ` | `0x15CB4` | 182 | UnwindData |  |
| 16 | `??0runtime_exception@Concurrency@@QEAA@PEBDJ@Z` | `0x15D6C` | 72 | UnwindData |  |
| 15 | `??0runtime_exception@Concurrency@@QEAA@J@Z` | `0x15DB4` | 78 | UnwindData |  |
| 14 | `??0runtime_exception@Concurrency@@QEAA@AEBV01@@Z` | `0x15E04` | 89 | UnwindData |  |
| 27 | `??4runtime_exception@Concurrency@@QEAAAEAV01@AEBV01@@Z` | `0x15E60` | 47 | UnwindData |  |
| 23 | `??1runtime_exception@Concurrency@@UEAA@XZ` | `0x15E90` | 39 | UnwindData |  |
| 112 | `?get_error_code@runtime_exception@Concurrency@@QEBAJXZ` | `0x15EB8` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `??0out_of_memory@Concurrency@@QEAA@PEBD@Z` | `0x15EBC` | 53 | UnwindData |  |
| 13 | `??0out_of_memory@Concurrency@@QEAA@XZ` | `0x15EF4` | 60 | UnwindData |  |
| 9 | `??0accelerator_view_removed@Concurrency@@QEAA@PEBDJ@Z` | `0x15F30` | 69 | UnwindData |  |
| 8 | `??0accelerator_view_removed@Concurrency@@QEAA@J@Z` | `0x15F78` | 67 | UnwindData |  |
| 122 | `?get_view_removed_reason@accelerator_view_removed@Concurrency@@QEBAJXZ` | `0x15FBC` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `??0invalid_compute_domain@Concurrency@@QEAA@PEBD@Z` | `0x15FC0` | 53 | UnwindData |  |
| 11 | `??0invalid_compute_domain@Concurrency@@QEAA@XZ` | `0x15FF8` | 60 | UnwindData |  |
| 17 | `??0unsupported_feature@Concurrency@@QEAA@PEBD@Z` | `0x16034` | 53 | UnwindData |  |
| 18 | `??0unsupported_feature@Concurrency@@QEAA@XZ` | `0x1606C` | 60 | UnwindData |  |
| 77 | `?_Recursive_array_copy@details@Concurrency@@YAJAEBU_Array_copy_desc@12@IV?$function@$$A6AJAEBU_Array_copy_desc@details@Concurrency@@@Z@std@@@Z` | `0x160A8` | 1,024 | UnwindData |  |
| 46 | `?_Create_view_shape@_View_shape@details@Concurrency@@SAPEAV123@IIPEBI00PEB_N@Z` | `0x164A8` | 130 | UnwindData |  |
| 40 | `?_Create_buffer@_Buffer@details@Concurrency@@SAPEAV123@Vaccelerator_view@3@_K1_N@Z` | `0x16710` | 205 | UnwindData |  |
| 39 | `?_Create_buffer@_Buffer@details@Concurrency@@SAPEAV123@PEAXVaccelerator_view@3@_K2@Z` | `0x167E0` | 201 | UnwindData |  |
| 41 | `?_Create_stage_buffer@_Buffer@details@Concurrency@@SAPEAV123@Vaccelerator_view@3@0_K1_N@Z` | `0x168AC` | 432 | UnwindData |  |
| 63 | `?_Get_temp_staging_buffer@_Buffer@details@Concurrency@@SA_KVaccelerator_view@3@_K1PEAPEAV123@@Z` | `0x16A5C` | 134 | UnwindData |  |
| 76 | `?_Map_stage_buffer@_Buffer@details@Concurrency@@QEAAPEAXW4_Access_mode@@_N@Z` | `0x16AE4` | 93 | UnwindData |  |
| 96 | `?_Unmap_stage_buffer@_Buffer@details@Concurrency@@QEAAXXZ` | `0x16B44` | 69 | UnwindData |  |
| 37 | `?_Copy_to_async@_Buffer@details@Concurrency@@QEAA?AV_Event@23@PEAV123@_K11@Z` | `0x16B8C` | 185 | UnwindData |  |
| 36 | `?_Copy_to_async@_Buffer@details@Concurrency@@QEAA?AV_Event@23@PEAV123@V?$_Reference_counted_obj_ptr@V_View_shape@details@Concurrency@@@23@1@Z` | `0x16C48` | 438 | UnwindData |  |
| 52 | `?_Get_accelerator_view@_Buffer@details@Concurrency@@QEBA?AVaccelerator_view@3@XZ` | `0x16E00` | 85 | UnwindData |  |
| 60 | `?_Get_master_accelerator_view@_Ubiquitous_buffer@details@Concurrency@@QEBA?AVaccelerator_view@3@XZ` | `0x16E00` | 85 | UnwindData |  |
| 55 | `?_Get_access_on_accelerator_view@_Buffer@details@Concurrency@@QEBA?AVaccelerator_view@3@XZ` | `0x16E58` | 85 | UnwindData |  |
| 79 | `?_Register_view@_Buffer@details@Concurrency@@QEAAXPEAU_Buffer_descriptor@23@@Z` | `0x16EB0` | 140 | UnwindData |  |
| 97 | `?_Unregister_view@_Buffer@details@Concurrency@@QEAAXPEAU_Buffer_descriptor@23@@Z` | `0x16F3C` | 127 | UnwindData |  |
| 44 | `?_Create_texture@_Texture@details@Concurrency@@SAPEAV123@Vaccelerator_view@3@I_K11IW4_Short_vector_base_type_id@23@II_N@Z` | `0x17164` | 413 | UnwindData |  |
| 43 | `?_Create_texture@_Texture@details@Concurrency@@SAPEAV123@IW4_Short_vector_base_type_id@23@PEAUIUnknown@@Vaccelerator_view@3@@Z` | `0x17304` | 341 | UnwindData |  |
| 42 | `?_Create_stage_texture@_Texture@details@Concurrency@@SAPEAV123@Vaccelerator_view@3@0I_K11II_N@Z` | `0x1745C` | 428 | UnwindData |  |
| 38 | `?_Copy_to_async@_Texture@details@Concurrency@@QEAA?AV_Event@23@PEAV123@@Z` | `0x17608` | 113 | UnwindData |  |
| 45 | `?_Create_ubiquitous_buffer@_Ubiquitous_buffer@details@Concurrency@@SAPEAV123@V?$_Reference_counted_obj_ptr@V_Buffer@details@Concurrency@@@23@@Z` | `0x17850` | 174 | UnwindData |  |
| 80 | `?_Register_view@_Ubiquitous_buffer@details@Concurrency@@QEAAXPEAU_Buffer_descriptor@23@Vaccelerator_view@3@V?$_Reference_counted_obj_ptr@V_View_shape@details@Concurrency@@@23@@Z` | `0x17900` | 604 | UnwindData |  |
| 81 | `?_Register_view_copy@_Ubiquitous_buffer@details@Concurrency@@QEAAXPEAU_Buffer_descriptor@23@0@Z` | `0x17B5C` | 307 | UnwindData |  |
| 98 | `?_Unregister_view@_Ubiquitous_buffer@details@Concurrency@@QEAAXPEAU_Buffer_descriptor@23@@Z` | `0x17C90` | 258 | UnwindData |  |
| 53 | `?_Get_access_async@_Ubiquitous_buffer@details@Concurrency@@AEAA?AV_Event@23@PEAU_Buffer_descriptor@23@Vaccelerator_view@3@W4_Access_mode@@AEAV?$_Reference_counted_obj_ptr@V_Buffer@details@Concurrency@@@23@PEA_K@Z` | `0x17E68` | 142 | UnwindData |  |
| 54 | `?_Get_access_async@_Ubiquitous_buffer@details@Concurrency@@QEAA?AV_Event@23@PEAU_Buffer_descriptor@23@V?$_Reference_counted_obj_ptr@V_Accelerator_view_impl@details@Concurrency@@@23@W4_Access_mode@@AEAV?$_Reference_counted_obj_ptr@V_Buffer@details@Concurrency@@@23@PEA_K@Z` | `0x17EF8` | 3,731 | UnwindData |  |
| 47 | `?_Discard@_Ubiquitous_buffer@details@Concurrency@@QEAAXPEAU_Buffer_descriptor@23@@Z` | `0x19240` | 306 | UnwindData |  |
| 64 | `?_Get_view_shape@_Ubiquitous_buffer@details@Concurrency@@QEAA?AV?$_Reference_counted_obj_ptr@V_View_shape@details@Concurrency@@@23@PEAU_Buffer_descriptor@23@@Z` | `0x19374` | 223 | UnwindData |  |
| 49 | `?_Get_CPU_access@_Buffer_descriptor@details@Concurrency@@QEBAXW4_Access_mode@@@Z` | `0x1A214` | 333 | UnwindData |  |
| 78 | `?_Register_async_event@details@Concurrency@@YAXAEBV_Event@12@AEBV?$shared_future@X@std@@@Z` | `0x1A364` | 332 | UnwindData |  |
| 124 | `__dpc_create_call_handle` | `0x2031C` | 234 | UnwindData |  |
| 126 | `__dpc_release_call_handle` | `0x20408` | 157 | UnwindData |  |
| 128 | `__dpc_set_device_buffer_info` | `0x204A8` | 409 | UnwindData |  |
| 130 | `__dpc_set_kernel_shader_info` | `0x20644` | 488 | UnwindData |  |
| 127 | `__dpc_set_const_buffer_info` | `0x2082C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `__dpc_set_kernel_dispatch_info` | `0x20838` | 1,425 | UnwindData |  |
| 125 | `__dpc_dispatch_kernel` | `0x20DCC` | 72 | UnwindData |  |
| 2 | `??0_Event@details@Concurrency@@QEAA@XZ` | `0x259E8` | 29 | UnwindData |  |
| 69 | `?_Is_finished_nothrow@_Event@details@Concurrency@@QEAA_NXZ` | `0x25A08` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `?_Is_finished@_Event@details@Concurrency@@QEAA_NXZ` | `0x25A18` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `?_Is_empty@_Event@details@Concurrency@@QEBA_NXZ` | `0x25A28` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `?_Get@_Event@details@Concurrency@@QEAAXXZ` | `0x25A34` | 22 | UnwindData |  |
| 35 | `?_Add_event@_Event@details@Concurrency@@QEAA?AV123@V123@@Z` | `0x25A4C` | 514 | UnwindData |  |
| 34 | `?_Add_continuation@_Event@details@Concurrency@@QEAA?AV123@AEBV?$function@$$A6A?AV_Event@details@Concurrency@@XZ@std@@@Z` | `0x25C50` | 296 | UnwindData |  |
| 19 | `??1_Amp_runtime_trace@details@Concurrency@@QEAA@XZ` | `0x26F50` | 91 | UnwindData |  |
| 56 | `?_Get_amp_trace@details@Concurrency@@YAPEAV_Amp_runtime_trace@12@XZ` | `0x27058` | 81 | UnwindData |  |
| 99 | `?_Write_end_event@_Amp_runtime_trace@details@Concurrency@@QEAAXK@Z` | `0x27154` | 96 | UnwindData |  |
| 88 | `?_Start_async_op_wait_event@_Amp_runtime_trace@details@Concurrency@@AEAAKK@Z` | `0x273A4` | 130 | UnwindData |  |
| 95 | `?_Start_parallel_for_each_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKPEAU_DPC_call_handle@23@@Z` | `0x27428` | 1,123 | UnwindData |  |
| 87 | `?_Start_array_view_synchronize_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Buffer_descriptor@23@@Z` | `0x2788C` | 467 | UnwindData |  |
| 70 | `?_Launch_array_view_synchronize_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Buffer_descriptor@23@@Z` | `0x27A60` | 467 | UnwindData |  |
| 92 | `?_Start_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Buffer_descriptor@23@0_K@Z` | `0x27D70` | 155 | UnwindData |  |
| 89 | `?_Start_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAK$$TAEBU_Buffer_descriptor@23@_K@Z` | `0x27E0C` | 120 | UnwindData |  |
| 91 | `?_Start_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Buffer_descriptor@23@$$T_K@Z` | `0x27E84` | 119 | UnwindData |  |
| 74 | `?_Launch_async_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Buffer_descriptor@23@0_K@Z` | `0x27EFC` | 155 | UnwindData |  |
| 71 | `?_Launch_async_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAK$$TAEBU_Buffer_descriptor@23@_K@Z` | `0x27F98` | 120 | UnwindData |  |
| 73 | `?_Launch_async_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Buffer_descriptor@23@$$T_K@Z` | `0x28010` | 119 | UnwindData |  |
| 93 | `?_Start_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Texture_descriptor@23@$$T_K@Z` | `0x2812C` | 119 | UnwindData |  |
| 90 | `?_Start_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAK$$TAEBU_Texture_descriptor@23@_K@Z` | `0x281A4` | 120 | UnwindData |  |
| 94 | `?_Start_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Texture_descriptor@23@0_K@Z` | `0x2821C` | 155 | UnwindData |  |
| 75 | `?_Launch_async_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAKAEBU_Texture_descriptor@23@$$T_K@Z` | `0x282B8` | 119 | UnwindData |  |
| 72 | `?_Launch_async_copy_event_helper@_Amp_runtime_trace@details@Concurrency@@QEAAK$$TAEBU_Texture_descriptor@23@_K@Z` | `0x28330` | 120 | UnwindData |  |
| 100 | `?cpu_accelerator@accelerator@Concurrency@@2QB_WB` | `0x355A0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `?direct3d_warp@accelerator@Concurrency@@2QB_WB` | `0x355A8` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `?direct3d_ref@accelerator@Concurrency@@2QB_WB` | `0x355C8` | 1,448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `?default_accelerator@accelerator@Concurrency@@2QB_WB` | `0x35B70` | 0 | Indeterminate |  |
