# Binary Specification: IMETIP.DLL

## Binary Metadata
* **Original Path:** `c:\windows\system32\IME\SHARED\IMETIP.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b013820241693076ffb2509d30621c63895f9af5e8dcb4dd8b284f6ffbff97ed`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x24C80` | 73 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x567F0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x56840` | 138 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x568D0` | 24 | UnwindData |  |
