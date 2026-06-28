# Binary Specification: occache.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\occache.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7b548c55a45bed8fb5b7669907a7e31f6112f0ce358386e980f90e7d127f8c32`
* **Total Exported Functions:** 17

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `FindFirstControlArch` | `0x1240` | 157 | UnwindData |  |
| 16 | `DllCanUnloadNow` | `0x1D50` | 1,856 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `FindFirstControl` | `0x2490` | 160 | UnwindData |  |
| 1 | `FindControlClose` | `0x2AF0` | 44 | UnwindData |  |
| 17 | `DllGetClassObject` | `0x58E0` | 1,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `RemoveExpiredControls` | `0x5E20` | 11,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `RemoveControlByHandle2` | `0x8C50` | 253 | UnwindData |  |
| 12 | `RemoveControlByName2` | `0x8D60` | 350 | UnwindData |  |
| 4 | `FindNextControl` | `0x14790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `FindNextControlArch` | `0x147A0` | 368 | UnwindData |  |
| 6 | `GetControlDependentFile` | `0x14920` | 262 | UnwindData |  |
| 7 | `GetControlInfo` | `0x14A30` | 468 | UnwindData |  |
| 8 | `IsModuleRemovable` | `0x156D0` | 41 | UnwindData |  |
| 9 | `ReleaseControlHandle` | `0x15B00` | 37 | UnwindData |  |
| 11 | `RemoveControlByHandle` | `0x15B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `RemoveControlByName` | `0x15B40` | 36 | UnwindData |  |
| 15 | `SweepControlsByLastAccessDate` | `0x16290` | 610 | UnwindData |  |
