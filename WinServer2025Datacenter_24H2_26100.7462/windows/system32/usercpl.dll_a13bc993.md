# Binary Specification: usercpl.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\usercpl.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a13bc993daef48301fd1ebef417967cd16a4d3a5fd2020dd0e854059a7679abd`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xE7E0` | 88 | UnwindData |  |
| 2 | `DllGetClassObject` | `0xE840` | 353 | UnwindData |  |
| 3 | `DllRegisterServer` | `0xEA70` | 457,506 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0xEA70` | 457,506 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
