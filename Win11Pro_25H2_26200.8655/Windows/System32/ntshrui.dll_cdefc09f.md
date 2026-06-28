# Binary Specification: ntshrui.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ntshrui.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `cdefc09f768813406f8daa6b5652a039b84d2472d06b437ed24f4468914be24f`
* **Total Exported Functions:** 16

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 13 | `IsPathSharedW` | `0x2D40` | 4 | UnwindData |  |
| 9 | `GetNetResourceFromLocalPathW` | `0x9010` | 912 | UnwindData |  |
| 6 | `GetLocalPathFromNetResourceW` | `0x145B0` | 83 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x18990` | 162 | UnwindData |  |
| 2 | `DllCanUnloadNow` | `0x1CC70` | 63,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `CanShareFolder` | `0x2C4C0` | 252 | UnwindData |  |
| 4 | `GetLocalPathFromNetResource` | `0x2C5D0` | 29 | UnwindData |  |
| 5 | `GetLocalPathFromNetResourceA` | `0x2C5D0` | 29 | UnwindData |  |
| 7 | `GetNetResourceFromLocalPath` | `0x2C5D0` | 29 | UnwindData |  |
| 8 | `GetNetResourceFromLocalPathA` | `0x2C5D0` | 29 | UnwindData |  |
| 11 | `IsPathShared` | `0x2C5D0` | 29 | UnwindData |  |
| 12 | `IsPathSharedA` | `0x2C5D0` | 29 | UnwindData |  |
| 14 | `RefreshShareCacheAsync` | `0x2C600` | 68 | UnwindData |  |
| 16 | `ShowShareFolderUI` | `0x2C650` | 249 | UnwindData |  |
| 10 | `IsFolderPrivateForUser` | `0x68910` | 645 | UnwindData |  |
| 15 | `SetFolderPermissionsForSharing` | `0x68BA0` | 1,856 | UnwindData |  |
