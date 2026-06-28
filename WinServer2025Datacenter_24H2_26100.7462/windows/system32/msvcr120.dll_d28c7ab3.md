# Binary Specification: msvcr120.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\msvcr120.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d28c7ab34842b6149609bd4e6b566ddab8b891f0d5062480a253ef20a6a2caaa`
* **Total Exported Functions:** 1925

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 9 | `??0_Context@details@Concurrency@@QEAA@PEAVContext@2@@Z` | `0x1100` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `??0_Scheduler@details@Concurrency@@QEAA@PEAVScheduler@2@@Z` | `0x1100` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `??_F_Context@details@Concurrency@@QEAAXXZ` | `0x1108` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `??_F_Scheduler@details@Concurrency@@QEAAXXZ` | `0x1108` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | `?_GetScheduler@_Scheduler@details@Concurrency@@QEAAPEAVScheduler@3@XZ` | `0x1110` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `??4__non_rtti_object@std@@QEAAAEAV01@AEBV01@@Z` | `0x1114` | 23 | UnwindData |  |
| 121 | `??4bad_cast@std@@QEAAAEAV01@AEBV01@@Z` | `0x1114` | 23 | UnwindData |  |
| 122 | `??4bad_typeid@std@@QEAAAEAV01@AEBV01@@Z` | `0x1114` | 23 | UnwindData |  |
| 134 | `??_Fbad_cast@std@@QEAAXXZ` | `0x112C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `??_Fbad_typeid@std@@QEAAXXZ` | `0x1138` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `??4?$_SpinWait@$00@details@Concurrency@@QEAAAEAV012@AEBV012@@Z` | `0x1144` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `??4?$_SpinWait@$0A@@details@Concurrency@@QEAAAEAV012@AEBV012@@Z` | `0x1144` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | `??_F?$_SpinWait@$00@details@Concurrency@@QEAAXXZ` | `0x1158` | 880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `??_F?$_SpinWait@$0A@@details@Concurrency@@QEAAXXZ` | `0x1158` | 880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0?$_SpinWait@$00@details@Concurrency@@QEAA@P6AXXZ@Z` | `0x14C8` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0?$_SpinWait@$0A@@details@Concurrency@@QEAA@P6AXXZ@Z` | `0x14C8` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 241 | `?_SpinOnce@?$_SpinWait@$00@details@Concurrency@@QEAA_NXZ` | `0x14D4` | 163 | UnwindData |  |
| 199 | `?_DoYield@?$_SpinWait@$00@details@Concurrency@@IEAAXXZ` | `0x1578` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 227 | `?_Reset@?$_SpinWait@$00@details@Concurrency@@IEAAXXZ` | `0x157C` | 36 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 214 | `?_NumberOfSpins@?$_SpinWait@$00@details@Concurrency@@IEAAKXZ` | `0x15A0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 215 | `?_NumberOfSpins@?$_SpinWait@$0A@@details@Concurrency@@IEAAKXZ` | `0x15A0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 239 | `?_ShouldSpinAgain@?$_SpinWait@$00@details@Concurrency@@IEAA_NXZ` | `0x15A8` | 268 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 240 | `?_ShouldSpinAgain@?$_SpinWait@$0A@@details@Concurrency@@IEAA_NXZ` | `0x15A8` | 268 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 236 | `?_SetSpinCount@?$_SpinWait@$00@details@Concurrency@@QEAAXI@Z` | `0x16B4` | 344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 198 | `?_Destroy@_AsyncTaskCollection@details@Concurrency@@EEAAXXZ` | `0x180C` | 24 | UnwindData |  |
| 190 | `?_CheckTaskCollection@_UnrealizedChore@details@Concurrency@@IEAAXXZ` | `0x1B70` | 108 | UnwindData |  |
| 164 | `?Id@Context@Concurrency@@SAIXZ` | `0x22E0` | 58 | UnwindData |  |
| 178 | `?VirtualProcessorId@Context@Concurrency@@SAIXZ` | `0x231C` | 59 | UnwindData |  |
| 172 | `?ScheduleGroupId@Context@Concurrency@@SAIXZ` | `0x2358` | 59 | UnwindData |  |
| 141 | `?Block@Context@Concurrency@@SAXXZ` | `0x2394` | 23 | UnwindData |  |
| 179 | `?Yield@Context@Concurrency@@SAXXZ` | `0x23AC` | 55 | UnwindData |  |
| 260 | `?_Yield@_Context@details@Concurrency@@SAXXZ` | `0x23AC` | 55 | UnwindData |  |
| 243 | `?_SpinYield@Context@Concurrency@@SAXXZ` | `0x23E4` | 55 | UnwindData |  |
| 167 | `?IsCurrentTaskCollectionCanceling@Context@Concurrency@@SA_NXZ` | `0x241C` | 96 | UnwindData |  |
| 148 | `?CurrentContext@Context@Concurrency@@SAPEAV12@XZ` | `0x247C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `?Oversubscribe@Context@Concurrency@@SAX_N@Z` | `0x2484` | 62 | UnwindData |  |
| 216 | `?_Oversubscribe@_Context@details@Concurrency@@SAX_N@Z` | `0x2484` | 62 | UnwindData |  |
| 196 | `?_CurrentContext@_Context@details@Concurrency@@SA?AV123@XZ` | `0x24C4` | 55 | UnwindData |  |
| 210 | `?_IsSynchronouslyBlocked@_Context@details@Concurrency@@QEBA_NXZ` | `0x24FC` | 5,772 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 217 | `?_Reference@_Scheduler@details@Concurrency@@QEAAIXZ` | `0x24FC` | 5,772 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `??0_Cancellation_beacon@details@Concurrency@@QEAA@XZ` | `0x3B88` | 445 | UnwindData |  |
| 92 | `??1_Cancellation_beacon@details@Concurrency@@QEAA@XZ` | `0x3D48` | 49 | UnwindData |  |
| 194 | `?_Confirm_cancel@_Cancellation_beacon@details@Concurrency@@QEAA_NXZ` | `0x3D7C` | 81 | UnwindData |  |
| 204 | `?_GetCurrentInlineDepth@_StackGuard@details@Concurrency@@CAAEA_KXZ` | `0x3DD0` | 47 | UnwindData |  |
| 242 | `?_SpinOnce@?$_SpinWait@$0A@@details@Concurrency@@QEAA_NXZ` | `0x41D8` | 1,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 200 | `?_DoYield@?$_SpinWait@$0A@@details@Concurrency@@IEAAXXZ` | `0x47C0` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 228 | `?_Reset@?$_SpinWait@$0A@@details@Concurrency@@IEAAXXZ` | `0x47C4` | 184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 237 | `?_SetSpinCount@?$_SpinWait@$0A@@details@Concurrency@@QEAAXI@Z` | `0x487C` | 108 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 165 | `?Id@CurrentScheduler@Concurrency@@SAIXZ` | `0x48E8` | 36 | UnwindData |  |
| 156 | `?GetNumberOfVirtualProcessors@CurrentScheduler@Concurrency@@SAIXZ` | `0x490C` | 36 | UnwindData |  |
| 158 | `?GetPolicy@CurrentScheduler@Concurrency@@SA?AVSchedulerPolicy@2@XZ` | `0x4930` | 41 | UnwindData |  |
| 153 | `?Get@CurrentScheduler@Concurrency@@SAPEAVScheduler@2@XZ` | `0x495C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `?Create@CurrentScheduler@Concurrency@@SAXAEBVSchedulerPolicy@2@@Z` | `0x4964` | 37 | UnwindData |  |
| 149 | `?Detach@CurrentScheduler@Concurrency@@SAXXZ` | `0x498C` | 184 | UnwindData |  |
| 170 | `?RegisterShutdownEvent@CurrentScheduler@Concurrency@@SAXPEAX@Z` | `0x4A68` | 65 | UnwindData |  |
| 147 | `?CreateScheduleGroup@CurrentScheduler@Concurrency@@SAPEAVScheduleGroup@2@XZ` | `0x4AAC` | 23 | UnwindData |  |
| 146 | `?CreateScheduleGroup@CurrentScheduler@Concurrency@@SAPEAVScheduleGroup@2@AEAVlocation@2@@Z` | `0x4AC4` | 32 | UnwindData |  |
| 173 | `?ScheduleTask@CurrentScheduler@Concurrency@@SAXP6AXPEAX@Z0@Z` | `0x4AE4` | 47 | UnwindData |  |
| 235 | `?_ScheduleTask@_CurrentScheduler@details@Concurrency@@SAXP6AXPEAX@Z0@Z` | `0x4AE4` | 47 | UnwindData |  |
| 174 | `?ScheduleTask@CurrentScheduler@Concurrency@@SAXP6AXPEAX@Z0AEAVlocation@2@@Z` | `0x4B14` | 63 | UnwindData |  |
| 166 | `?IsAvailableLocation@CurrentScheduler@Concurrency@@SA_NAEBVlocation@2@@Z` | `0x4B54` | 40 | UnwindData |  |
| 207 | `?_Id@_CurrentScheduler@details@Concurrency@@SAIXZ` | `0x4B7C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 205 | `?_GetNumberOfVirtualProcessors@_CurrentScheduler@details@Concurrency@@SAIXZ` | `0x4B84` | 23 | UnwindData |  |
| 201 | `?_Get@_CurrentScheduler@details@Concurrency@@SA?AV_Scheduler@23@XZ` | `0x4B9C` | 26 | UnwindData |  |
| 105 | `??1critical_section@Concurrency@@QEAA@XZ` | `0x4BB8` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `??1reader_writer_lock@Concurrency@@QEAA@XZ` | `0x4BB8` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 648 | `_freea` | `0x4BBC` | 31 | UnwindData |  |
| 649 | `_freea_s` | `0x4BBC` | 31 | UnwindData |  |
| 163 | `?GetSharedTimerQueue@details@Concurrency@@YAPEAXXZ` | `0x4BDC` | 200 | UnwindData |  |
| 8 | `??0_Condition_variable@details@Concurrency@@QEAA@XZ` | `0x4E74` | 44 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `??1_Condition_variable@details@Concurrency@@QEAA@XZ` | `0x4EA0` | 58 | UnwindData |  |
| 318 | `?wait@_Condition_variable@details@Concurrency@@QEAAXAEAVcritical_section@3@@Z` | `0x4EDC` | 211 | UnwindData |  |
| 320 | `?wait_for@_Condition_variable@details@Concurrency@@QEAA_NAEAVcritical_section@3@I@Z` | `0x4FB0` | 478 | UnwindData |  |
| 298 | `?notify_one@_Condition_variable@details@Concurrency@@QEAAXXZ` | `0x5190` | 173 | UnwindData |  |
| 297 | `?notify_all@_Condition_variable@details@Concurrency@@QEAAXXZ` | `0x5240` | 127 | UnwindData |  |
| 42 | `??0event@Concurrency@@QEAA@XZ` | `0x52C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `??1event@Concurrency@@QEAA@XZ` | `0x52F0` | 139 | UnwindData |  |
| 319 | `?wait@event@Concurrency@@QEAA_KI@Z` | `0x537C` | 309 | UnwindData |  |
| 300 | `?reset@event@Concurrency@@QEAAXXZ` | `0x54B4` | 135 | UnwindData |  |
| 301 | `?set@event@Concurrency@@QEAAXXZ` | `0x553C` | 506 | UnwindData |  |
| 321 | `?wait_for_multiple@event@Concurrency@@SA_KPEAPEAV12@_K_NI@Z` | `0x5738` | 1,062 | UnwindData |  |
| 81 | `??0scheduler_resource_allocation_error@Concurrency@@QEAA@PEBDJ@Z` | `0x616C` | 58 | UnwindData |  |
| 80 | `??0scheduler_resource_allocation_error@Concurrency@@QEAA@J@Z` | `0x61A8` | 47 | UnwindData |  |
| 291 | `?get_error_code@scheduler_resource_allocation_error@Concurrency@@QEBAJXZ` | `0x61D8` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `??0scheduler_worker_creation_error@Concurrency@@QEAA@PEBDJ@Z` | `0x61DC` | 33 | UnwindData |  |
| 82 | `??0scheduler_worker_creation_error@Concurrency@@QEAA@J@Z` | `0x6200` | 33 | UnwindData |  |
| 89 | `??0unsupported_os@Concurrency@@QEAA@PEBD@Z` | `0x6224` | 42 | UnwindData |  |
| 90 | `??0unsupported_os@Concurrency@@QEAA@XZ` | `0x6250` | 33 | UnwindData |  |
| 78 | `??0scheduler_not_attached@Concurrency@@QEAA@PEBD@Z` | `0x6274` | 42 | UnwindData |  |
| 79 | `??0scheduler_not_attached@Concurrency@@QEAA@XZ` | `0x62A0` | 33 | UnwindData |  |
| 49 | `??0improper_scheduler_attach@Concurrency@@QEAA@PEBD@Z` | `0x62C4` | 42 | UnwindData |  |
| 50 | `??0improper_scheduler_attach@Concurrency@@QEAA@XZ` | `0x62F0` | 33 | UnwindData |  |
| 51 | `??0improper_scheduler_detach@Concurrency@@QEAA@PEBD@Z` | `0x6314` | 42 | UnwindData |  |
| 52 | `??0improper_scheduler_detach@Concurrency@@QEAA@XZ` | `0x6340` | 33 | UnwindData |  |
| 53 | `??0improper_scheduler_reference@Concurrency@@QEAA@PEBD@Z` | `0x6364` | 42 | UnwindData |  |
| 54 | `??0improper_scheduler_reference@Concurrency@@QEAA@XZ` | `0x6390` | 33 | UnwindData |  |
| 40 | `??0default_scheduler_exists@Concurrency@@QEAA@PEBD@Z` | `0x63B4` | 42 | UnwindData |  |
| 41 | `??0default_scheduler_exists@Concurrency@@QEAA@XZ` | `0x63E0` | 33 | UnwindData |  |
| 37 | `??0context_unblock_unbalanced@Concurrency@@QEAA@PEBD@Z` | `0x6404` | 42 | UnwindData |  |
| 38 | `??0context_unblock_unbalanced@Concurrency@@QEAA@XZ` | `0x6430` | 33 | UnwindData |  |
| 35 | `??0context_self_unblock@Concurrency@@QEAA@PEBD@Z` | `0x6454` | 42 | UnwindData |  |
| 36 | `??0context_self_unblock@Concurrency@@QEAA@XZ` | `0x6480` | 33 | UnwindData |  |
| 71 | `??0missing_wait@Concurrency@@QEAA@PEBD@Z` | `0x64A4` | 42 | UnwindData |  |
| 72 | `??0missing_wait@Concurrency@@QEAA@XZ` | `0x64D0` | 33 | UnwindData |  |
| 31 | `??0bad_target@Concurrency@@QEAA@PEBD@Z` | `0x64F4` | 42 | UnwindData |  |
| 32 | `??0bad_target@Concurrency@@QEAA@XZ` | `0x6520` | 33 | UnwindData |  |
| 69 | `??0message_not_found@Concurrency@@QEAA@PEBD@Z` | `0x6544` | 42 | UnwindData |  |
| 70 | `??0message_not_found@Concurrency@@QEAA@XZ` | `0x6570` | 33 | UnwindData |  |
| 55 | `??0invalid_link_target@Concurrency@@QEAA@PEBD@Z` | `0x6594` | 42 | UnwindData |  |
| 56 | `??0invalid_link_target@Concurrency@@QEAA@XZ` | `0x65C0` | 33 | UnwindData |  |
| 63 | `??0invalid_scheduler_policy_key@Concurrency@@QEAA@PEBD@Z` | `0x65E4` | 42 | UnwindData |  |
| 64 | `??0invalid_scheduler_policy_key@Concurrency@@QEAA@XZ` | `0x6610` | 33 | UnwindData |  |
| 67 | `??0invalid_scheduler_policy_value@Concurrency@@QEAA@PEBD@Z` | `0x6634` | 42 | UnwindData |  |
| 68 | `??0invalid_scheduler_policy_value@Concurrency@@QEAA@XZ` | `0x6660` | 33 | UnwindData |  |
| 65 | `??0invalid_scheduler_policy_thread_specification@Concurrency@@QEAA@PEBD@Z` | `0x6684` | 42 | UnwindData |  |
| 66 | `??0invalid_scheduler_policy_thread_specification@Concurrency@@QEAA@XZ` | `0x66B0` | 33 | UnwindData |  |
| 59 | `??0invalid_operation@Concurrency@@QEAA@PEBD@Z` | `0x66D4` | 42 | UnwindData |  |
| 60 | `??0invalid_operation@Concurrency@@QEAA@XZ` | `0x6700` | 33 | UnwindData |  |
| 73 | `??0nested_scheduler_missing_detach@Concurrency@@QEAA@PEBD@Z` | `0x6724` | 42 | UnwindData |  |
| 74 | `??0nested_scheduler_missing_detach@Concurrency@@QEAA@XZ` | `0x6750` | 33 | UnwindData |  |
| 75 | `??0operation_timed_out@Concurrency@@QEAA@PEBD@Z` | `0x6774` | 42 | UnwindData |  |
| 76 | `??0operation_timed_out@Concurrency@@QEAA@XZ` | `0x67A0` | 33 | UnwindData |  |
| 57 | `??0invalid_multiple_scheduling@Concurrency@@QEAA@PEBD@Z` | `0x67C4` | 42 | UnwindData |  |
| 58 | `??0invalid_multiple_scheduling@Concurrency@@QEAA@XZ` | `0x67F0` | 33 | UnwindData |  |
| 61 | `??0invalid_oversubscribe_operation@Concurrency@@QEAA@PEBD@Z` | `0x6814` | 42 | UnwindData |  |
| 62 | `??0invalid_oversubscribe_operation@Concurrency@@QEAA@XZ` | `0x6840` | 33 | UnwindData |  |
| 47 | `??0improper_lock@Concurrency@@QEAA@PEBD@Z` | `0x6864` | 42 | UnwindData |  |
| 48 | `??0improper_lock@Concurrency@@QEAA@XZ` | `0x6890` | 33 | UnwindData |  |
| 87 | `??0task_canceled@Concurrency@@QEAA@PEBD@Z` | `0x68B4` | 42 | UnwindData |  |
| 88 | `??0task_canceled@Concurrency@@QEAA@XZ` | `0x68E0` | 33 | UnwindData |  |
| 10 | `??0_Interruption_exception@details@Concurrency@@QEAA@PEBD@Z` | `0x6904` | 42 | UnwindData |  |
| 11 | `??0_Interruption_exception@details@Concurrency@@QEAA@XZ` | `0x6930` | 33 | UnwindData |  |
| 150 | `?DisableTracing@Concurrency@@YAJXZ` | `0x70A0` | 10,676 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | `?EnableTracing@Concurrency@@YAJXZ` | `0x70A0` | 10,676 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 323 | `_CRT_RTC_INIT` | `0x70A0` | 10,676 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 324 | `_CRT_RTC_INITW` | `0x70A0` | 10,676 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 290 | `?from_numa_node@location@Concurrency@@SA?AV12@G@Z` | `0x9A54` | 87 | UnwindData |  |
| 289 | `?current@location@Concurrency@@SA?AV12@XZ` | `0x9AF8` | 134 | UnwindData |  |
| 197 | `?_Current_node@location@Concurrency@@SA?AV12@XZ` | `0x9B80` | 131 | UnwindData |  |
| 154 | `?GetCurrentThreadId@platform@details@Concurrency@@YAJXZ` | `0xA738` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 472 | `__threadid` | `0xA738` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `?CaptureCallstack@platform@details@Concurrency@@YA_KPEAPEAX_K1@Z` | `0xA740` | 32 | UnwindData |  |
| 259 | `?_Value@_SpinCount@details@Concurrency@@SAIXZ` | `0xA760` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `??0_NonReentrantBlockingLock@details@Concurrency@@QEAA@XZ` | `0xA768` | 32 | UnwindData |  |
| 15 | `??0_ReentrantBlockingLock@details@Concurrency@@QEAA@XZ` | `0xA768` | 32 | UnwindData |  |
| 94 | `??1_NonReentrantBlockingLock@details@Concurrency@@QEAA@XZ` | `0xA788` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `??1_ReentrantBlockingLock@details@Concurrency@@QEAA@XZ` | `0xA788` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `?_Acquire@_NonReentrantBlockingLock@details@Concurrency@@QEAAXXZ` | `0xA790` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `?_Acquire@_ReentrantBlockingLock@details@Concurrency@@QEAAXXZ` | `0xA790` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 249 | `?_TryAcquire@_NonReentrantBlockingLock@details@Concurrency@@QEAA_NXZ` | `0xA798` | 20 | UnwindData |  |
| 250 | `?_TryAcquire@_ReentrantBlockingLock@details@Concurrency@@QEAA_NXZ` | `0xA798` | 20 | UnwindData |  |
| 218 | `?_Release@_NonReentrantBlockingLock@details@Concurrency@@QEAAXXZ` | `0xA7AC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 220 | `?_Release@_ReentrantBlockingLock@details@Concurrency@@QEAAXXZ` | `0xA7AC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `??0_ReentrantLock@details@Concurrency@@QEAA@XZ` | `0xA7B4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | `?_Acquire@_ReentrantLock@details@Concurrency@@QEAAXXZ` | `0xA7C4` | 85 | UnwindData |  |
| 251 | `?_TryAcquire@_ReentrantLock@details@Concurrency@@QEAA_NXZ` | `0xA81C` | 45 | UnwindData |  |
| 221 | `?_Release@_ReentrantLock@details@Concurrency@@QEAAXXZ` | `0xA84C` | 48 | UnwindData |  |
| 13 | `??0_NonReentrantPPLLock@details@Concurrency@@QEAA@XZ` | `0xA87C` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `??0critical_section@Concurrency@@QEAA@XZ` | `0xA87C` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 182 | `?_Acquire@_NonReentrantPPLLock@details@Concurrency@@QEAAXPEAX@Z` | `0xA8A4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 219 | `?_Release@_NonReentrantPPLLock@details@Concurrency@@QEAAXXZ` | `0xA8AC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `??0_ReentrantPPLLock@details@Concurrency@@QEAA@XZ` | `0xA8B4` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `?_Acquire@_ReentrantPPLLock@details@Concurrency@@QEAAXPEAX@Z` | `0xA8E4` | 83 | UnwindData |  |
| 222 | `?_Release@_ReentrantPPLLock@details@Concurrency@@QEAAXXZ` | `0xA938` | 26 | UnwindData |  |
| 14 | `??0_ReaderWriterLock@details@Concurrency@@QEAA@XZ` | `0xA954` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `?_AcquireRead@_ReaderWriterLock@details@Concurrency@@QEAAXXZ` | `0xA968` | 56 | UnwindData |  |
| 224 | `?_ReleaseRead@_ReaderWriterLock@details@Concurrency@@QEAAXXZ` | `0xA9A0` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 187 | `?_AcquireWrite@_ReaderWriterLock@details@Concurrency@@QEAAXXZ` | `0xA9A4` | 55 | UnwindData |  |
| 225 | `?_ReleaseWrite@_ReaderWriterLock@details@Concurrency@@QEAAXXZ` | `0xA9DC` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 252 | `?_TryAcquireWrite@_ReaderWriterLock@details@Concurrency@@QEAA_NXZ` | `0xA9E8` | 808 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `??0_Scoped_lock@_NonReentrantPPLLock@details@Concurrency@@QEAA@AEAV123@@Z` | `0xAD10` | 102 | UnwindData |  |
| 96 | `??1_Scoped_lock@_NonReentrantPPLLock@details@Concurrency@@QEAA@XZ` | `0xAD78` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `??1scoped_lock@critical_section@Concurrency@@QEAA@XZ` | `0xAD78` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `??0_Scoped_lock@_ReentrantPPLLock@details@Concurrency@@QEAA@AEAV123@@Z` | `0xAD80` | 99 | UnwindData |  |
| 97 | `??1_Scoped_lock@_ReentrantPPLLock@details@Concurrency@@QEAA@XZ` | `0xADE4` | 29 | UnwindData |  |
| 296 | `?native_handle@critical_section@Concurrency@@QEAAAEAV12@XZ` | `0xAE04` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 292 | `?lock@critical_section@Concurrency@@QEAAXXZ` | `0xAE08` | 82 | UnwindData |  |
| 310 | `?try_lock@critical_section@Concurrency@@QEAA_NXZ` | `0xAE5C` | 194 | UnwindData |  |
| 312 | `?try_lock_for@critical_section@Concurrency@@QEAA_NI@Z` | `0xAF20` | 172 | UnwindData |  |
| 315 | `?unlock@critical_section@Concurrency@@QEAAXXZ` | `0xAFCC` | 276 | UnwindData |  |
| 84 | `??0scoped_lock@critical_section@Concurrency@@QEAA@AEAV12@@Z` | `0xB384` | 102 | UnwindData |  |
| 77 | `??0reader_writer_lock@Concurrency@@QEAA@XZ` | `0xB3EC` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 293 | `?lock@reader_writer_lock@Concurrency@@QEAAXXZ` | `0xB41C` | 82 | UnwindData |  |
| 311 | `?try_lock@reader_writer_lock@Concurrency@@QEAA_NXZ` | `0xB470` | 220 | UnwindData |  |
| 294 | `?lock_read@reader_writer_lock@Concurrency@@QEAAXXZ` | `0xB54C` | 329 | UnwindData |  |
| 313 | `?try_lock_read@reader_writer_lock@Concurrency@@QEAA_NXZ` | `0xB698` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 316 | `?unlock@reader_writer_lock@Concurrency@@QEAAXXZ` | `0xB6B4` | 81 | UnwindData |  |
| 85 | `??0scoped_lock@reader_writer_lock@Concurrency@@QEAA@AEAV12@@Z` | `0xBA98` | 102 | UnwindData |  |
| 110 | `??1scoped_lock@reader_writer_lock@Concurrency@@QEAA@XZ` | `0xBB00` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `??1scoped_lock_read@reader_writer_lock@Concurrency@@QEAA@XZ` | `0xBB00` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `??0scoped_lock_read@reader_writer_lock@Concurrency@@QEAA@AEAV12@@Z` | `0xBB08` | 29 | UnwindData |  |
| 157 | `?GetOSVersion@Concurrency@@YA?AW4OSVersion@IResourceManager@1@XZ` | `0xBD00` | 128 | UnwindData |  |
| 145 | `?CreateResourceManager@Concurrency@@YAPEAUIResourceManager@1@XZ` | `0xBD80` | 265 | UnwindData |  |
| 160 | `?GetProcessorCount@Concurrency@@YAIXZ` | `0xBE8C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 203 | `?_GetConcurrency@details@Concurrency@@YAIXZ` | `0xBE8C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 161 | `?GetProcessorNodeCount@Concurrency@@YAIXZ` | `0xBE94` | 130 | UnwindData |  |
| 162 | `?GetSchedulerId@Concurrency@@YAIXZ` | `0xBF18` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `?GetExecutionContextId@Concurrency@@YAIXZ` | `0xBF28` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 304 | `?set_task_execution_resources@Concurrency@@YAX_K@Z` | `0xBF38` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 303 | `?set_task_execution_resources@Concurrency@@YAXGPEAU_GROUP_AFFINITY@@@Z` | `0xBF40` | 26,960 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `?Create@Scheduler@Concurrency@@SAPEAV12@AEBVSchedulerPolicy@2@@Z` | `0x12890` | 40 | UnwindData |  |
| 176 | `?SetDefaultSchedulerPolicy@Scheduler@Concurrency@@SAXAEBVSchedulerPolicy@2@@Z` | `0x128B8` | 248 | UnwindData |  |
| 171 | `?ResetDefaultSchedulerPolicy@Scheduler@Concurrency@@SAXXZ` | `0x129B0` | 114 | UnwindData |  |
| 223 | `?_Release@_Scheduler@details@Concurrency@@QEAAIXZ` | `0x16858` | 584 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `??0SchedulerPolicy@Concurrency@@QEAA@XZ` | `0x16AA0` | 28 | UnwindData |  |
| 6 | `??0SchedulerPolicy@Concurrency@@QEAA@_KZZ` | `0x16ABC` | 49 | UnwindData |  |
| 4 | `??0SchedulerPolicy@Concurrency@@QEAA@AEBV01@@Z` | `0x16CC4` | 70 | UnwindData |  |
| 119 | `??4SchedulerPolicy@Concurrency@@QEAAAEAV01@AEBV01@@Z` | `0x16D0C` | 36 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `??1SchedulerPolicy@Concurrency@@QEAA@XZ` | `0x16D30` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `?GetPolicyValue@SchedulerPolicy@Concurrency@@QEBAIW4PolicyElementKey@2@@Z` | `0x16D38` | 75 | UnwindData |  |
| 177 | `?SetPolicyValue@SchedulerPolicy@Concurrency@@QEAAIW4PolicyElementKey@2@I@Z` | `0x16D84` | 202 | UnwindData |  |
| 175 | `?SetConcurrencyLimits@SchedulerPolicy@Concurrency@@QEAAXII@Z` | `0x16E50` | 178 | UnwindData |  |
| 140 | `?Alloc@Concurrency@@YAPEAX_K@Z` | `0x1B56C` | 142 | UnwindData |  |
| 152 | `?Free@Concurrency@@YAXPEAX@Z` | `0x1B5FC` | 68 | UnwindData |  |
| 22 | `??0_StructuredTaskCollection@details@Concurrency@@QEAA@PEAV_CancellationTokenState@12@@Z` | `0x1B9C8` | 159 | UnwindData |  |
| 99 | `??1_StructuredTaskCollection@details@Concurrency@@QEAA@XZ` | `0x1BA68` | 101 | UnwindData |  |
| 232 | `?_Schedule@_StructuredTaskCollection@details@Concurrency@@QEAAXPEAV_UnrealizedChore@23@PEAVlocation@3@@Z` | `0x1BAD8` | 152 | UnwindData |  |
| 231 | `?_Schedule@_StructuredTaskCollection@details@Concurrency@@QEAAXPEAV_UnrealizedChore@23@@Z` | `0x1BB94` | 136 | UnwindData |  |
| 229 | `?_RunAndWait@_StructuredTaskCollection@details@Concurrency@@QEAA?AW4_TaskCollectionStatus@23@PEAV_UnrealizedChore@23@@Z` | `0x1BC1C` | 732 | UnwindData |  |
| 191 | `?_CleanupToken@_StructuredTaskCollection@details@Concurrency@@AEAAXXZ` | `0x1BEF8` | 82 | UnwindData |  |
| 180 | `?_Abort@_StructuredTaskCollection@details@Concurrency@@AEAAXXZ` | `0x1BF4C` | 239 | UnwindData |  |
| 188 | `?_Cancel@_StructuredTaskCollection@details@Concurrency@@QEAAXXZ` | `0x1C03C` | 224 | UnwindData |  |
| 208 | `?_IsCanceling@_StructuredTaskCollection@details@Concurrency@@QEAA_NXZ` | `0x1C11C` | 204 | UnwindData |  |
| 24 | `??0_TaskCollection@details@Concurrency@@QEAA@XZ` | `0x1C30C` | 312 | UnwindData |  |
| 23 | `??0_TaskCollection@details@Concurrency@@QEAA@PEAV_CancellationTokenState@12@@Z` | `0x1C444` | 325 | UnwindData |  |
| 100 | `??1_TaskCollection@details@Concurrency@@QEAA@XZ` | `0x1C634` | 255 | UnwindData |  |
| 234 | `?_Schedule@_TaskCollection@details@Concurrency@@QEAAXPEAV_UnrealizedChore@23@PEAVlocation@3@@Z` | `0x1CCB8` | 295 | UnwindData |  |
| 233 | `?_Schedule@_TaskCollection@details@Concurrency@@QEAAXPEAV_UnrealizedChore@23@@Z` | `0x1CDE0` | 275 | UnwindData |  |
| 189 | `?_Cancel@_TaskCollection@details@Concurrency@@QEAAXXZ` | `0x1D028` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 230 | `?_RunAndWait@_TaskCollection@details@Concurrency@@QEAA?AW4_TaskCollectionStatus@23@PEAV_UnrealizedChore@23@@Z` | `0x1D03C` | 1,134 | UnwindData |  |
| 209 | `?_IsCanceling@_TaskCollection@details@Concurrency@@QEAA_NXZ` | `0x1D918` | 235 | UnwindData |  |
| 213 | `?_NewCollection@_AsyncTaskCollection@details@Concurrency@@SAPEAV123@PEAV_CancellationTokenState@23@@Z` | `0x1DAB0` | 134 | UnwindData |  |
| 226 | `?_ReportUnobservedException@details@Concurrency@@YAXXZ` | `0x1DB9C` | 84 | UnwindData |  |
| 238 | `?_SetUnobservedExceptionHandler@details@Concurrency@@YAXP6AXXZ@Z` | `0x1DBF0` | 3,188 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `??0_Timer@details@Concurrency@@IEAA@I_N@Z` | `0x1E864` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 244 | `?_Start@_Timer@details@Concurrency@@IEAAXXZ` | `0x1E880` | 305 | UnwindData |  |
| 101 | `??1_Timer@details@Concurrency@@MEAA@XZ` | `0x1E9B4` | 31 | UnwindData |  |
| 245 | `?_Stop@_Timer@details@Concurrency@@IEAAXXZ` | `0x1E9D4` | 62 | UnwindData |  |
| 317 | `?wait@Concurrency@@YAXI@Z` | `0x1EA14` | 186 | UnwindData |  |
| 202 | `?_GetConcRTTraceInfo@Concurrency@@YAPEBU_CONCRT_TRACE_INFO@details@1@XZ` | `0x1EE64` | 31 | UnwindData |  |
| 248 | `?_Trace_ppl_function@Concurrency@@YAXAEBU_GUID@@EW4ConcRT_EventType@1@@Z` | `0x1EE84` | 194 | UnwindData |  |
| 247 | `?_Trace_agents@Concurrency@@YAXW4Agents_EventType@1@_JZZ` | `0x1EF48` | 300 | UnwindData |  |
| 255 | `?_UnderlyingYield@details@Concurrency@@YAXXZ` | `0x1F074` | 62 | UnwindData |  |
| 192 | `?_ConcRT_CoreAssert@details@Concurrency@@YAXPEBD0H@Z` | `0x1F10C` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 193 | `?_ConcRT_Trace@details@Concurrency@@YAXHPEB_WZZ` | `0x1F110` | 207 | UnwindData |  |
| 21 | `??0_SpinLock@details@Concurrency@@QEAA@AECJ@Z` | `0x1F1E0` | 81 | UnwindData |  |
| 98 | `??1_SpinLock@details@Concurrency@@QEAA@XZ` | `0x1F234` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `?Log2@details@Concurrency@@YAK_K@Z` | `0x1F23C` | 8,020 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 277 | `?_query_new_handler@@YAP6AH_K@ZXZ` | `0x21190` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 279 | `?_set_new_handler@@YAP6AH_K@ZH@Z` | `0x211A0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 280 | `?_set_new_handler@@YAP6AH_K@ZP6AH0@Z@Z` | `0x211A8` | 79 | UnwindData |  |
| 521 | `_callnewh` | `0x211F8` | 51 | UnwindData |  |
| 302 | `?set_new_handler@@YAP6AXXZP6AXXZ@Z` | `0x21234` | 18 | UnwindData |  |
| 278 | `?_query_new_mode@@YAHXZ` | `0x21248` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 281 | `?_set_new_mode@@YAHH@Z` | `0x21250` | 47 | UnwindData |  |
| 464 | `__set_app_type` | `0x21280` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1079 | `_set_error_mode` | `0x21288` | 64 | UnwindData |  |
| 261 | `?__ExceptionPtrAssign@@YAXPEAXPEBX@Z` | `0x22024` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 262 | `?__ExceptionPtrCompare@@YA_NPEBX0@Z` | `0x2202C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 263 | `?__ExceptionPtrCopy@@YAXPEAXPEBX@Z` | `0x22038` | 35 | UnwindData |  |
| 264 | `?__ExceptionPtrCopyException@@YAXPEAXPEBX1@Z` | `0x2205C` | 78 | UnwindData |  |
| 265 | `?__ExceptionPtrCreate@@YAXPEAX@Z` | `0x220AC` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 266 | `?__ExceptionPtrCurrentException@@YAXPEAX@Z` | `0x220BC` | 107 | UnwindData |  |
| 267 | `?__ExceptionPtrDestroy@@YAXPEAX@Z` | `0x22128` | 50 | UnwindData |  |
| 268 | `?__ExceptionPtrRethrow@@YAXPEBX@Z` | `0x2215C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 269 | `?__ExceptionPtrSwap@@YAXPEAX0@Z` | `0x22164` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 270 | `?__ExceptionPtrToBool@@YA_NPEBX@Z` | `0x22184` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 466 | `__setusermatherr` | `0x22190` | 29 | UnwindData |  |
| 499 | `_amsg_exit` | `0x225C0` | 38 | UnwindData |  |
| 519 | `_c_exit` | `0x225E8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 523 | `_cexit` | `0x225F8` | 88 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 601 | `_exit` | `0x22650` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 690 | `_get_pgmptr` | `0x2265C` | 54 | UnwindData |  |
| 697 | `_get_wpgmptr` | `0x22694` | 54 | UnwindData |  |
| 738 | `_initterm` | `0x22718` | 96 | UnwindData |  |
| 739 | `_initterm_e` | `0x22778` | 57 | UnwindData |  |
| 1561 | `exit` | `0x229AC` | 472 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 425 | `__getmainargs` | `0x22B84` | 110 | UnwindData |  |
| 436 | `__p___argc` | `0x22BF4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 437 | `__p___argv` | `0x22BFC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 438 | `__p___initenv` | `0x22C04` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 439 | `__p___mb_cur_max` | `0x22C0C` | 59 | UnwindData |  |
| 440 | `__p___wargv` | `0x22C48` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 441 | `__p___winitenv` | `0x22C50` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 442 | `__p__acmdln` | `0x22C58` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 443 | `__p__commode` | `0x22C60` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 444 | `__p__daylight` | `0x22C68` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 445 | `__p__dstbias` | `0x22C70` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 446 | `__p__environ` | `0x22C78` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 447 | `__p__fmode` | `0x22C80` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 449 | `__p__mbcasemap` | `0x22C88` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 450 | `__p__mbctype` | `0x22C90` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 451 | `__p__pctype` | `0x22C98` | 59 | UnwindData |  |
| 452 | `__p__pgmptr` | `0x22CD4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 453 | `__p__pwctype` | `0x22CDC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 454 | `__p__timezone` | `0x22CE4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 455 | `__p__tzname` | `0x22CEC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 456 | `__p__wcmdln` | `0x22CF4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 457 | `__p__wenviron` | `0x22CFC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 458 | `__p__wpgmptr` | `0x22D04` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 485 | `__wgetmainargs` | `0x22D0C` | 157 | UnwindData |  |
| 860 | `_lock` | `0x22DAC` | 68 | UnwindData |  |
| 1224 | `_unlock` | `0x22F9C` | 712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 423 | `__get_flsindex` | `0x23264` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 424 | `__get_tlsindex` | `0x23264` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 471 | `__threadhandle` | `0x2326C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 650 | `_freefls` | `0x23274` | 307 | UnwindData |  |
| 712 | `_getptd` | `0x233E4` | 36 | UnwindData |  |
| 737 | `_initptd` | `0x2348C` | 194 | UnwindData |  |
| 514 | `_beginthread` | `0x24C9C` | 242 | UnwindData |  |
| 588 | `_endthread` | `0x24DBC` | 52 | UnwindData |  |
| 515 | `_beginthreadex` | `0x24E64` | 237 | UnwindData |  |
| 589 | `_endthreadex` | `0x24F80` | 144 | UnwindData |  |
| 506 | `_atoi64` | `0x2521C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1465 | `atoll` | `0x2521C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 507 | `_atoi64_l` | `0x25228` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 512 | `_atoll_l` | `0x25228` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 508 | `_atoi_l` | `0x25238` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 509 | `_atol_l` | `0x25238` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1463 | `atoi` | `0x25248` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1464 | `atol` | `0x25248` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1181 | `_swab` | `0x25254` | 88 | UnwindData |  |
| 1428 | `_wtoi64_l` | `0x25444` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1433 | `_wtoll_l` | `0x25444` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1429 | `_wtoi_l` | `0x25454` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1431 | `_wtol_l` | `0x25454` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1426 | `_wtoi` | `0x25464` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1430 | `_wtol` | `0x25464` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1427 | `_wtoi64` | `0x25470` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1432 | `_wtoll` | `0x25470` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 733 | `_i64toa` | `0x2547C` | 43 | UnwindData |  |
| 840 | `_itoa` | `0x254A8` | 42 | UnwindData |  |
| 871 | `_ltoa` | `0x254D4` | 40 | UnwindData |  |
| 1206 | `_ui64toa` | `0x254FC` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1210 | `_ultoa` | `0x2554C` | 26 | UnwindData |  |
| 734 | `_i64toa_s` | `0x25614` | 35 | UnwindData |  |
| 841 | `_itoa_s` | `0x25638` | 39 | UnwindData |  |
| 872 | `_ltoa_s` | `0x25660` | 34 | UnwindData |  |
| 1207 | `_ui64toa_s` | `0x25684` | 19 | UnwindData |  |
| 1211 | `_ultoa_s` | `0x25698` | 19 | UnwindData |  |
| 735 | `_i64tow` | `0x2589C` | 43 | UnwindData |  |
| 842 | `_itow` | `0x258C8` | 42 | UnwindData |  |
| 873 | `_ltow` | `0x258F4` | 40 | UnwindData |  |
| 1208 | `_ui64tow` | `0x2591C` | 26 | UnwindData |  |
| 1212 | `_ultow` | `0x25938` | 26 | UnwindData |  |
| 736 | `_i64tow_s` | `0x25A38` | 35 | UnwindData |  |
| 843 | `_itow_s` | `0x25A5C` | 39 | UnwindData |  |
| 874 | `_ltow_s` | `0x25A84` | 34 | UnwindData |  |
| 1209 | `_ui64tow_s` | `0x25AA8` | 19 | UnwindData |  |
| 1213 | `_ultow_s` | `0x25ABC` | 19 | UnwindData |  |
| 620 | `_findclose` | `0x25E14` | 37 | UnwindData |  |
| 621 | `_findfirst32` | `0x25E3C` | 147 | UnwindData |  |
| 625 | `_findnext32` | `0x25ED0` | 108 | UnwindData |  |
| 623 | `_findfirst64` | `0x25FD4` | 147 | UnwindData |  |
| 627 | `_findnext64` | `0x26068` | 108 | UnwindData |  |
| 624 | `_findfirst64i32` | `0x261F8` | 147 | UnwindData |  |
| 628 | `_findnext64i32` | `0x2628C` | 108 | UnwindData |  |
| 622 | `_findfirst32i64` | `0x26388` | 147 | UnwindData |  |
| 626 | `_findnext32i64` | `0x2641C` | 108 | UnwindData |  |
| 1358 | `_wfindfirst32` | `0x26488` | 325 | UnwindData |  |
| 1362 | `_wfindnext32` | `0x265D0` | 287 | UnwindData |  |
| 1360 | `_wfindfirst64` | `0x266F0` | 340 | UnwindData |  |
| 1364 | `_wfindnext64` | `0x26844` | 302 | UnwindData |  |
| 1361 | `_wfindfirst64i32` | `0x26974` | 328 | UnwindData |  |
| 1365 | `_wfindnext64i32` | `0x26ABC` | 290 | UnwindData |  |
| 1359 | `_wfindfirst32i64` | `0x26BE0` | 337 | UnwindData |  |
| 1363 | `_wfindnext32i64` | `0x26D34` | 299 | UnwindData |  |
| 705 | `_getdiskfree` | `0x26E60` | 163 | UnwindData |  |
| 708 | `_getdrives` | `0x26F04` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1086 | `_seterrormode` | `0x26F0C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 513 | `_beep` | `0x26F14` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1093 | `_sleep` | `0x26F1C` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 488 | `_access` | `0x26F30` | 18 | UnwindData |  |
| 489 | `_access_s` | `0x26F44` | 87 | UnwindData |  |
| 532 | `_chmod` | `0x26F9C` | 83 | UnwindData |  |
| 418 | `__doserrno` | `0x26FF0` | 32 | UnwindData |  |
| 578 | `_dosmaperr` | `0x27010` | 78 | UnwindData |  |
| 592 | `_errno` | `0x27060` | 32 | UnwindData |  |
| 682 | `_get_doserrno` | `0x27080` | 59 | UnwindData |  |
| 684 | `_get_errno` | `0x270BC` | 59 | UnwindData |  |
| 1077 | `_set_doserrno` | `0x27148` | 58 | UnwindData |  |
| 1078 | `_set_errno` | `0x27184` | 58 | UnwindData |  |
| 668 | `_fullpath` | `0x271C0` | 299 | UnwindData |  |
| 711 | `_getpid` | `0x272EC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1017 | `_mkdir` | `0x272F4` | 70 | UnwindData |  |
| 1763 | `rename` | `0x2733C` | 287 | UnwindData |  |
| 1054 | `_rmdir` | `0x2745C` | 70 | UnwindData |  |
| 1130 | `_stat32` | `0x274A4` | 85 | UnwindData |  |
| 1132 | `_stat64` | `0x274FC` | 85 | UnwindData |  |
| 1133 | `_stat64i32` | `0x27554` | 85 | UnwindData |  |
| 1131 | `_stat32i64` | `0x275AC` | 85 | UnwindData |  |
| 1222 | `_unlink` | `0x27604` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1759 | `remove` | `0x2760C` | 70 | UnwindData |  |
| 1286 | `_waccess` | `0x27654` | 18 | UnwindData |  |
| 1287 | `_waccess_s` | `0x27668` | 168 | UnwindData |  |
| 1292 | `_wchmod` | `0x27710` | 155 | UnwindData |  |
| 1371 | `_wfullpath` | `0x277AC` | 308 | UnwindData |  |
| 1378 | `_wmkdir` | `0x278E0` | 49 | UnwindData |  |
| 1392 | `_wrename` | `0x27914` | 53 | UnwindData |  |
| 1394 | `_wrmdir` | `0x2794C` | 47 | UnwindData |  |
| 1412 | `_wstat32` | `0x27A74` | 1,153 | UnwindData |  |
| 1414 | `_wstat64` | `0x27EF8` | 1,163 | UnwindData |  |
| 1415 | `_wstat64i32` | `0x28440` | 1,165 | UnwindData |  |
| 1413 | `_wstat32i64` | `0x288D0` | 1,151 | UnwindData |  |
| 1391 | `_wremove` | `0x28D50` | 47 | UnwindData |  |
| 1434 | `_wunlink` | `0x28D80` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 528 | `_chdir` | `0x28D88` | 301 | UnwindData |  |
| 529 | `_chdrive` | `0x28EB8` | 132 | UnwindData |  |
| 707 | `_getdrive` | `0x28F3C` | 235 | UnwindData |  |
| 703 | `_getcwd` | `0x29028` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 704 | `_getdcwd` | `0x29038` | 302 | UnwindData |  |
| 1291 | `_wchdir` | `0x291E8` | 331 | UnwindData |  |
| 1372 | `_wgetcwd` | `0x29334` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1373 | `_wgetdcwd` | `0x29344` | 333 | UnwindData |  |
| 593 | `_execl` | `0x29BE4` | 199 | UnwindData |  |
| 594 | `_execle` | `0x29CAC` | 214 | UnwindData |  |
| 595 | `_execlp` | `0x29D84` | 198 | UnwindData |  |
| 596 | `_execlpe` | `0x29E4C` | 214 | UnwindData |  |
| 597 | `_execv` | `0x29F24` | 69 | UnwindData |  |
| 598 | `_execve` | `0x29F6C` | 633 | UnwindData |  |
| 599 | `_execvp` | `0x2A270` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 600 | `_execvpe` | `0x2A278` | 781 | UnwindData |  |
| 706 | `_getdllprocaddr` | `0x2A588` | 36 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 854 | `_loaddll` | `0x2A5AC` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1223 | `_unloaddll` | `0x2A5B8` | 32 | UnwindData |  |
| 1114 | `_spawnl` | `0x2A5D8` | 207 | UnwindData |  |
| 1115 | `_spawnle` | `0x2A6A8` | 222 | UnwindData |  |
| 1116 | `_spawnlp` | `0x2A788` | 204 | UnwindData |  |
| 1117 | `_spawnlpe` | `0x2A854` | 222 | UnwindData |  |
| 1118 | `_spawnv` | `0x2A934` | 69 | UnwindData |  |
| 1119 | `_spawnve` | `0x2A97C` | 645 | UnwindData |  |
| 1120 | `_spawnvp` | `0x2AC94` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1121 | `_spawnvpe` | `0x2AC9C` | 749 | UnwindData |  |
| 1832 | `system` | `0x2AF8C` | 290 | UnwindData |  |
| 563 | `_cwait` | `0x2B0B0` | 182 | UnwindData |  |
| 1349 | `_wexecl` | `0x2B984` | 202 | UnwindData |  |
| 1350 | `_wexecle` | `0x2BA50` | 217 | UnwindData |  |
| 1351 | `_wexeclp` | `0x2BB2C` | 201 | UnwindData |  |
| 1352 | `_wexeclpe` | `0x2BBF8` | 217 | UnwindData |  |
| 1353 | `_wexecv` | `0x2BCD4` | 71 | UnwindData |  |
| 1354 | `_wexecve` | `0x2BD1C` | 637 | UnwindData |  |
| 1355 | `_wexecvp` | `0x2C024` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1356 | `_wexecvpe` | `0x2C02C` | 628 | UnwindData |  |
| 1402 | `_wspawnl` | `0x2C2A0` | 210 | UnwindData |  |
| 1403 | `_wspawnle` | `0x2C374` | 225 | UnwindData |  |
| 1404 | `_wspawnlp` | `0x2C458` | 207 | UnwindData |  |
| 1405 | `_wspawnlpe` | `0x2C528` | 225 | UnwindData |  |
| 1406 | `_wspawnv` | `0x2C60C` | 71 | UnwindData |  |
| 1407 | `_wspawnve` | `0x2C654` | 652 | UnwindData |  |
| 1408 | `_wspawnvp` | `0x2C970` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1409 | `_wspawnvpe` | `0x2C978` | 677 | UnwindData |  |
| 1420 | `_wsystem` | `0x2CC20` | 290 | UnwindData |  |
| 891 | `_mbclen` | `0x2CD44` | 45 | UnwindData |  |
| 892 | `_mbclen_l` | `0x2CD74` | 45 | UnwindData |  |
| 925 | `_mbsinc` | `0x2CDA4` | 66 | UnwindData |  |
| 926 | `_mbsinc_l` | `0x2CDE8` | 39 | UnwindData |  |
| 975 | `_mbsninc` | `0x2CE10` | 35 | UnwindData |  |
| 976 | `_mbsninc_l` | `0x2CE34` | 34 | UnwindData |  |
| 893 | `_mbctohira` | `0x2CE58` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 894 | `_mbctohira_l` | `0x2CE60` | 55 | UnwindData |  |
| 895 | `_mbctokata` | `0x2CE98` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 896 | `_mbctokata_l` | `0x2CEA0` | 41 | UnwindData |  |
| 1580 | `feof` | `0x2CECC` | 40 | UnwindData |  |
| 1582 | `ferror` | `0x2CEF4` | 40 | UnwindData |  |
| 698 | `_getc_nolock` | `0x2CF1C` | 37 | UnwindData |  |
| 1589 | `fgetc` | `0x2CF44` | 254 | UnwindData |  |
| 1631 | `getc` | `0x2CF44` | 254 | UnwindData |  |
| 613 | `_fgetchar` | `0x2D044` | 21 | UnwindData |  |
| 1632 | `getchar` | `0x2D044` | 21 | UnwindData |  |
| 1591 | `fgets` | `0x2D05C` | 351 | UnwindData |  |
| 614 | `_fgetwc_nolock` | `0x2D1BC` | 501 | UnwindData |  |
| 1592 | `fgetwc` | `0x2D3B4` | 92 | UnwindData |  |
| 1637 | `getwc` | `0x2D410` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1593 | `fgetws` | `0x2D418` | 200 | UnwindData |  |
| 615 | `_fgetwchar` | `0x2D4E0` | 21 | UnwindData |  |
| 1638 | `getwchar` | `0x2D4E0` | 21 | UnwindData |  |
| 619 | `_fileno` | `0x2D4F8` | 38 | UnwindData |  |
| 1611 | `fputc` | `0x2D520` | 272 | UnwindData |  |
| 1745 | `putc` | `0x2D520` | 272 | UnwindData |  |
| 1612 | `fputs` | `0x2D630` | 299 | UnwindData |  |
| 642 | `_fputchar` | `0x2D75C` | 29 | UnwindData |  |
| 1746 | `putchar` | `0x2D75C` | 29 | UnwindData |  |
| 643 | `_fputwc_nolock` | `0x2D77C` | 499 | UnwindData |  |
| 1613 | `fputwc` | `0x2D970` | 101 | UnwindData |  |
| 1748 | `putwc` | `0x2D9D8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1614 | `fputws` | `0x2D9E0` | 180 | UnwindData |  |
| 644 | `_fputwchar` | `0x2DA94` | 31 | UnwindData |  |
| 1749 | `putwchar` | `0x2DA94` | 31 | UnwindData |  |
| 616 | `_filbuf` | `0x2DAB4` | 323 | UnwindData |  |
| 427 | `__iob_func` | `0x2DE3C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 448 | `__p__iob` | `0x2DE3C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 861 | `_lock_file` | `0x2DE44` | 101 | UnwindData |  |
| 1225 | `_unlock_file` | `0x2DEE0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 631 | `_flsbuf` | `0x2DF50` | 395 | UnwindData |  |
| 1511 | `clearerr` | `0x2E6AC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1512 | `clearerr_s` | `0x2E6B4` | 178 | UnwindData |  |
| 604 | `_fcloseall` | `0x2E768` | 168 | UnwindData |  |
| 603 | `_fclose_nolock` | `0x2E810` | 122 | UnwindData |  |
| 1571 | `fclose` | `0x2E88C` | 102 | UnwindData |  |
| 608 | `_fdopen` | `0x2E8F4` | 414 | UnwindData |  |
| 612 | `_fflush_nolock` | `0x2EA94` | 76 | UnwindData |  |
| 632 | `_flushall` | `0x2EB5C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1588 | `fflush` | `0x2EB68` | 67 | UnwindData |  |
| 1590 | `fgetpos` | `0x2EC94` | 75 | UnwindData |  |
| 656 | `_fsopen` | `0x2ECE0` | 213 | UnwindData |  |
| 1607 | `fopen` | `0x2EDB8` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1608 | `fopen_s` | `0x2EDC4` | 83 | UnwindData |  |
| 638 | `_fprintf_l` | `0x2EE18` | 29 | UnwindData |  |
| 639 | `_fprintf_p` | `0x2EE38` | 36 | UnwindData |  |
| 640 | `_fprintf_p_l` | `0x2EE5C` | 29 | UnwindData |  |
| 641 | `_fprintf_s_l` | `0x2EE7C` | 29 | UnwindData |  |
| 1609 | `fprintf` | `0x2EE9C` | 296 | UnwindData |  |
| 1610 | `fprintf_s` | `0x2EFC4` | 36 | UnwindData |  |
| 645 | `_fread_nolock` | `0x2EFE8` | 29 | UnwindData |  |
| 646 | `_fread_nolock_s` | `0x2F008` | 543 | UnwindData |  |
| 1615 | `fread` | `0x2F228` | 29 | UnwindData |  |
| 1616 | `fread_s` | `0x2F248` | 167 | UnwindData |  |
| 1618 | `freopen` | `0x2F3E0` | 47 | UnwindData |  |
| 1619 | `freopen_s` | `0x2F410` | 22 | UnwindData |  |
| 651 | `_fscanf_l` | `0x2F428` | 49 | UnwindData |  |
| 652 | `_fscanf_s_l` | `0x2F45C` | 49 | UnwindData |  |
| 1621 | `fscanf` | `0x2F490` | 53 | UnwindData |  |
| 1622 | `fscanf_s` | `0x2F4C8` | 53 | UnwindData |  |
| 1856 | `vfscanf` | `0x2F500` | 35 | UnwindData |  |
| 1857 | `vfscanf_s` | `0x2F644` | 35 | UnwindData |  |
| 653 | `_fseek_nolock` | `0x2F668` | 169 | UnwindData |  |
| 1623 | `fseek` | `0x2F714` | 114 | UnwindData |  |
| 654 | `_fseeki64` | `0x2F788` | 116 | UnwindData |  |
| 655 | `_fseeki64_nolock` | `0x2F7FC` | 179 | UnwindData |  |
| 1624 | `fsetpos` | `0x2F8B0` | 53 | UnwindData |  |
| 661 | `_ftell_nolock` | `0x2F8E8` | 785 | UnwindData |  |
| 1625 | `ftell` | `0x2FBFC` | 88 | UnwindData |  |
| 662 | `_ftelli64` | `0x2FC54` | 91 | UnwindData |  |
| 663 | `_ftelli64_nolock` | `0x2FCB0` | 785 | UnwindData |  |
| 671 | `_fwprintf_l` | `0x2FFC4` | 29 | UnwindData |  |
| 672 | `_fwprintf_p` | `0x2FFE4` | 36 | UnwindData |  |
| 673 | `_fwprintf_p_l` | `0x30008` | 29 | UnwindData |  |
| 674 | `_fwprintf_s_l` | `0x30028` | 29 | UnwindData |  |
| 1626 | `fwprintf` | `0x30048` | 145 | UnwindData |  |
| 1627 | `fwprintf_s` | `0x300DC` | 36 | UnwindData |  |
| 675 | `_fwrite_nolock` | `0x30100` | 398 | UnwindData |  |
| 1628 | `fwrite` | `0x30290` | 143 | UnwindData |  |
| 676 | `_fwscanf_l` | `0x30320` | 49 | UnwindData |  |
| 677 | `_fwscanf_s_l` | `0x30354` | 49 | UnwindData |  |
| 1629 | `fwscanf` | `0x30388` | 53 | UnwindData |  |
| 1630 | `fwscanf_s` | `0x303C0` | 53 | UnwindData |  |
| 1860 | `vfwscanf` | `0x303F8` | 35 | UnwindData |  |
| 1861 | `vfwscanf_s` | `0x304AC` | 35 | UnwindData |  |
| 1635 | `gets` | `0x30724` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1636 | `gets_s` | `0x30734` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 714 | `_getw` | `0x3073C` | 179 | UnwindData |  |
| 719 | `_getws` | `0x307F0` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 720 | `_getws_s` | `0x30970` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 689 | `_get_output_format` | `0x30978` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1083 | `_set_output_format` | `0x30980` | 52 | UnwindData |  |
| 691 | `_get_printf_count_output` | `0x309B4` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1035 | `_printf_l` | `0x309CC` | 33 | UnwindData |  |
| 1036 | `_printf_p` | `0x309F0` | 39 | UnwindData |  |
| 1037 | `_printf_p_l` | `0x30A18` | 33 | UnwindData |  |
| 1038 | `_printf_s_l` | `0x30A3C` | 33 | UnwindData |  |
| 1084 | `_set_printf_count_output` | `0x30A60` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1743 | `printf` | `0x30A88` | 171 | UnwindData |  |
| 1744 | `printf_s` | `0x30B34` | 39 | UnwindData |  |
| 1747 | `puts` | `0x30B5C` | 378 | UnwindData |  |
| 1044 | `_putw` | `0x30CD8` | 175 | UnwindData |  |
| 1047 | `_putws` | `0x30D88` | 231 | UnwindData |  |
| 1764 | `rewind` | `0x30E70` | 185 | UnwindData |  |
| 1055 | `_rmtmp` | `0x30F2C` | 158 | UnwindData |  |
| 1062 | `_scanf_l` | `0x30FCC` | 46 | UnwindData |  |
| 1063 | `_scanf_s_l` | `0x30FFC` | 46 | UnwindData |  |
| 1777 | `scanf` | `0x3102C` | 50 | UnwindData |  |
| 1778 | `scanf_s` | `0x31060` | 50 | UnwindData |  |
| 1864 | `vscanf` | `0x31094` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1865 | `vscanf_s` | `0x310AC` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 709 | `_getmaxstdio` | `0x310C4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1089 | `_setmaxstdio` | `0x310CC` | 273 | UnwindData |  |
| 1779 | `setbuf` | `0x311E0` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1782 | `setvbuf` | `0x311FC` | 273 | UnwindData |  |
| 1094 | `_snprintf` | `0x31310` | 177 | UnwindData |  |
| 1097 | `_snprintf_l` | `0x313C4` | 29 | UnwindData |  |
| 1095 | `_snprintf_c` | `0x313E4` | 191 | UnwindData |  |
| 1096 | `_snprintf_c_l` | `0x314A4` | 29 | UnwindData |  |
| 1100 | `_snscanf` | `0x314C4` | 54 | UnwindData |  |
| 1101 | `_snscanf_l` | `0x314FC` | 49 | UnwindData |  |
| 1102 | `_snscanf_s` | `0x31530` | 54 | UnwindData |  |
| 1103 | `_snscanf_s_l` | `0x31568` | 49 | UnwindData |  |
| 1104 | `_snwprintf` | `0x31640` | 226 | UnwindData |  |
| 1105 | `_snwprintf_l` | `0x31724` | 29 | UnwindData |  |
| 1108 | `_snwscanf` | `0x31744` | 54 | UnwindData |  |
| 1109 | `_snwscanf_l` | `0x3177C` | 49 | UnwindData |  |
| 1110 | `_snwscanf_s` | `0x317B0` | 54 | UnwindData |  |
| 1111 | `_snwscanf_s_l` | `0x317E8` | 49 | UnwindData |  |
| 1064 | `_scprintf` | `0x318CC` | 37 | UnwindData |  |
| 1065 | `_scprintf_l` | `0x318F4` | 33 | UnwindData |  |
| 1066 | `_scprintf_p` | `0x31918` | 37 | UnwindData |  |
| 1067 | `_scprintf_p_l` | `0x31940` | 33 | UnwindData |  |
| 1098 | `_snprintf_s` | `0x31964` | 34 | UnwindData |  |
| 1099 | `_snprintf_s_l` | `0x31988` | 33 | UnwindData |  |
| 1124 | `_sprintf_l` | `0x319AC` | 29 | UnwindData |  |
| 1125 | `_sprintf_p` | `0x319CC` | 36 | UnwindData |  |
| 1126 | `_sprintf_p_l` | `0x319F0` | 29 | UnwindData |  |
| 1127 | `_sprintf_s_l` | `0x31A10` | 29 | UnwindData |  |
| 1788 | `sprintf` | `0x31A30` | 160 | UnwindData |  |
| 1789 | `sprintf_s` | `0x31AD0` | 36 | UnwindData |  |
| 1128 | `_sscanf_l` | `0x31AF4` | 49 | UnwindData |  |
| 1129 | `_sscanf_s_l` | `0x31B28` | 49 | UnwindData |  |
| 1793 | `sscanf` | `0x31B5C` | 53 | UnwindData |  |
| 1794 | `sscanf_s` | `0x31B94` | 53 | UnwindData |  |
| 1868 | `vsscanf` | `0x31C74` | 35 | UnwindData |  |
| 1869 | `vsscanf_s` | `0x31C98` | 35 | UnwindData |  |
| 468 | `__swprintf_l` | `0x31DF4` | 29 | UnwindData |  |
| 1068 | `_scwprintf` | `0x31E14` | 37 | UnwindData |  |
| 1069 | `_scwprintf_l` | `0x31E3C` | 33 | UnwindData |  |
| 1070 | `_scwprintf_p` | `0x31E60` | 37 | UnwindData |  |
| 1071 | `_scwprintf_p_l` | `0x31E88` | 33 | UnwindData |  |
| 1106 | `_snwprintf_s` | `0x31EAC` | 34 | UnwindData |  |
| 1107 | `_snwprintf_s_l` | `0x31ED0` | 33 | UnwindData |  |
| 1182 | `_swprintf` | `0x31EF4` | 196 | UnwindData |  |
| 1185 | `_swprintf_p` | `0x31FB8` | 36 | UnwindData |  |
| 1186 | `_swprintf_p_l` | `0x31FDC` | 29 | UnwindData |  |
| 1187 | `_swprintf_s_l` | `0x31FFC` | 29 | UnwindData |  |
| 1829 | `swprintf_s` | `0x3201C` | 36 | UnwindData |  |
| 1183 | `_swprintf_c` | `0x32040` | 252 | UnwindData |  |
| 1184 | `_swprintf_c_l` | `0x3213C` | 29 | UnwindData |  |
| 1188 | `_swscanf_l` | `0x3215C` | 49 | UnwindData |  |
| 1189 | `_swscanf_s_l` | `0x32190` | 49 | UnwindData |  |
| 1830 | `swscanf` | `0x321C4` | 53 | UnwindData |  |
| 1831 | `swscanf_s` | `0x321FC` | 53 | UnwindData |  |
| 1871 | `vswscanf` | `0x322E4` | 35 | UnwindData |  |
| 1872 | `vswscanf_s` | `0x32308` | 35 | UnwindData |  |
| 1194 | `_tempnam` | `0x3232C` | 725 | UnwindData |  |
| 1840 | `tmpfile` | `0x32C1C` | 35 | UnwindData |  |
| 1841 | `tmpfile_s` | `0x32C40` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1842 | `tmpnam` | `0x32C4C` | 48 | UnwindData |  |
| 1843 | `tmpnam_s` | `0x32C7C` | 64 | UnwindData |  |
| 1216 | `_ungetc_nolock` | `0x32CBC` | 263 | UnwindData |  |
| 1852 | `ungetc` | `0x32DC4` | 95 | UnwindData |  |
| 1219 | `_ungetwc_nolock` | `0x32E24` | 512 | UnwindData |  |
| 1853 | `ungetwc` | `0x33024` | 101 | UnwindData |  |
| 1249 | `_vprintf_l` | `0x3308C` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1250 | `_vprintf_p` | `0x330A4` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1251 | `_vprintf_p_l` | `0x330BC` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1252 | `_vprintf_s_l` | `0x330D4` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1862 | `vprintf` | `0x330EC` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1863 | `vprintf_s` | `0x331AC` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1241 | `_vfprintf_l` | `0x331C4` | 35 | UnwindData |  |
| 1242 | `_vfprintf_p` | `0x331E8` | 35 | UnwindData |  |
| 1243 | `_vfprintf_p_l` | `0x3320C` | 35 | UnwindData |  |
| 1244 | `_vfprintf_s_l` | `0x33230` | 35 | UnwindData |  |
| 1854 | `vfprintf` | `0x33254` | 35 | UnwindData |  |
| 1855 | `vfprintf_s` | `0x333B8` | 35 | UnwindData |  |
| 1245 | `_vfwprintf_l` | `0x333DC` | 35 | UnwindData |  |
| 1246 | `_vfwprintf_p` | `0x33400` | 35 | UnwindData |  |
| 1247 | `_vfwprintf_p_l` | `0x33424` | 35 | UnwindData |  |
| 1248 | `_vfwprintf_s_l` | `0x33448` | 35 | UnwindData |  |
| 1858 | `vfwprintf` | `0x3346C` | 35 | UnwindData |  |
| 1859 | `vfwprintf_s` | `0x33530` | 35 | UnwindData |  |
| 1253 | `_vscprintf` | `0x33554` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1254 | `_vscprintf_l` | `0x3356C` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1255 | `_vscprintf_p` | `0x33584` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1256 | `_vscprintf_p_l` | `0x3359C` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1271 | `_vsprintf_l` | `0x335B4` | 181 | UnwindData |  |
| 1866 | `vsprintf` | `0x3366C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1261 | `_vsnprintf` | `0x33678` | 22 | UnwindData |  |
| 1264 | `_vsnprintf_l` | `0x33690` | 203 | UnwindData |  |
| 1262 | `_vsnprintf_c` | `0x3375C` | 49 | UnwindData |  |
| 1263 | `_vsnprintf_c_l` | `0x33790` | 53 | UnwindData |  |
| 1265 | `_vsnprintf_s` | `0x338B0` | 30 | UnwindData |  |
| 1266 | `_vsnprintf_s_l` | `0x338D0` | 328 | UnwindData |  |
| 1272 | `_vsprintf_p` | `0x33A18` | 49 | UnwindData |  |
| 1273 | `_vsprintf_p_l` | `0x33A4C` | 53 | UnwindData |  |
| 1274 | `_vsprintf_s_l` | `0x33A84` | 110 | UnwindData |  |
| 1867 | `vsprintf_s` | `0x33AF4` | 22 | UnwindData |  |
| 1267 | `_vsnwprintf` | `0x33B0C` | 22 | UnwindData |  |
| 1268 | `_vsnwprintf_l` | `0x33B24` | 252 | UnwindData |  |
| 480 | `__vswprintf_l` | `0x33C20` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1257 | `_vscwprintf` | `0x33C28` | 168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1258 | `_vscwprintf_l` | `0x33CD0` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1259 | `_vscwprintf_p` | `0x33CE8` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1260 | `_vscwprintf_p_l` | `0x33D00` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1275 | `_vswprintf` | `0x33D18` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1278 | `_vswprintf_l` | `0x33D24` | 221 | UnwindData |  |
| 1269 | `_vsnwprintf_s` | `0x33E04` | 30 | UnwindData |  |
| 1270 | `_vsnwprintf_s_l` | `0x33E24` | 333 | UnwindData |  |
| 1276 | `_vswprintf_c` | `0x33F74` | 49 | UnwindData |  |
| 1277 | `_vswprintf_c_l` | `0x33FA8` | 53 | UnwindData |  |
| 1279 | `_vswprintf_p` | `0x340FC` | 49 | UnwindData |  |
| 1280 | `_vswprintf_p_l` | `0x34130` | 53 | UnwindData |  |
| 1281 | `_vswprintf_s_l` | `0x34168` | 121 | UnwindData |  |
| 1870 | `vswprintf_s` | `0x341E4` | 22 | UnwindData |  |
| 1282 | `_vwprintf_l` | `0x341FC` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1283 | `_vwprintf_p` | `0x34214` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1284 | `_vwprintf_p_l` | `0x3422C` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1285 | `_vwprintf_s_l` | `0x34244` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1873 | `vwprintf` | `0x3425C` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1874 | `vwprintf_s` | `0x34274` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1357 | `_wfdopen` | `0x3428C` | 439 | UnwindData |  |
| 1366 | `_wfopen` | `0x34444` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1367 | `_wfopen_s` | `0x34450` | 83 | UnwindData |  |
| 1370 | `_wfsopen` | `0x344A4` | 221 | UnwindData |  |
| 1368 | `_wfreopen` | `0x34584` | 47 | UnwindData |  |
| 1369 | `_wfreopen_s` | `0x346A4` | 22 | UnwindData |  |
| 1385 | `_wprintf_l` | `0x34998` | 33 | UnwindData |  |
| 1386 | `_wprintf_p` | `0x349BC` | 39 | UnwindData |  |
| 1387 | `_wprintf_p_l` | `0x349E4` | 33 | UnwindData |  |
| 1388 | `_wprintf_s_l` | `0x34A08` | 33 | UnwindData |  |
| 1922 | `wprintf` | `0x34A2C` | 171 | UnwindData |  |
| 1923 | `wprintf_s` | `0x34AD8` | 39 | UnwindData |  |
| 1395 | `_wscanf_l` | `0x34B00` | 46 | UnwindData |  |
| 1396 | `_wscanf_s_l` | `0x34B30` | 46 | UnwindData |  |
| 1875 | `vwscanf` | `0x34B60` | 168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1876 | `vwscanf_s` | `0x34C08` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1924 | `wscanf` | `0x34C20` | 50 | UnwindData |  |
| 1925 | `wscanf_s` | `0x34C54` | 50 | UnwindData |  |
| 1421 | `_wtempnam` | `0x34C88` | 660 | UnwindData |  |
| 1422 | `_wtmpnam` | `0x34F1C` | 48 | UnwindData |  |
| 1423 | `_wtmpnam_s` | `0x35118` | 64 | UnwindData |  |
| 1030 | `_pclose` | `0x3543C` | 220 | UnwindData |  |
| 1034 | `_popen` | `0x35518` | 1,666 | UnwindData |  |
| 1384 | `_wpopen` | `0x35C34` | 1,824 | UnwindData |  |
| 1716 | `memchr` | `0x36354` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1719 | `memcpy_s` | `0x36370` | 135 | UnwindData |  |
| 1014 | `_memccpy` | `0x363F8` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1721 | `memmove_s` | `0x36420` | 81 | UnwindData |  |
| 1802 | `strcspn` | `0x36474` | 160 | UnwindData |  |
| 1138 | `_strdup` | `0x36514` | 112 | UnwindData |  |
| 1156 | `_strnset` | `0x36584` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1813 | `strpbrk` | `0x3659C` | 161 | UnwindData |  |
| 1158 | `_strrev` | `0x36640` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1159 | `_strset` | `0x36678` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1815 | `strspn` | `0x36688` | 195 | UnwindData |  |
| 1797 | `strchr` | `0x36948` | 138 | UnwindData |  |
| 1814 | `strrchr` | `0x369D4` | 324 | UnwindData |  |
| 1816 | `strstr` | `0x36B18` | 477 | UnwindData |  |
| 1881 | `wcschr` | `0x36CF8` | 140 | UnwindData |  |
| 1896 | `wcsrchr` | `0x36D84` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1900 | `wcsstr` | `0x36E34` | 508 | UnwindData |  |
| 1812 | `strnlen` | `0x37030` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1796 | `strcat_s` | `0x37048` | 124 | UnwindData |  |
| 1808 | `strncat_s` | `0x370C4` | 213 | UnwindData |  |
| 1801 | `strcpy_s` | `0x3719C` | 97 | UnwindData |  |
| 1811 | `strncpy_s` | `0x37200` | 188 | UnwindData |  |
| 467 | `__strncnt` | `0x372BC` | 36 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1160 | `_strset_s` | `0x372E0` | 79 | UnwindData |  |
| 1157 | `_strnset_s` | `0x37330` | 122 | UnwindData |  |
| 1820 | `strtok` | `0x373AC` | 248 | UnwindData |  |
| 1821 | `strtok_s` | `0x374A4` | 283 | UnwindData |  |
| 1879 | `wcscat` | `0x375C0` | 44 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1884 | `wcscpy` | `0x375EC` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1880 | `wcscat_s` | `0x37608` | 133 | UnwindData |  |
| 1882 | `wcscmp` | `0x37690` | 60 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1885 | `wcscpy_s` | `0x376CC` | 107 | UnwindData |  |
| 1886 | `wcscspn` | `0x37738` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1297 | `_wcsdup` | `0x37778` | 117 | UnwindData |  |
| 1888 | `wcslen` | `0x377F0` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1894 | `wcsnlen` | `0x3780C` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1889 | `wcsncat` | `0x3782C` | 60 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1890 | `wcsncat_s` | `0x37868` | 231 | UnwindData |  |
| 1891 | `wcsncmp` | `0x37950` | 44 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 484 | `__wcsncnt` | `0x3797C` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1892 | `wcsncpy` | `0x379A4` | 70 | UnwindData |  |
| 1893 | `wcsncpy_s` | `0x379EC` | 204 | UnwindData |  |
| 1315 | `_wcsnset` | `0x37AB8` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1316 | `_wcsnset_s` | `0x37AD8` | 129 | UnwindData |  |
| 1895 | `wcspbrk` | `0x37B5C` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1317 | `_wcsrev` | `0x37B94` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1318 | `_wcsset` | `0x37BD4` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1319 | `_wcsset_s` | `0x37BE8` | 84 | UnwindData |  |
| 1899 | `wcsspn` | `0x37C3C` | 68 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1904 | `wcstok` | `0x37C80` | 167 | UnwindData |  |
| 1905 | `wcstok_s` | `0x37D28` | 191 | UnwindData |  |
| 1920 | `wmemcpy_s` | `0x37DE8` | 122 | UnwindData |  |
| 1921 | `wmemmove_s` | `0x37E64` | 82 | UnwindData |  |
| 1447 | `asctime` | `0x37EB8` | 121 | UnwindData |  |
| 1448 | `asctime_s` | `0x37F34` | 736 | UnwindData |  |
| 1513 | `clock` | `0x38240` | 61 | UnwindData |  |
| 559 | `_ctime32` | `0x38280` | 107 | UnwindData |  |
| 560 | `_ctime32_s` | `0x382EC` | 147 | UnwindData |  |
| 576 | `_difftime32` | `0x38380` | 43 | UnwindData |  |
| 577 | `_difftime64` | `0x383AC` | 46 | UnwindData |  |
| 664 | `_ftime32` | `0x38690` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 665 | `_ftime32_s` | `0x38698` | 399 | UnwindData |  |
| 721 | `_gmtime32` | `0x38870` | 69 | UnwindData |  |
| 722 | `_gmtime32_s` | `0x388B8` | 417 | UnwindData |  |
| 856 | `_localtime32` | `0x38A5C` | 69 | UnwindData |  |
| 857 | `_localtime32_s` | `0x38AA4` | 722 | UnwindData |  |
| 1018 | `_mkgmtime32` | `0x3902C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1022 | `_mktime32` | `0x39034` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1136 | `_strdate` | `0x39040` | 272 | UnwindData |  |
| 1137 | `_strdate_s` | `0x39150` | 303 | UnwindData |  |
| 1161 | `_strtime` | `0x39280` | 248 | UnwindData |  |
| 1162 | `_strtime_s` | `0x39378` | 279 | UnwindData |  |
| 1195 | `_time32` | `0x39490` | 85 | UnwindData |  |
| 416 | `__daylight` | `0x394E8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 419 | `__dstbias` | `0x394F0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 473 | `__timezone` | `0x394F8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 475 | `__tzname` | `0x39500` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 681 | `_get_daylight` | `0x39508` | 47 | UnwindData |  |
| 683 | `_get_dstbias` | `0x39538` | 47 | UnwindData |  |
| 694 | `_get_timezone` | `0x39568` | 47 | UnwindData |  |
| 695 | `_get_tzname` | `0x39598` | 177 | UnwindData |  |
| 1205 | `_tzset` | `0x39968` | 36 | UnwindData |  |
| 669 | `_futime32` | `0x3A0BC` | 500 | UnwindData |  |
| 1226 | `_utime32` | `0x3A2B0` | 134 | UnwindData |  |
| 561 | `_ctime64` | `0x3A338` | 108 | UnwindData |  |
| 562 | `_ctime64_s` | `0x3A3A4` | 162 | UnwindData |  |
| 666 | `_ftime64` | `0x3A714` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 667 | `_ftime64_s` | `0x3A71C` | 402 | UnwindData |  |
| 723 | `_gmtime64` | `0x3A8B0` | 69 | UnwindData |  |
| 724 | `_gmtime64_s` | `0x3A8F8` | 719 | UnwindData |  |
| 858 | `_localtime64` | `0x3ABC8` | 69 | UnwindData |  |
| 859 | `_localtime64_s` | `0x3AC10` | 780 | UnwindData |  |
| 1019 | `_mkgmtime64` | `0x3B1D0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1023 | `_mktime64` | `0x3B1D8` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1196 | `_time64` | `0x3B1E4` | 93 | UnwindData |  |
| 670 | `_futime64` | `0x3B244` | 504 | UnwindData |  |
| 1227 | `_utime64` | `0x3B43C` | 134 | UnwindData |  |
| 1288 | `_wasctime` | `0x3B4C4` | 121 | UnwindData |  |
| 1289 | `_wasctime_s` | `0x3B540` | 796 | UnwindData |  |
| 1340 | `_wctime32` | `0x3B85C` | 107 | UnwindData |  |
| 1341 | `_wctime32_s` | `0x3B8C8` | 141 | UnwindData |  |
| 1342 | `_wctime64` | `0x3B958` | 108 | UnwindData |  |
| 1343 | `_wctime64_s` | `0x3B9C4` | 158 | UnwindData |  |
| 1416 | `_wstrdate` | `0x3BA64` | 314 | UnwindData |  |
| 1417 | `_wstrdate_s` | `0x3BBA0` | 343 | UnwindData |  |
| 1418 | `_wstrtime` | `0x3BCF8` | 290 | UnwindData |  |
| 1419 | `_wstrtime_s` | `0x3BE1C` | 319 | UnwindData |  |
| 1435 | `_wutime32` | `0x3BF5C` | 134 | UnwindData |  |
| 1436 | `_wutime64` | `0x3BFE4` | 134 | UnwindData |  |
| 713 | `_getsystime` | `0x3C06C` | 158 | UnwindData |  |
| 1092 | `_setsystime` | `0x3C10C` | 163 | UnwindData |  |
| 1717 | `memcmp` | `0x3C1C0` | 199 | UnwindData |  |
| 1809 | `strncmp` | `0x3C2A0` | 125 | UnwindData |  |
| 1718 | `memcpy` | `0x3C330` | 1,381 | UnwindData |  |
| 1720 | `memmove` | `0x3C330` | 1,381 | UnwindData |  |
| 1722 | `memset` | `0x3C8B0` | 554 | UnwindData |  |
| 1795 | `strcat` | `0x3CAF0` | 144 | UnwindData |  |
| 1800 | `strcpy` | `0x3CB90` | 183 | UnwindData |  |
| 1798 | `strcmp` | `0x3CC60` | 103 | UnwindData |  |
| 1806 | `strlen` | `0x3CCE0` | 168 | UnwindData |  |
| 1807 | `strncat` | `0x3CDA0` | 405 | UnwindData |  |
| 1810 | `strncpy` | `0x3CF50` | 354 | UnwindData |  |
| 428 | `__isascii` | `0x3D15C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 429 | `__iscsym` | `0x3D168` | 40 | UnwindData |  |
| 430 | `__iscsymf` | `0x3D190` | 37 | UnwindData |  |
| 474 | `__toascii` | `0x3D1B8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 745 | `_isalnum_l` | `0x3D1C0` | 98 | UnwindData |  |
| 746 | `_isalpha_l` | `0x3D224` | 98 | UnwindData |  |
| 748 | `_isblank_l` | `0x3D288` | 109 | UnwindData |  |
| 749 | `_iscntrl_l` | `0x3D2F8` | 95 | UnwindData |  |
| 752 | `_isdigit_l` | `0x3D358` | 95 | UnwindData |  |
| 753 | `_isgraph_l` | `0x3D3B8` | 98 | UnwindData |  |
| 755 | `_islower_l` | `0x3D41C` | 95 | UnwindData |  |
| 820 | `_isprint_l` | `0x3D47C` | 98 | UnwindData |  |
| 821 | `_ispunct_l` | `0x3D4E0` | 95 | UnwindData |  |
| 822 | `_isspace_l` | `0x3D540` | 95 | UnwindData |  |
| 823 | `_isupper_l` | `0x3D5A0` | 95 | UnwindData |  |
| 839 | `_isxdigit_l` | `0x3D600` | 98 | UnwindData |  |
| 1645 | `isalnum` | `0x3D664` | 127 | UnwindData |  |
| 1646 | `isalpha` | `0x3D6E4` | 127 | UnwindData |  |
| 1647 | `isblank` | `0x3D764` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1648 | `iscntrl` | `0x3D794` | 122 | UnwindData |  |
| 1649 | `isdigit` | `0x3D810` | 122 | UnwindData |  |
| 1650 | `isgraph` | `0x3D88C` | 127 | UnwindData |  |
| 1652 | `islower` | `0x3D90C` | 122 | UnwindData |  |
| 1653 | `isprint` | `0x3D988` | 127 | UnwindData |  |
| 1654 | `ispunct` | `0x3DA08` | 122 | UnwindData |  |
| 1655 | `isspace` | `0x3DA84` | 122 | UnwindData |  |
| 1656 | `isupper` | `0x3DB00` | 122 | UnwindData |  |
| 1671 | `isxdigit` | `0x3DB7C` | 127 | UnwindData |  |
| 1005 | `_mbstrlen` | `0x3DBFC` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1006 | `_mbstrlen_l` | `0x3DC10` | 174 | UnwindData |  |
| 1007 | `_mbstrnlen` | `0x3DCC0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1008 | `_mbstrnlen_l` | `0x3DCC8` | 271 | UnwindData |  |
| 431 | `__iswcsym` | `0x3DDD8` | 44 | UnwindData |  |
| 828 | `_iswcsym_l` | `0x3DDD8` | 44 | UnwindData |  |
| 754 | `_isleadbyte_l` | `0x3DE04` | 67 | UnwindData |  |
| 825 | `_iswalpha_l` | `0x3DE48` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1658 | `iswalpha` | `0x3DE48` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 826 | `_iswblank_l` | `0x3DE54` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1660 | `iswblank` | `0x3DE54` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 432 | `__iswcsymf` | `0x3DE6C` | 44 | UnwindData |  |
| 829 | `_iswcsymf_l` | `0x3DE6C` | 44 | UnwindData |  |
| 831 | `_iswdigit_l` | `0x3DE98` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1663 | `iswdigit` | `0x3DE98` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 834 | `_iswprint_l` | `0x3DEA4` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1666 | `iswprint` | `0x3DEA4` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 835 | `_iswpunct_l` | `0x3DEB0` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1667 | `iswpunct` | `0x3DEB0` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 836 | `_iswspace_l` | `0x3DEBC` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1668 | `iswspace` | `0x3DEBC` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 837 | `_iswupper_l` | `0x3DEC8` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1669 | `iswupper` | `0x3DEC8` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 838 | `_iswxdigit_l` | `0x3DED4` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1670 | `iswxdigit` | `0x3DED4` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1651 | `isleadbyte` | `0x3DEE0` | 69 | UnwindData |  |
| 824 | `_iswalnum_l` | `0x3DF28` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1657 | `iswalnum` | `0x3DF28` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1659 | `iswascii` | `0x3DF34` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 827 | `_iswcntrl_l` | `0x3DF44` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1661 | `iswcntrl` | `0x3DF44` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 832 | `_iswgraph_l` | `0x3DF50` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1664 | `iswgraph` | `0x3DF50` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 833 | `_iswlower_l` | `0x3DF5C` | 220 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1665 | `iswlower` | `0x3DF5C` | 220 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 501 | `_atodbl` | `0x3E038` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 502 | `_atodbl_l` | `0x3E040` | 199 | UnwindData |  |
| 504 | `_atoflt` | `0x3E108` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 505 | `_atoflt_l` | `0x3E114` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 510 | `_atoldbl` | `0x3E11C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 511 | `_atoldbl_l` | `0x3E124` | 202 | UnwindData |  |
| 368 | `__STRINGTOLD` | `0x3E1F0` | 110 | UnwindData |  |
| 503 | `_atof_l` | `0x3E260` | 186 | UnwindData |  |
| 1462 | `atof` | `0x3E31C` | 152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 586 | `_ecvt` | `0x3E3B4` | 178 | UnwindData |  |
| 587 | `_ecvt_s` | `0x3E468` | 205 | UnwindData |  |
| 605 | `_fcvt` | `0x3E538` | 218 | UnwindData |  |
| 606 | `_fcvt_s` | `0x3E614` | 205 | UnwindData |  |
| 678 | `_gcvt` | `0x3E6E4` | 44 | UnwindData |  |
| 679 | `_gcvt_s` | `0x3E710` | 362 | UnwindData |  |
| 830 | `_iswctype_l` | `0x3E87C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1644 | `is_wctype` | `0x3E87C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1662 | `iswctype` | `0x3E884` | 102 | UnwindData |  |
| 750 | `_isctype` | `0x3E8EC` | 36 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 751 | `_isctype_l` | `0x3E910` | 219 | UnwindData |  |
| 904 | `_mblen_l` | `0x3E9EC` | 227 | UnwindData |  |
| 1708 | `mblen` | `0x3EAD0` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1003 | `_mbstowcs_l` | `0x3EAEC` | 484 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1004 | `_mbstowcs_s_l` | `0x3ECD0` | 304 | UnwindData |  |
| 1713 | `mbstowcs` | `0x3EE00` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1714 | `mbstowcs_s` | `0x3EE1C` | 30 | UnwindData |  |
| 1013 | `_mbtowc_l` | `0x3EE3C` | 337 | UnwindData |  |
| 1715 | `mbtowc` | `0x3EF90` | 852 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1468 | `btowc` | `0x3F2E4` | 100 | UnwindData |  |
| 1709 | `mbrlen` | `0x3F348` | 62 | UnwindData |  |
| 1710 | `mbrtowc` | `0x3F388` | 92 | UnwindData |  |
| 1711 | `mbsrtowcs` | `0x3F3E4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1712 | `mbsrtowcs_s` | `0x3F3EC` | 209 | UnwindData |  |
| 1163 | `_strtod_l` | `0x3F4C0` | 340 | UnwindData |  |
| 1817 | `strtod` | `0x3F614` | 580 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1168 | `_strtol_l` | `0x3F858` | 34 | UnwindData |  |
| 1173 | `_strtoul_l` | `0x3F87C` | 37 | UnwindData |  |
| 1822 | `strtol` | `0x3F8A4` | 48 | UnwindData |  |
| 1825 | `strtoul` | `0x3F8D4` | 51 | UnwindData |  |
| 1164 | `_strtof_l` | `0x3FB58` | 31 | UnwindData |  |
| 1165 | `_strtoi64` | `0x3FB78` | 48 | UnwindData |  |
| 1166 | `_strtoi64_l` | `0x3FBA8` | 34 | UnwindData |  |
| 1167 | `_strtoimax_l` | `0x3FBA8` | 34 | UnwindData |  |
| 1170 | `_strtoll_l` | `0x3FBA8` | 34 | UnwindData |  |
| 1169 | `_strtold_l` | `0x3FBCC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1171 | `_strtoui64` | `0x3FBD4` | 51 | UnwindData |  |
| 1172 | `_strtoui64_l` | `0x3FC08` | 37 | UnwindData |  |
| 1174 | `_strtoull_l` | `0x3FC08` | 37 | UnwindData |  |
| 1175 | `_strtoumax_l` | `0x3FC08` | 37 | UnwindData |  |
| 1818 | `strtof` | `0x3FC30` | 34 | UnwindData |  |
| 1823 | `strtold` | `0x3FC54` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1819 | `strtoimax` | `0x3FC5C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1824 | `strtoll` | `0x3FC5C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1826 | `strtoull` | `0x3FC64` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1827 | `strtoumax` | `0x3FC64` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1198 | `_tolower` | `0x3FC6C` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1199 | `_tolower_l` | `0x3FC70` | 338 | UnwindData |  |
| 1844 | `tolower` | `0x3FDC4` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1200 | `_toupper` | `0x3FDE4` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1201 | `_toupper_l` | `0x3FDE8` | 336 | UnwindData |  |
| 1845 | `toupper` | `0x3FF38` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1202 | `_towlower_l` | `0x3FF58` | 202 | UnwindData |  |
| 1847 | `towlower` | `0x40024` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1203 | `_towupper_l` | `0x4002C` | 207 | UnwindData |  |
| 1848 | `towupper` | `0x400FC` | 676 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1877 | `wcrtomb` | `0x403A0` | 58 | UnwindData |  |
| 1878 | `wcrtomb_s` | `0x403DC` | 136 | UnwindData |  |
| 1897 | `wcsrtombs` | `0x40464` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1898 | `wcsrtombs_s` | `0x4046C` | 192 | UnwindData |  |
| 1915 | `wctob` | `0x4052C` | 109 | UnwindData |  |
| 1320 | `_wcstod_l` | `0x4059C` | 303 | UnwindData |  |
| 1901 | `wcstod` | `0x406CC` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1325 | `_wcstol_l` | `0x408BC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1906 | `wcstol` | `0x408BC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1332 | `_wcstoul_l` | `0x408C4` | 628 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1911 | `wcstoul` | `0x408C4` | 628 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1321 | `_wcstof_l` | `0x40B38` | 270 | UnwindData |  |
| 1322 | `_wcstoi64` | `0x40C48` | 48 | UnwindData |  |
| 1323 | `_wcstoi64_l` | `0x40C78` | 34 | UnwindData |  |
| 1324 | `_wcstoimax_l` | `0x40C78` | 34 | UnwindData |  |
| 1327 | `_wcstoll_l` | `0x40C78` | 34 | UnwindData |  |
| 1326 | `_wcstold_l` | `0x40C9C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1330 | `_wcstoui64` | `0x40CA4` | 51 | UnwindData |  |
| 1331 | `_wcstoui64_l` | `0x40CD8` | 37 | UnwindData |  |
| 1333 | `_wcstoull_l` | `0x40CD8` | 37 | UnwindData |  |
| 1334 | `_wcstoumax_l` | `0x40CD8` | 37 | UnwindData |  |
| 1902 | `wcstof` | `0x40D00` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1907 | `wcstold` | `0x40D08` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1903 | `wcstoimax` | `0x40D10` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1908 | `wcstoll` | `0x40D10` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1912 | `wcstoull` | `0x40D18` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1913 | `wcstoumax` | `0x40D18` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1328 | `_wcstombs_l` | `0x40D20` | 824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1329 | `_wcstombs_s_l` | `0x41058` | 236 | UnwindData |  |
| 1909 | `wcstombs` | `0x41144` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1910 | `wcstombs_s` | `0x4114C` | 30 | UnwindData |  |
| 1344 | `_wctomb_l` | `0x4116C` | 123 | UnwindData |  |
| 1345 | `_wctomb_s_l` | `0x411E8` | 394 | UnwindData |  |
| 1916 | `wctomb` | `0x41374` | 84 | UnwindData |  |
| 1917 | `wctomb_s` | `0x413C8` | 20 | UnwindData |  |
| 1424 | `_wtof` | `0x413DC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1425 | `_wtof_l` | `0x413E4` | 142 | UnwindData |  |
| 814 | `_ismbslead` | `0x41474` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 815 | `_ismbslead_l` | `0x4147C` | 148 | UnwindData |  |
| 756 | `_ismbbalnum` | `0x4158C` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 757 | `_ismbbalnum_l` | `0x415A4` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 758 | `_ismbbalpha` | `0x415C0` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 759 | `_ismbbalpha_l` | `0x415D8` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 760 | `_ismbbblank` | `0x415F4` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 761 | `_ismbbblank_l` | `0x41610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 762 | `_ismbbgraph` | `0x41630` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 763 | `_ismbbgraph_l` | `0x41648` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 764 | `_ismbbkalnum` | `0x41664` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 765 | `_ismbbkalnum_l` | `0x41678` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 766 | `_ismbbkana` | `0x41690` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 767 | `_ismbbkana_l` | `0x41698` | 101 | UnwindData |  |
| 768 | `_ismbbkprint` | `0x41700` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 769 | `_ismbbkprint_l` | `0x41714` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 770 | `_ismbbkpunct` | `0x4172C` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 771 | `_ismbbkpunct_l` | `0x41740` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 772 | `_ismbblead` | `0x41758` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 773 | `_ismbblead_l` | `0x4176C` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 774 | `_ismbbprint` | `0x41784` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 775 | `_ismbbprint_l` | `0x4179C` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 776 | `_ismbbpunct` | `0x417B8` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 777 | `_ismbbpunct_l` | `0x417CC` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 778 | `_ismbbtrail` | `0x417E4` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 779 | `_ismbbtrail_l` | `0x417F8` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 710 | `_getmbcp` | `0x41BD8` | 58 | UnwindData |  |
| 1090 | `_setmbcp` | `0x41C14` | 580 | UnwindData |  |
| 780 | `_ismbcalnum` | `0x42108` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 781 | `_ismbcalnum_l` | `0x42110` | 202 | UnwindData |  |
| 782 | `_ismbcalpha` | `0x421DC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 783 | `_ismbcalpha_l` | `0x421E4` | 204 | UnwindData |  |
| 786 | `_ismbcdigit` | `0x422B0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 787 | `_ismbcdigit_l` | `0x422B8` | 206 | UnwindData |  |
| 788 | `_ismbcgraph` | `0x42388` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 789 | `_ismbcgraph_l` | `0x42390` | 209 | UnwindData |  |
| 790 | `_ismbchira` | `0x42464` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 791 | `_ismbchira_l` | `0x4246C` | 77 | UnwindData |  |
| 792 | `_ismbckata` | `0x424BC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 793 | `_ismbckata_l` | `0x424C4` | 85 | UnwindData |  |
| 810 | `_ismbcsymbol` | `0x4251C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 811 | `_ismbcsymbol_l` | `0x42524` | 85 | UnwindData |  |
| 800 | `_ismbclegal` | `0x4257C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 801 | `_ismbclegal_l` | `0x42584` | 82 | UnwindData |  |
| 802 | `_ismbclower` | `0x425D8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 803 | `_ismbclower_l` | `0x425E0` | 183 | UnwindData |  |
| 804 | `_ismbcprint` | `0x42698` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 805 | `_ismbcprint_l` | `0x426A0` | 204 | UnwindData |  |
| 784 | `_ismbcblank` | `0x4276C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 785 | `_ismbcblank_l` | `0x42774` | 211 | UnwindData |  |
| 806 | `_ismbcpunct` | `0x42848` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 807 | `_ismbcpunct_l` | `0x42850` | 199 | UnwindData |  |
| 808 | `_ismbcspace` | `0x42918` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 809 | `_ismbcspace_l` | `0x42920` | 204 | UnwindData |  |
| 816 | `_ismbstrail` | `0x429EC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 817 | `_ismbstrail_l` | `0x429F4` | 145 | UnwindData |  |
| 812 | `_ismbcupper` | `0x42A88` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 813 | `_ismbcupper_l` | `0x42A90` | 182 | UnwindData |  |
| 880 | `_mbbtype` | `0x42B48` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 881 | `_mbbtype_l` | `0x42B50` | 148 | UnwindData |  |
| 883 | `_mbccpy` | `0x42BE4` | 30 | UnwindData |  |
| 884 | `_mbccpy_l` | `0x42C04` | 29 | UnwindData |  |
| 885 | `_mbccpy_s` | `0x42C24` | 20 | UnwindData |  |
| 886 | `_mbccpy_s_l` | `0x42C38` | 261 | UnwindData |  |
| 908 | `_mbscat_s_l` | `0x42D40` | 461 | UnwindData |  |
| 916 | `_mbscpy_s_l` | `0x42F10` | 320 | UnwindData |  |
| 936 | `_mbsnbcat_s_l` | `0x43050` | 687 | UnwindData |  |
| 946 | `_mbsnbcpy_s_l` | `0x43300` | 519 | UnwindData |  |
| 954 | `_mbsnbset_s_l` | `0x43508` | 601 | UnwindData |  |
| 958 | `_mbsncat_s_l` | `0x43764` | 630 | UnwindData |  |
| 968 | `_mbsncpy_s_l` | `0x439DC` | 503 | UnwindData |  |
| 982 | `_mbsnset_s_l` | `0x43BD4` | 595 | UnwindData |  |
| 992 | `_mbsset_s_l` | `0x43E28` | 350 | UnwindData |  |
| 794 | `_ismbcl0` | `0x43F88` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 795 | `_ismbcl0_l` | `0x43F90` | 99 | UnwindData |  |
| 796 | `_ismbcl1` | `0x43FF4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 797 | `_ismbcl1_l` | `0x43FFC` | 104 | UnwindData |  |
| 798 | `_ismbcl2` | `0x44064` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 799 | `_ismbcl2_l` | `0x4406C` | 104 | UnwindData |  |
| 905 | `_mbsbtype` | `0x440D4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 906 | `_mbsbtype_l` | `0x440DC` | 179 | UnwindData |  |
| 907 | `_mbscat_s` | `0x44190` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 909 | `_mbschr` | `0x44198` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 910 | `_mbschr_l` | `0x441A0` | 189 | UnwindData |  |
| 911 | `_mbscmp` | `0x44260` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 912 | `_mbscmp_l` | `0x44268` | 221 | UnwindData |  |
| 915 | `_mbscpy_s` | `0x44348` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 913 | `_mbscoll` | `0x44350` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 914 | `_mbscoll_l` | `0x44358` | 201 | UnwindData |  |
| 917 | `_mbscspn` | `0x44424` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 918 | `_mbscspn_l` | `0x4442C` | 217 | UnwindData |  |
| 919 | `_mbsdec` | `0x44508` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 920 | `_mbsdec_l` | `0x44510` | 150 | UnwindData |  |
| 921 | `_mbsicmp` | `0x445A8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 922 | `_mbsicmp_l` | `0x445B0` | 493 | UnwindData |  |
| 923 | `_mbsicoll` | `0x447A0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 924 | `_mbsicoll_l` | `0x447A8` | 201 | UnwindData |  |
| 927 | `_mbslen` | `0x44874` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 928 | `_mbslen_l` | `0x4487C` | 107 | UnwindData |  |
| 977 | `_mbsnlen` | `0x448E8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 978 | `_mbsnlen_l` | `0x448F0` | 152 | UnwindData |  |
| 929 | `_mbslwr` | `0x44988` | 43 | UnwindData |  |
| 930 | `_mbslwr_l` | `0x449B4` | 43 | UnwindData |  |
| 931 | `_mbslwr_s` | `0x449E0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 932 | `_mbslwr_s_l` | `0x449E8` | 338 | UnwindData |  |
| 933 | `_mbsnbcat` | `0x44B3C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 934 | `_mbsnbcat_l` | `0x44B44` | 328 | UnwindData |  |
| 935 | `_mbsnbcat_s` | `0x44C8C` | 20 | UnwindData |  |
| 937 | `_mbsnbcmp` | `0x44CA0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 938 | `_mbsnbcmp_l` | `0x44CA8` | 300 | UnwindData |  |
| 939 | `_mbsnbcnt` | `0x44DD4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 940 | `_mbsnbcnt_l` | `0x44DDC` | 147 | UnwindData |  |
| 941 | `_mbsnbcoll` | `0x44E70` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 942 | `_mbsnbcoll_l` | `0x44E78` | 275 | UnwindData |  |
| 943 | `_mbsnbcpy` | `0x44F8C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 944 | `_mbsnbcpy_l` | `0x44F94` | 241 | UnwindData |  |
| 945 | `_mbsnbcpy_s` | `0x45088` | 20 | UnwindData |  |
| 947 | `_mbsnbicmp` | `0x4509C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 948 | `_mbsnbicmp_l` | `0x450A4` | 429 | UnwindData |  |
| 949 | `_mbsnbicoll` | `0x45254` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 950 | `_mbsnbicoll_l` | `0x4525C` | 255 | UnwindData |  |
| 951 | `_mbsnbset` | `0x4535C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 952 | `_mbsnbset_l` | `0x45364` | 242 | UnwindData |  |
| 953 | `_mbsnbset_s` | `0x45458` | 20 | UnwindData |  |
| 955 | `_mbsncat` | `0x4546C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 956 | `_mbsncat_l` | `0x45474` | 301 | UnwindData |  |
| 957 | `_mbsncat_s` | `0x455A4` | 20 | UnwindData |  |
| 959 | `_mbsnccnt` | `0x455B8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 960 | `_mbsnccnt_l` | `0x455C0` | 152 | UnwindData |  |
| 961 | `_mbsncmp` | `0x45658` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 962 | `_mbsncmp_l` | `0x45660` | 256 | UnwindData |  |
| 963 | `_mbsncoll` | `0x45760` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 964 | `_mbsncoll_l` | `0x45768` | 311 | UnwindData |  |
| 965 | `_mbsncpy` | `0x458A0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 966 | `_mbsncpy_l` | `0x458A8` | 228 | UnwindData |  |
| 967 | `_mbsncpy_s` | `0x4598C` | 20 | UnwindData |  |
| 969 | `_mbsnextc` | `0x459A0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 970 | `_mbsnextc_l` | `0x459A8` | 114 | UnwindData |  |
| 971 | `_mbsnicmp` | `0x45A1C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 972 | `_mbsnicmp_l` | `0x45A24` | 386 | UnwindData |  |
| 973 | `_mbsnicoll` | `0x45BA8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 974 | `_mbsnicoll_l` | `0x45BB0` | 311 | UnwindData |  |
| 979 | `_mbsnset` | `0x45CE8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 980 | `_mbsnset_l` | `0x45CF0` | 343 | UnwindData |  |
| 981 | `_mbsnset_s` | `0x45E48` | 20 | UnwindData |  |
| 983 | `_mbspbrk` | `0x45E5C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 984 | `_mbspbrk_l` | `0x45E64` | 207 | UnwindData |  |
| 985 | `_mbsrchr` | `0x45F34` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 986 | `_mbsrchr_l` | `0x45F3C` | 185 | UnwindData |  |
| 987 | `_mbsrev` | `0x45FF8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 988 | `_mbsrev_l` | `0x46000` | 197 | UnwindData |  |
| 989 | `_mbsset` | `0x460C8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 990 | `_mbsset_l` | `0x460D0` | 195 | UnwindData |  |
| 991 | `_mbsset_s` | `0x46194` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 993 | `_mbsspn` | `0x4619C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 994 | `_mbsspn_l` | `0x461A4` | 217 | UnwindData |  |
| 995 | `_mbsspnp` | `0x46280` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 996 | `_mbsspnp_l` | `0x46288` | 221 | UnwindData |  |
| 997 | `_mbsstr` | `0x46368` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 998 | `_mbsstr_l` | `0x46370` | 255 | UnwindData |  |
| 999 | `_mbstok` | `0x46470` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1000 | `_mbstok_l` | `0x46478` | 62 | UnwindData |  |
| 1001 | `_mbstok_s` | `0x464B8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1002 | `_mbstok_s_l` | `0x464C0` | 483 | UnwindData |  |
| 1009 | `_mbsupr` | `0x466A4` | 43 | UnwindData |  |
| 1010 | `_mbsupr_l` | `0x466D0` | 43 | UnwindData |  |
| 1011 | `_mbsupr_s` | `0x466FC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1012 | `_mbsupr_s_l` | `0x46704` | 338 | UnwindData |  |
| 897 | `_mbctolower` | `0x46858` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 898 | `_mbctolower_l` | `0x46860` | 192 | UnwindData |  |
| 901 | `_mbctoupper` | `0x46920` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 902 | `_mbctoupper_l` | `0x46928` | 192 | UnwindData |  |
| 887 | `_mbcjistojms` | `0x469E8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 888 | `_mbcjistojms_l` | `0x469F0` | 151 | UnwindData |  |
| 889 | `_mbcjmstojis` | `0x46A88` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 890 | `_mbcjmstojis_l` | `0x46A90` | 193 | UnwindData |  |
| 878 | `_mbbtombc` | `0x46B54` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 879 | `_mbbtombc_l` | `0x46B5C` | 169 | UnwindData |  |
| 899 | `_mbctombb` | `0x46C08` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 900 | `_mbctombb_l` | `0x46C10` | 206 | UnwindData |  |
| 555 | `_cscanf` | `0x51280` | 39 | UnwindData |  |
| 556 | `_cscanf_l` | `0x512A8` | 33 | UnwindData |  |
| 557 | `_cscanf_s` | `0x5224C` | 39 | UnwindData |  |
| 558 | `_cscanf_s_l` | `0x52274` | 33 | UnwindData |  |
| 570 | `_cwscanf` | `0x532D8` | 39 | UnwindData |  |
| 571 | `_cwscanf_l` | `0x53300` | 33 | UnwindData |  |
| 572 | `_cwscanf_s` | `0x54570` | 39 | UnwindData |  |
| 573 | `_cwscanf_s_l` | `0x54598` | 33 | UnwindData |  |
| 547 | `_cprintf_p` | `0x545BC` | 39 | UnwindData |  |
| 548 | `_cprintf_p_l` | `0x545E4` | 33 | UnwindData |  |
| 1231 | `_vcprintf_p` | `0x54608` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1232 | `_vcprintf_p_l` | `0x54614` | 4,183 | UnwindData |  |
| 549 | `_cprintf_s` | `0x5566C` | 39 | UnwindData |  |
| 550 | `_cprintf_s_l` | `0x55694` | 33 | UnwindData |  |
| 1233 | `_vcprintf_s` | `0x556B8` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1234 | `_vcprintf_s_l` | `0x556C4` | 2,502 | UnwindData |  |
| 564 | `_cwprintf` | `0x56168` | 39 | UnwindData |  |
| 565 | `_cwprintf_l` | `0x56190` | 33 | UnwindData |  |
| 1235 | `_vcwprintf` | `0x561B4` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1236 | `_vcwprintf_l` | `0x561C0` | 2,687 | UnwindData |  |
| 566 | `_cwprintf_p` | `0x56C40` | 39 | UnwindData |  |
| 567 | `_cwprintf_p_l` | `0x56C68` | 33 | UnwindData |  |
| 1237 | `_vcwprintf_p` | `0x56C8C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1238 | `_vcwprintf_p_l` | `0x56C98` | 4,484 | UnwindData |  |
| 568 | `_cwprintf_s` | `0x57EB4` | 39 | UnwindData |  |
| 569 | `_cwprintf_s_l` | `0x57EDC` | 33 | UnwindData |  |
| 1239 | `_vcwprintf_s` | `0x57F00` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1240 | `_vcwprintf_s_l` | `0x57F0C` | 2,719 | UnwindData |  |
| 545 | `_cprintf` | `0x589FC` | 39 | UnwindData |  |
| 546 | `_cprintf_l` | `0x58A24` | 33 | UnwindData |  |
| 1229 | `_vcprintf` | `0x58A48` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1230 | `_vcprintf_l` | `0x58A54` | 2,407 | UnwindData |  |
| 1015 | `_memicmp` | `0x59408` | 80 | UnwindData |  |
| 1016 | `_memicmp_l` | `0x59458` | 224 | UnwindData |  |
| 1135 | `_strcoll_l` | `0x59538` | 184 | UnwindData |  |
| 1799 | `strcoll` | `0x595F0` | 68 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1142 | `_stricmp` | `0x59634` | 70 | UnwindData |  |
| 1143 | `_stricmp_l` | `0x5967C` | 179 | UnwindData |  |
| 1144 | `_stricoll` | `0x59730` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1145 | `_stricoll_l` | `0x59748` | 184 | UnwindData |  |
| 1146 | `_strlwr` | `0x59A0C` | 88 | UnwindData |  |
| 1147 | `_strlwr_l` | `0x59A64` | 30 | UnwindData |  |
| 1148 | `_strlwr_s` | `0x59A84` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1149 | `_strlwr_s_l` | `0x59A8C` | 75 | UnwindData |  |
| 1150 | `_strncoll` | `0x59AD8` | 79 | UnwindData |  |
| 1151 | `_strncoll_l` | `0x59B28` | 255 | UnwindData |  |
| 1152 | `_strnicmp` | `0x59C70` | 79 | UnwindData |  |
| 1153 | `_strnicmp_l` | `0x59CC0` | 217 | UnwindData |  |
| 1154 | `_strnicoll` | `0x59D9C` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1155 | `_strnicoll_l` | `0x59DB4` | 256 | UnwindData |  |
| 1176 | `_strupr` | `0x5A0C0` | 88 | UnwindData |  |
| 1177 | `_strupr_l` | `0x5A118` | 30 | UnwindData |  |
| 1178 | `_strupr_s` | `0x5A138` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1179 | `_strupr_s_l` | `0x5A140` | 75 | UnwindData |  |
| 1180 | `_strxfrm_l` | `0x5A18C` | 374 | UnwindData |  |
| 1828 | `strxfrm` | `0x5A304` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1296 | `_wcscoll_l` | `0x5A30C` | 169 | UnwindData |  |
| 1883 | `wcscoll` | `0x5A3B8` | 70 | UnwindData |  |
| 1301 | `_wcsicmp` | `0x5A400` | 132 | UnwindData |  |
| 1302 | `_wcsicmp_l` | `0x5A484` | 237 | UnwindData |  |
| 1303 | `_wcsicoll` | `0x5A574` | 132 | UnwindData |  |
| 1304 | `_wcsicoll_l` | `0x5A5F8` | 230 | UnwindData |  |
| 1305 | `_wcslwr` | `0x5A8E0` | 95 | UnwindData |  |
| 1306 | `_wcslwr_l` | `0x5A940` | 30 | UnwindData |  |
| 1307 | `_wcslwr_s` | `0x5A960` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1308 | `_wcslwr_s_l` | `0x5A968` | 75 | UnwindData |  |
| 1309 | `_wcsncoll` | `0x5A9B4` | 79 | UnwindData |  |
| 1310 | `_wcsncoll_l` | `0x5AA04` | 214 | UnwindData |  |
| 1311 | `_wcsnicmp` | `0x5AADC` | 151 | UnwindData |  |
| 1312 | `_wcsnicmp_l` | `0x5AB74` | 278 | UnwindData |  |
| 1313 | `_wcsnicoll` | `0x5AC8C` | 146 | UnwindData |  |
| 1314 | `_wcsnicoll_l` | `0x5AD20` | 304 | UnwindData |  |
| 1335 | `_wcsupr` | `0x5B050` | 95 | UnwindData |  |
| 1336 | `_wcsupr_l` | `0x5B0B0` | 30 | UnwindData |  |
| 1337 | `_wcsupr_s` | `0x5B0D0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1338 | `_wcsupr_s_l` | `0x5B0D8` | 75 | UnwindData |  |
| 1339 | `_wcsxfrm_l` | `0x5B124` | 352 | UnwindData |  |
| 1914 | `wcsxfrm` | `0x5B284` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 332 | `_Getdays` | `0x5B28C` | 324 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 333 | `_Getmonths` | `0x5B3D0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 341 | `_Strftime` | `0x5B520` | 30 | UnwindData |  |
| 1141 | `_strftime_l` | `0x5B6E8` | 30 | UnwindData |  |
| 1805 | `strftime` | `0x5B708` | 26 | UnwindData |  |
| 342 | `_W_Getdays` | `0x5C360` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 343 | `_W_Getmonths` | `0x5C4E0` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 334 | `_Gettnames` | `0x5C660` | 2,012 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 344 | `_W_Gettnames` | `0x5C660` | 2,012 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 345 | `_Wcsftime` | `0x5CE3C` | 30 | UnwindData |  |
| 1300 | `_wcsftime_l` | `0x5CFF4` | 30 | UnwindData |  |
| 1887 | `wcsftime` | `0x5D014` | 26 | UnwindData |  |
| 272 | `?_inconsistency@@YAXXZ` | `0x5D030` | 32 | UnwindData |  |
| 309 | `?terminate@@YAXXZ` | `0x5D050` | 31 | UnwindData |  |
| 314 | `?unexpected@@YAXXZ` | `0x5D070` | 29 | UnwindData |  |
| 26 | `??0__non_rtti_object@std@@QEAA@AEBV01@@Z` | `0x5D0B0` | 33 | UnwindData |  |
| 27 | `??0__non_rtti_object@std@@QEAA@PEBD@Z` | `0x5D0D4` | 33 | UnwindData |  |
| 28 | `??0bad_cast@std@@AEAA@PEBQEBD@Z` | `0x5D0F8` | 33 | UnwindData |  |
| 29 | `??0bad_cast@std@@QEAA@AEBV01@@Z` | `0x5D11C` | 33 | UnwindData |  |
| 30 | `??0bad_cast@std@@QEAA@PEBD@Z` | `0x5D140` | 42 | UnwindData |  |
| 33 | `??0bad_typeid@std@@QEAA@AEBV01@@Z` | `0x5D16C` | 33 | UnwindData |  |
| 34 | `??0bad_typeid@std@@QEAA@PEBD@Z` | `0x5D190` | 42 | UnwindData |  |
| 43 | `??0exception@std@@QEAA@AEBQEBD@Z` | `0x5D1BC` | 45 | UnwindData |  |
| 44 | `??0exception@std@@QEAA@AEBQEBDH@Z` | `0x5D1EC` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `??0exception@std@@QEAA@AEBV01@@Z` | `0x5D208` | 42 | UnwindData |  |
| 46 | `??0exception@std@@QEAA@XZ` | `0x5D234` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `??1__non_rtti_object@std@@UEAA@XZ` | `0x5D24C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `??1bad_cast@std@@UEAA@XZ` | `0x5D24C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `??1bad_typeid@std@@UEAA@XZ` | `0x5D24C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `??1exception@std@@UEAA@XZ` | `0x5D24C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `??4exception@std@@QEAAAEAV01@AEBV01@@Z` | `0x5D25C` | 68 | UnwindData |  |
| 195 | `?_Copy_str@exception@std@@AEAAXPEBD@Z` | `0x5D314` | 90 | UnwindData |  |
| 246 | `?_Tidy@exception@std@@AEAAXXZ` | `0x5D370` | 39 | UnwindData |  |
| 322 | `?what@exception@std@@UEBAPEBDXZ` | `0x5D398` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `??1type_info@@UEAA@XZ` | `0x5D3AC` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `??8type_info@@QEBA_NAEBV0@@Z` | `0x5D3BC` | 30 | UnwindData |  |
| 125 | `??9type_info@@QEBA_NAEBV0@@Z` | `0x5D3DC` | 30 | UnwindData |  |
| 275 | `?_name_internal_method@type_info@@QEBAPEBDPEAU__type_info_node@@@Z` | `0x5D470` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 285 | `?_type_info_dtor_internal_method@type_info@@QEAAXXZ` | `0x5D478` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 288 | `?before@type_info@@QEBA_NAEBV1@@Z` | `0x5D480` | 30 | UnwindData |  |
| 295 | `?name@type_info@@QEBAPEBDPEAU__type_info_node@@@Z` | `0x5D4A0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 299 | `?raw_name@type_info@@QEBAPEBDXZ` | `0x5D4A8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 360 | `__DestructExceptionObject` | `0x5D4B0` | 110 | UnwindData |  |
| 271 | `__uncaught_exception` | `0x5DDD8` | 25 | UnwindData |  |
| 274 | `?_is_exception_typeof@@YAHAEBVtype_info@@PEAU_EXCEPTION_POINTERS@@@Z` | `0x5DDF4` | 191 | UnwindData |  |
| 340 | `_SetWinRTOutOfMemoryExceptionCallback` | `0x5DEB4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 347 | `__AdjustPointer` | `0x5DEBC` | 36 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 348 | `__BuildCatchObject` | `0x5DEE0` | 182 | UnwindData |  |
| 349 | `__BuildCatchObjectHelper` | `0x5DF98` | 591 | UnwindData |  |
| 352 | `__CxxDetectRethrow` | `0x5E3EC` | 71 | UnwindData |  |
| 353 | `__CxxExceptionFilter` | `0x5E434` | 502 | UnwindData |  |
| 357 | `__CxxQueryExceptionSize` | `0x5E62C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 358 | `__CxxRegisterExceptionObject` | `0x5E634` | 193 | UnwindData |  |
| 359 | `__CxxUnregisterExceptionObject` | `0x5E6F8` | 343 | UnwindData |  |
| 361 | `__FrameUnwindFilter` | `0x5E850` | 83 | UnwindData |  |
| 362 | `__GetPlatformExceptionInfo` | `0x5EA38` | 145 | UnwindData |  |
| 370 | `__TypeMatch` | `0x5ECF0` | 301 | UnwindData |  |
| 327 | `_CxxThrowException` | `0x5EE20` | 197 | UnwindData |  |
| 326 | `_CreateFrameInfo` | `0x5F26C` | 67 | UnwindData |  |
| 329 | `_FindAndUnlinkFrame` | `0x5F2B0` | 94 | UnwindData |  |
| 330 | `_GetImageBase` | `0x5F310` | 21 | UnwindData |  |
| 331 | `_GetThrowImageBase` | `0x5F328` | 21 | UnwindData |  |
| 336 | `_IsExceptionObjectToBeDestroyed` | `0x5F340` | 50 | UnwindData |  |
| 338 | `_SetImageBase` | `0x5F374` | 27 | UnwindData |  |
| 339 | `_SetThrowImageBase` | `0x5F390` | 27 | UnwindData |  |
| 354 | `__CxxFrameHandler` | `0x5F4D0` | 135 | UnwindData |  |
| 355 | `__CxxFrameHandler2` | `0x5F4D0` | 135 | UnwindData |  |
| 356 | `__CxxFrameHandler3` | `0x5F4D0` | 135 | UnwindData |  |
| 211 | `?_Name_base@type_info@@CAPEBDPEBV1@PEAU__type_info_node@@@Z` | `0x5F66C` | 308 | UnwindData |  |
| 212 | `?_Name_base_internal@type_info@@CAPEBDPEBV1@PEAU__type_info_node@@@Z` | `0x5F7A0` | 345 | UnwindData |  |
| 253 | `?_Type_info_dtor@type_info@@CAXPEAV1@@Z` | `0x5F8FC` | 108 | UnwindData |  |
| 254 | `?_Type_info_dtor_internal@type_info@@CAXPEAV1@@Z` | `0x5F8FC` | 108 | UnwindData |  |
| 381 | `__clean_type_info_names_internal` | `0x5F968` | 79 | UnwindData |  |
| 478 | `__unDNameHelper` | `0x5F9B8` | 53 | UnwindData |  |
| 256 | `?_ValidateExecute@@YAHP6A_JXZ@Z` | `0x5F9F0` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 257 | `?_ValidateRead@@YAHPEBXI@Z` | `0x5F9F0` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 258 | `?_ValidateWrite@@YAHPEAXI@Z` | `0x5F9F0` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 282 | `?_set_se_translator@@YAP6AXIPEAU_EXCEPTION_POINTERS@@@ZH@Z` | `0x5F9FC` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 283 | `?_set_se_translator@@YAP6AXIPEAU_EXCEPTION_POINTERS@@@ZP6AXI0@Z@Z` | `0x5FA0C` | 51 | UnwindData |  |
| 305 | `?set_terminate@@YAP6AXXZH@Z` | `0x5FA40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 306 | `?set_terminate@@YAP6AXXZP6AXXZ@Z` | `0x5FA50` | 75 | UnwindData |  |
| 307 | `?set_unexpected@@YAP6AXXZH@Z` | `0x5FA9C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 308 | `?set_unexpected@@YAP6AXXZP6AXXZ@Z` | `0x5FAAC` | 75 | UnwindData |  |
| 693 | `_get_terminate` | `0x5FAF8` | 21 | UnwindData |  |
| 696 | `_get_unexpected` | `0x5FB10` | 21 | UnwindData |  |
| 365 | `__RTCastToVoid` | `0x5FFB8` | 105 | UnwindData |  |
| 366 | `__RTDynamicCast` | `0x60024` | 380 | UnwindData |  |
| 367 | `__RTtypeid` | `0x601A0` | 169 | UnwindData |  |
| 476 | `__unDName` | `0x6652C` | 256 | UnwindData |  |
| 477 | `__unDNameEx` | `0x6662C` | 262 | UnwindData |  |
| 113 | `??2@YAPEAX_K@Z` | `0x668C8` | 105 | UnwindData |  |
| 115 | `??3@YAXPEAX@Z` | `0x66934` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1617 | `free` | `0x6693C` | 61 | UnwindData |  |
| 1707 | `malloc` | `0x6697C` | 182 | UnwindData |  |
| 522 | `_calloc_crt` | `0x66A34` | 127 | UnwindData |  |
| 877 | `_malloc_crt` | `0x66AB4` | 122 | UnwindData |  |
| 1050 | `_realloc_crt` | `0x66B30` | 129 | UnwindData |  |
| 1052 | `_recalloc_crt` | `0x66BB4` | 132 | UnwindData |  |
| 1082 | `_set_malloc_crt_max_wait` | `0x66C38` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 686 | `_get_heap_handle` | `0x66C48` | 52 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1478 | `calloc` | `0x66C7C` | 65 | UnwindData |  |
| 491 | `_aligned_free` | `0x66CC0` | 27 | UnwindData |  |
| 492 | `_aligned_malloc` | `0x66CDC` | 116 | UnwindData |  |
| 493 | `_aligned_msize` | `0x66D50` | 101 | UnwindData |  |
| 494 | `_aligned_offset_malloc` | `0x66DB8` | 179 | UnwindData |  |
| 495 | `_aligned_offset_realloc` | `0x66E6C` | 458 | UnwindData |  |
| 496 | `_aligned_offset_recalloc` | `0x67038` | 163 | UnwindData |  |
| 497 | `_aligned_realloc` | `0x670DC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 498 | `_aligned_recalloc` | `0x670E4` | 20 | UnwindData |  |
| 602 | `_expand` | `0x670F8` | 249 | UnwindData |  |
| 725 | `_heapadd` | `0x671F4` | 23 | UnwindData |  |
| 726 | `_heapchk` | `0x6720C` | 45 | UnwindData |  |
| 728 | `_heapset` | `0x6723C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 727 | `_heapmin` | `0x67244` | 33 | UnwindData |  |
| 729 | `_heapused` | `0x67268` | 22 | UnwindData |  |
| 730 | `_heapwalk` | `0x67280` | 363 | UnwindData |  |
| 1024 | `_msize` | `0x673EC` | 57 | UnwindData |  |
| 1051 | `_recalloc` | `0x67428` | 134 | UnwindData |  |
| 1053 | `_resetstkoflw` | `0x674B0` | 292 | UnwindData |  |
| 1755 | `realloc` | `0x675D4` | 211 | UnwindData |  |
| 657 | `_fstat32` | `0x67AE8` | 940 | UnwindData |  |
| 1381 | `_wopen` | `0x67E94` | 209 | UnwindData |  |
| 1400 | `_wsopen` | `0x67F68` | 65 | UnwindData |  |
| 1401 | `_wsopen_s` | `0x6883C` | 50 | UnwindData |  |
| 536 | `_close` | `0x68870` | 195 | UnwindData |  |
| 659 | `_fstat64` | `0x689F0` | 969 | UnwindData |  |
| 660 | `_fstat64i32` | `0x68DBC` | 951 | UnwindData |  |
| 658 | `_fstat32i64` | `0x69174` | 958 | UnwindData |  |
| 1049 | `_read` | `0x69534` | 284 | UnwindData |  |
| 747 | `_isatty` | `0x69EC0` | 95 | UnwindData |  |
| 1393 | `_write` | `0x69F20` | 225 | UnwindData |  |
| 870 | `_lseeki64` | `0x6A7F8` | 229 | UnwindData |  |
| 1028 | `_open` | `0x6A974` | 209 | UnwindData |  |
| 1112 | `_sopen` | `0x6AA48` | 65 | UnwindData |  |
| 1113 | `_sopen_s` | `0x6ABF4` | 50 | UnwindData |  |
| 537 | `_commit` | `0x6AC28` | 215 | UnwindData |  |
| 869 | `_lseek` | `0x6AD00` | 225 | UnwindData |  |
| 1033 | `_pipe` | `0x6AEC8` | 731 | UnwindData |  |
| 688 | `_get_osfhandle` | `0x6B4E0` | 116 | UnwindData |  |
| 1029 | `_open_osfhandle` | `0x6B554` | 250 | UnwindData |  |
| 699 | `_getch` | `0x6B72C` | 42 | UnwindData |  |
| 700 | `_getch_nolock` | `0x6B758` | 256 | UnwindData |  |
| 701 | `_getche` | `0x6B858` | 42 | UnwindData |  |
| 702 | `_getche_nolock` | `0x6B884` | 66 | UnwindData |  |
| 847 | `_kbhit` | `0x6B9AC` | 42 | UnwindData |  |
| 1217 | `_ungetch` | `0x6BB7C` | 46 | UnwindData |  |
| 1218 | `_ungetch_nolock` | `0x6BBAC` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 715 | `_getwch` | `0x6BBC8` | 44 | UnwindData |  |
| 716 | `_getwch_nolock` | `0x6BBF4` | 315 | UnwindData |  |
| 717 | `_getwche` | `0x6BD30` | 44 | UnwindData |  |
| 718 | `_getwche_nolock` | `0x6BD5C` | 79 | UnwindData |  |
| 1220 | `_ungetwch` | `0x6BDAC` | 50 | UnwindData |  |
| 1221 | `_ungetwch_nolock` | `0x6BDE0` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1040 | `_putch` | `0x6BE08` | 46 | UnwindData |  |
| 1041 | `_putch_nolock` | `0x6BE38` | 177 | UnwindData |  |
| 1045 | `_putwch` | `0x6BEEC` | 50 | UnwindData |  |
| 1046 | `_putwch_nolock` | `0x6BF20` | 89 | UnwindData |  |
| 276 | `?_open@@YAHPEBDHH@Z` | `0x6BF7C` | 52 | UnwindData |  |
| 284 | `?_sopen@@YAHPEBDHHH@Z` | `0x6BFB0` | 43 | UnwindData |  |
| 286 | `?_wopen@@YAHPEB_WHH@Z` | `0x6BFDC` | 52 | UnwindData |  |
| 287 | `?_wsopen@@YAHPEB_WHHH@Z` | `0x6C010` | 43 | UnwindData |  |
| 524 | `_cgets` | `0x6C03C` | 115 | UnwindData |  |
| 525 | `_cgets_s` | `0x6C0B0` | 302 | UnwindData |  |
| 526 | `_cgetws` | `0x6C1E0` | 107 | UnwindData |  |
| 527 | `_cgetws_s` | `0x6C24C` | 479 | UnwindData |  |
| 533 | `_chsize` | `0x6C42C` | 21 | UnwindData |  |
| 534 | `_chsize_s` | `0x6C5DC` | 239 | UnwindData |  |
| 551 | `_cputs` | `0x6C6CC` | 120 | UnwindData |  |
| 552 | `_cputws` | `0x6C744` | 218 | UnwindData |  |
| 553 | `_creat` | `0x6C820` | 55 | UnwindData |  |
| 583 | `_dup` | `0x6C858` | 203 | UnwindData |  |
| 584 | `_dup2` | `0x6CAD0` | 384 | UnwindData |  |
| 591 | `_eof` | `0x6CDC8` | 279 | UnwindData |  |
| 617 | `_filelength` | `0x6CEE0` | 263 | UnwindData |  |
| 618 | `_filelengthi64` | `0x6CFE8` | 274 | UnwindData |  |
| 685 | `_get_fmode` | `0x6D0FC` | 47 | UnwindData |  |
| 1080 | `_set_fmode` | `0x6D12C` | 61 | UnwindData |  |
| 1091 | `_setmode` | `0x6D16C` | 250 | UnwindData |  |
| 862 | `_locking` | `0x6D344` | 280 | UnwindData |  |
| 1020 | `_mktemp` | `0x6D578` | 77 | UnwindData |  |
| 1021 | `_mktemp_s` | `0x6D5C8` | 329 | UnwindData |  |
| 1192 | `_tell` | `0x6D714` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1193 | `_telli64` | `0x6D720` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1294 | `_wcreat` | `0x6D72C` | 55 | UnwindData |  |
| 1379 | `_wmktemp` | `0x6D764` | 77 | UnwindData |  |
| 1380 | `_wmktemp_s` | `0x6D7B4` | 336 | UnwindData |  |
| 273 | `?_invalid_parameter@@YAXPEBG00I_K@Z` | `0x6D9BC` | 252 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 687 | `_get_invalid_parameter_handler` | `0x6DAB8` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 740 | `_invalid_parameter` | `0x6DAD0` | 101 | UnwindData |  |
| 741 | `_invalid_parameter_noinfo` | `0x6DB38` | 30 | UnwindData |  |
| 742 | `_invalid_parameter_noinfo_noreturn` | `0x6DB58` | 47 | UnwindData |  |
| 743 | `_invoke_watson` | `0x6DB88` | 59 | UnwindData |  |
| 1081 | `_set_invalid_parameter_handler` | `0x6DBC4` | 59 | UnwindData |  |
| 692 | `_get_purecall_handler` | `0x6DC00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1039 | `_purecall` | `0x6DC10` | 42 | UnwindData |  |
| 1085 | `_set_purecall_handler` | `0x6DC3C` | 59 | UnwindData |  |
| 417 | `__dllonexit` | `0x6DCBC` | 209 | UnwindData |  |
| 1027 | `_onexit` | `0x6DD90` | 266 | UnwindData |  |
| 1461 | `atexit` | `0x6DE9C` | 23 | UnwindData |  |
| 383 | `__crtCaptureCurrentContext` | `0x6DF70` | 109 | UnwindData |  |
| 384 | `__crtCapturePreviousContext` | `0x6DFE0` | 113 | UnwindData |  |
| 388 | `__crtCreateEventExW` | `0x6E08C` | 44 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 389 | `__crtCreateSemaphoreExW` | `0x6E0B8` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 390 | `__crtCreateSymbolicLinkW` | `0x6E0D4` | 45 | UnwindData |  |
| 392 | `__crtFlsAlloc` | `0x6E134` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 393 | `__crtFlsFree` | `0x6E150` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 394 | `__crtFlsGetValue` | `0x6E16C` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 395 | `__crtFlsSetValue` | `0x6E188` | 108 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 397 | `__crtGetFileInformationByHandleEx` | `0x6E1F4` | 45 | UnwindData |  |
| 399 | `__crtGetShowWindowMode` | `0x6E224` | 44 | UnwindData |  |
| 400 | `__crtGetTickCount64` | `0x6E250` | 40 | UnwindData |  |
| 403 | `__crtInitializeCriticalSectionEx` | `0x6E278` | 43 | UnwindData |  |
| 404 | `__crtIsPackagedApp` | `0x6E2A4` | 76 | UnwindData |  |
| 409 | `__crtSetFileInformationByHandle` | `0x6E6EC` | 45 | UnwindData |  |
| 410 | `__crtSetThreadStackGuarantee` | `0x6E71C` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 411 | `__crtSetUnhandledExceptionFilter` | `0x6E76C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 412 | `__crtSleep` | `0x6E774` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 413 | `__crtTerminateProcess` | `0x6E77C` | 31 | UnwindData |  |
| 414 | `__crtUnhandledException` | `0x6E79C` | 32 | UnwindData |  |
| 420 | `__fpecode` | `0x6E9C8` | 20 | UnwindData |  |
| 462 | `__pxcptinfoptrs` | `0x6E9EC` | 20 | UnwindData |  |
| 1752 | `raise` | `0x6EAB4` | 563 | UnwindData |  |
| 1783 | `signal` | `0x6ECE8` | 651 | UnwindData |  |
| 1754 | `rand_s` | `0x6EF7C` | 314 | UnwindData |  |
| 350 | `__C_specific_handler` | `0x6F0B8` | 481 | UnwindData |  |
| 459 | `__pctype_func` | `0x6F92C` | 59 | UnwindData |  |
| 461 | `__pwctype_func` | `0x6F968` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 346 | `_XcptFilter` | `0x6F970` | 460 | UnwindData |  |
| 351 | `__CppXcptFilter` | `0x6FB3C` | 596 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 585 | `_dupenv_s` | `0x6FD90` | 258 | UnwindData |  |
| 1633 | `getenv` | `0x6FF30` | 107 | UnwindData |  |
| 1634 | `getenv_s` | `0x6FF9C` | 251 | UnwindData |  |
| 1347 | `_wdupenv_s` | `0x70150` | 258 | UnwindData |  |
| 1374 | `_wgetenv` | `0x70254` | 107 | UnwindData |  |
| 1375 | `_wgetenv_s` | `0x70374` | 252 | UnwindData |  |
| 855 | `_local_unwind` | `0x70570` | 36 | UnwindData |  |
| 363 | `__NLG_Dispatch2` | `0x705C0` | 1 | UnwindData |  |
| 364 | `__NLG_Return2` | `0x705D0` | 1 | UnwindData |  |
| 463 | `__report_gsfailure` | `0x706B8` | 209 | UnwindData |  |
| 371 | `___lc_codepage_func` | `0x7083C` | 55 | UnwindData |  |
| 372 | `___lc_collate_cp_func` | `0x70874` | 55 | UnwindData |  |
| 373 | `___lc_locale_name_func` | `0x708AC` | 59 | UnwindData |  |
| 374 | `___mb_cur_max_func` | `0x708E8` | 58 | UnwindData |  |
| 375 | `___mb_cur_max_l_func` | `0x70924` | 1,152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 376 | `___setlc_active_func` | `0x70DA4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 377 | `___unguarded_readlc_active_add_func` | `0x70DAC` | 140 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 382 | `__create_locale` | `0x70E38` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 421 | `__free_locale` | `0x70E40` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 422 | `__get_current_locale` | `0x70E48` | 612 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 539 | `_configthreadlocale` | `0x710AC` | 105 | UnwindData |  |
| 554 | `_create_locale` | `0x711D4` | 119 | UnwindData |  |
| 647 | `_free_locale` | `0x71620` | 154 | UnwindData |  |
| 680 | `_get_current_locale` | `0x716BC` | 156 | UnwindData |  |
| 1295 | `_wcreate_locale` | `0x71758` | 255 | UnwindData |  |
| 1399 | `_wsetlocale` | `0x718C0` | 411 | UnwindData |  |
| 406 | `__crtLCMapStringA` | `0x7268C` | 150 | UnwindData |  |
| 408 | `__crtLCMapStringW` | `0x72724` | 73 | UnwindData |  |
| 385 | `__crtCompareStringA` | `0x72AD8` | 137 | UnwindData |  |
| 387 | `__crtCompareStringW` | `0x72B64` | 165 | UnwindData |  |
| 386 | `__crtCompareStringEx` | `0x72CDC` | 143 | UnwindData |  |
| 391 | `__crtEnumSystemLocalesEx` | `0x72E5C` | 68 | UnwindData |  |
| 396 | `__crtGetDateFormatEx` | `0x72EA0` | 122 | UnwindData |  |
| 398 | `__crtGetLocaleInfoEx` | `0x72F1C` | 80 | UnwindData |  |
| 401 | `__crtGetTimeFormatEx` | `0x72F6C` | 117 | UnwindData |  |
| 402 | `__crtGetUserDefaultLocaleName` | `0x72FE4` | 65 | UnwindData |  |
| 405 | `__crtIsValidLocaleName` | `0x73028` | 50 | UnwindData |  |
| 407 | `__crtLCMapStringEx` | `0x7305C` | 143 | UnwindData |  |
| 114 | `??2@YAPEAX_KHPEBDH@Z` | `0x73144` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `??_U@YAPEAX_K@Z` | `0x73144` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `??_U@YAPEAX_KHPEBDH@Z` | `0x7314C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `??3@YAXPEAXHPEBDH@Z` | `0x73154` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `??_V@YAXPEAX@Z` | `0x73154` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `??_V@YAXPEAXHPEBDH@Z` | `0x7315C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 415 | `__crt_debugger_hook` | `0x73164` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1686 | `localeconv` | `0x7316C` | 56 | UnwindData |  |
| 434 | `__lconv_init` | `0x731A4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 469 | `__sys_errlist` | `0x731B4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 470 | `__sys_nerr` | `0x731BC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 482 | `__wcserror` | `0x731C4` | 392 | UnwindData |  |
| 483 | `__wcserror_s` | `0x7334C` | 238 | UnwindData |  |
| 500 | `_assert` | `0x7343C` | 2,262 | UnwindData |  |
| 516 | `_byteswap_uint64` | `0x73D14` | 116 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 517 | `_byteswap_ulong` | `0x73D88` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 518 | `_byteswap_ushort` | `0x73DB0` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 852 | `_lfind` | `0x73DC4` | 151 | UnwindData |  |
| 853 | `_lfind_s` | `0x73E5C` | 156 | UnwindData |  |
| 865 | `_lrotl` | `0x73EF8` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1056 | `_rotl` | `0x73EF8` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1057 | `_rotl64` | `0x73F04` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 866 | `_lrotr` | `0x73F10` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1058 | `_rotr` | `0x73F10` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1059 | `_rotr64` | `0x73F1C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 867 | `_lsearch` | `0x73F28` | 160 | UnwindData |  |
| 868 | `_lsearch_s` | `0x73FC8` | 165 | UnwindData |  |
| 875 | `_makepath` | `0x74070` | 39 | UnwindData |  |
| 876 | `_makepath_s` | `0x74098` | 328 | UnwindData |  |
| 1042 | `_putenv` | `0x741E0` | 50 | UnwindData |  |
| 1043 | `_putenv_s` | `0x7448C` | 117 | UnwindData |  |
| 1072 | `_searchenv` | `0x74504` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1073 | `_searchenv_s` | `0x74510` | 814 | UnwindData |  |
| 1075 | `_set_abort_behavior` | `0x74840` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1440 | `abort` | `0x7485C` | 85 | UnwindData |  |
| 1087 | `_setjmp` | `0x748D0` | 160 | UnwindData |  |
| 1780 | `setjmp` | `0x748D0` | 160 | UnwindData |  |
| 1088 | `_setjmpex` | `0x74980` | 144 | UnwindData |  |
| 1122 | `_splitpath` | `0x74A10` | 136 | UnwindData |  |
| 1123 | `_splitpath_s` | `0x74D28` | 671 | UnwindData |  |
| 1139 | `_strerror` | `0x74FC8` | 341 | UnwindData |  |
| 1140 | `_strerror_s` | `0x75120` | 228 | UnwindData |  |
| 1214 | `_umask` | `0x75204` | 34 | UnwindData |  |
| 1215 | `_umask_s` | `0x75228` | 67 | UnwindData |  |
| 1228 | `_vacopy` | `0x7526C` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1290 | `_wassert` | `0x75270` | 2,384 | UnwindData |  |
| 1298 | `_wcserror` | `0x75BE4` | 166 | UnwindData |  |
| 1299 | `_wcserror_s` | `0x75C8C` | 173 | UnwindData |  |
| 1376 | `_wmakepath` | `0x75D3C` | 39 | UnwindData |  |
| 1377 | `_wmakepath_s` | `0x75D64` | 341 | UnwindData |  |
| 1382 | `_wperror` | `0x75EBC` | 376 | UnwindData |  |
| 1389 | `_wputenv` | `0x76034` | 50 | UnwindData |  |
| 1390 | `_wputenv_s` | `0x7631C` | 117 | UnwindData |  |
| 1397 | `_wsearchenv` | `0x76394` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1398 | `_wsearchenv_s` | `0x763A0` | 834 | UnwindData |  |
| 1410 | `_wsplitpath` | `0x766E4` | 136 | UnwindData |  |
| 1411 | `_wsplitpath_s` | `0x76A00` | 688 | UnwindData |  |
| 1466 | `bsearch` | `0x76CB0` | 240 | UnwindData |  |
| 1467 | `bsearch_s` | `0x76DA0` | 250 | UnwindData |  |
| 1643 | `imaxdiv` | `0x76E9C` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1441 | `abs` | `0x76EBC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1672 | `labs` | `0x76EBC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1554 | `div` | `0x76EC4` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1674 | `ldiv` | `0x76EC4` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 487 | `_abs64` | `0x76EDC` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1642 | `imaxabs` | `0x76EDC` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1678 | `llabs` | `0x76EDC` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1679 | `lldiv` | `0x76EE8` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1700 | `longjmp` | `0x76F10` | 236 | UnwindData |  |
| 1740 | `perror` | `0x76FFC` | 173 | UnwindData |  |
| 1750 | `qsort` | `0x770B0` | 91 | UnwindData |  |
| 1751 | `qsort_s` | `0x77470` | 101 | UnwindData |  |
| 1753 | `rand` | `0x77880` | 41 | UnwindData |  |
| 1792 | `srand` | `0x778AC` | 22 | UnwindData |  |
| 1781 | `setlocale` | `0x778C4` | 807 | UnwindData |  |
| 1803 | `strerror` | `0x77BEC` | 154 | UnwindData |  |
| 1804 | `strerror_s` | `0x77C88` | 142 | UnwindData |  |
| 1846 | `towctrans` | `0x77D18` | 30 | UnwindData |  |
| 1918 | `wctrans` | `0x77D38` | 133 | UnwindData |  |
| 1919 | `wctype` | `0x77DC0` | 133 | UnwindData |  |
| 369 | `__STRINGTOLD_L` | `0x7C4F0` | 117 | UnwindData |  |
| 1 | `$I10_OUTPUT` | `0x7E674` | 2,776 | UnwindData |  |
| 731 | `_hypot` | `0x7F370` | 610 | UnwindData |  |
| 1533 | `cproj` | `0x7F5E0` | 186 | UnwindData |  |
| 328 | `_FCbuild` | `0x7F69C` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1534 | `cprojf` | `0x7F6B0` | 142 | UnwindData |  |
| 325 | `_Cbuild` | `0x7F740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 337 | `_LCbuild` | `0x7F740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1535 | `cprojl` | `0x7F750` | 186 | UnwindData |  |
| 520 | `_cabs` | `0x7F80C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 530 | `_chgsign` | `0x7F81C` | 36 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 531 | `_chgsignf` | `0x7F840` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 535 | `_clearfp` | `0x7F85C` | 80 | UnwindData |  |
| 540 | `_control87` | `0x7F8AC` | 656 | UnwindData |  |
| 541 | `_controlfp` | `0x7FB3C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 637 | `_fpreset` | `0x7FB48` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1076 | `_set_controlfp` | `0x7FB54` | 52 | UnwindData |  |
| 1134 | `_statusfp` | `0x7FB88` | 68 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 542 | `_controlfp_s` | `0x7FBCC` | 99 | UnwindData |  |
| 543 | `_copysign` | `0x7FC30` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 544 | `_copysignf` | `0x7FC68` | 44 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 575 | `_dclass` | `0x7FC94` | 25 | UnwindData |  |
| 579 | `_dpcomp` | `0x7FCB0` | 99 | UnwindData |  |
| 580 | `_dsign` | `0x7FD14` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 850 | `_ldsign` | `0x7FD14` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1725 | `nan` | `0x7FD2C` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 582 | `_dtest` | `0x7FE4C` | 312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 611 | `_fdtest` | `0x7FF84` | 228 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 851 | `_ldtest` | `0x80068` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 607 | `_fdclass` | `0x80070` | 25 | UnwindData |  |
| 609 | `_fdpcomp` | `0x8008C` | 97 | UnwindData |  |
| 610 | `_fdsign` | `0x800F0` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1726 | `nanf` | `0x80104` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 629 | `_finite` | `0x80110` | 44 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 630 | `_finitef` | `0x8013C` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 634 | `_fpclass` | `0x80154` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 635 | `_fpclassf` | `0x80204` | 120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 818 | `_isnan` | `0x8027C` | 44 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 819 | `_isnanf` | `0x802A8` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1025 | `_nextafter` | `0x802C4` | 484 | UnwindData |  |
| 1026 | `_nextafterf` | `0x804A8` | 393 | UnwindData |  |
| 1060 | `_scalb` | `0x80634` | 473 | UnwindData |  |
| 1061 | `_scalbf` | `0x80810` | 413 | UnwindData |  |
| 636 | `_fpieee_flt` | `0x809B0` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 732 | `_hypotf` | `0x809CC` | 326 | UnwindData |  |
| 844 | `_j0` | `0x80B14` | 576 | UnwindData |  |
| 845 | `_j1` | `0x80D54` | 619 | UnwindData |  |
| 846 | `_jn` | `0x80FC0` | 381 | UnwindData |  |
| 1437 | `_y0` | `0x81140` | 638 | UnwindData |  |
| 1438 | `_y1` | `0x813C0` | 663 | UnwindData |  |
| 1439 | `_yn` | `0x81658` | 231 | UnwindData |  |
| 848 | `_ldclass` | `0x81790` | 25 | UnwindData |  |
| 849 | `_ldpcomp` | `0x817AC` | 99 | UnwindData |  |
| 1727 | `nanl` | `0x81810` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 863 | `_logb` | `0x8181C` | 285 | UnwindData |  |
| 864 | `_logbf` | `0x8193C` | 224 | UnwindData |  |
| 1074 | `_set_FMA3_enable` | `0x81ACC` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1442 | `acos` | `0x81AE4` | 741 | UnwindData |  |
| 1443 | `acosf` | `0x81DCC` | 652 | UnwindData |  |
| 1444 | `acosh` | `0x82058` | 194 | UnwindData |  |
| 1445 | `acoshf` | `0x8211C` | 191 | UnwindData |  |
| 1446 | `acoshl` | `0x821DC` | 177 | UnwindData |  |
| 1449 | `asin` | `0x82290` | 709 | UnwindData |  |
| 1450 | `asinf` | `0x82558` | 596 | UnwindData |  |
| 1451 | `asinh` | `0x827AC` | 190 | UnwindData |  |
| 1452 | `asinhf` | `0x8286C` | 188 | UnwindData |  |
| 1453 | `asinhl` | `0x82928` | 191 | UnwindData |  |
| 1454 | `atan` | `0x829E8` | 603 | UnwindData |  |
| 1455 | `atan2` | `0x82C44` | 1,979 | UnwindData |  |
| 1456 | `atan2f` | `0x83400` | 1,152 | UnwindData |  |
| 1457 | `atanf` | `0x83880` | 573 | UnwindData |  |
| 1458 | `atanh` | `0x83AC0` | 189 | UnwindData |  |
| 1459 | `atanhf` | `0x83B80` | 186 | UnwindData |  |
| 1460 | `atanhl` | `0x83C3C` | 189 | UnwindData |  |
| 1470 | `cabsf` | `0x83CFC` | 50 | UnwindData |  |
| 1469 | `cabs` | `0x83D30` | 66 | UnwindData |  |
| 1471 | `cabsl` | `0x83D30` | 66 | UnwindData |  |
| 1472 | `cacos` | `0x83D74` | 820 | UnwindData |  |
| 1473 | `cacosf` | `0x840A8` | 689 | UnwindData |  |
| 1474 | `cacosh` | `0x8435C` | 872 | UnwindData |  |
| 1475 | `cacoshf` | `0x846C4` | 720 | UnwindData |  |
| 1476 | `cacoshl` | `0x84994` | 872 | UnwindData |  |
| 1477 | `cacosl` | `0x84CFC` | 820 | UnwindData |  |
| 1479 | `carg` | `0x85030` | 66 | UnwindData |  |
| 1481 | `cargl` | `0x85030` | 66 | UnwindData |  |
| 1480 | `cargf` | `0x85074` | 50 | UnwindData |  |
| 1482 | `casin` | `0x850A8` | 208 | UnwindData |  |
| 1483 | `casinf` | `0x85178` | 106 | UnwindData |  |
| 1484 | `casinh` | `0x851E4` | 822 | UnwindData |  |
| 1485 | `casinhf` | `0x8551C` | 640 | UnwindData |  |
| 1486 | `casinhl` | `0x8579C` | 822 | UnwindData |  |
| 1487 | `casinl` | `0x85AD4` | 208 | UnwindData |  |
| 1488 | `catan` | `0x85BA4` | 208 | UnwindData |  |
| 1489 | `catanf` | `0x85C74` | 106 | UnwindData |  |
| 1490 | `catanh` | `0x85CE0` | 840 | UnwindData |  |
| 1491 | `catanhf` | `0x86028` | 779 | UnwindData |  |
| 1492 | `catanhl` | `0x86334` | 840 | UnwindData |  |
| 1493 | `catanl` | `0x8667C` | 208 | UnwindData |  |
| 1494 | `cbrt` | `0x8674C` | 379 | UnwindData |  |
| 1495 | `cbrtf` | `0x868C8` | 336 | UnwindData |  |
| 1496 | `cbrtl` | `0x86A18` | 379 | UnwindData |  |
| 1497 | `ccos` | `0x86B94` | 121 | UnwindData |  |
| 1498 | `ccosf` | `0x86C10` | 65 | UnwindData |  |
| 1499 | `ccosh` | `0x86D4C` | 423 | UnwindData |  |
| 1500 | `ccoshf` | `0x86FEC` | 357 | UnwindData |  |
| 1501 | `ccoshl` | `0x8724C` | 445 | UnwindData |  |
| 1502 | `ccosl` | `0x8740C` | 121 | UnwindData |  |
| 1503 | `ceil` | `0x87488` | 273 | UnwindData |  |
| 1504 | `ceilf` | `0x8759C` | 211 | UnwindData |  |
| 1505 | `cexp` | `0x87670` | 503 | UnwindData |  |
| 1506 | `cexpf` | `0x87868` | 456 | UnwindData |  |
| 1507 | `cexpl` | `0x87A30` | 503 | UnwindData |  |
| 1509 | `cimagf` | `0x87C28` | 47 | UnwindData |  |
| 1508 | `cimag` | `0x87C58` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1510 | `cimagl` | `0x87C58` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1514 | `clog` | `0x87C60` | 579 | UnwindData |  |
| 1515 | `clog10` | `0x87EA4` | 81 | UnwindData |  |
| 1516 | `clog10f` | `0x87EF8` | 30 | UnwindData |  |
| 1517 | `clog10l` | `0x87F18` | 81 | UnwindData |  |
| 1518 | `clogf` | `0x87F6C` | 526 | UnwindData |  |
| 1519 | `clogl` | `0x8817C` | 591 | UnwindData |  |
| 1521 | `conjf` | `0x883CC` | 53 | UnwindData |  |
| 1520 | `conj` | `0x88404` | 102 | UnwindData |  |
| 1522 | `conjl` | `0x88404` | 102 | UnwindData |  |
| 1524 | `copysignf` | `0x8846C` | 52 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1523 | `copysign` | `0x884A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1525 | `copysignl` | `0x884A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1526 | `cos` | `0x884E0` | 1,370 | UnwindData |  |
| 1527 | `cosf` | `0x88A40` | 1,279 | UnwindData |  |
| 1528 | `cosh` | `0x88F40` | 937 | UnwindData |  |
| 1529 | `coshf` | `0x89414` | 704 | UnwindData |  |
| 1530 | `cpow` | `0x89940` | 334 | UnwindData |  |
| 1531 | `cpowf` | `0x89B60` | 168 | UnwindData |  |
| 1532 | `cpowl` | `0x89C08` | 334 | UnwindData |  |
| 1537 | `crealf` | `0x89D58` | 46 | UnwindData |  |
| 1536 | `creal` | `0x89D88` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1538 | `creall` | `0x89D88` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1539 | `csin` | `0x89D90` | 208 | UnwindData |  |
| 1540 | `csinf` | `0x89E60` | 106 | UnwindData |  |
| 1541 | `csinh` | `0x8A06C` | 339 | UnwindData |  |
| 1542 | `csinhf` | `0x8A340` | 278 | UnwindData |  |
| 1543 | `csinhl` | `0x8A5F8` | 365 | UnwindData |  |
| 1544 | `csinl` | `0x8A768` | 208 | UnwindData |  |
| 1545 | `csqrt` | `0x8AA1C` | 489 | UnwindData |  |
| 1546 | `csqrtf` | `0x8ADE4` | 443 | UnwindData |  |
| 1547 | `csqrtl` | `0x8B184` | 487 | UnwindData |  |
| 1548 | `ctan` | `0x8B36C` | 208 | UnwindData |  |
| 1549 | `ctanf` | `0x8B43C` | 106 | UnwindData |  |
| 1550 | `ctanh` | `0x8B4A8` | 437 | UnwindData |  |
| 1551 | `ctanhf` | `0x8B660` | 384 | UnwindData |  |
| 1552 | `ctanhl` | `0x8B7E0` | 437 | UnwindData |  |
| 1553 | `ctanl` | `0x8B998` | 208 | UnwindData |  |
| 1555 | `erf` | `0x8BAE0` | 373 | UnwindData |  |
| 1556 | `erfc` | `0x8BC74` | 611 | UnwindData |  |
| 1557 | `erfcf` | `0x8BEF4` | 596 | UnwindData |  |
| 1558 | `erfcl` | `0x8C148` | 611 | UnwindData |  |
| 1559 | `erff` | `0x8C434` | 294 | UnwindData |  |
| 1560 | `erfl` | `0x8C5D4` | 373 | UnwindData |  |
| 1562 | `exp` | `0x8C750` | 1,125 | UnwindData |  |
| 1563 | `exp2` | `0x8CE40` | 232 | UnwindData |  |
| 1564 | `exp2f` | `0x8D18C` | 228 | UnwindData |  |
| 1565 | `exp2l` | `0x8D4F8` | 232 | UnwindData |  |
| 1566 | `expf` | `0x8D5E0` | 613 | UnwindData |  |
| 1567 | `expm1` | `0x8D848` | 287 | UnwindData |  |
| 1568 | `expm1f` | `0x8D968` | 213 | UnwindData |  |
| 1569 | `expm1l` | `0x8DA40` | 287 | UnwindData |  |
| 1570 | `fabs` | `0x8DB60` | 224 | UnwindData |  |
| 1572 | `fdim` | `0x8DC40` | 96 | UnwindData |  |
| 1573 | `fdimf` | `0x8DCA0` | 95 | UnwindData |  |
| 1574 | `fdiml` | `0x8DD00` | 96 | UnwindData |  |
| 1575 | `feclearexcept` | `0x8DD60` | 70 | UnwindData |  |
| 1576 | `fegetenv` | `0x8DDA8` | 32 | UnwindData |  |
| 1577 | `fegetexceptflag` | `0x8DDC8` | 46 | UnwindData |  |
| 1578 | `fegetround` | `0x8DDF8` | 19 | UnwindData |  |
| 1579 | `feholdexcept` | `0x8DE0C` | 61 | UnwindData |  |
| 1581 | `feraiseexcept` | `0x8DE4C` | 67 | UnwindData |  |
| 1583 | `fesetenv` | `0x8DE90` | 76 | UnwindData |  |
| 1584 | `fesetexceptflag` | `0x8DEDC` | 87 | UnwindData |  |
| 1585 | `fesetround` | `0x8DF34` | 65 | UnwindData |  |
| 1586 | `fetestexcept` | `0x8DF78` | 30 | UnwindData |  |
| 1587 | `feupdateenv` | `0x8DF98` | 64 | UnwindData |  |
| 1594 | `floor` | `0x8DFD8` | 255 | UnwindData |  |
| 1595 | `floorf` | `0x8E0D8` | 205 | UnwindData |  |
| 1596 | `fma` | `0x8E8C8` | 609 | UnwindData |  |
| 1597 | `fmaf` | `0x8F1D4` | 629 | UnwindData |  |
| 1598 | `fmal` | `0x8FB1C` | 609 | UnwindData |  |
| 1599 | `fmax` | `0x8FD80` | 110 | UnwindData |  |
| 1600 | `fmaxf` | `0x8FDF0` | 108 | UnwindData |  |
| 1601 | `fmaxl` | `0x8FE5C` | 110 | UnwindData |  |
| 1602 | `fmin` | `0x8FECC` | 110 | UnwindData |  |
| 1603 | `fminf` | `0x8FF3C` | 108 | UnwindData |  |
| 1604 | `fminl` | `0x8FFA8` | 110 | UnwindData |  |
| 1605 | `fmod` | `0x90018` | 1,335 | UnwindData |  |
| 1606 | `fmodf` | `0x90550` | 710 | UnwindData |  |
| 1620 | `frexp` | `0x90818` | 220 | UnwindData |  |
| 1639 | `ilogb` | `0x908F4` | 68 | UnwindData |  |
| 1640 | `ilogbf` | `0x90938` | 68 | UnwindData |  |
| 1641 | `ilogbl` | `0x9097C` | 68 | UnwindData |  |
| 1673 | `ldexp` | `0x909C0` | 377 | UnwindData |  |
| 1675 | `lgamma` | `0x91104` | 582 | UnwindData |  |
| 1676 | `lgammaf` | `0x91A6C` | 567 | UnwindData |  |
| 1677 | `lgammal` | `0x9235C` | 582 | UnwindData |  |
| 1680 | `llrint` | `0x925A4` | 124 | UnwindData |  |
| 1681 | `llrintf` | `0x92620` | 121 | UnwindData |  |
| 1682 | `llrintl` | `0x9269C` | 124 | UnwindData |  |
| 1683 | `llround` | `0x92718` | 97 | UnwindData |  |
| 1684 | `llroundf` | `0x9277C` | 95 | UnwindData |  |
| 1685 | `llroundl` | `0x927DC` | 97 | UnwindData |  |
| 1687 | `log` | `0x92840` | 1,339 | UnwindData |  |
| 1688 | `log10` | `0x92D80` | 1,467 | UnwindData |  |
| 1689 | `log10f` | `0x93340` | 1,253 | UnwindData |  |
| 1690 | `log1p` | `0x93828` | 190 | UnwindData |  |
| 1691 | `log1pf` | `0x938E8` | 188 | UnwindData |  |
| 1692 | `log1pl` | `0x939A4` | 190 | UnwindData |  |
| 1693 | `log2` | `0x93A64` | 879 | UnwindData |  |
| 1694 | `log2f` | `0x93F88` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1695 | `log2l` | `0x941A8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1696 | `logb` | `0x941B0` | 107 | UnwindData |  |
| 1697 | `logbf` | `0x9421C` | 106 | UnwindData |  |
| 1698 | `logbl` | `0x94288` | 107 | UnwindData |  |
| 1699 | `logf` | `0x94300` | 1,030 | UnwindData |  |
| 1701 | `lrint` | `0x94708` | 123 | UnwindData |  |
| 1702 | `lrintf` | `0x94784` | 120 | UnwindData |  |
| 1703 | `lrintl` | `0x947FC` | 123 | UnwindData |  |
| 1704 | `lround` | `0x94878` | 96 | UnwindData |  |
| 1705 | `lroundf` | `0x948D8` | 94 | UnwindData |  |
| 1706 | `lroundl` | `0x94938` | 96 | UnwindData |  |
| 1723 | `modf` | `0x94998` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1724 | `modff` | `0x94A58` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1728 | `nearbyint` | `0x94AE8` | 44 | UnwindData |  |
| 1729 | `nearbyintf` | `0x94B14` | 44 | UnwindData |  |
| 1730 | `nearbyintl` | `0x94B40` | 44 | UnwindData |  |
| 1731 | `nextafter` | `0x94B6C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1732 | `nextafterf` | `0x94B74` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1733 | `nextafterl` | `0x94B80` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1734 | `nexttoward` | `0x94B88` | 354 | UnwindData |  |
| 1735 | `nexttowardf` | `0x94CEC` | 311 | UnwindData |  |
| 1736 | `nexttowardl` | `0x94E24` | 354 | UnwindData |  |
| 1738 | `normf` | `0x94F88` | 54 | UnwindData |  |
| 1737 | `norm` | `0x94FC0` | 78 | UnwindData |  |
| 1739 | `norml` | `0x94FC0` | 78 | UnwindData |  |
| 1741 | `pow` | `0x95010` | 5,777 | UnwindData |  |
| 1742 | `powf` | `0x966B0` | 2,949 | UnwindData |  |
| 1756 | `remainder` | `0x97238` | 1,457 | UnwindData |  |
| 1757 | `remainderf` | `0x977EC` | 774 | UnwindData |  |
| 1758 | `remainderl` | `0x97AF4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1760 | `remquo` | `0x97AFC` | 483 | UnwindData |  |
| 1761 | `remquof` | `0x97CE0` | 476 | UnwindData |  |
| 1762 | `remquol` | `0x97EBC` | 483 | UnwindData |  |
| 1765 | `rint` | `0x981D0` | 80 | UnwindData |  |
| 1766 | `rintf` | `0x98350` | 79 | UnwindData |  |
| 1767 | `rintl` | `0x984D0` | 80 | UnwindData |  |
| 1768 | `round` | `0x98520` | 101 | UnwindData |  |
| 1769 | `roundf` | `0x98588` | 101 | UnwindData |  |
| 1770 | `roundl` | `0x985F0` | 101 | UnwindData |  |
| 1771 | `scalbln` | `0x98658` | 94 | UnwindData |  |
| 1774 | `scalbn` | `0x98658` | 94 | UnwindData |  |
| 1772 | `scalblnf` | `0x986B8` | 94 | UnwindData |  |
| 1775 | `scalbnf` | `0x986B8` | 94 | UnwindData |  |
| 1773 | `scalblnl` | `0x98718` | 94 | UnwindData |  |
| 1776 | `scalbnl` | `0x98718` | 94 | UnwindData |  |
| 1784 | `sin` | `0x98780` | 1,300 | UnwindData |  |
| 1785 | `sinf` | `0x98CA0` | 1,734 | UnwindData |  |
| 1786 | `sinh` | `0x99368` | 1,013 | UnwindData |  |
| 1787 | `sinhf` | `0x99888` | 726 | UnwindData |  |
| 1790 | `sqrt` | `0x99C88` | 256 | UnwindData |  |
| 1791 | `sqrtf` | `0x99D88` | 220 | UnwindData |  |
| 1833 | `tan` | `0x99E70` | 1,363 | UnwindData |  |
| 1834 | `tanf` | `0x9A5B0` | 1,585 | UnwindData |  |
| 1835 | `tanh` | `0x9AD0C` | 720 | UnwindData |  |
| 1836 | `tanhf` | `0x9AFDC` | 729 | UnwindData |  |
| 1837 | `tgamma` | `0x9BC34` | 578 | UnwindData |  |
| 1838 | `tgammaf` | `0x9C720` | 572 | UnwindData |  |
| 1839 | `tgammal` | `0x9D2D8` | 578 | UnwindData |  |
| 1849 | `trunc` | `0x9D51C` | 33 | UnwindData |  |
| 1850 | `truncf` | `0x9D540` | 33 | UnwindData |  |
| 1851 | `truncl` | `0x9D564` | 33 | UnwindData |  |
| 129 | `??_7exception@std@@6B@` | `0xA97B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `??_7bad_cast@std@@6B@` | `0xA97E0` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `??_7bad_typeid@std@@6B@` | `0xA97F8` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `??_7__non_rtti_object@std@@6B@` | `0xA9810` | 6,416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1346 | `_wctype` | `0xAB120` | 16,112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1190 | `_sys_errlist` | `0xAF010` | 185,440 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 744 | `_iob` | `0xDC470` | 1,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1197 | `_timezone` | `0xDC8B0` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 574 | `_daylight` | `0xDC8B4` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 581 | `_dstbias` | `0xDC8B8` | 136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1204 | `_tzname` | `0xDC940` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 903 | `_mbctype` | `0xDC970` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 882 | `_mbcasemap` | `0xDCA80` | 1,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 380 | `__badioinfo` | `0xDD180` | 408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1031 | `_pctype` | `0xDD318` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1048 | `_pwctype` | `0xDD320` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 435 | `__mb_cur_max` | `0xDD328` | 1,112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 433 | `__lconv` | `0xDD780` | 172 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1191 | `_sys_nerr` | `0xDD82C` | 964 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 335 | `_HUGE` | `0xDDBF0` | 10,244 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 378 | `__argc` | `0xE03F4` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 379 | `__argv` | `0xE03F8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 481 | `__wargv` | `0xE0400` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 590 | `_environ` | `0xE0408` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1348 | `_wenviron` | `0xE0410` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1032 | `_pgmptr` | `0xE0418` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1383 | `_wpgmptr` | `0xE0428` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 486 | `__winitenv` | `0xE0438` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 426 | `__initenv` | `0xE0440` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 490 | `_acmdln` | `0xE0458` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1293 | `_wcmdln` | `0xE0460` | 4,836 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 538 | `_commode` | `0xE1744` | 620 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 460 | `__pioinfo` | `0xE19B0` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 633 | `_fmode` | `0xE1BB0` | 6,284 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 479 | `__unguarded_readlc_active` | `0xE343C` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 465 | `__setlc_active` | `0xE3440` | 0 | Indeterminate |  |
