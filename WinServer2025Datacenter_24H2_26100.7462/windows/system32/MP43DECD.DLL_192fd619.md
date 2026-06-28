# Binary Specification: MP43DECD.DLL

## Binary Metadata
* **Original Path:** `c:\windows\system32\MP43DECD.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `192fd619962cd5a514005a4571eb0ba6721887abb025fefac3d4ef046b912bff`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `DllRegisterServer` | `0x88C0` | 526 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x8AE0` | 119 | UnwindData |  |
| 1 | `CreateInstance` | `0x9430` | 135 | UnwindData |  |
| 2 | `DllCanUnloadNow` | `0x9520` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0x9550` | 233 | UnwindData |  |
