# Binary Specification: ntshrui.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ntshrui.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fe485d54c6482a47f295f1a0b0e19b614fd13346bf65a08fc0bd58d4c968d00f`
* **Total Exported Functions:** 15

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 13 | `IsPathSharedW` | `0x2D40` | 4 | UnwindData |  |
| 9 | `GetNetResourceFromLocalPathW` | `0xB030` | 912 | UnwindData |  |
| 6 | `GetLocalPathFromNetResourceW` | `0x17570` | 83 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x1AC60` | 162 | UnwindData |  |
| 2 | `DllCanUnloadNow` | `0x1DD30` | 54,448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `CanShareFolder` | `0x2B1E0` | 252 | UnwindData |  |
| 4 | `GetLocalPathFromNetResource` | `0x2B2F0` | 29 | UnwindData |  |
| 5 | `GetLocalPathFromNetResourceA` | `0x2B2F0` | 29 | UnwindData |  |
| 7 | `GetNetResourceFromLocalPath` | `0x2B2F0` | 29 | UnwindData |  |
| 8 | `GetNetResourceFromLocalPathA` | `0x2B2F0` | 29 | UnwindData |  |
| 11 | `IsPathShared` | `0x2B2F0` | 29 | UnwindData |  |
| 12 | `IsPathSharedA` | `0x2B2F0` | 29 | UnwindData |  |
| 15 | `ShowShareFolderUI` | `0x2B320` | 249 | UnwindData |  |
| 10 | `IsFolderPrivateForUser` | `0x67750` | 645 | UnwindData |  |
| 14 | `SetFolderPermissionsForSharing` | `0x679E0` | 1,856 | UnwindData |  |
