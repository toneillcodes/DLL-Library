# Binary Specification: pdmproxy100.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\F12\pdmproxy100.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2b5e43eae759501f8ecf4f1cc5e65317dab4c1f4fc55ce9ac89ecdfc6a743bda`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllGetClassObject` | `0x1000` | 46 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x1030` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x1080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x10A0` | 49,088 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
