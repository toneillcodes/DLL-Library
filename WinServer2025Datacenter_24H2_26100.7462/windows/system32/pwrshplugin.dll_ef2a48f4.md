# Binary Specification: pwrshplugin.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\pwrshplugin.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ef2a48f4b836316b0b9862517e9a0f6699c56f4e5521b4c8fd9aa40c41009d39`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `GetCLRVersionForPSVersion` | `0x2C70` | 465 | UnwindData |  |
| 2 | `PerformWSManPluginReportCompletion` | `0x3730` | 3,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `WSManPluginCommand` | `0x4350` | 100 | UnwindData |  |
| 4 | `WSManPluginConnect` | `0x43C0` | 100 | UnwindData |  |
| 5 | `WSManPluginReceive` | `0x4430` | 100 | UnwindData |  |
| 6 | `WSManPluginReleaseCommandContext` | `0x44A0` | 71 | UnwindData |  |
| 7 | `WSManPluginReleaseShellContext` | `0x44F0` | 50 | UnwindData |  |
| 8 | `WSManPluginSend` | `0x4530` | 116 | UnwindData |  |
| 9 | `WSManPluginShell` | `0x45B0` | 233 | UnwindData |  |
| 10 | `WSManPluginShutdown` | `0x46A0` | 214 | UnwindData |  |
| 11 | `WSManPluginSignal` | `0x4780` | 100 | UnwindData |  |
| 12 | `WSManPluginStartup` | `0x47F0` | 184 | UnwindData |  |
