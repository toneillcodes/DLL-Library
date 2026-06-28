# Binary Specification: Windows.Storage.Search.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Windows.Storage.Search.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f272b69963d77393f9e4061caab896d3583683aadcc00cf849ea21454bdcb945`
* **Total Exported Functions:** 28

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2022 | `SHCreateScopeItemFromIDList` | `0xAC40` | 149 | UnwindData |  |
| 2024 | `SHCreateScopeItemFromShellItem` | `0xC5E0` | 424 | UnwindData |  |
| 2019 | `SHCreateScope` | `0xDF00` | 435 | UnwindData |  |
| 2017 | `SHCreateAutoList` | `0x1A2C0` | 227 | UnwindData |  |
| 2025 | `SHCreateSearchIDListFromAutoList` | `0x262D0` | 961 | UnwindData |  |
| 2007 | `DllGetClassObject` | `0x349C0` | 204 | UnwindData |  |
| 2004 | `CreateSingleVisibleInList` | `0x3A940` | 107 | UnwindData |  |
| 2003 | `CreateResultSetFactory` | `0x41AF0` | 148 | UnwindData |  |
| 2002 | `CreateDefaultProviderResolver` | `0x437E0` | 179 | UnwindData |  |
| 2008 | `DllMain` | `0x49B90` | 77 | UnwindData |  |
| 2014 | `IsShellItemInSearchIndex` | `0x54C90` | 326 | UnwindData |  |
| 2013 | `IsMSSearchEnabled` | `0x54DE0` | 332 | UnwindData |  |
| 2009 | `DllRegisterServer` | `0x5BE10` | 9,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2010 | `DllUnregisterServer` | `0x5BE10` | 9,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2020 | `SHCreateScopeFromIDListsEx` | `0x5E1B0` | 286 | UnwindData |  |
| 2023 | `SHCreateScopeItemFromKnownFolder` | `0x60B10` | 244 | UnwindData |  |
| 2027 | `SHSaveBinaryAutoListToStream` | `0x621A0` | 168 | UnwindData |  |
| 2005 | `DllCanUnloadNow` | `0x657B0` | 78 | UnwindData |  |
| 2018 | `SHCreateAutoListWithID` | `0x76AF0` | 245 | UnwindData |  |
| 2000 | *Ordinal Only* | `0x90F80` | 35 | UnwindData |  |
| 2011 | `GetGatherAdmin` | `0x9BA00` | 579 | UnwindData |  |
| 2015 | `SEARCH_RemoteLocationsCscStateCache_IsRemoteLocationInCsc` | `0x9BE40` | 112 | UnwindData |  |
| 2016 | `SEARCH_WriteAutoListContents` | `0x9BEC0` | 108,240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2001 | *Ordinal Only* | `0xB6590` | 25 | UnwindData |  |
| 2021 | `SHCreateScopeFromShellItemArray` | `0xB8E40` | 15,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2012 | `GetScopeFolderType` | `0xBCB90` | 496 | UnwindData |  |
| 2026 | `SHCreateTransientVFolderIDList` | `0xBCFC0` | 487 | UnwindData |  |
| 2006 | `DllGetActivationFactory` | `0xBE7D0` | 223 | UnwindData |  |
