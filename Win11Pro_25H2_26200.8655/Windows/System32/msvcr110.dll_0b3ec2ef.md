# Binary Specification: msvcr110.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\msvcr110.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0b3ec2efbdd40f01326e993449a4cee5bf7e709c98f5c2920dbf1c4d983e8221`
* **Total Exported Functions:** 1655

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 10 | `??0_Context@details@Concurrency@@QEAA@PEAVContext@2@@Z` | `0x1000` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `??0_Scheduler@details@Concurrency@@QEAA@PEAVScheduler@2@@Z` | `0x1000` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `??_F_Context@details@Concurrency@@QEAAXXZ` | `0x1008` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `??_F_Scheduler@details@Concurrency@@QEAAXXZ` | `0x1008` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 208 | `?_GetScheduler@_Scheduler@details@Concurrency@@QEAAPEAVScheduler@3@XZ` | `0x1010` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `??4?$_SpinWait@$00@details@Concurrency@@QEAAAEAV012@AEBV012@@Z` | `0x1014` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `??4?$_SpinWait@$0A@@details@Concurrency@@QEAAAEAV012@AEBV012@@Z` | `0x1014` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `??_F?$_SpinWait@$00@details@Concurrency@@QEAAXXZ` | `0x1030` | 884 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `??_F?$_SpinWait@$0A@@details@Concurrency@@QEAAXXZ` | `0x1030` | 884 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0?$_SpinWait@$00@details@Concurrency@@QEAA@P6AXXZ@Z` | `0x13A4` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0?$_SpinWait@$0A@@details@Concurrency@@QEAA@P6AXXZ@Z` | `0x13A4` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 247 | `?_SpinOnce@?$_SpinWait@$00@details@Concurrency@@QEAA_NXZ` | `0x13B0` | 163 | UnwindData |  |
| 201 | `?_DoYield@?$_SpinWait@$00@details@Concurrency@@IEAAXXZ` | `0x1454` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 233 | `?_Reset@?$_SpinWait@$00@details@Concurrency@@IEAAXXZ` | `0x1458` | 36 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 218 | `?_NumberOfSpins@?$_SpinWait@$00@details@Concurrency@@IEAAKXZ` | `0x147C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 219 | `?_NumberOfSpins@?$_SpinWait@$0A@@details@Concurrency@@IEAAKXZ` | `0x147C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 245 | `?_ShouldSpinAgain@?$_SpinWait@$00@details@Concurrency@@IEAA_NXZ` | `0x1484` | 268 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 246 | `?_ShouldSpinAgain@?$_SpinWait@$0A@@details@Concurrency@@IEAA_NXZ` | `0x1484` | 268 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 242 | `?_SetSpinCount@?$_SpinWait@$00@details@Concurrency@@QEAAXI@Z` | `0x1590` | 268 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `??1critical_section@Concurrency@@QEAA@XZ` | `0x169C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `??1reader_writer_lock@Concurrency@@QEAA@XZ` | `0x169C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 199 | `?_Destroy@_AsyncTaskCollection@details@Concurrency@@EEAAXXZ` | `0x16AC` | 24 | UnwindData |  |
| 200 | `?_Destroy@_CancellationTokenState@details@Concurrency@@EEAAXXZ` | `0x16AC` | 24 | UnwindData |  |
| 217 | `?_NewTokenState@_CancellationTokenState@details@Concurrency@@SAPEAV123@XZ` | `0x1764` | 34 | UnwindData |  |
| 7 | `??0_CancellationTokenState@details@Concurrency@@AEAA@XZ` | `0x1788` | 100 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `??1_CancellationTokenState@details@Concurrency@@UEAA@XZ` | `0x17EC` | 168 | UnwindData |  |
| 187 | `?_Cancel@_CancellationTokenState@details@Concurrency@@QEAAXXZ` | `0x1894` | 141 | UnwindData |  |
| 223 | `?_RegisterCallback@_CancellationTokenState@details@Concurrency@@QEAAXPEAV_CancellationTokenRegistration@23@@Z` | `0x1924` | 177 | UnwindData |  |
| 222 | `?_RegisterCallback@_CancellationTokenState@details@Concurrency@@QEAAPEAV_CancellationTokenRegistration@23@P6AXPEAX@Z0H@Z` | `0x19D8` | 153 | UnwindData |  |
| 198 | `?_DeregisterCallback@_CancellationTokenState@details@Concurrency@@QEAAXPEAV_CancellationTokenRegistration@23@@Z` | `0x1A74` | 325 | UnwindData |  |
| 210 | `?_Invoke@_CancellationTokenRegistration@details@Concurrency@@AEAAXXZ` | `0x1BBC` | 91 | UnwindData |  |
| 190 | `?_CheckTaskCollection@_UnrealizedChore@details@Concurrency@@IEAAXXZ` | `0x1C84` | 108 | UnwindData |  |
| 163 | `?Id@Context@Concurrency@@SAIXZ` | `0x23A4` | 58 | UnwindData |  |
| 177 | `?VirtualProcessorId@Context@Concurrency@@SAIXZ` | `0x23E0` | 59 | UnwindData |  |
| 171 | `?ScheduleGroupId@Context@Concurrency@@SAIXZ` | `0x241C` | 59 | UnwindData |  |
| 142 | `?Block@Context@Concurrency@@SAXXZ` | `0x2458` | 23 | UnwindData |  |
| 178 | `?Yield@Context@Concurrency@@SAXXZ` | `0x2470` | 55 | UnwindData |  |
| 266 | `?_Yield@_Context@details@Concurrency@@SAXXZ` | `0x2470` | 55 | UnwindData |  |
| 249 | `?_SpinYield@Context@Concurrency@@SAXXZ` | `0x24A8` | 55 | UnwindData |  |
| 166 | `?IsCurrentTaskCollectionCanceling@Context@Concurrency@@SA_NXZ` | `0x24E0` | 96 | UnwindData |  |
| 148 | `?CurrentContext@Context@Concurrency@@SAPEAV12@XZ` | `0x2540` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `?Oversubscribe@Context@Concurrency@@SAX_N@Z` | `0x2548` | 62 | UnwindData |  |
| 220 | `?_Oversubscribe@_Context@details@Concurrency@@SAX_N@Z` | `0x2548` | 62 | UnwindData |  |
| 196 | `?_CurrentContext@_Context@details@Concurrency@@SA?AV123@XZ` | `0x2588` | 55 | UnwindData |  |
| 213 | `?_IsSynchronouslyBlocked@_Context@details@Concurrency@@QEBA_NXZ` | `0x25C0` | 5,772 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 221 | `?_Reference@_Scheduler@details@Concurrency@@QEAAIXZ` | `0x25C0` | 5,772 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `??0_Cancellation_beacon@details@Concurrency@@QEAA@XZ` | `0x3C4C` | 445 | UnwindData |  |
| 94 | `??1_Cancellation_beacon@details@Concurrency@@QEAA@XZ` | `0x3E0C` | 49 | UnwindData |  |
| 194 | `?_Confirm_cancel@_Cancellation_beacon@details@Concurrency@@QEAA_NXZ` | `0x3E40` | 81 | UnwindData |  |
| 206 | `?_GetCurrentInlineDepth@_StackGuard@details@Concurrency@@CAAEA_KXZ` | `0x3E94` | 47 | UnwindData |  |
| 248 | `?_SpinOnce@?$_SpinWait@$0A@@details@Concurrency@@QEAA_NXZ` | `0x429C` | 1,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | `?_DoYield@?$_SpinWait@$0A@@details@Concurrency@@IEAAXXZ` | `0x4884` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 234 | `?_Reset@?$_SpinWait@$0A@@details@Concurrency@@IEAAXXZ` | `0x4888` | 184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 243 | `?_SetSpinCount@?$_SpinWait@$0A@@details@Concurrency@@QEAAXI@Z` | `0x4940` | 108 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 164 | `?Id@CurrentScheduler@Concurrency@@SAIXZ` | `0x49AC` | 36 | UnwindData |  |
| 155 | `?GetNumberOfVirtualProcessors@CurrentScheduler@Concurrency@@SAIXZ` | `0x49D0` | 36 | UnwindData |  |
| 157 | `?GetPolicy@CurrentScheduler@Concurrency@@SA?AVSchedulerPolicy@2@XZ` | `0x49F4` | 41 | UnwindData |  |
| 153 | `?Get@CurrentScheduler@Concurrency@@SAPEAVScheduler@2@XZ` | `0x4A20` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `?Create@CurrentScheduler@Concurrency@@SAXAEBVSchedulerPolicy@2@@Z` | `0x4A28` | 37 | UnwindData |  |
| 149 | `?Detach@CurrentScheduler@Concurrency@@SAXXZ` | `0x4A50` | 184 | UnwindData |  |
| 169 | `?RegisterShutdownEvent@CurrentScheduler@Concurrency@@SAXPEAX@Z` | `0x4B2C` | 65 | UnwindData |  |
| 147 | `?CreateScheduleGroup@CurrentScheduler@Concurrency@@SAPEAVScheduleGroup@2@XZ` | `0x4B70` | 23 | UnwindData |  |
| 146 | `?CreateScheduleGroup@CurrentScheduler@Concurrency@@SAPEAVScheduleGroup@2@AEAVlocation@2@@Z` | `0x4B88` | 32 | UnwindData |  |
| 172 | `?ScheduleTask@CurrentScheduler@Concurrency@@SAXP6AXPEAX@Z0@Z` | `0x4BA8` | 47 | UnwindData |  |
| 241 | `?_ScheduleTask@_CurrentScheduler@details@Concurrency@@SAXP6AXPEAX@Z0@Z` | `0x4BA8` | 47 | UnwindData |  |
| 173 | `?ScheduleTask@CurrentScheduler@Concurrency@@SAXP6AXPEAX@Z0AEAVlocation@2@@Z` | `0x4BD8` | 63 | UnwindData |  |
| 165 | `?IsAvailableLocation@CurrentScheduler@Concurrency@@SA_NAEBVlocation@2@@Z` | `0x4C18` | 40 | UnwindData |  |
| 209 | `?_Id@_CurrentScheduler@details@Concurrency@@SAIXZ` | `0x4C40` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 207 | `?_GetNumberOfVirtualProcessors@_CurrentScheduler@details@Concurrency@@SAIXZ` | `0x4C48` | 23 | UnwindData |  |
| 203 | `?_Get@_CurrentScheduler@details@Concurrency@@SA?AV_Scheduler@23@XZ` | `0x4C60` | 26 | UnwindData |  |
| 621 | `_freea` | `0x4C7C` | 31 | UnwindData |  |
| 622 | `_freea_s` | `0x4C7C` | 31 | UnwindData |  |
| 162 | `?GetSharedTimerQueue@details@Concurrency@@YAPEAXXZ` | `0x4CE8` | 200 | UnwindData |  |
| 9 | `??0_Condition_variable@details@Concurrency@@QEAA@XZ` | `0x5070` | 44 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `??1_Condition_variable@details@Concurrency@@QEAA@XZ` | `0x509C` | 58 | UnwindData |  |
| 324 | `?wait@_Condition_variable@details@Concurrency@@QEAAXAEAVcritical_section@3@@Z` | `0x50D8` | 137 | UnwindData |  |
| 326 | `?wait_for@_Condition_variable@details@Concurrency@@QEAA_NAEAVcritical_section@3@I@Z` | `0x5164` | 418 | UnwindData |  |
| 304 | `?notify_one@_Condition_variable@details@Concurrency@@QEAAXXZ` | `0x5308` | 173 | UnwindData |  |
| 303 | `?notify_all@_Condition_variable@details@Concurrency@@QEAAXXZ` | `0x53B8` | 127 | UnwindData |  |
| 43 | `??0event@Concurrency@@QEAA@XZ` | `0x5438` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `??1event@Concurrency@@QEAA@XZ` | `0x5468` | 139 | UnwindData |  |
| 325 | `?wait@event@Concurrency@@QEAA_KI@Z` | `0x54F4` | 329 | UnwindData |  |
| 306 | `?reset@event@Concurrency@@QEAAXXZ` | `0x5640` | 135 | UnwindData |  |
| 307 | `?set@event@Concurrency@@QEAAXXZ` | `0x56C8` | 487 | UnwindData |  |
| 327 | `?wait_for_multiple@event@Concurrency@@SA_KPEAPEAV12@_K_NI@Z` | `0x58B0` | 1,061 | UnwindData |  |
| 82 | `??0scheduler_resource_allocation_error@Concurrency@@QEAA@PEBDJ@Z` | `0x63C8` | 58 | UnwindData |  |
| 81 | `??0scheduler_resource_allocation_error@Concurrency@@QEAA@J@Z` | `0x6404` | 47 | UnwindData |  |
| 297 | `?get_error_code@scheduler_resource_allocation_error@Concurrency@@QEBAJXZ` | `0x6434` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `??0scheduler_worker_creation_error@Concurrency@@QEAA@PEBDJ@Z` | `0x6438` | 33 | UnwindData |  |
| 83 | `??0scheduler_worker_creation_error@Concurrency@@QEAA@J@Z` | `0x645C` | 33 | UnwindData |  |
| 90 | `??0unsupported_os@Concurrency@@QEAA@PEBD@Z` | `0x6480` | 42 | UnwindData |  |
| 91 | `??0unsupported_os@Concurrency@@QEAA@XZ` | `0x64AC` | 33 | UnwindData |  |
| 79 | `??0scheduler_not_attached@Concurrency@@QEAA@PEBD@Z` | `0x64D0` | 42 | UnwindData |  |
| 80 | `??0scheduler_not_attached@Concurrency@@QEAA@XZ` | `0x64FC` | 33 | UnwindData |  |
| 50 | `??0improper_scheduler_attach@Concurrency@@QEAA@PEBD@Z` | `0x6520` | 42 | UnwindData |  |
| 51 | `??0improper_scheduler_attach@Concurrency@@QEAA@XZ` | `0x654C` | 33 | UnwindData |  |
| 52 | `??0improper_scheduler_detach@Concurrency@@QEAA@PEBD@Z` | `0x6570` | 42 | UnwindData |  |
| 53 | `??0improper_scheduler_detach@Concurrency@@QEAA@XZ` | `0x659C` | 33 | UnwindData |  |
| 54 | `??0improper_scheduler_reference@Concurrency@@QEAA@PEBD@Z` | `0x65C0` | 42 | UnwindData |  |
| 55 | `??0improper_scheduler_reference@Concurrency@@QEAA@XZ` | `0x65EC` | 33 | UnwindData |  |
| 41 | `??0default_scheduler_exists@Concurrency@@QEAA@PEBD@Z` | `0x6610` | 42 | UnwindData |  |
| 42 | `??0default_scheduler_exists@Concurrency@@QEAA@XZ` | `0x663C` | 33 | UnwindData |  |
| 38 | `??0context_unblock_unbalanced@Concurrency@@QEAA@PEBD@Z` | `0x6660` | 42 | UnwindData |  |
| 39 | `??0context_unblock_unbalanced@Concurrency@@QEAA@XZ` | `0x668C` | 33 | UnwindData |  |
| 36 | `??0context_self_unblock@Concurrency@@QEAA@PEBD@Z` | `0x66B0` | 42 | UnwindData |  |
| 37 | `??0context_self_unblock@Concurrency@@QEAA@XZ` | `0x66DC` | 33 | UnwindData |  |
| 72 | `??0missing_wait@Concurrency@@QEAA@PEBD@Z` | `0x6700` | 42 | UnwindData |  |
| 73 | `??0missing_wait@Concurrency@@QEAA@XZ` | `0x672C` | 33 | UnwindData |  |
| 32 | `??0bad_target@Concurrency@@QEAA@PEBD@Z` | `0x6750` | 42 | UnwindData |  |
| 33 | `??0bad_target@Concurrency@@QEAA@XZ` | `0x677C` | 33 | UnwindData |  |
| 70 | `??0message_not_found@Concurrency@@QEAA@PEBD@Z` | `0x67A0` | 42 | UnwindData |  |
| 71 | `??0message_not_found@Concurrency@@QEAA@XZ` | `0x67CC` | 33 | UnwindData |  |
| 56 | `??0invalid_link_target@Concurrency@@QEAA@PEBD@Z` | `0x67F0` | 42 | UnwindData |  |
| 57 | `??0invalid_link_target@Concurrency@@QEAA@XZ` | `0x681C` | 33 | UnwindData |  |
| 64 | `??0invalid_scheduler_policy_key@Concurrency@@QEAA@PEBD@Z` | `0x6840` | 42 | UnwindData |  |
| 65 | `??0invalid_scheduler_policy_key@Concurrency@@QEAA@XZ` | `0x686C` | 33 | UnwindData |  |
| 68 | `??0invalid_scheduler_policy_value@Concurrency@@QEAA@PEBD@Z` | `0x6890` | 42 | UnwindData |  |
| 69 | `??0invalid_scheduler_policy_value@Concurrency@@QEAA@XZ` | `0x68BC` | 33 | UnwindData |  |
| 66 | `??0invalid_scheduler_policy_thread_specification@Concurrency@@QEAA@PEBD@Z` | `0x68E0` | 42 | UnwindData |  |
| 67 | `??0invalid_scheduler_policy_thread_specification@Concurrency@@QEAA@XZ` | `0x690C` | 33 | UnwindData |  |
| 60 | `??0invalid_operation@Concurrency@@QEAA@PEBD@Z` | `0x6930` | 42 | UnwindData |  |
| 61 | `??0invalid_operation@Concurrency@@QEAA@XZ` | `0x695C` | 33 | UnwindData |  |
| 74 | `??0nested_scheduler_missing_detach@Concurrency@@QEAA@PEBD@Z` | `0x6980` | 42 | UnwindData |  |
| 75 | `??0nested_scheduler_missing_detach@Concurrency@@QEAA@XZ` | `0x69AC` | 33 | UnwindData |  |
| 76 | `??0operation_timed_out@Concurrency@@QEAA@PEBD@Z` | `0x69D0` | 42 | UnwindData |  |
| 77 | `??0operation_timed_out@Concurrency@@QEAA@XZ` | `0x69FC` | 33 | UnwindData |  |
| 58 | `??0invalid_multiple_scheduling@Concurrency@@QEAA@PEBD@Z` | `0x6A20` | 42 | UnwindData |  |
| 59 | `??0invalid_multiple_scheduling@Concurrency@@QEAA@XZ` | `0x6A4C` | 33 | UnwindData |  |
| 62 | `??0invalid_oversubscribe_operation@Concurrency@@QEAA@PEBD@Z` | `0x6A70` | 42 | UnwindData |  |
| 63 | `??0invalid_oversubscribe_operation@Concurrency@@QEAA@XZ` | `0x6A9C` | 33 | UnwindData |  |
| 48 | `??0improper_lock@Concurrency@@QEAA@PEBD@Z` | `0x6AC0` | 42 | UnwindData |  |
| 49 | `??0improper_lock@Concurrency@@QEAA@XZ` | `0x6AEC` | 33 | UnwindData |  |
| 88 | `??0task_canceled@Concurrency@@QEAA@PEBD@Z` | `0x6B10` | 42 | UnwindData |  |
| 89 | `??0task_canceled@Concurrency@@QEAA@XZ` | `0x6B3C` | 33 | UnwindData |  |
| 11 | `??0_Interruption_exception@details@Concurrency@@QEAA@PEBD@Z` | `0x6B60` | 42 | UnwindData |  |
| 12 | `??0_Interruption_exception@details@Concurrency@@QEAA@XZ` | `0x6B8C` | 33 | UnwindData |  |
| 150 | `?DisableTracing@Concurrency@@YAJXZ` | `0x72E8` | 10,700 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | `?EnableTracing@Concurrency@@YAJXZ` | `0x72E8` | 10,700 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 329 | `_CRT_RTC_INIT` | `0x72E8` | 10,700 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 330 | `_CRT_RTC_INITW` | `0x72E8` | 10,700 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 296 | `?from_numa_node@location@Concurrency@@SA?AV12@G@Z` | `0x9CB4` | 153 | UnwindData |  |
| 295 | `?current@location@Concurrency@@SA?AV12@XZ` | `0x9D9C` | 134 | UnwindData |  |
| 197 | `?_Current_node@location@Concurrency@@SA?AV12@XZ` | `0x9E24` | 131 | UnwindData |  |
| 265 | `?_Value@_SpinCount@details@Concurrency@@SAIXZ` | `0xA518` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `??0_NonReentrantBlockingLock@details@Concurrency@@QEAA@XZ` | `0xA520` | 30 | UnwindData |  |
| 16 | `??0_ReentrantBlockingLock@details@Concurrency@@QEAA@XZ` | `0xA520` | 30 | UnwindData |  |
| 96 | `??1_NonReentrantBlockingLock@details@Concurrency@@QEAA@XZ` | `0xA540` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `??1_ReentrantBlockingLock@details@Concurrency@@QEAA@XZ` | `0xA540` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 180 | `?_Acquire@_NonReentrantBlockingLock@details@Concurrency@@QEAAXXZ` | `0xA548` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 182 | `?_Acquire@_ReentrantBlockingLock@details@Concurrency@@QEAAXXZ` | `0xA548` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 255 | `?_TryAcquire@_NonReentrantBlockingLock@details@Concurrency@@QEAA_NXZ` | `0xA550` | 20 | UnwindData |  |
| 256 | `?_TryAcquire@_ReentrantBlockingLock@details@Concurrency@@QEAA_NXZ` | `0xA550` | 20 | UnwindData |  |
| 224 | `?_Release@_NonReentrantBlockingLock@details@Concurrency@@QEAAXXZ` | `0xA564` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 226 | `?_Release@_ReentrantBlockingLock@details@Concurrency@@QEAAXXZ` | `0xA564` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `??0_ReentrantLock@details@Concurrency@@QEAA@XZ` | `0xA56C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `?_Acquire@_ReentrantLock@details@Concurrency@@QEAAXXZ` | `0xA57C` | 85 | UnwindData |  |
| 257 | `?_TryAcquire@_ReentrantLock@details@Concurrency@@QEAA_NXZ` | `0xA5D4` | 45 | UnwindData |  |
| 227 | `?_Release@_ReentrantLock@details@Concurrency@@QEAAXXZ` | `0xA604` | 48 | UnwindData |  |
| 14 | `??0_NonReentrantPPLLock@details@Concurrency@@QEAA@XZ` | `0xA634` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `??0critical_section@Concurrency@@QEAA@XZ` | `0xA634` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `?_Acquire@_NonReentrantPPLLock@details@Concurrency@@QEAAXPEAX@Z` | `0xA65C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 225 | `?_Release@_NonReentrantPPLLock@details@Concurrency@@QEAAXXZ` | `0xA664` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `??0_ReentrantPPLLock@details@Concurrency@@QEAA@XZ` | `0xA66C` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | `?_Acquire@_ReentrantPPLLock@details@Concurrency@@QEAAXPEAX@Z` | `0xA69C` | 83 | UnwindData |  |
| 228 | `?_Release@_ReentrantPPLLock@details@Concurrency@@QEAAXXZ` | `0xA6F0` | 26 | UnwindData |  |
| 15 | `??0_ReaderWriterLock@details@Concurrency@@QEAA@XZ` | `0xA70C` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `?_AcquireRead@_ReaderWriterLock@details@Concurrency@@QEAAXXZ` | `0xA720` | 56 | UnwindData |  |
| 230 | `?_ReleaseRead@_ReaderWriterLock@details@Concurrency@@QEAAXXZ` | `0xA758` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `?_AcquireWrite@_ReaderWriterLock@details@Concurrency@@QEAAXXZ` | `0xA75C` | 55 | UnwindData |  |
| 231 | `?_ReleaseWrite@_ReaderWriterLock@details@Concurrency@@QEAAXXZ` | `0xA794` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 258 | `?_TryAcquireWrite@_ReaderWriterLock@details@Concurrency@@QEAA_NXZ` | `0xA7A0` | 828 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `??0_Scoped_lock@_NonReentrantPPLLock@details@Concurrency@@QEAA@AEAV123@@Z` | `0xAADC` | 102 | UnwindData |  |
| 98 | `??1_Scoped_lock@_NonReentrantPPLLock@details@Concurrency@@QEAA@XZ` | `0xAB44` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `??1scoped_lock@critical_section@Concurrency@@QEAA@XZ` | `0xAB44` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `??0_Scoped_lock@_ReentrantPPLLock@details@Concurrency@@QEAA@AEAV123@@Z` | `0xAB4C` | 99 | UnwindData |  |
| 99 | `??1_Scoped_lock@_ReentrantPPLLock@details@Concurrency@@QEAA@XZ` | `0xABB0` | 29 | UnwindData |  |
| 302 | `?native_handle@critical_section@Concurrency@@QEAAAEAV12@XZ` | `0xABD0` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 298 | `?lock@critical_section@Concurrency@@QEAAXXZ` | `0xABD4` | 82 | UnwindData |  |
| 316 | `?try_lock@critical_section@Concurrency@@QEAA_NXZ` | `0xAC28` | 194 | UnwindData |  |
| 318 | `?try_lock_for@critical_section@Concurrency@@QEAA_NI@Z` | `0xACEC` | 172 | UnwindData |  |
| 321 | `?unlock@critical_section@Concurrency@@QEAAXXZ` | `0xAD98` | 276 | UnwindData |  |
| 85 | `??0scoped_lock@critical_section@Concurrency@@QEAA@AEAV12@@Z` | `0xB150` | 102 | UnwindData |  |
| 78 | `??0reader_writer_lock@Concurrency@@QEAA@XZ` | `0xB1B8` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 299 | `?lock@reader_writer_lock@Concurrency@@QEAAXXZ` | `0xB1E8` | 82 | UnwindData |  |
| 317 | `?try_lock@reader_writer_lock@Concurrency@@QEAA_NXZ` | `0xB23C` | 220 | UnwindData |  |
| 300 | `?lock_read@reader_writer_lock@Concurrency@@QEAAXXZ` | `0xB318` | 329 | UnwindData |  |
| 319 | `?try_lock_read@reader_writer_lock@Concurrency@@QEAA_NXZ` | `0xB464` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 322 | `?unlock@reader_writer_lock@Concurrency@@QEAAXXZ` | `0xB480` | 81 | UnwindData |  |
| 86 | `??0scoped_lock@reader_writer_lock@Concurrency@@QEAA@AEAV12@@Z` | `0xB864` | 102 | UnwindData |  |
| 111 | `??1scoped_lock@reader_writer_lock@Concurrency@@QEAA@XZ` | `0xB8CC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `??1scoped_lock_read@reader_writer_lock@Concurrency@@QEAA@XZ` | `0xB8CC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `??0scoped_lock_read@reader_writer_lock@Concurrency@@QEAA@AEAV12@@Z` | `0xB8D4` | 29 | UnwindData |  |
| 156 | `?GetOSVersion@Concurrency@@YA?AW4OSVersion@IResourceManager@1@XZ` | `0xBACC` | 128 | UnwindData |  |
| 145 | `?CreateResourceManager@Concurrency@@YAPEAUIResourceManager@1@XZ` | `0xBB4C` | 265 | UnwindData |  |
| 159 | `?GetProcessorCount@Concurrency@@YAIXZ` | `0xBC58` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 205 | `?_GetConcurrency@details@Concurrency@@YAIXZ` | `0xBC58` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 160 | `?GetProcessorNodeCount@Concurrency@@YAIXZ` | `0xBC60` | 130 | UnwindData |  |
| 161 | `?GetSchedulerId@Concurrency@@YAIXZ` | `0xBCE4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `?GetExecutionContextId@Concurrency@@YAIXZ` | `0xBCF4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 310 | `?set_task_execution_resources@Concurrency@@YAX_K@Z` | `0xBD04` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 309 | `?set_task_execution_resources@Concurrency@@YAXGPEAU_GROUP_AFFINITY@@@Z` | `0xBD0C` | 27,388 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `?Create@Scheduler@Concurrency@@SAPEAV12@AEBVSchedulerPolicy@2@@Z` | `0x12808` | 40 | UnwindData |  |
| 175 | `?SetDefaultSchedulerPolicy@Scheduler@Concurrency@@SAXAEBVSchedulerPolicy@2@@Z` | `0x12830` | 248 | UnwindData |  |
| 170 | `?ResetDefaultSchedulerPolicy@Scheduler@Concurrency@@SAXXZ` | `0x12928` | 114 | UnwindData |  |
| 229 | `?_Release@_Scheduler@details@Concurrency@@QEAAIXZ` | `0x16860` | 584 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `??0SchedulerPolicy@Concurrency@@QEAA@XZ` | `0x16AA8` | 28 | UnwindData |  |
| 6 | `??0SchedulerPolicy@Concurrency@@QEAA@_KZZ` | `0x16AC4` | 49 | UnwindData |  |
| 4 | `??0SchedulerPolicy@Concurrency@@QEAA@AEBV01@@Z` | `0x16D10` | 121 | UnwindData |  |
| 120 | `??4SchedulerPolicy@Concurrency@@QEAAAEAV01@AEBV01@@Z` | `0x16D8C` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `??1SchedulerPolicy@Concurrency@@QEAA@XZ` | `0x16DDC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 158 | `?GetPolicyValue@SchedulerPolicy@Concurrency@@QEBAIW4PolicyElementKey@2@@Z` | `0x16DE4` | 75 | UnwindData |  |
| 176 | `?SetPolicyValue@SchedulerPolicy@Concurrency@@QEAAIW4PolicyElementKey@2@I@Z` | `0x16E30` | 202 | UnwindData |  |
| 174 | `?SetConcurrencyLimits@SchedulerPolicy@Concurrency@@QEAAXII@Z` | `0x16EFC` | 178 | UnwindData |  |
| 141 | `?Alloc@Concurrency@@YAPEAX_K@Z` | `0x1B55C` | 142 | UnwindData |  |
| 152 | `?Free@Concurrency@@YAXPEAX@Z` | `0x1B5EC` | 68 | UnwindData |  |
| 23 | `??0_StructuredTaskCollection@details@Concurrency@@QEAA@PEAV_CancellationTokenState@12@@Z` | `0x1B98C` | 214 | UnwindData |  |
| 238 | `?_Schedule@_StructuredTaskCollection@details@Concurrency@@QEAAXPEAV_UnrealizedChore@23@PEAVlocation@3@@Z` | `0x1BA6C` | 152 | UnwindData |  |
| 237 | `?_Schedule@_StructuredTaskCollection@details@Concurrency@@QEAAXPEAV_UnrealizedChore@23@@Z` | `0x1BB28` | 136 | UnwindData |  |
| 235 | `?_RunAndWait@_StructuredTaskCollection@details@Concurrency@@QEAA?AW4_TaskCollectionStatus@23@PEAV_UnrealizedChore@23@@Z` | `0x1BBB0` | 732 | UnwindData |  |
| 191 | `?_CleanupToken@_StructuredTaskCollection@details@Concurrency@@AEAAXXZ` | `0x1BE8C` | 82 | UnwindData |  |
| 179 | `?_Abort@_StructuredTaskCollection@details@Concurrency@@AEAAXXZ` | `0x1BEE0` | 239 | UnwindData |  |
| 188 | `?_Cancel@_StructuredTaskCollection@details@Concurrency@@QEAAXXZ` | `0x1BFD0` | 224 | UnwindData |  |
| 211 | `?_IsCanceling@_StructuredTaskCollection@details@Concurrency@@QEAA_NXZ` | `0x1C0B0` | 204 | UnwindData |  |
| 25 | `??0_TaskCollection@details@Concurrency@@QEAA@XZ` | `0x1C2A0` | 361 | UnwindData |  |
| 24 | `??0_TaskCollection@details@Concurrency@@QEAA@PEAV_CancellationTokenState@12@@Z` | `0x1C40C` | 374 | UnwindData |  |
| 101 | `??1_TaskCollection@details@Concurrency@@QEAA@XZ` | `0x1C62C` | 255 | UnwindData |  |
| 240 | `?_Schedule@_TaskCollection@details@Concurrency@@QEAAXPEAV_UnrealizedChore@23@PEAVlocation@3@@Z` | `0x1CCCC` | 295 | UnwindData |  |
| 239 | `?_Schedule@_TaskCollection@details@Concurrency@@QEAAXPEAV_UnrealizedChore@23@@Z` | `0x1CDF4` | 275 | UnwindData |  |
| 189 | `?_Cancel@_TaskCollection@details@Concurrency@@QEAAXXZ` | `0x1D03C` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 236 | `?_RunAndWait@_TaskCollection@details@Concurrency@@QEAA?AW4_TaskCollectionStatus@23@PEAV_UnrealizedChore@23@@Z` | `0x1D050` | 1,137 | UnwindData |  |
| 212 | `?_IsCanceling@_TaskCollection@details@Concurrency@@QEAA_NXZ` | `0x1D930` | 235 | UnwindData |  |
| 216 | `?_NewCollection@_AsyncTaskCollection@details@Concurrency@@SAPEAV123@PEAV_CancellationTokenState@23@@Z` | `0x1DAC8` | 134 | UnwindData |  |
| 232 | `?_ReportUnobservedException@details@Concurrency@@YAXXZ` | `0x1DBB4` | 84 | UnwindData |  |
| 244 | `?_SetUnobservedExceptionHandler@details@Concurrency@@YAXP6AXXZ@Z` | `0x1DC08` | 3,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `??0_Timer@details@Concurrency@@IEAA@I_N@Z` | `0x1E8E8` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 250 | `?_Start@_Timer@details@Concurrency@@IEAAXXZ` | `0x1E904` | 170 | UnwindData |  |
| 102 | `??1_Timer@details@Concurrency@@MEAA@XZ` | `0x1E9B0` | 31 | UnwindData |  |
| 251 | `?_Stop@_Timer@details@Concurrency@@IEAAXXZ` | `0x1E9D0` | 61 | UnwindData |  |
| 323 | `?wait@Concurrency@@YAXI@Z` | `0x1EA10` | 186 | UnwindData |  |
| 204 | `?_GetConcRTTraceInfo@Concurrency@@YAPEBU_CONCRT_TRACE_INFO@details@1@XZ` | `0x1EE60` | 31 | UnwindData |  |
| 254 | `?_Trace_ppl_function@Concurrency@@YAXAEBU_GUID@@EW4ConcRT_EventType@1@@Z` | `0x1EE80` | 194 | UnwindData |  |
| 253 | `?_Trace_agents@Concurrency@@YAXW4Agents_EventType@1@_JZZ` | `0x1EF44` | 300 | UnwindData |  |
| 261 | `?_UnderlyingYield@details@Concurrency@@YAXXZ` | `0x1F770` | 62 | UnwindData |  |
| 192 | `?_ConcRT_CoreAssert@details@Concurrency@@YAXPEBD0H@Z` | `0x1F808` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 193 | `?_ConcRT_Trace@details@Concurrency@@YAXHPEB_WZZ` | `0x1F810` | 207 | UnwindData |  |
| 22 | `??0_SpinLock@details@Concurrency@@QEAA@AECJ@Z` | `0x1F8E0` | 81 | UnwindData |  |
| 100 | `??1_SpinLock@details@Concurrency@@QEAA@XZ` | `0x1F934` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 167 | `?Log2@details@Concurrency@@YAK_K@Z` | `0x1F93C` | 6,128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 341 | `_Lock_shared_ptr_spin_lock` | `0x2112C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 345 | `_Unlock_shared_ptr_spin_lock` | `0x2113C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 283 | `?_query_new_handler@@YAP6AH_K@ZXZ` | `0x21148` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 285 | `?_set_new_handler@@YAP6AH_K@ZH@Z` | `0x21158` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 286 | `?_set_new_handler@@YAP6AH_K@ZP6AH0@Z@Z` | `0x21160` | 79 | UnwindData |  |
| 502 | `_callnewh` | `0x211B0` | 51 | UnwindData |  |
| 308 | `?set_new_handler@@YAP6AXXZP6AXXZ@Z` | `0x211EC` | 18 | UnwindData |  |
| 284 | `?_query_new_mode@@YAHXZ` | `0x21200` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 287 | `?_set_new_mode@@YAHH@Z` | `0x21208` | 47 | UnwindData |  |
| 446 | `__set_app_type` | `0x21238` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1041 | `_set_error_mode` | `0x21240` | 64 | UnwindData |  |
| 121 | `??4__non_rtti_object@std@@QEAAAEAV01@AEBV01@@Z` | `0x21744` | 23 | UnwindData |  |
| 122 | `??4bad_cast@std@@QEAAAEAV01@AEBV01@@Z` | `0x21744` | 23 | UnwindData |  |
| 123 | `??4bad_typeid@std@@QEAAAEAV01@AEBV01@@Z` | `0x21744` | 23 | UnwindData |  |
| 135 | `??_Fbad_cast@std@@QEAAXXZ` | `0x2175C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `??_Fbad_typeid@std@@QEAAXXZ` | `0x21768` | 2,276 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 267 | `?__ExceptionPtrAssign@@YAXPEAXPEBX@Z` | `0x2204C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 268 | `?__ExceptionPtrCompare@@YA_NPEBX0@Z` | `0x22054` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 269 | `?__ExceptionPtrCopy@@YAXPEAXPEBX@Z` | `0x22060` | 35 | UnwindData |  |
| 270 | `?__ExceptionPtrCopyException@@YAXPEAXPEBX1@Z` | `0x22084` | 78 | UnwindData |  |
| 271 | `?__ExceptionPtrCreate@@YAXPEAX@Z` | `0x220D4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 272 | `?__ExceptionPtrCurrentException@@YAXPEAX@Z` | `0x220E4` | 107 | UnwindData |  |
| 273 | `?__ExceptionPtrDestroy@@YAXPEAX@Z` | `0x22150` | 50 | UnwindData |  |
| 274 | `?__ExceptionPtrRethrow@@YAXPEBX@Z` | `0x22184` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 275 | `?__ExceptionPtrSwap@@YAXPEAX0@Z` | `0x2218C` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 276 | `?__ExceptionPtrToBool@@YA_NPEBX@Z` | `0x221AC` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 448 | `__setusermatherr` | `0x221B8` | 29 | UnwindData |  |
| 481 | `_amsg_exit` | `0x22A50` | 38 | UnwindData |  |
| 500 | `_c_exit` | `0x22A78` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 504 | `_cexit` | `0x22A88` | 88 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 578 | `_exit` | `0x22AE0` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 663 | `_get_pgmptr` | `0x22AEC` | 54 | UnwindData |  |
| 670 | `_get_wpgmptr` | `0x22B24` | 54 | UnwindData |  |
| 711 | `_initterm` | `0x22BA4` | 51 | UnwindData |  |
| 712 | `_initterm_e` | `0x22BD8` | 57 | UnwindData |  |
| 1417 | `exit` | `0x22E0C` | 1,176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 407 | `__getmainargs` | `0x232A4` | 110 | UnwindData |  |
| 418 | `__p___argc` | `0x23314` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 419 | `__p___argv` | `0x2331C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 420 | `__p___initenv` | `0x23324` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 421 | `__p___mb_cur_max` | `0x2332C` | 59 | UnwindData |  |
| 422 | `__p___wargv` | `0x23368` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 423 | `__p___winitenv` | `0x23370` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 424 | `__p__acmdln` | `0x23378` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 425 | `__p__commode` | `0x23380` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 426 | `__p__daylight` | `0x23388` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 427 | `__p__dstbias` | `0x23390` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 428 | `__p__environ` | `0x23398` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 429 | `__p__fmode` | `0x233A0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 431 | `__p__mbcasemap` | `0x233A8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 432 | `__p__mbctype` | `0x233B0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 433 | `__p__pctype` | `0x233B8` | 59 | UnwindData |  |
| 434 | `__p__pgmptr` | `0x233F4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 435 | `__p__pwctype` | `0x233FC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 436 | `__p__timezone` | `0x23404` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 437 | `__p__tzname` | `0x2340C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 438 | `__p__wcmdln` | `0x23414` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 439 | `__p__wenviron` | `0x2341C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 440 | `__p__wpgmptr` | `0x23424` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 467 | `__wgetmainargs` | `0x2342C` | 157 | UnwindData |  |
| 823 | `_lock` | `0x234CC` | 68 | UnwindData |  |
| 1180 | `_unlock` | `0x236B4` | 996 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 495 | `_beginthread` | `0x23A98` | 242 | UnwindData |  |
| 565 | `_endthread` | `0x23BB8` | 52 | UnwindData |  |
| 496 | `_beginthreadex` | `0x23C60` | 237 | UnwindData |  |
| 566 | `_endthreadex` | `0x23D7C` | 144 | UnwindData |  |
| 405 | `__get_flsindex` | `0x23F10` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 406 | `__get_tlsindex` | `0x23F10` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 453 | `__threadhandle` | `0x23F18` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 454 | `__threadid` | `0x23F20` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 623 | `_freefls` | `0x23F28` | 307 | UnwindData |  |
| 685 | `_getptd` | `0x24098` | 36 | UnwindData |  |
| 710 | `_initptd` | `0x24140` | 186 | UnwindData |  |
| 488 | `_atoi64` | `0x2514C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 489 | `_atoi64_l` | `0x25158` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 490 | `_atoi_l` | `0x25168` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 491 | `_atol_l` | `0x25168` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1401 | `atoi` | `0x25178` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1402 | `atol` | `0x25178` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1137 | `_swab` | `0x25184` | 88 | UnwindData |  |
| 1375 | `_wtoi` | `0x25374` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1379 | `_wtol` | `0x25374` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1376 | `_wtoi64` | `0x25380` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1377 | `_wtoi64_l` | `0x2538C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1378 | `_wtoi_l` | `0x2539C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1380 | `_wtol_l` | `0x2539C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 706 | `_i64toa` | `0x253AC` | 43 | UnwindData |  |
| 807 | `_itoa` | `0x253D8` | 42 | UnwindData |  |
| 834 | `_ltoa` | `0x25404` | 40 | UnwindData |  |
| 1162 | `_ui64toa` | `0x2542C` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1166 | `_ultoa` | `0x2547C` | 26 | UnwindData |  |
| 707 | `_i64toa_s` | `0x25548` | 35 | UnwindData |  |
| 808 | `_itoa_s` | `0x2556C` | 39 | UnwindData |  |
| 835 | `_ltoa_s` | `0x25594` | 34 | UnwindData |  |
| 1163 | `_ui64toa_s` | `0x255B8` | 19 | UnwindData |  |
| 1167 | `_ultoa_s` | `0x255CC` | 19 | UnwindData |  |
| 708 | `_i64tow` | `0x257D0` | 43 | UnwindData |  |
| 809 | `_itow` | `0x257FC` | 42 | UnwindData |  |
| 836 | `_ltow` | `0x25828` | 40 | UnwindData |  |
| 1164 | `_ui64tow` | `0x25850` | 26 | UnwindData |  |
| 1168 | `_ultow` | `0x2586C` | 26 | UnwindData |  |
| 709 | `_i64tow_s` | `0x2596C` | 35 | UnwindData |  |
| 810 | `_itow_s` | `0x25990` | 39 | UnwindData |  |
| 837 | `_ltow_s` | `0x259B8` | 34 | UnwindData |  |
| 1165 | `_ui64tow_s` | `0x259DC` | 19 | UnwindData |  |
| 1169 | `_ultow_s` | `0x259F0` | 19 | UnwindData |  |
| 681 | `_getdrives` | `0x25C28` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 678 | `_getdiskfree` | `0x25C30` | 163 | UnwindData |  |
| 593 | `_findclose` | `0x25D64` | 37 | UnwindData |  |
| 594 | `_findfirst32` | `0x25D8C` | 325 | UnwindData |  |
| 598 | `_findnext32` | `0x25ED4` | 287 | UnwindData |  |
| 596 | `_findfirst64` | `0x25FF4` | 340 | UnwindData |  |
| 600 | `_findnext64` | `0x26148` | 302 | UnwindData |  |
| 597 | `_findfirst64i32` | `0x26308` | 328 | UnwindData |  |
| 601 | `_findnext64i32` | `0x26450` | 290 | UnwindData |  |
| 595 | `_findfirst32i64` | `0x26574` | 337 | UnwindData |  |
| 599 | `_findnext32i64` | `0x266C8` | 299 | UnwindData |  |
| 1048 | `_seterrormode` | `0x267F4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 494 | `_beep` | `0x267FC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1055 | `_sleep` | `0x26804` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1307 | `_wfindfirst32` | `0x26818` | 325 | UnwindData |  |
| 1311 | `_wfindnext32` | `0x26960` | 287 | UnwindData |  |
| 1309 | `_wfindfirst64` | `0x26A80` | 340 | UnwindData |  |
| 1313 | `_wfindnext64` | `0x26BD4` | 302 | UnwindData |  |
| 1310 | `_wfindfirst64i32` | `0x26D04` | 328 | UnwindData |  |
| 1314 | `_wfindnext64i32` | `0x26E4C` | 290 | UnwindData |  |
| 1308 | `_wfindfirst32i64` | `0x26F70` | 337 | UnwindData |  |
| 1312 | `_wfindnext32i64` | `0x270C4` | 299 | UnwindData |  |
| 470 | `_access` | `0x271F0` | 18 | UnwindData |  |
| 471 | `_access_s` | `0x27204` | 87 | UnwindData |  |
| 513 | `_chmod` | `0x2725C` | 83 | UnwindData |  |
| 509 | `_chdir` | `0x272B0` | 301 | UnwindData |  |
| 400 | `__doserrno` | `0x273E0` | 32 | UnwindData |  |
| 558 | `_dosmaperr` | `0x27400` | 78 | UnwindData |  |
| 569 | `_errno` | `0x27450` | 32 | UnwindData |  |
| 655 | `_get_doserrno` | `0x27470` | 59 | UnwindData |  |
| 657 | `_get_errno` | `0x274AC` | 59 | UnwindData |  |
| 1039 | `_set_doserrno` | `0x27538` | 58 | UnwindData |  |
| 1040 | `_set_errno` | `0x27574` | 58 | UnwindData |  |
| 510 | `_chdrive` | `0x275B0` | 132 | UnwindData |  |
| 680 | `_getdrive` | `0x27634` | 235 | UnwindData |  |
| 641 | `_fullpath` | `0x27720` | 299 | UnwindData |  |
| 676 | `_getcwd` | `0x2784C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 677 | `_getdcwd` | `0x2785C` | 302 | UnwindData |  |
| 684 | `_getpid` | `0x27A0C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 980 | `_mkdir` | `0x27A14` | 70 | UnwindData |  |
| 1538 | `rename` | `0x27A5C` | 327 | UnwindData |  |
| 1017 | `_rmdir` | `0x27BA4` | 70 | UnwindData |  |
| 1092 | `_stat32` | `0x27BEC` | 85 | UnwindData |  |
| 1094 | `_stat64` | `0x27C44` | 85 | UnwindData |  |
| 1095 | `_stat64i32` | `0x27C9C` | 85 | UnwindData |  |
| 1093 | `_stat32i64` | `0x27CF4` | 85 | UnwindData |  |
| 1178 | `_unlink` | `0x27D4C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1537 | `remove` | `0x27D54` | 70 | UnwindData |  |
| 1241 | `_waccess` | `0x27D9C` | 18 | UnwindData |  |
| 1242 | `_waccess_s` | `0x27DB0` | 168 | UnwindData |  |
| 1246 | `_wchdir` | `0x27E58` | 331 | UnwindData |  |
| 1247 | `_wchmod` | `0x27FA4` | 155 | UnwindData |  |
| 1320 | `_wfullpath` | `0x28040` | 308 | UnwindData |  |
| 1321 | `_wgetcwd` | `0x28174` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1322 | `_wgetdcwd` | `0x28184` | 333 | UnwindData |  |
| 1327 | `_wmkdir` | `0x282D4` | 49 | UnwindData |  |
| 1341 | `_wrename` | `0x28308` | 53 | UnwindData |  |
| 1343 | `_wrmdir` | `0x28340` | 47 | UnwindData |  |
| 1361 | `_wstat32` | `0x28464` | 1,147 | UnwindData |  |
| 1363 | `_wstat64` | `0x288E0` | 1,157 | UnwindData |  |
| 1364 | `_wstat64i32` | `0x28E24` | 1,159 | UnwindData |  |
| 1362 | `_wstat32i64` | `0x292AC` | 1,145 | UnwindData |  |
| 1340 | `_wremove` | `0x29728` | 47 | UnwindData |  |
| 1381 | `_wunlink` | `0x29758` | 2,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 570 | `_execl` | `0x29F50` | 165 | UnwindData |  |
| 571 | `_execle` | `0x29FF8` | 180 | UnwindData |  |
| 572 | `_execlp` | `0x2A0AC` | 164 | UnwindData |  |
| 573 | `_execlpe` | `0x2A150` | 180 | UnwindData |  |
| 574 | `_execv` | `0x2A204` | 69 | UnwindData |  |
| 575 | `_execve` | `0x2A24C` | 633 | UnwindData |  |
| 576 | `_execvp` | `0x2A550` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 577 | `_execvpe` | `0x2A558` | 781 | UnwindData |  |
| 679 | `_getdllprocaddr` | `0x2A868` | 36 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 817 | `_loaddll` | `0x2A88C` | 46 | UnwindData |  |
| 1179 | `_unloaddll` | `0x2A8BC` | 32 | UnwindData |  |
| 1076 | `_spawnl` | `0x2A8DC` | 173 | UnwindData |  |
| 1077 | `_spawnle` | `0x2A98C` | 188 | UnwindData |  |
| 1078 | `_spawnlp` | `0x2AA48` | 170 | UnwindData |  |
| 1079 | `_spawnlpe` | `0x2AAF4` | 188 | UnwindData |  |
| 1080 | `_spawnv` | `0x2ABB0` | 69 | UnwindData |  |
| 1081 | `_spawnve` | `0x2ABF8` | 645 | UnwindData |  |
| 1082 | `_spawnvp` | `0x2AF10` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1083 | `_spawnvpe` | `0x2AF18` | 749 | UnwindData |  |
| 1589 | `system` | `0x2B208` | 264 | UnwindData |  |
| 544 | `_cwait` | `0x2B310` | 182 | UnwindData |  |
| 1298 | `_wexecl` | `0x2BB7C` | 168 | UnwindData |  |
| 1299 | `_wexecle` | `0x2BC24` | 183 | UnwindData |  |
| 1300 | `_wexeclp` | `0x2BCDC` | 167 | UnwindData |  |
| 1301 | `_wexeclpe` | `0x2BD84` | 183 | UnwindData |  |
| 1302 | `_wexecv` | `0x2BE3C` | 71 | UnwindData |  |
| 1303 | `_wexecve` | `0x2BE84` | 637 | UnwindData |  |
| 1304 | `_wexecvp` | `0x2C18C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1305 | `_wexecvpe` | `0x2C194` | 628 | UnwindData |  |
| 1351 | `_wspawnl` | `0x2C408` | 176 | UnwindData |  |
| 1352 | `_wspawnle` | `0x2C4B8` | 191 | UnwindData |  |
| 1353 | `_wspawnlp` | `0x2C578` | 173 | UnwindData |  |
| 1354 | `_wspawnlpe` | `0x2C628` | 191 | UnwindData |  |
| 1355 | `_wspawnv` | `0x2C6E8` | 71 | UnwindData |  |
| 1356 | `_wspawnve` | `0x2C730` | 652 | UnwindData |  |
| 1357 | `_wspawnvp` | `0x2CA4C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1358 | `_wspawnvpe` | `0x2CA54` | 677 | UnwindData |  |
| 1369 | `_wsystem` | `0x2CCFC` | 264 | UnwindData |  |
| 854 | `_mbclen` | `0x2CE04` | 45 | UnwindData |  |
| 855 | `_mbclen_l` | `0x2CE34` | 45 | UnwindData |  |
| 888 | `_mbsinc` | `0x2CE64` | 66 | UnwindData |  |
| 889 | `_mbsinc_l` | `0x2CEA8` | 39 | UnwindData |  |
| 938 | `_mbsninc` | `0x2CED0` | 35 | UnwindData |  |
| 939 | `_mbsninc_l` | `0x2CEF4` | 34 | UnwindData |  |
| 856 | `_mbctohira` | `0x2CF18` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 857 | `_mbctohira_l` | `0x2CF20` | 55 | UnwindData |  |
| 858 | `_mbctokata` | `0x2CF58` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 859 | `_mbctokata_l` | `0x2CF60` | 41 | UnwindData |  |
| 1422 | `feof` | `0x2CF8C` | 40 | UnwindData |  |
| 1423 | `ferror` | `0x2CFB4` | 40 | UnwindData |  |
| 671 | `_getc_nolock` | `0x2CFDC` | 37 | UnwindData |  |
| 1425 | `fgetc` | `0x2D004` | 266 | UnwindData |  |
| 1458 | `getc` | `0x2D004` | 266 | UnwindData |  |
| 586 | `_fgetchar` | `0x2D110` | 21 | UnwindData |  |
| 1459 | `getchar` | `0x2D110` | 21 | UnwindData |  |
| 1427 | `fgets` | `0x2D128` | 360 | UnwindData |  |
| 587 | `_fgetwc_nolock` | `0x2D290` | 521 | UnwindData |  |
| 1428 | `fgetwc` | `0x2D49C` | 92 | UnwindData |  |
| 1464 | `getwc` | `0x2D4F8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1429 | `fgetws` | `0x2D500` | 209 | UnwindData |  |
| 588 | `_fgetwchar` | `0x2D5D4` | 21 | UnwindData |  |
| 1465 | `getwchar` | `0x2D5D4` | 21 | UnwindData |  |
| 592 | `_fileno` | `0x2D5EC` | 38 | UnwindData |  |
| 1438 | `fputc` | `0x2D614` | 281 | UnwindData |  |
| 1526 | `putc` | `0x2D614` | 281 | UnwindData |  |
| 1439 | `fputs` | `0x2D730` | 308 | UnwindData |  |
| 615 | `_fputchar` | `0x2D864` | 29 | UnwindData |  |
| 1527 | `putchar` | `0x2D864` | 29 | UnwindData |  |
| 616 | `_fputwc_nolock` | `0x2D884` | 471 | UnwindData |  |
| 1440 | `fputwc` | `0x2DA5C` | 118 | UnwindData |  |
| 1529 | `putwc` | `0x2DAD4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1441 | `fputws` | `0x2DADC` | 180 | UnwindData |  |
| 617 | `_fputwchar` | `0x2DB90` | 31 | UnwindData |  |
| 1530 | `putwchar` | `0x2DB90` | 31 | UnwindData |  |
| 589 | `_filbuf` | `0x2DBB0` | 339 | UnwindData |  |
| 409 | `__iob_func` | `0x2DF0C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 430 | `__p__iob` | `0x2DF0C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 824 | `_lock_file` | `0x2DF14` | 101 | UnwindData |  |
| 1181 | `_unlock_file` | `0x2DFB0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 604 | `_flsbuf` | `0x2E020` | 406 | UnwindData |  |
| 1409 | `clearerr` | `0x2E798` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1410 | `clearerr_s` | `0x2E7A0` | 194 | UnwindData |  |
| 581 | `_fcloseall` | `0x2E864` | 168 | UnwindData |  |
| 580 | `_fclose_nolock` | `0x2E90C` | 122 | UnwindData |  |
| 1421 | `fclose` | `0x2E988` | 102 | UnwindData |  |
| 584 | `_fdopen` | `0x2E9F0` | 420 | UnwindData |  |
| 585 | `_fflush_nolock` | `0x2EB94` | 76 | UnwindData |  |
| 605 | `_flushall` | `0x2EC5C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1424 | `fflush` | `0x2EC68` | 67 | UnwindData |  |
| 1426 | `fgetpos` | `0x2ED94` | 75 | UnwindData |  |
| 629 | `_fsopen` | `0x2EDE0` | 213 | UnwindData |  |
| 1434 | `fopen` | `0x2EEB8` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1435 | `fopen_s` | `0x2EEC4` | 83 | UnwindData |  |
| 611 | `_fprintf_l` | `0x2EF18` | 29 | UnwindData |  |
| 612 | `_fprintf_p` | `0x2EF38` | 36 | UnwindData |  |
| 613 | `_fprintf_p_l` | `0x2EF5C` | 29 | UnwindData |  |
| 614 | `_fprintf_s_l` | `0x2EF7C` | 29 | UnwindData |  |
| 1436 | `fprintf` | `0x2EF9C` | 308 | UnwindData |  |
| 1437 | `fprintf_s` | `0x2F0D0` | 36 | UnwindData |  |
| 618 | `_fread_nolock` | `0x2F0F4` | 29 | UnwindData |  |
| 619 | `_fread_nolock_s` | `0x2F114` | 543 | UnwindData |  |
| 1442 | `fread` | `0x2F334` | 29 | UnwindData |  |
| 1443 | `fread_s` | `0x2F354` | 167 | UnwindData |  |
| 1445 | `freopen` | `0x2F4EC` | 47 | UnwindData |  |
| 1446 | `freopen_s` | `0x2F51C` | 22 | UnwindData |  |
| 624 | `_fscanf_l` | `0x2F534` | 49 | UnwindData |  |
| 625 | `_fscanf_s_l` | `0x2F568` | 49 | UnwindData |  |
| 1448 | `fscanf` | `0x2F59C` | 53 | UnwindData |  |
| 1449 | `fscanf_s` | `0x2F5D4` | 53 | UnwindData |  |
| 626 | `_fseek_nolock` | `0x2F734` | 169 | UnwindData |  |
| 1450 | `fseek` | `0x2F7E0` | 114 | UnwindData |  |
| 627 | `_fseeki64` | `0x2F854` | 116 | UnwindData |  |
| 628 | `_fseeki64_nolock` | `0x2F8C8` | 179 | UnwindData |  |
| 1451 | `fsetpos` | `0x2F97C` | 53 | UnwindData |  |
| 634 | `_ftell_nolock` | `0x2F9B4` | 753 | UnwindData |  |
| 1452 | `ftell` | `0x2FCA8` | 88 | UnwindData |  |
| 635 | `_ftelli64` | `0x2FD00` | 103 | UnwindData |  |
| 636 | `_ftelli64_nolock` | `0x2FD68` | 753 | UnwindData |  |
| 644 | `_fwprintf_l` | `0x3005C` | 29 | UnwindData |  |
| 645 | `_fwprintf_p` | `0x3007C` | 36 | UnwindData |  |
| 646 | `_fwprintf_p_l` | `0x300A0` | 29 | UnwindData |  |
| 647 | `_fwprintf_s_l` | `0x300C0` | 29 | UnwindData |  |
| 1453 | `fwprintf` | `0x300E0` | 145 | UnwindData |  |
| 1454 | `fwprintf_s` | `0x30174` | 36 | UnwindData |  |
| 648 | `_fwrite_nolock` | `0x30198` | 398 | UnwindData |  |
| 1455 | `fwrite` | `0x30328` | 143 | UnwindData |  |
| 649 | `_fwscanf_l` | `0x303B8` | 49 | UnwindData |  |
| 650 | `_fwscanf_s_l` | `0x303EC` | 49 | UnwindData |  |
| 1456 | `fwscanf` | `0x30420` | 53 | UnwindData |  |
| 1457 | `fwscanf_s` | `0x30458` | 53 | UnwindData |  |
| 1462 | `gets` | `0x30780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1463 | `gets_s` | `0x30790` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 687 | `_getw` | `0x30798` | 179 | UnwindData |  |
| 692 | `_getws` | `0x3084C` | 392 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 693 | `_getws_s` | `0x309D4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 662 | `_get_output_format` | `0x309DC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1045 | `_set_output_format` | `0x309E4` | 52 | UnwindData |  |
| 993 | `_pclose` | `0x30A18` | 220 | UnwindData |  |
| 997 | `_popen` | `0x30AF4` | 1,666 | UnwindData |  |
| 664 | `_get_printf_count_output` | `0x31210` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 998 | `_printf_l` | `0x31228` | 33 | UnwindData |  |
| 999 | `_printf_p` | `0x3124C` | 39 | UnwindData |  |
| 1000 | `_printf_p_l` | `0x31274` | 33 | UnwindData |  |
| 1001 | `_printf_s_l` | `0x31298` | 33 | UnwindData |  |
| 1046 | `_set_printf_count_output` | `0x312BC` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1524 | `printf` | `0x312E4` | 171 | UnwindData |  |
| 1525 | `printf_s` | `0x31390` | 39 | UnwindData |  |
| 1528 | `puts` | `0x313B8` | 387 | UnwindData |  |
| 1007 | `_putw` | `0x3153C` | 175 | UnwindData |  |
| 1010 | `_putws` | `0x315EC` | 240 | UnwindData |  |
| 1539 | `rewind` | `0x316DC` | 204 | UnwindData |  |
| 1018 | `_rmtmp` | `0x317A8` | 158 | UnwindData |  |
| 1025 | `_scanf_l` | `0x31848` | 46 | UnwindData |  |
| 1026 | `_scanf_s_l` | `0x31878` | 46 | UnwindData |  |
| 1540 | `scanf` | `0x318A8` | 50 | UnwindData |  |
| 1541 | `scanf_s` | `0x318DC` | 50 | UnwindData |  |
| 682 | `_getmaxstdio` | `0x31910` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1051 | `_setmaxstdio` | `0x31918` | 273 | UnwindData |  |
| 1542 | `setbuf` | `0x31A2C` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1545 | `setvbuf` | `0x31A48` | 273 | UnwindData |  |
| 1056 | `_snprintf` | `0x31B5C` | 177 | UnwindData |  |
| 1059 | `_snprintf_l` | `0x31C10` | 29 | UnwindData |  |
| 1057 | `_snprintf_c` | `0x31C30` | 191 | UnwindData |  |
| 1058 | `_snprintf_c_l` | `0x31CF0` | 29 | UnwindData |  |
| 1062 | `_snscanf` | `0x31D10` | 54 | UnwindData |  |
| 1063 | `_snscanf_l` | `0x31D48` | 49 | UnwindData |  |
| 1064 | `_snscanf_s` | `0x31D7C` | 54 | UnwindData |  |
| 1065 | `_snscanf_s_l` | `0x31DB4` | 49 | UnwindData |  |
| 1066 | `_snwprintf` | `0x31E8C` | 226 | UnwindData |  |
| 1067 | `_snwprintf_l` | `0x31F70` | 29 | UnwindData |  |
| 1070 | `_snwscanf` | `0x31F90` | 54 | UnwindData |  |
| 1071 | `_snwscanf_l` | `0x31FC8` | 49 | UnwindData |  |
| 1072 | `_snwscanf_s` | `0x31FFC` | 54 | UnwindData |  |
| 1073 | `_snwscanf_s_l` | `0x32034` | 49 | UnwindData |  |
| 1027 | `_scprintf` | `0x32118` | 37 | UnwindData |  |
| 1028 | `_scprintf_l` | `0x32140` | 33 | UnwindData |  |
| 1029 | `_scprintf_p` | `0x32164` | 37 | UnwindData |  |
| 1030 | `_scprintf_p_l` | `0x3218C` | 33 | UnwindData |  |
| 1060 | `_snprintf_s` | `0x321B0` | 34 | UnwindData |  |
| 1061 | `_snprintf_s_l` | `0x321D4` | 33 | UnwindData |  |
| 1086 | `_sprintf_l` | `0x321F8` | 29 | UnwindData |  |
| 1087 | `_sprintf_p` | `0x32218` | 36 | UnwindData |  |
| 1088 | `_sprintf_p_l` | `0x3223C` | 29 | UnwindData |  |
| 1089 | `_sprintf_s_l` | `0x3225C` | 29 | UnwindData |  |
| 1551 | `sprintf` | `0x3227C` | 160 | UnwindData |  |
| 1552 | `sprintf_s` | `0x3231C` | 36 | UnwindData |  |
| 1090 | `_sscanf_l` | `0x32340` | 49 | UnwindData |  |
| 1091 | `_sscanf_s_l` | `0x32374` | 49 | UnwindData |  |
| 1556 | `sscanf` | `0x323A8` | 53 | UnwindData |  |
| 1557 | `sscanf_s` | `0x323E0` | 53 | UnwindData |  |
| 450 | `__swprintf_l` | `0x325F4` | 29 | UnwindData |  |
| 1031 | `_scwprintf` | `0x32614` | 37 | UnwindData |  |
| 1032 | `_scwprintf_l` | `0x3263C` | 33 | UnwindData |  |
| 1033 | `_scwprintf_p` | `0x32660` | 37 | UnwindData |  |
| 1034 | `_scwprintf_p_l` | `0x32688` | 33 | UnwindData |  |
| 1068 | `_snwprintf_s` | `0x326AC` | 34 | UnwindData |  |
| 1069 | `_snwprintf_s_l` | `0x326D0` | 33 | UnwindData |  |
| 1138 | `_swprintf` | `0x326F4` | 196 | UnwindData |  |
| 1141 | `_swprintf_p` | `0x327B8` | 36 | UnwindData |  |
| 1142 | `_swprintf_p_l` | `0x327DC` | 29 | UnwindData |  |
| 1143 | `_swprintf_s_l` | `0x327FC` | 29 | UnwindData |  |
| 1586 | `swprintf_s` | `0x3281C` | 36 | UnwindData |  |
| 1139 | `_swprintf_c` | `0x32840` | 252 | UnwindData |  |
| 1140 | `_swprintf_c_l` | `0x3293C` | 29 | UnwindData |  |
| 1144 | `_swscanf_l` | `0x3295C` | 49 | UnwindData |  |
| 1145 | `_swscanf_s_l` | `0x32990` | 49 | UnwindData |  |
| 1587 | `swscanf` | `0x329C4` | 53 | UnwindData |  |
| 1588 | `swscanf_s` | `0x329FC` | 53 | UnwindData |  |
| 1150 | `_tempnam` | `0x32AE4` | 725 | UnwindData |  |
| 1594 | `tmpfile` | `0x333C4` | 35 | UnwindData |  |
| 1595 | `tmpfile_s` | `0x333E8` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1596 | `tmpnam` | `0x333F4` | 48 | UnwindData |  |
| 1597 | `tmpnam_s` | `0x33424` | 64 | UnwindData |  |
| 1172 | `_ungetc_nolock` | `0x33464` | 264 | UnwindData |  |
| 1602 | `ungetc` | `0x3356C` | 104 | UnwindData |  |
| 1175 | `_ungetwc_nolock` | `0x335D4` | 516 | UnwindData |  |
| 1603 | `ungetwc` | `0x337D8` | 110 | UnwindData |  |
| 1204 | `_vprintf_l` | `0x33848` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1205 | `_vprintf_p` | `0x33860` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1206 | `_vprintf_p_l` | `0x33878` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1207 | `_vprintf_s_l` | `0x33890` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1608 | `vprintf` | `0x338A8` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1609 | `vprintf_s` | `0x33968` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1196 | `_vfprintf_l` | `0x33980` | 35 | UnwindData |  |
| 1197 | `_vfprintf_p` | `0x339A4` | 35 | UnwindData |  |
| 1198 | `_vfprintf_p_l` | `0x339C8` | 35 | UnwindData |  |
| 1199 | `_vfprintf_s_l` | `0x339EC` | 35 | UnwindData |  |
| 1604 | `vfprintf` | `0x33A10` | 35 | UnwindData |  |
| 1605 | `vfprintf_s` | `0x33B7C` | 35 | UnwindData |  |
| 1200 | `_vfwprintf_l` | `0x33BA0` | 35 | UnwindData |  |
| 1201 | `_vfwprintf_p` | `0x33BC4` | 35 | UnwindData |  |
| 1202 | `_vfwprintf_p_l` | `0x33BE8` | 35 | UnwindData |  |
| 1203 | `_vfwprintf_s_l` | `0x33C0C` | 35 | UnwindData |  |
| 1606 | `vfwprintf` | `0x33C30` | 35 | UnwindData |  |
| 1607 | `vfwprintf_s` | `0x33CF4` | 35 | UnwindData |  |
| 1208 | `_vscprintf` | `0x33D18` | 168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1209 | `_vscprintf_l` | `0x33DC0` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1210 | `_vscprintf_p` | `0x33DD8` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1211 | `_vscprintf_p_l` | `0x33DF0` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1226 | `_vsprintf_l` | `0x33E08` | 181 | UnwindData |  |
| 1610 | `vsprintf` | `0x33EC0` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1216 | `_vsnprintf` | `0x33ECC` | 22 | UnwindData |  |
| 1219 | `_vsnprintf_l` | `0x33EE4` | 203 | UnwindData |  |
| 1217 | `_vsnprintf_c` | `0x33FB0` | 49 | UnwindData |  |
| 1218 | `_vsnprintf_c_l` | `0x33FE4` | 53 | UnwindData |  |
| 1220 | `_vsnprintf_s` | `0x34104` | 30 | UnwindData |  |
| 1221 | `_vsnprintf_s_l` | `0x34124` | 328 | UnwindData |  |
| 1227 | `_vsprintf_p` | `0x3426C` | 49 | UnwindData |  |
| 1228 | `_vsprintf_p_l` | `0x342A0` | 53 | UnwindData |  |
| 1229 | `_vsprintf_s_l` | `0x342D8` | 110 | UnwindData |  |
| 1611 | `vsprintf_s` | `0x34348` | 22 | UnwindData |  |
| 1222 | `_vsnwprintf` | `0x34360` | 22 | UnwindData |  |
| 1223 | `_vsnwprintf_l` | `0x34378` | 252 | UnwindData |  |
| 462 | `__vswprintf_l` | `0x34474` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1212 | `_vscwprintf` | `0x3447C` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1213 | `_vscwprintf_l` | `0x34494` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1214 | `_vscwprintf_p` | `0x344AC` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1215 | `_vscwprintf_p_l` | `0x344C4` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1230 | `_vswprintf` | `0x344DC` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1233 | `_vswprintf_l` | `0x344E8` | 221 | UnwindData |  |
| 1224 | `_vsnwprintf_s` | `0x345C8` | 30 | UnwindData |  |
| 1225 | `_vsnwprintf_s_l` | `0x345E8` | 333 | UnwindData |  |
| 1231 | `_vswprintf_c` | `0x34738` | 49 | UnwindData |  |
| 1232 | `_vswprintf_c_l` | `0x3476C` | 53 | UnwindData |  |
| 1234 | `_vswprintf_p` | `0x348C0` | 49 | UnwindData |  |
| 1235 | `_vswprintf_p_l` | `0x348F4` | 53 | UnwindData |  |
| 1236 | `_vswprintf_s_l` | `0x3492C` | 121 | UnwindData |  |
| 1612 | `vswprintf_s` | `0x349A8` | 22 | UnwindData |  |
| 1237 | `_vwprintf_l` | `0x349C0` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1238 | `_vwprintf_p` | `0x349D8` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1239 | `_vwprintf_p_l` | `0x349F0` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1240 | `_vwprintf_s_l` | `0x34A08` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1613 | `vwprintf` | `0x34A20` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1614 | `vwprintf_s` | `0x34A38` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1306 | `_wfdopen` | `0x34A50` | 454 | UnwindData |  |
| 1315 | `_wfopen` | `0x34C18` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1316 | `_wfopen_s` | `0x34C24` | 83 | UnwindData |  |
| 1319 | `_wfsopen` | `0x34C78` | 221 | UnwindData |  |
| 1317 | `_wfreopen` | `0x34D58` | 47 | UnwindData |  |
| 1318 | `_wfreopen_s` | `0x34E78` | 22 | UnwindData |  |
| 1333 | `_wpopen` | `0x3516C` | 1,824 | UnwindData |  |
| 1334 | `_wprintf_l` | `0x3588C` | 33 | UnwindData |  |
| 1335 | `_wprintf_p` | `0x358B0` | 39 | UnwindData |  |
| 1336 | `_wprintf_p_l` | `0x358D8` | 33 | UnwindData |  |
| 1337 | `_wprintf_s_l` | `0x358FC` | 33 | UnwindData |  |
| 1652 | `wprintf` | `0x35920` | 171 | UnwindData |  |
| 1653 | `wprintf_s` | `0x359CC` | 39 | UnwindData |  |
| 1344 | `_wscanf_l` | `0x359F4` | 46 | UnwindData |  |
| 1345 | `_wscanf_s_l` | `0x35A24` | 46 | UnwindData |  |
| 1654 | `wscanf` | `0x35AE4` | 50 | UnwindData |  |
| 1655 | `wscanf_s` | `0x35B18` | 50 | UnwindData |  |
| 1370 | `_wtempnam` | `0x35B4C` | 660 | UnwindData |  |
| 1371 | `_wtmpnam` | `0x35DE0` | 48 | UnwindData |  |
| 1372 | `_wtmpnam_s` | `0x35FD4` | 64 | UnwindData |  |
| 1512 | `memchr` | `0x362D8` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1515 | `memcpy_s` | `0x362F4` | 135 | UnwindData |  |
| 977 | `_memccpy` | `0x3637C` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1517 | `memmove_s` | `0x363A4` | 81 | UnwindData |  |
| 1565 | `strcspn` | `0x363F8` | 160 | UnwindData |  |
| 1100 | `_strdup` | `0x36498` | 112 | UnwindData |  |
| 1118 | `_strnset` | `0x36508` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1576 | `strpbrk` | `0x36524` | 161 | UnwindData |  |
| 1120 | `_strrev` | `0x365C8` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1121 | `_strset` | `0x36600` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1578 | `strspn` | `0x36614` | 195 | UnwindData |  |
| 1560 | `strchr` | `0x367E0` | 138 | UnwindData |  |
| 1577 | `strrchr` | `0x3686C` | 324 | UnwindData |  |
| 1579 | `strstr` | `0x369B0` | 477 | UnwindData |  |
| 1619 | `wcschr` | `0x36B90` | 140 | UnwindData |  |
| 1634 | `wcsrchr` | `0x36C1C` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1638 | `wcsstr` | `0x36CCC` | 508 | UnwindData |  |
| 1575 | `strnlen` | `0x36EC8` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1559 | `strcat_s` | `0x36EE4` | 124 | UnwindData |  |
| 1571 | `strncat_s` | `0x36F60` | 213 | UnwindData |  |
| 1564 | `strcpy_s` | `0x37038` | 97 | UnwindData |  |
| 1574 | `strncpy_s` | `0x3709C` | 188 | UnwindData |  |
| 449 | `__strncnt` | `0x37158` | 36 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1122 | `_strset_s` | `0x3717C` | 79 | UnwindData |  |
| 1119 | `_strnset_s` | `0x371CC` | 122 | UnwindData |  |
| 1581 | `strtok` | `0x37248` | 248 | UnwindData |  |
| 1582 | `strtok_s` | `0x37340` | 283 | UnwindData |  |
| 1617 | `wcscat` | `0x3745C` | 44 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1622 | `wcscpy` | `0x37488` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1618 | `wcscat_s` | `0x374A4` | 133 | UnwindData |  |
| 1620 | `wcscmp` | `0x3752C` | 60 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1623 | `wcscpy_s` | `0x37568` | 107 | UnwindData |  |
| 1624 | `wcscspn` | `0x375D4` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1252 | `_wcsdup` | `0x37614` | 117 | UnwindData |  |
| 1626 | `wcslen` | `0x3768C` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1632 | `wcsnlen` | `0x376A8` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1627 | `wcsncat` | `0x376C8` | 60 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1628 | `wcsncat_s` | `0x37704` | 231 | UnwindData |  |
| 1629 | `wcsncmp` | `0x377EC` | 44 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 466 | `__wcsncnt` | `0x37818` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1630 | `wcsncpy` | `0x37840` | 70 | UnwindData |  |
| 1631 | `wcsncpy_s` | `0x37888` | 204 | UnwindData |  |
| 1270 | `_wcsnset` | `0x37954` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1271 | `_wcsnset_s` | `0x37974` | 129 | UnwindData |  |
| 1633 | `wcspbrk` | `0x379F8` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1272 | `_wcsrev` | `0x37A30` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1273 | `_wcsset` | `0x37A70` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1274 | `_wcsset_s` | `0x37A84` | 84 | UnwindData |  |
| 1637 | `wcsspn` | `0x37AD8` | 83 | UnwindData |  |
| 1640 | `wcstok` | `0x37B2C` | 167 | UnwindData |  |
| 1641 | `wcstok_s` | `0x37BD4` | 191 | UnwindData |  |
| 1650 | `wmemcpy_s` | `0x37C94` | 122 | UnwindData |  |
| 1651 | `wmemmove_s` | `0x37D10` | 82 | UnwindData |  |
| 1391 | `asctime` | `0x37D64` | 121 | UnwindData |  |
| 1392 | `asctime_s` | `0x37DE0` | 725 | UnwindData |  |
| 1411 | `clock` | `0x380E4` | 61 | UnwindData |  |
| 540 | `_ctime32` | `0x38124` | 107 | UnwindData |  |
| 541 | `_ctime32_s` | `0x38190` | 147 | UnwindData |  |
| 556 | `_difftime32` | `0x38224` | 43 | UnwindData |  |
| 557 | `_difftime64` | `0x38250` | 46 | UnwindData |  |
| 637 | `_ftime32` | `0x38534` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 638 | `_ftime32_s` | `0x3853C` | 399 | UnwindData |  |
| 694 | `_gmtime32` | `0x38714` | 69 | UnwindData |  |
| 695 | `_gmtime32_s` | `0x3875C` | 424 | UnwindData |  |
| 819 | `_localtime32` | `0x38904` | 69 | UnwindData |  |
| 820 | `_localtime32_s` | `0x3894C` | 722 | UnwindData |  |
| 981 | `_mkgmtime32` | `0x38F04` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 985 | `_mktime32` | `0x38F0C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1098 | `_strdate` | `0x38F18` | 272 | UnwindData |  |
| 1099 | `_strdate_s` | `0x39028` | 303 | UnwindData |  |
| 1123 | `_strtime` | `0x39158` | 248 | UnwindData |  |
| 1124 | `_strtime_s` | `0x39250` | 279 | UnwindData |  |
| 1151 | `_time32` | `0x39368` | 85 | UnwindData |  |
| 398 | `__daylight` | `0x393C0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 401 | `__dstbias` | `0x393C8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 455 | `__timezone` | `0x393D0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 457 | `__tzname` | `0x393D8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 654 | `_get_daylight` | `0x393E0` | 47 | UnwindData |  |
| 656 | `_get_dstbias` | `0x39410` | 47 | UnwindData |  |
| 667 | `_get_timezone` | `0x39440` | 47 | UnwindData |  |
| 668 | `_get_tzname` | `0x39470` | 177 | UnwindData |  |
| 1161 | `_tzset` | `0x3983C` | 36 | UnwindData |  |
| 642 | `_futime32` | `0x39F9C` | 513 | UnwindData |  |
| 1182 | `_utime32` | `0x3A1A0` | 139 | UnwindData |  |
| 542 | `_ctime64` | `0x3A22C` | 108 | UnwindData |  |
| 543 | `_ctime64_s` | `0x3A298` | 162 | UnwindData |  |
| 639 | `_ftime64` | `0x3A608` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 640 | `_ftime64_s` | `0x3A610` | 402 | UnwindData |  |
| 696 | `_gmtime64` | `0x3A7A4` | 69 | UnwindData |  |
| 697 | `_gmtime64_s` | `0x3A7EC` | 724 | UnwindData |  |
| 821 | `_localtime64` | `0x3AAC0` | 69 | UnwindData |  |
| 822 | `_localtime64_s` | `0x3AB08` | 780 | UnwindData |  |
| 982 | `_mkgmtime64` | `0x3B0EC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 986 | `_mktime64` | `0x3B0F4` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 686 | `_getsystime` | `0x3B100` | 158 | UnwindData |  |
| 1054 | `_setsystime` | `0x3B1A0` | 163 | UnwindData |  |
| 1152 | `_time64` | `0x3B244` | 93 | UnwindData |  |
| 643 | `_futime64` | `0x3B2A4` | 517 | UnwindData |  |
| 1183 | `_utime64` | `0x3B4AC` | 139 | UnwindData |  |
| 1243 | `_wasctime` | `0x3B538` | 121 | UnwindData |  |
| 1244 | `_wasctime_s` | `0x3B5B4` | 785 | UnwindData |  |
| 1289 | `_wctime32` | `0x3B8C8` | 107 | UnwindData |  |
| 1290 | `_wctime32_s` | `0x3B934` | 141 | UnwindData |  |
| 1291 | `_wctime64` | `0x3B9C4` | 108 | UnwindData |  |
| 1292 | `_wctime64_s` | `0x3BA30` | 158 | UnwindData |  |
| 1365 | `_wstrdate` | `0x3BAD0` | 314 | UnwindData |  |
| 1366 | `_wstrdate_s` | `0x3BC0C` | 343 | UnwindData |  |
| 1367 | `_wstrtime` | `0x3BD64` | 290 | UnwindData |  |
| 1368 | `_wstrtime_s` | `0x3BE88` | 319 | UnwindData |  |
| 1382 | `_wutime32` | `0x3BFC8` | 139 | UnwindData |  |
| 1383 | `_wutime64` | `0x3C054` | 139 | UnwindData |  |
| 1513 | `memcmp` | `0x3C0F0` | 199 | UnwindData |  |
| 1572 | `strncmp` | `0x3C1D0` | 125 | UnwindData |  |
| 1514 | `memcpy` | `0x3C260` | 1,252 | UnwindData |  |
| 1516 | `memmove` | `0x3C260` | 1,252 | UnwindData |  |
| 1518 | `memset` | `0x3C760` | 266 | UnwindData |  |
| 1558 | `strcat` | `0x3C880` | 144 | UnwindData |  |
| 1563 | `strcpy` | `0x3C920` | 183 | UnwindData |  |
| 1561 | `strcmp` | `0x3C9F0` | 103 | UnwindData |  |
| 1569 | `strlen` | `0x3CA70` | 168 | UnwindData |  |
| 1570 | `strncat` | `0x3CB30` | 405 | UnwindData |  |
| 1573 | `strncpy` | `0x3CCE0` | 354 | UnwindData |  |
| 410 | `__isascii` | `0x3CEEC` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 411 | `__iscsym` | `0x3CEF8` | 40 | UnwindData |  |
| 412 | `__iscsymf` | `0x3CF20` | 37 | UnwindData |  |
| 456 | `__toascii` | `0x3CF48` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 718 | `_isalnum_l` | `0x3CF50` | 98 | UnwindData |  |
| 719 | `_isalpha_l` | `0x3CFB4` | 98 | UnwindData |  |
| 721 | `_iscntrl_l` | `0x3D018` | 95 | UnwindData |  |
| 724 | `_isdigit_l` | `0x3D078` | 95 | UnwindData |  |
| 725 | `_isgraph_l` | `0x3D0D8` | 98 | UnwindData |  |
| 727 | `_islower_l` | `0x3D13C` | 95 | UnwindData |  |
| 788 | `_isprint_l` | `0x3D19C` | 98 | UnwindData |  |
| 789 | `_ispunct_l` | `0x3D200` | 95 | UnwindData |  |
| 790 | `_isspace_l` | `0x3D260` | 95 | UnwindData |  |
| 791 | `_isupper_l` | `0x3D2C0` | 95 | UnwindData |  |
| 806 | `_isxdigit_l` | `0x3D320` | 98 | UnwindData |  |
| 1467 | `isalnum` | `0x3D384` | 127 | UnwindData |  |
| 1468 | `isalpha` | `0x3D404` | 127 | UnwindData |  |
| 1469 | `iscntrl` | `0x3D484` | 122 | UnwindData |  |
| 1470 | `isdigit` | `0x3D500` | 122 | UnwindData |  |
| 1471 | `isgraph` | `0x3D57C` | 127 | UnwindData |  |
| 1473 | `islower` | `0x3D5FC` | 122 | UnwindData |  |
| 1474 | `isprint` | `0x3D678` | 127 | UnwindData |  |
| 1475 | `ispunct` | `0x3D6F8` | 122 | UnwindData |  |
| 1476 | `isspace` | `0x3D774` | 122 | UnwindData |  |
| 1477 | `isupper` | `0x3D7F0` | 122 | UnwindData |  |
| 1491 | `isxdigit` | `0x3D86C` | 127 | UnwindData |  |
| 968 | `_mbstrlen` | `0x3D8EC` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 969 | `_mbstrlen_l` | `0x3D900` | 174 | UnwindData |  |
| 970 | `_mbstrnlen` | `0x3D9B0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 971 | `_mbstrnlen_l` | `0x3D9B8` | 271 | UnwindData |  |
| 413 | `__iswcsym` | `0x3DAC8` | 44 | UnwindData |  |
| 795 | `_iswcsym_l` | `0x3DAC8` | 44 | UnwindData |  |
| 414 | `__iswcsymf` | `0x3DAF4` | 44 | UnwindData |  |
| 796 | `_iswcsymf_l` | `0x3DAF4` | 44 | UnwindData |  |
| 726 | `_isleadbyte_l` | `0x3DB20` | 67 | UnwindData |  |
| 800 | `_iswlower_l` | `0x3DB64` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1485 | `iswlower` | `0x3DB64` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 801 | `_iswprint_l` | `0x3DB70` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1486 | `iswprint` | `0x3DB70` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 802 | `_iswpunct_l` | `0x3DB7C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1487 | `iswpunct` | `0x3DB7C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 803 | `_iswspace_l` | `0x3DB88` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1488 | `iswspace` | `0x3DB88` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 805 | `_iswxdigit_l` | `0x3DB94` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1490 | `iswxdigit` | `0x3DB94` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1472 | `isleadbyte` | `0x3DBA0` | 69 | UnwindData |  |
| 792 | `_iswalnum_l` | `0x3DBE8` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1478 | `iswalnum` | `0x3DBE8` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 793 | `_iswalpha_l` | `0x3DBF4` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1479 | `iswalpha` | `0x3DBF4` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1480 | `iswascii` | `0x3DC00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 794 | `_iswcntrl_l` | `0x3DC10` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1481 | `iswcntrl` | `0x3DC10` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 798 | `_iswdigit_l` | `0x3DC1C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1483 | `iswdigit` | `0x3DC1C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 799 | `_iswgraph_l` | `0x3DC28` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1484 | `iswgraph` | `0x3DC28` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 804 | `_iswupper_l` | `0x3DC34` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1489 | `iswupper` | `0x3DC34` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 483 | `_atodbl` | `0x3DC40` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 484 | `_atodbl_l` | `0x3DC48` | 199 | UnwindData |  |
| 486 | `_atoflt` | `0x3DD10` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 487 | `_atoflt_l` | `0x3DD18` | 199 | UnwindData |  |
| 492 | `_atoldbl` | `0x3DDE0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 493 | `_atoldbl_l` | `0x3DDE8` | 202 | UnwindData |  |
| 371 | `__STRINGTOLD` | `0x3DEB4` | 110 | UnwindData |  |
| 485 | `_atof_l` | `0x3DF24` | 186 | UnwindData |  |
| 1400 | `atof` | `0x3DFE0` | 152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 563 | `_ecvt` | `0x3E078` | 178 | UnwindData |  |
| 564 | `_ecvt_s` | `0x3E12C` | 205 | UnwindData |  |
| 582 | `_fcvt` | `0x3E1FC` | 218 | UnwindData |  |
| 583 | `_fcvt_s` | `0x3E2D8` | 205 | UnwindData |  |
| 651 | `_gcvt` | `0x3E3A8` | 44 | UnwindData |  |
| 652 | `_gcvt_s` | `0x3E3D4` | 362 | UnwindData |  |
| 797 | `_iswctype_l` | `0x3E540` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1466 | `is_wctype` | `0x3E540` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1482 | `iswctype` | `0x3E548` | 102 | UnwindData |  |
| 722 | `_isctype` | `0x3E5B0` | 36 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 723 | `_isctype_l` | `0x3E5D4` | 219 | UnwindData |  |
| 867 | `_mblen_l` | `0x3E6B0` | 227 | UnwindData |  |
| 1504 | `mblen` | `0x3E794` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 966 | `_mbstowcs_l` | `0x3E7B0` | 484 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 967 | `_mbstowcs_s_l` | `0x3E994` | 304 | UnwindData |  |
| 1509 | `mbstowcs` | `0x3EAC4` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1510 | `mbstowcs_s` | `0x3EAE0` | 30 | UnwindData |  |
| 976 | `_mbtowc_l` | `0x3EB00` | 337 | UnwindData |  |
| 1511 | `mbtowc` | `0x3EC54` | 852 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1405 | `btowc` | `0x3EFA8` | 100 | UnwindData |  |
| 1505 | `mbrlen` | `0x3F00C` | 62 | UnwindData |  |
| 1506 | `mbrtowc` | `0x3F04C` | 92 | UnwindData |  |
| 1507 | `mbsrtowcs` | `0x3F0A8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1508 | `mbsrtowcs_s` | `0x3F0B0` | 209 | UnwindData |  |
| 1125 | `_strtod_l` | `0x3F184` | 341 | UnwindData |  |
| 1580 | `strtod` | `0x3F2DC` | 580 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1128 | `_strtol_l` | `0x3F520` | 34 | UnwindData |  |
| 1131 | `_strtoul_l` | `0x3F544` | 37 | UnwindData |  |
| 1583 | `strtol` | `0x3F56C` | 48 | UnwindData |  |
| 1584 | `strtoul` | `0x3F59C` | 51 | UnwindData |  |
| 1126 | `_strtoi64` | `0x3F820` | 48 | UnwindData |  |
| 1127 | `_strtoi64_l` | `0x3F850` | 34 | UnwindData |  |
| 1129 | `_strtoui64` | `0x3F874` | 51 | UnwindData |  |
| 1130 | `_strtoui64_l` | `0x3F8A8` | 37 | UnwindData |  |
| 1154 | `_tolower` | `0x3F8D0` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1155 | `_tolower_l` | `0x3F8D4` | 338 | UnwindData |  |
| 1598 | `tolower` | `0x3FA28` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1156 | `_toupper` | `0x3FA48` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1157 | `_toupper_l` | `0x3FA4C` | 336 | UnwindData |  |
| 1599 | `toupper` | `0x3FB9C` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1158 | `_towlower_l` | `0x3FBBC` | 202 | UnwindData |  |
| 1600 | `towlower` | `0x3FC88` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1159 | `_towupper_l` | `0x3FC90` | 207 | UnwindData |  |
| 1601 | `towupper` | `0x3FD60` | 676 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1615 | `wcrtomb` | `0x40004` | 58 | UnwindData |  |
| 1616 | `wcrtomb_s` | `0x40040` | 136 | UnwindData |  |
| 1635 | `wcsrtombs` | `0x400C8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1636 | `wcsrtombs_s` | `0x400D0` | 192 | UnwindData |  |
| 1647 | `wctob` | `0x40190` | 109 | UnwindData |  |
| 1275 | `_wcstod_l` | `0x40200` | 304 | UnwindData |  |
| 1639 | `wcstod` | `0x40330` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1278 | `_wcstol_l` | `0x40520` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1642 | `wcstol` | `0x40520` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1283 | `_wcstoul_l` | `0x40528` | 628 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1645 | `wcstoul` | `0x40528` | 628 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1276 | `_wcstoi64` | `0x4079C` | 48 | UnwindData |  |
| 1277 | `_wcstoi64_l` | `0x407CC` | 34 | UnwindData |  |
| 1281 | `_wcstoui64` | `0x407F0` | 51 | UnwindData |  |
| 1282 | `_wcstoui64_l` | `0x40824` | 37 | UnwindData |  |
| 1279 | `_wcstombs_l` | `0x4084C` | 824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1280 | `_wcstombs_s_l` | `0x40B84` | 236 | UnwindData |  |
| 1643 | `wcstombs` | `0x40C70` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1644 | `wcstombs_s` | `0x40C78` | 30 | UnwindData |  |
| 1293 | `_wctomb_l` | `0x40C98` | 123 | UnwindData |  |
| 1294 | `_wctomb_s_l` | `0x40D14` | 394 | UnwindData |  |
| 1648 | `wctomb` | `0x40EA0` | 84 | UnwindData |  |
| 1649 | `wctomb_s` | `0x40EF4` | 20 | UnwindData |  |
| 1373 | `_wtof` | `0x40F08` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1374 | `_wtof_l` | `0x40F10` | 142 | UnwindData |  |
| 750 | `_ismbcalnum` | `0x40FA0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 751 | `_ismbcalnum_l` | `0x40FA8` | 202 | UnwindData |  |
| 752 | `_ismbcalpha` | `0x41074` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 753 | `_ismbcalpha_l` | `0x4107C` | 204 | UnwindData |  |
| 728 | `_ismbbalnum` | `0x411C4` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 729 | `_ismbbalnum_l` | `0x411DC` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 730 | `_ismbbalpha` | `0x411F8` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 731 | `_ismbbalpha_l` | `0x41210` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 732 | `_ismbbgraph` | `0x4122C` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 733 | `_ismbbgraph_l` | `0x41244` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 734 | `_ismbbkalnum` | `0x41260` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 735 | `_ismbbkalnum_l` | `0x41274` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 736 | `_ismbbkana` | `0x4128C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 737 | `_ismbbkana_l` | `0x41294` | 101 | UnwindData |  |
| 738 | `_ismbbkprint` | `0x412FC` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 739 | `_ismbbkprint_l` | `0x41310` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 740 | `_ismbbkpunct` | `0x41328` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 741 | `_ismbbkpunct_l` | `0x4133C` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 742 | `_ismbblead` | `0x41354` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 743 | `_ismbblead_l` | `0x41368` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 744 | `_ismbbprint` | `0x41380` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 745 | `_ismbbprint_l` | `0x41398` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 746 | `_ismbbpunct` | `0x413B4` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 747 | `_ismbbpunct_l` | `0x413C8` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 748 | `_ismbbtrail` | `0x413E0` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 749 | `_ismbbtrail_l` | `0x413F4` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 754 | `_ismbcdigit` | `0x4140C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 755 | `_ismbcdigit_l` | `0x41414` | 206 | UnwindData |  |
| 756 | `_ismbcgraph` | `0x414E4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 757 | `_ismbcgraph_l` | `0x414EC` | 209 | UnwindData |  |
| 758 | `_ismbchira` | `0x415C0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 759 | `_ismbchira_l` | `0x415C8` | 77 | UnwindData |  |
| 760 | `_ismbckata` | `0x41618` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 761 | `_ismbckata_l` | `0x41620` | 85 | UnwindData |  |
| 778 | `_ismbcsymbol` | `0x41678` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 779 | `_ismbcsymbol_l` | `0x41680` | 85 | UnwindData |  |
| 768 | `_ismbclegal` | `0x416D8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 769 | `_ismbclegal_l` | `0x416E0` | 82 | UnwindData |  |
| 770 | `_ismbclower` | `0x41734` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 771 | `_ismbclower_l` | `0x4173C` | 183 | UnwindData |  |
| 772 | `_ismbcprint` | `0x417F4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 773 | `_ismbcprint_l` | `0x417FC` | 204 | UnwindData |  |
| 774 | `_ismbcpunct` | `0x418C8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 775 | `_ismbcpunct_l` | `0x418D0` | 199 | UnwindData |  |
| 782 | `_ismbslead` | `0x41998` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 783 | `_ismbslead_l` | `0x419A0` | 148 | UnwindData |  |
| 776 | `_ismbcspace` | `0x41A34` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 777 | `_ismbcspace_l` | `0x41A3C` | 204 | UnwindData |  |
| 784 | `_ismbstrail` | `0x41B08` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 785 | `_ismbstrail_l` | `0x41B10` | 145 | UnwindData |  |
| 780 | `_ismbcupper` | `0x41BA4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 781 | `_ismbcupper_l` | `0x41BAC` | 182 | UnwindData |  |
| 843 | `_mbbtype` | `0x41C64` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 844 | `_mbbtype_l` | `0x41C6C` | 148 | UnwindData |  |
| 846 | `_mbccpy` | `0x41D00` | 30 | UnwindData |  |
| 847 | `_mbccpy_l` | `0x41D20` | 29 | UnwindData |  |
| 848 | `_mbccpy_s` | `0x41D40` | 20 | UnwindData |  |
| 849 | `_mbccpy_s_l` | `0x41D54` | 261 | UnwindData |  |
| 871 | `_mbscat_s_l` | `0x41E5C` | 461 | UnwindData |  |
| 879 | `_mbscpy_s_l` | `0x4202C` | 320 | UnwindData |  |
| 899 | `_mbsnbcat_s_l` | `0x4216C` | 687 | UnwindData |  |
| 909 | `_mbsnbcpy_s_l` | `0x4241C` | 519 | UnwindData |  |
| 917 | `_mbsnbset_s_l` | `0x42624` | 601 | UnwindData |  |
| 921 | `_mbsncat_s_l` | `0x42880` | 630 | UnwindData |  |
| 931 | `_mbsncpy_s_l` | `0x42AF8` | 503 | UnwindData |  |
| 945 | `_mbsnset_s_l` | `0x42CF0` | 595 | UnwindData |  |
| 955 | `_mbsset_s_l` | `0x42F44` | 350 | UnwindData |  |
| 762 | `_ismbcl0` | `0x430A4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 763 | `_ismbcl0_l` | `0x430AC` | 99 | UnwindData |  |
| 764 | `_ismbcl1` | `0x43110` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 765 | `_ismbcl1_l` | `0x43118` | 104 | UnwindData |  |
| 766 | `_ismbcl2` | `0x43180` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 767 | `_ismbcl2_l` | `0x43188` | 104 | UnwindData |  |
| 683 | `_getmbcp` | `0x435B8` | 58 | UnwindData |  |
| 1052 | `_setmbcp` | `0x435F4` | 604 | UnwindData |  |
| 868 | `_mbsbtype` | `0x43B00` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 869 | `_mbsbtype_l` | `0x43B08` | 179 | UnwindData |  |
| 870 | `_mbscat_s` | `0x43BBC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 872 | `_mbschr` | `0x43BC4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 873 | `_mbschr_l` | `0x43BCC` | 189 | UnwindData |  |
| 874 | `_mbscmp` | `0x43C8C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 875 | `_mbscmp_l` | `0x43C94` | 221 | UnwindData |  |
| 878 | `_mbscpy_s` | `0x43D74` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 876 | `_mbscoll` | `0x43D7C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 877 | `_mbscoll_l` | `0x43D84` | 201 | UnwindData |  |
| 880 | `_mbscspn` | `0x43E50` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 881 | `_mbscspn_l` | `0x43E58` | 217 | UnwindData |  |
| 882 | `_mbsdec` | `0x43F34` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 883 | `_mbsdec_l` | `0x43F3C` | 150 | UnwindData |  |
| 884 | `_mbsicmp` | `0x43FD4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 885 | `_mbsicmp_l` | `0x43FDC` | 493 | UnwindData |  |
| 886 | `_mbsicoll` | `0x441CC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 887 | `_mbsicoll_l` | `0x441D4` | 201 | UnwindData |  |
| 890 | `_mbslen` | `0x442A0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 891 | `_mbslen_l` | `0x442A8` | 107 | UnwindData |  |
| 940 | `_mbsnlen` | `0x44314` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 941 | `_mbsnlen_l` | `0x4431C` | 152 | UnwindData |  |
| 892 | `_mbslwr` | `0x443B4` | 43 | UnwindData |  |
| 893 | `_mbslwr_l` | `0x443E0` | 43 | UnwindData |  |
| 894 | `_mbslwr_s` | `0x4440C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 895 | `_mbslwr_s_l` | `0x44414` | 338 | UnwindData |  |
| 896 | `_mbsnbcat` | `0x44568` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 897 | `_mbsnbcat_l` | `0x44570` | 328 | UnwindData |  |
| 898 | `_mbsnbcat_s` | `0x446B8` | 20 | UnwindData |  |
| 900 | `_mbsnbcmp` | `0x446CC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 901 | `_mbsnbcmp_l` | `0x446D4` | 300 | UnwindData |  |
| 902 | `_mbsnbcnt` | `0x44800` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 903 | `_mbsnbcnt_l` | `0x44808` | 147 | UnwindData |  |
| 904 | `_mbsnbcoll` | `0x4489C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 905 | `_mbsnbcoll_l` | `0x448A4` | 275 | UnwindData |  |
| 906 | `_mbsnbcpy` | `0x449B8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 907 | `_mbsnbcpy_l` | `0x449C0` | 241 | UnwindData |  |
| 908 | `_mbsnbcpy_s` | `0x44AB4` | 20 | UnwindData |  |
| 910 | `_mbsnbicmp` | `0x44AC8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 911 | `_mbsnbicmp_l` | `0x44AD0` | 429 | UnwindData |  |
| 912 | `_mbsnbicoll` | `0x44C80` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 913 | `_mbsnbicoll_l` | `0x44C88` | 255 | UnwindData |  |
| 914 | `_mbsnbset` | `0x44D88` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 915 | `_mbsnbset_l` | `0x44D90` | 242 | UnwindData |  |
| 916 | `_mbsnbset_s` | `0x44E84` | 20 | UnwindData |  |
| 918 | `_mbsncat` | `0x44E98` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 919 | `_mbsncat_l` | `0x44EA0` | 301 | UnwindData |  |
| 920 | `_mbsncat_s` | `0x44FD0` | 20 | UnwindData |  |
| 922 | `_mbsnccnt` | `0x44FE4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 923 | `_mbsnccnt_l` | `0x44FEC` | 152 | UnwindData |  |
| 924 | `_mbsncmp` | `0x45084` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 925 | `_mbsncmp_l` | `0x4508C` | 256 | UnwindData |  |
| 926 | `_mbsncoll` | `0x4518C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 927 | `_mbsncoll_l` | `0x45194` | 311 | UnwindData |  |
| 928 | `_mbsncpy` | `0x452CC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 929 | `_mbsncpy_l` | `0x452D4` | 228 | UnwindData |  |
| 930 | `_mbsncpy_s` | `0x453B8` | 20 | UnwindData |  |
| 932 | `_mbsnextc` | `0x453CC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 933 | `_mbsnextc_l` | `0x453D4` | 114 | UnwindData |  |
| 934 | `_mbsnicmp` | `0x45448` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 935 | `_mbsnicmp_l` | `0x45450` | 386 | UnwindData |  |
| 936 | `_mbsnicoll` | `0x455D4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 937 | `_mbsnicoll_l` | `0x455DC` | 311 | UnwindData |  |
| 942 | `_mbsnset` | `0x45714` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 943 | `_mbsnset_l` | `0x4571C` | 343 | UnwindData |  |
| 944 | `_mbsnset_s` | `0x45874` | 20 | UnwindData |  |
| 946 | `_mbspbrk` | `0x45888` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 947 | `_mbspbrk_l` | `0x45890` | 207 | UnwindData |  |
| 948 | `_mbsrchr` | `0x45960` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 949 | `_mbsrchr_l` | `0x45968` | 185 | UnwindData |  |
| 950 | `_mbsrev` | `0x45A24` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 951 | `_mbsrev_l` | `0x45A2C` | 197 | UnwindData |  |
| 952 | `_mbsset` | `0x45AF4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 953 | `_mbsset_l` | `0x45AFC` | 195 | UnwindData |  |
| 954 | `_mbsset_s` | `0x45BC0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 956 | `_mbsspn` | `0x45BC8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 957 | `_mbsspn_l` | `0x45BD0` | 217 | UnwindData |  |
| 958 | `_mbsspnp` | `0x45CAC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 959 | `_mbsspnp_l` | `0x45CB4` | 221 | UnwindData |  |
| 960 | `_mbsstr` | `0x45D94` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 961 | `_mbsstr_l` | `0x45D9C` | 255 | UnwindData |  |
| 962 | `_mbstok` | `0x45E9C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 963 | `_mbstok_l` | `0x45EA4` | 62 | UnwindData |  |
| 964 | `_mbstok_s` | `0x45EE4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 965 | `_mbstok_s_l` | `0x45EEC` | 483 | UnwindData |  |
| 972 | `_mbsupr` | `0x460D0` | 43 | UnwindData |  |
| 973 | `_mbsupr_l` | `0x460FC` | 43 | UnwindData |  |
| 974 | `_mbsupr_s` | `0x46128` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 975 | `_mbsupr_s_l` | `0x46130` | 338 | UnwindData |  |
| 860 | `_mbctolower` | `0x46284` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 861 | `_mbctolower_l` | `0x4628C` | 192 | UnwindData |  |
| 864 | `_mbctoupper` | `0x4634C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 865 | `_mbctoupper_l` | `0x46354` | 192 | UnwindData |  |
| 850 | `_mbcjistojms` | `0x46414` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 851 | `_mbcjistojms_l` | `0x4641C` | 151 | UnwindData |  |
| 852 | `_mbcjmstojis` | `0x464B4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 853 | `_mbcjmstojis_l` | `0x464BC` | 193 | UnwindData |  |
| 841 | `_mbbtombc` | `0x46580` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 842 | `_mbbtombc_l` | `0x46588` | 169 | UnwindData |  |
| 862 | `_mbctombb` | `0x46634` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 863 | `_mbctombb_l` | `0x4663C` | 206 | UnwindData |  |
| 536 | `_cscanf` | `0x4764C` | 39 | UnwindData |  |
| 537 | `_cscanf_l` | `0x47674` | 33 | UnwindData |  |
| 538 | `_cscanf_s` | `0x48654` | 39 | UnwindData |  |
| 539 | `_cscanf_s_l` | `0x4867C` | 33 | UnwindData |  |
| 551 | `_cwscanf` | `0x496EC` | 39 | UnwindData |  |
| 552 | `_cwscanf_l` | `0x49714` | 33 | UnwindData |  |
| 553 | `_cwscanf_s` | `0x4A990` | 39 | UnwindData |  |
| 554 | `_cwscanf_s_l` | `0x4A9B8` | 33 | UnwindData |  |
| 526 | `_cprintf` | `0x4A9DC` | 39 | UnwindData |  |
| 527 | `_cprintf_l` | `0x4AA04` | 33 | UnwindData |  |
| 1184 | `_vcprintf` | `0x4AA28` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1185 | `_vcprintf_l` | `0x4AA34` | 2,448 | UnwindData |  |
| 528 | `_cprintf_p` | `0x4B410` | 39 | UnwindData |  |
| 529 | `_cprintf_p_l` | `0x4B438` | 33 | UnwindData |  |
| 1186 | `_vcprintf_p` | `0x4B45C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1187 | `_vcprintf_p_l` | `0x4B468` | 4,146 | UnwindData |  |
| 530 | `_cprintf_s` | `0x4C4A8` | 39 | UnwindData |  |
| 531 | `_cprintf_s_l` | `0x4C4D0` | 33 | UnwindData |  |
| 1188 | `_vcprintf_s` | `0x4C4F4` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1189 | `_vcprintf_s_l` | `0x4C500` | 2,490 | UnwindData |  |
| 545 | `_cwprintf` | `0x4CF4C` | 39 | UnwindData |  |
| 546 | `_cwprintf_l` | `0x4CF74` | 33 | UnwindData |  |
| 1190 | `_vcwprintf` | `0x4CF98` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1191 | `_vcwprintf_l` | `0x4CFA4` | 2,709 | UnwindData |  |
| 547 | `_cwprintf_p` | `0x4DAD4` | 39 | UnwindData |  |
| 548 | `_cwprintf_p_l` | `0x4DAFC` | 33 | UnwindData |  |
| 1192 | `_vcwprintf_p` | `0x4DB20` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1193 | `_vcwprintf_p_l` | `0x4DB2C` | 4,518 | UnwindData |  |
| 549 | `_cwprintf_s` | `0x4ED24` | 39 | UnwindData |  |
| 550 | `_cwprintf_s_l` | `0x4ED4C` | 33 | UnwindData |  |
| 1194 | `_vcwprintf_s` | `0x4ED70` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1195 | `_vcwprintf_s_l` | `0x4ED7C` | 2,819 | UnwindData |  |
| 978 | `_memicmp` | `0x58FD0` | 80 | UnwindData |  |
| 979 | `_memicmp_l` | `0x59020` | 224 | UnwindData |  |
| 1097 | `_strcoll_l` | `0x59100` | 184 | UnwindData |  |
| 1562 | `strcoll` | `0x591B8` | 68 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1104 | `_stricmp` | `0x591FC` | 70 | UnwindData |  |
| 1105 | `_stricmp_l` | `0x59244` | 179 | UnwindData |  |
| 1106 | `_stricoll` | `0x592F8` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1107 | `_stricoll_l` | `0x59310` | 184 | UnwindData |  |
| 1108 | `_strlwr` | `0x595CC` | 88 | UnwindData |  |
| 1109 | `_strlwr_l` | `0x59624` | 30 | UnwindData |  |
| 1110 | `_strlwr_s` | `0x59644` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1111 | `_strlwr_s_l` | `0x5964C` | 75 | UnwindData |  |
| 1112 | `_strncoll` | `0x59698` | 79 | UnwindData |  |
| 1113 | `_strncoll_l` | `0x596E8` | 255 | UnwindData |  |
| 1114 | `_strnicmp` | `0x59830` | 79 | UnwindData |  |
| 1115 | `_strnicmp_l` | `0x59880` | 217 | UnwindData |  |
| 1116 | `_strnicoll` | `0x5995C` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1117 | `_strnicoll_l` | `0x59974` | 256 | UnwindData |  |
| 1132 | `_strupr` | `0x59C78` | 88 | UnwindData |  |
| 1133 | `_strupr_l` | `0x59CD0` | 30 | UnwindData |  |
| 1134 | `_strupr_s` | `0x59CF0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1135 | `_strupr_s_l` | `0x59CF8` | 75 | UnwindData |  |
| 1136 | `_strxfrm_l` | `0x59D44` | 374 | UnwindData |  |
| 1585 | `strxfrm` | `0x59EBC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1251 | `_wcscoll_l` | `0x59EC4` | 169 | UnwindData |  |
| 1621 | `wcscoll` | `0x59F70` | 70 | UnwindData |  |
| 1256 | `_wcsicmp` | `0x59FB8` | 132 | UnwindData |  |
| 1257 | `_wcsicmp_l` | `0x5A03C` | 237 | UnwindData |  |
| 1258 | `_wcsicoll` | `0x5A12C` | 132 | UnwindData |  |
| 1259 | `_wcsicoll_l` | `0x5A1B0` | 230 | UnwindData |  |
| 1260 | `_wcslwr` | `0x5A48C` | 95 | UnwindData |  |
| 1261 | `_wcslwr_l` | `0x5A4EC` | 30 | UnwindData |  |
| 1262 | `_wcslwr_s` | `0x5A50C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1263 | `_wcslwr_s_l` | `0x5A514` | 75 | UnwindData |  |
| 1264 | `_wcsncoll` | `0x5A560` | 79 | UnwindData |  |
| 1265 | `_wcsncoll_l` | `0x5A5B0` | 214 | UnwindData |  |
| 1266 | `_wcsnicmp` | `0x5A688` | 151 | UnwindData |  |
| 1267 | `_wcsnicmp_l` | `0x5A720` | 278 | UnwindData |  |
| 1268 | `_wcsnicoll` | `0x5A838` | 146 | UnwindData |  |
| 1269 | `_wcsnicoll_l` | `0x5A8CC` | 304 | UnwindData |  |
| 1284 | `_wcsupr` | `0x5ABF0` | 95 | UnwindData |  |
| 1285 | `_wcsupr_l` | `0x5AC50` | 30 | UnwindData |  |
| 1286 | `_wcsupr_s` | `0x5AC70` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1287 | `_wcsupr_s_l` | `0x5AC78` | 75 | UnwindData |  |
| 1288 | `_wcsxfrm_l` | `0x5ACC4` | 352 | UnwindData |  |
| 1646 | `wcsxfrm` | `0x5AE24` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 336 | `_Getdays` | `0x5AE2C` | 324 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 337 | `_Getmonths` | `0x5AF70` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 344 | `_Strftime` | `0x5B0C0` | 30 | UnwindData |  |
| 1103 | `_strftime_l` | `0x5B288` | 30 | UnwindData |  |
| 1568 | `strftime` | `0x5B2A8` | 26 | UnwindData |  |
| 346 | `_W_Getdays` | `0x5BEE8` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 347 | `_W_Getmonths` | `0x5C068` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 338 | `_Gettnames` | `0x5C1E8` | 2,012 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 348 | `_W_Gettnames` | `0x5C1E8` | 2,012 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 349 | `_Wcsftime` | `0x5C9C4` | 30 | UnwindData |  |
| 1255 | `_wcsftime_l` | `0x5CB7C` | 30 | UnwindData |  |
| 1625 | `wcsftime` | `0x5CB9C` | 26 | UnwindData |  |
| 278 | `?_inconsistency@@YAXXZ` | `0x5CBB8` | 32 | UnwindData |  |
| 315 | `?terminate@@YAXXZ` | `0x5CBD8` | 31 | UnwindData |  |
| 320 | `?unexpected@@YAXXZ` | `0x5CBF8` | 29 | UnwindData |  |
| 27 | `??0__non_rtti_object@std@@QEAA@AEBV01@@Z` | `0x5CC38` | 33 | UnwindData |  |
| 28 | `??0__non_rtti_object@std@@QEAA@PEBD@Z` | `0x5CC5C` | 33 | UnwindData |  |
| 29 | `??0bad_cast@std@@AEAA@PEBQEBD@Z` | `0x5CC80` | 33 | UnwindData |  |
| 30 | `??0bad_cast@std@@QEAA@AEBV01@@Z` | `0x5CCA4` | 33 | UnwindData |  |
| 31 | `??0bad_cast@std@@QEAA@PEBD@Z` | `0x5CCC8` | 42 | UnwindData |  |
| 34 | `??0bad_typeid@std@@QEAA@AEBV01@@Z` | `0x5CCF4` | 33 | UnwindData |  |
| 35 | `??0bad_typeid@std@@QEAA@PEBD@Z` | `0x5CD18` | 42 | UnwindData |  |
| 44 | `??0exception@std@@QEAA@AEBQEBD@Z` | `0x5CD44` | 45 | UnwindData |  |
| 45 | `??0exception@std@@QEAA@AEBQEBDH@Z` | `0x5CD74` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `??0exception@std@@QEAA@AEBV01@@Z` | `0x5CD90` | 42 | UnwindData |  |
| 47 | `??0exception@std@@QEAA@XZ` | `0x5CDBC` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `??1__non_rtti_object@std@@UEAA@XZ` | `0x5CDD4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `??1bad_cast@std@@UEAA@XZ` | `0x5CDD4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `??1bad_typeid@std@@UEAA@XZ` | `0x5CDD4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `??1exception@std@@UEAA@XZ` | `0x5CDD4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `??4exception@std@@QEAAAEAV01@AEBV01@@Z` | `0x5CDE4` | 68 | UnwindData |  |
| 195 | `?_Copy_str@exception@std@@AEAAXPEBD@Z` | `0x5CE9C` | 90 | UnwindData |  |
| 252 | `?_Tidy@exception@std@@AEAAXXZ` | `0x5CEF8` | 39 | UnwindData |  |
| 328 | `?what@exception@std@@UEBAPEBDXZ` | `0x5CF20` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `??1type_info@@UEAA@XZ` | `0x5CF34` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `??8type_info@@QEBA_NAEBV0@@Z` | `0x5CF44` | 30 | UnwindData |  |
| 126 | `??9type_info@@QEBA_NAEBV0@@Z` | `0x5CF64` | 30 | UnwindData |  |
| 281 | `?_name_internal_method@type_info@@QEBAPEBDPEAU__type_info_node@@@Z` | `0x5CFF8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 291 | `?_type_info_dtor_internal_method@type_info@@QEAAXXZ` | `0x5D000` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 294 | `?before@type_info@@QEBA_NAEBV1@@Z` | `0x5D008` | 30 | UnwindData |  |
| 301 | `?name@type_info@@QEBAPEBDPEAU__type_info_node@@@Z` | `0x5D028` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 305 | `?raw_name@type_info@@QEBAPEBDXZ` | `0x5D030` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 364 | `__DestructExceptionObject` | `0x5D038` | 110 | UnwindData |  |
| 277 | `__uncaught_exception` | `0x5D960` | 25 | UnwindData |  |
| 280 | `?_is_exception_typeof@@YAHAEBVtype_info@@PEAU_EXCEPTION_POINTERS@@@Z` | `0x5D97C` | 191 | UnwindData |  |
| 351 | `__AdjustPointer` | `0x5DA3C` | 36 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 352 | `__BuildCatchObject` | `0x5DA60` | 182 | UnwindData |  |
| 353 | `__BuildCatchObjectHelper` | `0x5DB18` | 509 | UnwindData |  |
| 356 | `__CxxDetectRethrow` | `0x5DF1C` | 71 | UnwindData |  |
| 357 | `__CxxExceptionFilter` | `0x5DF64` | 502 | UnwindData |  |
| 361 | `__CxxQueryExceptionSize` | `0x5E15C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 362 | `__CxxRegisterExceptionObject` | `0x5E164` | 193 | UnwindData |  |
| 363 | `__CxxUnregisterExceptionObject` | `0x5E228` | 343 | UnwindData |  |
| 365 | `__FrameUnwindFilter` | `0x5E380` | 83 | UnwindData |  |
| 373 | `__TypeMatch` | `0x5E78C` | 286 | UnwindData |  |
| 332 | `_CxxThrowException` | `0x5E8AC` | 223 | UnwindData |  |
| 331 | `_CreateFrameInfo` | `0x5ED10` | 67 | UnwindData |  |
| 333 | `_FindAndUnlinkFrame` | `0x5ED54` | 94 | UnwindData |  |
| 334 | `_GetImageBase` | `0x5EDB4` | 21 | UnwindData |  |
| 335 | `_GetThrowImageBase` | `0x5EDCC` | 21 | UnwindData |  |
| 340 | `_IsExceptionObjectToBeDestroyed` | `0x5EDE4` | 50 | UnwindData |  |
| 342 | `_SetImageBase` | `0x5EE18` | 27 | UnwindData |  |
| 343 | `_SetThrowImageBase` | `0x5EE34` | 27 | UnwindData |  |
| 358 | `__CxxFrameHandler` | `0x5EFC8` | 135 | UnwindData |  |
| 359 | `__CxxFrameHandler2` | `0x5EFC8` | 135 | UnwindData |  |
| 360 | `__CxxFrameHandler3` | `0x5EFC8` | 135 | UnwindData |  |
| 214 | `?_Name_base@type_info@@CAPEBDPEBV1@PEAU__type_info_node@@@Z` | `0x5F160` | 308 | UnwindData |  |
| 215 | `?_Name_base_internal@type_info@@CAPEBDPEBV1@PEAU__type_info_node@@@Z` | `0x5F294` | 345 | UnwindData |  |
| 259 | `?_Type_info_dtor@type_info@@CAXPEAV1@@Z` | `0x5F3F0` | 108 | UnwindData |  |
| 260 | `?_Type_info_dtor_internal@type_info@@CAXPEAV1@@Z` | `0x5F3F0` | 108 | UnwindData |  |
| 384 | `__clean_type_info_names_internal` | `0x5F45C` | 79 | UnwindData |  |
| 460 | `__unDNameHelper` | `0x5F4AC` | 53 | UnwindData |  |
| 262 | `?_ValidateExecute@@YAHP6A_JXZ@Z` | `0x5F4E4` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 263 | `?_ValidateRead@@YAHPEBXI@Z` | `0x5F4E4` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 264 | `?_ValidateWrite@@YAHPEAXI@Z` | `0x5F4E4` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 288 | `?_set_se_translator@@YAP6AXIPEAU_EXCEPTION_POINTERS@@@ZH@Z` | `0x5F4F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 289 | `?_set_se_translator@@YAP6AXIPEAU_EXCEPTION_POINTERS@@@ZP6AXI0@Z@Z` | `0x5F500` | 51 | UnwindData |  |
| 311 | `?set_terminate@@YAP6AXXZH@Z` | `0x5F534` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 312 | `?set_terminate@@YAP6AXXZP6AXXZ@Z` | `0x5F544` | 75 | UnwindData |  |
| 313 | `?set_unexpected@@YAP6AXXZH@Z` | `0x5F590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 314 | `?set_unexpected@@YAP6AXXZP6AXXZ@Z` | `0x5F5A0` | 75 | UnwindData |  |
| 666 | `_get_terminate` | `0x5F5EC` | 21 | UnwindData |  |
| 669 | `_get_unexpected` | `0x5F604` | 21 | UnwindData |  |
| 368 | `__RTCastToVoid` | `0x5FAAC` | 105 | UnwindData |  |
| 369 | `__RTDynamicCast` | `0x5FB18` | 380 | UnwindData |  |
| 370 | `__RTtypeid` | `0x5FC94` | 169 | UnwindData |  |
| 458 | `__unDName` | `0x65F54` | 261 | UnwindData |  |
| 459 | `__unDNameEx` | `0x6605C` | 267 | UnwindData |  |
| 114 | `??2@YAPEAX_K@Z` | `0x662F8` | 105 | UnwindData |  |
| 116 | `??3@YAXPEAX@Z` | `0x66364` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1444 | `free` | `0x6636C` | 61 | UnwindData |  |
| 1503 | `malloc` | `0x663AC` | 182 | UnwindData |  |
| 503 | `_calloc_crt` | `0x66464` | 128 | UnwindData |  |
| 840 | `_malloc_crt` | `0x664E4` | 123 | UnwindData |  |
| 1013 | `_realloc_crt` | `0x66560` | 130 | UnwindData |  |
| 1015 | `_recalloc_crt` | `0x665E4` | 133 | UnwindData |  |
| 1044 | `_set_malloc_crt_max_wait` | `0x6666C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 659 | `_get_heap_handle` | `0x6667C` | 52 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1406 | `calloc` | `0x666B0` | 65 | UnwindData |  |
| 115 | `??2@YAPEAX_KHPEBDH@Z` | `0x666F4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `??_U@YAPEAX_K@Z` | `0x666F4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `??3@YAXPEAXHPEBDH@Z` | `0x666FC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `??_V@YAXPEAX@Z` | `0x666FC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 473 | `_aligned_free` | `0x66704` | 27 | UnwindData |  |
| 474 | `_aligned_malloc` | `0x66720` | 116 | UnwindData |  |
| 475 | `_aligned_msize` | `0x66794` | 101 | UnwindData |  |
| 476 | `_aligned_offset_malloc` | `0x667FC` | 179 | UnwindData |  |
| 477 | `_aligned_offset_realloc` | `0x668B0` | 458 | UnwindData |  |
| 478 | `_aligned_offset_recalloc` | `0x66A7C` | 163 | UnwindData |  |
| 479 | `_aligned_realloc` | `0x66B20` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 480 | `_aligned_recalloc` | `0x66B28` | 20 | UnwindData |  |
| 579 | `_expand` | `0x66B3C` | 249 | UnwindData |  |
| 698 | `_heapadd` | `0x66C38` | 23 | UnwindData |  |
| 699 | `_heapchk` | `0x66C50` | 45 | UnwindData |  |
| 701 | `_heapset` | `0x66C80` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 700 | `_heapmin` | `0x66C88` | 33 | UnwindData |  |
| 702 | `_heapused` | `0x66CAC` | 22 | UnwindData |  |
| 703 | `_heapwalk` | `0x66CC4` | 327 | UnwindData |  |
| 987 | `_msize` | `0x66E0C` | 57 | UnwindData |  |
| 1014 | `_recalloc` | `0x66E48` | 134 | UnwindData |  |
| 1016 | `_resetstkoflw` | `0x66ED0` | 293 | UnwindData |  |
| 1536 | `realloc` | `0x66FF8` | 211 | UnwindData |  |
| 630 | `_fstat32` | `0x67584` | 951 | UnwindData |  |
| 1330 | `_wopen` | `0x67A30` | 205 | UnwindData |  |
| 1349 | `_wsopen` | `0x67B00` | 65 | UnwindData |  |
| 1350 | `_wsopen_s` | `0x683FC` | 50 | UnwindData |  |
| 517 | `_close` | `0x68430` | 208 | UnwindData |  |
| 632 | `_fstat64` | `0x685CC` | 980 | UnwindData |  |
| 633 | `_fstat64i32` | `0x689A0` | 962 | UnwindData |  |
| 631 | `_fstat32i64` | `0x68D64` | 969 | UnwindData |  |
| 1012 | `_read` | `0x69130` | 295 | UnwindData |  |
| 720 | `_isatty` | `0x69AC4` | 115 | UnwindData |  |
| 1342 | `_write` | `0x69B38` | 236 | UnwindData |  |
| 833 | `_lseeki64` | `0x6A398` | 240 | UnwindData |  |
| 991 | `_open` | `0x6A51C` | 205 | UnwindData |  |
| 1074 | `_sopen` | `0x6A5EC` | 65 | UnwindData |  |
| 1075 | `_sopen_s` | `0x6A794` | 50 | UnwindData |  |
| 518 | `_commit` | `0x6A7C8` | 234 | UnwindData |  |
| 832 | `_lseek` | `0x6A8B4` | 236 | UnwindData |  |
| 996 | `_pipe` | `0x6AA38` | 733 | UnwindData |  |
| 661 | `_get_osfhandle` | `0x6B05C` | 131 | UnwindData |  |
| 992 | `_open_osfhandle` | `0x6B0E0` | 250 | UnwindData |  |
| 672 | `_getch` | `0x6B2B8` | 42 | UnwindData |  |
| 673 | `_getch_nolock` | `0x6B2E4` | 256 | UnwindData |  |
| 674 | `_getche` | `0x6B3E4` | 42 | UnwindData |  |
| 675 | `_getche_nolock` | `0x6B410` | 66 | UnwindData |  |
| 814 | `_kbhit` | `0x6B538` | 42 | UnwindData |  |
| 1173 | `_ungetch` | `0x6B6FC` | 46 | UnwindData |  |
| 1174 | `_ungetch_nolock` | `0x6B72C` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 688 | `_getwch` | `0x6B748` | 44 | UnwindData |  |
| 689 | `_getwch_nolock` | `0x6B774` | 315 | UnwindData |  |
| 690 | `_getwche` | `0x6B8B0` | 44 | UnwindData |  |
| 691 | `_getwche_nolock` | `0x6B8DC` | 79 | UnwindData |  |
| 1176 | `_ungetwch` | `0x6B92C` | 50 | UnwindData |  |
| 1177 | `_ungetwch_nolock` | `0x6B960` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1003 | `_putch` | `0x6B988` | 46 | UnwindData |  |
| 1004 | `_putch_nolock` | `0x6B9B8` | 177 | UnwindData |  |
| 1008 | `_putwch` | `0x6BA6C` | 50 | UnwindData |  |
| 1009 | `_putwch_nolock` | `0x6BAA0` | 89 | UnwindData |  |
| 282 | `?_open@@YAHPEBDHH@Z` | `0x6BAFC` | 52 | UnwindData |  |
| 290 | `?_sopen@@YAHPEBDHHH@Z` | `0x6BB30` | 43 | UnwindData |  |
| 292 | `?_wopen@@YAHPEB_WHH@Z` | `0x6BB5C` | 52 | UnwindData |  |
| 293 | `?_wsopen@@YAHPEB_WHHH@Z` | `0x6BB90` | 43 | UnwindData |  |
| 505 | `_cgets` | `0x6BBBC` | 110 | UnwindData |  |
| 506 | `_cgets_s` | `0x6BC2C` | 302 | UnwindData |  |
| 507 | `_cgetws` | `0x6BD5C` | 90 | UnwindData |  |
| 508 | `_cgetws_s` | `0x6BDB8` | 479 | UnwindData |  |
| 514 | `_chsize` | `0x6BF98` | 21 | UnwindData |  |
| 515 | `_chsize_s` | `0x6C148` | 248 | UnwindData |  |
| 532 | `_cputs` | `0x6C240` | 120 | UnwindData |  |
| 533 | `_cputws` | `0x6C2B8` | 218 | UnwindData |  |
| 534 | `_creat` | `0x6C394` | 55 | UnwindData |  |
| 560 | `_dup` | `0x6C3CC` | 216 | UnwindData |  |
| 561 | `_dup2` | `0x6C654` | 390 | UnwindData |  |
| 568 | `_eof` | `0x6C94C` | 291 | UnwindData |  |
| 590 | `_filelength` | `0x6CA70` | 276 | UnwindData |  |
| 591 | `_filelengthi64` | `0x6CB84` | 287 | UnwindData |  |
| 658 | `_get_fmode` | `0x6CCA4` | 47 | UnwindData |  |
| 1042 | `_set_fmode` | `0x6CCD4` | 61 | UnwindData |  |
| 1053 | `_setmode` | `0x6CD14` | 260 | UnwindData |  |
| 825 | `_locking` | `0x6CEF8` | 291 | UnwindData |  |
| 983 | `_mktemp` | `0x6D138` | 77 | UnwindData |  |
| 984 | `_mktemp_s` | `0x6D188` | 329 | UnwindData |  |
| 1148 | `_tell` | `0x6D2D4` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1149 | `_telli64` | `0x6D2E0` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1249 | `_wcreat` | `0x6D2EC` | 55 | UnwindData |  |
| 1328 | `_wmktemp` | `0x6D324` | 77 | UnwindData |  |
| 1329 | `_wmktemp_s` | `0x6D374` | 336 | UnwindData |  |
| 279 | `?_invalid_parameter@@YAXPEBG00I_K@Z` | `0x6D57C` | 252 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 660 | `_get_invalid_parameter_handler` | `0x6D678` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 713 | `_invalid_parameter` | `0x6D690` | 101 | UnwindData |  |
| 714 | `_invalid_parameter_noinfo` | `0x6D6F8` | 30 | UnwindData |  |
| 715 | `_invalid_parameter_noinfo_noreturn` | `0x6D718` | 47 | UnwindData |  |
| 716 | `_invoke_watson` | `0x6D748` | 59 | UnwindData |  |
| 1043 | `_set_invalid_parameter_handler` | `0x6D784` | 59 | UnwindData |  |
| 665 | `_get_purecall_handler` | `0x6D7C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1002 | `_purecall` | `0x6D7D0` | 52 | UnwindData |  |
| 1047 | `_set_purecall_handler` | `0x6D804` | 59 | UnwindData |  |
| 399 | `__dllonexit` | `0x6D884` | 209 | UnwindData |  |
| 990 | `_onexit` | `0x6D958` | 266 | UnwindData |  |
| 1399 | `atexit` | `0x6DA64` | 23 | UnwindData |  |
| 386 | `__crtCaptureCurrentContext` | `0x6DB30` | 109 | UnwindData |  |
| 387 | `__crtCapturePreviousContext` | `0x6DBA0` | 113 | UnwindData |  |
| 390 | `__crtGetShowWindowMode` | `0x6DC34` | 44 | UnwindData |  |
| 391 | `__crtIsPackagedApp` | `0x6DC60` | 94 | UnwindData |  |
| 394 | `__crtSetUnhandledExceptionFilter` | `0x6DCC0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 395 | `__crtTerminateProcess` | `0x6DCC8` | 31 | UnwindData |  |
| 396 | `__crtUnhandledException` | `0x6DCE8` | 32 | UnwindData |  |
| 1535 | `rand_s` | `0x6DF00` | 314 | UnwindData |  |
| 402 | `__fpecode` | `0x6E03C` | 20 | UnwindData |  |
| 444 | `__pxcptinfoptrs` | `0x6E060` | 20 | UnwindData |  |
| 1533 | `raise` | `0x6E128` | 548 | UnwindData |  |
| 1546 | `signal` | `0x6E34C` | 656 | UnwindData |  |
| 354 | `__C_specific_handler` | `0x6E5DC` | 478 | UnwindData |  |
| 441 | `__pctype_func` | `0x6F0C8` | 59 | UnwindData |  |
| 443 | `__pwctype_func` | `0x6F104` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 350 | `_XcptFilter` | `0x6F10C` | 460 | UnwindData |  |
| 355 | `__CppXcptFilter` | `0x6F2D8` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 562 | `_dupenv_s` | `0x6F2EC` | 258 | UnwindData |  |
| 1460 | `getenv` | `0x6F48C` | 107 | UnwindData |  |
| 1461 | `getenv_s` | `0x6F4F8` | 251 | UnwindData |  |
| 1296 | `_wdupenv_s` | `0x6F6AC` | 258 | UnwindData |  |
| 1323 | `_wgetenv` | `0x6F7B0` | 107 | UnwindData |  |
| 1324 | `_wgetenv_s` | `0x6F8D0` | 252 | UnwindData |  |
| 818 | `_local_unwind` | `0x6FAC0` | 36 | UnwindData |  |
| 366 | `__NLG_Dispatch2` | `0x6FB10` | 1 | UnwindData |  |
| 367 | `__NLG_Return2` | `0x6FB20` | 1 | UnwindData |  |
| 445 | `__report_gsfailure` | `0x6FC08` | 209 | UnwindData |  |
| 374 | `___lc_codepage_func` | `0x6FD8C` | 55 | UnwindData |  |
| 375 | `___lc_collate_cp_func` | `0x6FDC4` | 55 | UnwindData |  |
| 376 | `___lc_locale_name_func` | `0x6FDFC` | 59 | UnwindData |  |
| 377 | `___mb_cur_max_func` | `0x6FE38` | 58 | UnwindData |  |
| 378 | `___mb_cur_max_l_func` | `0x6FE74` | 1,152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 379 | `___setlc_active_func` | `0x702F4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 380 | `___unguarded_readlc_active_add_func` | `0x702FC` | 140 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 385 | `__create_locale` | `0x70388` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 403 | `__free_locale` | `0x70390` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 404 | `__get_current_locale` | `0x70398` | 612 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 520 | `_configthreadlocale` | `0x705FC` | 105 | UnwindData |  |
| 535 | `_create_locale` | `0x70748` | 119 | UnwindData |  |
| 620 | `_free_locale` | `0x70B60` | 154 | UnwindData |  |
| 653 | `_get_current_locale` | `0x70BFC` | 156 | UnwindData |  |
| 1250 | `_wcreate_locale` | `0x70C98` | 255 | UnwindData |  |
| 1348 | `_wsetlocale` | `0x70E00` | 411 | UnwindData |  |
| 392 | `__crtLCMapStringA` | `0x71BA0` | 150 | UnwindData |  |
| 393 | `__crtLCMapStringW` | `0x71C38` | 73 | UnwindData |  |
| 388 | `__crtCompareStringA` | `0x71FCC` | 137 | UnwindData |  |
| 389 | `__crtCompareStringW` | `0x72058` | 165 | UnwindData |  |
| 138 | `??_U@YAPEAX_KHPEBDH@Z` | `0x721C4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `??_V@YAXPEAXHPEBDH@Z` | `0x721CC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 397 | `__crt_debugger_hook` | `0x721D4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1497 | `localeconv` | `0x721DC` | 56 | UnwindData |  |
| 416 | `__lconv_init` | `0x72214` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 451 | `__sys_errlist` | `0x72224` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 452 | `__sys_nerr` | `0x7222C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 464 | `__wcserror` | `0x72234` | 392 | UnwindData |  |
| 465 | `__wcserror_s` | `0x723BC` | 238 | UnwindData |  |
| 1388 | `abs` | `0x724AC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1492 | `labs` | `0x724AC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 482 | `_assert` | `0x724B4` | 2,262 | UnwindData |  |
| 497 | `_byteswap_uint64` | `0x72D8C` | 116 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 498 | `_byteswap_ulong` | `0x72E00` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 499 | `_byteswap_ushort` | `0x72E28` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 815 | `_lfind` | `0x72E38` | 151 | UnwindData |  |
| 816 | `_lfind_s` | `0x72ED0` | 156 | UnwindData |  |
| 828 | `_lrotl` | `0x72F6C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1019 | `_rotl` | `0x72F6C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1020 | `_rotl64` | `0x72F78` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 829 | `_lrotr` | `0x72F84` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1021 | `_rotr` | `0x72F84` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1022 | `_rotr64` | `0x72F90` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 830 | `_lsearch` | `0x72F9C` | 160 | UnwindData |  |
| 831 | `_lsearch_s` | `0x7303C` | 165 | UnwindData |  |
| 838 | `_makepath` | `0x730E4` | 39 | UnwindData |  |
| 839 | `_makepath_s` | `0x7310C` | 328 | UnwindData |  |
| 1005 | `_putenv` | `0x73254` | 50 | UnwindData |  |
| 1006 | `_putenv_s` | `0x73500` | 117 | UnwindData |  |
| 1035 | `_searchenv` | `0x73578` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1036 | `_searchenv_s` | `0x73584` | 814 | UnwindData |  |
| 1037 | `_set_abort_behavior` | `0x738B4` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1387 | `abort` | `0x738D0` | 85 | UnwindData |  |
| 1049 | `_setjmp` | `0x73940` | 160 | UnwindData |  |
| 1543 | `setjmp` | `0x73940` | 160 | UnwindData |  |
| 1050 | `_setjmpex` | `0x739F0` | 144 | UnwindData |  |
| 1084 | `_splitpath` | `0x73A80` | 136 | UnwindData |  |
| 1085 | `_splitpath_s` | `0x73D98` | 671 | UnwindData |  |
| 1101 | `_strerror` | `0x74038` | 341 | UnwindData |  |
| 1102 | `_strerror_s` | `0x74190` | 228 | UnwindData |  |
| 1170 | `_umask` | `0x74274` | 34 | UnwindData |  |
| 1171 | `_umask_s` | `0x74298` | 67 | UnwindData |  |
| 1245 | `_wassert` | `0x742DC` | 2,384 | UnwindData |  |
| 1253 | `_wcserror` | `0x74C50` | 166 | UnwindData |  |
| 1254 | `_wcserror_s` | `0x74CF8` | 173 | UnwindData |  |
| 1325 | `_wmakepath` | `0x74DA8` | 39 | UnwindData |  |
| 1326 | `_wmakepath_s` | `0x74DD0` | 341 | UnwindData |  |
| 1331 | `_wperror` | `0x74F28` | 391 | UnwindData |  |
| 1338 | `_wputenv` | `0x750B0` | 50 | UnwindData |  |
| 1339 | `_wputenv_s` | `0x75398` | 117 | UnwindData |  |
| 1346 | `_wsearchenv` | `0x75410` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1347 | `_wsearchenv_s` | `0x7541C` | 834 | UnwindData |  |
| 1359 | `_wsplitpath` | `0x75760` | 136 | UnwindData |  |
| 1360 | `_wsplitpath_s` | `0x75A7C` | 688 | UnwindData |  |
| 1403 | `bsearch` | `0x75D2C` | 240 | UnwindData |  |
| 1404 | `bsearch_s` | `0x75E1C` | 250 | UnwindData |  |
| 1416 | `div` | `0x75F18` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1494 | `ldiv` | `0x75F18` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 469 | `_abs64` | `0x75F30` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1495 | `llabs` | `0x75F30` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1496 | `lldiv` | `0x75F3C` | 36 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1502 | `longjmp` | `0x75F60` | 236 | UnwindData |  |
| 1521 | `perror` | `0x7604C` | 186 | UnwindData |  |
| 1531 | `qsort` | `0x76110` | 80 | UnwindData |  |
| 1532 | `qsort_s` | `0x764C0` | 80 | UnwindData |  |
| 1534 | `rand` | `0x768D0` | 43 | UnwindData |  |
| 1555 | `srand` | `0x768FC` | 22 | UnwindData |  |
| 1544 | `setlocale` | `0x76914` | 623 | UnwindData |  |
| 1566 | `strerror` | `0x76B84` | 154 | UnwindData |  |
| 1567 | `strerror_s` | `0x76C20` | 142 | UnwindData |  |
| 372 | `__STRINGTOLD_L` | `0x7A9F4` | 117 | UnwindData |  |
| 1 | `$I10_OUTPUT` | `0x7CB5C` | 2,764 | UnwindData |  |
| 501 | `_cabs` | `0x7D860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 511 | `_chgsign` | `0x7D870` | 36 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 512 | `_chgsignf` | `0x7D894` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 516 | `_clearfp` | `0x7D8B0` | 80 | UnwindData |  |
| 521 | `_control87` | `0x7D900` | 656 | UnwindData |  |
| 522 | `_controlfp` | `0x7DB90` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 610 | `_fpreset` | `0x7DB9C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1038 | `_set_controlfp` | `0x7DBA8` | 52 | UnwindData |  |
| 1096 | `_statusfp` | `0x7DBDC` | 68 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 523 | `_controlfp_s` | `0x7DC20` | 99 | UnwindData |  |
| 524 | `_copysign` | `0x7DC84` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 525 | `_copysignf` | `0x7DCBC` | 44 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 602 | `_finite` | `0x7DCE8` | 44 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 603 | `_finitef` | `0x7DD14` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 607 | `_fpclass` | `0x7DD2C` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 608 | `_fpclassf` | `0x7DDDC` | 120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 786 | `_isnan` | `0x7DE54` | 44 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 787 | `_isnanf` | `0x7DE80` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 988 | `_nextafter` | `0x7DE9C` | 484 | UnwindData |  |
| 989 | `_nextafterf` | `0x7E080` | 393 | UnwindData |  |
| 1023 | `_scalb` | `0x7E20C` | 473 | UnwindData |  |
| 1024 | `_scalbf` | `0x7E3E8` | 414 | UnwindData |  |
| 609 | `_fpieee_flt` | `0x7E588` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 704 | `_hypot` | `0x7E5A4` | 610 | UnwindData |  |
| 705 | `_hypotf` | `0x7E808` | 326 | UnwindData |  |
| 811 | `_j0` | `0x7E950` | 571 | UnwindData |  |
| 812 | `_j1` | `0x7EB8C` | 614 | UnwindData |  |
| 813 | `_jn` | `0x7EDF4` | 382 | UnwindData |  |
| 1384 | `_y0` | `0x7EF74` | 632 | UnwindData |  |
| 1385 | `_y1` | `0x7F1EC` | 657 | UnwindData |  |
| 1386 | `_yn` | `0x7F480` | 221 | UnwindData |  |
| 826 | `_logb` | `0x7F5B0` | 285 | UnwindData |  |
| 827 | `_logbf` | `0x7F6D0` | 229 | UnwindData |  |
| 1389 | `acos` | `0x7F7B8` | 742 | UnwindData |  |
| 1390 | `acosf` | `0x7FAA0` | 652 | UnwindData |  |
| 1393 | `asin` | `0x7FD2C` | 711 | UnwindData |  |
| 1394 | `asinf` | `0x7FFF4` | 596 | UnwindData |  |
| 1395 | `atan` | `0x80248` | 606 | UnwindData |  |
| 1396 | `atan2` | `0x804A8` | 1,968 | UnwindData |  |
| 1397 | `atan2f` | `0x80C58` | 1,158 | UnwindData |  |
| 1398 | `atanf` | `0x810E0` | 576 | UnwindData |  |
| 1407 | `ceil` | `0x81320` | 273 | UnwindData |  |
| 1408 | `ceilf` | `0x81434` | 212 | UnwindData |  |
| 1412 | `cos` | `0x81510` | 1,165 | UnwindData |  |
| 1413 | `cosf` | `0x819A0` | 768 | UnwindData |  |
| 1414 | `cosh` | `0x81CA0` | 938 | UnwindData |  |
| 1415 | `coshf` | `0x82174` | 705 | UnwindData |  |
| 1418 | `exp` | `0x82560` | 664 | UnwindData |  |
| 1419 | `expf` | `0x82800` | 344 | UnwindData |  |
| 1420 | `fabs` | `0x82958` | 225 | UnwindData |  |
| 1430 | `floor` | `0x82A3C` | 255 | UnwindData |  |
| 1431 | `floorf` | `0x82B3C` | 206 | UnwindData |  |
| 1432 | `fmod` | `0x82C0C` | 1,340 | UnwindData |  |
| 1433 | `fmodf` | `0x83148` | 713 | UnwindData |  |
| 1447 | `frexp` | `0x83414` | 220 | UnwindData |  |
| 1493 | `ldexp` | `0x834F0` | 377 | UnwindData |  |
| 1498 | `log` | `0x83670` | 702 | UnwindData |  |
| 1499 | `log10` | `0x83930` | 798 | UnwindData |  |
| 1500 | `log10f` | `0x83C50` | 645 | UnwindData |  |
| 1501 | `logf` | `0x83EE0` | 597 | UnwindData |  |
| 1519 | `modf` | `0x84138` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1520 | `modff` | `0x841F8` | 152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1522 | `pow` | `0x84290` | 2,993 | UnwindData |  |
| 1523 | `powf` | `0x84E50` | 2,093 | UnwindData |  |
| 1547 | `sin` | `0x85680` | 1,165 | UnwindData |  |
| 1548 | `sinf` | `0x85B10` | 893 | UnwindData |  |
| 1549 | `sinh` | `0x85E90` | 1,015 | UnwindData |  |
| 1550 | `sinhf` | `0x863B0` | 726 | UnwindData |  |
| 1553 | `sqrt` | `0x867B0` | 256 | UnwindData |  |
| 1554 | `sqrtf` | `0x868B0` | 220 | UnwindData |  |
| 1590 | `tan` | `0x8698C` | 714 | UnwindData |  |
| 1591 | `tanf` | `0x87098` | 871 | UnwindData |  |
| 1592 | `tanh` | `0x87528` | 722 | UnwindData |  |
| 1593 | `tanhf` | `0x877FC` | 725 | UnwindData |  |
| 130 | `??_7exception@std@@6B@` | `0x93820` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `??_7bad_cast@std@@6B@` | `0x93850` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `??_7bad_typeid@std@@6B@` | `0x93868` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `??_7__non_rtti_object@std@@6B@` | `0x93880` | 5,776 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1295 | `_wctype` | `0x94F10` | 2,912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1146 | `_sys_errlist` | `0x95A70` | 158,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 717 | `_iob` | `0xBC5A0` | 1,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1153 | `_timezone` | `0xBC9E0` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 555 | `_daylight` | `0xBC9E4` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 559 | `_dstbias` | `0xBC9E8` | 136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1160 | `_tzname` | `0xBCA70` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 866 | `_mbctype` | `0xBCBA0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 845 | `_mbcasemap` | `0xBCCB0` | 1,904 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 383 | `__badioinfo` | `0xBD420` | 408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 994 | `_pctype` | `0xBD5B8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1011 | `_pwctype` | `0xBD5C0` | 1,096 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 417 | `__mb_cur_max` | `0xBDA08` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 415 | `__lconv` | `0xBDA28` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1147 | `_sys_nerr` | `0xBDAC8` | 968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 339 | `_HUGE` | `0xBDE90` | 9,348 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 381 | `__argc` | `0xC0314` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 382 | `__argv` | `0xC0318` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 463 | `__wargv` | `0xC0320` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 567 | `_environ` | `0xC0328` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1297 | `_wenviron` | `0xC0330` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 995 | `_pgmptr` | `0xC0338` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1332 | `_wpgmptr` | `0xC0340` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 468 | `__winitenv` | `0xC0358` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 408 | `__initenv` | `0xC0360` | 1,624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 472 | `_acmdln` | `0xC09B8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1248 | `_wcmdln` | `0xC09C0` | 2,452 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 519 | `_commode` | `0xC1354` | 588 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 606 | `_fmode` | `0xC15A0` | 6,272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 442 | `__pioinfo` | `0xC2E20` | 516 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 461 | `__unguarded_readlc_active` | `0xC3024` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 447 | `__setlc_active` | `0xC3028` | 0 | Indeterminate |  |
