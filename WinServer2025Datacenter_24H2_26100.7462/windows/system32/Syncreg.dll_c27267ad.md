# Binary Specification: Syncreg.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Syncreg.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c27267ad17b1fe1c082cad1b3f806676ae6508dcc53913e714dc8b0a13b2b7f9`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x11C0` | 9,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x3530` | 85 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x4A00` | 106 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x4A70` | 36,528 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
