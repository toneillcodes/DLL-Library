# Binary Specification: appmgmts.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\appmgmts.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d6f2ace7f110e077bdb25570805d7b90f7b8d242dda461cbf8be2c39d569e075`
* **Total Exported Functions:** 19

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 13 | `GenerateGroupPolicy` | `0xBF90` | 375 | UnwindData |  |
| 15 | `ProcessGroupPolicyObjectsEx` | `0xC1C0` | 731 | UnwindData |  |
| 19 | `ServiceMain` | `0xE2B0` | 357 | UnwindData |  |
| 11 | `DllCanUnloadNow` | `0x1B430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `DllGetClassObject` | `0x1B450` | 191 | UnwindData |  |
| 1 | `CsSetOptions` | `0x1CF70` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CsCreateClassStore` | `0x1D1F0` | 282 | UnwindData |  |
| 3 | `CsEnumApps` | `0x1D310` | 151 | UnwindData |  |
| 4 | `CsGetAppCategories` | `0x1D3B0` | 102 | UnwindData |  |
| 5 | `CsGetClassAccess` | `0x1D490` | 48 | UnwindData |  |
| 6 | `CsGetClassStore` | `0x1D4D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `CsGetClassStorePath` | `0x1D4F0` | 213 | UnwindData |  |
| 8 | `CsRegisterAppCategory` | `0x1D5D0` | 103 | UnwindData |  |
| 9 | `CsServerGetClassStore` | `0x1D640` | 110 | UnwindData |  |
| 10 | `CsUnregisterAppCategory` | `0x1D6C0` | 103 | UnwindData |  |
| 16 | `ReleaseAppCategoryInfoList` | `0x1D730` | 103 | UnwindData |  |
| 17 | `ReleasePackageDetail` | `0x1D7A0` | 633 | UnwindData |  |
| 18 | `ReleasePackageInfo` | `0x1DA20` | 379 | UnwindData |  |
| 14 | `IID_IClassAdmin` | `0x33E58` | 0 | Indeterminate |  |
