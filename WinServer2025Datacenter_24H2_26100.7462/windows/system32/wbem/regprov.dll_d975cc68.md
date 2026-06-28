# Binary Specification: regprov.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wbem\regprov.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d975cc68c1b9dd952f25e577c75ac9ffc72189e1214c1301ef2c84d739b6c68c`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xDEB0` | 47 | UnwindData |  |
| 2 | `DllGetClassObject` | `0xDEF0` | 119 | UnwindData |  |
| 3 | `DllMain` | `0xDF70` | 82 | UnwindData |  |
| 4 | `DllRegisterServer` | `0xDFD0` | 72 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0xE020` | 65 | UnwindData |  |
| 6 | `GetProviderClassID` | `0xE070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `MI_Main` | `0xE090` | 3,010 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
