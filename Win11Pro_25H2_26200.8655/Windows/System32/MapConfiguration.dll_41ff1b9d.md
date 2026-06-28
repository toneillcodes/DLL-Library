# Binary Specification: MapConfiguration.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\MapConfiguration.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `41ff1b9da530d5c2b48078424e6fba518c0409d2009e1129500ad54280d5770b`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `ConfigurationManager_Create` | `0xBDD0` | 566 | UnwindData |  |
| 2 | `ConfigurationManager_GetLocaleMapConfiguration` | `0xC010` | 203 | UnwindData |  |
| 3 | `ConfigurationManager_SetCustomStorageFolder` | `0xC0F0` | 152 | UnwindData |  |
| 4 | `ConfigurationManager_SetServiceCallbacks` | `0xC4B0` | 224,540 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
