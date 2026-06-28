# Binary Specification: AppxProvider.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Dism\AppxProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `266730d9778bd2c0a0adce0367da57d02758229a108324caad6ced82e39e1cd1`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DLLGetDISMProviderCLSID` | `0x4CD0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x4D00` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x4D30` | 302 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x4ED0` | 243 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x4FD0` | 114 | UnwindData |  |
