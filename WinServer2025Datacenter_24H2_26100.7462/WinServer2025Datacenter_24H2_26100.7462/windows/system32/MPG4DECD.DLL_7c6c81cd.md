# Binary Specification: MPG4DECD.DLL

## Binary Metadata
* **Original Path:** `c:\windows\system32\MPG4DECD.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7c6c81cd12ba9d9044535df8665ff390de3d6d6162fa95b39b00ffd9f878eae3`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `DllRegisterServer` | `0x8970` | 521 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x8B80` | 119 | UnwindData |  |
| 1 | `CreateInstance` | `0x94D0` | 135 | UnwindData |  |
| 2 | `DllCanUnloadNow` | `0x95C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0x95F0` | 233 | UnwindData |  |
