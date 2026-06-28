# Binary Specification: Query.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Query.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0468bb1d8c19890d924ec52e17bc345b793f54319fa175b5abbcc8911ac1f4b6`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `DllGetClassObject` | `0x1B10` | 208 | UnwindData |  |
| 3 | `BindIFilterFromStorage` | `0x2750` | 204 | UnwindData |  |
| 5 | `DllCanUnloadNow` | `0x46E0` | 58,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `DllRegisterServer` | `0x12C50` | 184 | UnwindData |  |
| 8 | `DllUnregisterServer` | `0x12D10` | 37 | UnwindData |  |
| 1 | `LoadBinaryFilter` | `0x12E40` | 151 | UnwindData |  |
| 2 | `LoadTextFilter` | `0x12EE0` | 151 | UnwindData |  |
| 4 | `BindIFilterFromStream` | `0x12F80` | 104 | UnwindData |  |
| 9 | `LoadIFilter` | `0x12FF0` | 104 | UnwindData |  |
| 10 | `LoadIFilterEx` | `0x13060` | 558 | UnwindData |  |
