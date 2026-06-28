# Binary Specification: WinSATAPI.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\WinSATAPI.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `abdfbfc7fd629610add5ad96c5797cbb22223ae89e3b4ecf337bd7716a696186`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xB700` | 53 | UnwindData |  |
| 2 | `DllGetClassObject` | `0xD540` | 274 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x1A780` | 100 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x1A7F0` | 94,732 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
