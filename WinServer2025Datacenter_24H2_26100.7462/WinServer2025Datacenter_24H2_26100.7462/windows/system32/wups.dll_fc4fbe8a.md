# Binary Specification: wups.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wups.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fc4fbe8adaa42dc01dfc8f6e74e56bd4bcde2bb762ebf096be85702b21c7cb3f`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 13 | `DllMain` | `0x7B70` | 371 | UnwindData |  |
| 11 | `DllCanUnloadNow` | `0x7E40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `DllGetClassObject` | `0x7E60` | 187 | UnwindData |  |
| 14 | `DllRegisterServer` | `0x7F30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `DllUnregisterServer` | `0x7F50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | *Ordinal Only* | `0x7F70` | 138 | UnwindData |  |
