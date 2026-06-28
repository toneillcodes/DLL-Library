# Binary Specification: MsiProvider.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Dism\MsiProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `65b915be2338dfd31c5827ba2c219f199f652edefec6362b56dfae76afa42994`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DLLGetDISMProviderCLSID` | `0x3A60` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x3A90` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x3AC0` | 302 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x3C30` | 243 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x3D30` | 114 | UnwindData |  |
