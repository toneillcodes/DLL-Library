# Binary Specification: rdbui.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\rdbui.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `db9aa1719256e9699a766e1e8fc5112ab240d261b782dcfdc64da14fe8b94be1`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `RDBMgmtLaunchPropertiesW` | `0x7AA0` | 504 | UnwindData |  |
| 2 | `DllCanUnloadNow` | `0x7E60` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x7E90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0x7EB0` | 76 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x7F10` | 386,540 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
