# Binary Specification: WMADMOD.DLL

## Binary Metadata
* **Original Path:** `C:\Windows\System32\WMADMOD.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `359a85c7722f235c1c1ae5dab0c3288caf2ea3664d4b2c12f256a8b66bef4020`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `DllRegisterServer` | `0x1CDB0` | 493 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x1CFB0` | 40 | UnwindData |  |
| 1 | `CreateInstance` | `0x38FF0` | 121 | UnwindData |  |
| 2 | `DllCanUnloadNow` | `0x39070` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0x390A0` | 232 | UnwindData |  |
