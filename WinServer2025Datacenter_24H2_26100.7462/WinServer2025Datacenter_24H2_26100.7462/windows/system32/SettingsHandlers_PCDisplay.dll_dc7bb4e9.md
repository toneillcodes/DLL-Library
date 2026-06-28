# Binary Specification: SettingsHandlers_PCDisplay.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\SettingsHandlers_PCDisplay.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `dc7bb4e9c97d535b94b5168e4d5c4db83c6d0ffbba2b0a132536eb7203b61b83`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `NotifyDisplayHandler` | `0xB330` | 50 | UnwindData |  |
| 2 | `DllCanUnloadNow` | `0x10800` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x10830` | 69 | UnwindData |  |
| 4 | `GetSetting` | `0x108F0` | 533,356 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
