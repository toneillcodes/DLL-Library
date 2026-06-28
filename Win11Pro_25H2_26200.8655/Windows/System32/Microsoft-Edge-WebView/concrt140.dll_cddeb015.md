# Binary Specification: concrt140.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Microsoft-Edge-WebView\concrt140.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `cddeb01549b63c73344ddbbb81ea9ca980668d2d1ddd76e1fd1a9096da2ba68c`
* **Total Exported Functions:** 291

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `??0?$_SpinWait@$00@details@Concurrency@@QEAA@P6AXXZ@Z` | `0x1060` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0?$_SpinWait@$0A@@details@Concurrency@@QEAA@P6AXXZ@Z` | `0x1060` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `??0_Context@details@Concurrency@@QEAA@PEAVContext@2@@Z` | `0x1070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `??0_Scheduler@details@Concurrency@@QEAA@PEAVScheduler@2@@Z` | `0x1070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `??4?$_SpinWait@$00@details@Concurrency@@QEAAAEAV012@$$QEAV012@@Z` | `0x1090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `??4?$_SpinWait@$0A@@details@Concurrency@@QEAAAEAV012@$$QEAV012@@Z` | `0x1090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `??4?$_SpinWait@$00@details@Concurrency@@QEAAAEAV012@AEBV012@@Z` | `0x10B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `??4?$_SpinWait@$0A@@details@Concurrency@@QEAAAEAV012@AEBV012@@Z` | `0x10B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `??_F?$_SpinWait@$00@details@Concurrency@@QEAAXXZ` | `0x10D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `??_F?$_SpinWait@$0A@@details@Concurrency@@QEAAXXZ` | `0x10D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `??_F_Context@details@Concurrency@@QEAAXXZ` | `0x10F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `??_F_Scheduler@details@Concurrency@@QEAAXXZ` | `0x10F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `?_DoYield@?$_SpinWait@$00@details@Concurrency@@IEAAXXZ` | `0x1100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 193 | `?_GetScheduler@_Scheduler@details@Concurrency@@QEAAPEAVScheduler@3@XZ` | `0x1110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 219 | `?_NumberOfSpins@?$_SpinWait@$00@details@Concurrency@@IEAAKXZ` | `0x1120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 220 | `?_NumberOfSpins@?$_SpinWait@$0A@@details@Concurrency@@IEAAKXZ` | `0x1120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 231 | `?_Reset@?$_SpinWait@$00@details@Concurrency@@IEAAXXZ` | `0x1130` | 51 | UnwindData |  |
| 241 | `?_SetSpinCount@?$_SpinWait@$00@details@Concurrency@@QEAAXI@Z` | `0x1170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 243 | `?_ShouldSpinAgain@?$_SpinWait@$00@details@Concurrency@@IEAA_NXZ` | `0x1190` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 244 | `?_ShouldSpinAgain@?$_SpinWait@$0A@@details@Concurrency@@IEAA_NXZ` | `0x1190` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 245 | `?_SpinOnce@?$_SpinWait@$00@details@Concurrency@@QEAA_NXZ` | `0x11A0` | 187 | UnwindData |  |
| 95 | `??1critical_section@Concurrency@@QEAA@XZ` | `0x1260` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `??1reader_writer_lock@Concurrency@@QEAA@XZ` | `0x1260` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `??0_Runtime_object@details@Concurrency@@QEAA@H@Z` | `0x2160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `??0_Runtime_object@details@Concurrency@@QEAA@XZ` | `0x2180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `??0agent@Concurrency@@QEAA@AEAVScheduleGroup@1@@Z` | `0x21A0` | 129 | UnwindData |  |
| 28 | `??0agent@Concurrency@@QEAA@AEAVScheduler@1@@Z` | `0x2230` | 129 | UnwindData |  |
| 29 | `??0agent@Concurrency@@QEAA@XZ` | `0x22C0` | 120 | UnwindData |  |
| 94 | `??1agent@Concurrency@@UEAA@XZ` | `0x37E0` | 46 | UnwindData |  |
| 277 | `?status_port@agent@Concurrency@@QEAAPEAV?$ISource@W4agent_status@Concurrency@@@2@XZ` | `0x48F0` | 4,416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 259 | `?cancel@agent@Concurrency@@QEAA_NXZ` | `0x5A30` | 208 | UnwindData |  |
| 261 | `?done@agent@Concurrency@@IEAA_NXZ` | `0x5F10` | 243 | UnwindData |  |
| 275 | `?start@agent@Concurrency@@QEAA_NXZ` | `0x7F20` | 174 | UnwindData |  |
| 276 | `?status@agent@Concurrency@@QEAA?AW4agent_status@2@XZ` | `0x7FD0` | 2,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 286 | `?wait@agent@Concurrency@@SA?AW4agent_status@2@PEAV12@I@Z` | `0x8A80` | 175 | UnwindData |  |
| 289 | `?wait_for_all@agent@Concurrency@@SAX_KPEAPEAV12@PEAW4agent_status@2@I@Z` | `0x8B30` | 488 | UnwindData |  |
| 291 | `?wait_for_one@agent@Concurrency@@SAX_KPEAPEAV12@AEAW4agent_status@2@AEA_KI@Z` | `0x8D20` | 322 | UnwindData |  |
| 143 | `?NFS_Allocate@details@Concurrency@@YAPEAX_K0PEAX@Z` | `0x9430` | 95 | UnwindData |  |
| 144 | `?NFS_Free@details@Concurrency@@YAXPEAX@Z` | `0x9490` | 24 | UnwindData |  |
| 145 | `?NFS_GetLineSize@details@Concurrency@@YA_KXZ` | `0x94B0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 177 | `?_CheckTaskCollection@_UnrealizedChore@details@Concurrency@@IEAAXXZ` | `0x9650` | 108 | UnwindData |  |
| 184 | `?_Destroy@_AsyncTaskCollection@details@Concurrency@@EEAAXXZ` | `0x9820` | 31 | UnwindData |  |
| 7 | `??0_Concurrent_queue_base_v4@details@Concurrency@@IEAA@_K@Z` | `0xA120` | 145 | UnwindData |  |
| 8 | `??0_Concurrent_queue_iterator_base_v4@details@Concurrency@@IEAA@AEBV_Concurrent_queue_base_v4@12@@Z` | `0xA1C0` | 173 | UnwindData |  |
| 82 | `??1_Concurrent_queue_base_v4@details@Concurrency@@MEAA@XZ` | `0xA270` | 29 | UnwindData |  |
| 83 | `??1_Concurrent_queue_iterator_base_v4@details@Concurrency@@IEAA@XZ` | `0xA290` | 30 | UnwindData |  |
| 172 | `?_Advance@_Concurrent_queue_iterator_base_v4@details@Concurrency@@IEAAXXZ` | `0xA400` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 173 | `?_Assign@_Concurrent_queue_iterator_base_v4@details@Concurrency@@IEAAXAEBV123@@Z` | `0xA490` | 125 | UnwindData |  |
| 200 | `?_Internal_empty@_Concurrent_queue_base_v4@details@Concurrency@@IEBA_NXZ` | `0xA510` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | `?_Internal_finish_clear@_Concurrent_queue_base_v4@details@Concurrency@@IEAAXXZ` | `0xA540` | 107 | UnwindData |  |
| 204 | `?_Internal_move_push@_Concurrent_queue_base_v4@details@Concurrency@@IEAAXPEAX@Z` | `0xA5B0` | 67 | UnwindData |  |
| 205 | `?_Internal_pop_if_present@_Concurrent_queue_base_v4@details@Concurrency@@IEAA_NPEAX@Z` | `0xA600` | 119 | UnwindData |  |
| 206 | `?_Internal_push@_Concurrent_queue_base_v4@details@Concurrency@@IEAAXPEBX@Z` | `0xA680` | 67 | UnwindData |  |
| 210 | `?_Internal_size@_Concurrent_queue_base_v4@details@Concurrency@@IEBA_KXZ` | `0xA6D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 211 | `?_Internal_swap@_Concurrent_queue_base_v4@details@Concurrency@@IEAAXAEAV123@@Z` | `0xA6F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 213 | `?_Internal_throw_exception@_Concurrent_queue_base_v4@details@Concurrency@@IEBAXXZ` | `0xA710` | 32 | UnwindData |  |
| 84 | `??1_Concurrent_vector_base_v4@details@Concurrency@@IEAA@XZ` | `0xAA30` | 52 | UnwindData |  |
| 195 | `?_Internal_assign@_Concurrent_vector_base_v4@details@Concurrency@@IEAAXAEBV123@_KP6AXPEAX1@ZP6AX2PEBX1@Z5@Z` | `0xAA70` | 517 | UnwindData |  |
| 196 | `?_Internal_capacity@_Concurrent_vector_base_v4@details@Concurrency@@IEBA_KXZ` | `0xAC80` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 197 | `?_Internal_clear@_Concurrent_vector_base_v4@details@Concurrency@@IEAA_KP6AXPEAX_K@Z@Z` | `0xACC0` | 190 | UnwindData |  |
| 198 | `?_Internal_compact@_Concurrent_vector_base_v4@details@Concurrency@@IEAAPEAX_KPEAXP6AX10@ZP6AX1PEBX0@Z@Z` | `0xAD80` | 807 | UnwindData |  |
| 199 | `?_Internal_copy@_Concurrent_vector_base_v4@details@Concurrency@@IEAAXAEBV123@_KP6AXPEAXPEBX1@Z@Z` | `0xB0B0` | 280 | UnwindData |  |
| 202 | `?_Internal_grow_by@_Concurrent_vector_base_v4@details@Concurrency@@IEAA_K_K0P6AXPEAXPEBX0@Z2@Z` | `0xB290` | 57 | UnwindData |  |
| 203 | `?_Internal_grow_to_at_least_with_result@_Concurrent_vector_base_v4@details@Concurrency@@IEAA_K_K0P6AXPEAXPEBX0@Z2@Z` | `0xB3F0` | 290 | UnwindData |  |
| 207 | `?_Internal_push_back@_Concurrent_vector_base_v4@details@Concurrency@@IEAAPEAX_KAEA_K@Z` | `0xB520` | 237 | UnwindData |  |
| 208 | `?_Internal_reserve@_Concurrent_vector_base_v4@details@Concurrency@@IEAAX_K00@Z` | `0xB610` | 222 | UnwindData |  |
| 209 | `?_Internal_resize@_Concurrent_vector_base_v4@details@Concurrency@@IEAAX_K00P6AXPEAX0@ZP6AX1PEBX0@Z3@Z` | `0xB6F0` | 474 | UnwindData |  |
| 212 | `?_Internal_swap@_Concurrent_vector_base_v4@details@Concurrency@@IEAAXAEAV123@@Z` | `0xB8D0` | 217 | UnwindData |  |
| 214 | `?_Internal_throw_exception@_Concurrent_vector_base_v4@details@Concurrency@@IEBAX_K@Z` | `0xB9B0` | 65 | UnwindData |  |
| 240 | `?_Segment_index_of@_Concurrent_vector_base_v4@details@Concurrency@@KA_K_K@Z` | `0xBA00` | 20 | UnwindData |  |
| 112 | `?Block@Context@Concurrency@@SAXXZ` | `0xBC50` | 61 | UnwindData |  |
| 122 | `?CurrentContext@Context@Concurrency@@SAPEAV12@XZ` | `0xBC90` | 42 | UnwindData |  |
| 137 | `?Id@Context@Concurrency@@SAIXZ` | `0xBCC0` | 45 | UnwindData |  |
| 140 | `?IsCurrentTaskCollectionCanceling@Context@Concurrency@@SA_NXZ` | `0xBCF0` | 85 | UnwindData |  |
| 146 | `?Oversubscribe@Context@Concurrency@@SAX_N@Z` | `0xBD50` | 68 | UnwindData |  |
| 221 | `?_Oversubscribe@_Context@details@Concurrency@@SAX_N@Z` | `0xBD50` | 68 | UnwindData |  |
| 154 | `?ScheduleGroupId@Context@Concurrency@@SAIXZ` | `0xBDA0` | 46 | UnwindData |  |
| 162 | `?VirtualProcessorId@Context@Concurrency@@SAIXZ` | `0xBDD0` | 46 | UnwindData |  |
| 163 | `?Yield@Context@Concurrency@@SAXXZ` | `0xBE00` | 61 | UnwindData |  |
| 258 | `?_Yield@_Context@details@Concurrency@@SAXXZ` | `0xBE00` | 61 | UnwindData |  |
| 182 | `?_CurrentContext@_Context@details@Concurrency@@SA?AV123@XZ` | `0xBE40` | 54 | UnwindData |  |
| 217 | `?_IsSynchronouslyBlocked@_Context@details@Concurrency@@QEBA_NXZ` | `0xBE80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `?_Reference@_Scheduler@details@Concurrency@@QEAAIXZ` | `0xBE80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 247 | `?_SpinYield@Context@Concurrency@@SAXXZ` | `0xBEA0` | 61 | UnwindData |  |
| 6 | `??0_Cancellation_beacon@details@Concurrency@@QEAA@XZ` | `0xC030` | 62 | UnwindData |  |
| 81 | `??1_Cancellation_beacon@details@Concurrency@@QEAA@XZ` | `0xC1D0` | 48 | UnwindData |  |
| 124 | `?DisableTracing@Concurrency@@YAJXZ` | `0xCAD0` | 6,480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `?EnableTracing@Concurrency@@YAJXZ` | `0xCAD0` | 6,480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `?GetSharedTimerQueue@details@Concurrency@@YAPEAXXZ` | `0xCAD0` | 6,480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `?_Confirm_cancel@_Cancellation_beacon@details@Concurrency@@QEAA_NXZ` | `0xE420` | 77 | UnwindData |  |
| 186 | `?_DoYield@?$_SpinWait@$0A@@details@Concurrency@@IEAAXXZ` | `0xE470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 191 | `?_GetCurrentInlineDepth@_StackGuard@details@Concurrency@@CAAEA_KXZ` | `0xE480` | 46 | UnwindData |  |
| 232 | `?_Reset@?$_SpinWait@$0A@@details@Concurrency@@IEAAXXZ` | `0xE4B0` | 55 | UnwindData |  |
| 242 | `?_SetSpinCount@?$_SpinWait@$0A@@details@Concurrency@@QEAAXI@Z` | `0xE4F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 246 | `?_SpinOnce@?$_SpinWait@$0A@@details@Concurrency@@QEAA_NXZ` | `0xE510` | 173 | UnwindData |  |
| 117 | `?Create@CurrentScheduler@Concurrency@@SAXAEBVSchedulerPolicy@2@@Z` | `0xE600` | 33 | UnwindData |  |
| 120 | `?CreateScheduleGroup@CurrentScheduler@Concurrency@@SAPEAVScheduleGroup@2@AEAVlocation@2@@Z` | `0xE630` | 39 | UnwindData |  |
| 121 | `?CreateScheduleGroup@CurrentScheduler@Concurrency@@SAPEAVScheduleGroup@2@XZ` | `0xE660` | 33 | UnwindData |  |
| 123 | `?Detach@CurrentScheduler@Concurrency@@SAXXZ` | `0xE690` | 54 | UnwindData |  |
| 127 | `?Get@CurrentScheduler@Concurrency@@SAPEAVScheduler@2@XZ` | `0xE6D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `?GetNumberOfVirtualProcessors@CurrentScheduler@Concurrency@@SAIXZ` | `0xE6E0` | 46 | UnwindData |  |
| 131 | `?GetPolicy@CurrentScheduler@Concurrency@@SA?AVSchedulerPolicy@2@XZ` | `0xE710` | 42 | UnwindData |  |
| 138 | `?Id@CurrentScheduler@Concurrency@@SAIXZ` | `0xE740` | 46 | UnwindData |  |
| 139 | `?IsAvailableLocation@CurrentScheduler@Concurrency@@SA_NAEBVlocation@2@@Z` | `0xE770` | 46 | UnwindData |  |
| 150 | `?RegisterShutdownEvent@CurrentScheduler@Concurrency@@SAXPEAX@Z` | `0xE7A0` | 72 | UnwindData |  |
| 155 | `?ScheduleTask@CurrentScheduler@Concurrency@@SAXP6AXPEAX@Z0@Z` | `0xE7F0` | 54 | UnwindData |  |
| 239 | `?_ScheduleTask@_CurrentScheduler@details@Concurrency@@SAXP6AXPEAX@Z0@Z` | `0xE7F0` | 54 | UnwindData |  |
| 156 | `?ScheduleTask@CurrentScheduler@Concurrency@@SAXP6AXPEAX@Z0AEAVlocation@2@@Z` | `0xE830` | 70 | UnwindData |  |
| 187 | `?_Get@_CurrentScheduler@details@Concurrency@@SA?AV_Scheduler@23@XZ` | `0xE880` | 26 | UnwindData |  |
| 192 | `?_GetNumberOfVirtualProcessors@_CurrentScheduler@details@Concurrency@@SAIXZ` | `0xE8A0` | 33 | UnwindData |  |
| 194 | `?_Id@_CurrentScheduler@details@Concurrency@@SAIXZ` | `0xE8D0` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `??0_Condition_variable@details@Concurrency@@QEAA@XZ` | `0xEAF0` | 34 | UnwindData |  |
| 39 | `??0event@Concurrency@@QEAA@XZ` | `0xEB20` | 42 | UnwindData |  |
| 85 | `??1_Condition_variable@details@Concurrency@@QEAA@XZ` | `0xEBC0` | 49 | UnwindData |  |
| 96 | `??1event@Concurrency@@QEAA@XZ` | `0xEC00` | 160 | UnwindData |  |
| 269 | `?notify_all@_Condition_variable@details@Concurrency@@QEAAXXZ` | `0xF300` | 151 | UnwindData |  |
| 270 | `?notify_one@_Condition_variable@details@Concurrency@@QEAAXXZ` | `0xF3A0` | 183 | UnwindData |  |
| 271 | `?reset@event@Concurrency@@QEAAXXZ` | `0xF460` | 133 | UnwindData |  |
| 272 | `?set@event@Concurrency@@QEAAXXZ` | `0xF4F0` | 473 | UnwindData |  |
| 285 | `?wait@_Condition_variable@details@Concurrency@@QEAAXAEAVcritical_section@3@@Z` | `0xF6D0` | 118 | UnwindData |  |
| 287 | `?wait@event@Concurrency@@QEAA_KI@Z` | `0xF750` | 300 | UnwindData |  |
| 288 | `?wait_for@_Condition_variable@details@Concurrency@@QEAA_NAEAVcritical_section@3@I@Z` | `0xF880` | 280 | UnwindData |  |
| 290 | `?wait_for_multiple@event@Concurrency@@SA_KPEAPEAV12@_K_NI@Z` | `0xF9A0` | 809 | UnwindData |  |
| 30 | `??0bad_target@Concurrency@@QEAA@PEBD@Z` | `0xFCD0` | 71 | UnwindData |  |
| 31 | `??0bad_target@Concurrency@@QEAA@XZ` | `0xFD20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `??0context_self_unblock@Concurrency@@QEAA@PEBD@Z` | `0xFD40` | 71 | UnwindData |  |
| 33 | `??0context_self_unblock@Concurrency@@QEAA@XZ` | `0xFD90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `??0context_unblock_unbalanced@Concurrency@@QEAA@PEBD@Z` | `0xFDB0` | 71 | UnwindData |  |
| 35 | `??0context_unblock_unbalanced@Concurrency@@QEAA@XZ` | `0xFE00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `??0default_scheduler_exists@Concurrency@@QEAA@PEBD@Z` | `0xFE20` | 71 | UnwindData |  |
| 38 | `??0default_scheduler_exists@Concurrency@@QEAA@XZ` | `0xFE70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `??0improper_lock@Concurrency@@QEAA@PEBD@Z` | `0xFE90` | 71 | UnwindData |  |
| 41 | `??0improper_lock@Concurrency@@QEAA@XZ` | `0xFEE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `??0improper_scheduler_attach@Concurrency@@QEAA@PEBD@Z` | `0xFF00` | 71 | UnwindData |  |
| 43 | `??0improper_scheduler_attach@Concurrency@@QEAA@XZ` | `0xFF50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `??0improper_scheduler_detach@Concurrency@@QEAA@PEBD@Z` | `0xFF70` | 71 | UnwindData |  |
| 45 | `??0improper_scheduler_detach@Concurrency@@QEAA@XZ` | `0xFFC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `??0improper_scheduler_reference@Concurrency@@QEAA@PEBD@Z` | `0xFFE0` | 71 | UnwindData |  |
| 47 | `??0improper_scheduler_reference@Concurrency@@QEAA@XZ` | `0x10030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `??0invalid_link_target@Concurrency@@QEAA@PEBD@Z` | `0x10050` | 71 | UnwindData |  |
| 49 | `??0invalid_link_target@Concurrency@@QEAA@XZ` | `0x100A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `??0invalid_multiple_scheduling@Concurrency@@QEAA@PEBD@Z` | `0x100C0` | 71 | UnwindData |  |
| 51 | `??0invalid_multiple_scheduling@Concurrency@@QEAA@XZ` | `0x10110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `??0invalid_oversubscribe_operation@Concurrency@@QEAA@PEBD@Z` | `0x10130` | 71 | UnwindData |  |
| 53 | `??0invalid_oversubscribe_operation@Concurrency@@QEAA@XZ` | `0x10180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `??0invalid_scheduler_policy_key@Concurrency@@QEAA@PEBD@Z` | `0x101A0` | 71 | UnwindData |  |
| 55 | `??0invalid_scheduler_policy_key@Concurrency@@QEAA@XZ` | `0x101F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `??0invalid_scheduler_policy_thread_specification@Concurrency@@QEAA@PEBD@Z` | `0x10210` | 71 | UnwindData |  |
| 57 | `??0invalid_scheduler_policy_thread_specification@Concurrency@@QEAA@XZ` | `0x10260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `??0invalid_scheduler_policy_value@Concurrency@@QEAA@PEBD@Z` | `0x10280` | 71 | UnwindData |  |
| 59 | `??0invalid_scheduler_policy_value@Concurrency@@QEAA@XZ` | `0x102D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `??0message_not_found@Concurrency@@QEAA@PEBD@Z` | `0x102F0` | 71 | UnwindData |  |
| 61 | `??0message_not_found@Concurrency@@QEAA@XZ` | `0x10340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `??0missing_wait@Concurrency@@QEAA@PEBD@Z` | `0x10360` | 71 | UnwindData |  |
| 63 | `??0missing_wait@Concurrency@@QEAA@XZ` | `0x103B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `??0nested_scheduler_missing_detach@Concurrency@@QEAA@PEBD@Z` | `0x103D0` | 71 | UnwindData |  |
| 65 | `??0nested_scheduler_missing_detach@Concurrency@@QEAA@XZ` | `0x10420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `??0operation_timed_out@Concurrency@@QEAA@PEBD@Z` | `0x10440` | 71 | UnwindData |  |
| 67 | `??0operation_timed_out@Concurrency@@QEAA@XZ` | `0x10490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `??0scheduler_not_attached@Concurrency@@QEAA@PEBD@Z` | `0x104B0` | 71 | UnwindData |  |
| 70 | `??0scheduler_not_attached@Concurrency@@QEAA@XZ` | `0x10500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `??0scheduler_resource_allocation_error@Concurrency@@QEAA@J@Z` | `0x10520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `??0scheduler_resource_allocation_error@Concurrency@@QEAA@PEBDJ@Z` | `0x10540` | 86 | UnwindData |  |
| 73 | `??0scheduler_worker_creation_error@Concurrency@@QEAA@J@Z` | `0x105A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `??0scheduler_worker_creation_error@Concurrency@@QEAA@PEBDJ@Z` | `0x105C0` | 33 | UnwindData |  |
| 78 | `??0unsupported_os@Concurrency@@QEAA@PEBD@Z` | `0x105F0` | 71 | UnwindData |  |
| 79 | `??0unsupported_os@Concurrency@@QEAA@XZ` | `0x10640` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 263 | `?get_error_code@scheduler_resource_allocation_error@Concurrency@@QEBAJXZ` | `0x106B0` | 12,624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `?_Current_node@location@Concurrency@@SA?AV12@XZ` | `0x13800` | 163 | UnwindData |  |
| 260 | `?current@location@Concurrency@@SA?AV12@XZ` | `0x13990` | 166 | UnwindData |  |
| 262 | `?from_numa_node@location@Concurrency@@SA?AV12@G@Z` | `0x13A40` | 87 | UnwindData |  |
| 188 | `?_GetCombinableSize@details@Concurrency@@YA_KXZ` | `0x144A0` | 68 | UnwindData |  |
| 264 | `?is_current_task_group_canceling@Concurrency@@YA_NXZ` | `0x144F0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `??0_NonReentrantBlockingLock@details@Concurrency@@QEAA@XZ` | `0x145A0` | 45 | UnwindData |  |
| 14 | `??0_ReentrantBlockingLock@details@Concurrency@@QEAA@XZ` | `0x145A0` | 45 | UnwindData |  |
| 12 | `??0_NonReentrantPPLLock@details@Concurrency@@QEAA@XZ` | `0x145D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `??0critical_section@Concurrency@@QEAA@XZ` | `0x145D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `??0_ReaderWriterLock@details@Concurrency@@QEAA@XZ` | `0x14610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `??0_ReentrantLock@details@Concurrency@@QEAA@XZ` | `0x14630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `??0_ReentrantPPLLock@details@Concurrency@@QEAA@XZ` | `0x14650` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `??0_Scoped_lock@_NonReentrantPPLLock@details@Concurrency@@QEAA@AEAV123@@Z` | `0x14690` | 119 | UnwindData |  |
| 21 | `??0_Scoped_lock@_ReentrantPPLLock@details@Concurrency@@QEAA@AEAV123@@Z` | `0x14710` | 116 | UnwindData |  |
| 68 | `??0reader_writer_lock@Concurrency@@QEAA@XZ` | `0x147C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `??0scoped_lock@critical_section@Concurrency@@QEAA@AEAV12@@Z` | `0x14800` | 121 | UnwindData |  |
| 76 | `??0scoped_lock@reader_writer_lock@Concurrency@@QEAA@AEAV12@@Z` | `0x14880` | 121 | UnwindData |  |
| 77 | `??0scoped_lock_read@reader_writer_lock@Concurrency@@QEAA@AEAV12@@Z` | `0x14900` | 29 | UnwindData |  |
| 86 | `??1_NonReentrantBlockingLock@details@Concurrency@@QEAA@XZ` | `0x14920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `??1_ReentrantBlockingLock@details@Concurrency@@QEAA@XZ` | `0x14920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `??1_Scoped_lock@_NonReentrantPPLLock@details@Concurrency@@QEAA@XZ` | `0x14930` | 18 | UnwindData |  |
| 98 | `??1scoped_lock@critical_section@Concurrency@@QEAA@XZ` | `0x14930` | 18 | UnwindData |  |
| 89 | `??1_Scoped_lock@_ReentrantPPLLock@details@Concurrency@@QEAA@XZ` | `0x14950` | 31 | UnwindData |  |
| 99 | `??1scoped_lock@reader_writer_lock@Concurrency@@QEAA@XZ` | `0x14970` | 18 | UnwindData |  |
| 100 | `??1scoped_lock_read@reader_writer_lock@Concurrency@@QEAA@XZ` | `0x14970` | 18 | UnwindData |  |
| 165 | `?_Acquire@_NonReentrantBlockingLock@details@Concurrency@@QEAAXXZ` | `0x14AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 167 | `?_Acquire@_ReentrantBlockingLock@details@Concurrency@@QEAAXXZ` | `0x14AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `?_Acquire@_NonReentrantPPLLock@details@Concurrency@@QEAAXPEAX@Z` | `0x14AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `?_Acquire@_ReentrantLock@details@Concurrency@@QEAAXXZ` | `0x14AD0` | 91 | UnwindData |  |
| 169 | `?_Acquire@_ReentrantPPLLock@details@Concurrency@@QEAAXPEAX@Z` | `0x14B30` | 83 | UnwindData |  |
| 170 | `?_AcquireRead@_ReaderWriterLock@details@Concurrency@@QEAAXXZ` | `0x14B90` | 52 | UnwindData |  |
| 171 | `?_AcquireWrite@_ReaderWriterLock@details@Concurrency@@QEAAXXZ` | `0x14BD0` | 60 | UnwindData |  |
| 223 | `?_Release@_NonReentrantBlockingLock@details@Concurrency@@QEAAXXZ` | `0x15010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 225 | `?_Release@_ReentrantBlockingLock@details@Concurrency@@QEAAXXZ` | `0x15010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 224 | `?_Release@_NonReentrantPPLLock@details@Concurrency@@QEAAXXZ` | `0x15020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 226 | `?_Release@_ReentrantLock@details@Concurrency@@QEAAXXZ` | `0x15030` | 49 | UnwindData |  |
| 227 | `?_Release@_ReentrantPPLLock@details@Concurrency@@QEAAXXZ` | `0x15070` | 27 | UnwindData |  |
| 229 | `?_ReleaseRead@_ReaderWriterLock@details@Concurrency@@QEAAXXZ` | `0x15090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 230 | `?_ReleaseWrite@_ReaderWriterLock@details@Concurrency@@QEAAXXZ` | `0x150A0` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 252 | `?_TryAcquire@_NonReentrantBlockingLock@details@Concurrency@@QEAA_NXZ` | `0x152B0` | 20 | UnwindData |  |
| 253 | `?_TryAcquire@_ReentrantBlockingLock@details@Concurrency@@QEAA_NXZ` | `0x152B0` | 20 | UnwindData |  |
| 254 | `?_TryAcquire@_ReentrantLock@details@Concurrency@@QEAA_NXZ` | `0x152D0` | 45 | UnwindData |  |
| 255 | `?_TryAcquireWrite@_ReaderWriterLock@details@Concurrency@@QEAA_NXZ` | `0x15300` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 257 | `?_Value@_SpinCount@details@Concurrency@@SAIXZ` | `0x15420` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 265 | `?lock@critical_section@Concurrency@@QEAAXXZ` | `0x154A0` | 121 | UnwindData |  |
| 266 | `?lock@reader_writer_lock@Concurrency@@QEAAXXZ` | `0x15520` | 121 | UnwindData |  |
| 267 | `?lock_read@reader_writer_lock@Concurrency@@QEAAXXZ` | `0x155A0` | 397 | UnwindData |  |
| 268 | `?native_handle@critical_section@Concurrency@@QEAAAEAV12@XZ` | `0x15730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 278 | `?try_lock@critical_section@Concurrency@@QEAA_NXZ` | `0x15740` | 235 | UnwindData |  |
| 279 | `?try_lock@reader_writer_lock@Concurrency@@QEAA_NXZ` | `0x15830` | 265 | UnwindData |  |
| 280 | `?try_lock_for@critical_section@Concurrency@@QEAA_NI@Z` | `0x15940` | 180 | UnwindData |  |
| 281 | `?try_lock_read@reader_writer_lock@Concurrency@@QEAA_NXZ` | `0x15A00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 282 | `?unlock@critical_section@Concurrency@@QEAAXXZ` | `0x15A20` | 289 | UnwindData |  |
| 283 | `?unlock@reader_writer_lock@Concurrency@@QEAAXXZ` | `0x15B50` | 38 | UnwindData |  |
| 119 | `?CreateResourceManager@Concurrency@@YAPEAUIResourceManager@1@XZ` | `0x163C0` | 5,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `?GetExecutionContextId@Concurrency@@YAIXZ` | `0x17A90` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | `?GetOSVersion@Concurrency@@YA?AW4OSVersion@IResourceManager@1@XZ` | `0x17C10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `?GetProcessorCount@Concurrency@@YAIXZ` | `0x17C20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `?_GetConcurrency@details@Concurrency@@YAIXZ` | `0x17C20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `?GetProcessorNodeCount@Concurrency@@YAIXZ` | `0x17C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `?GetSchedulerId@Concurrency@@YAIXZ` | `0x17C40` | 10,304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 273 | `?set_task_execution_resources@Concurrency@@YAXGPEAU_GROUP_AFFINITY@@@Z` | `0x1A480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 274 | `?set_task_execution_resources@Concurrency@@YAX_K@Z` | `0x1A490` | 12,640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `?Create@Scheduler@Concurrency@@SAPEAV12@AEBVSchedulerPolicy@2@@Z` | `0x1D5F0` | 47 | UnwindData |  |
| 151 | `?ResetDefaultSchedulerPolicy@Scheduler@Concurrency@@SAXXZ` | `0x20060` | 784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `?SetDefaultSchedulerPolicy@Scheduler@Concurrency@@SAXAEBVSchedulerPolicy@2@@Z` | `0x20370` | 3,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 228 | `?_Release@_Scheduler@details@Concurrency@@QEAAIXZ` | `0x20F80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0SchedulerPolicy@Concurrency@@QEAA@AEBV01@@Z` | `0x20FA0` | 70 | UnwindData |  |
| 4 | `??0SchedulerPolicy@Concurrency@@QEAA@XZ` | `0x20FF0` | 28 | UnwindData |  |
| 5 | `??0SchedulerPolicy@Concurrency@@QEAA@_KZZ` | `0x21010` | 49 | UnwindData |  |
| 80 | `??1SchedulerPolicy@Concurrency@@QEAA@XZ` | `0x21100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `??4SchedulerPolicy@Concurrency@@QEAAAEAV01@AEBV01@@Z` | `0x21110` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `?GetPolicyValue@SchedulerPolicy@Concurrency@@QEBAIW4PolicyElementKey@2@@Z` | `0x21140` | 64 | UnwindData |  |
| 158 | `?SetConcurrencyLimits@SchedulerPolicy@Concurrency@@QEAAXII@Z` | `0x21180` | 187 | UnwindData |  |
| 160 | `?SetPolicyValue@SchedulerPolicy@Concurrency@@QEAAIW4PolicyElementKey@2@I@Z` | `0x21240` | 181 | UnwindData |  |
| 111 | `?Alloc@Concurrency@@YAPEAX_K@Z` | `0x25810` | 113 | UnwindData |  |
| 126 | `?Free@Concurrency@@YAXPEAX@Z` | `0x25930` | 74 | UnwindData |  |
| 23 | `??0_StructuredTaskCollection@details@Concurrency@@QEAA@PEAV_CancellationTokenState@12@@Z` | `0x25AD0` | 188 | UnwindData |  |
| 24 | `??0_TaskCollection@details@Concurrency@@QEAA@PEAV_CancellationTokenState@12@@Z` | `0x25D10` | 277 | UnwindData |  |
| 25 | `??0_TaskCollection@details@Concurrency@@QEAA@XZ` | `0x25E30` | 252 | UnwindData |  |
| 91 | `??1_StructuredTaskCollection@details@Concurrency@@QEAA@XZ` | `0x25FB0` | 114 | UnwindData |  |
| 92 | `??1_TaskCollection@details@Concurrency@@QEAA@XZ` | `0x26030` | 269 | UnwindData |  |
| 164 | `?_Abort@_StructuredTaskCollection@details@Concurrency@@AEAAXXZ` | `0x264C0` | 251 | UnwindData |  |
| 175 | `?_Cancel@_StructuredTaskCollection@details@Concurrency@@QEAAXXZ` | `0x268C0` | 135 | UnwindData |  |
| 176 | `?_Cancel@_TaskCollection@details@Concurrency@@QEAAXXZ` | `0x26A30` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 178 | `?_CleanupToken@_StructuredTaskCollection@details@Concurrency@@AEAAXXZ` | `0x26C10` | 108 | UnwindData |  |
| 215 | `?_IsCanceling@_StructuredTaskCollection@details@Concurrency@@QEAA_NXZ` | `0x26EE0` | 188 | UnwindData |  |
| 216 | `?_IsCanceling@_TaskCollection@details@Concurrency@@QEAA_NXZ` | `0x26FA0` | 247 | UnwindData |  |
| 218 | `?_NewCollection@_AsyncTaskCollection@details@Concurrency@@SAPEAV123@PEAV_CancellationTokenState@23@@Z` | `0x270C0` | 49 | UnwindData |  |
| 233 | `?_RunAndWait@_StructuredTaskCollection@details@Concurrency@@QEAA?AW4_TaskCollectionStatus@23@PEAV_UnrealizedChore@23@@Z` | `0x27390` | 824 | UnwindData |  |
| 234 | `?_RunAndWait@_TaskCollection@details@Concurrency@@QEAA?AW4_TaskCollectionStatus@23@PEAV_UnrealizedChore@23@@Z` | `0x276D0` | 1,272 | UnwindData |  |
| 235 | `?_Schedule@_StructuredTaskCollection@details@Concurrency@@QEAAXPEAV_UnrealizedChore@23@@Z` | `0x27BD0` | 136 | UnwindData |  |
| 236 | `?_Schedule@_StructuredTaskCollection@details@Concurrency@@QEAAXPEAV_UnrealizedChore@23@PEAVlocation@3@@Z` | `0x27C60` | 152 | UnwindData |  |
| 237 | `?_Schedule@_TaskCollection@details@Concurrency@@QEAAXPEAV_UnrealizedChore@23@@Z` | `0x27D00` | 256 | UnwindData |  |
| 238 | `?_Schedule@_TaskCollection@details@Concurrency@@QEAAXPEAV_UnrealizedChore@23@PEAVlocation@3@@Z` | `0x27E00` | 262 | UnwindData |  |
| 26 | `??0_Timer@details@Concurrency@@IEAA@I_N@Z` | `0x28ED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `??1_Timer@details@Concurrency@@MEAA@XZ` | `0x28EF0` | 47 | UnwindData |  |
| 248 | `?_Start@_Timer@details@Concurrency@@IEAAXXZ` | `0x29020` | 81 | UnwindData |  |
| 249 | `?_Stop@_Timer@details@Concurrency@@IEAAXXZ` | `0x29080` | 32 | UnwindData |  |
| 284 | `?wait@Concurrency@@YAXI@Z` | `0x290A0` | 107 | UnwindData |  |
| 189 | `?_GetConcRTTraceInfo@Concurrency@@YAPEBU_CONCRT_TRACE_INFO@details@1@XZ` | `0x295B0` | 31 | UnwindData |  |
| 250 | `?_Trace_agents@Concurrency@@YAXW4Agents_EventType@1@_JZZ` | `0x296A0` | 261 | UnwindData |  |
| 251 | `?_Trace_ppl_function@Concurrency@@YAXAEBU_GUID@@EW4ConcRT_EventType@1@@Z` | `0x297B0` | 87 | UnwindData |  |
| 22 | `??0_SpinLock@details@Concurrency@@QEAA@AECJ@Z` | `0x2B180` | 87 | UnwindData |  |
| 90 | `??1_SpinLock@details@Concurrency@@QEAA@XZ` | `0x2B1E0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `?Log2@details@Concurrency@@YAK_K@Z` | `0x2B330` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `?_ConcRT_CoreAssert@details@Concurrency@@YAXPEBD0H@Z` | `0x2B5A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 180 | `?_ConcRT_Trace@details@Concurrency@@YAXHPEB_WZZ` | `0x2B5B0` | 190 | UnwindData |  |
| 256 | `?_UnderlyingYield@details@Concurrency@@YAXXZ` | `0x2B6C0` | 47 | UnwindData |  |
| 174 | `?_Byte_reverse_table@details@Concurrency@@3QBEB` | `0x30930` | 5,440 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `?ConcRT_ProviderGuid@Concurrency@@3U_GUID@@B` | `0x31E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `?ConcRTEventGuid@Concurrency@@3U_GUID@@B` | `0x31E80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `?SchedulerEventGuid@Concurrency@@3U_GUID@@B` | `0x31E90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `?ScheduleGroupEventGuid@Concurrency@@3U_GUID@@B` | `0x31EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `?ContextEventGuid@Concurrency@@3U_GUID@@B` | `0x31EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `?ChoreEventGuid@Concurrency@@3U_GUID@@B` | `0x31EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 161 | `?VirtualProcessorEventGuid@Concurrency@@3U_GUID@@B` | `0x31ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `?LockEventGuid@Concurrency@@3U_GUID@@B` | `0x31EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `?ResourceManagerEventGuid@Concurrency@@3U_GUID@@B` | `0x31EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `?PPLParallelInvokeEventGuid@Concurrency@@3U_GUID@@B` | `0x31F00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `?PPLParallelForEventGuid@Concurrency@@3U_GUID@@B` | `0x31F10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 148 | `?PPLParallelForeachEventGuid@Concurrency@@3U_GUID@@B` | `0x31F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `?AgentEventGuid@Concurrency@@3U_GUID@@B` | `0x31F30` | 0 | Indeterminate |  |
