# Binary Specification: msvcr100.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\msvcr100.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ae3cb6c6afba9a4aa5c85f66023c35338ca579b30326dd02918f9d55259503d5`
* **Total Exported Functions:** 1591

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 103 | `??4?$_SpinWait@$00@details@Concurrency@@QEAAAEAV012@AEBV012@@Z` | `0x1008` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `??4?$_SpinWait@$0A@@details@Concurrency@@QEAAAEAV012@AEBV012@@Z` | `0x1008` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0?$_SpinWait@$00@details@Concurrency@@QEAA@P6AXXZ@Z` | `0x1028` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0?$_SpinWait@$0A@@details@Concurrency@@QEAA@P6AXXZ@Z` | `0x1028` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 200 | `?_SpinOnce@?$_SpinWait@$00@details@Concurrency@@QEAA_NXZ` | `0x103C` | 169 | UnwindData |  |
| 175 | `?_DoYield@?$_SpinWait@$00@details@Concurrency@@IEAAXXZ` | `0x10EC` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `?_Reset@?$_SpinWait@$00@details@Concurrency@@IEAAXXZ` | `0x10F8` | 44 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 198 | `?_ShouldSpinAgain@?$_SpinWait@$00@details@Concurrency@@IEAA_NXZ` | `0x1124` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 199 | `?_ShouldSpinAgain@?$_SpinWait@$0A@@details@Concurrency@@IEAA_NXZ` | `0x1124` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 196 | `?_SetSpinCount@?$_SpinWait@$00@details@Concurrency@@QEAAXI@Z` | `0x1130` | 72 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `?_CheckTaskCollection@_UnrealizedChore@details@Concurrency@@IEAAXXZ` | `0x1178` | 108 | UnwindData |  |
| 145 | `?Id@Context@Concurrency@@SAIXZ` | `0x168C` | 58 | UnwindData |  |
| 157 | `?VirtualProcessorId@Context@Concurrency@@SAIXZ` | `0x16CC` | 59 | UnwindData |  |
| 152 | `?ScheduleGroupId@Context@Concurrency@@SAIXZ` | `0x1710` | 59 | UnwindData |  |
| 125 | `?Block@Context@Concurrency@@SAXXZ` | `0x1754` | 55 | UnwindData |  |
| 158 | `?Yield@Context@Concurrency@@SAXXZ` | `0x1794` | 55 | UnwindData |  |
| 202 | `?_SpinYield@Context@Concurrency@@SAXXZ` | `0x17D4` | 55 | UnwindData |  |
| 147 | `?IsCurrentTaskCollectionCanceling@Context@Concurrency@@SA_NXZ` | `0x1814` | 81 | UnwindData |  |
| 130 | `?CurrentContext@Context@Concurrency@@SAPEAV12@XZ` | `0x186C` | 43 | UnwindData |  |
| 149 | `?Oversubscribe@Context@Concurrency@@SAX_N@Z` | `0x18A0` | 62 | UnwindData |  |
| 117 | `??_F?$_SpinWait@$00@details@Concurrency@@QEAAXXZ` | `0x1F6C` | 3,092 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `??_F?$_SpinWait@$0A@@details@Concurrency@@QEAAXXZ` | `0x1F6C` | 3,092 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | `?_SpinOnce@?$_SpinWait@$0A@@details@Concurrency@@QEAA_NXZ` | `0x2B80` | 728 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `?_DoYield@?$_SpinWait@$0A@@details@Concurrency@@IEAAXXZ` | `0x2E58` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 191 | `?_Reset@?$_SpinWait@$0A@@details@Concurrency@@IEAAXXZ` | `0x2E64` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 197 | `?_SetSpinCount@?$_SpinWait@$0A@@details@Concurrency@@QEAAXI@Z` | `0x2F14` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `?Id@CurrentScheduler@Concurrency@@SAIXZ` | `0x2F34` | 36 | UnwindData |  |
| 137 | `?GetNumberOfVirtualProcessors@CurrentScheduler@Concurrency@@SAIXZ` | `0x2F60` | 36 | UnwindData |  |
| 139 | `?GetPolicy@CurrentScheduler@Concurrency@@SA?AVSchedulerPolicy@2@XZ` | `0x2F8C` | 41 | UnwindData |  |
| 135 | `?Get@CurrentScheduler@Concurrency@@SAPEAVScheduler@2@XZ` | `0x2FBC` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `?Create@CurrentScheduler@Concurrency@@SAXAEBVSchedulerPolicy@2@@Z` | `0x2FC8` | 37 | UnwindData |  |
| 131 | `?Detach@CurrentScheduler@Concurrency@@SAXXZ` | `0x2FF4` | 176 | UnwindData |  |
| 150 | `?RegisterShutdownEvent@CurrentScheduler@Concurrency@@SAXPEAX@Z` | `0x30D4` | 65 | UnwindData |  |
| 129 | `?CreateScheduleGroup@CurrentScheduler@Concurrency@@SAPEAVScheduleGroup@2@XZ` | `0x311C` | 23 | UnwindData |  |
| 153 | `?ScheduleTask@CurrentScheduler@Concurrency@@SAXP6AXPEAX@Z0@Z` | `0x313C` | 47 | UnwindData |  |
| 556 | `_freea` | `0x3174` | 31 | UnwindData |  |
| 557 | `_freea_s` | `0x3174` | 31 | UnwindData |  |
| 144 | `?GetSharedTimerQueue@details@Concurrency@@YAPEAXXZ` | `0x31F4` | 214 | UnwindData |  |
| 34 | `??0event@Concurrency@@QEAA@XZ` | `0x32F8` | 44 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `??1event@Concurrency@@QEAA@XZ` | `0x3324` | 168 | UnwindData |  |
| 266 | `?wait@event@Concurrency@@QEAA_KI@Z` | `0x33D4` | 298 | UnwindData |  |
| 251 | `?reset@event@Concurrency@@QEAAXXZ` | `0x3504` | 135 | UnwindData |  |
| 252 | `?set@event@Concurrency@@QEAAXXZ` | `0x3594` | 367 | UnwindData |  |
| 267 | `?wait_for_multiple@event@Concurrency@@SA_KPEAPEAV12@_K_NI@Z` | `0x370C` | 916 | UnwindData |  |
| 92 | `??1critical_section@Concurrency@@QEAA@XZ` | `0x3F08` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `??1reader_writer_lock@Concurrency@@QEAA@XZ` | `0x3F08` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `??0scheduler_resource_allocation_error@Concurrency@@QEAA@PEBDJ@Z` | `0x4068` | 58 | UnwindData |  |
| 72 | `??0scheduler_resource_allocation_error@Concurrency@@QEAA@J@Z` | `0x40A8` | 64 | UnwindData |  |
| 244 | `?get_error_code@scheduler_resource_allocation_error@Concurrency@@QEBAJXZ` | `0x40F0` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `??0unsupported_os@Concurrency@@QEAA@PEBD@Z` | `0x40FC` | 42 | UnwindData |  |
| 80 | `??0unsupported_os@Concurrency@@QEAA@XZ` | `0x412C` | 50 | UnwindData |  |
| 70 | `??0scheduler_not_attached@Concurrency@@QEAA@PEBD@Z` | `0x4164` | 42 | UnwindData |  |
| 71 | `??0scheduler_not_attached@Concurrency@@QEAA@XZ` | `0x4194` | 50 | UnwindData |  |
| 41 | `??0improper_scheduler_attach@Concurrency@@QEAA@PEBD@Z` | `0x41CC` | 42 | UnwindData |  |
| 42 | `??0improper_scheduler_attach@Concurrency@@QEAA@XZ` | `0x41FC` | 50 | UnwindData |  |
| 43 | `??0improper_scheduler_detach@Concurrency@@QEAA@PEBD@Z` | `0x4234` | 42 | UnwindData |  |
| 44 | `??0improper_scheduler_detach@Concurrency@@QEAA@XZ` | `0x4264` | 50 | UnwindData |  |
| 45 | `??0improper_scheduler_reference@Concurrency@@QEAA@PEBD@Z` | `0x429C` | 42 | UnwindData |  |
| 46 | `??0improper_scheduler_reference@Concurrency@@QEAA@XZ` | `0x42CC` | 50 | UnwindData |  |
| 32 | `??0default_scheduler_exists@Concurrency@@QEAA@PEBD@Z` | `0x4304` | 42 | UnwindData |  |
| 33 | `??0default_scheduler_exists@Concurrency@@QEAA@XZ` | `0x4334` | 50 | UnwindData |  |
| 29 | `??0context_unblock_unbalanced@Concurrency@@QEAA@PEBD@Z` | `0x436C` | 42 | UnwindData |  |
| 30 | `??0context_unblock_unbalanced@Concurrency@@QEAA@XZ` | `0x439C` | 50 | UnwindData |  |
| 27 | `??0context_self_unblock@Concurrency@@QEAA@PEBD@Z` | `0x43D4` | 42 | UnwindData |  |
| 28 | `??0context_self_unblock@Concurrency@@QEAA@XZ` | `0x443C` | 50 | UnwindData |  |
| 63 | `??0missing_wait@Concurrency@@QEAA@PEBD@Z` | `0x4474` | 42 | UnwindData |  |
| 64 | `??0missing_wait@Concurrency@@QEAA@XZ` | `0x44A4` | 50 | UnwindData |  |
| 23 | `??0bad_target@Concurrency@@QEAA@PEBD@Z` | `0x44DC` | 42 | UnwindData |  |
| 24 | `??0bad_target@Concurrency@@QEAA@XZ` | `0x450C` | 50 | UnwindData |  |
| 61 | `??0message_not_found@Concurrency@@QEAA@PEBD@Z` | `0x4544` | 42 | UnwindData |  |
| 62 | `??0message_not_found@Concurrency@@QEAA@XZ` | `0x4574` | 50 | UnwindData |  |
| 47 | `??0invalid_link_target@Concurrency@@QEAA@PEBD@Z` | `0x45AC` | 42 | UnwindData |  |
| 48 | `??0invalid_link_target@Concurrency@@QEAA@XZ` | `0x45DC` | 50 | UnwindData |  |
| 55 | `??0invalid_scheduler_policy_key@Concurrency@@QEAA@PEBD@Z` | `0x4614` | 42 | UnwindData |  |
| 56 | `??0invalid_scheduler_policy_key@Concurrency@@QEAA@XZ` | `0x4644` | 50 | UnwindData |  |
| 59 | `??0invalid_scheduler_policy_value@Concurrency@@QEAA@PEBD@Z` | `0x467C` | 42 | UnwindData |  |
| 60 | `??0invalid_scheduler_policy_value@Concurrency@@QEAA@XZ` | `0x46AC` | 50 | UnwindData |  |
| 57 | `??0invalid_scheduler_policy_thread_specification@Concurrency@@QEAA@PEBD@Z` | `0x46E4` | 42 | UnwindData |  |
| 58 | `??0invalid_scheduler_policy_thread_specification@Concurrency@@QEAA@XZ` | `0x4714` | 50 | UnwindData |  |
| 51 | `??0invalid_operation@Concurrency@@QEAA@PEBD@Z` | `0x474C` | 42 | UnwindData |  |
| 52 | `??0invalid_operation@Concurrency@@QEAA@XZ` | `0x477C` | 50 | UnwindData |  |
| 65 | `??0nested_scheduler_missing_detach@Concurrency@@QEAA@PEBD@Z` | `0x47B4` | 42 | UnwindData |  |
| 66 | `??0nested_scheduler_missing_detach@Concurrency@@QEAA@XZ` | `0x47E4` | 50 | UnwindData |  |
| 67 | `??0operation_timed_out@Concurrency@@QEAA@PEBD@Z` | `0x481C` | 42 | UnwindData |  |
| 68 | `??0operation_timed_out@Concurrency@@QEAA@XZ` | `0x484C` | 50 | UnwindData |  |
| 49 | `??0invalid_multiple_scheduling@Concurrency@@QEAA@PEBD@Z` | `0x4884` | 42 | UnwindData |  |
| 50 | `??0invalid_multiple_scheduling@Concurrency@@QEAA@XZ` | `0x48B4` | 50 | UnwindData |  |
| 53 | `??0invalid_oversubscribe_operation@Concurrency@@QEAA@PEBD@Z` | `0x48EC` | 42 | UnwindData |  |
| 54 | `??0invalid_oversubscribe_operation@Concurrency@@QEAA@XZ` | `0x491C` | 50 | UnwindData |  |
| 39 | `??0improper_lock@Concurrency@@QEAA@PEBD@Z` | `0x4954` | 42 | UnwindData |  |
| 40 | `??0improper_lock@Concurrency@@QEAA@XZ` | `0x4984` | 50 | UnwindData |  |
| 77 | `??0task_canceled@details@Concurrency@@QEAA@PEBD@Z` | `0x49BC` | 42 | UnwindData |  |
| 78 | `??0task_canceled@details@Concurrency@@QEAA@XZ` | `0x49EC` | 50 | UnwindData |  |
| 217 | `?_Value@_SpinCount@details@Concurrency@@SAIXZ` | `0x7E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `??0_NonReentrantBlockingLock@details@Concurrency@@QEAA@XZ` | `0x7E60` | 30 | UnwindData |  |
| 10 | `??0_ReentrantBlockingLock@details@Concurrency@@QEAA@XZ` | `0x7E60` | 30 | UnwindData |  |
| 207 | `?_TryAcquire@_NonReentrantBlockingLock@details@Concurrency@@QEAA_NXZ` | `0x7E84` | 20 | UnwindData |  |
| 208 | `?_TryAcquire@_ReentrantBlockingLock@details@Concurrency@@QEAA_NXZ` | `0x7E84` | 20 | UnwindData |  |
| 183 | `?_Release@_NonReentrantBlockingLock@details@Concurrency@@QEAAXXZ` | `0x7EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `?_Release@_ReentrantBlockingLock@details@Concurrency@@QEAAXXZ` | `0x7EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `??1_NonReentrantBlockingLock@details@Concurrency@@QEAA@XZ` | `0x7EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `??1_ReentrantBlockingLock@details@Concurrency@@QEAA@XZ` | `0x7EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `??0_ReentrantLock@details@Concurrency@@QEAA@XZ` | `0x7EC0` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 160 | `?_Acquire@_NonReentrantBlockingLock@details@Concurrency@@QEAAXXZ` | `0x7ED4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 162 | `?_Acquire@_ReentrantBlockingLock@details@Concurrency@@QEAAXXZ` | `0x7ED4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 163 | `?_Acquire@_ReentrantLock@details@Concurrency@@QEAAXXZ` | `0x7EE4` | 85 | UnwindData |  |
| 209 | `?_TryAcquire@_ReentrantLock@details@Concurrency@@QEAA_NXZ` | `0x7F40` | 48 | UnwindData |  |
| 186 | `?_Release@_ReentrantLock@details@Concurrency@@QEAAXXZ` | `0x7F78` | 48 | UnwindData |  |
| 8 | `??0_NonReentrantPPLLock@details@Concurrency@@QEAA@XZ` | `0x7FB0` | 36 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `??0critical_section@Concurrency@@QEAA@XZ` | `0x7FB0` | 36 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 161 | `?_Acquire@_NonReentrantPPLLock@details@Concurrency@@QEAAXPEAX@Z` | `0x7FD4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | `?_Release@_NonReentrantPPLLock@details@Concurrency@@QEAAXXZ` | `0x7FE4` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `??0_ReentrantPPLLock@details@Concurrency@@QEAA@XZ` | `0x7FF0` | 44 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 164 | `?_Acquire@_ReentrantPPLLock@details@Concurrency@@QEAAXPEAX@Z` | `0x801C` | 83 | UnwindData |  |
| 187 | `?_Release@_ReentrantPPLLock@details@Concurrency@@QEAAXXZ` | `0x8078` | 26 | UnwindData |  |
| 9 | `??0_ReaderWriterLock@details@Concurrency@@QEAA@XZ` | `0x8098` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 165 | `?_AcquireRead@_ReaderWriterLock@details@Concurrency@@QEAAXXZ` | `0x80B0` | 56 | UnwindData |  |
| 188 | `?_ReleaseRead@_ReaderWriterLock@details@Concurrency@@QEAAXXZ` | `0x80F0` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `?_AcquireWrite@_ReaderWriterLock@details@Concurrency@@QEAAXXZ` | `0x80FC` | 55 | UnwindData |  |
| 189 | `?_ReleaseWrite@_ReaderWriterLock@details@Concurrency@@QEAAXXZ` | `0x813C` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 210 | `?_TryAcquireWrite@_ReaderWriterLock@details@Concurrency@@QEAA_NXZ` | `0x8150` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `??0_Scoped_lock@_NonReentrantPPLLock@details@Concurrency@@QEAA@AEAV123@@Z` | `0x8270` | 121 | UnwindData |  |
| 14 | `??0_Scoped_lock@_ReentrantPPLLock@details@Concurrency@@QEAA@AEAV123@@Z` | `0x82F0` | 118 | UnwindData |  |
| 85 | `??1_Scoped_lock@_ReentrantPPLLock@details@Concurrency@@QEAA@XZ` | `0x836C` | 29 | UnwindData |  |
| 249 | `?native_handle@critical_section@Concurrency@@QEAAAEAV12@XZ` | `0x8390` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 245 | `?lock@critical_section@Concurrency@@QEAAXXZ` | `0x839C` | 97 | UnwindData |  |
| 259 | `?try_lock@critical_section@Concurrency@@QEAA_NXZ` | `0x8404` | 190 | UnwindData |  |
| 263 | `?unlock@critical_section@Concurrency@@QEAAXXZ` | `0x84C8` | 131 | UnwindData |  |
| 74 | `??0scoped_lock@critical_section@Concurrency@@QEAA@AEAV12@@Z` | `0x8798` | 122 | UnwindData |  |
| 84 | `??1_Scoped_lock@_NonReentrantPPLLock@details@Concurrency@@QEAA@XZ` | `0x8818` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `??1scoped_lock@critical_section@Concurrency@@QEAA@XZ` | `0x8818` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `??0reader_writer_lock@Concurrency@@QEAA@XZ` | `0x8828` | 44 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 246 | `?lock@reader_writer_lock@Concurrency@@QEAAXXZ` | `0x8854` | 97 | UnwindData |  |
| 260 | `?try_lock@reader_writer_lock@Concurrency@@QEAA_NXZ` | `0x88BC` | 220 | UnwindData |  |
| 247 | `?lock_read@reader_writer_lock@Concurrency@@QEAAXXZ` | `0x89A0` | 286 | UnwindData |  |
| 261 | `?try_lock_read@reader_writer_lock@Concurrency@@QEAA_NXZ` | `0x8AC4` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 264 | `?unlock@reader_writer_lock@Concurrency@@QEAAXXZ` | `0x8AE4` | 176 | UnwindData |  |
| 75 | `??0scoped_lock@reader_writer_lock@Concurrency@@QEAA@AEAV12@@Z` | `0x8E98` | 122 | UnwindData |  |
| 76 | `??0scoped_lock_read@reader_writer_lock@Concurrency@@QEAA@AEAV12@@Z` | `0x8F18` | 29 | UnwindData |  |
| 97 | `??1scoped_lock@reader_writer_lock@Concurrency@@QEAA@XZ` | `0x8F3C` | 340 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `??1scoped_lock_read@reader_writer_lock@Concurrency@@QEAA@XZ` | `0x8F3C` | 340 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `??_Fbad_cast@std@@QEAAXXZ` | `0x9090` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `??4__non_rtti_object@std@@QEAAAEAV01@AEBV01@@Z` | `0x90A4` | 23 | UnwindData |  |
| 107 | `??4bad_cast@std@@QEAAAEAV01@AEBV01@@Z` | `0x90A4` | 23 | UnwindData |  |
| 108 | `??4bad_typeid@std@@QEAAAEAV01@AEBV01@@Z` | `0x90A4` | 23 | UnwindData |  |
| 120 | `??_Fbad_typeid@std@@QEAAXXZ` | `0x90C4` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `?GetOSVersion@Concurrency@@YA?AW4OSVersion@IResourceManager@1@XZ` | `0x90D8` | 133 | UnwindData |  |
| 128 | `?CreateResourceManager@Concurrency@@YAPEAUIResourceManager@1@XZ` | `0x9164` | 251 | UnwindData |  |
| 141 | `?GetProcessorCount@Concurrency@@YAIXZ` | `0x9268` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `?GetProcessorNodeCount@Concurrency@@YAIXZ` | `0x9274` | 139 | UnwindData |  |
| 143 | `?GetSchedulerId@Concurrency@@YAIXZ` | `0x9308` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `?GetExecutionContextId@Concurrency@@YAIXZ` | `0x9320` | 23,176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `?Create@Scheduler@Concurrency@@SAPEAV12@AEBVSchedulerPolicy@2@@Z` | `0xEDA8` | 41 | UnwindData |  |
| 155 | `?SetDefaultSchedulerPolicy@Scheduler@Concurrency@@SAXAEBVSchedulerPolicy@2@@Z` | `0xEDD8` | 251 | UnwindData |  |
| 151 | `?ResetDefaultSchedulerPolicy@Scheduler@Concurrency@@SAXXZ` | `0xEEDC` | 117 | UnwindData |  |
| 5 | `??0SchedulerPolicy@Concurrency@@QEAA@XZ` | `0x11AD8` | 28 | UnwindData |  |
| 6 | `??0SchedulerPolicy@Concurrency@@QEAA@_KZZ` | `0x11AFC` | 49 | UnwindData |  |
| 4 | `??0SchedulerPolicy@Concurrency@@QEAA@AEBV01@@Z` | `0x11D48` | 60 | UnwindData |  |
| 105 | `??4SchedulerPolicy@Concurrency@@QEAAAEAV01@AEBV01@@Z` | `0x11D8C` | 35 | UnwindData |  |
| 81 | `??1SchedulerPolicy@Concurrency@@QEAA@XZ` | `0x11DB8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `?GetPolicyValue@SchedulerPolicy@Concurrency@@QEBAIW4PolicyElementKey@2@@Z` | `0x11DC8` | 75 | UnwindData |  |
| 156 | `?SetPolicyValue@SchedulerPolicy@Concurrency@@QEAAIW4PolicyElementKey@2@I@Z` | `0x11E1C` | 205 | UnwindData |  |
| 154 | `?SetConcurrencyLimits@SchedulerPolicy@Concurrency@@QEAAXII@Z` | `0x11EF0` | 269 | UnwindData |  |
| 124 | `?Alloc@Concurrency@@YAPEAX_K@Z` | `0x15D50` | 142 | UnwindData |  |
| 134 | `?Free@Concurrency@@YAXPEAX@Z` | `0x15DE4` | 68 | UnwindData |  |
| 194 | `?_Schedule@_StructuredTaskCollection@details@Concurrency@@QEAAXPEAV_UnrealizedChore@23@@Z` | `0x160E8` | 136 | UnwindData |  |
| 192 | `?_RunAndWait@_StructuredTaskCollection@details@Concurrency@@QEAA?AW4_TaskCollectionStatus@23@PEAV_UnrealizedChore@23@@Z` | `0x161A0` | 531 | UnwindData |  |
| 159 | `?_Abort@_StructuredTaskCollection@details@Concurrency@@AEAAXXZ` | `0x163BC` | 314 | UnwindData |  |
| 167 | `?_Cancel@_StructuredTaskCollection@details@Concurrency@@QEAAXXZ` | `0x164FC` | 248 | UnwindData |  |
| 177 | `?_IsCanceling@_StructuredTaskCollection@details@Concurrency@@QEAA_NXZ` | `0x165FC` | 145 | UnwindData |  |
| 16 | `??0_TaskCollection@details@Concurrency@@QEAA@XZ` | `0x167C0` | 280 | UnwindData |  |
| 87 | `??1_TaskCollection@details@Concurrency@@QEAA@XZ` | `0x1698C` | 199 | UnwindData |  |
| 195 | `?_Schedule@_TaskCollection@details@Concurrency@@QEAAXPEAV_UnrealizedChore@23@@Z` | `0x16F70` | 385 | UnwindData |  |
| 193 | `?_RunAndWait@_TaskCollection@details@Concurrency@@QEAA?AW4_TaskCollectionStatus@23@PEAV_UnrealizedChore@23@@Z` | `0x17220` | 1,044 | UnwindData |  |
| 168 | `?_Cancel@_TaskCollection@details@Concurrency@@QEAAXXZ` | `0x1798C` | 476 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 178 | `?_IsCanceling@_TaskCollection@details@Concurrency@@QEAA_NXZ` | `0x17B68` | 253 | UnwindData |  |
| 17 | `??0_Timer@details@Concurrency@@IEAA@I_N@Z` | `0x19448` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 203 | `?_Start@_Timer@details@Concurrency@@IEAAXXZ` | `0x19468` | 170 | UnwindData |  |
| 88 | `??1_Timer@details@Concurrency@@IEAA@XZ` | `0x19518` | 31 | UnwindData |  |
| 204 | `?_Stop@_Timer@details@Concurrency@@IEAAXXZ` | `0x19540` | 61 | UnwindData |  |
| 265 | `?wait@Concurrency@@YAXI@Z` | `0x19584` | 113 | UnwindData |  |
| 133 | `?EnableTracing@Concurrency@@YAJXZ` | `0x198EC` | 160 | UnwindData |  |
| 132 | `?DisableTracing@Concurrency@@YAJXZ` | `0x19994` | 126 | UnwindData |  |
| 206 | `?_Trace_ppl_function@Concurrency@@YAXAEBU_GUID@@EW4ConcRT_EventType@1@@Z` | `0x19A18` | 173 | UnwindData |  |
| 213 | `?_UnderlyingYield@details@Concurrency@@YAXXZ` | `0x1DE00` | 62 | UnwindData |  |
| 170 | `?_ConcRT_Assert@details@Concurrency@@YAXPEBD0H@Z` | `0x1DF50` | 400 | UnwindData |  |
| 171 | `?_ConcRT_CoreAssert@details@Concurrency@@YAXPEBD0H@Z` | `0x1E0E8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 172 | `?_ConcRT_DumpMessage@details@Concurrency@@YAXPEB_WZZ` | `0x1E0F8` | 127 | UnwindData |  |
| 173 | `?_ConcRT_Trace@details@Concurrency@@YAXHPEB_WZZ` | `0x1E180` | 207 | UnwindData |  |
| 15 | `??0_SpinLock@details@Concurrency@@QEAA@AECJ@Z` | `0x1E258` | 81 | UnwindData |  |
| 86 | `??1_SpinLock@details@Concurrency@@QEAA@XZ` | `0x1E2B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 148 | `?Log2@details@Concurrency@@YAK_K@Z` | `0x1E2C0` | 3,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 235 | `?_set_new_handler@@YAP6AH_K@ZP6AH0@Z@Z` | `0x1F230` | 79 | UnwindData |  |
| 234 | `?_set_new_handler@@YAP6AH_K@ZH@Z` | `0x1F288` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 232 | `?_query_new_handler@@YAP6AH_K@ZXZ` | `0x1F298` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 436 | `_callnewh` | `0x1F2AC` | 51 | UnwindData |  |
| 253 | `?set_new_handler@@YAP6AXXZP6AXXZ@Z` | `0x1F2E8` | 18 | UnwindData |  |
| 236 | `?_set_new_mode@@YAHH@Z` | `0x1F300` | 51 | UnwindData |  |
| 233 | `?_query_new_mode@@YAHXZ` | `0x1F33C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 977 | `_set_error_mode` | `0x1F34C` | 64 | UnwindData |  |
| 379 | `__set_app_type` | `0x1F394` | 1,556 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `?__ExceptionPtrCreate@@YAXPEAX@Z` | `0x1F9A8` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 219 | `?__ExceptionPtrCompare@@YA_NPEBX0@Z` | `0x1F9C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 225 | `?__ExceptionPtrRethrow@@YAXPEBX@Z` | `0x1F9D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 224 | `?__ExceptionPtrDestroy@@YAXPEAX@Z` | `0x1F9E0` | 50 | UnwindData |  |
| 220 | `?__ExceptionPtrCopy@@YAXPEAXPEBX@Z` | `0x1FD4C` | 58 | UnwindData |  |
| 218 | `?__ExceptionPtrAssign@@YAXPEAXPEBX@Z` | `0x1FD8C` | 1,060 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 223 | `?__ExceptionPtrCurrentException@@YAXPEAX@Z` | `0x201B0` | 88 | UnwindData |  |
| 221 | `?__ExceptionPtrCopyException@@YAXPEAXPEBX1@Z` | `0x20210` | 89 | UnwindData |  |
| 382 | `__setusermatherr` | `0x202F4` | 29 | UnwindData |  |
| 647 | `_initterm` | `0x209CC` | 51 | UnwindData |  |
| 648 | `_initterm_e` | `0x20A08` | 57 | UnwindData |  |
| 605 | `_get_wpgmptr` | `0x20A48` | 54 | UnwindData |  |
| 598 | `_get_pgmptr` | `0x20A84` | 54 | UnwindData |  |
| 1353 | `exit` | `0x20D20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 513 | `_exit` | `0x20D30` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 438 | `_cexit` | `0x20D44` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 434 | `_c_exit` | `0x20D58` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 415 | `_amsg_exit` | `0x20D70` | 38 | UnwindData |  |
| 401 | `__wgetmainargs` | `0x2107C` | 155 | UnwindData |  |
| 340 | `__getmainargs` | `0x21120` | 110 | UnwindData |  |
| 357 | `__p__acmdln` | `0x2131C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 371 | `__p__wcmdln` | `0x2132C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 351 | `__p___argc` | `0x2133C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 352 | `__p___argv` | `0x2134C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 355 | `__p___wargv` | `0x2135C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 358 | `__p__commode` | `0x2136C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 359 | `__p__daylight` | `0x2137C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 360 | `__p__dstbias` | `0x21388` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 361 | `__p__environ` | `0x21394` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 372 | `__p__wenviron` | `0x213A4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 362 | `__p__fmode` | `0x213B4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 353 | `__p___initenv` | `0x213C4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 356 | `__p___winitenv` | `0x213D4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 342 | `__iob_func` | `0x213E4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 363 | `__p__iob` | `0x213E4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 365 | `__p__mbctype` | `0x213F4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 364 | `__p__mbcasemap` | `0x21404` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 354 | `__p___mb_cur_max` | `0x21414` | 59 | UnwindData |  |
| 366 | `__p__pctype` | `0x21458` | 59 | UnwindData |  |
| 368 | `__p__pwctype` | `0x2149C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 367 | `__p__pgmptr` | `0x214AC` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 373 | `__p__wpgmptr` | `0x214BC` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 369 | `__p__timezone` | `0x214CC` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 370 | `__p__tzname` | `0x214D8` | 348 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1116 | `_unlock` | `0x21634` | 268 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 759 | `_lock` | `0x21740` | 68 | UnwindData |  |
| 500 | `_endthread` | `0x21B74` | 52 | UnwindData |  |
| 429 | `_beginthread` | `0x21C5C` | 247 | UnwindData |  |
| 501 | `_endthreadex` | `0x21D5C` | 35 | UnwindData |  |
| 430 | `_beginthreadex` | `0x21E44` | 242 | UnwindData |  |
| 499 | `_encoded_null` | `0x21F3C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 333 | `__fls_getvalue` | `0x21F4C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 338 | `__get_flsindex` | `0x21F5C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 339 | `__get_tlsindex` | `0x21F5C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 334 | `__fls_setvalue` | `0x21F6C` | 60 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 646 | `_initptd` | `0x21FA8` | 181 | UnwindData |  |
| 621 | `_getptd` | `0x220F0` | 36 | UnwindData |  |
| 558 | `_freefls` | `0x2211C` | 307 | UnwindData |  |
| 388 | `__threadid` | `0x2229C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 387 | `__threadhandle` | `0x222AC` | 3,884 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1337 | `atoi` | `0x231D8` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1338 | `atol` | `0x231D8` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 424 | `_atoi_l` | `0x231EC` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 425 | `_atol_l` | `0x231EC` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 422 | `_atoi64` | `0x23200` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 423 | `_atoi64_l` | `0x23214` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1073 | `_swab` | `0x23228` | 88 | UnwindData |  |
| 1311 | `_wtoi` | `0x23424` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1315 | `_wtol` | `0x23424` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1314 | `_wtoi_l` | `0x23438` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1316 | `_wtol_l` | `0x23438` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1312 | `_wtoi64` | `0x2344C` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1313 | `_wtoi64_l` | `0x23460` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 743 | `_itoa` | `0x234D0` | 42 | UnwindData |  |
| 770 | `_ltoa` | `0x23500` | 40 | UnwindData |  |
| 1102 | `_ultoa` | `0x23530` | 26 | UnwindData |  |
| 642 | `_i64toa` | `0x235B0` | 43 | UnwindData |  |
| 1098 | `_ui64toa` | `0x235E4` | 332 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 744 | `_itoa_s` | `0x23730` | 39 | UnwindData |  |
| 771 | `_ltoa_s` | `0x23760` | 34 | UnwindData |  |
| 1103 | `_ultoa_s` | `0x23788` | 19 | UnwindData |  |
| 643 | `_i64toa_s` | `0x238A0` | 35 | UnwindData |  |
| 1099 | `_ui64toa_s` | `0x238CC` | 19 | UnwindData |  |
| 745 | `_itow` | `0x2395C` | 42 | UnwindData |  |
| 772 | `_ltow` | `0x2398C` | 40 | UnwindData |  |
| 1104 | `_ultow` | `0x239BC` | 26 | UnwindData |  |
| 644 | `_i64tow` | `0x23A58` | 43 | UnwindData |  |
| 1100 | `_ui64tow` | `0x23A8C` | 26 | UnwindData |  |
| 746 | `_itow_s` | `0x23BC0` | 39 | UnwindData |  |
| 773 | `_ltow_s` | `0x23BF0` | 34 | UnwindData |  |
| 1105 | `_ultow_s` | `0x23C18` | 19 | UnwindData |  |
| 645 | `_i64tow_s` | `0x23D4C` | 35 | UnwindData |  |
| 1101 | `_ui64tow_s` | `0x23D78` | 19 | UnwindData |  |
| 617 | `_getdrives` | `0x23D94` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 614 | `_getdiskfree` | `0x23DA4` | 163 | UnwindData |  |
| 528 | `_findclose` | `0x23E50` | 37 | UnwindData |  |
| 529 | `_findfirst32` | `0x23F10` | 325 | UnwindData |  |
| 533 | `_findnext32` | `0x2405C` | 287 | UnwindData |  |
| 531 | `_findfirst64` | `0x24184` | 340 | UnwindData |  |
| 535 | `_findnext64` | `0x242E0` | 302 | UnwindData |  |
| 532 | `_findfirst64i32` | `0x244A8` | 328 | UnwindData |  |
| 536 | `_findnext64i32` | `0x245F8` | 290 | UnwindData |  |
| 530 | `_findfirst32i64` | `0x24720` | 337 | UnwindData |  |
| 534 | `_findnext32i64` | `0x24878` | 299 | UnwindData |  |
| 984 | `_seterrormode` | `0x249AC` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 991 | `_sleep` | `0x249BC` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 428 | `_beep` | `0x249D4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1242 | `_wfindfirst32` | `0x249E4` | 325 | UnwindData |  |
| 1246 | `_wfindnext32` | `0x24B30` | 287 | UnwindData |  |
| 1244 | `_wfindfirst64` | `0x24C58` | 340 | UnwindData |  |
| 1248 | `_wfindnext64` | `0x24DB4` | 302 | UnwindData |  |
| 1245 | `_wfindfirst64i32` | `0x24EE8` | 328 | UnwindData |  |
| 1249 | `_wfindnext64i32` | `0x25038` | 290 | UnwindData |  |
| 1243 | `_wfindfirst32i64` | `0x25160` | 337 | UnwindData |  |
| 1247 | `_wfindnext32i64` | `0x252B8` | 299 | UnwindData |  |
| 405 | `_access_s` | `0x253EC` | 128 | UnwindData |  |
| 404 | `_access` | `0x25474` | 18 | UnwindData |  |
| 447 | `_chmod` | `0x2548C` | 115 | UnwindData |  |
| 443 | `_chdir` | `0x25508` | 301 | UnwindData |  |
| 504 | `_errno` | `0x2568C` | 32 | UnwindData |  |
| 331 | `__doserrno` | `0x256B4` | 32 | UnwindData |  |
| 492 | `_dosmaperr` | `0x256DC` | 70 | UnwindData |  |
| 976 | `_set_errno` | `0x25728` | 58 | UnwindData |  |
| 592 | `_get_errno` | `0x25768` | 59 | UnwindData |  |
| 975 | `_set_doserrno` | `0x257AC` | 58 | UnwindData |  |
| 590 | `_get_doserrno` | `0x257EC` | 59 | UnwindData |  |
| 616 | `_getdrive` | `0x25830` | 239 | UnwindData |  |
| 444 | `_chdrive` | `0x25928` | 156 | UnwindData |  |
| 576 | `_fullpath` | `0x259CC` | 299 | UnwindData |  |
| 613 | `_getdcwd_nolock` | `0x25B6C` | 299 | UnwindData |  |
| 611 | `_getcwd` | `0x25CA0` | 66 | UnwindData |  |
| 612 | `_getdcwd` | `0x25CE8` | 79 | UnwindData |  |
| 620 | `_getpid` | `0x25D40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 916 | `_mkdir` | `0x25D50` | 49 | UnwindData |  |
| 1474 | `rename` | `0x25D88` | 47 | UnwindData |  |
| 953 | `_rmdir` | `0x25DC0` | 47 | UnwindData |  |
| 1028 | `_stat32` | `0x25EE8` | 1,270 | UnwindData |  |
| 1030 | `_stat64` | `0x263E4` | 1,260 | UnwindData |  |
| 1031 | `_stat64i32` | `0x268D8` | 1,278 | UnwindData |  |
| 1029 | `_stat32i64` | `0x26DDC` | 1,252 | UnwindData |  |
| 1473 | `remove` | `0x272C8` | 47 | UnwindData |  |
| 1114 | `_unlink` | `0x27300` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1178 | `_waccess_s` | `0x2730C` | 128 | UnwindData |  |
| 1177 | `_waccess` | `0x27394` | 18 | UnwindData |  |
| 1182 | `_wchdir` | `0x273AC` | 331 | UnwindData |  |
| 1183 | `_wchmod` | `0x27500` | 115 | UnwindData |  |
| 1255 | `_wfullpath` | `0x2757C` | 308 | UnwindData |  |
| 1258 | `_wgetdcwd_nolock` | `0x276B8` | 337 | UnwindData |  |
| 1256 | `_wgetcwd` | `0x27810` | 66 | UnwindData |  |
| 1257 | `_wgetdcwd` | `0x27858` | 79 | UnwindData |  |
| 1263 | `_wmkdir` | `0x278B0` | 49 | UnwindData |  |
| 1277 | `_wrename` | `0x278E8` | 47 | UnwindData |  |
| 1279 | `_wrmdir` | `0x27920` | 47 | UnwindData |  |
| 1297 | `_wstat32` | `0x27B1C` | 1,121 | UnwindData |  |
| 1299 | `_wstat64` | `0x27F84` | 1,115 | UnwindData |  |
| 1300 | `_wstat64i32` | `0x283E8` | 1,133 | UnwindData |  |
| 1298 | `_wstat32i64` | `0x2885C` | 1,103 | UnwindData |  |
| 1276 | `_wremove` | `0x28CB4` | 47 | UnwindData |  |
| 1317 | `_wunlink` | `0x28CEC` | 1,924 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 505 | `_execl` | `0x29470` | 165 | UnwindData |  |
| 506 | `_execle` | `0x2951C` | 180 | UnwindData |  |
| 507 | `_execlp` | `0x295D8` | 164 | UnwindData |  |
| 508 | `_execlpe` | `0x29684` | 180 | UnwindData |  |
| 509 | `_execv` | `0x29740` | 69 | UnwindData |  |
| 510 | `_execve` | `0x29818` | 635 | UnwindData |  |
| 511 | `_execvp` | `0x29A9C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 512 | `_execvpe` | `0x29AAC` | 783 | UnwindData |  |
| 615 | `_getdllprocaddr` | `0x29DC4` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 753 | `_loaddll` | `0x29DEC` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1115 | `_unloaddll` | `0x29DFC` | 32 | UnwindData |  |
| 1012 | `_spawnl` | `0x29E24` | 173 | UnwindData |  |
| 1013 | `_spawnle` | `0x29ED8` | 188 | UnwindData |  |
| 1014 | `_spawnlp` | `0x29F9C` | 170 | UnwindData |  |
| 1015 | `_spawnlpe` | `0x2A04C` | 188 | UnwindData |  |
| 1016 | `_spawnv` | `0x2A110` | 69 | UnwindData |  |
| 1017 | `_spawnve` | `0x2A1F0` | 646 | UnwindData |  |
| 1018 | `_spawnvp` | `0x2A47C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1019 | `_spawnvpe` | `0x2A48C` | 718 | UnwindData |  |
| 1525 | `system` | `0x2A760` | 264 | UnwindData |  |
| 478 | `_cwait` | `0x2A870` | 179 | UnwindData |  |
| 1233 | `_wexecl` | `0x2B174` | 168 | UnwindData |  |
| 1234 | `_wexecle` | `0x2B224` | 183 | UnwindData |  |
| 1235 | `_wexeclp` | `0x2B2E4` | 167 | UnwindData |  |
| 1236 | `_wexeclpe` | `0x2B394` | 183 | UnwindData |  |
| 1237 | `_wexecv` | `0x2B454` | 71 | UnwindData |  |
| 1238 | `_wexecve` | `0x2B530` | 636 | UnwindData |  |
| 1239 | `_wexecvp` | `0x2B7B4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1240 | `_wexecvpe` | `0x2B7C4` | 626 | UnwindData |  |
| 1287 | `_wspawnl` | `0x2BA3C` | 176 | UnwindData |  |
| 1288 | `_wspawnle` | `0x2BAF4` | 191 | UnwindData |  |
| 1289 | `_wspawnlp` | `0x2BBBC` | 173 | UnwindData |  |
| 1290 | `_wspawnlpe` | `0x2BC70` | 191 | UnwindData |  |
| 1291 | `_wspawnv` | `0x2BD38` | 71 | UnwindData |  |
| 1292 | `_wspawnve` | `0x2BE1C` | 653 | UnwindData |  |
| 1293 | `_wspawnvp` | `0x2C0B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1294 | `_wspawnvpe` | `0x2C0C0` | 647 | UnwindData |  |
| 1305 | `_wsystem` | `0x2C350` | 264 | UnwindData |  |
| 791 | `_mbclen_l` | `0x2C460` | 45 | UnwindData |  |
| 790 | `_mbclen` | `0x2C494` | 45 | UnwindData |  |
| 825 | `_mbsinc_l` | `0x2C4C8` | 39 | UnwindData |  |
| 824 | `_mbsinc` | `0x2C4F8` | 66 | UnwindData |  |
| 875 | `_mbsninc_l` | `0x2C540` | 34 | UnwindData |  |
| 874 | `_mbsninc` | `0x2C568` | 35 | UnwindData |  |
| 793 | `_mbctohira_l` | `0x2C594` | 55 | UnwindData |  |
| 792 | `_mbctohira` | `0x2C5D4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 795 | `_mbctokata_l` | `0x2C5E4` | 41 | UnwindData |  |
| 794 | `_mbctokata` | `0x2C614` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1358 | `feof` | `0x2C624` | 40 | UnwindData |  |
| 1359 | `ferror` | `0x2C654` | 40 | UnwindData |  |
| 1361 | `fgetc` | `0x2C684` | 260 | UnwindData |  |
| 1394 | `getc` | `0x2C684` | 260 | UnwindData |  |
| 606 | `_getc_nolock` | `0x2C790` | 37 | UnwindData |  |
| 521 | `_fgetchar` | `0x2C7BC` | 21 | UnwindData |  |
| 1395 | `getchar` | `0x2C7BC` | 21 | UnwindData |  |
| 1363 | `fgets` | `0x2C7D8` | 359 | UnwindData |  |
| 522 | `_fgetwc_nolock` | `0x2C948` | 506 | UnwindData |  |
| 1364 | `fgetwc` | `0x2CB48` | 92 | UnwindData |  |
| 1400 | `getwc` | `0x2CBAC` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1365 | `fgetws` | `0x2CBB8` | 205 | UnwindData |  |
| 523 | `_fgetwchar` | `0x2CC8C` | 21 | UnwindData |  |
| 1401 | `getwchar` | `0x2CC8C` | 21 | UnwindData |  |
| 527 | `_fileno` | `0x2CCA8` | 38 | UnwindData |  |
| 1374 | `fputc` | `0x2CCD4` | 278 | UnwindData |  |
| 1462 | `putc` | `0x2CCD4` | 278 | UnwindData |  |
| 1375 | `fputs` | `0x2CDF0` | 305 | UnwindData |  |
| 550 | `_fputchar` | `0x2CF28` | 29 | UnwindData |  |
| 1463 | `putchar` | `0x2CF28` | 29 | UnwindData |  |
| 551 | `_fputwc_nolock` | `0x2CF4C` | 511 | UnwindData |  |
| 1376 | `fputwc` | `0x2D154` | 101 | UnwindData |  |
| 1465 | `putwc` | `0x2D1C0` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1377 | `fputws` | `0x2D1CC` | 181 | UnwindData |  |
| 552 | `_fputwchar` | `0x2D288` | 31 | UnwindData |  |
| 1466 | `putwchar` | `0x2D288` | 31 | UnwindData |  |
| 524 | `_filbuf` | `0x2D2B0` | 338 | UnwindData |  |
| 760 | `_lock_file` | `0x2D66C` | 99 | UnwindData |  |
| 1117 | `_unlock_file` | `0x2D710` | 120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 539 | `_flsbuf` | `0x2D788` | 397 | UnwindData |  |
| 1346 | `clearerr_s` | `0x2DF14` | 184 | UnwindData |  |
| 1345 | `clearerr` | `0x2DFD4` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 516 | `_fcloseall` | `0x2DFE0` | 170 | UnwindData |  |
| 515 | `_fclose_nolock` | `0x2E090` | 122 | UnwindData |  |
| 1357 | `fclose` | `0x2E110` | 102 | UnwindData |  |
| 519 | `_fdopen` | `0x2E17C` | 406 | UnwindData |  |
| 520 | `_fflush_nolock` | `0x2E398` | 76 | UnwindData |  |
| 1360 | `fflush` | `0x2E4E0` | 67 | UnwindData |  |
| 540 | `_flushall` | `0x2E52C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1362 | `fgetpos` | `0x2E53C` | 75 | UnwindData |  |
| 564 | `_fsopen` | `0x2E590` | 213 | UnwindData |  |
| 1370 | `fopen` | `0x2E66C` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1371 | `fopen_s` | `0x2E680` | 83 | UnwindData |  |
| 1372 | `fprintf` | `0x2E6DC` | 302 | UnwindData |  |
| 546 | `_fprintf_l` | `0x2E810` | 29 | UnwindData |  |
| 549 | `_fprintf_s_l` | `0x2E834` | 29 | UnwindData |  |
| 1373 | `fprintf_s` | `0x2E858` | 36 | UnwindData |  |
| 548 | `_fprintf_p_l` | `0x2E884` | 29 | UnwindData |  |
| 547 | `_fprintf_p` | `0x2E8A8` | 36 | UnwindData |  |
| 554 | `_fread_nolock_s` | `0x2E8D4` | 567 | UnwindData |  |
| 553 | `_fread_nolock` | `0x2EB14` | 29 | UnwindData |  |
| 1379 | `fread_s` | `0x2EB38` | 167 | UnwindData |  |
| 1378 | `fread` | `0x2EBE8` | 29 | UnwindData |  |
| 1381 | `freopen` | `0x2ED04` | 47 | UnwindData |  |
| 1382 | `freopen_s` | `0x2ED3C` | 22 | UnwindData |  |
| 1384 | `fscanf` | `0x2EE84` | 53 | UnwindData |  |
| 559 | `_fscanf_l` | `0x2EEC0` | 49 | UnwindData |  |
| 1385 | `fscanf_s` | `0x2EEF8` | 53 | UnwindData |  |
| 560 | `_fscanf_s_l` | `0x2EF34` | 49 | UnwindData |  |
| 561 | `_fseek_nolock` | `0x2EF6C` | 178 | UnwindData |  |
| 1386 | `fseek` | `0x2F024` | 122 | UnwindData |  |
| 563 | `_fseeki64_nolock` | `0x2F0A4` | 203 | UnwindData |  |
| 562 | `_fseeki64` | `0x2F178` | 124 | UnwindData |  |
| 1387 | `fsetpos` | `0x2F1FC` | 53 | UnwindData |  |
| 569 | `_ftell_nolock` | `0x2F238` | 438 | UnwindData |  |
| 1388 | `ftell` | `0x2F3F4` | 88 | UnwindData |  |
| 571 | `_ftelli64_nolock` | `0x2F454` | 751 | UnwindData |  |
| 570 | `_ftelli64` | `0x2F74C` | 91 | UnwindData |  |
| 1389 | `fwprintf` | `0x2F7B0` | 145 | UnwindData |  |
| 579 | `_fwprintf_l` | `0x2F848` | 29 | UnwindData |  |
| 582 | `_fwprintf_s_l` | `0x2F86C` | 29 | UnwindData |  |
| 1390 | `fwprintf_s` | `0x2F890` | 36 | UnwindData |  |
| 581 | `_fwprintf_p_l` | `0x2F8BC` | 29 | UnwindData |  |
| 580 | `_fwprintf_p` | `0x2F8E0` | 36 | UnwindData |  |
| 583 | `_fwrite_nolock` | `0x2F90C` | 394 | UnwindData |  |
| 1391 | `fwrite` | `0x2FA9C` | 143 | UnwindData |  |
| 1392 | `fwscanf` | `0x2FBC8` | 53 | UnwindData |  |
| 584 | `_fwscanf_l` | `0x2FC04` | 49 | UnwindData |  |
| 1393 | `fwscanf_s` | `0x2FC3C` | 53 | UnwindData |  |
| 585 | `_fwscanf_s_l` | `0x2FC78` | 49 | UnwindData |  |
| 1399 | `gets_s` | `0x2FF14` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1398 | `gets` | `0x2FF24` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 623 | `_getw` | `0x2FF3C` | 180 | UnwindData |  |
| 629 | `_getws_s` | `0x30178` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 628 | `_getws` | `0x30188` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 981 | `_set_output_format` | `0x301A0` | 52 | UnwindData |  |
| 597 | `_get_output_format` | `0x301DC` | 172 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 933 | `_popen` | `0x30288` | 1,644 | UnwindData |  |
| 929 | `_pclose` | `0x308FC` | 220 | UnwindData |  |
| 1460 | `printf` | `0x309E0` | 171 | UnwindData |  |
| 934 | `_printf_l` | `0x30A94` | 33 | UnwindData |  |
| 937 | `_printf_s_l` | `0x30ABC` | 33 | UnwindData |  |
| 1461 | `printf_s` | `0x30AE4` | 39 | UnwindData |  |
| 936 | `_printf_p_l` | `0x30B14` | 33 | UnwindData |  |
| 935 | `_printf_p` | `0x30B3C` | 39 | UnwindData |  |
| 982 | `_set_printf_count_output` | `0x30B6C` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 599 | `_get_printf_count_output` | `0x30B9C` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1464 | `puts` | `0x30BBC` | 382 | UnwindData |  |
| 943 | `_putw` | `0x30D40` | 175 | UnwindData |  |
| 946 | `_putws` | `0x30DF8` | 231 | UnwindData |  |
| 1475 | `rewind` | `0x30EE8` | 190 | UnwindData |  |
| 954 | `_rmtmp` | `0x30FAC` | 160 | UnwindData |  |
| 1476 | `scanf` | `0x310EC` | 50 | UnwindData |  |
| 961 | `_scanf_l` | `0x31124` | 46 | UnwindData |  |
| 1477 | `scanf_s` | `0x31158` | 50 | UnwindData |  |
| 962 | `_scanf_s_l` | `0x31190` | 46 | UnwindData |  |
| 987 | `_setmaxstdio` | `0x311C4` | 277 | UnwindData |  |
| 618 | `_getmaxstdio` | `0x312E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1478 | `setbuf` | `0x312F0` | 36 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1481 | `setvbuf` | `0x31314` | 264 | UnwindData |  |
| 992 | `_snprintf` | `0x31424` | 177 | UnwindData |  |
| 995 | `_snprintf_l` | `0x314DC` | 29 | UnwindData |  |
| 993 | `_snprintf_c` | `0x31500` | 191 | UnwindData |  |
| 994 | `_snprintf_c_l` | `0x315C8` | 29 | UnwindData |  |
| 998 | `_snscanf` | `0x31698` | 54 | UnwindData |  |
| 999 | `_snscanf_l` | `0x316D4` | 49 | UnwindData |  |
| 1000 | `_snscanf_s` | `0x3170C` | 54 | UnwindData |  |
| 1001 | `_snscanf_s_l` | `0x31748` | 49 | UnwindData |  |
| 1002 | `_snwprintf` | `0x31780` | 226 | UnwindData |  |
| 1003 | `_snwprintf_l` | `0x31868` | 29 | UnwindData |  |
| 1006 | `_snwscanf` | `0x31940` | 54 | UnwindData |  |
| 1007 | `_snwscanf_l` | `0x3197C` | 49 | UnwindData |  |
| 1008 | `_snwscanf_s` | `0x319B4` | 54 | UnwindData |  |
| 1009 | `_snwscanf_s_l` | `0x319F0` | 49 | UnwindData |  |
| 1487 | `sprintf` | `0x31A28` | 160 | UnwindData |  |
| 1022 | `_sprintf_l` | `0x31AD0` | 29 | UnwindData |  |
| 1488 | `sprintf_s` | `0x31AF4` | 36 | UnwindData |  |
| 1025 | `_sprintf_s_l` | `0x31B20` | 29 | UnwindData |  |
| 996 | `_snprintf_s` | `0x31B44` | 34 | UnwindData |  |
| 997 | `_snprintf_s_l` | `0x31B6C` | 33 | UnwindData |  |
| 1023 | `_sprintf_p` | `0x31B94` | 36 | UnwindData |  |
| 1024 | `_sprintf_p_l` | `0x31BC0` | 29 | UnwindData |  |
| 963 | `_scprintf` | `0x31BE4` | 37 | UnwindData |  |
| 965 | `_scprintf_p` | `0x31C10` | 37 | UnwindData |  |
| 964 | `_scprintf_l` | `0x31C3C` | 33 | UnwindData |  |
| 966 | `_scprintf_p_l` | `0x31C64` | 33 | UnwindData |  |
| 1492 | `sscanf` | `0x31D38` | 53 | UnwindData |  |
| 1026 | `_sscanf_l` | `0x31D74` | 49 | UnwindData |  |
| 1493 | `sscanf_s` | `0x31DAC` | 53 | UnwindData |  |
| 1027 | `_sscanf_s_l` | `0x31DE8` | 49 | UnwindData |  |
| 1074 | `_swprintf` | `0x31F80` | 196 | UnwindData |  |
| 384 | `__swprintf_l` | `0x3204C` | 29 | UnwindData |  |
| 1522 | `swprintf_s` | `0x32070` | 36 | UnwindData |  |
| 1004 | `_snwprintf_s` | `0x3209C` | 34 | UnwindData |  |
| 1077 | `_swprintf_p` | `0x320C4` | 36 | UnwindData |  |
| 1079 | `_swprintf_s_l` | `0x320F0` | 29 | UnwindData |  |
| 1005 | `_snwprintf_s_l` | `0x32114` | 33 | UnwindData |  |
| 1078 | `_swprintf_p_l` | `0x3213C` | 29 | UnwindData |  |
| 967 | `_scwprintf` | `0x32160` | 37 | UnwindData |  |
| 969 | `_scwprintf_p` | `0x3218C` | 37 | UnwindData |  |
| 968 | `_scwprintf_l` | `0x321B8` | 33 | UnwindData |  |
| 970 | `_scwprintf_p_l` | `0x321E0` | 33 | UnwindData |  |
| 1075 | `_swprintf_c` | `0x32208` | 253 | UnwindData |  |
| 1076 | `_swprintf_c_l` | `0x3230C` | 29 | UnwindData |  |
| 1523 | `swscanf` | `0x323E8` | 53 | UnwindData |  |
| 1080 | `_swscanf_l` | `0x32424` | 49 | UnwindData |  |
| 1524 | `swscanf_s` | `0x3245C` | 53 | UnwindData |  |
| 1081 | `_swscanf_s_l` | `0x32498` | 49 | UnwindData |  |
| 1086 | `_tempnam` | `0x324D0` | 724 | UnwindData |  |
| 1533 | `tmpnam_s` | `0x32B74` | 64 | UnwindData |  |
| 1532 | `tmpnam` | `0x32BBC` | 48 | UnwindData |  |
| 1530 | `tmpfile` | `0x32E84` | 35 | UnwindData |  |
| 1531 | `tmpfile_s` | `0x32EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1108 | `_ungetc_nolock` | `0x32EC0` | 267 | UnwindData |  |
| 1538 | `ungetc` | `0x32FD4` | 95 | UnwindData |  |
| 1111 | `_ungetwc_nolock` | `0x3303C` | 515 | UnwindData |  |
| 1539 | `ungetwc` | `0x33248` | 101 | UnwindData |  |
| 1140 | `_vprintf_l` | `0x33364` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1143 | `_vprintf_s_l` | `0x33380` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1142 | `_vprintf_p_l` | `0x3339C` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1544 | `vprintf` | `0x333B8` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1545 | `vprintf_s` | `0x333D4` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1141 | `_vprintf_p` | `0x333F0` | 360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1132 | `_vfprintf_l` | `0x33558` | 35 | UnwindData |  |
| 1135 | `_vfprintf_s_l` | `0x33584` | 35 | UnwindData |  |
| 1134 | `_vfprintf_p_l` | `0x335B0` | 35 | UnwindData |  |
| 1540 | `vfprintf` | `0x335DC` | 35 | UnwindData |  |
| 1541 | `vfprintf_s` | `0x33608` | 35 | UnwindData |  |
| 1133 | `_vfprintf_p` | `0x33634` | 35 | UnwindData |  |
| 1136 | `_vfwprintf_l` | `0x33708` | 35 | UnwindData |  |
| 1139 | `_vfwprintf_s_l` | `0x33734` | 35 | UnwindData |  |
| 1138 | `_vfwprintf_p_l` | `0x33760` | 35 | UnwindData |  |
| 1542 | `vfwprintf` | `0x3378C` | 35 | UnwindData |  |
| 1543 | `vfwprintf_s` | `0x337B8` | 35 | UnwindData |  |
| 1137 | `_vfwprintf_p` | `0x337E4` | 35 | UnwindData |  |
| 1162 | `_vsprintf_l` | `0x33810` | 181 | UnwindData |  |
| 1546 | `vsprintf` | `0x338CC` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1144 | `_vscprintf` | `0x338E0` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1145 | `_vscprintf_l` | `0x338FC` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1146 | `_vscprintf_p` | `0x33918` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1147 | `_vscprintf_p_l` | `0x33934` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1155 | `_vsnprintf_l` | `0x33950` | 203 | UnwindData |  |
| 1152 | `_vsnprintf` | `0x33A24` | 22 | UnwindData |  |
| 1153 | `_vsnprintf_c` | `0x33B2C` | 49 | UnwindData |  |
| 1154 | `_vsnprintf_c_l` | `0x33B64` | 53 | UnwindData |  |
| 1165 | `_vsprintf_s_l` | `0x33BA0` | 110 | UnwindData |  |
| 1547 | `vsprintf_s` | `0x33C14` | 22 | UnwindData |  |
| 1157 | `_vsnprintf_s_l` | `0x33C30` | 328 | UnwindData |  |
| 1156 | `_vsnprintf_s` | `0x33D80` | 30 | UnwindData |  |
| 1163 | `_vsprintf_p` | `0x33DA4` | 49 | UnwindData |  |
| 1164 | `_vsprintf_p_l` | `0x33DDC` | 53 | UnwindData |  |
| 1159 | `_vsnwprintf_l` | `0x33E18` | 252 | UnwindData |  |
| 1158 | `_vsnwprintf` | `0x33F1C` | 22 | UnwindData |  |
| 1169 | `_vswprintf_l` | `0x33F38` | 221 | UnwindData |  |
| 1166 | `_vswprintf` | `0x3401C` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 396 | `__vswprintf_l` | `0x34030` | 164 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1148 | `_vscwprintf` | `0x340D4` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1149 | `_vscwprintf_l` | `0x340F0` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1150 | `_vscwprintf_p` | `0x3410C` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1151 | `_vscwprintf_p_l` | `0x34128` | 316 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1167 | `_vswprintf_c` | `0x34264` | 49 | UnwindData |  |
| 1168 | `_vswprintf_c_l` | `0x3429C` | 53 | UnwindData |  |
| 1172 | `_vswprintf_s_l` | `0x342D8` | 121 | UnwindData |  |
| 1548 | `vswprintf_s` | `0x34358` | 22 | UnwindData |  |
| 1161 | `_vsnwprintf_s_l` | `0x34374` | 333 | UnwindData |  |
| 1160 | `_vsnwprintf_s` | `0x344C8` | 30 | UnwindData |  |
| 1170 | `_vswprintf_p` | `0x344EC` | 49 | UnwindData |  |
| 1171 | `_vswprintf_p_l` | `0x34524` | 53 | UnwindData |  |
| 1173 | `_vwprintf_l` | `0x34560` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1176 | `_vwprintf_s_l` | `0x3457C` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1175 | `_vwprintf_p_l` | `0x34598` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1549 | `vwprintf` | `0x345B4` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1550 | `vwprintf_s` | `0x345D0` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1174 | `_vwprintf_p` | `0x345EC` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1241 | `_wfdopen` | `0x34608` | 436 | UnwindData |  |
| 1254 | `_wfsopen` | `0x347C4` | 221 | UnwindData |  |
| 1250 | `_wfopen` | `0x348A8` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1251 | `_wfopen_s` | `0x348BC` | 83 | UnwindData |  |
| 1252 | `_wfreopen` | `0x34A10` | 47 | UnwindData |  |
| 1253 | `_wfreopen_s` | `0x34A48` | 22 | UnwindData |  |
| 1269 | `_wpopen` | `0x34D40` | 1,804 | UnwindData |  |
| 1588 | `wprintf` | `0x35454` | 171 | UnwindData |  |
| 1270 | `_wprintf_l` | `0x35508` | 33 | UnwindData |  |
| 1273 | `_wprintf_s_l` | `0x35530` | 33 | UnwindData |  |
| 1589 | `wprintf_s` | `0x35558` | 39 | UnwindData |  |
| 1272 | `_wprintf_p_l` | `0x35588` | 33 | UnwindData |  |
| 1271 | `_wprintf_p` | `0x355B0` | 39 | UnwindData |  |
| 1590 | `wscanf` | `0x355E0` | 50 | UnwindData |  |
| 1280 | `_wscanf_l` | `0x35618` | 46 | UnwindData |  |
| 1591 | `wscanf_s` | `0x3564C` | 50 | UnwindData |  |
| 1281 | `_wscanf_s_l` | `0x35684` | 46 | UnwindData |  |
| 1306 | `_wtempnam` | `0x356B8` | 665 | UnwindData |  |
| 1308 | `_wtmpnam_s` | `0x35D54` | 64 | UnwindData |  |
| 1307 | `_wtmpnam` | `0x35D9C` | 48 | UnwindData |  |
| 1448 | `memchr` | `0x35DD4` | 36 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1451 | `memcpy_s` | `0x35DF8` | 135 | UnwindData |  |
| 913 | `_memccpy` | `0x35E88` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1453 | `memmove_s` | `0x35EB8` | 81 | UnwindData |  |
| 1496 | `strchr` | `0x35F10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1501 | `strcspn` | `0x35F30` | 147 | UnwindData |  |
| 1036 | `_strdup` | `0x35FCC` | 112 | UnwindData |  |
| 1054 | `_strnset` | `0x36044` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1512 | `strpbrk` | `0x36064` | 153 | UnwindData |  |
| 1513 | `strrchr` | `0x36104` | 44 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1056 | `_strrev` | `0x36130` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1057 | `_strset` | `0x36170` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1514 | `strspn` | `0x36188` | 178 | UnwindData |  |
| 1515 | `strstr` | `0x36240` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1511 | `strnlen` | `0x362A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1495 | `strcat_s` | `0x362C0` | 124 | UnwindData |  |
| 1507 | `strncat_s` | `0x36344` | 213 | UnwindData |  |
| 1500 | `strcpy_s` | `0x36420` | 97 | UnwindData |  |
| 1510 | `strncpy_s` | `0x36488` | 191 | UnwindData |  |
| 383 | `__strncnt` | `0x36550` | 44 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1058 | `_strset_s` | `0x3657C` | 79 | UnwindData |  |
| 1055 | `_strnset_s` | `0x365D4` | 122 | UnwindData |  |
| 1517 | `strtok` | `0x36654` | 235 | UnwindData |  |
| 1518 | `strtok_s` | `0x36748` | 270 | UnwindData |  |
| 1553 | `wcscat` | `0x3685C` | 52 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1558 | `wcscpy` | `0x36890` | 36 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1554 | `wcscat_s` | `0x368B4` | 133 | UnwindData |  |
| 1555 | `wcschr` | `0x36940` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1556 | `wcscmp` | `0x36968` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1559 | `wcscpy_s` | `0x369A8` | 107 | UnwindData |  |
| 1560 | `wcscspn` | `0x36A1C` | 68 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1187 | `_wcsdup` | `0x36A60` | 117 | UnwindData |  |
| 1562 | `wcslen` | `0x36ADC` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1568 | `wcsnlen` | `0x36AFC` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1563 | `wcsncat` | `0x36B24` | 68 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1564 | `wcsncat_s` | `0x36B68` | 230 | UnwindData |  |
| 1565 | `wcsncmp` | `0x36C54` | 52 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 400 | `__wcsncnt` | `0x36C88` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1566 | `wcsncpy` | `0x36CB8` | 70 | UnwindData |  |
| 1567 | `wcsncpy_s` | `0x36D04` | 207 | UnwindData |  |
| 1205 | `_wcsnset` | `0x36DDC` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1206 | `_wcsnset_s` | `0x36E04` | 129 | UnwindData |  |
| 1569 | `wcspbrk` | `0x36E8C` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1570 | `wcsrchr` | `0x36ECC` | 52 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1207 | `_wcsrev` | `0x36F00` | 72 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1208 | `_wcsset` | `0x36F48` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1209 | `_wcsset_s` | `0x36F64` | 84 | UnwindData |  |
| 1573 | `wcsspn` | `0x36FC0` | 72 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1574 | `wcsstr` | `0x37008` | 108 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1576 | `wcstok` | `0x37074` | 167 | UnwindData |  |
| 1577 | `wcstok_s` | `0x37124` | 191 | UnwindData |  |
| 1586 | `wmemcpy_s` | `0x371EC` | 122 | UnwindData |  |
| 1587 | `wmemmove_s` | `0x3726C` | 82 | UnwindData |  |
| 1328 | `asctime_s` | `0x372C4` | 773 | UnwindData |  |
| 1327 | `asctime` | `0x375D0` | 810 | UnwindData |  |
| 1347 | `clock` | `0x37900` | 62 | UnwindData |  |
| 475 | `_ctime32_s` | `0x37978` | 147 | UnwindData |  |
| 474 | `_ctime32` | `0x37A14` | 107 | UnwindData |  |
| 490 | `_difftime32` | `0x37A88` | 44 | UnwindData |  |
| 491 | `_difftime64` | `0x37ABC` | 48 | UnwindData |  |
| 573 | `_ftime32_s` | `0x37DB0` | 400 | UnwindData |  |
| 572 | `_ftime32` | `0x37F48` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 631 | `_gmtime32_s` | `0x37F54` | 416 | UnwindData |  |
| 630 | `_gmtime32` | `0x38148` | 69 | UnwindData |  |
| 756 | `_localtime32_s` | `0x38194` | 723 | UnwindData |  |
| 755 | `_localtime32` | `0x38470` | 69 | UnwindData |  |
| 921 | `_mktime32` | `0x38780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 917 | `_mkgmtime32` | `0x38790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1035 | `_strdate_s` | `0x387A0` | 304 | UnwindData |  |
| 1034 | `_strdate` | `0x388D8` | 273 | UnwindData |  |
| 1060 | `_strtime_s` | `0x389F0` | 280 | UnwindData |  |
| 1059 | `_strtime` | `0x38B10` | 249 | UnwindData |  |
| 1087 | `_time32` | `0x38C10` | 85 | UnwindData |  |
| 589 | `_get_daylight` | `0x38C6C` | 47 | UnwindData |  |
| 591 | `_get_dstbias` | `0x38CA4` | 47 | UnwindData |  |
| 602 | `_get_timezone` | `0x38CDC` | 47 | UnwindData |  |
| 603 | `_get_tzname` | `0x38D14` | 182 | UnwindData |  |
| 329 | `__daylight` | `0x38DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 332 | `__dstbias` | `0x38DE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 389 | `__timezone` | `0x38DF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 391 | `__tzname` | `0x38E00` | 2,660 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1097 | `_tzset` | `0x39864` | 36 | UnwindData |  |
| 577 | `_futime32` | `0x398C8` | 502 | UnwindData |  |
| 1118 | `_utime32` | `0x39AC4` | 139 | UnwindData |  |
| 477 | `_ctime64_s` | `0x39B58` | 162 | UnwindData |  |
| 476 | `_ctime64` | `0x39C00` | 108 | UnwindData |  |
| 575 | `_ftime64_s` | `0x39F44` | 403 | UnwindData |  |
| 574 | `_ftime64` | `0x3A0E0` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 633 | `_gmtime64_s` | `0x3A0EC` | 720 | UnwindData |  |
| 632 | `_gmtime64` | `0x3A3C4` | 69 | UnwindData |  |
| 758 | `_localtime64_s` | `0x3A410` | 794 | UnwindData |  |
| 757 | `_localtime64` | `0x3A730` | 69 | UnwindData |  |
| 922 | `_mktime64` | `0x3AA34` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 918 | `_mkgmtime64` | `0x3AA44` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 622 | `_getsystime` | `0x3AA54` | 158 | UnwindData |  |
| 990 | `_setsystime` | `0x3AAF8` | 165 | UnwindData |  |
| 1088 | `_time64` | `0x3ABA4` | 93 | UnwindData |  |
| 578 | `_futime64` | `0x3AC08` | 504 | UnwindData |  |
| 1119 | `_utime64` | `0x3AE08` | 139 | UnwindData |  |
| 1180 | `_wasctime_s` | `0x3AE9C` | 830 | UnwindData |  |
| 1179 | `_wasctime` | `0x3B1E0` | 865 | UnwindData |  |
| 1225 | `_wctime32_s` | `0x3B548` | 141 | UnwindData |  |
| 1224 | `_wctime32` | `0x3B5DC` | 107 | UnwindData |  |
| 1227 | `_wctime64_s` | `0x3B650` | 158 | UnwindData |  |
| 1226 | `_wctime64` | `0x3B6F4` | 108 | UnwindData |  |
| 1302 | `_wstrdate_s` | `0x3B768` | 343 | UnwindData |  |
| 1301 | `_wstrdate` | `0x3B8C8` | 314 | UnwindData |  |
| 1304 | `_wstrtime_s` | `0x3BA08` | 319 | UnwindData |  |
| 1303 | `_wstrtime` | `0x3BB50` | 290 | UnwindData |  |
| 1318 | `_wutime32` | `0x3BC78` | 139 | UnwindData |  |
| 1319 | `_wutime64` | `0x3BD0C` | 139 | UnwindData |  |
| 1449 | `memcmp` | `0x3BDB0` | 199 | UnwindData |  |
| 1508 | `strncmp` | `0x3BE90` | 181 | UnwindData |  |
| 1450 | `memcpy` | `0x3BF60` | 820 | UnwindData |  |
| 1452 | `memmove` | `0x3BF60` | 820 | UnwindData |  |
| 1454 | `memset` | `0x3C2B0` | 234 | UnwindData |  |
| 1494 | `strcat` | `0x3C3B0` | 144 | UnwindData |  |
| 1499 | `strcpy` | `0x3C450` | 183 | UnwindData |  |
| 1497 | `strcmp` | `0x3C520` | 176 | UnwindData |  |
| 1505 | `strlen` | `0x3C5E0` | 168 | UnwindData |  |
| 1506 | `strncat` | `0x3C6A0` | 405 | UnwindData |  |
| 1509 | `strncpy` | `0x3C850` | 354 | UnwindData |  |
| 655 | `_isalpha_l` | `0x3CA60` | 102 | UnwindData |  |
| 1404 | `isalpha` | `0x3CACC` | 131 | UnwindData |  |
| 727 | `_isupper_l` | `0x3CB58` | 99 | UnwindData |  |
| 1413 | `isupper` | `0x3CBC4` | 126 | UnwindData |  |
| 663 | `_islower_l` | `0x3CC48` | 99 | UnwindData |  |
| 1409 | `islower` | `0x3CCB4` | 126 | UnwindData |  |
| 660 | `_isdigit_l` | `0x3CD38` | 99 | UnwindData |  |
| 1406 | `isdigit` | `0x3CDA4` | 126 | UnwindData |  |
| 742 | `_isxdigit_l` | `0x3CE28` | 102 | UnwindData |  |
| 1427 | `isxdigit` | `0x3CE94` | 131 | UnwindData |  |
| 726 | `_isspace_l` | `0x3CF20` | 99 | UnwindData |  |
| 1412 | `isspace` | `0x3CF8C` | 126 | UnwindData |  |
| 725 | `_ispunct_l` | `0x3D010` | 99 | UnwindData |  |
| 1411 | `ispunct` | `0x3D07C` | 126 | UnwindData |  |
| 654 | `_isalnum_l` | `0x3D100` | 102 | UnwindData |  |
| 1403 | `isalnum` | `0x3D16C` | 131 | UnwindData |  |
| 724 | `_isprint_l` | `0x3D1F8` | 102 | UnwindData |  |
| 1410 | `isprint` | `0x3D264` | 131 | UnwindData |  |
| 661 | `_isgraph_l` | `0x3D2F0` | 102 | UnwindData |  |
| 1407 | `isgraph` | `0x3D35C` | 131 | UnwindData |  |
| 657 | `_iscntrl_l` | `0x3D3E8` | 99 | UnwindData |  |
| 1405 | `iscntrl` | `0x3D454` | 126 | UnwindData |  |
| 343 | `__isascii` | `0x3D4D8` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 390 | `__toascii` | `0x3D4EC` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 345 | `__iscsymf` | `0x3D4F8` | 37 | UnwindData |  |
| 344 | `__iscsym` | `0x3D524` | 40 | UnwindData |  |
| 905 | `_mbstrlen_l` | `0x3D554` | 190 | UnwindData |  |
| 904 | `_mbstrlen` | `0x3D618` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 907 | `_mbstrnlen_l` | `0x3D634` | 318 | UnwindData |  |
| 906 | `_mbstrnlen` | `0x3D778` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 662 | `_isleadbyte_l` | `0x3D788` | 69 | UnwindData |  |
| 1408 | `isleadbyte` | `0x3D7D4` | 71 | UnwindData |  |
| 729 | `_iswalpha_l` | `0x3D824` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1415 | `iswalpha` | `0x3D824` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 740 | `_iswupper_l` | `0x3D834` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1425 | `iswupper` | `0x3D834` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 736 | `_iswlower_l` | `0x3D844` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1421 | `iswlower` | `0x3D844` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 734 | `_iswdigit_l` | `0x3D854` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1419 | `iswdigit` | `0x3D854` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 741 | `_iswxdigit_l` | `0x3D864` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1426 | `iswxdigit` | `0x3D864` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 739 | `_iswspace_l` | `0x3D874` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1424 | `iswspace` | `0x3D874` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 738 | `_iswpunct_l` | `0x3D884` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1423 | `iswpunct` | `0x3D884` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 728 | `_iswalnum_l` | `0x3D894` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1414 | `iswalnum` | `0x3D894` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 737 | `_iswprint_l` | `0x3D8A4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1422 | `iswprint` | `0x3D8A4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 735 | `_iswgraph_l` | `0x3D8B4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1420 | `iswgraph` | `0x3D8B4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 730 | `_iswcntrl_l` | `0x3D8C4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1417 | `iswcntrl` | `0x3D8C4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1416 | `iswascii` | `0x3D8D4` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 346 | `__iswcsym` | `0x3D8E8` | 44 | UnwindData |  |
| 731 | `_iswcsym_l` | `0x3D8E8` | 44 | UnwindData |  |
| 347 | `__iswcsymf` | `0x3D91C` | 44 | UnwindData |  |
| 732 | `_iswcsymf_l` | `0x3D91C` | 44 | UnwindData |  |
| 418 | `_atodbl_l` | `0x3D950` | 255 | UnwindData |  |
| 417 | `_atodbl` | `0x3DA58` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 427 | `_atoldbl_l` | `0x3DA68` | 258 | UnwindData |  |
| 426 | `_atoldbl` | `0x3DB70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 421 | `_atoflt_l` | `0x3DB80` | 255 | UnwindData |  |
| 420 | `_atoflt` | `0x3DC88` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 419 | `_atof_l` | `0x3DC98` | 205 | UnwindData |  |
| 1336 | `atof` | `0x3DD6C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 309 | `__STRINGTOLD` | `0x3DD7C` | 110 | UnwindData |  |
| 518 | `_fcvt_s` | `0x3DE84` | 205 | UnwindData |  |
| 517 | `_fcvt` | `0x3DF58` | 220 | UnwindData |  |
| 498 | `_ecvt_s` | `0x3E03C` | 199 | UnwindData |  |
| 497 | `_ecvt` | `0x3E10C` | 180 | UnwindData |  |
| 587 | `_gcvt_s` | `0x3E1C8` | 421 | UnwindData |  |
| 586 | `_gcvt` | `0x3E374` | 45 | UnwindData |  |
| 1418 | `iswctype` | `0x3E3A8` | 102 | UnwindData |  |
| 733 | `_iswctype_l` | `0x3E414` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1402 | `is_wctype` | `0x3E414` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 659 | `_isctype_l` | `0x3E420` | 232 | UnwindData |  |
| 658 | `_isctype` | `0x3E510` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 803 | `_mblen_l` | `0x3E538` | 263 | UnwindData |  |
| 1440 | `mblen` | `0x3E648` | 532 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 902 | `_mbstowcs_l` | `0x3E85C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1445 | `mbstowcs` | `0x3E868` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 903 | `_mbstowcs_s_l` | `0x3E888` | 379 | UnwindData |  |
| 1446 | `mbstowcs_s` | `0x3EA0C` | 30 | UnwindData |  |
| 912 | `_mbtowc_l` | `0x3EA30` | 373 | UnwindData |  |
| 1447 | `mbtowc` | `0x3EBAC` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1341 | `btowc` | `0x3EDEC` | 100 | UnwindData |  |
| 1441 | `mbrlen` | `0x3EE58` | 62 | UnwindData |  |
| 1442 | `mbrtowc` | `0x3EE9C` | 92 | UnwindData |  |
| 1443 | `mbsrtowcs` | `0x3F060` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1444 | `mbsrtowcs_s` | `0x3F06C` | 206 | UnwindData |  |
| 1061 | `_strtod_l` | `0x3F140` | 364 | UnwindData |  |
| 1516 | `strtod` | `0x3F2B4` | 644 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1519 | `strtol` | `0x3F538` | 48 | UnwindData |  |
| 1064 | `_strtol_l` | `0x3F570` | 34 | UnwindData |  |
| 1520 | `strtoul` | `0x3F598` | 51 | UnwindData |  |
| 1067 | `_strtoul_l` | `0x3F5D4` | 37 | UnwindData |  |
| 1062 | `_strtoi64` | `0x3F86C` | 48 | UnwindData |  |
| 1063 | `_strtoi64_l` | `0x3F8A4` | 34 | UnwindData |  |
| 1065 | `_strtoui64` | `0x3F8CC` | 51 | UnwindData |  |
| 1066 | `_strtoui64_l` | `0x3F908` | 37 | UnwindData |  |
| 1090 | `_tolower` | `0x3F934` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1091 | `_tolower_l` | `0x3F940` | 334 | UnwindData |  |
| 1534 | `tolower` | `0x3FA94` | 36 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1092 | `_toupper` | `0x3FAB8` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1093 | `_toupper_l` | `0x3FAC4` | 333 | UnwindData |  |
| 1535 | `toupper` | `0x3FC18` | 36 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1094 | `_towlower_l` | `0x3FC3C` | 213 | UnwindData |  |
| 1536 | `towlower` | `0x3FD18` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1095 | `_towupper_l` | `0x3FD28` | 218 | UnwindData |  |
| 1537 | `towupper` | `0x3FE08` | 276 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1552 | `wcrtomb_s` | `0x3FF1C` | 138 | UnwindData |  |
| 1551 | `wcrtomb` | `0x3FFAC` | 58 | UnwindData |  |
| 1571 | `wcsrtombs` | `0x401D8` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1572 | `wcsrtombs_s` | `0x401E4` | 192 | UnwindData |  |
| 1583 | `wctob` | `0x402AC` | 109 | UnwindData |  |
| 1210 | `_wcstod_l` | `0x40320` | 327 | UnwindData |  |
| 1575 | `wcstod` | `0x40470` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1213 | `_wcstol_l` | `0x40670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1578 | `wcstol` | `0x40670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1218 | `_wcstoul_l` | `0x40680` | 668 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1581 | `wcstoul` | `0x40680` | 668 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1211 | `_wcstoi64` | `0x4091C` | 48 | UnwindData |  |
| 1212 | `_wcstoi64_l` | `0x40954` | 34 | UnwindData |  |
| 1216 | `_wcstoui64` | `0x4097C` | 51 | UnwindData |  |
| 1217 | `_wcstoui64_l` | `0x409B8` | 37 | UnwindData |  |
| 1214 | `_wcstombs_l` | `0x40D7C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1579 | `wcstombs` | `0x40D88` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1215 | `_wcstombs_s_l` | `0x40D98` | 236 | UnwindData |  |
| 1580 | `wcstombs_s` | `0x40E8C` | 30 | UnwindData |  |
| 1229 | `_wctomb_s_l` | `0x40EB0` | 452 | UnwindData |  |
| 1585 | `wctomb_s` | `0x4107C` | 20 | UnwindData |  |
| 1228 | `_wctomb_l` | `0x41098` | 123 | UnwindData |  |
| 1584 | `wctomb` | `0x4111C` | 84 | UnwindData |  |
| 1310 | `_wtof_l` | `0x41178` | 161 | UnwindData |  |
| 1309 | `_wtof` | `0x41220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 687 | `_ismbcalnum_l` | `0x41230` | 260 | UnwindData |  |
| 686 | `_ismbcalnum` | `0x4133C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 689 | `_ismbcalpha_l` | `0x4134C` | 262 | UnwindData |  |
| 688 | `_ismbcalpha` | `0x41458` | 148 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 671 | `_ismbbkalnum_l` | `0x414EC` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 670 | `_ismbbkalnum` | `0x41508` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 675 | `_ismbbkprint_l` | `0x41520` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 674 | `_ismbbkprint` | `0x4153C` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 677 | `_ismbbkpunct_l` | `0x41554` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 676 | `_ismbbkpunct` | `0x41570` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 665 | `_ismbbalnum_l` | `0x41588` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 664 | `_ismbbalnum` | `0x415A8` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 667 | `_ismbbalpha_l` | `0x415C4` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 666 | `_ismbbalpha` | `0x415E4` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 669 | `_ismbbgraph_l` | `0x41600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 668 | `_ismbbgraph` | `0x41620` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 681 | `_ismbbprint_l` | `0x4163C` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 680 | `_ismbbprint` | `0x4165C` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 683 | `_ismbbpunct_l` | `0x41678` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 682 | `_ismbbpunct` | `0x41698` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 679 | `_ismbblead_l` | `0x416B4` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 678 | `_ismbblead` | `0x416D0` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 685 | `_ismbbtrail_l` | `0x416E8` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 684 | `_ismbbtrail` | `0x41704` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 673 | `_ismbbkana_l` | `0x4171C` | 117 | UnwindData |  |
| 672 | `_ismbbkana` | `0x41798` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 691 | `_ismbcdigit_l` | `0x417A8` | 265 | UnwindData |  |
| 690 | `_ismbcdigit` | `0x418B8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 693 | `_ismbcgraph_l` | `0x418C8` | 262 | UnwindData |  |
| 692 | `_ismbcgraph` | `0x419D4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 695 | `_ismbchira_l` | `0x419E4` | 77 | UnwindData |  |
| 694 | `_ismbchira` | `0x41A38` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 697 | `_ismbckata_l` | `0x41A48` | 85 | UnwindData |  |
| 696 | `_ismbckata` | `0x41AA4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 715 | `_ismbcsymbol_l` | `0x41AB4` | 85 | UnwindData |  |
| 714 | `_ismbcsymbol` | `0x41B10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 705 | `_ismbclegal_l` | `0x41B20` | 85 | UnwindData |  |
| 704 | `_ismbclegal` | `0x41B7C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 707 | `_ismbclower_l` | `0x41B8C` | 232 | UnwindData |  |
| 706 | `_ismbclower` | `0x41C7C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 709 | `_ismbcprint_l` | `0x41C8C` | 257 | UnwindData |  |
| 708 | `_ismbcprint` | `0x41D94` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 711 | `_ismbcpunct_l` | `0x41DA4` | 252 | UnwindData |  |
| 710 | `_ismbcpunct` | `0x41EA8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 719 | `_ismbslead_l` | `0x41EB8` | 167 | UnwindData |  |
| 718 | `_ismbslead` | `0x41F68` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 713 | `_ismbcspace_l` | `0x41F78` | 263 | UnwindData |  |
| 712 | `_ismbcspace` | `0x42088` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 721 | `_ismbstrail_l` | `0x42098` | 164 | UnwindData |  |
| 720 | `_ismbstrail` | `0x42144` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 717 | `_ismbcupper_l` | `0x42154` | 232 | UnwindData |  |
| 716 | `_ismbcupper` | `0x42244` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 780 | `_mbbtype_l` | `0x42254` | 201 | UnwindData |  |
| 779 | `_mbbtype` | `0x42324` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 783 | `_mbccpy_l` | `0x42334` | 29 | UnwindData |  |
| 782 | `_mbccpy` | `0x42358` | 30 | UnwindData |  |
| 784 | `_mbccpy_s` | `0x4237C` | 20 | UnwindData |  |
| 785 | `_mbccpy_s_l` | `0x42398` | 308 | UnwindData |  |
| 807 | `_mbscat_s_l` | `0x424D4` | 579 | UnwindData |  |
| 815 | `_mbscpy_s_l` | `0x42720` | 418 | UnwindData |  |
| 835 | `_mbsnbcat_s_l` | `0x428C8` | 806 | UnwindData |  |
| 845 | `_mbsnbcpy_s_l` | `0x42BF4` | 631 | UnwindData |  |
| 853 | `_mbsnbset_s_l` | `0x42E74` | 693 | UnwindData |  |
| 857 | `_mbsncat_s_l` | `0x43130` | 728 | UnwindData |  |
| 867 | `_mbsncpy_s_l` | `0x43410` | 576 | UnwindData |  |
| 881 | `_mbsnset_s_l` | `0x43658` | 703 | UnwindData |  |
| 891 | `_mbsset_s_l` | `0x43920` | 451 | UnwindData |  |
| 699 | `_ismbcl0_l` | `0x43AEC` | 99 | UnwindData |  |
| 698 | `_ismbcl0` | `0x43B58` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 701 | `_ismbcl1_l` | `0x43B68` | 104 | UnwindData |  |
| 700 | `_ismbcl1` | `0x43BD8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 703 | `_ismbcl2_l` | `0x43BE8` | 104 | UnwindData |  |
| 702 | `_ismbcl2` | `0x43C58` | 1,648 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 619 | `_getmbcp` | `0x442C8` | 80 | UnwindData |  |
| 988 | `_setmbcp` | `0x44320` | 478 | UnwindData |  |
| 805 | `_mbsbtype_l` | `0x44520` | 188 | UnwindData |  |
| 804 | `_mbsbtype` | `0x445E4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 806 | `_mbscat_s` | `0x445F4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 809 | `_mbschr_l` | `0x44604` | 236 | UnwindData |  |
| 808 | `_mbschr` | `0x446F8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 811 | `_mbscmp_l` | `0x44708` | 267 | UnwindData |  |
| 810 | `_mbscmp` | `0x4481C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 814 | `_mbscpy_s` | `0x4482C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 813 | `_mbscoll_l` | `0x4483C` | 223 | UnwindData |  |
| 812 | `_mbscoll` | `0x44924` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 817 | `_mbscspn_l` | `0x44934` | 270 | UnwindData |  |
| 816 | `_mbscspn` | `0x44A48` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 819 | `_mbsdec_l` | `0x44A58` | 170 | UnwindData |  |
| 818 | `_mbsdec` | `0x44B08` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 821 | `_mbsicmp_l` | `0x44B18` | 523 | UnwindData |  |
| 820 | `_mbsicmp` | `0x44D2C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 823 | `_mbsicoll_l` | `0x44D3C` | 223 | UnwindData |  |
| 822 | `_mbsicoll` | `0x44E24` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 827 | `_mbslen_l` | `0x44E34` | 101 | UnwindData |  |
| 826 | `_mbslen` | `0x44EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 877 | `_mbsnlen_l` | `0x44EB0` | 168 | UnwindData |  |
| 876 | `_mbsnlen` | `0x44F60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 831 | `_mbslwr_s_l` | `0x44F70` | 338 | UnwindData |  |
| 830 | `_mbslwr_s` | `0x450C8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 829 | `_mbslwr_l` | `0x450D8` | 43 | UnwindData |  |
| 828 | `_mbslwr` | `0x4510C` | 43 | UnwindData |  |
| 833 | `_mbsnbcat_l` | `0x45140` | 349 | UnwindData |  |
| 832 | `_mbsnbcat` | `0x452A4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 834 | `_mbsnbcat_s` | `0x452B4` | 20 | UnwindData |  |
| 837 | `_mbsnbcmp_l` | `0x452D0` | 352 | UnwindData |  |
| 836 | `_mbsnbcmp` | `0x45438` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 839 | `_mbsnbcnt_l` | `0x45448` | 166 | UnwindData |  |
| 838 | `_mbsnbcnt` | `0x454F4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 841 | `_mbsnbcoll_l` | `0x45504` | 264 | UnwindData |  |
| 840 | `_mbsnbcoll` | `0x45614` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 843 | `_mbsnbcpy_l` | `0x45624` | 279 | UnwindData |  |
| 842 | `_mbsnbcpy` | `0x45744` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 844 | `_mbsnbcpy_s` | `0x45754` | 20 | UnwindData |  |
| 847 | `_mbsnbicmp_l` | `0x45770` | 486 | UnwindData |  |
| 846 | `_mbsnbicmp` | `0x4595C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 849 | `_mbsnbicoll_l` | `0x4596C` | 258 | UnwindData |  |
| 848 | `_mbsnbicoll` | `0x45A74` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 851 | `_mbsnbset_l` | `0x45A84` | 285 | UnwindData |  |
| 850 | `_mbsnbset` | `0x45BA8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 852 | `_mbsnbset_s` | `0x45BB8` | 20 | UnwindData |  |
| 855 | `_mbsncat_l` | `0x45BD4` | 322 | UnwindData |  |
| 854 | `_mbsncat` | `0x45D1C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 856 | `_mbsncat_s` | `0x45D2C` | 20 | UnwindData |  |
| 859 | `_mbsnccnt_l` | `0x45D48` | 171 | UnwindData |  |
| 858 | `_mbsnccnt` | `0x45DFC` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 861 | `_mbsncmp_l` | `0x45E0C` | 313 | UnwindData |  |
| 860 | `_mbsncmp` | `0x45F4C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 863 | `_mbsncoll_l` | `0x45F5C` | 312 | UnwindData |  |
| 862 | `_mbsncoll` | `0x4609C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 865 | `_mbsncpy_l` | `0x460AC` | 266 | UnwindData |  |
| 864 | `_mbsncpy` | `0x461BC` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 866 | `_mbsncpy_s` | `0x461CC` | 20 | UnwindData |  |
| 869 | `_mbsnextc_l` | `0x461E8` | 133 | UnwindData |  |
| 868 | `_mbsnextc` | `0x46274` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 871 | `_mbsnicmp_l` | `0x46284` | 443 | UnwindData |  |
| 870 | `_mbsnicmp` | `0x46448` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 873 | `_mbsnicoll_l` | `0x46458` | 312 | UnwindData |  |
| 872 | `_mbsnicoll` | `0x46598` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 879 | `_mbsnset_l` | `0x465A8` | 407 | UnwindData |  |
| 878 | `_mbsnset` | `0x46748` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 880 | `_mbsnset_s` | `0x46758` | 20 | UnwindData |  |
| 883 | `_mbspbrk_l` | `0x46774` | 242 | UnwindData |  |
| 882 | `_mbspbrk` | `0x4686C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 885 | `_mbsrchr_l` | `0x4687C` | 221 | UnwindData |  |
| 884 | `_mbsrchr` | `0x46960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 887 | `_mbsrev_l` | `0x46970` | 237 | UnwindData |  |
| 886 | `_mbsrev` | `0x46A64` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 889 | `_mbsset_l` | `0x46A74` | 235 | UnwindData |  |
| 888 | `_mbsset` | `0x46B68` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 890 | `_mbsset_s` | `0x46B78` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 893 | `_mbsspn_l` | `0x46B88` | 270 | UnwindData |  |
| 892 | `_mbsspn` | `0x46C9C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 895 | `_mbsspnp_l` | `0x46CAC` | 256 | UnwindData |  |
| 894 | `_mbsspnp` | `0x46DB4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 897 | `_mbsstr_l` | `0x46DC4` | 331 | UnwindData |  |
| 896 | `_mbsstr` | `0x46F18` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 899 | `_mbstok_l` | `0x46F28` | 62 | UnwindData |  |
| 898 | `_mbstok` | `0x46F6C` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 901 | `_mbstok_s_l` | `0x46F7C` | 517 | UnwindData |  |
| 900 | `_mbstok_s` | `0x47188` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 911 | `_mbsupr_s_l` | `0x47198` | 338 | UnwindData |  |
| 910 | `_mbsupr_s` | `0x472F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 909 | `_mbsupr_l` | `0x47300` | 43 | UnwindData |  |
| 908 | `_mbsupr` | `0x47334` | 43 | UnwindData |  |
| 797 | `_mbctolower_l` | `0x47368` | 228 | UnwindData |  |
| 796 | `_mbctolower` | `0x47454` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 801 | `_mbctoupper_l` | `0x47464` | 228 | UnwindData |  |
| 800 | `_mbctoupper` | `0x47550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 787 | `_mbcjistojms_l` | `0x47560` | 193 | UnwindData |  |
| 786 | `_mbcjistojms` | `0x47628` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 789 | `_mbcjmstojis_l` | `0x47638` | 243 | UnwindData |  |
| 788 | `_mbcjmstojis` | `0x47734` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 778 | `_mbbtombc_l` | `0x47744` | 216 | UnwindData |  |
| 777 | `_mbbtombc` | `0x47824` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 799 | `_mbctombb_l` | `0x47834` | 237 | UnwindData |  |
| 798 | `_mbctombb` | `0x47928` | 3,760 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 470 | `_cscanf` | `0x487D8` | 39 | UnwindData |  |
| 471 | `_cscanf_l` | `0x48808` | 33 | UnwindData |  |
| 472 | `_cscanf_s` | `0x49830` | 39 | UnwindData |  |
| 473 | `_cscanf_s_l` | `0x49860` | 33 | UnwindData |  |
| 485 | `_cwscanf` | `0x4A918` | 39 | UnwindData |  |
| 486 | `_cwscanf_l` | `0x4A948` | 33 | UnwindData |  |
| 487 | `_cwscanf_s` | `0x4BC28` | 39 | UnwindData |  |
| 488 | `_cwscanf_s_l` | `0x4BC58` | 33 | UnwindData |  |
| 1121 | `_vcprintf_l` | `0x4BC80` | 2,561 | UnwindData |  |
| 461 | `_cprintf_l` | `0x4C688` | 33 | UnwindData |  |
| 460 | `_cprintf` | `0x4C6B0` | 39 | UnwindData |  |
| 1120 | `_vcprintf` | `0x4C6E0` | 264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1123 | `_vcprintf_p_l` | `0x4C7E8` | 4,263 | UnwindData |  |
| 463 | `_cprintf_p_l` | `0x4D898` | 33 | UnwindData |  |
| 462 | `_cprintf_p` | `0x4D8C0` | 39 | UnwindData |  |
| 1122 | `_vcprintf_p` | `0x4D8F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1125 | `_vcprintf_s_l` | `0x4D900` | 2,611 | UnwindData |  |
| 465 | `_cprintf_s_l` | `0x4E33C` | 33 | UnwindData |  |
| 464 | `_cprintf_s` | `0x4E364` | 39 | UnwindData |  |
| 1124 | `_vcprintf_s` | `0x4E394` | 104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1127 | `_vcwprintf_l` | `0x4E3FC` | 2,786 | UnwindData |  |
| 480 | `_cwprintf_l` | `0x4EEE4` | 33 | UnwindData |  |
| 479 | `_cwprintf` | `0x4EF0C` | 39 | UnwindData |  |
| 1126 | `_vcwprintf` | `0x4EF3C` | 172 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1129 | `_vcwprintf_p_l` | `0x4EFE8` | 4,590 | UnwindData |  |
| 482 | `_cwprintf_p_l` | `0x501DC` | 33 | UnwindData |  |
| 481 | `_cwprintf_p` | `0x50204` | 39 | UnwindData |  |
| 1128 | `_vcwprintf_p` | `0x50234` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1131 | `_vcwprintf_s_l` | `0x50244` | 2,813 | UnwindData |  |
| 484 | `_cwprintf_s_l` | `0x50D48` | 33 | UnwindData |  |
| 483 | `_cwprintf_s` | `0x50D70` | 39 | UnwindData |  |
| 1130 | `_vcwprintf_s` | `0x50DA0` | 40,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 915 | `_memicmp_l` | `0x5AA88` | 250 | UnwindData |  |
| 914 | `_memicmp` | `0x5AB88` | 80 | UnwindData |  |
| 1033 | `_strcoll_l` | `0x5ABE0` | 204 | UnwindData |  |
| 1498 | `strcoll` | `0x5ACB4` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1041 | `_stricmp_l` | `0x5AD04` | 214 | UnwindData |  |
| 1040 | `_stricmp` | `0x5ADE0` | 70 | UnwindData |  |
| 1043 | `_stricoll_l` | `0x5AE2C` | 204 | UnwindData |  |
| 1042 | `_stricoll` | `0x5AF00` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1047 | `_strlwr_s_l` | `0x5B120` | 75 | UnwindData |  |
| 1046 | `_strlwr_s` | `0x5B174` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1045 | `_strlwr_l` | `0x5B184` | 30 | UnwindData |  |
| 1044 | `_strlwr` | `0x5B1A8` | 98 | UnwindData |  |
| 1049 | `_strncoll_l` | `0x5B210` | 240 | UnwindData |  |
| 1048 | `_strncoll` | `0x5B308` | 79 | UnwindData |  |
| 1051 | `_strnicmp_l` | `0x5B3AC` | 259 | UnwindData |  |
| 1050 | `_strnicmp` | `0x5B4B8` | 79 | UnwindData |  |
| 1053 | `_strnicoll_l` | `0x5B510` | 259 | UnwindData |  |
| 1052 | `_strnicoll` | `0x5B61C` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1071 | `_strupr_s_l` | `0x5B83C` | 75 | UnwindData |  |
| 1070 | `_strupr_s` | `0x5B890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1069 | `_strupr_l` | `0x5B8A0` | 30 | UnwindData |  |
| 1068 | `_strupr` | `0x5B8C4` | 98 | UnwindData |  |
| 1072 | `_strxfrm_l` | `0x5B92C` | 415 | UnwindData |  |
| 1521 | `strxfrm` | `0x5BAD4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1186 | `_wcscoll_l` | `0x5BAE4` | 190 | UnwindData |  |
| 1557 | `wcscoll` | `0x5BBA8` | 70 | UnwindData |  |
| 1192 | `_wcsicmp_l` | `0x5BBF4` | 258 | UnwindData |  |
| 1191 | `_wcsicmp` | `0x5BCFC` | 134 | UnwindData |  |
| 1194 | `_wcsicoll_l` | `0x5BD88` | 261 | UnwindData |  |
| 1193 | `_wcsicoll` | `0x5BE94` | 134 | UnwindData |  |
| 1198 | `_wcslwr_s_l` | `0x5C114` | 75 | UnwindData |  |
| 1197 | `_wcslwr_s` | `0x5C168` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1196 | `_wcslwr_l` | `0x5C178` | 30 | UnwindData |  |
| 1195 | `_wcslwr` | `0x5C19C` | 111 | UnwindData |  |
| 1200 | `_wcsncoll_l` | `0x5C214` | 225 | UnwindData |  |
| 1199 | `_wcsncoll` | `0x5C2FC` | 79 | UnwindData |  |
| 1202 | `_wcsnicmp_l` | `0x5C354` | 278 | UnwindData |  |
| 1201 | `_wcsnicmp` | `0x5C470` | 152 | UnwindData |  |
| 1204 | `_wcsnicoll_l` | `0x5C510` | 296 | UnwindData |  |
| 1203 | `_wcsnicoll` | `0x5C640` | 148 | UnwindData |  |
| 1222 | `_wcsupr_s_l` | `0x5C8D0` | 75 | UnwindData |  |
| 1221 | `_wcsupr_s` | `0x5C924` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1220 | `_wcsupr_l` | `0x5C934` | 30 | UnwindData |  |
| 1219 | `_wcsupr` | `0x5C958` | 111 | UnwindData |  |
| 1223 | `_wcsxfrm_l` | `0x5C9D0` | 341 | UnwindData |  |
| 1582 | `wcsxfrm` | `0x5CB2C` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 276 | `_Getdays` | `0x5CC7C` | 348 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 277 | `_Getmonths` | `0x5CDD8` | 1,020 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 278 | `_Gettnames` | `0x5D1D4` | 3,704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1039 | `_strftime_l` | `0x5E04C` | 30 | UnwindData |  |
| 1504 | `strftime` | `0x5E070` | 26 | UnwindData |  |
| 283 | `_Strftime` | `0x5E090` | 30 | UnwindData |  |
| 1190 | `_wcsftime_l` | `0x5EF04` | 30 | UnwindData |  |
| 1561 | `wcsftime` | `0x5EF28` | 26 | UnwindData |  |
| 38 | `??0exception@std@@QEAA@XZ` | `0x5EF48` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `??0exception@std@@QEAA@AEBQEBDH@Z` | `0x5EF68` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 268 | `?what@exception@std@@UEBAPEBDXZ` | `0x5EF88` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 174 | `?_Copy_str@exception@std@@AEAAXPEBD@Z` | `0x5EFA0` | 90 | UnwindData |  |
| 205 | `?_Tidy@exception@std@@AEAAXXZ` | `0x5F000` | 39 | UnwindData |  |
| 35 | `??0exception@std@@QEAA@AEBQEBD@Z` | `0x5F030` | 45 | UnwindData |  |
| 109 | `??4exception@std@@QEAAAEAV01@AEBV01@@Z` | `0x5F064` | 68 | UnwindData |  |
| 22 | `??0bad_cast@std@@QEAA@PEBD@Z` | `0x5F0B0` | 42 | UnwindData |  |
| 20 | `??0bad_cast@std@@AEAA@PEBQEBD@Z` | `0x5F0E0` | 33 | UnwindData |  |
| 26 | `??0bad_typeid@std@@QEAA@PEBD@Z` | `0x5F108` | 42 | UnwindData |  |
| 19 | `??0__non_rtti_object@std@@QEAA@PEBD@Z` | `0x5F138` | 33 | UnwindData |  |
| 89 | `??1__non_rtti_object@std@@UEAA@XZ` | `0x5F160` | 148 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `??1bad_cast@std@@UEAA@XZ` | `0x5F160` | 148 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `??1bad_typeid@std@@UEAA@XZ` | `0x5F160` | 148 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `??1exception@std@@UEAA@XZ` | `0x5F160` | 148 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `??0exception@std@@QEAA@AEBV01@@Z` | `0x5F1F4` | 42 | UnwindData |  |
| 21 | `??0bad_cast@std@@QEAA@AEBV01@@Z` | `0x5F224` | 33 | UnwindData |  |
| 25 | `??0bad_typeid@std@@QEAA@AEBV01@@Z` | `0x5F24C` | 33 | UnwindData |  |
| 18 | `??0__non_rtti_object@std@@QEAA@AEBV01@@Z` | `0x5F274` | 33 | UnwindData |  |
| 248 | `?name@type_info@@QEBAPEBDPEAU__type_info_node@@@Z` | `0x5F29C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `??1type_info@@UEAA@XZ` | `0x5F2A8` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 230 | `?_name_internal_method@type_info@@QEBAPEBDPEAU__type_info_node@@@Z` | `0x5F2C0` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 240 | `?_type_info_dtor_internal_method@type_info@@QEAAXXZ` | `0x5F2CC` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `??8type_info@@QEBA_NAEBV0@@Z` | `0x5F2D8` | 30 | UnwindData |  |
| 111 | `??9type_info@@QEBA_NAEBV0@@Z` | `0x5F2FC` | 30 | UnwindData |  |
| 243 | `?before@type_info@@QEBAHAEBV1@@Z` | `0x5F320` | 34 | UnwindData |  |
| 250 | `?raw_name@type_info@@QEBAPEBDXZ` | `0x5F348` | 376 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 274 | `_GetImageBase` | `0x5F4C0` | 21 | UnwindData |  |
| 275 | `_GetThrowImageBase` | `0x5F4DC` | 21 | UnwindData |  |
| 281 | `_SetImageBase` | `0x5F4F8` | 27 | UnwindData |  |
| 282 | `_SetThrowImageBase` | `0x5F51C` | 27 | UnwindData |  |
| 296 | `__CxxFrameHandler` | `0x5F5F4` | 135 | UnwindData |  |
| 297 | `__CxxFrameHandler2` | `0x5F5F4` | 135 | UnwindData |  |
| 298 | `__CxxFrameHandler3` | `0x5F5F4` | 135 | UnwindData |  |
| 271 | `_CreateFrameInfo` | `0x5F8B4` | 67 | UnwindData |  |
| 280 | `_IsExceptionObjectToBeDestroyed` | `0x5F900` | 50 | UnwindData |  |
| 273 | `_FindAndUnlinkFrame` | `0x5F938` | 94 | UnwindData |  |
| 258 | `?terminate@@YAXXZ` | `0x5FA94` | 35 | UnwindData |  |
| 262 | `?unexpected@@YAXXZ` | `0x5FAC0` | 29 | UnwindData |  |
| 227 | `?_inconsistency@@YAXXZ` | `0x5FAE4` | 37 | UnwindData |  |
| 311 | `__TypeMatch` | `0x5FB34` | 291 | UnwindData |  |
| 303 | `__FrameUnwindFilter` | `0x5FC60` | 81 | UnwindData |  |
| 302 | `__DestructExceptionObject` | `0x5FE48` | 66 | UnwindData |  |
| 285 | `__AdjustPointer` | `0x5FE90` | 44 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 226 | `__uncaught_exception` | `0x5FEBC` | 25 | UnwindData |  |
| 300 | `__CxxRegisterExceptionObject` | `0x5FEDC` | 207 | UnwindData |  |
| 294 | `__CxxDetectRethrow` | `0x5FFB4` | 85 | UnwindData |  |
| 301 | `__CxxUnregisterExceptionObject` | `0x60010` | 343 | UnwindData |  |
| 299 | `__CxxQueryExceptionSize` | `0x60170` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 290 | `__CxxCallUnwindDelDtor` | `0x6017C` | 19 | UnwindData |  |
| 291 | `__CxxCallUnwindDtor` | `0x6017C` | 19 | UnwindData |  |
| 292 | `__CxxCallUnwindStdDelDtor` | `0x6017C` | 19 | UnwindData |  |
| 293 | `__CxxCallUnwindVecDtor` | `0x60198` | 42 | UnwindData |  |
| 229 | `?_is_exception_typeof@@YAHAEBVtype_info@@PEAU_EXCEPTION_POINTERS@@@Z` | `0x602A4` | 204 | UnwindData |  |
| 287 | `__BuildCatchObjectHelper` | `0x60590` | 514 | UnwindData |  |
| 286 | `__BuildCatchObject` | `0x60798` | 176 | UnwindData |  |
| 295 | `__CxxExceptionFilter` | `0x60850` | 527 | UnwindData |  |
| 272 | `_CxxThrowException` | `0x61470` | 147 | UnwindData |  |
| 211 | `?_Type_info_dtor@type_info@@CAXPEAV1@@Z` | `0x616DC` | 108 | UnwindData |  |
| 212 | `?_Type_info_dtor_internal@type_info@@CAXPEAV1@@Z` | `0x616DC` | 108 | UnwindData |  |
| 179 | `?_Name_base@type_info@@CAPEBDPEBV1@PEAU__type_info_node@@@Z` | `0x61750` | 308 | UnwindData |  |
| 394 | `__unDNameHelper` | `0x6188C` | 53 | UnwindData |  |
| 180 | `?_Name_base_internal@type_info@@CAPEBDPEBV1@PEAU__type_info_node@@@Z` | `0x618C8` | 345 | UnwindData |  |
| 322 | `__clean_type_info_names_internal` | `0x61A28` | 79 | UnwindData |  |
| 214 | `?_ValidateExecute@@YAHP6A_JXZ@Z` | `0x61A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 215 | `?_ValidateRead@@YAHPEBXI@Z` | `0x61A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 216 | `?_ValidateWrite@@YAHPEAXI@Z` | `0x61A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 255 | `?set_terminate@@YAP6AXXZP6AXXZ@Z` | `0x61A90` | 51 | UnwindData |  |
| 601 | `_get_terminate` | `0x61ACC` | 21 | UnwindData |  |
| 257 | `?set_unexpected@@YAP6AXXZP6AXXZ@Z` | `0x61AE8` | 51 | UnwindData |  |
| 604 | `_get_unexpected` | `0x61B24` | 21 | UnwindData |  |
| 238 | `?_set_se_translator@@YAP6AXIPEAU_EXCEPTION_POINTERS@@@ZP6AXI0@Z@Z` | `0x61B40` | 51 | UnwindData |  |
| 254 | `?set_terminate@@YAP6AXXZH@Z` | `0x61B7C` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 256 | `?set_unexpected@@YAP6AXXZH@Z` | `0x61B90` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 237 | `?_set_se_translator@@YAP6AXIPEAU_EXCEPTION_POINTERS@@@ZH@Z` | `0x61BA4` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 306 | `__RTCastToVoid` | `0x61C94` | 105 | UnwindData |  |
| 308 | `__RTtypeid` | `0x61D04` | 171 | UnwindData |  |
| 307 | `__RTDynamicCast` | `0x621B4` | 383 | UnwindData |  |
| 181 | `?_NumberOfSpins@?$_SpinWait@$00@details@Concurrency@@IEAAKXZ` | `0x62984` | 21,748 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 182 | `?_NumberOfSpins@?$_SpinWait@$0A@@details@Concurrency@@IEAAKXZ` | `0x62984` | 21,748 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 392 | `__unDName` | `0x67E78` | 261 | UnwindData |  |
| 393 | `__unDNameEx` | `0x67F84` | 267 | UnwindData |  |
| 102 | `??3@YAXPEAX@Z` | `0x68A70` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 980 | `_set_malloc_crt_max_wait` | `0x68A7C` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 776 | `_malloc_crt` | `0x68A90` | 126 | UnwindData |  |
| 437 | `_calloc_crt` | `0x68B14` | 131 | UnwindData |  |
| 949 | `_realloc_crt` | `0x68BA0` | 133 | UnwindData |  |
| 951 | `_recalloc_crt` | `0x68C2C` | 136 | UnwindData |  |
| 1439 | `malloc` | `0x68CBC` | 182 | UnwindData |  |
| 1380 | `free` | `0x68D78` | 61 | UnwindData |  |
| 100 | `??2@YAPEAX_K@Z` | `0x68DBC` | 163 | UnwindData |  |
| 594 | `_get_heap_handle` | `0x68EE8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1342 | `calloc` | `0x68EF8` | 65 | UnwindData |  |
| 101 | `??2@YAPEAX_KHPEBDH@Z` | `0x68F40` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `??_U@YAPEAX_K@Z` | `0x68F40` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `??_V@YAXPEAX@Z` | `0x68F4C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 410 | `_aligned_offset_malloc` | `0x68F58` | 175 | UnwindData |  |
| 409 | `_aligned_msize` | `0x69010` | 101 | UnwindData |  |
| 407 | `_aligned_free` | `0x6907C` | 27 | UnwindData |  |
| 408 | `_aligned_malloc` | `0x690A0` | 112 | UnwindData |  |
| 411 | `_aligned_offset_realloc` | `0x69118` | 455 | UnwindData |  |
| 412 | `_aligned_offset_recalloc` | `0x692E8` | 163 | UnwindData |  |
| 413 | `_aligned_realloc` | `0x69394` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 414 | `_aligned_recalloc` | `0x693A4` | 20 | UnwindData |  |
| 514 | `_expand` | `0x693C0` | 249 | UnwindData |  |
| 634 | `_heapadd` | `0x694C0` | 23 | UnwindData |  |
| 635 | `_heapchk` | `0x694E0` | 45 | UnwindData |  |
| 637 | `_heapset` | `0x69514` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 636 | `_heapmin` | `0x69520` | 33 | UnwindData |  |
| 638 | `_heapused` | `0x69548` | 22 | UnwindData |  |
| 639 | `_heapwalk` | `0x69564` | 327 | UnwindData |  |
| 923 | `_msize` | `0x696B4` | 57 | UnwindData |  |
| 950 | `_recalloc` | `0x696F4` | 134 | UnwindData |  |
| 952 | `_resetstkoflw` | `0x69780` | 294 | UnwindData |  |
| 1472 | `realloc` | `0x698AC` | 211 | UnwindData |  |
| 451 | `_close` | `0x69E40` | 195 | UnwindData |  |
| 565 | `_fstat32` | `0x69F0C` | 935 | UnwindData |  |
| 927 | `_open` | `0x6AA6C` | 213 | UnwindData |  |
| 1010 | `_sopen` | `0x6AC20` | 65 | UnwindData |  |
| 1011 | `_sopen_s` | `0x6AC68` | 50 | UnwindData |  |
| 567 | `_fstat64` | `0x6ACA0` | 964 | UnwindData |  |
| 568 | `_fstat64i32` | `0x6B06C` | 946 | UnwindData |  |
| 566 | `_fstat32i64` | `0x6B424` | 953 | UnwindData |  |
| 1266 | `_wopen` | `0x6BF94` | 213 | UnwindData |  |
| 1285 | `_wsopen` | `0x6C148` | 65 | UnwindData |  |
| 1286 | `_wsopen_s` | `0x6C190` | 50 | UnwindData |  |
| 948 | `_read` | `0x6C8F4` | 283 | UnwindData |  |
| 769 | `_lseeki64` | `0x6CAB4` | 227 | UnwindData |  |
| 1278 | `_write` | `0x6D308` | 223 | UnwindData |  |
| 656 | `_isatty` | `0x6D3F0` | 95 | UnwindData |  |
| 452 | `_commit` | `0x6D458` | 215 | UnwindData |  |
| 768 | `_lseek` | `0x6D5D4` | 223 | UnwindData |  |
| 932 | `_pipe` | `0x6D6BC` | 739 | UnwindData |  |
| 596 | `_get_osfhandle` | `0x6DB0C` | 116 | UnwindData |  |
| 928 | `_open_osfhandle` | `0x6DE74` | 251 | UnwindData |  |
| 1110 | `_ungetch_nolock` | `0x6DF78` | 212 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 608 | `_getch_nolock` | `0x6E04C` | 256 | UnwindData |  |
| 610 | `_getche_nolock` | `0x6E154` | 66 | UnwindData |  |
| 1109 | `_ungetch` | `0x6E340` | 46 | UnwindData |  |
| 607 | `_getch` | `0x6E374` | 42 | UnwindData |  |
| 609 | `_getche` | `0x6E3A4` | 42 | UnwindData |  |
| 750 | `_kbhit` | `0x6E3D4` | 42 | UnwindData |  |
| 625 | `_getwch_nolock` | `0x6E404` | 315 | UnwindData |  |
| 627 | `_getwche_nolock` | `0x6E548` | 79 | UnwindData |  |
| 1113 | `_ungetwch_nolock` | `0x6E5A0` | 44 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 624 | `_getwch` | `0x6E5CC` | 44 | UnwindData |  |
| 626 | `_getwche` | `0x6E600` | 44 | UnwindData |  |
| 1112 | `_ungetwch` | `0x6E634` | 50 | UnwindData |  |
| 940 | `_putch_nolock` | `0x6E66C` | 185 | UnwindData |  |
| 939 | `_putch` | `0x6E72C` | 46 | UnwindData |  |
| 945 | `_putwch_nolock` | `0x6E760` | 89 | UnwindData |  |
| 944 | `_putwch` | `0x6E7C0` | 50 | UnwindData |  |
| 231 | `?_open@@YAHPEBDHH@Z` | `0x6E7F8` | 52 | UnwindData |  |
| 239 | `?_sopen@@YAHPEBDHHH@Z` | `0x6E834` | 43 | UnwindData |  |
| 241 | `?_wopen@@YAHPEB_WHH@Z` | `0x6E868` | 52 | UnwindData |  |
| 242 | `?_wsopen@@YAHPEB_WHHH@Z` | `0x6E8A4` | 43 | UnwindData |  |
| 440 | `_cgets_s` | `0x6E8D8` | 302 | UnwindData |  |
| 439 | `_cgets` | `0x6EA0C` | 110 | UnwindData |  |
| 442 | `_cgetws_s` | `0x6EA80` | 479 | UnwindData |  |
| 441 | `_cgetws` | `0x6EC68` | 90 | UnwindData |  |
| 449 | `_chsize_s` | `0x6EE68` | 239 | UnwindData |  |
| 448 | `_chsize` | `0x6EF60` | 21 | UnwindData |  |
| 466 | `_cputs` | `0x6EF7C` | 120 | UnwindData |  |
| 467 | `_cputws` | `0x6EFFC` | 218 | UnwindData |  |
| 468 | `_creat` | `0x6F0DC` | 55 | UnwindData |  |
| 494 | `_dup` | `0x6F2D0` | 203 | UnwindData |  |
| 495 | `_dup2` | `0x6F514` | 380 | UnwindData |  |
| 503 | `_eof` | `0x6F698` | 280 | UnwindData |  |
| 525 | `_filelength` | `0x6F7B8` | 263 | UnwindData |  |
| 526 | `_filelengthi64` | `0x6F8C8` | 274 | UnwindData |  |
| 978 | `_set_fmode` | `0x6FAB4` | 64 | UnwindData |  |
| 593 | `_get_fmode` | `0x6FAFC` | 47 | UnwindData |  |
| 989 | `_setmode` | `0x6FB34` | 250 | UnwindData |  |
| 761 | `_locking` | `0x6FD20` | 223 | UnwindData |  |
| 920 | `_mktemp_s` | `0x6FE08` | 330 | UnwindData |  |
| 919 | `_mktemp` | `0x6FF58` | 77 | UnwindData |  |
| 1084 | `_tell` | `0x6FFAC` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1085 | `_telli64` | `0x6FFC0` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1185 | `_wcreat` | `0x6FFD4` | 55 | UnwindData |  |
| 1265 | `_wmktemp_s` | `0x70014` | 333 | UnwindData |  |
| 1264 | `_wmktemp` | `0x70168` | 77 | UnwindData |  |
| 979 | `_set_invalid_parameter_handler` | `0x703F8` | 59 | UnwindData |  |
| 595 | `_get_invalid_parameter_handler` | `0x7043C` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 652 | `_invoke_watson` | `0x70450` | 49 | UnwindData |  |
| 649 | `_invalid_parameter` | `0x70488` | 111 | UnwindData |  |
| 650 | `_invalid_parameter_noinfo` | `0x70500` | 30 | UnwindData |  |
| 651 | `_invalid_parameter_noinfo_noreturn` | `0x70524` | 47 | UnwindData |  |
| 228 | `?_invalid_parameter@@YAXPEBG00I_K@Z` | `0x7055C` | 24 | UnwindData |  |
| 938 | `_purecall` | `0x7057C` | 55 | UnwindData |  |
| 983 | `_set_purecall_handler` | `0x705BC` | 59 | UnwindData |  |
| 600 | `_get_purecall_handler` | `0x70600` | 292 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 926 | `_onexit` | `0x70724` | 266 | UnwindData |  |
| 1335 | `atexit` | `0x70834` | 23 | UnwindData |  |
| 330 | `__dllonexit` | `0x70854` | 215 | UnwindData |  |
| 335 | `__fpecode` | `0x70A08` | 20 | UnwindData |  |
| 377 | `__pxcptinfoptrs` | `0x70A24` | 20 | UnwindData |  |
| 1482 | `signal` | `0x70A40` | 701 | UnwindData |  |
| 1469 | `raise` | `0x70D04` | 562 | UnwindData |  |
| 1471 | `rand_s` | `0x70F4C` | 260 | UnwindData |  |
| 288 | `__C_specific_handler` | `0x7124C` | 509 | UnwindData |  |
| 376 | `__pwctype_func` | `0x71C50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 374 | `__pctype_func` | `0x71C60` | 59 | UnwindData |  |
| 284 | `_XcptFilter` | `0x71D60` | 464 | UnwindData |  |
| 289 | `__CppXcptFilter` | `0x71F38` | 344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1396 | `getenv` | `0x72090` | 107 | UnwindData |  |
| 1397 | `getenv_s` | `0x72104` | 253 | UnwindData |  |
| 496 | `_dupenv_s` | `0x72208` | 258 | UnwindData |  |
| 1259 | `_wgetenv` | `0x72484` | 107 | UnwindData |  |
| 1260 | `_wgetenv_s` | `0x724F8` | 254 | UnwindData |  |
| 1231 | `_wdupenv_s` | `0x725FC` | 258 | UnwindData |  |
| 754 | `_local_unwind` | `0x72800` | 36 | UnwindData |  |
| 304 | `__NLG_Dispatch2` | `0x72850` | 1 | UnwindData |  |
| 305 | `__NLG_Return2` | `0x72860` | 1 | UnwindData |  |
| 315 | `___mb_cur_max_func` | `0x72C90` | 58 | UnwindData |  |
| 316 | `___mb_cur_max_l_func` | `0x72CD0` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 312 | `___lc_codepage_func` | `0x72CEC` | 55 | UnwindData |  |
| 313 | `___lc_collate_cp_func` | `0x72D2C` | 55 | UnwindData |  |
| 314 | `___lc_handle_func` | `0x72D6C` | 56 | UnwindData |  |
| 317 | `___setlc_active_func` | `0x72DAC` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 318 | `___unguarded_readlc_active_add_func` | `0x72DBC` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 454 | `_configthreadlocale` | `0x72DCC` | 105 | UnwindData |  |
| 555 | `_free_locale` | `0x72E3C` | 166 | UnwindData |  |
| 336 | `__free_locale` | `0x72EE8` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 588 | `_get_current_locale` | `0x72EF4` | 156 | UnwindData |  |
| 337 | `__get_current_locale` | `0x72F98` | 3,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 469 | `_create_locale` | `0x73BC8` | 311 | UnwindData |  |
| 323 | `__create_locale` | `0x73D08` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1480 | `setlocale` | `0x73D14` | 444 | UnwindData |  |
| 326 | `__crtLCMapStringA` | `0x74390` | 150 | UnwindData |  |
| 327 | `__crtLCMapStringW` | `0x7442C` | 93 | UnwindData |  |
| 324 | `__crtCompareStringA` | `0x747DC` | 137 | UnwindData |  |
| 325 | `__crtCompareStringW` | `0x7486C` | 166 | UnwindData |  |
| 122 | `??_U@YAPEAX_KHPEBDH@Z` | `0x74918` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 269 | `_CRT_RTC_INIT` | `0x74924` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 270 | `_CRT_RTC_INITW` | `0x74924` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 380 | `__set_flsgetvalue` | `0x74924` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 328 | `__crt_debugger_hook` | `0x74930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1433 | `localeconv` | `0x74940` | 56 | UnwindData |  |
| 349 | `__lconv_init` | `0x74980` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 378 | `__report_gsfailure` | `0x74994` | 330 | UnwindData |  |
| 386 | `__sys_nerr` | `0x74AE4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 385 | `__sys_errlist` | `0x74AF4` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 398 | `__wcserror` | `0x74B04` | 388 | UnwindData |  |
| 399 | `__wcserror_s` | `0x74C90` | 241 | UnwindData |  |
| 1324 | `abs` | `0x74D88` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1428 | `labs` | `0x74D88` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 403 | `_abs64` | `0x74D98` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1431 | `llabs` | `0x74D98` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 416 | `_assert` | `0x74DAC` | 2,138 | UnwindData |  |
| 432 | `_byteswap_ulong` | `0x7560C` | 44 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 433 | `_byteswap_ushort` | `0x75638` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 431 | `_byteswap_uint64` | `0x75654` | 120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 751 | `_lfind` | `0x756CC` | 151 | UnwindData |  |
| 752 | `_lfind_s` | `0x7576C` | 156 | UnwindData |  |
| 764 | `_lrotl` | `0x75810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 955 | `_rotl` | `0x75810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 956 | `_rotl64` | `0x75820` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 765 | `_lrotr` | `0x75834` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 957 | `_rotr` | `0x75834` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 958 | `_rotr64` | `0x75844` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 766 | `_lsearch` | `0x75858` | 163 | UnwindData |  |
| 767 | `_lsearch_s` | `0x75904` | 165 | UnwindData |  |
| 774 | `_makepath` | `0x759B0` | 39 | UnwindData |  |
| 775 | `_makepath_s` | `0x759E0` | 326 | UnwindData |  |
| 941 | `_putenv` | `0x75DA8` | 50 | UnwindData |  |
| 942 | `_putenv_s` | `0x75DE0` | 117 | UnwindData |  |
| 972 | `_searchenv_s` | `0x75E5C` | 797 | UnwindData |  |
| 971 | `_searchenv` | `0x76180` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1323 | `abort` | `0x76194` | 64 | UnwindData |  |
| 973 | `_set_abort_behavior` | `0x761DC` | 52 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 985 | `_setjmp` | `0x76210` | 160 | UnwindData |  |
| 1479 | `setjmp` | `0x76210` | 160 | UnwindData |  |
| 986 | `_setjmpex` | `0x762C0` | 144 | UnwindData |  |
| 1020 | `_splitpath` | `0x765EC` | 142 | UnwindData |  |
| 1021 | `_splitpath_s` | `0x76680` | 670 | UnwindData |  |
| 1037 | `_strerror` | `0x76924` | 337 | UnwindData |  |
| 1038 | `_strerror_s` | `0x76A7C` | 231 | UnwindData |  |
| 1107 | `_umask_s` | `0x76B6C` | 67 | UnwindData |  |
| 1106 | `_umask` | `0x76BB8` | 34 | UnwindData |  |
| 1181 | `_wassert` | `0x76C0C` | 2,254 | UnwindData |  |
| 1188 | `_wcserror` | `0x774E0` | 166 | UnwindData |  |
| 1189 | `_wcserror_s` | `0x7758C` | 177 | UnwindData |  |
| 1261 | `_wmakepath` | `0x77644` | 39 | UnwindData |  |
| 1262 | `_wmakepath_s` | `0x77674` | 341 | UnwindData |  |
| 1267 | `_wperror` | `0x777D0` | 386 | UnwindData |  |
| 1274 | `_wputenv` | `0x77C10` | 50 | UnwindData |  |
| 1275 | `_wputenv_s` | `0x77C48` | 117 | UnwindData |  |
| 1283 | `_wsearchenv_s` | `0x77CC4` | 814 | UnwindData |  |
| 1282 | `_wsearchenv` | `0x77FF8` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1284 | `_wsetlocale` | `0x7800C` | 634 | UnwindData |  |
| 1295 | `_wsplitpath` | `0x78528` | 142 | UnwindData |  |
| 1296 | `_wsplitpath_s` | `0x785BC` | 692 | UnwindData |  |
| 1339 | `bsearch` | `0x78878` | 240 | UnwindData |  |
| 1340 | `bsearch_s` | `0x78970` | 250 | UnwindData |  |
| 1352 | `div` | `0x78A70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1430 | `ldiv` | `0x78A70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1432 | `lldiv` | `0x78A90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1438 | `longjmp` | `0x78AC0` | 236 | UnwindData |  |
| 1457 | `perror` | `0x78BB4` | 173 | UnwindData |  |
| 1467 | `qsort` | `0x78D40` | 80 | UnwindData |  |
| 1468 | `qsort_s` | `0x79110` | 80 | UnwindData |  |
| 1491 | `srand` | `0x79458` | 22 | UnwindData |  |
| 1470 | `rand` | `0x79474` | 43 | UnwindData |  |
| 1502 | `strerror` | `0x794A8` | 154 | UnwindData |  |
| 1503 | `strerror_s` | `0x79548` | 142 | UnwindData |  |
| 310 | `__STRINGTOLD_L` | `0x7DB1C` | 117 | UnwindData |  |
| 1 | `$I10_OUTPUT` | `0x7F558` | 2,730 | UnwindData |  |
| 1489 | `sqrt` | `0x80238` | 266 | UnwindData |  |
| 1356 | `fabs` | `0x80358` | 232 | UnwindData |  |
| 435 | `_cabs` | `0x80448` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 445 | `_chgsign` | `0x8045C` | 44 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 446 | `_chgsignf` | `0x80488` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 545 | `_fpreset` | `0x804A8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1032 | `_statusfp` | `0x804B8` | 72 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 450 | `_clearfp` | `0x80500` | 80 | UnwindData |  |
| 455 | `_control87` | `0x80558` | 656 | UnwindData |  |
| 456 | `_controlfp` | `0x807F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 974 | `_set_controlfp` | `0x80800` | 52 | UnwindData |  |
| 457 | `_controlfp_s` | `0x8083C` | 99 | UnwindData |  |
| 458 | `_copysign` | `0x808A8` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 459 | `_copysignf` | `0x808E8` | 52 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 537 | `_finite` | `0x8091C` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 538 | `_finitef` | `0x8094C` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 722 | `_isnan` | `0x8096C` | 52 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 723 | `_isnanf` | `0x809A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 542 | `_fpclass` | `0x809C0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 543 | `_fpclassf` | `0x80A80` | 124 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 924 | `_nextafter` | `0x80AFC` | 485 | UnwindData |  |
| 925 | `_nextafterf` | `0x80CE8` | 393 | UnwindData |  |
| 959 | `_scalb` | `0x80E78` | 476 | UnwindData |  |
| 960 | `_scalbf` | `0x8105C` | 414 | UnwindData |  |
| 544 | `_fpieee_flt` | `0x81200` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 640 | `_hypot` | `0x81228` | 623 | UnwindData |  |
| 641 | `_hypotf` | `0x814A0` | 335 | UnwindData |  |
| 747 | `_j0` | `0x815F8` | 584 | UnwindData |  |
| 748 | `_j1` | `0x81848` | 628 | UnwindData |  |
| 749 | `_jn` | `0x81AC4` | 404 | UnwindData |  |
| 1320 | `_y0` | `0x81CB8` | 647 | UnwindData |  |
| 1321 | `_y1` | `0x81F48` | 673 | UnwindData |  |
| 1322 | `_yn` | `0x821F0` | 228 | UnwindData |  |
| 762 | `_logb` | `0x822DC` | 290 | UnwindData |  |
| 763 | `_logbf` | `0x82404` | 226 | UnwindData |  |
| 1325 | `acos` | `0x824EC` | 762 | UnwindData |  |
| 1326 | `acosf` | `0x827EC` | 665 | UnwindData |  |
| 1329 | `asin` | `0x82A8C` | 730 | UnwindData |  |
| 1330 | `asinf` | `0x82D6C` | 601 | UnwindData |  |
| 1331 | `atan` | `0x82FCC` | 618 | UnwindData |  |
| 1332 | `atan2` | `0x8323C` | 2,006 | UnwindData |  |
| 1333 | `atan2f` | `0x83A18` | 1,222 | UnwindData |  |
| 1334 | `atanf` | `0x83EE4` | 588 | UnwindData |  |
| 1343 | `ceil` | `0x84138` | 276 | UnwindData |  |
| 1344 | `ceilf` | `0x84254` | 209 | UnwindData |  |
| 1350 | `cosh` | `0x8446C` | 952 | UnwindData |  |
| 1351 | `coshf` | `0x84960` | 708 | UnwindData |  |
| 1366 | `floor` | `0x84C38` | 259 | UnwindData |  |
| 1367 | `floorf` | `0x84D44` | 203 | UnwindData |  |
| 1368 | `fmod` | `0x84E20` | 202 | UnwindData |  |
| 1369 | `fmodf` | `0x84EF0` | 198 | UnwindData |  |
| 1383 | `frexp` | `0x84FBC` | 228 | UnwindData |  |
| 1429 | `ldexp` | `0x850A8` | 386 | UnwindData |  |
| 1455 | `modf` | `0x85238` | 200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1456 | `modff` | `0x85300` | 460 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1485 | `sinh` | `0x854CC` | 1,030 | UnwindData |  |
| 1486 | `sinhf` | `0x85A0C` | 727 | UnwindData |  |
| 1490 | `sqrtf` | `0x85CEC` | 224 | UnwindData |  |
| 1526 | `tan` | `0x85FB4` | 758 | UnwindData |  |
| 1527 | `tanf` | `0x86528` | 889 | UnwindData |  |
| 1528 | `tanh` | `0x869DC` | 732 | UnwindData |  |
| 1529 | `tanhf` | `0x86CC0` | 730 | UnwindData |  |
| 116 | `??_7exception@std@@6B@` | `0x92768` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `??_7bad_cast@std@@6B@` | `0x92798` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `??_7bad_typeid@std@@6B@` | `0x927B0` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `??_7__non_rtti_object@std@@6B@` | `0x927C8` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `??_7exception@@6B@` | `0x928D8` | 6,376 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1230 | `_wctype` | `0x941C0` | 123,904 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 653 | `_iob` | `0xB25C0` | 1,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1089 | `_timezone` | `0xB2A00` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 489 | `_daylight` | `0xB2A04` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 493 | `_dstbias` | `0xB2A08` | 136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1096 | `_tzname` | `0xB2A90` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 802 | `_mbctype` | `0xB2CE0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 781 | `_mbcasemap` | `0xB2DF0` | 1,424 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 321 | `__badioinfo` | `0xB3380` | 1,496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 930 | `_pctype` | `0xB3958` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 947 | `_pwctype` | `0xB3960` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 348 | `__lconv` | `0xB3988` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 350 | `__mb_cur_max` | `0xB3A28` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1082 | `_sys_errlist` | `0xB3A40` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1083 | `_sys_nerr` | `0xB3BA0` | 960 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 279 | `_HUGE` | `0xB3F60` | 13,412 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 319 | `__argc` | `0xB73C4` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 320 | `__argv` | `0xB73C8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 397 | `__wargv` | `0xB73D0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 502 | `_environ` | `0xB73D8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 341 | `__initenv` | `0xB73E0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1232 | `_wenviron` | `0xB73E8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 402 | `__winitenv` | `0xB73F0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 931 | `_pgmptr` | `0xB73F8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1268 | `_wpgmptr` | `0xB7400` | 1,616 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1184 | `_wcmdln` | `0xB7A50` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 406 | `_acmdln` | `0xB7A58` | 1,692 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 453 | `_commode` | `0xB80F4` | 612 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 541 | `_fmode` | `0xB8358` | 6,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 375 | `__pioinfo` | `0xB9B40` | 516 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 381 | `__setlc_active` | `0xB9D44` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 395 | `__unguarded_readlc_active` | `0xB9D48` | 33,480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1354 | `exp` | `0xC2010` | 664 | UnwindData |  |
| 1348 | `cos` | `0xC22B0` | 1,165 | UnwindData |  |
| 1349 | `cosf` | `0xC2750` | 768 | UnwindData |  |
| 1355 | `expf` | `0xC2A60` | 344 | UnwindData |  |
| 1434 | `log` | `0xC2BC0` | 702 | UnwindData |  |
| 1435 | `log10` | `0xC2E90` | 798 | UnwindData |  |
| 1436 | `log10f` | `0xC31C0` | 645 | UnwindData |  |
| 1437 | `logf` | `0xC3450` | 597 | UnwindData |  |
| 1458 | `pow` | `0xC36B0` | 2,993 | UnwindData |  |
| 1459 | `powf` | `0xC4270` | 2,093 | UnwindData |  |
| 1483 | `sin` | `0xC4AB0` | 1,165 | UnwindData |  |
| 1484 | `sinf` | `0xC4F50` | 893 | UnwindData |  |
