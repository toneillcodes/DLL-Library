# Binary Specification: SettingsHandlers_Accessibility.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\SettingsHandlers_Accessibility.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d03ddadb62d5ca9bbe2f7447837f93ce077ca0589cf14e1b364fe914fa68bb4f`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `GetProxyDllInfo` | `0xC100` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllGetActivationFactory` | `0xC2F0` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0xC480` | 115 | UnwindData |  |
| 3 | `DllGetClassObject` | `0xC500` | 53 | UnwindData |  |
| 5 | `GetSetting` | `0xC570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `GetSettingForUser` | `0xC580` | 247,980 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
