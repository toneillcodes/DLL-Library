# Binary Specification: SettingsHandlers_UserIntent.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\SettingsHandlers_UserIntent.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `05be5bcc2d885a1f8ad52d77f58875ff0bd3f91e2982ef73610eb01c327cac1f`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xD8B0` | 32 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0xD8E0` | 45 | UnwindData |  |
| 3 | `DllGetClassObject` | `0xD920` | 65 | UnwindData |  |
| 4 | `GetSetting` | `0xD990` | 56,876 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
