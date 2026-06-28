# Binary Specification: msxml6.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\msxml6.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `bcac2d3d33dd03d94f8c2f4a2daf035587c0d793f0eae15a0e2184747a556124`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllGetActivationFactory` | `0x6FA40` | 134 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x6FE60` | 346 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x8B770` | 124 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x9B590` | 136,496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllUnregisterServer` | `0x9B590` | 136,496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllSetProperty` | `0xBCAC0` | 795,212 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
