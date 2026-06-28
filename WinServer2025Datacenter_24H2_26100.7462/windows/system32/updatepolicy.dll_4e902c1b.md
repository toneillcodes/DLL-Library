# Binary Specification: updatepolicy.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\updatepolicy.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4e902c1bf0e7caa691c5bd0d9820a660fe0c8ee5918257730ced89dd2a6a7b05`
* **Total Exported Functions:** 13

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 10 | `DllGetClassObject` | `0x3A00` | 187 | UnwindData |  |
| 9 | `DllCanUnloadNow` | `0x3AD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `DllRegisterServer` | `0x3AF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `DllUnregisterServer` | `0x3B10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `ReadPolicy` | `0x3B30` | 169 | UnwindData |  |
| 5 | `ReadPolicyWithFallback` | `0x3BE0` | 169 | UnwindData |  |
| 13 | `GetSkuUpdateManagementGroup` | `0x3C90` | 140 | UnwindData |  |
| 3 | `GetUpdatePolicyName` | `0x3D30` | 169 | UnwindData |  |
| 2 | `GetEnterprisePolicyName` | `0x3DE0` | 169 | UnwindData |  |
| 7 | `ReleaseEnterprisePolicyValue` | `0x3E90` | 155 | UnwindData |  |
| 8 | `ReleaseUpdatePolicyValue` | `0x3F40` | 155 | UnwindData |  |
| 1 | `GetAutoUpdatePolicy` | `0x3FF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `ReleaseAutoUpdatePolicy` | `0x4010` | 71,506 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
