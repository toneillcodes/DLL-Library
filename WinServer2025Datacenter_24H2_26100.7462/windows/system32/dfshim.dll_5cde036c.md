# Binary Specification: dfshim.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\dfshim.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5cde036cc65a8c24fef6f1a32e2e1e2c323f7d71061cb487e70a0916412c618f`
* **Total Exported Functions:** 20

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `KillService` | `0xEC40` | 103 | UnwindData |  |
| 7 | `LaunchApplication` | `0xECB0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `ShArpMaintain` | `0xEE10` | 326 | UnwindData |  |
| 10 | `ShArpMaintainW` | `0xEF60` | 326 | UnwindData |  |
| 11 | `ShOpenVerbApplication` | `0xF0B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `ShOpenVerbApplicationW` | `0xF0D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `ShOpenVerbExtension` | `0xF0F0` | 193 | UnwindData |  |
| 14 | `ShOpenVerbExtensionW` | `0xF1C0` | 193 | UnwindData |  |
| 15 | `ShOpenVerbShortcut` | `0xF290` | 245 | UnwindData |  |
| 16 | `ShOpenVerbShortcutW` | `0xF390` | 288 | UnwindData |  |
| 17 | `CleanOnlineAppCache` | `0xF750` | 110 | UnwindData |  |
| 18 | `DllCanUnloadNow` | `0xF7D0` | 107 | UnwindData |  |
| 19 | `DllGetClassObject` | `0xF850` | 275 | UnwindData |  |
| 20 | `GetDeploymentDataFromManifest` | `0xF9A0` | 442 | UnwindData |  |
| 1 | `CreateActContext` | `0x12780` | 81 | UnwindData |  |
| 2 | `CreateCMSFromXml` | `0x127E0` | 121 | UnwindData |  |
| 3 | `GetCurrentActContext` | `0x12860` | 66 | UnwindData |  |
| 4 | `GetUserStateManager` | `0x128B0` | 111 | UnwindData |  |
| 5 | `GetUserStore` | `0x12930` | 111 | UnwindData |  |
| 8 | `ParseManifest` | `0x129B0` | 113 | UnwindData |  |
