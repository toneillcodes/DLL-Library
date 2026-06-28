# Binary Specification: appmgmts.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\appmgmts.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `abb2ad5aad8bfb9432390117d937c710eacbd61346d78c39dabd391a3da467c8`
* **Total Exported Functions:** 19

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 13 | `GenerateGroupPolicy` | `0xC3C0` | 375 | UnwindData |  |
| 15 | `ProcessGroupPolicyObjectsEx` | `0xC5F0` | 731 | UnwindData |  |
| 19 | `ServiceMain` | `0xE770` | 357 | UnwindData |  |
| 11 | `DllCanUnloadNow` | `0x1B540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `DllGetClassObject` | `0x1B560` | 191 | UnwindData |  |
| 1 | `CsSetOptions` | `0x1D080` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CsCreateClassStore` | `0x1D2F0` | 282 | UnwindData |  |
| 3 | `CsEnumApps` | `0x1D410` | 151 | UnwindData |  |
| 4 | `CsGetAppCategories` | `0x1D4B0` | 102 | UnwindData |  |
| 5 | `CsGetClassAccess` | `0x1D590` | 48 | UnwindData |  |
| 6 | `CsGetClassStore` | `0x1D5D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `CsGetClassStorePath` | `0x1D5F0` | 213 | UnwindData |  |
| 8 | `CsRegisterAppCategory` | `0x1D6D0` | 103 | UnwindData |  |
| 9 | `CsServerGetClassStore` | `0x1D740` | 110 | UnwindData |  |
| 10 | `CsUnregisterAppCategory` | `0x1D7C0` | 103 | UnwindData |  |
| 16 | `ReleaseAppCategoryInfoList` | `0x1D830` | 103 | UnwindData |  |
| 17 | `ReleasePackageDetail` | `0x1D8A0` | 633 | UnwindData |  |
| 18 | `ReleasePackageInfo` | `0x1DB20` | 379 | UnwindData |  |
| 14 | `IID_IClassAdmin` | `0x329C8` | 0 | Indeterminate |  |
