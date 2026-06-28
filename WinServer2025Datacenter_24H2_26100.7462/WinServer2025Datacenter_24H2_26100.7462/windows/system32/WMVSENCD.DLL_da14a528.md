# Binary Specification: WMVSENCD.DLL

## Binary Metadata
* **Original Path:** `c:\windows\system32\WMVSENCD.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `da14a528ce922d0f51a6e118d4824a278bf8e85bf520018028a6f7633e81a90b`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `DllRegisterServer` | `0xB1A0` | 338 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0xB300` | 119 | UnwindData |  |
| 1 | `CreateInstance` | `0xBA90` | 121 | UnwindData |  |
| 2 | `DllCanUnloadNow` | `0xBB70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0xBBA0` | 231 | UnwindData |  |
