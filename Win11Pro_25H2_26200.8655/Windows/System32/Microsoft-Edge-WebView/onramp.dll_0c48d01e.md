# Binary Specification: onramp.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Microsoft-Edge-WebView\onramp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0c48d01efba9645c6a6ada3167fc433ab6ddd77c5529ad20ce16b080f59d0a64`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `?GetEdgeAppId@@YA?AU_GUID@@XZ` | `0x1000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `GetEdgeAppId` | `0x1000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `ConstructPasswordImporter` | `0x1020` | 56 | UnwindData |  |
| 5 | `DestructPasswordImporter` | `0x1060` | 2,656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `?UnobfuscateDataSafe@@YAJV?$span@E$0?0@__Cr@std@@0@Z` | `0x1AC0` | 443 | UnwindData |  |
| 12 | `UnobfuscateDataSafe` | `0x1AC0` | 443 | UnwindData |  |
| 1 | `?FetchSearchEngineDataSafe@@YAJV?$span@E$0?0@__Cr@std@@PEAKPEAIPEAUtagBLOB@@@Z` | `0x1C80` | 152 | UnwindData |  |
| 6 | `FetchSearchEngineDataSafe` | `0x1C80` | 152 | UnwindData |  |
| 9 | `GetSearchEngineRawData` | `0x1D20` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `GetSearchEngineDataType` | `0x1DF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `IsSearchEngineImportAllowed` | `0x1E20` | 67 | UnwindData |  |
| 10 | `IsBingDefaultSearchEngine` | `0x1E70` | 65 | UnwindData |  |
