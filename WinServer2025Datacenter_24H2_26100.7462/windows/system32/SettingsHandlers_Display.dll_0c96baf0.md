# Binary Specification: SettingsHandlers_Display.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\SettingsHandlers_Display.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0c96baf0bc98c2d0cdf0fbdc6f740c796f765b216bd701490fa754ca76376350`
* **Total Exported Functions:** 3

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xC350` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0xC380` | 69 | UnwindData |  |
| 3 | `GetSetting` | `0xC430` | 253,660 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
