# Binary Specification: EscMigPlugin.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\EscMigPlugin.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `35497d89b041711f1bb1bb0b4865dc2eb905b3dccfc3077e0ab679bb418aacc0`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x57E0` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x5810` | 302 | UnwindData |  |
| 3 | `DllMain` | `0x5950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0x5970` | 293 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x5AA0` | 151 | UnwindData |  |
