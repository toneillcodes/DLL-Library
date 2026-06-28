# Binary Specification: silprovider.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wbem\silprovider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a6acdbf23f8508fbef1210801cc6e1b0e0a8df2c6498dd98fce8ed57cccadb67`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x1DD0` | 47 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x1E10` | 119 | UnwindData |  |
| 3 | `DllMain` | `0x1E90` | 82 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x1EF0` | 72 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x1F40` | 65 | UnwindData |  |
| 6 | `GetProviderClassID` | `0x2160` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `MI_Main` | `0x21E0` | 44,956 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
