# Binary Specification: linkinfo.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\linkinfo.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f967389394d1f3bf15c1e125d81f8f45cbafc499b6b9385d74b8021b395dc6ee`
* **Total Exported Functions:** 15

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 12 | `IsValidLinkInfo` | `0x1010` | 970 | UnwindData |  |
| 15 | `ResolveLinkInfoW` | `0x1690` | 291 | UnwindData |  |
| 10 | `GetCanonicalPathInfoW` | `0x2010` | 70 | UnwindData |  |
| 5 | `CreateLinkInfoW` | `0x38B0` | 48 | UnwindData |  |
| 6 | `DestroyLinkInfo` | `0x38F0` | 3,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `GetCanonicalPathInfo` | `0x4570` | 267 | UnwindData |  |
| 9 | `GetCanonicalPathInfoA` | `0x4570` | 267 | UnwindData |  |
| 1 | `CompareLinkInfoReferents` | `0x5370` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CompareLinkInfoVolumes` | `0x53E0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `CreateLinkInfo` | `0x5470` | 92 | UnwindData |  |
| 4 | `CreateLinkInfoA` | `0x5470` | 92 | UnwindData |  |
| 7 | `DisconnectLinkInfo` | `0x54E0` | 17 | UnwindData |  |
| 11 | `GetLinkInfoData` | `0x5500` | 99 | UnwindData |  |
| 13 | `ResolveLinkInfo` | `0x5570` | 156 | UnwindData |  |
| 14 | `ResolveLinkInfoA` | `0x5570` | 156 | UnwindData |  |
