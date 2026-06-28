# Binary Specification: concrt140d.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\concrt140d.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `972fa5b99d9e995cefe477a9f21f013d295024c9424c2bb9f23f377e552fa591`
* **Total Exported Functions:** 291

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `??0?$_SpinWait@$00@details@Concurrency@@QEAA@P6AXXZ@Z` | `0x1110` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `??0_Context@details@Concurrency@@QEAA@PEAVContext@2@@Z` | `0x1160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `??0_Scheduler@details@Concurrency@@QEAA@PEAVScheduler@2@@Z` | `0x1180` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `??4?$_SpinWait@$00@details@Concurrency@@QEAAAEAV012@$$QEAV012@@Z` | `0x11D0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `??4?$_SpinWait@$00@details@Concurrency@@QEAAAEAV012@AEBV012@@Z` | `0x1220` | 37 | UnwindData |  |
| 106 | `??_F?$_SpinWait@$00@details@Concurrency@@QEAAXXZ` | `0x12F0` | 32 | UnwindData |  |
| 108 | `??_F_Context@details@Concurrency@@QEAAXXZ` | `0x1310` | 27 | UnwindData |  |
| 109 | `??_F_Scheduler@details@Concurrency@@QEAAXXZ` | `0x1330` | 27 | UnwindData |  |
| 185 | `?_DoYield@?$_SpinWait@$00@details@Concurrency@@IEAAXXZ` | `0x13D0` | 122 | UnwindData |  |
| 193 | `?_GetScheduler@_Scheduler@details@Concurrency@@QEAAPEAVScheduler@3@XZ` | `0x1450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 219 | `?_NumberOfSpins@?$_SpinWait@$00@details@Concurrency@@IEAAKXZ` | `0x1460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 231 | `?_Reset@?$_SpinWait@$00@details@Concurrency@@IEAAXXZ` | `0x1470` | 120 | UnwindData |  |
| 241 | `?_SetSpinCount@?$_SpinWait@$00@details@Concurrency@@QEAAXI@Z` | `0x14F0` | 150 | UnwindData |  |
| 243 | `?_ShouldSpinAgain@?$_SpinWait@$00@details@Concurrency@@IEAA_NXZ` | `0x1590` | 65 | UnwindData |  |
| 245 | `?_SpinOnce@?$_SpinWait@$00@details@Concurrency@@QEAA_NXZ` | `0x15E0` | 382 | UnwindData |  |
| 17 | `??0_Runtime_object@details@Concurrency@@QEAA@H@Z` | `0x49A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `??0_Runtime_object@details@Concurrency@@QEAA@XZ` | `0x49D0` | 138 | UnwindData |  |
| 27 | `??0agent@Concurrency@@QEAA@AEAVScheduleGroup@1@@Z` | `0x4A60` | 201 | UnwindData |  |
| 28 | `??0agent@Concurrency@@QEAA@AEAVScheduler@1@@Z` | `0x4B30` | 201 | UnwindData |  |
| 29 | `??0agent@Concurrency@@QEAA@XZ` | `0x4C00` | 195 | UnwindData |  |
| 94 | `??1agent@Concurrency@@UEAA@XZ` | `0x6840` | 71 | UnwindData |  |
| 259 | `?cancel@agent@Concurrency@@QEAA_NXZ` | `0x10270` | 247 | UnwindData |  |
| 261 | `?done@agent@Concurrency@@IEAA_NXZ` | `0x112A0` | 248 | UnwindData |  |
| 275 | `?start@agent@Concurrency@@QEAA_NXZ` | `0x16190` | 405 | UnwindData |  |
| 276 | `?status@agent@Concurrency@@QEAA?AW4agent_status@2@XZ` | `0x16330` | 36 | UnwindData |  |
| 277 | `?status_port@agent@Concurrency@@QEAAPEAV?$ISource@W4agent_status@Concurrency@@@2@XZ` | `0x16360` | 7,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 286 | `?wait@agent@Concurrency@@SA?AW4agent_status@2@PEAV12@I@Z` | `0x17F00` | 174 | UnwindData |  |
| 289 | `?wait_for_all@agent@Concurrency@@SAX_KPEAPEAV12@PEAW4agent_status@2@I@Z` | `0x17FB0` | 496 | UnwindData |  |
| 291 | `?wait_for_one@agent@Concurrency@@SAX_KPEAPEAV12@AEAW4agent_status@2@AEA_KI@Z` | `0x181F0` | 372 | UnwindData |  |
| 143 | `?NFS_Allocate@details@Concurrency@@YAPEAX_K0PEAX@Z` | `0x194B0` | 476 | UnwindData |  |
| 144 | `?NFS_Free@details@Concurrency@@YAXPEAX@Z` | `0x19690` | 164 | UnwindData |  |
| 145 | `?NFS_GetLineSize@details@Concurrency@@YA_KXZ` | `0x19740` | 3,888 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 177 | `?_CheckTaskCollection@_UnrealizedChore@details@Concurrency@@IEAAXXZ` | `0x1A670` | 212 | UnwindData |  |
| 7 | `??0_Concurrent_queue_base_v4@details@Concurrency@@IEAA@_K@Z` | `0x1C1D0` | 785 | UnwindData |  |
| 8 | `??0_Concurrent_queue_iterator_base_v4@details@Concurrency@@IEAA@AEBV_Concurrent_queue_base_v4@12@@Z` | `0x1C4F0` | 147 | UnwindData |  |
| 82 | `??1_Concurrent_queue_base_v4@details@Concurrency@@MEAA@XZ` | `0x1C6C0` | 228 | UnwindData |  |
| 83 | `??1_Concurrent_queue_iterator_base_v4@details@Concurrency@@IEAA@XZ` | `0x1C7B0` | 76 | UnwindData |  |
| 172 | `?_Advance@_Concurrent_queue_iterator_base_v4@details@Concurrency@@IEAAXXZ` | `0x1CAC0` | 447 | UnwindData |  |
| 173 | `?_Assign@_Concurrent_queue_iterator_base_v4@details@Concurrency@@IEAAXAEBV123@@Z` | `0x1CC80` | 234 | UnwindData |  |
| 200 | `?_Internal_empty@_Concurrent_queue_base_v4@details@Concurrency@@IEBA_NXZ` | `0x1CDF0` | 139 | UnwindData |  |
| 201 | `?_Internal_finish_clear@_Concurrent_queue_base_v4@details@Concurrency@@IEAAXXZ` | `0x1CE80` | 312 | UnwindData |  |
| 204 | `?_Internal_move_push@_Concurrent_queue_base_v4@details@Concurrency@@IEAAXPEAX@Z` | `0x1CFC0` | 122 | UnwindData |  |
| 205 | `?_Internal_pop_if_present@_Concurrent_queue_base_v4@details@Concurrency@@IEAA_NPEAX@Z` | `0x1D040` | 204 | UnwindData |  |
| 206 | `?_Internal_push@_Concurrent_queue_base_v4@details@Concurrency@@IEAAXPEBX@Z` | `0x1D110` | 122 | UnwindData |  |
| 210 | `?_Internal_size@_Concurrent_queue_base_v4@details@Concurrency@@IEBA_KXZ` | `0x1D190` | 65 | UnwindData |  |
| 211 | `?_Internal_swap@_Concurrent_queue_base_v4@details@Concurrency@@IEAAXAEAV123@@Z` | `0x1D1E0` | 66 | UnwindData |  |
| 213 | `?_Internal_throw_exception@_Concurrent_queue_base_v4@details@Concurrency@@IEBAXXZ` | `0x1D230` | 42 | UnwindData |  |
| 84 | `??1_Concurrent_vector_base_v4@details@Concurrency@@IEAA@XZ` | `0x1DB80` | 142 | UnwindData |  |
| 195 | `?_Internal_assign@_Concurrent_vector_base_v4@details@Concurrency@@IEAAXAEBV123@_KP6AXPEAX1@ZP6AX2PEBX1@Z5@Z` | `0x1DD80` | 1,438 | UnwindData |  |
| 196 | `?_Internal_capacity@_Concurrent_vector_base_v4@details@Concurrency@@IEBA_KXZ` | `0x1E320` | 32 | UnwindData |  |
| 197 | `?_Internal_clear@_Concurrent_vector_base_v4@details@Concurrency@@IEAA_KP6AXPEAX_K@Z@Z` | `0x1E340` | 446 | UnwindData |  |
| 198 | `?_Internal_compact@_Concurrent_vector_base_v4@details@Concurrency@@IEAAPEAX_KPEAXP6AX10@ZP6AX1PEBX0@Z@Z` | `0x1E500` | 1,536 | UnwindData |  |
| 199 | `?_Internal_copy@_Concurrent_vector_base_v4@details@Concurrency@@IEAAXAEBV123@_KP6AXPEAXPEBX1@Z@Z` | `0x1EB00` | 491 | UnwindData |  |
| 202 | `?_Internal_grow_by@_Concurrent_vector_base_v4@details@Concurrency@@IEAA_K_K0P6AXPEAXPEBX0@Z2@Z` | `0x1EE40` | 127 | UnwindData |  |
| 203 | `?_Internal_grow_to_at_least_with_result@_Concurrent_vector_base_v4@details@Concurrency@@IEAA_K_K0P6AXPEAXPEBX0@Z2@Z` | `0x1F040` | 520 | UnwindData |  |
| 207 | `?_Internal_push_back@_Concurrent_vector_base_v4@details@Concurrency@@IEAAPEAX_KAEA_K@Z` | `0x1F250` | 270 | UnwindData |  |
| 208 | `?_Internal_reserve@_Concurrent_vector_base_v4@details@Concurrency@@IEAAX_K00@Z` | `0x1F360` | 181 | UnwindData |  |
| 209 | `?_Internal_resize@_Concurrent_vector_base_v4@details@Concurrency@@IEAAX_K00P6AXPEAX0@ZP6AX1PEBX0@Z3@Z` | `0x1F420` | 1,298 | UnwindData |  |
| 212 | `?_Internal_swap@_Concurrent_vector_base_v4@details@Concurrency@@IEAAXAEAV123@@Z` | `0x1F940` | 785 | UnwindData |  |
| 214 | `?_Internal_throw_exception@_Concurrent_vector_base_v4@details@Concurrency@@IEBAX_K@Z` | `0x1FC60` | 94 | UnwindData |  |
| 240 | `?_Segment_index_of@_Concurrent_vector_base_v4@details@Concurrency@@KA_K_K@Z` | `0x1FCF0` | 33 | UnwindData |  |
| 112 | `?Block@Context@Concurrency@@SAXXZ` | `0x203D0` | 53 | UnwindData |  |
| 122 | `?CurrentContext@Context@Concurrency@@SAPEAV12@XZ` | `0x20410` | 14 | UnwindData |  |
| 137 | `?Id@Context@Concurrency@@SAIXZ` | `0x20470` | 77 | UnwindData |  |
| 140 | `?IsCurrentTaskCollectionCanceling@Context@Concurrency@@SA_NXZ` | `0x204C0` | 134 | UnwindData |  |
| 146 | `?Oversubscribe@Context@Concurrency@@SAX_N@Z` | `0x20580` | 72 | UnwindData |  |
| 154 | `?ScheduleGroupId@Context@Concurrency@@SAIXZ` | `0x205D0` | 78 | UnwindData |  |
| 162 | `?VirtualProcessorId@Context@Concurrency@@SAIXZ` | `0x20620` | 78 | UnwindData |  |
| 163 | `?Yield@Context@Concurrency@@SAXXZ` | `0x20670` | 53 | UnwindData |  |
| 182 | `?_CurrentContext@_Context@details@Concurrency@@SA?AV123@XZ` | `0x206B0` | 37 | UnwindData |  |
| 217 | `?_IsSynchronouslyBlocked@_Context@details@Concurrency@@QEBA_NXZ` | `0x20720` | 53 | UnwindData |  |
| 221 | `?_Oversubscribe@_Context@details@Concurrency@@SAX_N@Z` | `0x20760` | 72 | UnwindData |  |
| 247 | `?_SpinYield@Context@Concurrency@@SAXXZ` | `0x207B0` | 53 | UnwindData |  |
| 258 | `?_Yield@_Context@details@Concurrency@@SAXXZ` | `0x207F0` | 53 | UnwindData |  |
| 2 | `??0?$_SpinWait@$0A@@details@Concurrency@@QEAA@P6AXXZ@Z` | `0x20960` | 1,008 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `??0_Cancellation_beacon@details@Concurrency@@QEAA@XZ` | `0x20D50` | 47 | UnwindData |  |
| 81 | `??1_Cancellation_beacon@details@Concurrency@@QEAA@XZ` | `0x210F0` | 35 | UnwindData |  |
| 103 | `??4?$_SpinWait@$0A@@details@Concurrency@@QEAAAEAV012@$$QEAV012@@Z` | `0x21160` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `??4?$_SpinWait@$0A@@details@Concurrency@@QEAAAEAV012@AEBV012@@Z` | `0x211B0` | 37 | UnwindData |  |
| 107 | `??_F?$_SpinWait@$0A@@details@Concurrency@@QEAAXXZ` | `0x21360` | 32 | UnwindData |  |
| 181 | `?_Confirm_cancel@_Cancellation_beacon@details@Concurrency@@QEAA_NXZ` | `0x26C60` | 71 | UnwindData |  |
| 186 | `?_DoYield@?$_SpinWait@$0A@@details@Concurrency@@IEAAXXZ` | `0x26CB0` | 20 | UnwindData |  |
| 191 | `?_GetCurrentInlineDepth@_StackGuard@details@Concurrency@@CAAEA_KXZ` | `0x26CD0` | 18 | UnwindData |  |
| 220 | `?_NumberOfSpins@?$_SpinWait@$0A@@details@Concurrency@@IEAAKXZ` | `0x26EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 232 | `?_Reset@?$_SpinWait@$0A@@details@Concurrency@@IEAAXXZ` | `0x26ED0` | 120 | UnwindData |  |
| 242 | `?_SetSpinCount@?$_SpinWait@$0A@@details@Concurrency@@QEAAXI@Z` | `0x26F90` | 150 | UnwindData |  |
| 244 | `?_ShouldSpinAgain@?$_SpinWait@$0A@@details@Concurrency@@IEAA_NXZ` | `0x27030` | 65 | UnwindData |  |
| 246 | `?_SpinOnce@?$_SpinWait@$0A@@details@Concurrency@@QEAA_NXZ` | `0x27080` | 382 | UnwindData |  |
| 117 | `?Create@CurrentScheduler@Concurrency@@SAXAEBVSchedulerPolicy@2@@Z` | `0x272A0` | 63 | UnwindData |  |
| 120 | `?CreateScheduleGroup@CurrentScheduler@Concurrency@@SAPEAVScheduleGroup@2@AEAVlocation@2@@Z` | `0x272E0` | 72 | UnwindData |  |
| 121 | `?CreateScheduleGroup@CurrentScheduler@Concurrency@@SAPEAVScheduleGroup@2@XZ` | `0x27330` | 52 | UnwindData |  |
| 123 | `?Detach@CurrentScheduler@Concurrency@@SAXXZ` | `0x27370` | 70 | UnwindData |  |
| 127 | `?Get@CurrentScheduler@Concurrency@@SAPEAVScheduler@2@XZ` | `0x273C0` | 14 | UnwindData |  |
| 129 | `?GetNumberOfVirtualProcessors@CurrentScheduler@Concurrency@@SAIXZ` | `0x273D0` | 78 | UnwindData |  |
| 131 | `?GetPolicy@CurrentScheduler@Concurrency@@SA?AVSchedulerPolicy@2@XZ` | `0x27420` | 96 | UnwindData |  |
| 138 | `?Id@CurrentScheduler@Concurrency@@SAIXZ` | `0x27480` | 78 | UnwindData |  |
| 139 | `?IsAvailableLocation@CurrentScheduler@Concurrency@@SA_NAEBVlocation@2@@Z` | `0x274D0` | 96 | UnwindData |  |
| 150 | `?RegisterShutdownEvent@CurrentScheduler@Concurrency@@SAXPEAX@Z` | `0x27530` | 113 | UnwindData |  |
| 155 | `?ScheduleTask@CurrentScheduler@Concurrency@@SAXP6AXPEAX@Z0@Z` | `0x275B0` | 83 | UnwindData |  |
| 156 | `?ScheduleTask@CurrentScheduler@Concurrency@@SAXP6AXPEAX@Z0AEAVlocation@2@@Z` | `0x27610` | 93 | UnwindData |  |
| 187 | `?_Get@_CurrentScheduler@details@Concurrency@@SA?AV_Scheduler@23@XZ` | `0x27670` | 37 | UnwindData |  |
| 192 | `?_GetNumberOfVirtualProcessors@_CurrentScheduler@details@Concurrency@@SAIXZ` | `0x276A0` | 52 | UnwindData |  |
| 194 | `?_Id@_CurrentScheduler@details@Concurrency@@SAIXZ` | `0x276E0` | 14 | UnwindData |  |
| 239 | `?_ScheduleTask@_CurrentScheduler@details@Concurrency@@SAXP6AXPEAX@Z0@Z` | `0x276F0` | 83 | UnwindData |  |
| 9 | `??0_Condition_variable@details@Concurrency@@QEAA@XZ` | `0x27C80` | 49 | UnwindData |  |
| 39 | `??0event@Concurrency@@QEAA@XZ` | `0x27CC0` | 62 | UnwindData |  |
| 85 | `??1_Condition_variable@details@Concurrency@@QEAA@XZ` | `0x27DC0` | 60 | UnwindData |  |
| 96 | `??1event@Concurrency@@QEAA@XZ` | `0x27E00` | 195 | UnwindData |  |
| 136 | `?GetSharedTimerQueue@details@Concurrency@@YAPEAXXZ` | `0x281B0` | 4,288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 269 | `?notify_all@_Condition_variable@details@Concurrency@@QEAAXXZ` | `0x29270` | 212 | UnwindData |  |
| 270 | `?notify_one@_Condition_variable@details@Concurrency@@QEAAXXZ` | `0x29350` | 250 | UnwindData |  |
| 271 | `?reset@event@Concurrency@@QEAAXXZ` | `0x29450` | 214 | UnwindData |  |
| 272 | `?set@event@Concurrency@@QEAAXXZ` | `0x29530` | 606 | UnwindData |  |
| 285 | `?wait@_Condition_variable@details@Concurrency@@QEAAXAEAVcritical_section@3@@Z` | `0x29790` | 164 | UnwindData |  |
| 287 | `?wait@event@Concurrency@@QEAA_KI@Z` | `0x29840` | 426 | UnwindData |  |
| 288 | `?wait_for@_Condition_variable@details@Concurrency@@QEAA_NAEAVcritical_section@3@I@Z` | `0x299F0` | 448 | UnwindData |  |
| 290 | `?wait_for_multiple@event@Concurrency@@SA_KPEAPEAV12@_K_NI@Z` | `0x29BB0` | 1,524 | UnwindData |  |
| 30 | `??0bad_target@Concurrency@@QEAA@PEBD@Z` | `0x2A2D0` | 54 | UnwindData |  |
| 31 | `??0bad_target@Concurrency@@QEAA@XZ` | `0x2A310` | 44 | UnwindData |  |
| 32 | `??0context_self_unblock@Concurrency@@QEAA@PEBD@Z` | `0x2A340` | 54 | UnwindData |  |
| 33 | `??0context_self_unblock@Concurrency@@QEAA@XZ` | `0x2A380` | 44 | UnwindData |  |
| 34 | `??0context_unblock_unbalanced@Concurrency@@QEAA@PEBD@Z` | `0x2A3B0` | 54 | UnwindData |  |
| 35 | `??0context_unblock_unbalanced@Concurrency@@QEAA@XZ` | `0x2A3F0` | 44 | UnwindData |  |
| 37 | `??0default_scheduler_exists@Concurrency@@QEAA@PEBD@Z` | `0x2A420` | 54 | UnwindData |  |
| 38 | `??0default_scheduler_exists@Concurrency@@QEAA@XZ` | `0x2A460` | 44 | UnwindData |  |
| 40 | `??0improper_lock@Concurrency@@QEAA@PEBD@Z` | `0x2A490` | 54 | UnwindData |  |
| 41 | `??0improper_lock@Concurrency@@QEAA@XZ` | `0x2A4D0` | 44 | UnwindData |  |
| 42 | `??0improper_scheduler_attach@Concurrency@@QEAA@PEBD@Z` | `0x2A500` | 54 | UnwindData |  |
| 43 | `??0improper_scheduler_attach@Concurrency@@QEAA@XZ` | `0x2A540` | 44 | UnwindData |  |
| 44 | `??0improper_scheduler_detach@Concurrency@@QEAA@PEBD@Z` | `0x2A570` | 54 | UnwindData |  |
| 45 | `??0improper_scheduler_detach@Concurrency@@QEAA@XZ` | `0x2A5B0` | 44 | UnwindData |  |
| 46 | `??0improper_scheduler_reference@Concurrency@@QEAA@PEBD@Z` | `0x2A5E0` | 54 | UnwindData |  |
| 47 | `??0improper_scheduler_reference@Concurrency@@QEAA@XZ` | `0x2A620` | 44 | UnwindData |  |
| 48 | `??0invalid_link_target@Concurrency@@QEAA@PEBD@Z` | `0x2A650` | 54 | UnwindData |  |
| 49 | `??0invalid_link_target@Concurrency@@QEAA@XZ` | `0x2A690` | 44 | UnwindData |  |
| 50 | `??0invalid_multiple_scheduling@Concurrency@@QEAA@PEBD@Z` | `0x2A6C0` | 54 | UnwindData |  |
| 51 | `??0invalid_multiple_scheduling@Concurrency@@QEAA@XZ` | `0x2A700` | 44 | UnwindData |  |
| 52 | `??0invalid_oversubscribe_operation@Concurrency@@QEAA@PEBD@Z` | `0x2A730` | 54 | UnwindData |  |
| 53 | `??0invalid_oversubscribe_operation@Concurrency@@QEAA@XZ` | `0x2A770` | 44 | UnwindData |  |
| 54 | `??0invalid_scheduler_policy_key@Concurrency@@QEAA@PEBD@Z` | `0x2A7A0` | 54 | UnwindData |  |
| 55 | `??0invalid_scheduler_policy_key@Concurrency@@QEAA@XZ` | `0x2A7E0` | 44 | UnwindData |  |
| 56 | `??0invalid_scheduler_policy_thread_specification@Concurrency@@QEAA@PEBD@Z` | `0x2A810` | 54 | UnwindData |  |
| 57 | `??0invalid_scheduler_policy_thread_specification@Concurrency@@QEAA@XZ` | `0x2A850` | 44 | UnwindData |  |
| 58 | `??0invalid_scheduler_policy_value@Concurrency@@QEAA@PEBD@Z` | `0x2A880` | 54 | UnwindData |  |
| 59 | `??0invalid_scheduler_policy_value@Concurrency@@QEAA@XZ` | `0x2A8C0` | 44 | UnwindData |  |
| 60 | `??0message_not_found@Concurrency@@QEAA@PEBD@Z` | `0x2A8F0` | 54 | UnwindData |  |
| 61 | `??0message_not_found@Concurrency@@QEAA@XZ` | `0x2A930` | 44 | UnwindData |  |
| 62 | `??0missing_wait@Concurrency@@QEAA@PEBD@Z` | `0x2A960` | 54 | UnwindData |  |
| 63 | `??0missing_wait@Concurrency@@QEAA@XZ` | `0x2A9A0` | 44 | UnwindData |  |
| 64 | `??0nested_scheduler_missing_detach@Concurrency@@QEAA@PEBD@Z` | `0x2A9D0` | 54 | UnwindData |  |
| 65 | `??0nested_scheduler_missing_detach@Concurrency@@QEAA@XZ` | `0x2AA10` | 44 | UnwindData |  |
| 66 | `??0operation_timed_out@Concurrency@@QEAA@PEBD@Z` | `0x2AA40` | 54 | UnwindData |  |
| 67 | `??0operation_timed_out@Concurrency@@QEAA@XZ` | `0x2AA80` | 44 | UnwindData |  |
| 69 | `??0scheduler_not_attached@Concurrency@@QEAA@PEBD@Z` | `0x2AAB0` | 54 | UnwindData |  |
| 70 | `??0scheduler_not_attached@Concurrency@@QEAA@XZ` | `0x2AAF0` | 44 | UnwindData |  |
| 71 | `??0scheduler_resource_allocation_error@Concurrency@@QEAA@J@Z` | `0x2AB20` | 60 | UnwindData |  |
| 72 | `??0scheduler_resource_allocation_error@Concurrency@@QEAA@PEBDJ@Z` | `0x2AB60` | 71 | UnwindData |  |
| 73 | `??0scheduler_worker_creation_error@Concurrency@@QEAA@J@Z` | `0x2ABB0` | 52 | UnwindData |  |
| 74 | `??0scheduler_worker_creation_error@Concurrency@@QEAA@PEBDJ@Z` | `0x2ABF0` | 64 | UnwindData |  |
| 78 | `??0unsupported_os@Concurrency@@QEAA@PEBD@Z` | `0x2AC30` | 54 | UnwindData |  |
| 79 | `??0unsupported_os@Concurrency@@QEAA@XZ` | `0x2AC70` | 44 | UnwindData |  |
| 263 | `?get_error_code@scheduler_resource_allocation_error@Concurrency@@QEBAJXZ` | `0x2B2A0` | 41,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `?_Current_node@location@Concurrency@@SA?AV12@XZ` | `0x35410` | 378 | UnwindData |  |
| 260 | `?current@location@Concurrency@@SA?AV12@XZ` | `0x35770` | 365 | UnwindData |  |
| 262 | `?from_numa_node@location@Concurrency@@SA?AV12@G@Z` | `0x358E0` | 126 | UnwindData |  |
| 188 | `?_GetCombinableSize@details@Concurrency@@YA_KXZ` | `0x37520` | 154 | UnwindData |  |
| 264 | `?is_current_task_group_canceling@Concurrency@@YA_NXZ` | `0x375C0` | 14 | UnwindData |  |
| 11 | `??0_NonReentrantBlockingLock@details@Concurrency@@QEAA@XZ` | `0x376F0` | 87 | UnwindData |  |
| 12 | `??0_NonReentrantPPLLock@details@Concurrency@@QEAA@XZ` | `0x37750` | 33 | UnwindData |  |
| 13 | `??0_ReaderWriterLock@details@Concurrency@@QEAA@XZ` | `0x37780` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `??0_ReentrantBlockingLock@details@Concurrency@@QEAA@XZ` | `0x377B0` | 87 | UnwindData |  |
| 15 | `??0_ReentrantLock@details@Concurrency@@QEAA@XZ` | `0x37810` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `??0_ReentrantPPLLock@details@Concurrency@@QEAA@XZ` | `0x37840` | 56 | UnwindData |  |
| 20 | `??0_Scoped_lock@_NonReentrantPPLLock@details@Concurrency@@QEAA@AEAV123@@Z` | `0x37880` | 116 | UnwindData |  |
| 21 | `??0_Scoped_lock@_ReentrantPPLLock@details@Concurrency@@QEAA@AEAV123@@Z` | `0x37900` | 116 | UnwindData |  |
| 36 | `??0critical_section@Concurrency@@QEAA@XZ` | `0x37980` | 114 | UnwindData |  |
| 68 | `??0reader_writer_lock@Concurrency@@QEAA@XZ` | `0x37A40` | 139 | UnwindData |  |
| 75 | `??0scoped_lock@critical_section@Concurrency@@QEAA@AEAV12@@Z` | `0x37AD0` | 142 | UnwindData |  |
| 76 | `??0scoped_lock@reader_writer_lock@Concurrency@@QEAA@AEAV12@@Z` | `0x37B60` | 142 | UnwindData |  |
| 77 | `??0scoped_lock_read@reader_writer_lock@Concurrency@@QEAA@AEAV12@@Z` | `0x37BF0` | 51 | UnwindData |  |
| 86 | `??1_NonReentrantBlockingLock@details@Concurrency@@QEAA@XZ` | `0x37C30` | 36 | UnwindData |  |
| 87 | `??1_ReentrantBlockingLock@details@Concurrency@@QEAA@XZ` | `0x37C60` | 36 | UnwindData |  |
| 88 | `??1_Scoped_lock@_NonReentrantPPLLock@details@Concurrency@@QEAA@XZ` | `0x37C90` | 28 | UnwindData |  |
| 89 | `??1_Scoped_lock@_ReentrantPPLLock@details@Concurrency@@QEAA@XZ` | `0x37CB0` | 28 | UnwindData |  |
| 95 | `??1critical_section@Concurrency@@QEAA@XZ` | `0x37CD0` | 87 | UnwindData |  |
| 97 | `??1reader_writer_lock@Concurrency@@QEAA@XZ` | `0x37D30` | 85 | UnwindData |  |
| 98 | `??1scoped_lock@critical_section@Concurrency@@QEAA@XZ` | `0x37D90` | 28 | UnwindData |  |
| 99 | `??1scoped_lock@reader_writer_lock@Concurrency@@QEAA@XZ` | `0x37DB0` | 28 | UnwindData |  |
| 100 | `??1scoped_lock_read@reader_writer_lock@Concurrency@@QEAA@XZ` | `0x37DD0` | 28 | UnwindData |  |
| 165 | `?_Acquire@_NonReentrantBlockingLock@details@Concurrency@@QEAAXXZ` | `0x38510` | 36 | UnwindData |  |
| 166 | `?_Acquire@_NonReentrantPPLLock@details@Concurrency@@QEAAXPEAX@Z` | `0x38540` | 48 | UnwindData |  |
| 167 | `?_Acquire@_ReentrantBlockingLock@details@Concurrency@@QEAAXXZ` | `0x38570` | 36 | UnwindData |  |
| 168 | `?_Acquire@_ReentrantLock@details@Concurrency@@QEAAXXZ` | `0x385A0` | 252 | UnwindData |  |
| 169 | `?_Acquire@_ReentrantPPLLock@details@Concurrency@@QEAAXPEAX@Z` | `0x386A0` | 115 | UnwindData |  |
| 170 | `?_AcquireRead@_ReaderWriterLock@details@Concurrency@@QEAAXXZ` | `0x38720` | 205 | UnwindData |  |
| 171 | `?_AcquireWrite@_ReaderWriterLock@details@Concurrency@@QEAAXXZ` | `0x387F0` | 101 | UnwindData |  |
| 223 | `?_Release@_NonReentrantBlockingLock@details@Concurrency@@QEAAXXZ` | `0x38D30` | 36 | UnwindData |  |
| 224 | `?_Release@_NonReentrantPPLLock@details@Concurrency@@QEAAXXZ` | `0x38D60` | 28 | UnwindData |  |
| 225 | `?_Release@_ReentrantBlockingLock@details@Concurrency@@QEAAXXZ` | `0x38D80` | 36 | UnwindData |  |
| 226 | `?_Release@_ReentrantLock@details@Concurrency@@QEAAXXZ` | `0x38DB0` | 115 | UnwindData |  |
| 227 | `?_Release@_ReentrantPPLLock@details@Concurrency@@QEAAXXZ` | `0x38E30` | 248 | UnwindData |  |
| 229 | `?_ReleaseRead@_ReaderWriterLock@details@Concurrency@@QEAAXXZ` | `0x38F30` | 105 | UnwindData |  |
| 230 | `?_ReleaseWrite@_ReaderWriterLock@details@Concurrency@@QEAAXXZ` | `0x38FA0` | 208 | UnwindData |  |
| 252 | `?_TryAcquire@_NonReentrantBlockingLock@details@Concurrency@@QEAA_NXZ` | `0x393C0` | 62 | UnwindData |  |
| 253 | `?_TryAcquire@_ReentrantBlockingLock@details@Concurrency@@QEAA_NXZ` | `0x39400` | 62 | UnwindData |  |
| 254 | `?_TryAcquire@_ReentrantLock@details@Concurrency@@QEAA_NXZ` | `0x39440` | 198 | UnwindData |  |
| 255 | `?_TryAcquireWrite@_ReaderWriterLock@details@Concurrency@@QEAA_NXZ` | `0x39510` | 80 | UnwindData |  |
| 257 | `?_Value@_SpinCount@details@Concurrency@@SAIXZ` | `0x397A0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 265 | `?lock@critical_section@Concurrency@@QEAAXXZ` | `0x39840` | 73 | UnwindData |  |
| 266 | `?lock@reader_writer_lock@Concurrency@@QEAAXXZ` | `0x39890` | 73 | UnwindData |  |
| 267 | `?lock_read@reader_writer_lock@Concurrency@@QEAAXXZ` | `0x398E0` | 405 | UnwindData |  |
| 268 | `?native_handle@critical_section@Concurrency@@QEAAAEAV12@XZ` | `0x39A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 278 | `?try_lock@critical_section@Concurrency@@QEAA_NXZ` | `0x39A90` | 151 | UnwindData |  |
| 279 | `?try_lock@reader_writer_lock@Concurrency@@QEAA_NXZ` | `0x39B30` | 230 | UnwindData |  |
| 280 | `?try_lock_for@critical_section@Concurrency@@QEAA_NI@Z` | `0x39C20` | 159 | UnwindData |  |
| 281 | `?try_lock_read@reader_writer_lock@Concurrency@@QEAA_NXZ` | `0x39CC0` | 89 | UnwindData |  |
| 282 | `?unlock@critical_section@Concurrency@@QEAAXXZ` | `0x39D20` | 456 | UnwindData |  |
| 283 | `?unlock@reader_writer_lock@Concurrency@@QEAAXXZ` | `0x39EF0` | 133 | UnwindData |  |
| 119 | `?CreateResourceManager@Concurrency@@YAPEAUIResourceManager@1@XZ` | `0x3BAC0` | 14 | UnwindData |  |
| 128 | `?GetExecutionContextId@Concurrency@@YAIXZ` | `0x40CF0` | 14 | UnwindData |  |
| 130 | `?GetOSVersion@Concurrency@@YA?AW4OSVersion@IResourceManager@1@XZ` | `0x41180` | 14 | UnwindData |  |
| 133 | `?GetProcessorCount@Concurrency@@YAIXZ` | `0x41190` | 14 | UnwindData |  |
| 134 | `?GetProcessorNodeCount@Concurrency@@YAIXZ` | `0x411A0` | 14 | UnwindData |  |
| 135 | `?GetSchedulerId@Concurrency@@YAIXZ` | `0x411D0` | 14 | UnwindData |  |
| 273 | `?set_task_execution_resources@Concurrency@@YAXGPEAU_GROUP_AFFINITY@@@Z` | `0x48E30` | 35 | UnwindData |  |
| 274 | `?set_task_execution_resources@Concurrency@@YAX_K@Z` | `0x48E60` | 25 | UnwindData |  |
| 118 | `?Create@Scheduler@Concurrency@@SAPEAV12@AEBVSchedulerPolicy@2@@Z` | `0x50C90` | 67 | UnwindData |  |
| 151 | `?ResetDefaultSchedulerPolicy@Scheduler@Concurrency@@SAXXZ` | `0x57070` | 15 | UnwindData |  |
| 159 | `?SetDefaultSchedulerPolicy@Scheduler@Concurrency@@SAXAEBVSchedulerPolicy@2@@Z` | `0x575D0` | 25 | UnwindData |  |
| 222 | `?_Reference@_Scheduler@details@Concurrency@@QEAAIXZ` | `0x59120` | 53 | UnwindData |  |
| 228 | `?_Release@_Scheduler@details@Concurrency@@QEAAIXZ` | `0x59160` | 53 | UnwindData |  |
| 3 | `??0SchedulerPolicy@Concurrency@@QEAA@AEBV01@@Z` | `0x591A0` | 86 | UnwindData |  |
| 4 | `??0SchedulerPolicy@Concurrency@@QEAA@XZ` | `0x59200` | 35 | UnwindData |  |
| 5 | `??0SchedulerPolicy@Concurrency@@QEAA@_KZZ` | `0x59230` | 65 | UnwindData |  |
| 80 | `??1SchedulerPolicy@Concurrency@@QEAA@XZ` | `0x59340` | 43 | UnwindData |  |
| 105 | `??4SchedulerPolicy@Concurrency@@QEAAAEAV01@AEBV01@@Z` | `0x59370` | 39 | UnwindData |  |
| 132 | `?GetPolicyValue@SchedulerPolicy@Concurrency@@QEBAIW4PolicyElementKey@2@@Z` | `0x593A0` | 90 | UnwindData |  |
| 158 | `?SetConcurrencyLimits@SchedulerPolicy@Concurrency@@QEAAXII@Z` | `0x59400` | 335 | UnwindData |  |
| 160 | `?SetPolicyValue@SchedulerPolicy@Concurrency@@QEAAIW4PolicyElementKey@2@I@Z` | `0x59550` | 211 | UnwindData |  |
| 111 | `?Alloc@Concurrency@@YAPEAX_K@Z` | `0x648E0` | 117 | UnwindData |  |
| 126 | `?Free@Concurrency@@YAXPEAX@Z` | `0x64C40` | 83 | UnwindData |  |
| 23 | `??0_StructuredTaskCollection@details@Concurrency@@QEAA@PEAV_CancellationTokenState@12@@Z` | `0x65560` | 282 | UnwindData |  |
| 24 | `??0_TaskCollection@details@Concurrency@@QEAA@PEAV_CancellationTokenState@12@@Z` | `0x65880` | 310 | UnwindData |  |
| 25 | `??0_TaskCollection@details@Concurrency@@QEAA@XZ` | `0x659C0` | 272 | UnwindData |  |
| 91 | `??1_StructuredTaskCollection@details@Concurrency@@QEAA@XZ` | `0x65D40` | 137 | UnwindData |  |
| 92 | `??1_TaskCollection@details@Concurrency@@QEAA@XZ` | `0x65DD0` | 462 | UnwindData |  |
| 164 | `?_Abort@_StructuredTaskCollection@details@Concurrency@@AEAAXXZ` | `0x66900` | 539 | UnwindData |  |
| 175 | `?_Cancel@_StructuredTaskCollection@details@Concurrency@@QEAAXXZ` | `0x671A0` | 170 | UnwindData |  |
| 176 | `?_Cancel@_TaskCollection@details@Concurrency@@QEAAXXZ` | `0x67400` | 56 | UnwindData |  |
| 178 | `?_CleanupToken@_StructuredTaskCollection@details@Concurrency@@AEAAXXZ` | `0x67780` | 182 | UnwindData |  |
| 184 | `?_Destroy@_AsyncTaskCollection@details@Concurrency@@EEAAXXZ` | `0x67950` | 95 | UnwindData |  |
| 215 | `?_IsCanceling@_StructuredTaskCollection@details@Concurrency@@QEAA_NXZ` | `0x67E60` | 234 | UnwindData |  |
| 216 | `?_IsCanceling@_TaskCollection@details@Concurrency@@QEAA_NXZ` | `0x67F50` | 405 | UnwindData |  |
| 218 | `?_NewCollection@_AsyncTaskCollection@details@Concurrency@@SAPEAV123@PEAV_CancellationTokenState@23@@Z` | `0x68260` | 83 | UnwindData |  |
| 233 | `?_RunAndWait@_StructuredTaskCollection@details@Concurrency@@QEAA?AW4_TaskCollectionStatus@23@PEAV_UnrealizedChore@23@@Z` | `0x68AE0` | 1,527 | UnwindData |  |
| 234 | `?_RunAndWait@_TaskCollection@details@Concurrency@@QEAA?AW4_TaskCollectionStatus@23@PEAV_UnrealizedChore@23@@Z` | `0x690E0` | 2,320 | UnwindData |  |
| 235 | `?_Schedule@_StructuredTaskCollection@details@Concurrency@@QEAAXPEAV_UnrealizedChore@23@@Z` | `0x699F0` | 163 | UnwindData |  |
| 236 | `?_Schedule@_StructuredTaskCollection@details@Concurrency@@QEAAXPEAV_UnrealizedChore@23@PEAVlocation@3@@Z` | `0x69AA0` | 173 | UnwindData |  |
| 237 | `?_Schedule@_TaskCollection@details@Concurrency@@QEAAXPEAV_UnrealizedChore@23@@Z` | `0x69B50` | 760 | UnwindData |  |
| 238 | `?_Schedule@_TaskCollection@details@Concurrency@@QEAAXPEAV_UnrealizedChore@23@PEAVlocation@3@@Z` | `0x69E50` | 781 | UnwindData |  |
| 26 | `??0_Timer@details@Concurrency@@IEAA@I_N@Z` | `0x6C420` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `??1_Timer@details@Concurrency@@MEAA@XZ` | `0x6C490` | 52 | UnwindData |  |
| 248 | `?_Start@_Timer@details@Concurrency@@IEAAXXZ` | `0x6C660` | 116 | UnwindData |  |
| 249 | `?_Stop@_Timer@details@Concurrency@@IEAAXXZ` | `0x6C6E0` | 41 | UnwindData |  |
| 284 | `?wait@Concurrency@@YAXI@Z` | `0x6C710` | 53 | UnwindData |  |
| 124 | `?DisableTracing@Concurrency@@YAJXZ` | `0x6CA30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `?EnableTracing@Concurrency@@YAJXZ` | `0x6CA40` | 1,008 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 189 | `?_GetConcRTTraceInfo@Concurrency@@YAPEBU_CONCRT_TRACE_INFO@details@1@XZ` | `0x6CE30` | 32 | UnwindData |  |
| 250 | `?_Trace_agents@Concurrency@@YAXW4Agents_EventType@1@_JZZ` | `0x6CF20` | 707 | UnwindData |  |
| 251 | `?_Trace_ppl_function@Concurrency@@YAXAEBU_GUID@@EW4ConcRT_EventType@1@@Z` | `0x6D1F0` | 82 | UnwindData |  |
| 22 | `??0_SpinLock@details@Concurrency@@QEAA@AECJ@Z` | `0x70DF0` | 128 | UnwindData |  |
| 90 | `??1_SpinLock@details@Concurrency@@QEAA@XZ` | `0x70E70` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `?Log2@details@Concurrency@@YAK_K@Z` | `0x71120` | 29 | UnwindData |  |
| 179 | `?_ConcRT_CoreAssert@details@Concurrency@@YAXPEBD0H@Z` | `0x714A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 180 | `?_ConcRT_Trace@details@Concurrency@@YAXHPEB_WZZ` | `0x714C0` | 320 | UnwindData |  |
| 190 | `?_GetConcurrency@details@Concurrency@@YAIXZ` | `0x71600` | 14 | UnwindData |  |
| 256 | `?_UnderlyingYield@details@Concurrency@@YAXXZ` | `0x716F0` | 69 | UnwindData |  |
| 174 | `?_Byte_reverse_table@details@Concurrency@@3QBEB` | `0x7C2B0` | 56,760 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `?ConcRT_ProviderGuid@Concurrency@@3U_GUID@@B` | `0x8A068` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `?ConcRTEventGuid@Concurrency@@3U_GUID@@B` | `0x8A078` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `?SchedulerEventGuid@Concurrency@@3U_GUID@@B` | `0x8A088` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `?ScheduleGroupEventGuid@Concurrency@@3U_GUID@@B` | `0x8A098` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `?ContextEventGuid@Concurrency@@3U_GUID@@B` | `0x8A0A8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `?ChoreEventGuid@Concurrency@@3U_GUID@@B` | `0x8A0B8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 161 | `?VirtualProcessorEventGuid@Concurrency@@3U_GUID@@B` | `0x8A0C8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `?LockEventGuid@Concurrency@@3U_GUID@@B` | `0x8A0D8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `?ResourceManagerEventGuid@Concurrency@@3U_GUID@@B` | `0x8A0E8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `?PPLParallelInvokeEventGuid@Concurrency@@3U_GUID@@B` | `0x8A0F8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `?PPLParallelForEventGuid@Concurrency@@3U_GUID@@B` | `0x8A108` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 148 | `?PPLParallelForeachEventGuid@Concurrency@@3U_GUID@@B` | `0x8A118` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `?AgentEventGuid@Concurrency@@3U_GUID@@B` | `0x8A128` | 0 | Indeterminate |  |
