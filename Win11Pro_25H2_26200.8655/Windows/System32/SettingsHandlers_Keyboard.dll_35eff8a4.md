# Binary Specification: SettingsHandlers_Keyboard.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\SettingsHandlers_Keyboard.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `35eff8a4af9ddfd1a3f3b2dd33ed2038484d840c4a3da8ac2bc7d101c6a0a43e`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x10C70` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x10CA0` | 69 | UnwindData |  |
| 3 | `GetSetting` | `0x10D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `GetSettingForUser` | `0x10D70` | 382,028 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
