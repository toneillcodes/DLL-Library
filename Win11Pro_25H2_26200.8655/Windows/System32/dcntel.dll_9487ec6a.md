# Binary Specification: dcntel.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\dcntel.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9487ec6aef2e2c4bd00e32045788da9255a03869ea316d7e2a31cc3e062df241`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `GetCensusPropertyAlloc` | `0xA2FC0` | 628 | UnwindData |  |
| 2 | `GetCensusRegistryLocation` | `0xDD9D0` | 37 | UnwindData |  |
| 3 | `RunSystemContextCensus` | `0xDDA00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `RunUserContextCensus` | `0xDDA10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `SetCustomTrigger` | `0xDDA20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `SetCustomTriggerEx` | `0xDDA40` | 1,019 | UnwindData |  |
| 7 | `SysprepCleanupEnableCustomTrigger` | `0xDDE50` | 78 | UnwindData |  |
