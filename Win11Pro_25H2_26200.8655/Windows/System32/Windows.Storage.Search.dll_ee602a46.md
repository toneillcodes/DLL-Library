# Binary Specification: Windows.Storage.Search.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Windows.Storage.Search.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ee602a467a58edc9a9e6c39e1712234a97fe3a44c9e27e511d33ebbcfe0c12aa`
* **Total Exported Functions:** 29

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2003 | `CreateDefaultProviderResolver` | `0x5060` | 179 | UnwindData |  |
| 2021 | `SHCreateScopeFromIDListsEx` | `0x5DC0` | 286 | UnwindData |  |
| 2023 | `SHCreateScopeItemFromIDList` | `0x7C60` | 149 | UnwindData |  |
| 2025 | `SHCreateScopeItemFromShellItem` | `0x9600` | 424 | UnwindData |  |
| 2020 | `SHCreateScope` | `0xAF20` | 435 | UnwindData |  |
| 2004 | `CreateResultSetFactory` | `0x19020` | 148 | UnwindData |  |
| 2026 | `SHCreateSearchIDListFromAutoList` | `0x1A040` | 961 | UnwindData |  |
| 2018 | `SHCreateAutoList` | `0x2DAC0` | 197 | UnwindData |  |
| 2008 | `DllGetClassObject` | `0x36C20` | 204 | UnwindData |  |
| 2005 | `CreateSingleVisibleInList` | `0x3CC00` | 107 | UnwindData |  |
| 2009 | `DllMain` | `0x4A5E0` | 77 | UnwindData |  |
| 2015 | `IsShellItemInSearchIndex` | `0x54AD0` | 326 | UnwindData |  |
| 2014 | `IsMSSearchEnabled` | `0x54C20` | 332 | UnwindData |  |
| 2010 | `DllRegisterServer` | `0x5BA40` | 20,352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2011 | `DllUnregisterServer` | `0x5BA40` | 20,352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2024 | `SHCreateScopeItemFromKnownFolder` | `0x609C0` | 244 | UnwindData |  |
| 2028 | `SHSaveBinaryAutoListToStream` | `0x62420` | 168 | UnwindData |  |
| 2006 | `DllCanUnloadNow` | `0x65E00` | 78 | UnwindData |  |
| 2019 | `SHCreateAutoListWithID` | `0x776C0` | 245 | UnwindData |  |
| 2000 | *Ordinal Only* | `0x8FC20` | 35 | UnwindData |  |
| 2002 | *Ordinal Only* | `0x958B0` | 35 | UnwindData |  |
| 2012 | `GetGatherAdmin` | `0xA2FA0` | 579 | UnwindData |  |
| 2016 | `SEARCH_RemoteLocationsCscStateCache_IsRemoteLocationInCsc` | `0xA33E0` | 112 | UnwindData |  |
| 2017 | `SEARCH_WriteAutoListContents` | `0xA3460` | 109,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2001 | *Ordinal Only* | `0xBDE50` | 25 | UnwindData |  |
| 2022 | `SHCreateScopeFromShellItemArray` | `0xC0700` | 15,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2013 | `GetScopeFolderType` | `0xC4450` | 496 | UnwindData |  |
| 2027 | `SHCreateTransientVFolderIDList` | `0xC4880` | 487 | UnwindData |  |
| 2007 | `DllGetActivationFactory` | `0xC60A0` | 223 | UnwindData |  |
