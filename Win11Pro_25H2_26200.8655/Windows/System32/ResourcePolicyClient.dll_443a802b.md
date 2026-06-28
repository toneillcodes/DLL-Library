# Binary Specification: ResourcePolicyClient.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ResourcePolicyClient.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `443a802b2287d316661794f69c690651f46d28fe905e93871cd8cbc99528e79c`
* **Total Exported Functions:** 15

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `CreateResourcePolicyEngineClient` | `0x22D0` | 48 | UnwindData |  |
| 3 | `CreateResourcePolicyStoreClient` | `0x2EF0` | 134 | UnwindData |  |
| 5 | `FreeResourcePolicyStoreClient` | `0x2F80` | 96 | UnwindData |  |
| 6 | `InterruptiveUIStateChanged_Subscribe` | `0x31E0` | 250 | UnwindData |  |
| 7 | `InterruptiveUIStateChanged_Unsubscribe` | `0x32E0` | 117 | UnwindData |  |
| 8 | `QueryApplicationInterruptiveUIState` | `0x3360` | 221 | UnwindData |  |
| 9 | `QueryApplicationInterruptiveUIStateByPsmKey` | `0x3450` | 221 | UnwindData |  |
| 10 | `QueryPackageInterruptiveUIState` | `0x3540` | 221 | UnwindData |  |
| 11 | `ResourcePolicy_GetGlobalProcessAffinityMask` | `0x3630` | 13,968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `ResourcePolicy_GetProcessAffinityMask` | `0x3630` | 13,968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `ResourcePolicy_RevertProcessAffinityMask` | `0x3630` | 13,968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `ResourcePolicy_SetGlobalProcessAffinityMask` | `0x3630` | 13,968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `ResourcePolicy_SetProcessAffinityMask` | `0x3630` | 13,968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `CreateGameConfigStoreClient` | `0x6CC0` | 181 | UnwindData |  |
| 4 | `FreeGameConfigStoreClient` | `0x6D80` | 22 | UnwindData |  |
