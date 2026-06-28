# Binary Specification: WMVENCOD.DLL

## Binary Metadata
* **Original Path:** `C:\Windows\System32\WMVENCOD.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `642427cea40aa1e9762fad10bfb78d4353cab333d1fdd1f4a8456f180874c046`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `DllRegisterServer` | `0x17330` | 525 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x17550` | 119 | UnwindData |  |
| 1 | `CreateInstance` | `0x17CE0` | 121 | UnwindData |  |
| 2 | `DllCanUnloadNow` | `0x17DC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0x17DF0` | 231 | UnwindData |  |
