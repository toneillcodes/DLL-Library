# Binary Specification: gpapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\gpapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5349e3cf29745c009d14979069b70e3ad4b01e19bc6e82f8f7e48cf0d561bbf6`
* **Total Exported Functions:** 53

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 121 | `GetAppliedGPOListInternalWWorker` | `0x14B0` | 29 | UnwindData |  |
| 130 | `UnregisterGPNotificationInternalWorker` | `0x17B0` | 820 | UnwindData |  |
| 128 | `RegisterGPNotificationInternalWorker` | `0x1B30` | 225 | UnwindData |  |
| 125 | `LeaveCriticalPolicySectionInternalWorker` | `0x2240` | 460 | UnwindData |  |
| 120 | `GetAppliedGPOListInternalAWorker` | `0x45E0` | 55 | UnwindData |  |
| 115 | *Ordinal Only* | `0x5490` | 741 | UnwindData |  |
| 126 | `RefreshPolicyExInternalWorker` | `0x5780` | 257 | UnwindData |  |
| 129 | `RsopLoggingEnabledInternalWorker` | `0x5FA0` | 297 | UnwindData |  |
| 112 | `EnterCriticalPolicySectionExStub` | `0x68A0` | 1,872 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `FreeGPOListInternalAWorker` | `0x6FF0` | 47 | UnwindData |  |
| 117 | `EnterCriticalPolicySectionInternalWorker` | `0x7030` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | *Ordinal Only* | `0x7280` | 12 | UnwindData |  |
| 145 | `GetNextFgPolicyRefreshInfoInternalWorker` | `0xDE20` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `GetGPOListInternalAWorker` | `0xF160` | 259 | UnwindData |  |
| 131 | `AreThereVisibleLogoffScriptsInternal` | `0x10B80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `AreThereVisibleLogoffScriptsInternalWorker` | `0x10B80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `AreThereVisibleShutdownScriptsInternal` | `0x10BB0` | 2,176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `AreThereVisibleShutdownScriptsInternalWorker` | `0x10BB0` | 2,176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `GenerateGPNotificationInternalWorker` | `0x11430` | 333 | UnwindData |  |
| 123 | `GetGPOListInternalWWorker` | `0x11F60` | 1,444 | UnwindData |  |
| 116 | *Ordinal Only* | `0x12AC0` | 1,126 | UnwindData |  |
| 148 | `HasPolicyForegroundProcessingCompletedInternal` | `0x131C0` | 7,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `HasPolicyForegroundProcessingCompletedInternalWorker` | `0x131C0` | 7,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `RefreshPolicyInternalWorker` | `0x14DD0` | 189 | UnwindData |  |
| 114 | *Ordinal Only* | `0x17080` | 533 | UnwindData |  |
| 107 | *Ordinal Only* | `0x172A0` | 164 | UnwindData |  |
| 133 | `EnterCriticalPolicySectionInternal` | `0x18500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `ForceSyncFgPolicyInternal` | `0x18520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `ForceSyncFgPolicyInternalWorker` | `0x18540` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `FreeGPOListInternalA` | `0x18570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `FreeGPOListInternalW` | `0x18590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `FreeGPOListInternalWWorker` | `0x185B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `GenerateGPNotificationInternal` | `0x185C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `GetAppliedGPOListInternalA` | `0x185E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `GetAppliedGPOListInternalW` | `0x18600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `GetGPOListInternalA` | `0x18620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `GetGPOListInternalW` | `0x18640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `GetNextFgPolicyRefreshInfoInternal` | `0x18660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `GetPreviousFgPolicyRefreshInfoInternal` | `0x18680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `GetPreviousFgPolicyRefreshInfoInternalWorker` | `0x186A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | *Ordinal Only* | `0x186C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `IsSyncForegroundPolicyRefreshWorker` | `0x186E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `LeaveCriticalPolicySectionInternal` | `0x186F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | `RefreshPolicyExInternal` | `0x18710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `RefreshPolicyInternal` | `0x18730` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `RegisterGPNotificationInternal` | `0x18750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `RsopLoggingEnabledInternal` | `0x18770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `UnregisterGPNotificationInternal` | `0x18790` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `WaitForMachinePolicyForegroundProcessingInternal` | `0x187B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `WaitForMachinePolicyForegroundProcessingInternalWorker` | `0x187D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 158 | `WaitForUserPolicyForegroundProcessingInternal` | `0x187E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `WaitForUserPolicyForegroundProcessingInternalWorker` | `0x18800` | 6,288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | *Ordinal Only* | `0x1A090` | 0 | Indeterminate |  |
