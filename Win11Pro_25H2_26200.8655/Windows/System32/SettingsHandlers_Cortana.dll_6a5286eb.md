# Binary Specification: SettingsHandlers_Cortana.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\SettingsHandlers_Cortana.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6a5286ebff63885e33c86bae719c3d014a71cd9187bcb24e7875bc5ad5172625`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xB900` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0xB930` | 69 | UnwindData |  |
| 3 | `GetSetting` | `0xB9B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `GetSettingForUser` | `0xB9C0` | 283,612 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
