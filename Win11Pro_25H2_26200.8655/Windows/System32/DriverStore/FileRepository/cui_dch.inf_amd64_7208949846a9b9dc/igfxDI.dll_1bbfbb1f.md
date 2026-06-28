# Binary Specification: igfxDI.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\cui_dch.inf_amd64_7208949846a9b9dc\igfxDI.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1bbfbb1f1dd21824ae1eb50ad12a435eb1a751b615a1af7b84136153ec0a6aaf`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x47D0` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x4800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllInstall` | `0x4820` | 125 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x48A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0x48C0` | 261,182 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
