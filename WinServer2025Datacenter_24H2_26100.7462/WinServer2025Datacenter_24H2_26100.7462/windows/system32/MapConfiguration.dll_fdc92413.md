# Binary Specification: MapConfiguration.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\MapConfiguration.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fdc924130e2871436ef3ed54209c359a119fa6342aa57b3ba636d98fac521dd6`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `ConfigurationManager_Create` | `0xBDD0` | 566 | UnwindData |  |
| 2 | `ConfigurationManager_GetLocaleMapConfiguration` | `0xC010` | 203 | UnwindData |  |
| 3 | `ConfigurationManager_SetCustomStorageFolder` | `0xC0F0` | 152 | UnwindData |  |
| 4 | `ConfigurationManager_SetServiceCallbacks` | `0xC4B0` | 224,508 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
