# Binary Specification: WMVXENCD.DLL

## Binary Metadata
* **Original Path:** `C:\Windows\System32\WMVXENCD.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c5d2e50c39443c8018a57786adcd477c1511a4fce2033695463df7f9f3995c4d`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `DllRegisterServer` | `0x10F60` | 526 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x11180` | 119 | UnwindData |  |
| 1 | `CreateInstance` | `0x11910` | 121 | UnwindData |  |
| 2 | `DllCanUnloadNow` | `0x119F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0x11A20` | 231 | UnwindData |  |
