# Binary Specification: wups.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wups.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2acfb499c7ea028888005e71be03d9b927fe904ad3157f9b6459d7bbac53adbd`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 13 | `DllMain` | `0x7D00` | 345 | UnwindData |  |
| 11 | `DllCanUnloadNow` | `0x7FB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `DllGetClassObject` | `0x7FD0` | 187 | UnwindData |  |
| 14 | `DllRegisterServer` | `0x80A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `DllUnregisterServer` | `0x80C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | *Ordinal Only* | `0x80E0` | 138 | UnwindData |  |
