# Binary Specification: smbwmiv2.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\smbwmiv2.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `afcec661af022d7257f237d58f09287065fb0254a090870eac65b532481d2da2`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x2640` | 47 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x2680` | 113 | UnwindData |  |
| 3 | `DllMain` | `0x2700` | 82 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x2760` | 72 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x27B0` | 65 | UnwindData |  |
| 6 | `GetProviderClassID` | `0x2930` | 704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `MI_Main` | `0x2BF0` | 197,724 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
