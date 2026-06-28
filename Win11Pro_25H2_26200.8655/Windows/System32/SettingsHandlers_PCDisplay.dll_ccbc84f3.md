# Binary Specification: SettingsHandlers_PCDisplay.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\SettingsHandlers_PCDisplay.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ccbc84f3838ef566f7482ae39a1ac8e636e852b63ce8e7964317ed001a551472`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `NotifyDisplayHandler` | `0xB1E0` | 50 | UnwindData |  |
| 2 | `DllCanUnloadNow` | `0x105E0` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x10610` | 69 | UnwindData |  |
| 4 | `GetSetting` | `0x106D0` | 590,492 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
