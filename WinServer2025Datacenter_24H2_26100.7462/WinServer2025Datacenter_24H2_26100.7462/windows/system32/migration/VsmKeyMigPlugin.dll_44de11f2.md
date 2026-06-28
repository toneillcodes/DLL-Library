# Binary Specification: VsmKeyMigPlugin.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\migration\VsmKeyMigPlugin.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `44de11f2ef73e194ef55e75c0c3602272062052a9cc5a98780dfe83259e6d5ea`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x55E0` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x5610` | 302 | UnwindData |  |
| 3 | `DllMain` | `0x5750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0x5770` | 301 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x58B0` | 162 | UnwindData |  |
