# Binary Specification: concrt140.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\concrt140.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `54716f0738af891f283d213b5c8d11b25896bb8ee3097d301eae718560cf974e`
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
| 231 | `?_Reset@?$_SpinWait@$00@details@Concurrency@@IEAAXXZ` | `0x1130` | 60 | UnwindData |  |
| 241 | `?_SetSpinCount@?$_SpinWait@$00@details@Concurrency@@QEAAXI@Z` | `0x1170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 243 | `?_ShouldSpinAgain@?$_SpinWait@$00@details@Concurrency@@IEAA_NXZ` | `0x1190` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 244 | `?_ShouldSpinAgain@?$_SpinWait@$0A@@details@Concurrency@@IEAA_NXZ` | `0x1190` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 245 | `?_SpinOnce@?$_SpinWait@$00@details@Concurrency@@QEAA_NXZ` | `0x11A0` | 255 | UnwindData |  |
| 95 | `??1critical_section@Concurrency@@QEAA@XZ` | `0x12A0` | 6,544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `??1reader_writer_lock@Concurrency@@QEAA@XZ` | `0x12A0` | 6,544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `??0_Runtime_object@details@Concurrency@@QEAA@H@Z` | `0x2C30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `??0_Runtime_object@details@Concurrency@@QEAA@XZ` | `0x2C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `??0agent@Concurrency@@QEAA@AEAVScheduleGroup@1@@Z` | `0x2C70` | 132 | UnwindData |  |
| 28 | `??0agent@Concurrency@@QEAA@AEAVScheduler@1@@Z` | `0x2D00` | 126 | UnwindData |  |
| 29 | `??0agent@Concurrency@@QEAA@XZ` | `0x2D80` | 123 | UnwindData |  |
| 94 | `??1agent@Concurrency@@UEAA@XZ` | `0x48D0` | 46 | UnwindData |  |
| 277 | `?status_port@agent@Concurrency@@QEAAPEAV?$ISource@W4agent_status@Concurrency@@@2@XZ` | `0x5B00` | 2,960 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 259 | `?cancel@agent@Concurrency@@QEAA_NXZ` | `0x6690` | 202 | UnwindData |  |
| 261 | `?done@agent@Concurrency@@IEAA_NXZ` | `0x6BD0` | 244 | UnwindData |  |
| 275 | `?start@agent@Concurrency@@QEAA_NXZ` | `0x8DE0` | 211 | UnwindData |  |
| 276 | `?status@agent@Concurrency@@QEAA?AW4agent_status@2@XZ` | `0x8EC0` | 3,136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 286 | `?wait@agent@Concurrency@@SA?AW4agent_status@2@PEAV12@I@Z` | `0x9B00` | 178 | UnwindData |  |
| 289 | `?wait_for_all@agent@Concurrency@@SAX_KPEAPEAV12@PEAW4agent_status@2@I@Z` | `0x9BC0` | 688 | UnwindData |  |
| 291 | `?wait_for_one@agent@Concurrency@@SAX_KPEAPEAV12@AEAW4agent_status@2@AEA_KI@Z` | `0x9E70` | 410 | UnwindData |  |
| 143 | `?NFS_Allocate@details@Concurrency@@YAPEAX_K0PEAX@Z` | `0xAA00` | 95 | UnwindData |  |
| 144 | `?NFS_Free@details@Concurrency@@YAXPEAX@Z` | `0xAA60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `?NFS_GetLineSize@details@Concurrency@@YA_KXZ` | `0xAA80` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 177 | `?_CheckTaskCollection@_UnrealizedChore@details@Concurrency@@IEAAXXZ` | `0xABD0` | 103 | UnwindData |  |
| 184 | `?_Destroy@_AsyncTaskCollection@details@Concurrency@@EEAAXXZ` | `0xADD0` | 2,576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `??0_Concurrent_queue_base_v4@details@Concurrency@@IEAA@_K@Z` | `0xB7E0` | 153 | UnwindData |  |
| 8 | `??0_Concurrent_queue_iterator_base_v4@details@Concurrency@@IEAA@AEBV_Concurrent_queue_base_v4@12@@Z` | `0xB880` | 196 | UnwindData |  |
| 82 | `??1_Concurrent_queue_base_v4@details@Concurrency@@MEAA@XZ` | `0xB950` | 29 | UnwindData |  |
| 83 | `??1_Concurrent_queue_iterator_base_v4@details@Concurrency@@IEAA@XZ` | `0xB970` | 30 | UnwindData |  |
| 172 | `?_Advance@_Concurrent_queue_iterator_base_v4@details@Concurrency@@IEAAXXZ` | `0xBB00` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 173 | `?_Assign@_Concurrent_queue_iterator_base_v4@details@Concurrency@@IEAAXAEBV123@@Z` | `0xBBA0` | 147 | UnwindData |  |
| 200 | `?_Internal_empty@_Concurrent_queue_base_v4@details@Concurrency@@IEBA_NXZ` | `0xBC40` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | `?_Internal_finish_clear@_Concurrent_queue_base_v4@details@Concurrency@@IEAAXXZ` | `0xBC70` | 100 | UnwindData |  |
| 204 | `?_Internal_move_push@_Concurrent_queue_base_v4@details@Concurrency@@IEAAXPEAX@Z` | `0xBCE0` | 67 | UnwindData |  |
| 205 | `?_Internal_pop_if_present@_Concurrent_queue_base_v4@details@Concurrency@@IEAA_NPEAX@Z` | `0xBD30` | 134 | UnwindData |  |
| 206 | `?_Internal_push@_Concurrent_queue_base_v4@details@Concurrency@@IEAAXPEBX@Z` | `0xBDC0` | 67 | UnwindData |  |
| 210 | `?_Internal_size@_Concurrent_queue_base_v4@details@Concurrency@@IEBA_KXZ` | `0xBE10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 211 | `?_Internal_swap@_Concurrent_queue_base_v4@details@Concurrency@@IEAAXAEAV123@@Z` | `0xBE30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 213 | `?_Internal_throw_exception@_Concurrent_queue_base_v4@details@Concurrency@@IEBAXXZ` | `0xBE50` | 32 | UnwindData |  |
| 84 | `??1_Concurrent_vector_base_v4@details@Concurrency@@IEAA@XZ` | `0xC540` | 53 | UnwindData |  |
| 195 | `?_Internal_assign@_Concurrent_vector_base_v4@details@Concurrency@@IEAAXAEBV123@_KP6AXPEAX1@ZP6AX2PEBX1@Z5@Z` | `0xC580` | 186 | UnwindData |  |
| 196 | `?_Internal_capacity@_Concurrent_vector_base_v4@details@Concurrency@@IEBA_KXZ` | `0xC920` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 197 | `?_Internal_clear@_Concurrent_vector_base_v4@details@Concurrency@@IEAA_KP6AXPEAX_K@Z@Z` | `0xC960` | 84 | UnwindData |  |
| 198 | `?_Internal_compact@_Concurrent_vector_base_v4@details@Concurrency@@IEAAPEAX_KPEAXP6AX10@ZP6AX1PEBX0@Z@Z` | `0xCA20` | 266 | UnwindData |  |
| 199 | `?_Internal_copy@_Concurrent_vector_base_v4@details@Concurrency@@IEAAXAEBV123@_KP6AXPEAXPEBX1@Z@Z` | `0xCE70` | 52 | UnwindData |  |
| 202 | `?_Internal_grow_by@_Concurrent_vector_base_v4@details@Concurrency@@IEAA_K_K0P6AXPEAXPEBX0@Z2@Z` | `0xD0C0` | 57 | UnwindData |  |
| 203 | `?_Internal_grow_to_at_least_with_result@_Concurrent_vector_base_v4@details@Concurrency@@IEAA_K_K0P6AXPEAXPEBX0@Z2@Z` | `0xD1E0` | 664 | UnwindData |  |
| 207 | `?_Internal_push_back@_Concurrent_vector_base_v4@details@Concurrency@@IEAAPEAX_KAEA_K@Z` | `0xD480` | 154 | UnwindData |  |
| 208 | `?_Internal_reserve@_Concurrent_vector_base_v4@details@Concurrency@@IEAAX_K00@Z` | `0xD520` | 621 | UnwindData |  |
| 209 | `?_Internal_resize@_Concurrent_vector_base_v4@details@Concurrency@@IEAAX_K00P6AXPEAX0@ZP6AX1PEBX0@Z3@Z` | `0xD790` | 485 | UnwindData |  |
| 212 | `?_Internal_swap@_Concurrent_vector_base_v4@details@Concurrency@@IEAAXAEAV123@@Z` | `0xD980` | 57 | UnwindData |  |
| 214 | `?_Internal_throw_exception@_Concurrent_vector_base_v4@details@Concurrency@@IEBAX_K@Z` | `0xDA90` | 65 | UnwindData |  |
| 240 | `?_Segment_index_of@_Concurrent_vector_base_v4@details@Concurrency@@KA_K_K@Z` | `0xDAE0` | 20 | UnwindData |  |
| 112 | `?Block@Context@Concurrency@@SAXXZ` | `0xDF20` | 61 | UnwindData |  |
| 122 | `?CurrentContext@Context@Concurrency@@SAPEAV12@XZ` | `0xDF60` | 46 | UnwindData |  |
| 137 | `?Id@Context@Concurrency@@SAIXZ` | `0xDF90` | 47 | UnwindData |  |
| 140 | `?IsCurrentTaskCollectionCanceling@Context@Concurrency@@SA_NXZ` | `0xDFC0` | 85 | UnwindData |  |
| 146 | `?Oversubscribe@Context@Concurrency@@SAX_N@Z` | `0xE020` | 70 | UnwindData |  |
| 221 | `?_Oversubscribe@_Context@details@Concurrency@@SAX_N@Z` | `0xE020` | 70 | UnwindData |  |
| 154 | `?ScheduleGroupId@Context@Concurrency@@SAIXZ` | `0xE070` | 48 | UnwindData |  |
| 162 | `?VirtualProcessorId@Context@Concurrency@@SAIXZ` | `0xE0A0` | 48 | UnwindData |  |
| 163 | `?Yield@Context@Concurrency@@SAXXZ` | `0xE0D0` | 61 | UnwindData |  |
| 258 | `?_Yield@_Context@details@Concurrency@@SAXXZ` | `0xE0D0` | 61 | UnwindData |  |
| 182 | `?_CurrentContext@_Context@details@Concurrency@@SA?AV123@XZ` | `0xE110` | 54 | UnwindData |  |
| 217 | `?_IsSynchronouslyBlocked@_Context@details@Concurrency@@QEBA_NXZ` | `0xE150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `?_Reference@_Scheduler@details@Concurrency@@QEAAIXZ` | `0xE150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 247 | `?_SpinYield@Context@Concurrency@@SAXXZ` | `0xE170` | 61 | UnwindData |  |
| 6 | `??0_Cancellation_beacon@details@Concurrency@@QEAA@XZ` | `0xE2F0` | 143 | UnwindData |  |
| 81 | `??1_Cancellation_beacon@details@Concurrency@@QEAA@XZ` | `0xE4B0` | 48 | UnwindData |  |
| 124 | `?DisableTracing@Concurrency@@YAJXZ` | `0xF330` | 6,752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `?EnableTracing@Concurrency@@YAJXZ` | `0xF330` | 6,752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `?GetSharedTimerQueue@details@Concurrency@@YAPEAXXZ` | `0xF330` | 6,752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `?_Confirm_cancel@_Cancellation_beacon@details@Concurrency@@QEAA_NXZ` | `0x10D90` | 77 | UnwindData |  |
| 186 | `?_DoYield@?$_SpinWait@$0A@@details@Concurrency@@IEAAXXZ` | `0x10DE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 191 | `?_GetCurrentInlineDepth@_StackGuard@details@Concurrency@@CAAEA_KXZ` | `0x10DF0` | 46 | UnwindData |  |
| 232 | `?_Reset@?$_SpinWait@$0A@@details@Concurrency@@IEAAXXZ` | `0x10E20` | 60 | UnwindData |  |
| 242 | `?_SetSpinCount@?$_SpinWait@$0A@@details@Concurrency@@QEAAXI@Z` | `0x10E60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 246 | `?_SpinOnce@?$_SpinWait@$0A@@details@Concurrency@@QEAA_NXZ` | `0x10E80` | 227 | UnwindData |  |
| 117 | `?Create@CurrentScheduler@Concurrency@@SAXAEBVSchedulerPolicy@2@@Z` | `0x10FB0` | 33 | UnwindData |  |
| 120 | `?CreateScheduleGroup@CurrentScheduler@Concurrency@@SAPEAVScheduleGroup@2@AEAVlocation@2@@Z` | `0x10FE0` | 39 | UnwindData |  |
| 121 | `?CreateScheduleGroup@CurrentScheduler@Concurrency@@SAPEAVScheduleGroup@2@XZ` | `0x11010` | 33 | UnwindData |  |
| 123 | `?Detach@CurrentScheduler@Concurrency@@SAXXZ` | `0x11040` | 54 | UnwindData |  |
| 127 | `?Get@CurrentScheduler@Concurrency@@SAPEAVScheduler@2@XZ` | `0x11080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `?GetNumberOfVirtualProcessors@CurrentScheduler@Concurrency@@SAIXZ` | `0x11090` | 48 | UnwindData |  |
| 131 | `?GetPolicy@CurrentScheduler@Concurrency@@SA?AVSchedulerPolicy@2@XZ` | `0x110C0` | 42 | UnwindData |  |
| 138 | `?Id@CurrentScheduler@Concurrency@@SAIXZ` | `0x110F0` | 48 | UnwindData |  |
| 194 | `?_Id@_CurrentScheduler@details@Concurrency@@SAIXZ` | `0x110F0` | 48 | UnwindData |  |
| 139 | `?IsAvailableLocation@CurrentScheduler@Concurrency@@SA_NAEBVlocation@2@@Z` | `0x11120` | 50 | UnwindData |  |
| 150 | `?RegisterShutdownEvent@CurrentScheduler@Concurrency@@SAXPEAX@Z` | `0x11160` | 72 | UnwindData |  |
| 155 | `?ScheduleTask@CurrentScheduler@Concurrency@@SAXP6AXPEAX@Z0@Z` | `0x111B0` | 54 | UnwindData |  |
| 239 | `?_ScheduleTask@_CurrentScheduler@details@Concurrency@@SAXP6AXPEAX@Z0@Z` | `0x111B0` | 54 | UnwindData |  |
| 156 | `?ScheduleTask@CurrentScheduler@Concurrency@@SAXP6AXPEAX@Z0AEAVlocation@2@@Z` | `0x111F0` | 70 | UnwindData |  |
| 187 | `?_Get@_CurrentScheduler@details@Concurrency@@SA?AV_Scheduler@23@XZ` | `0x11240` | 26 | UnwindData |  |
| 192 | `?_GetNumberOfVirtualProcessors@_CurrentScheduler@details@Concurrency@@SAIXZ` | `0x11260` | 33 | UnwindData |  |
| 9 | `??0_Condition_variable@details@Concurrency@@QEAA@XZ` | `0x11380` | 34 | UnwindData |  |
| 39 | `??0event@Concurrency@@QEAA@XZ` | `0x113B0` | 36 | UnwindData |  |
| 85 | `??1_Condition_variable@details@Concurrency@@QEAA@XZ` | `0x11480` | 49 | UnwindData |  |
| 96 | `??1event@Concurrency@@QEAA@XZ` | `0x114C0` | 141 | UnwindData |  |
| 269 | `?notify_all@_Condition_variable@details@Concurrency@@QEAAXXZ` | `0x11D00` | 25 | UnwindData |  |
| 270 | `?notify_one@_Condition_variable@details@Concurrency@@QEAAXXZ` | `0x11DB0` | 195 | UnwindData |  |
| 271 | `?reset@event@Concurrency@@QEAAXXZ` | `0x11E80` | 125 | UnwindData |  |
| 272 | `?set@event@Concurrency@@QEAAXXZ` | `0x11F00` | 451 | UnwindData |  |
| 285 | `?wait@_Condition_variable@details@Concurrency@@QEAAXAEAVcritical_section@3@@Z` | `0x120D0` | 225 | UnwindData |  |
| 287 | `?wait@event@Concurrency@@QEAA_KI@Z` | `0x121C0` | 486 | UnwindData |  |
| 288 | `?wait_for@_Condition_variable@details@Concurrency@@QEAA_NAEAVcritical_section@3@I@Z` | `0x123B0` | 316 | UnwindData |  |
| 290 | `?wait_for_multiple@event@Concurrency@@SA_KPEAPEAV12@_K_NI@Z` | `0x124F0` | 1,081 | UnwindData |  |
| 30 | `??0bad_target@Concurrency@@QEAA@PEBD@Z` | `0x12930` | 71 | UnwindData |  |
| 31 | `??0bad_target@Concurrency@@QEAA@XZ` | `0x12980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `??0context_self_unblock@Concurrency@@QEAA@PEBD@Z` | `0x129A0` | 71 | UnwindData |  |
| 33 | `??0context_self_unblock@Concurrency@@QEAA@XZ` | `0x129F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `??0context_unblock_unbalanced@Concurrency@@QEAA@PEBD@Z` | `0x12A10` | 71 | UnwindData |  |
| 35 | `??0context_unblock_unbalanced@Concurrency@@QEAA@XZ` | `0x12A60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `??0default_scheduler_exists@Concurrency@@QEAA@PEBD@Z` | `0x12A80` | 71 | UnwindData |  |
| 38 | `??0default_scheduler_exists@Concurrency@@QEAA@XZ` | `0x12AD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `??0improper_lock@Concurrency@@QEAA@PEBD@Z` | `0x12AF0` | 71 | UnwindData |  |
| 41 | `??0improper_lock@Concurrency@@QEAA@XZ` | `0x12B40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `??0improper_scheduler_attach@Concurrency@@QEAA@PEBD@Z` | `0x12B60` | 71 | UnwindData |  |
| 43 | `??0improper_scheduler_attach@Concurrency@@QEAA@XZ` | `0x12BB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `??0improper_scheduler_detach@Concurrency@@QEAA@PEBD@Z` | `0x12BD0` | 71 | UnwindData |  |
| 45 | `??0improper_scheduler_detach@Concurrency@@QEAA@XZ` | `0x12C20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `??0improper_scheduler_reference@Concurrency@@QEAA@PEBD@Z` | `0x12C40` | 71 | UnwindData |  |
| 47 | `??0improper_scheduler_reference@Concurrency@@QEAA@XZ` | `0x12C90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `??0invalid_link_target@Concurrency@@QEAA@PEBD@Z` | `0x12CB0` | 71 | UnwindData |  |
| 49 | `??0invalid_link_target@Concurrency@@QEAA@XZ` | `0x12D00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `??0invalid_multiple_scheduling@Concurrency@@QEAA@PEBD@Z` | `0x12D20` | 71 | UnwindData |  |
| 51 | `??0invalid_multiple_scheduling@Concurrency@@QEAA@XZ` | `0x12D70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `??0invalid_oversubscribe_operation@Concurrency@@QEAA@PEBD@Z` | `0x12D90` | 71 | UnwindData |  |
| 53 | `??0invalid_oversubscribe_operation@Concurrency@@QEAA@XZ` | `0x12DE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `??0invalid_scheduler_policy_key@Concurrency@@QEAA@PEBD@Z` | `0x12E00` | 71 | UnwindData |  |
| 55 | `??0invalid_scheduler_policy_key@Concurrency@@QEAA@XZ` | `0x12E50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `??0invalid_scheduler_policy_thread_specification@Concurrency@@QEAA@PEBD@Z` | `0x12E70` | 71 | UnwindData |  |
| 57 | `??0invalid_scheduler_policy_thread_specification@Concurrency@@QEAA@XZ` | `0x12EC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `??0invalid_scheduler_policy_value@Concurrency@@QEAA@PEBD@Z` | `0x12EE0` | 71 | UnwindData |  |
| 59 | `??0invalid_scheduler_policy_value@Concurrency@@QEAA@XZ` | `0x12F30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `??0message_not_found@Concurrency@@QEAA@PEBD@Z` | `0x12F50` | 71 | UnwindData |  |
| 61 | `??0message_not_found@Concurrency@@QEAA@XZ` | `0x12FA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `??0missing_wait@Concurrency@@QEAA@PEBD@Z` | `0x12FC0` | 71 | UnwindData |  |
| 63 | `??0missing_wait@Concurrency@@QEAA@XZ` | `0x13010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `??0nested_scheduler_missing_detach@Concurrency@@QEAA@PEBD@Z` | `0x13030` | 71 | UnwindData |  |
| 65 | `??0nested_scheduler_missing_detach@Concurrency@@QEAA@XZ` | `0x13080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `??0operation_timed_out@Concurrency@@QEAA@PEBD@Z` | `0x130A0` | 71 | UnwindData |  |
| 67 | `??0operation_timed_out@Concurrency@@QEAA@XZ` | `0x130F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `??0scheduler_not_attached@Concurrency@@QEAA@PEBD@Z` | `0x13110` | 71 | UnwindData |  |
| 70 | `??0scheduler_not_attached@Concurrency@@QEAA@XZ` | `0x13160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `??0scheduler_resource_allocation_error@Concurrency@@QEAA@J@Z` | `0x13180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `??0scheduler_resource_allocation_error@Concurrency@@QEAA@PEBDJ@Z` | `0x131A0` | 86 | UnwindData |  |
| 73 | `??0scheduler_worker_creation_error@Concurrency@@QEAA@J@Z` | `0x13200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `??0scheduler_worker_creation_error@Concurrency@@QEAA@PEBDJ@Z` | `0x13220` | 86 | UnwindData |  |
| 78 | `??0unsupported_os@Concurrency@@QEAA@PEBD@Z` | `0x13280` | 71 | UnwindData |  |
| 79 | `??0unsupported_os@Concurrency@@QEAA@XZ` | `0x132D0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 263 | `?get_error_code@scheduler_resource_allocation_error@Concurrency@@QEBAJXZ` | `0x13340` | 16,288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `?_Current_node@location@Concurrency@@SA?AV12@XZ` | `0x172E0` | 56 | UnwindData |  |
| 260 | `?current@location@Concurrency@@SA?AV12@XZ` | `0x174A0` | 56 | UnwindData |  |
| 262 | `?from_numa_node@location@Concurrency@@SA?AV12@G@Z` | `0x17550` | 87 | UnwindData |  |
| 188 | `?_GetCombinableSize@details@Concurrency@@YA_KXZ` | `0x182B0` | 81 | UnwindData |  |
| 264 | `?is_current_task_group_canceling@Concurrency@@YA_NXZ` | `0x18310` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `??0_NonReentrantBlockingLock@details@Concurrency@@QEAA@XZ` | `0x183C0` | 45 | UnwindData |  |
| 14 | `??0_ReentrantBlockingLock@details@Concurrency@@QEAA@XZ` | `0x183C0` | 45 | UnwindData |  |
| 12 | `??0_NonReentrantPPLLock@details@Concurrency@@QEAA@XZ` | `0x183F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `??0critical_section@Concurrency@@QEAA@XZ` | `0x183F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `??0_ReaderWriterLock@details@Concurrency@@QEAA@XZ` | `0x18430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `??0_ReentrantLock@details@Concurrency@@QEAA@XZ` | `0x18440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `??0_ReentrantPPLLock@details@Concurrency@@QEAA@XZ` | `0x18460` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `??0_Scoped_lock@_NonReentrantPPLLock@details@Concurrency@@QEAA@AEAV123@@Z` | `0x184A0` | 92 | UnwindData |  |
| 21 | `??0_Scoped_lock@_ReentrantPPLLock@details@Concurrency@@QEAA@AEAV123@@Z` | `0x185E0` | 145 | UnwindData |  |
| 68 | `??0reader_writer_lock@Concurrency@@QEAA@XZ` | `0x186C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `??0scoped_lock@critical_section@Concurrency@@QEAA@AEAV12@@Z` | `0x18700` | 107 | UnwindData |  |
| 76 | `??0scoped_lock@reader_writer_lock@Concurrency@@QEAA@AEAV12@@Z` | `0x18850` | 120 | UnwindData |  |
| 77 | `??0scoped_lock_read@reader_writer_lock@Concurrency@@QEAA@AEAV12@@Z` | `0x188D0` | 29 | UnwindData |  |
| 86 | `??1_NonReentrantBlockingLock@details@Concurrency@@QEAA@XZ` | `0x188F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `??1_ReentrantBlockingLock@details@Concurrency@@QEAA@XZ` | `0x188F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `??1_Scoped_lock@_NonReentrantPPLLock@details@Concurrency@@QEAA@XZ` | `0x18900` | 18 | UnwindData |  |
| 98 | `??1scoped_lock@critical_section@Concurrency@@QEAA@XZ` | `0x18900` | 18 | UnwindData |  |
| 89 | `??1_Scoped_lock@_ReentrantPPLLock@details@Concurrency@@QEAA@XZ` | `0x18920` | 31 | UnwindData |  |
| 99 | `??1scoped_lock@reader_writer_lock@Concurrency@@QEAA@XZ` | `0x18940` | 18 | UnwindData |  |
| 100 | `??1scoped_lock_read@reader_writer_lock@Concurrency@@QEAA@XZ` | `0x18940` | 18 | UnwindData |  |
| 165 | `?_Acquire@_NonReentrantBlockingLock@details@Concurrency@@QEAAXXZ` | `0x18CE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 167 | `?_Acquire@_ReentrantBlockingLock@details@Concurrency@@QEAAXXZ` | `0x18CE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `?_Acquire@_NonReentrantPPLLock@details@Concurrency@@QEAAXPEAX@Z` | `0x18CF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `?_Acquire@_ReentrantLock@details@Concurrency@@QEAAXXZ` | `0x18D00` | 311 | UnwindData |  |
| 169 | `?_Acquire@_ReentrantPPLLock@details@Concurrency@@QEAAXPEAX@Z` | `0x18E40` | 97 | UnwindData |  |
| 170 | `?_AcquireRead@_ReaderWriterLock@details@Concurrency@@QEAAXXZ` | `0x18EB0` | 118 | UnwindData |  |
| 171 | `?_AcquireWrite@_ReaderWriterLock@details@Concurrency@@QEAAXXZ` | `0x18F30` | 30 | UnwindData |  |
| 223 | `?_Release@_NonReentrantBlockingLock@details@Concurrency@@QEAAXXZ` | `0x192A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 225 | `?_Release@_ReentrantBlockingLock@details@Concurrency@@QEAAXXZ` | `0x192A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 224 | `?_Release@_NonReentrantPPLLock@details@Concurrency@@QEAAXXZ` | `0x192B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 226 | `?_Release@_ReentrantLock@details@Concurrency@@QEAAXXZ` | `0x192C0` | 49 | UnwindData |  |
| 227 | `?_Release@_ReentrantPPLLock@details@Concurrency@@QEAAXXZ` | `0x19300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 229 | `?_ReleaseRead@_ReaderWriterLock@details@Concurrency@@QEAAXXZ` | `0x19320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 230 | `?_ReleaseWrite@_ReaderWriterLock@details@Concurrency@@QEAAXXZ` | `0x19330` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 252 | `?_TryAcquire@_NonReentrantBlockingLock@details@Concurrency@@QEAA_NXZ` | `0x194E0` | 20 | UnwindData |  |
| 253 | `?_TryAcquire@_ReentrantBlockingLock@details@Concurrency@@QEAA_NXZ` | `0x194E0` | 20 | UnwindData |  |
| 254 | `?_TryAcquire@_ReentrantLock@details@Concurrency@@QEAA_NXZ` | `0x19500` | 51 | UnwindData |  |
| 255 | `?_TryAcquireWrite@_ReaderWriterLock@details@Concurrency@@QEAA_NXZ` | `0x19540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 257 | `?_Value@_SpinCount@details@Concurrency@@SAIXZ` | `0x19560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 265 | `?lock@critical_section@Concurrency@@QEAAXXZ` | `0x19570` | 91 | UnwindData |  |
| 266 | `?lock@reader_writer_lock@Concurrency@@QEAAXXZ` | `0x196B0` | 110 | UnwindData |  |
| 267 | `?lock_read@reader_writer_lock@Concurrency@@QEAAXXZ` | `0x19720` | 90 | UnwindData |  |
| 268 | `?native_handle@critical_section@Concurrency@@QEAAAEAV12@XZ` | `0x19890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 278 | `?try_lock@critical_section@Concurrency@@QEAA_NXZ` | `0x198A0` | 152 | UnwindData |  |
| 279 | `?try_lock@reader_writer_lock@Concurrency@@QEAA_NXZ` | `0x19940` | 179 | UnwindData |  |
| 280 | `?try_lock_for@critical_section@Concurrency@@QEAA_NI@Z` | `0x19A00` | 181 | UnwindData |  |
| 281 | `?try_lock_read@reader_writer_lock@Concurrency@@QEAA_NXZ` | `0x19AC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 282 | `?unlock@critical_section@Concurrency@@QEAAXXZ` | `0x19AF0` | 74 | UnwindData |  |
| 283 | `?unlock@reader_writer_lock@Concurrency@@QEAAXXZ` | `0x19CE0` | 103 | UnwindData |  |
| 119 | `?CreateResourceManager@Concurrency@@YAPEAUIResourceManager@1@XZ` | `0x1AAE0` | 174 | UnwindData |  |
| 133 | `?GetProcessorCount@Concurrency@@YAIXZ` | `0x1C530` | 71 | UnwindData |  |
| 128 | `?GetExecutionContextId@Concurrency@@YAIXZ` | `0x1C630` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | `?GetOSVersion@Concurrency@@YA?AW4OSVersion@IResourceManager@1@XZ` | `0x1C720` | 79 | UnwindData |  |
| 134 | `?GetProcessorNodeCount@Concurrency@@YAIXZ` | `0x1C770` | 71 | UnwindData |  |
| 135 | `?GetSchedulerId@Concurrency@@YAIXZ` | `0x1C7C0` | 12,704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 273 | `?set_task_execution_resources@Concurrency@@YAXGPEAU_GROUP_AFFINITY@@@Z` | `0x1F960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 274 | `?set_task_execution_resources@Concurrency@@YAX_K@Z` | `0x1F970` | 442 | UnwindData |  |
| 118 | `?Create@Scheduler@Concurrency@@SAPEAV12@AEBVSchedulerPolicy@2@@Z` | `0x235C0` | 47 | UnwindData |  |
| 151 | `?ResetDefaultSchedulerPolicy@Scheduler@Concurrency@@SAXXZ` | `0x26930` | 93 | UnwindData |  |
| 159 | `?SetDefaultSchedulerPolicy@Scheduler@Concurrency@@SAXAEBVSchedulerPolicy@2@@Z` | `0x26B40` | 190 | UnwindData |  |
| 228 | `?_Release@_Scheduler@details@Concurrency@@QEAAIXZ` | `0x27730` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0SchedulerPolicy@Concurrency@@QEAA@AEBV01@@Z` | `0x27750` | 70 | UnwindData |  |
| 4 | `??0SchedulerPolicy@Concurrency@@QEAA@XZ` | `0x277A0` | 28 | UnwindData |  |
| 5 | `??0SchedulerPolicy@Concurrency@@QEAA@_KZZ` | `0x277C0` | 52 | UnwindData |  |
| 80 | `??1SchedulerPolicy@Concurrency@@QEAA@XZ` | `0x278C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `??4SchedulerPolicy@Concurrency@@QEAAAEAV01@AEBV01@@Z` | `0x278D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `?GetPolicyValue@SchedulerPolicy@Concurrency@@QEBAIW4PolicyElementKey@2@@Z` | `0x27900` | 64 | UnwindData |  |
| 158 | `?SetConcurrencyLimits@SchedulerPolicy@Concurrency@@QEAAXII@Z` | `0x27940` | 182 | UnwindData |  |
| 160 | `?SetPolicyValue@SchedulerPolicy@Concurrency@@QEAAIW4PolicyElementKey@2@I@Z` | `0x27A00` | 165 | UnwindData |  |
| 111 | `?Alloc@Concurrency@@YAPEAX_K@Z` | `0x2DC00` | 113 | UnwindData |  |
| 126 | `?Free@Concurrency@@YAXPEAX@Z` | `0x2DD60` | 74 | UnwindData |  |
| 23 | `??0_StructuredTaskCollection@details@Concurrency@@QEAA@PEAV_CancellationTokenState@12@@Z` | `0x2DED0` | 178 | UnwindData |  |
| 24 | `??0_TaskCollection@details@Concurrency@@QEAA@PEAV_CancellationTokenState@12@@Z` | `0x2E120` | 255 | UnwindData |  |
| 25 | `??0_TaskCollection@details@Concurrency@@QEAA@XZ` | `0x2E220` | 253 | UnwindData |  |
| 91 | `??1_StructuredTaskCollection@details@Concurrency@@QEAA@XZ` | `0x2E3A0` | 108 | UnwindData |  |
| 92 | `??1_TaskCollection@details@Concurrency@@QEAA@XZ` | `0x2E410` | 408 | UnwindData |  |
| 164 | `?_Abort@_StructuredTaskCollection@details@Concurrency@@AEAAXXZ` | `0x2E970` | 496 | UnwindData |  |
| 175 | `?_Cancel@_StructuredTaskCollection@details@Concurrency@@QEAAXXZ` | `0x2EFD0` | 140 | UnwindData |  |
| 176 | `?_Cancel@_TaskCollection@details@Concurrency@@QEAAXXZ` | `0x2F1F0` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 178 | `?_CleanupToken@_StructuredTaskCollection@details@Concurrency@@AEAAXXZ` | `0x2F3B0` | 118 | UnwindData |  |
| 215 | `?_IsCanceling@_StructuredTaskCollection@details@Concurrency@@QEAA_NXZ` | `0x2F7A0` | 114 | UnwindData |  |
| 216 | `?_IsCanceling@_TaskCollection@details@Concurrency@@QEAA_NXZ` | `0x2F860` | 268 | UnwindData |  |
| 218 | `?_NewCollection@_AsyncTaskCollection@details@Concurrency@@SAPEAV123@PEAV_CancellationTokenState@23@@Z` | `0x2F990` | 138 | UnwindData |  |
| 233 | `?_RunAndWait@_StructuredTaskCollection@details@Concurrency@@QEAA?AW4_TaskCollectionStatus@23@PEAV_UnrealizedChore@23@@Z` | `0x2FE50` | 836 | UnwindData |  |
| 234 | `?_RunAndWait@_TaskCollection@details@Concurrency@@QEAA?AW4_TaskCollectionStatus@23@PEAV_UnrealizedChore@23@@Z` | `0x301A0` | 2,069 | UnwindData |  |
| 235 | `?_Schedule@_StructuredTaskCollection@details@Concurrency@@QEAAXPEAV_UnrealizedChore@23@@Z` | `0x309C0` | 136 | UnwindData |  |
| 236 | `?_Schedule@_StructuredTaskCollection@details@Concurrency@@QEAAXPEAV_UnrealizedChore@23@PEAVlocation@3@@Z` | `0x30A50` | 152 | UnwindData |  |
| 237 | `?_Schedule@_TaskCollection@details@Concurrency@@QEAAXPEAV_UnrealizedChore@23@@Z` | `0x30AF0` | 322 | UnwindData |  |
| 238 | `?_Schedule@_TaskCollection@details@Concurrency@@QEAAXPEAV_UnrealizedChore@23@PEAVlocation@3@@Z` | `0x30C40` | 343 | UnwindData |  |
| 26 | `??0_Timer@details@Concurrency@@IEAA@I_N@Z` | `0x31FA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `??1_Timer@details@Concurrency@@MEAA@XZ` | `0x31FC0` | 47 | UnwindData |  |
| 248 | `?_Start@_Timer@details@Concurrency@@IEAAXXZ` | `0x32130` | 82 | UnwindData |  |
| 249 | `?_Stop@_Timer@details@Concurrency@@IEAAXXZ` | `0x32190` | 32 | UnwindData |  |
| 284 | `?wait@Concurrency@@YAXI@Z` | `0x321B0` | 170 | UnwindData |  |
| 189 | `?_GetConcRTTraceInfo@Concurrency@@YAPEBU_CONCRT_TRACE_INFO@details@1@XZ` | `0x32530` | 31 | UnwindData |  |
| 250 | `?_Trace_agents@Concurrency@@YAXW4Agents_EventType@1@_JZZ` | `0x327E0` | 346 | UnwindData |  |
| 251 | `?_Trace_ppl_function@Concurrency@@YAXAEBU_GUID@@EW4ConcRT_EventType@1@@Z` | `0x32940` | 191 | UnwindData |  |
| 22 | `??0_SpinLock@details@Concurrency@@QEAA@AECJ@Z` | `0x349F0` | 34 | UnwindData |  |
| 90 | `??1_SpinLock@details@Concurrency@@QEAA@XZ` | `0x34B70` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `?Log2@details@Concurrency@@YAK_K@Z` | `0x34D00` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `?_ConcRT_CoreAssert@details@Concurrency@@YAXPEBD0H@Z` | `0x34F70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 180 | `?_ConcRT_Trace@details@Concurrency@@YAXHPEB_WZZ` | `0x34F80` | 57 | UnwindData |  |
| 190 | `?_GetConcurrency@details@Concurrency@@YAIXZ` | `0x351C0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 256 | `?_UnderlyingYield@details@Concurrency@@YAXXZ` | `0x35230` | 47 | UnwindData |  |
| 174 | `?_Byte_reverse_table@details@Concurrency@@3QBEB` | `0x3A940` | 5,472 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `?ConcRT_ProviderGuid@Concurrency@@3U_GUID@@B` | `0x3BEA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `?ConcRTEventGuid@Concurrency@@3U_GUID@@B` | `0x3BEB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `?SchedulerEventGuid@Concurrency@@3U_GUID@@B` | `0x3BEC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `?ScheduleGroupEventGuid@Concurrency@@3U_GUID@@B` | `0x3BED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `?ContextEventGuid@Concurrency@@3U_GUID@@B` | `0x3BEE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `?ChoreEventGuid@Concurrency@@3U_GUID@@B` | `0x3BEF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 161 | `?VirtualProcessorEventGuid@Concurrency@@3U_GUID@@B` | `0x3BF00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `?LockEventGuid@Concurrency@@3U_GUID@@B` | `0x3BF10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `?ResourceManagerEventGuid@Concurrency@@3U_GUID@@B` | `0x3BF20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `?PPLParallelInvokeEventGuid@Concurrency@@3U_GUID@@B` | `0x3BF30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `?PPLParallelForEventGuid@Concurrency@@3U_GUID@@B` | `0x3BF40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 148 | `?PPLParallelForeachEventGuid@Concurrency@@3U_GUID@@B` | `0x3BF50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `?AgentEventGuid@Concurrency@@3U_GUID@@B` | `0x3BF60` | 0 | Indeterminate |  |
