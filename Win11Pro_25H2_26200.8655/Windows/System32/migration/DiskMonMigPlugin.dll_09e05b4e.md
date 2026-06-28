# Binary Specification: DiskMonMigPlugin.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\migration\DiskMonMigPlugin.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `09e05b4e54092400db9462bf2469c16e7a4d1bec195a4e31c98e71d22e0277c1`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xF5A0` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0xF5D0` | 302 | UnwindData |  |
| 3 | `DllMain` | `0xF710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0xF730` | 301 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0xF870` | 162 | UnwindData |  |
