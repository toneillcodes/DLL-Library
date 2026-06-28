# Binary Specification: sud.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\sud.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b4d09f4d558058e889ea806912cf0335f26d326c8e4b8fc261bf0d2716dab0b5`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xE150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0xE170` | 26 | UnwindData |  |
| 3 | `DllRegisterServer` | `0xE190` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0xE1C0` | 50,892 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
