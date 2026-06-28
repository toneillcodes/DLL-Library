# Binary Specification: profprov.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\profprov.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `81dd7aedabab7969d2e0ccb95eae0c6551fdb13806944c1ea05f792ec5f51716`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x5FD0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x6000` | 167 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x60E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x60F0` | 54,828 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
