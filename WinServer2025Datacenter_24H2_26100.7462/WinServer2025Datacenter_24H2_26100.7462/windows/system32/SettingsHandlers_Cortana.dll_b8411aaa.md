# Binary Specification: SettingsHandlers_Cortana.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\SettingsHandlers_Cortana.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b8411aaa3b8cb8afbe86b171c1670e277bcb5836a8f0a218da45089a4b8cdee5`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xB050` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0xB080` | 69 | UnwindData |  |
| 3 | `GetSetting` | `0xB100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `GetSettingForUser` | `0xB110` | 199,196 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
