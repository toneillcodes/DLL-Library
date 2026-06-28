# Binary Specification: AddressParser.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\AddressParser.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9a0ef17293ec6e86ef83cac6a940edf24d3c2309cf57fc23380ca405aafaf2a2`
* **Total Exported Functions:** 18

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DestroyAddressParser` | `0x1BC0` | 33 | UnwindData |  |
| 2 | `GetCity` | `0x1BF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `GetCountryName` | `0x1C10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `GetCountryStringFromIndex` | `0x1C30` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `GetFullAddress` | `0x1C80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `GetNewAddressParser` | `0x1CA0` | 266 | UnwindData |  |
| 7 | `GetPostalCode` | `0x1DB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `GetState` | `0x1DD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `GetStreet` | `0x1DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `ParseAddress` | `0x1E10` | 334 | UnwindData |  |
| 11 | `RebuildAddress` | `0x1F70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `SetCity` | `0x1F80` | 40 | UnwindData |  |
| 13 | `SetCountryName` | `0x1FB0` | 261 | UnwindData |  |
| 14 | `SetFullAddress` | `0x20C0` | 39 | UnwindData |  |
| 15 | `SetPostalCode` | `0x20F0` | 40 | UnwindData |  |
| 16 | `SetState` | `0x2120` | 40 | UnwindData |  |
| 17 | `SetStreet` | `0x2150` | 40 | UnwindData |  |
| 18 | `UpdateDefCountry` | `0x2180` | 29 | UnwindData |  |
