# Binary Specification: MDMAppProv.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wbem\MDMAppProv.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `cacc08fae3c35835960af3deba572dac09e71a562cbb8728e29faa2adf88aedf`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x2450` | 47 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x2490` | 119 | UnwindData |  |
| 3 | `DllMain` | `0x2510` | 224 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x2600` | 72 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x2650` | 65 | UnwindData |  |
| 6 | `GetProviderClassID` | `0x27E0` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `MI_Main` | `0x2A10` | 84,977 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
