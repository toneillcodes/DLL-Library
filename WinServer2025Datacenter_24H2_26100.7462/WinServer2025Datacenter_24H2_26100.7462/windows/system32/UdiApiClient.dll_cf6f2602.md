# Binary Specification: UdiApiClient.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\UdiApiClient.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `cf6f2602bc3a674824b10751e7c2b0ea85608965d5beea98b97ab0a326fcb3b0`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `CreateDownloaderSession` | `0x4DC40` | 1,542 | UnwindData |  |
| 1 | `CleanDownloaderSession` | `0x4E410` | 1,496 | UnwindData |  |
| 11 | `IsHotpatchRecipeValid` | `0x4EBB0` | 1,520 | UnwindData |  |
| 7 | `DllMain` | `0x61C50` | 1,284 | UnwindData |  |
| 5 | `DllCanUnloadNow` | `0x62270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllGetActivationFactory` | `0x62280` | 831 | UnwindData |  |
| 4 | `CreateUpdate` | `0x6DB00` | 1,542 | UnwindData |  |
| 10 | `InPlaceCreateUpdate` | `0x6E2D0` | 1,531 | UnwindData |  |
| 12 | `LoadUpdate` | `0x6EA90` | 1,531 | UnwindData |  |
| 2 | `CleanUpdate` | `0x6F250` | 1,496 | UnwindData |  |
| 9 | `GetDeviceInfo` | `0x6F9F0` | 1,986 | UnwindData |  |
| 8 | `ETW_TRACE_LOGGING_METADATA` | `0x9BCD28` | 0 | Indeterminate |  |
