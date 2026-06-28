# Binary Specification: CPFilters.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\CPFilters.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `59487ec9f0d7b649ee2d3130ccc7cde526b69aa996f36a52f33019fe1b1485f4`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllRegisterServer` | `0xB9E0` | 629 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0xBC60` | 243 | UnwindData |  |
| 5 | `UpdatePlayready` | `0xC580` | 297 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x13AC0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x13B20` | 224 | UnwindData |  |
