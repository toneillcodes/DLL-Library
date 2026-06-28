# Binary Specification: coreglobconfig.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\coreglobconfig.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `cc75b2b8292650f9b84a80c948210cb49719b0a004bccdb8425515961b94975c`
* **Total Exported Functions:** 13

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `SyncLanguageDataToCloudSynchronous` | `0x1B9B0` | 252 | UnwindData |  |
| 2 | `CreateUserSpecificGlobalizationSettings` | `0x1F900` | 2,470 | UnwindData |  |
| 5 | `GetDisplayLanguageLocalizedName` | `0x202B0` | 138 | UnwindData |  |
| 6 | `GetDisplayLanguageNativeName` | `0x20340` | 135 | UnwindData |  |
| 7 | `GetSupportedDisplayLanguages` | `0x203D0` | 687 | UnwindData |  |
| 8 | `SetDisplayLanguageCore` | `0x20690` | 256 | UnwindData |  |
| 9 | `SetUserDisplayLanguageCore` | `0x207A0` | 245 | UnwindData |  |
| 10 | `SyncLanguageDataFromCloud` | `0x208A0` | 761 | UnwindData |  |
| 11 | `SyncLanguageDataToCloud` | `0x20BA0` | 180 | UnwindData |  |
| 12 | `SyncLanguageDataToCloudDirect` | `0x20C60` | 204 | UnwindData |  |
| 13 | `UpdateDefaultGlobalizationSettings` | `0x20D40` | 1,259 | UnwindData |  |
| 3 | `DllCanUnloadNow` | `0x22360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllGetClassObject` | `0x22380` | 8,588 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
