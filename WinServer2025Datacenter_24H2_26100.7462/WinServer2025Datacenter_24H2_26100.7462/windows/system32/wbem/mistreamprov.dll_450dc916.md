# Binary Specification: mistreamprov.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wbem\mistreamprov.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `450dc916cd6bf3dacaad4be2fc2eaef916ba8faa0ee39ff16689680e1507e64d`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x29A0` | 47 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x29E0` | 119 | UnwindData |  |
| 3 | `DllMain` | `0x2A60` | 82 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x2AC0` | 72 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x2B10` | 65 | UnwindData |  |
| 6 | `GetProviderClassID` | `0x2D30` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `MI_Main` | `0x2DA0` | 186,208 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
