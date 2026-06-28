# Binary Specification: SettingsHandlers_Keyboard.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\SettingsHandlers_Keyboard.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f005713fc0fff09e8f49a84982e10b78d05a63efab19c0e239024b5c27950431`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x10C40` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x10C70` | 69 | UnwindData |  |
| 3 | `GetSetting` | `0x10D30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `GetSettingForUser` | `0x10D40` | 394,508 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
