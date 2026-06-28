# Binary Specification: sppwinob.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\sppwinob.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3b8ad58e625d8cc44bfe55439f8d1861090754ce2ae1e81d80b056bad8ddfaac`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `SppPluginCanUnloadNow` | `0x9B80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `SppPluginCreateInstance` | `0x9BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `SppPluginInitialize` | `0x9BB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `SppPluginShutdown` | `0x9BC0` | 24 | UnwindData |  |
| 5 | `SppPluginVersion` | `0x9C7D8` | 0 | Indeterminate |  |
