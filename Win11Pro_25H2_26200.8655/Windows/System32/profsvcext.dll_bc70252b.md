# Binary Specification: profsvcext.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\profsvcext.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `bc70252b662bc11eaa04761e6efbadb869c672e6c31a2f15814cd54633328554`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `InitializeSuspendFolderPolicyAndUploadTaskConfig` | `0x29E0` | 152 | UnwindData |  |
| 1 | `CreateRoamingProviderInstance` | `0x43A0` | 69 | UnwindData |  |
| 5 | `StartRoamingClassFactories` | `0x6DD0` | 21,504 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `ConnectToRoamingVhdProfile` | `0xC1D0` | 56 | UnwindData |  |
| 4 | `RefreshSuspendFolderPolicyAndUploadTaskConfig` | `0xC350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `StopRoamingClassFactories` | `0xC360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `WaitForNetworkForRoamingProfile` | `0xC370` | 79,621 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
