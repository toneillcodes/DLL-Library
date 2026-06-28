# Binary Specification: Query.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Query.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `492abb10fdd04e4cbcf3f12bbf11f3af8055f1a2a5a3b8ffac083d1337fa2346`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `DllGetClassObject` | `0x1B00` | 208 | UnwindData |  |
| 3 | `BindIFilterFromStorage` | `0x2740` | 204 | UnwindData |  |
| 5 | `DllCanUnloadNow` | `0x46C0` | 55,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `DllRegisterServer` | `0x11DE0` | 184 | UnwindData |  |
| 8 | `DllUnregisterServer` | `0x11EA0` | 37 | UnwindData |  |
| 1 | `LoadBinaryFilter` | `0x11FD0` | 151 | UnwindData |  |
| 2 | `LoadTextFilter` | `0x12070` | 151 | UnwindData |  |
| 4 | `BindIFilterFromStream` | `0x12110` | 104 | UnwindData |  |
| 9 | `LoadIFilter` | `0x12180` | 104 | UnwindData |  |
| 10 | `LoadIFilterEx` | `0x121F0` | 558 | UnwindData |  |
