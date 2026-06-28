# Binary Specification: occache.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\occache.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0991d46b17c1bbde8a69ceeba8205c171487289a450b44e67eba102c67203dd2`
* **Total Exported Functions:** 17

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `FindFirstControlArch` | `0x1050` | 157 | UnwindData |  |
| 16 | `DllCanUnloadNow` | `0x1B60` | 1,856 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `FindFirstControl` | `0x22A0` | 160 | UnwindData |  |
| 1 | `FindControlClose` | `0x2900` | 44 | UnwindData |  |
| 17 | `DllGetClassObject` | `0x5630` | 1,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `RemoveExpiredControls` | `0x5B70` | 11,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `RemoveControlByHandle2` | `0x89A0` | 253 | UnwindData |  |
| 12 | `RemoveControlByName2` | `0x8AB0` | 350 | UnwindData |  |
| 4 | `FindNextControl` | `0xC630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `FindNextControlArch` | `0xC640` | 368 | UnwindData |  |
| 6 | `GetControlDependentFile` | `0xC7C0` | 262 | UnwindData |  |
| 7 | `GetControlInfo` | `0xC8D0` | 468 | UnwindData |  |
| 8 | `IsModuleRemovable` | `0xD570` | 41 | UnwindData |  |
| 9 | `ReleaseControlHandle` | `0xD9A0` | 37 | UnwindData |  |
| 11 | `RemoveControlByHandle` | `0xD9D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `RemoveControlByName` | `0xD9E0` | 36 | UnwindData |  |
| 15 | `SweepControlsByLastAccessDate` | `0xE130` | 610 | UnwindData |  |
