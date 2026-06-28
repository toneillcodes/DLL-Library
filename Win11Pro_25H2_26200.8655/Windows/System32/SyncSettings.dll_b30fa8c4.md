# Binary Specification: SyncSettings.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\SyncSettings.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b30fa8c45c29bdd5112bb9c3566069f5d601bf26e5ba4a9573774ae71cf7cb46`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `GetProxyDllInfo` | `0xB7B0` | 2,752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0xC270` | 72 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0xC2C0` | 45 | UnwindData |  |
| 3 | `DllGetClassObject` | `0xC300` | 111 | UnwindData |  |
| 5 | `GetSetting` | `0xC3A0` | 196,124 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
