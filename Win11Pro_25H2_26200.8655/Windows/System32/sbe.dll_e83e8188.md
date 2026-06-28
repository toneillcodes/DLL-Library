# Binary Specification: sbe.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\sbe.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e83e818813aea3f2069be85621fca6a1ee6bd76eba48cb7c363af1b57ff728f2`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllRegisterServer` | `0x3110` | 75 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x3170` | 72 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x31C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x3200` | 120 | UnwindData |  |
