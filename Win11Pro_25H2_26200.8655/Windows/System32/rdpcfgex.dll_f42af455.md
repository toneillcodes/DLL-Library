# Binary Specification: rdpcfgex.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\rdpcfgex.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f42af4553f70f2888533c98f0b661d8362afdcb843010bb812608c23f6139866`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `ExGetCfgVersionInfo` | `0x1730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `ExtEncryptionLevels` | `0x1740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `ExtEnd` | `0x1760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `ExtStart` | `0x1760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `ExtGetCapabilities` | `0x1770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `ExtGetEncryptionLevelAndDescrEx` | `0x1780` | 285 | UnwindData |  |
| 6 | `ExtGetEncryptionLevelDescr` | `0x18B0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `ExtGetSecurityLayerDescrString` | `0x1900` | 154 | UnwindData |  |
| 8 | `ExtGetSecurityLayerName` | `0x19A0` | 154 | UnwindData |  |
| 9 | `ExtSecurityLayers` | `0x1A40` | 0 | Indeterminate |  |
