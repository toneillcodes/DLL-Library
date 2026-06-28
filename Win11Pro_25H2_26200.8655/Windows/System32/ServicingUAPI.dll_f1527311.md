# Binary Specification: ServicingUAPI.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ServicingUAPI.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f1527311f1be35b0203a43dc8dfc0c89d83448913550407119f3394d1f446268`
* **Total Exported Functions:** 13

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllMain` | `0x5C60` | 219 | UnwindData |  |
| 2 | `EnumerateFeatures` | `0xFA90` | 747 | UnwindData |  |
| 3 | `FreeEnumerateFeaturesResult` | `0xFD90` | 77 | UnwindData |  |
| 7 | `GetFeatureState` | `0xFDF0` | 537 | UnwindData |  |
| 8 | `GetServicingStatus` | `0x10010` | 169 | UnwindData |  |
| 10 | `IsFeatureInstalled` | `0x100C0` | 638 | UnwindData |  |
| 4 | `FreeInstallFeaturesResult` | `0x108D0` | 78 | UnwindData |  |
| 5 | `FreeModifyFeaturesResult` | `0x108D0` | 78 | UnwindData |  |
| 9 | `InstallFeatures` | `0x10930` | 244 | UnwindData |  |
| 11 | `ModifyFeatures` | `0x11620` | 2,432 | UnwindData |  |
| 12 | `PrepareSandboxForInboxUse` | `0x11FB0` | 192 | UnwindData |  |
| 6 | `FreeUninstallFeaturesResult` | `0x12130` | 78 | UnwindData |  |
| 13 | `UninstallFeatures` | `0x12190` | 227 | UnwindData |  |
