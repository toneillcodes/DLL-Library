# Binary Specification: msvcr110.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\msvcr110.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ae996edb9b050677c4f82d56092efdc75f0addc97a14e2c46753e2db3f6bd732`
* **Total Exported Functions:** 1671

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
| 637 | `_freea` | `0x4C7C` | 31 | UnwindData |  |
| 638 | `_freea_s` | `0x4C7C` | 31 | UnwindData |  |
| 162 | `?GetSharedTimerQueue@details@Concurrency@@YAPEAXXZ` | `0x4CE8` | 200 | UnwindData |  |
| 9 | `??0_Condition_variable@details@Concurrency@@QEAA@XZ` | `0x505C` | 44 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `??1_Condition_variable@details@Concurrency@@QEAA@XZ` | `0x5088` | 58 | UnwindData |  |
| 324 | `?wait@_Condition_variable@details@Concurrency@@QEAAXAEAVcritical_section@3@@Z` | `0x50C4` | 137 | UnwindData |  |
| 326 | `?wait_for@_Condition_variable@details@Concurrency@@QEAA_NAEAVcritical_section@3@I@Z` | `0x5150` | 417 | UnwindData |  |
| 304 | `?notify_one@_Condition_variable@details@Concurrency@@QEAAXXZ` | `0x52F4` | 173 | UnwindData |  |
| 303 | `?notify_all@_Condition_variable@details@Concurrency@@QEAAXXZ` | `0x53A4` | 127 | UnwindData |  |
| 43 | `??0event@Concurrency@@QEAA@XZ` | `0x5424` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `??1event@Concurrency@@QEAA@XZ` | `0x5454` | 139 | UnwindData |  |
| 325 | `?wait@event@Concurrency@@QEAA_KI@Z` | `0x54E0` | 329 | UnwindData |  |
| 306 | `?reset@event@Concurrency@@QEAAXXZ` | `0x562C` | 135 | UnwindData |  |
| 307 | `?set@event@Concurrency@@QEAAXXZ` | `0x56B4` | 487 | UnwindData |  |
| 327 | `?wait_for_multiple@event@Concurrency@@SA_KPEAPEAV12@_K_NI@Z` | `0x589C` | 1,060 | UnwindData |  |
| 82 | `??0scheduler_resource_allocation_error@Concurrency@@QEAA@PEBDJ@Z` | `0x638C` | 58 | UnwindData |  |
| 81 | `??0scheduler_resource_allocation_error@Concurrency@@QEAA@J@Z` | `0x63C8` | 47 | UnwindData |  |
| 297 | `?get_error_code@scheduler_resource_allocation_error@Concurrency@@QEBAJXZ` | `0x63F8` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `??0scheduler_worker_creation_error@Concurrency@@QEAA@PEBDJ@Z` | `0x63FC` | 33 | UnwindData |  |
| 83 | `??0scheduler_worker_creation_error@Concurrency@@QEAA@J@Z` | `0x6420` | 33 | UnwindData |  |
| 90 | `??0unsupported_os@Concurrency@@QEAA@PEBD@Z` | `0x6444` | 42 | UnwindData |  |
| 91 | `??0unsupported_os@Concurrency@@QEAA@XZ` | `0x6470` | 33 | UnwindData |  |
| 79 | `??0scheduler_not_attached@Concurrency@@QEAA@PEBD@Z` | `0x6494` | 42 | UnwindData |  |
| 80 | `??0scheduler_not_attached@Concurrency@@QEAA@XZ` | `0x64C0` | 33 | UnwindData |  |
| 50 | `??0improper_scheduler_attach@Concurrency@@QEAA@PEBD@Z` | `0x64E4` | 42 | UnwindData |  |
| 51 | `??0improper_scheduler_attach@Concurrency@@QEAA@XZ` | `0x6510` | 33 | UnwindData |  |
| 52 | `??0improper_scheduler_detach@Concurrency@@QEAA@PEBD@Z` | `0x6534` | 42 | UnwindData |  |
| 53 | `??0improper_scheduler_detach@Concurrency@@QEAA@XZ` | `0x6560` | 33 | UnwindData |  |
| 54 | `??0improper_scheduler_reference@Concurrency@@QEAA@PEBD@Z` | `0x6584` | 42 | UnwindData |  |
| 55 | `??0improper_scheduler_reference@Concurrency@@QEAA@XZ` | `0x65B0` | 33 | UnwindData |  |
| 41 | `??0default_scheduler_exists@Concurrency@@QEAA@PEBD@Z` | `0x65D4` | 42 | UnwindData |  |
| 42 | `??0default_scheduler_exists@Concurrency@@QEAA@XZ` | `0x6600` | 33 | UnwindData |  |
| 38 | `??0context_unblock_unbalanced@Concurrency@@QEAA@PEBD@Z` | `0x6624` | 42 | UnwindData |  |
| 39 | `??0context_unblock_unbalanced@Concurrency@@QEAA@XZ` | `0x6650` | 33 | UnwindData |  |
| 36 | `??0context_self_unblock@Concurrency@@QEAA@PEBD@Z` | `0x6674` | 42 | UnwindData |  |
| 37 | `??0context_self_unblock@Concurrency@@QEAA@XZ` | `0x66A0` | 33 | UnwindData |  |
| 72 | `??0missing_wait@Concurrency@@QEAA@PEBD@Z` | `0x66C4` | 42 | UnwindData |  |
| 73 | `??0missing_wait@Concurrency@@QEAA@XZ` | `0x66F0` | 33 | UnwindData |  |
| 32 | `??0bad_target@Concurrency@@QEAA@PEBD@Z` | `0x6714` | 42 | UnwindData |  |
| 33 | `??0bad_target@Concurrency@@QEAA@XZ` | `0x6740` | 33 | UnwindData |  |
| 70 | `??0message_not_found@Concurrency@@QEAA@PEBD@Z` | `0x6764` | 42 | UnwindData |  |
| 71 | `??0message_not_found@Concurrency@@QEAA@XZ` | `0x6790` | 33 | UnwindData |  |
| 56 | `??0invalid_link_target@Concurrency@@QEAA@PEBD@Z` | `0x67B4` | 42 | UnwindData |  |
| 57 | `??0invalid_link_target@Concurrency@@QEAA@XZ` | `0x67E0` | 33 | UnwindData |  |
| 64 | `??0invalid_scheduler_policy_key@Concurrency@@QEAA@PEBD@Z` | `0x6804` | 42 | UnwindData |  |
| 65 | `??0invalid_scheduler_policy_key@Concurrency@@QEAA@XZ` | `0x6830` | 33 | UnwindData |  |
| 68 | `??0invalid_scheduler_policy_value@Concurrency@@QEAA@PEBD@Z` | `0x6854` | 42 | UnwindData |  |
| 69 | `??0invalid_scheduler_policy_value@Concurrency@@QEAA@XZ` | `0x6880` | 33 | UnwindData |  |
| 66 | `??0invalid_scheduler_policy_thread_specification@Concurrency@@QEAA@PEBD@Z` | `0x68A4` | 42 | UnwindData |  |
| 67 | `??0invalid_scheduler_policy_thread_specification@Concurrency@@QEAA@XZ` | `0x68D0` | 33 | UnwindData |  |
| 60 | `??0invalid_operation@Concurrency@@QEAA@PEBD@Z` | `0x68F4` | 42 | UnwindData |  |
| 61 | `??0invalid_operation@Concurrency@@QEAA@XZ` | `0x6920` | 33 | UnwindData |  |
| 74 | `??0nested_scheduler_missing_detach@Concurrency@@QEAA@PEBD@Z` | `0x6944` | 42 | UnwindData |  |
| 75 | `??0nested_scheduler_missing_detach@Concurrency@@QEAA@XZ` | `0x6970` | 33 | UnwindData |  |
| 76 | `??0operation_timed_out@Concurrency@@QEAA@PEBD@Z` | `0x6994` | 42 | UnwindData |  |
| 77 | `??0operation_timed_out@Concurrency@@QEAA@XZ` | `0x69C0` | 33 | UnwindData |  |
| 58 | `??0invalid_multiple_scheduling@Concurrency@@QEAA@PEBD@Z` | `0x69E4` | 42 | UnwindData |  |
| 59 | `??0invalid_multiple_scheduling@Concurrency@@QEAA@XZ` | `0x6A10` | 33 | UnwindData |  |
| 62 | `??0invalid_oversubscribe_operation@Concurrency@@QEAA@PEBD@Z` | `0x6A34` | 42 | UnwindData |  |
| 63 | `??0invalid_oversubscribe_operation@Concurrency@@QEAA@XZ` | `0x6A60` | 33 | UnwindData |  |
| 48 | `??0improper_lock@Concurrency@@QEAA@PEBD@Z` | `0x6A84` | 42 | UnwindData |  |
| 49 | `??0improper_lock@Concurrency@@QEAA@XZ` | `0x6AB0` | 33 | UnwindData |  |
| 88 | `??0task_canceled@Concurrency@@QEAA@PEBD@Z` | `0x6AD4` | 42 | UnwindData |  |
| 89 | `??0task_canceled@Concurrency@@QEAA@XZ` | `0x6B00` | 33 | UnwindData |  |
| 11 | `??0_Interruption_exception@details@Concurrency@@QEAA@PEBD@Z` | `0x6B24` | 42 | UnwindData |  |
| 12 | `??0_Interruption_exception@details@Concurrency@@QEAA@XZ` | `0x6B50` | 33 | UnwindData |  |
| 150 | `?DisableTracing@Concurrency@@YAJXZ` | `0x72AC` | 10,760 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | `?EnableTracing@Concurrency@@YAJXZ` | `0x72AC` | 10,760 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 329 | `_CRT_RTC_INIT` | `0x72AC` | 10,760 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 330 | `_CRT_RTC_INITW` | `0x72AC` | 10,760 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 296 | `?from_numa_node@location@Concurrency@@SA?AV12@G@Z` | `0x9CB4` | 153 | UnwindData |  |
| 295 | `?current@location@Concurrency@@SA?AV12@XZ` | `0x9D9C` | 134 | UnwindData |  |
| 197 | `?_Current_node@location@Concurrency@@SA?AV12@XZ` | `0x9E24` | 131 | UnwindData |  |
| 265 | `?_Value@_SpinCount@details@Concurrency@@SAIXZ` | `0xA8CC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `??0_NonReentrantBlockingLock@details@Concurrency@@QEAA@XZ` | `0xA8D4` | 30 | UnwindData |  |
| 16 | `??0_ReentrantBlockingLock@details@Concurrency@@QEAA@XZ` | `0xA8D4` | 30 | UnwindData |  |
| 96 | `??1_NonReentrantBlockingLock@details@Concurrency@@QEAA@XZ` | `0xA8F4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `??1_ReentrantBlockingLock@details@Concurrency@@QEAA@XZ` | `0xA8F4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 180 | `?_Acquire@_NonReentrantBlockingLock@details@Concurrency@@QEAAXXZ` | `0xA8FC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 182 | `?_Acquire@_ReentrantBlockingLock@details@Concurrency@@QEAAXXZ` | `0xA8FC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 255 | `?_TryAcquire@_NonReentrantBlockingLock@details@Concurrency@@QEAA_NXZ` | `0xA904` | 20 | UnwindData |  |
| 256 | `?_TryAcquire@_ReentrantBlockingLock@details@Concurrency@@QEAA_NXZ` | `0xA904` | 20 | UnwindData |  |
| 224 | `?_Release@_NonReentrantBlockingLock@details@Concurrency@@QEAAXXZ` | `0xA918` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 226 | `?_Release@_ReentrantBlockingLock@details@Concurrency@@QEAAXXZ` | `0xA918` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `??0_ReentrantLock@details@Concurrency@@QEAA@XZ` | `0xA920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `?_Acquire@_ReentrantLock@details@Concurrency@@QEAAXXZ` | `0xA930` | 85 | UnwindData |  |
| 257 | `?_TryAcquire@_ReentrantLock@details@Concurrency@@QEAA_NXZ` | `0xA988` | 45 | UnwindData |  |
| 227 | `?_Release@_ReentrantLock@details@Concurrency@@QEAAXXZ` | `0xA9B8` | 48 | UnwindData |  |
| 14 | `??0_NonReentrantPPLLock@details@Concurrency@@QEAA@XZ` | `0xA9E8` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `??0critical_section@Concurrency@@QEAA@XZ` | `0xA9E8` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `?_Acquire@_NonReentrantPPLLock@details@Concurrency@@QEAAXPEAX@Z` | `0xAA10` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 225 | `?_Release@_NonReentrantPPLLock@details@Concurrency@@QEAAXXZ` | `0xAA18` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `??0_ReentrantPPLLock@details@Concurrency@@QEAA@XZ` | `0xAA20` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | `?_Acquire@_ReentrantPPLLock@details@Concurrency@@QEAAXPEAX@Z` | `0xAA50` | 83 | UnwindData |  |
| 228 | `?_Release@_ReentrantPPLLock@details@Concurrency@@QEAAXXZ` | `0xAAA4` | 26 | UnwindData |  |
| 15 | `??0_ReaderWriterLock@details@Concurrency@@QEAA@XZ` | `0xAAC0` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `?_AcquireRead@_ReaderWriterLock@details@Concurrency@@QEAAXXZ` | `0xAAD4` | 56 | UnwindData |  |
| 230 | `?_ReleaseRead@_ReaderWriterLock@details@Concurrency@@QEAAXXZ` | `0xAB0C` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `?_AcquireWrite@_ReaderWriterLock@details@Concurrency@@QEAAXXZ` | `0xAB10` | 55 | UnwindData |  |
| 231 | `?_ReleaseWrite@_ReaderWriterLock@details@Concurrency@@QEAAXXZ` | `0xAB48` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 258 | `?_TryAcquireWrite@_ReaderWriterLock@details@Concurrency@@QEAA_NXZ` | `0xAB54` | 808 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `??0_Scoped_lock@_NonReentrantPPLLock@details@Concurrency@@QEAA@AEAV123@@Z` | `0xAE7C` | 102 | UnwindData |  |
| 98 | `??1_Scoped_lock@_NonReentrantPPLLock@details@Concurrency@@QEAA@XZ` | `0xAEE4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `??1scoped_lock@critical_section@Concurrency@@QEAA@XZ` | `0xAEE4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `??0_Scoped_lock@_ReentrantPPLLock@details@Concurrency@@QEAA@AEAV123@@Z` | `0xAEEC` | 99 | UnwindData |  |
| 99 | `??1_Scoped_lock@_ReentrantPPLLock@details@Concurrency@@QEAA@XZ` | `0xAF50` | 29 | UnwindData |  |
| 302 | `?native_handle@critical_section@Concurrency@@QEAAAEAV12@XZ` | `0xAF70` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 298 | `?lock@critical_section@Concurrency@@QEAAXXZ` | `0xAF74` | 82 | UnwindData |  |
| 316 | `?try_lock@critical_section@Concurrency@@QEAA_NXZ` | `0xAFC8` | 194 | UnwindData |  |
| 318 | `?try_lock_for@critical_section@Concurrency@@QEAA_NI@Z` | `0xB08C` | 172 | UnwindData |  |
| 321 | `?unlock@critical_section@Concurrency@@QEAAXXZ` | `0xB138` | 276 | UnwindData |  |
| 85 | `??0scoped_lock@critical_section@Concurrency@@QEAA@AEAV12@@Z` | `0xB4F0` | 102 | UnwindData |  |
| 78 | `??0reader_writer_lock@Concurrency@@QEAA@XZ` | `0xB558` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 299 | `?lock@reader_writer_lock@Concurrency@@QEAAXXZ` | `0xB588` | 82 | UnwindData |  |
| 317 | `?try_lock@reader_writer_lock@Concurrency@@QEAA_NXZ` | `0xB5DC` | 220 | UnwindData |  |
| 300 | `?lock_read@reader_writer_lock@Concurrency@@QEAAXXZ` | `0xB6B8` | 329 | UnwindData |  |
| 319 | `?try_lock_read@reader_writer_lock@Concurrency@@QEAA_NXZ` | `0xB804` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 322 | `?unlock@reader_writer_lock@Concurrency@@QEAAXXZ` | `0xB820` | 81 | UnwindData |  |
| 86 | `??0scoped_lock@reader_writer_lock@Concurrency@@QEAA@AEAV12@@Z` | `0xBC04` | 102 | UnwindData |  |
| 111 | `??1scoped_lock@reader_writer_lock@Concurrency@@QEAA@XZ` | `0xBC6C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `??1scoped_lock_read@reader_writer_lock@Concurrency@@QEAA@XZ` | `0xBC6C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `??0scoped_lock_read@reader_writer_lock@Concurrency@@QEAA@AEAV12@@Z` | `0xBC74` | 29 | UnwindData |  |
| 156 | `?GetOSVersion@Concurrency@@YA?AW4OSVersion@IResourceManager@1@XZ` | `0xBE6C` | 128 | UnwindData |  |
| 145 | `?CreateResourceManager@Concurrency@@YAPEAUIResourceManager@1@XZ` | `0xBEEC` | 265 | UnwindData |  |
| 159 | `?GetProcessorCount@Concurrency@@YAIXZ` | `0xBFF8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 205 | `?_GetConcurrency@details@Concurrency@@YAIXZ` | `0xBFF8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 160 | `?GetProcessorNodeCount@Concurrency@@YAIXZ` | `0xC000` | 130 | UnwindData |  |
| 161 | `?GetSchedulerId@Concurrency@@YAIXZ` | `0xC084` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `?GetExecutionContextId@Concurrency@@YAIXZ` | `0xC094` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 310 | `?set_task_execution_resources@Concurrency@@YAX_K@Z` | `0xC0A4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 309 | `?set_task_execution_resources@Concurrency@@YAXGPEAU_GROUP_AFFINITY@@@Z` | `0xC0AC` | 27,124 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `?Create@Scheduler@Concurrency@@SAPEAV12@AEBVSchedulerPolicy@2@@Z` | `0x12AA0` | 40 | UnwindData |  |
| 175 | `?SetDefaultSchedulerPolicy@Scheduler@Concurrency@@SAXAEBVSchedulerPolicy@2@@Z` | `0x12AC8` | 248 | UnwindData |  |
| 170 | `?ResetDefaultSchedulerPolicy@Scheduler@Concurrency@@SAXXZ` | `0x12BC0` | 114 | UnwindData |  |
| 229 | `?_Release@_Scheduler@details@Concurrency@@QEAAIXZ` | `0x16AD4` | 584 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `??0SchedulerPolicy@Concurrency@@QEAA@XZ` | `0x16D1C` | 28 | UnwindData |  |
| 6 | `??0SchedulerPolicy@Concurrency@@QEAA@_KZZ` | `0x16D38` | 49 | UnwindData |  |
| 4 | `??0SchedulerPolicy@Concurrency@@QEAA@AEBV01@@Z` | `0x16F84` | 121 | UnwindData |  |
| 120 | `??4SchedulerPolicy@Concurrency@@QEAAAEAV01@AEBV01@@Z` | `0x17000` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `??1SchedulerPolicy@Concurrency@@QEAA@XZ` | `0x17050` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 158 | `?GetPolicyValue@SchedulerPolicy@Concurrency@@QEBAIW4PolicyElementKey@2@@Z` | `0x17058` | 75 | UnwindData |  |
| 176 | `?SetPolicyValue@SchedulerPolicy@Concurrency@@QEAAIW4PolicyElementKey@2@I@Z` | `0x170A4` | 202 | UnwindData |  |
| 174 | `?SetConcurrencyLimits@SchedulerPolicy@Concurrency@@QEAAXII@Z` | `0x17170` | 178 | UnwindData |  |
| 141 | `?Alloc@Concurrency@@YAPEAX_K@Z` | `0x1B7D0` | 142 | UnwindData |  |
| 152 | `?Free@Concurrency@@YAXPEAX@Z` | `0x1B860` | 68 | UnwindData |  |
| 23 | `??0_StructuredTaskCollection@details@Concurrency@@QEAA@PEAV_CancellationTokenState@12@@Z` | `0x1BC00` | 214 | UnwindData |  |
| 238 | `?_Schedule@_StructuredTaskCollection@details@Concurrency@@QEAAXPEAV_UnrealizedChore@23@PEAVlocation@3@@Z` | `0x1BCE0` | 152 | UnwindData |  |
| 237 | `?_Schedule@_StructuredTaskCollection@details@Concurrency@@QEAAXPEAV_UnrealizedChore@23@@Z` | `0x1BD9C` | 136 | UnwindData |  |
| 235 | `?_RunAndWait@_StructuredTaskCollection@details@Concurrency@@QEAA?AW4_TaskCollectionStatus@23@PEAV_UnrealizedChore@23@@Z` | `0x1BE24` | 732 | UnwindData |  |
| 191 | `?_CleanupToken@_StructuredTaskCollection@details@Concurrency@@AEAAXXZ` | `0x1C100` | 82 | UnwindData |  |
| 179 | `?_Abort@_StructuredTaskCollection@details@Concurrency@@AEAAXXZ` | `0x1C154` | 239 | UnwindData |  |
| 188 | `?_Cancel@_StructuredTaskCollection@details@Concurrency@@QEAAXXZ` | `0x1C244` | 224 | UnwindData |  |
| 211 | `?_IsCanceling@_StructuredTaskCollection@details@Concurrency@@QEAA_NXZ` | `0x1C324` | 204 | UnwindData |  |
| 25 | `??0_TaskCollection@details@Concurrency@@QEAA@XZ` | `0x1C514` | 361 | UnwindData |  |
| 24 | `??0_TaskCollection@details@Concurrency@@QEAA@PEAV_CancellationTokenState@12@@Z` | `0x1C680` | 374 | UnwindData |  |
| 101 | `??1_TaskCollection@details@Concurrency@@QEAA@XZ` | `0x1C8A0` | 255 | UnwindData |  |
| 240 | `?_Schedule@_TaskCollection@details@Concurrency@@QEAAXPEAV_UnrealizedChore@23@PEAVlocation@3@@Z` | `0x1CF40` | 295 | UnwindData |  |
| 239 | `?_Schedule@_TaskCollection@details@Concurrency@@QEAAXPEAV_UnrealizedChore@23@@Z` | `0x1D068` | 275 | UnwindData |  |
| 189 | `?_Cancel@_TaskCollection@details@Concurrency@@QEAAXXZ` | `0x1D2B0` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 236 | `?_RunAndWait@_TaskCollection@details@Concurrency@@QEAA?AW4_TaskCollectionStatus@23@PEAV_UnrealizedChore@23@@Z` | `0x1D2C4` | 1,137 | UnwindData |  |
| 212 | `?_IsCanceling@_TaskCollection@details@Concurrency@@QEAA_NXZ` | `0x1DBA4` | 235 | UnwindData |  |
| 216 | `?_NewCollection@_AsyncTaskCollection@details@Concurrency@@SAPEAV123@PEAV_CancellationTokenState@23@@Z` | `0x1DD3C` | 134 | UnwindData |  |
| 232 | `?_ReportUnobservedException@details@Concurrency@@YAXXZ` | `0x1DE28` | 84 | UnwindData |  |
| 244 | `?_SetUnobservedExceptionHandler@details@Concurrency@@YAXP6AXXZ@Z` | `0x1DE7C` | 3,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `??0_Timer@details@Concurrency@@IEAA@I_N@Z` | `0x1EB5C` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 250 | `?_Start@_Timer@details@Concurrency@@IEAAXXZ` | `0x1EB78` | 170 | UnwindData |  |
| 102 | `??1_Timer@details@Concurrency@@MEAA@XZ` | `0x1EC24` | 31 | UnwindData |  |
| 251 | `?_Stop@_Timer@details@Concurrency@@IEAAXXZ` | `0x1EC44` | 41 | UnwindData |  |
| 323 | `?wait@Concurrency@@YAXI@Z` | `0x1EC70` | 186 | UnwindData |  |
| 204 | `?_GetConcRTTraceInfo@Concurrency@@YAPEBU_CONCRT_TRACE_INFO@details@1@XZ` | `0x1F0C0` | 31 | UnwindData |  |
| 254 | `?_Trace_ppl_function@Concurrency@@YAXAEBU_GUID@@EW4ConcRT_EventType@1@@Z` | `0x1F0E0` | 194 | UnwindData |  |
| 253 | `?_Trace_agents@Concurrency@@YAXW4Agents_EventType@1@_JZZ` | `0x1F1A4` | 300 | UnwindData |  |
| 261 | `?_UnderlyingYield@details@Concurrency@@YAXXZ` | `0x1F9D0` | 62 | UnwindData |  |
| 192 | `?_ConcRT_CoreAssert@details@Concurrency@@YAXPEBD0H@Z` | `0x1FA68` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 193 | `?_ConcRT_Trace@details@Concurrency@@YAXHPEB_WZZ` | `0x1FA70` | 207 | UnwindData |  |
| 22 | `??0_SpinLock@details@Concurrency@@QEAA@AECJ@Z` | `0x1FB40` | 81 | UnwindData |  |
| 100 | `??1_SpinLock@details@Concurrency@@QEAA@XZ` | `0x1FB94` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 167 | `?Log2@details@Concurrency@@YAK_K@Z` | `0x1FB9C` | 6,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 341 | `_Lock_shared_ptr_spin_lock` | `0x21384` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 345 | `_Unlock_shared_ptr_spin_lock` | `0x21394` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 283 | `?_query_new_handler@@YAP6AH_K@ZXZ` | `0x213A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 285 | `?_set_new_handler@@YAP6AH_K@ZH@Z` | `0x213B0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 286 | `?_set_new_handler@@YAP6AH_K@ZP6AH0@Z@Z` | `0x213B8` | 79 | UnwindData |  |
| 518 | `_callnewh` | `0x21408` | 51 | UnwindData |  |
| 308 | `?set_new_handler@@YAP6AXXZP6AXXZ@Z` | `0x21444` | 18 | UnwindData |  |
| 284 | `?_query_new_mode@@YAHXZ` | `0x21458` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 287 | `?_set_new_mode@@YAHH@Z` | `0x21460` | 47 | UnwindData |  |
| 462 | `__set_app_type` | `0x21490` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1057 | `_set_error_mode` | `0x21498` | 64 | UnwindData |  |
| 273 | `?__ExceptionPtrDestroy@@YAXPEAX@Z` | `0x21804` | 50 | UnwindData |  |
| 121 | `??4__non_rtti_object@std@@QEAAAEAV01@AEBV01@@Z` | `0x219D0` | 23 | UnwindData |  |
| 122 | `??4bad_cast@std@@QEAAAEAV01@AEBV01@@Z` | `0x219D0` | 23 | UnwindData |  |
| 123 | `??4bad_typeid@std@@QEAAAEAV01@AEBV01@@Z` | `0x219D0` | 23 | UnwindData |  |
| 135 | `??_Fbad_cast@std@@QEAAXXZ` | `0x219E8` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `??_Fbad_typeid@std@@QEAAXXZ` | `0x219F4` | 2,276 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 267 | `?__ExceptionPtrAssign@@YAXPEAXPEBX@Z` | `0x222D8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 268 | `?__ExceptionPtrCompare@@YA_NPEBX0@Z` | `0x222E0` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 269 | `?__ExceptionPtrCopy@@YAXPEAXPEBX@Z` | `0x222EC` | 35 | UnwindData |  |
| 270 | `?__ExceptionPtrCopyException@@YAXPEAXPEBX1@Z` | `0x22310` | 78 | UnwindData |  |
| 271 | `?__ExceptionPtrCreate@@YAXPEAX@Z` | `0x22360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 272 | `?__ExceptionPtrCurrentException@@YAXPEAX@Z` | `0x22370` | 107 | UnwindData |  |
| 274 | `?__ExceptionPtrRethrow@@YAXPEBX@Z` | `0x223DC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 275 | `?__ExceptionPtrSwap@@YAXPEAX0@Z` | `0x223E4` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 276 | `?__ExceptionPtrToBool@@YA_NPEBX@Z` | `0x22404` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 464 | `__setusermatherr` | `0x22410` | 29 | UnwindData |  |
| 497 | `_amsg_exit` | `0x22CBC` | 38 | UnwindData |  |
| 516 | `_c_exit` | `0x22CE4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 520 | `_cexit` | `0x22CF4` | 88 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 594 | `_exit` | `0x22D4C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 679 | `_get_pgmptr` | `0x22D58` | 54 | UnwindData |  |
| 686 | `_get_wpgmptr` | `0x22D90` | 54 | UnwindData |  |
| 727 | `_initterm` | `0x22E14` | 51 | UnwindData |  |
| 728 | `_initterm_e` | `0x22E48` | 57 | UnwindData |  |
| 1433 | `exit` | `0x2307C` | 1,192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 423 | `__getmainargs` | `0x23524` | 110 | UnwindData |  |
| 434 | `__p___argc` | `0x23594` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 435 | `__p___argv` | `0x2359C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 436 | `__p___initenv` | `0x235A4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 437 | `__p___mb_cur_max` | `0x235AC` | 59 | UnwindData |  |
| 438 | `__p___wargv` | `0x235E8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 439 | `__p___winitenv` | `0x235F0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 440 | `__p__acmdln` | `0x235F8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 441 | `__p__commode` | `0x23600` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 442 | `__p__daylight` | `0x23608` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 443 | `__p__dstbias` | `0x23610` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 444 | `__p__environ` | `0x23618` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 445 | `__p__fmode` | `0x23620` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 425 | `__iob_func` | `0x23628` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 446 | `__p__iob` | `0x23628` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 447 | `__p__mbcasemap` | `0x23630` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 448 | `__p__mbctype` | `0x23638` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 449 | `__p__pctype` | `0x23640` | 59 | UnwindData |  |
| 450 | `__p__pgmptr` | `0x2367C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 451 | `__p__pwctype` | `0x23684` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 452 | `__p__timezone` | `0x2368C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 453 | `__p__tzname` | `0x23694` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 454 | `__p__wcmdln` | `0x2369C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 455 | `__p__wenviron` | `0x236A4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 456 | `__p__wpgmptr` | `0x236AC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 483 | `__wgetmainargs` | `0x236B4` | 157 | UnwindData |  |
| 839 | `_lock` | `0x23754` | 68 | UnwindData |  |
| 1196 | `_unlock` | `0x2393C` | 996 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 511 | `_beginthread` | `0x23D20` | 242 | UnwindData |  |
| 581 | `_endthread` | `0x23E40` | 52 | UnwindData |  |
| 512 | `_beginthreadex` | `0x23EE8` | 237 | UnwindData |  |
| 582 | `_endthreadex` | `0x24004` | 144 | UnwindData |  |
| 421 | `__get_flsindex` | `0x24198` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 422 | `__get_tlsindex` | `0x24198` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 469 | `__threadhandle` | `0x241A0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 470 | `__threadid` | `0x241A8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 639 | `_freefls` | `0x241B0` | 307 | UnwindData |  |
| 701 | `_getptd` | `0x24320` | 36 | UnwindData |  |
| 726 | `_initptd` | `0x243C8` | 194 | UnwindData |  |
| 504 | `_atoi64` | `0x253DC` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 505 | `_atoi64_l` | `0x253E8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 506 | `_atoi_l` | `0x253F8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 507 | `_atol_l` | `0x253F8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1417 | `atoi` | `0x25408` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1418 | `atol` | `0x25408` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1153 | `_swab` | `0x25414` | 88 | UnwindData |  |
| 1392 | `_wtoi64` | `0x25604` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1393 | `_wtoi64_l` | `0x25610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1394 | `_wtoi_l` | `0x25620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1396 | `_wtol_l` | `0x25620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1391 | `_wtoi` | `0x25630` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1395 | `_wtol` | `0x25630` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 722 | `_i64toa` | `0x2563C` | 43 | UnwindData |  |
| 823 | `_itoa` | `0x25668` | 42 | UnwindData |  |
| 850 | `_ltoa` | `0x25694` | 40 | UnwindData |  |
| 1178 | `_ui64toa` | `0x256BC` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1182 | `_ultoa` | `0x2570C` | 26 | UnwindData |  |
| 723 | `_i64toa_s` | `0x257D8` | 35 | UnwindData |  |
| 824 | `_itoa_s` | `0x257FC` | 39 | UnwindData |  |
| 851 | `_ltoa_s` | `0x25824` | 34 | UnwindData |  |
| 1179 | `_ui64toa_s` | `0x25848` | 19 | UnwindData |  |
| 1183 | `_ultoa_s` | `0x2585C` | 19 | UnwindData |  |
| 724 | `_i64tow` | `0x25A60` | 43 | UnwindData |  |
| 825 | `_itow` | `0x25A8C` | 42 | UnwindData |  |
| 852 | `_ltow` | `0x25AB8` | 40 | UnwindData |  |
| 1180 | `_ui64tow` | `0x25AE0` | 26 | UnwindData |  |
| 1184 | `_ultow` | `0x25AFC` | 26 | UnwindData |  |
| 725 | `_i64tow_s` | `0x25BFC` | 35 | UnwindData |  |
| 826 | `_itow_s` | `0x25C20` | 39 | UnwindData |  |
| 853 | `_ltow_s` | `0x25C48` | 34 | UnwindData |  |
| 1181 | `_ui64tow_s` | `0x25C6C` | 19 | UnwindData |  |
| 1185 | `_ultow_s` | `0x25C80` | 19 | UnwindData |  |
| 697 | `_getdrives` | `0x25EB8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 694 | `_getdiskfree` | `0x25EC0` | 163 | UnwindData |  |
| 609 | `_findclose` | `0x25FF4` | 37 | UnwindData |  |
| 610 | `_findfirst32` | `0x2601C` | 325 | UnwindData |  |
| 614 | `_findnext32` | `0x26164` | 287 | UnwindData |  |
| 612 | `_findfirst64` | `0x26284` | 340 | UnwindData |  |
| 616 | `_findnext64` | `0x263D8` | 302 | UnwindData |  |
| 613 | `_findfirst64i32` | `0x26598` | 328 | UnwindData |  |
| 617 | `_findnext64i32` | `0x266E0` | 290 | UnwindData |  |
| 611 | `_findfirst32i64` | `0x26804` | 337 | UnwindData |  |
| 615 | `_findnext32i64` | `0x26958` | 299 | UnwindData |  |
| 1064 | `_seterrormode` | `0x26A84` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 510 | `_beep` | `0x26A8C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1071 | `_sleep` | `0x26A94` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1323 | `_wfindfirst32` | `0x26AA8` | 325 | UnwindData |  |
| 1327 | `_wfindnext32` | `0x26BF0` | 287 | UnwindData |  |
| 1325 | `_wfindfirst64` | `0x26D10` | 340 | UnwindData |  |
| 1329 | `_wfindnext64` | `0x26E64` | 302 | UnwindData |  |
| 1326 | `_wfindfirst64i32` | `0x26F94` | 328 | UnwindData |  |
| 1330 | `_wfindnext64i32` | `0x270DC` | 290 | UnwindData |  |
| 1324 | `_wfindfirst32i64` | `0x27200` | 337 | UnwindData |  |
| 1328 | `_wfindnext32i64` | `0x27354` | 299 | UnwindData |  |
| 486 | `_access` | `0x27480` | 18 | UnwindData |  |
| 487 | `_access_s` | `0x27494` | 87 | UnwindData |  |
| 529 | `_chmod` | `0x274EC` | 83 | UnwindData |  |
| 525 | `_chdir` | `0x27540` | 301 | UnwindData |  |
| 416 | `__doserrno` | `0x27670` | 32 | UnwindData |  |
| 574 | `_dosmaperr` | `0x27690` | 78 | UnwindData |  |
| 585 | `_errno` | `0x276E0` | 32 | UnwindData |  |
| 671 | `_get_doserrno` | `0x27700` | 59 | UnwindData |  |
| 673 | `_get_errno` | `0x2773C` | 59 | UnwindData |  |
| 1055 | `_set_doserrno` | `0x277C8` | 58 | UnwindData |  |
| 1056 | `_set_errno` | `0x27804` | 58 | UnwindData |  |
| 526 | `_chdrive` | `0x27840` | 132 | UnwindData |  |
| 696 | `_getdrive` | `0x278C4` | 235 | UnwindData |  |
| 657 | `_fullpath` | `0x279B0` | 299 | UnwindData |  |
| 692 | `_getcwd` | `0x27ADC` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 693 | `_getdcwd` | `0x27AEC` | 302 | UnwindData |  |
| 700 | `_getpid` | `0x27C9C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 996 | `_mkdir` | `0x27CA4` | 70 | UnwindData |  |
| 1554 | `rename` | `0x27CEC` | 327 | UnwindData |  |
| 1033 | `_rmdir` | `0x27E34` | 70 | UnwindData |  |
| 1108 | `_stat32` | `0x27E7C` | 85 | UnwindData |  |
| 1110 | `_stat64` | `0x27ED4` | 85 | UnwindData |  |
| 1111 | `_stat64i32` | `0x27F2C` | 85 | UnwindData |  |
| 1109 | `_stat32i64` | `0x27F84` | 85 | UnwindData |  |
| 1194 | `_unlink` | `0x27FDC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1553 | `remove` | `0x27FE4` | 70 | UnwindData |  |
| 1257 | `_waccess` | `0x2802C` | 18 | UnwindData |  |
| 1258 | `_waccess_s` | `0x28040` | 168 | UnwindData |  |
| 1262 | `_wchdir` | `0x280E8` | 331 | UnwindData |  |
| 1263 | `_wchmod` | `0x28234` | 155 | UnwindData |  |
| 1336 | `_wfullpath` | `0x282D0` | 308 | UnwindData |  |
| 1337 | `_wgetcwd` | `0x28404` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1338 | `_wgetdcwd` | `0x28414` | 333 | UnwindData |  |
| 1343 | `_wmkdir` | `0x28564` | 49 | UnwindData |  |
| 1357 | `_wrename` | `0x28598` | 53 | UnwindData |  |
| 1359 | `_wrmdir` | `0x285D0` | 47 | UnwindData |  |
| 1377 | `_wstat32` | `0x287B0` | 1,147 | UnwindData |  |
| 1379 | `_wstat64` | `0x28C2C` | 1,157 | UnwindData |  |
| 1380 | `_wstat64i32` | `0x290B4` | 1,159 | UnwindData |  |
| 1378 | `_wstat32i64` | `0x2953C` | 1,145 | UnwindData |  |
| 1356 | `_wremove` | `0x299B8` | 47 | UnwindData |  |
| 1397 | `_wunlink` | `0x299E8` | 1,876 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 586 | `_execl` | `0x2A13C` | 165 | UnwindData |  |
| 587 | `_execle` | `0x2A1E4` | 180 | UnwindData |  |
| 588 | `_execlp` | `0x2A298` | 164 | UnwindData |  |
| 589 | `_execlpe` | `0x2A33C` | 180 | UnwindData |  |
| 590 | `_execv` | `0x2A3F0` | 69 | UnwindData |  |
| 591 | `_execve` | `0x2A438` | 633 | UnwindData |  |
| 592 | `_execvp` | `0x2A73C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 593 | `_execvpe` | `0x2A744` | 781 | UnwindData |  |
| 695 | `_getdllprocaddr` | `0x2AA54` | 36 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 833 | `_loaddll` | `0x2AA78` | 46 | UnwindData |  |
| 1195 | `_unloaddll` | `0x2AAA8` | 32 | UnwindData |  |
| 1092 | `_spawnl` | `0x2AAC8` | 173 | UnwindData |  |
| 1093 | `_spawnle` | `0x2AB78` | 188 | UnwindData |  |
| 1094 | `_spawnlp` | `0x2AC34` | 170 | UnwindData |  |
| 1095 | `_spawnlpe` | `0x2ACE0` | 188 | UnwindData |  |
| 1096 | `_spawnv` | `0x2AD9C` | 69 | UnwindData |  |
| 1097 | `_spawnve` | `0x2ADE4` | 645 | UnwindData |  |
| 1098 | `_spawnvp` | `0x2B0FC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1099 | `_spawnvpe` | `0x2B104` | 749 | UnwindData |  |
| 1605 | `system` | `0x2B3F4` | 264 | UnwindData |  |
| 560 | `_cwait` | `0x2B4FC` | 182 | UnwindData |  |
| 1314 | `_wexecl` | `0x2BDF0` | 168 | UnwindData |  |
| 1315 | `_wexecle` | `0x2BE98` | 183 | UnwindData |  |
| 1316 | `_wexeclp` | `0x2BF50` | 167 | UnwindData |  |
| 1317 | `_wexeclpe` | `0x2BFF8` | 183 | UnwindData |  |
| 1318 | `_wexecv` | `0x2C0B0` | 71 | UnwindData |  |
| 1319 | `_wexecve` | `0x2C0F8` | 637 | UnwindData |  |
| 1320 | `_wexecvp` | `0x2C400` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1321 | `_wexecvpe` | `0x2C408` | 628 | UnwindData |  |
| 1367 | `_wspawnl` | `0x2C67C` | 176 | UnwindData |  |
| 1368 | `_wspawnle` | `0x2C72C` | 191 | UnwindData |  |
| 1369 | `_wspawnlp` | `0x2C7EC` | 173 | UnwindData |  |
| 1370 | `_wspawnlpe` | `0x2C89C` | 191 | UnwindData |  |
| 1371 | `_wspawnv` | `0x2C95C` | 71 | UnwindData |  |
| 1372 | `_wspawnve` | `0x2C9A4` | 652 | UnwindData |  |
| 1373 | `_wspawnvp` | `0x2CCC0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1374 | `_wspawnvpe` | `0x2CCC8` | 677 | UnwindData |  |
| 1385 | `_wsystem` | `0x2CF70` | 264 | UnwindData |  |
| 870 | `_mbclen` | `0x2D078` | 45 | UnwindData |  |
| 871 | `_mbclen_l` | `0x2D0A8` | 45 | UnwindData |  |
| 904 | `_mbsinc` | `0x2D0D8` | 66 | UnwindData |  |
| 905 | `_mbsinc_l` | `0x2D11C` | 39 | UnwindData |  |
| 954 | `_mbsninc` | `0x2D144` | 35 | UnwindData |  |
| 955 | `_mbsninc_l` | `0x2D168` | 34 | UnwindData |  |
| 872 | `_mbctohira` | `0x2D18C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 873 | `_mbctohira_l` | `0x2D194` | 55 | UnwindData |  |
| 874 | `_mbctokata` | `0x2D1CC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 875 | `_mbctokata_l` | `0x2D1D4` | 41 | UnwindData |  |
| 1438 | `feof` | `0x2D200` | 40 | UnwindData |  |
| 1439 | `ferror` | `0x2D228` | 40 | UnwindData |  |
| 687 | `_getc_nolock` | `0x2D250` | 37 | UnwindData |  |
| 1441 | `fgetc` | `0x2D278` | 254 | UnwindData |  |
| 1474 | `getc` | `0x2D278` | 254 | UnwindData |  |
| 602 | `_fgetchar` | `0x2D378` | 21 | UnwindData |  |
| 1475 | `getchar` | `0x2D378` | 21 | UnwindData |  |
| 1443 | `fgets` | `0x2D390` | 351 | UnwindData |  |
| 603 | `_fgetwc_nolock` | `0x2D4F0` | 501 | UnwindData |  |
| 1444 | `fgetwc` | `0x2D6E8` | 92 | UnwindData |  |
| 1480 | `getwc` | `0x2D744` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1445 | `fgetws` | `0x2D74C` | 200 | UnwindData |  |
| 604 | `_fgetwchar` | `0x2D814` | 21 | UnwindData |  |
| 1481 | `getwchar` | `0x2D814` | 21 | UnwindData |  |
| 608 | `_fileno` | `0x2D82C` | 38 | UnwindData |  |
| 1454 | `fputc` | `0x2D854` | 272 | UnwindData |  |
| 1542 | `putc` | `0x2D854` | 272 | UnwindData |  |
| 1455 | `fputs` | `0x2D964` | 299 | UnwindData |  |
| 631 | `_fputchar` | `0x2DA90` | 29 | UnwindData |  |
| 1543 | `putchar` | `0x2DA90` | 29 | UnwindData |  |
| 632 | `_fputwc_nolock` | `0x2DAB0` | 471 | UnwindData |  |
| 1456 | `fputwc` | `0x2DC88` | 101 | UnwindData |  |
| 1545 | `putwc` | `0x2DCF0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1457 | `fputws` | `0x2DCF8` | 180 | UnwindData |  |
| 633 | `_fputwchar` | `0x2DDAC` | 31 | UnwindData |  |
| 1546 | `putwchar` | `0x2DDAC` | 31 | UnwindData |  |
| 605 | `_filbuf` | `0x2DDCC` | 323 | UnwindData |  |
| 840 | `_lock_file` | `0x2E108` | 101 | UnwindData |  |
| 1197 | `_unlock_file` | `0x2E1A4` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 620 | `_flsbuf` | `0x2E214` | 395 | UnwindData |  |
| 1425 | `clearerr` | `0x2E970` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1426 | `clearerr_s` | `0x2E978` | 180 | UnwindData |  |
| 597 | `_fcloseall` | `0x2EA2C` | 168 | UnwindData |  |
| 596 | `_fclose_nolock` | `0x2EAD4` | 122 | UnwindData |  |
| 1437 | `fclose` | `0x2EB50` | 102 | UnwindData |  |
| 600 | `_fdopen` | `0x2EBB8` | 406 | UnwindData |  |
| 601 | `_fflush_nolock` | `0x2ED50` | 76 | UnwindData |  |
| 621 | `_flushall` | `0x2EE18` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1440 | `fflush` | `0x2EE24` | 67 | UnwindData |  |
| 1442 | `fgetpos` | `0x2EF50` | 75 | UnwindData |  |
| 645 | `_fsopen` | `0x2EF9C` | 213 | UnwindData |  |
| 1450 | `fopen` | `0x2F074` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1451 | `fopen_s` | `0x2F080` | 83 | UnwindData |  |
| 627 | `_fprintf_l` | `0x2F0D4` | 29 | UnwindData |  |
| 628 | `_fprintf_p` | `0x2F0F4` | 36 | UnwindData |  |
| 629 | `_fprintf_p_l` | `0x2F118` | 29 | UnwindData |  |
| 630 | `_fprintf_s_l` | `0x2F138` | 29 | UnwindData |  |
| 1452 | `fprintf` | `0x2F158` | 296 | UnwindData |  |
| 1453 | `fprintf_s` | `0x2F280` | 36 | UnwindData |  |
| 634 | `_fread_nolock` | `0x2F2A4` | 29 | UnwindData |  |
| 635 | `_fread_nolock_s` | `0x2F2C4` | 543 | UnwindData |  |
| 1458 | `fread` | `0x2F4E4` | 29 | UnwindData |  |
| 1459 | `fread_s` | `0x2F504` | 167 | UnwindData |  |
| 1461 | `freopen` | `0x2F69C` | 47 | UnwindData |  |
| 1462 | `freopen_s` | `0x2F6CC` | 22 | UnwindData |  |
| 640 | `_fscanf_l` | `0x2F6E4` | 49 | UnwindData |  |
| 641 | `_fscanf_s_l` | `0x2F718` | 49 | UnwindData |  |
| 1464 | `fscanf` | `0x2F74C` | 53 | UnwindData |  |
| 1465 | `fscanf_s` | `0x2F784` | 53 | UnwindData |  |
| 642 | `_fseek_nolock` | `0x2F8DC` | 169 | UnwindData |  |
| 1466 | `fseek` | `0x2F988` | 114 | UnwindData |  |
| 643 | `_fseeki64` | `0x2F9FC` | 116 | UnwindData |  |
| 644 | `_fseeki64_nolock` | `0x2FA70` | 179 | UnwindData |  |
| 1467 | `fsetpos` | `0x2FB24` | 53 | UnwindData |  |
| 650 | `_ftell_nolock` | `0x2FB5C` | 753 | UnwindData |  |
| 1468 | `ftell` | `0x2FE50` | 88 | UnwindData |  |
| 651 | `_ftelli64` | `0x2FEA8` | 91 | UnwindData |  |
| 652 | `_ftelli64_nolock` | `0x2FF04` | 753 | UnwindData |  |
| 660 | `_fwprintf_l` | `0x301F8` | 29 | UnwindData |  |
| 661 | `_fwprintf_p` | `0x30218` | 36 | UnwindData |  |
| 662 | `_fwprintf_p_l` | `0x3023C` | 29 | UnwindData |  |
| 663 | `_fwprintf_s_l` | `0x3025C` | 29 | UnwindData |  |
| 1469 | `fwprintf` | `0x3027C` | 145 | UnwindData |  |
| 1470 | `fwprintf_s` | `0x30310` | 36 | UnwindData |  |
| 664 | `_fwrite_nolock` | `0x30334` | 398 | UnwindData |  |
| 1471 | `fwrite` | `0x304C4` | 143 | UnwindData |  |
| 665 | `_fwscanf_l` | `0x30554` | 49 | UnwindData |  |
| 666 | `_fwscanf_s_l` | `0x30588` | 49 | UnwindData |  |
| 1472 | `fwscanf` | `0x305BC` | 53 | UnwindData |  |
| 1473 | `fwscanf_s` | `0x305F4` | 53 | UnwindData |  |
| 1478 | `gets` | `0x30910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1479 | `gets_s` | `0x30920` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 703 | `_getw` | `0x30928` | 179 | UnwindData |  |
| 708 | `_getws` | `0x309DC` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 709 | `_getws_s` | `0x30B5C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 678 | `_get_output_format` | `0x30B64` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1061 | `_set_output_format` | `0x30B6C` | 52 | UnwindData |  |
| 1009 | `_pclose` | `0x30BA0` | 220 | UnwindData |  |
| 1013 | `_popen` | `0x30C7C` | 1,666 | UnwindData |  |
| 680 | `_get_printf_count_output` | `0x31398` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1014 | `_printf_l` | `0x313B0` | 33 | UnwindData |  |
| 1015 | `_printf_p` | `0x313D4` | 39 | UnwindData |  |
| 1016 | `_printf_p_l` | `0x313FC` | 33 | UnwindData |  |
| 1017 | `_printf_s_l` | `0x31420` | 33 | UnwindData |  |
| 1062 | `_set_printf_count_output` | `0x31444` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1540 | `printf` | `0x3146C` | 171 | UnwindData |  |
| 1541 | `printf_s` | `0x31518` | 39 | UnwindData |  |
| 1544 | `puts` | `0x31540` | 378 | UnwindData |  |
| 1023 | `_putw` | `0x316BC` | 175 | UnwindData |  |
| 1026 | `_putws` | `0x3176C` | 231 | UnwindData |  |
| 1555 | `rewind` | `0x31854` | 185 | UnwindData |  |
| 1034 | `_rmtmp` | `0x31910` | 158 | UnwindData |  |
| 1041 | `_scanf_l` | `0x319B0` | 46 | UnwindData |  |
| 1042 | `_scanf_s_l` | `0x319E0` | 46 | UnwindData |  |
| 1556 | `scanf` | `0x31A10` | 50 | UnwindData |  |
| 1557 | `scanf_s` | `0x31A44` | 50 | UnwindData |  |
| 698 | `_getmaxstdio` | `0x31A78` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1067 | `_setmaxstdio` | `0x31A80` | 273 | UnwindData |  |
| 1558 | `setbuf` | `0x31B94` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1561 | `setvbuf` | `0x31BB0` | 273 | UnwindData |  |
| 1072 | `_snprintf` | `0x31CC4` | 177 | UnwindData |  |
| 1075 | `_snprintf_l` | `0x31D78` | 29 | UnwindData |  |
| 1073 | `_snprintf_c` | `0x31D98` | 191 | UnwindData |  |
| 1074 | `_snprintf_c_l` | `0x31E58` | 29 | UnwindData |  |
| 1078 | `_snscanf` | `0x31E78` | 54 | UnwindData |  |
| 1079 | `_snscanf_l` | `0x31EB0` | 49 | UnwindData |  |
| 1080 | `_snscanf_s` | `0x31EE4` | 54 | UnwindData |  |
| 1081 | `_snscanf_s_l` | `0x31F1C` | 49 | UnwindData |  |
| 1082 | `_snwprintf` | `0x31FF4` | 226 | UnwindData |  |
| 1083 | `_snwprintf_l` | `0x320D8` | 29 | UnwindData |  |
| 1086 | `_snwscanf` | `0x320F8` | 54 | UnwindData |  |
| 1087 | `_snwscanf_l` | `0x32130` | 49 | UnwindData |  |
| 1088 | `_snwscanf_s` | `0x32164` | 54 | UnwindData |  |
| 1089 | `_snwscanf_s_l` | `0x3219C` | 49 | UnwindData |  |
| 1043 | `_scprintf` | `0x32280` | 37 | UnwindData |  |
| 1044 | `_scprintf_l` | `0x322A8` | 33 | UnwindData |  |
| 1045 | `_scprintf_p` | `0x322CC` | 37 | UnwindData |  |
| 1046 | `_scprintf_p_l` | `0x322F4` | 33 | UnwindData |  |
| 1076 | `_snprintf_s` | `0x32318` | 34 | UnwindData |  |
| 1077 | `_snprintf_s_l` | `0x3233C` | 33 | UnwindData |  |
| 1102 | `_sprintf_l` | `0x32360` | 29 | UnwindData |  |
| 1103 | `_sprintf_p` | `0x32380` | 36 | UnwindData |  |
| 1104 | `_sprintf_p_l` | `0x323A4` | 29 | UnwindData |  |
| 1105 | `_sprintf_s_l` | `0x323C4` | 29 | UnwindData |  |
| 1567 | `sprintf` | `0x323E4` | 160 | UnwindData |  |
| 1568 | `sprintf_s` | `0x32484` | 36 | UnwindData |  |
| 1106 | `_sscanf_l` | `0x324A8` | 49 | UnwindData |  |
| 1107 | `_sscanf_s_l` | `0x324DC` | 49 | UnwindData |  |
| 1572 | `sscanf` | `0x32510` | 53 | UnwindData |  |
| 1573 | `sscanf_s` | `0x32548` | 53 | UnwindData |  |
| 466 | `__swprintf_l` | `0x3275C` | 29 | UnwindData |  |
| 1047 | `_scwprintf` | `0x3277C` | 37 | UnwindData |  |
| 1048 | `_scwprintf_l` | `0x327A4` | 33 | UnwindData |  |
| 1049 | `_scwprintf_p` | `0x327C8` | 37 | UnwindData |  |
| 1050 | `_scwprintf_p_l` | `0x327F0` | 33 | UnwindData |  |
| 1084 | `_snwprintf_s` | `0x32814` | 34 | UnwindData |  |
| 1085 | `_snwprintf_s_l` | `0x32838` | 33 | UnwindData |  |
| 1154 | `_swprintf` | `0x3285C` | 196 | UnwindData |  |
| 1157 | `_swprintf_p` | `0x32920` | 36 | UnwindData |  |
| 1158 | `_swprintf_p_l` | `0x32944` | 29 | UnwindData |  |
| 1159 | `_swprintf_s_l` | `0x32964` | 29 | UnwindData |  |
| 1602 | `swprintf_s` | `0x32984` | 36 | UnwindData |  |
| 1155 | `_swprintf_c` | `0x329A8` | 252 | UnwindData |  |
| 1156 | `_swprintf_c_l` | `0x32AA4` | 29 | UnwindData |  |
| 1160 | `_swscanf_l` | `0x32AC4` | 49 | UnwindData |  |
| 1161 | `_swscanf_s_l` | `0x32AF8` | 49 | UnwindData |  |
| 1603 | `swscanf` | `0x32B2C` | 53 | UnwindData |  |
| 1604 | `swscanf_s` | `0x32B64` | 53 | UnwindData |  |
| 1166 | `_tempnam` | `0x32C4C` | 725 | UnwindData |  |
| 1610 | `tmpfile` | `0x3352C` | 35 | UnwindData |  |
| 1611 | `tmpfile_s` | `0x33550` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1612 | `tmpnam` | `0x3355C` | 48 | UnwindData |  |
| 1613 | `tmpnam_s` | `0x3358C` | 64 | UnwindData |  |
| 1188 | `_ungetc_nolock` | `0x335CC` | 264 | UnwindData |  |
| 1618 | `ungetc` | `0x336D4` | 95 | UnwindData |  |
| 1191 | `_ungetwc_nolock` | `0x33734` | 516 | UnwindData |  |
| 1619 | `ungetwc` | `0x33938` | 101 | UnwindData |  |
| 1220 | `_vprintf_l` | `0x339A0` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1221 | `_vprintf_p` | `0x339B8` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1222 | `_vprintf_p_l` | `0x339D0` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1223 | `_vprintf_s_l` | `0x339E8` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1624 | `vprintf` | `0x33A00` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1625 | `vprintf_s` | `0x33AC0` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1212 | `_vfprintf_l` | `0x33AD8` | 35 | UnwindData |  |
| 1213 | `_vfprintf_p` | `0x33AFC` | 35 | UnwindData |  |
| 1214 | `_vfprintf_p_l` | `0x33B20` | 35 | UnwindData |  |
| 1215 | `_vfprintf_s_l` | `0x33B44` | 35 | UnwindData |  |
| 1620 | `vfprintf` | `0x33B68` | 35 | UnwindData |  |
| 1621 | `vfprintf_s` | `0x33CCC` | 35 | UnwindData |  |
| 1216 | `_vfwprintf_l` | `0x33CF0` | 35 | UnwindData |  |
| 1217 | `_vfwprintf_p` | `0x33D14` | 35 | UnwindData |  |
| 1218 | `_vfwprintf_p_l` | `0x33D38` | 35 | UnwindData |  |
| 1219 | `_vfwprintf_s_l` | `0x33D5C` | 35 | UnwindData |  |
| 1622 | `vfwprintf` | `0x33D80` | 35 | UnwindData |  |
| 1623 | `vfwprintf_s` | `0x33E44` | 35 | UnwindData |  |
| 1224 | `_vscprintf` | `0x33E68` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1225 | `_vscprintf_l` | `0x33E80` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1226 | `_vscprintf_p` | `0x33E98` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1227 | `_vscprintf_p_l` | `0x33EB0` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1242 | `_vsprintf_l` | `0x33EC8` | 181 | UnwindData |  |
| 1626 | `vsprintf` | `0x33F80` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1232 | `_vsnprintf` | `0x33F8C` | 22 | UnwindData |  |
| 1235 | `_vsnprintf_l` | `0x33FA4` | 203 | UnwindData |  |
| 1233 | `_vsnprintf_c` | `0x34070` | 49 | UnwindData |  |
| 1234 | `_vsnprintf_c_l` | `0x340A4` | 53 | UnwindData |  |
| 1236 | `_vsnprintf_s` | `0x341C4` | 30 | UnwindData |  |
| 1237 | `_vsnprintf_s_l` | `0x341E4` | 328 | UnwindData |  |
| 1243 | `_vsprintf_p` | `0x3432C` | 49 | UnwindData |  |
| 1244 | `_vsprintf_p_l` | `0x34360` | 53 | UnwindData |  |
| 1245 | `_vsprintf_s_l` | `0x34398` | 110 | UnwindData |  |
| 1627 | `vsprintf_s` | `0x34408` | 22 | UnwindData |  |
| 1238 | `_vsnwprintf` | `0x34420` | 22 | UnwindData |  |
| 1239 | `_vsnwprintf_l` | `0x34438` | 252 | UnwindData |  |
| 478 | `__vswprintf_l` | `0x34534` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1228 | `_vscwprintf` | `0x3453C` | 168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1229 | `_vscwprintf_l` | `0x345E4` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1230 | `_vscwprintf_p` | `0x345FC` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1231 | `_vscwprintf_p_l` | `0x34614` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1246 | `_vswprintf` | `0x3462C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1249 | `_vswprintf_l` | `0x34638` | 221 | UnwindData |  |
| 1240 | `_vsnwprintf_s` | `0x34718` | 30 | UnwindData |  |
| 1241 | `_vsnwprintf_s_l` | `0x34738` | 333 | UnwindData |  |
| 1247 | `_vswprintf_c` | `0x34888` | 49 | UnwindData |  |
| 1248 | `_vswprintf_c_l` | `0x348BC` | 53 | UnwindData |  |
| 1250 | `_vswprintf_p` | `0x34A10` | 49 | UnwindData |  |
| 1251 | `_vswprintf_p_l` | `0x34A44` | 53 | UnwindData |  |
| 1252 | `_vswprintf_s_l` | `0x34A7C` | 121 | UnwindData |  |
| 1628 | `vswprintf_s` | `0x34AF8` | 22 | UnwindData |  |
| 1253 | `_vwprintf_l` | `0x34B10` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1254 | `_vwprintf_p` | `0x34B28` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1255 | `_vwprintf_p_l` | `0x34B40` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1256 | `_vwprintf_s_l` | `0x34B58` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1629 | `vwprintf` | `0x34B70` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1630 | `vwprintf_s` | `0x34B88` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1322 | `_wfdopen` | `0x34BA0` | 436 | UnwindData |  |
| 1331 | `_wfopen` | `0x34D54` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1332 | `_wfopen_s` | `0x34D60` | 83 | UnwindData |  |
| 1335 | `_wfsopen` | `0x34DB4` | 221 | UnwindData |  |
| 1333 | `_wfreopen` | `0x34E94` | 47 | UnwindData |  |
| 1334 | `_wfreopen_s` | `0x34FB4` | 22 | UnwindData |  |
| 1349 | `_wpopen` | `0x352A8` | 1,824 | UnwindData |  |
| 1350 | `_wprintf_l` | `0x359C8` | 33 | UnwindData |  |
| 1351 | `_wprintf_p` | `0x359EC` | 39 | UnwindData |  |
| 1352 | `_wprintf_p_l` | `0x35A14` | 33 | UnwindData |  |
| 1353 | `_wprintf_s_l` | `0x35A38` | 33 | UnwindData |  |
| 1668 | `wprintf` | `0x35A5C` | 171 | UnwindData |  |
| 1669 | `wprintf_s` | `0x35B08` | 39 | UnwindData |  |
| 1360 | `_wscanf_l` | `0x35B30` | 46 | UnwindData |  |
| 1361 | `_wscanf_s_l` | `0x35B60` | 46 | UnwindData |  |
| 1670 | `wscanf` | `0x35C20` | 50 | UnwindData |  |
| 1671 | `wscanf_s` | `0x35C54` | 50 | UnwindData |  |
| 1386 | `_wtempnam` | `0x35C88` | 660 | UnwindData |  |
| 1387 | `_wtmpnam` | `0x35F1C` | 48 | UnwindData |  |
| 1388 | `_wtmpnam_s` | `0x36110` | 64 | UnwindData |  |
| 1528 | `memchr` | `0x36414` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1531 | `memcpy_s` | `0x36430` | 135 | UnwindData |  |
| 993 | `_memccpy` | `0x364B8` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1533 | `memmove_s` | `0x364E0` | 81 | UnwindData |  |
| 1581 | `strcspn` | `0x36534` | 160 | UnwindData |  |
| 1116 | `_strdup` | `0x365D4` | 112 | UnwindData |  |
| 1134 | `_strnset` | `0x36644` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1592 | `strpbrk` | `0x36660` | 161 | UnwindData |  |
| 1136 | `_strrev` | `0x36704` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1137 | `_strset` | `0x3673C` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1594 | `strspn` | `0x36750` | 195 | UnwindData |  |
| 1576 | `strchr` | `0x3691C` | 138 | UnwindData |  |
| 1593 | `strrchr` | `0x369A8` | 324 | UnwindData |  |
| 1595 | `strstr` | `0x36AEC` | 477 | UnwindData |  |
| 1635 | `wcschr` | `0x36CCC` | 140 | UnwindData |  |
| 1650 | `wcsrchr` | `0x36D58` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1654 | `wcsstr` | `0x36E08` | 508 | UnwindData |  |
| 1591 | `strnlen` | `0x37004` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1575 | `strcat_s` | `0x37020` | 124 | UnwindData |  |
| 1587 | `strncat_s` | `0x3709C` | 213 | UnwindData |  |
| 1580 | `strcpy_s` | `0x37174` | 97 | UnwindData |  |
| 1590 | `strncpy_s` | `0x371D8` | 188 | UnwindData |  |
| 465 | `__strncnt` | `0x37294` | 36 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1138 | `_strset_s` | `0x372B8` | 79 | UnwindData |  |
| 1135 | `_strnset_s` | `0x37308` | 122 | UnwindData |  |
| 1597 | `strtok` | `0x37384` | 248 | UnwindData |  |
| 1598 | `strtok_s` | `0x3747C` | 283 | UnwindData |  |
| 1633 | `wcscat` | `0x37598` | 44 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1638 | `wcscpy` | `0x375C4` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1634 | `wcscat_s` | `0x375E0` | 133 | UnwindData |  |
| 1636 | `wcscmp` | `0x37668` | 60 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1639 | `wcscpy_s` | `0x376A4` | 107 | UnwindData |  |
| 1640 | `wcscspn` | `0x37710` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1268 | `_wcsdup` | `0x37750` | 117 | UnwindData |  |
| 1642 | `wcslen` | `0x377C8` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1648 | `wcsnlen` | `0x377E4` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1643 | `wcsncat` | `0x37804` | 60 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1644 | `wcsncat_s` | `0x37840` | 231 | UnwindData |  |
| 1645 | `wcsncmp` | `0x37928` | 44 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 482 | `__wcsncnt` | `0x37954` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1646 | `wcsncpy` | `0x3797C` | 70 | UnwindData |  |
| 1647 | `wcsncpy_s` | `0x379C4` | 204 | UnwindData |  |
| 1286 | `_wcsnset` | `0x37A90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1287 | `_wcsnset_s` | `0x37AB0` | 129 | UnwindData |  |
| 1649 | `wcspbrk` | `0x37B34` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1288 | `_wcsrev` | `0x37B6C` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1289 | `_wcsset` | `0x37BAC` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1290 | `_wcsset_s` | `0x37BC0` | 84 | UnwindData |  |
| 1653 | `wcsspn` | `0x37C14` | 83 | UnwindData |  |
| 1656 | `wcstok` | `0x37C68` | 167 | UnwindData |  |
| 1657 | `wcstok_s` | `0x37D10` | 191 | UnwindData |  |
| 1666 | `wmemcpy_s` | `0x37DD0` | 122 | UnwindData |  |
| 1667 | `wmemmove_s` | `0x37E4C` | 82 | UnwindData |  |
| 1407 | `asctime` | `0x37EA0` | 121 | UnwindData |  |
| 1408 | `asctime_s` | `0x37F1C` | 725 | UnwindData |  |
| 1427 | `clock` | `0x38220` | 61 | UnwindData |  |
| 556 | `_ctime32` | `0x38260` | 107 | UnwindData |  |
| 557 | `_ctime32_s` | `0x382CC` | 147 | UnwindData |  |
| 572 | `_difftime32` | `0x38360` | 43 | UnwindData |  |
| 573 | `_difftime64` | `0x3838C` | 46 | UnwindData |  |
| 653 | `_ftime32` | `0x38670` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 654 | `_ftime32_s` | `0x38678` | 399 | UnwindData |  |
| 710 | `_gmtime32` | `0x38850` | 69 | UnwindData |  |
| 711 | `_gmtime32_s` | `0x38898` | 424 | UnwindData |  |
| 835 | `_localtime32` | `0x38A40` | 69 | UnwindData |  |
| 836 | `_localtime32_s` | `0x38A88` | 722 | UnwindData |  |
| 997 | `_mkgmtime32` | `0x39040` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1001 | `_mktime32` | `0x39048` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1114 | `_strdate` | `0x39054` | 272 | UnwindData |  |
| 1115 | `_strdate_s` | `0x39164` | 303 | UnwindData |  |
| 1139 | `_strtime` | `0x39294` | 248 | UnwindData |  |
| 1140 | `_strtime_s` | `0x3938C` | 279 | UnwindData |  |
| 1167 | `_time32` | `0x394A4` | 85 | UnwindData |  |
| 414 | `__daylight` | `0x394FC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 417 | `__dstbias` | `0x39504` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 471 | `__timezone` | `0x3950C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 473 | `__tzname` | `0x39514` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 670 | `_get_daylight` | `0x3951C` | 47 | UnwindData |  |
| 672 | `_get_dstbias` | `0x3954C` | 47 | UnwindData |  |
| 683 | `_get_timezone` | `0x3957C` | 47 | UnwindData |  |
| 684 | `_get_tzname` | `0x395AC` | 177 | UnwindData |  |
| 1177 | `_tzset` | `0x39978` | 36 | UnwindData |  |
| 658 | `_futime32` | `0x3A0D8` | 500 | UnwindData |  |
| 1198 | `_utime32` | `0x3A2CC` | 139 | UnwindData |  |
| 558 | `_ctime64` | `0x3A358` | 108 | UnwindData |  |
| 559 | `_ctime64_s` | `0x3A3C4` | 162 | UnwindData |  |
| 655 | `_ftime64` | `0x3A734` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 656 | `_ftime64_s` | `0x3A73C` | 402 | UnwindData |  |
| 712 | `_gmtime64` | `0x3A8D0` | 69 | UnwindData |  |
| 713 | `_gmtime64_s` | `0x3A918` | 724 | UnwindData |  |
| 837 | `_localtime64` | `0x3ABEC` | 69 | UnwindData |  |
| 838 | `_localtime64_s` | `0x3AC34` | 780 | UnwindData |  |
| 998 | `_mkgmtime64` | `0x3B218` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1002 | `_mktime64` | `0x3B220` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 702 | `_getsystime` | `0x3B22C` | 158 | UnwindData |  |
| 1070 | `_setsystime` | `0x3B2CC` | 163 | UnwindData |  |
| 1168 | `_time64` | `0x3B370` | 93 | UnwindData |  |
| 659 | `_futime64` | `0x3B3D0` | 504 | UnwindData |  |
| 1199 | `_utime64` | `0x3B5C8` | 139 | UnwindData |  |
| 1259 | `_wasctime` | `0x3B654` | 121 | UnwindData |  |
| 1260 | `_wasctime_s` | `0x3B6D0` | 785 | UnwindData |  |
| 1305 | `_wctime32` | `0x3B9E4` | 107 | UnwindData |  |
| 1306 | `_wctime32_s` | `0x3BA50` | 141 | UnwindData |  |
| 1307 | `_wctime64` | `0x3BAE0` | 108 | UnwindData |  |
| 1308 | `_wctime64_s` | `0x3BB4C` | 158 | UnwindData |  |
| 1381 | `_wstrdate` | `0x3BBEC` | 314 | UnwindData |  |
| 1382 | `_wstrdate_s` | `0x3BD28` | 343 | UnwindData |  |
| 1383 | `_wstrtime` | `0x3BE80` | 290 | UnwindData |  |
| 1384 | `_wstrtime_s` | `0x3BFA4` | 319 | UnwindData |  |
| 1398 | `_wutime32` | `0x3C0E4` | 139 | UnwindData |  |
| 1399 | `_wutime64` | `0x3C170` | 139 | UnwindData |  |
| 1529 | `memcmp` | `0x3C210` | 199 | UnwindData |  |
| 1588 | `strncmp` | `0x3C2F0` | 125 | UnwindData |  |
| 1530 | `memcpy` | `0x3C380` | 1,252 | UnwindData |  |
| 1532 | `memmove` | `0x3C380` | 1,252 | UnwindData |  |
| 1534 | `memset` | `0x3C880` | 266 | UnwindData |  |
| 1574 | `strcat` | `0x3C9A0` | 144 | UnwindData |  |
| 1579 | `strcpy` | `0x3CA40` | 183 | UnwindData |  |
| 1577 | `strcmp` | `0x3CB10` | 103 | UnwindData |  |
| 1585 | `strlen` | `0x3CB90` | 168 | UnwindData |  |
| 1586 | `strncat` | `0x3CC50` | 405 | UnwindData |  |
| 1589 | `strncpy` | `0x3CE00` | 354 | UnwindData |  |
| 426 | `__isascii` | `0x3D00C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 427 | `__iscsym` | `0x3D018` | 40 | UnwindData |  |
| 428 | `__iscsymf` | `0x3D040` | 37 | UnwindData |  |
| 472 | `__toascii` | `0x3D068` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 734 | `_isalnum_l` | `0x3D070` | 98 | UnwindData |  |
| 735 | `_isalpha_l` | `0x3D0D4` | 98 | UnwindData |  |
| 737 | `_iscntrl_l` | `0x3D138` | 95 | UnwindData |  |
| 740 | `_isdigit_l` | `0x3D198` | 95 | UnwindData |  |
| 741 | `_isgraph_l` | `0x3D1F8` | 98 | UnwindData |  |
| 743 | `_islower_l` | `0x3D25C` | 95 | UnwindData |  |
| 804 | `_isprint_l` | `0x3D2BC` | 98 | UnwindData |  |
| 805 | `_ispunct_l` | `0x3D320` | 95 | UnwindData |  |
| 806 | `_isspace_l` | `0x3D380` | 95 | UnwindData |  |
| 807 | `_isupper_l` | `0x3D3E0` | 95 | UnwindData |  |
| 822 | `_isxdigit_l` | `0x3D440` | 98 | UnwindData |  |
| 1483 | `isalnum` | `0x3D4A4` | 127 | UnwindData |  |
| 1484 | `isalpha` | `0x3D524` | 127 | UnwindData |  |
| 1485 | `iscntrl` | `0x3D5A4` | 122 | UnwindData |  |
| 1486 | `isdigit` | `0x3D620` | 122 | UnwindData |  |
| 1487 | `isgraph` | `0x3D69C` | 127 | UnwindData |  |
| 1489 | `islower` | `0x3D71C` | 122 | UnwindData |  |
| 1490 | `isprint` | `0x3D798` | 127 | UnwindData |  |
| 1491 | `ispunct` | `0x3D818` | 122 | UnwindData |  |
| 1492 | `isspace` | `0x3D894` | 122 | UnwindData |  |
| 1493 | `isupper` | `0x3D910` | 122 | UnwindData |  |
| 1507 | `isxdigit` | `0x3D98C` | 127 | UnwindData |  |
| 984 | `_mbstrlen` | `0x3DA0C` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 985 | `_mbstrlen_l` | `0x3DA20` | 174 | UnwindData |  |
| 986 | `_mbstrnlen` | `0x3DAD0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 987 | `_mbstrnlen_l` | `0x3DAD8` | 271 | UnwindData |  |
| 742 | `_isleadbyte_l` | `0x3DBE8` | 67 | UnwindData |  |
| 809 | `_iswalpha_l` | `0x3DC2C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1495 | `iswalpha` | `0x3DC2C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 810 | `_iswcntrl_l` | `0x3DC38` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1497 | `iswcntrl` | `0x3DC38` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 429 | `__iswcsym` | `0x3DC44` | 44 | UnwindData |  |
| 811 | `_iswcsym_l` | `0x3DC44` | 44 | UnwindData |  |
| 430 | `__iswcsymf` | `0x3DC70` | 44 | UnwindData |  |
| 812 | `_iswcsymf_l` | `0x3DC70` | 44 | UnwindData |  |
| 815 | `_iswgraph_l` | `0x3DC9C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1500 | `iswgraph` | `0x3DC9C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 816 | `_iswlower_l` | `0x3DCA8` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1501 | `iswlower` | `0x3DCA8` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 820 | `_iswupper_l` | `0x3DCB4` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1505 | `iswupper` | `0x3DCB4` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1488 | `isleadbyte` | `0x3DCC0` | 69 | UnwindData |  |
| 808 | `_iswalnum_l` | `0x3DD08` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1494 | `iswalnum` | `0x3DD08` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1496 | `iswascii` | `0x3DD14` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 814 | `_iswdigit_l` | `0x3DD24` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1499 | `iswdigit` | `0x3DD24` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 817 | `_iswprint_l` | `0x3DD30` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1502 | `iswprint` | `0x3DD30` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 818 | `_iswpunct_l` | `0x3DD3C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1503 | `iswpunct` | `0x3DD3C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 819 | `_iswspace_l` | `0x3DD48` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1504 | `iswspace` | `0x3DD48` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 821 | `_iswxdigit_l` | `0x3DD54` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1506 | `iswxdigit` | `0x3DD54` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 499 | `_atodbl` | `0x3DD60` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 500 | `_atodbl_l` | `0x3DD68` | 199 | UnwindData |  |
| 502 | `_atoflt` | `0x3DE30` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 503 | `_atoflt_l` | `0x3DE38` | 199 | UnwindData |  |
| 508 | `_atoldbl` | `0x3DF00` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 509 | `_atoldbl_l` | `0x3DF08` | 202 | UnwindData |  |
| 371 | `__STRINGTOLD` | `0x3DFD4` | 110 | UnwindData |  |
| 501 | `_atof_l` | `0x3E044` | 186 | UnwindData |  |
| 1416 | `atof` | `0x3E100` | 152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 579 | `_ecvt` | `0x3E198` | 178 | UnwindData |  |
| 580 | `_ecvt_s` | `0x3E24C` | 205 | UnwindData |  |
| 598 | `_fcvt` | `0x3E31C` | 218 | UnwindData |  |
| 599 | `_fcvt_s` | `0x3E3F8` | 205 | UnwindData |  |
| 667 | `_gcvt` | `0x3E4C8` | 44 | UnwindData |  |
| 668 | `_gcvt_s` | `0x3E4F4` | 362 | UnwindData |  |
| 813 | `_iswctype_l` | `0x3E660` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1482 | `is_wctype` | `0x3E660` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1498 | `iswctype` | `0x3E668` | 102 | UnwindData |  |
| 738 | `_isctype` | `0x3E6D0` | 36 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 739 | `_isctype_l` | `0x3E6F4` | 219 | UnwindData |  |
| 883 | `_mblen_l` | `0x3E7D0` | 227 | UnwindData |  |
| 1520 | `mblen` | `0x3E8B4` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 982 | `_mbstowcs_l` | `0x3E8D0` | 484 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 983 | `_mbstowcs_s_l` | `0x3EAB4` | 304 | UnwindData |  |
| 1525 | `mbstowcs` | `0x3EBE4` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1526 | `mbstowcs_s` | `0x3EC00` | 30 | UnwindData |  |
| 992 | `_mbtowc_l` | `0x3EC20` | 337 | UnwindData |  |
| 1527 | `mbtowc` | `0x3ED74` | 852 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1421 | `btowc` | `0x3F0C8` | 100 | UnwindData |  |
| 1521 | `mbrlen` | `0x3F12C` | 62 | UnwindData |  |
| 1522 | `mbrtowc` | `0x3F16C` | 92 | UnwindData |  |
| 1523 | `mbsrtowcs` | `0x3F1C8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1524 | `mbsrtowcs_s` | `0x3F1D0` | 209 | UnwindData |  |
| 1141 | `_strtod_l` | `0x3F2A4` | 341 | UnwindData |  |
| 1596 | `strtod` | `0x3F3FC` | 580 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1144 | `_strtol_l` | `0x3F640` | 34 | UnwindData |  |
| 1147 | `_strtoul_l` | `0x3F664` | 37 | UnwindData |  |
| 1599 | `strtol` | `0x3F68C` | 48 | UnwindData |  |
| 1600 | `strtoul` | `0x3F6BC` | 51 | UnwindData |  |
| 1142 | `_strtoi64` | `0x3F940` | 48 | UnwindData |  |
| 1143 | `_strtoi64_l` | `0x3F970` | 34 | UnwindData |  |
| 1145 | `_strtoui64` | `0x3F994` | 51 | UnwindData |  |
| 1146 | `_strtoui64_l` | `0x3F9C8` | 37 | UnwindData |  |
| 1170 | `_tolower` | `0x3F9F0` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1171 | `_tolower_l` | `0x3F9F4` | 338 | UnwindData |  |
| 1614 | `tolower` | `0x3FB48` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1172 | `_toupper` | `0x3FB68` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1173 | `_toupper_l` | `0x3FB6C` | 336 | UnwindData |  |
| 1615 | `toupper` | `0x3FCBC` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1174 | `_towlower_l` | `0x3FCDC` | 202 | UnwindData |  |
| 1616 | `towlower` | `0x3FDA8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1175 | `_towupper_l` | `0x3FDB0` | 207 | UnwindData |  |
| 1617 | `towupper` | `0x3FE80` | 676 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1631 | `wcrtomb` | `0x40124` | 58 | UnwindData |  |
| 1632 | `wcrtomb_s` | `0x40160` | 136 | UnwindData |  |
| 1651 | `wcsrtombs` | `0x401E8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1652 | `wcsrtombs_s` | `0x401F0` | 192 | UnwindData |  |
| 1663 | `wctob` | `0x402B0` | 109 | UnwindData |  |
| 1291 | `_wcstod_l` | `0x40320` | 304 | UnwindData |  |
| 1655 | `wcstod` | `0x40450` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1294 | `_wcstol_l` | `0x40640` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1658 | `wcstol` | `0x40640` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1299 | `_wcstoul_l` | `0x40648` | 628 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1661 | `wcstoul` | `0x40648` | 628 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1292 | `_wcstoi64` | `0x408BC` | 48 | UnwindData |  |
| 1293 | `_wcstoi64_l` | `0x408EC` | 34 | UnwindData |  |
| 1297 | `_wcstoui64` | `0x40910` | 51 | UnwindData |  |
| 1298 | `_wcstoui64_l` | `0x40944` | 37 | UnwindData |  |
| 1295 | `_wcstombs_l` | `0x4096C` | 824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1296 | `_wcstombs_s_l` | `0x40CA4` | 236 | UnwindData |  |
| 1659 | `wcstombs` | `0x40D90` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1660 | `wcstombs_s` | `0x40D98` | 30 | UnwindData |  |
| 1309 | `_wctomb_l` | `0x40DB8` | 123 | UnwindData |  |
| 1310 | `_wctomb_s_l` | `0x40E34` | 394 | UnwindData |  |
| 1664 | `wctomb` | `0x40FC0` | 84 | UnwindData |  |
| 1665 | `wctomb_s` | `0x41014` | 20 | UnwindData |  |
| 1389 | `_wtof` | `0x41028` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1390 | `_wtof_l` | `0x41030` | 142 | UnwindData |  |
| 766 | `_ismbcalnum` | `0x410C0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 767 | `_ismbcalnum_l` | `0x410C8` | 202 | UnwindData |  |
| 768 | `_ismbcalpha` | `0x41194` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 769 | `_ismbcalpha_l` | `0x4119C` | 204 | UnwindData |  |
| 744 | `_ismbbalnum` | `0x412E4` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 745 | `_ismbbalnum_l` | `0x412FC` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 746 | `_ismbbalpha` | `0x41318` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 747 | `_ismbbalpha_l` | `0x41330` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 748 | `_ismbbgraph` | `0x4134C` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 749 | `_ismbbgraph_l` | `0x41364` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 750 | `_ismbbkalnum` | `0x41380` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 751 | `_ismbbkalnum_l` | `0x41394` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 752 | `_ismbbkana` | `0x413AC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 753 | `_ismbbkana_l` | `0x413B4` | 101 | UnwindData |  |
| 754 | `_ismbbkprint` | `0x4141C` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 755 | `_ismbbkprint_l` | `0x41430` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 756 | `_ismbbkpunct` | `0x41448` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 757 | `_ismbbkpunct_l` | `0x4145C` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 758 | `_ismbblead` | `0x41474` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 759 | `_ismbblead_l` | `0x41488` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 760 | `_ismbbprint` | `0x414A0` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 761 | `_ismbbprint_l` | `0x414B8` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 762 | `_ismbbpunct` | `0x414D4` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 763 | `_ismbbpunct_l` | `0x414E8` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 764 | `_ismbbtrail` | `0x41500` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 765 | `_ismbbtrail_l` | `0x41514` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 770 | `_ismbcdigit` | `0x4152C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 771 | `_ismbcdigit_l` | `0x41534` | 206 | UnwindData |  |
| 772 | `_ismbcgraph` | `0x41604` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 773 | `_ismbcgraph_l` | `0x4160C` | 209 | UnwindData |  |
| 774 | `_ismbchira` | `0x416E0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 775 | `_ismbchira_l` | `0x416E8` | 77 | UnwindData |  |
| 776 | `_ismbckata` | `0x41738` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 777 | `_ismbckata_l` | `0x41740` | 85 | UnwindData |  |
| 794 | `_ismbcsymbol` | `0x41798` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 795 | `_ismbcsymbol_l` | `0x417A0` | 85 | UnwindData |  |
| 784 | `_ismbclegal` | `0x417F8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 785 | `_ismbclegal_l` | `0x41800` | 82 | UnwindData |  |
| 786 | `_ismbclower` | `0x41854` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 787 | `_ismbclower_l` | `0x4185C` | 183 | UnwindData |  |
| 788 | `_ismbcprint` | `0x41914` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 789 | `_ismbcprint_l` | `0x4191C` | 204 | UnwindData |  |
| 790 | `_ismbcpunct` | `0x419E8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 791 | `_ismbcpunct_l` | `0x419F0` | 199 | UnwindData |  |
| 798 | `_ismbslead` | `0x41AB8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 799 | `_ismbslead_l` | `0x41AC0` | 148 | UnwindData |  |
| 792 | `_ismbcspace` | `0x41B54` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 793 | `_ismbcspace_l` | `0x41B5C` | 204 | UnwindData |  |
| 800 | `_ismbstrail` | `0x41C28` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 801 | `_ismbstrail_l` | `0x41C30` | 145 | UnwindData |  |
| 796 | `_ismbcupper` | `0x41CC4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 797 | `_ismbcupper_l` | `0x41CCC` | 182 | UnwindData |  |
| 859 | `_mbbtype` | `0x41D84` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 860 | `_mbbtype_l` | `0x41D8C` | 148 | UnwindData |  |
| 862 | `_mbccpy` | `0x41E20` | 30 | UnwindData |  |
| 863 | `_mbccpy_l` | `0x41E40` | 29 | UnwindData |  |
| 864 | `_mbccpy_s` | `0x41E60` | 20 | UnwindData |  |
| 865 | `_mbccpy_s_l` | `0x41E74` | 261 | UnwindData |  |
| 887 | `_mbscat_s_l` | `0x41F7C` | 461 | UnwindData |  |
| 895 | `_mbscpy_s_l` | `0x4214C` | 320 | UnwindData |  |
| 915 | `_mbsnbcat_s_l` | `0x4228C` | 687 | UnwindData |  |
| 925 | `_mbsnbcpy_s_l` | `0x4253C` | 519 | UnwindData |  |
| 933 | `_mbsnbset_s_l` | `0x42744` | 601 | UnwindData |  |
| 937 | `_mbsncat_s_l` | `0x429A0` | 630 | UnwindData |  |
| 947 | `_mbsncpy_s_l` | `0x42C18` | 503 | UnwindData |  |
| 961 | `_mbsnset_s_l` | `0x42E10` | 595 | UnwindData |  |
| 971 | `_mbsset_s_l` | `0x43064` | 350 | UnwindData |  |
| 778 | `_ismbcl0` | `0x431C4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 779 | `_ismbcl0_l` | `0x431CC` | 99 | UnwindData |  |
| 780 | `_ismbcl1` | `0x43230` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 781 | `_ismbcl1_l` | `0x43238` | 104 | UnwindData |  |
| 782 | `_ismbcl2` | `0x432A0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 783 | `_ismbcl2_l` | `0x432A8` | 104 | UnwindData |  |
| 699 | `_getmbcp` | `0x436D8` | 58 | UnwindData |  |
| 1068 | `_setmbcp` | `0x43714` | 604 | UnwindData |  |
| 884 | `_mbsbtype` | `0x43C20` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 885 | `_mbsbtype_l` | `0x43C28` | 179 | UnwindData |  |
| 886 | `_mbscat_s` | `0x43CDC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 888 | `_mbschr` | `0x43CE4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 889 | `_mbschr_l` | `0x43CEC` | 189 | UnwindData |  |
| 890 | `_mbscmp` | `0x43DAC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 891 | `_mbscmp_l` | `0x43DB4` | 221 | UnwindData |  |
| 894 | `_mbscpy_s` | `0x43E94` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 892 | `_mbscoll` | `0x43E9C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 893 | `_mbscoll_l` | `0x43EA4` | 201 | UnwindData |  |
| 896 | `_mbscspn` | `0x43F70` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 897 | `_mbscspn_l` | `0x43F78` | 217 | UnwindData |  |
| 898 | `_mbsdec` | `0x44054` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 899 | `_mbsdec_l` | `0x4405C` | 150 | UnwindData |  |
| 900 | `_mbsicmp` | `0x440F4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 901 | `_mbsicmp_l` | `0x440FC` | 493 | UnwindData |  |
| 902 | `_mbsicoll` | `0x442EC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 903 | `_mbsicoll_l` | `0x442F4` | 201 | UnwindData |  |
| 906 | `_mbslen` | `0x443C0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 907 | `_mbslen_l` | `0x443C8` | 107 | UnwindData |  |
| 956 | `_mbsnlen` | `0x44434` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 957 | `_mbsnlen_l` | `0x4443C` | 152 | UnwindData |  |
| 908 | `_mbslwr` | `0x444D4` | 43 | UnwindData |  |
| 909 | `_mbslwr_l` | `0x44500` | 43 | UnwindData |  |
| 910 | `_mbslwr_s` | `0x4452C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 911 | `_mbslwr_s_l` | `0x44534` | 338 | UnwindData |  |
| 912 | `_mbsnbcat` | `0x44688` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 913 | `_mbsnbcat_l` | `0x44690` | 328 | UnwindData |  |
| 914 | `_mbsnbcat_s` | `0x447D8` | 20 | UnwindData |  |
| 916 | `_mbsnbcmp` | `0x447EC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 917 | `_mbsnbcmp_l` | `0x447F4` | 300 | UnwindData |  |
| 918 | `_mbsnbcnt` | `0x44920` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 919 | `_mbsnbcnt_l` | `0x44928` | 147 | UnwindData |  |
| 920 | `_mbsnbcoll` | `0x449BC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 921 | `_mbsnbcoll_l` | `0x449C4` | 275 | UnwindData |  |
| 922 | `_mbsnbcpy` | `0x44AD8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 923 | `_mbsnbcpy_l` | `0x44AE0` | 241 | UnwindData |  |
| 924 | `_mbsnbcpy_s` | `0x44BD4` | 20 | UnwindData |  |
| 926 | `_mbsnbicmp` | `0x44BE8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 927 | `_mbsnbicmp_l` | `0x44BF0` | 429 | UnwindData |  |
| 928 | `_mbsnbicoll` | `0x44DA0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 929 | `_mbsnbicoll_l` | `0x44DA8` | 255 | UnwindData |  |
| 930 | `_mbsnbset` | `0x44EA8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 931 | `_mbsnbset_l` | `0x44EB0` | 242 | UnwindData |  |
| 932 | `_mbsnbset_s` | `0x44FA4` | 20 | UnwindData |  |
| 934 | `_mbsncat` | `0x44FB8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 935 | `_mbsncat_l` | `0x44FC0` | 301 | UnwindData |  |
| 936 | `_mbsncat_s` | `0x450F0` | 20 | UnwindData |  |
| 938 | `_mbsnccnt` | `0x45104` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 939 | `_mbsnccnt_l` | `0x4510C` | 152 | UnwindData |  |
| 940 | `_mbsncmp` | `0x451A4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 941 | `_mbsncmp_l` | `0x451AC` | 256 | UnwindData |  |
| 942 | `_mbsncoll` | `0x452AC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 943 | `_mbsncoll_l` | `0x452B4` | 311 | UnwindData |  |
| 944 | `_mbsncpy` | `0x453EC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 945 | `_mbsncpy_l` | `0x453F4` | 228 | UnwindData |  |
| 946 | `_mbsncpy_s` | `0x454D8` | 20 | UnwindData |  |
| 948 | `_mbsnextc` | `0x454EC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 949 | `_mbsnextc_l` | `0x454F4` | 114 | UnwindData |  |
| 950 | `_mbsnicmp` | `0x45568` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 951 | `_mbsnicmp_l` | `0x45570` | 386 | UnwindData |  |
| 952 | `_mbsnicoll` | `0x456F4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 953 | `_mbsnicoll_l` | `0x456FC` | 311 | UnwindData |  |
| 958 | `_mbsnset` | `0x45834` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 959 | `_mbsnset_l` | `0x4583C` | 343 | UnwindData |  |
| 960 | `_mbsnset_s` | `0x45994` | 20 | UnwindData |  |
| 962 | `_mbspbrk` | `0x459A8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 963 | `_mbspbrk_l` | `0x459B0` | 207 | UnwindData |  |
| 964 | `_mbsrchr` | `0x45A80` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 965 | `_mbsrchr_l` | `0x45A88` | 185 | UnwindData |  |
| 966 | `_mbsrev` | `0x45B44` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 967 | `_mbsrev_l` | `0x45B4C` | 197 | UnwindData |  |
| 968 | `_mbsset` | `0x45C14` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 969 | `_mbsset_l` | `0x45C1C` | 195 | UnwindData |  |
| 970 | `_mbsset_s` | `0x45CE0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 972 | `_mbsspn` | `0x45CE8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 973 | `_mbsspn_l` | `0x45CF0` | 217 | UnwindData |  |
| 974 | `_mbsspnp` | `0x45DCC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 975 | `_mbsspnp_l` | `0x45DD4` | 221 | UnwindData |  |
| 976 | `_mbsstr` | `0x45EB4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 977 | `_mbsstr_l` | `0x45EBC` | 255 | UnwindData |  |
| 978 | `_mbstok` | `0x45FBC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 979 | `_mbstok_l` | `0x45FC4` | 62 | UnwindData |  |
| 980 | `_mbstok_s` | `0x46004` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 981 | `_mbstok_s_l` | `0x4600C` | 483 | UnwindData |  |
| 988 | `_mbsupr` | `0x461F0` | 43 | UnwindData |  |
| 989 | `_mbsupr_l` | `0x4621C` | 43 | UnwindData |  |
| 990 | `_mbsupr_s` | `0x46248` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 991 | `_mbsupr_s_l` | `0x46250` | 338 | UnwindData |  |
| 876 | `_mbctolower` | `0x463A4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 877 | `_mbctolower_l` | `0x463AC` | 192 | UnwindData |  |
| 880 | `_mbctoupper` | `0x4646C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 881 | `_mbctoupper_l` | `0x46474` | 192 | UnwindData |  |
| 866 | `_mbcjistojms` | `0x46534` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 867 | `_mbcjistojms_l` | `0x4653C` | 151 | UnwindData |  |
| 868 | `_mbcjmstojis` | `0x465D4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 869 | `_mbcjmstojis_l` | `0x465DC` | 193 | UnwindData |  |
| 857 | `_mbbtombc` | `0x466A0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 858 | `_mbbtombc_l` | `0x466A8` | 169 | UnwindData |  |
| 878 | `_mbctombb` | `0x46754` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 879 | `_mbctombb_l` | `0x4675C` | 206 | UnwindData |  |
| 552 | `_cscanf` | `0x47700` | 39 | UnwindData |  |
| 553 | `_cscanf_l` | `0x47728` | 33 | UnwindData |  |
| 554 | `_cscanf_s` | `0x486B8` | 39 | UnwindData |  |
| 555 | `_cscanf_s_l` | `0x486E0` | 33 | UnwindData |  |
| 567 | `_cwscanf` | `0x49740` | 39 | UnwindData |  |
| 568 | `_cwscanf_l` | `0x49768` | 33 | UnwindData |  |
| 569 | `_cwscanf_s` | `0x4A9D8` | 39 | UnwindData |  |
| 570 | `_cwscanf_s_l` | `0x4AA00` | 33 | UnwindData |  |
| 542 | `_cprintf` | `0x4AA24` | 39 | UnwindData |  |
| 543 | `_cprintf_l` | `0x4AA4C` | 33 | UnwindData |  |
| 1200 | `_vcprintf` | `0x4AA70` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1201 | `_vcprintf_l` | `0x4AA7C` | 2,478 | UnwindData |  |
| 544 | `_cprintf_p` | `0x4B42C` | 39 | UnwindData |  |
| 545 | `_cprintf_p_l` | `0x4B454` | 33 | UnwindData |  |
| 1202 | `_vcprintf_p` | `0x4B478` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1203 | `_vcprintf_p_l` | `0x4B484` | 4,191 | UnwindData |  |
| 546 | `_cprintf_s` | `0x4C53C` | 39 | UnwindData |  |
| 547 | `_cprintf_s_l` | `0x4C564` | 33 | UnwindData |  |
| 1204 | `_vcprintf_s` | `0x4C588` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1205 | `_vcprintf_s_l` | `0x4C594` | 2,509 | UnwindData |  |
| 561 | `_cwprintf` | `0x4CFF4` | 39 | UnwindData |  |
| 562 | `_cwprintf_l` | `0x4D01C` | 33 | UnwindData |  |
| 1206 | `_vcwprintf` | `0x4D040` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1207 | `_vcwprintf_l` | `0x4D04C` | 2,694 | UnwindData |  |
| 563 | `_cwprintf_p` | `0x4DB6C` | 39 | UnwindData |  |
| 564 | `_cwprintf_p_l` | `0x4DB94` | 33 | UnwindData |  |
| 1208 | `_vcwprintf_p` | `0x4DBB8` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1209 | `_vcwprintf_p_l` | `0x4DBC4` | 4,490 | UnwindData |  |
| 565 | `_cwprintf_s` | `0x4EDA0` | 39 | UnwindData |  |
| 566 | `_cwprintf_s_l` | `0x4EDC8` | 33 | UnwindData |  |
| 1210 | `_vcwprintf_s` | `0x4EDEC` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1211 | `_vcwprintf_s_l` | `0x4EDF8` | 2,726 | UnwindData |  |
| 994 | `_memicmp` | `0x58F7C` | 80 | UnwindData |  |
| 995 | `_memicmp_l` | `0x58FCC` | 224 | UnwindData |  |
| 1113 | `_strcoll_l` | `0x590AC` | 184 | UnwindData |  |
| 1578 | `strcoll` | `0x59164` | 68 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1120 | `_stricmp` | `0x591A8` | 70 | UnwindData |  |
| 1121 | `_stricmp_l` | `0x591F0` | 179 | UnwindData |  |
| 1122 | `_stricoll` | `0x592A4` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1123 | `_stricoll_l` | `0x592BC` | 184 | UnwindData |  |
| 1124 | `_strlwr` | `0x59578` | 88 | UnwindData |  |
| 1125 | `_strlwr_l` | `0x595D0` | 30 | UnwindData |  |
| 1126 | `_strlwr_s` | `0x595F0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1127 | `_strlwr_s_l` | `0x595F8` | 75 | UnwindData |  |
| 1128 | `_strncoll` | `0x59644` | 79 | UnwindData |  |
| 1129 | `_strncoll_l` | `0x59694` | 255 | UnwindData |  |
| 1130 | `_strnicmp` | `0x597DC` | 79 | UnwindData |  |
| 1131 | `_strnicmp_l` | `0x5982C` | 217 | UnwindData |  |
| 1132 | `_strnicoll` | `0x59908` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1133 | `_strnicoll_l` | `0x59920` | 256 | UnwindData |  |
| 1148 | `_strupr` | `0x59C24` | 88 | UnwindData |  |
| 1149 | `_strupr_l` | `0x59C7C` | 30 | UnwindData |  |
| 1150 | `_strupr_s` | `0x59C9C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1151 | `_strupr_s_l` | `0x59CA4` | 75 | UnwindData |  |
| 1152 | `_strxfrm_l` | `0x59CF0` | 374 | UnwindData |  |
| 1601 | `strxfrm` | `0x59E68` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1267 | `_wcscoll_l` | `0x59E70` | 169 | UnwindData |  |
| 1637 | `wcscoll` | `0x59F1C` | 70 | UnwindData |  |
| 1272 | `_wcsicmp` | `0x59F64` | 132 | UnwindData |  |
| 1273 | `_wcsicmp_l` | `0x59FE8` | 237 | UnwindData |  |
| 1274 | `_wcsicoll` | `0x5A0D8` | 132 | UnwindData |  |
| 1275 | `_wcsicoll_l` | `0x5A15C` | 230 | UnwindData |  |
| 1276 | `_wcslwr` | `0x5A438` | 95 | UnwindData |  |
| 1277 | `_wcslwr_l` | `0x5A498` | 30 | UnwindData |  |
| 1278 | `_wcslwr_s` | `0x5A4B8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1279 | `_wcslwr_s_l` | `0x5A4C0` | 75 | UnwindData |  |
| 1280 | `_wcsncoll` | `0x5A50C` | 79 | UnwindData |  |
| 1281 | `_wcsncoll_l` | `0x5A55C` | 214 | UnwindData |  |
| 1282 | `_wcsnicmp` | `0x5A634` | 151 | UnwindData |  |
| 1283 | `_wcsnicmp_l` | `0x5A6CC` | 278 | UnwindData |  |
| 1284 | `_wcsnicoll` | `0x5A7E4` | 146 | UnwindData |  |
| 1285 | `_wcsnicoll_l` | `0x5A878` | 304 | UnwindData |  |
| 1300 | `_wcsupr` | `0x5AB9C` | 95 | UnwindData |  |
| 1301 | `_wcsupr_l` | `0x5ABFC` | 30 | UnwindData |  |
| 1302 | `_wcsupr_s` | `0x5AC1C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1303 | `_wcsupr_s_l` | `0x5AC24` | 75 | UnwindData |  |
| 1304 | `_wcsxfrm_l` | `0x5AC70` | 352 | UnwindData |  |
| 1662 | `wcsxfrm` | `0x5ADD0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 336 | `_Getdays` | `0x5ADD8` | 324 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 337 | `_Getmonths` | `0x5AF1C` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 338 | `_Gettnames` | `0x5B06C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 348 | `_W_Gettnames` | `0x5B06C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 344 | `_Strftime` | `0x5B074` | 30 | UnwindData |  |
| 1119 | `_strftime_l` | `0x5B23C` | 30 | UnwindData |  |
| 1584 | `strftime` | `0x5B25C` | 26 | UnwindData |  |
| 346 | `_W_Getdays` | `0x5BE9C` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 347 | `_W_Getmonths` | `0x5C01C` | 2,388 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 349 | `_Wcsftime` | `0x5C970` | 30 | UnwindData |  |
| 1271 | `_wcsftime_l` | `0x5CB28` | 30 | UnwindData |  |
| 1641 | `wcsftime` | `0x5CB48` | 26 | UnwindData |  |
| 278 | `?_inconsistency@@YAXXZ` | `0x5CB64` | 32 | UnwindData |  |
| 315 | `?terminate@@YAXXZ` | `0x5CB84` | 31 | UnwindData |  |
| 320 | `?unexpected@@YAXXZ` | `0x5CBA4` | 29 | UnwindData |  |
| 27 | `??0__non_rtti_object@std@@QEAA@AEBV01@@Z` | `0x5CBE4` | 33 | UnwindData |  |
| 28 | `??0__non_rtti_object@std@@QEAA@PEBD@Z` | `0x5CC08` | 33 | UnwindData |  |
| 29 | `??0bad_cast@std@@AEAA@PEBQEBD@Z` | `0x5CC2C` | 33 | UnwindData |  |
| 30 | `??0bad_cast@std@@QEAA@AEBV01@@Z` | `0x5CC50` | 33 | UnwindData |  |
| 31 | `??0bad_cast@std@@QEAA@PEBD@Z` | `0x5CC74` | 42 | UnwindData |  |
| 34 | `??0bad_typeid@std@@QEAA@AEBV01@@Z` | `0x5CCA0` | 33 | UnwindData |  |
| 35 | `??0bad_typeid@std@@QEAA@PEBD@Z` | `0x5CCC4` | 42 | UnwindData |  |
| 44 | `??0exception@std@@QEAA@AEBQEBD@Z` | `0x5CCF0` | 45 | UnwindData |  |
| 45 | `??0exception@std@@QEAA@AEBQEBDH@Z` | `0x5CD20` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `??0exception@std@@QEAA@AEBV01@@Z` | `0x5CD3C` | 42 | UnwindData |  |
| 47 | `??0exception@std@@QEAA@XZ` | `0x5CD68` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `??1__non_rtti_object@std@@UEAA@XZ` | `0x5CD80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `??1bad_cast@std@@UEAA@XZ` | `0x5CD80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `??1bad_typeid@std@@UEAA@XZ` | `0x5CD80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `??1exception@std@@UEAA@XZ` | `0x5CD80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `??4exception@std@@QEAAAEAV01@AEBV01@@Z` | `0x5CD90` | 68 | UnwindData |  |
| 195 | `?_Copy_str@exception@std@@AEAAXPEBD@Z` | `0x5CE48` | 90 | UnwindData |  |
| 252 | `?_Tidy@exception@std@@AEAAXXZ` | `0x5CEA4` | 39 | UnwindData |  |
| 328 | `?what@exception@std@@UEBAPEBDXZ` | `0x5CECC` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `??1type_info@@UEAA@XZ` | `0x5CEE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `??8type_info@@QEBA_NAEBV0@@Z` | `0x5CEF0` | 30 | UnwindData |  |
| 126 | `??9type_info@@QEBA_NAEBV0@@Z` | `0x5CF10` | 30 | UnwindData |  |
| 281 | `?_name_internal_method@type_info@@QEBAPEBDPEAU__type_info_node@@@Z` | `0x5CFA4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 291 | `?_type_info_dtor_internal_method@type_info@@QEAAXXZ` | `0x5CFAC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 294 | `?before@type_info@@QEBA_NAEBV1@@Z` | `0x5CFB4` | 30 | UnwindData |  |
| 301 | `?name@type_info@@QEBAPEBDPEAU__type_info_node@@@Z` | `0x5CFD4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 305 | `?raw_name@type_info@@QEBAPEBDXZ` | `0x5CFDC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 364 | `__DestructExceptionObject` | `0x5CFE4` | 110 | UnwindData |  |
| 277 | `__uncaught_exception` | `0x5D90C` | 25 | UnwindData |  |
| 280 | `?_is_exception_typeof@@YAHAEBVtype_info@@PEAU_EXCEPTION_POINTERS@@@Z` | `0x5D928` | 191 | UnwindData |  |
| 351 | `__AdjustPointer` | `0x5D9E8` | 36 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 352 | `__BuildCatchObject` | `0x5DA0C` | 182 | UnwindData |  |
| 353 | `__BuildCatchObjectHelper` | `0x5DAC4` | 509 | UnwindData |  |
| 356 | `__CxxDetectRethrow` | `0x5DEC8` | 71 | UnwindData |  |
| 357 | `__CxxExceptionFilter` | `0x5DF10` | 502 | UnwindData |  |
| 361 | `__CxxQueryExceptionSize` | `0x5E108` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 362 | `__CxxRegisterExceptionObject` | `0x5E110` | 193 | UnwindData |  |
| 363 | `__CxxUnregisterExceptionObject` | `0x5E1D4` | 343 | UnwindData |  |
| 365 | `__FrameUnwindFilter` | `0x5E32C` | 83 | UnwindData |  |
| 373 | `__TypeMatch` | `0x5E738` | 286 | UnwindData |  |
| 332 | `_CxxThrowException` | `0x5E858` | 223 | UnwindData |  |
| 331 | `_CreateFrameInfo` | `0x5ECBC` | 67 | UnwindData |  |
| 333 | `_FindAndUnlinkFrame` | `0x5ED00` | 94 | UnwindData |  |
| 334 | `_GetImageBase` | `0x5ED60` | 21 | UnwindData |  |
| 335 | `_GetThrowImageBase` | `0x5ED78` | 21 | UnwindData |  |
| 340 | `_IsExceptionObjectToBeDestroyed` | `0x5ED90` | 50 | UnwindData |  |
| 342 | `_SetImageBase` | `0x5EDC4` | 27 | UnwindData |  |
| 343 | `_SetThrowImageBase` | `0x5EDE0` | 27 | UnwindData |  |
| 358 | `__CxxFrameHandler` | `0x5EF74` | 135 | UnwindData |  |
| 359 | `__CxxFrameHandler2` | `0x5EF74` | 135 | UnwindData |  |
| 360 | `__CxxFrameHandler3` | `0x5EF74` | 135 | UnwindData |  |
| 214 | `?_Name_base@type_info@@CAPEBDPEBV1@PEAU__type_info_node@@@Z` | `0x5F10C` | 308 | UnwindData |  |
| 215 | `?_Name_base_internal@type_info@@CAPEBDPEBV1@PEAU__type_info_node@@@Z` | `0x5F240` | 345 | UnwindData |  |
| 259 | `?_Type_info_dtor@type_info@@CAXPEAV1@@Z` | `0x5F39C` | 108 | UnwindData |  |
| 260 | `?_Type_info_dtor_internal@type_info@@CAXPEAV1@@Z` | `0x5F39C` | 108 | UnwindData |  |
| 384 | `__clean_type_info_names_internal` | `0x5F408` | 79 | UnwindData |  |
| 476 | `__unDNameHelper` | `0x5F458` | 53 | UnwindData |  |
| 262 | `?_ValidateExecute@@YAHP6A_JXZ@Z` | `0x5F490` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 263 | `?_ValidateRead@@YAHPEBXI@Z` | `0x5F490` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 264 | `?_ValidateWrite@@YAHPEAXI@Z` | `0x5F490` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 288 | `?_set_se_translator@@YAP6AXIPEAU_EXCEPTION_POINTERS@@@ZH@Z` | `0x5F49C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 289 | `?_set_se_translator@@YAP6AXIPEAU_EXCEPTION_POINTERS@@@ZP6AXI0@Z@Z` | `0x5F4AC` | 51 | UnwindData |  |
| 311 | `?set_terminate@@YAP6AXXZH@Z` | `0x5F4E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 312 | `?set_terminate@@YAP6AXXZP6AXXZ@Z` | `0x5F4F0` | 75 | UnwindData |  |
| 313 | `?set_unexpected@@YAP6AXXZH@Z` | `0x5F53C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 314 | `?set_unexpected@@YAP6AXXZP6AXXZ@Z` | `0x5F54C` | 75 | UnwindData |  |
| 682 | `_get_terminate` | `0x5F598` | 21 | UnwindData |  |
| 685 | `_get_unexpected` | `0x5F5B0` | 21 | UnwindData |  |
| 368 | `__RTCastToVoid` | `0x5FA58` | 105 | UnwindData |  |
| 369 | `__RTDynamicCast` | `0x5FAC4` | 380 | UnwindData |  |
| 370 | `__RTtypeid` | `0x5FC40` | 169 | UnwindData |  |
| 474 | `__unDName` | `0x65F00` | 261 | UnwindData |  |
| 475 | `__unDNameEx` | `0x66008` | 267 | UnwindData |  |
| 114 | `??2@YAPEAX_K@Z` | `0x662A8` | 105 | UnwindData |  |
| 116 | `??3@YAXPEAX@Z` | `0x66314` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1460 | `free` | `0x6631C` | 61 | UnwindData |  |
| 1519 | `malloc` | `0x6635C` | 182 | UnwindData |  |
| 519 | `_calloc_crt` | `0x66414` | 128 | UnwindData |  |
| 856 | `_malloc_crt` | `0x66494` | 123 | UnwindData |  |
| 1029 | `_realloc_crt` | `0x66510` | 130 | UnwindData |  |
| 1031 | `_recalloc_crt` | `0x66594` | 133 | UnwindData |  |
| 1060 | `_set_malloc_crt_max_wait` | `0x6661C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 675 | `_get_heap_handle` | `0x6662C` | 52 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1422 | `calloc` | `0x66660` | 65 | UnwindData |  |
| 489 | `_aligned_free` | `0x666A4` | 27 | UnwindData |  |
| 490 | `_aligned_malloc` | `0x666C0` | 116 | UnwindData |  |
| 491 | `_aligned_msize` | `0x66734` | 101 | UnwindData |  |
| 492 | `_aligned_offset_malloc` | `0x6679C` | 179 | UnwindData |  |
| 493 | `_aligned_offset_realloc` | `0x66850` | 458 | UnwindData |  |
| 494 | `_aligned_offset_recalloc` | `0x66A1C` | 163 | UnwindData |  |
| 495 | `_aligned_realloc` | `0x66AC0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 496 | `_aligned_recalloc` | `0x66AC8` | 20 | UnwindData |  |
| 595 | `_expand` | `0x66ADC` | 249 | UnwindData |  |
| 714 | `_heapadd` | `0x66BD8` | 23 | UnwindData |  |
| 715 | `_heapchk` | `0x66BF0` | 45 | UnwindData |  |
| 717 | `_heapset` | `0x66C20` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 716 | `_heapmin` | `0x66C28` | 33 | UnwindData |  |
| 718 | `_heapused` | `0x66C4C` | 22 | UnwindData |  |
| 719 | `_heapwalk` | `0x66C64` | 327 | UnwindData |  |
| 1003 | `_msize` | `0x66DAC` | 57 | UnwindData |  |
| 1030 | `_recalloc` | `0x66DE8` | 134 | UnwindData |  |
| 1032 | `_resetstkoflw` | `0x66E70` | 292 | UnwindData |  |
| 1552 | `realloc` | `0x66F94` | 211 | UnwindData |  |
| 646 | `_fstat32` | `0x674A4` | 938 | UnwindData |  |
| 1346 | `_wopen` | `0x67944` | 205 | UnwindData |  |
| 1365 | `_wsopen` | `0x67A14` | 65 | UnwindData |  |
| 1366 | `_wsopen_s` | `0x682F0` | 50 | UnwindData |  |
| 533 | `_close` | `0x68324` | 195 | UnwindData |  |
| 648 | `_fstat64` | `0x684A4` | 967 | UnwindData |  |
| 649 | `_fstat64i32` | `0x6886C` | 949 | UnwindData |  |
| 647 | `_fstat32i64` | `0x68C24` | 956 | UnwindData |  |
| 1028 | `_read` | `0x68FE0` | 282 | UnwindData |  |
| 736 | `_isatty` | `0x69960` | 95 | UnwindData |  |
| 1358 | `_write` | `0x699C0` | 223 | UnwindData |  |
| 849 | `_lseeki64` | `0x6A1DC` | 227 | UnwindData |  |
| 1007 | `_open` | `0x6A354` | 205 | UnwindData |  |
| 1090 | `_sopen` | `0x6A424` | 65 | UnwindData |  |
| 1091 | `_sopen_s` | `0x6A5CC` | 50 | UnwindData |  |
| 534 | `_commit` | `0x6A600` | 215 | UnwindData |  |
| 848 | `_lseek` | `0x6A6D8` | 223 | UnwindData |  |
| 1012 | `_pipe` | `0x6A850` | 704 | UnwindData |  |
| 677 | `_get_osfhandle` | `0x6AE4C` | 116 | UnwindData |  |
| 1008 | `_open_osfhandle` | `0x6AEC0` | 250 | UnwindData |  |
| 688 | `_getch` | `0x6B098` | 42 | UnwindData |  |
| 689 | `_getch_nolock` | `0x6B0C4` | 256 | UnwindData |  |
| 690 | `_getche` | `0x6B1C4` | 42 | UnwindData |  |
| 691 | `_getche_nolock` | `0x6B1F0` | 66 | UnwindData |  |
| 830 | `_kbhit` | `0x6B318` | 42 | UnwindData |  |
| 1189 | `_ungetch` | `0x6B4DC` | 46 | UnwindData |  |
| 1190 | `_ungetch_nolock` | `0x6B50C` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 704 | `_getwch` | `0x6B528` | 44 | UnwindData |  |
| 705 | `_getwch_nolock` | `0x6B554` | 315 | UnwindData |  |
| 706 | `_getwche` | `0x6B690` | 44 | UnwindData |  |
| 707 | `_getwche_nolock` | `0x6B6BC` | 79 | UnwindData |  |
| 1192 | `_ungetwch` | `0x6B70C` | 50 | UnwindData |  |
| 1193 | `_ungetwch_nolock` | `0x6B740` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1019 | `_putch` | `0x6B768` | 46 | UnwindData |  |
| 1020 | `_putch_nolock` | `0x6B798` | 177 | UnwindData |  |
| 1024 | `_putwch` | `0x6B84C` | 50 | UnwindData |  |
| 1025 | `_putwch_nolock` | `0x6B880` | 89 | UnwindData |  |
| 282 | `?_open@@YAHPEBDHH@Z` | `0x6B8DC` | 52 | UnwindData |  |
| 290 | `?_sopen@@YAHPEBDHHH@Z` | `0x6B910` | 43 | UnwindData |  |
| 292 | `?_wopen@@YAHPEB_WHH@Z` | `0x6B93C` | 52 | UnwindData |  |
| 293 | `?_wsopen@@YAHPEB_WHHH@Z` | `0x6B970` | 43 | UnwindData |  |
| 521 | `_cgets` | `0x6B99C` | 110 | UnwindData |  |
| 522 | `_cgets_s` | `0x6BA0C` | 302 | UnwindData |  |
| 523 | `_cgetws` | `0x6BB3C` | 90 | UnwindData |  |
| 524 | `_cgetws_s` | `0x6BB98` | 479 | UnwindData |  |
| 530 | `_chsize` | `0x6BD78` | 21 | UnwindData |  |
| 531 | `_chsize_s` | `0x6BF28` | 237 | UnwindData |  |
| 548 | `_cputs` | `0x6C018` | 120 | UnwindData |  |
| 549 | `_cputws` | `0x6C090` | 218 | UnwindData |  |
| 550 | `_creat` | `0x6C16C` | 55 | UnwindData |  |
| 576 | `_dup` | `0x6C1A4` | 203 | UnwindData |  |
| 577 | `_dup2` | `0x6C420` | 377 | UnwindData |  |
| 584 | `_eof` | `0x6C70C` | 278 | UnwindData |  |
| 606 | `_filelength` | `0x6C824` | 263 | UnwindData |  |
| 607 | `_filelengthi64` | `0x6C92C` | 274 | UnwindData |  |
| 674 | `_get_fmode` | `0x6CA40` | 47 | UnwindData |  |
| 1058 | `_set_fmode` | `0x6CA70` | 61 | UnwindData |  |
| 1069 | `_setmode` | `0x6CAB0` | 248 | UnwindData |  |
| 841 | `_locking` | `0x6CC88` | 278 | UnwindData |  |
| 999 | `_mktemp` | `0x6CEBC` | 77 | UnwindData |  |
| 1000 | `_mktemp_s` | `0x6CF0C` | 329 | UnwindData |  |
| 1164 | `_tell` | `0x6D058` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1165 | `_telli64` | `0x6D064` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1265 | `_wcreat` | `0x6D070` | 55 | UnwindData |  |
| 1344 | `_wmktemp` | `0x6D0A8` | 77 | UnwindData |  |
| 1345 | `_wmktemp_s` | `0x6D0F8` | 336 | UnwindData |  |
| 279 | `?_invalid_parameter@@YAXPEBG00I_K@Z` | `0x6D300` | 252 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 676 | `_get_invalid_parameter_handler` | `0x6D3FC` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 729 | `_invalid_parameter` | `0x6D414` | 101 | UnwindData |  |
| 730 | `_invalid_parameter_noinfo` | `0x6D47C` | 30 | UnwindData |  |
| 731 | `_invalid_parameter_noinfo_noreturn` | `0x6D49C` | 47 | UnwindData |  |
| 732 | `_invoke_watson` | `0x6D4CC` | 59 | UnwindData |  |
| 1059 | `_set_invalid_parameter_handler` | `0x6D508` | 59 | UnwindData |  |
| 681 | `_get_purecall_handler` | `0x6D544` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1018 | `_purecall` | `0x6D554` | 52 | UnwindData |  |
| 1063 | `_set_purecall_handler` | `0x6D588` | 59 | UnwindData |  |
| 415 | `__dllonexit` | `0x6D608` | 209 | UnwindData |  |
| 1006 | `_onexit` | `0x6D6DC` | 266 | UnwindData |  |
| 1415 | `atexit` | `0x6D7E8` | 23 | UnwindData |  |
| 386 | `__crtCaptureCurrentContext` | `0x6D8C0` | 109 | UnwindData |  |
| 387 | `__crtCapturePreviousContext` | `0x6D930` | 113 | UnwindData |  |
| 391 | `__crtCreateSemaphoreExW` | `0x6D9DC` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 392 | `__crtCreateSymbolicLinkW` | `0x6D9F8` | 45 | UnwindData |  |
| 394 | `__crtFlsAlloc` | `0x6DA58` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 395 | `__crtFlsFree` | `0x6DA74` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 396 | `__crtFlsGetValue` | `0x6DA90` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 397 | `__crtFlsSetValue` | `0x6DAAC` | 156 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 400 | `__crtGetShowWindowMode` | `0x6DB48` | 44 | UnwindData |  |
| 403 | `__crtInitializeCriticalSectionEx` | `0x6DB74` | 43 | UnwindData |  |
| 404 | `__crtIsPackagedApp` | `0x6DBA0` | 76 | UnwindData |  |
| 409 | `__crtSetThreadStackGuarantee` | `0x6DF70` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 410 | `__crtSetUnhandledExceptionFilter` | `0x6DFC0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 411 | `__crtTerminateProcess` | `0x6DFC8` | 31 | UnwindData |  |
| 412 | `__crtUnhandledException` | `0x6DFE8` | 32 | UnwindData |  |
| 1551 | `rand_s` | `0x6E21C` | 314 | UnwindData |  |
| 418 | `__fpecode` | `0x6E358` | 20 | UnwindData |  |
| 460 | `__pxcptinfoptrs` | `0x6E37C` | 20 | UnwindData |  |
| 1549 | `raise` | `0x6E444` | 548 | UnwindData |  |
| 1562 | `signal` | `0x6E668` | 656 | UnwindData |  |
| 354 | `__C_specific_handler` | `0x6E8F8` | 478 | UnwindData |  |
| 457 | `__pctype_func` | `0x6F3D8` | 59 | UnwindData |  |
| 459 | `__pwctype_func` | `0x6F414` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 350 | `_XcptFilter` | `0x6F41C` | 460 | UnwindData |  |
| 355 | `__CppXcptFilter` | `0x6F5E8` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 578 | `_dupenv_s` | `0x6F5FC` | 258 | UnwindData |  |
| 1476 | `getenv` | `0x6F79C` | 107 | UnwindData |  |
| 1477 | `getenv_s` | `0x6F808` | 251 | UnwindData |  |
| 1312 | `_wdupenv_s` | `0x6F9BC` | 258 | UnwindData |  |
| 1339 | `_wgetenv` | `0x6FAC0` | 107 | UnwindData |  |
| 1340 | `_wgetenv_s` | `0x6FBE0` | 252 | UnwindData |  |
| 834 | `_local_unwind` | `0x6FDD0` | 36 | UnwindData |  |
| 366 | `__NLG_Dispatch2` | `0x6FE20` | 1 | UnwindData |  |
| 367 | `__NLG_Return2` | `0x6FE30` | 1 | UnwindData |  |
| 461 | `__report_gsfailure` | `0x6FF18` | 209 | UnwindData |  |
| 374 | `___lc_codepage_func` | `0x7009C` | 55 | UnwindData |  |
| 375 | `___lc_collate_cp_func` | `0x700D4` | 55 | UnwindData |  |
| 376 | `___lc_locale_name_func` | `0x7010C` | 59 | UnwindData |  |
| 377 | `___mb_cur_max_func` | `0x70148` | 58 | UnwindData |  |
| 378 | `___mb_cur_max_l_func` | `0x70184` | 1,152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 379 | `___setlc_active_func` | `0x70604` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 380 | `___unguarded_readlc_active_add_func` | `0x7060C` | 140 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 385 | `__create_locale` | `0x70698` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 419 | `__free_locale` | `0x706A0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 420 | `__get_current_locale` | `0x706A8` | 612 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 536 | `_configthreadlocale` | `0x7090C` | 105 | UnwindData |  |
| 551 | `_create_locale` | `0x70A58` | 119 | UnwindData |  |
| 636 | `_free_locale` | `0x70EA4` | 154 | UnwindData |  |
| 669 | `_get_current_locale` | `0x70F40` | 156 | UnwindData |  |
| 1266 | `_wcreate_locale` | `0x70FDC` | 255 | UnwindData |  |
| 1364 | `_wsetlocale` | `0x71144` | 411 | UnwindData |  |
| 406 | `__crtLCMapStringA` | `0x71EE4` | 150 | UnwindData |  |
| 408 | `__crtLCMapStringW` | `0x71F7C` | 73 | UnwindData |  |
| 388 | `__crtCompareStringA` | `0x72310` | 137 | UnwindData |  |
| 390 | `__crtCompareStringW` | `0x7239C` | 165 | UnwindData |  |
| 389 | `__crtCompareStringEx` | `0x72514` | 143 | UnwindData |  |
| 393 | `__crtEnumSystemLocalesEx` | `0x72694` | 68 | UnwindData |  |
| 398 | `__crtGetDateFormatEx` | `0x726D8` | 122 | UnwindData |  |
| 399 | `__crtGetLocaleInfoEx` | `0x72754` | 80 | UnwindData |  |
| 401 | `__crtGetTimeFormatEx` | `0x727A4` | 117 | UnwindData |  |
| 402 | `__crtGetUserDefaultLocaleName` | `0x7281C` | 65 | UnwindData |  |
| 405 | `__crtIsValidLocaleName` | `0x72860` | 50 | UnwindData |  |
| 407 | `__crtLCMapStringEx` | `0x72894` | 143 | UnwindData |  |
| 115 | `??2@YAPEAX_KHPEBDH@Z` | `0x7297C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `??_U@YAPEAX_K@Z` | `0x7297C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `??_U@YAPEAX_KHPEBDH@Z` | `0x72984` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `??3@YAXPEAXHPEBDH@Z` | `0x7298C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `??_V@YAXPEAX@Z` | `0x7298C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `??_V@YAXPEAXHPEBDH@Z` | `0x72994` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 413 | `__crt_debugger_hook` | `0x7299C` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1513 | `localeconv` | `0x729A4` | 56 | UnwindData |  |
| 432 | `__lconv_init` | `0x729DC` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 467 | `__sys_errlist` | `0x729EC` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 468 | `__sys_nerr` | `0x729F4` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 480 | `__wcserror` | `0x729FC` | 392 | UnwindData |  |
| 481 | `__wcserror_s` | `0x72B84` | 238 | UnwindData |  |
| 498 | `_assert` | `0x72C74` | 2,262 | UnwindData |  |
| 513 | `_byteswap_uint64` | `0x7354C` | 116 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 514 | `_byteswap_ulong` | `0x735C0` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 515 | `_byteswap_ushort` | `0x735E8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 831 | `_lfind` | `0x735F8` | 151 | UnwindData |  |
| 832 | `_lfind_s` | `0x73690` | 156 | UnwindData |  |
| 844 | `_lrotl` | `0x7372C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1035 | `_rotl` | `0x7372C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1036 | `_rotl64` | `0x73738` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 845 | `_lrotr` | `0x73744` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1037 | `_rotr` | `0x73744` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1038 | `_rotr64` | `0x73750` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 846 | `_lsearch` | `0x7375C` | 160 | UnwindData |  |
| 847 | `_lsearch_s` | `0x737FC` | 165 | UnwindData |  |
| 854 | `_makepath` | `0x738A4` | 39 | UnwindData |  |
| 855 | `_makepath_s` | `0x738CC` | 328 | UnwindData |  |
| 1021 | `_putenv` | `0x73A14` | 50 | UnwindData |  |
| 1022 | `_putenv_s` | `0x73CC0` | 117 | UnwindData |  |
| 1051 | `_searchenv` | `0x73D38` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1052 | `_searchenv_s` | `0x73D44` | 814 | UnwindData |  |
| 1053 | `_set_abort_behavior` | `0x74074` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1403 | `abort` | `0x74090` | 85 | UnwindData |  |
| 1065 | `_setjmp` | `0x74100` | 160 | UnwindData |  |
| 1559 | `setjmp` | `0x74100` | 160 | UnwindData |  |
| 1066 | `_setjmpex` | `0x741B0` | 144 | UnwindData |  |
| 1100 | `_splitpath` | `0x74240` | 136 | UnwindData |  |
| 1101 | `_splitpath_s` | `0x74558` | 671 | UnwindData |  |
| 1117 | `_strerror` | `0x747F8` | 341 | UnwindData |  |
| 1118 | `_strerror_s` | `0x74950` | 228 | UnwindData |  |
| 1186 | `_umask` | `0x74A34` | 34 | UnwindData |  |
| 1187 | `_umask_s` | `0x74A58` | 67 | UnwindData |  |
| 1261 | `_wassert` | `0x74A9C` | 2,384 | UnwindData |  |
| 1269 | `_wcserror` | `0x75410` | 166 | UnwindData |  |
| 1270 | `_wcserror_s` | `0x754B8` | 173 | UnwindData |  |
| 1341 | `_wmakepath` | `0x75568` | 39 | UnwindData |  |
| 1342 | `_wmakepath_s` | `0x75590` | 341 | UnwindData |  |
| 1347 | `_wperror` | `0x756E8` | 376 | UnwindData |  |
| 1354 | `_wputenv` | `0x75860` | 50 | UnwindData |  |
| 1355 | `_wputenv_s` | `0x75B48` | 117 | UnwindData |  |
| 1362 | `_wsearchenv` | `0x75BC0` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1363 | `_wsearchenv_s` | `0x75BCC` | 834 | UnwindData |  |
| 1375 | `_wsplitpath` | `0x75F10` | 136 | UnwindData |  |
| 1376 | `_wsplitpath_s` | `0x7622C` | 688 | UnwindData |  |
| 1419 | `bsearch` | `0x764DC` | 240 | UnwindData |  |
| 1420 | `bsearch_s` | `0x765CC` | 250 | UnwindData |  |
| 1404 | `abs` | `0x766C8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1508 | `labs` | `0x766C8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1432 | `div` | `0x766D0` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1510 | `ldiv` | `0x766D0` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 485 | `_abs64` | `0x766E8` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1511 | `llabs` | `0x766E8` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1512 | `lldiv` | `0x766F4` | 44 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1518 | `longjmp` | `0x76720` | 236 | UnwindData |  |
| 1537 | `perror` | `0x7680C` | 173 | UnwindData |  |
| 1547 | `qsort` | `0x768C0` | 80 | UnwindData |  |
| 1548 | `qsort_s` | `0x76C70` | 80 | UnwindData |  |
| 1550 | `rand` | `0x77080` | 43 | UnwindData |  |
| 1571 | `srand` | `0x770AC` | 22 | UnwindData |  |
| 1560 | `setlocale` | `0x770C4` | 623 | UnwindData |  |
| 1582 | `strerror` | `0x77334` | 154 | UnwindData |  |
| 1583 | `strerror_s` | `0x773D0` | 142 | UnwindData |  |
| 372 | `__STRINGTOLD_L` | `0x7BB44` | 117 | UnwindData |  |
| 1 | `$I10_OUTPUT` | `0x7DCAC` | 2,764 | UnwindData |  |
| 517 | `_cabs` | `0x7E9B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 527 | `_chgsign` | `0x7E9C0` | 36 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 528 | `_chgsignf` | `0x7E9E4` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 532 | `_clearfp` | `0x7EA00` | 80 | UnwindData |  |
| 537 | `_control87` | `0x7EA50` | 656 | UnwindData |  |
| 538 | `_controlfp` | `0x7ECE0` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 626 | `_fpreset` | `0x7ECEC` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1054 | `_set_controlfp` | `0x7ECF8` | 52 | UnwindData |  |
| 1112 | `_statusfp` | `0x7ED2C` | 68 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 539 | `_controlfp_s` | `0x7ED70` | 99 | UnwindData |  |
| 540 | `_copysign` | `0x7EDD4` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 541 | `_copysignf` | `0x7EE0C` | 44 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 618 | `_finite` | `0x7EE38` | 44 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 619 | `_finitef` | `0x7EE64` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 623 | `_fpclass` | `0x7EE7C` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 624 | `_fpclassf` | `0x7EF2C` | 120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 802 | `_isnan` | `0x7EFA4` | 44 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 803 | `_isnanf` | `0x7EFD0` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1004 | `_nextafter` | `0x7EFEC` | 484 | UnwindData |  |
| 1005 | `_nextafterf` | `0x7F1D0` | 393 | UnwindData |  |
| 1039 | `_scalb` | `0x7F35C` | 473 | UnwindData |  |
| 1040 | `_scalbf` | `0x7F538` | 414 | UnwindData |  |
| 625 | `_fpieee_flt` | `0x7F6D8` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 720 | `_hypot` | `0x7F6F4` | 610 | UnwindData |  |
| 721 | `_hypotf` | `0x7F958` | 326 | UnwindData |  |
| 827 | `_j0` | `0x7FAA0` | 571 | UnwindData |  |
| 828 | `_j1` | `0x7FCDC` | 614 | UnwindData |  |
| 829 | `_jn` | `0x7FF44` | 382 | UnwindData |  |
| 1400 | `_y0` | `0x800C4` | 632 | UnwindData |  |
| 1401 | `_y1` | `0x8033C` | 657 | UnwindData |  |
| 1402 | `_yn` | `0x805D0` | 221 | UnwindData |  |
| 842 | `_logb` | `0x80700` | 285 | UnwindData |  |
| 843 | `_logbf` | `0x80820` | 229 | UnwindData |  |
| 1405 | `acos` | `0x80908` | 742 | UnwindData |  |
| 1406 | `acosf` | `0x80BF0` | 652 | UnwindData |  |
| 1409 | `asin` | `0x80E7C` | 711 | UnwindData |  |
| 1410 | `asinf` | `0x81144` | 596 | UnwindData |  |
| 1411 | `atan` | `0x81398` | 606 | UnwindData |  |
| 1412 | `atan2` | `0x815F8` | 1,968 | UnwindData |  |
| 1413 | `atan2f` | `0x81DA8` | 1,158 | UnwindData |  |
| 1414 | `atanf` | `0x82230` | 576 | UnwindData |  |
| 1423 | `ceil` | `0x82470` | 273 | UnwindData |  |
| 1424 | `ceilf` | `0x82584` | 212 | UnwindData |  |
| 1428 | `cos` | `0x82660` | 1,165 | UnwindData |  |
| 1429 | `cosf` | `0x82AF0` | 768 | UnwindData |  |
| 1430 | `cosh` | `0x82DF0` | 938 | UnwindData |  |
| 1431 | `coshf` | `0x832C4` | 705 | UnwindData |  |
| 1434 | `exp` | `0x836B0` | 664 | UnwindData |  |
| 1435 | `expf` | `0x83950` | 344 | UnwindData |  |
| 1436 | `fabs` | `0x83AA8` | 225 | UnwindData |  |
| 1446 | `floor` | `0x83B8C` | 255 | UnwindData |  |
| 1447 | `floorf` | `0x83C8C` | 206 | UnwindData |  |
| 1448 | `fmod` | `0x83D5C` | 1,340 | UnwindData |  |
| 1449 | `fmodf` | `0x84298` | 713 | UnwindData |  |
| 1463 | `frexp` | `0x84564` | 220 | UnwindData |  |
| 1509 | `ldexp` | `0x84640` | 377 | UnwindData |  |
| 1514 | `log` | `0x847C0` | 702 | UnwindData |  |
| 1515 | `log10` | `0x84A80` | 798 | UnwindData |  |
| 1516 | `log10f` | `0x84DA0` | 645 | UnwindData |  |
| 1517 | `logf` | `0x85030` | 597 | UnwindData |  |
| 1535 | `modf` | `0x85288` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1536 | `modff` | `0x85348` | 152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1538 | `pow` | `0x853E0` | 2,993 | UnwindData |  |
| 1539 | `powf` | `0x85FA0` | 2,093 | UnwindData |  |
| 1563 | `sin` | `0x867D0` | 1,165 | UnwindData |  |
| 1564 | `sinf` | `0x86C60` | 893 | UnwindData |  |
| 1565 | `sinh` | `0x86FE0` | 1,015 | UnwindData |  |
| 1566 | `sinhf` | `0x87500` | 726 | UnwindData |  |
| 1569 | `sqrt` | `0x87900` | 256 | UnwindData |  |
| 1570 | `sqrtf` | `0x87A00` | 220 | UnwindData |  |
| 1606 | `tan` | `0x87ADC` | 714 | UnwindData |  |
| 1607 | `tanf` | `0x881E8` | 871 | UnwindData |  |
| 1608 | `tanh` | `0x88678` | 722 | UnwindData |  |
| 1609 | `tanhf` | `0x8894C` | 725 | UnwindData |  |
| 130 | `??_7exception@std@@6B@` | `0x947A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `??_7bad_cast@std@@6B@` | `0x947D0` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `??_7bad_typeid@std@@6B@` | `0x947E8` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `??_7__non_rtti_object@std@@6B@` | `0x94800` | 6,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1311 | `_wctype` | `0x96120` | 15,968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1162 | `_sys_errlist` | `0x99F80` | 161,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 733 | `_iob` | `0xC15A0` | 1,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1169 | `_timezone` | `0xC19E0` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 571 | `_daylight` | `0xC19E4` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 575 | `_dstbias` | `0xC19E8` | 136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1176 | `_tzname` | `0xC1A70` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 882 | `_mbctype` | `0xC1BA0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 861 | `_mbcasemap` | `0xC1CB0` | 1,904 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 383 | `__badioinfo` | `0xC2420` | 408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1010 | `_pctype` | `0xC25B8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1027 | `_pwctype` | `0xC25C0` | 1,096 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 433 | `__mb_cur_max` | `0xC2A08` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 431 | `__lconv` | `0xC2A28` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1163 | `_sys_nerr` | `0xC2AC8` | 968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 339 | `_HUGE` | `0xC2E90` | 9,348 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 381 | `__argc` | `0xC5314` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 382 | `__argv` | `0xC5318` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 479 | `__wargv` | `0xC5320` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 583 | `_environ` | `0xC5328` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1313 | `_wenviron` | `0xC5330` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1011 | `_pgmptr` | `0xC5338` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1348 | `_wpgmptr` | `0xC5340` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 484 | `__winitenv` | `0xC5358` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 424 | `__initenv` | `0xC5360` | 1,632 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 488 | `_acmdln` | `0xC59C0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1264 | `_wcmdln` | `0xC59C8` | 2,444 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 535 | `_commode` | `0xC6354` | 588 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 458 | `__pioinfo` | `0xC65A0` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 622 | `_fmode` | `0xC67A0` | 6,272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 477 | `__unguarded_readlc_active` | `0xC8020` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 463 | `__setlc_active` | `0xC8024` | 0 | Indeterminate |  |
