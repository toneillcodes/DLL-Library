# Binary Specification: netnccim.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wbem\netnccim.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `97aa283c642fc5b1b6d34bb5fa8e809998021d1c0782f88ed30022757cb17422`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x1910` | 47 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x1950` | 119 | UnwindData |  |
| 3 | `DllMain` | `0x19D0` | 82 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x1A30` | 72 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x1A80` | 65 | UnwindData |  |
| 6 | `GetProviderClassID` | `0x1CA0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `MI_Main` | `0x1D10` | 14,128 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
