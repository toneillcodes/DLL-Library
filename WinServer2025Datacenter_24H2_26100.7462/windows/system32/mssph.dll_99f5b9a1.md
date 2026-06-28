# Binary Specification: mssph.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\mssph.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `99f5b9a1c958255419912c09380d530d3c66198a38ba50b323d250105388872d`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x1BA50` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x1BA80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x1BAA0` | 338 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x1BC00` | 200 | UnwindData |  |
