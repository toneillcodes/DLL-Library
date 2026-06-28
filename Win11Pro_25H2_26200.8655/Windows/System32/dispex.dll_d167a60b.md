# Binary Specification: dispex.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\dispex.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d167a60bfc43d2cc1349de20a0229f277f78aebbb727878a0e4dc3fcb371fb1a`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x20B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x20D0` | 70 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x2150` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x2190` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `GetProxyDllInfo` | `0x21D0` | 27,980 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
