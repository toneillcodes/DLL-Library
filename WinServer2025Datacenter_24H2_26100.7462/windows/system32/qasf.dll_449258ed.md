# Binary Specification: qasf.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\qasf.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `449258ed3385a4843922b1fc1c7dfc35f54b0a7e4b95e2d1404c6bedca0adae4`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x19E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x1A10` | 225 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x1B00` | 513 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x1D10` | 117,476 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
