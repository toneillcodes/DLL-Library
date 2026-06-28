# Binary Specification: mfps.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\mfps.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2fe40a638a49651433fc122d929be131c432fa964297d0475c90ede10d9148de`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllGetClassObject` | `0x5260` | 73 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x5720` | 45 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x7950` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x7990` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `GetProxyDllInfo` | `0x79D0` | 4,348 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
