# Binary Specification: dcntel.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\dcntel.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1ce92486f04cfd78c28bd77e9e272fccec8e3b4b659f0829f09ae04bd0551772`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `GetCensusPropertyAlloc` | `0x230D0` | 621 | UnwindData |  |
| 2 | `GetCensusRegistryLocation` | `0x95E10` | 37 | UnwindData |  |
| 3 | `RunSystemContextCensus` | `0x95E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `RunUserContextCensus` | `0x95E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `SetCustomTrigger` | `0x95E60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `SetCustomTriggerEx` | `0x95E80` | 1,019 | UnwindData |  |
| 7 | `SysprepCleanupEnableCustomTrigger` | `0x96290` | 78 | UnwindData |  |
