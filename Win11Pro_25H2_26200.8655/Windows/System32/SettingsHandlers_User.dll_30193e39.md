# Binary Specification: SettingsHandlers_User.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\SettingsHandlers_User.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `30193e39cec0050ebeb24ef55616e3a167ffa52a01e087e8999773304721db6c`
* **Total Exported Functions:** 3

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xD190` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0xD1C0` | 69 | UnwindData |  |
| 3 | `GetSetting` | `0xD280` | 225,683 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
