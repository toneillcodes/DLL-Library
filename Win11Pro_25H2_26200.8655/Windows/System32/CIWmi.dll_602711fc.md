# Binary Specification: CIWmi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\CIWmi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `602711fcbd76a28cc96ab1d5cecbd6ad844896ded598e3462166df9d009fb7e8`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `MI_Main` | `0x1E20` | 2,080 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x2640` | 47 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x2680` | 119 | UnwindData |  |
| 3 | `DllMain` | `0x2700` | 82 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x2760` | 72 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x27B0` | 65 | UnwindData |  |
| 6 | `GetProviderClassID` | `0x29D0` | 5,008 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
