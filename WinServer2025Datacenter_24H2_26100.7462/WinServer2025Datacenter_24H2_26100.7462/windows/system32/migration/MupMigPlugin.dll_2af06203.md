# Binary Specification: MupMigPlugin.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\migration\MupMigPlugin.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2af062036c87e6e0748e7fefa9dc8d70a4a5246be5a78c975821b61a530ca438`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x6530` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x6560` | 302 | UnwindData |  |
| 3 | `DllMain` | `0x66A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0x66C0` | 301 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x6800` | 162 | UnwindData |  |
