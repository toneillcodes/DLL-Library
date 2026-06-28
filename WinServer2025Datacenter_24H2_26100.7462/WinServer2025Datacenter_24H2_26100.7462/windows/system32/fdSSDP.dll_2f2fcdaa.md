# Binary Specification: fdSSDP.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\fdSSDP.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2f2fcdaacd9b4de02e8b1754f8abf4a4f60e3074e53e23d270e091c70cd7cf66`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xC750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0xC770` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0xC9D0` | 166 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0xCA80` | 127 | UnwindData |  |
| 5 | `FdphostSessionChange` | `0xCB10` | 20 | UnwindData |  |
| 6 | `FdphostSetComContext` | `0xCB30` | 69 | UnwindData |  |
| 7 | `FdphostSetSharedService` | `0xCB80` | 59 | UnwindData |  |
