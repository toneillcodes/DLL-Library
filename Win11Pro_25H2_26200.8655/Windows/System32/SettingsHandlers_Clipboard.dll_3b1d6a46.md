# Binary Specification: SettingsHandlers_Clipboard.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\SettingsHandlers_Clipboard.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3b1d6a464f874aa941a0892c6613417556f974d3544b1edf77b8c119be22d3d4`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xAE40` | 32 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0xAE70` | 45 | UnwindData |  |
| 3 | `DllGetClassObject` | `0xAEB0` | 65 | UnwindData |  |
| 4 | `GetSetting` | `0xAF20` | 115,292 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
