# Binary Specification: updatepolicy.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\updatepolicy.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `03c2a38d06d92080780466f3d8cc84ee02927f7a80915938a43227b727b1b53c`
* **Total Exported Functions:** 13

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 10 | `DllGetClassObject` | `0x3B40` | 187 | UnwindData |  |
| 9 | `DllCanUnloadNow` | `0x3C10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `DllRegisterServer` | `0x3C30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `DllUnregisterServer` | `0x3C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `ReadPolicy` | `0x3C70` | 169 | UnwindData |  |
| 5 | `ReadPolicyWithFallback` | `0x3D20` | 169 | UnwindData |  |
| 13 | `GetSkuUpdateManagementGroup` | `0x3DD0` | 140 | UnwindData |  |
| 3 | `GetUpdatePolicyName` | `0x3E70` | 169 | UnwindData |  |
| 2 | `GetEnterprisePolicyName` | `0x3F20` | 169 | UnwindData |  |
| 7 | `ReleaseEnterprisePolicyValue` | `0x3FD0` | 155 | UnwindData |  |
| 8 | `ReleaseUpdatePolicyValue` | `0x4080` | 155 | UnwindData |  |
| 1 | `GetAutoUpdatePolicy` | `0x4130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `ReleaseAutoUpdatePolicy` | `0x4150` | 72,386 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
