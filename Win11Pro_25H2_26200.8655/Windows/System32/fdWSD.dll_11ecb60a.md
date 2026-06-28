# Binary Specification: fdWSD.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\fdWSD.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `11ecb60ad305be2738d5b3b3e821943385ba9bcba00c146b7517f1f9f3d9741d`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x61C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x61E0` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x6440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x6450` | 127 | UnwindData |  |
| 5 | `FdphostSessionChange` | `0x64E0` | 20 | UnwindData |  |
| 6 | `FdphostSetComContext` | `0x6500` | 69 | UnwindData |  |
| 7 | `FdphostSetSharedService` | `0x6550` | 59 | UnwindData |  |
