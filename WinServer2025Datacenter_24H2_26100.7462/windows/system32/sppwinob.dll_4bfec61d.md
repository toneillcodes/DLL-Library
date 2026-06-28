# Binary Specification: sppwinob.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\sppwinob.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4bfec61df23b981a59d833f226ca2addcf79cbccc4e74de6097e00fbc680ebf2`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `SppPluginCanUnloadNow` | `0x9B60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `SppPluginCreateInstance` | `0x9B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `SppPluginInitialize` | `0x9B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `SppPluginShutdown` | `0x9BA0` | 24 | UnwindData |  |
| 5 | `SppPluginVersion` | `0x9B7D8` | 0 | Indeterminate |  |
