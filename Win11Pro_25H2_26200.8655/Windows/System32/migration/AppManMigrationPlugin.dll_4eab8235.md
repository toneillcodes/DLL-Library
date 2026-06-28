# Binary Specification: AppManMigrationPlugin.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\migration\AppManMigrationPlugin.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4eab823539e7bf6176743b270d98c3c35e05d1c621a759a3af74ee3f6eb56e67`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x15710` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x15740` | 302 | UnwindData |  |
| 3 | `DllMain` | `0x15880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0x158A0` | 301 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x159E0` | 162 | UnwindData |  |
