# Binary Specification: Windows.UI.AppDefaults.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Windows.UI.AppDefaults.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c15108e2d017012469e78b6f8bb061ea06bdd338e85429c4b68942e30cf5a75f`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xD3C0` | 42 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0xD3F0` | 45 | UnwindData |  |
| 3 | `DllGetClassObject` | `0xD430` | 65 | UnwindData |  |
| 4 | `GetSetting` | `0xD4A0` | 272,428 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
