# Binary Specification: onramp.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Microsoft-Edge-WebView\onramp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `dbcbf47dd4cf9aa12143ccbd53b908edbb300e8a4d62fdd09a34aac8dd1e4625`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `?GetEdgeAppId@@YA?AU_GUID@@XZ` | `0x1000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `GetEdgeAppId` | `0x1000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `ConstructPasswordImporter` | `0x1020` | 56 | UnwindData |  |
| 5 | `DestructPasswordImporter` | `0x1060` | 2,544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `?UnobfuscateDataSafe@@YAJV?$span@E$0?0@__Cr@std@@0@Z` | `0x1A50` | 453 | UnwindData |  |
| 12 | `UnobfuscateDataSafe` | `0x1A50` | 453 | UnwindData |  |
| 1 | `?FetchSearchEngineDataSafe@@YAJV?$span@E$0?0@__Cr@std@@PEAKPEAIPEAUtagBLOB@@@Z` | `0x1C20` | 161 | UnwindData |  |
| 6 | `FetchSearchEngineDataSafe` | `0x1C20` | 161 | UnwindData |  |
| 9 | `GetSearchEngineRawData` | `0x1CD0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `GetSearchEngineDataType` | `0x1DB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `IsSearchEngineImportAllowed` | `0x1DE0` | 67 | UnwindData |  |
| 10 | `IsBingDefaultSearchEngine` | `0x1E30` | 65 | UnwindData |  |
