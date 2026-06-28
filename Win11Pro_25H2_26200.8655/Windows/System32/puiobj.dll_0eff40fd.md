# Binary Specification: puiobj.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\puiobj.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0eff40fd5873ca6db26e35273263ba7208babfc0ae26b0b61640898c9492a75f`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x8220` | 27 | UnwindData |  |
| 3 | `DllRegisterServer` | `0xF100` | 6,880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0xF100` | 6,880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x10BE0` | 158,580 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
