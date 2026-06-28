# Binary Specification: SettingsHandlers_UserIntent.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\SettingsHandlers_UserIntent.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `51ac6960efa771565bf9512d1bac0c44929762968c8f533d407efd709c719aeb`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xDAE0` | 32 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0xDB10` | 45 | UnwindData |  |
| 3 | `DllGetClassObject` | `0xDB50` | 65 | UnwindData |  |
| 4 | `GetSetting` | `0xDBC0` | 63,580 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
