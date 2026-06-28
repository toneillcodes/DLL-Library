# Binary Specification: DiskMonMigPlugin.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\migration\DiskMonMigPlugin.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6198eba622cfcc041f31d5ecf4bf4f9aa2e7da26f63b84b2a47f01e35f629f48`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xF2A0` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0xF2D0` | 302 | UnwindData |  |
| 3 | `DllMain` | `0xF410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0xF430` | 301 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0xF570` | 162 | UnwindData |  |
