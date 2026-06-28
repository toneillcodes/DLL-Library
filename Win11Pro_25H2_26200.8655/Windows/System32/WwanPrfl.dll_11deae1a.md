# Binary Specification: WwanPrfl.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\WwanPrfl.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `11deae1abe12e4ebc2bb19d98999853726b7762c9da532438b4f2e71048c69b2`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `WwanProfileDeinit` | `0xDC30` | 1,504 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `WwanProfileCleanup` | `0xE210` | 217 | UnwindData |  |
| 2 | `WwanProfileCopyProfile` | `0xE2F0` | 574 | UnwindData |  |
| 3 | `WwanProfileDecryptPassword` | `0xE540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `WwanProfileGenerateFile` | `0xE560` | 251 | UnwindData |  |
| 6 | `WwanProfileGenerateXml` | `0xE670` | 427 | UnwindData |  |
| 7 | `WwanProfileGetPath` | `0xE830` | 134 | UnwindData |  |
| 8 | `WwanProfileGetRootPath` | `0xE8C0` | 227 | UnwindData |  |
| 9 | `WwanProfileInit` | `0xE9B0` | 283 | UnwindData |  |
| 10 | `WwanProfileLoadFile` | `0xEAE0` | 237 | UnwindData |  |
| 11 | `WwanProfileLoadXml` | `0xEBE0` | 289 | UnwindData |  |
| 12 | `WwanValidateApn` | `0xED10` | 342 | UnwindData |  |
