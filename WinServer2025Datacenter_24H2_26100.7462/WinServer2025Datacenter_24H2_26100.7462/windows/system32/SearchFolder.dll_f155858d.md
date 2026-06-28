# Binary Specification: SearchFolder.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\SearchFolder.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f155858deb3fd24b0e7006b695289820c5917be32524017da3dba10386a656e4`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `DllMain` | `0x2D80` | 95 | UnwindData |  |
| 5 | `DllCanUnloadNow` | `0x3B50` | 97 | UnwindData |  |
| 10 | `GetAggregateQueryError` | `0xFA20` | 345 | UnwindData |  |
| 1 | `CDBFolderViewCB_CreateInstance` | `0x11E80` | 27,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `DllRegisterServer` | `0x188B0` | 34,976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `DllUnregisterServer` | `0x188B0` | 34,976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `CDBFolderUI_CreateInstance` | `0x21150` | 154 | UnwindData |  |
| 6 | `DllGetClassObject` | `0x243A0` | 88 | UnwindData |  |
| 2 | `AppendHiddenSearchContext` | `0x26280` | 403 | UnwindData |  |
| 4 | `CSearchDelegateFolderUI_CreateInstance` | `0x269A0` | 154 | UnwindData |  |
| 11 | `s_GetStartMenuFilesScope` | `0x3CA90` | 642 | UnwindData |  |
