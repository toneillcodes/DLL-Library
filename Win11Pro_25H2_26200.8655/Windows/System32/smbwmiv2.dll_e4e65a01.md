# Binary Specification: smbwmiv2.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\smbwmiv2.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e4e65a014bbb6045995bc1053fca35e6da3296b526e5f18f1e9b8898a58287d1`
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
| 7 | `MI_Main` | `0x2BF0` | 197,788 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
