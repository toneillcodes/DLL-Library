# Binary Specification: coreglobconfig.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\coreglobconfig.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e7d7da2944ebb55a8b0c7cff8131cacadb007ddaccb8120af513a07669f29f0e`
* **Total Exported Functions:** 13

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `SyncLanguageDataToCloudSynchronous` | `0x1B8D0` | 252 | UnwindData |  |
| 2 | `CreateUserSpecificGlobalizationSettings` | `0x1F810` | 2,470 | UnwindData |  |
| 5 | `GetDisplayLanguageLocalizedName` | `0x201C0` | 138 | UnwindData |  |
| 6 | `GetDisplayLanguageNativeName` | `0x20250` | 135 | UnwindData |  |
| 7 | `GetSupportedDisplayLanguages` | `0x202E0` | 687 | UnwindData |  |
| 8 | `SetDisplayLanguageCore` | `0x205A0` | 256 | UnwindData |  |
| 9 | `SetUserDisplayLanguageCore` | `0x206B0` | 245 | UnwindData |  |
| 10 | `SyncLanguageDataFromCloud` | `0x207B0` | 761 | UnwindData |  |
| 11 | `SyncLanguageDataToCloud` | `0x20AB0` | 180 | UnwindData |  |
| 12 | `SyncLanguageDataToCloudDirect` | `0x20B70` | 204 | UnwindData |  |
| 13 | `UpdateDefaultGlobalizationSettings` | `0x20C50` | 1,259 | UnwindData |  |
| 3 | `DllCanUnloadNow` | `0x22270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllGetClassObject` | `0x22290` | 8,604 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
