# Binary Specification: wisp.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wisp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `eb047e7a5f7e968cc5c38bf0cb53597a0d3564f2e4050151c55125e60930b1ff`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x19290` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x1CBB0` | 87,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x321C0` | 6,652 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x321C0` | 6,652 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
