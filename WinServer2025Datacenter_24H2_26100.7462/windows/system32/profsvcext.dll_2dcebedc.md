# Binary Specification: profsvcext.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\profsvcext.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2dcebedc144cae692dbbb222aa1592440db253b400d0a6d44c899a6cef543654`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `InitializeSuspendFolderPolicyAndUploadTaskConfig` | `0x28E0` | 152 | UnwindData |  |
| 1 | `CreateRoamingProviderInstance` | `0x42A0` | 69 | UnwindData |  |
| 5 | `StartRoamingClassFactories` | `0x6CA0` | 21,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `ConnectToRoamingVhdProfile` | `0xC000` | 56 | UnwindData |  |
| 4 | `RefreshSuspendFolderPolicyAndUploadTaskConfig` | `0xC180` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `StopRoamingClassFactories` | `0xC190` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `WaitForNetworkForRoamingProfile` | `0xC1A0` | 63,516 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
