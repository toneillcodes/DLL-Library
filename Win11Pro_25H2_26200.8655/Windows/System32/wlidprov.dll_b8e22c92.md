# Binary Specification: wlidprov.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wlidprov.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b8e22c9258f7ee0f58d7ef06803a32870ae37b1d6b0ca7f9cb6486edb445a076`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllGetClassObject` | `0x14010` | 360 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x14C50` | 65 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x1EB30` | 241,916 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x1EB30` | 241,916 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
