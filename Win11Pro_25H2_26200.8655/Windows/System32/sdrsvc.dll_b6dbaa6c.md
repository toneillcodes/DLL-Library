# Binary Specification: sdrsvc.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\sdrsvc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b6dbaa6c40043a334e271ac71cbfc0eedf8249d37b64263b90d35547e6cf4b5f`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xE420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0xE440` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0xE5D0` | 131 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0xE660` | 102 | UnwindData |  |
| 5 | `ServiceMain` | `0xE7D0` | 78,060 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
