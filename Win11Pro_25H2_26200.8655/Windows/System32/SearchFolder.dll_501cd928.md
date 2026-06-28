# Binary Specification: SearchFolder.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\SearchFolder.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `501cd9284f559156801d75a996f8f66049834e050a8ce1351949e5c2aecf305a`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `DllMain` | `0x2DA0` | 95 | UnwindData |  |
| 5 | `DllCanUnloadNow` | `0x3B70` | 97 | UnwindData |  |
| 10 | `GetAggregateQueryError` | `0xFF30` | 345 | UnwindData |  |
| 1 | `CDBFolderViewCB_CreateInstance` | `0x12C30` | 27,936 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `DllRegisterServer` | `0x19950` | 35,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `DllUnregisterServer` | `0x19950` | 35,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `CDBFolderUI_CreateInstance` | `0x22440` | 154 | UnwindData |  |
| 6 | `DllGetClassObject` | `0x25990` | 88 | UnwindData |  |
| 2 | `AppendHiddenSearchContext` | `0x27870` | 403 | UnwindData |  |
| 4 | `CSearchDelegateFolderUI_CreateInstance` | `0x27F50` | 154 | UnwindData |  |
| 11 | `s_GetStartMenuFilesScope` | `0x3E070` | 642 | UnwindData |  |
