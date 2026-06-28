# Binary Specification: gpapi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\gpapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b1fba0742e0f859cb177804a8e97bb9a00c73a4bbf2edf7abc53c023b7ddeaf8`
* **Total Exported Functions:** 53

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 126 | `RefreshPolicyExInternalWorker` | `0x14E0` | 257 | UnwindData |  |
| 115 | *Ordinal Only* | `0x15F0` | 741 | UnwindData |  |
| 121 | `GetAppliedGPOListInternalWWorker` | `0x1D60` | 29 | UnwindData |  |
| 130 | `UnregisterGPNotificationInternalWorker` | `0x2090` | 665 | UnwindData |  |
| 112 | `EnterCriticalPolicySectionExStub` | `0x23A0` | 841 | UnwindData |  |
| 113 | *Ordinal Only* | `0x23A0` | 841 | UnwindData |  |
| 128 | `RegisterGPNotificationInternalWorker` | `0x26F0` | 225 | UnwindData |  |
| 125 | `LeaveCriticalPolicySectionInternalWorker` | `0x2DE0` | 460 | UnwindData |  |
| 120 | `GetAppliedGPOListInternalAWorker` | `0x51B0` | 55 | UnwindData |  |
| 129 | `RsopLoggingEnabledInternalWorker` | `0x6CA0` | 297 | UnwindData |  |
| 118 | `FreeGPOListInternalAWorker` | `0x76D0` | 47 | UnwindData |  |
| 117 | `EnterCriticalPolicySectionInternalWorker` | `0x7710` | 26,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `GetNextFgPolicyRefreshInfoInternalWorker` | `0xDE50` | 3,856 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `GetGPOListInternalAWorker` | `0xED60` | 259 | UnwindData |  |
| 131 | `AreThereVisibleLogoffScriptsInternal` | `0xEEA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `AreThereVisibleLogoffScriptsInternalWorker` | `0xEEA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `AreThereVisibleShutdownScriptsInternal` | `0xEED0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `AreThereVisibleShutdownScriptsInternalWorker` | `0xEED0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `GenerateGPNotificationInternalWorker` | `0xEF30` | 333 | UnwindData |  |
| 123 | `GetGPOListInternalWWorker` | `0xF090` | 1,444 | UnwindData |  |
| 116 | *Ordinal Only* | `0xF640` | 1,126 | UnwindData |  |
| 148 | `HasPolicyForegroundProcessingCompletedInternal` | `0xFD40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `HasPolicyForegroundProcessingCompletedInternalWorker` | `0xFD40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `RefreshPolicyInternalWorker` | `0xFD50` | 189 | UnwindData |  |
| 114 | *Ordinal Only* | `0xFE20` | 298 | UnwindData |  |
| 107 | *Ordinal Only* | `0xFF50` | 164 | UnwindData |  |
| 133 | `EnterCriticalPolicySectionInternal` | `0x10780` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `ForceSyncFgPolicyInternal` | `0x107A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `ForceSyncFgPolicyInternalWorker` | `0x107C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `FreeGPOListInternalA` | `0x107F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `FreeGPOListInternalW` | `0x10810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `FreeGPOListInternalWWorker` | `0x10830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `GenerateGPNotificationInternal` | `0x10840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `GetAppliedGPOListInternalA` | `0x10860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `GetAppliedGPOListInternalW` | `0x10880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `GetGPOListInternalA` | `0x108A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `GetGPOListInternalW` | `0x108C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `GetNextFgPolicyRefreshInfoInternal` | `0x108E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `GetPreviousFgPolicyRefreshInfoInternal` | `0x10900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `GetPreviousFgPolicyRefreshInfoInternalWorker` | `0x10920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | *Ordinal Only* | `0x10940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `IsSyncForegroundPolicyRefreshWorker` | `0x10960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `LeaveCriticalPolicySectionInternal` | `0x10970` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | `RefreshPolicyExInternal` | `0x10990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `RefreshPolicyInternal` | `0x109B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `RegisterGPNotificationInternal` | `0x109D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `RsopLoggingEnabledInternal` | `0x109F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `UnregisterGPNotificationInternal` | `0x10A10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `WaitForMachinePolicyForegroundProcessingInternal` | `0x10A30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `WaitForMachinePolicyForegroundProcessingInternalWorker` | `0x10A50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 158 | `WaitForUserPolicyForegroundProcessingInternal` | `0x10A60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `WaitForUserPolicyForegroundProcessingInternalWorker` | `0x10A80` | 43,152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | *Ordinal Only* | `0x1B310` | 0 | Indeterminate |  |
