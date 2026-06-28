# Binary Specification: VsmKeyMigPlugin.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\migration\VsmKeyMigPlugin.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `91dd04928ee8ab31a1004f7db17e4379576976aa1db265508d6ff71a1694b813`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x55E0` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x5610` | 302 | UnwindData |  |
| 3 | `DllMain` | `0x5750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0x5770` | 301 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x58B0` | 162 | UnwindData |  |
