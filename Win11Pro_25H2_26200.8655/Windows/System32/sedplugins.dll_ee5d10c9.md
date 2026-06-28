# Binary Specification: sedplugins.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\sedplugins.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ee5d10c9f99ad0eed081a2578c0de1943b79fd09efa526b243ac5456fa841a5c`
* **Total Exported Functions:** 19

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CheckShellTask` | `0x133D0` | 197 | UnwindData |  |
| 4 | `ExecuteShell` | `0x134A0` | 152 | UnwindData |  |
| 17 | `SedimentDriver_Init` | `0x13540` | 362 | UnwindData |  |
| 18 | `SedimentDriver_Init_Aqua` | `0x136C0` | 174 | UnwindData |  |
| 19 | `SedimentDriver_Uninit` | `0x13780` | 75 | UnwindData |  |
| 8 | `Plugin_Init` | `0x137E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `Plugin_Uninit` | `0x137F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `RegisterApplication` | `0x13800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `EnumeratePluginsWithApplicationSource` | `0x13820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `EnumeratePlugins` | `0x13840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `Plugin_IsEnabled` | `0x13860` | 68 | UnwindData |  |
| 9 | `Plugin_IsActionApplicable` | `0x138B0` | 96 | UnwindData |  |
| 11 | `Plugin_IsInteractiveOnly` | `0x13920` | 60 | UnwindData |  |
| 7 | `Plugin_DetectCondition` | `0x13970` | 68 | UnwindData |  |
| 12 | `Plugin_PerformAction` | `0x139C0` | 65 | UnwindData |  |
| 13 | `Plugin_Process` | `0x13A10` | 73 | UnwindData |  |
| 14 | `Plugin_Process_Aqua` | `0x13A70` | 185 | UnwindData |  |
| 5 | `GetPluginDefaultSettings` | `0x13B40` | 220,451 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `GetSettingsName` | `0x13B40` | 220,451 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
