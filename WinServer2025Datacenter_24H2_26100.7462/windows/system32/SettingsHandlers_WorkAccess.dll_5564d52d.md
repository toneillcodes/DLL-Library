# Binary Specification: SettingsHandlers_WorkAccess.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\SettingsHandlers_WorkAccess.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5564d52d5d4d3467c0801bf426039e02f08340634fbd97c4789800bc13fc2698`
* **Total Exported Functions:** 3

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xC620` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0xC650` | 69 | UnwindData |  |
| 3 | `GetSetting` | `0xC710` | 290,752 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
