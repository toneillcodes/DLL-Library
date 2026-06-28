# Binary Specification: iemigplugin.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\iemigplugin.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `81c003d04d8e0ca398c1e62687072d7557f497e04e08d4d7e7ed4d26e789e514`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllInstall` | `0x92D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0x92D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0x92D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x9300` | 93 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x9370` | 3,610 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
