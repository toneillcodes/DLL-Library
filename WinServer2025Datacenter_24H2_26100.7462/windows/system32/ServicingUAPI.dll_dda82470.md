# Binary Specification: ServicingUAPI.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ServicingUAPI.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `dda8247049436bccf8c39e0385e42aee2d6f567d3979892e3ea025fc0689aec1`
* **Total Exported Functions:** 13

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllMain` | `0x5C50` | 219 | UnwindData |  |
| 2 | `EnumerateFeatures` | `0xF9D0` | 747 | UnwindData |  |
| 3 | `FreeEnumerateFeaturesResult` | `0xFCD0` | 77 | UnwindData |  |
| 7 | `GetFeatureState` | `0xFD30` | 537 | UnwindData |  |
| 8 | `GetServicingStatus` | `0xFF50` | 169 | UnwindData |  |
| 10 | `IsFeatureInstalled` | `0x10000` | 638 | UnwindData |  |
| 4 | `FreeInstallFeaturesResult` | `0x10810` | 78 | UnwindData |  |
| 5 | `FreeModifyFeaturesResult` | `0x10810` | 78 | UnwindData |  |
| 9 | `InstallFeatures` | `0x10870` | 244 | UnwindData |  |
| 11 | `ModifyFeatures` | `0x11560` | 2,432 | UnwindData |  |
| 12 | `PrepareSandboxForInboxUse` | `0x11EF0` | 192 | UnwindData |  |
| 6 | `FreeUninstallFeaturesResult` | `0x12070` | 78 | UnwindData |  |
| 13 | `UninstallFeatures` | `0x120D0` | 227 | UnwindData |  |
