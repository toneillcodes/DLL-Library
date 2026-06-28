# Binary Specification: TlsBrand.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\TlsBrand.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a8e064479a152952795619d90cfc53ce37ab3e6738cd4fc52b095ab724945e57`
* **Total Exported Functions:** 46

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `??0ICALDetails@@QEAA@AEBV0@@Z` | `0x27D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0ICALDetails@@QEAA@XZ` | `0x27D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0ICALStringDetails@@QEAA@AEBV0@@Z` | `0x27F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `??0ICALStringDetails@@QEAA@XZ` | `0x27F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `??0IW2K3ADPUCALDetails@@QEAA@AEBV0@@Z` | `0x2810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `??0IW2K3ADPUCALDetails@@QEAA@XZ` | `0x2810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `??0IWMICALDetails@@QEAA@AEBV0@@Z` | `0x2830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `??0IWMICALDetails@@QEAA@XZ` | `0x2830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `??1ICALDetails@@UEAA@XZ` | `0x2850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `??1ICALStringDetails@@UEAA@XZ` | `0x2870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `??1IW2K3ADPUCALDetails@@UEAA@XZ` | `0x2890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `??1IWMICALDetails@@UEAA@XZ` | `0x28B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `??4ICALDetails@@QEAAAEAV0@AEBV0@@Z` | `0x28D0` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `??4ICALStringDetails@@QEAAAEAV0@AEBV0@@Z` | `0x28D0` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `??4IRDSProductDetails@@QEAAAEAV0@AEBV0@@Z` | `0x28D0` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `??4IW2K3ADPUCALDetails@@QEAAAEAV0@AEBV0@@Z` | `0x28D0` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `??4IWMICALDetails@@QEAAAEAV0@AEBV0@@Z` | `0x28D0` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `LicBrandFormatString` | `0x2AE0` | 33,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `CALDetailsCreator` | `0xACE0` | 232 | UnwindData |  |
| 37 | `GetCALVersion` | `0xD550` | 115 | UnwindData |  |
| 38 | `GetCALVersionStrings` | `0xD5D0` | 421 | UnwindData |  |
| 39 | `GetConversionVersionStrings` | `0xD780` | 789 | UnwindData |  |
| 27 | `CALStringDetailsCreator` | `0xE450` | 232 | UnwindData |  |
| 28 | `CRetailCALCreator` | `0x10480` | 232 | UnwindData |  |
| 29 | `CWMICALDetailsCreator` | `0x10E00` | 232 | UnwindData |  |
| 35 | `W2K3ADPUCALDetailsCreator` | `0x11FD0` | 172 | UnwindData |  |
| 5 | `??0IRDSProductDetails@@QEAA@AEBV0@@Z` | `0x121D0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `??0IRDSProductDetails@@QEAA@XZ` | `0x121D0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `??1IRDSProductDetails@@UEAA@XZ` | `0x12310` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `?GetAccessRights@IRDSProductDetails@@UEAAJPEAGPEAK1@Z` | `0x12550` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `?GetProductFromAccessRights@IRDSProductDetails@@UEAAJKKPEAPEAG@Z` | `0x12550` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `?IsTestHookValid@IRDSProductDetails@@UEAAHPEAK@Z` | `0x12550` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `RDSProductDetailsCreator` | `0x12630` | 172 | UnwindData |  |
| 45 | `RDSGetProductAccessRights` | `0x12910` | 132 | UnwindData |  |
| 42 | `RDSGetCALVersionString` | `0x129A0` | 121 | UnwindData |  |
| 43 | `RDSGetCurrentVersion` | `0x12A20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `RDSGetOSVersionString` | `0x12A30` | 121 | UnwindData |  |
| 36 | `CleanupRDLSConfig` | `0x13870` | 243 | UnwindData |  |
| 40 | `GetRdlsSupportedFeatureMask` | `0x13970` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `LoadRDLSConfig` | `0x139B0` | 8,204 | UnwindData |  |
| 46 | `UpdateRDLSConfig` | `0x159D0` | 2,090 | UnwindData |  |
| 21 | `??_7ICALDetails@@6B@` | `0x1BA98` | 104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `??_7ICALStringDetails@@6B@` | `0x1BB00` | 88 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `??_7IW2K3ADPUCALDetails@@6B@` | `0x1BB58` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `??_7IWMICALDetails@@6B@` | `0x1BB70` | 552 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `??_7IRDSProductDetails@@6B@` | `0x1BD98` | 0 | Indeterminate |  |
