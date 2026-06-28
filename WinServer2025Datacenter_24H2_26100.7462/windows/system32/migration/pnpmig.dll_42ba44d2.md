# Binary Specification: pnpmig.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\migration\pnpmig.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `42ba44d2e71ea648c906f93ba714b93f7d405cd2e5203b1fa15b30cc0fc43ed8`
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
