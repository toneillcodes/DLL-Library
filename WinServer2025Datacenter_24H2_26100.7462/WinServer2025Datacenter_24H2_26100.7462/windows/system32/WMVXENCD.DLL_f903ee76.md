# Binary Specification: WMVXENCD.DLL

## Binary Metadata
* **Original Path:** `c:\windows\system32\WMVXENCD.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f903ee761e3b5eacb10277a8db04ed4226b7502d28ce5032b2d8c1513b473d68`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `DllRegisterServer` | `0x10F60` | 526 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x11180` | 119 | UnwindData |  |
| 1 | `CreateInstance` | `0x11910` | 121 | UnwindData |  |
| 2 | `DllCanUnloadNow` | `0x119F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0x11A20` | 231 | UnwindData |  |
