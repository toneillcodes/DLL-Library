# Binary Specification: dnsclientpsprovider.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wbem\dnsclientpsprovider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b5a5731eb965b6ef42fa8d6c06f2f909d74fbb41e90dbaf6e8c7b46de72edf33`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `MI_Main` | `0x2C40` | 736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x2F20` | 47 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x2F60` | 113 | UnwindData |  |
| 3 | `DllMain` | `0x2FE0` | 82 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x3040` | 72 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x3090` | 65 | UnwindData |  |
| 6 | `GetProviderClassID` | `0x3210` | 79,820 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
