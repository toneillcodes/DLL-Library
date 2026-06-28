# Binary Specification: thumbcache.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\thumbcache.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0aaaf63febe3877938c5ab75f56045e557c013ccd8d632cd74264b5b907b9058`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllGetClassObject` | `0x182A0` | 403 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0x27170` | 45 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x271D0` | 72 | UnwindData |  |
| 4 | `GetProxyDllInfo` | `0x3A3D0` | 67,308 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
