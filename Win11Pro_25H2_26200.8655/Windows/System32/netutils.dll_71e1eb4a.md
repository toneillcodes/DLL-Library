# Binary Specification: netutils.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\netutils.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `71e1eb4a3027cf348d71bfdfebf0ede76d05d521293250d627417f7c2d9478d8`
* **Total Exported Functions:** 22

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 20 | `NetpwPathCanonicalize` | `0x1010` | 106 | UnwindData |  |
| 22 | `NetpwPathType` | `0x17D0` | 336 | UnwindData |  |
| 10 | `NetpIsRemote` | `0x2530` | 148 | UnwindData |  |
| 7 | `NetpIsComputerNameValid` | `0x2730` | 63 | UnwindData |  |
| 8 | `NetpIsDomainNameValid` | `0x27C0` | 51 | UnwindData |  |
| 14 | `NetpIsUserNameValid` | `0x2840` | 63 | UnwindData |  |
| 18 | `NetpwNameCompare` | `0x28D0` | 1,004 | UnwindData |  |
| 17 | `NetpwNameCanonicalize` | `0x2CD0` | 640 | UnwindData |  |
| 19 | `NetpwNameValidate` | `0x2F60` | 616 | UnwindData |  |
| 2 | `NetApiBufferFree` | `0x31D0` | 47 | UnwindData |  |
| 1 | `NetApiBufferAllocate` | `0x32F0` | 65 | UnwindData |  |
| 5 | `NetRemoteComputerSupports` | `0x3340` | 44 | UnwindData |  |
| 11 | `NetpIsRemoteNameValid` | `0x36F0` | 181 | UnwindData |  |
| 13 | `NetpIsUncComputerNameValid` | `0x37B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `NetApiBufferSize` | `0x37F0` | 64 | UnwindData |  |
| 16 | `NetpwListTraverse` | `0x3840` | 75 | UnwindData |  |
| 6 | `NetapipBufferAllocate` | `0x38C0` | 4,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `NetApiBufferReallocate` | `0x4A60` | 144 | UnwindData |  |
| 15 | `NetpwListCanonicalize` | `0x4BB0` | 1,370 | UnwindData |  |
| 9 | `NetpIsGroupNameValid` | `0x5110` | 100 | UnwindData |  |
| 12 | `NetpIsShareNameValid` | `0x5180` | 100 | UnwindData |  |
| 21 | `NetpwPathCompare` | `0x51F0` | 364 | UnwindData |  |
