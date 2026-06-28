# Binary Specification: pnpmig.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\migration\pnpmig.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4d894642c70373491109847fb6890006c8376e573c27b86a8a967f8d0dcd2ef7`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllCanUnloadNow` | `0x9610` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x9640` | 302 | UnwindData |  |
| 4 | `DllMain` | `0x9780` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllRegisterServer` | `0x97A0` | 301 | UnwindData |  |
| 6 | `DllUnregisterServer` | `0x98E0` | 162 | UnwindData |  |
| 1 | `PnpMigRunDllW` | `0xA960` | 178 | UnwindData |  |
