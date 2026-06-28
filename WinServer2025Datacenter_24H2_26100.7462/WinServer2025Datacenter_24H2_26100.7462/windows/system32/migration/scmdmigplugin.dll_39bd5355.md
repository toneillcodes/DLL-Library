# Binary Specification: scmdmigplugin.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\migration\scmdmigplugin.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `39bd5355173cdfdef218692c93e71b5bbceaf0dca135d09c136cb5f4eb72eb7c`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xA4E0` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0xA510` | 302 | UnwindData |  |
| 3 | `DllMain` | `0xA650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0xA670` | 293 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0xA7A0` | 152 | UnwindData |  |
