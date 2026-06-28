# Binary Specification: AppManMigrationPlugin.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\migration\AppManMigrationPlugin.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d85fe6e5ec29d79727fac55aae1835c7109254d7d857457053b5f82425a23160`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x15700` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x15730` | 302 | UnwindData |  |
| 3 | `DllMain` | `0x15870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0x15890` | 301 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x159D0` | 162 | UnwindData |  |
